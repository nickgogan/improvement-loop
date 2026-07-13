---
name: "Add-Then-Retire Abstraction Lifecycle at Framework Scale"
summary: |-
  Plain English: a healthy framework retires capabilities as routinely as it adds them
  — each retirement shipped with a stated cost rationale and a migration path, which is
  what keeps a 47-skill suite from becoming 60. Within eight minor versions BMAD
  retired four capabilities: bmad-investigate ("reached the same conclusions as plain
  investigation at higher cost; the case-file artifact didn't justify the overhead"),
  the standalone deletion auditor (folded into edge-case hunter: "cold-start cost for
  near-zero yield"), bmad-distillator (superseded by bmad-spec), and bmad-automator
  (superseded by bmad-loop) — each with forwarding shims and installer cleanup, removal
  scheduled as a feature-grade change. Upstream corroboration for the engine's
  standing "abstractions must earn their keep" rule (IL agent-rules rule 11), adding
  the piece the rule doesn't specify: a worked deprecation mechanic.
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P3 (Monitor)"
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "ratchet-recipe-skill-retirement.md"
    rel: "same-problem"
  - file: "benchmark-dataset-deprecation-lifecycle.md"
    rel: "same-problem"
  - file: "skill-library-drift-failure-mode.md"
    rel: "same-problem"
  - file: "tool-pruning-as-harness-maintenance.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
tags:
  - "governance"
  - "lifecycle"
  - "abstractions-earn-their-keep"
---

# Add-Then-Retire Abstraction Lifecycle at Framework Scale

## What It Is

An observed deprecation practice, exercised four times in eight minor versions
(v6.3.0–v6.10.0):

| Retired | Rationale stated in changelog | Path |
|---------|-------------------------------|------|
| bmad-investigate | Same conclusions as plain investigation at higher cost; case-file artifact didn't justify overhead | Removed; capability folded back into ordinary usage |
| Standalone deletion auditor | "Cold-start cost for near-zero yield" | Folded into edge-case hunter |
| bmad-distillator | Superseded | Replaced by bmad-spec |
| bmad-automator | Superseded | Replaced by bmad-loop |

Three properties make it a lifecycle rather than housekeeping: every removal carries a
*cost rationale* (the abstraction was tried and measured against its overhead), every
removal ships a *migration path* (forwarding shims that route legacy invocations to the
successor with the right intent, installer cleanup, removal pre-announced for v7), and
removal is treated as *feature-grade change* — changelogged with the same prominence as
additions.

## Why It Matters

Skill/agent suites ratchet upward by default: additions have advocates, removals have
none, and the suite's context cost grows monotonically. This is production evidence
that the counter-discipline works at framework scale — including the humility case
(bmad-investigate was added in v6.7.0 and retired in v6.10.0; three versions from ship
to kill, with the failure reason published). For the engine, this corroborates the
standing "abstractions must earn their keep" rule and supplies what the rule lacks: the
retirement half. Earning keep is an ongoing test, and the mechanics of failing it —
stated rationale, shim, scheduled removal — are reusable as-is.

## Why People Are Using It

Practiced by a 47-skill framework shipping to 42 platform targets, where every retained
skill costs every installation context and maintenance. Source: Observed in
[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) v6.10.0 — see
[[bmad-method-analysis]] for structural details.

## Potential Alternatives

- **Outcome-linked automated retirement** (ratchet recipes: usage/contribution
  thresholds, capped active banks) — the measured, mechanical version; BMAD's is
  judgment-based with published reasoning.
- **Accretion + periodic spring-cleaning** — the common default; removals arrive in
  batches, unrationalized, and users learn to distrust upgrades.
- **Never retire, only deprecate** — keeps compatibility forever at permanent context
  and maintenance cost.

## Potential Improvements

- Pre-registration: declaring at *add* time what evidence within N versions would
  justify retirement would make the lifecycle symmetric.
- Retirement telemetry — usage data cited in the rationale rather than qualitative
  cost judgments.

## Potential Failure Modes

- **Shim accumulation** — forwarding shims are themselves abstractions; without their
  own removal schedule (BMAD pins theirs to v7) they become the new sprawl.
- **Churn tax** — aggressive retirement breaks user muscle memory and tutorials;
  feature-grade changelog treatment mitigates, not eliminates.
- **Rationale theater** — a stated reason is not a measured one; cost rationales can
  rationalize decisions made for other reasons.
