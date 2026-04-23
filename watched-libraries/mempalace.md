---
name: "MemPalace"
type: "watched-library"
repo_url: "https://github.com/MemPalace/mempalace"
description: "Local-first AI memory — verbatim-storage thesis with 96.6% LongMemEval R@5 using only ChromaDB defaults (zero LLM calls)"
spectrum_position: "evaluating"
what_we_use: "Verbatim-storage thesis, structured-index + unstructured-retrieval (wings/rooms/drawers + AAAK closets), background-hooks save model (Stop + PreCompact), AGENTS.md↔CLAUDE.md symlink, multi-harness plugin architecture, retraction log as governance artifact, tool-enforced dev/held-out split"
local_derivations: []
last_evaluated_version: "3.3.2 (2026-04-23)"
last_evaluated_date: "2026-04-23"
maintainer: "MemPalace (Milla Jovovich, Ben Sigman, Igor Lins e Silva, contributors)"
status: "active"
tags:
  - "memory"
  - "chromadb"
  - "context-engineering"
  - "mcp"
  - "benchmark-discipline"
  - "governance"
related_findings:
  - "retraction-log-as-governance-artifact.md"
  - "tool-enforced-dev-heldout-split.md"
  - "universal-harness-context-via-symlink.md"
  - "shared-instructions-multi-harness-plugin-wrappers.md"
  - "background-hooks-as-token-economy.md"
  - "verbatim-storage-thesis-for-memory.md"
  - "independent-convergence-retrieval-ceiling.md"
  - "declared-transformations-contract-conformance.md"
  - "impostor-domain-readme-callout.md"
related_sources: []
date_added: "2026-04-23"
---

## What It Does

Local-first AI memory that stores conversation history as verbatim text and retrieves it with semantic search — no summarization, no LLM-based extraction, no cloud dependency. The palace is structured: people/projects become *wings*, topics become *rooms*, verbatim text lives in *drawers*, and an AAAK-compressed index layer (closets) lets an LLM scan thousands of entries without reading each one. Knowledge graph is a local SQLite with temporal validity windows. Retrieval backend is pluggable; ChromaDB is the default. Benchmark claims: **96.6% R@5 on LongMemEval in raw mode with zero API calls**, 98.4% R@5 on a held-out 450-question split with hybrid heuristics, 100% with LLM rerank (withdrawn from headlines as teaching-to-the-test). 29 MCP tools. Two Claude Code hooks (Stop + PreCompact) move all memory operations into background execution, eliminating per-session token cost for memory bookkeeping. MIT licensed, Python 3.9+, ~49k GitHub stars at evaluation date (repo created 2026-04-05).

## What We Use From It

Candidate patterns for extraction (gate pending in analysis doc):

- **Verbatim-storage thesis** — counter-stance to mem0's extraction and adjacent to Memongo's single-store polymorphic evidence memory.
- **Background-hooks save model** — Stop + PreCompact hooks move memory save operations out of the chat window entirely ($1.13/session → $0 reported token-cost change).
- **AGENTS.md ↔ CLAUDE.md symlink** — universal-harness context pattern: one authored file, two harnesses read it.
- **Multi-harness plugin architecture** — `.claude-plugin/`, `.codex-plugin/`, `.agents/` wrap a single authored-once source (`mempalace/instructions/*.md`).
- **Retraction-and-correction log as first-class governance artifact** — `docs/HISTORY.md` captures dated public corrections, audit responses, impostor-domain warnings.
- **Tool-enforced dev/held-out split** — `benchmarks/lme_split_50_450.json` + CLI flags (`--dev-only` / `--held-out`) prevent overfitting at the tool layer.
- **Declared-transformations contract with conformance tests** (RFC 002) — turns "verbatim" from a social contract into a machine-verified property.

## Spectrum Rationale

Evaluating. The verbatim-storage thesis is architecturally oppositional to the dominant extraction-based approach (mem0, Mastra, Supermemory ASMR) and complements Memongo's single-store thesis. Its governance discipline — retraction log, tool-enforced benchmark split, self-disclosed teaching-to-the-test, negative-space contribution boundaries — is independently valuable as a research-findings source even if MemPalace itself isn't adopted as MetaSystem's memory layer. MetaSystem already uses Memongo for agent memory; MemPalace is a comparative reference, not a replacement candidate at this stage.

## Source Note (Correction to Prior Handoff)

The session-56 carry-forward referenced `mempalace.tech` as the benchmark domain. Per the repo's README scam-alert block and `docs/HISTORY.md` (2026-04-11 entry), **`mempalace.tech` is an impostor domain distributing malware**; the official domains are `github.com/MemPalace/mempalace`, `pypi.org/project/mempalace`, and `mempalaceofficial.com`. The prior scan's "Mampalace / MemPalace" leaderboard numbers were mined from the scam domain and from `vectorize.io`; the authoritative benchmark source is the repo itself (`benchmarks/BENCHMARKS.md`).

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-23 | 3.3.2 | Initial evaluation (session 57). Full 5-dimension `/repo-analyzer` pass; workflow-topology and cross-agent-protocol recorded as N/A (MemPalace is memory infrastructure, not an agent framework). Scam-domain correction logged. |
