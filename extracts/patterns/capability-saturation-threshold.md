---
title: "Capability Saturation Threshold"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "capability-saturation-threshold-45-percent"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Single-agent baseline performance is measurable on the target task; evaluation criteria are well-defined and agreed upon before measurement."
  invariants: "The decision to use single-agent vs. multi-agent is always backed by measured baseline performance, never by architectural preference or hype."
  governance: "Threshold evaluation is reviewed at each new task type introduction. Overrides require explicit justification with comparative metrics."
  recovery: "If multi-agent coordination is deployed past the threshold and degrades performance, revert to single-agent execution and document the regression in the System Log."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Capability Saturation Threshold

**Source:** [[capability-saturation-threshold-45-percent]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Teams default to multi-agent orchestration for complex tasks because it feels architecturally sophisticated, without measuring whether a single agent already handles the task adequately. This leads to FOMO-driven adoption of orchestrators that degrade results through coordination overhead -- information loss at handoff boundaries, error amplification across agents, and wasted token budgets on breadth instead of depth.

## Forces

- **Scalability intuition vs. coordination cost.** Adding agents feels like adding capacity, but each agent boundary introduces information loss and error amplification (independent agents amplify errors 17.2x vs. centralized coordination at 4.4x).
- **Fixed computational budgets.** Tokens spent on inter-agent communication are tokens not spent on deeper single-agent reasoning. Tool-heavy tasks suffer disproportionately.
- **Measurement difficulty.** Evaluating single-agent baseline performance requires well-defined eval criteria, creating a dependency on evaluation infrastructure that many teams lack.
- **Genuine parallelism exceptions.** Some tasks are inherently parallelizable (independent subtasks with no shared state), where multi-agent coordination legitimately outperforms single-agent sequential execution.

## Solution

**Before committing to a multi-agent architecture, measure single-agent baseline performance on the target task.** If the single agent achieves greater than approximately 45% performance on the evaluation criteria, do not orchestrate -- invest in making that single agent better (deeper reasoning, better tools, richer context).

The reusable shape:

1. **Define evaluation criteria** for the task before choosing an architecture.
2. **Run a single-agent baseline** and record its performance score.
3. **Apply the threshold heuristic:** if baseline exceeds 45%, invest in single-agent improvement (better prompts, more tools, richer context). If baseline is below 45% AND the task has genuinely parallelizable subtasks, evaluate multi-agent coordination.
4. **Re-measure after architectural changes** to confirm improvement rather than assuming it.

The 45% number is conservative and derived from empirical research. The exact breakeven varies by task, but the principle -- measure before orchestrating -- is universal.

## Consequences

**Positive:**
- Eliminates FOMO-driven multi-agent adoption by replacing intuition with measurement.
- Reduces token waste on coordination overhead for tasks a single agent handles well.
- Provides a concrete, repeatable decision heuristic that any team can apply.
- Aligns with the L>D hypothesis (depth over breadth in token allocation).

**Negative:**
- Requires evaluation infrastructure as a prerequisite -- teams without well-defined evals cannot apply the heuristic.
- The 45% threshold is an approximation; some tasks may benefit from orchestration at lower baselines or degrade at higher ones.
- May discourage exploration of legitimate multi-agent architectures for tasks that are genuinely parallelizable but happen to have a high single-agent baseline.
- Task-specific calibration of the threshold is not yet standardized.

## Known Uses

- Google DeepMind research demonstrating independent agent error amplification (17.2x) vs. centralized coordination (4.4x).
- The "Agent Orchestrators Are Bad" analysis, which synthesized production evidence against reflexive multi-agent adoption.
- Complements the L>D hypothesis and the Specialization Theater anti-pattern findings in this KB.

## Contract

### Preconditions
Single-agent baseline performance is measurable on the target task. Evaluation criteria are well-defined and agreed upon before measurement begins. The task scope is bounded enough for meaningful performance scoring.

### Invariants
The decision to use single-agent vs. multi-agent is always backed by measured baseline performance, never by architectural preference or hype. The threshold is treated as a heuristic, not an absolute rule -- deviations require documented justification.

### Governance
Threshold evaluation is reviewed at each new task type introduction. Any override of the heuristic (choosing multi-agent despite baseline above 45%) requires explicit justification with comparative metrics showing multi-agent improvement. Results are logged for future calibration of the threshold.

### Recovery
If multi-agent coordination is deployed past the threshold and degrades performance, revert to single-agent execution. Document the regression in the System Log with before/after metrics. Update task-specific threshold calibration data if available.
