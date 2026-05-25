---
name: "Tiered Review Escalation Strategy"
summary: "Match review depth to PR importance: quick single-pass /review for routine PRs, add cross-model verification for more coverage, escalate to full multi-agent fleet review (Ultra Review) only for critical or large features. Cost scales with risk."
implementation_notes: null
category: "Evaluation"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General / Cross-System"
adopted_in: []
sources:
  - "claude-code-ultra-review-multi-agent-verification.md"
related_findings:
  - file: ultra-review-multi-agent-bug-hunting-fleet.md
    rel: extends
  - file: cross-model-verification-for-bug-finding.md
    rel: extends
  - file: task-complexity-tiering-quick-campaign-deep-build.md
    rel: same-problem
  - file: two-stage-sequential-review.md
    rel: same-problem
  - file: gstack-review-army-parallel-specialist-dispatch.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-19"
last_updated: "2026-04-19"
pipeline_status: synthesized
consumed_by:
  - "building-agent-evaluation-suites.md"
---
# Tiered Review Escalation Strategy

## What It Is
Not all PRs warrant the same review investment. A practitioner working with Claude Code's Ultra Review identified a three-tier escalation pattern based on PR size and importance:

**Tier 1 — Quick audit:** Run `/review` (Claude Code's built-in local review). Completes in 3-4 minutes. Covers the entire diff broadly, flagging anything that deviates from norms. Best for routine, low-risk changes.

**Tier 2 — Cross-model review:** Add Codex (or another model) running in parallel to find bugs that Claude's traversal misses. Cross-model disagreement surfaces the highest-priority items for human attention. Best for standard feature PRs.

**Tier 3 — Fleet review:** Use Ultra Review (`/ultra-review`) for features that are large (e.g., 11,000+ lines) or high-criticality. Takes 10-20 minutes with a full find→verify→dedup pipeline. Catches race conditions and lifecycle bugs that the quick audit misses entirely. Best for major features, security-sensitive changes, or releases.

The tiering logic: cost should scale with risk. Running ultra-review on every commit wastes compute. Running only quick review on a critical authentication change misses bugs.

## Why It Matters
Review tools have different tradeoffs. A quick audit sweeps broadly but lacks depth. A full fleet review provides depth but costs significantly more in time and tokens. Treating all PRs identically either over-spends on trivial changes or under-invests in critical ones. The tiered approach right-sizes the review depth to the risk profile of the change.

## Why People Are Using It
Observed in practitioner usage of Claude Code Ultra Review. The speaker explicitly described developing a personal escalation heuristic: quick /review as default, cross-model verification for more coverage, ultra-review for big or important features. This mirrors patterns from other engineering contexts — automated test suites have unit tests (fast, broad), integration tests (slower, deeper), and end-to-end tests (slowest, highest confidence).

## Potential Improvements
- Formalize tier selection criteria: define quantitative thresholds (e.g., lines changed, number of files, risk tags in the PR description) that automatically recommend a tier.
- Add a Tier 0: automated static analysis as a pre-gate before any LLM review runs, filtering trivially clean changes.
- Track review outcomes by tier to validate that the escalation heuristics are correctly calibrated.

## Potential Failure Modes
- Tier selection requires judgment — teams may systematically under-escalate for political reasons (speed pressure) or over-escalate for risk-averse ones (wasted compute).
- Ultra Review is currently limited in uses on the $200/month plan, making it unavailable for sustained Tier 3 usage without dedicated tooling.
- The tiers assume the reviewer's tooling is stable. If Ultra Review pricing or availability changes, the escalation logic needs to be revisited.
