---
notion_id: 32b1e08b-9b34-8177-be0a-d9f568a68f58
name: Skill-as-New-Employee Mental Model
summary: 'Framing skill design as ''onboarding a new employee'' produces more complete instructions: what the process accomplishes, when to invoke it, step-by-step execution, internal policies/constraints,
  and expected output format — rather than writing a generic task description.'
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- Perplexity Skills
adopted_in: []
sources:
- most-people-build-claude-skills-wrong-heres-what-w.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
- file: video-transcript-driven-voice-skill-generation.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Skill-as-New-Employee Mental Model

## What It Is
When designing a skill prompt, Bart recommends imagining you are writing an onboarding document for a new hire assigned to that specific task. This naturally prompts the designer to include: (1) purpose/scope of the process, (2) triggering conditions and context that must be provided at invocation, (3) step-by-step execution instructions with branching logic, (4) internal policies and constraints (compliance rules, tone guidelines, escalation thresholds), and (5) the precise format and content of the expected output. This framing prevents the common failure of writing only 'what to do' without 'how, when, and to what standard'.

## Why It Matters
Generic skill prompts produce inconsistent results because they lack the constraints and branching logic a human employee would internalize from proper training. The employee metaphor makes it natural to include all necessary context.

## Why People Are Using It
Intuitive mental model that non-technical practitioners can apply immediately. Makes the 'context provided at invocation' vs. 'context baked into the skill' distinction concrete: the skill is the onboarding manual, and the invocation call is the specific work order.

## Potential Alternatives
Constitutional AI / rule-based prompt design frameworks, chain-of-thought template libraries.

## Potential Improvements
Pairing this mental model with a checklist of required fields for each of the five patterns would make it mechanical and auditable.

## Potential Failure Modes
Onboarding documents can become too verbose and hit context limits. Important edge cases that the 'employee' would ask about in person don't always surface in written specs.
