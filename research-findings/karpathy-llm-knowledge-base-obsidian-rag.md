---
name: Karpathy LLM Knowledge Base (Obsidian RAG Alternative)
summary: 'Andrej Karpathy''s approach: LLM ''compiles'' raw documents into a structured Markdown wiki (index, concept articles, cross-references) in an Obsidian vault. No vector DB needed under ~1000 docs.
  Four-phase cycle: ingest → compile (index + concepts) → query → enhance. Cole Medin adapts this for Claude Code session logs — self-evolving memory that compounds over time.'
implementation_notes: MetaSystem IS an Obsidian vault with this exact pattern emerging organically. The explicit compile step (LLM building index + concept pages from raw data) and session-log capture via
  hooks are directly actionable enhancements.
category: Memory Architecture
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- karpathys-obsidian-rag-claude-code.md
- self-evolving-claude-code-memory.md
proposals: null
date_discovered: '2026-04-07'
last_updated: 2026-04-08
related_findings:
  - file: "claudemd-as-knowledge-base-traversal-guide.md"
    rel: "same-problem"
  - file: "ace-agentic-context-engineering-rag-based.md"
    rel: "contradicts"
pipeline_status: "raw"
consumed_by: []
---
# Karpathy LLM Knowledge Base (Obsidian RAG Alternative)

## What It Is
Replace traditional RAG (vector DB + embeddings + retrieval) with an LLM-compiled Markdown wiki. Raw sources go into a raw/ folder. The LLM compiles index files (summaries as query entry points), concept articles (~100 articles, ~400K words), and auto-maintained cross-references. Query via file traversal, not vector search. Cole Medin's adaptation: feed Claude Code session logs as raw input instead of external articles, creating codebase-specific long-term memory that compounds with each session.

Karpathy frames the system as a software compiler pipeline: Source code (raw articles/session logs) → Compiler (LLM processing) → Executable/Wiki (queryable knowledge base with index.md, concepts/, connections/) → Test suite (health checks: gap detection, stale data, broken link repair) → Runtime (agent queries via index.md at session start). Cole Medin's internal adaptation captures every Claude Code session via three hooks (session_start, pre_compact, session_end) that produce structured summaries appended to daily-logs/, then a daily flush promotes concepts and connections to the wiki.

Claude's implementation bypasses the raw/ folder entirely, using only the processed/structured knowledge files for context — avoiding ingestion of unprocessed source material that would dilute retrieval quality.

Two-tier index system: master-index.md lists all wikis; per-wiki index lists articles within that wiki. This hierarchical navigation typically requires only 2-3 file reads instead of scanning everything. Wiki folder convention: wiki/concepts/, wiki/connections/, wiki/index.md. Knowledge linting is a CORE pipeline stage (stage 4 of 5 in the compiler analogy), not an optional improvement — it covers gap detection, stale data identification, broken link repair, and raw-vs-wiki discrepancy checks. Automated health checks for wiki consistency are already built into the pipeline (see "Test suite" stage above).

## Why It Matters
Solo devs and small teams (like MetaSystem's two-person team) don't need vector DB infrastructure. Obsidian's native graph view, Dataview queries, and wiki-link navigation provide the retrieval layer. Knowledge compounds — each query's output feeds back into the wiki, making the system smarter over time.

## Why People Are Using It
Karpathy's original system handles hundreds of documents effectively. Chase AI and Cole Medin demonstrate production use with Claude Code. Frank's World documents setup steps. The approach is especially appealing for teams already using Obsidian as their knowledge management tool.

## Potential Alternatives
Full RAG with vector DB (needed for 1000+ docs). Hybrid DuckDB + Obsidian. GraphRAG for relationship-heavy domains. Direct context injection for small document sets.

## Potential Improvements
Incremental compile — only process new or changed docs instead of full recompilation. Tiered compilation with different detail levels for different document types.

## Potential Failure Modes
Wiki quality degrades if LLM compilation isn't periodically supervised. Index can grow unwieldy without periodic pruning. Scale ceiling around ~1000 docs before vector search outperforms file traversal. Session log noise can pollute the knowledge base if not filtered.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[llm-compiled-knowledge-base-over-vector-rag.md]] in `extracts/patterns/`
