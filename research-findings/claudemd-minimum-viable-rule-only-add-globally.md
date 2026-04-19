---
notion_id: 32b1e08b-9b34-817c-8ed8-ccb5774c8e74
name: 'CLAUDE.md Minimum Viable Rule: Only Add Globally True Lines'
summary: CLAUDE.md should only contain rules that would be manually typed into context in virtually every session — anything less universally applicable should be excluded to prevent context rot from the
  very first token.
implementation_notes: null
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- your-ai-coding-is-bad-heres-how-to-fix-it.md
proposals: []
date_discovered: '2026-03-22'
last_updated: 2026-04-08
related_findings:
  - file: "context-file-instruction-bloat-eth-zurich.md"
    rel: "same-problem"
  - file: "context-curation-over-context-stuffing.md"
    rel: "same-problem"
  - file: "tiered-context-injection-over-monolithic-files.md"
    rel: "same-problem"
  - file: "ace-agentic-context-engineering-evolving-playbook.md"
    rel: "same-problem"
  - file: "ace-delta-updates-over-monolithic-rewrites.md"
    rel: "same-problem"
  - file: "agent-context-kiss-commandments-minimum-viable.md"
    rel: "same-problem"
pipeline_status: "raw"
consumed_by: []
---
# CLAUDE.md Minimum Viable Rule: Only Add Globally True Lines

## What It Is
Roman's rule for CLAUDE.md: treat each line as something you would manually type into context at the start of nearly every coding session. If you would not type it most of the time, it should not be in CLAUDE.md. His own CLAUDE.md is 3-5 lines. Most developers start sessions at ~60% context utilization because their CLAUDE.md is bloated with rules that apply to 20% of sessions. This is called 'starting at 60%' — meaning the model is already context-burdened before any work has been done.

## Why It Matters
Every token in CLAUDE.md costs context window space in every session. Even rules that occasionally help cause net harm if they create noise in the 80% of sessions where they are irrelevant.

## Why People Are Using It
The discipline to resist adding rules is non-intuitive. Every failed interaction produces an impulse to add a rule; the MACHINE framework provides the principle to counteract this.

## Potential Alternatives
Per-project CLAUDE.md files (only loaded for relevant projects). Slash commands for session-specific context injection. ACE system (see Video 8) for domain-specific behavioral knowledge.

## Potential Improvements
Claude Code tooling that shows token budget consumption from CLAUDE.md before each session.

## Potential Failure Modes
Too-lean CLAUDE.md means the model repeatedly makes the same preventable mistakes. Finding the right balance requires empirical experimentation per workflow.
