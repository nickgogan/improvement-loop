---
name: "File Search Outperforms RAG for Small Corpora"
summary: "For smaller knowledge bases, file search tools (grep, glob, file traversal) outperform traditional RAG (vector databases, semantic search, embedding pipelines). LlamaIndex study and coding agent ecosystem shift (Claude Code, Cursor) confirmed this in 2025. Semantic search remains superior for larger knowledge bases with thousands of documents where it is more accurate and cheaper at scale."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: P2
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "sdk-vs-framework-decision-ai-agents.md"
related_findings:
  - file: scale-threshold-heuristic-obsidian-vs-rag.md
    rel: same-problem
  - file: hybrid-retrieval-pattern-semantic-lexical-graph.md
    rel: same-problem
  - file: ace-agentic-context-engineering-rag-based.md
    rel: contradicts
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "structuring-agent-context.md"
  - "rules/default-to-file-search-before-rag.md"
tags:
  - "session-95-reextract"
---

## What It Is

A reversal in the default retrieval strategy for AI agents. In 2024, essentially every agent used semantic search (RAG) to access external knowledge. In 2025, the coding agent ecosystem demonstrated that file search tools -- grep, glob, file system traversal -- actually outperform RAG for smaller corpora. LlamaIndex conducted a study confirming this. Major coding agents (Claude Code, Cursor) stopped using vector databases entirely, relying instead on lexical search tools built directly into their SDKs.

The mechanism: for smaller document sets, the precision of exact text matching (grep) and the ability to navigate file structure (glob, directory traversal) eliminates the lossy compression inherent in embedding-based retrieval. No chunking strategy, no embedding model selection, no retrieval threshold tuning -- just direct text search.

However, the reversal is corpus-size-dependent. For larger knowledge bases with thousands of documents, semantic search remains more accurate and significantly cheaper than exhaustive file search. The compute cost of grep-scanning thousands of files exceeds vector similarity lookups.

## Why It Matters

The "RAG is dead" narrative is overstated but contains a valid core: the default assumption that every agent needs a vector database and embedding pipeline is wrong. For personal tools, small-team knowledge bases, and codebases, file search is both simpler and more effective. This shifts the default: start with file search, add semantic search only when corpus scale demands it.

For MetaSystem specifically, the IL knowledge base currently uses file-based navigation (grep, glob, Read) rather than RAG. This finding validates that approach at current KB scale. The threshold for migration would be reached if the KB grew to thousands of documents -- which is not imminent.

## Why People Are Using It

- Simpler infrastructure: no vector database, no embedding pipeline, no chunking strategy
- Higher accuracy for small corpora: exact text matching beats approximate vector similarity
- Built into SDK tooling: coding agent SDKs provide grep/glob/file-search out of the box
- Zero maintenance: no embedding model upgrades, no re-indexing, no retrieval threshold tuning
- Faster iteration: add a document and it's immediately searchable without ingestion

## Potential Improvements

- Hybrid tools that automatically route to file search or semantic search based on corpus size
- Smarter file search with fuzzy matching and ranking (not just grep)
- Benchmarks establishing the specific corpus-size crossover point where RAG outperforms file search

## Potential Failure Modes

- Scaling past the file-search threshold without adding semantic search -- slow degradation in retrieval quality
- Over-indexing on "RAG is dead" and removing semantic capabilities from agents that will eventually need them
- File search misses conceptually related content that doesn't share lexical terms (the core weakness vs. semantic search)
- Grep-heavy search patterns becoming expensive for large file systems without caching
