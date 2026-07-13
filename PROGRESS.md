# Improvement Loop — Progress

Updated: 2026-07-13 (session 144 — Phase 1 shipped: wave-3 triaged + extracted, named
deps grounded, delta report → checkpoint #1 recorded in the plan; KB currency sweep
re-analyzed 4 repos, onboarded pydantic-ai, applied the Nick-accepted priority
reassessment (2 new P1s). Next: Codifier pipeline over the new crop.)

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
`operations/plans/2026-07-12-engine-restructure-program.md` (checkpoint #1 outcome
recorded there, incl. Phase 5 revisions).

- `[x]` **Phase 0 — session-ops restructure** — shipped 2026-07-12 (session 138) · [HISTORY.md](HISTORY.md)
- `[x]` **Phase 1 — research grounding** — shipped 2026-07-13 (session 144): wave-3
  triaged + extracted, named-deps gap-check grounded, delta report → checkpoint #1;
  bulk video intake closed as a phase instrument · [HISTORY.md](HISTORY.md)
- `[x]` **Phase 2 — substrate audit & memory-system design** — shipped 2026-07-13
  (session 142): gates G1–G8; design ruled →
  `project-management/design-notes/2026-07-13-memory-system-design.md`; build = IB-176 · [HISTORY.md](HISTORY.md)
- `[ ]` **Phase 3 — user manual** — Nick gates whether/when; audience/altitude locked
  (Nick-builder; both, direction-bounded); manual-as-kernel-layer question open
- `[ ]` **Phase 4 — structured interview** → engine PRD/constitution/actors; decide
  generalize-first vs harness-first → plan checkpoint #2
- `[ ]` **Phase 5 — harness + generalize** (order per Phase 4; checkpoint-#1 revisions:
  capability-as-composition-unit named input; maintenance/fitness DoD added)

## Current milestone

**KB codification + memory-system v1 build.** Codification DoD: Codifier pipeline run
over the post-sweep P1/P2 crop — `/identify-artifacts` → gated report →
`/extract-artifacts` → gated staging (Nick ruled this next, session 144). Build DoD:
IB-176 ship-order steps 1–2 (self-improve loop + demand ledger live; SL distilled and
closed).

Scopes (hill):
- `codifier-run` — `/identify-artifacts` over the new P1/P2 crop (2 new P1s incl.
  ralph-wiggum + append-only-run-log; 4 new P2s), then `/extract-artifacts` on the
  approved report — **downhill** (procedure known; both gates are Nick's).
- `memory-system-build` — IB-176 — **uphill, queued after codifier-run.** Design ruled
  (session 142); today's Pass 2 independently corroborated it (memory triad, session-
  history bootstrap ⇒ SL distill-then-close). Spec:
  `project-management/design-notes/2026-07-13-memory-system-design.md`.

**Next unit of work:** `codifier-run`.

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

- **"Attachés" clarification** — direction-note superpowers ask; likely transcription
  artifact (gap-check 2026-07-13; plan open-question 7) — one-liner from Nick
- **Design-mode video-intake spec** — is a formal `/meta-skill-author` spec still wanted?
- **Verbatim-storage finding null→P3** — session-132 reassessment, unruled
- **Re-injection correction** — next step unchosen (KB updated; remedy refuted upstream)
- **"Division, to a degree" garbled fragment** — resolve in the Phase 4 interview
- **Mirror question** — automate `il-published` subtree push, or retire it
