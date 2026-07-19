---
name: Goal-Backward Verification
summary: 'GSD''s verifier starts from the desired outcome and works backwards to check what actually exists in code, rather than checking task checklists forward. Explicitly distrusts agent-generated summaries:
  ''Do NOT trust SUMMARY.md claims. Verify what ACTUALLY exists.'''
implementation_notes: null
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: context-pollution-same-window-verification-bias.md
  rel: same-problem
- file: qa-agent-independent-compliance-review.md
  rel: same-problem
- file: builder-validator-chain-pattern.md
  rel: same-problem
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
- file: ultra-review-multi-agent-bug-hunting-fleet.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
  - verifying-agent-output.md
  - "rules/agent-self-reporting-unreliability-independent-eval.md"
  - writing-agent-specifications.md
---
# Goal-Backward Verification

## What It Is
GSD's verification phase inverts the typical checking direction. Instead of walking through task lists and confirming each was completed (forward verification), the verifier starts from the phase's intended outcome and works backward to confirm the code actually achieves it. The verifier is explicitly instructed: "Task completion != goal achievement" and "Do NOT trust SUMMARY.md claims. Verify what ACTUALLY exists in the code." This is a trust-nothing mindset applied to agent output validation.

## Why It Matters
Forward verification (did you do what the plan said?) catches omissions but misses a critical failure mode: the plan itself may have been incomplete, or tasks may have been marked done without achieving the intended effect. Goal-backward verification asks a different question — does the codebase now accomplish what this phase was supposed to accomplish? — which catches both task-level failures and plan-level gaps.

## Why People Are Using It
Observed in [GSD](https://github.com/gsd-build/get-shit-done) v1.33.0 — see [[gsd-analysis]] for structural details. GSD runs this as the final phase after execution, with the verifier operating as a separate agent that reads PLAN.md goals and then inspects the actual codebase. The explicit distrust of SUMMARY.md (the executor's own output) reflects learned experience that agents reliably produce optimistic self-reports.

## Potential Alternatives
Forward checklist verification (most common — check each task off). Two-stage sequential review (Superpowers — spec compliance then quality). QA agent in fresh context (BMAD — independent compliance review). Automated test suites as verification (code-level, not goal-level). Human review as the sole verification gate.

## Potential Improvements
Combining goal-backward with forward verification — backward catches plan-level gaps, forward catches task-level omissions. Structured goal decomposition where the verifier has explicit success criteria (not just phase descriptions) to verify against. Confidence scoring on each backward-traced verification point so the human reviewer knows which areas the verifier is least certain about.

## Potential Failure Modes
Goal ambiguity — if the phase goal is vaguely stated, backward verification degenerates into subjective judgment. The verifier may not have sufficient domain knowledge to assess whether the code actually achieves a goal (it can check structure but not correctness). Over-reliance on a single verification pass without iterative feedback to the executor.
