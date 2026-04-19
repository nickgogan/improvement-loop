---
title: "Worktree Isolation for Parallel Agent Sessions"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "worktree-isolation-for-parallel-agent-sessions"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A git repository exists with tasks that can be decomposed into independent units of work. The operator can manage 3-5 concurrent terminal sessions. Tasks do not have tight sequential dependencies that require shared intermediate state."
  invariants: "Each parallel agent session operates in its own git worktree with a dedicated branch. No two sessions modify the same files simultaneously. Context windows are isolated -- one session's context does not bleed into another's. Worktree cleanup occurs when sessions complete."
  governance: "The operator (human) is responsible for coordinating task assignment across sessions, resolving merge conflicts when worktrees converge, and relaying context between sessions when tasks turn out to be dependent. Session count is bounded by human attention capacity, not system limits."
  recovery: "If merge conflicts arise when converging worktrees, the operator resolves them manually with full context from both sessions. If a session fails or produces incorrect output, its worktree branch is discarded without affecting other sessions. Abandoned worktrees with no changes are cleaned up automatically."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Worktree Isolation for Parallel Agent Sessions

**Source:** [[worktree-isolation-for-parallel-agent-sessions]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Sequential agent task execution limits throughput to one task at a time, even when multiple tasks are independent. Running multiple agent sessions against the same working directory causes file conflicts and context contamination -- one session's changes interfere with another's reads and writes. Without filesystem-level isolation, parallel execution is unreliable and produces unpredictable results. Agent teams (multiple agents within a single session) solve this but at 4-7x token cost and with shared context window limitations.

## Forces

- **Throughput vs. isolation:** Running tasks in parallel increases throughput, but sharing a workspace creates file conflicts and context contamination between sessions.
- **Isolation cost vs. coordination cost:** Full filesystem isolation (separate worktrees) eliminates file conflicts but creates merge conflicts when results converge. Shared workspaces avoid merge conflicts but create runtime conflicts.
- **Human attention vs. parallelism:** The operator can manage more parallel sessions than they can merge, creating a bottleneck at convergence rather than execution.
- **Independence assumption vs. task reality:** The pattern works when tasks are genuinely independent, but many tasks have hidden dependencies that only surface at merge time.
- **Token cost vs. throughput:** Agent teams within a single session provide coordination but at 4-7x token cost. Worktree isolation provides parallelism at 1x token cost per session but with no inter-session communication.

## Solution

Use git worktrees to provide filesystem-level isolation for parallel agent sessions, with a human operator coordinating across sessions:

1. **One worktree per task.** Each parallel agent session gets its own git worktree -- a separate copy of the repository with its own branch. This provides complete filesystem isolation: one session's writes cannot affect another session's reads.

2. **Independent context windows.** Each worktree session has its own context window, preventing one task from bloating another's context. A complex task that fills its context does not degrade the quality of a simpler parallel task.

3. **Operator pattern for coordination.** A human operator opens 3-5 terminal sessions, each with an independent agent instance working in its own worktree. The operator assigns tasks, monitors progress, and relays context between sessions when needed. This is the pragmatic middle ground between sequential execution and fully autonomous multi-agent coordination.

4. **Automatic cleanup.** When a worktree session closes with no changes, the worktree is cleaned up automatically. When changes exist, the operator decides whether to merge, discard, or continue the branch.

5. **Bounded parallelism.** Effective parallelism is bounded by human attention, not by system capacity. Practitioners report 3-5 sessions as the practical maximum. Beyond 5, the operator cannot track progress or make timely coordination decisions.

Task selection criteria for worktree parallelism:
- Tasks that modify non-overlapping files are ideal candidates
- Tasks with shared dependencies should be sequenced, not parallelized
- Tasks that require intermediate results from other tasks are not candidates
- Exploratory tasks (multiple approaches to the same problem) benefit from parallel worktrees with a "pick the best result" convergence strategy

## Consequences

**Positive:**
- Linear throughput scaling for independent tasks: 3 worktrees produce roughly 3x the output of sequential execution
- Complete filesystem isolation eliminates the most common failure mode of parallel execution (file conflicts during writes)
- Context isolation prevents one task's complexity from degrading another task's quality
- Lower token cost than agent teams (1x per session vs. 4-7x for coordinated multi-agent)
- Clean git history: each worktree produces its own branch, making changes reviewable independently

**Negative:**
- Merge conflicts when multiple worktrees modify overlapping files -- resolution requires human judgment with full context
- No inter-session communication: if tasks turn out to be dependent, the operator must manually relay context, which is slow and error-prone
- Human attention bottleneck: beyond 5 parallel sessions, the operator cannot track progress effectively
- Setup overhead: creating worktrees, assigning tasks, and managing branches adds coordination cost that must be amortized over task execution time
- Does not help with tasks that are inherently sequential or tightly coupled

## Known Uses

- Claude Code's `-w` flag (`claude -w "fix checkout bug"`) automates worktree creation and cleanup
- Practitioners report managing 3-5 parallel sessions effectively, limited by human attention for coordination
- Anthropic's internal development (building the C compiler) uses this pattern for parallel feature development
- The "operator pattern" (human coordinates independent agent sessions) is documented across multiple agentic coding practitioners
- MetaSystem could apply this pattern for parallel research extraction, skill development, and governance updates across independent systems

## Contract

### Preconditions
A git repository exists with tasks that can be decomposed into independent units of work (non-overlapping file modifications). The operator can manage 3-5 concurrent terminal sessions and make timely coordination decisions. Tasks do not have tight sequential dependencies that require shared intermediate state between sessions.

### Invariants
Each parallel agent session operates in its own git worktree with a dedicated branch -- no shared working directory. No two sessions are assigned tasks that modify the same files simultaneously. Context windows are isolated: one session's loaded context does not appear in another session's context. Worktree cleanup occurs when sessions complete, either automatically (no changes) or via operator decision (changes exist).

### Governance
The operator (human) is responsible for: decomposing work into parallelizable units, assigning tasks to sessions, monitoring progress across sessions, resolving merge conflicts at convergence, and relaying context between sessions when hidden dependencies surface. Session count is bounded by human attention capacity (3-5), not by system limits. Task independence is validated before parallelization -- overlapping file modifications are sequenced, not parallelized.

### Recovery
If merge conflicts arise when converging worktree branches: the operator resolves them manually with full context from both sessions' git diffs and conversation logs. If a session fails or produces incorrect output: its worktree branch is discarded or reset without affecting other sessions' worktrees. If tasks are discovered to be dependent mid-execution: pause the dependent session, complete the prerequisite session first, merge its results, then resume the dependent session in an updated worktree. Abandoned worktrees with no uncommitted changes are cleaned up automatically; worktrees with changes are flagged for operator review.
