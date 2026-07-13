# Improvement Loop — Progress

Updated: 2026-07-13 (session 142 — memory-system design brainstormed and ruled inline;
demand ledger (query/intent log) added to the CareerBuddy-lift loop. Design note filed,
build = IB-176, IB-172 closed. Next: wave-3 retry — Nick added 9 new links to LINKS.md.)

## Start here

New session? This file is the only cold-start artifact — read it top to bottom, then act.
"PROGRESS" / "continue" from Nick = proceed with the **next unit of work** under Current
milestone, no recital. Orientation lives in `CLAUDE.md` (engine) and `../../CHARTER.md`
(vision); the foundational-DD spine is `governance/FOUNDATIONS.md`. Shipped work lives in
[HISTORY.md](HISTORY.md) (newest-first, commit ranges); git carries the atomic log
(Conventional Commits). Session close = `/session-handoff` (reconcile-in-place; never a
dated handoff file). Every line here must pass route-then-compact: history → HISTORY.md,
decisions → DDs, work items → IB, research → KB.

## North Star

Formalize the engine into an **agentic OS**: a harnessed system (a formal harness layer,
not agent-remembers-to-invoke-skills) whose `governance/` becomes a **portable kernel** —
the export unit any downstream agentic system pulls (PRD · constitution · generalized
asset forms · YAML descriptor), with harness materializations compiled per target.
Research remains the substrate: the KB grounds every design move. Full capture:
`project-management/design-notes/2026-06-22-agentic-os-direction.md` + plan §2.

## Roadmap

**Engine restructure & harness program** — plan of record:
`operations/plans/2026-07-12-engine-restructure-program.md`.

- `[x]` **Phase 0 — session-ops restructure** — shipped 2026-07-12 (session 138) · [HISTORY.md](HISTORY.md)
- `[>]` **Phase 1 — research grounding** — cresting: CareerBuddy + #8 done; remaining =
  wave-3 chain (unblocked ≥07-13) + named-deps gap-check + delta report → plan checkpoint #1
- `[x]` **Phase 2 — substrate audit & memory-system design** — shipped 2026-07-13
  (session 142): gates G1–G8 executed; design ruled →
  `project-management/design-notes/2026-07-13-memory-system-design.md`; build = IB-176 · [HISTORY.md](HISTORY.md)
- `[ ]` **Phase 3 — user manual** — Nick gates whether/when; audience/altitude locked
  (Nick-builder; both, direction-bounded); manual-as-kernel-layer question open
- `[ ]` **Phase 4 — structured interview** → engine PRD/constitution/actors; decide
  generalize-first vs harness-first → plan checkpoint #2
- `[ ]` **Phase 5 — harness + generalize** (order per Phase 4)

## Current milestone

**Phase 1 wrap + memory-system v1 build.** Phase 1 DoD: wave-3 resolved or honestly
closed, named-deps gap-check verified against the direction-note asks, delta report →
checkpoint #1. Build DoD: IB-176 ship-order steps 1–2 (self-improve loop + demand
ledger live; SL distilled and closed).

Scopes (hill):
- `wave-3-retry` — LINKS.md backlog (20 retry videos + 9 new links from Nick, one dup) —
  **uphill, unblocked (≥2026-07-13).** Chain: plain `fetch.py --input LINKS.md` →
  `--backend browser` rung (live-unverified) → `/link-intake` triage; whole-chain
  failure = stop, respace ≥1 day. Then named-deps gap-check (BMAD/superpowers/Archon/
  Jones vs direction-note asks — also feeds the deferred DD/IB task-queue study, design
  note §6) → delta report → checkpoint #1.
- `memory-system-build` — IB-176 — **uphill, queued after wave-3.** Design ruled
  (session 142): `operations/self/` store + 4-mode skill + UserPromptSubmit capture
  hook + store checker in pre-commit + `/session-handoff` lessons-check;
  `/process-feedback` folds into scan mode; first scan run = SL distill-then-close.
  Spec: `project-management/design-notes/2026-07-13-memory-system-design.md`.

**Next unit of work:** `wave-3-retry`.

## Backlog / Icebox

Unscheduled — promote into a milestone when ready. Work items carry IB numbers; triggers
noted where promotion is event-gated.

- **IB-173** — three-bucket gate tiering, DD-29 refinement (approved direction; absorbs
  IB-103 per gate G7)
- **IB-171** — corpus-wide linkage-hygiene sweep (Nick: "save for later")
- **IB-145** — GSD version-drift re-analysis
- **IB-174** — meta-skill-author assess follow-ups A/D/E (Nick-gated guard rulings)
- **IB-175** — governance visualization (DD corpus + architecture in glanceable form)
- Findings hybrid search (FTS5 + local embeddings under `app/`) — designed-in component
  (design note §6); implementation shape parked by Nick (session 142)
- Multi-tenant agentic-system design — named research-gap candidate (session 139
  observation: single-operator exemplars dominate the corpus); Nick gates promotion
- `/link-intake` escalation-language watch item (Rule 11)
- G3 / G9 guide bifurcation — trigger: DD-102 threshold (45 findings)
- MongoDB sizing-engine pilot — trigger: `/design-harness` ships
- Memongo improvement surfaces — `watched-libraries/memongo.md`
- GitHub collaborators for `il-published` — trigger: usernames from Nick
- Obsidian Workspaces config + Dataview install — trigger: Obsidian UI session
- Temp-directory cleanup — `/cleanup-cache` covers; run opportunistically

## Blockers / gates (Nick)

- **Design-mode video-intake spec** — is a formal `/meta-skill-author` spec still wanted?
- **Verbatim-storage finding null→P3** — session-132 reassessment, unruled
- **Re-injection correction** — next step unchosen (KB updated; remedy refuted upstream)
- **"Division, to a degree" garbled fragment** — resolve in the Phase 4 interview
- **Mirror question** — automate `il-published` subtree push, or retire it
