---
notion_id: "32c1e08b-9b34-8156-9ea5-c7be51666092"
name: "Add Cross-Encoder Reranking to Retrieval Pipelines"
proposal: "Any retrieval pipeline using single-vector embeddings (memory search, skill matching, Notion semantic search) should add a cross-encoder reranking stage after initial retrieval. This addresses the mathematically proven limitation that single-vector embeddings cannot represent all top-k subsets for realistic corpus sizes."
rationale: "Fundamental Limits of Single-Vector Embedding Retrieval (Strong evidence): Google DeepMind proved dimensionality bounds limit top-k subset representation. SOTA models fail catastrophically on LIMIT benchmark (<20% R@100). BM25 outperforms dense models on combinatorial queries. Hybrid retrieval with cross-encoder reranking achieves 100% on the same benchmark."
status: "Not started"
target_system: "General / Cross-System"
priority: "P1 (Implement Now)"
risk_level: "Medium"
implementation_complexity: "Medium"
effort: "Medium (1-4 hours)"
door_type: "Two-Way"
ops_impact: "Neutral"
conflicts: false
conflict_group: null
findings: []
date_proposed: "2026-03-23"
date_resolved: null
---

# Add Cross-Encoder Reranking to Retrieval Pipelines

## Current State
Our retrieval pipelines (Notion semantic search, Perplexity memory_search, skill matching) likely rely on single-vector embedding similarity as the primary retrieval mechanism. The existing KB finding "Hybrid Retrieval Pattern (Semantic + Lexical + Graph)" already recommends hybrid approaches, but the theoretical proof of WHY single-vector retrieval fails was not previously available. No cross-encoder reranking stage exists in any of our retrieval paths.

## Proposed Change
For each retrieval pipeline that uses embedding-based search:

1. **First stage (keep):** Use existing embedding-based retrieval to get a broad candidate set (top-N, where N is larger than the final k needed)
2. **Second stage (add):** Pass candidates through a cross-encoder reranker that scores each (query, document) pair with full attention. Return the top-k from reranked results.
3. **For combinatorial queries** (AND/OR logic, multiple relevant documents): Consider adding BM25/lexical retrieval as a parallel first-stage alongside embeddings, then merge before reranking.

Priority order for implementation:
- Perplexity memory_search (directly affects conversation quality)
- Skill matching (determines which skill gets loaded)
- Notion semantic search (affects research loop and KB queries)

## Rationale
The theoretical proof (Theorem 1 in arxiv 2508.21038) establishes that for n documents, k results, and margin gamma, the embedding dimension must satisfy d >= log(C(n,k)) / log(1 + 1/gamma). For n=10^6, k=100, gamma=0.1, this requires d>425 -- and real models need 4-5x the theoretical minimum. Current embedding models (768-4096 dimensions) are provably insufficient for exhaustive combinatorial retrieval over realistic corpora. The LIMIT benchmark demonstrates this empirically: all tested SOTA models fail.

## Door Type Assessment
Two-way door. Reranking is an additive pipeline stage. It can be disabled or removed at any time without affecting the underlying embedding index. The original retrieval results are always available as a fallback.

## Implementation Assessment
Medium complexity. Requires: (1) selecting a cross-encoder model, (2) integrating it as a pipeline stage after each embedding retrieval call, (3) tuning the first-stage candidate set size (retrieve more candidates than before to give the reranker enough to work with). Does not require changing any embedding indexes or data schemas. May require evaluating latency impact since cross-encoders are more compute-intensive per pair.

## Operational Impact
Neutral. Adds a processing step to retrieval but doesn't change what operators need to monitor. May slightly increase retrieval latency. No new failure modes beyond the reranker model itself being unavailable (fallback: return first-stage results unranked).

## Implementation Steps
1. Evaluate cross-encoder options suitable for our retrieval tasks (consider model size vs latency trade-offs)
2. Implement reranking wrapper that takes (query, candidate_list) and returns reranked results
3. Integrate into Perplexity memory_search pipeline first (highest impact)
4. Measure retrieval quality before/after on representative queries
5. Extend to skill matching and Notion search pipelines
6. Consider adding BM25 parallel first-stage for queries with AND/OR logic patterns
