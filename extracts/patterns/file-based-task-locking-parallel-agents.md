---
title: "File-Based Task Locking for Parallel Agents"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "file-based-task-locking-parallel-agents"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Multiple agents operate on a shared codebase or task set; a shared filesystem (or git repository) is accessible to all agents; tasks are decomposable into independent, claimable units of work."
  invariants: "Exactly one agent owns each task at any time. Lock acquisition is atomic. Lock release happens after work is committed, not before."
  governance: "Lock directory structure and naming conventions are documented. Lock timeout policy is defined and enforced. Abandoned lock cleanup is automated or scheduled."
  recovery: "When an agent crashes mid-task: detect abandoned locks via timeout, release them, and make the task available for re-claim. When merge conflicts occur on push: the conflicting agent pulls, resolves, and retries — the lock is not released until resolution succeeds."
tags:
  - "extracted-artifact"
  - "pattern"
---

# File-Based Task Locking for Parallel Agents

**Source:** [[file-based-task-locking-parallel-agents]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

When multiple agents work in parallel on a shared codebase or task set, they need a coordination mechanism to prevent duplicate work, merge conflicts, and race conditions. Traditional solutions (message queues, orchestrator-based task assignment, inter-agent communication protocols) introduce complexity, single points of failure, and protocol overhead that scale poorly and are difficult to debug.

## Forces

- **Coordination overhead vs. independence.** Agents need to avoid stepping on each other, but heavy coordination protocols reduce the parallelism benefit.
- **Simplicity vs. robustness.** Simple mechanisms (filesystem locks) are easy to implement and debug but lack the guarantees of distributed coordination systems (queues, consensus protocols).
- **Scalability vs. contention.** As agent count grows, lock contention increases. The coordination mechanism must scale linearly, not quadratically.
- **Crash resilience.** Any agent can crash mid-task. The coordination mechanism must handle abandoned work without blocking other agents indefinitely.
- **Auditability.** The coordination mechanism should produce a natural record of who did what and when, without requiring separate logging infrastructure.

## Solution

Use the **filesystem as the coordination layer**. Each agent claims exclusive ownership of a task by writing a lock file to a shared directory. No orchestrator, no inter-agent communication, no message queue.

**Workflow per agent:**

1. **Select task.** Agent identifies the next unclaimed task (e.g., scans a task list, picks the "next most obvious" item).
2. **Acquire lock.** Create a file in `current_tasks/` (or equivalent lock directory) named after the task (e.g., `current_tasks/parse_if_statement.txt`). File creation must be atomic (use exclusive-create flags to prevent races).
3. **Pull and merge.** Pull latest from the shared upstream repository and merge.
4. **Work.** Complete the task in the agent's isolated workspace.
5. **Push.** Commit and push changes to the shared upstream.
6. **Release lock.** Delete the lock file.

**Structural requirements:**

- Each agent operates in its own workspace (clone, worktree, or container) — never directly in the shared repo.
- The shared upstream is a bare git repository or equivalent shared state.
- Lock files can contain metadata (agent ID, timestamp, task description) for debugging and timeout enforcement.
- Git history naturally records lock acquisition and release as part of the commit trail.

## Consequences

**Positive:**
- Simplest viable coordination mechanism — no orchestrator, no protocol complexity, no single point of failure.
- Universally accessible and trivially debuggable: list the lock directory to see current work assignments.
- Natural audit trail through git history.
- Scales linearly — add more agents, each with its own workspace.
- No inter-agent communication means no message format negotiations, no version mismatches, no protocol bugs.

**Negative:**
- Race conditions are possible if lock acquisition is not truly atomic (two agents creating the same file simultaneously).
- Abandoned locks from crashed agents block tasks indefinitely unless a timeout/cleanup mechanism is implemented.
- No dependency ordering — agents may work on tasks whose prerequisites are not yet complete.
- No priority system — agents self-select tasks without awareness of critical-path ordering.
- Merge conflicts are possible when agents push changes to overlapping files; resolution requires manual or automated conflict handling.

## Known Uses

- **Anthropic C compiler project:** Used this pattern to coordinate parallel Claude instances building a 100,000-line Rust C compiler. Multiple Docker containers shared a bare git repo at `/upstream`, each cloning to its own `/workspace`. The system compiled Linux 6.9 for x86/ARM/RISC-V, QEMU, FFmpeg, and other major projects with a 99% test pass rate.

## Contract

### Preconditions
- Multiple agents operate on a shared codebase or task set.
- A shared filesystem or git repository is accessible to all agents.
- Tasks are decomposable into independent, claimable units of work (not tightly interdependent subtasks requiring sequential execution).
- Each agent has its own isolated workspace (clone, worktree, or container).

### Invariants
- Exactly one agent owns each task at any given time — no shared ownership, no optimistic concurrency.
- Lock acquisition is atomic — two agents cannot simultaneously claim the same task.
- Lock release happens only after work is committed and pushed, not before. The lock protects the full lifecycle: claim, work, commit, push, release.
- The lock directory is the single source of truth for current task assignments.

### Governance
- Lock directory structure and naming conventions are documented and consistent across all agents.
- Lock timeout policy is defined (e.g., locks older than N minutes are considered abandoned) and enforced via automated cleanup or monitoring.
- Task decomposition granularity is reviewed periodically — tasks that are too large create long lock holds; tasks that are too small create excessive lock overhead.

### Recovery
- When an agent crashes mid-task: detect the abandoned lock via timeout, release it, and make the task available for re-claim by another agent.
- When a merge conflict occurs on push: the conflicting agent pulls, resolves the conflict, and retries the push. The lock is not released until resolution succeeds or the agent explicitly abandons the task.
- When a task is re-claimed after abandonment: the new agent starts from the latest upstream state, not from the crashed agent's partial work (which was never pushed).
