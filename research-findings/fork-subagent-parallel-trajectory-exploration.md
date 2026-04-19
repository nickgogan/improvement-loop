---
name: 'Fork Sub-Agent: Parallel Trajectory Exploration via Context Forking'
summary: 'Claude Code''s codebase contains a feature-flagged fork_subagent that spawns sub-agents with full parent session context (vs current behavior of fresh context). Enables genetic-algorithm-style
  parallel solution exploration: fork 3 approaches, compare, feed winning path back to orchestrator.'
implementation_notes: Feature-flagged (not yet live). Monitor for release. The pattern of forking context for parallel exploration can be approximated today using multiple Claude Code instances with shared
  PROGRESS.md.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-codes-leak-changes-everything.md
related_findings:
- file: cloud-plan-parallel-multitasking-pattern.md
  rel: same-problem
- file: trajectory-engineering-non-linear-session-forking.md
  rel: same-problem
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: same-problem
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
pipeline_status: "raw"
consumed_by: []
---

## What It Is

A feature flag called `fork_subagent` exists in Claude Code's codebase. When enabled, sub-agents would inherit the full session context of their parent (currently sub-agents start with a blank slate). This is functionally equivalent to forking -- the same mechanism that powers `/btw` (which forks context for inline questions, then trims the branch automatically).

The key insight: context-aware sub-agents enable parallel trajectory exploration. Spin up three forks, give each a different approach to the same problem, watch which one succeeds, and feed the winning path back to the orchestrator. Agentic Lab calls this "trajectory engineering" -- defined as "the practice of exploring the output trajectory of the LLM through different context inputs" -- and compares it to a genetic algorithm for agents.

The transcript confirms the mechanism already works in production via the `/btw` command, which forks the current context for inline questions and then automatically trims the branched context when done, allowing the user to resume the main task. Fork sub-agent generalizes this same forking primitive to sub-agents, so the infrastructure is proven rather than theoretical.

This is distinct from the existing "Trajectory Engineering" finding (which covers /re-based manual session forking). Fork sub-agent is an automated, parallelized version built into the infrastructure.

## Why It Matters

Current sub-agents lose all session context, requiring expensive re-reads and re-orientation. Context-aware forks would eliminate this overhead and enable a fundamentally new pattern: speculative parallel execution where multiple approaches compete and the best wins.

## Why People Are Using It

Not yet live -- feature-flagged off. However, the infrastructure is "fully built" per source code analysis. The /btw command already demonstrates the forking mechanism works. Practitioners are anticipating this as a near-term release.

## Potential Improvements

When released, combine with verification agent patterns to have each fork independently verified before selecting the winner. Could enable "tournament-style" development where multiple approaches are evaluated by an impartial judge.

## Potential Failure Modes

Full context duplication multiplies token costs linearly with fork count. Forked contexts may diverge in incompatible ways, making merge-back difficult. Without clear evaluation criteria, selecting the "winning" fork becomes subjective.
