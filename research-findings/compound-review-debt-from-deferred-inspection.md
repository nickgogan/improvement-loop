---
name: Compound Review Debt from Deferred Inspection
summary: 'Skipping review on agent-produced work creates compound debt: each unreviewed change builds assumptions for subsequent changes, making later review exponentially harder. The cost of reviewing
  a chain of 10 unreviewed commits is much higher than reviewing each individually.'
implementation_notes: Argues for atomic review at each human gate rather than batch review at milestones.
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- agent-produces-100x-org-reviews-3x.md
related_findings:
- file: review-pipeline-bottleneck-and-quality-at-source.md
  rel: same-problem
- file: review-bandwidth-as-organizational-bottleneck.md
  rel: same-problem
- file: staged-delivery-for-review-digestibility.md
  rel: same-problem
- file: dark-code-organizational-capability-problem.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-20'
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
- maximum-unreviewed-depth-policy.md
---

# Compound Review Debt from Deferred Inspection

## What It Is
The observation that unreviewed agent-produced changes create compound debt analogous to technical debt. Each unreviewed change embeds assumptions that subsequent changes build upon. Reviewing a chain of 10 unreviewed commits costs far more than reviewing each commit individually, because the reviewer must untangle cascading dependencies and determine which assumptions were valid at each step.

## Why It Matters
The temptation to defer review is strongest precisely when agents are most productive -- the output volume makes per-change review feel impossible, so teams batch reviews at milestones. But this batching dramatically increases per-unit review cost. The math works against deferral: 10 individually-reviewed changes might take 10 minutes each, while the same 10 changes reviewed as a batch might take 3 hours due to interconnected assumptions.

## Why People Are Using It
Teams that experienced painful batch-review sessions are shifting to atomic review at each human gate. This means smaller, more frequent review checkpoints even if it feels slower in the moment. The key insight is that total review time decreases when review is done incrementally rather than in bulk.

## Potential Improvements
MetaSystem's phase-based execution model in GSD already supports incremental review. The improvement would be to formalize a maximum "unreviewed depth" policy -- no more than N changes should accumulate before a review gate triggers, regardless of whether a phase boundary has been reached.

## Potential Failure Modes
Strict atomic review can slow agent throughput to the reviewer's pace, negating the speed advantage of agents. The challenge is finding the right granularity -- too fine and review becomes constant interruption, too coarse and compound debt accumulates. Different task types likely need different review granularity.

## Extraction Note — 2026-04-27

Extracted as **rule**: [[maximum-unreviewed-depth-policy]] in `extracts/rules/`. Harvested from the G9 (agent-governance-and-trust) queue per IB-164 / DD-101 promotion path.
