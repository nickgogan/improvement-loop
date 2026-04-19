---
name: Token Budget Tracking with Pre-Turn Projection Checks
summary: 'Hard token limits with pre-turn projection that calculates expected cost before each API call and stops execution before the call is made if the budget would be exceeded. Config: max turns, max
  tokens, compaction threshold.'
implementation_notes: MetaSystem doesn't currently track token budgets. This would be valuable for research-loop and other expensive scan operations.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropics-2-5-billion-leak-12-critical-pieces.md
related_findings:
- file: gsd-stall-detection-revision-loop-escalation.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
pipeline_status: extracted
consumed_by:
- rules/token-budget-pre-turn-projection.md
---

# Token Budget Tracking with Pre-Turn Projection Checks

## What It Is
Before each API call, the system projects the token cost. If projected usage exceeds the configured limit, execution stops before the call (not after). Configuration includes max_turns, max_tokens, and compaction_threshold. This prevents runaway costs and enables graceful degradation.

## Why It Matters
Without pre-turn checks, agents can exceed budgets by the margin of a single expensive call. Post-hoc limits waste the final call's cost. Pre-turn projection catches overruns before they happen.

## Why People Are Using It
Anthropic's production Claude Code configuration.

## Potential Alternatives
Post-hoc budget caps (simpler but wasteful). Hard conversation turn limits. Manual monitoring.

## Potential Improvements
Adaptive budget allocation based on task complexity. Budget sharing across multi-agent sessions. Real-time budget visualization.

## Potential Failure Modes
Over-conservative projections that stop agents too early. Projection accuracy depends on estimating response length. Budget allocation doesn't account for retry costs.

## Extraction Note — 2026-04-19
Extracted as **rule**: [[token-budget-pre-turn-projection]] in `extracts/rules/`
