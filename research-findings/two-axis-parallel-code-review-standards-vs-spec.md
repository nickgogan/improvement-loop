---
name: Two-Axis Parallel Code Review — Standards Conformance vs Spec Fidelity
summary: 'Plain English: a code review answers two different questions — "is this good code by our

  standards?" and "is this the code we asked for?" — and conflating them in one reviewer

  dilutes both. Pocock''s v1.1 code-review skill runs one parallel subagent per axis: the

  standards axis checks conformance against the repo''s documented coding standards (a

  coding-standards.md kept deliberately *outside* agents.md — standards are most useful at

  review time, not as always-loaded context), and the spec axis checks whether the code

  faithfully implements the originating issue/PR/spec, walking through each part. A

  placement claim rides along: refactoring belongs in code review, not in the

  implementation loop (his TDD loop dropped to red-green, with refactor moved to review)

  so implementation isn''t overloaded.'
implementation_notes: |-
  Caveat (reassessment 2026-07-13, Nick-accepted; P3 kept): contradicted by
  unified-dual-verdict-reviewer (superpowers measured ~2x faster / ~50% cheaper for
  the unified shape); unlike two-stage-sequential-review, this is an independent live
  practice (Pocock v1.1) not deprecated by its originator, so the contradiction is an
  open trade (parallel-axis separation vs single-read economy), not a supersession.
category: Evaluation
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- pocock-skills-v1-1-wayfinder-research-implement.md
related_findings:
- file: headless-multi-pass-iterative-review.md
  rel: same-problem
- file: generator-assessor-separation-in-skill-iteration.md
  rel: same-problem
- file: push-vs-pull-context-loading.md
  rel: extends
- file: fowler-code-smell-names-as-prior-invocation.md
  rel: enabled-by
- file: unified-dual-verdict-reviewer.md
  rel: contradicts
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-13'
pipeline_status: raw
---

# Two-Axis Parallel Code Review — Standards Conformance vs Spec Fidelity

## What It Is

A review decomposition from Pocock's skills v1.1 code-review skill: spawn one subagent per
review axis, in parallel —

1. **Standards axis**: "Does the code conform to this repo's documented coding
   standards?" Reads a `coding-standards.md` from the repo and checks against it; also
   carries the Fowler smell catalog (see the prior-invocation finding).
2. **Spec-fidelity axis**: "Does the code faithfully implement the originating issue, PR,
   or spec?" Walks through each part of the originating artifact against the diff.

Two placement decisions travel with the pattern:

- **Coding standards live outside agents.md** — "they're supposed to be somewhere
  separate, and the code review point is where they're most useful." Standards are pulled
  at review time rather than pushed into every session's context.
- **Refactoring lives in review, not implementation** — v1.1's TDD skill dropped from
  red-green-refactor to red-green, with refactoring judged "a lot more productive" at the
  code-review stage "because then you don't overload the implementation."

## Why It Matters

The two axes have different failure modes when merged: a single reviewer anchored on the
spec forgives style debt; anchored on standards, it rubber-stamps scope drift. Splitting
them gives each subagent one question and clean context — the same isolation logic the
engine already applies in generator-assessor separation, here applied *within* the
assessor side. The standards-placement claim is a concrete instance of pull-over-push
context loading: reference material consulted at a known decision point shouldn't pay
always-loaded rent. And the refactor relocation keeps the implementation loop (and any AFK
implement skill) single-purpose.

## Why People Are Using It

Graduated out of in-progress status in Pocock's repo — it's the review step his `/implement`
skill calls on every ticket, so it sits in the default path of one of the most-used skill
suites in circulation.

## Potential Alternatives

Single-reviewer combined rubric (cheaper, dilution risk). N independent full-scope passes
(headless multi-pass — samples the space rather than partitioning it; complementary, not
competing). Deterministic gates for the standards axis (linters/CI) with an agent only on
spec fidelity.

## Potential Improvements

A third axis where relevant (security, performance) as additional parallel subagents.
Cross-axis conflict resolution (standards fix that breaks spec intent). Feeding axis
disagreement rates back into standards-doc quality.

## Potential Failure Modes

- **Missing substrate**: no coding-standards.md means the standards axis reviews against
  nothing — the pattern silently degrades to spec-only review.
- **Gap between axes**: defects that are neither standards violations nor spec deviations
  (latent bugs in unspecified behavior) belong to neither reviewer.
- **Double-flagging noise**: both axes reporting the same hunk in different vocabulary
  doubles triage cost without an aggregation step.
