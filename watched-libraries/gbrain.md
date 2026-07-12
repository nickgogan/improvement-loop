---
name: "Gbrain"
type: "watched-library"
repo_url: "https://github.com/garrytan/gbrain"
description: |-
  Garry Tan's MIT-licensed open-source "second brain" for AI agents — markdown-in-git
  system of record synced to a derived Postgres layer, self-wiring typed knowledge
  graph (zero LLM calls), hybrid search, and a 30+-tool MCP server; the production
  brain behind his OpenClaw and Hermes deployments
spectrum_position: "study"
what_we_use: |-
  Nothing adopted yet — study target. Shipped instance of patterns already extracted
  as findings: markdown-git system of record with derived disposable DB, world-KB leg
  of the memory/wiki/world trichotomy, write-back discipline, stateful MCP subprocess
  vs CLI shell-out tradeoff
local_derivations: []
last_evaluated_version: "HEAD (2026-07-12)"
last_evaluated_date: "2026-07-12"
maintainer: "garrytan (Garry Tan, Y Combinator CEO)"
status: "active"
tags:
  - "memory"
  - "knowledge-base"
  - "vault-architecture"
  - "mcp"
  - "knowledge-graph"
related_findings:
  - "memory-wiki-world-kb-trichotomy.md"
  - "markdown-git-system-of-record-derived-disposable-db.md"
  - "stateful-mcp-subprocess-vs-cli-shell-out.md"
  - "write-back-discipline-memory-is-not-the-brain.md"
  - "query-shape-first-storage-design.md"
  - "evergreen-vs-volatile-ingestion-rule.md"
  - "per-folder-heterogeneous-retrieval-levels.md"
related_sources:
  - "give-your-ai-agent-a-second-brain-gbrain-hermes.md"
  - "every-level-of-a-claude-second-brain-explained.md"
date_added: "2026-07-12"
---

## What It Does

Open-source (MIT, TypeScript, ~26.0k stars as of 2026-07-12; open-sourced 2026-04-05)
world-knowledge base for AI agents, built and run in production by Garry Tan as "the
production brain behind my OpenClaw and Hermes deployments." Architecture: markdown files
in a git repo as the system of record, synced into Postgres for retrieval; a self-wiring
typed knowledge graph extracted with zero LLM calls; hybrid search (vector + keyword +
graph signals — vendor benchmark BrainBench claims P@5 49.1% / R@5 97.9%, a +31.4-point
P@5 lead over the same codebase with the graph layer disabled); and a synthesis layer that
returns cited prose plus explicit gap analysis rather than raw pages. Exposed as 30+ typed
tools over an MCP server (stdio and HTTP) for Claude Code, Codex, Cursor, and Claude
Desktop.

## What We Use From It

Study target — nothing adopted. It is the cleanest shipped instance of several findings
the KB already holds: the memory/wiki/world-KB boundary taxonomy (agent memory remembers
conversations; a world-KB knows your world), markdown-git as system of record with a
derived disposable database, the write-back discipline ("memory is not the brain"), and
the stateful-MCP-subprocess-vs-CLI-shell-out tradeoff. The parts to mine: the sync layer
between git and the derived DB, the zero-LLM-call typed-edge graph extraction, and the
typed-tool surface design.

## Spectrum Rationale

Study. The engine is itself a markdown-git knowledge system, so Gbrain is a direct
architectural comparison point rather than a dependency — its derived-DB retrieval layer
answers the "what would a query layer over our KB look like" question without us running
it. Benchmark numbers are vendor-published (BrainBench is Gbrain's own harness); treat as
claims, not corroborated measurements.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-07-12 | HEAD | Initial entry, Nick-approved (session 137). Repo verified via GitHub API: 26,015 stars, MIT, TypeScript. Cross-linked to the Tonbi's AI Garage Gbrain+Hermes walkthrough source and 7 existing findings. |
