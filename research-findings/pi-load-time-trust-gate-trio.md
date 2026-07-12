---
name: 'Pi Load-Time Trust Trio — Trust Gate, Declared Absences, Loaded-State Report'
summary: 'Three composition-time honesty mechanics attributed to the Pi harness in CareerBuddy''s MV21 Phase R research: a load-time trust gate (composed parts pass a trust check before they join the system), declared absences (the system states what it does NOT enforce, as first-class data), and a loaded-state report (after composition, report what actually loaded rather than what was supposed to). CareerBuddy adopted all three fingerprints into its shipped contract and adaptation protocol; the primary research brief was swept at ship.'
implementation_notes: 'Queued by CareerBuddy explicitly as a corpus contribution to this engine. The trio maps cleanly onto the engine: (1) trust gate — the engine''s intake of external artifacts (imported skills, consumer submissions) could carry an explicit load-time trust framing; (2) declared absences — the engine''s own governance already has undeclared enforcement gaps (prose rules vs hooks) that a declared_absences block would make honest; (3) loaded-state report — the cold-start echo pattern: a fresh session reports what actually composed, not what PROGRESS.md claims. Before design work, re-research Pi from primary sources to restore the swept evidence — treat this finding as a pointer.'
category: Governance
evidence_strength: 'Low (backlog entry plus downstream-artifact fingerprints; the primary MV21 research brief was swept at ship and the clone is shallow, so R3''s Pi analysis could not be located)'
adoption_status: Not Yet Started
priority: P3 (Watch)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-improve-backlog-corpus-contributions.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- trust-gating
- declared-absences
- loaded-state-report
- cold-start
---
# Pi Load-Time Trust Trio — Trust Gate, Declared Absences, Loaded-State Report

## What It Is

A trio of load-time mechanics from Pi (a coding-agent harness with a typed-composition
model, surveyed as research thread R3 — "Pi typed-composition/trust-gate model" — in
CareerBuddy's MV21 Phase R research):

1. **Load-time trust gate** — components pass a trust check at the moment they are
   composed into the running system, not after they act.
2. **Declared absences** — the system carries an explicit, machine-readable statement of
   what it does *not* enforce, as a first-class part of its self-description.
3. **Loaded-state report** — after load, the system reports what *actually* composed
   (which parts are live, which degraded), rather than assuming the intended
   configuration took effect.

## Why It Matters

Plain English: most agent-system failures at install or session start are silent — a
rule file that never injected, a permission gate that was assumed but absent, a memory
scope that didn't mount. All three mechanics attack the same root: the gap between the
system you *think* is running and the system that *is*. The trust gate checks before
composition, declared absences keep the security story honest, and the loaded-state
report closes the loop by observing reality after composition. Together they turn "the
install succeeded" from an assumption into a report.

## How It Works

Evidence caveat first: the MV21 research brief containing the R3 Pi analysis was swept
at ship per CareerBuddy's lifecycle discipline, and the available clone is
single-commit, so the primary mechanics could not be recovered. What survives — and what
this finding documents — is the backlog entry plus three verifiable fingerprints the
trio left in CareerBuddy's shipped artifacts:

- **Loaded-state report → the cold-start echo.** ADAPTATION.md's design-provenance
  section states directly: "the cold-start echo from Pi's loaded-state reporting." The
  shipped acceptance test (step 6) is a push report: in a fresh session, load only the
  standard entry points, then "*echo what actually composed*" — purpose, active user
  pointer, next unit of work, and which wiring rows are live vs degraded, with zero
  guidance.
- **Declared absences → the contract's trust block.** `system-contract.yaml` carries
  `trust.declared_absences` as first-class data: no enforced permission system
  (prose-only guards), no continuous behavioral-conformance enforcement (narrowed twice,
  each narrowing versioned), no network isolation, sidecar coverage gaps. Absences are
  maintained — when a check became post-install-checkable, the absence was *narrowed* in
  a versioned contract change rather than deleted.
- **Load-time trust gate → trust-first install framing.** ADAPTATION.md opens with a
  mandatory trust framing before any step: "Read `trust:` in the contract first. You are
  installing a system that declares no enforced permission layer" — the receiving agent
  gates composition on reading the trust declaration, the declare-and-adapt analog of a
  load-time trust check.

## How It Could Fail

As a finding, the main risk is provenance: the trio is reconstructed from fingerprints,
and Pi's actual mechanics (typed composition, what the trust gate checks, report format)
may differ materially from this reconstruction — re-research from Pi's own docs/repo
before any design work builds on it. As a pattern, declared absences rot if not
maintained (an absence that was closed but never narrowed erodes trust in the whole
block), and a loaded-state report that echoes the config file instead of observed state
is worse than no report — it certifies the assumption it exists to test.
