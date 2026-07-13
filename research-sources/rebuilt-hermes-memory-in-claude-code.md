---
name: "Simon Scrapes — I Rebuilt Hermes's Best Feature in Claude Code (Steal This)"
source_type: "Video"
status: "Done"
key_takeaways: |-
  A practitioner rebuilds Hermes-grade memory inside Claude Code as portable local
  markdown — the engine's exact stack — and corroborates the ruled IB-176 memory design
  point-for-point: post-turn hook capture into a size-capped curated snapshot (2,500-char
  memory.md) kept separate from append-only full transcripts, files-over-runtime
  portability, and Hermes' self-rewrite failure mode as evidence for gated promotion with
  generator-assessor separation. Decision-relevant number: Kilo's analysis of 1,300
  Reddit comments found ~30% of Hermes switchers cite memory defaults as the reason.
  Novel extractions: the storage/injection/recall triad as a memory-system evaluation
  rubric; session-history import as day-one memory bootstrap (independently validates the
  planned SL distill-then-close); a recall ladder (hybrid semantic+keyword → rerank →
  expand to neighboring context → cite source transcript → say-don't-know); and
  asker-scoped team memory ("TeamOS", beta) as a datapoint for the multi-tenant gap.
relevance: "High"
added_by: "Nick"
tags:
  - "memory"
  - "claude-code"
  - "session-management"
  - "context-engineering"
url: "https://www.youtube.com/watch?v=9CiOwbmOKdU"
authority:
  - "simon-scrapes.md"
findings:
  - "memory-system-evaluation-triad-storage-injection-recall.md"
  - "session-history-import-as-memory-bootstrap.md"
  - "memory-recall-ladder-staged-deepening-with-citation-and-abstention.md"
  - "bounded-tiered-memory-inference-driven-curation.md"
  - "memory-cross-layer-promotion-governance.md"
  - "hierarchical-container-tag-multi-tenancy.md"
date_added: "2026-07-13"
date_processed: "2026-07-13"
date_published: "2026-07-10"
---

# Simon Scrapes — I Rebuilt Hermes's Best Feature in Claude Code

Session-144 Pass 2 deep extraction (link-intake wave 3, architecture/memory cluster).
Transcript: `app/transcript-fetcher/transcripts/9CiOwbmOKdU.md`. Newest source in the
memory cluster — its framing leads per the recency rule.

The build distills Hermes' celebrated memory system to "a few markdown files injected at
session start, an agent that writes conversations into a character-capped summary, and a
search index over past conversations" — then reimplements it inside Claude Code with
three claimed advantages: portable (files move across Claude Code/Codex/any harness),
inexpensive (no VPS, no second model billing, runs on the existing subscription), and
owned (local, no external security surface). Recall is where he goes beyond Hermes:
Hermes ships FTS5 keyword-only session search (open GitHub issue acknowledges it); his
rebuild embeds sessions in local PGlite + pgvector for hybrid semantic+keyword recall
with rerank, context expansion, and transcript citation (citation discipline credited to
Garry Tan's Gbrain). Three findings from this source extend existing KB entries rather
than duplicating them: the capped-snapshot + post-turn promotion mechanics extend
`bounded-tiered-memory-inference-driven-curation` (the Hermes-side original), the
self-rewrite failure evidence extends `memory-cross-layer-promotion-governance`, and the
asker-scoped TeamOS beta extends `hierarchical-container-tag-multi-tenancy`.
