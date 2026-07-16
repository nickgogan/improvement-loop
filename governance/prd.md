---
title: "Engine PRD"
id: "engine-prd"
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
  - "prd"
  - "phase4"
---

# PRD: Improvement Loop (the engine)

> **Kernel document.** Every section approved by Nick section-by-section in the
> Phase 4 interview (2026-07-16). Covers the remaining restructure program: memory +
> task layers, self-description, harness + generalize — order of the harness/compiler
> pair ruled at plan checkpoint #2. Changes to approved sections only by explicit
> supersession (constitution §Principles 2).

Updated: 2026-07-16 · Approved by: Nick

## Vision

**Status: APPROVED (2026-07-16, interview Block B1).**

The engine formalizes into an **agentic OS**: a harnessed, self-describing,
single-operator system whose `governance/` is its portable kernel. The kernel fully
describes the system — constitution, PRD, actors, and eventually one YAML per agent
and one per harness under a root harness descriptor — so that anyone can read
`governance/` to know what the system is, and any downstream consumer can pull it and
compile harness materializations for their own target. Research stays the substrate:
the knowledge base grounds every design move, and the engine's audits return both a
KB-grounded efficacy description and a portable remediation prompt the asker runs in
their own system. This PRD scopes the remaining restructure program: kernel documents
(this interview), then harness and generalization in the order ruled at checkpoint #2.

## Users

**Status: APPROVED (2026-07-16, interview Block B2). Three archetypes act as PRD
users; presenter/evaluator are constitution-level audience.**

| User | Job-to-be-done | Workspace evidence |
|------|----------------|--------------------|
| **Nick-the-builder** (steward/operator) | Build real agentic systems faster and better; steward the engine's evolution; gate content | The whole workspace; CareerBuddy + Household OS as produced/consulted systems; every gate ruling in HISTORY |
| **The asker** (practitioner-friend, builder-friend) | Submit an agent/skill/system for audit; receive an efficacy description + a portable remediation prompt to paste into their own harness | `/assess-*` skills invocable as subagents; the audit-deliverable vision (constitution §Mission); consumer-abstractions-map demand rows |
| **The downstream kernel consumer** | Pull the kernel (or a produced system's kernel) and instantiate it on their own harness | Kernel litmus (constitution §Principles 5); `il-published` subtree; `/vision-to-plan` as the kernel compiler's front end |

**Audience, not users:** the portfolio-presenter and employer-evaluator archetypes
evaluate the engine's outputs but never invoke it — they stay at constitution level
(§Purpose) and impose a quality bar (legible artifacts, honest reporting), not
requirements of their own.

## Goals

**Status: APPROVED (2026-07-16, interview Block B3).**

1. **The engine is self-describing.** `governance/` fully describes the system —
   constitution, PRD, actors, and one YAML per agent + per harness under a root
   harness descriptor. *Test:* a reader with no conversation context reconstructs the
   agent set, their tools/resources/access, and the system's purpose from
   `governance/` alone (the cold-start test, extended to strangers).
2. **The engine is harnessed.** Skill invocation, gates, and session discipline are
   enforced by a formal harness layer, not by the agent remembering. *Test:* a named
   harness surface exists (hooks/checks/config) and the engine's own sessions run on
   it; removing it observably breaks enforcement.
3. **The kernel is compilable.** Harness materializations (`.claude/` today; other
   targets later) are derived from kernel sources by a compile step, with
   generalized↔installed drift detection. *Test:* the compiler produces a working
   materialization from `governance/` and a `--check` run flags a seeded drift.
4. **Audits ship remedies.** An audit of a submitted artifact returns the efficacy
   description plus, for each flagged gap, a portable remediation prompt runnable in
   the asker's harness. *Test:* an `/assess-*` run on an external artifact emits both
   deliverables.
5. **The harness has a fitness loop.** Harness health is reviewed on a recurring
   cadence (bidirectional-breakage evidence: world drift AND model improvement).
   *Test:* the fitness review is a scheduled, documented operation that has run at
   least once and produced at least one accepted adjustment or an explicit
   no-change verdict.
6. **Knowledge and action close the loop.** *(Added by amendment 2026-07-16, approved
   at the Block B4 gate.)* The system's accumulated operational data (session
   runs, tool calls, session logs) is reflected into knowledge, and knowledge routes
   into tasks — per agent and for the system as a whole. *Test:* a captured
   operational signal traceably becomes a knowledge entry and then a scheduled task
   with no human transcription step.

