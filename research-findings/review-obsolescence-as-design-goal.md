---
name: Review Obsolescence as Design Goal
summary: Every review comment should trigger the question 'how do I make this comment impossible in the future?' Tooling that eliminates entire classes of review feedback (e.g., go fmt eliminating whitespace
  debates) is more valuable than faster review. The reviewer's job is to obsolete their own review, not to catch errors.
implementation_notes: 'Apply to MetaSystem: when a review gate catches an issue, the fix should include a linter rule, schema constraint, or automated check that prevents the same class of issue from recurring.
  This converts reactive review into proactive prevention.'
category: Governance
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- General
adopted_in: []
sources:
- every-layer-of-review-makes-you-10x-slower.md
related_findings:
- file: review-pipeline-bottleneck-and-quality-at-source.md
  rel: same-problem
- file: review-bandwidth-as-organizational-bottleneck.md
  rel: same-problem
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: "synthesized"
consumed_by:
  - "agent-governance-and-trust.md"
---
## What It Is

A design principle from Avery Pennarun (CEO, Tailscale): the purpose of a code review comment is not to fix the current instance of a problem, but to figure out how to eliminate that entire class of review comment in all future cases. The canonical example is `go fmt` -- a tool that ended all whitespace and formatting debates permanently by making them impossible.

This reframes the reviewer's role from "error catcher" to "system designer." Each review finding is a signal that the system allowed a preventable error class.

## Why It Matters

Review layers add ~10x wall-clock time each. Eliminating categories of review comments reduces the volume of review needed, directly attacking the bottleneck. This is the constructive counterpart to the "review pipeline bottleneck" finding -- it says what to DO about the problem, not just what's wrong.

## Why People Are Using It

Pennarun draws on decades of systems design at Tailscale and Google. The `go fmt` example is widely known in the Go community as a case study in eliminating an entire class of engineering friction through tooling. Toyota's quality-at-source philosophy is the manufacturing equivalent -- the goal is preventing defects, not inspecting for them.

## Potential Improvements

AI agents could analyze review comment history to identify the most frequent comment categories, then propose automated checks or linting rules for each. This creates a feedback loop: review -> detect pattern -> automate check -> eliminate future reviews of that type.

## Potential Failure Modes

Not all review comments can be automated away -- judgment calls about architecture, naming, and design require human evaluation. Over-automating can create rigid systems that resist legitimate innovation. The goal is to eliminate mechanical review, not eliminate all review.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[review-obsolescence-as-design-goal.md]] in `extracts/patterns/`
