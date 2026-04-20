---
name: Staged Delivery for Review Digestibility
summary: Agents should deliver work in review-digestible chunks rather than monolithic outputs. Each delivery stage should be independently reviewable and reversible. The chunk size is calibrated to the
  reviewer's capacity, not the agent's production capacity.
implementation_notes: GSD's phase model already does this. The insight is that chunk size should be reviewer-calibrated, not production-calibrated.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in:
- S3 (Claude Code Build)
sources:
- agent-produces-100x-org-reviews-3x.md
related_findings:
- file: review-pipeline-bottleneck-and-quality-at-source.md
  rel: same-problem
- file: compound-review-debt-from-deferred-inspection.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
pipeline_status: synthesized
consumed_by:
- agent-workflow-and-execution.md
---

# Staged Delivery for Review Digestibility

## What It Is
A delivery pattern where agents break their output into independently reviewable and reversible chunks, sized to the reviewer's absorption capacity rather than the agent's production speed. Each stage is a self-contained unit that can be approved, rejected, or revised without affecting other stages. The chunk boundary is determined by what a human can meaningfully evaluate in one sitting.

## Why It Matters
Monolithic delivery -- where an agent produces a complete feature or document in one pass -- creates review paralysis. The reviewer faces an all-or-nothing choice on a large body of work, making it harder to provide targeted feedback or catch specific issues. Staged delivery converts one large review decision into multiple small ones, each with lower cognitive cost.

## Why People Are Using It
GSD's phase model already implements staged delivery, breaking work into discuss, plan, and execute stages with human gates between them. The refinement from the 100x/3x analysis is that stage boundaries should be set by what the reviewer can digest, not by natural production breakpoints. A phase that produces 500 lines of changes may need to be split further if the reviewer cannot meaningfully evaluate 500 lines at once.

## Potential Improvements
MetaSystem could formalize reviewer-calibrated chunk sizing as a parameter in GSD's phase planning. Rather than fixed phase boundaries, the system could estimate review complexity and suggest splits when a phase's output would exceed the reviewer's demonstrated capacity.

## Potential Failure Modes
Over-segmentation creates context-switching overhead for the reviewer, who must reload context for each small chunk. There is a sweet spot between monolithic delivery and micro-delivery that varies per task type and reviewer. Staged delivery also requires the agent to maintain coherence across stages, which not all agent architectures handle well.