## Non-goals

**Status: APPROVED (2026-07-16, interview Block B3).**

- **Multi-operator / multi-tenant kernels.** Single-operator is the ruled scope
  (constitution §Vision); no external exemplar exists and no concrete demand row
  names it. Stays a research-gap candidate, Nick-gated.
- **Bulk video intake as research strategy.** Closed as an instrument after two
  consecutive zero-ADD/ENHANCE triage runs; `/link-intake` handles future batches as
  routine ops. Research spend goes to targeted queries and primary sources.
- **Household OS as a peer system.** It is a consumer the engine helps design
  (DD-106), not a second live system to govern.
- **Building an orchestration platform.** Orchestration is a subsystem/compile target
  of an agentic OS (Databricks comparison, direction note) — the engine compiles
  *onto* such substrates; it does not compete with them.

## Epics

**Status: APPROVED (2026-07-16, interview Block B4 — v2, after Nick's elicitation
added the memory and task-management epics upstream). E4 ↔ E5 execution order is the
Block D decision; dependency lines permit either order. Checkpoint-#1 revisions
carried as named inputs (capability-as-composition-unit; fitness DoD; Archon
rules-layer-collapse as counter-signal against over-layering).**

**Ordering decision (plan checkpoint #2, ruled 2026-07-16, interview Block D):
harness-first — E4 before E5.** Rationale: the ruled orchestration end-state
(per-actor queues, signal-driven wake-up, Owner as acting owner — `actors.md`
§Orchestration) is harness machinery and cannot run without E4; E3's descriptors keep
the generalization thread active in the interim; E5 then compiles against a harness
that exists, and its drift `--check` has a real materialization to verify.
Counter-signal held: do not over-layer (Archon's rules-layer collapse).

### E1 — Memory & knowledge layer (per-agent + system)

- **Outcome:** a designed and built memory architecture for the engine: how the
  system accumulates operational data (session runs, tool calls, session logs), how
  reflection turns that data into knowledge (wiki/knowledge-base shape, per the KB's
  own convergence), and what each agent's memory surfaces are — what it reads, writes,
  and retains across sessions. Extends the shipped `/self-improve` loop (IB-176) from
  one system-level store to a designed layer.
- **Inputs:** `operations/self/` (shipped lesson store, demand ledger, calibration
  registry); the frozen System Log corpus (read-only feedstock, IB-172); KB memory
  cluster: `rebuilt-hermes-memory-in-claude-code`,
  `memory-system-evaluation-triad-storage-injection-recall`,
  `memory-recall-ladder-staged-deepening-with-citation-and-abstention`,
  `session-history-import-as-memory-bootstrap`,
  `append-only-lesson-store-owning-surface-identity`; `governance/actors.md`.
- **Acceptance criteria (binary):** a memory-architecture spec is approved (spec
  before build); every actor in actors.md has its memory surfaces named; a reflection
  mechanism over at least one accumulation surface (e.g. session logs) runs and routes
  its outputs by shape (decision → DD, pattern → knowledge/, work → task layer); a
  deterministic store check exists and a seeded violation fails it.
- **Depends on:** actors.md approved (this interview).
- **Appetite:** large — Nick flagged this as potentially the big one.

### E2 — Task management layer (per-agent + system)

- **Outcome:** a designed task-management system for each agent and for the system as
  a whole — the action half of the knowledge↔action loop, and the layer a multi-agent
  system needs to function at all. Includes a ruled work-item contract (what a
  well-formed task carries) and absorbs the DD + IB corpus cleanup: per-item verdicts
  (keep / distill / archive / migrate) and migration of live work into the new layer.
- **Inputs:** the assembled task-queue study feedstock (named-deps gap-check §6):
  `work-ticket-contract-prompt-mode-vs-work-mode` (Jones five-element assignment
  contract), Archon loop-node-as-queue-iteration + typed output sidecars, BMAD
  epics→stories sharding, superpowers/GSD state-file queues; the live IB corpus;
  IB-173 (gate tiering, approved direction); E1's routing design.
- **Acceptance criteria (binary):** a task-contract schema is ruled; the DD/IB
  cleanup verdicts are recorded and executed (every live IB item either migrated,
  archived, or explicitly kept); one signal completes the full round trip —
  operational data → reflection → knowledge → scheduled task → execution — with each
  hop file-traceable.
- **Depends on:** E1 (knowledge routing feeds the task layer).
- **Appetite:** large.

### E3 — YAML self-description set (descriptor schema + instances)

- **Outcome:** a ruled schema for agent and harness descriptors, plus the instances:
  one YAML per agent and one per harness under a root harness descriptor in
  `governance/` — each agent's purpose, callable tools, resources held, access rights,
  execution access, and memory system stated machine-readably.
- **Inputs:** `governance/actors.md` (Sitting 2 output); `agents/*/agent.md`; E1's
  memory-surface design (fills the descriptor's memory fields); constitution §Vision;
  KB: `machine-readable-system-contract-with-wiring-rows`,
  `hub-and-spoke-two-tier-skill-taxonomy`, wiring-canon findings.
- **Acceptance criteria (binary):** every actor named in actors.md has a descriptor
  that validates against the schema; a deterministic check exists and a seeded schema
  violation fails it; a reader given only the YAML set can list each agent's tools and
  access (spot-check against actors.md).
- **Depends on:** actors.md approved; E1 memory design (for the memory fields —
  schema work may start earlier with that field stubbed).
- **Appetite:** medium.

### E4 — Harness the engine

- **Outcome:** a formal harness layer on the first target runtime (Claude Code) —
  gates, skill routing, and session discipline enforced by named surfaces (hooks,
  checks, config), not by agent recall. The engine's own sessions run on it.
- **Inputs:** KB: `capability-as-agent-composition-primitive` (pydantic-ai 2.0),
  Archon v0.5.0 tiered capability registry + Ralph-loop anatomy,
  `lean-core-vs-harness-two-lane-framework-layering`, six-pattern harness-composition
  taxonomy; counter-signal: Archon's rules-layer collapse (don't over-layer); existing
  pre-commit hooks as the seed surface.
- **Acceptance criteria (binary):** the harness's enforcement points are enumerated in
  the harness descriptor (E1 root YAML); a deliberately induced gate violation is
  blocked with the harness on and passes with it off (negative test); no skill the
  kernel declares mandatory depends on unprompted agent memory to fire.
- **Depends on:** none hard; E3 root descriptor is its documentation home (can land
  in either order per Block D).
- **Appetite:** large.

### E5 — Kernel compiler v1 (generalize)

- **Outcome:** generalized forms of the engine's assets (skills, agents, rules, hooks)
  with adaptation commentary live in `governance/`; a compile step derives the
  installed materializations (`.claude/` first); generalized↔installed drift detection
  runs deterministically. *Checkpoint-#2 addendum (2026-07-16, Block E ruling):* also
  the kernel's **human-readable manual layer** — Phase 3's standalone user manual was
  folded in here; the manual is a rendering of the kernel, not a separate doc.
- **Inputs:** KB: `wiring-canon-abstract-then-adapt-doc-structure`,
  `two-tree-model-authoring-vs-canonical-generated-pack`,
  `manifest-hash-drift-detection-for-derived-docs`,
  `superset-spec-for-cross-platform-skill-authoring`,
  `receiver-relative-tier-semantics`; meta-harness-author pattern
  (generalize→adapt→install→verify); `/vision-to-plan` + `/meta-skill-author` as
  existing front-end tooling.
- **Acceptance criteria (binary):** the compiler regenerates working materializations
  for every asset the kernel declares portable; a hand-edit to a derived file is
  flagged by `--check`; a second target's adaptation commentary exists for at least
  one asset class (proves the generalized form isn't Claude-Code-shaped).
- **Depends on:** kernel docs (this interview); E3 schema for the descriptor layer.
- **Appetite:** large.

### E6 — Audits ship remedies

- **Outcome:** every `/assess-*` audit returns the two-part deliverable: efficacy
  description (artifact vs its own design + KB best practice) and, per flagged gap, a
  portable remediation prompt runnable in the asker's harness.
- **Inputs:** `/assess-skill`, `/assess-agent`, `/assess-prompt` contracts; Librarian
  reference layer (`audit.md`); KB:
  `human-ai-seam-identification-three-question-rubric`,
  `self-improvement-dispatch-table-route-never-reimplement`; the session-log
  reflection example (constitution §Mission).
- **Acceptance criteria (binary):** an assess run on an external sample artifact emits
  both deliverables; each remediation prompt is self-contained — it names no
  IL-internal paths and states its own success check; one prompt validated end-to-end
  in a non-engine harness.
- **Depends on:** none (can run before or alongside E4/E5).
- **Appetite:** medium.

### E7 — Harness fitness loop

- **Outcome:** a recurring, documented harness fitness review — checking for world
  drift and model-improvement over-restriction — carried by the existing
  model-capability registry refresh + `/system-health`.
- **Inputs:** KB: `bidirectional-agent-breakage-world-drift-model-improvement`,
  `tool-pruning-as-harness-maintenance`, `five-point-agent-health-checklist`,
  `harness-depth-as-maintenance-ownership`; the calibration registry (IB-176).
- **Acceptance criteria (binary):** cadence and checklist documented in the harness
  descriptor; first review executed with a recorded outcome (accepted adjustment or
  explicit no-change verdict).
- **Depends on:** E4.
- **Appetite:** small.

## Risks & assumptions

**Status: APPROVED (2026-07-16, interview Block B5).**

**Assumptions (verifiable):**

- The KB's memory, harness, and wiring clusters are sufficient grounding to design
  E1–E5 without another bulk research phase. *Verify:* each epic's spec cites its
  findings; a gap triggers targeted `/research-query`, not a new intake wave.
- Claude Code's harness surfaces (hooks, skills, settings, pre-commit) expose enough
  enforcement points for E4. *Verify:* early E4 spike enumerates them against the
  gate list.
- The actor model ruled in actors.md (Sitting 2) stays stable through the program —
  E1 and E3 build on it. *Verify:* any actor change reopens those epics' specs
  explicitly.

**Risks (mitigatable):**

- **Over-layering.** Seven infrastructure epics invite kernel bloat; Archon deleted
  its own rules layer after building it. *Mitigation:* Rule-11 evidence at every epic
  spec gate; constitution Principle 8 (positive-space governance); the Archon
  counter-signal named in E4/E5 inputs.
- **Memory-layer scope explosion.** Nick flagged E1 as potentially the big one.
  *Mitigation:* spec-before-build is in E1's acceptance criteria; start-lean value;
  stage the design as gated design notes before any build.
- **Premature schema lock-in.** Ruling the E3 YAML schema before enough real
  instances exist. *Mitigation:* schema derives from actors.md + the four live
  agents; version the schema; deterministic check makes migration mechanical.
- **Kernel↔reality drift during a long program.** *Mitigation:* amendments-only
  discipline on approved docs; E5's `--check`; `/system-health` between epics.
- **Human-gate bottleneck.** Seven epics × per-section gates could stall on Nick.
  *Mitigation:* door-type delegation (execute two-way doors, surface one-way);
  scoped delegated-judgment grants with rulings listed for review.

## Open questions

**Status: APPROVED (2026-07-16, interview Block B5).**

| Question | Who decides | Matters by |
|----------|-------------|------------|
| ~~E4 ↔ E5 order~~ — **resolved: harness-first** (Block D, 2026-07-16; rationale in §Epics) | — | closed |
| ~~Actor model~~ — **resolved: four actors, full stop** (Block C1, 2026-07-16; see actors.md) | — | closed |
| Engine rename (Nick: "we'll probably change the main name later") | Nick | Before E5 publishes the kernel — the name lands in every descriptor |
| Phase 3 user manual: whether/when; manual-as-kernel-layer | Nick | Block E sweep, or explicit re-deferral |
| Design-mode video-intake spec still wanted? | Nick | Block E sweep |
| E3 descriptor schema form (fields, validation tooling) | Deferred by design | Inside E3 — not before |
