---
name: Harness Simplification as Models Improve
summary: As model capabilities improve, harness complexity should decrease. Sprint decomposition essential with Sonnet 4.5 became unnecessary overhead with Opus 4.6, yielding 38% cost reduction and 36%
  time reduction.
implementation_notes: MetaSystem should periodically audit harness complexity against current model capabilities. Scaffolding that was necessary for earlier models may now be overhead.
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General / Cross-System
adopted_in: []
sources:
- anthropic-harness-design-long-running-apps.md
- anthropic-effective-harnesses-long-running-agents.md
related_findings:
- file: minimal-agent-harness-skeleton-three-primitives.md
  rel: same-problem
- file: agent-harness-distributed-system-mental-model.md
  rel: same-problem
- file: bidirectional-agent-breakage-world-drift-model-improvement.md
  rel: extended-by
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
  - "agent-design-patterns.md"
---

## What It Is

V1 harness used sprint decomposition with 10 sprints and contract negotiation. V2 removed the sprint construct entirely, relying on Opus 4.6's improved capability. The evaluator remains valuable at capability boundaries but becomes unnecessary overhead for simpler work. The shift yielded V1: $200/6hrs to V2: $124.70/3h50m.

## Why It Matters

Harness design is not static architecture — it co-evolves with model capabilities. Over-engineering for current model weaknesses creates technical debt when those weaknesses are resolved. The interesting work is finding novel component combinations suited to emerging capabilities.

## Why People Are Using It

Anthropic documented this evolution explicitly, noting that "context anxiety" in Sonnet 4.5 required sprint decomposition, while Opus 4.5/4.6 largely eliminated this behavior.

## Potential Improvements

Automatic harness complexity selection based on model capability profiling. A/B testing different harness configurations per model tier.

## Potential Failure Modes

Premature simplification — removing scaffolding before the model reliably handles the full scope, leading to quality regressions. Need eval data to justify each simplification.
