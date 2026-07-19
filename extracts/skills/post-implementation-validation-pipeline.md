---
title: "Post-Implementation Validation Pipeline"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "no-mistakes-post-implementation-validation-pipeline"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "verifying-agent-output.harvest-queue"
identification_report: "verifying-agent-output.harvest-queue"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Teams shipping a high volume of machine-generated code changes, where reading every diff by hand caps how fast changes can land"
    - "Workflows that need a repeatable gate between an implementing agent's first-pass change and a merged pull request"
    - "Setups running several agent sessions in parallel, where a human cannot watch every change as it is produced"
    - "Contexts that want review depth scaled to a change's risk rather than a uniform manual review of everything"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "medium — the pipeline produces a pull request that a human risk-gates before merge, so it lands nothing on its own; but a miscalibrated risk gate can let a change merge with no diff read, reversible only by revert"
  auditability: "Strong — each stage leaves an inspectable artifact: the isolation branch/worktree, a recovered-intent summary, the fresh-context review findings, the attached evidence files, and a PR body carrying intent, test method, what was found/fixed, and the risk assessment. Compliance is checkable by opening the PR."
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented by an open-source practitioner who ships 40–50 tested production changes daily through this pipeline across parallel agent sessions. Not yet instantiated as a running validation harness in this project."
contract:
  preconditions: "A first-pass change exists as a branch + commit produced by an implementing agent. The agent session (transcript/log) that produced the change is accessible for intent recovery. An isolated worktree capability is available so validation never touches the working repo. The remote main branch is reachable for rebase. A reviewer that runs in a fresh, separate context window is available. Evidence-capture appropriate to the change class (screenshot, video, log, benchmark) is available. A human reviewer is reachable for escalations and the final risk-gated review."
  invariants: "Stages run in fixed order and none is skipped. All validation runs inside the isolated worktree — the working repo state is never mutated by validation. The adversarial review runs in a context distinct from the one that produced the change (generator and reviewer are separate). Every change carries evidence proportional to its class attached to the PR before the PR is offered for merge. The PR carries a risk assessment that gates how deeply the human reviews — it never confers autonomous merge authority. Ambiguous changes with product implications are escalated to a human for decision rather than self-resolved."
  governance: "Owner: the team or system operating the pipeline. The risk-assessment rubric and the change-class → evidence-type mapping are owned, versioned, and reviewed — silent drift in either is a governance gap. The human retains merge authority and final judgment on evidence and risk. The low-risk auto-pass policy (human reads no diff) is a calibrated decision that must be periodically re-audited against a sample of shipped low-risk changes."
  recovery: "End-to-end test fails or the change is non-reproducible against recovered intent: halt before raising the PR. Recovered intent contradicts what was built: escalate to a human rather than validating against a possibly-wrong intent. Reviewer flags a product-implication ambiguity: escalate to a human decision. Babysitting auto-resolves an incoming merge conflict in a way that changes already-reviewed code: re-run the adversarial review over the post-resolution diff before merge. Risk-gate drift suspected: deep-review a sample of recently-merged low-risk changes and recalibrate the rubric."
tags:
  - "extracted-artifact"
  - "skill"
---

# Post-Implementation Validation Pipeline

**Source:** [[no-mistakes-post-implementation-validation-pipeline]]
**Form:** skill
**Extraction date:** 2026-07-19

A fixed, orchestrated pipeline that takes an implementing agent's first-pass change all the way to a clean pull request — invoked by handing the change to the pipeline instead of opening the diff. It resolves the reviewer bottleneck ("if every change requires your review, throughput is hard-capped by it") by influencing quality through process and spending human attention only at the two ends: planning up front, and judgment on the evidence and risk at the end. Several stages are independently established practice (fresh-context review, worktree isolation, distrusting agent self-report); the distinctive contribution is their composition into one deterministic rail plus two stages most workflows lack — intent recovered from the producing session, and evidence artifacts used as the review substrate instead of the diff.

## Inputs

