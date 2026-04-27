---
title: "Comprehension Gate at PR Review"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "dark-code-organizational-capability-problem"
identification_report: "agent-governance-and-trust.harvest-queue.md::dark-code-organizational-capability-problem::skill::comprehension-gate-at-pr-review"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "code review pipelines that include AI-generated or AI-assisted code changes where comprehension can decouple from authorship"
    - "PR review workflows seeking to make architectural questions immediately legible to reviewers rather than requiring them to surface questions from scratch"
    - "engineering teams using AI-assisted review as a flywheel that feeds back into eval suites to improve code quality and review quality simultaneously"
  platform_coupling: "agnostic"
  autonomy: "supervised"
  stage: "verify"
  reversibility: "trivial — the skill produces a structured comprehension report attached to the PR; it does not modify code, merge state, or repository configuration"
  auditability: "high — every gate run produces a per-question artifact (question, evidence cited, verdict) attached to the PR; verdicts and unanswered questions are preserved as first-class outputs that feed back into eval suites"
  evidence_strength: "Moderate"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A PR diff is available and readable. The senior-engineer-style question set is defined before invocation (dependency rationale, caching topology, separation-of-concerns implications, failure-mode handling, retry semantics, etc.). At least one human reviewer is identified as the gate's recipient. Optional eval-feedback destination is configured if the gate output is to feed back into eval suites."
  invariants: "Every question in the configured set runs against the diff — the gate does not skip questions even when no obvious match is found. Each question's verdict cites concrete evidence from the diff or surrounding code. The gate's output is a recommendation to the human reviewer, never an autonomous merge decision. Unanswered questions and low-confidence verdicts are surfaced as explicit blockers, not silently passed. The gate never modifies the diff, the PR description, or repository state."
  governance: "Owner: the team or system that maintains the question set and invokes the gate. Question-set changes are versioned and reviewed — drift in the question set without review is treated as a governance gap. The gate's output is advisory; the human reviewer remains the merge authority. Eval-feedback emission is opt-in per repository; teams that emit must designate a destination and a retention policy."
  recovery: "If the diff is unreadable or partial: halt and return a structured incomplete-diff verdict with the unread regions named. If a question produces no evidence in the diff: emit an explicit no-evidence verdict with the question identifier — do not synthesize a verdict from prior commits. If the question set is missing or empty: halt before running and prompt the caller to configure the question set. If reviewer latency exceeds the configured threshold: surface the gate output as a standalone report so the bottleneck does not silently extend merge time."
tags:
  - "extracted-artifact"
  - "skill"
  - "code-review"
  - "comprehension"
  - "pr-gate"
  - "ai-assisted-review"
---

# Comprehension Gate at PR Review

**Source:** [[dark-code-organizational-capability-problem]]
**Form:** skill
**Extraction date:** 2026-04-27

## Inputs

- **PR diff:** The full set of changes under review, including added, modified, and deleted regions, with surrounding context lines sufficient to understand call sites and dependency wiring.
- **Senior-engineer question set:** A configured list of architectural-comprehension questions to run against the diff. Starter set drawn from senior-engineer review patterns, e.g.:
  - Why was this dependency called here? Is there a closer collaborator?
  - How is caching structured in relation to other services touched by this change?
  - What are the separation-of-concerns implications? Does this change cross a boundary that should remain intact?
  - What failure modes are introduced? What is the retry semantic?
  - What is the performance expectation for this code path?
  - Which interfaces gained behavioral contracts, and which interfaces gained only shape changes?
- **Reviewer identity:** Who receives the gate output. The reviewer is the merge authority; the gate is advisory.
- **Optional — eval-feedback destination:** A path or structured output location where per-question verdicts are emitted for downstream eval-suite consumption.
- **Optional — prior context:** Adjacent files, module manifests, or behavioral contracts that the question set may reference (enables better dependency-rationale verdicts when the codebase is self-describing).

## Procedure

1. **Load question set and diff.** Read the configured question set and the PR diff into the gate's working context. If either is missing or empty, halt and return a configuration error — do not run a partial gate.

2. **Per-question scan.** For each question in the set:
   - Identify the regions of the diff most relevant to the question (e.g., for "why was this dependency called here," locate import statements, constructor injections, or call sites added in the diff).
   - Cite the specific line ranges or symbols as evidence.
   - Produce a verdict: `clear`, `unclear`, or `no-evidence-in-diff`.
   - For `clear` verdicts, write a one-sentence justification grounded in the cited evidence.
   - For `unclear` and `no-evidence-in-diff` verdicts, write the specific architectural question the reviewer should ask the author before merge.

3. **Aggregate verdicts.** Collect all per-question verdicts into a structured comprehension report. Count clear vs. unclear vs. no-evidence outcomes.

4. **Emit reviewer-facing output.** Attach the comprehension report to the PR (as a comment, check run, or sidecar artifact, depending on the platform). The report ordering surfaces unclear and no-evidence verdicts first — those are the items the reviewer must engage with.

