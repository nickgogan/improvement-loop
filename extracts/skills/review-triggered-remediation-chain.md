---
title: "Review-Triggered Remediation Chain"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "review-triggered-remediation-dispatch"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "orchestrators running code review followed by automated remediation of identified issues"
    - "any evaluation step that produces a structured issue list and should chain into dispatch rather than returning control to a human router"
    - "skills or workflows implementing builder-validator patterns where validation failures trigger automated fixes"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "medium — once the review-and-fix chain is integrated into a workflow, removing it requires rerouting the review output back to a human triage step; the fixes already applied cannot be automatically undone"
  auditability: "high when the remediation report records each issue, its severity, the fix agent assigned, and the post-fix verification result; low when only a final pass/fail is surfaced"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Documented from Superpowers workflow (Eric Tech tutorial, BookZero.ai). Convergently present in GSD's /gsd-code-review-fix skill (REVIEW.md → fixer agents per finding → REVIEW-FIX.md). Pattern is converging across frameworks. No standalone MetaSystem implementation yet."
contract:
  preconditions: "A code or specification artifact is available for review. A review skill or agent is callable and produces a structured issue list with severity classifications. At least one fix agent is available and can receive an issue description plus relevant code context. The reviewed artifact is in a state where targeted fixes can be applied without breaking in-progress work by other agents."
  invariants: "Review produces a structured issue list before any fix is dispatched. Each issue in the list has a severity classification before dispatch. Fix agents are dispatched per issue, not per batch — each fix agent receives exactly one issue plus its relevant context. Post-fix verification is run for each fix before closing the issue. A remediation report is produced summarizing all issues found, fixes applied, and issues deferred."
  governance: "Owner: the orchestrator or workflow designer integrating this skill. Severity thresholds for auto-dispatch must be defined before the chain is activated — issues above the threshold are auto-dispatched; issues below are surfaced for human decision. Human review of the completed remediation report is required before the fixed artifact is accepted as production-ready. This skill does not replace a human code review gate; it removes the human from the triage-and-routing step only."
  recovery: "If a fix agent introduces a new bug → run the full test suite after all fixes complete; revert the specific fix if tests fail; re-dispatch the fix agent with expanded context including the failed test output. If a severity misclassification causes a cosmetic issue to be auto-fixed unnecessarily → log as a calibration failure; adjust the severity rubric used by the review skill. If fix agents produce conflicting changes to the same file → detect at post-fix merge time; resolve sequentially with the later fix agent receiving the current (already-modified) file as context. If the review skill is unavailable → halt; do not attempt manual issue enumeration as a substitute."
tags:
  - "extracted-artifact"
  - "skill"
  - "orchestration"
  - "code-review"
  - "remediation"
  - "multi-agent"
---

# Review-Triggered Remediation Chain

**Source:** [[review-triggered-remediation-dispatch]]
**Form:** skill
**Extraction date:** 2026-05-25

A procedural skill for chaining code (or specification) review directly into automated remediation. The review step is a trigger, not a terminus: the issue list it produces becomes the dispatch queue for fix agents. The human gate shifts from "which issues do I route to a fixer?" to "are the automated fixes correct?"

## Inputs

| Input | Type | Required | Notes |
|-------|------|----------|-------|
| `artifact` | File path or code block | Yes | The code, spec, or document to be reviewed |
| `review_skill` | Skill reference or agent | Yes | The review agent/skill that produces the issue list |
| `fix_agent` | Agent reference | Yes | The agent dispatched per issue to apply a fix |
| `severity_threshold` | Enum: `critical`, `important`, `informational` | Yes | Minimum severity for auto-dispatch; issues below threshold are deferred |
| `spec_context` | File path(s) | No | Architectural constraints or design rationale to give fix agents; prevents fixes that satisfy the review finding but violate design intent |
| `test_suite` | Command or script path | No | Test suite run after all fixes complete; if omitted, final verification is manual |
| `parallel_dispatch` | Boolean | No | Whether to dispatch fix agents in parallel (default: false — sequential to avoid file conflicts) |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `fixed_artifact` | File or code block | The reviewed artifact with all auto-dispatched fixes applied |
| `remediation_report` | Structured document | Lists every issue found, its severity, whether it was auto-dispatched or deferred, the fix applied, and the post-fix verification result |
| `deferred_issues` | List | Issues below the severity threshold, surfaced for human decision |
| `test_results` | Log | Output of the test suite run after all fixes, if provided |

## Steps

### Step 1 — Run Review

Invoke `review_skill` on `artifact`. The review skill must produce a **structured issue list** — a machine-readable enumeration of issues, each with:
- Issue identifier
- Severity classification (critical / important / informational)
- Issue description (plain English)
- Relevant code location (file path and line range, or equivalent)