- A first-pass change committed on a branch by an implementing agent.
- Access to the agent session that produced the change (for intent extraction).
- An isolated worktree (or equivalent) so validation runs off to the side.
- A reachable remote main branch to rebase onto.
- A reviewer that runs in a fresh, separate context window.
- Evidence-capture tooling matched to the change class (UI → screenshot/video; performance → benchmark log; logic → test log).
- A human reviewer available for escalations and the final risk-gated review.

## Outputs

- A pull request, rebased on latest main, lint-clean, with documentation updated.
- Evidence artifacts attached to the PR as proof-of-done.
- A PR body summarizing: original intent, what changed, how it was tested, what the pipeline found and fixed, and a **risk assessment** that tells the human how deeply to review.
- Escalation records for any ambiguous, product-implication decisions handed to the human.

## Steps

Stages execute in strict order; no stage is skipped.

1. **Worktree isolation.** Branch and commit, then run all validation in an isolated worktree so nothing can affect the current repo state.
2. **Intent extraction.** Analyze the agent session that produced the change to recover the *real* intent, so validation targets what was asked for, not merely what was built.
3. **Rebase-first.** Rebase onto latest remote main and resolve merge conflicts before any review, so review sees the code that will actually land.
4. **Adversarial fresh-context review.** A reviewer in its own fresh context window catches most problems. Obvious problems are self-corrected; ambiguous ones with product implications are escalated to the human.
5. **End-to-end test against intent, with evidence.** Exercise the change against the recovered intent and record evidence (screenshot, video, or log — whatever most directly shows it working); attach it to the PR.
6. **Documentation pass, lint, PR, babysitting.** Update docs, run lint, push the branch, raise the PR, then watch the PR for incoming merge conflicts and CI failures until merge.

## Failure Modes

- **Risk-assessment gaming/miscalibration.** The pipeline scores its own change low-risk and the human never looks — the gate inherits self-report unreliability one level up. Mitigate by periodically deep-reviewing a sample of "low-risk" merges.
- **Evidence theater.** A screenshot proves one path works, not that others didn't break; evidence is necessary, not sufficient.
- **Wrong intent recovered.** Intent extraction from a messy session can recover the wrong intent and then validate against it convincingly. Escalate on contradiction rather than trusting a clean-looking recovery.
- **Silent post-review changes.** Babysitting agents that auto-resolve PR conflicts can make changes that were never reviewed; re-review the post-resolution diff.

## Contract

### Preconditions
A first-pass change exists as a branch + commit produced by an implementing agent. The agent session (transcript/log) that produced the change is accessible for intent recovery. An isolated worktree capability is available so validation never touches the working repo. The remote main branch is reachable for rebase. A reviewer that runs in a fresh, separate context window is available. Evidence-capture appropriate to the change class (screenshot, video, log, benchmark) is available. A human reviewer is reachable for escalations and the final risk-gated review.

### Invariants
Stages run in fixed order and none is skipped. All validation runs inside the isolated worktree — the working repo state is never mutated by validation. The adversarial review runs in a context distinct from the one that produced the change (generator and reviewer are separate). Every change carries evidence proportional to its class attached to the PR before the PR is offered for merge. The PR carries a risk assessment that gates how deeply the human reviews — it never confers autonomous merge authority. Ambiguous changes with product implications are escalated to a human for decision rather than self-resolved.

### Governance
Owner: the team or system operating the pipeline. The risk-assessment rubric and the change-class → evidence-type mapping are owned, versioned, and reviewed — silent drift in either is a governance gap. The human retains merge authority and final judgment on evidence and risk. The low-risk auto-pass policy (human reads no diff) is a calibrated decision that must be periodically re-audited against a sample of shipped low-risk changes.

### Recovery
End-to-end test fails or the change is non-reproducible against recovered intent: halt before raising the PR. Recovered intent contradicts what was built: escalate to a human rather than validating against a possibly-wrong intent. Reviewer flags a product-implication ambiguity: escalate to a human decision. Babysitting auto-resolves an incoming merge conflict in a way that changes already-reviewed code: re-run the adversarial review over the post-resolution diff before merge. Risk-gate drift suspected: deep-review a sample of recently-merged low-risk changes and recalibrate the rubric.
