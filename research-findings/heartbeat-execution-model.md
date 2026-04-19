---
name: Heartbeat Execution Model
summary: Agents run in discrete heartbeat cycles — wake on trigger, check inbox, pick work by priority, checkout task atomically, execute, update status, exit. Not continuous loops; bounded execution windows
  with clear entry/exit conditions.
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: agent-lifecycle-formalization-spectrum.md
  rel: extended-by
- file: agent-state-machine-with-witness-monitoring.md
  rel: same-problem
- file: env-var-context-injection.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

# Heartbeat Execution Model

## What It Is
Paperclip agents run in heartbeat cycles: wake on trigger (timer, @-mention, comment, approval, blocker-resolved, children-completed), check inbox, pick work by priority (in_progress > in_review > todo), checkout task atomically, execute, update status, exit. This is not a continuous loop — each cycle is a discrete, short execution window. Wake reasons are injected via the PAPERCLIP_WAKE_REASON environment variable, providing context without full state reload.

## Why It Matters
Continuous agent loops accumulate context and cost over time. User-invoked skills require human initiation for every action. The heartbeat model is autonomous but bounded — each cycle starts fresh, has clear entry/exit conditions, and doesn't accumulate context across cycles. This bounds both cost and context window consumption per cycle.

## Why People Are Using It
Observed in [Paperclip](https://github.com/paperclipai/paperclip) v2026.403.0 — see [[paperclip-analysis]] for structural details. Different from continuous agent loops (OpenClaw) and user-invoked skills (GSD, Superpowers). Heartbeat is autonomous but bounded — each cycle is short, has clear entry/exit conditions, and doesn't accumulate context across cycles.

## Potential Alternatives
Continuous polling loops (simpler but wasteful). Event-driven architectures with persistent listeners. User-invoked skills (no autonomy). Cron-scheduled batch execution (less responsive).

## Potential Improvements
Adaptive heartbeat frequency based on workload. Priority-aware wake scheduling (urgent triggers processed before timers). Heartbeat health monitoring to detect stuck or failed cycles.

## Potential Failure Modes
Wake reason misclassification causing wrong work prioritization. Too-frequent heartbeats wasting resources on empty inboxes. Too-infrequent heartbeats causing response lag. Loss of cross-cycle context when a task requires multi-cycle reasoning.
