---
name: "MongoDB Single-Store Polymorphic Evidence Memory"
summary: "Memongo stores all agent memory evidence types — conversation turns, session evidence, userfact evidence, QA evidence — in one `chunks` collection using MongoDB's `$jsonSchema` oneOf polymorphic validator. Total surface: 29 collections, 84 standard indexes, 14 search indexes. Explicit architectural claim: 'One database, one collection for all evidence types, one retrieval authority' — counter-stance to multi-store architectures like mem0's vector + graph + SQLite split."
implementation_notes: "Evaluate for Memongo improvement: does single-collection polymorphism scale beyond the current benchmark? Polymorphic schemas complicate per-type index tuning and migration. The architectural tradeoff is operational simplicity (one backup, one query plane, one consistency boundary) vs. per-type optimization flexibility."
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
  - file: triple-storage-memory-architecture.md
    rel: contradicts
  - file: four-layer-enterprise-memory-stack.md
    rel: same-problem
  - file: production-memory-architecture-spectrum.md
    rel: same-problem
  - file: agent-memory-architecture-multi-agent-layered.md
    rel: same-problem
  - file: verbatim-storage-thesis-for-memory.md
    rel: same-problem
  - file: typed-relationship-memory-graph.md
    rel: same-problem
  - file: agentic-search-memory-retrieval-architecture.md
    rel: same-problem
  - file: subagent-persistent-memory-directory.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-27"
pipeline_status: synthesized
consumed_by:
  - "session-persistence-and-memory.md"
---

## What It Is

Memongo stores every form of long-term memory evidence — raw conversation turns, synthesized session evidence, extracted user facts, and generated QA pairs — in a single MongoDB `chunks` collection. The collection uses `$jsonSchema` with a `oneOf` validator so each document is polymorphic to its evidence type while sharing storage, indexing, and query surfaces.

The repository's explicit architectural framing: **"One database, one collection for all evidence types, one retrieval authority."**

Total storage surface across the system: 29 MongoDB collections, 84 standard indexes, 14 Atlas Search / vector search indexes. The `chunks` collection is the retrieval focal point; surrounding collections handle metadata (access tracking, consolidation state, reasoning chains).

## Why It Matters

The dominant pattern in 2026 agent-memory frameworks (mem0, Letta, Zep, layered enterprise stacks) is to split storage across specialized substrates — vector store for similarity, graph store for relationships, relational store for metadata. Memongo's counter-stance is that a single well-tuned document database with hybrid search primitives can serve all four retrieval modes, and that the operational cost of multi-store architectures (consistency, ops burden, provider lock-in) outweighs per-mode optimization gains for most agents.

The claim is testable: if Memongo matches or beats multi-store frameworks on a standardized benchmark (LongMemEval-S, 98.1% R@5 per the README) while running on one DB, the operational-simplicity argument strengthens.

## Why People Are Using It

Observed in [Memongo](https://github.com/romiluz13/Memongo) (MIT, ~22k commits, sole maintainer). README claims LongMemEval-S R@5 98.1%, R@10 98.9%, Hit Rate 98.8%, NDCG@10 0.889 on 500 scenarios / 23,867 sessions / 246,750 turns. The single-collection claim is part of the repo's explicit differentiator framing. Currently pre-audience (1 GitHub star at extraction time), so adoption evidence is limited to the author's own production use.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Vector + graph + relational split (mem0) | Three specialized stores with abstract provider interfaces | When relationship traversal is a dominant query mode or team has per-store ops expertise |
| Layered enterprise memory stack | Distinct tiers per memory type (session, entity, semantic, procedural) | When regulatory boundaries require physical separation between memory types |
| Flat-file markdown memory (CLAUDE.md / PARA) | No database; agent reads/writes files | When deployment simplicity and transparency trump scale |

## Potential Improvements

- Contradiction handling is not detailed in the README — single-collection polymorphism makes cross-type contradiction detection easier in principle; explicit implementation would be a differentiator.
- Per-type index tuning within a polymorphic collection is non-trivial; benchmarks on heterogeneous workloads (not just LongMemEval-S) would clarify whether specialized indexes per evidence type are necessary.
- A formal comparison to mem0 on the same LongMemEval-S benchmark would settle the single-store vs. multi-store debate empirically.

## Potential Failure Modes

- **Per-type index contention** as collections grow — one query's optimal index shape may conflict with another's, forcing index bloat.
- **Migration friction** — schema changes to one evidence type trigger validator updates that affect all types in the collection.
- **Query plan unpredictability** — polymorphic `oneOf` validation interacts with the aggregation planner in ways that can surprise under load.
- **Single point of failure** — one DB outage takes down all memory surfaces simultaneously, vs. multi-store graceful degradation.
- **Benchmark-overfit risk** — LongMemEval-S performance does not guarantee the single-store architecture dominates on open-ended multi-session agent workloads.
