---
notion_id: 32b1e08b-9b34-811a-8956-c76647e0212a
name: Hybrid Retrieval Pattern (Semantic + Lexical + Graph)
summary: 'Three complementary retrieval modes used together: Cursor semantic search (embedding-based, 12.5-23.5% accuracy gain), Claude Code lexical search (grep/glob for exact matches), and Obsidian MCP
  graph traversal (wikilink-based, N-level deep for relationship queries).'
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- march-18-agent-memory-architecture-research.md
- sdk-vs-framework-decision-ai-agents.md
proposals: null
date_discovered: '2026-03-18'
last_updated: '2026-07-12'
related_findings:
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
- file: rank-fusion-hybrid-retrieval-mongodb-atlas.md
  rel: extended-by
- file: query-decomposition-sub-query-rrf-merge.md
  rel: extended-by
- file: post-retrieval-reranking-weighted-signal-composition.md
  rel: extended-by
- file: agentic-rag-multi-strategy-retrieval-2026.md
  rel: extended-by
- file: file-search-outperforms-rag-for-small-corpora.md
  rel: same-problem
- file: curated-spine-plus-rag-hybrid-query-router.md
  rel: same-problem
- file: markdown-git-system-of-record-derived-disposable-db.md
  rel: enabled-by
- file: per-folder-heterogeneous-retrieval-levels.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
---
# Hybrid Retrieval Pattern (Semantic + Lexical + Graph)

## What It Is
This pattern defines how agents find information inside a vault by routing queries to one of three retrieval modes: semantic search (Cursor/Turbopuffer, embedding-based) for fuzzy or conceptual queries; lexical search (Claude Code grep/glob) for exact term or pattern matches; and graph traversal (Obsidian MCP, wikilink-based) for relationship and context queries spanning N levels of depth. Each mode is exposed as a distinct tool definition.

## Why It Matters
No single retrieval method covers all query types well. Semantic search misses exact strings; grep misses conceptual synonyms; neither captures multi-hop relationships between notes. Combining all three ensures agents can find information regardless of how the query is framed or where relevant content lives.

## Why People Are Using It
Practitioners have documented the accuracy gains from semantic retrieval (12.5-23.5% improvement over lexical-only baselines) and the relationship-discovery value of graph traversal in knowledge management systems. The pattern is gaining traction as vaults grow too large for any single retrieval mode.

**2026 update (SDK vs Framework analysis):** LlamaIndex study confirmed file search outperforms RAG for smaller corpora. Coding agents (Claude Code, Codex) switched from vector databases to grep/file search for code retrieval. The emerging 2026 middle ground is "agentic RAG" — the agent dynamically chooses between semantic search, grep, keyword search, and graph RAG depending on the query type. For larger knowledge bases (thousands of documents), semantic search remains more accurate and cheaper than brute-force file search. Practitioners report using both built-in file search capabilities AND custom RAG (via skills and MCP servers) in the same agent, reinforcing the hybrid pattern rather than picking one mode.

## Potential Improvements
A meta-retriever layer that classifies the query type and automatically selects the appropriate mode (or fan-out across all three) would reduce the need for explicit routing rules and improve agent autonomy. Scoping rules per retrieval mode would also help contain result sets.

## Potential Failure Modes
Over-linking in Obsidian creates a dense, noisy graph where traversal returns too many tangentially related nodes, degrading precision. Without a vault schema enforcing frontmatter and linking conventions, the graph retrieval mode degrades into an unstructured crawl.
