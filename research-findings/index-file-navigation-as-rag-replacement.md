---
name: Index-File Navigation as RAG Replacement
summary: Using an LLM-maintained index.md file for natural language navigation of a knowledge base instead of vector databases and semantic search pipelines. The LLM auto-maintains the index, and queries
  start with file traversal rather than embedding lookup.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
- S3 (Claude Code Build)
adopted_in: []
sources:
- self-evolving-claude-code-memory.md
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
related_findings:
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: contradicts
- file: pointers-over-copies-in-context-files.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
---

# Index-File Navigation as RAG Replacement

## What It Is
Instead of building a vector DB + embedding pipeline for knowledge retrieval, the LLM maintains an index.md that maps the entire knowledge base structure. Agents navigate by reading index.md first, then traversing to relevant concept files via wiki-links. Karpathy quote: "I thought I had to reach for fancy RAG, but the large language model has been pretty good about auto-maintaining index files."

## Why It Matters
Eliminates the vector DB dependency for small-to-medium knowledge bases (<1000 docs). Simpler infrastructure, no embedding costs, no retrieval tuning. Works naturally with Obsidian vaults.

## Why People Are Using It
Karpathy's system handles hundreds of documents effectively. Cole Medin and Chase AI demonstrate production use with Claude Code. The approach leverages LLMs' existing ability to navigate structured text.

## Potential Alternatives
Full RAG with vector DB (needed for 1000+ docs). Hybrid approaches (DuckDB + Obsidian). GraphRAG for relationship-heavy domains.

## Potential Improvements
Hierarchical indices for larger vaults. Health checks for index staleness and broken links. Automated index rebuild triggered by significant content changes.

## Potential Failure Modes
Scale ceiling around ~1000 docs before vector search outperforms. Index can grow unwieldy without pruning. LLM may miss relevant files if index descriptions are vague.
