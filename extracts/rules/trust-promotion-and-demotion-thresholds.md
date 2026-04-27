---
title: "Trust Promotion and Demotion Thresholds — Progressive-Autonomy Discipline Rule"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "trust-calibration-progressive-autonomy-ramp"
identification_report: "agent-governance-and-trust.harvest-queue.md::trust-calibration-progressive-autonomy-ramp::rule::trust-promotion-and-demotion-thresholds"
extraction_date: "2026-04-27"
last_change_session: 82
last_change_sl: "session-82-codifier-extract-artifacts-harvest-promotion-batch"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent governance regimes that operate across multiple task types with varying stakes"
    - "deployments where review burden is high enough that uniform human-required review is unsustainable"
    - "any system where an agent's autonomy level can be configured per task type and tracked over time"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — promotions and demotions are configuration changes; the ledger keeps history; restoring prior state is a single-step operation"
  auditability: "high when promotions/demotions and execution outcomes are recorded in a ledger; medium when tracked manually; low when relied on by convention"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Anthropic's 'Trustworthy agents in practice' validates progressive-autonomy calibration as production-tested at scale (Tier 1 confirmation). The discipline of explicit promotion/demotion thresholds with a per-task-type ramp is the practitioner-documented form."
contract:
  preconditions: "An agent governance regime exists where autonomy levels can be configured per task type. Task-type taxonomy is defined or definable (e.g., documentation, research, code generation, infrastructure changes). Execution outcomes — success, failure-detected, failure-reaching-production — are observable and recordable per task type."
  invariants: "Three sub-invariants hold simultaneously: (1) **Start restrictive** — every new task type starts at the most-restrictive autonomy level the regime supports (proposal-first or human-required). No task type begins at full autonomy under any circumstance. (2) **Promote per task type, not globally** — autonomy promotions apply only to the specific task type that earned them; trust on documentation does not transfer to infrastructure. (3) **Concrete thresholds, both directions** — promotion requires meeting a stated success threshold (e.g., N consecutive successful executions; the threshold is a number, not a vibe); demotion is triggered by stated failure conditions (e.g., any failure reaching production) and is immediate, not deliberated. The promotion threshold and demotion trigger are recorded in the regime's policy."
  governance: "Owner: the policy that establishes autonomy levels and review-gate configuration for agent task types. The regime must declare (a) the closed enum of autonomy levels; (b) the promotion threshold per task type (or a per-task-type default); (c) the demotion trigger conditions (closed enum); (d) the tracking surface — a trust ledger that records executions and outcomes per task type. Audit verifies that no task type starts at full autonomy, every promotion has a threshold-met record, every demotion has a trigger-met record, and no global promotions exist."
  recovery: "If a task type was promoted without meeting the stated threshold: demote it; require re-earning the promotion by satisfying the threshold from the demotion forward. If a failure reached production but no demotion occurred: demote retroactively; investigate why the demotion trigger did not fire (ledger gap, tracking miss, policy ambiguity); close the gap. If a global promotion is discovered (autonomy raised across multiple task types based on success on one): revert to per-task-type levels; the broad promotion was unearned. If thresholds are being hit so quickly that promotions feel routine: re-evaluate whether the threshold is too low for the actual failure-detection latency — promotions earned without enough exposure to edge cases are calibration debt."
tags:
  - "extracted-artifact"
  - "rule"
  - "agent-governance"
  - "progressive-autonomy"
  - "trust-calibration"
  - "review-gate"
---

# Trust Promotion and Demotion Thresholds — Progressive-Autonomy Discipline Rule

