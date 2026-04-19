---
title: "Health Metrics vs. Hard Constraints Distinction"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "health-metrics-vs-hard-constraints-distinction"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The system has documented constraints (in CLAUDE.md, system prompts, governance docs, or equivalent). A constraint classification exercise has been completed — each constraint is tagged as either a health metric or a hard constraint. For each hard constraint, an enforcement mechanism outside the prompt layer has been identified or designed."
  invariants: "Every hard constraint has a corresponding enforcement mechanism in the orchestration or infrastructure layer — never solely in the prompt. Health metrics are measurable and automatically checked — never stated as aspirational prose without a measurement mechanism. The classification of each constraint is documented and reviewable."
  governance: "Nick owns the constraint registry and the classification of each constraint. Reclassification (health metric to hard, or vice versa) requires explicit authorization. Agents may propose reclassifications but must not act on them autonomously."
  recovery: "If a hard constraint is violated despite orchestration-layer enforcement, treat it as a security incident — halt, log, escalate. If a health metric degrades below its threshold, the agent pauses the current strategy and reports the degradation with diagnosis before continuing. If a constraint is discovered to lack its designated enforcement mechanism, escalate immediately — do not rely on prompt-layer compliance as a substitute."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Health Metrics vs. Hard Constraints Distinction

**Source:** [[health-metrics-vs-hard-constraints-distinction]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent systems mix all constraints together in the prompt layer (CLAUDE.md rules, system prompt instructions, skill definitions). Some constraints are preferences that guide reasoning ("don't degrade test coverage"), while others are non-negotiable safety boundaries ("never delete production data"). Treating them identically means safety-critical constraints depend on the LLM choosing to follow an instruction — which is probabilistic, not guaranteed. Meanwhile, genuine preferences are over-enforced, reducing agent flexibility.

## Forces

- **Safety vs. flexibility.** Enforcing every constraint deterministically creates a rigid system where the agent cannot adapt to novel situations. Under-enforcing allows catastrophic violations.
- **Prompt simplicity vs. constraint volume.** Every constraint in the prompt consumes tokens and attention. As constraints accumulate, the model's ability to attend to each one degrades.
- **Measurability vs. expressiveness.** Health metrics only work if they can be measured automatically. Many desirable properties ("code should be clean," "don't degrade user experience") resist precise measurement.
- **Enforcement cost vs. violation cost.** Orchestration-layer enforcement (filesystem permissions, API gates, pre-commit hooks) requires engineering effort. The question is whether the cost of enforcement is justified by the cost of violation.

## Solution

Classify every system constraint into one of two categories and route each to the appropriate enforcement mechanism:

**Health Metrics (steering constraints):**
- Define what must not degrade while the agent pursues its objective.
- Express as observable, measurable values with explicit thresholds (e.g., "test coverage must not drop below 80%," "customer satisfaction must stay above 4.2/5").
- Live in the prompt layer as context that guides the agent's reasoning and trade-off decisions.
- Prevent Goodhart's Law: the agent optimizing one metric at the expense of everything else.
- Checked automatically at defined intervals (post-action, post-session, or continuous).

**Hard Constraints (enforced boundaries):**
- Non-negotiable rules where violation is catastrophic or irreversible.
- Enforced in the orchestration or infrastructure layer — filesystem permissions, API authentication gates, pre-tool-use hooks, CI checks — not via prompt instructions.
- If a constraint matters enough to be hard, it must not depend on the LLM choosing to follow it.
- Examples: "never modify files outside system boundary" enforced via filesystem permissions; "never run destructive commands" enforced via pre-tool-use hooks.

**Key mechanics:**

1. **Classify every constraint.** Build a constraint registry that lists each constraint, its classification (health/hard), its enforcement mechanism, and its measurement method (for health metrics).
2. **Audit enforcement coverage.** For every hard constraint, verify that a non-prompt enforcement mechanism exists. If it doesn't, either build one or reclassify the constraint.
3. **Make health metrics measurable.** "Don't degrade test coverage" is meaningless without automated coverage measurement. If you can't measure it, it's aspirational prose, not a health metric.
4. **Separate layers cleanly.** Prompt-layer instructions guide reasoning. Orchestration-layer mechanisms guarantee compliance. Don't duplicate — a constraint should live in one layer or the other.

## Consequences

**Positive:**
- Safety-critical constraints get deterministic enforcement instead of probabilistic compliance.
- The prompt layer is lighter — only steering guidance, not safety rules — improving model attention on the actual task.
- Health metrics with explicit thresholds prevent Goodhart's Law and make degradation detectable.
- Maps to well-understood software engineering patterns: input validation (hard) vs. code style (steering), authentication (hard) vs. UX guidelines (steering).

**Negative:**
- Over-classifying constraints as hard creates rigidity — the agent has too little room for judgment on edge cases.
- Under-classifying creates safety risks — constraints that should be enforced are left to probabilistic compliance.
- Health metrics that cannot be measured automatically provide false comfort — the constraint exists in name only.
- Building orchestration-layer enforcement for each hard constraint requires engineering investment.

## Known Uses

- **Huryn's Intent Engineering Framework:** Formalizes the health metric vs. hard constraint distinction as a core agent design principle. Cited in multiple production agent deployments.
- **MetaSystem CLAUDE.md rules:** Currently all prompt-layer. The finding identifies specific candidates for migration — e.g., "never modify files outside system boundary" could be enforced via filesystem permissions or hooks.
- **Claude Code pre-tool-use hooks:** An existing enforcement mechanism in MetaSystem's environment that implements the hard constraint pattern for CLI command interception.
- **Software engineering precedent:** Authentication (hard) vs. UX guidelines (steering); input validation (hard) vs. code style (steering).

## Contract

### Preconditions

- The system has documented constraints (in CLAUDE.md, system prompts, governance docs, or equivalent).
- A constraint classification exercise has been completed — each constraint is tagged as health metric or hard constraint.
- For each hard constraint, an enforcement mechanism outside the prompt layer has been identified or designed.

### Invariants

- Every hard constraint has a corresponding enforcement mechanism in the orchestration or infrastructure layer — never solely in the prompt.
- Health metrics are measurable and automatically checked — never stated as aspirational prose without a measurement mechanism.
- The classification of each constraint is documented and reviewable.

### Governance

- Nick owns the constraint registry and the classification of each constraint.
- Reclassification (health metric to hard constraint, or vice versa) requires explicit authorization.
- Agents may propose reclassifications but must not act on them autonomously.

### Recovery

- If a hard constraint is violated despite orchestration-layer enforcement, treat it as a security incident — halt, log, escalate.
- If a health metric degrades below its threshold, the agent pauses the current strategy and reports the degradation with diagnosis before continuing.
- If a constraint is discovered to lack its designated enforcement mechanism, escalate immediately — do not rely on prompt-layer compliance as a temporary substitute.
