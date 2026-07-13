# Improvement Loop — Progress

Updated: 2026-07-13 (session 141 — gate-execution closed (G8 + follow-ups). Second-brain
proposal drafted at residue-triage scope; Nick REJECTED that scoping and re-set the
direction: build an actual memory system. Four research reports persisted as design input.)

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
- `[>]` **Phase 2 — substrate audit & memory-system design** — audit gates all executed
  (G1–G8); remaining = the memory-system design (absorbs IB-172; Nick direction set
  session 141), proposed and Nick-ruled
- `[ ]` **Phase 3 — user manual** — Nick gates whether/when; audience/altitude locked
  (Nick-builder; both, direction-bounded); manual-as-kernel-layer question open
- `[ ]` **Phase 4 — structured interview** → engine PRD/constitution/actors; decide
  generalize-first vs harness-first → plan checkpoint #2
- `[ ]` **Phase 5 — harness + generalize** (order per Phase 4)

## Current milestone

**Phase 1 wrap + Phase 2 execution.** Phase 1 DoD: wave-3 resolved or honestly closed,
named-deps verified against the direction-note asks, delta report → checkpoint #1.
Phase 2 DoD: audit gates executed (done), memory-system design proposed and Nick-ruled.

Scopes (hill):
- `memory-system-design` — **uphill; Nick direction set (session 141), design open.**
  Build an actual memory system: Hermes-style external memory wired to self-improvement;
  OpenClaw + GBrain as references; **IL loop = one big agent** framing (consistent with
  single-implicit-agent). Must answer: **existing-corpus disposition** ("what to do with
  all of it") + **archiving policy**; G9 (boundary-case destination) folds in.
  Self-improvement exemplar: **CareerBuddy `ops-self-improve`** — pattern-lift it
  (`gh repo clone nickgogan/CareerBuddy`; its `ops/self/improve-backlog.md` queues 5
  contributions). Inputs: ruling atop
  `project-management/design-notes/2026-07-12-second-brain-proposal.md` (its residue
  triage + question table remain valid evidence; P1–P3 not adopted) + 4 reports in
  `operations/research-reports/` (2026-07-12/13: Librarian residue consult, Librarian
  architecture consult, web question-sweep, web OKF/Obsidian/RAG/lifecycle deep-dive).
  Key measured fact: findings corpus = **907 files**, at the KB's ~1000-doc traversal
  ceiling — KB prescribes hierarchical index reinforcement before RAG. Absorbs IB-172.
- `wave-3-retry` — 20-video LINKS.md backlog — **uphill, now unblocked (≥2026-07-13).**
  Chain: plain `fetch.py --input LINKS.md` → `--backend browser` rung (live-unverified) →
  `/link-intake` triage; whole-chain failure = stop, respace ≥1 day. Then named-deps
  gap-check (BMAD/superpowers/Archon/Jones vs direction-note asks) → delta report →
  checkpoint #1.
- `gate-execution` — **done (session 141)** · [HISTORY.md](HISTORY.md)

**Next unit of work:** `memory-system-design` brainstorm with Nick inline — start from
the four research reports + the design-note ruling; frame options for corpus disposition,
archiving, and the self-improvement write-back loop. Then `wave-3-retry`.

## Backlog / Icebox

Unscheduled — promote into a milestone when ready. Work items carry IB numbers; triggers
noted where promotion is event-gated.

- **IB-173** — three-bucket gate tiering, DD-29 refinement (approved direction; absorbs
  IB-103 per gate G7)
- **IB-171** — corpus-wide linkage-hygiene sweep (Nick: "save for later")
- **IB-145** — GSD version-drift re-analysis
- **IB-174** — meta-skill-author assess follow-ups A/D/E (Nick-gated guard rulings)
- **IB-175** — governance visualization (DD corpus + architecture in glanceable form)
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
