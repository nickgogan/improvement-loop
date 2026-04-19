---
name: Semantic Memory Decay Compaction
summary: Closed/completed work items are summarized rather than deleted, preserving context while reducing noise. Decay-weighted scoring determines what survives compaction — recent and high-impact items
  get higher survival priority.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: five-context-management-techniques-in-claude-code.md
  rel: extends
- file: claude-code-long-term-memory-via-pre-prompt-recall.md
  rel: extends
- file: ace-delta-updates-over-monolithic-rewrites.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: context-usage-status-line-visual-budget-tracking.md
  rel: same-problem
- file: cross-session-learnings-jsonl.md
  rel: same-problem
- file: dreaming-memory-consolidation.md
  rel: same-problem
- file: dynamic-tool-pool-assembly-transcript-compaction.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
---

## What It Is

A compaction strategy where completed work items are semantically summarized rather than dropped or truncated. The system applies decay-weighted scoring to determine what information survives compaction: recent items, high-impact decisions, and items with active dependency links score higher. Combined with compaction-survival mechanics — critical fields (notes, design decisions, acceptance criteria) are persisted in the database rather than in-context, so they survive context window resets.

## Why It Matters

Standard compaction strategies (truncation, FIFO dropping, sliding window) lose information indiscriminately. Semantic decay preserves the most valuable context by weighting recency and impact. For long-running agent sessions with many completed tasks, this prevents the "amnesia" problem where agents lose awareness of decisions made earlier in the session.

## Why People Are Using It

Observed in [Beads](https://github.com/gastownhall/beads) v1.0.2 — see [[beads-analysis]] for structural details. Beads uses `bd` CLI's compaction recovery workflow: critical fields (notes, design, acceptance) are stored in Dolt and survive context compaction. The `PreCompact` hook auto-pushes state before Claude Code's context compression fires. On recovery, `bd show` restores the full context for the current task.

## Potential Alternatives

- Simple FIFO compaction (drop oldest messages)
- Sliding window with fixed token budget
- Two-threshold compaction (OpenViking pattern — see related finding)

## Potential Improvements

Could be combined with the L0/L1/L2 tiered loading pattern to store compacted summaries at L0 level and full content at L2, enabling re-expansion on demand.

## Potential Failure Modes

- Decay scoring may not weight correctly for all use cases
- Summary quality depends on the LLM's ability to capture key decisions
- Over-aggressive decay can lose important context about why decisions were made
