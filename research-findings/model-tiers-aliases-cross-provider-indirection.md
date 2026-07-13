---
name: "Model Tiers and Aliases as a Cross-Provider Indirection Layer with Per-User Precedence"
summary: |-
  Plain English: workflows should say "use a small/cheap model here" — never "use
  claude-haiku-x.y" — so model churn never touches workflow definitions. Archon v0.5.0
  gives workflows symbolic `small`/`medium`/`large` tiers plus user-definable `@alias`
  refs; each resolves to a concrete provider + model + effort at run time through a
  layered precedence chain: global config < repo config < per-user preferences
  (highest). Reserved tier names are protected from being shadowed by aliases. Default
  workflows exercise the indirection for cost routing (`model: small` on classification
  nodes). Decouples workflow authoring from provider/model churn and makes model
  choice a per-user setting rather than a hardcoded constant.
implementation_notes: null
category: "Model Selection"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "model-tier-routing-expensive-orchestrator-cheap-s.md"
    rel: "extends"
  - file: "effort-level-tuning-as-first-order-cost-lever.md"
    rel: "same-problem"
  - file: "tiered-capability-registry-engine-behavior-branching.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "model-selection"
  - "cost-routing"
  - "multi-provider"
  - "archon"
---

# Model Tiers and Aliases as a Cross-Provider Indirection Layer with Per-User Precedence

## What It Is

Archon v0.5.0 inserts a symbolic layer between workflow definitions and concrete models:

- **Tiers**: `small` / `medium` / `large` — workflow nodes declare a tier (`model: small`), and the engine resolves it to a concrete provider + model + effort setting at run time.
- **Aliases**: `@alias` references let users name their own resolution bundles; reserved tier names are protected so an alias cannot shadow `small`/`medium`/`large`.
- **Layered precedence**: resolution consults global config < repo config < **per-user AI preferences** (`user_ai_prefs` table, the highest-precedence config layer) — so two users running the same workflow can get different concrete models without workflow changes.

Shipped default workflows use the indirection for intra-workflow cost routing — e.g. `archon-ralph-dag` routes its input-classification node to `model: small` while implementation iterations run on larger tiers.

## Why It Matters

Model identifiers churn constantly; workflows that hardcode them rot on every provider release. Tier indirection makes model choice a *deployment/user concern* instead of an *authoring concern* — the same decoupling move as environment variables for endpoints. The per-user precedence layer is the novel part: in a multi-user engine, model/cost tradeoffs are personal (one user pays for `large` everywhere, another caps at `small`), and putting user prefs at the top of the resolution chain expresses that without forking workflows. The KB already holds the *routing practice* (expensive orchestrator, cheap subagents); this finding is the *naming abstraction* that makes such routing declarable and portable across providers.

## Why People Are Using It

Observed in [Archon](https://github.com/coleam00/archon) v0.5.0 — see [[archon-analysis]] for structural details. The tier/alias layer landed alongside the multi-provider registry (Pi's ~20 backends, OpenCode, Copilot) — once workflows can run on heterogeneous providers, literal model names in YAML become untenable, and the Pi model catalog ships cost/reasoning hints that inform tier mapping.

## Potential Alternatives

Hardcoded model literals per node (simple, rots fast). Environment-variable substitution (decouples, but no semantics — no notion of "small"). Automatic model selection by task classification (removes the author's declaration entirely; harder to predict cost).

## Potential Improvements

Tier definitions annotated with cost/latency budgets so the resolver can enforce ceilings. Telemetry feedback: track per-tier success rates and suggest tier promotions/demotions per node.

## Potential Failure Modes

Three-way precedence (global/repo/user) makes "which model actually ran?" a debugging question — observability must surface the resolved concrete model per node. Tier semantics drift across providers (one provider's `medium` outperforms another's `large`), silently changing workflow behavior when users switch providers.
