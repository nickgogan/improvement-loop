---
name: "Memongo — MongoDB-Native Long-Term Memory for AI Agents (GitHub)"
source_type: "Documentation"
status: "Done"
key_takeaways: "MongoDB-only agent memory stack: single chunks collection with polymorphic schema stores turns + session/userfact/QA evidence across 29 collections, 84 standard indexes, 14 search indexes. Retrieval combines $vectorSearch + Atlas Search via $rankFusion/$scoreFusion, with query decomposition and RRF at query time and post-retrieval scoring (keyword 0.30, temporal 0.40, entity 0.40, quoted phrase 0.60). LongMemEval-S: R@5 98.1%, R@10 98.9%, Hit Rate 98.8% using exact $vectorSearch (zero ANN approximation error). Consolidation via 'Dreamer' agent; importance-based decay (not time-TTL); surprisal-based novelty detection. 48 MCP tools expose the engine."
relevance: "High"
added_by: "Nick"
tags:
  - "memory"
  - "context-engineering"
  - "orchestration"
  - "evaluation"
  - "mcp"
  - "mongodb"
url: "https://github.com/romiluz13/Memongo"
authority:
  - "memongo-romiluz13.md"
findings:
  - "mongodb-single-store-polymorphic-evidence-memory.md"
  - "rank-fusion-hybrid-retrieval-mongodb-atlas.md"
  - "query-decomposition-sub-query-rrf-merge.md"
  - "post-retrieval-reranking-weighted-signal-composition.md"
  - "importance-based-decay-permanent-exemption.md"
  - "surprisal-novelty-as-memory-write-gate.md"
date_added: "2026-04-20"
date_processed: "2026-04-20"
date_published: "2026-03-24"
---

# Memongo — MongoDB-Native Long-Term Memory for AI Agents

MongoDB-native long-term AI memory framework authored by `romiluz13`. MIT licensed, ~22k commits, 1 GitHub star at time of extraction.

## Scope of Extraction

Nick has built Memongo and framed the intake as a search for improvement ideas. The README is the primary evidence surface. The following README claims were extracted verbatim for KB findings:

- **Architecture:** Single `chunks` collection with polymorphic `$jsonSchema oneOf` validator stores conversation turns, session evidence, userfact evidence, and QA evidence. 29 collections, 84 standard indexes, 14 search indexes total.
- **Retrieval:** `$vectorSearch` + auto-embed (Voyage 4 Large), Atlas `$search`, fused via `$rankFusion` / `$scoreFusion`; `$vectorSearch exact:true` for benchmark runs.
- **Ingestion enrichment:** GPT-4-mini fact extraction, QA pair generation, session evidence synthesis.
- **Query-time:** Query decomposition into sub-queries with RRF merge.
- **Reranking weights:** keyword overlap 0.30, temporal proximity 0.40, entity name 0.40, quoted phrase 0.60.
- **Consolidation:** "Dreamer" agent at `mongodb-consolidator.ts` → `POST /v1/consolidate`.
- **Decay:** Importance-based via `computeImportanceDecay()`; permanent/ongoing exempt. No wall-clock TTL.
- **Novelty:** Surprisal-based novelty detection at `mongodb-novelty.ts`.
- **Benchmark:** LongMemEval-S, 500 scenarios, 23,867 sessions, 246,750 turns. R@5 98.1% (baseline 73.4%, +24.7pp), R@10 98.9%, NDCG@10 0.889, Hit Rate 98.8%. Per-category: single-session-assistant 100% (56 cases), multi-session 85.6% (133 cases), temporal-reasoning 84.0% (133 cases).
- **Integration:** TypeScript client, MCP server (stdio-over-HTTP, 48 tools), Vercel AI SDK tool helpers.

## Items Flagged for Future Scans

- README does not reference Mampalace or Supermemory — Nick's cited "92% raw / Mampalace 96.6% / Supermemory 70%" numbers came from an external leaderboard not linked in the repo. Locate and process that leaderboard source in a future scan.
- `PRODUCTION-READY.md`, `docs/benchmarks/benchmark-operating-contract.md`, and `docs/platform/self-host.md` are referenced but not in the README body. Worth a Pass 2 deep-dive once Memongo is added to watched-libraries.
- Companion repositories for the benchmark harness (if any) not yet located.
