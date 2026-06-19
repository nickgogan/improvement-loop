# Improvement Loop — Progress

**Last Updated:** 2026-06-18 (session 120)

## Current Focus

**Engine-collapse Phase 1 is COMPLETE; post-Phase-1 cleanup and Phase 2 Slice 1 are done** (branch `engine-collapse-phase-1`, not yet merged to main — Nick's call). The federation collapsed into one self-evolving engine (Household OS → Notion, Claude Build retired, `meta-system` shell dissolved). The engine is fractal-complete with three altitudes (research → per-artifact assess/design → whole-system composition) and a root-level `CHARTER.md`.

**Phase 2 is underway in small gated slices.** Slice 1 (session 120) defined the engine's top-altitude artifact form — the **schematic** (an evidence-grounded demand→configuration blueprint with a *required* evaluation/feedback layer): `_schema.yaml` registration, a Dataview-cataloged `knowledge/schematics/`, a form-contract template, **DD-107**, and 2 grounded seeds (`research-scanning-agent`, `codebase-audit-workcell`).

**Active focus / next session:** **Phase 2 Slice 2** — extend `/detect-drift` to cover schematics (scan `knowledge/schematics/`, read the array `grounded_in`, flag when a grounding finding's `last_updated` moves past the schematic's `updated`). Then the remaining Phase-2 items stay demand-gated (execution-surface axis, Builder-mode matching).

**Next session target:** Session 121 — Phase 2 Slice 2 (drift integration). See `operations/handoffs/handoff-prompt-session-121-phase-2-slice-2-drift.md`.

---

## What Changed This Session (120)

- **Post-Phase-1 cleanup sweep:** memories reconciled (3 rewritten, 2 deleted as superseded, framing memory updated — memories live outside the repo); `target_system` vocab mass-collapsed to `improvement-loop` across 242 live files (`e59a741`, `archive/meta-system/` left as history); research-to-codification guide reframed to in-engine reality (`dafc99d`); priority queue seeded (`172b8ef`).
- **Phase 2 Slice 1:** schematic form defined + DD-107 (`d8af4dc`); 2 grounded seeds + SL (`5d9c574`). All 11 `grounded_in` links resolve.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

1. **Phase 2 — schematics + evaluation/feedback layer** (in gated slices; plan of record: `project-management/design-notes/2026-06-18-engine-collapse-restructure-plan.md` §Phase 2).
   - ✅ **Slice 1 (done, session 120):** schematic form defined — `_schema.yaml`, `knowledge/schematics/` + template + `_index`, DD-107, 2 grounded seeds.
   - **`[next]` Slice 2:** extend `/detect-drift` to schematics (scan `knowledge/schematics/`, read `grounded_in`, flag on moved grounding). Small, mechanical.
   - **`[deferred]` Execution-surface Librarian axis** — weak demand per consumer-abstractions-map (Rule 11); revisit at 2–3+ requests.
   - **`[deferred]` Builder-mode demand→schematic matching** (`/ask-kb`) — needs a fuller schematic library first.
   - **`[trigger]` More seed schematics** (project-coding-workcell, household-assistant) — when exercising the form against more demand is useful.
2. **`[nick-gate]` Merge `engine-collapse-phase-1` → main.** Phase 1 + cleanup + Phase 2 Slice 1 are committed on the branch; merge is Nick's call (do not auto-merge).
3. **`[optional]` Full `/system-audit`.** Post-collapse whole-system consistency sweep (fractal compliance incl. `app/`/`knowledge/`, cross-reference integrity, charter references). Run before or after merge at Nick's discretion.

---

## Logged-for-future

Trigger-gated carryover. Don't action unless trigger fires.

1. Create Owner agent skills: skill-assessment, skill-extraction, agent-assessment, agent-extraction. Check if these exist already.
2. Place IL system on an actual harness, not just rely on the agent to invoke the right skills to take the right actions in the right order every time. 
3. - **`[deferred]` G3 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-architecture-decisions-split-proposal.md`. At 42 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45.
4. **`[deferred]` G9 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-governance-and-trust-split-proposal.md`. At 38 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45 or enforcement cluster hits 10.
