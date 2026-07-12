---
name: "Autonomy Progression Gated by System Maturity (Level-3 Sandwich)"
summary: |-
  Plain English: don't buy autonomy — earn it, and earn it in a specific order. Cole
  Medin's position (built on Dan Shapiro's five-level ladder, spicy autocomplete → dark
  factory): the sweet spot of reliability and autonomy is level 3, where you delegate
  100% of the coding *because* human planning and human validation sandwich the
  implementation on both sides. Progression to levels 4-5 is not achieved by granting
  more autonomy — it is achieved by building a supervised system first, evolving it after
  every mistake, and then *removing the human* from steps the system has already proven
  it can carry ("you build that muscle of what you can trust your system to accomplish").
  The direction is invariant: subtract oversight from a trusted workflow, never add
  autonomy to an untrusted one. Notable because Medin — who built his own dark factory
  experiment — argues from independent evidence for the supervised tier the engine's
  DD-108 already commits to.
implementation_notes: |-
  Third distinct source arguing the supervised-autonomy/maturity-gated-progression
  position (with the trust-calibration ramp and autonomy-gradient source sets) —
  flagged as a DD-108 evidence-strength candidate for the next /reassess-priorities
  pass. Design-relevant detail: the readiness signal for removing a gate is subjective
  confidence built from repeated system evolution ("I know my coding agent will knock
  this out of the park — I don't even have to iterate on the plan"), i.e. per-workflow,
  not global.
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "IL (gate design, DD-108 lane)"
  - "General"
adopted_in:
  - "Improvement Loop"
sources:
  - "the-best-ai-coding-setup-isnt-the-most-autonomous-one.md"
related_findings:
  - file: "trust-calibration-progressive-autonomy-ramp.md"
    rel: "extends"
  - file: "autonomy-gradient-not-binary-delegation.md"
    rel: "same-problem"
  - file: "human-on-the-loop-hotl-autonomy-tiering-framework.md"
    rel: "same-problem"
  - file: "dark-factory-ai-only-codebase-management.md"
    rel: "extends"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-12"
pipeline_status: "raw"
---

## What It Is

Two coupled claims mapped onto Shapiro's five-level autonomy ladder:

**The level-3 sandwich principle.** Full coding delegation (the agent writes every line;
Medin hasn't written code in over a year) is justified *only* by what brackets it: the
human is deeply in the planning (structured plan, validation strategy, the agent grilling
the human to remove assumptions) and in the validation (unit + end-to-end + human
spot-check). "The only reason we delegate all the coding and trust it is because we're
sandwiching the implementation with planning and validation we are very much a part of."
Level 4 (epic/PRD-sized delegation, human at the ends only) and level 5 (spec in, shipped
code out) shrink the sandwich until it disappears.

**Maturity-gated progression.** The path to higher levels is subtractive: build the
supervised system (rules, skills, subagents composed into a research → plan → implement →
validate flow), evolve it after every mistake ("what part of our AI layer can we improve
so this doesn't happen again"), and only when a workflow reliably needs no plan iteration
and no validation beyond spot checks, remove the human from *that* workflow. Reliability
"really starts to tank" at level 4 for anyone without that established system — the level
that's right for you changes over time, and jumping levels ahead of system maturity is
the failure mode.

## Why It Matters

This is the operational answer to "when do we loosen a gate?" — not a matrix assigned up
front but a ratchet: per-workflow trust accumulated through system evolution, spent by
removing one human touchpoint at a time. It reframes autonomy as an *output* of harness
maturity rather than a setting. For the engine, it corroborates DD-108's supervised
posture from a source with skin in the opposite game — Medin sells autonomy tooling,
built a dark factory experiment, and still tells his audience to stay at level 3 "for a
long time."

## Why People Are Using It

Medin operates at level 3 across all his production work and teaches it (Dynamis
community/course); StrongDM's documented production dark factory plus rumored
banking-sector deployments define the far end that maturity-gated progression is aimed
at. The driving-automation analogy (level 3 = "Waymo with a safety driver") is doing real
work: the industry that coined the levels also learned that skipping them kills.

## Potential Alternatives

- Static autonomy assignment by blast radius/reversibility (the autonomy-gradient 2x2) —
  complementary: the gradient sets the floor per decision type; maturity gating governs
  movement over time
- Capability-triggered autonomy (grant more when the model improves) — Medin's framing
  rejects this: trust attaches to the *system* (harness + process), not the model

## Potential Improvements

- Objective promotion criteria to replace felt confidence: N consecutive runs with zero
  plan iterations and zero validation findings before a gate is removed
- Demotion symmetry: a mistake in a promoted workflow reinstates the removed human
  touchpoint (the ratchet must run both ways)

## Potential Failure Modes

- Confidence outruns evidence: "I know it'll knock this out of the park" is a feeling;
  without failure telemetry it drifts into supervision debt
- Trust earned on one workflow silently generalized to another ("it handles features, so
  it can handle migrations")
- Model or harness updates invalidate accumulated trust without resetting the ratchet
- Level-4+ failure modes arrive exactly when attention has been withdrawn by design —
  see the dark-factory failure taxonomy (cascading failures, stalled handoffs,
  evaluation gaming)
