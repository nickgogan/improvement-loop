---
name: "Post-Retrieval Reranking via Weighted Signal Composition"
summary: "After initial retrieval and rank fusion, Memongo applies post-retrieval reranking via a weighted composition of four explicit signals: keyword overlap (0.30), temporal proximity (0.40), entity name match (0.40), quoted phrase match (0.60). Signals are human-inspectable weights rather than a learned reranker, making the rerank stage auditable and tuneable without retraining."
implementation_notes: "This is a cheap, interpretable alternative to a neural reranker (ColBERT, Cohere Rerank). The weights make tradeoffs explicit — for instance, quoted phrase (0.60) > temporal (0.40) means exact-phrase memory is prioritized over recency. Worth replicating in any system where reranker opacity is a blocker for debugging retrieval failures. For Memongo improvement: evaluate whether these weights were hand-tuned or swept, and whether task-conditional weights improve on a fixed vector."
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "memongo-mongodb-native-agent-memory-github.md"
related_findings:
  - file: rank-fusion-hybrid-retrieval-mongodb-atlas.md
    rel: extends
  - file: hybrid-retrieval-pattern-semantic-lexical-graph.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-27"
pipeline_status: synthesized
consumed_by:
  - "session-persistence-and-memory.md"
---

## What It Is

A post-retrieval reranking stage that assigns each candidate a score as the weighted sum of four orthogonal signals:

| Signal | Weight | What it measures |
|--------|--------|------------------|
| Quoted phrase match | 0.60 | Exact-phrase presence from the query |
| Temporal proximity | 0.40 | Recency relative to query-time |
| Entity name match | 0.40 | Named-entity agreement with query |
| Keyword overlap | 0.30 | Lexical token overlap |

Memongo applies this on top of the `$rankFusion`-combined vector + lexical result set. The weights are constants (the repo shows them as coefficients), not learned parameters.

## Why It Matters

Learned rerankers (ColBERT, Cohere Rerank, Anthropic's contextual retrieval) produce strong scores but are opaque. When a retrieval surface returns the wrong memory, "the reranker thought this was more relevant" is not actionable debugging. Explicit weighted signals give three properties neural rerankers do not:

1. **Inspectability** — for any result, you can decompose its score into contributing signals and see which one dominated.
2. **Tuneability** — weights are ops-editable. If temporal proximity should dominate for one use case, adjust the coefficient.
3. **No training loop** — no labeled data, no model artifact, no retraining when the embedding model changes.

The weights themselves communicate design intent: quoted-phrase highest (literal matches are strong signals), temporal and entity tied, keyword overlap lowest (because semantic search already handles loose token overlap).

## Why People Are Using It

Observed in [Memongo](https://github.com/romiluz13/Memongo). The pattern generalizes — many production RAG pipelines implement similar weighted-signal reranks when neural rerankers are too expensive or too opaque for their error-debugging needs. Memongo's packaging of the specific weight set as part of the public architecture is what makes it citable.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Neural reranker (ColBERT / Cohere Rerank) | Learned model scores query-document pairs | When labeled preference data exists and absolute top-1 precision matters more than debuggability |
| LLM-as-reranker | Send top-K to an LLM with a rerank prompt | When retrieval volume is low and LLM latency is acceptable |
| No reranking | Use fusion output directly | When the fused result is already good enough and post-processing adds cost without precision gain |

## Potential Improvements

- **Query-conditioned weights** — classify the query type (factual / temporal / identity lookup / open-ended) and swap weight vectors per class.
- **Weight sweep on LongMemEval-S** — publish the sensitivity of the Hit Rate score to each weight. Static weights that weren't swept are a missed optimization.
- **Add a semantic-overlap signal** — currently there's a lexical keyword signal (0.30) but no explicit semantic-overlap signal post-fusion; the fused score may already encode this, but making it an explicit weight would close the loop.

## Potential Failure Modes

- **Weight drift** — weights that worked on LongMemEval-S may mis-rank on different workloads; no feedback loop updates them.
- **Score-scale mismatch** — signals need to be normalized to comparable ranges before weighted sum; a bug here makes one signal silently dominate.
- **Missing signals** — any query dimension not in the four-signal basis cannot be reranked on; e.g., sentiment, topic, or modality are unreachable without extending the vector.
- **Coupling to data shape** — "quoted phrase" relies on the query containing quoted phrases; most user queries won't. The weight is only active on a small query subset.
