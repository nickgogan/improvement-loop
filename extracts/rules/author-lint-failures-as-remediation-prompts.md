---
title: "Author Lint and Test Failures as Remediation Prompts"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "lint-test-failures-as-remediation-prompts"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "production-agent-execution.harvest-queue"
identification_report: "production-agent-execution.harvest-queue.md::lint-test-failures-as-remediation-prompts::rule::author-lint-failures-as-remediation-prompts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams authoring custom lint rules, structural tests, or CI gates that a coding agent will encounter as failures during automated work"
    - "any codebase where the same lint or test violation recurs across sessions or agents, suggesting the failure message itself isn't changing behavior"
    - "harness or tooling maintainers deciding how much authoring effort to put into a check's failure text versus its detection logic"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — failure message text; rewording a message has no migration cost beyond the next time the check fires"
  auditability: "high — a failure message either states the convention, the reason, and the fix, or it doesn't; a reviewer can check any given lint rule or test assertion's message text directly against this standard"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Reported as one team's default authoring pattern for every custom lint rule and structural test across a large multi-package workspace, adopted after observing that terse failure messages did not change repeat model behavior on the same violation."
contract:
  preconditions: "A custom lint rule, structural test, or CI check exists (or is being authored) that a coding agent may encounter as a failure. The check's underlying convention and rationale can be stated in one or two sentences — if the convention itself is unclear or contested, fix that first; a well-worded message cannot compensate for an unclear rule."
  invariants: "Every failure message states three things in the same breath the failure fires: the convention being enforced, the reason for it, and the specific fix — not just that something is wrong. A failure message that names only the symptom (what broke) without the convention (why it's wrong) and the fix (what to do instead) does not satisfy this rule. Judgment-shaped checks too fuzzy for a fixed assertion may be implemented as an explicit model-judgment call rather than left as an unenforceable convention, but any such embedded model call is scoped narrowly and does not silently expand to checks that could have been expressed mechanically."
  governance: "Owner: whoever authors or maintains the lint rule, structural test, or CI gate. Authoring the remediation-shaped message is a one-time cost per rule that pays out on every future violation — treat it as part of writing the check, not an optional polish pass. When authoring effort becomes a bottleneck at scale, delegating message-drafting to an agent (working from an internal prompting reference) is an accepted extension, provided the output is still reviewed against this rule's invariants before being shipped as the check's live message."
  recovery: "If a failure message is found to name only the symptom (a bare 'unknown type at this depth' with no convention or fix): rewrite it to state the convention, the reason, and the fix before the next release of the check. If a remediation message is found to cite a convention or pattern that has since changed (convention drift): update the message alongside the convention change — treat drifted remediation text as a defect, not a low-priority cleanup. If verbose remediation text is adding meaningful token cost on repeated CI re-triggers: trim to the minimum that still states convention + reason + fix, rather than reverting to a bare symptom message. If an embedded model-judgment check (used for checks too fuzzy for a fixed rule) becomes unreliable or drifts in scope: narrow it back to what genuinely cannot be expressed mechanically, or replace it with a deterministic check if one becomes expressible."
tags:
  - "extracted-artifact"
  - "rule"
  - "context-engineering"
  - "lint-authoring"
  - "ci-feedback"
---

# Author Lint and Test Failures as Remediation Prompts

