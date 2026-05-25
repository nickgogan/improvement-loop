---
notion_id: 32c1e08b-9b34-81e1-a5e8-dafb8b253a54
name: Context Enrichment for Task Clarity
summary: 'Provide upfront: what task results will be used for, target audience, workflow position, and success criteria with measurable thresholds. This consistent contextual framing dramatically improves
  output quality by constraining the solution space.'
implementation_notes: We do this inconsistently. Every skill should have a Task Context section passing purpose, audience, workflow position, and success criteria. Subagent objectives especially lack this
  context. Low effort, high impact.
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
priority: P1 (Implement Now)
applicability:
- Perplexity Skills
adopted_in: []
sources:
- prompting-best-practices-nick-gogan.md
proposals: []
date_discovered: '2026-03-23'
last_updated: 2026-04-08
related_findings:
- file: advanced-elicitation-techniques-library.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
- writing-agent-specifications.md
---
# Context Enrichment for Task Clarity

## What It Is
A prompting pattern requiring four types of contextual information upfront: (1) what the task results will be used for, (2) what audience the output is for, (3) what workflow the task is part of, (4) success criteria with measurable thresholds.

## Why It Matters
Without task context, models optimize for generic output. With explicit purpose, audience, workflow position, and success criteria, the model can make informed tradeoffs.

## Why People Are Using It
Documented in both Anthropic and OpenAI best practices. The pattern is foundational to context engineering.

## Potential Alternatives
Implicit context from conversation history, template-based prompts, dynamic context injection.

## Potential Improvements
Context enrichment could be automated: a pre-processing step that infers purpose, audience, and workflow position from the task description.

## Potential Failure Modes
Over-specifying context for simple tasks adds overhead. Incorrect context is worse than no context. Maintaining context accuracy across multi-step workflows requires careful propagation.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[context-enrichment-for-task-clarity]] in `extracts/patterns/`
