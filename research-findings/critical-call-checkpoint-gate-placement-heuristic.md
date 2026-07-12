---
name: "Critical-Call-Checkpoint Heuristic for Human-Gate Placement"
summary: |-
  Gate-placement rule for loops: identify the critical call checkpoints — steps where a
  wrong call invalidates everything downstream (e.g., plan sign-off before build, review,
  and verify) — and place a human approval gate at exactly those points. Some loops need
  zero gates, others four or five; gate count is a property of the loop's risk structure,
  not a fixed policy.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "IL (gate design)"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "8-claude-loops-to-build-10x-faster.md"
related_findings:
  - file: "human-on-the-loop-hotl-autonomy-tiering-framework.md"
    rel: "same-problem"
  - file: "three-bucket-change-approval-tiering.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

A heuristic for deciding *where* human approval gates belong in an agent loop. A critical
call checkpoint is any step where being wrong invalidates all downstream steps — in a
six-step build loop (extract goal → plan → sign off → build → code review → verify), the
plan sign-off is the checkpoint because a wrong plan makes steps four through six wasted
time and money. Rule of thumb: for any loop you create, every critical call checkpoint
gets a human approval gate; steps that are cheaply reversible or self-verifying don't.
Gate density is therefore variable — zero for low-stakes loops, four or five for
high-stakes ones.

## Why It Matters for Us

The engine's DD-29 places a human gate at every pipeline stage boundary — a structural
rule. This heuristic offers the *reason* those gates work (stage boundaries are exactly
where a wrong classification/extraction poisons everything downstream) and a portable
test for gate placement in new loops and skills where DD-29's stage structure doesn't
directly apply. It is positive-space framing: derive gates from downstream-invalidation
risk, rather than gating everything or nothing.

## Why People Are Using It

Practitioner rule of thumb (Marchese, 2026-07), taught as one of the two concepts to
carry when designing loops from scratch. Consistent with the KB's autonomy-tiering
findings, which reach the same place from the risk-tiering direction.

## Potential Improvements

- Making "invalidates downstream" testable: estimated cost of proceeding wrong vs cost of
  the interruption — turning the heuristic into a calibration table.
- Combining with approve-and-don't-ask-again preference memory so checkpoints that never
  produce rejections get demoted over time.

## Potential Failure Modes

- Under-gating: checkpoint identification is itself a judgment call; a missed critical
  call runs ungated.
- Over-gating: labeling every step "critical" recreates review-everything fatigue and the
  gates start getting rubber-stamped.
- Static placement: the risk structure of a loop changes as it matures, but gates placed
  once tend to stay.
