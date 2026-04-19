---
name: File-Based Task Locking for Parallel Agents
summary: Parallel agents claim exclusive tasks by writing lock files to a shared directory (e.g., current_tasks/parse_if_statement.txt). No inter-agent communication or orchestration needed -- agents self-select
  tasks, acquire locks, pull/merge/work/push, and release locks. Git handles conflicts.
implementation_notes: Applicable to MetaSystem parallel skill execution. Could use a locks/ directory in the workspace for concurrent agent coordination.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- anthropic-building-c-compiler.md
related_findings:
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: same-problem
- file: parallel-claude-code-instances-per-workspace.md
  rel: extends
- file: atomic-checkout-with-409-exclusion.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- session-persistence-and-memory.md
---

## What It Is

Multiple Docker containers share a bare git repo mounted at `/upstream`. Each agent clones to its own `/workspace`. To claim a task, an agent writes a text file to `current_tasks/` (e.g., `current_tasks/parse_if_statement.txt`). The workflow per agent: (1) acquire lock by creating the task file, (2) pull and merge from upstream, (3) work on the task, (4) push changes to upstream, (5) remove the lock file. Agents self-select the "next most obvious" task or maintain docs of failures/remaining work. There is no inter-agent communication, no orchestrator, no central coordinator -- just the filesystem and git. Git history shows lock-taking as a natural audit trail.

## Why It Matters

This is the simplest viable coordination mechanism for parallel agents. No orchestrator means no single point of failure. No inter-agent communication means no protocol complexity. The filesystem lock is universally accessible, trivially debuggable (list the directory), and creates a natural audit trail in git. The pattern scales linearly -- add more containers, each with its own agent.

## Why People Are Using It

Anthropic used this pattern to build a 100,000-line Rust C compiler with a team of parallel Claude instances. The approach compiled Linux 6.9 for x86/ARM/RISC-V, QEMU, FFmpeg, and other major projects with a 99% test pass rate.

## Potential Improvements

Priority-based lock acquisition (critical tasks claimed first). Lock timeout to prevent abandoned locks from blocking tasks. Lock contention metrics to detect hot tasks.

## Potential Failure Modes

Race conditions between agents claiming the same task simultaneously (mitigated by atomic file creation). Abandoned locks from crashed agents blocking tasks indefinitely. No dependency ordering -- agents may work on tasks that depend on uncompleted prerequisites.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[file-based-task-locking-parallel-agents.md]] in `extracts/patterns/`
