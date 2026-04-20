---
name: Shell Preamble as Boot Sequence
summary: 'Every SKILL.md starts with an identical ~80-line bash preamble that runs on invocation: checks updates, creates session markers, loads config, detects repo mode, loads learnings, records timeline
  events, checks routing rules. Injected by template generator.'
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: cross-session-learnings-jsonl.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

# Shell Preamble as Boot Sequence

## What It Is
Every gstack SKILL.md starts with an identical ~80-line bash preamble block that runs on invocation. The preamble checks for updates, creates session markers, loads configuration (proactive mode, skill prefix, telemetry settings), detects repo mode, loads the learnings count, records session timeline events, and checks for CLAUDE.md routing rules. This preamble is injected by the template generator, ensuring consistency across all skills.

## Why It Matters
Context assembly via shell execution is a distinct approach from file loading or config parsing. The preamble serves dual purposes: context injection (loading state into the session) and state management (creating session markers, recording timeline events, updating analytics). This pragmatic approach bootstraps a full execution environment before the skill's actual logic begins.

## Why People Are Using It
Observed in [gstack](https://github.com/garrytan/gstack) v0.15.16.0 — see [[gstack-analysis]] for structural details. Context assembly via shell execution rather than file loading or config parsing. The preamble is both context injection AND state management (session markers, timeline events, analytics). Pragmatic approach but creates a coupling between skill behavior and shell environment.

## Potential Alternatives
File-based context loading at session start. Init hooks provided by the AI tool. Lazy loading (fetch context only when needed). API-based context injection.

## Potential Improvements
Conditional preamble sections that skip unnecessary checks (e.g., skip update check if checked recently). Preamble caching to avoid re-executing unchanged steps. Parallel execution of independent preamble steps.

## Potential Failure Modes
Shell execution failures blocking skill invocation entirely. Preamble overhead adding latency to every skill call. Coupling between skill behavior and shell environment making skills non-portable. Silent failures in preamble steps that corrupt downstream state.
