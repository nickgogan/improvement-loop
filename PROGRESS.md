# Improvement Loop — Progress

**Last Updated:** 2026-06-18 (session 121)

## Current Focus

**The engine collapse is fully landed on `main`.** The `engine-collapse-phase-1` branch was merged (`--no-ff`, `199a6ee`), pushed to `origin/main`, and deleted — **`main` is now the live line.** The federation collapsed into one self-evolving engine (Household OS → Notion, Claude Build retired, `meta-system` shell dissolved); the engine is fractal-complete with three altitudes (research → per-artifact assess/design → whole-system composition) and a root-level `CHARTER.md`.

**Phase 2 progress.** Slice 1 (session 120) defined the engine's top-altitude artifact form — the **schematic** (an evidence-grounded demand→configuration blueprint with a *required* evaluation/feedback layer): `_schema.yaml`, `knowledge/schematics/` + template + Dataview `_index`, **DD-107**, 2 grounded seeds. Slice 2 (session 121) brought schematics into the self-evolution loop by extending `/detect-drift` to scan `knowledge/schematics/` (array `grounded_in` + `updated` date basis; flags when any grounding `finding.last_updated > schematic.updated`).

**Active focus / next session:** **finish restructure-plan §Phase 2 item 2** — the two remaining sub-parts: (1) confirm/wire Dimension 7 (Evaluation) + Dimension 9 (Governance) queries to feed schematic re-evaluation; (2) note schematics as input to `/solicit-proposals` reflection rounds. Both small. Remaining Phase-2 items stay demand-gated (execution-surface axis, Builder-mode matching, more seeds).

**Next session target:** Session 122 — finish Phase 2 item 2. See `operations/handoffs/handoff-prompt-session-122-phase-2-item-2-finish.md`.

---

## What Changed This Session (121)

- **Phase 2 Slice 2 — `/detect-drift` extended to schematics** (`9416655`): `scan.py` gained `knowledge/schematics/` as a second scan root; reads array `grounded_in` + `updated`; drift = any grounding `finding.last_updated > schematic.updated`. New `schematic_drift_hits`, two-value schematic Recommendation enum, report section, and SL note recording the date-basis contract. Verified (2 seeds enumerated, all 11 groundings resolve, clean; drift branch proven via temporary backdate, reverted).
- **Merged + published the collapse:** `engine-collapse-phase-1` → `main` (`--no-ff`, `199a6ee`), pushed to `origin/main`, local branch deleted.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

1. **Phase 2 — schematics + evaluation/feedback layer** (in gated slices; plan of record: `project-management/design-notes/2026-06-18-engine-collapse-restructure-plan.md` §Phase 2).
   - ✅ **Slice 1 (done, session 120):** schematic form defined — `_schema.yaml`, `knowledge/schematics/` + template + `_index`, DD-107, 2 grounded seeds.
   - ✅ **Slice 2 (done, session 121):** `/detect-drift` extended to schematics (`9416655`); merged to main.
   - **`[next]` Finish §Phase 2 item 2:** (a) confirm/wire Dimension 7 (Evaluation) + Dimension 9 (Governance) queries to feed schematic re-evaluation; (b) note schematics as input to `/solicit-proposals` reflection rounds. Both small.
   - **`[deferred]` Execution-surface Librarian axis** — weak demand per consumer-abstractions-map (Rule 11); revisit at 2–3+ requests.
   - **`[deferred]` Builder-mode demand→schematic matching** (`/ask-kb`) — needs a fuller schematic library first.
   - **`[trigger]` More seed schematics** (project-coding-workcell, household-assistant) — when exercising the form against more demand is useful.
2. **`[optional]` Full `/system-audit`.** Post-collapse whole-system consistency sweep (fractal compliance incl. `app/`/`knowledge/`, cross-reference integrity, charter references). Run at Nick's discretion.

---

## Logged-for-future

Trigger-gated carryover. Don't action unless trigger fires.

1. Create Owner agent skills: skill-assessment, skill-extraction, agent-assessment, agent-extraction. Check if these exist already.
2. Place IL system on an actual harness, not just rely on the agent to invoke the right skills to take the right actions in the right order every time. 
3. - **`[deferred]` G3 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-architecture-decisions-split-proposal.md`. At 42 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45.
4. **`[deferred]` G9 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-governance-and-trust-split-proposal.md`. At 38 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45 or enforcement cluster hits 10.
