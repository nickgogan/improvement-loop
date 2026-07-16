---
name: Prototype at Frontier, Then Downshift Execution to Cheaper Models
summary: 'Sequencing rule for the two-layer model stack: prove a new capability end-to-end on

  the frontier model first, then decompose the proven flow and migrate sub-tasks to

  cheaper models, keeping frontier only where it uniquely earns its cost. Jones''s worked

  example: a hyper-targeted mailer campaign (Google Maps sun/shade analysis of porches +

  3D structure models + custom cards) prototyped entirely with Fable 5 — "once the idea

  is prototyped through with Fable 5, you can get a cheaper pipeline put together"; the

  image-merge step doesn''t need frontier, the spatial+logical reasoning that proved the

  flow did. Each downshift emits a validated task→cheap-model mapping — this is the

  process that generates routing-table entries rather than consuming them.'
implementation_notes: 'Adopt as the engine''s default sequence for new task classes: first instance on the

  frontier tier, then record which decomposed sub-tasks downshifted cleanly — each such

  record is a KB-grounded routing datapoint feeding task-specific-model-routing-table

  and the model-capability registry''s Nick-gated refresh. Caveat from the same source

  (Stripe''s 50M-line one-day migration): the downshift/harvest step presupposes

  verification infrastructure — test coverage and review systems built in advance —

  otherwise frontier output is "changes nobody could approve."'
category: Model Selection
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- Improvement Loop
- General
adopted_in: []
sources:
- you-cant-compete-on-cheap-models-anymore.md
related_findings:
- file: task-specific-model-routing-table-march-2026-bench.md
  rel: enables
- file: model-tier-routing-expensive-orchestrator-cheap-s.md
  rel: same-problem
- file: advisor-executor-api-pattern.md
  rel: same-problem
- file: center-vs-edge-of-distribution-task-classification.md
  rel: enabled-by
- file: frontier-capability-probing-scouting.md
  rel: enabled-by
- file: frontier-model-as-harness-designer.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- model-resilient-prompt-engineering.md
---

## What It Is

A lifecycle for frontier capability: frontier models convert edge-of-distribution tasks
into proven flows; proven flows are then center-of-distribution for the parts that
matter, so execution migrates down-tier. The frontier model's role in the prototype is
doing the whole thing at once — in the mailer example, combining spatial reasoning (sun/
shade analysis), 3D model retrieval, tool orchestration (Blender and others), and
translation into a business flow with an address table. After the prototype validates,
sub-tasks with familiar shapes (image-into-mailer merge, batch generation) move to a
cheaper pipeline. The output of each migration is a concrete routing decision: this
sub-task, this cheap model, validated against the frontier-built reference.

Complementary evidence in the source: Stripe's 50M-line codebase migration in one day
worked because years of task coverage, review systems, and model-driving skill preceded
it — "Stripe built the infrastructure first and then harvested the value with frontier
models."

## Why It Matters

The KB's routing findings (tier routing, routing tables) describe steady-state
allocations but not where the entries come from; this supplies the generator. For the
engine it is a budget-shaped rule: frontier spend is a one-time cost per task class, not
a recurring cost per task — which changes the ROI math on expensive models and gives the
model-capability registry a refresh mechanism grounded in first-party runs rather than
vendor benchmarks. Combined with capability-probing (which discovers the task class),
it closes the loop: probe → prototype → downshift → routing entry.

## Why People Are Using It

Practitioner-documented at the anecdote level (Jones's sourced example from X; Stripe's
publicly reported migration) plus the analyst framing that routing-to-cheap alone is
commoditizing. No systematic study; the pattern's two halves (frontier uniqueness at the
edge, cheap parity at the center) are separately corroborated by Hashimoto's quantified
experiment.

## Potential Alternatives

- **Straight-to-cheap with retries:** attempt the task on the cheap tier first, escalate
  on failure — fine at the center, but edge tasks fail silently or were never conceived.
- **Advisor-executor coupling** (advisor-executor-api-pattern): keep frontier in the
  loop as consultant rather than prototyping then exiting — better when the task class
  never fully stabilizes.

## Potential Improvements

- A downshift checklist: what must be true (reference output, verification harness,
  stable decomposition) before a sub-task leaves the frontier tier.
- Registry integration: a standard record shape for downshift events so routing entries
  accumulate without per-session bookkeeping.

## Potential Failure Modes

- **Downshifting too early:** the cheap model reproduces the demo but not the edge
  cases the frontier model was silently absorbing.
- **No verification substrate:** without the Stripe-style infrastructure, downshifted
  output can't be approved at the new volume — the harvest stalls at review.
- **Prototype overfit:** the frontier prototype encodes one instance, not the task
  class; the "validated" routing entry generalizes worse than assumed.