**Source:** [[lint-test-failures-as-remediation-prompts]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A custom lint rule, structural test, or CI check exists (or is being authored) whose failure output a coding agent will read as part of its normal working loop — the highest-frequency touchpoint an agent has with "did I do this right."

## Action

**Required:** Write every failure message as if it were a prompt, not a diagnostic string. Each message states, in the same breath the failure fires:
1. The convention being enforced.
2. The reason the convention exists.
3. The specific fix to apply instead.

For checks that are genuinely too judgment-shaped for a regex or AST rule to express, an explicit model-judgment call embedded in the test is an acceptable substitute for an unenforceable convention — but this is the exception, scoped to checks that truly can't be made mechanical, not a default.

**Forbidden:** Shipping a lint rule or structural test whose failure message names only the symptom ("unknown type at this depth," "why is this function called X") without stating the convention and the fix. Treating a bare pass/fail signal as sufficient because "the rule is documented elsewhere" — a message that requires the model to go looking for context it wasn't given does not satisfy this rule.

## Boundary

Enforced at the point a lint rule, structural test, or CI gate is authored or edited — specifically, at the authoring of its failure-message text. Applies to any check whose failure output a coding agent is expected to read and act on, across the full surface of a harness that can carry text to a model: lint rules, structural tests, pre-commit hooks, review-agent feedback converted into failing tests, and equivalent CI gates.

Out of scope: failures intended purely for human consumption with no agent in the loop, and checks whose failure is never expected to recur (one-off migration scripts, for instance) where the amortization argument for authoring effort doesn't hold.

## Enforcement

- **Mechanism:** Manual authoring review — before a new lint rule or structural test ships, its failure message is checked against the three-part standard (convention, reason, fix).
- **Check (semi-deterministic):** For any given failure message, ask: does it name what's wrong (symptom), why it's wrong (convention + reason), and what to do instead (fix)? A message missing the reason or the fix is incomplete even if the symptom is clear.
- **Violation response:** A failure message found to state only the symptom is rewritten before the check ships, or flagged for rewrite if already in production and observed to have high repeat-violation rates.
- **Delegated authorship (extension):** When authoring good remediation prompts becomes its own time sink at scale, an agent may draft the message text (e.g., pointed at an internal prompting reference); the drafted message is still reviewed against this rule's three-part standard before being accepted as the check's live text.

## Rationale

A generic failure naming only the symptom tells the model nothing actionable and does not reliably change repeat behavior — the model needs the "why" and the "what instead," not just the "no." Collapsing the usual distinction between deliberately-authored prompts (CLAUDE.md, skill files) and lint/test output (assumed to be terse, machine-directed diagnostic text) turns the highest-frequency touchpoint an agent has with its own correctness into a teaching moment, at zero marginal authorship cost per future occurrence: the remediation text is written once and fires on every future violation for free. Every layer of a harness that can carry text to the model — prompts, rules files, skills, lint error messages, review-agent feedback — is a place this standard applies; lint and test failures are simply the layer that gets treated as exempt from authorial care by default, and this rule closes that gap.

## Failure Modes

- **Convention drift.** A remediation message keeps citing a rule or pattern that has since changed, the same way any embedded documentation can drift from current reality. Mitigation: treat drifted remediation text as a defect and update it alongside the convention change, not as a separate low-priority cleanup.
- **Token cost compounding at the worst moment.** Verbose remediation text in every failure adds cost exactly when a CI run may be re-triggered several times in a row. Mitigation: trim to the minimum that still states convention, reason, and fix — don't solve this by reverting to a bare symptom message.
- **Nondeterminism creep.** Embedding a model-judgment call inside a test (for genuinely fuzzy checks) introduces a costed, nondeterministic call into what is conventionally a fast deterministic gate. Mitigation: scope explicitly to checks that truly can't be expressed as a mechanical rule; if a mechanical expression later becomes possible, replace the judgment call.

## Contract

### Preconditions
A custom lint rule, structural test, or CI check exists (or is being authored) that a coding agent may encounter as a failure. The check's underlying convention and rationale can be stated in one or two sentences — if the convention itself is unclear or contested, fix that first; a well-worded message cannot compensate for an unclear rule.

### Invariants
Every failure message states three things in the same breath the failure fires: the convention being enforced, the reason for it, and the specific fix — not just that something is wrong. A failure message that names only the symptom (what broke) without the convention (why it's wrong) and the fix (what to do instead) does not satisfy this rule. Judgment-shaped checks too fuzzy for a fixed assertion may be implemented as an explicit model-judgment call rather than left as an unenforceable convention, but any such embedded model call is scoped narrowly and does not silently expand to checks that could have been expressed mechanically.

### Governance
Owner: whoever authors or maintains the lint rule, structural test, or CI gate. Authoring the remediation-shaped message is a one-time cost per rule that pays out on every future violation — treat it as part of writing the check, not an optional polish pass. When authoring effort becomes a bottleneck at scale, delegating message-drafting to an agent (working from an internal prompting reference) is an accepted extension, provided the output is still reviewed against this rule's invariants before being shipped as the check's live message.

### Recovery
If a failure message is found to name only the symptom (a bare 'unknown type at this depth' with no convention or fix): rewrite it to state the convention, the reason, and the fix before the next release of the check. If a remediation message is found to cite a convention or pattern that has since changed (convention drift): update the message alongside the convention change — treat drifted remediation text as a defect, not a low-priority cleanup. If verbose remediation text is adding meaningful token cost on repeated CI re-triggers: trim to the minimum that still states convention + reason + fix, rather than reverting to a bare symptom message. If an embedded model-judgment check (used for checks too fuzzy for a fixed rule) becomes unreliable or drifts in scope: narrow it back to what genuinely cannot be expressed mechanically, or replace it with a deterministic check if one becomes expressible.
