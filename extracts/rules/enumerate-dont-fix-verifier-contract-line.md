---
title: "Enumerate, Don't Fix — Verifier Contract Line"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "enumerate-dont-fix-hostile-reviewer-prompt"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "verifying-agent-output.harvest-queue"
identification_report: "verifying-agent-output.harvest-queue.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "prompts that ask a model to review, audit, or verify another model's (or its own) output for correctness"
    - "verification or quality-assurance subagents used in multi-agent build or content pipelines"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "verify"
  reversibility: "trivial — a prompt-level instruction change with no migration cost"
  auditability: "high when the reviewer's raw output is retained verbatim (an enumerated issue list is easy to check against); low if only a pass/fail summary survives"
  evidence_strength: "Medium"
  adoption:
    status: "Partially Adopted"
    notes: "Practitioner-documented in an adversarial deck/workbook review workflow; report-only verifier subagents in comparable pipelines already follow a compatible posture but often lack the explicit multi-category checklist or the verbatim terminal instruction as a contract line."
contract:
  preconditions: "An agent or subagent is instructed to review, audit, or verify another agent's (or its own) output for correctness, completeness, or quality issues, and has read/write access sufficient to also 'fix' the artifact under review."
  invariants: "The reviewer's prompt explicitly forbids fixing, editing, or resolving any issue it finds. Its only permitted output is a written enumeration of issues. Each enumerated issue names the specific concern (unsupported claim, missing source, untraceable data, inconsistent formula, assumption presented as fact, etc.) rather than a vague general impression."
  governance: "Owner: whoever authors the verifier/reviewer prompt (skill instructions, subagent system prompt, or a CLAUDE.md verification section). The instruction 'don't fix anything, just enumerate' must appear as an explicit terminal directive in the prompt — not left to be inferred from role framing alone."
  recovery: "If the reviewer's output includes a fix, a diff, or a rewritten artifact instead of (or alongside) an enumerated issue list, treat the review as contaminated — discard any embedded fix and re-run the review with the enumerate-only instruction reinforced. If issues are found but not itemized (a vague summary instead of a list), request re-output in enumerated form before acting on it."
tags:
  - "extracted-artifact"
  - "rule"
  - "verification"
  - "prompt-craft"
---

# Enumerate, Don't Fix — Verifier Contract Line

**Source:** [[enumerate-dont-fix-hostile-reviewer-prompt]]
**Form:** rule
**Extraction date:** 2026-07-19

## Condition

A model is assigned a reviewer, verifier, or auditor role over an artifact — its own prior output or another agent's — and the review's purpose is to surface correctness or quality problems (unsupported claims, missing sources, inconsistent data, unverified assumptions, and similar).

## Action

**Required:** State a hostile-reviewer stance ("suspect every claim and every number") together with a concrete enumeration checklist appropriate to the artifact type. Instruct the model that its only permitted output is a written list of every issue found, each one named specifically (what the issue is and where it occurs).

**Forbidden:** Allowing the reviewer to fix, patch, rewrite, or otherwise resolve any issue it identifies. Accepting a review output that is a general impression ("looks mostly fine, a few number issues") instead of a discrete, itemized list.

## Boundary

Enforced at the prompt layer of any verification or review step — a dedicated reviewer subagent, a review-mode invocation of a skill, or a review section inside a larger orchestrator prompt. Applies whenever a model's output feeds a downstream decision about whether other content is correct.

## Enforcement

- **Mechanism:** The reviewer prompt must contain an explicit terminal instruction equivalent to "don't fix anything, just enumerate" — not implied by "review this" framing alone.
- **Check (deterministic):** the reviewer's output is a list of discrete issues (not prose summary, not a revised artifact, not a diff). Any embedded fix, patch, or rewritten passage in the output is a contract violation.
- **Violation response:** discard any fix embedded in the review output; re-invoke the reviewer with the enumerate-only instruction reinforced; do not act on the fix without a separate, explicit fix pass.

## Rationale

Finding and solving a problem are different tasks with different failure modes: a model asked to "fix issues" is biased toward completing and polishing, which papers over exactly the audit it was supposed to perform. Forbidding the fix output removes that bias — the model's only success criterion becomes finding problems, not making the artifact look done. This holds even when the same model reviews its own output, though cross-model review reduces shared blind spots further. The mechanism is the cheapest version of generator-assessor separation: no second model or fresh context is strictly required, only a different task framing.

## Failure Modes

- **Enumeration without severity ranking** buries the two consequential problems under twenty nitpicks — pair the enumeration with a severity or priority field where the review feeds a triage step.
- **Checklist tunnel vision.** The reviewer only reliably finds what its checklist names; novel failure classes still need the general hostile-suspicion framing to fire, not just the itemized categories.
- **Same-model blind spots.** Same-model enumeration still shares the generator's training priors and can miss the same class of error the generator would miss; cross-model or cross-context review reduces but does not eliminate this.

## Contract

### Preconditions
An agent or subagent is instructed to review, audit, or verify another agent's (or its own) output for correctness, completeness, or quality issues, and has read/write access sufficient to also "fix" the artifact under review.

### Invariants
The reviewer's prompt explicitly forbids fixing, editing, or resolving any issue it finds. Its only permitted output is a written enumeration of issues. Each enumerated issue names the specific concern (unsupported claim, missing source, untraceable data, inconsistent formula, assumption presented as fact, etc.) rather than a vague general impression.

### Governance
Owner: whoever authors the verifier/reviewer prompt (skill instructions, subagent system prompt, or a CLAUDE.md verification section). The instruction "don't fix anything, just enumerate" must appear as an explicit terminal directive in the prompt — not left to be inferred from role framing alone.

### Recovery
If the reviewer's output includes a fix, a diff, or a rewritten artifact instead of (or alongside) an enumerated issue list, treat the review as contaminated — discard any embedded fix and re-run the review with the enumerate-only instruction reinforced. If issues are found but not itemized (a vague summary instead of a list), request re-output in enumerated form before acting on it.
