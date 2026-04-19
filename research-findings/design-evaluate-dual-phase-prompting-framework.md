---
name: Design/Evaluate Dual-Phase Prompting Framework
summary: 'Every prompting technique has two phases requiring human judgment: a Design phase (before prompting -- choosing lens, prioritizing constraints, curating evidence) and an Evaluate phase (after
  output -- judging whether the model''s strategic frame, redefinition, or synthesis matches the human''s intent). The framework reframes prompting as a cognitive discipline, not a copy-paste recipe.'
implementation_notes: Applicable to how MetaSystem designs agent briefs and evaluates outputs. The Design phase maps to spec-first briefs; the Evaluate phase maps to acceptance criteria. The framework provides
  the cognitive rationale for why both are necessary.
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- every-ai-prompting-technique-that-works-on-reasoni.md
- prompting-best-practices-nick-gogan.md
related_findings:
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
- file: reasoning-model-anti-pattern-prescribed-reasoning.md
  rel: same-problem
- file: spec-first-agent-briefs-prompt-craft-context-inten.md
  rel: same-problem
- file: the-four-discipline-prompting-stack-nate-b-jones.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: "synthesized"
consumed_by:
  - "model-resilient-prompt-engineering.md"
---

## What It Is

A meta-framework applied to 19 prompting techniques across 12 disciplines (foundational prompting, problem reframing, critique, memory, multi-agent, meta-cognition, philosophy, science, music theory, physics, game theory, anthropology). Each technique is decomposed into:

**Design Phase (before prompting):** The human cognitive work required to use the technique well:
- Role prompting: choosing the interpretive lens and recognizing what it misses
- Instruction-based: prioritizing tradeoffs (format vs. tone, length vs. depth)
- RAG: curating what counts as evidence
- Multi-agent: designing a disagreement worth having

**Evaluate Phase (after output):** The human judgment required to assess the output:
- Step-back: does the model's strategic frame match mine?
- Socratic: does the model's redefinition match the question I needed to ask?
- RAG: did the model stay grounded in evidence or drift from it?
- Multi-agent: is the synthesis a genuine resolution or a false compromise?

The core insight: "Prompting techniques that change how you think, not just what you type."

## Why It Matters

Most prompting guides treat techniques as recipes to copy-paste. This framework reveals that the technique's value comes from the human judgment it demands at both ends. Without the Design phase, the prompt lacks intentionality. Without the Evaluate phase, the human cannot detect when the model's reasoning diverges from their intent.

## Why People Are Using It

Tested across GPT-5.4, Claude 4.6, and Gemini 3.1. The framework is model-agnostic because it operates on human cognition, not model internals. All 19 techniques were tested against a single running example to demonstrate how they connect and build on each other.

## Potential Improvements

- Embed Design/Evaluate checklists into MetaSystem's prompt-evaluator rubric
- Map each technique to the Four-Discipline stack layer it primarily operates on
- Create a technique selection guide based on task type

## Potential Failure Modes

- **Treating it as a recipe:** If the Design phase is skipped and the technique is applied mechanically, it degrades to the copy-paste approach it was designed to replace
- **Evaluate phase fatigue:** In high-throughput settings, humans may skip evaluation, defeating the framework's purpose
- **Technique overload:** Applying all 19 techniques to every prompt is counterproductive; selection matters
