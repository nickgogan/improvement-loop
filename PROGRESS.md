# Improvement Loop — Progress

**Last Updated:** 2026-06-19 (session 123)

## Current Focus

**The engine collapse is fully landed on `main`.** The `engine-collapse-phase-1` branch was merged (`--no-ff`, `199a6ee`), pushed to `origin/main`, and deleted — **`main` is now the live line.** The federation collapsed into one self-evolving engine (Household OS → Notion, Claude Build retired, `meta-system` shell dissolved); the engine is fractal-complete with three altitudes (research → per-artifact assess/design → whole-system composition) and a root-level `CHARTER.md`.

**Phase 2 progress.** Slices 1–2 (sessions 120–121) defined the **schematic** form (DD-107) and brought it into `/detect-drift`. Session 122 finished **§Phase 2 item 2** (made the Dimension 7/9 → schematic re-evaluation wiring explicit; added schematics as a `/solicit-proposals` reflection input) and **item 3** (two consumer-facing seed schematics — `project-coding-workcell`, `scheduled-operations-assistant`; the library now spans research/operations/audit/coding, 4 seeds, `/detect-drift` clean). Remaining Phase-2 items stay demand-gated (execution-surface axis, Builder-mode matching).

**First `/system-audit` (session 122)** ran post-collapse: 0 Critical, structurally sound. All findings remediated this session — **DD-108** (Owner files DDs as mechanics; Nick gates content), **DD-109** (re-home system-scoped-skills / skills-as-atomic-unit into live governance), agent + skill contract fixes, post-collapse framing fixes, and all 148 system-log entries normalized to canonical `date:`. Report: `operations/audit-reports/2026-06-18-system-audit.md`.

**Session 123 (governance hygiene + audit-home disambiguation) landed.** The stale-IB sweep cleared 15 post-collapse items; the open backlog is now small and engine-relevant. IB-169 was resolved by **DD-110** — the two audits (`/audit-artifacts`, renamed from `/audit-system`, and `/system-audit`) were disambiguated, not consolidated, with both homes moved under `operations/`. Post-collapse "MetaSystem vs IL" framing was reconciled to the one-engine three-altitude model and the two consumer-abstractions maps merged into one.

**Active focus / next session (124):** **rationalize concept docs, agent reference/helper files, and the `knowledge/` folder (IB-170)** — discuss-first, spec-before-build. Immediate trigger: concept docs are split across two homes (`operations/references/librarian/` vs `knowledge/reference/harness.md`). See `operations/handoffs/handoff-prompt-session-124-concept-doc-reorg.md`.

---

## What Changed This Session (123)

- **Stale-IB sweep** (`2dd1b2f`): 15 post-collapse items reconciled. Cancelled the meta-system-era items (IB-167/168/142/136/137 — DD-103) and Household OS/Notion-era items (IB-96/28/49/51/106/100 — DD-106), and proposer-era items (IB-147/101 — DD-80); verified IB-146 (`/synthesize-guide`) and IB-139 (fractal-complete) as Done. Open backlog now: IB-102, IB-103 (Deferred), IB-145, IB-148, IB-170.
- **IB-169 resolved → DD-110** (`b6a5cd8`): verified the two audits are genuinely distinct (per-artifact contract conformance vs. system drift/consistency), so disambiguated rather than consolidated. `/audit-system` renamed **`/audit-artifacts`**; both audit homes moved under `operations/` — `operations/artifact-audits/` (`/audit-artifacts`) and `operations/system-audits/` (`/system-audit`); root `audit-reports/` removed. All live references updated; immutable/historical docs preserved with banners.
- **Post-collapse framing reconciled + maps merged** (`3cb1c91`): the two consumer-abstractions maps (per-artifact + whole-system, from the two-system era) **merged into one** altitude-sectioned map at `operations/references/consumer-abstractions-map.md`; `harness.md` reframed to top/middle altitude (fixed a live bug — template `target_system: meta-system` → `improvement-loop`); `capability-roadmap.md` bannered superseded.
- **IB-170 filed** (`89c02df`): concept-docs / agent-helpers / `knowledge/`-folder rationalization — next session's task.
- **Not yet pushed:** 5 commits ahead of `origin/main` (the 4 above + the session-122 close `b1e7585`).

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

1. **`[next]` Concept-docs / agent-helpers / `knowledge/`-folder rationalization (session 124, IB-170).** Discuss-first, spec-before-build. Decide where concept docs, agent reference/helper files, and `knowledge/` content belong and how they relate; immediate trigger is the concept-doc split (`operations/references/librarian/` vs `knowledge/reference/harness.md`). Gate the taxonomy, write a placement spec, then move with `git mv`. Handoff: `operations/handoffs/handoff-prompt-session-124-concept-doc-reorg.md`.
2. **Phase 2 — schematics + evaluation/feedback layer** (gated slices; plan of record: `project-management/design-notes/2026-06-18-engine-collapse-restructure-plan.md` §Phase 2).
   - ✅ **Slices 1–2 (sessions 120–121):** schematic form (DD-107) + `/detect-drift` integration.
   - ✅ **Item 2 (session 122):** D7/D9 → schematic re-evaluation wiring made explicit; schematics as `/solicit-proposals` input.
   - ✅ **Item 3 (session 122):** 2 seed schematics (`project-coding-workcell`, `scheduled-operations-assistant`).
   - **`[deferred]` Item 4 — Builder-mode demand→schematic matching** (`/ask-kb`) — now more plausible with a 4-seed library; revisit when exercising it is useful.
   - **`[deferred]` Execution-surface Librarian axis** — weak demand per consumer-abstractions-map (Rule 11); revisit at 2–3+ requests.
   - **`[trigger]` More seed schematics** — when exercising the form against more demand is useful.
3. **`[deferred]` Ready maintenance** — IB-145 (re-analyze GSD for version drift) and IB-148 (build `/session-handoff-review`). Self-contained; pick up when the queue clears.

---

## Logged-for-future

Trigger-gated carryover. Don't action unless trigger fires.

1. Place the engine on an actual harness, not just relying on the agent to invoke the right skills in the right order every time. (Aligns with the supervised-autonomy trajectory in DD-108 — URLs-in / queries-in under Nick's oversight.)
2. **`[deferred]` G3 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-architecture-decisions-split-proposal.md`. At 42 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45.
3. **`[deferred]` G9 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-governance-and-trust-split-proposal.md`. At 38 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45 or enforcement cluster hits 10.
