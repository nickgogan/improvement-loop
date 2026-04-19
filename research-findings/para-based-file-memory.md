---
name: PARA-Based File Memory
summary: 'Three-layer memory system based on PARA (Projects/Areas/Resources/Archives): knowledge graph with atomic YAML facts and supersession tracking, daily notes as raw timeline, and tacit knowledge
  (MEMORY.md) for user operating patterns. Includes memory decay and weekly synthesis.'
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
- file: four-tier-agent-memory-model-with-write-policy.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-08'
pipeline_status: raw
consumed_by: []
---

# PARA-Based File Memory

## What It Is
Paperclip implements a three-layer memory system based on the PARA framework (Projects/Areas/Resources/Archives): (1) Knowledge graph organized in PARA folders with atomic YAML facts and supersession tracking, (2) Daily notes as a raw timeline of events and observations, (3) Tacit knowledge (MEMORY.md) for user operating patterns and preferences. The system includes memory decay rules that expire stale facts, weekly synthesis that compacts daily notes into durable knowledge, and a `qmd` semantic recall tool for querying stored memory. Supersession means newer facts replace older contradictory ones.

## Why It Matters
Flat memory files grow unbounded and lack organizational structure. The PARA framework provides natural categories for different types of knowledge. Memory decay prevents stale facts from persisting indefinitely — a critical concern for long-running agent systems. Weekly synthesis compacts raw timeline data into durable, reusable knowledge without losing the original granularity.

## Why People Are Using It
Observed in [Paperclip](https://github.com/paperclipai/paperclip) v2026.403.0 — see [[paperclip-analysis]] for structural details. More structured than OpenClaw's flat memory files. The PARA framework provides organizational categories. Memory decay prevents stale facts from persisting indefinitely. Weekly synthesis compacts daily notes into durable knowledge.

## Potential Alternatives
Flat MEMORY.md files (simpler, no structure). Key-value stores. Vector databases for semantic retrieval. Append-only logs with manual curation.

## Potential Improvements
Confidence scoring on facts to prioritize recall. Cross-project knowledge transfer for shared patterns. Automated detection of contradictory facts beyond simple supersession.

## Potential Failure Modes
PARA categorization overhead for simple facts that don't fit neatly into one category. Memory decay removing facts that are still relevant but infrequently accessed. Weekly synthesis losing nuance from daily notes. Supersession incorrectly replacing a valid older fact with a newer incorrect one.
