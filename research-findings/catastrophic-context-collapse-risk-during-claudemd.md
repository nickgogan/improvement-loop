---
notion_id: 32b1e08b-9b34-8183-a67e-d8bd28e95dd0
name: Catastrophic Context Collapse Risk During CLAUDE.md Compaction
summary: Asking Claude to periodically summarize or compact CLAUDE.md introduces a fixed probability of 'catastrophic rewrite' — where the model collapses the entire playbook to ~100-200 tokens, destroying
  accumulated knowledge and pushing accuracy below the no-context baseline.
implementation_notes: null
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- why-your-coding-agent-keeps-getting-dumber.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: ace-delta-updates-over-monolithic-rewrites.md
  rel: enabled-by
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: ace-agentic-context-engineering-rag-based.md
  rel: same-problem
- file: context-curation-over-context-stuffing.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Catastrophic Context Collapse Risk During CLAUDE.md Compaction

## What It Is
The naive 'fix' for a bloated CLAUDE.md is to ask Claude to summarize it. Each compaction step has a small but fixed probability (e.g., 3%, increasing by 0.25% per additional compaction) of producing a catastrophic rewrite — a context collapse where the entire file is reduced to a thin, unhelpful summary. After collapse, accuracy can drop to around 57% of previous performance, often below the baseline of having no CLAUDE.md at all. This is because a sparse, inaccurate summary is worse than no context — it introduces context pollution that actively misleads the model.

## Why It Matters
This is a black-swan failure. The probability per attempt is low but cumulative, and users who compact repeatedly are eventually guaranteed to trigger collapse. They then continue with a poisoned context without knowing it, blaming the model for poor output.

## Why People Are Using It
Compaction feels like maintenance. It appears to shrink the file and reduce token costs. The failure mode is not immediately apparent.

## Potential Alternatives
Use ACE's voting-based curator instead of asking Claude to rewrite the whole file. Use /clear + handoff documents at natural break points instead of compaction.

## Potential Improvements
Version-controlled CLAUDE.md with git snapshots before each compaction would allow rollback. Automated tests on a golden task set before/after compaction could catch quality drops early.

## Potential Failure Modes
If the collapse is not caught and undone within the session, the poisoned CLAUDE.md persists permanently and affects all future sessions.
