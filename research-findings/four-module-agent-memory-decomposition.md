---
name: "Four-Module Decomposition of Agent Memory (Representation, Extraction, Retrieval, Maintenance)"
summary: |-
  Gives us a neutral frame for comparing any two memory systems — including our own KB — instead of
  arguing whole-architecture vs whole-architecture. Decomposes every agent memory system into four
  modules: representation/storage (what form memories take), extraction (how raw streams become
  memory primitives), retrieval/routing (how relevant memory is found), and maintenance (how the
  store evolves over time). Each module has a small enumerable design space, so systems become
  comparable point-by-point.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (empirical benchmarks)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "arxiv-agent-native-memory-system-survey.md"
related_findings:
  - file: "no-single-memory-architecture-workload-alignment.md"
    rel: "enables"
  - file: "converged-memory-substrate-vs-patchwork.md"
    rel: "same-problem"
  - file: "production-memory-architecture-spectrum.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-11"
last_updated: "2026-07-11"
---

## What It Is

An analytical decomposition (formally M_sys = ⟨R, S, Q, U⟩) from a data-management-perspective
evaluation of 12 agent memory systems:

- **Representation & storage (R)** — logical form (token sequences, graphs/trees, heterogeneous
  composites) and physical persistence (transient registers, specialized databases, multi-engine
  backends)
- **Extraction (S)** — how heterogeneous input streams become memory primitives: raw
  concatenation, schema-free semantic extraction, or schema-constrained structured extraction
- **Retrieval & routing (Q)** — native attention, semantic KNN, topological traversal, agentic
  routing (function calls / query expansion), or multi-stage hybrid execution
- **Maintenance (U)** — timestamp versioning, capacity-driven eviction, LLM-driven semantic
  consolidation, or continuous parametric optimization

## Why It Matters

The KB's memory findings are currently organized by whole architectures (verbatim vs extraction vs
converged vs tiered). Those poles conflate module choices: e.g., the verbatim-storage thesis is
really "raw-concatenation extraction + semantic KNN retrieval" — its storage and maintenance
choices are independent. The four-module frame lets us classify existing and future findings by
which module they actually make a claim about, and evaluate designs module-by-module against the
workload instead of adopting an architecture wholesale.

## Why People Are Using It

Proposed by Zhou et al., arXiv:2606.24775, "Are We Ready For An Agent-Native Memory System?"
(Tsinghua / SJTU database groups) — used as the organizing frame for benchmarking 12 memory
systems plus 2 baselines across 5 workloads / 11 datasets. Code and a curated agent-memory paper
list published at OpenDataBox/MemoryData.

## Potential Improvements

- Tag existing KB memory findings with the module(s) they address; use the frame in
  /ask-kb Builder-mode answers about memory design
- Extend the frame with a fifth concern the paper folds into retrieval — cross-agent sharing/
  scoping — which several KB findings treat as first-class

## Potential Failure Modes

- Module boundaries blur in agentic systems where an LLM performs extraction, retrieval, and
  maintenance in a single loop
- A taxonomy from a single survey may not survive contact with the next architecture generation
  (e.g., parametric/continual-learning memory sits awkwardly in all four modules)
