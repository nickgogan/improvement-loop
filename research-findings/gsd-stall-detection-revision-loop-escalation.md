---
name: GSD Stall Detection — Revision Loop Escalation
summary: Monitors issue-count trajectory in plan-phase revision loops and escalates when progress plateaus, combined with hard stop gates and consecutive-call guards.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General / Cross-System
adopted_in: []
sources:
- gsd-v1340-v1342-changelog.md
related_findings:
- file: loop-detection-hash-based-sliding-window.md
  rel: same-problem
- file: graceful-degradation-modes-for-agent-failure.md
  rel: same-problem
- file: token-budget-pre-turn-projection.md
  rel: same-problem
- file: agent-cost-blowup-mitigation-strategies.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: 2026-04-08
pipeline_status: synthesized
consumed_by:
- production-agent-execution.md
---

## What It Is

A stall detection mechanism for plan-phase revision loops that monitors whether issue counts are decreasing across iterations. When the delta between iterations plateaus — meaning the agent is no longer making meaningful progress — the system escalates early rather than waiting for a hard iteration limit. This operates alongside two other safety mechanisms: hard stop gates that enforce absolute iteration ceilings, and a consecutive-call guard in `/gsd-next` that prevents runaway autonomous execution.

## Why It Matters

Revision loops are one of the most common sources of wasted tokens and time in agentic workflows. An agent that keeps iterating without reducing issues is burning resources on a problem it cannot solve at its current level. Trajectory-based detection (watching the delta, not the absolute count) catches this earlier than threshold-based approaches — an agent stuck at 5 issues for 3 iterations is stalled even though 5 is below most absolute thresholds.

## Why People Are Using It

Practitioners running autonomous multi-phase workflows discovered that agents frequently enter unproductive revision loops — rewriting the same section, oscillating between two approaches, or making cosmetic changes that don't resolve the flagged issues. The combination of trajectory monitoring, hard stops, and consecutive-call guards provides defense in depth: the trajectory monitor catches subtle stalls, the hard stop catches everything else, and the call guard prevents runaway chains.

## Potential Improvements

The stall detector could incorporate semantic analysis of changes — not just whether issue count decreased, but whether the agent is making substantively different attempts. A backoff strategy (e.g., switching to a different model or expanding context) could be tried before escalation. The trajectory window size could be configurable per workflow complexity — simple plans stall faster than complex ones.

## Potential Failure Modes

False escalation on legitimately hard problems where progress is slow but real — the detector may interpret small deltas as stalls. The hard stop gate can also mask the underlying issue: if the ceiling is too generous, agents burn significant resources before hitting it. Conversely, aggressive thresholds may escalate prematurely on plans that need a few more iterations to converge. The consecutive-call guard could also interfere with legitimately long autonomous runs if not tuned per workflow.
