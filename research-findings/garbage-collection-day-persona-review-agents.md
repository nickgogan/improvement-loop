---
name: 'Garbage Collection Day — Converting PR-Review Friction into Persona-Keyed Review Agents'
summary: |-
  A weekly ritual (Fridays, "garbage collection day") where every engineer's sole job is
  to take every piece of "slop" observed that week in PR review and durably eliminate the
  underlying cause — not with more review comments, but with documentation, tests, or
  lints that make the failure structurally impossible to repeat. Paired architecture:
  review feedback gets bucketed by the reviewing engineer's persona (front-end architect,
  reliability engineer, scalability engineer), and each persona gets its own review agent
  that triggers on every push, reads that persona's accumulated "what good looks like"
  docs, and surfaces any P2-or-above blocking issue. Lopopolo (OpenAI): "this is kind of
  how you go from synchronous human time spent giving feedback as code review comments to
  documentation in the repository... started to see slop reduce reduce reduce."
implementation_notes: |-
  IL doesn't have a multi-engineer PR-review flow to bucket by persona, but the underlying
  mechanism — recurring Nick feedback converted into a durable, automated check rather
  than re-given each session — maps directly onto the engine's /self-improve
  capture-and-promote loop; worth comparing garbage collection day's fixed weekly cadence
  against self-improve's scan mode.
category: Evaluation
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
- file: harness-engineering-third-evolution.md
  rel: extends
- file: multi-perspective-review-council.md
  rel: same-problem
- file: reviewer-skill-elevation-for-agentic-output.md
  rel: same-problem
- file: generator-assessor-separation-in-skill-iteration.md
  rel: same-problem
- file: ai-shepherding-anti-pattern-manual-workflow-sequencing.md
  rel: same-problem
- file: qa-plan-as-agent-trust-gate.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-18'
last_updated: '2026-07-18'
pipeline_status: synthesized
consumed_by:
  - "building-agent-evaluation-suites.md"
---

## What It Is

A time-boxed weekly ritual paired with a specific downstream architecture. Every Friday,
every engineer's job is to take every bit of slop observed over the week — anything that
made a PR difficult to merge — and figure out how to categorically eliminate it from ever
happening again, rather than just flagging it again next time. The loop this closes:
human gives feedback once (as a PR comment, indicating some context failure on the
agent's part) → during garbage collection day, that feedback gets converted into either
(a) a failing test or lint that makes the agent self-heal automatically, or (b) an
addition to a persona's review-agent documentation. Either way the fix is durable — the
next occurrence catches itself, without a human back in the loop. The downstream
architecture: the team buckets the *types* of review feedback they give into the persona
they were operating as when they gave it (front-end architect, reliability engineer,
scalability engineer), then spins up one review agent per persona, triggered on every
push, that asserts "is this code good?" against that persona's accumulated documentation
and surfaces any P2-or-above blocking issue before merge.

## Why It Matters

Directly names and operationalizes the mechanism the KB's "AI shepherding" finding
diagnoses as a problem (human as manual orchestrator/rememberer) without prescribing a
fix — garbage collection day is a concrete conversion mechanism, not just a diagnosis. It
also answers a question reviewer-skill-elevation-for-agentic-output.md leaves open: how
do you scale one senior reviewer's judgment to every PR without that reviewer personally
reading every diff? Capture the persona's judgment once, in writing, and deploy it as an
agent that runs on every push forever — every engineer driving agents gets the benefit of
every other engineer's expertise, not just their own blind spots.

## Why People Are Using It

Lopopolo's team (OpenAI) adopted this after finding that low-signal code review was both
a bottleneck (blocking on human availability) and a knowledge-transfer failure (only the
reviewing engineer benefited from having noticed a given pattern). Time-boxing the
"durably fix it" work to a fixed weekly slot prevented it from being perpetually
deprioritized against feature work. The team sustained 3-5 PRs/engineer/day on a 3-person
team without merge-conflict overhead becoming the dominant time sink — the throughput
outcome the pattern is meant to protect.

## Potential Alternatives

- **Continuous ad-hoc hardening** (fix each pattern the moment it's noticed): lower
  latency to fix, but competes with feature-work priority and tends to get deferred
  indefinitely — the exact failure mode garbage collection day is designed to prevent.
- **Multi-perspective review council's fixed four dimensions** (factual/domain/safety/
  style, see multi-perspective-review-council.md): pre-defined and uniform across
  projects; garbage collection day's persona set grows organically from whoever is
  actually reviewing, so review coverage matches the team's real expertise rather than a
  generic template.

## Potential Improvements

- A structured intake for garbage collection day itself: a running log of "slop observed
  this week" so the Friday session works from a queue rather than relying on memory —
  otherwise the ritual inherits the same context-loss problem it's meant to fix elsewhere.
- Explicit versioning or expiry on persona docs, so stale review criteria (from a team
  member who's left, or a convention that's since changed) don't silently keep blocking
  PRs.

## Potential Failure Modes

- **Unpruned growth:** persona review-agent documentation can accumulate contradictory or
  superseded guidance the same way any long-lived CLAUDE.md does, with no built-in
  garbage-collection for the garbage-collection artifacts themselves.
- **Persona coverage gaps:** a review dimension nobody currently on the team happens to
  embody (e.g., no one is "the accessibility reviewer") never gets a persona agent —
  coverage is a function of team composition, not task risk.
- **Convenience erosion under deadline pressure:** garbage collection day competes
  directly with feature work; the discipline is most likely to be skipped exactly when
  the backlog of unaddressed slop is largest.
