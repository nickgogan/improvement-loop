---
name: 'Per-Proposal Human-Gated Promotion Pipeline (Threshold → Sandbox → Grade → Gate → Log)'
summary: 'A fixed five-stage pipeline turns an at-threshold lesson into a system change: draft the minimal edit against the owning surface, validate it in a shadow sandbox, grade it in a separate assessor context against a binary rubric, present one human gate per proposal (never batch), and log both outcomes append-only. A declined proposal is signal, not failure. Rollback is a git revert plus a new log row — the audit trail never rewrites history.'
implementation_notes: 'How this could apply to the MetaSystem engine — Phase 2 of its restructure program will size a second-brain-for-operations against this store model; IB-172 (layered memory architecture) is the related backlog item. The pipeline composes three patterns the engine already holds (sandbox-first validation, generator-assessor separation, human gate) into one concrete production loop with a proposal shape and an audit-log schema that could be lifted nearly verbatim.'
category: Governance
evidence_strength: Medium (practitioner-documented, single production system with live store evidence)
adoption_status: Not Yet Started
priority: P1 (Direct Adoption)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-ops-self-improve.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- human-gate
- promotion-pipeline
- self-improvement
- audit-log
- proposal-shape
---

# Per-Proposal Human-Gated Promotion Pipeline

## Why It Matters

The dangerous step in any self-improving system is the write-back: the moment an accumulated lesson modifies a live control surface. CareerBuddy shows a complete production answer — every write-back runs the same five stages, every stage has a hard failure rule, and the human sees exactly one decision at a time with everything needed to judge it. Sixteen proposals have flowed through it, each individually graded and gated; batch approval is defined as "a failed gate."

## What It Is

For each open lesson at threshold, the `promote` mode runs: **draft → shadow sandbox → separate-context grade → per-proposal human gate → append-only log**. The applying commit references the lesson (`Refs: ops/self L-<seq>`), so the log, the lesson, and git history triangulate.

## How It Works

**Proposal shape (one per lesson, minimal by construction):**
- **The edit** — the smallest change to the owning surface that prevents recurrence. If the honest fix is large, the proposal becomes "dispatch a rewrite run to the meta layer," not a direct edit.
- **Evidence** — the lesson's occurrences and source traces, verbatim.
- **Blast radius** — what else reads the edited surface, one line.
- **Class** — working file vs. governance surface; governance surfaces are proposal-only without exception.

**Shadow sandbox (fail-closed):** copy the owning surface to `ops/tmp/`, apply the edit to the copy only, run the surface's *own* validators. Validators fail → the proposal never reaches the gate; the failure is recorded on the lesson and the run stops.

**Grading — separate assessor context (hard invariant):** the drafting context never grades. A fresh context receives only the lesson, the proposal, the shadow diff, and the rubric — four binary checks: **grounded** (traces to evidence, not taste), **minimal** (scope creep = fail), **effective** (would have prevented the recorded occurrences), **non-regressive** (shadow passes; contradicts no standing guard). Any fail → back to drafting.

**The gate:** per proposal, never batch. The operator sees diff, evidence, blast radius, class, grade — and applies or declines. Both outcomes are terminal and both are logged (`P-<seq> · date · L-<seq> · applied|declined` with Proposal / Surface / Diff summary / Grade fields). "A declined proposal is signal, not failure — it often means the owning surface was misidentified."

**Rollback:** a regressing applied proposal is `git revert`ed, the lesson reopens with an occurrence note, and a *new* P-row records the reversal — the audit trail never rewrites history.

**Live evidence:** proposal-log.md P-1 through P-16, all with one-line grades; a P-6 numbering collision was resolved in-file with an explicit resumption note rather than renumbering (append-only discipline held even for its own bookkeeping errors). Where a shadow sandbox fit poorly (script edits), the log records substituted *deterministic verification* — regenerate outputs from the original seed and diff (P-12) — keeping the "validated before gate" invariant while swapping the mechanism.

## How It Could Fail

- Gate fatigue: sixteen sequential per-proposal decisions is fine at low volume; at high volume the operator rubber-stamps and the gate degrades into batch approval by another name.
- The minimality rule pushes real restructuring needs into repeated small patches unless the "dispatch a rewrite instead" escape hatch is actually used.
- Separate-context grading costs a subagent per proposal; under time pressure the temptation is inline self-grading — CareerBuddy makes that a named stop rule ("asked to self-grade → decline").
