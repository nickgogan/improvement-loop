---
name: "Declarative AgentSpec with Serialization-Name Registry and Typed Opt-Out"
summary: |-
  Plain English: agents can be built from YAML/JSON config files — but only if every
  composable part declares a stable serialization name in a registry, and parts that
  hold live code (functions, callables) explicitly opt out rather than pretending to
  round-trip. Pydantic AI v2.9.0's `AgentSpec` constructs agents declaratively; a
  `CAPABILITY_TYPES` registry keys capability classes by `get_serialization_name()`,
  and capabilities that carry callables return `None` — declaring themselves
  non-spec-constructible instead of failing at load time. Agent-as-configuration with
  an honest, typed boundary around what configuration can express.
implementation_notes: null
category: "Intent Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "archon-yaml-defined-harness-workflows.md"
    rel: "same-problem"
  - file: "spec-as-generator-agent-spec-pattern.md"
    rel: "same-problem"
  - file: "capability-as-agent-composition-primitive.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "intent-engineering"
  - "agent-design"
  - "declarative-config"
---

# Declarative AgentSpec with Serialization-Name Registry and Typed Opt-Out

## What It Is

A declarative construction path for agents (`_spec.py`, `agent/spec.py`,
`docs/agent-spec.md`): an `AgentSpec` in YAML/JSON names a model and a capability list,
and the framework assembles the live agent. Two design details carry the pattern:

1. **Serialization-name registry** — capability types register under a stable name
   returned by `get_serialization_name()`; the spec references parts by that name, so
   config files survive class renames and version churn.
2. **Typed opt-out** — capabilities that hold functions or callables return `None` from
   the serialization hook, explicitly declaring themselves non-round-trippable. The
   boundary between "expressible as config" and "requires code" is part of each unit's
   contract, not a runtime surprise.

## Why It Matters

Agent-as-configuration keeps resurfacing (YAML workflows, spec-driven scaffolds) because
config is diffable, storable, and generateable by other agents. The recurring failure is
pretending everything round-trips: specs that silently drop hooks or serialize stale
closures. The contribution here is the honest boundary — a registry for what config
*can* express, an explicit opt-out for what it cannot — which makes declarative agents
safe to generate, validate, and version without a hidden capability cliff.

## Why People Are Using It

Shipped as a first-class construction path in a top-tier production framework, enabling
stored/generated agent definitions alongside code-defined ones. Source: Observed in
[pydantic-ai](https://github.com/pydantic/pydantic-ai) v2.9.0 — see
[[pydantic-ai-analysis]] for structural details.

## Potential Alternatives

- **Code-only agent definition** — full expressiveness, no storable/diffable artifact.
- **Workflow-level YAML** (Archon-style DAGs) — declares orchestration rather than agent
  internals; complementary altitude.
- **Full serialization frameworks** (pickle-style) — round-trip everything, including
  what should not survive a trip.

## Potential Improvements

- Spec-level validation and linting (schema + registry cross-check) as a CI gate for
  stored agent definitions.
- Cross-framework spec portability — a common agent-spec dialect compiling to multiple
  frameworks' registries.

## Potential Failure Modes

- **Registry drift** — renamed serialization names orphan stored specs; the registry
  needs the same compat discipline as any public API.
- **Capability second-class-ness** — pressure to make everything spec-constructible can
  push logic out of callables into stringly-typed config.
- **False confidence** — a spec that loads is not an agent that behaves; declarative
  construction still needs behavioral evals.
