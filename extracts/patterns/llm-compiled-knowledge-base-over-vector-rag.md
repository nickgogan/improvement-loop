---
title: "LLM-Compiled Knowledge Base over Vector RAG"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "karpathy-llm-knowledge-base-obsidian-rag"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Raw source corpus is under ~1000 documents. A structured vault (Obsidian or equivalent) with wiki-link support exists. An LLM with sufficient context window to process individual source documents is available."
  invariants: "Query-time retrieval uses file traversal through index files, never vector search. The compile step is explicit and auditable — raw sources are never served directly to querying agents. Index hierarchy stays at two tiers (master index + per-wiki index)."
  governance: "Owned by Meta-System knowledge layer. Changes to the compilation pipeline (index structure, concept article schema, cross-reference format) require a Design Decision. Knowledge linting is a mandatory pipeline stage, not optional."
  recovery: "If compilation produces malformed or contradictory concept articles, revert to the previous compiled state via git and re-compile from raw sources. If index drift is detected (broken links, orphaned articles), run the linting stage before serving queries."
tags:
  - "extracted-artifact"
  - "pattern"
---

# LLM-Compiled Knowledge Base over Vector RAG

**Source:** [[karpathy-llm-knowledge-base-obsidian-rag]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Teams building agent knowledge systems default to vector-database RAG (embeddings + similarity search + retrieval). For small-to-medium corpora (under ~1000 documents), this introduces unnecessary infrastructure complexity (vector DB hosting, embedding model selection, index management, chunking strategy tuning) without proportional retrieval quality gains. Meanwhile, the retrieved chunks lack the relational structure — cross-references, concept hierarchies, contextual framing — that agents need to reason coherently about a domain.

## Forces

- **Infrastructure cost vs. retrieval quality.** Vector DBs require hosting, tuning, and maintenance. For small corpora, the overhead exceeds the benefit, but teams adopt them reflexively because they are the default RAG pattern.
- **Chunk isolation vs. relational context.** Embedding-based retrieval returns isolated chunks stripped of their relational context. An agent retrieving "how to handle X" gets the procedure but not the constraints, exceptions, or related concepts — unless those happen to fall in the same chunk.
- **Freshness vs. compilation cost.** A compiled wiki requires an explicit compilation step when sources change. Vector DBs re-index incrementally. The compilation cost is tolerable for small corpora but becomes a bottleneck at scale.
- **Human readability vs. machine optimization.** A Markdown wiki is human-readable and editable (useful for Obsidian vaults); a vector index is opaque. But human readability is only valuable if humans actually review and curate the knowledge base.

## Solution

Replace vector-database RAG with an **LLM-compiled Markdown wiki** that agents query via file traversal.

The pattern follows a compiler analogy with five stages:

1. **Ingest (source code).** Raw documents — articles, session logs, transcripts, PDFs — are placed in a `raw/` folder. These are the "source code" of the knowledge base. For session-log capture (Cole Medin's adaptation), three hooks (`session_start`, `pre_compact`, `session_end`) produce structured summaries appended to `daily-logs/`.

2. **Compile (build).** An LLM processes raw sources into three output types: an `index.md` file per wiki (summaries as query entry points), concept articles (~100 articles synthesizing related sources), and auto-maintained cross-references (wiki-links between related concepts). A two-tier index hierarchy — `master-index.md` listing all wikis, per-wiki `index.md` listing articles — enables retrieval in 2-3 file reads.

3. **Query (runtime).** Agents start at the master index, navigate to the relevant wiki index, then read the specific concept articles needed. No vector search involved. The hierarchical navigation replaces similarity scoring with structured traversal.

4. **Lint (test suite).** Knowledge linting is a core pipeline stage, not an optional improvement. It covers gap detection (topics in raw sources not yet compiled), stale data identification (compiled articles whose sources have been updated), broken link repair, and raw-vs-wiki discrepancy checks.

5. **Enhance (feedback loop).** Query outputs and new session logs feed back into the raw folder, making the system self-improving. Each session's output enriches the next compilation cycle.

The compiled wiki bypasses the `raw/` folder at query time — agents interact only with the processed, structured knowledge files, avoiding ingestion of unprocessed source material that would dilute retrieval quality.

## Consequences

**Positive:**
- Eliminates vector DB infrastructure entirely for corpora under ~1000 documents.
- Concept articles preserve relational context (cross-references, hierarchies, constraints) that chunk-based retrieval discards.
- Knowledge compounds over time — each compilation cycle integrates new sources with existing concepts.
- Human-readable Markdown is inspectable, editable, and version-controlled via git. Obsidian's graph view and Dataview queries provide additional navigation without custom tooling.
- 2-3 file reads per query is predictable and token-efficient compared to variable-length retrieval results.

**Negative:**
- Scale ceiling around ~1000 documents. Beyond this, file traversal becomes slower than vector search, and compilation cost becomes prohibitive.
- Compilation quality depends on the LLM — unsupervised compilation can introduce errors, hallucinate cross-references, or miss nuances. Periodic human review is required.
- Session log noise can pollute the knowledge base if not filtered before compilation.
- Incremental compilation (processing only changed sources) is not yet standard — most implementations do full recompilation.
- The two-tier index can grow unwieldy without periodic pruning of stale or low-value entries.

## Known Uses

- **Andrej Karpathy's personal knowledge system.** Handles hundreds of documents with the compiler pipeline (ingest, compile, query, lint, enhance). Published as the originating reference for this pattern.
- **Cole Medin's Claude Code adaptation.** Feeds session logs as raw input instead of external articles, creating codebase-specific long-term memory. Uses three hooks for structured session capture with daily flush to wiki.
- **Chase AI production deployment.** Documents production use with Claude Code using the compiled wiki approach.
- **MetaSystem (organic emergence).** The Improvement Loop's research-findings + research-sources + extracts structure follows this pattern organically — raw sources are processed into structured findings with cross-references and index files.

## Contract

### Preconditions

- Raw source corpus is under ~1000 documents (the scale ceiling for this pattern).
- A structured vault with wiki-link support (Obsidian or equivalent) exists and is version-controlled.
- An LLM with sufficient context window to process individual source documents is available for the compilation step.
- A linting stage (gap detection, stale data, broken links) is implemented before the pattern is considered operational.

### Invariants

- Query-time retrieval uses file traversal through the index hierarchy, never vector search.
- The compile step is explicit, auditable, and version-controlled — raw sources are never served directly to querying agents.
- The index hierarchy stays at two tiers: master index listing wikis, per-wiki index listing articles.
- Knowledge linting runs after every compilation cycle, not on an ad-hoc basis.

### Governance

- Owned by Meta-System knowledge layer.
- Changes to the compilation pipeline (index structure, concept article schema, cross-reference format) require a Design Decision.
- Knowledge linting is a mandatory pipeline stage — removing or skipping it requires explicit human authorization.
- Scale ceiling reassessment (when to migrate to vector search) is reviewed when the corpus approaches 800 documents.

### Recovery

- If compilation produces malformed or contradictory concept articles, revert to the previous compiled state via git and re-compile from the corrected raw sources.
- If index drift is detected (broken links, orphaned articles, stale entries), run the linting stage and repair before serving any queries.
- If compilation LLM quality degrades (e.g., model change introduces errors), freeze the wiki at the last known-good compilation and investigate before resuming.
