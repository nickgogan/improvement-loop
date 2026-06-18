---
title: "Headless Multi-Pass Iterative Review"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "headless-multi-pass-iterative-review"
extraction_date: "2026-05-25"
last_change_session: 94
last_change_sl: "session-94-codifier-extract-non-pattern-artifacts"
identification_report: "2026-05-24-identification-report-2.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Code review pipelines where single-pass review is known to miss issues due to reviewer-attention bias or context saturation"
    - "Teams that need confidence tiers on review findings — distinguishing issues flagged consistently across independent reviewers from one-off observations"
    - "Any workflow where review thoroughness is a compliance or quality gate and a single reviewer's oversight would be unacceptable"
    - "Automated PR review in CI/CD pipelines where a shell-scriptable, non-interactive review agent can be invoked repeatedly"
  platform_coupling: "specific:claude-code"
  autonomy: "autonomous-only"
  stage: "verify"
  reversibility: "trivial — the skill produces reports only; no persistent state is written to the codebase or external systems; removing it from a pipeline requires no migration"
  auditability: "High when per-pass report files are retained alongside the consolidated report — the confidence tiers in the consolidated report are independently verifiable by counting per-pass occurrences; low when only the consolidated report is kept"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "A target (PR URL or branch) is accessible to the headless claude -p invocation at the time of the run. A self-contained review prompt file exists before the loop starts. The execution environment supports spawning N headless Claude invocations without hitting a hard concurrency or rate-limit ceiling that would abort the run. The caller has set an acceptable N and sub-agent count that fits within available token and cost budget."
  invariants: "Each pass is executed with a fresh context window — no pass may read or reference the output of a prior pass. The same review prompt is used for every pass within a single run. Per-pass reports are written to durable storage before aggregation begins. The consolidated report includes a coverage summary that is honest about pass failures. Aggregation confidence tiers are derived from actual pass counts, not editorial judgment."
  governance: "Owner: the caller (human or orchestrating agent) who defines the prompt file, sets N, and triggers the run. The review prompt is caller-owned and is not modified by the skill during execution. Per-pass reports are the primary audit artifacts and must be retained alongside the consolidated report."
  recovery: "If one or more passes fail: record the failure in the coverage summary; proceed with aggregation over the successful passes; label the consolidated report with the actual pass count. If aggregation produces zero high-confidence findings: surface per-pass reports for manual review — do not interpret as 'no issues.' If cost exceeds limits: reduce N or sub-agent count; do not silently skip passes."
tags:
  - "extracted-artifact"
  - "skill"
---

# Headless Multi-Pass Iterative Review

**Source:** [[headless-multi-pass-iterative-review]]
**Form:** skill
**Extraction date:** 2026-05-25

An iterative review skill that executes N independent review passes, each in a completely fresh context window via headless `claude -p`, then aggregates all findings into a single consolidated report with confidence tiers based on cross-pass agreement. Practitioner baseline: 5 iterations, each spawning 5-7 sub-agents — 25-35 review agents total per PR review session.

## Inputs

- **Target:** A PR URL or branch name identifying the code to be reviewed.
- **Iteration count (N):** An integer specifying how many independent review passes to execute. Practitioner baseline: 5.
- **Review prompt:** A markdown file containing the prompt used for each headless invocation. The same prompt is used for all passes — variation comes from fresh-context sampling, not prompt changes.
- **Sub-agent count (optional):** The number of sub-agents each pass spawns internally via a split-and-merge pattern. Practitioner baseline: 5-7.
- **Aggregation instruction (optional):** How to merge N independent pass reports — e.g., "surface findings mentioned in 3 or more passes as high-confidence; findings from a single pass as low-confidence."

## Outputs

- **Per-pass finding reports (N files):** Each pass produces its own independent findings list. These are intermediate outputs feeding the aggregation step.
- **Consolidated review report:** A single document merging all N pass reports. Findings appearing across multiple passes are marked with a confidence tier. Findings unique to one pass are marked as low-confidence.
- **Coverage summary:** Total agent invocations (N x sub-agents), pass completion status, and any rate-limit or fetch errors encountered.

## Steps

1. **Prepare the review prompt.** Write or verify the prompt file that each headless pass will receive. The prompt must be self-contained — it cannot reference output from prior passes.

2. **Initialize the pass loop.** Set a counter `i = 1`. Create an output directory to hold per-pass reports.

3. **Execute pass `i` headlessly.** Run `claude -p "$(cat review-prompt.md)"` with the target PR URL or branch embedded in the prompt. The `-p` flag ensures the invocation is non-interactive and starts with a fresh context window.

4. **Capture pass output.** Write the pass report to the output directory as `pass-{i}.md`. Check the exit code; if the pass failed (timeout, rate limit, fetch error), record the failure and continue to the next pass.

5. **Repeat steps 3-4 until `i = N`.** Each invocation is independent. Do not share context, intermediate results, or accumulated state between passes.

6. **Aggregate findings.** Read all pass reports. For each distinct finding: count how many passes surface it (by semantic equivalence, not exact match); assign a confidence tier based on cross-pass agreement; merge duplicate descriptions into a single canonical entry.

7. **Produce the consolidated report.** Output the aggregated findings sorted by confidence tier (high → medium → low). Include the coverage summary as a header.

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Token cost explosion | N passes x sub-agents exceeds budget | Tune N downward for large diffs; consider two-tier approach (1 broad pass, N passes on flagged sections) |
| Aggregation noise | N independent vocabularies for the same issue produce confusing merges | Use a separate agent pass for semantic deduplication, not string-matching |
| Shell script fragility | Single pass failure aborts the entire run | Add per-pass error handling; log failures in coverage summary; do not abort on single-pass failure |
| Context freshness degradation | Rate limits cause later passes to fail or receive stale data | Add short backoff between passes on rate-limit errors; do not treat rate-limit failures as review findings |
| Self-confirming low-confidence findings | Findings in 1 of N passes are discarded as noise | Retain low-confidence findings in a clearly labeled section; do not discard silently |

## Contract

### Preconditions
A target (PR URL or branch) is accessible to the headless `claude -p` invocation at the time of the run. A self-contained review prompt file exists before the loop starts. The execution environment supports spawning N headless Claude invocations. The caller has set an acceptable N and sub-agent count within token and cost budget.

### Invariants
Each pass is executed with a fresh context window — no pass may read or reference the output of a prior pass. The same review prompt is used for every pass within a single run. Per-pass reports are written to durable storage before aggregation begins. The consolidated report includes a coverage summary that is honest about pass failures. Aggregation confidence tiers are derived from actual pass counts, not editorial judgment.

### Governance
Owner: the caller (human or orchestrating agent) who defines the prompt file, sets N, and triggers the run. The review prompt is caller-owned and is not modified by the skill during execution. Per-pass reports are the primary audit artifacts and must be retained alongside the consolidated report; the consolidated report alone is not sufficient to reconstruct how a high-confidence finding was determined.

### Recovery
If one or more passes fail (timeout, rate limit, network error): record the failure in the coverage summary; proceed with aggregation over the successful passes; label the consolidated report with the actual pass count (e.g., "3 of 5 passes completed"); do not treat the partial run as equivalent to a full N-pass run. If aggregation produces zero high-confidence findings across N passes: do not interpret as "no issues" — surface per-pass reports for manual review. If cost exceeds limits: reduce N or sub-agent count; do not silently skip passes while reporting a full run.
