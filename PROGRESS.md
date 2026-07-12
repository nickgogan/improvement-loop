# Improvement Loop — Progress

Updated: 2026-07-12 (session 139 — Phase 1 nearly closed: CareerBuddy + #8 context-hub
intaken to the KB (anonymized). Phase 2 opened early per Nick: substrate audit filed with
gates G1–G9; Nick granted door-type delegation — G1–G8 sanctioned, G9 folds into the
second-brain proposal.)

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
  wave-3 chain (≥07-13) + named-deps gap-check + delta report → plan checkpoint #1
- `[>]` **Phase 2 — substrate audit & second-brain design** — audit filed
  (`project-management/design-notes/2026-07-12-substrate-audit.md`); gate execution +
  second-brain proposal remain
- `[ ]` **Phase 3 — user manual** — Nick gates whether/when; audience/altitude locked
  (Nick-builder; both, direction-bounded); manual-as-kernel-layer question open
- `[ ]` **Phase 4 — structured interview** → engine PRD/constitution/actors; decide
  generalize-first vs harness-first → plan checkpoint #2
- `[ ]` **Phase 5 — harness + generalize** (order per Phase 4)

## Current milestone

**Phase 1 wrap + Phase 2 execution.** Phase 1 DoD: wave-3 resolved or honestly closed,
named-deps verified against the direction-note asks, delta report → checkpoint #1.
Phase 2 DoD: audit gates executed, second-brain design proposed and Nick-ruled.

Scopes (hill):
- `wave-3-retry` — 20-video LINKS.md backlog — **uphill, unblocks ≥2026-07-13**. Chain:
  plain `fetch.py --input LINKS.md` → `--backend browser` rung (live-unverified) →
  `/link-intake` triage; whole-chain failure = stop, respace ≥1 day. Then named-deps
  gap-check (BMAD/superpowers/Archon/Jones vs direction-note asks — existing KB coverage
  unverified, skipped session 139) → delta report → checkpoint #1.
- `gate-execution` — **downhill, sanctioned**: execute substrate-audit gates G1–G8 per
  the door-type delegation (G5 anchor ruling: identification report). Includes the
  urgent `/extract-artifacts` repair (broken by SL retirement — fix first), IB hygiene,
  design-note archive sweep, no-gate `/maintain-docs` follow-ups.
- `second-brain-proposal` — **uphill, Nick gates the mechanism** (Rule 11): size against
  the audit's drop-inventory (§System Log distill candidates — dominant pattern:
  stranded calibration data; §IB closure-note overflow). G9 (boundary-case routing
  destination) folds into this proposal, not decided ad hoc.

**Next unit of work:** `wave-3-retry` if the date allows (≥07-13), else start
`gate-execution` with the `/extract-artifacts` repair.

## Backlog / Icebox

Unscheduled — promote into a milestone when ready. Work items carry IB numbers; triggers
noted where promotion is event-gated.

- **IB-172** — layered memory architecture + OKF design (approved direction; SL corpus is
  feedstock; second-brain proposal is the near-term slice)
- **IB-173** — three-bucket gate tiering, DD-29 refinement (approved direction; absorbs
  IB-103 per gate G7)
- **IB-171** — corpus-wide linkage-hygiene sweep (Nick: "save for later")
- **IB-145** — GSD version-drift re-analysis
- meta-skill-author assess follow-ups A/D/E + governance visualization — get IB numbers
  during gate-execution (G7)
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

- **Second-brain mechanism** — Rule 11 gate on the upcoming proposal (G9 folded in)
- **Design-mode video-intake spec** — is a formal `/meta-skill-author` spec still wanted?
- **Verbatim-storage finding null→P3** — session-132 reassessment, unruled
- **Re-injection correction** — next step unchosen (KB updated; remedy refuted upstream)
- **"Division, to a degree" garbled fragment** — resolve in the Phase 4 interview
- **Mirror question** — automate `il-published` subtree push, or retire it
