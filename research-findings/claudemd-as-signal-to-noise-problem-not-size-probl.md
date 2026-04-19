---
notion_id: 32b1e08b-9b34-81fc-a26e-dc0b098e3689
name: CLAUDE.md as Signal-to-Noise Problem, Not Size Problem
summary: The author reframes CLAUDE.md bloat as fundamentally a signal-to-noise problem -- irrelevant instructions don't get ignored, they actively dilute model attention. The goal is focused context, not
  maximum context.
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-08'
related_findings:
- file: context-file-instruction-bloat-eth-zurich.md
  rel: same-problem
- file: context-rot-silent-killer-and-mitigations.md
  rel: same-problem
- file: tiered-context-injection-over-monolithic-files.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# CLAUDE.md as Signal-to-Noise Problem, Not Size Problem

## What It Is
The insight is that Claude's attention mechanism means every instruction present in the context competes for the model's attention, even instructions irrelevant to the current task. A 700-line CLAUDE.md where 650 lines are irrelevant doesn't give Claude more power -- it dilutes the 50 relevant lines.

## Why It Matters
Many power users believe that more instructions always produce better results. This mental model is wrong and produces the opposite effect.

## Why People Are Using It
This framing shifts users from the additive mindset ('what else should I tell Claude?') to the subtractive mindset ('what should I not be loading right now?').

## Potential Improvements
Empirical token-attribution studies showing which CLAUDE.md sections most affect output quality for specific task types.

## Potential Failure Modes
Over-pruning context in pursuit of minimalism can remove rules that provide important safety guards or style constraints.
