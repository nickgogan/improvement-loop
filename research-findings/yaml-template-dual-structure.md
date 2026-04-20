---
name: YAML Template Dual Structure (Schema + Coaching Instructions)
summary: 'BMAD agent templates are YAML files containing two layers: (1) the document outline/schema for the output, and (2) embedded instructions telling the LLM how to coach the user through each section.
  Templates are interaction protocols, not just output schemas.'
implementation_notes: null
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- Perplexity Skills
adopted_in: []
sources:
- bmad-method-masterclass.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-19'
related_findings:
- file: bmad-method-v6-multi-agent-sdlc.md
  rel: enabled-by
- file: composable-templates-for-lazy-capture.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- model-resilient-prompt-engineering.md
---
# YAML Template Dual Structure (Schema + Coaching Instructions)

## What It Is
A template design pattern from the BMad Method where YAML files serve as both output schemas and interaction protocols. Each template contains two layers: (1) the document outline defining what the output should contain, and (2) embedded instructions telling the LLM how to coach the user through completing each section. Brian (BMad): "Embedded in the template is instructions for the LLM and how it should work with you."

## Why It Matters
Templates that only define output structure leave the agent guessing about how to elicit information from the user. The dual structure is what enables BMad's interactive coaching behavior -- the agent knows both what to produce and how to guide the conversation to get there.

## Why People Are Using It
The pattern produces consistently high-quality outputs because the agent follows a structured elicitation process rather than asking generic questions. Example: a PRD template that both defines PRD sections AND tells the agent which questions to ask per section, what level of detail to push for, and when to move on.

## Potential Improvements
MetaSystem skill design could adopt this pattern. Skills currently define output expectations but not interaction protocols. Embedding coaching instructions alongside output schemas would improve skill execution quality, especially for complex multi-step skills like /research-proposer or /prompt-evaluator.

## Potential Failure Modes
Over-coaching makes templates bloated and reduces flexibility for experienced users who already know what they want. Templates with heavy instruction layers consume more context tokens. Needs a mechanism for experienced users to skip the coaching layer and provide direct input.
