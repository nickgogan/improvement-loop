---
name: "Lean Core vs Harness — Two-Lane Framework Layering"
summary: |-
  Pydantic AI 2.0 splits its capability catalog into two named lanes: a LEAN CORE of
  capabilities considered critical to most agents (thinking, web search, tool search —
  imported directly, tuned by a couple of parameters) and a HARNESS lane for capabilities
  the framework wants to support but does not consider critical to the majority (e.g.,
  code mode — agent-written code executing in Monty, Pydantic's own lightweight
  open-source sandbox). The harness is the wrapper above the lean core: the framework
  stays lightweight by default while still offering batteries when reached for.
  Significant as vocabulary convergence — a major framework now names its
  beyond-the-core layer "harness," the same term the engine uses for the layer that
  wraps and operationalizes an agent.
implementation_notes: |-
  Monty (Pydantic's sandbox) is a watched-library candidate in its own right (Nick's
  call, wave-3 triage) — noted in the source entry; no registry entry created here.
  For the engine, the two-lane split is a datapoint for the portable-kernel design:
  keep the kernel (governance + core skills) lean; ship optional heavier capabilities
  as a separately-adoptable harness lane.
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "pydantic-ai-2-0-composing-capabilities.md"
related_findings:
  - file: "capability-as-agent-composition-primitive.md"
    rel: "same-problem"
  - file: "framework-abstraction-tax-for-agents.md"
    rel: "same-problem"
  - file: "platform-native-harness-over-agent-frameworks.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "agent-design"
  - "orchestration"
  - "tools"
---

# Lean Core vs Harness — Two-Lane Framework Layering

## What It Is

A framework-packaging discipline with an explicit criticality test:

- **Lane 1 — lean core:** capabilities most agents need (thinking, web search, tool
  search / progressive disclosure). First-party, imported directly, minimal
  configuration.
- **Lane 2 — harness:** capabilities that are important for a meaningful minority of
  agents but not the majority — supported, but kept out of the core so the framework
  stays light. Example: code mode (the agent writes and executes code in a sandbox,
  backed by Monty, Pydantic's lightweight open-source sandbox) and third-party
  capability integrations.

The lane assignment rule is demand-share ("critical for a majority?"), not difficulty or
prestige.

## Why It Matters

Two things transfer. First, the **layering rule itself**: frameworks (and knowledge
systems) bloat when every supported feature lands in the default surface; a named
second lane lets the project say yes to breadth without taxing every consumer. This is
the same economics as the engine's core-vs-optional split decisions and answers the
framework-abstraction-tax critique structurally — the tax becomes opt-in. Second, the
**vocabulary convergence**: "harness" as the name for the wrap-around-the-core layer is
now shipping in a major framework, corroborating the engine's own harness-layer language
and making cross-source synthesis on this concept easier.

## Why People Are Using It

Shipped design of Pydantic AI 2.0, presented in its launch material and independently
highlighted by a Tier-2 practitioner as the release's second-most-important idea after
capabilities. Parallel evidence in the KB: platform-native harness arguments and SDK
graduation paths all wrestle with the same core-vs-batteries boundary; this is the first
source that names the boundary inside a single framework.

## Potential Alternatives

- **Monolithic batteries-included** (classic LangChain-style) — everything first-class;
  maximum convenience, maximum abstraction tax.
- **Micro-core + community plugins** — smaller core than lean-core, with the second lane
  fully externalized; cheaper for maintainers, quality variance for consumers.
- **Platform-native harness** (Claude Code as the harness; no framework) — the KB's
  existing counter-position for personal/context-heavy agents.

## Potential Improvements

- Published promotion/demotion criteria between lanes (what usage evidence moves a
  harness capability into core, and vice versa) — the same recurrence-gated promotion
  discipline the engine applies to abstractions.

## Potential Failure Modes

- **Lane creep** — without a hard criticality test, the lean core re-accumulates
  batteries and the split becomes cosmetic.
- **Second-class harness lane** — harness capabilities getting slower maintenance turns
  the layering into deprecation-by-neglect.
- **Terminology collision** — "harness" here is a framework lane; in engine/industry
  usage it can mean the whole operational wrapper around an agent. Cross-source reads
  must disambiguate before treating claims as commensurable.
