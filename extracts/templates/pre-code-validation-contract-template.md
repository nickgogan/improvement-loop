---
title: "Pre-Code Validation Contract Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "pre-code-validation-contracts-dual-blind-validators"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-architecture-decisions.harvest-queue"
identification_report: "agent-architecture-decisions.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "complex, multi-feature builds where correctness needs to be defined before any implementation exists, so that verification checks the plan rather than confirming whatever the code happened to do"
    - "projects large enough to decompose into many discrete features, where a single reviewer skimming the diff cannot realistically hold the full correctness surface in mind"
    - "teams that want an independent, adversarial check on both code quality and actual runtime behavior, rather than relying on one reviewer or one test suite to catch everything"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "low — the document itself is cheap to edit or version, but an under-specified or wrong contract still gets faithfully validated against; the cost shows up downstream as validation that passes against the wrong definition of correct, not as difficulty changing the document."
  auditability: "high — every feature is traceable to the specific assertions that cover it, and both validator runs produce an explicit record (pass/fail per assertion, follow-up items created) that a reviewer can check against the contract without needing to have watched the work happen."
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Reported as production-tested — described as the primary reason a multi-day autonomous build could run without drifting, with most of the build's wall-clock time spent in the behavioral (user-testing) validator. Not yet observed as a standalone reusable document format outside that one production system."
contract:
  preconditions: "A person or planning agent is scoping a project or milestone before any implementation exists. The project decomposes into discrete, nameable features. Two independent validator roles can be run with no visibility into the implementation under test — either two separate people, two separate agent sessions with no shared context, or a human plus an isolated agent session."
  invariants: "Every feature has at least one assertion, and the sum of all features' assertions covers the full contract — no feature is left unassigned. The contract is written and frozen before implementation begins; it is not backfilled from what the code ends up doing. Both validators run after every milestone, and neither validator is given access to the implementation, the other validator's findings, or planning-time reasoning that would let it infer implementation details."
  governance: "Owner: whoever scopes the project or milestone — the planner, orchestrator, or lead who has visibility into the full feature set. That owner is responsible for keeping the contract complete (every feature covered) and for not relaxing the blind-isolation constraint between validators for convenience. Any downstream process that accepts a milestone as 'done' gates on both validator runs having completed against this contract, not on either validator's judgment alone."
  recovery: "If a validator reports a failure, treat it as expected, normal course — create a follow-up feature or fix rather than treating first-pass failure as a process breakdown. If a validator's failure looks wrong, first check whether the contract itself was under-specified or mis-scoped before assuming the implementation is at fault — a wrong contract still gets faithfully validated against. If either validator turns out to have had implementation visibility (a context leak), treat every validation run made under that leak as unverified and re-run after isolation is restored."
tags:
  - "extracted-artifact"
  - "template"
  - "verification"
  - "evaluation"
  - "adversarial-validation"
---

# Pre-Code Validation Contract Template

**Source:** [[pre-code-validation-contracts-dual-blind-validators]]
**Form:** template
**Extraction date:** 2026-07-19

## Variables

| Variable | Type | Description |
|---|---|---|
| `{{PROJECT_ID}}` | string | Identifier of the project or milestone this contract covers. |
| `{{FEATURE_ID}}` | string (repeated, one per feature) | Identifier of a discrete feature within the project's scope. |
| `{{ASSERTION_ID}}` | string (repeated, one or more per feature) | Identifier of a single testable assertion. Assertion IDs are the atomic unit of the contract — a complex project may carry hundreds. |
| `{{ASSERTION_TEXT}}` | string | The assertion itself, stated as a checkable claim about correct behavior — independent of how it will be implemented. |
| `{{COVERING_FEATURES}}` | list of `{{FEATURE_ID}}` | Which feature(s) this assertion applies to. Used to compute coverage completeness: every `{{FEATURE_ID}}` must appear in at least one assertion's `{{COVERING_FEATURES}}`. |
| `{{SCRUTINY_VALIDATOR_RESULT}}` | per-assertion: pass / fail / not-yet-run, plus notes | Outcome from the validator that checks tests, type-checking, lint, and code-review — without having seen the implementation's design intent, only the code and the contract. |
| `{{USER_TESTING_VALIDATOR_RESULT}}` | per-assertion: pass / fail / not-yet-run, plus notes | Outcome from the validator that drives the running application end-to-end (or performs the equivalent live walkthrough for non-UI systems) and checks functional behavior against the assertion — without having seen the implementation code. |
| `{{BLIND_ISOLATION_CONFIRMED}}` | boolean | Whether both validators ran with no access to the implementation, to each other's findings, or to planning-time reasoning that would leak implementation details. False or unknown invalidates the run. |
| `{{FOLLOW_UP_ITEMS}}` | list of strings | Features or fixes created in response to a validator failure. Expected to be non-empty on most runs — a milestone passing every assertion on the first attempt is the exception, not the baseline. |

## Body

