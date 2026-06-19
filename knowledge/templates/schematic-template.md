---
title: "{Schematic name — the cluster this captures}"
id: "{kebab-case-id}"
type: "schematic"
category: "system-design"
target_system:
  - "improvement-loop"
stage: "draft"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
author: "{nick | claude}"
altitude: "{middle | top}"          # middle = single-agent; top = multi-agent / composition
maturity: "{seed | validated}"      # seed = first-cut; validated = exercised against real demand
grounded_in:                        # research-finding stems (must resolve to research-findings/<stem>.md)
  - "{finding-stem}"
composed_of:                        # artifacts/skills/templates this configuration is built from
  - "{path or skill name}"
source_dd:
  - "DD-107"
tags:
  - "schematic"
  - "{function-tag}"
aliases:
  - "{Alternative name}"
---

# {Schematic name}

> One-sentence statement of the demand→configuration this captures.

## Demand

What need this configuration answers. Indexed on three axes:

| Axis | Value |
|------|-------|
| **Function** | {coding / research / operations / assistant / audit} |
| **Scope / lifespan** | {personal-persistent ↔ project-bound} |
| **Non-functionals** | data boundary: {…}; reliability: {…}; autonomy need: {…}; cost: {…} |

{One short paragraph: when you'd reach for this schematic, and the shape of the problem it solves.}

## Configuration

The layered internals, ordered by volatility — most-stable core first. Cores are reusable across
schematics; the outer layers vary per deployment.

### Capability + memory core

{What the agent can do (its capability surface) and how it remembers (memory tiers: working /
session / persistent KB / none). This is the reusable core.}

### Coordination / architecture

{Single-agent, or multi-agent? If multi: topology (fan-out, pipeline, orchestrator-worker),
how work is split, how results merge.}

### Autonomy

State the level on the 5-level ladder and **why** it sits there:

`operator` → `collaborator` → `consultant` → `approver` → `observer`

{e.g., "approver — the agent drafts and stages; a human gates every promotion (DD-29)."}

### Deployment surface

{Where it runs: Claude Code harness / local + local-LLM / provider-API / Notion-embedded.
State the surface and the one or two constraints it imposes.}

## Evaluation & feedback

**Required.** A schematic without this layer is not self-evolving — it's a static recipe.

- **How it's evaluated:** {outcome vs process; independent vs self-report — name the mechanism.}
- **Feedback mechanism:** {internal / external / multi-agent / human — how signal returns and
  what it changes.}

## Grounding & composition

- **`grounded_in`** — the evidence this configuration rests on:
  - `{finding-stem}` — {why this finding grounds a choice above}
- **`composed_of`** — what it's built from:
  - `{artifact/skill/template}` — {how it's used here}

## Risk & maturity

- **Known risks / failure modes:** {the 1–3 ways this configuration bites.}
- **Maturity:** {seed | validated} — {if seed, name what's unvalidated or where grounding is thin.}
- **Revisit when:** {trigger — a grounding finding moves, demand shifts, a new cluster member appears.}
