---
name: Advanced Elicitation Techniques for LLM Output Quality
summary: 'A library of 18 advanced prompting techniques (tree of thought, red team/blue team, REWOO, critique and refine, stakeholder roundtable, etc.) embedded in YAML agent templates to push LLM output
  beyond first-pass quality. BMad quote: "The advanced elicitation is your chance to really stick the cattle prod to the agent."'
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-method-masterclass.md
- prompting-best-practices-nick-gogan.md
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
related_findings:
- file: yaml-templates-with-embedded-elicitation-instructions.md
  rel: enables
- file: bidirectional-prompting-for-spec-creation.md
  rel: same-problem
- file: business-analyst-upstream-quality-gate.md
  rel: same-problem
- file: context-enrichment-for-task-clarity.md
  rel: same-problem
- file: design-evaluate-dual-phase-prompting-framework.md
  rel: same-problem
- file: emergent-internal-self-debate-reasoning-models-spo.md
  rel: same-problem
- file: explore-tokens-and-receive-tokens-non-linear.md
  rel: same-problem
- file: five-layer-agent-prompt-architecture.md
  rel: same-problem
- file: iterative-refinement-loop-with-quality-gate.md
  rel: same-problem
- file: llm-as-judge-pattern-for-verification-agents.md
  rel: same-problem
- file: meta-prompting-separating-analysis-from-execution.md
  rel: same-problem
- file: metaprompting-karpathy-autoresearch-for-build.md
  rel: same-problem
- file: model-agnostic-prompting-three-properties.md
  rel: same-problem
- file: negative-constraints-as-probabilistic-output-collapse.md
  rel: same-problem
- file: prompt-as-policy-version-control-and-cicd-for-agen.md
  rel: same-problem
- file: reasoning-model-anti-pattern-prescribed-reasoning.md
  rel: contradicts
- file: skill-as-new-employee-mental-model.md
  rel: same-problem
- file: star-commands-for-explicit-output-format-override.md
  rel: same-problem
- file: the-four-discipline-prompting-stack-nate-b-jones.md
  rel: same-problem
- file: thinking-models-mental-framework-commands-for-codi.md
  rel: same-problem
- file: brevity-constraints-reverse-llm-performance.md
  rel: contradicts
pipeline_status: "synthesized"
consumed_by:
  - "model-resilient-prompt-engineering.md"
---
# Advanced Elicitation Techniques for LLM Output Quality

## What It Is
18 techniques embedded in BMad Method YAML agent templates: explain reasoning, critique and refine, analyze logical flow, assess goal alignment, risk identification, critical perspective, tree of thought, deep dives, hindsight 2020, agile team shift, stakeholder roundtable, metaprompting, self-consistency, REWOO (Reasoning Without Observation), persona hybrid, red team vs blue team, innovative tournament, escape room challenge. Agents use these to push past initial answers.

## Why It Matters
First-pass LLM output is often generic. These techniques create structured "second pass" reasoning that surfaces edge cases, contradictions, and deeper insights. The technique library is reusable across agent types.

## Why People Are Using It
Core component of BMad Method. The techniques are documented in YAML templates and can be cherry-picked.

## Potential Alternatives
- Manual prompt iteration.
- Chain-of-thought prompting (less structured).
- Prompt-evaluator + prompt-enhancer feedback loops.

## Potential Improvements
- Technique selection based on task type (not all 18 apply to every situation).
- Effectiveness metrics per technique.
- Integration with prompt-evaluator rubric dimensions.

## Potential Failure Modes
Technique overload — applying too many techniques wastes tokens without improving quality. Some techniques (escape room challenge, innovative tournament) may be gimmicky rather than productive. Over-elicitation can produce analysis paralysis in agents.
