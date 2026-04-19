---
name: Budget Governance with Hard Stop
summary: Real resource governance with auto-pause at 100% budget, critical-tasks-only above 80%, per-agent billing codes, and board approval gates for consequential spend. Budget is a server-enforced hard
  constraint — agents cannot overspend.
implementation_notes: null
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: token-budget-pre-turn-projection.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-08'
pipeline_status: raw
consumed_by: []
---

# Budget Governance with Hard Stop

## What It Is
Paperclip implements real resource governance at the dollar level: auto-pause at 100% budget, critical-tasks-only mode above 80%, per-agent budget tracking with billing codes for cross-team work. Budget is a hard constraint enforced by the server — agents cannot overspend because the API stops them. Board approval gates are required for consequential spend decisions. The 80% threshold triggers a graduated response where only critical tasks proceed.

## Why It Matters
Most agent budget systems are advisory — they log spend but don't prevent overruns. Server-enforced hard stops eliminate the gap between policy and enforcement. The graduated response (80% critical-only, 100% full stop) prevents cliff-edge failures where agents are mid-task when budget runs out.

## Why People Are Using It
Observed in [Paperclip](https://github.com/paperclipai/paperclip) v2026.403.0 — see [[paperclip-analysis]] for structural details. Only repo in the KB with economic enforcement. Token budgets (existing KB) are advisory; Paperclip's dollar-budget hard-stop is real resource management. The 80% threshold for critical-only mode is a graduated response pattern not seen elsewhere.

## Potential Alternatives
Token-based budget caps (advisory, no enforcement). Hard turn limits per conversation. Manual monitoring with alert thresholds. Per-session cost caps via API provider settings.

## Potential Improvements
Dynamic budget reallocation between agents based on task priority. Budget forecasting based on historical task costs. Automatic escalation paths when budget is exhausted but critical work remains.

## Potential Failure Modes
Over-aggressive budget limits that prevent legitimate work. The 80% critical-only threshold may be too early or too late depending on workload distribution. Billing code overhead for simple tasks. Board approval gates creating bottlenecks for time-sensitive spend decisions.
