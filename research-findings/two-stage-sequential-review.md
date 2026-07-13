---
name: Two-Stage Sequential Review
summary: 'After each task in Superpowers'' subagent workflow, two sequential review stages run by fresh subagents: (1) spec compliance — does the implementation match the spec? (2) code quality — is the
  code well-written? Sequential ordering ensures you cannot have high-quality code that does not match the spec.'
implementation_notes: |-
  Priority downgraded P3 → Not Flagged (reassessment 2026-07-13, Nick-accepted;
  rule-4 exception with documented cause): pattern deprecated by its own originator.
  Superpowers v6.0.0 collapsed the two sequential per-task reviewers into one
  dual-verdict reviewer (see contradicts link to unified-dual-verdict-reviewer.md)
  with upstream eval data — similar quality, ~2x faster, ~50% fewer tokens. Retained
  in the KB as history; the contradicts link preserves the supersession trail.
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: builder-validator-chain-pattern.md
  rel: extends
- file: cross-model-verification-for-bug-finding.md
  rel: same-problem
- file: review-triggered-remediation-dispatch.md
  rel: enables
- file: unified-dual-verdict-reviewer.md
  rel: contradicts
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-07-13'
pipeline_status: raw
consumed_by: []
---
# Two-Stage Sequential Review

## What It Is
After each task in Superpowers' subagent-driven development workflow, two sequential review stages execute. Stage 1 is spec compliance review: does the implementation match what the spec said to build? Stage 2 is code quality review: is the code well-written, maintainable, and following best practices? Each review is performed by a fresh subagent with no context contamination from the implementer. If either stage fails, the implementer receives feedback and iterates. The sequential ordering is intentional — spec compliance is verified before quality, because high-quality code that does not match the spec is still wrong.

## Why It Matters
Single-pass review conflates two distinct concerns: correctness (does it do the right thing?) and quality (does it do it well?). By separating these into sequential stages with fresh-context agents, Superpowers ensures neither concern is subordinated to the other. The fresh-context requirement eliminates the verification bias documented in same-window review patterns — the reviewer cannot be influenced by the implementer's reasoning.

## Why People Are Using It
Observed in [Superpowers](https://github.com/obra/superpowers) v5.0.7 — see [[superpowers-analysis]] for structural details. The two-stage review runs automatically after each task in the spec-driven development workflow. Compare: GSD's plan-checker reviews plans (not task outputs) and verification is goal-backward (not spec-forward). gstack's Review Army dispatches parallel specialist reviewers rather than sequential stages.

## Potential Alternatives
Single-pass review combining spec compliance and quality in one agent. Parallel specialist review (gstack's Review Army approach). Goal-backward verification (GSD) that checks outcomes rather than specs. Human-only review. Automated test suites as the primary verification mechanism.

## Potential Improvements
Adding a third stage for security review on tasks that touch authentication, authorization, or data handling. Configurable review depth based on task risk — critical tasks get full two-stage, low-risk tasks get a lightweight single pass. Accumulating review feedback across tasks to identify systemic patterns (e.g., the implementer consistently mishandles edge cases).

## Potential Failure Modes
Double the review cost in tokens and time — for large projects with many tasks, this adds significant overhead. Spec quality is the ceiling — if the spec is vague or wrong, spec compliance review rubber-stamps incorrect implementation. The sequential dependency means a slow spec compliance review blocks the quality review. Fresh-context agents may lack project-level understanding that an in-context reviewer would have.