5. **Optional — emit eval-feedback signal.** If an eval-feedback destination is configured, write the per-question verdicts (without the diff content) to the destination so that eval-suite curators can identify question categories that produce repeated low-confidence verdicts and refine the question set or the underlying code patterns.

6. **Surface to reviewer.** Notify the configured reviewer that the gate has run. The reviewer reads the report, engages with unclear/no-evidence items, and applies their own merge judgment. The gate does not participate in the merge decision.

## Outputs

- **Comprehension report:** A structured document with one entry per question, each containing the question text, the cited evidence from the diff, the verdict (`clear` / `unclear` / `no-evidence-in-diff`), and a justification or follow-up question.
- **Verdict summary:** Counts of clear vs. unclear vs. no-evidence outcomes; list of unanswered questions; PR-level recommendation (`reviewer-attention-required` or `comprehension-clear`).
- **Optional eval-feedback signal:** Per-question verdict records emitted to the configured destination for downstream eval-suite refinement.

## Boundary

The gate fires on PR-review events for code changes (and configuration changes that affect runtime behavior). It does not fire on documentation-only PRs, on dependency version bumps without code-touching follow-up, or on revert-only PRs.

The gate does not replace the human reviewer. It does not approve or block merges. It does not modify the diff, the PR description, or repository state. It does not infer answers from prior commits when the diff itself does not contain evidence — silent extrapolation defeats the purpose of restoring comprehension.

The gate is not a security scanner, a static analyzer, or a test runner. Those tools answer different questions and operate on different evidence.

## Failure Modes

- **Question set drift.** Over time, the configured questions may stop matching the actual review patterns of senior engineers, producing reports that look thorough but miss real architectural concerns. Mitigation: version the question set, schedule periodic reviews tied to senior-engineer feedback, and treat unreviewed drift as a governance gap.

- **Reviewer fatigue from no-evidence verdicts.** If many questions produce `no-evidence-in-diff` verdicts on routine PRs, reviewers may start ignoring the report. Mitigation: tune the question set to fire only on questions whose evidence regions are actually present in the diff scope; suppress questions that systematically produce no-evidence outcomes for a given repository.

- **Synthesized verdicts.** The gate may be tempted to fill in answers from prior commits or from training-data patterns when the diff itself does not contain evidence. This re-introduces dark code under the guise of comprehension. Mitigation: enforce the invariant that every verdict cites evidence from the diff or refuses to render — `no-evidence-in-diff` is a valid output, not a failure.

- **Gate becomes the bottleneck.** Adding the gate to the PR pipeline can extend review latency, especially if the reviewer waits for both the gate and human review serially. The original problem framing warns against this explicitly. Mitigation: run the gate concurrently with reviewer assignment; surface its output as advisory rather than blocking; monitor latency impact and tune the question set down if it adds friction without proportional comprehension gain.

- **Eval-feedback loop accelerates the wrong target.** If the eval-feedback signal is naively used to optimize for "more clear verdicts," teams may drift toward question sets that produce easy-to-verdict questions rather than genuinely architecturally important ones. Mitigation: eval-feedback consumers must distinguish between "verdict quality" and "question-set quality"; periodic senior-engineer review of the question set is non-negotiable.

- **Gate runs on PRs with unreadable or partial diffs.** Large PRs, binary changes, or generated-code regions may produce diffs the gate cannot fully process. Mitigation: emit an explicit incomplete-diff verdict naming the unread regions; do not pass an incomplete scan as a clear comprehension report.

## Contract

### Preconditions
A PR diff is available and readable. The senior-engineer-style question set is defined before invocation (dependency rationale, caching topology, separation-of-concerns implications, failure-mode handling, retry semantics, etc.). At least one human reviewer is identified as the gate's recipient. Optional eval-feedback destination is configured if the gate output is to feed back into eval suites.

### Invariants
Every question in the configured set runs against the diff — the gate does not skip questions even when no obvious match is found. Each question's verdict cites concrete evidence from the diff or surrounding code. The gate's output is a recommendation to the human reviewer, never an autonomous merge decision. Unanswered questions and low-confidence verdicts are surfaced as explicit blockers, not silently passed. The gate never modifies the diff, the PR description, or repository state.

### Governance
Owner: the team or system that maintains the question set and invokes the gate. Question-set changes are versioned and reviewed — drift in the question set without review is treated as a governance gap. The gate's output is advisory; the human reviewer remains the merge authority. Eval-feedback emission is opt-in per repository; teams that emit must designate a destination and a retention policy.

### Recovery
If the diff is unreadable or partial: halt and return a structured incomplete-diff verdict with the unread regions named. If a question produces no evidence in the diff: emit an explicit no-evidence verdict with the question identifier — do not synthesize a verdict from prior commits. If the question set is missing or empty: halt before running and prompt the caller to configure the question set. If reviewer latency exceeds the configured threshold: surface the gate output as a standalone report so the bottleneck does not silently extend merge time.
