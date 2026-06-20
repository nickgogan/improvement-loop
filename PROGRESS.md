# Improvement Loop — Progress

**Last Updated:** 2026-06-20 (session 124)

## Current Focus

**The engine collapse is fully landed on `main`.** The `engine-collapse-phase-1` branch was merged (`--no-ff`, `199a6ee`), pushed to `origin/main`, and deleted — **`main` is now the live line.** The federation collapsed into one self-evolving engine (Household OS → Notion, Claude Build retired, `meta-system` shell dissolved); the engine is fractal-complete with three altitudes (research → per-artifact assess/design → whole-system composition) and a root-level `CHARTER.md`.

**Phase 2 progress.** Slices 1–2 (sessions 120–121) defined the **schematic** form (DD-107) and brought it into `/detect-drift`. Session 122 finished **§Phase 2 item 2** (made the Dimension 7/9 → schematic re-evaluation wiring explicit; added schematics as a `/solicit-proposals` reflection input) and **item 3** (two consumer-facing seed schematics — `project-coding-workcell`, `scheduled-operations-assistant`; the library now spans research/operations/audit/coding, 4 seeds, `/detect-drift` clean). Remaining Phase-2 items stay demand-gated (execution-surface axis, Builder-mode matching).

**First `/system-audit` (session 122)** ran post-collapse: 0 Critical, structurally sound. All findings remediated this session — **DD-108** (Owner files DDs as mechanics; Nick gates content), **DD-109** (re-home system-scoped-skills / skills-as-atomic-unit into live governance), agent + skill contract fixes, post-collapse framing fixes, and all 148 system-log entries normalized to canonical `date:`. Report: `operations/audit-reports/2026-06-18-system-audit.md`.

**Session 123 (governance hygiene + audit-home disambiguation) landed.** The stale-IB sweep cleared 15 post-collapse items; the open backlog is now small and engine-relevant. IB-169 was resolved by **DD-110** — the two audits (`/audit-artifacts`, renamed from `/audit-system`, and `/system-audit`) were disambiguated, not consolidated, with both homes moved under `operations/`. Post-collapse "MetaSystem vs IL" framing was reconciled to the one-engine three-altitude model and the two consumer-abstractions maps merged into one.

**Active focus / next session (125):** **governance-health audit + knowledge-caching coverage.** Two phases with a gate: (1) read-only diagnostic of DD coherence + DD↔IB↔git mapping (lean on `/governance-audit` and `/system-audit`) → governance-health report → gated hygiene fixes; (2) propose-only knowledge-coverage map (do `knowledge/reference`+guides+patterns represent the DD/IB design wisdom?) + caching-policy recommendation (include/exclude criteria, Owner-vs-Librarian wiring) — no DD/IB/caching writes (Rule 11). See `operations/handoffs/handoff-prompt-session-125-governance-health-caching-audit.md`.

---

## What Changed This Session (124)

IB-170 was reframed by Nick from "concept-doc placement" to a broader `knowledge/`↔`extracts/` reconciliation. The concept-doc split is now understood as a sub-case.

- **Household-os archived** (`d19eb1b`): `knowledge/reference/household-os/` → `archive/household-os/` (40 files; git renames, history preserved). Pre-collapse four-system material, retained (not deleted) as design substrate for the planned Notion second-brain + custom-agents work with the Librarian. 2 live schematic `composed_of` pointers updated; `_ARCHIVED.md` breadcrumb added.
- **Pipeline-guide drift fixed** (`b8e87bf`): `research-to-codification-pipeline.md` — stale form-rubric path, stale Current State, a Process-Rule-1-violating `_index` upkeep step.
- **`skill-authoring-guide.md` slimmed** (`7d8c933`): reduced to a SKILL.md *mechanics* reference; design content now owned by `librarian/skill.md` §Construction + `/design-skill`.
- **extracts↔knowledge design-note** (`adba869`): live-vs-orphaned audit → **guides 14/14 live (Tier-1 Librarian substrate, not staging)**, patterns Tier-2 (browsed by dimension, ~10% slug-pinned), rules/skills/templates/agents = staging residue (~5% pinned). Reframes `extracts/` (research substrate) vs `knowledge/` (engine self-knowledge) as two bodies, not two pipeline stages. Recommends recognize-substrate-in-place (1a) + a scoped promote-or-prune of the ~121-file residue. IB-170 updated with session progress + next gate. Note: `2026-06-20-extracts-knowledge-reconciliation.md`.
- **Not yet pushed:** 10 commits ahead of `origin/main` (the 4 above + 6 prior incl. session-122 close `b1e7585`).

### Open gates carried forward (Nick's call)
- extracts↔knowledge model: **1a rename-in-place** (recommended) vs **1b relocate** `guides/`+`patterns/`; staging-residue promote-or-prune.
- IB-170 concept-doc placement — follows the substrate decision.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

1. **`[next]` Governance-health audit + knowledge-caching coverage (session 125).** Two phases, gate between: (1) read-only DD coherence + DD↔IB↔git mapping (via `/governance-audit`, `/system-audit`) → governance-health report → gated hygiene fixes; (2) propose-only knowledge-coverage map + caching-policy recommendation (include/exclude criteria, Owner-vs-Librarian wiring; no writes — Rule 11). Handoff: `operations/handoffs/handoff-prompt-session-125-governance-health-caching-audit.md`.
2. **`[nick-gate]` extracts↔knowledge model + IB-170.** Decide 1a rename-in-place (recommended) vs 1b relocate the substrate (`guides/`+`patterns/`); promote-or-prune the ~121-file staging residue; then the concept-doc placement (IB-170) follows. Design-note: `project-management/design-notes/2026-06-20-extracts-knowledge-reconciliation.md`.
3. **Phase 2 — schematics + evaluation/feedback layer** (gated slices; plan of record: `project-management/design-notes/2026-06-18-engine-collapse-restructure-plan.md` §Phase 2).
   - ✅ **Slices 1–2 (sessions 120–121):** schematic form (DD-107) + `/detect-drift` integration.
   - ✅ **Item 2 (session 122):** D7/D9 → schematic re-evaluation wiring made explicit; schematics as `/solicit-proposals` input.
   - ✅ **Item 3 (session 122):** 2 seed schematics (`project-coding-workcell`, `scheduled-operations-assistant`).
   - **`[deferred]` Item 4 — Builder-mode demand→schematic matching** (`/ask-kb`) — now more plausible with a 4-seed library; revisit when exercising it is useful.
   - **`[deferred]` Execution-surface Librarian axis** — weak demand per consumer-abstractions-map (Rule 11); revisit at 2–3+ requests.
   - **`[trigger]` More seed schematics** — when exercising the form against more demand is useful.
4. **`[deferred]` Ready maintenance** — IB-145 (re-analyze GSD for version drift) and IB-148 (build `/session-handoff-review`). Self-contained; pick up when the queue clears.

---

## Logged-for-future

Trigger-gated carryover. Don't action unless trigger fires.

1. Place the engine on an actual harness, not just relying on the agent to invoke the right skills in the right order every time. (Aligns with the supervised-autonomy trajectory in DD-108 — URLs-in / queries-in under Nick's oversight.)
2. **`[deferred]` G3 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-architecture-decisions-split-proposal.md`. At 42 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45.
3. **`[deferred]` G9 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-governance-and-trust-split-proposal.md`. At 38 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45 or enforcement cluster hits 10.
