---
title: Filesystem-Lock Parallel Agent Coordination
type: extracted-artifact
assigned_form: skill
source_finding: file-based-task-locking-parallel-agents
identification_report: "session-persistence-and-memory.harvest-queue.md::file-based-task-locking-parallel-agents::skill::filesystem-lock-parallel-agent-coordination"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
  - parallel agent fleets where multiple workers self-select tasks from a shared backlog and need exclusive ownership of each task
  - environments with a shared filesystem and a shared git remote (containers mounting a bare repo, multiple worktrees on one host, or any setup where all agents see the same `locks/` directory)
  - workflows where adding a central orchestrator or message bus is undesirable — coordination must emerge from filesystem and git primitives alone
  - audit-sensitive contexts where the act of claiming a task should leave a durable trace (lock file in git history)
  platform_coupling: agnostic
  autonomy: high
  stage: execute
  reversibility: trivial — abandoning the skill leaves only filesystem entries (lock files, claimed tasks); no schema, no service, no migration to undo
  auditability: high — every lock acquisition and release is a filesystem operation, observable via `ls locks/` and via git history when the lock file is committed; stale-lock detection produces explicit log lines
  evidence_strength: Strong
  adoption:
    status: Not Yet Started
    notes: "Anthropic used this pattern to coordinate parallel Claude instances building a 100,000-line Rust C compiler (compiled Linux 6.9, QEMU, FFmpeg with 99% test pass rate)."
contract:
  preconditions: A shared `locks/` directory is reachable by every participating agent (shared filesystem mount, bind-mount, or shared volume). A shared git remote (`/upstream` or equivalent) is reachable by every agent for pull/merge/push. Each agent has a unique identifier (container ID, agent name, or PID) it can write into its lock file as the owner field. A naming convention for tasks exists so two agents asking for "the same task" produce the same lock filename. The filesystem supports atomic file creation (`O_CREAT | O_EXCL` semantics) — POSIX filesystems satisfy this; some network filesystems do not.
  invariants: At any moment a given task name has at most one valid (non-stale) lock file. A lock file always names its owner; an unowned lock file is a bug. The agent that created a lock is the only agent that releases it under normal operation; stale-lock recovery is the only exception and must log explicitly. The pull→work→push sequence happens entirely while the lock is held — no work is pushed without the lock, and no lock is released before the push completes.
  governance: 'Owner: each agent owns the locks it creates. Stale-lock detection is policy-owned by the operator who configures the timeout and the recovery agent. The `locks/` directory itself is shared infrastructure — no single agent owns it. Lock-file naming and the timeout policy must be agreed before fleet startup; changing them mid-flight causes split-brain claims. If the lock files are committed to git (audit-trail variant), the git history of `locks/` becomes the canonical record of who-claimed-what-when and must be retained per the audit policy of the host system.'
  recovery: 'If lock acquisition fails because the file already exists: read the existing lock; if its owner is alive and timestamp is recent, abandon this task and select another. If the existing lock is stale (owner unreachable or timestamp older than the configured timeout), log the stale-lock detection, remove the lock, and retry acquisition once. If the agent crashes mid-work: on restart, scan `locks/` for files owned by self, decide per-file whether to resume or abandon (resume if local workspace state is consistent; abandon and remove the lock if not). If the push step fails after work is complete: do not release the lock; log the failure; surface to the operator. Releasing the lock before the push lands creates a window where another agent can claim a task whose changes are still unmerged.'
tags:
- extracted-artifact
- skill
- parallel-agents
- coordination
- filesystem
---

# Filesystem-Lock Parallel Agent Coordination

**Source:** [[file-based-task-locking-parallel-agents]]
**Form:** skill
**Extraction date:** 2026-04-27

A coordination procedure for parallel agents that need exclusive ownership of tasks without a central orchestrator. Agents claim tasks by atomically creating named lock files in a shared directory, do their work behind the lock, and remove the file on completion. Git provides the conflict-resolution layer; the filesystem provides the mutex.

## Inputs

