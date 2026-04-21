---
name: Triple Storage Memory Architecture
summary: mem0 implements triple storage — vector stores for semantic similarity, graph stores for relationship-aware retrieval, and SQLite for metadata/history/dedup. The graph layer is optional on top
  of vector, not a replacement. 78 total providers across 5 categories all following abstract base + factory pattern.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- mem0-analysis.md
related_findings:
- file: four-layer-enterprise-memory-stack.md
  rel: same-problem
- file: mongodb-single-store-polymorphic-evidence-memory.md
  rel: contradicts
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-20'
pipeline_status: raw
consumed_by: []
---
## What It Is

mem0 implements a triple storage architecture for agent memory:

1. **Vector stores** (30 providers) — semantic similarity search over embedded memories
2. **Graph stores** (4 providers: Neo4j, Memgraph, Kuzu, Apache AGE) — relationship-aware retrieval that captures connections between entities
3. **SQLite** — metadata tracking, history logging, and deduplication

The graph layer is additive — it sits on top of vector storage, not as a replacement. Systems can start with vector-only and add graph when relationship queries become valuable. The full provider ecosystem spans 78 integrations across 5 categories (24 LLM, 30 vector, 15 embedding, 4 graph, 5 reranker), all following an abstract base class + factory instantiation pattern.

## Why It Matters

Most memory systems commit to a single storage paradigm: either vector (similarity search) or graph (relationship traversal). Each has strengths the other lacks — vector excels at "find memories similar to X" while graph excels at "what do we know about entity Y and its connections." By layering both over a shared metadata store, mem0 lets the retrieval strategy match the query type rather than forcing all queries through one paradigm.

The SQLite layer handles the unglamorous but critical work: deduplication, history tracking, and metadata that neither vector nor graph stores manage well.

## Why People Are Using It

Observed in [mem0](https://github.com/mem0ai/mem0) v1.0.11 — see [[mem0-analysis]] for structural details.

This is the most flexible memory architecture across all 7 analyzed repos. The optional graph layer on top of vector is a pragmatic design choice — it avoids the complexity of graph storage for teams that don't need it while keeping the upgrade path open. The 78-provider ecosystem means teams can swap infrastructure without rewriting application code.

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Vector-only (Chroma, Pinecone) | Single-paradigm semantic search | When all queries are similarity-based and relationships don't matter |
| Graph-only (Neo4j + embeddings) | Graph database with vector index extensions | When relationship traversal dominates and similarity search is secondary |
| Flat file state (STATE.md) | Simple markdown-based memory | For ephemeral agents where session persistence is unnecessary |
| Structured file memory (PARA/Dreaming) | File-based memory with scoring and decay | When infrastructure dependencies are unacceptable |

## Potential Improvements

- Evaluate whether the graph layer's relationship extraction could be automated rather than requiring explicit entity linking
- Assess the query routing logic — how does mem0 decide when to use vector vs. graph retrieval for a given query
- Investigate whether the SQLite metadata layer could be replaced with the vector store's built-in metadata filtering in simpler deployments

## Potential Failure Modes

- **Operational complexity**: Three storage systems to maintain, monitor, and back up — significant ops burden for small teams
- **Consistency across stores**: A memory update must propagate to vector, graph, and SQLite atomically — partial failures create inconsistent state
- **Graph layer overhead**: Adding graph storage when vector-only is sufficient wastes resources and adds latency
- **Provider lock-in through abstraction**: While the abstract base enables swapping, real-world provider-specific features may leak through the abstraction
- **Cold start problem**: Graph relationships require enough memories to form meaningful connections — sparse graphs add complexity without retrieval benefit
