---
name: "Session-History Import as Day-One Memory Bootstrap"
summary: |-
  When installing a memory system, don't start from an empty store — import existing
  session history and distill it into memory at setup time. Simon Scrapes' Claude Code
  memory rebuild ships an import command (npm run memory import sessions) that detects
  available sources (current-workspace sessions vs all Claude Code history), lets the
  user choose scope, summarizes each conversation with a cheap model (Claude Haiku),
  embeds the summaries into long-term memory, and preserves complete transcripts in
  compact JSON for later citation-grade recall. Contrast: Hermes cannot import prior
  conversations — the day you install it, months of history stay unremembered.
implementation_notes: |-
  Independently validates the ruled IB-176 plan of record: the first scan run is the SL
  distill-then-close backfill (mine the frozen System Log corpus once into the
  calibration registry + lessons.md, then close it as a read-only archive) — the same
  bootstrap-from-existing-history move, applied to the engine's own historical corpus.
  Key mechanics worth copying: cheap-model summarization for the bulk pass, and keeping
  the raw corpus intact for citation rather than discarding it after distillation.
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
  - file: "session-history-mining-for-skill-discovery.md"
    rel: "extends"
  - file: "memory-system-evaluation-triad-storage-injection-recall.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "session-persistence-and-memory.md"
tags:
  - "memory"
  - "session-management"
  - "claude-code"
---

# Session-History Import as Day-One Memory Bootstrap

## What It Is

A one-time setup step for any new memory system: enumerate existing conversation history
(Claude Code stores ~30 days of sessions locally by default), let the operator pick the
import scope, summarize each session with a cheap model, embed the summaries into
long-term memory, and archive full transcripts in an efficient format so recall can later
expand from summary to exact conversation. The result is a memory system that is
searchable, cited, and useful from day one instead of starting empty.

## Why It Matters

The cold-start problem is the silent tax of every memory-system migration: Hermes imports
settings, memories, skills, and API keys from Open Claude — but not conversations — so
its conversation database starts empty and months of context are lost. The bootstrap
inverts that: history you already paid to produce becomes the initial memory corpus.

For the engine this is corroboration, not news to act on separately: the IB-176 ruled
design already commits to distill-then-close over the frozen SL corpus (calibration
numbers → registry, lesson-shaped residue → lessons.md, then the corpus closes as a
read-only archive). This finding is independent practitioner evidence that
bootstrap-from-existing-history is the right first move, and it adds two transferable
mechanics: cheap-model bulk summarization and keep-the-raw-corpus-for-citation.

## Why People Are Using It

Extends the established practice of mining local session history as "the most relevant
training data you'll ever find" (see `session-history-mining-for-skill-discovery` — bulk
retro-analysis, continuous sync pipelines, proof-based concept grounding). This finding
is the memory-population application of the same substrate: same input, different
consumer.

## Potential Failure Modes

- **Garbage in at scale:** bulk-importing months of sessions imports stale decisions and
  abandoned directions as confidently as good ones; without dated provenance per entry,
  bootstrapped memories can outrank current reality.
- **Cheap-model distillation loss:** Haiku-tier summarization is a lossy pass over
  exactly the corpus you will never re-read; anything the summarizer drops is invisible
  unless the raw transcript archive is preserved and reachable from recall.
- **Default retention windows:** the 30-day session default means the bootstrap can only
  recover what the harness kept — history hygiene has to precede the import decision.