- **Task name:** A stable, agent-agreed identifier for the unit of work (e.g., `parse_if_statement`, `migrate_table_users`). Two agents that would attempt the same task must produce the same task name.
- **Agent identity:** A unique identifier for the calling agent (container ID, hostname-PID, or assigned agent name) — written into the lock file as the owner.
- **Locks directory path:** Absolute path to the shared `locks/` directory, reachable identically by every agent.
- **Upstream git remote:** Path or URL to the shared bare repo or remote (e.g., `/upstream`).
- **Stale-lock timeout:** Duration after which a lock with no recent heartbeat is considered abandoned (recommended default: 30 minutes; tune to expected task duration × 3).
- **Optional — heartbeat interval:** If long-running tasks update the lock file's mtime periodically, the interval at which the agent touches its own lock (recommended: timeout / 5).

## Procedure

1. **Select a task.** Choose a task name from the available backlog (per the agent's task-selection policy — "next most obvious", priority queue, or dependency-aware ordering). The selection mechanism is out of scope for this skill; the skill begins once a task name has been chosen.

2. **Attempt atomic lock acquisition.** Try to create `locks/<task-name>` exclusively (`O_CREAT | O_EXCL`, or `git ls-files locks/<task-name>` followed by `git add`). Write the agent identity, current timestamp, and (optionally) task metadata into the file as the body. If creation succeeds → proceed to step 4.

3. **Handle pre-existing lock.** If the file already exists:
   - Read it. Extract the owner and timestamp.
   - If timestamp is within the stale-lock timeout → another agent owns this task. Return `task-unavailable`; the caller selects a different task.
   - If timestamp is older than the timeout → run stale-lock recovery:
     - Log a stale-lock-detected event with the prior owner and timestamp.
     - Remove the lock file.
     - Retry step 2 *exactly once*. If that retry also fails (someone else got there first), return `task-unavailable`.

4. **Pull and merge from upstream.** With the lock held, run `git pull --rebase` (or equivalent) against `/upstream` to bring the local workspace to current head. If merge conflicts emerge, resolve per the workflow's conflict policy or surface to the operator while keeping the lock held.

5. **Critical section — execute the task.** Do the work the task names. (Optional) During long-running tasks, periodically update the lock file's mtime or rewrite its timestamp body to refresh the heartbeat.

6. **Push changes to upstream.** Run `git push` (or equivalent) to land the work on `/upstream`. If push fails (rejected, network error): do not release the lock; log; surface to operator. The lock is only released after a successful push.

7. **Release the lock.** Remove `locks/<task-name>`. If the locks directory is itself committed to git, commit the removal as part of the same push (or a follow-up push) so the git history reflects task completion.

8. **Return result.** Emit `task-completed` with the task name, agent identity, lock-acquired timestamp, lock-released timestamp, and the upstream commit SHA(s) produced by the work.

## Outputs

- **Task result:** One of `task-completed`, `task-unavailable` (lock held by live owner), or `task-failed` (work or push failed; lock state surfaced).
- **Lock file lifecycle record:** Acquired-at, released-at (or stale-recovered-at), owner identity. When the locks directory is committed to git, this record is durable in git history.
- **Stale-lock detections:** Log entries for any stale locks recovered, naming the prior owner and the age of the abandoned lock.
- **Upstream commits:** SHA(s) of the commit(s) the agent pushed during the critical section, attributable to the lock-acquisition window.

## Boundary

This skill governs only the mutex-and-merge mechanics around a single task. Out of scope:

- **Task selection / prioritization.** Which task to claim is the caller's policy. The skill begins with a chosen task name.
- **Dependency ordering.** The skill does not enforce that prerequisite tasks complete before dependent tasks start. A separate dependency layer (or human curation of the backlog) is required if order matters.
- **Inter-agent communication.** The skill explicitly assumes none. Any need for agents to coordinate beyond claim-and-release belongs in a different layer.
- **Conflict resolution beyond git.** Merge conflicts during step 4 are deferred to git's resolution model and the workflow's conflict policy.

## Failure Modes

- **Race during atomic creation.** Two agents call step 2 in the same instant. The atomic primitive (`O_CREAT | O_EXCL`) guarantees only one succeeds; the other receives EEXIST and proceeds to step 3. *On filesystems without atomic creation semantics* (some NFS configurations, some object-store mounts), this guarantee fails — duplicate claims become possible. Mitigation: verify the host filesystem supports atomic create-exclusive before deploying; if it does not, layer a second mutex (database row, redis SETNX) in front of the file write.

- **Abandoned lock from crashed agent.** An agent dies mid-task; its lock file remains. Stale-lock detection (step 3) is the recovery mechanism, but the timeout creates a window where the task is blocked. Mitigation: tune the timeout to expected task duration × 3; implement heartbeat updates for long-running tasks so liveness is detectable sooner than the timeout would suggest.

- **Lock released before push completes.** A bug in step 6/7 ordering — releasing the lock before the push lands — opens a window where a second agent claims the task and starts working on a base that has not yet seen the first agent's changes. Mitigation: the skill mandates push-then-release ordering; if push fails, the lock stays held until operator resolution. Treat any code path that releases the lock without a confirmed-successful push as a bug.

- **Stale-lock false positive under heavy load.** Under sustained load, an alive agent may not heartbeat within the timeout window, and another agent steals the lock. Both agents now believe they own the task; pushes will collide at git. Mitigation: keep the timeout safely above worst-case tick rate; rely on git's atomic ref updates as the second line of defense (the second push will be rejected); on rejection, the loser detects the collision and abandons cleanly.

- **Locks directory grows unbounded.** Successful releases remove their files, but stale-lock detections, crashed cleanups, and audit-mode commits can leave residue. Mitigation: periodic sweep of `locks/` for files older than N timeouts, with operator review before deletion. If the directory is git-tracked, a separate retention policy applies to git history.

- **Naming collisions.** Two semantically different tasks accidentally produce the same task name → they appear as one task to the lock layer; one is silently skipped. Mitigation: agree on a structured naming scheme (e.g., `<phase>__<unit>__<variant>`); validate uniqueness at backlog generation time, not at lock acquisition.

## Contract

### Preconditions

A shared `locks/` directory is reachable by every participating agent (shared filesystem mount, bind-mount, or shared volume). A shared git remote (`/upstream` or equivalent) is reachable by every agent for pull/merge/push. Each agent has a unique identifier (container ID, agent name, or PID) it can write into its lock file as the owner field. A naming convention for tasks exists so two agents asking for "the same task" produce the same lock filename. The filesystem supports atomic file creation (`O_CREAT | O_EXCL` semantics) — POSIX filesystems satisfy this; some network filesystems do not.

### Invariants

At any moment a given task name has at most one valid (non-stale) lock file. A lock file always names its owner; an unowned lock file is a bug. The agent that created a lock is the only agent that releases it under normal operation; stale-lock recovery is the only exception and must log explicitly. The pull→work→push sequence happens entirely while the lock is held — no work is pushed without the lock, and no lock is released before the push completes.

### Governance

Owner: each agent owns the locks it creates. Stale-lock detection is policy-owned by the operator who configures the timeout and the recovery agent. The `locks/` directory itself is shared infrastructure — no single agent owns it. Lock-file naming and the timeout policy must be agreed before fleet startup; changing them mid-flight causes split-brain claims. If the lock files are committed to git (audit-trail variant), the git history of `locks/` becomes the canonical record of who-claimed-what-when and must be retained per the audit policy of the host system.

### Recovery

If lock acquisition fails because the file already exists: read the existing lock; if its owner is alive and timestamp is recent, abandon this task and select another. If the existing lock is stale (owner unreachable or timestamp older than the configured timeout), log the stale-lock detection, remove the lock, and retry acquisition once. If the agent crashes mid-work: on restart, scan `locks/` for files owned by self, decide per-file whether to resume or abandon (resume if local workspace state is consistent; abandon and remove the lock if not). If the push step fails after work is complete: do not release the lock; log the failure; surface to the operator. Releasing the lock before the push lands creates a window where another agent can claim a task whose changes are still unmerged.
