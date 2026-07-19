---
name: QA Plan as Agent Trust Gate (Delegation-Depth Lever)
summary: |-
  A required artifact — the "QA plan" — documenting, per feature, the critical user
  journeys and how users engage with the app/API/service being changed, plus what media
  (screenshots, logs, recordings) should be attached to the PR as evidence of correct
  behavior. Written once by the most product-knowledgeable engineer, then enforced
  mechanically: "all user-facing work has a QA plan" becomes an assertable expectation a
  review agent can check. Lopopolo (OpenAI) frames it explicitly as a trust lever, not
  just a correctness lever: having the QA plan is what lets him "trust the output more,
  need to shoulder-surf the agent less, and remove myself from the loop even more to
  delegate more and more of the work to agents."
implementation_notes: |-
  The engine already produces an analogous artifact at the end of every Pass 2 extraction
  batch — a MANIFEST is itself a QA-plan-shaped trust gate for Nick's human review. Worth
  an explicit design pass on whether /extract-artifacts and the self-improve promotion
  pipeline should require a similarly-shaped "what was proven, what evidence backs it"
  block before staged work reaches the human gate.
category: Governance
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- Improvement Loop
- General
adopted_in: []
sources:
- harness-engineering-humans-steer-agents-execute.md
related_findings:
- file: trust-calibration-progressive-autonomy-ramp.md
  rel: same-problem
- file: reviewer-skill-elevation-for-agentic-output.md
  rel: extends
- file: agent-proof-of-work-ui-trust-building.md
  rel: same-problem
- file: pre-code-validation-contracts-dual-blind-validators.md
  rel: same-problem
- file: harness-engineering-third-evolution.md
  rel: extends
- file: garbage-collection-day-persona-review-agents.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-18'
last_updated: '2026-07-18'
pipeline_status: raw
consumed_by: []
---

## What It Is

A specific documentation artifact — the QA plan — required for all user-facing work.
Its content: the features being changed, the critical user journeys through them, and
how users actually engage with the app, APIs, and services involved. It also specifies
what media should be attached to the PR (screenshots, logs, recordings) as evidence the
work was actually done, not just claimed done. One engineer on the team wrote down, once,
what a good QA plan looks like for the team's product surface; from then on a review
agent can mechanically check "does this PR have a QA plan, and does the attached media
actually demonstrate the claimed behavior?" without a human having to personally
transmit that product knowledge on every review. The framing is explicitly about trust,
not just correctness: the QA plan is what lets the engineer delegate more of the loop to
agents, because the agent's own output now carries legible proof of having done the job.

## Why It Matters

This gives trust-calibration-progressive-autonomy-ramp.md's abstract claim ("trust builds
through demonstrated reliability, unlocking broader scope") a concrete mechanism: what
specifically gets checked to grant that trust, and what artifact the agent must produce
to make its own reliability legible to a reviewer who didn't watch it work. It's also a
direct answer to a gap reviewer-skill-elevation-for-agentic-output.md names but doesn't
resolve — "MetaSystem could develop review checklists... that reduce cognitive load" —
the QA plan is exactly that checklist, authored once by the most qualified person and
then mechanically enforced rather than re-derived by every reviewer on every PR.

## Why People Are Using It

The team's own account: blocking on ad-hoc, low-signal code review to transmit "what does
a good QA plan look like" didn't scale past one engineer's attention span. Writing it
down once and asserting it as a gate meant every agent trajectory — not just the ones a
particular reviewer happened to catch — got the benefit of that one engineer's product
knowledge.

## Potential Alternatives

- **Manual per-PR review checklists a human fills out:** carries the same information,
  but re-derived (or skipped) each time rather than durably encoded and mechanically
  enforced.
- **Factory's pre-code validation contract** (pre-code-validation-contracts-dual-blind-validators.md):
  assertion-based and written pre-implementation, rather than usage/journey-based and
  applied at PR-review time — a different, formally-stricter axis of "what counts as
  proof of done." The two are convergent evidence from different vendors for the same
  underlying instinct (define done before or alongside the work), not the same mechanism.

## Potential Improvements

- A minimum-viable QA-plan template scoped to the artifact type (finding, guide, skill,
  agent) rather than requiring the same shape for every deliverable.
- Fold the QA-plan-presence check into the persona-review-agent architecture in
  garbage-collection-day-persona-review-agents.md rather than treating it as a separate
  gate — one persona (e.g., "product/QA reviewer") owns it.

## Potential Failure Modes

- **Hollow-but-present plans:** boilerplate critical-user-journeys that don't reflect the
  actual change can pass a mechanical "does it exist" check without providing real
  evidence — presence is not the same as quality.
- **Fakeable or stale media:** a screenshot from an earlier run, not the actual PR's
  behavior, satisfies the letter of the requirement; the check needs to verify
  provenance, not just presence.
- **Coverage skew:** trust concentrates on QA-plan-covered (user-facing) work while a
  whole class of non-user-facing work (infra, internal tooling) has no equivalent gate
  and silently gets less scrutiny even as delegation deepens across the board.
