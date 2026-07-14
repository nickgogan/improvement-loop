---
name: vision-to-plan
description: >-
  Turn a system steward's vision into approved kernel documents — constitution →
  PRD → actors, with epics mapped into PROGRESS.md milestones — through Socratic
  elicitation and section-by-section human approval. Use when asked to capture a
  system's vision or intent, write its constitution or PRD, define its actors,
  plan a system or subsystem, or turn direction into an executable roadmap —
  trigger phrases: "create a PRD", "capture the vision", "write the constitution",
  "define the actors", "plan this system", "turn direction into a roadmap".
  Distills the BMAD planning arc and chunked-design-approval discipline into the
  engine's governance-first kernel model; hands finished epics to /session-handoff's
  milestone/scope vocabulary. Do not use for end-of-session reconciliation (use
  /session-handoff), skill authoring (use /design-skill or /meta-skill-author), or
  research intake (use /research-loop).
license: MIT
compatibility: >-
  Requires an interactive per-section human-approval channel — the section gate is
  the method; do not install without one (unattended runs are out of scope). Works
  best with durable editable documents, the elicitation templates attached, and
  versioned checkpoints (git); each optional capability carries a named degradation
  in capability-contract.yaml.
metadata:
  distribution-scope: "internal"
  output: "governance/constitution.md (or a CHARTER amendment set), governance/prd.md, governance/actors.md, PROGRESS.md milestone proposals"
  version: "0.3.0-il.1"
  upstream: "nickgogan/CareerBuddy .github/skills/ops-vision-to-plan @ 0.3.0"
  imported: "2026-07-13 (session 147, restructure-program Phase 4)"
  exportable-canon: "ports/generic.md (harness-neutral; re-derive on SKILL.md change)"
allowed-tools: Read, Write, Edit
---

## Purpose (L0)

Extract a system steward's intent and encode it as durable **kernel documents** a
context-free agent can execute against. The engine's governance-first model puts the
constitution above the PRD, and the architecture layer's role is played by the kernel's
"how it works" + **actors** layers. Engine artifact chain: **confirmation summary →
constitution → PRD → actors → ordering decision → plan update**; every artifact is
approved by the human **section by section** before the next begins. This skill produces
vision-layer / kernel documents; execution tracking stays in PROGRESS.md/HISTORY.md,
owned by `/session-handoff` — this skill proposes milestones in that vocabulary and never
duplicates those conventions.

> **Engine deltas from upstream `ops-vision-to-plan`** (full list + provenance in
> [ADAPTATION.md](ADAPTATION.md)): artifact chain reordered to constitution-first; no
> standalone brief (opens with a pre-filled confirmation summary drafted from the
> corpus); architecture template replaced by an actors template; outputs land in
> `governance/` as kernel content. **Caution (Phase 1 delta report):** no external
> exemplar generates the layer above the PRD — the constitution-first arc is
> engine-original; where the method feels underspecified above the PRD, resolve by
> judgment at the gate, not by searching for a reference.

## When to use / when not

**Use** when a steward wants to start or re-plan a system/subsystem, capture vision so
agents need minimal guidance, produce the engine's own kernel docs, or refresh a stale
constitution/PRD/actors set after direction changes. Phase 5's kernel-compiler arc
re-invokes this skill to produce the same three kernel docs for downstream produced
systems.

**Do not use** for: end-of-session reconciliation (`/session-handoff`), authoring skills
(`/design-skill`, `/meta-skill-author`), or research intake (`/research-loop`). If the
request is a single small task with an obvious plan, skip this skill — plan inline.

## Goal

At completion the target system's `governance/` contains:

1. **constitution.md** (or a CHARTER amendment set — the Charter-relationship question is
   decided first, see the constitution template) — vision/mission/values/principles,
   reconciled with `CHARTER.md`.
2. **prd.md** — vision, users, goals/non-goals, epics with binary acceptance criteria,
   risks, open questions.
3. **actors.md** — the system's LLM actors (or single implicit agent): task boundaries,
   permission sets, dispositions, and the human's seat.

Plus **milestone proposals** for PROGRESS.md — each epic mapped to a milestone with a
testable definition-of-done and initial scopes, in `/session-handoff` hill vocabulary.

Success test (**cold-start test**): a fresh session, loading only PROGRESS.md plus these
kernel docs, can state the system's purpose and the next unit of work with zero guidance
from the human.

## Constraints

**Hard (halt-if-violated; the safety-critical gates):**

- **Human gates are mandatory.** Draft one section at a time; wait for explicit approval
  before the next. No kernel/governance file is written without in-turn human approval.
- **Governance writes are Proposal-first or Human-required** (see the HITL table) — never
  Full-autonomy. Conflicts with an approved DD or the charter are escalated, not resolved
  silently (DD-44 governs supersession).
- **Enforcement note:** the section gate is enforced at the **prompt layer** — there is no
  hook/interceptor backstop, and this workspace runs `bypassPermissions` (no permission
  prompts on `Write`/`Edit`). The residual risk of a skipped gate is **accepted** for this
  interactive-only skill; the standing mitigations are the workspace push-gate and Nick's
  presence (the skill is inert without an interactive approval channel — see
  `compatibility`). If this skill is ever run less-attended, add a structural backstop
  (confirm-tool-call / required echo-back) before doing so.

**Steering (quality; prompt-layer guidance):**

- **Elicit, don't dump.** Vision is extracted through questions, never invented. Ask one
  focused question set at a time. Prefer options with trade-offs over open-ended prompts
  when the steward seems undecided.
