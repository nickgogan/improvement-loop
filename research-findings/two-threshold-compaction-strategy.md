---
name: Two-Threshold Compaction Strategy
summary: 'Dual-threshold context management: at 50% context window, trigger non-blocking background upload/archival; at 70%, force-clear uploaded messages and replace with summary. Two stages prevent both
  premature context loss and context overflow.'
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: token-budget-pre-turn-projection.md
  rel: extends
- file: semantic-memory-decay-compaction.md
  rel: same-problem
- file: ace-delta-updates-over-monolithic-rewrites.md
  rel: same-problem
- file: context-bracket-auto-adaptation.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: context-usage-status-line-visual-budget-tracking.md
  rel: same-problem
- file: dynamic-tool-pool-assembly-transcript-compaction.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
pipeline_status: "classified"
---

## What It Is

A context window management strategy with two distinct thresholds: (1) At 50% context utilization, trigger a non-blocking background upload of current messages to persistent storage (archive). The session continues uninterrupted. (2) At 70% utilization, force-clear the uploaded messages from active context and replace them with a `[Session History Summary]` + `[Archive Index]` (L0 abstracts of archived chunks). The two-stage approach provides a grace period where messages are both in-context and archived.

## Why It Matters

Single-threshold compaction (e.g., Claude Code's built-in compaction) is a cliff: context is either all present or suddenly compressed. The two-threshold approach creates a buffer zone where messages are safely archived before they're removed from context. The non-blocking first threshold means no latency hit during active work. The forced second threshold prevents context overflow.

## Why People Are Using It

Observed in [OpenViking](https://github.com/volcengine/OpenViking) — see [[openviking-analysis]] for structural details. OpenViking implements this in its session manager with configurable thresholds. The background upload at threshold 1 feeds into the memory extraction pipeline, ensuring memories are captured before context is lost.

## Potential Alternatives

- Single-threshold compaction (compress everything at once)
- Sliding window (drop oldest messages continuously)
- Manual compaction (user triggers when needed)

## Potential Improvements

Thresholds could be adaptive based on message importance scoring — high-value turns (containing decisions, code changes) get higher retention priority during the force-clear phase.

## Potential Failure Modes

- Background upload at threshold 1 may fail silently, leading to data loss at threshold 2
- Summary quality at threshold 2 determines how much context is preserved
- Threshold values may need tuning per use case (50/70 is not universal)
