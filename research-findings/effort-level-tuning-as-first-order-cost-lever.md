---
name: Effort-Level Tuning as First-Order Cost Lever
summary: 'Plain English: within one frontier model, the effort dial moves cost more than the model

  picker does — a low-effort frontier model can match the previous tier at max effort for a

  fraction of the price. Deep Sweet long-horizon agentic benchmark: Fable 5 at max effort

  costs $22/task; at low effort $3.76/task (>80% cheaper) while scoring 60% — beating Opus

  4.8 at MAX effort (59%, $13/task). Fable 5 effort curve: low 60%, medium 65%, high 69%,

  extra-high 70% (max adds little over extra-high). Anthropic''s own frontier-code

  accuracy-vs-cost chart corroborates: Fable low (~$5) matches Opus 4.8 max (~$11) at half

  the cost. Practical rule: default effort (high) is wrong for most tasks; match effort to

  task complexity (web design -> low/medium), switch via /effort in Claude Code.'
implementation_notes: 'P2: feeds the Nick-gated model-capability-registry refresh bundle (next intentional

  D2/2.A refresh, not piecemeal) — registry datapoints itemized in the session-136 return

  summary. Corroborates the existing claude-5-family finding''s caveat that effort-level

  tuning matters more than tier choice at the margin. Benchmark provenance caveat: Deep

  Sweet numbers presented in a practitioner video; the second chart is Anthropic''s own

  (announcement-adjacent) — re-anchor when independent numbers accumulate.'
category: Model Selection
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (model routing)
- General
adopted_in: []
sources:
- make-fable-5-80-percent-cheaper.md
related_findings:
- file: claude-5-family-retiers-claude-line.md
  rel: extends
- file: task-specific-model-routing-table-march-2026-bench.md
  rel: same-problem
- file: effort-scaling-rules-embedded-in-orchestrator.md
  rel: same-problem
- file: token-economics-as-architecture-driver.md
  rel: same-problem
- file: advisor-executor-api-pattern.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
pipeline_status: raw
---

# Effort-Level Tuning as First-Order Cost Lever

## What It Is

Treating the reasoning-effort setting — not model choice — as the primary cost control for
frontier-model usage. The quantified case (Deep Sweet, long-horizon agentic tasks):

| Configuration | Pass rate | Cost/task |
|---|---|---|
| Fable 5 — low | 60% | $3.76 |
| Fable 5 — medium | 65% | — |
| Fable 5 — high (default) | 69% | — |
| Fable 5 — extra high | 70% | — |
| Fable 5 — max | ~70% | $22 |
| Opus 4.8 — max | 59% | $13 |

Low-effort Fable 5 outscores max-effort Opus 4.8 at ~29% of its cost, and at ~1/6 the cost
of max-effort Fable 5. Anthropic's frontier-code accuracy-vs-cost chart shows the same
shape: Fable low (~$5) equals Opus 4.8 max (~$11) on score. Mechanics: `/effort` in the
Claude Code terminal; default is high.

## Why It Matters

Most routing discussion is about which model; this evidence says the bigger, cheaper win
is usually which effort. The diminishing-returns tail (extra-high -> max buys ~nothing for
2-4x the cost) means default-high users are overpaying on the majority of tasks that
aren't long-horizon-complex. For the engine, effort belongs alongside model tier as a
routing input in the capability registry and any future harness/routing design.

## Why People Are Using It

Frontier pricing pressure (Fable 5 leaving subscription plans; weekly usage caps) is
forcing practitioners to find levers that preserve quality; this one requires zero
workflow change.

## Potential Alternatives

Tier-downshifting (route to Sonnet/Opus) — coarser, loses frontier-specific strengths;
advisor-executor pairing — better for tasks needing occasional frontier judgment;
prompt-side token diet (brevity/reuse skills) — orthogonal, composable with effort tuning.

## Potential Improvements

Per-task-class effort defaults encoded in orchestrator/skill configs rather than a global
session setting; independent replication of the Deep Sweet numbers; extending the curve
with tokenizer-effect-corrected effective costs.

## Potential Failure Modes

Benchmark-shape dependence — the flat tail is measured on one benchmark family; genuinely
hard long-horizon tasks may still need high/max. Silent quality erosion on tasks where the
10-point pass-rate spread (60 vs 70) is exactly the margin that matters. Effort settings
interact with provider-side changes (defaults, pricing) and can go stale quickly —
registry data, not prose, should carry the numbers.
