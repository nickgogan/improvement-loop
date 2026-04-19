---
title: "Reasoning Model Anti-Pattern — Prescribed Reasoning Paths Degrade Performance"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "reasoning-model-anti-pattern-prescribed-reasoning"
confidence: "HIGH"
tier: "auto"
reason_codes:
  - "must-not"
  - "deterministic-check"
  - "binary-pass-fail"
  - "enforcement-boundary"
  - "anti-pattern-expressible-as-check"
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Target model is identified as reasoning-class. Prompt author understands Goal + Constraints + Context replacement pattern."
  invariants: "No reasoning-model prompt contains CoT scaffolding, few-shot examples, self-consistency runs, least-to-most decomposition, or skeleton-of-thought. Non-reasoning model prompts are explicitly excluded."
  governance: "Owner: Meta-System (cross-system rule). Modification requires a Design Decision. Model class boundaries updated as new generations emerge."
  recovery: "False positive: add inline exception comment and document. Quality regression after CoT removal: add explicit constraints, do not re-introduce CoT. Ambiguous model class: treat as reasoning-class."
tags:
  - "extracted-artifact"
  - "rule"
---

# Reasoning Model Anti-Pattern — Prescribed Reasoning Paths Degrade Performance

**Source:** [[reasoning-model-anti-pattern-prescribed-reasoning]]
**Form:** rule
**Extraction date:** 2026-04-19

## Condition

Any system prompt, skill definition, agent specification, or template that will be consumed by a reasoning-class model (Claude Opus 4.6, GPT-5.4, Gemini 3.1, or successors).

## Action

The following techniques MUST NOT be used in prompts targeting reasoning models:

1. **Chain-of-thought scaffolding** — "Think step by step", "Let's work through this", "First... then... finally..."
2. **Few-shot examples** — Providing input/output pairs to demonstrate reasoning patterns.
3. **Self-consistency runs** — Asking the model to generate multiple reasoning paths and pick the best.
4. **Least-to-most decomposition** — "Start with the simplest sub-problem, then build up."
5. **Skeleton-of-thought** — "First outline your approach, then fill in each section."

Instead, use the **Goal + Constraints + Context** pattern:
- **Goal:** What to produce (the deliverable, not the thinking process).
- **Constraints:** What boundaries apply (format, length, scope, must/must-not rules).
- **Context:** What information the model needs to work with.

## Boundary

- **Skill definitions:** Audit all `SKILL.md` files. Remove CoT scaffolding from procedure descriptions.
- **Agent specifications:** Audit cognitive disposition and directive sections. Remove prescribed reasoning sequences.
- **Templates:** Audit template bodies for embedded reasoning instructions.
- **Prompt evaluator/enhancer:** The `/prompt-evaluator` rubric should penalize prescribed reasoning in prompts targeting reasoning models.
- **Exception:** Non-reasoning model deployments (e.g., Haiku for classification tasks) may still benefit from CoT and few-shot. This rule applies only to reasoning-class models.

## Enforcement

- **Text pattern scan:** Flag prompts containing: "step by step", "let's think", "work through this", "first.*then.*finally" (case-insensitive).
- **Few-shot detection:** Flag prompts containing labeled example blocks ("Example 1:", "Input:.*Output:", "Q:.*A:").
- **Audit trigger:** Any new or modified skill/agent/template undergoes a single-pass check for the five anti-patterns.
- **Binary pass/fail:** Presence of any anti-pattern in a reasoning-model prompt is a fail.

## Rationale

Reasoning models perform internal chain-of-thought natively. Prescribing reasoning paths is redundant at best and actively harmful at worst — it overwhelms the model's internal reasoning with external scaffolding, producing worse outputs than a clean Goal + Constraints + Context prompt. Tested across all three frontier reasoning models (GPT-5.4, Claude 4.6, Gemini 3.1).

This is a breaking change in prompting convention. Legacy prompts written for non-reasoning models must be audited and migrated.

### Known Risks

- Removing CoT scaffolding without adding sufficient constraints can under-specify the task. When stripping reasoning instructions, ensure constraints are explicit enough to guide output quality.
- Non-reasoning model deployments still benefit from classic techniques. The rule must be scoped to model class, not applied universally.

## Contract

### Preconditions
- The target model is identified as a reasoning-class model (not a lightweight/classification model).
- The prompt author understands the Goal + Constraints + Context replacement pattern.

### Invariants
- No reasoning-model prompt contains any of the five prohibited techniques.
- The Goal + Constraints + Context structure is used as the replacement pattern.
- Non-reasoning model prompts are explicitly excluded from this rule.

### Governance
- **Owner:** Meta-System (cross-system rule).
- **Modification gate:** Design Decision required. Model class boundaries may shift as new model generations emerge.
- **Audit scope:** All skills, agents, templates, and inline prompts across all systems.

### Recovery
- If a flagged prompt is a false positive (e.g., "step by step" appears in output format, not reasoning instruction): add an inline exception comment (`<!-- not-cot: output format -->`) and document in the audit log.
- If a reasoning-model prompt fails quality checks after CoT removal: add more explicit constraints to the Goal + Constraints + Context structure rather than re-introducing CoT.
- If model class is ambiguous (e.g., a model with partial reasoning capabilities): treat as reasoning-class and apply the rule. Err on the side of cleaner prompts.
