# Improvement Loop — Progress

Updated: 2026-07-12 (session 138 — restructure-program Phase 0 in flight: HISTORY.md
backfilled, this file restructured forward-only, `/session-handoff` rewritten
reconcile-in-place, dated handoffs archived, Conventional Commits + line-budget hook
adopted; SL-narrowing ruling pending at close. Wave-3 retry still parked — 24h window.)

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

- `[>]` **Phase 0 — session-ops restructure** — landing this session (138, 2026-07-12)
- `[ ]` **Phase 1 — research grounding** — wave-3 video backlog, Nick's second-brain/harness
  links, CareerBuddy as primary source, named research dependencies → plan checkpoint #1
- `[ ]` **Phase 2 — substrate audit & second-brain design** — kernel-vs-state verdicts per
  class (DDs, IB, design notes, SL, guides, concept docs); ops second-brain sized per Rule 11
- `[ ]` **Phase 3 — user manual** — Nick gates whether/when; audience/altitude locked
  (Nick-builder; both, direction-bounded); manual-as-kernel-layer question open
- `[ ]` **Phase 4 — structured interview** → engine PRD/constitution/actors; decide
  generalize-first vs harness-first → plan checkpoint #2
- `[ ]` **Phase 5 — harness + generalize** (order per Phase 4)

**Engine-collapse Phase 2 leftovers** (older plan:
`project-management/design-notes/2026-06-18-engine-collapse-restructure-plan.md`) — all
demand-gated: Builder-mode schematic matching, execution-surface axis, more seed
schematics. Revisit on demand signals, not on a schedule.

## Current milestone

**Phase 0 — session-ops restructure.** DoD: a fresh session cold-starts from this file
alone; no dated handoff is authored; commit convention + line-budget check live; Nick has
ruled on the System Log's narrowed role.

Hill: HISTORY backfill, PROGRESS restructure, `/session-handoff` rewrite, handoff
archive + wake-up idiom, commit convention + hook — **over the top, landing** · SL
ruling — **up the hill, gated at session close**.

**Next unit of work:** finish Phase 0 (SL ruling at close), then open **Phase 1** with
the wave-3 retry — parked until ≥2026-07-13 (full ~24h from wave-2's 2026-07-12 IP
block); chain: plain `fetch.py --input LINKS.md` → `--backend browser` rung
(live-unverified) → `/link-intake` triage on recoveries; if the whole chain fails, stop
and respace ≥1 day. Then CareerBuddy primary-source intake (plan §Phase 1 item 2).

## Backlog / Icebox

Unscheduled — promote into a milestone when ready. Work items carry IB numbers; triggers
noted where promotion is event-gated.

- **IB-172** — layered memory architecture + OKF design (approved direction; Hermes/OpenClaw inspiration)
- **IB-173** — three-bucket gate tiering, DD-29 refinement (approved direction)
- **IB-171** — corpus-wide linkage-hygiene sweep (Nick: "save for later")
- **IB-145** — GSD version-drift re-analysis; **IB-148** — handoff-review skill (likely
  mooted by Phase 0's `/session-handoff` rewrite — resolve or close next maintenance pass)
- meta-skill-author assess follow-ups A/D/E
- `/link-intake` escalation-language watch item (Rule 11)
- Governance visualization (boil DDs/architecture into a human-visualizable form)
- G3 / G9 guide bifurcation — trigger: DD-102 threshold (45 findings)
- MongoDB sizing-engine pilot — trigger: `/design-harness` ships
- Memongo improvement surfaces — `watched-libraries/memongo.md`
- GitHub collaborators for `il-published` — trigger: usernames from Nick
- Obsidian Workspaces config + Dataview install — trigger: Obsidian UI session
- Temp-directory cleanup — `/cleanup-cache` covers; run opportunistically

## Blockers / gates (Nick)

- **SL-narrowing ruling** (Phase 0 item 6; recommended option (a): git + HISTORY carry
  session tracking, SL keeps only learnings) — presented at session-138 close
- **#8 taxonomy/clustering repo name** — Phase 1 input
- **Design-mode video-intake spec** — is a formal `/meta-skill-author` spec still wanted?
- **Verbatim-storage finding null→P3** — session-132 reassessment, unruled
- **Re-injection correction** — next step unchosen (KB updated; remedy refuted upstream)
- **"Division, to a degree" garbled fragment** — resolve in the Phase 4 interview
- **Mirror question** — automate `il-published` subtree push, or retire it