If the review skill produces only narrative output, halt and request structured output before proceeding.

### Step 2 — Partition by Severity Threshold

Divide the issue list into two buckets:
- **Auto-dispatch queue:** issues at or above `severity_threshold`
- **Deferred list:** issues below `severity_threshold`

If the auto-dispatch queue is empty, skip to Step 5 (produce remediation report with deferred list only).

### Step 3 — Dispatch Fix Agent Per Issue

For each issue in the auto-dispatch queue (sequentially unless `parallel_dispatch: true`):

1. Prepare a fix agent context containing:
   - The issue description
   - The relevant code location (file + line range)
   - The current state of the file (post any previous fix in this session)
   - `spec_context` files, if provided
2. Dispatch `fix_agent` with this context.
3. Receive the fix result (modified file or patch).
4. Apply the fix to the artifact.
5. Run post-fix verification for this specific issue (re-run the targeted review check if the review skill supports it; otherwise confirm the symptom is no longer present).
6. Record in the remediation report: issue ID, fix applied, verification result.

If `parallel_dispatch: true`, fan out all fix agents simultaneously and merge results. On merge conflict (two agents modified the same file), fall back to sequential dispatch for the conflicting pair.

### Step 4 — Run Full Test Suite

If `test_suite` is provided, run it against the fully-fixed artifact. Record the output. If tests fail, identify which fix introduced the failure (bisect if necessary), revert that specific fix, and re-dispatch the fix agent with expanded context including the failure output.

### Step 5 — Produce Remediation Report

Assemble the remediation report with:
- Total issues found
- Issues auto-dispatched and fixed
- Issues auto-dispatched but reverted (with failure reason)
- Issues deferred (with severity and description, for human decision)
- Test suite results (pass/fail summary and log path)

Surface the report and deferred issues to the human for review before accepting the fixed artifact as production-ready.

## Failure Modes

- **Fix agent introduces a new bug.** The fix agent's context is narrow (one issue + relevant code). It may satisfy the review finding while breaking adjacent code outside its context. Mitigation: run the full test suite after all fixes (Step 4); provide `spec_context` to fix agents to constrain the solution space.
- **Severity misclassification inflates the auto-dispatch queue.** If the review skill over-classifies issues as critical/important, cosmetic issues are auto-fixed unnecessarily, wasting tokens and potentially introducing unnecessary changes. Mitigation: review and calibrate the severity rubric before production use; log misclassifications for rubric improvement.
- **Cascading file conflicts when parallel dispatch is enabled.** Two fix agents independently modify the same file. Mitigation: default to sequential dispatch; use parallel dispatch only for issues confirmed to affect distinct files.
- **Fix bypasses design intent.** The fix agent knows what the code should look like to satisfy the review finding, but does not know the architectural rationale. It may choose a solution that violates constraints not expressed in the code. Mitigation: always provide `spec_context`; treat any fix that touches architectural boundaries as requiring human review before acceptance.
- **Review skill produces unstructured output.** The chain cannot proceed without a machine-readable issue list. Mitigation: validate review output format in Step 1 before dispatching any fix agents; if unstructured, halt and request reformatting.

## Contract

### Preconditions
A code or specification artifact is available for review. A review skill or agent is callable and produces a structured issue list with severity classifications. At least one fix agent is available and can receive an issue description plus relevant code context. The reviewed artifact is in a state where targeted fixes can be applied without breaking in-progress work by other agents.

### Invariants
Review produces a structured issue list before any fix is dispatched. Each issue in the list has a severity classification before dispatch. Fix agents are dispatched per issue, not per batch — each fix agent receives exactly one issue plus its relevant context. Post-fix verification is run for each fix before closing the issue. A remediation report is produced summarizing all issues found, fixes applied, and issues deferred.

### Governance
Owner: the orchestrator or workflow designer integrating this skill. Severity thresholds for auto-dispatch must be defined before the chain is activated — issues above the threshold are auto-dispatched; issues below are surfaced for human decision. Human review of the completed remediation report is required before the fixed artifact is accepted as production-ready. This skill does not replace a human code review gate; it removes the human from the triage-and-routing step only.

### Recovery
If a fix agent introduces a new bug → run the full test suite after all fixes complete; revert the specific fix if tests fail; re-dispatch the fix agent with expanded context including the failed test output. If a severity misclassification causes a cosmetic issue to be auto-fixed unnecessarily → log as a calibration failure; adjust the severity rubric used by the review skill. If fix agents produce conflicting changes to the same file → detect at post-fix merge time; resolve sequentially with the later fix agent receiving the current (already-modified) file as context. If the review skill is unavailable → halt; do not attempt manual issue enumeration as a substitute.
