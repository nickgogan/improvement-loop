---
title: "A3 — Per-Actor Memory-Surface Requirements"
type: "resource"
target_system:
  - "improvement-loop"
category: "plan-input"
stage: "draft"
created: "2026-07-16"
author: "claude"
tags:
  - "memory"
  - "E1"
  - "actors"
  - "spec-input"
---

# A3 — Per-Actor Memory-Surface Requirements

> **Input to the E1 memory-architecture spec.** Feeds the E1 acceptance criterion
> *"every actor in actors.md has its memory surfaces named."* Derived from
> `governance/actors.md`, `governance/prd.md` §E1, the four `agents/*/agent.md`
> constitutions, and `agents/handoff-protocol.md`. **Scope discipline:** this doc
> supplies per-actor evidence for the spec's open unknown (*per-actor vs shared store
> shape*). It does **not** resolve that unknown, and it does not invent memory types
> beyond the standard episodic / semantic / procedural triad the E1 criteria imply.

## Method and shared framing

Three recall needs, applied only where an actor's duties require them:

- **Episodic** — *what happened*: which work items this actor has already processed,
  where it left off, what it dispatched or returned across separate wake-ups.
- **Semantic** — *what it learned*: durable calibration (rubric edge cases, dedup
  judgments, drift patterns, recurring gaps) that should shape future decisions.
- **Procedural** — *how it works*: the actor's own operating procedure.

**Procedural is largely a non-need at the memory layer.** Each actor's procedure lives
statically in `agents/<actor>/agent.md` plus its `SKILL.md` set, loaded by the harness
(E4), not recalled from session memory. Where procedure *adapts from experience*, that
adaptation is semantic calibration, not a distinct procedural store. So the procedural
column below is marked "covered by agent.md/skills" unless a genuine gap exists.

**The end-state that creates the gaps** (`actors.md` §Orchestration): every actor —
Owner included — runs off a **work queue**, woken **periodically and signal-driven**,
with the **human out of the loop by default**. Today's model is the degenerate case:
Nick hands each actor a bounded, framed task and every actor boots by re-reading a
fixed pointer (`PROGRESS.md`, "the last delta report"). Remove the human scheduler and
each actor must recall, from durable state alone, what it has done and what it learned.

---

## Owner

### Today

- **Reads:** `../../CHARTER.md`, `CLAUDE.md`, `PROGRESS.md`, `feedback/`,
  `agents/*/agent.md`, `.claude/skills/*/SKILL.md`, `governance/`, `knowledge/`,
  the frozen `operations/system-log/` corpus, and (as `/self-improve` owner) the whole
  `operations/self/` store.
- **Writes:** `governance/` (incl. `governance/proposals/`), `knowledge/` docs, DD/IB
  registries, `operations/` — including the `operations/self/` lesson store,
  `proposal-log.md`, and retro output — and `agents/owner/reflections/` (append-only,
  agent-private).
