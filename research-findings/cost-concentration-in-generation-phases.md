---
name: Cost Concentration in Generation vs Evaluation Phases
summary: In multi-agent harnesses, token cost is overwhelmingly concentrated in generation (57% in build round 1) while planning (0.4%) and QA (8% total) are negligible, making GAN-style architectures economically
  viable.
implementation_notes: null
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
adopted_in: []
sources:
- anthropic-harness-design-long-running-apps.md
related_findings: []
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: raw
consumed_by: []
---

## What It Is

Detailed cost breakdowns show planning ($0.46/0.4%) and QA ($10.39/8% for 3 rounds) are negligible compared to build rounds ($71.08 first round, 57% of total). The generator consumes the vast majority of tokens reading/writing code and iterating. Full harness (Planner+Generator+Evaluator): $124.70/3h50m vs solo run: $9/20min (non-functional output).

## Why It Matters

This inverts the assumption that adding evaluator agents doubles cost. Evaluation is cheap relative to generation. It also suggests optimizing generator context management has the highest ROI for cost reduction. The 20x cost increase from solo to full harness is justified by the quality gap (non-functional to fully playable).

## Why People Are Using It

Anthropic published detailed cost breakdowns across multiple project types to validate the economic viability of multi-agent harnesses.

## Potential Improvements

Generator context optimization (reducing unnecessary file reads) could dramatically reduce the dominant cost center. Caching intermediate results across build rounds.

## Potential Failure Modes

Cost concentration means generator failures are expensive. A poorly-scoped sprint contract can lead to expensive wasted build rounds.
