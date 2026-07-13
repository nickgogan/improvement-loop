---
name: "Mandatory Explicit Model per Dispatch with Tiering Heuristics"
summary: |-
  Plain English: every subagent dispatch must name its model explicitly, because an
  omitted model silently inherits the session's most expensive one — one observed
  Superpowers run put all 26 reviewers on the top tier. v6.0.0 hard-requires a model
  in every dispatch template and ships the selection heuristics: a task-complexity →
  model-tier mapping, "turn count beats token price" (the cheapest models take 2-3x
  the turns on multi-step work and end up costing more), per-task review models scaled
  to diff size and risk, and the final whole-branch review pinned to the most capable
  model. Model selection becomes a governed resource decision per dispatch, not an
  inherited default.
implementation_notes: |-
  Candidate input for the engine's model capability registry
  (operations/references/): the registry records what models can do; this finding
  supplies the dispatch-side discipline — no dispatch without an explicit tier choice,
  and the turn-count-vs-token-price heuristic for multi-step work. The silent-
  inheritance failure mode applies directly to the engine's subagent fan-outs.
category: "Model Selection"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "model-tier-routing-expensive-orchestrator-cheap-s.md"
    rel: "extends"
  - file: "agent-cost-blowup-mitigation-strategies.md"
    rel: "same-problem"
  - file: "model-tiers-aliases-cross-provider-indirection.md"
    rel: "same-problem"
  - file: "no-mid-session-model-switching-subagent-handoff.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "model-selection"
  - "cost-governance"
  - "subagent-dispatch"
---

# Mandatory Explicit Model per Dispatch with Tiering Heuristics

## What It Is

A dispatch-time governance rule plus the heuristics to satisfy it:

1. **The rule.** Every subagent dispatch MUST name a model. The failure it targets is
   silent inheritance: an unspecified model defaults to the session's model — usually
   the most expensive — and nothing surfaces the cost until the bill. Observed
   incident: all 26 reviewers in one run on the top tier.
2. **The heuristics.**
   - Task complexity maps to model tier (boilerplate implementation down-tier;
     judgment-heavy review up-tier).
   - "Turn count beats token price": the cheapest models take 2-3x the turns on
     multi-step work, costing more end-to-end than a mid-tier model that finishes in
     fewer turns.
   - Review models scale with diff size and risk.
   - Exactly one dispatch is pinned to the most capable model: the final whole-branch
     review, where breadth is concentrated by design.

## Why It Matters

Model-tier routing is well established as an architecture pattern (expensive
orchestrator, cheap specialists); what this adds is the *enforcement point*. Tiering
plans fail silently at dispatch time — the one place the decision is actually made —
whenever defaults fill the gap. Making the model parameter mandatory converts a cost
architecture from an intention into a checkable property of every dispatch prompt. The
turn-count heuristic is the non-obvious half: naive down-tiering on token price
backfires on multi-step work, so the rule needs the heuristics or it produces cheap
models failing expensively.

## Why People Are Using It

Hard-required by Superpowers' v6.0.0 dispatch templates after the 26-top-tier-reviewers
incident; part of an eval-backed rewrite that cut flow cost ~50%. Source: Observed in
[superpowers](https://github.com/obra/superpowers) v6.1.1 — see
[[superpowers-analysis]] for structural details.

## Potential Alternatives

- **Tier aliases resolved by config** (Archon small/medium/large with precedence
  layers) — moves the choice into governed config; complementary, but still needs a
  no-silent-default rule at dispatch.
- **Cost caps / budget alarms** — catch blowups after the fact; dispatch-time
  explicitness prevents them.
- **One model everywhere** — simple and predictable; leaves the tier savings on the
  table.

## Potential Improvements

- Harness support: dispatch APIs that *reject* model-less subagent calls would turn the
  prose rule structural.
- Measured tier tables per task family (the complexity→tier mapping is currently
  heuristic prose).

## Potential Failure Modes

- **Cargo-cult down-tiering** — the rule without the turn-count heuristic yields cheap
  models thrashing through multi-step tasks at higher total cost.
- **Stale mappings** — model generations shift the complexity→tier boundaries; the
  mapping needs a refresh owner.
- **Compliance theater** — controllers can satisfy the letter by always naming the
  default model; audits should check tier *distribution*, not field presence.
