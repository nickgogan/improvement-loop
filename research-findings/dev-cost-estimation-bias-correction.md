---
name: Dev-Cost-Estimation Bias Correction (Standing Rule)
summary: 'Plain English: models systematically pick cheap, low-quality designs because they think

  building the good design takes weeks — a human-timeline bias baked in from training

  data. Kun Chen''s demonstration: ask a frontier model to estimate building a 3D game and

  it answers in days/weeks/months; ask it to build the same thing and it returns a

  playable version in minutes. Because the model implicitly prices options at human

  development cost, it steers technical decisions toward "cheap" solutions that are low

  quality, unscalable, or hard to maintain. His correction is a one-line standing rule in

  the always-loaded global memory file: "when making technical decisions, don''t give too

  much weight to development cost."'
implementation_notes: 'Directly adoptable as a candidate standing rule in the engine''s CLAUDE.md / agent

  constitutions wherever agents make design or scoping decisions (design-* skills,

  Codifier drafting, Owner proposals) — the same bias would make our agents under-scope

  designs. One line of always-loaded context; the cost is trivial, the gate is Nick''s

  (CLAUDE.md changes are deployment). Note the interaction with the engine''s Occam''s

  razor standing preference: the rule corrects cost *mis-estimation*, it does not license

  gold-plating — minimum viable abstraction still applies.'
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (agent constitutions, design-* skills)
- General
adopted_in: []
sources:
- l8-principals-agentic-engineering-workflow.md
related_findings: []
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- model-resilient-prompt-engineering.md
- rules/discount-dev-cost-in-design-decisions.md
---

## What It Is

A one-line standing rule that corrects a specific, demonstrable model bias: LLMs trained
on human development data estimate implementation cost on human timelines ("AI doesn't
seem to know it can code much faster than humans yet"). When the model weighs design
options, the implicitly inflated cost of the better option biases it toward cheap
solutions. The correction lives in the global memory file so it applies to every session:
*when making technical decisions, don't give too much weight to development cost.*

## Why It Matters

Design-option selection is upstream of everything an agent builds. A silent cost bias
means the agent repeatedly proposes the low-quality architecture not because it judged
quality/maintainability tradeoffs, but because it mispriced the alternative. The fix
costs one line of context and reframes the whole option space: in an agentic workflow,
development cost has collapsed, so quality, scalability, and maintainability should
dominate the decision.

## Why People Are Using It

Kun Chen (ex-Meta/Microsoft principal, builds coding agents at Atlassian, ships 40-50
tested production changes daily) keeps it in a deliberately minimal (~27-line) global
memory file — one of the few rules that earns permanent always-loaded placement, based on
repeatedly observing the estimate-vs-actual mismatch ("I have done this so many times").

## Potential Improvements

- Pair with an explicit decision heuristic: "price options by tokens and review burden,
  not calendar time"
- Scope the rule to design/architecture decisions to avoid it bleeding into contexts
  where cost genuinely matters (e.g., human process planning, real deadline estimation)

## Potential Failure Modes

- Over-correction: the agent stops considering cost entirely and gold-plates —
  development cost is lower, not zero (tokens, review burden, and maintenance are real)
- The bias claim rests on one practitioner's repeated informal observation, not a
  controlled eval; magnitude may vary by model and task
- Human-facing estimates still need human timelines when humans execute — the rule must
  not leak into project planning for people

## Extraction Note — 2026-07-19
Extracted as **rule**: [[discount-dev-cost-in-design-decisions]] in `extracts/rules/`
