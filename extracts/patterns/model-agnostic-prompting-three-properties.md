---
title: "Model-Agnostic Prompting -- Three Properties"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "model-agnostic-prompting-three-properties"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "A prompt or skill exists that will be used across model versions or across different model providers. The prompt has been tested on at least one model so its current behavior is known."
  invariants: "Every prompt instruction specifies what to produce, never how to reason. Human judgment is surfaced before generation, not delegated to the model. Output evaluation responsibility stays on the human side."
  governance: "Prompt authors audit against the three properties before committing. Any instruction that prescribes reasoning steps, provides few-shot examples, or asks the model to self-evaluate is flagged for rewrite. Re-audit after model upgrades to confirm durability."
  recovery: "If a prompt fails the three-property test after a model upgrade, isolate the failing property, rewrite the offending instructions to be goal-oriented, re-surface human judgment, and re-anchor evaluation on the human side. Do not patch with model-specific workarounds."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Model-Agnostic Prompting -- Three Properties

**Source:** [[model-agnostic-prompting-three-properties]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Prompting techniques break when models are upgraded or swapped. Chain-of-thought, few-shot examples, and self-consistency checks that worked on one model version degrade or fail entirely on reasoning models. Teams spend repeated effort re-tuning prompts after every model update, and technique catalogs become stale as soon as the underlying model changes.

## Forces

- **Control vs. autonomy:** Prompt authors want predictable outputs but reasoning models internalize their own thinking processes, making prescribed reasoning steps counterproductive.
- **Reusability vs. optimization:** Model-specific prompt tuning yields short-term gains but creates maintenance debt across model versions and providers.
- **Evaluation accuracy vs. convenience:** Delegating output evaluation to the model is easy but unreliable -- models are poor judges of their own work, and self-assessment techniques break across model boundaries.
- **Upfront effort vs. durability:** Surfacing human judgment before generation requires more prompt design work, but produces prompts that survive model transitions without modification.

## Solution

Design every prompt to satisfy three testable properties:

1. **Goal-oriented, not process-oriented.** Tell the model *what* to produce, not *how* to think. Do not prescribe reasoning chains, decomposition steps, or thinking sequences. Reasoning models have internalized their own reasoning processes; prescribing steps conflicts with their architecture and degrades performance. State the desired output shape, constraints, and quality criteria -- let the model determine its own path.

2. **Human judgment surfaces first.** Require the human to make decisions -- prioritize constraints, choose a lens, curate evidence, define trade-offs -- *before* the model generates. This front-loads intent into the prompt rather than hoping the model will infer it. The prompt encodes the human's choices, not a request for the model to guess what the human wants.

3. **Human-side evaluation.** Keep the responsibility for evaluating output quality on the human side. Do not ask the model to judge, score, or rank its own output. The model produces; the human (or a separate evaluation pipeline) judges whether the output matches intent.

**Audit test:** For any existing prompt or skill, check each instruction against these three properties. Flag any instruction that (a) prescribes reasoning steps, (b) provides few-shot examples as implicit process templates, or (c) asks the model to self-evaluate. Rewrite flagged instructions to specify goals, surface human judgment, and externalize evaluation.

These three properties explain why classic techniques (chain-of-thought, few-shot, self-consistency) degrade on reasoning models: they violate property 1 by prescribing the thinking process and often violate property 3 by asking the model to judge its own output.

## Consequences

**Positive:**
- Prompts survive model upgrades and provider switches without rewriting
- Eliminates the need to maintain per-model technique catalogs
- Provides a simple, testable litmus test for prompt durability -- three binary checks
- Aligns with reasoning model architectures that internalize their own planning

**Negative:**
- Requires more upfront design effort to externalize human judgment into the prompt
- Goal-oriented prompts may still fail due to poor context or underspecified constraints -- the three properties are necessary but not sufficient
- Older or smaller models may still benefit from prescribed reasoning; applying these properties universally could hurt performance on non-reasoning deployments
- Teams accustomed to few-shot and chain-of-thought techniques face a paradigm shift in how they write prompts

## Known Uses

- Derived from testing 19 prompting techniques across GPT-5.4, Claude 4.6, and Gemini 3.1 -- the three properties emerged as the common thread across all techniques that performed well on reasoning models
- Properties drawn from 12 disciplines beyond computer science, suggesting cross-domain durability
- MetaSystem's prompt-evaluator skill already scores against related criteria (Prompt Craft, Context Engineering, Intent Engineering, Specification Engineering)
- Anthropic's building-effective-agents guidance implicitly follows these properties by specifying goals and constraints rather than reasoning steps

## Contract

### Preconditions
A prompt or skill exists that will be used across model versions or across different model providers. The prompt has been tested on at least one model so its current behavior is known. The prompt author understands the task well enough to specify desired outputs as goals rather than processes.

### Invariants
Every prompt instruction specifies what to produce, never how to reason. Human judgment (priorities, constraints, trade-offs, evaluation lens) is surfaced in the prompt before generation begins. Output evaluation responsibility stays on the human side -- the model never scores or ranks its own output. These three properties are checked as binary pass/fail conditions, not subjective quality judgments.

### Governance
Prompt authors audit against the three properties before committing any new or modified prompt. Any instruction that prescribes reasoning steps, provides few-shot examples as process templates, or asks the model to self-evaluate is flagged for rewrite. Re-audit prompts after model upgrades to confirm continued compliance and effectiveness. The three properties themselves are updated only through the Improvement Loop pipeline -- not ad hoc.

### Recovery
If a prompt fails one or more properties after a model upgrade: isolate which property is violated, rewrite the offending instructions to restore compliance, and retest. Do not patch with model-specific workarounds -- that creates the version coupling this pattern exists to prevent. If a goal-oriented prompt produces poor outputs despite passing all three properties, the issue is in context or specification quality, not in the properties themselves -- escalate to context engineering or spec refinement.
