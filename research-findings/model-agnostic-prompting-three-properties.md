---
name: Model-Agnostic Prompting -- Three Properties That Survive Model Updates
summary: 'Prompting techniques that work across reasoning and standard models share three properties: (1) they tell the model what to produce, not how to think; (2) they surface the human''s judgment before
  the model generates; (3) they keep the evaluation responsibility on the human side. Techniques violating these properties (CoT, few-shot, self-consistency) break with reasoning models.'
implementation_notes: Use as a litmus test when designing or auditing MetaSystem skills and agent prompts. Any instruction that prescribes reasoning steps, provides few-shot examples, or asks the model
  to self-evaluate should be flagged for review against these three properties.
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- every-ai-prompting-technique-that-works-on-reasoni.md
related_findings:
- file: reasoning-model-anti-pattern-prescribed-reasoning.md
  rel: same-problem
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
- file: the-four-discipline-prompting-stack-nate-b-jones.md
  rel: same-problem
- file: context-engineering-supersedes-prompt-engineering.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: "synthesized"
consumed_by:
  - "model-resilient-prompt-engineering.md"
---
## What It Is

Three testable properties that distinguish prompting techniques which survive across model generations and architectures:

1. **Goal-oriented, not process-oriented:** Tell the model *what* to produce, not *how* to think. Techniques that prescribe reasoning steps (chain-of-thought, skeleton-of-thought, least-to-most decomposition) conflict with reasoning models that have internalized their own reasoning processes.

2. **Human judgment surfaces first:** The technique requires the human to make decisions (prioritize constraints, choose a lens, curate evidence) *before* the model generates. This front-loads intent rather than hoping the model will infer it.

3. **Human-side evaluation:** The technique keeps the responsibility for evaluating output quality on the human side, not delegating it to the model's self-assessment. The model produces; the human judges whether the output matches their intent.

These three properties explain *why* classic techniques (CoT, few-shot, self-consistency) degrade on reasoning models: they violate property 1 by prescribing the thinking process, and often violate property 3 by asking the model to judge its own output.

## Why It Matters

Provides a durable, model-agnostic test for whether a prompting technique will survive the next model update. Instead of cataloguing which techniques work on which model version, teams can evaluate any technique against these three properties. Techniques that satisfy all three are structurally resistant to model changes.

## Why People Are Using It

Derived from testing 19 techniques across GPT-5.4, Claude 4.6, and Gemini 3.1. The three properties emerged as the common thread across all techniques that performed well on reasoning models. The properties are drawn from 12 disciplines beyond computer science.

## Potential Failure Modes

- **Over-abstraction:** The three properties are necessary but may not be sufficient -- some goal-oriented prompts still fail due to poor context or specification
- **Edge cases with non-reasoning models:** Older or smaller models may still benefit from prescribed reasoning; applying these properties universally could hurt performance on those deployments

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[model-agnostic-prompting-three-properties.md]] in `extracts/patterns/`
