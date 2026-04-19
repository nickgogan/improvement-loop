---
notion_id: 3351e08b-9b34-8170-adcc-c525cd96622f
name: Reasoning Model Anti-Pattern -- Prescribed Reasoning Paths Degrade Performance
summary: 'On reasoning models (GPT-5.4, Claude 4.6 Opus with extended thinking), five classic prompting techniques demonstrably hurt performance: explicit CoT ("think step by step"), few-shot examples,
  self-consistency runs, least-to-most decomposition, and skeleton-of-thought. The operative principle: define goals and constraints; never prescribe the reasoning path. Tested across all three frontier
  models in March 2026.'
implementation_notes: 'Any skill or system prompt in the KB that uses CoT scaffolding, few-shot examples, or decomposition instructions needs to be audited. This is a breaking change in prompting convention
  that applies to Claude Code and Perplexity skills stack. Source: https://karozieminski.substack.com/p/ai-prompting-techniques-reasoning-models-2026'
category: Prompt Craft
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- every-ai-prompting-technique-that-works-on-reasoni.md
proposals: []
date_discovered: '2026-04-01'
last_updated: '2026-04-09'
related_findings:
- file: emergent-internal-self-debate-reasoning-models-spo.md
  rel: same-problem
- file: model-agnostic-prompting-three-properties.md
  rel: same-problem
- file: advanced-elicitation-techniques-library.md
  rel: contradicts
pipeline_status: synthesized
consumed_by:
- model-resilient-prompt-engineering.md
- rules/reasoning-model-anti-pattern-prescribed-reasoning.md
---
# Reasoning Model Anti-Pattern -- Prescribed Reasoning Paths Degrade Performance

## What It Is
Five techniques that DEGRADE performance on reasoning models:
1. "Think step by step" (CoT) -- redundant; model already does this internally
2. Few-shot examples -- overwhelms internal reasoning
3. Self-consistency runs -- models are already consistent
4. Least-to-most decomposition -- model handles decomposition better without prescription
5. Skeleton-of-thought -- same issue

**Replacement pattern:** Goal + Constraints + Context (what to produce, not how to think).

## Why It Matters
Any skill or system prompt that uses CoT scaffolding, few-shot examples, or decomposition instructions needs to be audited. This is a breaking change in prompting convention.

## Why People Are Using It
Tested across all three frontier models (GPT-5.4, Claude 4.6, Gemini 3.1).

## Potential Failure Modes
Non-reasoning model deployments may still benefit from classic techniques. Risk of under-specifying constraints when removing CoT scaffolding.

## Extraction Note — 2026-04-19
Extracted as **rule**: [[reasoning-model-anti-pattern-prescribed-reasoning.md]] in `extracts/rules/`
