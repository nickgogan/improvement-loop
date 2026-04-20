---
name: Review Army — Parallel Specialist Dispatch
summary: Parallel specialist reviewer dispatch with adaptive gating and cross-review dedup for comprehensive code review.
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General / Cross-System
adopted_in: []
sources:
- gstack-v01590-v015160-changelog.md
related_findings:
- file: review-bandwidth-as-organizational-bottleneck.md
  rel: same-problem
- file: gstack-dx-review-developer-experience-audit.md
  rel: extended-by
- file: review-pipeline-bottleneck-and-quality-at-source.md
  rel: same-problem
- file: builder-validator-chain-pattern.md
  rel: same-problem
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
- file: ultra-review-multi-agent-bug-hunting-fleet.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- building-agent-evaluation-suites.md
---
# Review Army — Parallel Specialist Dispatch

## What It Is
gstack's `/review` and `/ship` commands dispatch 8 specialist reviewers in parallel, each evaluating a different dimension of code quality: testing, maintainability, security, performance, data-migration, api-contract, design, and red-team. Adaptive gating adjusts review depth per specialist based on a diff size heuristic that counts insertions + deletions (previously insertions-only, which missed deletion-heavy refactors). Cross-review dedup auto-suppresses findings already skipped in a prior review unless the relevant code has changed since. Re-run behavior for `/ship` re-executes every verification step, with idempotent actions only skipping where safe.

## Why It Matters
Single-pass code review consistently misses category-specific issues — a generalist reviewer catches security flaws less reliably than a security specialist. Parallel dispatch means review latency is bounded by the slowest specialist, not the sum of all specialists. Cross-review dedup prevents reviewer fatigue from seeing the same suppressed findings across repeated review cycles.

## Why People Are Using It
gstack implements this as a core workflow primitive for its `/review` and `/ship` commands. The 8-specialist taxonomy covers the most common dimensions where code changes introduce risk. The adaptive gating mechanism ensures small changes don't trigger heavyweight review, while large changes get full scrutiny.

## Potential Improvements
Specialist taxonomy could be made extensible — allow users to define custom specialist dimensions (e.g., accessibility, i18n, compliance). The diff size heuristic could incorporate semantic complexity (AST diff) rather than pure line counts. Specialist weighting could be learned from historical review outcomes.

## Potential Failure Modes
Parallel specialist dispatch multiplies token cost by the number of specialists — 8x cost for every review. Adaptive gating thresholds may be miscalibrated for specific codebases (e.g., infrastructure code where small diffs have outsized impact). Cross-review dedup may suppress legitimate re-flagging if the "relevant code changed" detection is too narrow.
