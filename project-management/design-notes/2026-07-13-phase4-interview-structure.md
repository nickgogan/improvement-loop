---
title: "Phase 4 interview structure — engine PRD, constitution, actors"
id: "phase4-interview-structure"
type: "design-note"
category: "architecture-direction"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-07-13"
updated: "2026-07-13"
author: "claude"
gated_by: "nick"
tags:
  - "design-note"
  - "phase4"
  - "interview"
  - "prd"
  - "constitution"
  - "actors"
  - "portable-kernel"
---

# Phase 4 interview structure

> **Prep artifact, drafted autonomously** (session 146, per PROGRESS.md: "an autonomous
> session should instead prep `phase4-interview`"). Nick gates this structure before the
> interview runs; nothing here is a decision. Method adapted from CareerBuddy
> `ops-vision-to-plan` v0.3.0 (import verdict locked in the program plan §4; source
> re-read from upstream `nickgogan/CareerBuddy` this session).

## 1. What the interview must produce

Plain English first: the interview is one or two sittings where Nick answers focused
questions and approves short drafts section by section, and at the end the engine has
its own kernel documents — the things any downstream consumer would pull.

Per program plan §Phase 4, the outputs are:

1. **Constitution** — the engine's vision/mission/values/principles layer, reconciled
   with `CHARTER.md`.
2. **PRD** — users, goals/non-goals, epics with binary acceptance criteria for the
   remaining program (harness + generalize).
3. **actors.md** — the engine's LLM actors: task boundaries, permission sets,
   dispositions.
4. **The ordering decision** — generalize-first vs harness-first → plan checkpoint #2
   (update the program plan).

One caution to hold during the sitting (Phase 1 delta report, insight #2): **no external
exemplar generates the layer above the PRD.** BMAD starts at analysis/PRD; the
constitution-first arc is engine-original. Where the method feels underspecified, that
is expected — resolve by judgment at the gate, not by searching for a reference.

## 2. Method — what we keep from `ops-vision-to-plan`, what changes

**Keep (the method IS the section gate):**

- Socratic elicitation — vision is extracted through questions, never invented; one
  focused question set at a time; **options-with-tradeoffs over open-ended prompts**
  when Nick seems undecided.
- **One section at a time, explicit approval before the next.** Two rejections of the
  same section → stop drafting and re-elicit (the misunderstanding is upstream of the
  prose).
- **Binary acceptance criteria** on every epic; testable DoD on every proposed
  milestone; no volatile metrics in any artifact.
- **Cold-start test** as the success bar: a fresh session loading PROGRESS.md plus the
  kernel docs can state the engine's purpose and next unit of work with zero guidance.
- **Re-entry mode as the default posture.** The engine is not greenfield — CHARTER.md,
  FOUNDATIONS.md, `agents/`, and the direction note already exist. Diff Nick's current
  intent against them and propose amendments; record supersessions, never silently
  rewrite.

**Change (engine deltas):**

- **Artifact chain reordered:** upstream runs brief → PRD → architecture → epics. The
  engine's governance-first model (direction note) puts the constitution above the PRD,
  and the architecture doc's role is largely played by the kernel's "how it works" +
  actors layers. Engine chain: **confirmation summary → constitution → PRD → actors →
  ordering decision → plan update**.
- **No standalone brief.** The brief's content (problem, who, outcome, constraints,
  out-of-scope, bet size) is already answered by the plan §1–2 and CHARTER.md. Instead,
  the interview **opens with a pre-filled brief-equivalent summary for confirmation** —
  drafted from the corpus, corrected by Nick — honoring the standing
  reduce-Nick-bottleneck rule: AI drafts from what exists; Nick corrects.
- **Outputs land in `governance/` as kernel content** (kernel litmus: a downstream
  consumer would pull all three). Proposed homes — Nick gates naming at the sitting:
  `governance/prd.md`, `governance/constitution.md` (or an amendment set to CHARTER —
  see Block A question 1), `governance/actors.md`.

## 3. Interview blocks

### Block 0 — one-line clarifications (minutes, no drafting)

Clear the two transcription artifacts assigned to the interview:

1. **"Attachés"** (direction note §research-deps; KB-wide search found nothing) — what
   was the intended word/ask?
2. **"Division, to a degree"** (direction note §governance-first) — garbled fragment
   after "principles"; possibly "provision," "vision to a degree," or a sixth
   governance element?

### Block A — Constitution (re-elicit + diff against CHARTER.md)

Pre-load: CHARTER.md, FOUNDATIONS.md, direction note §governance-first.

- **A1 — Charter relationship (structural, decide first):** is the engine constitution
  (a) CHARTER.md itself, compiled/pointed into the kernel; (b) an engine-scoped
  constitution that cites CHARTER; or (c) CHARTER superseded into the kernel doc?
  Present as options with tradeoffs (DD-105 put the charter at workspace root
  deliberately; the kernel litmus pulls constitution content into `governance/`).
- **A2 — Vision/mission/purpose diff:** CHARTER.md is 2026-06-18, pre-dating the
  kernel model and single-implicit-agent input. Probe: what in it is stale? Does
  "produces and audits agentic systems of any kind" survive as-is?
- **A3 — Values/principles:** confirm the charter's seven values still bind; elicit
  any principles that the last month's rulings (SL retirement, route-then-compact,
  door-type delegation) have made load-bearing but unwritten.
- **A4 — Governance & permissions: layers or cross-cutting?** (direction-note open
  question, assigned here by plan §Phase 4). The Databricks comparison partially
  resolved layer definitions; this question decides constitution *structure* — whether
  permissions get their own kernel section or fold into actors + harness description.

### Block B — PRD

