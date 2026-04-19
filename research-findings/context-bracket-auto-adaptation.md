---
notion_id: 32b1e08b-9b34-8136-a31d-f032327fb9fa
name: Context Bracket Auto-Adaptation
summary: Carl monitors remaining context window space and automatically adjusts Claude's verbosity through three brackets (fresh/moderate/depleted), progressively compressing responses and ultimately switching
  to code-only survival mode without requiring user intervention.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources: []
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: two-threshold-compaction-strategy.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Context Bracket Auto-Adaptation

## What It Is
Carl defines three context brackets based on estimated remaining context window: Fresh (plenty of room — Claude operates at full depth), Moderate (context filling — Claude switches to more concise output style), Depleted (critical — code-only, no explanations, Claude verbally reminds itself of its prime directive and urges the user to create a handoff document). These transitions happen automatically; the user does not need to manually monitor token counts or issue format-change instructions.

## Why It Matters
As context fills in a long session, Claude's output quality degrades and its attention to early instructions diminishes. If Claude continues to generate three-paragraph explanations when context is nearly full, it wastes the remaining budget on prose rather than productive work. Auto-adapting verbosity extends the effective working life of a session.

## Why People Are Using It
Long-running Claude Code sessions (building complex features across many files) frequently hit context pressure. The auto-adaptation allows developers to stay in a single session longer without manually managing a compact-and-restart workflow.

## Potential Alternatives
Claude's built-in /compact command to manually compress context; session handoff documents generated at the developer's discretion; GSD/PAUL plugins that restart fresh context windows at phase boundaries.

## Potential Improvements
Smarter bracket detection using actual token counts from Claude's API rather than heuristics. A user-visible indicator (in the terminal output) showing which bracket is currently active would help developers plan their remaining session.

## Potential Failure Modes
In depleted mode, code-only output may produce fixes that are harder to understand or audit later. The bracket transitions could surprise users who expect consistent behavior throughout a session.
