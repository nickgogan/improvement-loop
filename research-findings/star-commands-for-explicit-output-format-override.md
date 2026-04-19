---
notion_id: 32b1e08b-9b34-81b5-9410-e8e2a6d01c62
name: Star Commands for Explicit Output Format Override
summary: Carl introduces user-defined star commands (e.g., *brief, *dev, *plan) that override Claude's default response style regardless of context, providing deterministic output format control without
  relying on Claude to interpret implicit format preferences.
implementation_notes: null
category: Prompt Craft
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
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
- file: brevity-constraints-reverse-llm-performance.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Star Commands for Explicit Output Format Override

## What It Is
Carl allows users to define named star commands in the manifest. Each command maps to a specific output mode: *brief = bullet points only, no prose; *dev = code over explanation, show the fix don't describe it; *plan = explicit step-by-step structured output. Users prefix their prompt with the star command to override Claude's default tendency to provide verbose contextual explanations. The author distinguishes this as 'domains are autopilot, star commands are manual override.'

## Why It Matters
Claude tends toward verbose explanatory prose by default, which wastes tokens and is inappropriate when a developer just needs a quick code fix. Without explicit override mechanisms, users have to re-state format preferences on every prompt or rely on CLAUDE.md rules that may not be context-specific enough.

## Why People Are Using It
Developers in mid-session debugging cycles use *dev to skip explanations entirely. Managers reviewing outputs use *brief to get condensed summaries. The explicit command removes ambiguity about output expectations.

## Potential Alternatives
Inline prompt suffixes (respond in bullet points only); output format sections in CLAUDE.md; project-level system prompts that prescribe formatting per file type.

## Potential Improvements
Dynamic star commands that accept parameters (e.g., *brief:3 for maximum 3 bullets) would add granularity. Integration with context bracket logic so the active bracket auto-suggests the appropriate command.

## Potential Failure Modes
Users must remember the defined star commands; there's no discovery mechanism beyond memorization or checking the manifest. Conflicts between a loaded domain's format instructions and a star command override could produce inconsistent behavior.
