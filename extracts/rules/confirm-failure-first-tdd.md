---
title: "Confirm-Failure-First TDD — Agent Discipline Rule"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "confirm-failure-first-tdd-agent-discipline"
identification_report: "2026-04-24-identification-report.md"
extraction_date: "2026-04-24"
deployed: false
deployed_to: null
context:
  applies_to:
    - "coding agents executing TDD or BDD workflows"
    - "new-behavior test authoring (not regression tests)"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — prompt-level instruction; removal is a deletion with no migration cost"
  auditability: "high when session logs capture runner output verbatim; low when only exit codes are retained"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "No production deployments known at time of extraction. Simon Willison's own practice implicitly relies on model-internalized TDD definition rather than explicit enforcement — evidence of partial adoption via implicit delegation, not reliable enforcement."
contract:
  preconditions: "The agent is executing a TDD-style workflow (red/green, BDD, or equivalent) and has just authored a new-behavior test. A test runner is available. The agent can capture and surface the runner's failure output verbatim. The test under verification is a new-behavior test, not a regression test."
  invariants: "Before any implementation is written, the new test is run and observed to fail. The observed failure message is inspected (not only the exit code) and identifies the expected missing behavior — not an import error, missing file, or other incidental failure. The rule applies only to new-behavior tests; regression tests that are designed to pass on current code are explicitly exempt."
  governance: "Owner: Any skill, agent, or CLAUDE.md section that instructs a coding agent to use TDD. The rule must be embedded explicitly in that prompt layer (\"confirm red before green\") rather than delegated to the model's implicit definition of TDD. Consumer-side audit tooling (e.g., skill-assessment rubrics) validates that TDD-invoking skills declare a red-verification protocol. Exemption (regression tests) must be declared in the skill or instruction set that relies on it."
  recovery: "If the new test passes on first run → halt the TDD cycle; reformulate the test (existing behavior already satisfies it, or the assertion is trivial) before any implementation. If the test fails for the wrong reason (missing module, syntax error, fixture bug) → fix the incidental cause and re-run until the failure identifies the target behavior. If verification is skipped or self-reported without evidence → treat subsequent green as unverified and re-run verification before accepting the implementation."
tags:
  - "extracted-artifact"
  - "rule"
  - "tdd"
  - "agent-discipline"
  - "evaluation"
---

# Confirm-Failure-First TDD — Agent Discipline Rule

**Source:** [[confirm-failure-first-tdd-agent-discipline]]
**Form:** rule
**Extraction date:** 2026-04-24

## Condition

A coding agent is executing a TDD-style workflow (red/green, BDD given-when-then, or equivalent) and has just authored a new-behavior test. The agent is about to proceed from test-authoring to implementation.

Scope of application: **new-behavior tests only.** Regression tests — which exist specifically to pass on the current code — are explicitly exempt from this rule.

## Action

**Required:** Run the newly authored test and observe it fail. Capture the specific failure message. Confirm the failure is due to the target behavior being absent (not an import error, missing file, fixture bug, or other incidental cause). Only then proceed to implementation.

**Forbidden:** Proceeding from test authoring to implementation without having run the test and observed its failure. Self-reporting "I confirmed the test fails" without producing the specific failure output as evidence. Treating a test that passes on first run as a valid red state.

## Boundary

Enforced at the transition between the test-authoring step and the implementation step of the TDD cycle. Applies from the moment a new-behavior test is declared (e.g., in response to a `/write-test` or TDD instruction) until either:
- verified failure is observed and recorded, *or*
- the test is reformulated and re-run.

## Enforcement

- **Mechanism:** The agent must surface the specific failure output (error type, error message, relevant stack frame) in its working log before any implementation edit is made. Downstream readers (human review, hook, audit) check for this artifact.
- **Check (deterministic):** `(test_was_run == true) AND (test_outcome == fail) AND (failure_reason_identifies_target_behavior == true)`. Any branch false → violation.
- **Violation response:**
  - *First-run pass:* halt the cycle; diagnose whether the test is malformed or the behavior already exists; reformulate before any implementation.
  - *Wrong-reason failure:* fix the incidental cause (import, fixture, path) and re-run; do not accept this as verified red.
  - *Skipped verification:* any green that follows is unverified; re-run red-verification before accepting the implementation.
- **Cannot be self-certified:** Ideally enforced by a layer the agent cannot bypass — a PostToolUse hook on test commands, a harness-level verifier, or a pre-commit gate that checks for the red-state artifact in the session log. Agent self-attestation is necessary but not sufficient.

## Rationale

Classical TDD implicitly assumes a human who would notice a test passing immediately — the surprise itself is the signal. Agents follow recipes literally and do not reliably notice. A skipped red-verification produces silent false-positives: tests that look like they validate new code but actually validate nothing, which then generate false confidence when the implementation is accepted.

Simon Willison's observation: models understand "red/green TDD" as shorthand for the full workflow *including* red-verification, but implicit delegation is not reliable enforcement. For load-bearing use (agent-driven code that gets merged), the verification step must be explicit in the prompt layer.

This rule is the positive-space reformulation of a known anti-pattern. Instead of enumerating failure modes (tests that pass first run, silent verification, assumed-correct tests), the positive invariant is "red observed, then green." One rule; bounded enforcement.

## Failure Modes

- **Red-verification passes for the wrong reason.** Test fails because the file doesn't exist, not because the logic is missing. Agent interprets exit code as sufficient, implements, test still fails. Mitigation: inspect the failure *message*, not just the exit code.
- **Model skips verification silently.** Agent asserts "I confirmed the test fails" without actually running it. Mitigation: require the specific error output in the response; back with a hook that checks for it.
- **Red-verification on non-determinism.** Flaky tests may fail once and pass next. Mitigation: scope the rule to deterministic tests; for flaky tests, run N times and require a strict failure rate.
- **Overzealous application to regression tests.** The rule fails if applied to retrofit coverage — regression tests should pass on current code by definition. Mitigation: explicit exemption in scope; the rule fires on new-behavior tests only.

## Contract

### Preconditions
The agent is executing a TDD-style workflow (red/green, BDD, or equivalent) and has just authored a new-behavior test. A test runner is available. The agent can capture and surface the runner's failure output verbatim. The test under verification is a new-behavior test, not a regression test.

### Invariants
Before any implementation is written, the new test is run and observed to fail. The observed failure message is inspected (not only the exit code) and identifies the expected missing behavior — not an import error, missing file, or other incidental failure. The rule applies only to new-behavior tests; regression tests that are designed to pass on current code are explicitly exempt.

### Governance
Owner: Any skill, agent, or CLAUDE.md section that instructs a coding agent to use TDD. The rule must be embedded explicitly in that prompt layer ("confirm red before green") rather than delegated to the model's implicit definition of TDD. `/assess-skill` validates that TDD-invoking skills declare a red-verification protocol. Exemption (regression tests) must be declared in the skill or instruction set that relies on it.

### Recovery
If the new test passes on first run → halt the TDD cycle; reformulate the test (existing behavior already satisfies it, or the assertion is trivial) before any implementation. If the test fails for the wrong reason (missing module, syntax error, fixture bug) → fix the incidental cause and re-run until the failure identifies the target behavior. If verification is skipped or self-reported without evidence → treat subsequent green as unverified and re-run verification before accepting the implementation.