- **Evidence-grounded.** Claims about users, facts, or history must trace to CHARTER.md,
  FOUNDATIONS.md, PROGRESS.md/HISTORY.md, the DD/IB registry, or `agents/` — never to
  training-data assumptions.
- **Re-entry is the default posture.** The engine is not greenfield — CHARTER.md,
  FOUNDATIONS.md, `agents/`, and the direction note already exist. Diff the steward's
  current intent against them and propose amendments (section-scoped `Edit`s); record
  supersessions, never silently rewrite.
- **Context-free executability.** Every epic and milestone proposal must be actionable by
  an agent with no access to this conversation: name the inputs, the outputs, and a
  binary definition-of-done.
- **No volatile metrics.** No counts that go stale in any artifact — durable rules only
  (workspace Process Rule 3).
- **Pointers over copies.** Reference `/session-handoff`'s PROGRESS/HISTORY/commit
  conventions and existing governance; never restate them.

## Context

- Templates with embedded per-section elicitation instructions:
  `references/constitution-template.md`, `references/prd-template.md`,
  `references/actors-template.md`. Follow each section's embedded instruction, then
  delete the instruction comments from the final artifact.
- Authoritative inputs to load before elicitation: `CHARTER.md`,
  `governance/FOUNDATIONS.md`, PROGRESS.md, HISTORY.md, `agents/*/agent.md`, the active
  direction/plan note, relevant DDs.
- PM vocabulary (milestones, scopes, hill states, DoD): the engine `/session-handoff`
  skill.
- **Run-spec (when one exists):** a per-engagement design note may pre-structure the
  blocks and pre-load evidence (e.g. the Phase 4 interview structure at
  `project-management/design-notes/2026-07-13-phase4-interview-structure.md`). When a
  run-spec is provided, follow its block ordering and pre-load list; this SKILL is the
  reusable capability, the run-spec is the parameters for one invocation.

## Workflow

1. **Confirm.** Draft a pre-filled brief-equivalent summary from the corpus (problem,
   who, outcome, constraints, out-of-scope, bet size — already answered by the plan and
   CHARTER) and present it for correction. No standalone brief file; this honors the
   reduce-steward-bottleneck posture (AI drafts from what exists; the human corrects).
2. **Constitution.** Draft from `references/constitution-template.md`, one section at a
   time with approval between sections. Decide the Charter-relationship question first
   (own doc / amendment set / compiled-in) — it determines the doc's home and name.
3. **PRD.** Draft from `references/prd-template.md`, same chunked approval. Every epic
   gets ≥1 binary acceptance criterion and a named input set.
4. **Actors.** Draft from `references/actors-template.md`, same chunked approval. Decide
   the actor-model question first (one implicit agent / N actors / one agent with N
   dispositions) — it determines the doc's entire shape. The human's seat is an actor.
5. **Ordering + handoff.** Make the binary ordering decision the engagement was chartered
   to make (options with trade-offs, evidence pre-loaded). Then propose the epic →
   milestone mapping for PROGRESS.md (milestone name, DoD, initial scopes with hill
   status) → human gate. On approval, milestone entries and any plan update are written
   by the normal PROGRESS/plan editing flow; future reconciliation belongs to
   `/session-handoff`.

Re-entry: when kernel docs already exist, diff the steward's new intent against the
current constitution/PRD/actors, propose amendments section by section (section-scoped
`Edit`s), and record superseded decisions rather than silently rewriting them.

**Progress tracking (resume across sittings).** A full engagement is multi-section and
often multi-sitting. Track approved sections durably, independent of conversation
history: as each section lands, write it to its `governance/` file (an approved section
in the file *is* the checkpoint) and mark it in the run-spec design note's block list.
On resume, the completed artifact files plus the run-spec tell a fresh session exactly
which sections are approved and where to continue — do not re-elicit settled sections.

## Stop Rules

The `§Acceptance criteria` list below is this skill's **completion criterion** — the
engagement is done when every item there is satisfied. Before then, **halt and ask** the
human when any of these occur:

- The same artifact section is rejected twice.
- Elicited intent contradicts CHARTER.md, an approved DD, or an existing approved kernel
  doc.
- An epic cannot be given a binary acceptance criterion or a milestone DoD.
- The engagement would write to any governance file without an explicit approval given in
  the current turn.
- The scope grows beyond kernel/planning artifacts into implementation — hand off to the
  next program phase instead of drifting.

## Reversibility & HITL tiers

| Action | Reversibility | Tier |
|--------|---------------|------|
| Elicitation questions, drafts shown in chat | Fully reversible | Full autonomy |
| Drafting the confirmation summary from the corpus | Fully reversible | Full autonomy |
| Creating/editing constitution.md, prd.md, actors.md | Reversible (git) but governance | Proposal-first (approve each section) |
| PROGRESS.md milestone entries, plan update | Reversible (git) | Proposal-first |
| Superseding an approved kernel doc or DD | Reversible with effort | Human-required (DD-44) |
| Pushing or sharing artifacts externally | Practically irreversible | Human-required (workspace push-gate) |

## Acceptance criteria (per engagement, binary)

- constitution.md (or approved CHARTER amendment set), prd.md, and actors.md exist, every
  section human-approved.
- Each epic has ≥1 binary acceptance criterion; each proposed milestone has a testable
  DoD.
- The ordering decision the engagement was chartered to make is recorded with rationale.
- No template instruction comments remain in final artifacts.
- No volatile metrics in any artifact.
- Cold-start test passes.