**Source:** [[trust-calibration-progressive-autonomy-ramp]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

An agent governance regime supports configurable autonomy per task type — review-required, proposal-first, spot-check, full-autonomy, or equivalent levels. The regime spans multiple task types with varying risk profiles (documentation, research, code generation, infrastructure, security-sensitive operations). Execution outcomes are observable and can be recorded.

Scope of application: any deployment where uniform human-required review is unsustainable AND where graduated autonomy is a feasible alternative. Out of scope: deployments where every operation is high-stakes (no progressive ramp warranted) or where outcomes cannot be reliably observed (no basis for promotion/demotion).

## Action

**Required:** Apply three disciplines simultaneously.

1. **Start restrictive.** Every new task type begins at the most-restrictive autonomy level the regime supports — proposal-first, human-required, or equivalent. No task type starts at full autonomy under any circumstance, regardless of perceived risk.

2. **Promote per task type, never globally.** Autonomy promotions apply only to the specific task type that earned them. A task type's promotion does not transfer to other task types, even if they appear similar.

3. **Set concrete thresholds in both directions.**
   - **Promotion threshold:** a stated number — e.g., "N consecutive successful executions of task type T" — that must be met before autonomy is raised.
   - **Demotion trigger:** stated conditions — e.g., "any failure reaching production for task type T" — that immediately revert autonomy to a lower level.
   - Both are recorded in the regime's policy and applied uniformly.

Track every promotion, demotion, and execution outcome on a trust ledger. The ledger is the audit surface.

**Forbidden:** Starting any task type at full autonomy. Globalizing a single task type's earned trust. Using vague promotion criteria ("when it feels reliable") or vague demotion triggers ("when something seems off"). Deliberating before demotion when a stated trigger has fired.

## Boundary

Enforced at the regime-policy level (which configures autonomy per task type) and at the trust-ledger level (which records and applies promotions/demotions). The rule fires whenever a task type is created, executed, or has its autonomy level changed.

Out of scope: determining the *content* of the autonomy levels themselves (that is the regime's design), or the *exact numeric value* of the promotion threshold (that is per-team calibration). The rule fires on the *discipline*: thresholds exist, are stated, are applied.

## Enforcement

- **Mechanism:** A trust ledger records (a) task-type definitions, (b) current autonomy level per task type, (c) execution outcomes (success, failure-detected, failure-reaching-production), (d) promotion events (with threshold-met evidence), and (e) demotion events (with trigger-met evidence). Audit tooling reads the ledger and verifies the three sub-invariants are honored.
- **Check (deterministic):** For every task type `T`: `initial_autonomy(T) == most_restrictive_level` AND `for every promotion P on T: threshold_met_at(P) is recorded` AND `for every failure F on T satisfying demotion_trigger: demotion_event_at(F) is recorded` AND `no promotion of T raises autonomy on any other task type`. Any branch false → violation.
- **Violation response:**
  - *New task type started at non-restrictive level:* demote to the most-restrictive level immediately; investigate how the start-level was set; close the policy gap.
  - *Promotion without threshold-met record:* demote; require re-earning from current ledger state; investigate whether the threshold was bypassed deliberately or via a tracking gap.
  - *Demotion trigger fired but no demotion occurred:* demote retroactively; investigate why the trigger did not fire (manual override, ledger gap, ambiguous trigger definition); close the gap.
  - *Global promotion discovered (one task type's promotion applied to others):* revert each affected task type to per-type-earned level; the global was unearned for any non-source type.
- **Cannot be silently exempted:** A task type that is configured at non-restrictive autonomy at creation, or that escapes a stated demotion trigger, is in violation. The rule does not require any specific number for the threshold — it requires a *stated, applied* threshold and a *stated, immediate* demotion trigger.

## Rationale

The rule exists because autonomy decisions otherwise default to either too-strict (every operation gates on human review, defeating the agent's value) or too-lax (everything runs autonomously, accruing risk that materializes at the worst time). A progressive ramp matches review effort to actual risk by earning autonomy through observed reliability per task type.

The three sub-invariants are inseparable. Without "start restrictive," new task types ship with unearned autonomy. Without "promote per task type," success on low-stakes work transfers risk to high-stakes work. Without "concrete thresholds," promotion becomes a vibe and demotion becomes deliberation — both of which lose the discipline's value.

The "demotion is immediate" property is load-bearing. If demotion is debated when a trigger fires, the regime degrades to "we decide later," which is the failure mode the rule prevents. The trigger fires; the demotion happens; investigation comes after.

The rule is the positive-space restatement of the static-autonomy anti-pattern. Rather than enumerating ways uniform review or uniform autonomy fail (review bottleneck, missed high-stakes scrutiny, novel-task surprise, regression after agent update), the positive invariant is "start restrictive; promote per task type; threshold both directions." Three sub-rules, deterministic enforcement.

## Failure Modes

- **Threshold-too-low.** Promotion threshold (e.g., "5 successful executions") is met before edge cases have had time to surface. Mitigation: tune the threshold based on observed failure-detection latency for each task type; raise it for task types where failures are detected late.
- **Demotion deliberation.** Demotion trigger fires; team discusses whether to demote rather than demoting. Mitigation: the trigger fires the demotion mechanically; investigation is a separate, post-demotion activity. Re-promotion is the discussion path, not no-demotion.
- **Task-type collapse.** Two genuinely different task types are merged into one task type for promotion-tracking convenience; trust earned on the easier sub-type promotes the harder sub-type. Mitigation: keep task types narrow when failure profiles differ; the cost of more task types is small relative to the cost of unearned promotion.
- **Regression invisibility.** An agent update changes the agent's behavior; previously-earned trust is invalidated; the system does not detect the change. Mitigation: agent-version changes are first-class events on the ledger; all task types using the changed agent revert to a lower autonomy until re-earned (or to a verification window where outcomes are sample-checked).
- **Ledger drift.** The ledger falls behind actual execution outcomes; promotions are based on stale data. Mitigation: every execution writes to the ledger atomically with the execution itself; missing ledger writes are themselves a regime violation.
- **Promotion-by-fatigue.** Reviewers tire of reviewing a high-volume task type and approve a promotion to reduce their own load, even though the threshold has not been met. Mitigation: the threshold is the gate, not the reviewer's preference; promotion-without-threshold-met is a violation regardless of who approves it.

## Contract

### Preconditions
An agent governance regime exists where autonomy levels can be configured per task type. Task-type taxonomy is defined or definable (e.g., documentation, research, code generation, infrastructure changes). Execution outcomes — success, failure-detected, failure-reaching-production — are observable and recordable per task type.

### Invariants
Three sub-invariants hold simultaneously: (1) Start restrictive — every new task type starts at the most-restrictive autonomy level the regime supports (proposal-first or human-required). No task type begins at full autonomy under any circumstance. (2) Promote per task type, not globally — autonomy promotions apply only to the specific task type that earned them; trust on documentation does not transfer to infrastructure. (3) Concrete thresholds, both directions — promotion requires meeting a stated success threshold (e.g., N consecutive successful executions; the threshold is a number, not a vibe); demotion is triggered by stated failure conditions (e.g., any failure reaching production) and is immediate, not deliberated. The promotion threshold and demotion trigger are recorded in the regime's policy.

### Governance
Owner: the policy that establishes autonomy levels and review-gate configuration for agent task types. The regime must declare (a) the closed enum of autonomy levels; (b) the promotion threshold per task type (or a per-task-type default); (c) the demotion trigger conditions (closed enum); (d) the tracking surface — a trust ledger that records executions and outcomes per task type. Audit verifies that no task type starts at full autonomy, every promotion has a threshold-met record, every demotion has a trigger-met record, and no global promotions exist.

### Recovery
If a task type was promoted without meeting the stated threshold: demote it; require re-earning the promotion by satisfying the threshold from the demotion forward. If a failure reached production but no demotion occurred: demote retroactively; investigate why the demotion trigger did not fire (ledger gap, tracking miss, policy ambiguity); close the gap. If a global promotion is discovered (autonomy raised across multiple task types based on success on one): revert to per-task-type levels; the broad promotion was unearned. If thresholds are being hit so quickly that promotions feel routine: re-evaluate whether the threshold is too low for the actual failure-detection latency — promotions earned without enough exposure to edge cases are calibration debt.
