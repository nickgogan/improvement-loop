---
name: IsolationResolver — 7-Step Worktree Lifecycle Algorithm
summary: 'Archon implements a concrete 7-step algorithm for worktree resolution: existing env → no codebase skip → workflow reuse → linked issue sharing → PR branch adoption → limit check + auto-cleanup
  → create new. Includes orphan cleanup and branded types (RepoPath, BranchName, WorktreePath) to prevent string-type confusion.'
implementation_notes: null
category: Sandboxing
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: extends
- file: archon-yaml-defined-harness-workflows.md
  rel: extends
- file: all-in-one-sandbox-architecture.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

## What It Is

Archon's `IsolationResolver` implements a concrete 7-step algorithm for deciding which git worktree a workflow should execute in:

1. **Existing environment check** — if the workflow is already in a worktree, reuse it
2. **No-codebase skip** — if the workflow doesn't need a codebase, skip worktree creation entirely
3. **Workflow reuse** — if the same workflow has a worktree from a previous run, reuse it
4. **Linked issue sharing** — if another workflow is working on the same issue, share its worktree
5. **PR branch adoption** — if a PR branch exists for the target, use it
6. **Limit check + auto-cleanup** — if at the worktree limit, clean up orphaned worktrees
7. **Create new** — create a fresh worktree with a deterministic port allocation (3190-4089 range)

If the database write fails after worktree creation, orphan cleanup runs automatically. The system uses branded types (`RepoPath`, `BranchName`, `WorktreePath`) to prevent string-type confusion between different path semantics at the TypeScript level.

## Why It Matters

Worktree isolation is becoming a standard pattern for parallel agent execution (Claude Code's `-w` flag, Archon's workflow engine). But worktree lifecycle management — when to create, reuse, share, or clean up worktrees — is a non-trivial problem. Naive "always create new" wastes resources and hits git limits. Naive "always reuse" causes state contamination between workflows.

Archon's 7-step algorithm is the most concrete worktree lifecycle policy observed in the watched-library registry. It balances isolation (separate worktrees per workflow) with efficiency (reuse when safe) and safety (orphan cleanup, branded types).

## Why People Are Using It

Observed in [Archon](https://github.com/coleam00/archon) v0.3.2 — see [[archon-analysis]] for structural details. Archon runs multiple workflows in parallel via separate git worktrees, each with auto-allocated ports for self-testing. The IsolationResolver is the decision engine that manages this pool.

## Potential Alternatives

Simple "always create new" policy (wastes resources). Docker containers instead of worktrees (heavier but more isolated). User-specified worktree assignment (explicit but burdensome).

## Potential Improvements

Configurable reuse policies (e.g., never reuse for security-sensitive workflows). Worktree health checks before reuse (dirty state, stale branches). Telemetry on worktree creation/reuse rates to tune the algorithm.

## Potential Failure Modes

Issue-sharing step (4) can cause contamination if two workflows modify overlapping files. Port allocation collisions in edge cases. Orphan cleanup deleting a worktree that's still in use by a slow workflow.
