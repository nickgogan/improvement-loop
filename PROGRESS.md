# Improvement Loop — Progress

Updated: 2026-07-19 (session 151 — link-intake wave-4 shipped end-to-end: 30-link triage
Nick-accepted, Pass 2 extracted into the KB behind the G9.I6 gate, eve + openwiki
registered, LINKS.md empty; ruled-queue item 1 done. Next: guide refresh.)

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
- `[ ]` **self-description (E3)** — one YAML per actor + per harness, root descriptor.
  Expanded (Nick, 2026-07-18): a portable JSON/YAML **asset-description language** fully
  describing engine assets — reusable foundations for port/reharness meta-skills
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
- `memory-spec` — the memory-architecture design note (spec before build) —
  **cresting**; research corpus complete + synthesized in
  `operations/plans/memory-spec-inputs/` (A internal briefs, B 12-framework survey,
  C harness survey; both former unknowns answered; the E1↔E4 reflection-cadence seam
  is stated there). Drafting is section-gated with Nick; parked behind the ruled queue.
- `reflection-build` — the reflection mechanism — uphill (waits on spec)
- `store-checks` — deterministic checks + seeded-violation test — uphill (waits on spec)

**Nick-ruled queue (2026-07-18)** — front-runs memory-spec drafting; E1 scopes stay
parked-cresting until this clears or Nick re-prioritizes. (Original item 1 — the full
`/link-intake` run — shipped session 151 · [HISTORY.md](HISTORY.md).)
1. **Guide refresh** — update the guides on creating **agent memories, harnesses, and
   agentic systems** from the wave-4 intake + the memory-spec corpus.
2. **Asset-description language** — begin the portable JSON/YAML language describing
   engine assets (pulls E3 forward; foundations for port/reharness meta-skills).
   Wave-4 prior art in KB: eve's folder-compiled-manifest (carries a flagged
   `contradicts` tension vs `machine-readable-system-contract-with-wiring-rows` —
   implicit discovery vs explicit wiring) + the per-control record from `/simplify-
   context`'s ENHANCE deltas.
3. **Eval sophistication** — upgrade `/meta-skill-author`'s eval discipline, anchored
   on the DeepMind good-skills framework. Anchor talk extracted at wave-4: the five
   ENHANCE deltas (SkillBench numbers, capability-vs-preference taxonomy, executable
   eval harness, retirement protocol, multi-trial discipline) are in the 2026-07-18
   triage report §ENHANCE.

**Next unit of work:** queue item 1 — the guide refresh. Items 2–3 follow in order.

## Backlog / Icebox

Unscheduled — promote into a milestone when ready. Work items carry IB numbers;
triggers noted where promotion is event-gated.

- **Wave-4 follow-ups** (each Nick-gated; canonical list: 2026-07-18 triage report
  §Follow-up): comprehension-gate skill ADD via `/design-skill` (Litt ExplainDiff
  gist); ENHANCE deltas for `/self-improve`, `/dd`, `/simplify-context` (the
  `/meta-skill-author` deltas ride queue item 3); `/repo-analyzer` passes on eve +
  openwiki; reciprocal back-links via the next `/finding-crosslink` pass
- **IB-180** — kome.ai fallback backend inside fetch.py (trigger fired twice: s143
  24/24, s151 7/7 — chunking alone doesn't prevent mid-run IP blocks)
- **IB-179** — build `/watch-youtube` per the 2026-07-18 design note (v0 tool + eval
  fixture in place; strict filter bar ruled; regression bar = the eval numbers)
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
- **IB-178** — KB corrections sweep: stale/misattributed ledger from the memory survey
  (canonical list in B-synthesis §KB corrections ledger; wave-4 appended the openwiki
  survey gap + pre-collapse applicability values)
- `/detect-drift` predicate hardening — currency baseline must be
  max(extraction_date, last_change_report); lesson L-10, second occurrence files the IB
- Findings hybrid search (FTS5 + local embeddings under `app/`) — designed-in
  component; implementation shape parked by Nick (session 142)
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
