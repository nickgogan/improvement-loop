---
title: "Spec-First Agent Briefs"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "spec-first-agent-briefs-prompt-craft-context-inten"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The agentic task is non-trivial (estimated at 3+ tool calls or 2+ minutes of agent work). A task spec template is available."
  invariants: "Every agent brief contains at minimum: objective, acceptance criteria, constraints, and escalation triggers. No long-running agentic task is initiated without a spec."
  governance: "The spec template is a governed artifact. Changes to required spec fields require DD-level review. Specs are retained as audit records of what was requested vs. what was produced."
  recovery: "If an agent task fails or produces unacceptable output, review the spec first. Missing or ambiguous spec fields are the most common root cause. Fix the spec and re-run before investigating agent behavior."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Spec-First Agent Briefs

**Source:** [[spec-first-agent-briefs-prompt-craft-context-inten]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Long-running agentic tasks fail or produce off-target results because the agent was given vague, implicit instructions. Natural-language prompts that work for conversational interactions ("help me refactor this module") are insufficient for multi-step autonomous work where the agent must make dozens of decisions without human checkpoints. The agent fills in ambiguity with defaults that may not match the human's intent, and neither party discovers the mismatch until the work is complete.

## Forces

- **Brevity vs. precision.** Detailed specs take time to write. Terse prompts are faster but leave critical parameters implicit. The cost of writing a spec must be weighed against the cost of re-doing failed work.
- **Flexibility vs. predictability.** Over-specified tasks constrain the agent's ability to adapt to unexpected findings. Under-specified tasks produce unpredictable output.
- **Context vs. token budget.** Comprehensive specs with all authoritative inputs, definitions, and background consume context window. But missing context forces the agent to guess.
- **Trust vs. verification.** Teams that trust their agents skip specs and acceptance criteria. But without verifiable criteria, "done" is a subjective judgment that erodes over time.
- **Speed vs. plan-first.** Stopping to write a spec and requiring plan-first checkpoints adds latency before any work begins. But unplanned work has higher variance and higher rework rates.

## Solution

Package every non-trivial agentic task as a self-contained specification with these required sections:

1. **Objective + Why.** What the agent should accomplish and why it matters. The "why" enables the agent to make aligned decisions when the spec is ambiguous.

2. **Success Metrics.** Quantifiable or observable indicators that the objective was achieved. Not aspirational goals -- measurable outcomes.

3. **Authoritative Inputs.** The documents, repos, tool definitions, memory files, and reference materials the agent should treat as ground truth. Explicitly listed, not assumed.

4. **Deliverables + Format.** What the agent produces and in exactly what format. File paths, schemas, naming conventions -- nothing left to inference.

5. **Acceptance Criteria.** Verifiable conditions that determine whether the output is acceptable. Ideally runnable commands (tests, linters, validators) rather than subjective assessments.

6. **Constraints.** Three tiers:
   - **Must:** Hard requirements (never violate).
   - **Must-not:** Explicit prohibitions (never do X).
   - **Preferences:** Soft guidance (prefer Y over Z, but not blocking).

7. **Escalation Triggers.** Conditions under which the agent should stop and ask rather than proceed: ambiguity it cannot resolve, policy conflicts, changes that feel risky, scope creep.

8. **Workflow: Plan-First + Checkpoints.** The agent plans before executing, presents the plan for confirmation at defined checkpoints, executes, then provides verification notes. The spec defines where checkpoints occur.

Context (authoritative inputs, domain definitions, background) and Intent (trade-offs like speed vs. quality, cost vs. correctness) are first-class sections, not scattered prose within the prompt.

## Consequences

**Positive:**
- Dramatically reduces rework from misaligned agent output by making intent explicit upfront.
- Acceptance criteria enable automated verification, reducing review burden.
- Escalation triggers prevent the agent from silently making bad decisions in ambiguous situations.
- Specs serve as audit records: what was requested, what constraints applied, what was produced.
- Plan-first checkpoints catch misunderstandings before expensive execution.

**Negative:**
- Spec writing has overhead. For truly trivial tasks, the spec costs more than the task.
- Over-specification can constrain beneficial agent creativity and adaptation.
- Maintaining a spec template is itself a governance cost.
- Teams may treat spec-writing as bureaucracy and produce hollow specs that check boxes without adding clarity.

## Known Uses

- The "prompting after Feb 2026" practitioner guide documents this as the dominant pattern for production agentic work.
- The intent engineering framework for AI agents formalizes the Context -> Intent -> Specification progression.
- MetaSystem's Build Spec pattern (used for all Claude Build work) implements a version of this with plan-first, review gates, and acceptance criteria.
- MetaSystem's skill definitions (SKILL.md files) embody this pattern with structured sections for inputs, outputs, constraints, and workflow steps.

## Contract

### Preconditions
The agentic task is non-trivial -- estimated at 3+ tool calls, 2+ minutes of agent work, or involving decisions the agent must make autonomously. A spec template is available and the person issuing the task has sufficient context to fill in the required fields.

### Invariants
Every agent brief for a non-trivial task contains at minimum: objective, acceptance criteria, constraints (must/must-not), and escalation triggers. No long-running agentic task is initiated from a bare natural-language prompt without a spec. Context and intent are explicit sections, not implicit prompt text.

### Governance
The spec template is a governed artifact. Changes to the required fields of the template require DD-level review. Completed specs are retained alongside agent output as audit records of what was requested vs. what was produced. Escalation trigger definitions are reviewed periodically for completeness.

### Recovery
If an agent task fails or produces unacceptable output, review the spec first before investigating agent behavior. Missing or ambiguous spec fields (especially acceptance criteria and constraints) are the most common root cause of agent misalignment. Fix the spec, verify it addresses the failure mode, and re-run. If the spec was adequate and the agent still failed, the issue is agent capability, not specification.
