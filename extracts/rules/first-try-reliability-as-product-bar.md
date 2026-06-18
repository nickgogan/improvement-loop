---
title: "First-Try Reliability as Product Bar"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "anti-slop-reliability-standard-first-try-quality"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent products and skills assessed for production readiness"
    - "any workflow where the operator is deciding whether to ship, promote, or gate an agent capability"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "verify"
  reversibility: "trivial — a go/no-go gate; removing it is a policy change with no migration cost"
  auditability: "measurable when first-attempt success rate is tracked as a distinct metric from eventual success rate; low when only final outcomes are logged"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A product readiness review is being conducted for an agent capability or skill. A sample of representative tasks has been run and outcomes recorded. Outcomes include whether the task succeeded on the first attempt, not only whether it eventually succeeded."
  invariants: "The go/no-go decision uses first-attempt success rate as the primary gate, not eventual success rate after retries. 'Usually works' (success on 3-5 of 10 first attempts) is not sufficient to pass. Retry tolerance may be declared as a secondary threshold but does not substitute for the first-attempt gate. The gate threshold (minimum acceptable first-attempt success rate) is declared explicitly before evaluation — not adjusted after seeing the results."
  governance: "Owner: the product readiness review process for any agent capability. The first-attempt success rate metric must be collected and surfaced before any shipping decision. Evaluation rubrics for skills and agent workflows must include a first-attempt success rate field. Any capability shipped without first-attempt gate data must be flagged as ungated and treated as experimental."
  recovery: "If first-attempt success rate is below the declared threshold → do not ship; invest in scope constraint, guardrails, or error recovery until the threshold is met, then re-evaluate. If first-attempt data is absent (only eventual success rate was tracked) → treat the capability as ungated; re-run evaluation with first-attempt tracking before making a shipping decision. If the threshold itself is disputed → escalate to the product owner; do not lower the threshold to clear a failing capability."
tags:
  - "extracted-artifact"
  - "rule"
  - "agent-design"
  - "reliability"
  - "product-readiness"
---

# First-Try Reliability as Product Bar

**Source:** [[anti-slop-reliability-standard-first-try-quality]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

A product readiness review is being conducted for an agent capability, skill, or workflow. Evaluation data is available. The decision is whether to ship, promote to production, or continue development.

## Action

**Required:** Gate the shipping decision on first-attempt success rate — the fraction of representative tasks that succeed without any retry, reformulation, or human intervention. Declare the minimum acceptable threshold before evaluation begins. If first-attempt success rate is below the threshold, do not ship.

**Forbidden:** Using eventual success rate (success after N retries) as the primary shipping gate. Treating "usually works" (50-80% first-attempt success) as sufficient for a production capability. Adjusting the threshold downward after seeing evaluation results.

## Boundary

Applies at the product readiness review step — the decision point between development and production promotion. Does not apply during active development iterations, where partial reliability is expected. The rule governs the go/no-go gate, not the development process that precedes it.

The rule does not require statistical perfection. The threshold is set explicitly per capability type; the invariant is that the threshold is declared before evaluation and enforced without retroactive adjustment.

## Enforcement

- **Mechanism:** Evaluation rubrics include a first-attempt success rate field. Readiness review checklists require this field to be populated with observed data before a shipping decision is recorded.
- **Check (deterministic):** `(first_attempt_rate_measured == true) AND (threshold_declared_before_eval == true) AND (first_attempt_rate >= threshold == true)`. Any branch false → no-ship.
- **Violation response:** If the gate fails, document the gap (observed rate vs threshold), identify the failure modes driving misses, and queue targeted improvements. Re-evaluate when improvements are in place.
- **Cannot be self-certified:** The agent or skill under evaluation cannot report its own first-attempt success rate. Measurement requires an independent evaluation harness or human-observed test runs logged separately from agent self-report.

## Rationale

The agent ecosystem has developed a tolerance for non-determinism: "it usually works" has become an acceptable shipping bar as teams normalize retry loops. The compound error math (probability of N-step success = product of per-step reliability) shows why this fails at scale — a pipeline of five "usually works" steps at 70% each succeeds only 17% of the time on first attempt.

The anti-slop standard is the product discipline that follows from the math: design for first-try success through scope constraint, guardrails, and error recovery, rather than relying on retries to compensate for unreliability. This does not mean zero tolerance for failure — it means the go/no-go threshold is set on first-attempt outcomes, not eventual outcomes.

The risk of analysis paralysis (never shipping because nothing is perfect) is addressed by the explicit threshold: the builder sets the bar per capability type before evaluation. The rule enforces discipline around the declared bar, not perfection.

## Failure Modes

- **Threshold set after evaluation.** The team observes a 60% first-attempt rate and declares the threshold to be 55%. Mitigation: the threshold is a pre-evaluation commitment; any post-hoc adjustment is a governance violation requiring escalation.
- **Retry masking.** The evaluation harness counts a task as successful if it eventually succeeds, collapsing first-attempt and eventual success into one metric. Mitigation: evaluation logging must record attempt number at success; first-attempt and eventual success rates are reported separately.
- **Scope narrowing to inflate the rate.** The team narrows the evaluation task set to only the cases the agent handles well. Mitigation: the evaluation task set must be representative; coverage of the declared capability scope is a precondition for the gate.
- **Analysis paralysis.** No capability ever ships because the threshold can always be raised. Mitigation: the threshold is set by the product owner at the start of the development cycle, not raised during evaluation.

## Contract

### Preconditions
A product readiness review is being conducted for an agent capability or skill. A sample of representative tasks has been run and outcomes recorded. Outcomes include whether the task succeeded on the first attempt, not only whether it eventually succeeded.

### Invariants
The go/no-go decision uses first-attempt success rate as the primary gate, not eventual success rate after retries. "Usually works" (success on 3-5 of 10 first attempts) is not sufficient to pass. Retry tolerance may be declared as a secondary threshold but does not substitute for the first-attempt gate. The gate threshold (minimum acceptable first-attempt success rate) is declared explicitly before evaluation — not adjusted after seeing the results.

### Governance
Owner: the product readiness review process for any agent capability. The first-attempt success rate metric must be collected and surfaced before any shipping decision. Evaluation rubrics for skills and agent workflows must include a first-attempt success rate field. Any capability shipped without first-attempt gate data must be flagged as ungated and treated as experimental.

### Recovery
If first-attempt success rate is below the declared threshold → do not ship; invest in scope constraint, guardrails, or error recovery until the threshold is met, then re-evaluate. If first-attempt data is absent (only eventual success rate was tracked) → treat the capability as ungated; re-run evaluation with first-attempt tracking before making a shipping decision. If the threshold itself is disputed → escalate to the product owner; do not lower the threshold to clear a failing capability.
