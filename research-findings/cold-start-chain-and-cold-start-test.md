---
name: 'Cold-Start Chain as Load Order, Cold-Start Test as System Regression Test'
summary: 'A fresh agent session follows one documented, ordered load path from zero context to working state: always-on entry file → active-user context → vision layer → control surfaces → method router → task skill. The system''s standing regression test is the cold-start test: a fresh session loading only the standard entry points must state the system''s purpose and the next unit of work with zero guidance. The same test, run as a "cold-start echo," is the acceptance test for installing the system on a new harness.'
implementation_notes: 'The engine''s Phase 0 spine (PROGRESS.md as the only cold-start artifact, wake-up idiom) is a two-hop version of this. The adoptable delta: (1) document the engine''s full load order explicitly as a chain, (2) institutionalize the cold-start test as a periodic regression check — fresh session, standard entry points only, must state purpose + next unit of work, and (3) use the echo form ("state what actually composed") as the acceptance test whenever wiring changes or the kernel is ported.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P1 (Direct Adoption)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-wiring-canon.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- cold-start
- session-continuity
- load-order
- regression-test
---
# Cold-Start Chain as Load Order, Cold-Start Test as System Regression Test

## What It Is

Two coupled patterns. The **chain**: a documented, ordered load path a fresh session
follows from zero context to working state — always-on entry file → active user's
profile and invocation context → vision layer (PRD + ARCHITECTURE) → control surfaces
(system-track PROGRESS.md + user-track PROGRESS.md) → method router → the skill for the
task at hand. The **test**: a fresh session, loading only the standard entry points,
must be able to state the system's purpose and the next unit of work with zero guidance.

## Why It Matters

Plain English: sessions are stateless, and the only way to make them *disposable* — no
session depending on a previous conversation — is to make the path from nothing to
working state explicit and then continuously test it. Most systems document their
context files; almost none define the pass/fail condition for whether a cold session
actually composes. The cold-start test turns "is our context wiring healthy?" from a
feeling into a runnable check, and it doubles as the acceptance test for any harness
port.

## How It Works

- **Only the first hop is platform-specific.** The chain's first hop is whatever file
  the platform reads unconditionally; every hop after that is workspace-internal
  (file-to-file pointers) and moves unchanged across harnesses. This isolates harness
  lock-in to a single link.
- **Control-surface split:** the root PROGRESS/HISTORY pair is the system track only;
  each user's execution track lives in their own scope. Identity discipline: user
  display names never appear in root surfaces — path-form ids only.
- **The chain terminates in the operating contract:** autonomy tiers, standing guards,
  and session protocol live in one authoritative ARCHITECTURE section; the canon
  requires the chain to *reach* it, not restate it (pointer discipline again).
- **The test as install acceptance ("cold-start echo"):** after wiring the system onto
  a new harness, run the test as a push report — the fresh session must echo what
  actually composed: the system's purpose, the active-user pointer, the next unit of
  work, and which wiring rows are live vs degraded, with zero guidance. If the echo
  fails or misstates any of these, the install is not done; return to the failing row
  and re-run.
- **Doc convention supporting the chain:** every top-level content folder carries a
  human-facing HUMANS.md and an agent-facing AGENTS.md; new content folders scaffold
  both in the same change, so the router layer never lags the tree.

## How It Could Fail

The test only guards what the entry points reach — context loaded by habit in warm
sessions can mask a broken chain for weeks. The echo can pass while lying if the grader
is the same session that composed (self-assessment); run it fresh and verify the stated
next unit of work against the control surface. A chain with too many hops reintroduces
the ramp-up cost the pattern exists to kill.
