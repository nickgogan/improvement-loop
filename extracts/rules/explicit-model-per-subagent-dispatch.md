---
title: "Explicit Model per Subagent Dispatch"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "mandatory-explicit-model-per-dispatch"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "model-resilient-prompt-engineering.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "orchestrator agents or scripts that spawn subagents to handle parts of a task"
    - "multi-agent systems where different subtasks could reasonably use different model tiers"
    - "teams that have been surprised by an unexpectedly large model-usage bill after a multi-agent run"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — a dispatch-template or prompt-layer change; no data migration, effective on the next dispatch"
  auditability: "high — dispatch records with a required model field are mechanically greppable; a missing or inherited-default field is a checkable property, and the tier distribution across a run's dispatches is auditable after the fact"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Observed in production as a hard requirement in another team's subagent dispatch templates, adopted after an incident where an entire batch of parallel reviewers silently ran on the most expensive tier."
contract:
  preconditions: "The system dispatches subagents (or any delegated unit of work) that can run on more than one model or model tier. A dispatch mechanism exists (a template, a tool call, a script) where a model parameter can be specified per dispatch."
  invariants: "Every subagent dispatch specifies a model explicitly. No dispatch is issued with the model field blank, defaulted, or left to silently inherit the calling session's model. Model choice follows a stated tiering heuristic (task complexity maps to tier; total turns, not just per-token price, are weighed for multi-step work; review-type dispatches scale with diff size and risk) rather than being applied uniformly by default."
  governance: "Owner: whoever authors or maintains the dispatch templates, orchestration prompts, or fan-out scripts that spawn subagents. Any new dispatch surface (a skill, a script, an orchestration prompt) must declare a model per dispatch before it is used. Periodic review of dispatch logs checks tier *distribution*, not merely field presence, to catch compliance theater (always naming the same default model)."
  recovery: "If a dispatch is found without an explicit model → treat as a governance violation; add the model parameter and re-run rather than accepting the silent-inherited result retroactively where cost or quality is material. If tier assignments consistently produce worse outcomes than expected (cheap models thrashing through multi-step work) → recalibrate the complexity-to-tier mapping rather than abandoning the explicit-model requirement. If model generations shift and a tier mapping goes stale → assign an owner to refresh it; do not let the mapping silently drift out of date."
tags:
  - "extracted-artifact"
  - "rule"
  - "model-selection"
  - "cost-governance"
  - "subagent-dispatch"
---

# Explicit Model per Subagent Dispatch

**Source:** [[mandatory-explicit-model-per-dispatch]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

An orchestrator, script, or agent is about to dispatch a subagent (or otherwise delegate a unit of work to a separately-invoked model) and a dispatch mechanism exists where the model can be specified per call.

## Action

**Required:** Name a model explicitly on every subagent dispatch. Choose the model tier using a stated heuristic — task complexity maps to tier (boilerplate work down-tier, judgment-heavy review up-tier); for multi-step work, weigh total turns as well as per-token price, since the cheapest models can take several times as many turns and end up costing more overall; scale review-dispatch tier to the size and risk of what is being reviewed; reserve the single most capable-model dispatch for the point where breadth is concentrated by design (e.g., a final whole-branch review).

**Forbidden:** Issuing a subagent dispatch with no model field, or with a model field left to default. Silently inheriting the calling session's model for a dispatch without that being a deliberate tier choice.

## Boundary

Enforced at the moment a dispatch is issued — the dispatch template, tool call, or script invocation that spawns the subagent. This is a call-time check, not a design-time one: it applies to every individual dispatch, not just to a system's overall architecture.

## Enforcement

- **Mechanism:** Dispatch calls carry a required model field. Dispatch logs or transcripts record the model used per call.
- **Check (deterministic):** `(model_field_present_on_every_dispatch == true) AND (model_field_not_silently_defaulted == true)`. Either branch false → violation.
- **Violation response:** Flag the dispatch as non-compliant; identify the correct tier per the complexity/turn-count/risk heuristic and re-issue if cost or quality is material. Periodically audit tier *distribution* across dispatches, not just field presence — a controller can satisfy the letter of the rule by always naming the same (often top-tier) default model.
- **Cannot be fully self-certified:** field presence can be checked mechanically, but tier appropriateness requires either a periodic human audit of the tier distribution or a maintained complexity-to-tier mapping that the dispatcher is checked against.

## Rationale

Model-tier routing (expensive orchestrator, cheap specialists) is an established architecture pattern, but plans for it fail silently at the one place the decision is actually made: the dispatch call itself. When the model parameter is optional, an unspecified dispatch defaults to the session's model — usually the most expensive one available — and nothing surfaces the resulting cost until the bill arrives. Making the model parameter mandatory converts a cost-architecture intention into a checkable property of every dispatch. The turn-count heuristic matters because naive down-tiering on token price alone backfires on multi-step work: cheap models that take three times as many turns can cost more end-to-end than a mid-tier model that finishes faster.

## Failure Modes

- **Cargo-cult down-tiering.** Applying the mandatory-field rule without the turn-count heuristic routes cheap models onto multi-step tasks where they thrash and cost more overall. Mitigation: pair the field requirement with the tiering heuristic, not just the field itself.
- **Stale complexity-to-tier mapping.** Model generations shift the boundary between what counts as "cheap" or "capable" work; a mapping that isn't refreshed drifts out of calibration. Mitigation: assign an owner to the mapping and review it periodically.
- **Compliance theater.** A dispatcher can satisfy the letter of the rule by always naming the same default (often top-tier) model on every dispatch, defeating the cost-governance intent while appearing compliant. Mitigation: audits must check tier distribution across dispatches, not merely that a model field is present.

## Contract

### Preconditions
The system dispatches subagents (or any delegated unit of work) that can run on more than one model or model tier. A dispatch mechanism exists (a template, a tool call, a script) where a model parameter can be specified per dispatch.

### Invariants
Every subagent dispatch specifies a model explicitly. No dispatch is issued with the model field blank, defaulted, or left to silently inherit the calling session's model. Model choice follows a stated tiering heuristic (task complexity maps to tier; total turns, not just per-token price, are weighed for multi-step work; review-type dispatches scale with diff size and risk) rather than being applied uniformly by default.

### Governance
Owner: whoever authors or maintains the dispatch templates, orchestration prompts, or fan-out scripts that spawn subagents. Any new dispatch surface (a skill, a script, an orchestration prompt) must declare a model per dispatch before it is used. Periodic review of dispatch logs checks tier distribution, not merely field presence, to catch compliance theater (always naming the same default model).

### Recovery
If a dispatch is found without an explicit model → treat as a governance violation; add the model parameter and re-run rather than accepting the silent-inherited result retroactively where cost or quality is material. If tier assignments consistently produce worse outcomes than expected (cheap models thrashing through multi-step work) → recalibrate the complexity-to-tier mapping rather than abandoning the explicit-model requirement. If model generations shift and a tier mapping goes stale → assign an owner to refresh it; do not let the mapping silently drift out of date.
