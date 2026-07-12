---
name: "Reference-Only Skill Shape for AFK Agents"
summary: |-
  Plain English: if a skill will be handed to an unattended (AFK) agent, prescriptive
  step-by-step procedure is the wrong shape — steps assume an interactive walkthrough with
  a human present. Pocock's v1.1 TDD skill was converted from a stepped procedure (confirm
  tests with the user, walk through together) to reference-only material: no steps at all,
  just the invariants that constrain any correct execution — "red before green, one slice
  at a time" — with refactoring split out of the loop entirely (into code review). The
  driver was user expectation: "you should be able to pass an AFK agent the TDD skill and
  it should just work." Consumer autonomy, not content size, decided the skill's shape.
implementation_notes: |-
  Rubric-relevant for /design-skill (construction: output/procedure shape decision): the
  steps-vs-reference choice should be driven by who consumes the skill — interactive
  sessions tolerate (and benefit from) stepped procedure with gates; AFK/autonomous
  consumers need ordering invariants expressed as reference, relying on the agent's priors
  and harness for the loop mechanics. Complements the skill-content-lifecycle guidance
  that skill bodies read as standing instructions, not one-time setup. Nick-gated
  restructure Phase 2 decides substrate entry.
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "IL (assess-skill/design-skill substrate)"
  - "General"
adopted_in: []
sources:
  - "pocock-skills-v1-1-wayfinder-research-implement.md"
related_findings:
  - file: "branch-analysis-externalization-rule-skill-reference.md"
    rel: "extends"
  - file: "skill-content-lifecycle-context-budget.md"
    rel: "same-problem"
  - file: "leg-work-amplification-hiding-future-steps.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

# Reference-Only Skill Shape for AFK Agents

## What It Is

A shape decision within the steps+reference anatomy of skills: for consumers that run
unattended, drop the steps unit entirely and ship the skill as **reference-only** —
invariants that constrain execution order without scripting an interaction. The worked
example is Pocock's v1.1 TDD skill: the old version prescribed steps (confirm intended
tests with the user, walk through the loop), which "didn't fit with most people's idea of
how TDD should work — you should be able to pass an AFK agent the TDD skill and it should
just work." The new version specifies only the ordering invariants — red before green, one
slice at a time — and removes refactoring from the loop (relocated to code review) so the
implementation loop stays minimal.

The companion data point is the v1.1 `/implement` skill: a five-line, almost-empty skill
("implement per spec/tickets, TDD at pre-agreed seams, type-check regularly, full suite
once at the end, then code review and commit") that Pocock almost didn't write because it
"mostly relies on the agent's priors and the harness." Minimal skills earn their place as
flow markers, not instruction payloads.

## Why It Matters

It gives `/design-skill` a construction-time question the current substrate doesn't ask
crisply: **who consumes this skill, and at what autonomy level?** Interactive skills can
carry stepped procedure, human gates, and confirmation checkpoints; a skill destined for
AFK/background agents must instead express its content as standing invariants, because
there is no user present for the steps to coordinate with. Written the wrong way round,
the failure is silent — an AFK agent either stalls at a phantom checkpoint or ignores the
choreography. This is the same insight as "standing instructions, not one-time setup" from
the skill-content-lifecycle finding, promoted from a compaction concern to a primary
design axis.

## Why People Are Using It

Shipped in v1.1 in response to repeated user requests — the stepped TDD skill was
"awkward" in practice, and the reference-only rewrite matches how users actually deploy
TDD guidance (attached to autonomous implementation runs).

## Potential Alternatives

Two skill variants (interactive-tdd and afk-tdd) — duplication with drift risk. Branching
inside one skill ("if running unattended, skip gates") — workable but pays the branch in
every context. Harness-level modes (plan/auto-accept) — orthogonal; the skill content
still has to match.

## Potential Improvements

A frontmatter conventions for declaring intended consumer autonomy (interactive /
supervised / AFK), lintable against the presence of steps and gates. Applying the same
test to agent definitions, not just skills.

## Potential Failure Modes

- **Invariants too thin**: reference-only works when the loop mechanics live in the
  model's priors (TDD does); for procedures without strong priors, deleting the steps
  deletes the skill.
- **Lost human gates**: converting to AFK shape removes checkpoints that existed for
  safety, not choreography — gates must be re-homed (e.g. into review), not just dropped.
- **Wrong-audience reuse**: an interactive session invoking the AFK-shaped skill loses
  the collaborative confirm-points users may still want.
