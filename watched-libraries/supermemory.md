---
name: "Supermemory"
type: "watched-library"
repo_url: "https://github.com/supermemoryai/supermemory"
description: "Cloud-capable memory + context engine built as a Turborepo Bun monorepo, deployed on Cloudflare Workers. Extraction-based memory with typed-relationship evolution graph (updates/extends/derives), static+dynamic user profiles, and an open-source cross-provider benchmarking harness (MemoryBench)."
spectrum_position: "evaluating"
what_we_use: "Typed-relationship memory graph (updates/extends/derives), static+dynamic user profile composition, memory-vs-RAG framing, content-derived temporal expiration, hierarchical container-tag multi-tenancy, cross-provider benchmarking pattern (MemoryBench), SKILL-as-package-export with architecture-first references/"
local_derivations: []
last_evaluated_version: "latest (2026-04-23)"
last_evaluated_date: "2026-04-23"
maintainer: "Supermemory Inc. (Soham Daga, Sreeram Sreedhar, Dhravya Shah; community contributors)"
status: "active"
tags:
  - "memory"
  - "cloud"
  - "mcp"
  - "multi-tenant"
  - "benchmark-framework"
  - "typescript"
related_findings:
  - "typed-relationship-memory-graph.md"
  - "static-dynamic-profile-composition.md"
  - "memory-vs-rag-product-distinction.md"
  - "content-derived-temporal-expiration-contradiction-resolution.md"
  - "cross-provider-benchmarking-framework.md"
  - "hierarchical-container-tag-multi-tenancy.md"
  - "skill-as-package-export-with-references.md"
related_sources: []
date_added: "2026-04-23"
---

## What It Does

Cloud-capable memory infrastructure for AI agents, built as a Turborepo Bun monorepo (TypeScript-dominant) and deployed on Cloudflare Workers (Durable Objects for MCP session state, Hyperdrive for DB, KV, Workflows, cron every 4 hours). Primary architecture components: (1) Memory Engine that extracts facts from conversations and builds a typed-relationship graph (Updates / Extends / Derives); (2) User Profiles combining `static` (permanent) facts with `dynamic` (recent) context in a single ~50ms API call; (3) Hybrid Search that runs RAG and Memory in one query; (4) Real-time Connectors for Google Drive / Gmail / Notion / OneDrive / GitHub / Web Crawler; (5) Multi-modal extractors for PDFs / images (OCR) / videos (transcription) / code (AST-aware chunking). Ships an open-source cross-provider benchmarking framework (MemoryBench — `npx skills add supermemoryai/memorybench` → `/benchmark-context`) for head-to-head comparison of memory providers including competitors. Plugin ecosystem lives in separate repos (`claude-supermemory`, `openclaw-supermemory`, `opencode-supermemory`, `hermes-agent`). ~22k GitHub stars, MIT licensed. Claims #1 on LongMemEval, LoCoMo, and ConvoMem (LongMemEval 81.6% headlined; the ASMR experimental variant reports ~99% QA accuracy separately).

## What We Use From It

Candidate patterns for extraction (gate pending in analysis doc):

- **Typed-relationship memory graph** — three named relationships (updates/extends/derives) for how memories evolve.
- **Static + dynamic profile composition** in a single call — splits identity context from state context at the storage API.
- **Memory vs RAG as product distinction** — explicit framing ("memory tracks facts about users; RAG retrieves chunks").
- **Content-derived temporal expiration + automatic contradiction resolution** — third memory-decay strategy (beyond importance-based and surprisal-based).
- **Cross-provider benchmarking framework** — MemoryBench as a competitor-inclusive trust mechanism.
- **Hierarchical container-tag multi-tenancy** with scope-at-query-time selection.
- **SKILL-as-package-export** with architecture-first `references/` directory.

## Spectrum Rationale

Evaluating. Supermemory is architecturally opposite to MemPalace (extraction vs verbatim) and distinct from Memongo (typed-relationship graph + cloud-capable SaaS vs single-store MongoDB-native). Cross-compares well against both. MetaSystem does not need to adopt Supermemory directly — Memongo is the active memory layer — but the memory-architecture patterns and the cross-provider benchmarking framework are independently valuable extractions.

## Architectural Contrasts (vs MemPalace, Memongo)

| Dimension | Supermemory | MemPalace | Memongo |
|---|---|---|---|
| Storage strategy | Typed-relationship graph over extracted facts | Verbatim text in ChromaDB | Single MongoDB collection, polymorphic $jsonSchema |
| LLM dependency | Required at write time (extraction) | Optional (rerank) | Optional (dreamer consolidation) |
| Deployment | Cloud-first (Cloudflare Workers) | Local-first, zero cloud | Self-hosted |
| Multi-tenancy | Container tags with hierarchy | Single-user (wings/rooms) | Per-collection scoping |
| Plugin distribution | Separate repos per harness | In-tree plugin directories | N/A (library only) |
| Cross-provider eval | MemoryBench (includes competitors) | Own benchmarks with retraction log | Benchmark operating contract |

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-23 | latest (monorepo, no single version tag) | Initial evaluation (session 57). Full 5-dimension `/repo-analyzer` pass; workflow-topology recorded as N/A (library), cross-agent-protocol recorded as Low (shared-memory coordination via container tags). Seven finding candidates surfaced; promotion pending Nick review. |
