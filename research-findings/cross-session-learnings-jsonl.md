---
name: Cross-Session Learnings JSONL
summary: Per-project learnings stored in append-only JSONL files that persist across sessions. Loaded in preamble, searched at skill start. Managed via /learn skill (review, search, prune, export). Complemented
  by session markers and timeline events.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: gsd-global-learnings-store-cross-session-persistence.md
  rel: same-problem
- file: hook-based-transparent-memory-injection.md
  rel: same-problem
- file: semantic-memory-decay-compaction.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

# Cross-Session Learnings JSONL

## What It Is
gstack stores per-project learnings in `~/.gstack/projects/{slug}/learnings.jsonl` — append-only JSONL files that persist across sessions. Learnings are loaded in the preamble and searched at skill start. The `/learn` skill manages the learnings store with review, search, prune, and export operations. Session markers in `~/.gstack/sessions/` and timeline events in `~/.gstack/analytics/` complement the learnings with session intelligence, providing a complete picture of what was learned and when.

## Why It Matters
Without cross-session persistence, agents repeat mistakes and rediscover solutions. JSONL provides append-only durability — writes never corrupt existing entries. Per-project scoping prevents learnings from one project polluting another. The agent gets smarter within a project over time as learnings from early sessions inform later ones.

## Why People Are Using It
Observed in [gstack](https://github.com/garrytan/gstack) v0.15.16.0 — see [[gstack-analysis]] for structural details. Distinct from GSD's learnings store (which lives in .planning/). gstack's implementation uses JSONL for append-only durability and provides search/prune/export operations. The agent gets smarter within a project over time — learnings from early sessions inform later ones.

## Potential Alternatives
GSD's .planning/-based learnings store. MEMORY.md flat files. Database-backed learning stores. Vector stores for semantic learning retrieval.

## Potential Improvements
Learning quality scoring to prioritize high-value learnings in context. Cross-project learning transfer for shared patterns. Automatic learning extraction from session transcripts without explicit /learn invocation.

## Potential Failure Modes
JSONL files growing unbounded without pruning discipline. Stale learnings persisting and providing outdated guidance. Learning search returning too many results, consuming context window. Per-project scoping missing valuable cross-project patterns.
