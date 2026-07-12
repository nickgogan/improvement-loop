---
name: "Semantic Caching Failure Modes"
summary: |-
  Semantic caching (serve a cached answer when a new prompt's embedding is "close enough"
  to a past one) skips the model entirely on a hit — near-zero cost, instant reply — but
  carries three production failure modes: (1) similarity false-positives where opposite
  intents sit adjacent in embedding space ("sort ascending" vs "sort descending"), so a
  loose threshold serves wrong answers; (2) stale cached answers after the underlying
  fact changes (a price update the cache never saw); (3) upgrading the embedding model
  silently invalidates the entire cache. Verdict from the source: a knob to turn
  carefully, not a switch to leave on — dazzles in demos, frays nerves in production.
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "Not Flagged"
applicability:
  - "General"
adopted_in: []
sources:
  - "ai-gateway-the-layer-every-ai-stack-eventually-needs.md"
related_findings:
  - file: "ai-gateway-model-traffic-layer.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A gateway-layer optimization distinct from provider-side prompt caching: instead of
requiring a character-for-character identical prompt, semantic caching embeds each prompt
into a vector, checks whether any past prompt means roughly the same thing, and on a hit
serves the stored answer without calling the model at all ("What's the capital of
France?" and "France capital city, please" share one cached answer).

The danger lives in "roughly." Three documented failure modes:

1. **Opposite-intent collisions.** Prompts that look alike but mean opposite things land
   nearly on top of each other in embedding space — "sort ascending" vs "sort
   descending." A similarity threshold set too loose serves someone the wrong answer.
2. **Stale answers.** The cached answer outlives the fact it encodes — a price changes,
   the cache doesn't.
3. **Embedding-upgrade cache wipe.** Upgrading the embedding model changes the vector
   space and can invalidate the entire cache without warning.

## Why It Matters

The KB's caching findings are all about provider-side *prompt* caching (prefix
stability, cache-hit-rate SLOs, model-switch invalidation). Semantic caching is a
different mechanism — answer reuse, not prefix reuse — with a different failure
signature: it can be silently *wrong*, not just silently expensive. Recorded now so any
future gateway adoption decision inherits the caveats with the feature.

## Why People Are Using It

On paper it is the best cost lever a gateway offers — a hit skips inference entirely.
That demo economics ("dazzles in a demo") is exactly why it gets switched on before the
threshold, invalidation, and staleness work has been done.

## Potential Alternatives

- **Exact-match response caching:** far fewer hits, but no wrong-answer risk.
- **Provider-side prompt caching** (existing KB cluster): reduces cost of reprocessing
  context without reusing answers.
- **No caching on semantically sensitive routes:** scope semantic caching to genuinely
  idempotent, fact-stable query classes only.

## Potential Improvements

- Per-route similarity thresholds instead of one global knob.
- TTLs and invalidation hooks tied to the underlying data (price tables, policy docs).
- Version-pinned embeddings with planned cache migration on upgrade.

## Potential Failure Modes

The three above are the finding. Meta-failure: treating the cache-hit rate as a pure win
metric — a rising hit rate with a loose threshold may be measuring an increase in wrong
answers served.
