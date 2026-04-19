---
name: "Memory Decay/Compaction Is Converging on Multi-Strategy Approaches"
summary: "Four repos address context compaction with semantically-aware strategies beyond simple truncation: Beads (semantic decay), OpenViking (two-threshold), Paperclip (weekly synthesis + decay), DeerFlow (async summarization). Each solves a different facet of the same problem."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: null
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - {file: "semantic-memory-decay-compaction.md", rel: "extends"}
  - {file: "two-threshold-compaction-strategy.md", rel: "extends"}
  - {file: "five-context-management-techniques-in-claude-code.md", rel: "same-problem"}
proposals: null
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
---

## What It Is

A cross-repo convergence observation: four repos independently implement semantically-aware compaction — going beyond FIFO/sliding-window to use importance scoring, thresholds, or summarization to decide what survives. Each implementation solves a different facet:
- **Beads**: What to keep — decay-weighted scoring prioritizes recent and high-impact items
- **OpenViking**: When to compact — dual thresholds (50% async archive, 70% forced clear)
- **Paperclip**: How often to consolidate — weekly synthesis cycles with decay rules
- **DeerFlow**: Where to persist — per-thread async summarization via MemoryMiddleware

## Why It Matters

The community has collectively learned that naive compaction (truncation, FIFO) loses too much valuable context. All four implementations use semantic understanding — LLM-based summarization or importance scoring — to make intelligent retention decisions. A complete solution would combine all four facets: importance-weighted retention (what), threshold-triggered timing (when), periodic consolidation (how often), and scoped persistence (where).

## Why People Are Using It

Cross-repo observation across 14 analyzed repos — see [[cross-repo-comparison]] for structural details. Observed in [Beads](https://github.com/gastownhall/beads), [OpenViking](https://github.com/volcengine/OpenViking), [Paperclip](https://github.com/nicholasgriffintn/paperclip), and [DeerFlow](https://github.com/bytedance/deer-flow).

## Potential Alternatives

- Simple FIFO compaction (drop oldest)
- Sliding window with fixed token budget
- Manual compaction (user-triggered)

## Potential Improvements

Combine all four facets into a unified compaction architecture: importance scoring decides what → dual thresholds decide when → periodic consolidation sweeps → scoped storage persists.

## Potential Failure Modes

- Summary quality is the bottleneck — bad summaries lose information permanently
- Multiple strategies add complexity and debugging difficulty
- Threshold values need per-use-case tuning
