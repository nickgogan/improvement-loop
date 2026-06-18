---
title: "Never Reveal Implementation Scope to Validation Agent"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "holdout-validation-pattern-blind-regression"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent workflows that include a validation or QA step following an implementation step"
    - "any pipeline where one agent builds and a separate agent (or session) validates"
  platform_coupling: "agnostic"
  autonomy: "autonomous-only"
  stage: "verify"
  reversibility: "low — removing the holdout constraint reintroduces sycophantic validation; workflow reconfiguration required"
  auditability: "high — the holdout constraint is a workflow configuration setting; auditors can inspect whether the validate node is granted access to PR descriptions, git history, or branch names"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Production use by StrongDM (dark factory). Cole Medin's public Archon implementation is a reference. Not yet adopted in MetaSystem workflows."
contract:
  preconditions: "An implementation workflow has completed and produced a codebase change. A separate validation agent or session exists. A full regression test suite is available that can be run against the codebase."
  invariants: "The validation agent never receives the PR description, git commit messages, branch name, or issue description. The validation session is fresh — no context continuation from the implementation session. The validator runs the full regression suite, not a targeted subset scoped to the just-implemented feature."
  governance: "Workflow configuration for the validate node must explicitly deny access to git history, PR metadata, and branch names. Any artifact directory naming convention must not encode implementation scope (e.g., no feature-named output directories passed to the validator). Pre-launch audit of the validate node's input contract must confirm holdout."
  recovery: "If the validator's output contains phrases that indicate it inferred implementation scope despite holdout, auto-fail the PR and label it needs-human review. If pre-existing test failures are detected by the blind validator, triage separately as technical debt — do not conflate with the current PR's regressions."
tags:
  - "extracted-artifact"
  - "rule"
  - "validation"
  - "evaluation"
  - "agent-discipline"
  - "sycophancy"
---

# Never Reveal Implementation Scope to Validation Agent

**Source:** [[holdout-validation-pattern-blind-regression]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent pipeline includes a validation step that runs after an implementation step. The same pipeline or a downstream agent is responsible for determining whether the implementation is correct and ready to merge.

## Action

**Required:** Run the validation step in a fresh context session with no access to the implementation's PR description, git commit messages, branch names, or issue descriptions. Provide only the codebase state and the test script. The validator must arrive at its verdict independently.

**Forbidden:** Passing the PR description, implementation rationale, or any scope-revealing artifact to the validation agent. Reusing the implementation agent's context window for validation. Running only the tests scoped to the just-implemented feature (rather than the full regression suite).

## Boundary

Enforced at the boundary between implementation completion and validation start. Applies to every automated validation step in any agent pipeline that produces codebase changes. Exemption: human-in-the-loop review where a human reads both the PR and the test results; the human is not subject to sycophancy in the same mechanical way as an agent.

## Enforcement

- **Mechanism:** Workflow configuration for the validate node must explicitly deny access to git history, PR metadata, and branch names. Implemented as a `fresh=true` session setting (Archon pattern) or equivalent isolation in the target harness.
- **Check (deterministic):** `(validator_session_has_pr_description == false) AND (validator_session_has_git_history == false) AND (validator_session_has_branch_name == false) AND (test_scope == full_regression_suite)`. Any branch false → violation.
- **Violation response:** Treat validation output as untrustworthy. Re-run with holdout constraint enforced before acting on the result.
- **Cannot be self-certified:** Holdout must be enforced by workflow architecture — a configuration that blocks access — not by asking the validation agent not to read context it has access to.

## Rationale

LLMs are systemically sycophantic in verification when they know what they just built. An implementation agent that also performs validation will interpret ambiguous test results charitably, rationalize edge case failures, and anchor on the implementation's stated intent. The holdout pattern eliminates this failure mode structurally: a validator with no knowledge of the implementation cannot be sycophantic about it. If the feature is broken, blind regression testing catches it because the validator has no intent to confirm.

This is the machine equivalent of the ML holdout set: the validator was never exposed to the implementation decisions, so it cannot have accumulated bias toward them.

## Failure Modes

- **Blind validator flags pre-existing failures.** Regressions unrelated to the current PR appear as new failures. Mitigation: maintain a baseline test-failure manifest; diff the validation report against baseline before routing to the PR author.
- **Intent vs. regression ambiguity.** Without knowing the implementation, the validator cannot distinguish intentional behavior change from regression. Mitigation: maintain a comprehensive acceptance test suite as the objective ground truth; acceptance tests encode expected behavior, removing the need for the validator to infer intent.
- **Subtle context leakage.** Artifact directory naming conventions (e.g., feature-named output folders) can partially reveal scope to the validator. Mitigation: use anonymous or hash-named output directories; audit the validator's input contract before launch.
- **Holdout breaks on git access.** If the fresh session can read git history, branch names, or PR descriptions via tool access, the constraint fails silently. Mitigation: explicitly enumerate and block these tools at the validate node level.

## Contract

### Preconditions
An implementation workflow has completed and produced a codebase change. A separate validation agent or session exists. A full regression test suite is available that can be run against the codebase.

### Invariants
The validation agent never receives the PR description, git commit messages, branch name, or issue description. The validation session is fresh — no context continuation from the implementation session. The validator runs the full regression suite, not a targeted subset scoped to the just-implemented feature.

### Governance
Workflow configuration for the validate node must explicitly deny access to git history, PR metadata, and branch names. Any artifact directory naming convention must not encode implementation scope. Pre-launch audit of the validate node's input contract must confirm holdout.

### Recovery
If the validator's output contains phrases that indicate it inferred implementation scope despite holdout, auto-fail the PR and label it needs-human review. If pre-existing test failures are detected by the blind validator, triage separately as technical debt — do not conflate with the current PR's regressions.
