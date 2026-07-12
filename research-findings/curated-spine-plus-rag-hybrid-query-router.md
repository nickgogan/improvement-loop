---
name: "Curated-Spine + RAG Hybrid with Query Router"
summary: |-
  Architecture for when a knowledge base outgrows pure curation: keep a curated OKF-style
  spine for the canonical ~80% (answers you can't get wrong) and a RAG index for the
  messy long tail you'd never curate by hand, with a thin router in front — canonical,
  high-stakes queries go to the curated KB for exact cited answers; open-ended
  exploratory queries go to retrieval. Coupling rules make the halves reinforce each
  other: when a curated concept exists it outranks fuzzy retrieved chunks, and the
  curated index serves as a pre-search map (progressive disclosure) so the agent drills
  into retrieval only where curation runs out. The whole stack can hide behind a single
  retrieval facade (even one MCP server) so the agent never cares which path answered.
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Weak (theoretical)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "IL (research KB substrate)"
  - "General"
adopted_in: []
sources:
  - "google-okf-rag-the-ultimate-ai-agent-architecture.md"
related_findings:
  - file: "okf-open-knowledge-format-curated-bundle-spec.md"
    rel: "extends"
  - file: "scale-threshold-heuristic-obsidian-vs-rag.md"
    rel: "extends"
  - file: "hybrid-retrieval-pattern-semantic-lexical-graph.md"
    rel: "same-problem"
  - file: "file-search-outperforms-rag-for-small-corpora.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

In plain English: the answer to "curated markdown KB or vector-search RAG?" is a
routing question, not a bet. The architecture layers three pieces:

1. **Curated spine (the canonical ~80%).** An OKF-style bundle carries the knowledge
   you simply can't get wrong — policies, schemas, definitions. Deterministic
   retrieval: a human decided exactly what the model sees, no cosine-distance lottery,
   diffable in git with an accountable owner.
2. **RAG reach (the long tail ~20%).** A vector index over the huge, messy, uncurated
   archive (tickets, transcripts, PDFs) where good-enough semantic matching is honestly
   good enough and hand-curation will never happen.
3. **Query router.** Per query: canonical and high-stakes ("what's our refund window?")
   routes to the curated spine for an exact, cited answer; open-ended and exploratory
   ("has anyone hit this billing bug?") routes to retrieval over the archive.

Two coupling rules make the halves better than either alone:

- **Curated concepts outrank retrieved chunks.** When a curated concept exists for a
  question, the agent trusts it over fuzzy retrieval — the source claims this single
  precedence rule makes a real dent in hallucinations (no data shown).
- **Curated index as pre-search map.** The spine's index files tell the agent what
  knowledge exists *before* any search runs (progressive disclosure), so it drills into
  RAG only where the curated answer runs out instead of blind-searching from zero.

Optionally, everything hides behind **one retrieval facade** — index the OKF bundle
into the vector store too, expose a single retrieval interface (even a single MCP
server), and the agent just asks for knowledge while routing stays plumbing.

Economics: the curated spine is text in git (write once, edit a line); RAG carries
standing cost (embedding, re-embedding on change, a vector DB that never sleeps).
Curate what's worth curating, pay to index the rest. The source also rejects the
million-token-context alternative: irrelevant knowledge degrades answers and burns
tokens; selective routed retrieval beats brute force.

## Why It Matters

The KB's existing guidance is mostly either/or: file traversal below a corpus-size
threshold, vector search above it (scale-threshold-heuristic-obsidian-vs-rag.md,
file-search-outperforms-rag-for-small-corpora.md). This pattern extends that with a
both/and answer for corpora that are *mixed* — a small high-stakes core plus a large
uncurated tail — which is the realistic long-run shape of most knowledge systems,
including ours if transcript archives and raw sources ever outgrow curated navigation.
It's a live design reference for our knowledge architecture, not a current need.

## Why People Are Using It

Presented as the emerging production default ("almost every serious agent headed for
production" runs both) with a plausible team split — data owners curate bundles,
engineers index the archive, frameworks wire the two — but this is explainer-channel
synthesis: no built system, benchmarks, or artifacts are shown. Treat as an
architectural direction signal, corroborated in spirit by the KB's hybrid-retrieval and
agentic-RAG findings.

## Potential Alternatives

Pure file-traversal KB below the scale threshold (our current state; simplest and
validated). Pure RAG over everything (loses determinism and auditability on the
canonical core). Agentic RAG where the model picks a retrieval tool per query without a
curated-precedence rule (hybrid-retrieval-pattern-semantic-lexical-graph.md — same
problem, no spine/tail distinction). Long-context stuffing (rejected above).

## Potential Improvements

Evidence is the gap: hallucination-reduction numbers for the precedence rule, and
router-accuracy data (misrouting a canonical query to fuzzy retrieval silently
reintroduces the failure the spine exists to prevent). Router implementations range
from a prompt rubric to a trained classifier; nothing is specified.

## Potential Failure Modes

- **Router misclassification.** A high-stakes query routed to RAG gets a fuzzy answer
  dressed as a citation — the architecture's whole value inverts on routing errors.
- **Spine staleness.** The 80/20 boundary drifts; canonical answers age in the bundle
  while fresher truth sits unretrieved in the tail (precedence rule then actively
  harms).
- **Double-indexing drift.** If the bundle is also embedded into the vector store
  (facade variant), stale embedded copies of curated concepts can outrank the current
  file.
- **Premature adoption.** Standing RAG costs and routing complexity are pure overhead
  for corpora still comfortably below the file-search threshold.
