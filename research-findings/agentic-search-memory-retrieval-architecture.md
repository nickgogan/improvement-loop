---
name: Agentic Search and Memory Retrieval (ASMR) Architecture
summary: 'A memory-system architecture that replaces vector-similarity retrieval with active LLM-driven reasoning over stored findings, end to end. Ingestion uses parallel reader agents extracting across
  multiple vectors (personal info, preferences, events, temporal, updates); retrieval uses specialized search agents that reason through the memory rather than nearest-neighbor-query it; answering uses
  an ensemble of N variant reasoning paths. Trades per-query LLM cost for higher retrieval quality on long-context / cross-session benchmarks. Plain English: instead of ''find the nearest document,'' the
  system runs several small agents that literally reason through the memory and return what they figured out. Expensive but powerful for hard cross-session reasoning questions.'
implementation_notes: Reference implementation is Supermemory's ASMR sandbox. Explicitly labeled 'highly experimental / not production' by the vendor ([[experimental-sandbox-labeling-discipline]]). Cost/latency
  disclosures completely absent from the source — production-readiness claims are unsupported.
category: Context Engineering
evidence_strength: Low (single-vendor sandbox, not production-shipped)
adoption_status: Exploratory
priority: P3
applicability:
- General
adopted_in: []
sources:
- supermemory-99-sota-blog.md
related_findings:
- file: typed-relationship-memory-graph.md
  rel: extends
- file: verbatim-storage-thesis-for-memory.md
  rel: contradicts
- file: triple-storage-memory-architecture.md
  rel: same-problem
- file: mongodb-single-store-polymorphic-evidence-memory.md
  rel: same-problem
- file: query-decomposition-sub-query-rrf-merge.md
  rel: extends
- file: ensemble-eval-majority-required-for-success.md
  rel: same-problem
- file: write-time-vs-query-time-synthesis-kb-poisoning.md
  rel: contradicts
proposals: null
date_discovered: '2026-04-23'
last_updated: '2026-05-24'
pipeline_status: classified
consumed_by: []
---

## What It Is

A memory-system architecture with three agent-driven stages, each replacing what a vector-RAG system would do with similarity search:

1. **Ingestion** — parallel LLM reader agents (Supermemory documents 3) extract memories across a fixed set of dimensions (6 in Supermemory: Personal Information, Preferences, Events, Temporal Data, Updates, Assistant Info). Each reader focuses on one dimension; outputs are atomic memory units rather than raw chunks.
2. **Retrieval** — specialized search agents (Supermemory documents 3) actively reason over the stored memory graph to produce candidate answer sets. Instead of "top-k nearest neighbors," each search agent can traverse typed relationships, follow temporal chains, or pursue counter-example searches. Multiple search agents run in parallel with different strategies.
3. **Answering** — an ensemble of reasoning paths generates candidate answers; an aggregation rule (majority vote, decision forest, union-of-successes) produces the final output.

