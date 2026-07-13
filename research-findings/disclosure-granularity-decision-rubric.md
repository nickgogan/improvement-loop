---
name: "Shipped Decision Rubric for Disclosure Granularity"
summary: |-
  Plain English: "what stays in the always-loaded prompt vs what loads on demand" is a
  design question that deserves an explicit, shipped decision rubric — not per-author
  intuition. Pydantic AI's packaged consumer skill instructs coding agents to treat
  `defer_loading=True` as a design question for EVERY capability, to keep the eager
  prompt to four things (identity, task boundaries, global safety, routing), and to
  choose between two disclosure granularities by shape: capability-on-demand for
  bundles whose tools share instructions, tool search for large flat catalogs of
  independent tools. The framework ships the rubric to its consumers as part of the
  skill that teaches agent construction — disclosure discipline as documented doctrine
  rather than folklore.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "capability-as-agent-composition-primitive.md"
    rel: "extends"
  - file: "agent-context-kiss-commandments-minimum-viable.md"
    rel: "same-problem"
  - file: "gpt-54-tool-search-deferred-tool-loading.md"
    rel: "same-problem"
  - file: "cache-stable-progressive-disclosure-catalog.md"
    rel: "same-problem"
  - file: "on-demand-vs-always-on-skill-activation.md"
    rel: "same-problem"
  - file: "branch-analysis-externalization-rule-skill-reference.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "agent-design-patterns.md"
tags:
  - "context-engineering"
  - "progressive-disclosure"
  - "design-rubric"
---

# Shipped Decision Rubric for Disclosure Granularity

## What It Is

An opinionated, distributed design rubric answering the eager-vs-deferred context
question (`.agents/skills/building-pydantic-ai-agents/references/ON-DEMAND-CAPABILITIES.md`):

1. **Default question, not default answer** — `defer_loading=True` must be *considered*
   for every capability; disclosure is a per-unit design decision, never an
   afterthought.
2. **Eager-prompt whitelist** — the always-loaded prompt is bounded to identity, task
   boundaries, global safety, and routing. Everything else earns eager status or loads
   on demand.
3. **Granularity by shape** — capability-on-demand when tools come in bundles with
   shared instructions (the instructions justify the bundle loading together); tool
   search when the surface is a large flat catalog of independent tools.

## Why It Matters

The KB records the ingredients repeatedly — minimum-viable context commandments, tool
search, progressive disclosure — but teams still decide disclosure ad hoc, per author.
The notable move is packaging the decision procedure itself: the framework's consumer
skill carries the rubric, so every downstream agent-builder inherits the same
disclosure doctrine. For any system with a growing catalog surface (skills, tools,
capabilities), the transferable artifact is a written rubric with an eager whitelist
and a shape test — cheap to adopt, and it converts recurring judgment calls into a
checkable standard.

## Why People Are Using It

Distributed inside the framework's packaged skill, so it reaches every consumer project
that installs it; the framework's own first-party capabilities follow the same
discipline. Source: Observed in
[pydantic-ai](https://github.com/pydantic/pydantic-ai) v2.9.0 — see
[[pydantic-ai-analysis]] for structural details.

## Potential Alternatives

- **Per-author judgment** — the status quo; works until catalogs grow past a few
  entries.
- **Everything deferred** — minimal eager prompt but adds a load round-trip to every
  first use; the rubric's eager whitelist exists precisely to avoid deferring routing
  and safety.
- **Token-budget-triggered review** (audit when the prompt exceeds N tokens) — reactive
  rather than per-unit; catches bloat late.

## Potential Improvements

- Quantified thresholds (bundle size, catalog width) at which each granularity wins,
  measured rather than asserted.
- Lint integration: flag eager content that falls outside the whitelist categories.

## Potential Failure Modes

- **Whitelist creep** — "routing" is elastic; eager prompts regrow unless the whitelist
  is policed.
- **Shape misreads** — bundles with weakly-shared instructions deferred as capabilities
  pay catalog cost without the coherence benefit.
- **Rubric fossilization** — as models get better at tool search, the shape boundary
  moves; a shipped rubric needs a revision owner.
