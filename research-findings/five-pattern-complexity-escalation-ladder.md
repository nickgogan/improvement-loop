---
name: Five-Pattern Complexity Escalation Ladder
summary: A decision framework for choosing among five agentic patterns — sequential flow, operator (parallel terminals), split-and-merge (sub-agents), agent teams (shared communication), and headless (autonomous)
  — based on task complexity, inter-task dependency, and human attention budget. Each pattern trades off isolation, coordination, cost, and autonomy. Escalate only when the current pattern's ceiling is
  hit.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- five-agentic-patterns-claude-code.md
related_findings:
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: same-problem
- file: agent-teams-shared-communication-channel.md
  rel: same-problem
- file: sub-agent-context-isolation-for-parallel-complex.md
  rel: same-problem
- file: orchestrator-headless-dispatch-context-isolation.md
  rel: same-problem
- file: claude-p-headless-mode-as-openclaw-replacement.md
  rel: same-problem
- file: end-to-end-sequential-bug-fix-pipeline.md
  rel: same-problem
- file: context-degradation-40-50-percent-threshold.md
  rel: enables
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
tags:
- session-95-reextract
---

## What It Is

A five-level escalation ladder for selecting agentic orchestration patterns, ordered by increasing complexity, cost, and autonomy:

1. **Sequential Flow** — Single terminal, single conversation. Tasks build on each other in shared context. Ceiling: context window fills up (context rot). Escalation trigger: accumulated context degrades quality.
2. **Operator** — Human opens multiple terminals, each with its own Claude instance (optionally via `claude -w` worktrees). Tasks must be independent. Ceiling: human attention (4-5 terminals max before coordination overhead dominates). Escalation trigger: too many parallel streams to track manually.
3. **Split-and-Merge** — Within a single session, Claude fans out work to sub-agents (up to 10 concurrent, queued beyond that). Hub-and-spoke: sub-agents report to the main agent only, never to each other. Ceiling: sub-agents cannot coordinate with each other. Escalation trigger: tasks have real-time interdependencies.
4. **Agent Teams** — Sub-agents share a communication channel (shared task list) and can coordinate directly. 4-7x token cost vs single session. Experimental (shipped with Opus 4.6). Ceiling: token cost and complexity. Escalation trigger: output needs human-free autonomous execution.
5. **Headless** — `claude -p` with no human in the loop. Best for batch processing and easy-to-verify output. Composable with cron scheduling for recurring workflows.

The key decision criteria at each escalation boundary: task dependency (independent vs interdependent), context budget (single window vs multiple), human attention budget (how many streams can you track), coordination need (hub-and-spoke vs peer-to-peer), and trust level (can you verify the output without watching each step).

## Why It Matters

Most practitioners default to either sequential flow (too conservative) or jump straight to agent teams (too expensive). The ladder provides a structured decision framework: start at the simplest level that fits the task, and escalate only when you hit the current level's ceiling. This prevents both under-utilization (staying sequential when parallel would save time) and over-engineering (using agent teams when split-and-merge would suffice at 1/5 the token cost).

## Why People Are Using It

The video frames the five patterns as a spectrum, not a menu. The sequential-to-headless progression maps to increasing task complexity and decreasing human involvement. Practitioners who understand the full spectrum can match their orchestration pattern to the actual demands of the task rather than defaulting to what they know.

## Potential Improvements

- Formalize the escalation triggers as measurable criteria (e.g., context utilization > 40%, task count > 4, dependency graph has cycles)
- Add a cost estimator: given task shape, predict token usage across patterns and recommend the cheapest viable option
- Build a decision tree or flowchart for quick pattern selection

## Potential Failure Modes

- Premature escalation wastes tokens — agent teams at 4-7x cost for tasks that split-and-merge could handle
- Under-escalation wastes human attention — staying in operator mode when sub-agents could self-coordinate
- The ladder assumes clean boundaries between patterns, but real tasks often straddle levels (e.g., mostly independent tasks with one dependency)
- Token cost estimates for agent teams may vary widely depending on communication intensity
