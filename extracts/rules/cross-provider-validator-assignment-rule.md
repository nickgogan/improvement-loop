---
title: "Cross-Provider Validator Assignment — Bias-Decorrelation Rule"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "droid-whispering-per-role-model-assignment"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-architecture-decisions.harvest-queue"
identification_report: "agent-architecture-decisions.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "multi-agent or multi-step systems where one model implements or produces work and a separate model validates, reviews, or checks it"
    - "teams designing adversarial validation or QA stages meant to catch the implementer's mistakes rather than agree with them"
    - "architects choosing per-role model-and-provider assignments across a pipeline (planner / implementer / validator) where the system is not locked to one provider"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "low — pointing the validator at a different provider means standing up a second API/billing/tool-calling integration; reverting collapses back to same-provider validation, but the engineering surface added is non-trivial to unwind cleanly"
  auditability: "high — the validator's model and provider are configuration values; an auditor can read the per-role assignment and confirm the validator's provider differs from the implementer's, without inspecting model behavior"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Named and practiced internally at a coding-agent company ('droid whispering'), presented as evolving team judgment and a customizable default rather than benchmarked assignment; the cross-provider-for-validation move is the distinguishing element. Not yet adopted by the extracting system."
contract:
  preconditions: "A pipeline has a distinct validation/review role that checks the output of an implementation role, and per-role model choice is configurable (the system is model-agnostic, not locked to a single provider). At least two model providers are operationally available."
  invariants: "The model that validates or reviews an implementation runs on a different model *provider* than the model that produced the implementation. The distinction is provider-level — different training data — not merely a different model within the same family or a different context window on the same model."
  governance: "Owner: whoever configures per-role model assignment in the multi-agent system. The validator's provider must be explicit and differ from the implementer's. Role-to-provider defaults are a customizable starting point, revisited as model capabilities shift — not a frozen lookup table. The decorrelation assumption (different providers have meaningfully uncorrelated training data and failure modes) is itself reviewed periodically as frontier providers converge."
  recovery: "If validator and implementer share a provider, reassign the validator to a different provider. If no second provider is operationally available, treat bias-decorrelation as unmet: compensate with other validator-independence mechanisms (e.g., information holdout) and record the residual shared-training-data risk rather than assuming the validation is unbiased. If cross-provider validation is measured to catch no more issues than same-provider, downgrade this to an optional optimization for that context."
tags:
  - "extracted-artifact"
  - "rule"
---

# Cross-Provider Validator Assignment — Bias-Decorrelation Rule

**Source:** [[droid-whispering-per-role-model-assignment]]
**Form:** rule
**Extraction date:** 2026-07-19

> **Related rule (same family, orthogonal mechanism):** [[holdout-validation-pattern-blind-regression]] ("Never Reveal Implementation Scope to Validation Agent") also keeps the validator unbiased, but by withholding *information* — the PR description, git history, branch names, a fresh session — so the validator cannot be sycophantic about implementation intent it is aware of. This rule withholds nothing informational; it constrains *which model* runs the validator, requiring a different provider so shared training-data blind spots don't correlate between builder and checker. Ruled create-new (not a merge into the holdout rule) per the 2026-07-19 extension-proposals report — the two constraints are orthogonal and jointly necessary: a maximally unbiased validator wants both (full information holdout *and* cross-provider assignment); neither implies the other.

## Condition

A pipeline has a distinct validation, review, or QA role whose job is to catch mistakes in the output of an implementation role, and per-role model choice is configurable (the system is model-agnostic rather than locked to one provider). Fires whenever the per-role model assignment for such a system is being designed or reviewed.

## Action

**Required:** Assign the validation/review role to a model from a **different provider** than the model that produced the implementation being checked. The requirement is provider-level — different training data — not merely a different model in the same family or a different context window on the same model.

**Forbidden:** Running the validator on the same provider (or the same model) as the implementer and treating the result as an independent, unbiased check. Justifying same-provider validation purely on cost or capability grounds while claiming the validation is bias-independent.

**Permitted:** Same-provider assignment as an explicit, acknowledged fallback when no second provider is operationally available — but only with the residual shared-training-data risk recorded and other independence mechanisms compensating.

## Boundary

Enforced at per-role model-assignment configuration time in a multi-agent / multi-step system, and at any subsequent review of that assignment. Applies to the implementer→validator seam specifically; it does not prescribe provider diversity for roles that are not checking each other's work (e.g., planner and implementer may share a provider without violating this rule).

## Enforcement

- **Mechanism:** Inspect the per-role model-assignment configuration. Read the implementer's provider and the validator's provider.
- **Check:** `provider(validator) != provider(implementer)`. Equality is a violation (unless the acknowledged-fallback exception is explicitly recorded).
- **Violation response:** Reassign the validator to a different provider. If none is available, mark bias-decorrelation as unmet, lean on information-holdout and other independence mechanisms, and log the residual risk — do not silently claim independent validation.

## Rationale

A validator built on the same model family as the implementer shares that family's training-data blind spots: the two can be wrong in the same way, so the checker fails to flag errors it would itself have made. Assigning the validator to a *different provider* decorrelates those blind spots — the check is independent in the way that matters (different training data), not just independent in context. This is a distinct axis from ordinary task-based or cost-based model routing, which never captures the "decorrelate the validator from the implementer" rationale at all.

The broader framing: a model-agnostic architecture is "only as strong as its weakest link" — locking into one provider constrains the whole system to that family's weakest capability, whereas a well-structured multi-role system (validation contracts, milestone checkpoints, cross-provider assignment) can let different providers cover each other's gaps. The role-to-provider assignment is offered as a discipline to develop and customize per project, not a fixed lookup table.

## Failure Modes

- **Operational surface multiplication.** Cross-provider architectures multiply auth, rate-limit, cost-tracking, and tool-call-semantics surfaces. Mitigation: weigh the coordination cost against the validation-independence benefit; the rule applies where an independent validator is load-bearing, not everywhere.
- **Convention calcification.** Role-to-provider defaults set once by one person risk calcifying into unexamined convention. Mitigation: the governance clause requires periodic revisiting as models change; treat defaults as a starting point, not an answer.
- **Weakening decorrelation assumption.** As frontier providers converge on similar data and techniques, "different provider ⇒ uncorrelated blind spots" may weaken with no visible signal. Mitigation: periodically re-examine the assumption; where possible, measure whether cross-provider validation actually catches more issues than same-provider.

## Contract

### Preconditions
A pipeline has a distinct validation/review role that checks the output of an implementation role, and per-role model choice is configurable (the system is model-agnostic, not locked to a single provider). At least two model providers are operationally available.

### Invariants
The model that validates or reviews an implementation runs on a different model *provider* than the model that produced the implementation. The distinction is provider-level — different training data — not merely a different model within the same family or a different context window on the same model.

### Governance
Owner: whoever configures per-role model assignment in the multi-agent system. The validator's provider must be explicit and differ from the implementer's. Role-to-provider defaults are a customizable starting point, revisited as model capabilities shift — not a frozen lookup table. The decorrelation assumption (different providers have meaningfully uncorrelated training data and failure modes) is itself reviewed periodically as frontier providers converge.

### Recovery
If validator and implementer share a provider, reassign the validator to a different provider. If no second provider is operationally available, treat bias-decorrelation as unmet: compensate with other validator-independence mechanisms (e.g., information holdout) and record the residual shared-training-data risk rather than assuming the validation is unbiased. If cross-provider validation is measured to catch no more issues than same-provider, downgrade this to an optional optimization for that context.
