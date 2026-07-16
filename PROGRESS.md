# Improvement Loop — Progress

Updated: 2026-07-16 (session 148 — Phase 4 interview COMPLETE in one sitting: kernel
docs `governance/{constitution,prd,actors}.md` all Nick-approved; harness-first ruled
at checkpoint #2; Phase 3 folded into the kernel compiler. Next: E1 `memory-spec`.)

## Start here

New session? This file is the only cold-start artifact — read it top to bottom, then act.
"PROGRESS" / "continue" from Nick = proceed with the **next unit of work** under Current
milestone, no recital. The engine's **kernel docs** are `governance/constitution.md`
(vision/values/principles/gates), `governance/prd.md` (users, goals, epics E1–E7 — the
roadmap's source), and `governance/actors.md` (four actors, orchestration end-state,
human seat). Orientation lives in `CLAUDE.md` (engine) and `../../CHARTER.md`; the
foundational-DD spine is `governance/FOUNDATIONS.md`. Shipped work lives in
[HISTORY.md](HISTORY.md) (newest-first, commit ranges); git carries the atomic log
(Conventional Commits). Session close = `/session-handoff` (reconcile-in-place; never a
dated handoff file). Every line here must pass route-then-compact: history → HISTORY.md,
decisions → DDs, work items → IB, research → KB. Operational lessons + demand rows live
in `operations/self/` (`/self-improve`; capture hook + store checker are harness-wired).

## North Star

Formalize the engine into an **agentic OS**: a harnessed, self-describing,
**single-operator** system (any harness; Claude Code first) whose `governance/` is a
**portable kernel** — the export unit any downstream system pulls, with harness
materializations compiled per target. End state: the Owner acts as owner of the whole
system, waking the other actors off per-actor work queues; the human drops to periodic
review + occasional use. Canonical statements: constitution §Vision, prd §Vision,
actors §Orchestration (approved 2026-07-16).

## Roadmap

**Engine restructure & harness program** — plan of record:
`operations/plans/2026-07-12-engine-restructure-program.md` (checkpoints #1 + #2
recorded there). Epic definitions, inputs, and binary ACs: `governance/prd.md` §Epics.

- `[x]` **Phase 0 — session-ops restructure** — shipped 2026-07-12 (s138) · [HISTORY.md](HISTORY.md)
- `[x]` **Phase 1 — research grounding** — shipped 2026-07-13 (s144) · [HISTORY.md](HISTORY.md)
- `[x]` **Phase 2 — substrate audit & memory-system design + build (IB-176)** — shipped
  2026-07-13 (s142/s145) · [HISTORY.md](HISTORY.md)
- `[x]` **Phase 3 — user manual** — folded into kernel-compiler (E5) at checkpoint #2;
  no standalone doc
- `[x]` **Phase 4 — structured interview** — shipped 2026-07-16 (s148): kernel docs +
  harness-first ruling · [HISTORY.md](HISTORY.md)
- `[>]` **memory-layer (E1)** — per-actor memory surfaces; data → reflection → knowledge
- `[ ]` **task-layer (E2)** — per-actor work queues + task contract; absorbs DD/IB cleanup
- `[ ]` **self-description (E3)** — one YAML per actor + per harness, root descriptor
- `[ ]` **harness (E4+E7)** — enforcement points, wake/dispatch, fitness loop
- `[ ]` **kernel-compiler (E5)** — generalized forms, compile + drift `--check`,
  human-readable manual layer
- `[ ]` **audits-ship-remedies (E6)** — floating, order-independent; schedulable any time

## Current milestone

**memory-layer (E1)** — the memory & knowledge layer, per-agent + system-wide.
**DoD (PRD E1):** memory-architecture spec approved; every actor's memory surfaces
named; one reflection mechanism runs over an accumulation surface and routes outputs by
shape (decision → DD, pattern → knowledge/, work → task layer); deterministic store
check with a seeded-violation test.

Scopes (hill):
- `memory-spec` — the memory-architecture design note (spec before build) — **uphill**;
  open unknowns: per-actor vs shared store shape, which accumulation surfaces
  (session runs / tool calls / logs) to start with
- `reflection-build` — the reflection mechanism — uphill (waits on spec)
- `store-checks` — deterministic checks + seeded-violation test — uphill (waits on spec)

**Next unit of work:** `memory-spec` — draft the design note from PRD E1's named inputs
(`operations/self/` store, frozen SL corpus, KB memory cluster, `governance/actors.md`).
Nick flagged E1 as potentially the big one; memory-design thoroughness is opted in.

## Backlog / Icebox

Unscheduled — promote into a milestone when ready. Work items carry IB numbers;
triggers noted where promotion is event-gated.

- **IB-173** — three-bucket gate tiering, DD-29 refinement (approved direction; absorbs
  IB-103 per gate G7)
- **IB-171** — corpus-wide linkage-hygiene sweep (~87 legacy asymmetries measured
  session 144; Nick: "save for later")
- **IB-145** — GSD version-drift re-analysis
- **IB-174** — meta-skill-author assess follow-ups A/D/E (Nick-gated guard rulings)
- **IB-175** — governance visualization (strongest input in KB:
  `mdx-visual-plans-with-reusable-components` + visual-recap findings)
- **IB-177** — design-mode video-intake spec via `/meta-skill-author` (filed at the
  Phase 4 Block E sweep; was a blocker line)
- `/detect-drift` predicate hardening — currency baseline must be
  max(extraction_date, last_change_report); lesson L-10, second occurrence files the IB
- Findings hybrid search (FTS5 + local embeddings under `app/`) — designed-in
  component; implementation shape parked by Nick (session 142)
- kome.ai fallback backend for transcript-fetcher — trigger: next YouTube IP block
- Multi-tenant agentic-system design — named research gap (PRD non-goal for now);
  Nick gates promotion
- `/link-intake` escalation-language watch item (Rule 11)
- G3 / G9 guide bifurcation — trigger: DD-102 threshold (45 findings)
- MongoDB sizing-engine pilot — trigger: `/design-harness` ships
- Memongo improvement surfaces — `watched-libraries/memongo.md`
- GitHub collaborators for `il-published` — trigger: usernames from Nick
- Obsidian Workspaces config + Dataview install — trigger: Obsidian UI session
- Temp-directory cleanup — `/cleanup-cache` covers; run opportunistically

## Blockers / gates (Nick)

- **Five gate-clearance consolidation calls (optional review)** — the DD-97/DD-100
  extend/version-bump/create-new/merge rulings (HISTORY s146) were made under the
  delegated grant; all git-reversible if Nick wants a different granularity
- **Verbatim-storage finding null→P3** — session-132 reassessment, unruled
- **Re-injection correction** — next step unchosen (KB updated; remedy refuted upstream)
- **Mirror question** — automate `il-published` subtree push, or retire it (the engine
  rename, PRD open question, lands before E5 publishes the kernel)
