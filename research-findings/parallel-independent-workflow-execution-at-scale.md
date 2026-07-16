---
name: Parallel Independent Workflow Execution at Scale
summary: Running multiple complete, independent workflow instances simultaneously — each handling a separate task (e.g., fixing different GitHub issues) through the full multi-node DAG. Distinct from sub-agent
  parallelism (splitting one task into parallel sub-tasks). Archon demonstrates 6+ simultaneous workflow runs, each progressing through classification, investigation, implementation, validation, and PR
  creation independently.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- archon-open-source-harness-builder.md
related_findings:
- file: archon-yaml-defined-harness-workflows.md
  rel: extends
- file: sub-agent-context-isolation-for-parallel-complex.md
  rel: same-problem
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: same-problem
- file: parallel-claude-code-instances-per-workspace.md
  rel: same-problem
- file: reversible-forks-enable-parallel-sampling.md
  rel: same-problem
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
tags:
- session-95-reextract
---

## What It Is

A workflow-level parallelism pattern where multiple complete workflow instances run simultaneously, each handling an independent task. In Archon's demonstration, a user says "use Archon to fix GitHub issues 5, 7, 8, 9, 10, and 11" — the CLI dispatches six separate workflow runs, each going through the full DAG (classify issue, investigate/plan, implement, validate, create PR). Each workflow instance runs as a background process with its own context window per node.

This is distinct from two other parallelism patterns in the KB: (1) **sub-agent parallelism** (one task split into parallel sub-tasks, e.g., analyzing 34 contract clauses simultaneously), and (2) **parallel workspace instances** (multiple Claude Code sessions in separate worktrees). This pattern is **task-level parallelism** — completely independent workflows running concurrently, each producing an independent output (a separate PR).

The workflows can be monitored through Claude Code (asking for status updates), the web UI dashboard (seeing all active workflows), or automated polling via the `/loop` command.

## Why It Matters

Most agentic coding workflows are sequential: fix one issue, then the next. Task-level parallelism converts a serial queue of N issues into N concurrent workflows, dramatically reducing total wall-clock time. The 6-issue demo produces 6 PRs in the time it would take to do approximately 1.5 sequentially. For teams with large issue backlogs, this is a multiplier on throughput.

The token economics also shift: Archon's per-node model selection means classification nodes use Haiku across all 6 workflows, while only implementation nodes use the expensive model. Four parallel GitHub issue fix workflows used approximately 20% of a 5-hour Claude subscription limit.

## Why People Are Using It

Cole Medin demonstrates fixing 6 GitHub issues simultaneously, producing 8 PRs in total (including 2 from earlier runs). The web UI shows all workflows progressing through their DAG stages concurrently. The pattern is also viable on a VPS for autonomous "dark factory" operation, where a cron job dispatches workflows for new issues on a schedule.

## Potential Improvements

- Rate-limit-aware scheduling that queues workflows when approaching API limits
- Priority ordering when parallel capacity is constrained
- Cross-workflow deduplication (detect if two issues require overlapping code changes)
- Shared research cache across workflows investigating related issues

## Potential Failure Modes

- API rate limit exhaustion when too many workflows hit implementation nodes simultaneously
- Merge conflicts when parallel workflows modify the same files
- Cost amplification — 6 workflows each consuming full DAG token budgets
- Monitoring overload — tracking 6+ workflows simultaneously requires good observability tooling
