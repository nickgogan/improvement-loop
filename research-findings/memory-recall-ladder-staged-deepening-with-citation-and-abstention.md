---
name: "Memory Recall Ladder — Staged Deepening with Citation and Abstention"
summary: |-
  Recall over long-term agent memory as a staged ladder rather than a single lookup:
  (1) hybrid search by meaning AND keyword (local PGlite + pgvector embeddings alongside
  lexical match), (2) rerank the candidates, (3) expand winners into neighboring
  conversation context so the answer carries surrounding detail, (4) cite the exact
  source transcript — the words, who decided, and the date — and (5) abstain ("say it
  doesn't know") instead of fabricating when nothing clears the bar. Built as the
  replacement for Hermes' keyword-only FTS5 session search, which misses any past
  conversation that doesn't share the query's exact words (asking about "payment
  processing" won't find the Stripe conversation).
implementation_notes: |-
  Direct design input for the parked IB-176 recall component (findings-search over
  research-findings/; hybrid FTS5 + local embeddings was already the sketched lean
  shape). The ladder adds the stages after search: rerank, neighbor expansion, source
  citation, and abstention — the citation + abstention stages are what make recall
  trustworthy enough for team/multi-user use (credited to Gbrain's cite-everything rule).
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources:
  - "rebuilt-hermes-memory-in-claude-code.md"
related_findings:
  - file: "hybrid-retrieval-pattern-semantic-lexical-graph.md"
    rel: "extends"
  - file: "write-back-discipline-memory-is-not-the-brain.md"
    rel: "same-problem"
  - file: "agentic-search-memory-retrieval-architecture.md"
    rel: "same-problem"
  - file: "memory-system-evaluation-triad-storage-injection-recall.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "memory"
  - "context-engineering"
  - "claude-code"
---

# Memory Recall Ladder — Staged Deepening with Citation and Abstention

## What It Is

A five-stage recall pipeline over stored conversation memory that gets "deeper and
deeper" until the query is genuinely answered:

1. **Hybrid search** — semantic (vector embeddings in local PGlite + pgvector) and
   keyword search together, so meaning-matches surface even when vocabulary differs.
2. **Rerank** — reorder candidates for relevance to the actual query.
3. **Context expansion** — expand top hits into the neighboring conversation / full
   session transcript so the answer carries the surrounding decision context.
4. **Citation** — answer with the exact source: the words used, who decided, the date,
   and which conversation it came from.
5. **Abstention** — if nothing clears the relevance bar, say so rather than fabricate;
   the demo answer distinguishes "you asked about your brand today" from near-misses
   ("previous activity was setting up brand context, not asking about it").

All local, no external memory service — contrasted with bolting MemZero/Honcho onto
Hermes to patch its keyword-only recall.

## Why It Matters

Recall is the weak axis of the current memory-system generation (see the
storage/injection/recall triad finding): keyword-only search silently fails on synonym
queries, and single-stage vector search returns decontextualized fragments. The ladder
addresses both, and stages 4–5 convert recall from plausible-sounding to auditable —
which is precisely the property a governed engine needs before recalled memory can
inform decisions ("memory is a hint, not an authority" requires knowing where the hint
came from). For team memory, citation is what makes a teammate's recalled decision
usable: you can read the original conversation instead of trusting the summary.

## Why People Are Using It

Practitioner-built and demonstrated on camera against real history; motivated by an
acknowledged upstream limitation (open Hermes GitHub issue on FTS5-only session search).
The citation discipline is adopted from Garry Tan's Gbrain; the hybrid+rerank+expand
shape matches what retrieval systems converged on elsewhere in the KB
(`hybrid-retrieval-pattern-semantic-lexical-graph`), extended here with the two
trust stages (cite, abstain).

## Potential Alternatives

- **Agentic retrieval** (`agentic-search-memory-retrieval-architecture`) — replace the
  fixed ladder with LLM-driven reasoning over the store; higher per-query cost, no
  pipeline to maintain.
- **External memory services** (MemZero, Honcho) — same capability as a hosted bolt-on;
  another runtime to operate, against the files-over-runtime portability argument.
- **Raw long-context** — load everything and let the model find it; viable only at small
  corpus sizes and hostile to citation.

## Potential Improvements

- Query-conditioned ladder depth: cheap queries stop at stage 1–2; only ambiguous or
  high-stakes queries pay for expansion and full citation.
- Feeding abstentions into a demand ledger (unserved recalls are exactly the
  zero-result-query signal the IB-176 design already logs for system evolution).

## Potential Failure Modes

- **Local embedding stack maintenance** — PGlite + pgvector is another moving part per
  machine; index drift vs the markdown source of truth must be rebuild-on-demand, not
  hand-repaired.
- **Rerank/expansion cost creep** — every recall paying all five stages inflates latency
  and tokens; without a depth policy the ladder becomes a fixed tax.
- **False confidence in citations** — citing a transcript proves provenance, not
  correctness; a confidently cited stale decision still misleads unless recency/
  supersession is surfaced alongside the date.