- **Retains across sessions:** **explicitly stateless** — the constitution states "The
  Owner is stateless across sessions. It re-reads system state each time… Memory is not
  truth." Durable state is the filesystem: `governance/` files, git, the
  `operations/self/` store, `MEMORY.md` (Nick's working-style memory), and
  `reflections/`.

### Gaps at the orchestration end-state

The Owner's role changes the most: it becomes the **acting owner/orchestrator** that
wakes the other actors. That is a net-new duty with net-new memory needs.

- **Episodic (gap):** no orchestration state. To dispatch off queues across wake
  cycles, the Owner must recall *which actors it woke, what it dispatched, what came
  back, and what is still outstanding*. Today Nick is that memory (he schedules and
  frames each session); statelessness + re-derive-from-files does not reconstruct
  in-flight dispatch state. There is no dispatch/wake ledger.
- **Semantic (partially covered):** cross-actor operational lessons already land in
  `operations/self/lessons.md` (shipped). The remaining gap is the Owner's own
  **delegated-judgment authority state** — which gates Nick has delegated so the Owner
  can act without him (`actors.md` §The human seat: "Gates migrate to the Owner under
  recorded delegated-judgment grants"). Today grants are ad hoc and conversational
  (e.g. proposal-log P-1's "trusting your judgement"); off-human they must be a durable,
  queryable ledger the Owner reads before acting on a gate.
- **Procedural:** covered by `owner/agent.md` + Owner skills.

### Candidate memory surfaces

- **Owner dispatch/wake ledger** *(per-actor · gap)* — the Owner's episodic record of
  orchestration actions. Per-actor because only the Owner orchestrates; no other actor
  dispatches. *Overlap flag:* may be the Owner-side view of E2's queue machinery rather
  than a separate store — **unclear, spec question.**
- **Delegated-grant ledger** *(shared-leaning · gap)* — recorded gate delegations.
  Owner-*written* but system-*read* (any actor acting on a gate needs to know its tier),
  so plausibly a shared governance surface, not Owner-private. **Spec question: home and
  reader set.**
- `operations/self/lessons.md`, `query-log.md`, `proposal-log.md` *(shared · shipped)* —
  the Owner already reads/writes these as `/self-improve` owner; see §System-wide.

---

## Researcher

### Today

- **Reads:** `PROGRESS.md`, the last delta report in `operations/research-reports/`,
  existing KB state (`research-findings/`, `research-sources/`, `research-authorities/`)
  for deduplication, and `watched-libraries/` / `watched-blogs/` entries.
- **Writes:** `research-findings/` (sets `pipeline_status: raw`), `research-sources/`,
  `research-authorities/`, `watched-*`, delta reports in `operations/research-reports/`,
  and `agents/researcher/reflections/`.
- **Retains across sessions:** "the delta report IS the session record." Cross-session
  persistence is deliberately routed into **structured records** — IB items, findings,
  or corrections to a `watched-library`/`authority` file — plus `MEMORY.md` for Nick's
  working style. Explicitly "**no free-form carry-forward file.**"

### Gaps at the orchestration end-state

- **Episodic (gap):** no durable *intake cursor*. Recovery today — "next session
  resumes from unprocessed sources" — depends on a human-initiated session reading the
  last delta report. Woken off a queue with no human framing, the Researcher needs to
  recall *which sources / queue items it has already consumed* to avoid re-processing.
  The delta report is a per-session snapshot, not a resumable cursor over the intake
  backlog.
- **Semantic (largely covered):** the KB is itself the Researcher's semantic store —
  findings are canonical and deduplicated ("one canonical entry per pattern"), and
  authority-credibility judgments live in `research-authorities/`. This is a genuine
  strength: dedup/coverage memory is already durable and queryable via grep. Residual
  gap: *source-triage verdicts* (extract/skip/defer) are not persisted, so a
  signal-woken session could re-triage an already-rejected source.
- **Procedural:** covered by `researcher/agent.md` + intake/maintenance skills.

### Candidate memory surfaces

- **Intake cursor / processed-source ledger** *(per-actor · gap)* — episodic record of
  consumed sources and triage verdicts. Per-actor because it indexes the Researcher's
  own intake backlog; no other actor consumes sources. *Overlap flag:* the E2 queue's
  terminal-item records may subsume this — **spec question.**
- **KB (findings + authorities)** *(per-actor by ownership · shipped)* — already the
  Researcher's semantic store; named here so the spec records that this need is met and
  need not build a second store.
- `agents/researcher/reflections/` *(per-actor · shipped, underused)* — see cross-actor
  note in §System-wide on promoting `reflections/` from a `/solicit-proposals`-only
  buffer to a live semantic-calibration surface.

---

## Codifier

### Today

- **Reads:** `operations/references/guide-routing-table.md`, the last identification
  report, `PROGRESS.md`, `research-findings/` (filtered by `priority` /
  `pipeline_status`), `operations/references/form-classification-rubric.md`, approved
  identification reports, and existing `extracts/`.
- **Writes:** `extracts/`, `operations/` (identification reports, guide reports),
  `project-management/design-notes/`, `agents/codifier/reflections/`, and **metadata
  only** on findings (`pipeline_status`, `consumed_by` — never content).
- **Retains across sessions:** "identification reports and guide reports in
  `operations/` are the session records." Classification edge cases and rubric
  calibration notes are routed to `operations/references/` **or `MEMORY.md`**. The
  Codifier also maintains the guide routing table as canonical finding→guide state.

### Gaps at the orchestration end-state

- **Episodic (largely covered):** `pipeline_status` + `consumed_by` on each finding is
  an embedded, durable episodic trace — "have I classified/consumed this finding?" is
  answerable from the data itself. This is another existing strength. Residual gap:
  batch-level state (which *identification report* is mid-extraction) relies on a human
  knowing which report is "approved and pending."
- **Semantic (gap — mis-routed):** the Codifier's most acute need. Rubric calibration
  and prior edge-case rulings are what keep classification *consistent* across
  independently-woken batches — but the constitution routes them to `MEMORY.md`, which
  is **Nick's cross-conversation memory, not an actor store**. There is no durable,
  Codifier-owned calibration surface; consistency currently depends on Nick carrying
  context between sessions.
- **Procedural:** covered by `codifier/agent.md` + the Form Router rubric.

### Candidate memory surfaces

- **Rubric-calibration store** *(per-actor · gap)* — durable record of classification
  edge-case rulings. **Necessarily per-actor:** Form Router calibration is duty-specific
  and meaningless to the other three actors. Closing this gap = giving the Codifier a
  real home for what today mis-routes to `MEMORY.md`; `agents/codifier/reflections/` is
  the natural host if promoted to a live surface.
- **Findings `pipeline_status`/`consumed_by`** *(shared substrate · shipped)* — already
  the Codifier's episodic trace; named so the spec records the need as met.
- **Guide routing table** *(per-actor by ownership · shipped)* — canonical synthesis
  state the Codifier already self-maintains.

---

## Librarian

### Today

- **Reads:** `research-findings/`, `extracts/guides/`, `extracts/{form}/`, deployed
  `knowledge/`, `operations/references/guide-routing-table.md`, and
  `operations/references/research-dimensions.md`.
- **Writes:** **none**, except `agents/librarian/reflections/` (agent-private). "The
  Librarian produces answers, not artifacts."
- **Retains across sessions:** **explicitly stateless** — "it re-reads the KB each time.
  No persistent Librarian-specific state."

### Gaps at the orchestration end-state

- **Episodic / demand (gap):** the Librarian "reports gaps, never fixes them" — but
  today gap reports **evaporate into conversation to Nick**, who then routes them to the
  Researcher or Codifier. With the human out of the loop, a surfaced gap must land in a
  **durable signal** so recurring gaps can *wake* a producer actor. A stateless,
  write-nothing Librarian cannot emit that signal. This is the Librarian's single
  biggest gap: it has no durable output surface for the demand/gap signals its role
  exists to produce.
- **Semantic (minor):** recurring-gap *patterns* (topics repeatedly asked about with
  thin KB coverage) would sharpen research prioritization, but this is subsumed by the
  demand signal above rather than a separate store.
- **Procedural:** covered by `librarian/agent.md` + assess/design/query skills.

### Candidate memory surfaces

- **Gap/demand signal** *(shared · partially shipped)* — the Librarian's gap reports and
  query outcomes should **route into `operations/self/query-log.md`** (the demand
  ledger), whose `served / partial / unserved` outcomes are exactly this signal and
  which is already named "the ground-truth routing corpus for the future implicit-routing
  harness." **Plausibly shared, not per-actor:** the demand ledger is a system surface;
  the Librarian is one writer into it. *Spec question: does the Librarian write the
  ledger directly, or does the harness capture its query outcomes?*
- `agents/librarian/reflections/` *(per-actor · shipped, underused)* — for gap
  *patterns* if a per-actor semantic surface proves warranted.

---

## System-wide seat

What the **system as a whole** — no single actor — must retain, per E1's "per-agent +
system" framing and Goal 6 (knowledge↔action loop).

**Already covered by the shipped `operations/self/` store (IB-176):**

- **`lessons.md`** — append-only, cross-actor **semantic** lesson store; identity =
  (owning surface, failure pattern); promotion pipeline routes lessons by shape
  (decision→DD, pattern→`knowledge/`, work→IB). This already satisfies much of the E1
  criterion "reflection routes its outputs by shape."
- **`query-log.md`** — the **demand ledger**: one row per incoming intent with
  served/partial/unserved outcome; the routing corpus and the Librarian's gap-signal
  home.
- **`proposal-log.md`** — append-only **promotion audit** (procedural/audit trail).
- **`retro-latest.md`** — the scan-mode **reflection output** over the capture buffer.
- **`.query-capture.jsonl`** — raw prompt-capture buffer (gitignored) feeding the ledger.

**Genuine system-level gap:**

- **Operational-run accumulation surface** *(shared · gap)* — E1's outcome explicitly
  names "session runs, tool calls, session logs" as the substrate reflection turns into
  knowledge. Today only the prompt buffer (`.query-capture.jsonl`) is captured; there is
  **no accumulation surface for session-run records or tool-call traces**. This is the
  raw feedstock the reflection mechanism (E1 acceptance criterion) is supposed to run
  over, and it does not yet exist. **Spec must design it.**

**Cross-actor observation feeding the open unknown:** the shipped evidence already
*bifurcates* the memory need. System-cutting failure-lessons want the **shared** home
(`lessons.md`, keyed by owning surface). Duty-specific calibration (Codifier's rubric,
Researcher's dedup, Owner's drift patterns) wants a **per-actor** home
(`reflections/`, currently a `/solicit-proposals`-only buffer, and today mis-routed to
`MEMORY.md`). This is per-actor evidence *for* the spec's unknown, not a resolution of
it: some memory is provably duty-scoped, some provably system-scoped, and the shape
question is where the boundary sits — **left to the spec.**

---

## Consolidated requirements table

Status: **shipped** = exists today · **underused** = exists but not wired for this need ·
**gap** = must be designed/built by E1.

| Actor | Candidate surface | Per-actor / Shared | Status | Grounded in which duty |
|-------|-------------------|--------------------|--------|------------------------|
| Owner | Dispatch/wake ledger (episodic) | Per-actor | Gap | Acting orchestrator wakes actors off queues (`actors.md` §Orchestration) |
| Owner | Delegated-grant ledger | Shared-leaning | Gap | Gates migrate to Owner under recorded grants (§The human seat) |
| Owner | `operations/self/*` (lessons, query-log, proposal-log, retro) | Shared | Shipped | Owner is `/self-improve` owner (DD-86, IB-176) |
| Owner | `agents/owner/reflections/` | Per-actor | Shipped (underused) | Agent-private self-reflection → `/solicit-proposals` |
| Researcher | Intake cursor / processed-source ledger (episodic) | Per-actor | Gap | Resume intake without human framing; avoid re-processing (recovery clause) |
| Researcher | KB — findings + authorities (semantic) | Per-actor (by ownership) | Shipped | Dedup/coverage/credibility memory; "one canonical entry per pattern" |
| Researcher | `agents/researcher/reflections/` | Per-actor | Shipped (underused) | Triage/dedup calibration |
| Codifier | Rubric-calibration store (semantic) | **Necessarily per-actor** | Gap (mis-routed to `MEMORY.md`) | Consistent Form Router classification across woken batches |
| Codifier | Findings `pipeline_status` / `consumed_by` (episodic) | Shared substrate | Shipped | "Have I classified/consumed this finding?" embedded in data |
| Codifier | Guide routing table | Per-actor (by ownership) | Shipped | Canonical finding→guide synthesis state |
| Librarian | Gap/demand signal → `query-log.md` (episodic/demand) | Shared | Partially shipped | "Reports gaps, never fixes" must become a durable wake signal |
| Librarian | `agents/librarian/reflections/` | Per-actor | Shipped (underused) | Recurring-gap patterns |
| System | `operations/self/lessons.md` (semantic) | Shared | Shipped | Cross-actor lessons routed by shape (Goal 6) |
| System | `operations/self/query-log.md` (demand) | Shared | Shipped | Demand ledger / routing corpus |
| System | Operational-run accumulation (session runs, tool calls, logs) | Shared | **Gap** | E1 outcome — feedstock reflection turns into knowledge |

**Distinct surface *types* by scope:** necessarily/plausibly per-actor — dispatch ledger,
intake cursor, rubric-calibration store, plus the four `reflections/` (2 net-new gap
types + the reflections pattern). Plausibly/actually shared — `lessons.md`, `query-log.md`
demand ledger, `proposal-log.md`, operational-run accumulation, delegated-grant ledger
(5 types; 4 shipped, 1 gap). Boundary placement is the spec's to decide.
</content>
</invoke>
