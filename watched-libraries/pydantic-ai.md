---
name: "Pydantic AI"
type: "watched-library"
repo_url: "https://github.com/pydantic/pydantic-ai"
description: |-
  Pydantic's production agent framework (Python, MIT, ~18.5k stars). 2.0 centers agent
  construction on a single "capability" primitive — instructions + tools + lifecycle
  hooks + guardrails + model settings as one shareable, composable unit ("the layer
  above MCP") — and splits its catalog into a lean core of critical capabilities versus
  a named "harness" lane for supported-but-not-critical ones
spectrum_position: "study"
what_we_use: |-
  Nothing adopted — study target. Watching the capability primitive's implementation
  (composition mechanics, progressive disclosure, lifecycle hooks, guardrails) and the
  lean-core-vs-harness package split, both of which independently converged on the
  engine's harness-layer North Star vocabulary and the portable-kernel /
  single-implicit-agent design direction
local_derivations: []
last_evaluated_version: "v2.9.0"
last_evaluated_date: "2026-07-13"
maintainer: "pydantic (Samuel Colvin / Pydantic team)"
status: "active"
tags:
  - "agent-framework"
  - "skills"
  - "orchestration"
  - "agent-design"
  - "tools"
related_findings:
  - "capability-as-agent-composition-primitive.md"
  - "lean-core-vs-harness-two-lane-framework-layering.md"
related_sources:
  - "pydantic-ai-2-0-composing-capabilities.md"
date_added: "2026-07-13"
---

## What It Does

Production agent framework from the Pydantic team (Python, MIT; ~18.5k stars, ~2.4k
forks as of 2026-07-13; latest release v2.9.0, 2026-07-10 — 1.x maintained in parallel
as v1.107.x). Type-safe agent construction with model-agnostic providers, structured
outputs, durable execution, and OpenTelemetry-native observability (Logfire).

The 2.0 release re-centers the framework on one primitive:

- **Capability** — instructions + tools/toolsets (incl. MCP servers) + lifecycle hooks
  + guardrails + model settings packaged as a single shareable unit. An agent collapses
  to `model + [capabilities]`; a capability evolved once upgrades every agent that
  mounts it. Framed as "the layer above MCP."
- **Progressive disclosure** — the agent holds a catalog of brief capability
  descriptions and loads a capability's full instructions only when it decides it needs
  them (the skills pattern migrated into a framework primitive).
- **Lean core vs harness** — first-party capabilities split into a lean core considered
  critical to most agents (thinking, web search, tool search) versus a named "harness"
  lane for supported-but-not-critical capabilities (e.g., code mode).

## What We Use From It

Study target — nothing adopted. Rationale for watching: Pydantic AI 2.0's capability
primitive and its lean-core-vs-harness split independently converged on the engine's
harness-layer North Star vocabulary — a major framework now ships "instructions + tools
+ guards as one composable unit" and names its beyond-the-core lane "harness," the same
concepts the engine's skill-plus-context bundles and portable-kernel /
single-implicit-agent direction rest on. See source
`research-sources/pydantic-ai-2-0-composing-capabilities.md` and findings
`capability-as-agent-composition-primitive.md`,
`lean-core-vs-harness-two-lane-framework-layering.md`. The parts to mine: capability
composition mechanics, the progressive-disclosure implementation, lifecycle-hook and
guardrail seams, and how the core-vs-harness boundary is drawn at the package level.

## Related-Repo Watch Item: Monty

**Monty** (`pydantic/monty`) — Pydantic's minimal, secure Python interpreter written in
Rust (~7.9k stars, MIT), the lightweight sandbox backing the harness lane's code-mode
capability (agent-written code executes inside it). Watched from within this entry as a
related repo — no separate registry entry (Nick's call, wave-3 triage follow-up).
Signals to watch: sandbox escape/security disclosures, whether Monty generalizes beyond
Pydantic AI's code mode, and adoption by other frameworks as a sandboxing layer.

## Spectrum Rationale

Study. The engine is harness-native (Claude Code) and is not adopting a Python agent
framework; the value is architectural comparison. The capability primitive is the
framework-native version of what the engine builds as skills + context contracts, and
the two-lane split is a shipped instance of the kernel-lean/optional-heavy packaging
question the portable-kernel design must answer. Watching implementation details here is
cheaper than deriving them from first principles.

## Change Signals

Watch for:

- Capability API changes — composition mechanics, lifecycle hooks, guardrail semantics
- Progressive-disclosure mechanism changes (catalog format, load triggers)
- Movement of capabilities between the lean core and the harness lane (lane
  promotion/demotion criteria becoming explicit)
- Cross-framework capability portability efforts (capability spec compiling to other
  targets)
- Monty security disclosures or standalone adoption
- 1.x → 2.x migration pressure signals (deprecation timelines for the parallel 1.107.x
  line)

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-07-13 | v2.9.0 | Initial entry, Nick-approved (wave-3 triage follow-up). Repo verified via GitHub API: 18,490 stars, MIT, Python; v2.9.0 released 2026-07-10 with 1.107.x maintained in parallel. Linked to the Cole Medin 2.0-capabilities source and 2 findings. Monty noted as related-repo watch item. |
