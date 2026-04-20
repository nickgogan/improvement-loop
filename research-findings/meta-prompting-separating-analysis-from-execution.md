---
notion_id: 3311e08b-9b34-8114-b973-d6d4af4f0b55
name: 'Meta-Prompting: Separating Analysis from Execution in Agent Workflows'
summary: TACHES implements a meta-prompting pattern where the user describes intent in natural language, Claude generates a rigorous prompt with XML structure, then executes it in a fresh sub-agent context
  -- cleanly separating the 'what to do' phase from the 'doing it' phase.
implementation_notes: Similar pattern exists in our research-loop (extraction -> writing) and Perplexity skills (planning -> execution). Worth monitoring for the specific implementation of prompt generation
  as a first-class operation.
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P3 (Monitor)
applicability:
- S3 (Claude Code Build)
- Perplexity Skills
- General
adopted_in: []
sources:
- taches-claude-code-resources-commands-skills-thinki.md
proposals: []
date_discovered: '2026-03-28'
last_updated: '2026-04-09'
related_findings:
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Meta-Prompting: Separating Analysis from Execution in Agent Workflows

## What It Is
A two-command workflow (/create-prompt and /run-prompt) where the user describes what they want in natural language, Claude generates an optimized prompt with XML structure, and then that prompt is executed in a fresh sub-agent context.

## Why It Matters
When analysis and execution happen in the same context, the agent's reasoning about what to do gets tangled with its attempt to do it. Meta-prompting enforces separation.

## Why People Are Using It
TACHES positions meta-prompts as the foundation for Claude->Claude pipelines. The pattern naturally supports workflow composition through dependency detection.

## Potential Alternatives
Single-context planning and execution, Superpowers brainstorming pipeline, custom system prompts.

## Potential Improvements
Prompt versioning and A/B testing. Prompt templates that capture recurring patterns across projects.

## Potential Failure Modes
Overhead for simple tasks. The generated prompt may lose nuance if the generation step over-abstracts. Fresh sub-agent context means losing domain knowledge from planning.
