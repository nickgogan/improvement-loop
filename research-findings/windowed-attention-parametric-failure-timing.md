---
name: "Windowed Attention — Parametrically Predictable Failure Timing"
summary: |-
  For models with sliding-window attention, the turn at which instructions become unreachable
  is computable in advance from the window size and token positions — not a fuzzy degradation
  but a schedulable event. In the paper's Mistral-7B validation, doubling the attention window
  roughly doubles the failure turn (W=1024 fails near turn 6, W=8192 near turn 44) with a
  linear dose-response at R-squared > 0.999. For us this means session-length budgets for such
  models can be derived, not guessed.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (empirical benchmarks)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "arxiv-when-attention-closes-goal-accessibility.md"
related_findings:
  - file: "attention-closure-goal-accessibility-collapse.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

## What It Is

A result from arXiv 2605.12922: under sliding-window attention with window size W, the attention channel to goal tokens closes at the turn where the distance between the first response token position and the last goal token position reaches W — formally, closure at turn τ when R_min(τ) − G_max ≥ W. Empirical validation on Mistral-7B: W=1024 closes around turn 6, W=2048 around turn 12, W=4096 around turn 23, W=8192 around turn 44 — a linear dose-response with R² > 0.999.

## Why It Matters

It converts "long conversations eventually drift" into an equation for a class of architectures. If you know a model's attention window and your typical tokens-per-turn, you can compute the turn budget after which the system prompt is structurally out of reach — and schedule compaction, handoff, or session restart *before* that point rather than reacting to observed drift. It also sharpens procurement/model-selection questions: a model's effective instruction-retention horizon under windowed attention is a derivable spec, not a benchmark vibe.

## Why People Are Using It

Academic result (same paper as the attention-closure mechanism); no production adoption yet. Relevant to anyone running open-weight models with sliding-window or hybrid attention (Mistral-family and similar), and to harness designers setting session-length policies.

## Potential Improvements

- If we ever run windowed-attention models locally, derive the closure turn for our typical turn sizes and set handoff thresholds below it
- Watch for follow-ups extending the parametric prediction to hybrid local/global attention schemes used by frontier models

## Potential Failure Modes

- **Architecture opacity:** hosted frontier models don't disclose attention windowing, making the formula inapplicable where we'd most want it
- **Turn-size variance:** the prediction is in token positions; bursty tool outputs shift the closure turn earlier than a per-turn average suggests
- **False precision:** validated primarily on Mistral-7B; treating the linear law as universal across windowed architectures is unwarranted