Contrasts with:
- **Vector RAG** (`mem0`, Supermemory's pre-ASMR 85% configuration): embed, k-NN, rerank.
- **Single-store polymorphic** ([[mongodb-single-store-polymorphic-evidence-memory]], Memongo): raw turns + structured evidence in one collection, hybrid retrieval.
- **Verbatim storage** ([[verbatim-storage-thesis-for-memory]], MemPalace): exact words + semantic search, no LLM in retrieval path.
- **Triple-store extraction** ([[triple-storage-memory-architecture]], mem0): LLM extraction into graph + vector + relational.

The ASMR position: extend [[typed-relationship-memory-graph]] (Supermemory's own extraction approach) by replacing the retrieval path with active agent reasoning rather than similarity search. Contradicts [[verbatim-storage-thesis-for-memory]] on the "no LLM in retrieval path" claim — ASMR is maximally LLM-dependent throughout.

## Why It Matters

Completes a 4-point architectural design space for agent memory:

| Pole | Example | Storage Strategy | Retrieval Strategy |
|---|---|---|---|
| Multi-store extraction | mem0 | LLM-extracted structured facts | Multi-store merge |
| Single-store polymorphic | Memongo | Raw turns + evidence | $rankFusion hybrid |
| Verbatim | MemPalace | Exact text | Semantic + optional rerank |
| **Agentic** | **Supermemory ASMR** | **LLM-extracted typed relationships** | **LLM-driven reasoning** |

For MetaSystem's memory-architecture thinking: any future comparative analysis against Memongo or other memory backends needs to position against all four poles. ASMR is the high-cost / high-quality corner; verbatim is low-cost / surprisingly-high-quality; single-store polymorphic is the mid-path balance; extraction is the legacy approach most mature systems started from.

For MetaSystem's own use: unlikely to adopt ASMR directly — the per-query cost is prohibitive for a personal-scale system, and the governance is immature (no cost disclosures, sandbox-only). The pattern is more useful as a design reference: when does paying full LLM cost per retrieval make sense? Answer (from Supermemory): when the task is hard cross-session reasoning and the target is research-grade accuracy rather than cost-per-query.

## Why People Are Using It

Observed in [Supermemory's 99% SOTA ASMR blog post](https://supermemory.ai/blog/we-broke-the-frontier-in-agent-memory-introducing-99-sota-memory-system/) 2026-03-22 — see [[supermemory-99-sota-blog]] for the source and [[supermemory-analysis]] for structural context on the production Supermemory. Concrete configuration: Gemini 2.0 Flash for orchestration, GPT-4o-mini for the decision-forest variants, 8-variant ensemble (98.60%) and 12-variant decision forest (97.20%) reported.

The vendor labels the implementation as experimental and not production (per [[experimental-sandbox-labeling-discipline]]); it's explicitly framed as exploratory rather than shipping. Cost disclosures are absent — a notable gap per [[production-configuration-baseline-discipline]] — so direct comparative economics vs vector-RAG alternatives can't be computed from the source.

The architectural pattern is likely to spread even if Supermemory's specific implementation doesn't. Agent-driven retrieval is a generalization of the "search agent" idea in broader agent design (compare [[query-decomposition-sub-query-rrf-merge]] and Memongo's sub-query patterns). ASMR extends this from "decompose the query" to "decompose the retrieval process itself."

## Potential Alternatives

- **Vector RAG with reranking.** Standard industry baseline. Cheap, decent quality, predictable.
- **Verbatim storage + rerank** ([[verbatim-storage-thesis-for-memory]]). Surprisingly strong on retrieval recall; no LLM in path.
- **Single-store polymorphic** ([[mongodb-single-store-polymorphic-evidence-memory]]). Midway — extracts evidence but keeps raw turns accessible.
- **Query-decomposition hybrid** ([[query-decomposition-sub-query-rrf-merge]]). Multiple retrieval queries merged; simpler than ASMR's full agent pipeline.
- **Best-of-N retrievers with cheap picker.** Run N different retrieval strategies in parallel, use a cheap picker to pick one — simpler than ASMR, cheaper than full ensembles.

## Potential Improvements

- **Cost-to-quality Pareto reporting.** Publish (latency, tokens, accuracy) triples so readers can see where ASMR pays off vs vector RAG.
- **Agent specialization protocols.** What's the optimal set of reader/search dimensions? Supermemory uses 6/3/3; is this domain-tunable?
- **Fallback mechanism.** ASMR's failure mode is expensive-timeout; a fallback to vector RAG when ASMR exceeds a cost budget would make production-readiness plausible.
- **Per-query ensemble sizing.** Easy queries don't need 8 variants; hard queries might need 16. Dynamic ensemble sizing based on query-difficulty signals.
- **Graduated ASMR.** Start with 1 reader + 1 searcher + 1 answerer; scale up based on confidence.

## Potential Failure Modes

- **Cost explosion.** ~8-12 LLM calls per query (plus orchestration) makes per-query cost 10-20× vector RAG. Scales poorly for high-QPS workloads. Mitigation: graduated ASMR or fallback to cheaper paths.
- **Latency.** Parallel but still bounded by the slowest variant; 8-variant decision forest = 8 × per-call latency in worst case. Mitigation: aggressive timeouts + fallback retrieval.
- **Ensemble inflation.** Union-of-successes aggregation inflates reported accuracy relative to deployable accuracy ([[ensemble-eval-majority-required-for-success]]). Production use requires declared aggregation; real-world accuracy may be 10-20pp below reported.
- **Non-determinism.** Ensemble outputs vary run-to-run; hard to debug, hard to test. Mitigation: record per-query ensemble outputs for replay.
- **Opacity.** "The agents figured it out" is less explainable than "here are the top-5 retrieved chunks." For regulated domains (medical, legal, financial), this is disqualifying. Mitigation: mandatory logging of each agent's reasoning trace.
- **Lock-in to the vendor's specific agent topology.** 3 readers + 3 searchers + 8-12 variants is Supermemory's specific choice; the architectural pattern needs to be abstracted from the specific numbers before it's transferable.
