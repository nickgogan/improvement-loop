---
name: "Capability as the Single Agent-Composition Primitive"
summary: |-
  Pydantic AI 2.0 centers agent construction on one primitive: the "capability" —
  instructions + tools + lifecycle hooks + guardrails + model settings bundled into a
  single shareable, composable unit that can reach every layer of the agent through one
  concept. An agent is defined as a model plus a set of capabilities; capabilities are
  reused across agents (two agents mount the same knowledge-base capability; improving
  it upgrades both simultaneously). Framed as "the layer above MCP": MCP packages tools
  only, a capability also carries the instructions, settings, hooks, and guardrails
  around them. Capabilities support progressive disclosure — the agent holds a catalog
  of brief descriptions and loads a capability's full instructions only when it decides
  it needs them — so dozens or hundreds of capabilities can be mounted without
  overwhelming context. Nothing inside is new (skills, hooks, guardrails, MCP already
  existed); the novelty is unifying them as one composition unit in a framework.
implementation_notes: |-
  Industry-convergence datapoint for the engine's portable-kernel / single-implicit-agent
  direction: the capability is what the engine's skill-plus-context bundles would look
  like as a framework primitive. pydantic/pydantic-ai is flagged as a watched-library
  candidate (Nick's call, wave-3 triage follow-up 3) — dependency-grade tracking would
  route through that registry, not through this finding.
  Priority upgraded P3 → P2 (reassessment 2026-07-13, Nick-accepted): C5 — hub of the
  sweep's largest new cluster (9 typed links, 7 extends/enables, five pydantic-ai
  children) + C4 cross-framework convergence on capability/skill-as-unit; North Star
  (portable-kernel / single-implicit-agent) strategic premium.
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "pydantic-ai-2-0-composing-capabilities.md"
related_findings:
  - file: "everything-as-skill-architecture.md"
    rel: "same-problem"
  - file: "skills-portability-across-sdk-and-framework-boundaries.md"
    rel: "extends"
  - file: "skill-as-directory-progressive-disclosure-three-levels.md"
    rel: "extends"
  - file: "lean-core-vs-harness-two-lane-framework-layering.md"
    rel: "same-problem"
  - file: "cache-stable-progressive-disclosure-catalog.md"
    rel: "extended-by"
  - file: "capability-composition-declared-ordering-constraints.md"
    rel: "extended-by"
  - file: "declarative-agent-spec-with-serialization-registry.md"
    rel: "extended-by"
  - file: "disclosure-granularity-decision-rubric.md"
    rel: "extended-by"
  - file: "guardrails-as-hook-lattice-capabilities.md"
    rel: "extended-by"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "agent-design"
  - "skills"
  - "orchestration"
---

# Capability as the Single Agent-Composition Primitive

## What It Is

A framework-level unit that packages everything one responsibility needs:

- **instructions** (the system-prompt fragment for this responsibility),
- **tools / toolsets** (including MCP servers),
- **lifecycle hooks** (e.g., pre-tool-use, for deterministic security/guidance),
- **guardrails** (input/output constraints),
- **model settings**.

Agent definition collapses to `model + [capabilities]`. In the 1.0 style, an agent was a
hodgepodge of tools and prompt text with no seams; in 2.0, seams follow responsibilities,
so a knowledge-base capability or an escalation capability moves between agents intact.
Progressive disclosure operates at the capability level: catalog descriptions always
visible, full instructions loaded on demand — demonstrated in-video by an agent loading
its escalation capability only when a refund complaint required it.

## Why It Matters

This is the composition question every agent system answers somewhere: what is the unit
of reuse? The ecosystem has been converging piecemeal (skills as portable directories,
MCP as portable tool bundles, hooks as portable determinism); the capability is the
first mainstream framework primitive that bundles all of them with the instructions that
govern them. For the engine — whose skills already pair procedure with context contracts
— it is external confirmation that "instructions + tools + guards as one shareable unit"
is where the industry is landing, which matters for the portable-kernel design and for
any future export target.

## Why People Are Using It

Shipped in Pydantic AI 2.0 (a top-tier production agent framework); covered by a Tier-2
practitioner who explicitly frames it as the industry-consolidation moment. Same-problem
precedent in the KB: BMAD's everything-as-skill merge
(`everything-as-skill-architecture`) unified agent/workflow/persona under SKILL.md —
the capability is the framework-native version of the same collapse.

## Potential Alternatives

- **Skills + MCP + hooks kept separate** (Claude Code today) — same ingredients,
  composition happens by convention in the harness rather than by a typed primitive.
- **Everything-as-skill** (BMAD) — one file-based primitive; capability is its
  code-based sibling with typed settings and guardrails attached.
- **Subagents as the composition unit** — package responsibility as a whole agent;
  heavier isolation, worse reuse granularity.

## Potential Improvements

- Cross-framework capability portability (a capability spec that compiles to Pydantic
  AI, Claude Code skill + hooks, etc.) — the video's skills-portability precedent
  suggests the market will demand it.
- Versioning/provenance on shared capabilities — once two agents mount one capability,
  its evolution needs the same lifecycle discipline as any shared dependency.

## Potential Failure Modes

- **Capability sprawl** — hundred-capability catalogs recreate the tool-overload problem
  one level up; disclosure mitigates tokens, not decision quality.
- **Leaky bundling** — capabilities that quietly assume global agent state (shared
  memory, ordering) break the composability promise.
- **Framework lock-in of the unit itself** — the capability is Pydantic-AI-shaped; teams
  standardizing on it inherit the framework's abstraction tax (see
  `framework-abstraction-tax-for-agents`).
