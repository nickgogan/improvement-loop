---
name: "Frontier Model as Harness Designer"
summary: |-
  Practitioner pattern (Nate B Jones): use the strongest available model (Fable 5) not to
  execute coding work but to design the goals and the harness — detailed goal
  specifications, custom scaffolding — that a cheaper executor model (e.g. Codex) then
  works within. Companion prompting guidance: give frontier models short prompts with
  differentiated context and maximum degrees of freedom; don't constrain them to a linear
  solution path.
implementation_notes: |-
  "Fable 5 is particularly useful at designing detailed goals and even goal harnesses for
  complicated coding tasks… build a custom harness with Fable to help my Codex 5.5 or
  whatever model I choose get this work done." Also: pick problems that would need a
  domain expert (audits, cost reduction, complex product capability modeling), pose them
  with short prompts + net-new context, "tell it to go figure it out." Aligns with the
  engine's agentic-OS direction (design-time governance by the strongest model; execution
  delegated) and with the model-capability registry's Fable 5 positioning.
category: "Agent Design"
evidence_strength: "Low (single practitioner opinion, no artifacts shown)"
adoption_status: "Not Yet Started"
priority: "P3"
applicability:
  - "IL (harness design, model routing)"
  - "General"
adopted_in: []
sources:
  - "free-fable-5-tokens-heres-how-to-max-them.md"
related_findings: []
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

The conventional split is "strong model plans, cheap model codes." This pushes one level
up: the strong model **designs the harness** — the goal structure, constraints, and
scaffolding — that the executor model runs inside. The frontier model's output is not a
plan for one task but a reusable execution environment for a class of tasks. Companion
guidance on invoking frontier models: short prompts, differentiated (net-new) context, and
deliberately preserved degrees of freedom — over-constraining to a linear procedure wastes
exactly the capability being paid for.

## Why It Matters for Us

This is independent practitioner convergence on the engine's own thesis: the valuable
design-time artifact is the harness/governance layer, with execution delegated downward
(agentic-OS direction note; DD-108 supervised autonomy). It also feeds two concrete
surfaces: the model-capability registry's Fable 5 row (harness-design as a named strength)
and the eventual `/design-harness` skill — whose product is precisely what this pattern
says the strongest model should be asked to produce. The short-prompt/degrees-of-freedom
guidance matters for how our skills address frontier reasoning models (consistent with the
KB's prescribed-reasoning anti-pattern findings).

## Caveats

Opinion-tier evidence: no artifacts, benchmarks, or worked examples shown; single source.
Treat as a direction signal corroborating existing internal direction, not as a proven
technique.
