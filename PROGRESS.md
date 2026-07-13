# Improvement Loop — Progress

Updated: 2026-07-13 (session 146 — gate-clearance COMPLETE under Nick's delegated-judgment
grant: L-1/L-2/L-4 promotions applied, all 18 harvest rows resolved [14 extracted incl. a
DD-100 v2 + a DD-97 extend + 2 create-new, 2 merged, 2 dismissed], 11 drift re-extractions
+ 3 schematic re-evals done. Phase 4 interview structure drafted. Next: Nick gates.)

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
- `gate-clearance` — **done**: promotions L-1/L-2/L-4 applied (proposal-log `P-1..P-3`);
  all 18 harvest rows across 4 queues resolved; 11/11 drift re-extractions + 3 schematic
  re-evals done. Five corpus-scan gates (DD-97/DD-100) ruled inline under the delegated
  grant — all two-way doors, listed in HISTORY for Nick's review/override: byte-stable
  catalog → extend; static-first → seven-layer v2; lesson-store-entry-schema + pruning →
  create-new; derive-dont-edit twin → merged.
- `phase4-interview` — **cresting**: structure drafted
  (`project-management/design-notes/2026-07-13-phase4-interview-structure.md`, adapts
  CareerBuddy `ops-vision-to-plan`); awaits Nick's gate on its §5 open questions before running.

**Next unit of work:** Nick gates the `phase4-interview` structure (§5 open questions),
then the interview runs. Optional Nick review: the five DD-97/DD-100 consolidation calls
in HISTORY (any can be reverted/re-split — all git-reversible).

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

- **Phase 4 interview structure gate** — the drafted structure's §5 open questions
  (sitting count; kernel-doc naming/homes) need a ruling before the interview runs
- **Five gate-clearance consolidation calls (optional review)** — the DD-97/DD-100
  extend/version-bump/create-new/merge rulings (HISTORY session 146) were made under the
  delegated grant; all git-reversible if Nick wants a different granularity
- **"Attachés" clarification** — likely transcription artifact (plan open-question 7);
  resolve in the Phase 4 interview (now Block 0 of the drafted structure)
- **Design-mode video-intake spec** — is a formal `/meta-skill-author` spec still wanted?
- **Verbatim-storage finding null→P3** — session-132 reassessment, unruled
- **Re-injection correction** — next step unchosen (KB updated; remedy refuted upstream)
- **"Division, to a degree" garbled fragment** — resolve in the Phase 4 interview
- **Mirror question** — automate `il-published` subtree push, or retire it