```
PRE-CODE VALIDATION CONTRACT: {{PROJECT_ID}}

FEATURES AND ASSERTIONS
For each {{FEATURE_ID}}:
  - {{ASSERTION_ID}}: {{ASSERTION_TEXT}}
    covers: {{COVERING_FEATURES}}

COVERAGE CHECK
Every {{FEATURE_ID}} appears in {{COVERING_FEATURES}} of at least one assertion: [confirm before freezing the contract]

--- After each milestone ---

SCRUTINY VALIDATOR RUN
Per assertion: {{SCRUTINY_VALIDATOR_RESULT}}

USER-TESTING VALIDATOR RUN
Per assertion: {{USER_TESTING_VALIDATOR_RESULT}}

BLIND ISOLATION CONFIRMED: {{BLIND_ISOLATION_CONFIRMED}}

FOLLOW-UP ITEMS CREATED
{{FOLLOW_UP_ITEMS}}
```

## Usage

Write this contract during planning, before any implementation exists, then re-run its validation section after every milestone.

1. **Decompose the project into features, then write assertions per feature — not the reverse.** Start from what must be true, not from what the code will do. If an assertion can only be stated by looking at existing code, it belongs to the old "tests confirm decisions" failure mode this template exists to avoid.
2. **Check coverage completeness before freezing the contract.** Every `{{FEATURE_ID}}` must appear in at least one assertion's `{{COVERING_FEATURES}}`. An uncovered feature is a gap in the contract, not an acceptable omission.
3. **Freeze the contract before implementation begins.** Assertions may be clarified if ambiguous, but should not be quietly loosened to match what got built.
4. **Run both validators after every milestone, never just one.** The scrutiny validator (tests, type-checking, lint, code review) and the user-testing validator (live, end-to-end functional check) cover different failure surfaces — a system can pass one and fail the other.
5. **Maintain blind isolation between validators and the implementation.** Neither validator should have access to the implementation's design reasoning, source code walkthroughs, or the other validator's findings before it runs. Confirm `{{BLIND_ISOLATION_CONFIRMED}}` explicitly rather than assuming it held.
6. **Expect failure on the first run.** A milestone clearing every assertion on the first attempt is the exception. Record `{{FOLLOW_UP_ITEMS}}` as standard course, not as a sign the process failed.

## Variation Axis

What drives a different rendering of this template:

- **Assertion granularity.** A small project might carry a dozen assertions; a complex one, hundreds. Coarser assertions are cheaper to write and check but catch less; finer assertions cost more to maintain but shrink the blind spot between "assertion passed" and "feature actually correct."
- **Validator identity.** The scrutiny and user-testing roles can be filled by two people, two isolated agent sessions, or one of each — what matters is independence and blindness to the implementation, not who or what performs the check. Using genuinely different reasoning sources for the two roles (rather than the same model or reviewer twice) reduces the chance both share the same blind spot.
- **Live-execution depth for the user-testing validator.** For a UI-driven system this is literal end-to-end interaction (filling forms, clicking through flows); for a non-interactive system (API, batch pipeline, library) the equivalent is a live invocation against real inputs rather than a mock. The heavier the live-execution check, the more wall-clock time it costs — this is typically the dominant cost of the whole approach and should be budgeted for accordingly.
- **Coverage-completeness enforcement.** Whether the "every feature covered" check is a manual read-through of the contract or a mechanical check (e.g., a script that verifies every `{{FEATURE_ID}}` appears in some `{{COVERING_FEATURES}}` list) is a variation point independent of the contract's content.

## Contract

### Preconditions
A person or planning agent is scoping a project or milestone before any implementation exists. The project decomposes into discrete, nameable features. Two independent validator roles can be run with no visibility into the implementation under test — either two separate people, two separate agent sessions with no shared context, or a human plus an isolated agent session.

### Invariants
Every feature has at least one assertion, and the sum of all features' assertions covers the full contract — no feature is left unassigned. The contract is written and frozen before implementation begins; it is not backfilled from what the code ends up doing. Both validators run after every milestone, and neither validator is given access to the implementation, the other validator's findings, or planning-time reasoning that would let it infer implementation details.

### Governance
Owner: whoever scopes the project or milestone — the planner, orchestrator, or lead who has visibility into the full feature set. That owner is responsible for keeping the contract complete (every feature covered) and for not relaxing the blind-isolation constraint between validators for convenience. Any downstream process that accepts a milestone as "done" gates on both validator runs having completed against this contract, not on either validator's judgment alone.

### Recovery
If a validator reports a failure, treat it as expected, normal course — create a follow-up feature or fix rather than treating first-pass failure as a process breakdown. If a validator's failure looks wrong, first check whether the contract itself was under-specified or mis-scoped before assuming the implementation is at fault — a wrong contract still gets faithfully validated against. If either validator turns out to have had implementation visibility (a context leak), treat every validation run made under that leak as unverified and re-run after isolation is restored.
