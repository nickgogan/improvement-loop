---
name: "Agentic RAG: Agent-Selected Multi-Strategy Retrieval"
summary: "The 2026 middle ground between 'RAG is dead' and traditional semantic-search-only RAG: give the agent the ability to perform multiple retrieval strategies (semantic search, grep/keyword search, graph RAG) and let it choose per query. The agent becomes the retrieval orchestrator rather than being locked into a single strategy."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "sdk-vs-framework-decision-ai-agents.md"
related_findings:
  - file: hybrid-retrieval-pattern-semantic-lexical-graph.md
    rel: extends
  - file: file-search-outperforms-rag-for-small-corpora.md
    rel: same-problem
  - file: rank-fusion-hybrid-retrieval-mongodb-atlas.md
    rel: same-problem
  - file: ace-agentic-context-engineering-rag-based.md
    rel: same-problem
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "structuring-agent-context.md"
tags:
  - "session-95-reextract"
---

## What It Is

Agentic RAG is the convergence point between two extremes: the 2024 default of semantic-search-for-everything and the 2025 counter-narrative that file search replaces RAG. Rather than hardcoding a single retrieval strategy, the agent is given multiple retrieval tools and autonomously selects the best strategy per query.

The retrieval toolkit typically includes:
- **Semantic search** -- embedding-based vector similarity for conceptual/fuzzy queries
- **Lexical search** -- grep, keyword matching for exact terms, identifiers, error messages
- **Graph RAG** -- relationship traversal for connected knowledge, especially across large codebases or multi-project systems
- **File system navigation** -- glob, directory listing for structural queries ("find all configs")

The agent decides which strategy (or combination) to use based on the query type. A search for "how does authentication work" routes to semantic search. A search for "ERROR_CODE_1234" routes to grep. A search for "what depends on the auth module" routes to graph traversal.

This pattern is gaining traction for enterprise AI coding and for AI agents managing large knowledge bases where neither file search alone nor semantic search alone is sufficient.

## Why It Matters

The "RAG is dead" vs. "RAG is essential" debate is a false dichotomy. Both are correct for different corpus sizes and query types. Agentic RAG resolves the debate by making the agent the decision-maker rather than the architect. The architect provides the retrieval toolkit; the agent picks the right tool per query.

For MetaSystem's KB, this validates a potential future architecture: as the KB grows, adding semantic search alongside existing grep/glob/Read tools and letting the agent choose per query. The existing hybrid-retrieval finding covers the technical combinations; this finding covers the agent-as-retrieval-orchestrator pattern.

## Why People Are Using It

- Eliminates the false choice between file search and semantic search
- Agent adapts retrieval strategy to query type automatically
- Graph RAG handles relationship queries that neither semantic nor lexical search can answer well
- Enterprise codebases and large knowledge bases benefit most from multi-strategy approaches
- Can be implemented incrementally: start with file search, add semantic later, add graph when needed

## Potential Improvements

- Meta-retrieval: agent learns which strategy works best for which query type over time
- Retrieval strategy caching: reuse strategy decisions for similar query patterns
- Cost-aware routing: prefer cheaper retrieval (file search) when accuracy is comparable

## Potential Failure Modes

- Agent defaulting to one strategy due to prompt bias (e.g., always choosing semantic search)
- Overhead of multiple retrieval tools adding latency and token cost for simple queries
- Graph RAG requiring significant upfront investment in knowledge graph construction
- Strategy selection errors compounding: wrong retrieval strategy leads to wrong context leads to wrong answer
