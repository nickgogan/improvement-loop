---
name: Query Decomposition with Sub-Query RRF Merge
summary: 'At query time, Memongo uses a lightweight LLM (GPT-4-mini) to decompose a user query into multiple sub-queries, runs retrieval on each, and merges the results via reciprocal rank fusion (RRF).
  The agent''s retrieval recipe is: decompose → parallel retrieve → RRF merge → post-retrieval reranking. Decomposition is cheap (small model) and happens before any expensive semantic work; the parallelism
  means sub-queries can fan out across vector + lexical indexes simultaneously.'
implementation_notes: 'A natural complement to native rank fusion — fan-out decomposed queries through `$rankFusion` for each sub-query, then RRF-merge across sub-queries. For Memongo improvement: evaluate
  whether a larger decomposition model produces better sub-queries for multi-hop temporal reasoning (Memongo''s weakest category at 84.0% on LongMemEval-S). The decomposition prompt itself is a prompt-engineering
  surface worth versioning as a ContractSpec.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- memongo-mongodb-native-agent-memory-github.md
related_findings:
- file: rank-fusion-hybrid-retrieval-mongodb-atlas.md
  rel: enables
- file: programmatic-tool-calling-code-orchestrated-tool-use.md
  rel: same-problem
- file: hybrid-retrieval-pattern-semantic-lexical-graph.md
  rel: extends
- file: agentic-search-memory-retrieval-architecture.md
  rel: extended-by
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-04-27'
pipeline_status: synthesized
consumed_by:
- session-persistence-and-memory.md
- structuring-agent-context.md
---

## What It Is

A retrieval-time preprocessing step: a small LLM rewrites the user's original query into several targeted sub-queries, each of which is executed independently against the retrieval index, then the ranked lists are merged with reciprocal rank fusion (RRF).

Memongo's choices:
- **Decomposer model:** GPT-4-mini (cheap, fast)
- **Fan-out target:** vector and lexical indexes (both Atlas-native)
- **Merge:** RRF across sub-query result sets
- **Downstream:** post-retrieval reranking with weighted signals (keyword / temporal / entity / quoted phrase)

## Why It Matters

A single user query often compresses several distinct retrieval needs. "What was the thing Nick mentioned about Atlas Search during the last Memongo session, and did we ever ship that fix?" contains a temporal constraint, an entity constraint, a topic constraint, and a status constraint. A single embedding of the full sentence blurs all four. Decomposition lets each concern hit the index as a separate signal, and RRF combines ranks rather than scores — making the merge robust to cross-sub-query score incomparability.

The economics work because decomposition with a small model (GPT-4-mini) is cheap relative to the retrieval it steers, and the retrieval quality gain typically outweighs the extra LLM latency.

## Why People Are Using It

Observed in [Memongo](https://github.com/romiluz13/Memongo). The pattern is also established in academic RAG literature (Multi-query RAG, HyDE, Step-Back Prompting) and in Anthropic's advanced tool use where Claude writes code to fan out retrieval, but Memongo's packaging — small-model decomposition coupled to native MongoDB rank fusion — is a distinctive production-ready configuration.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Single-query retrieval | Embed the user's sentence, top-K, done | For simple queries where decomposition overhead isn't justified |
| HyDE (Hypothetical Document Embeddings) | Generate a hypothetical answer, embed that, retrieve on it | When answers are more embedding-stable than questions |
| Agentic-RAG (let the agent itself iterate) | Agent writes queries, sees results, writes next query | When the retrieval budget per turn is unbounded |

## Potential Improvements

- Decomposition-model selection: larger models (Sonnet 4.6 / Gemini 2.5-Flash) may produce better sub-queries for multi-hop or temporal queries — worth A/B testing against the 84.0% temporal-reasoning score on LongMemEval-S.
- Adaptive fan-out: for queries classified as single-intent, skip decomposition entirely; for multi-intent queries, scale fan-out.
- Cache decomposition outputs keyed on the normalized query — repeat queries avoid the LLM hop.

## Potential Failure Modes

- Over-decomposition dilutes precision: too many sub-queries produce too many marginal matches, and RRF cannot compensate for noise at the input.
- Decomposer model drift — model upgrades change sub-query shapes, silently shifting retrieval behavior.
- Latency floor is set by the decomposition call; for interactive use cases every LLM hop is felt.
- RRF assumes comparable rank distributions across sub-queries — if some sub-queries return many hits and others none, merge behavior is lumpy.
