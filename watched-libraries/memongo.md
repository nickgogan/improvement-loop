---
name: "Memongo"
type: "watched-library"
repo_url: "https://github.com/romiluz13/Memongo"
description: "MongoDB-native long-term memory framework for AI agents"
spectrum_position: "evaluating"
what_we_use: "Single-store polymorphic memory architecture, MongoDB Atlas native hybrid retrieval ($rankFusion/$scoreFusion), query decomposition + RRF, weighted-signal post-retrieval reranking, importance-based decay with permanent exemption, surprisal-based novelty write gate, 'Dreamer' consolidation agent, 48-MCP-tool surface"
local_derivations: []
last_evaluated_version: "latest (2026-04-20)"
last_evaluated_date: "2026-04-20"
maintainer: "romiluz13"
status: "active"
tags:
  - "memory"
  - "mongodb"
  - "context-engineering"
  - "mcp"
related_findings:
  - "mongodb-single-store-polymorphic-evidence-memory.md"
  - "rank-fusion-hybrid-retrieval-mongodb-atlas.md"
  - "query-decomposition-sub-query-rrf-merge.md"
  - "post-retrieval-reranking-weighted-signal-composition.md"
  - "importance-based-decay-permanent-exemption.md"
  - "surprisal-novelty-as-memory-write-gate.md"
  - "structured-fact-extraction-from-conversations.md"
  - "dreaming-memory-consolidation.md"
related_sources:
  - "memongo-mongodb-native-agent-memory-github.md"
date_added: "2026-04-20"
---

## What It Does

MongoDB-native long-term memory framework for AI agents. Single `chunks` collection with polymorphic `$jsonSchema` oneOf validator stores conversation turns, session evidence, userfact evidence, and QA evidence. 29 collections, 84 standard indexes, 14 search indexes total. Retrieval combines `$vectorSearch` (Voyage 4 Large auto-embed) with Atlas `$search` via `$rankFusion` / `$scoreFusion`, fronted by query decomposition (GPT-4-mini sub-query rewrites + RRF merge) and post-retrieval reranking with explicit weights (keyword 0.30, temporal 0.40, entity 0.40, quoted phrase 0.60). Consolidation via "Dreamer" agent (`mongodb-consolidator.ts` → `POST /v1/consolidate`). Decay is importance-based with permanent/ongoing exemption. Novelty gated at write time via `mongodb-novelty.ts` (surprisal). LongMemEval-S claims: R@5 98.1%, R@10 98.9%, Hit Rate 98.8%, NDCG@10 0.889 using `$vectorSearch exact:true` (zero ANN approximation error for benchmark runs). Integration via TypeScript client, MCP server (stdio-over-HTTP, 48 tools), Vercel AI SDK tool helpers. MIT licensed. Pre-audience (1 GitHub star at date of add) but ~22k commits from sole maintainer.

## What We Use From It

Nick has adopted Memongo as his agent memory layer and is iterating on it. MetaSystem tracks it as a live system whose improvement is directly in-scope.

Specific patterns extracted into the KB (see related_findings):
- Single-store polymorphic evidence memory (counter-stance to mem0's triple-store split)
- MongoDB Atlas-native rank fusion hybrid retrieval
- Query decomposition + RRF merge at query time
- Weighted-signal post-retrieval reranking (interpretable alternative to neural rerankers)
- Importance-based decay with permanent/ongoing exemption
- Surprisal-based novelty gating at write time
- Benchmark discipline: `$vectorSearch exact:true` for zero ANN noise

## Spectrum Rationale

Evaluating → likely moving to "wholesale" or "thin-wrapper" once Nick's own Memongo instance stabilizes. The architectural thesis (one database, one collection, one retrieval authority) is the key property worth tracking against the dominant multi-store pattern (mem0 / Letta / layered enterprise stacks).

## Improvement Surfaces Identified in Session 45

The README intake surfaced several areas worth investigating for Memongo itself:

1. **Contradiction handling** — README doesn't detail how Memongo handles "User said A" followed by "User said not-A." Surprisal novelty catches redundant agreement but not direct contradiction.
2. **Importance score provenance** — how is importance computed, and is it recomputed or fixed at write time?
3. **Decomposition-model choice** — GPT-4-mini for sub-query rewrites; multi-hop/temporal-reasoning is Memongo's weakest LongMemEval-S category at 84.0% — a larger decomposer may help.
4. **Reranker weight sensitivity** — weights (0.30/0.40/0.40/0.60) appear hand-tuned; publishing a LongMemEval-S sensitivity sweep would strengthen the evidence.
5. **Per-type index tuning** in a polymorphic `oneOf` collection is non-trivial — benchmarks outside LongMemEval-S would clarify.
6. **Benchmark comparison gap** — Nick cited external figures (Mampalace 96.6%, Supermemory 70%) not present in the README. Locate and process the leaderboard source.

## Deferred for Future Scan

- `docs/benchmarks/benchmark-operating-contract.md`, `PRODUCTION-READY.md`, `docs/platform/self-host.md` — referenced in the repo but not in the README body. Worth a Pass 2 extraction via `/repo-analyzer`.
- Companion benchmark-harness repository, if it exists as a separate project.
- Mampalace and Supermemory repositories / leaderboards for comparison.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-20 | latest | Initial evaluation. Session 45 intake extracted 6 net-new findings + updated 3 existing (structured-fact-extraction, dreaming-memory-consolidation, trajectory-engineering) with Memongo evidence. Nick explicitly requested the repo be added to watched-libraries. |