Pre-load: plan §2 (target end state), Phase 1 delta report, PROGRESS Backlog.

- **B1 — Vision:** compress the confirmed summary into 3–5 sentences of durable
  intent; must not contradict PROGRESS.md's North Star (they should be the same claim
  at two altitudes).
- **B2 — Users:** the five locked archetypes (Nick-builder, portfolio-presenter,
  practitioner-friend, builder-friend, employer-evaluator) — per archetype: job-to-be-
  done and what evidence in the workspace represents them. Probe whether all five
  survive as PRD users or some are constitution-level audience only.
- **B3 — Goals / non-goals:** 3–6 observable outcome statements. Push for ≥2
  non-goals with one-line "why not" each (an empty non-goals list means scope isn't
  understood). Candidate non-goals to probe: multi-tenant design (backlog, Nick-gated),
  bulk video intake (closed as instrument), Household OS as peer.
- **B4 — Epics:** break the remaining program (Phase 5 both halves + kernel compiler +
  drift-check tooling) into epics — each with named inputs, outputs, ≥1 binary
  acceptance criterion, dependency line, and appetite. Carry the checkpoint-#1
  revisions in as named inputs: capability-as-composition-unit;
  harness-maintenance/fitness DoD; Archon rules-layer-collapse as counter-signal.
- **B5 — Risks & assumptions, open questions:** separate verifiable assumptions from
  mitigatable risks; park unresolved items with an owner and a "matters by when".

### Block C — actors.md

Pre-load: `agents/` definitions, plan §2 single-implicit-agent capture, agent.md
Constitution sections.

- **C1 — The pivotal question:** is the engine **one implicit agent** (the CareerBuddy
  model Nick named as exemplar: the kernel is the full description of the one agent,
  session state scoped to the system) or **four actors** (Owner/Researcher/Codifier/
  Librarian, DD-82/DD-86)? A middle option exists: one system-agent whose four
  dispositions are internal roles, not actors. Present all three with tradeoffs —
  this decides actors.md's entire shape.
- **C2 — Per-actor contract** (shape follows C1): task boundaries, permission sets,
  skills owned, disposition/soul. Drafting is mostly mechanical from `agents/` — elicit
  only deltas, do not re-interview settled contracts.
- **C3 — Nick's seat:** the human gate is an actor with a permission set too; the
  human/AI seam findings (wave-3 ruling) say the kernel should name what stays human.

### Block D — Ordering decision: generalize-first vs harness-first

Binary decision, options-with-tradeoffs, evidence pre-loaded:

- **Harness-first case:** capability-as-composition-unit has independent convergence
  (pydantic-ai 2.0 + Archon v0.5.0 tiered registry); the engine feels its own
  agent-remembers-to-invoke-skills fragility every session; Phase 5's maintenance/
  fitness DoD (Jones bidirectional-breakage evidence) is harness-side.
- **Generalize-first case:** the kernel docs Block A–C just produced ARE the
  generalized forms' spine; generalizing while the interview is fresh avoids a second
  elicitation pass; harness materializations are supposed to be *derived* from the
  kernel (plan §2), which argues kernel-before-harness.
- **Counter-signal to hold against both:** Archon's rules-layer-collapse — don't
  over-layer whichever goes first.

Outcome feeds Block E directly.

### Block E — Checkpoint #2: plan update + milestone mapping

- Update the program plan (§Phase 5 order, §6 open questions closed by Blocks 0/A/D).
- Propose the epic → milestone mapping for PROGRESS.md in hill vocabulary (milestone
  name, testable DoD, initial scopes) — Nick gates; `/session-handoff` and the normal
  PROGRESS flow own the write.
- Sweep the interview-adjacent blocker list: Phase 3 manual-as-kernel-layer (decide
  whether/when, or explicitly re-defer); design-mode video-intake spec (still wanted?).

## 4. Sitting plan and mechanics

- **Two sittings recommended:** Sitting 1 = Blocks 0 + A + B (constitution + PRD —
  the heavy elicitation); Sitting 2 = Blocks C + D + E (actors is mostly diff-work;
  D/E are decisions over pre-loaded evidence). One long sitting is viable if Nick
  prefers; Block boundaries are the checkpoint seams either way.
- **Import step precedes the first sitting:** `ops-vision-to-plan` import + engine
  adaptation (this note is the adaptation spec for its templates) + Rule-10
  `/assess-skill` pass, per the locked §4 verdict. Whether it lands as a reusable
  engine skill or a one-shot procedure is itself gated — Rule 11 says one interview
  is not yet recurrence; recommend importing to `.claude/skills/` anyway since the
  verdict is already locked and the kernel-compiler arc (Phase 5) will re-invoke it
  for produced systems.
- **Pre-load list (agent reads before Sitting 1):** program plan, direction note,
  CHARTER.md, FOUNDATIONS.md, Phase 1 delta report §insights, `agents/*/agent.md`,
  PROGRESS.md. Optional cheap `/watch-upstream` on BMAD + superpowers first (delta
  residual: registries ~3 months stale; Phase 5 consumes them, so this can also wait).
- **Stop rules carried from upstream:** two rejections of one section → re-elicit;
  elicited intent contradicting an approved artifact → escalate, don't resolve
  silently; no governance file written without in-turn approval; scope growing into
  implementation → hand off to Phase 5, don't drift.

## 5. Open questions on this structure (for Nick's gate)

1. Sitting count — two as recommended, or one?
2. Kernel doc naming/homes (§2 proposal) — accept, or decide at the sitting?
3. Should Block E also rule the gate-clearance queues if they're still open (PROMOTE
   flags, harvest rows, drift re-runs), or keep those in their own sitting as PROGRESS
   currently scopes them?
