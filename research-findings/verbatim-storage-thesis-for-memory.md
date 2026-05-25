---
name: Verbatim-Storage Thesis for Long-Term Agent Memory
summary: Store the actual conversation words; don't extract facts. On LongMemEval, a verbatim store with default ChromaDB embeddings and zero LLM calls reaches 96.6% R@5 — matching or beating every extraction-based
  system measured on the same benchmark. The field's assumption that an LLM must decide what to remember is the load-bearing error. 'The key insight is removal, not addition.'
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: null
applicability:
- General
adopted_in: []
sources: []
related_findings:
- file: mongodb-single-store-polymorphic-evidence-memory.md
  rel: same-problem
- file: triple-storage-memory-architecture.md
  rel: contradicts
- file: typed-relationship-memory-graph.md
  rel: same-problem
- file: agentic-search-memory-retrieval-architecture.md
  rel: contradicts
- file: subagent-persistent-memory-directory.md
  rel: same-problem
- file: bounded-tiered-memory-inference-driven-curation.md
  rel: contradicts
proposals: null
date_discovered: '2026-04-23'
last_updated: '2026-05-24'
pipeline_status: raw
consumed_by: []
---

## What It Is

A third architectural pole in the agent-memory design space, distinct from both extraction-based (mem0, Mastra, Supermemory ASMR) and single-store-polymorphic (Memongo) approaches:

- **Never summarize, paraphrase, or lossy-compress user content.** The system stores the exact words the user said.
- **Retrieval is semantic search over raw text.** Default embeddings (e.g., ChromaDB's all-MiniLM-L6-v2) applied to verbatim session chunks, no LLM in the retrieval path.
- **Structure is scoping, not extraction.** Metadata filters (wings = people/projects, rooms = topics, drawers = verbatim chunks) keep retrieval predictable when a palace holds many unrelated subjects. They do not replace the content.
- **Optional LLM rerank improves ceiling.** Post-retrieval Haiku or Sonnet rerank lifts the score from 96.6% to 99.4%, but the baseline works without any LLM.

The architectural claim, phrased in the benchmark doc: "Every competitive memory system uses an LLM to manage memory... They all start from the assumption that you need AI to decide what to remember. Raw verbatim text with good embeddings is a stronger baseline than anyone realized."

Positioning in the architectural triangle:

| Pole | Example | Storage | Extraction | Retrieval |
|---|---|---|---|---|
| Multi-store extraction | mem0 | Vector + graph + relational | LLM-driven fact extraction | Multi-store merge |
| Single-store polymorphic | Memongo | One MongoDB collection, polymorphic $jsonSchema | Structured-fact extraction at write time | $rankFusion hybrid |
| **Verbatim** | **MemPalace** | **One ChromaDB collection, raw text** | **None** | **Semantic search + optional rerank** |

## Why It Matters

The dominant assumption in 2026 agent-memory frameworks is that long-term memory requires an LLM to decide what to remember — extract facts, discard the rest, store the structured residue. This is expensive (API calls on every write), lossy (extraction throws away the original context of *why* something was said), and error-prone (when the extractor extracts wrong, the memory is gone). The verbatim thesis says: keep all the words, search them well, and you match or beat the extractor-based systems at significantly lower cost.

For MetaSystem's active Memongo work: Memongo's thesis is single-store + structured evidence extraction. MemPalace's thesis is verbatim + no extraction. These are different positions on the extraction axis; both are oppositional to mem0's triple-store extraction. Registering MemPalace as a distinct pole completes the architectural triangle for any future design round. Directly relevant to Nick's ongoing Memongo iteration.

The benchmark claim (96.6% R@5 on LongMemEval, zero LLM) is independently reproducible from the repo. Retrieval recall is not end-to-end QA accuracy — a separate measurement would be needed for that comparison — but within the retrieval-recall metric, the verbatim baseline is as strong as any system published on the same metric.

## Why People Are Using It

Observed in [MemPalace](https://github.com/MemPalace/mempalace) 3.3.2 — see [[mempalace-analysis]] for structural details. The repo explicitly states the design principle in CLAUDE.md: "Verbatim always — Never summarize, paraphrase, or lossy-compress user data." The CONTRIBUTING document rejects any PR that violates this invariant. Benchmark reproducibility is documented in `benchmarks/BENCHMARKS.md` and `benchmarks/README.md`; per-question result JSONLs are committed for audit.

MemPalace launched 2026-04-05 and reached ~49k GitHub stars within three weeks — evidence of strong community resonance with the verbatim framing. The architectural thesis and the benchmark discipline are separable; even if the benchmark numbers are later adjusted (as they partially have been — see [[retraction-log-as-governance-artifact]]), the thesis itself stands as a design-space option.

## Potential Alternatives

- **LLM fact extraction (mem0)** — an LLM reads each session and extracts structured facts. When extraction is correct, lookups are fast. When it's wrong, the memory is lost. Reported ~30–45% on ConvoMem (from MemPalace's comparison table).
- **Observational extraction (Mastra)** — GPT-5-mini observes conversations and writes structured memory. Reported 94.87% QA accuracy on LongMemEval. Requires ongoing LLM cost.
- **Agentic multi-pass search (Supermemory ASMR)** — an ensemble of LLMs runs multi-pass search passes. Reported ~99% QA accuracy (experimental). High LLM cost, non-deterministic.
- **Polymorphic evidence storage (Memongo)** — raw turns + extracted evidence coexist in one collection. Preserves context while providing structured retrieval surfaces.

## Potential Improvements

- **Hybrid verbatim + thin extraction.** MemPalace's hybrid_v3 added 16 regex patterns for preference-expression detection (not full LLM extraction, but pattern-based synthesis). This lifted scores by 0.6pp. A middle ground between pure verbatim and LLM extraction is worth mapping.
- **Embedding-model sensitivity.** The 96.6% result uses ChromaDB's default all-MiniLM-L6-v2. Better embedders (bge-large) may lift the verbatim baseline further without adding any extraction — separating "how much is the heuristics doing" from "how much is the embedder."
- **Cross-benchmark validation.** MemPalace's strongest benchmark is LongMemEval retrieval recall; its weakest (MemBench `noisy` at 43.4%, `post_processing` at 56.6%) are reasoning-heavy categories where retrieval alone is insufficient. The verbatim thesis needs testing on benchmarks where retrieval is the bottleneck vs where reasoning is.

## Potential Failure Modes

- **Retrieval recall ≠ end-to-end answer quality.** A system can have 100% retrieval recall and 40% QA accuracy. The verbatim thesis wins on retrieval; it has not been evaluated head-to-head on end-to-end QA accuracy against LLM-extractor systems at the same benchmark configuration.
- **Scaling with corpus size.** 500-question benchmarks don't stress-test retrieval across 1M+ drawer corpora. Verbatim storage grows linearly with input; extraction compresses. At very large scale, extraction's lossy compression may outperform verbatim's linear growth.
- **Preference/inference-heavy workloads.** When the answer isn't in any session verbatim — e.g., an inference across multiple preference hints — retrieval of the right set of sessions is not sufficient; a reasoner must synthesize. Verbatim storage helps but doesn't close the gap alone.
- **The "honest" number is smaller than the headline.** MemPalace's public 96.6% is retrieval recall; competitor "99%" numbers are often end-to-end QA accuracy. These are different metrics. Direct numeric comparison without labeling is the non-equivalent-comparison anti-pattern that MemPalace itself retracted (see [[retraction-log-as-governance-artifact]]).
