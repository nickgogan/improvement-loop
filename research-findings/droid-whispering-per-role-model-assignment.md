---
name: '"Droid Whispering" — Deliberate Per-Role Model Assignment with Cross-Provider Bias Avoidance'
summary: |-
  Factory's internal term for deliberately assigning different models to different roles
  within one multi-agent system: planning benefits from slow, careful reasoning;
  implementation from fast code fluency and creativity; validation from precise
  instruction-following. No single model or provider is best at all three. The
  distinguishing move beyond ordinary task-based routing: validation is recommended to
  run on a model from a different provider entirely than implementation, specifically so
  validation isn't biased by the same training data as the work it's checking — a
  deliberate decorrelation move, not just a cost or capability optimization. Framed as a
  structural advantage of model-agnostic architecture: "you're only as strong as your
  weakest link... if you're locked into one model provider, you're constrained by that
  family's weakest capability." Role-to-model defaults were set by one team member as a
  starting point, with an explicit invitation for teams to customize per project.
implementation_notes: |-
  The engine's existing model-tier-routing findings are task-type-based; this finding's
  role-based axis is worth checking against any future IL multi-agent skill design (e.g.,
  if /design-agent ever produces a multi-role system) — and the cross-provider-for-
  validation angle specifically is relevant to hardening
  pre-code-validation-contracts-dual-blind-validators.md's isolation claim if that
  pattern is ever adopted.
category: Model Selection
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- Improvement Loop
- General
adopted_in: []
sources:
- multi-agent-architecture-that-actually-ships.md
related_findings:
- file: task-specific-model-routing-table-march-2026-bench.md
  rel: same-problem
- file: center-vs-edge-of-distribution-task-classification.md
  rel: same-problem
- file: missions-three-role-architecture-serial-targeted-parallelization.md
  rel: extends
- file: pre-code-validation-contracts-dual-blind-validators.md
  rel: enables
proposals: null
date_discovered: '2026-07-18'
last_updated: '2026-07-18'
pipeline_status: "synthesized"
consumed_by:
  - "agent-architecture-decisions.md"
  - "rules/cross-provider-validator-assignment-rule.md"
---

## What It Is

A named practice ("droid whispering," internal Factory terminology) for deliberately
assigning different models to different *roles* within one multi-agent system, on the
premise that no single model or provider is best at all of: planning (rewarded by slow,
careful reasoning), implementation (rewarded by fast code fluency and creativity), and
validation (rewarded by precise instruction-following). The distinguishing move beyond
ordinary task-based model routing: validation is recommended to run on a model from a
**different provider entirely** than implementation, specifically so validation isn't
"biased by the same training data" as the work it's checking — a deliberate decorrelation
move, not just a cost or capability optimization. Framed as a structural advantage of
model-agnostic architecture generally: "you're only as strong as your weakest link... if
you're locked into one model provider, then you're constrained by that family's weakest
capability," and conversely, a well-structured multi-role system (validation contracts,
milestone checkpoints) can let weaker or open-weight models fill some roles successfully
because the surrounding structure compensates. Role-to-model defaults were set by one
team member (Theo) as a starting point, with an explicit invitation for teams to
customize per their own project's needs — offered as a discipline to develop, not a fixed
lookup table.

## Why It Matters

The KB's existing model-routing findings (task-specific-model-routing-table-march-2026-bench.md,
center-vs-edge-of-distribution-task-classification.md) route by *task type* — what kind
of work is this. This finding supplies an orthogonal axis specific to multi-agent
systems: given a fixed task, which *role in the pipeline* is a given call playing, and
does that role's job (careful reasoning vs. fast fluency vs. precise instruction-
following) call for a different model than the role next to it — plus a distinct
rationale (bias decorrelation for adversarial validation) that pure cost/capability
routing tables don't capture at all. This is directly relevant to
pre-code-validation-contracts-dual-blind-validators.md's "neither validator has seen the
implementation" claim: cross-provider model assignment is one concrete way to make that
isolation more robust — different training data, not just different context window.

## Why People Are Using It

Practitioner-named and practiced at Factory, but explicitly presented as evolving team
judgment ("we really encourage people to make these their own") rather than settled,
benchmarked assignment — the specific reason this is rated Medium evidence despite
sitting inside an otherwise strong-evidence production system.

## Potential Alternatives

- **Single-provider, single-model-family multi-agent systems:** simpler operationally
  (one API/billing relationship) — explicitly the condition this finding argues against
  ("you're only as strong as your weakest link"), but avoids the cross-provider
  engineering overhead (different tool-calling conventions, different rate limits,
  different prompt-formatting quirks).
- **Task-type routing without role-awareness**
  (task-specific-model-routing-table-march-2026-bench.md): simpler to apply, but doesn't
  capture the specific "decorrelate the validator from the implementer" rationale this
  finding is built around.

## Potential Improvements

- A published rationale, even informal, for *why* a given model sits in a given role
  beyond "someone tried it and it worked" — the talk names the reasoning categories
  (slow reasoning / fast fluency / precise instruction-following) but doesn't map
  specific models to specific reasoning strengths in a reusable way.
- Measuring whether cross-provider validation actually catches more issues than
  same-provider validation in practice, to convert the bias-decorrelation rationale from
  a plausible theory into evidence.

## Potential Failure Modes

- **Operational surface multiplication:** cross-provider architectures multiply
  operational surface area (auth, rate limits, cost tracking, differing tool-call
  semantics — see harness-engineering-third-evolution.md's note on post-training being
  harness-specific) — the coordination cost of droid whispering itself is not accounted
  for in this source.
- **Unexamined convention calcification:** role-to-model defaults set once by one person
  risk calcifying into unexamined convention the way any other unversioned
  tribal-knowledge assignment does, unless revisited as models change — this source's own
  framing anticipates this by calling the defaults a customizable starting point, not a
  fixed answer.
- **Weakening decorrelation assumption:** the rationale assumes different providers'
  training data and failure modes are meaningfully uncorrelated — as frontier labs
  converge on similar data sources and techniques, this assumption may weaken over time
  with no signal that it has.

## Extraction Note — 2026-07-19
Extracted as **rule**: [[cross-provider-validator-assignment-rule]] in `extracts/rules/` (harvest-queue promotion, DD-101). The DD-97 corpus scan matched [[holdout-validation-pattern-blind-regression]]; ruled **create new (false positive)** per the 2026-07-19 extension-proposals report — orthogonal bias-mitigation mechanism (different provider vs. information holdout), complementary sibling.
