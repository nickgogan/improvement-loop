---
name: Three Enforcement Pipeline Architectures — Middleware vs Hooks vs Rules
summary: 'Three governance enforcement architectures at increasing sophistication: static rules (GSD, BMAD), event-driven hooks (Archon, Beads), request-pipeline middleware (DeerFlow). Each trades simplicity
  for power.'
implementation_notes: null
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: null
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources: []
related_findings:
- file: middleware-as-enforcement-architecture.md
  rel: extends
- file: hook-based-enforcement-for-agent-outputs.md
  rel: same-problem
- file: structural-vs-psychological-vs-economic-governance.md
  rel: extends
- file: agent-identity-governance-enforcement-layer.md
  rel: same-problem
- file: distributed-boundary-guides.md
  rel: extends
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
---

## What It Is

A cross-repo comparison finding: three architectures for enforcing governance at runtime, forming a sophistication spectrum:

1. **Rule-based allowlists** (GSD, BMAD, n8n) — Static rules (tool allowlists, validators, lint configs) evaluated at invocation time. No interception of ongoing execution. Simplest to reason about. Applied once, not per-interaction.

2. **Event-driven hooks** (Archon, Beads, Superpowers) — PostToolUse/SessionStart/PreCompact hooks fire on specific events. Can validate, modify, or block. No guaranteed ordering between hooks. Applied per-event, not per-interaction.

3. **Request-pipeline middleware** (DeerFlow) — Composable, ordered layers intercept every tool call and model response. 12 layers with specific hook points (before_model, after_model, wrap_tool_call, after_agent). Ordering matters. Most powerful but most complex.

## Why It Matters

Extends the existing governance philosophies finding (structural/psychological/economic/specification) with an orthogonal dimension: not *what* is enforced, but *how the enforcement pipeline is architectured*. MetaSystem currently uses event-driven hooks (Claude Code hooks). Understanding the full spectrum helps evaluate whether to invest in middleware-style enforcement as agent complexity grows.

## Why People Are Using It

Cross-repo observation across 14 analyzed repos — see [[cross-repo-comparison]] for structural details. Rules observed in GSD, BMAD, n8n. Hooks in Archon, Beads, Superpowers. Middleware in DeerFlow.

## Potential Alternatives

- No runtime enforcement (trust prompts — fragile)
- Declarative policy engines (OPA-style — not yet observed in agentic repos)

## Potential Improvements

Layered approach: rules for static constraints, hooks for event-specific validation, middleware for cross-cutting concerns. MetaSystem could evolve from hooks-only to a layered model as needed.

## Potential Failure Modes

- Rules are too static for dynamic situations
- Hooks have no ordering guarantees — interaction effects between hooks are hard to predict
- Middleware ordering is powerful but creates subtle bugs when layers interact
