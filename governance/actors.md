---
title: "Engine Actors"
id: "engine-actors"
type: "governance"
category: "kernel"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-07-16"
updated: "2026-07-16"
author: "claude"
gated_by: "nick"
tags:
  - "kernel"
  - "actors"
  - "phase4"
---

# Actors: Improvement Loop (the engine)

> **Kernel document.** Every section approved by Nick in the Phase 4 interview
> (2026-07-16). The full per-agent contracts remain canonical in `agents/*/agent.md`;
> this kernel doc is the system-level view a downstream consumer reads first. The
> per-agent YAML descriptors (PRD E3) will make it machine-readable.

Updated: 2026-07-16 · Approved by: Nick

## Actor model

**Status: RULED (2026-07-16, interview Block C1): four actors, full stop.**

The engine is a **four-actor system with file-mediated communication** (DD-82). Actors
never talk directly — handoffs travel through the filesystem (`pipeline_status` fields,
queues, reports), which is what lets them run in separate sessions, at different times,
on different harness invocations. The human steward holds a fifth, shrinking seat
(§The human seat).

Today all four actors typically execute inside one interactive session as dispositions
selected by the invoked skill, with Owner as default (DD-86). That is an implementation
detail of the current harness, not the model: the kernel describes four actors, and the
target harness (PRD E4) runs them as separately woken sessions.

## The four actors

**Status: APPROVED (2026-07-16, interview Block C2). Compressed from
`agents/*/agent.md` (canonical); no contract content changed.**

| Actor | Owns | Task boundary | Write access (invariant) |
|-------|------|---------------|--------------------------|
| **Owner** | System stewardship — governance, drift, docs, feedback, audits; (target state) orchestration of the other actors | Mechanics autonomous, content gated: files DDs, applies authorized supersessions, fixes drift; never raises its own autonomy, never crosses system boundaries | `governance/`, `knowledge/`, docs, DD/IB registries, `operations/`; charter + CLAUDE.md + agent constitutions proposal-first |
| **Researcher** | Pipeline stage 1 — intake, KB population, KB maintenance | Expansive intake, ruthless extraction; neutral on implementation; never advocates adoption | `research-findings/`, `research-sources/`, `research-authorities/`, `watched-libraries/`, `watched-blogs/`, `operations/`; never `extracts/` or governance |
| **Codifier** | Pipeline stages 2–3 — classification, extraction, guide synthesis | Form follows evidence (Form Router rubric); stages, never deploys | `extracts/`, `operations/`, `project-management/design-notes/`; findings metadata only (`pipeline_status`, `consumed_by`), never finding content |
| **Librarian** | Consumption layer — KB queries (Teacher/Builder), assess/design skills | Citation-grounded, KB-scoped; reports gaps, never fixes them | Read-only on the KB (sole exception: its own `reflections/`) |

Each actor keeps: its constitution (core truths, boundaries, vibe, continuity) and
autonomy table in `agents/<actor>/agent.md`; its skill inventory (listed per-agent in
`CLAUDE.md` §Skills); an agent-private `reflections/` folder. Two are additionally
invocable as workspace subagents (`.claude/agents/owner.md`, `.claude/agents/librarian.md`).

**Fields deliberately left to later epics:** per-actor memory surfaces (PRD E1 designs
them), per-actor work queues (PRD E2 builds them), machine-readable descriptors
(PRD E3 encodes all of it as one YAML per actor + per harness).

## Orchestration — target state

**Status: APPROVED (2026-07-16, interview Block C3 elicitation).**

The end-state operating model, ruled at this interview:

- **The Owner is the acting owner of the whole system.** It uses the harness to wake
  the other actors in separate sessions to do their work.
- **Every actor has a work queue — including the Owner.** A researcher queue, a
  codifier queue, a librarian queue, an owner queue (PRD E2 rules the queue/task
  contract).
- **Wake-up is periodic and signal-driven.** Either a meta-harness or the Owner itself
  wakes on a schedule and processes queues; file-mediation signals (the communication
  protocol's status fields and queue entries) wake or assign work to the other actors.
- **The human is out of the loop by default.** Sessions are not human-initiated in
  steady state; the human's residual role is §The human seat.

Path there: today's model (human-initiated sessions, dispositions-by-skill) is the
degenerate case — one session, queues empty, human as scheduler. E2 (queues) + E4
(wake/dispatch machinery) close the gap. Autonomy expansion along the way follows the
constitution's gates: delegated-judgment grants, rulings listed for review — the
supervised-autonomy trajectory (DD-108) run to its endpoint.

## The human seat

**Status: APPROVED (2026-07-16, interview Block C3).**

**Today:** Nick gates decision content, promotions/deployments, autonomy-tier changes,
and one-way doors (constitution §Governance & permissions). AI executes mechanics and
two-way doors (door-type delegation).

**End state:** the human does almost nothing operationally — comes in every once in a
while to **review what has changed** with the system, and occasionally **uses it** to
get value from it. Gates migrate to the Owner under recorded delegated-judgment grants
as trust accrues; every delegated ruling stays listed for after-the-fact human review.

**What stays human even at end state** (the human/AI seam, wave-3 ruling):

- Reviewing the change log and overriding any delegated ruling (all remain reversible
  by construction — two-way-door discipline).
- Constitutional amendments and supersession of kernel documents (DD-44 class).
- Practically irreversible or outward-facing acts: external publication, spend,
  cross-system writes.
- Being the beneficiary — the system exists to produce value for its human, not to
  run for its own sake.

## Communication protocol

**Status: APPROVED (2026-07-16, interview Block C2; pointer section).**

File-mediated only; no direct actor-to-actor channel. The canonical protocol
(`agents/handoff-protocol.md`) defines the `pipeline_status` state model
(`raw → classified → extracted` / `raw → synthesized`) and per-stage interface
fields. PRD E2 extends this from pipeline handoffs to general work queues; the
signals that wake actors in the target state are this same protocol's writes.
