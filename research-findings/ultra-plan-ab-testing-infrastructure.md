---
name: Ultra Plan A/B Testing Infrastructure for Planning Modes
summary: 'Anthropic uses server-controlled remote config to A/B/C test Ultra Plan variants (simple, visual, deep) by measuring acceptance rates. The same infrastructure can route to unreleased models. Users
  cannot choose their variant. Practitioner recommendation: extract the deep plan prompt as a deterministic skill.'
implementation_notes: The A/B testing pattern itself is interesting -- measuring plan acceptance rates as a proxy for plan quality. Could inform how MetaSystem evaluates its own planning skills.
category: Evaluation
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-just-dropped-ultra-plan.md
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
related_findings:
- file: claude-code-ultra-plan-three-mode-planning.md
  rel: same-problem
---

## What It Is

Ray Amjad's analysis of Claude Code's Ultra Plan reveals that Anthropic operates an A/B/C testing infrastructure behind it. Three planning mode variants (simple, visual, deep) are assigned to users via server-controlled remote config -- the user never picks which variant they receive. Anthropic measures plan acceptance rates per variant to determine which planning prompt performs best.

The infrastructure is general-purpose: it can also route to unreleased models for plan generation, measuring whether a new model produces more-accepted plans. This means Ultra Plan is simultaneously a user feature AND an evaluation pipeline.

Key finding from practitioner testing (10 Ultra Plans vs 10 local plans on matched prompts): Ultra Plan is consistently 2x faster. The deep plan variant (multi-agent with critique) produces better results for dependency-upgrade-style tasks (caught more issues in tRPC v10-to-v11 migration). Simple and visual variants showed no meaningful improvement over local planning.

## Why It Matters

Using plan acceptance as a quality metric is a practical, low-overhead evaluation approach. It measures real user satisfaction rather than synthetic benchmarks. The dual-use infrastructure (feature + evaluation pipeline) is an efficient pattern for any team shipping AI features.

## Why People Are Using It

Users experience this passively -- they cannot opt out of A/B assignment. The practitioner response has been to extract the deep plan prompt and use it as a deterministic skill, bypassing the randomization entirely.

## Potential Improvements

Apply the acceptance-rate-as-quality-metric pattern to MetaSystem's own planning skills. Track how often generated plans are approved vs. revised as a proxy for planning quality.

## Potential Failure Modes

A/B testing without user awareness erodes trust when discovered. Acceptance rate may not correlate with plan quality -- users may accept mediocre plans due to time pressure. The infrastructure creates an implicit dependency on Anthropic's servers for what could be a local operation.
