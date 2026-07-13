---
name: "Storage / Injection / Recall Triad as Memory-System Evaluation Rubric"
summary: |-
  Evaluate any agent memory system by answering three questions: STORAGE — when something
  matters, how and where does it get saved, and who decides? INJECTION — when a session
  starts, what loads automatically as short-term context? RECALL — when you ask about
  something old, how does it get found, and does it get found reliably? The rubric makes
  memory-system comparisons commensurable: Claude Code out-of-the-box scores poorly on
  all three (sparse auto-saves to a memory.md index, near-empty injection, keyword-only
  trawl over 30 days of session files); Hermes scores well on storage and injection but
  is weak on recall (FTS5 keyword-only). A practitioner used exactly this triad to decide
  what to copy from Hermes and what to rebuild.
implementation_notes: |-
  Use as a review lens for the ruled IB-176 memory design
  (project-management/design-notes/2026-07-13-memory-system-design.md): the design
  answers storage (append-only capture + curated distillate, gated promotion) and
  injection (curated snapshot; on-demand calibration registry) explicitly; recall is the
  parked component (findings-search implementation deferred, Nick session 142). The triad
  names the parked axis precisely.
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "rebuilt-hermes-memory-in-claude-code.md"
related_findings:
  - file: "no-single-memory-architecture-workload-alignment.md"
    rel: "same-problem"
  - file: "memory-wiki-world-kb-trichotomy.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "memory"
  - "evaluation"
  - "context-engineering"
---

# Storage / Injection / Recall Triad as Memory-System Evaluation Rubric

## What It Is

A three-question decomposition for evaluating or comparing agent memory systems:

1. **Storage** — when something that matters is discussed, how does it get saved, where,
   and who decides what is worth saving (user command vs agent inference)?
2. **Injection** — at session start, what is loaded automatically as short-term,
   quick-recall context, and how is its size bounded?
3. **Recall** — when the user asks about something old, what mechanism finds it, and does
   it find it reliably (by meaning, not just by exact keyword)?

Simon Scrapes applies the triad to score Claude Code stock memory (weak on all three),
Hermes (strong storage/injection: curated capped snapshot + every-session SQLite archive;
weak recall: FTS5 keyword-only, acknowledged in an open Hermes GitHub issue), and his own
rebuild (keeps Hermes' storage/injection answers, replaces recall with hybrid
semantic+keyword search).

## Why It Matters

Memory-system debates conflate the three axes — "X has better memory" usually means X is
better on exactly one of them. The triad turns a vibes comparison into a per-axis one and
localizes weaknesses: the switching wave from Open Claude to Hermes (~30% of switchers in
Kilo's 1,300-comment Reddit analysis citing memory defaults) was won on storage +
injection defaults, while recall remained mediocre in both. For the engine, the triad
maps cleanly onto the ruled IB-176 memory design and names its one open axis (recall —
the parked findings-search implementation).

## Why People Are Using It

The video's author uses it as his standing analysis frame across multiple memory videos;
the axis separation matches how the broader ecosystem splits (capture hooks vs injection
snapshots vs retrieval pipelines are separate products/plugins). It also explains
observed market behavior: Hermes' growth on defaults, and the plugin ecosystem forming
around Hermes' weak recall axis (MemZero, Honcho as bolt-on semantic memory).

## Potential Improvements

- A fourth axis is arguably missing: **curation/forgetting** (what removes or supersedes
  stale memories). The triad treats storage as write-only; the engine's gated-promotion
  and supersession rules live on this missing axis.
- Per-axis scoring rubric (e.g., 1–5 with anchor descriptions) would make triad
  comparisons repeatable across evaluators.

## Potential Failure Modes

- Scoring axes independently hides coupling: an aggressive storage policy degrades
  injection (snapshot bloat) unless a cap + curation step mediates — the axes are not
  orthogonal in implementation.
- The rubric says nothing about provenance/trust (whether recalled memory should be
  believed), which the engine treats as first-class ("memory is a hint, not an
  authority").
