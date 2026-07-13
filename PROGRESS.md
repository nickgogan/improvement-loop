# Improvement Loop — Progress

Updated: 2026-07-13 (session 145 — milestone shipped: codifier-run executed over the
post-sweep crop (4 guide re-syntheses) and memory-system v1 built end-to-end (IB-176
steps 1–2: /self-improve loop + demand ledger live, SL distilled and closed). Next:
Nick-gated clearance of the promote/harvest/drift ruling queues.)

## Start here

New session? This file is the only cold-start artifact — read it top to bottom, then act.
"PROGRESS" / "continue" from Nick = proceed with the **next unit of work** under Current
milestone, no recital. Orientation lives in `CLAUDE.md` (engine) and `../../CHARTER.md`
(vision); the foundational-DD spine is `governance/FOUNDATIONS.md`. Shipped work lives in
[HISTORY.md](HISTORY.md) (newest-first, commit ranges); git carries the atomic log
(Conventional Commits). Session close = `/session-handoff` (reconcile-in-place; never a
dated handoff file). Every line here must pass route-then-compact: history → HISTORY.md,
decisions → DDs, work items → IB, research → KB. Operational lessons + demand rows live
in `operations/self/` (`/self-improve`; capture hook + store checker are harness-wired).

## North Star

Formalize the engine into an **agentic OS**: a harnessed system (a formal harness layer,
not agent-remembers-to-invoke-skills) whose `governance/` becomes a **portable kernel** —
the export unit any downstream agentic system pulls (PRD · constitution · generalized
asset forms · YAML descriptor), with harness materializations compiled per target.
Research remains the substrate: the KB grounds every design move. Full capture:
`project-management/design-notes/2026-06-22-agentic-os-direction.md` + plan §2.

## Roadmap

**Engine restructure & harness program** — plan of record:
`operations/plans/2026-07-12-engine-restructure-program.md` (checkpoint #1 outcome
recorded there, incl. Phase 5 revisions).

- `[x]` **Phase 0 — session-ops restructure** — shipped 2026-07-12 (session 138) · [HISTORY.md](HISTORY.md)
- `[x]` **Phase 1 — research grounding** — shipped 2026-07-13 (session 144) · [HISTORY.md](HISTORY.md)
- `[x]` **Phase 2 — substrate audit & memory-system design** — shipped 2026-07-13
  (session 142); design note ruled; **build (IB-176) shipped session 145** —
  `/self-improve` loop, demand ledger, calibration registry, SL closed · [HISTORY.md](HISTORY.md)
- `[ ]` **Phase 3 — user manual** — Nick gates whether/when; audience/altitude locked
  (Nick-builder; both, direction-bounded); manual-as-kernel-layer question open
- `[>]` **Phase 4 — structured interview** → engine PRD/constitution/actors; decide
  generalize-first vs harness-first → plan checkpoint #2
- `[ ]` **Phase 5 — harness + generalize** (order per Phase 4; checkpoint-#1 revisions:
  capability-as-composition-unit named input; maintenance/fitness DoD added)

## Current milestone

**Phase 4 — structured interview** (engine PRD/constitution/actors; ends at plan
checkpoint #2). Nick-present by nature. Phase 3 (user manual) stays Nick-gated and can
interleave if he opens it.

Scopes (hill):
- `gate-clearance` — pre-step, **downhill, all-Nick rulings in one sitting**: (a)
  `/self-improve promote` over the PROMOTE flags in `operations/self/retro-latest.md`
  (two high-severity, per-proposal gates); (b) harvest-queue rows across the four
  re-synthesized guides (`extracts/guides/*.harvest-queue.md`); (c) drift-report
  re-run/re-evaluate recommendations (`operations/drift-reports/2026-07-13-source-drift.md`).
- `phase4-interview` — **uphill**: interview structure not yet designed; plan
  open-questions (incl. "attachés", "division, to a degree" fragments) resolve inside it.

**Next unit of work:** `gate-clearance` (needs Nick live; an autonomous session should
instead prep `phase4-interview` — draft the interview structure from the plan's §Phase 4).

## Backlog / Icebox

Unscheduled — promote into a milestone when ready. Work items carry IB numbers; triggers
noted where promotion is event-gated.

- **IB-173** — three-bucket gate tiering, DD-29 refinement (approved direction; absorbs
  IB-103 per gate G7)
- **IB-171** — corpus-wide linkage-hygiene sweep (~87 legacy asymmetries measured
  session 144; Nick: "save for later")
- **IB-145** — GSD version-drift re-analysis
- **IB-174** — meta-skill-author assess follow-ups A/D/E (Nick-gated guard rulings)
- **IB-175** — governance visualization (strongest input now in KB:
  `mdx-visual-plans-with-reusable-components` + visual-recap findings, session 144)
- Findings hybrid search (FTS5 + local embeddings under `app/`) — designed-in component
  (design note §6); implementation shape parked by Nick (session 142)
- kome.ai fallback backend for transcript-fetcher — trigger: next YouTube IP block
  (technique in agent memory; fetch.py browser rung already hardened, session 143)
- Multi-tenant agentic-system design — named research-gap candidate; asker-scoped
  team-memory datapoint landed session 144; Nick gates promotion
- `/link-intake` escalation-language watch item (Rule 11)
- G3 / G9 guide bifurcation — trigger: DD-102 threshold (45 findings)
- MongoDB sizing-engine pilot — trigger: `/design-harness` ships
- Memongo improvement surfaces — `watched-libraries/memongo.md`
- GitHub collaborators for `il-published` — trigger: usernames from Nick
- Obsidian Workspaces config + Dataview install — trigger: Obsidian UI session
- Temp-directory cleanup — `/cleanup-cache` covers; run opportunistically

## Blockers / gates (Nick)

- **Gate-clearance queues** (the next unit of work): PROMOTE proposals (retro-latest),
  harvest-queue rows, drift-report re-runs — all per-item rulings
- **"Attachés" clarification** — likely transcription artifact (plan open-question 7);
  resolve in the Phase 4 interview
- **Design-mode video-intake spec** — is a formal `/meta-skill-author` spec still wanted?
- **Verbatim-storage finding null→P3** — session-132 reassessment, unruled
- **Re-injection correction** — next step unchosen (KB updated; remedy refuted upstream)
- **"Division, to a degree" garbled fragment** — resolve in the Phase 4 interview
- **Mirror question** — automate `il-published` subtree push, or retire it
