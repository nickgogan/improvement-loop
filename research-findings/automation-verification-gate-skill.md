---
name: "Automation-Verification Gate (Automate Only What You've Systematized)"
summary: |-
  A gate skill that must sign off before any robust automation gets built, enforcing the
  tail of a five-step framework: question the requirement → delete what can be deleted →
  simplify what remains → skill-driven augmentation (do the task with AI manually; if it
  repeats, capture it as a skill and improve it per use) → only then skill-driven
  automation. "If you're automating something you haven't already systematized manually,
  you're wasting your time." The practitioner doesn't trust himself to run the check
  mentally, so the check is externalized as a skill that has to approve the decision.
  Same discipline as skill-driven loop creation: every loop starts as a manually tested
  skill, then gets wrapped in a scheduled routine that references the skill.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "IL (mechanism/automation intake)"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "youre-the-problem-not-claude-6-fixes.md"
  - "8-claude-loops-to-build-10x-faster.md"
related_findings:
  - file: "three-bucket-change-approval-tiering.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

An executable check against premature automation. The five-step frame (explicitly
Elon-derived): (1) question every requirement — is the step necessary at all; (2) delete
— "the most common error of a smart engineer is to optimize the thing that should not
exist," and if you aren't deleting so much you have to add 10% back, you aren't deleting
enough; (3) simplify/optimize what survives; (4) skill-driven augmentation — do the task
with AI as assistant, and when it repeats, capture the exact procedure as a skill,
improving it each use; (5) skill-driven automation — automate only skills already proven
manually. The distinctive move is step 5's enforcement: an **automation verification
skill** that has to sign off on any decision to build a robust automation, because the
practitioner "doesn't trust himself to run this check in his head."

The companion mechanic from the same author's loop video: **skill-driven loop creation**
— every scheduled loop starts life as a skill that is run manually and confirmed working
before a routine wraps it; the routine references the skill (rather than inlining
instructions), so improving the skill automatically improves the scheduled automation.

## Why It Matters for Us

This corroborates engine Rule 11 (abstractions must earn their keep — recurrence
evidence before mechanism cost) from an independent practitioner, and adds the delta the
rule lacks: an *executable* enforcement point. Rule 11 is prose the agent must remember
to apply; a gate skill is a check that must be passed. The routine-references-skill
mechanic also matches how the engine's skills front its scheduled work. Recorded as
corroboration + one concrete upgrade path; the principle itself is already adopted.

## Why People Are Using It

Marchese (2026-07-07) teaches it as the fix for "if you hand someone Claude, everything
starts looking like an AI problem," with the sign-off skill as his personal guardrail;
his loops video (2026-07-03) applies the same manual-first discipline to every loop.
Aligns with the KB's audit-before-automate and ratchet/retirement findings.

## Potential Improvements

- Recurrence thresholds in the gate (2-3+ observed repetitions) to make Rule 11's
  evidence bar machine-checkable.
- Recording rejected automations and their reasons, so repeated proposals accumulate
  evidence instead of being re-litigated.

## Potential Failure Modes

- Rubber-stamp risk: a gate skill authored by the same enthusiasm that wants the
  automation can be prompted into approving it.
- Over-deletion: the delete step is a judgment call; aggressive pruning of processes that
  existed for non-obvious reasons (compliance, edge cases) causes late failures.
- Gate bypass: nothing forces the check to be invoked; it only works as a standing habit
  or a hard hook.
