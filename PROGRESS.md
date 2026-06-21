# Improvement Loop — Progress

**Last Updated:** 2026-06-21 (session 125)

## Current Focus

**The engine collapse is fully landed on `main`.** The `engine-collapse-phase-1` branch was merged (`--no-ff`, `199a6ee`), pushed to `origin/main`, and deleted — **`main` is now the live line.** The federation collapsed into one self-evolving engine (Household OS → Notion, Claude Build retired, `meta-system` shell dissolved); the engine is fractal-complete with three altitudes (research → per-artifact assess/design → whole-system composition) and a root-level `CHARTER.md`.

**Phase 2 progress.** Slices 1–2 (sessions 120–121) defined the **schematic** form (DD-107) and brought it into `/detect-drift`. Session 122 finished **§Phase 2 item 2** (made the Dimension 7/9 → schematic re-evaluation wiring explicit; added schematics as a `/solicit-proposals` reflection input) and **item 3** (two consumer-facing seed schematics — `project-coding-workcell`, `scheduled-operations-assistant`; the library now spans research/operations/audit/coding, 4 seeds, `/detect-drift` clean). Remaining Phase-2 items stay demand-gated (execution-surface axis, Builder-mode matching).

**First `/system-audit` (session 122)** ran post-collapse: 0 Critical, structurally sound. All findings remediated this session — **DD-108** (Owner files DDs as mechanics; Nick gates content), **DD-109** (re-home system-scoped-skills / skills-as-atomic-unit into live governance), agent + skill contract fixes, post-collapse framing fixes, and all 148 system-log entries normalized to canonical `date:`. Report: `operations/audit-reports/2026-06-18-system-audit.md`.

**Session 123 (governance hygiene + audit-home disambiguation) landed.** The stale-IB sweep cleared 15 post-collapse items; the open backlog is now small and engine-relevant. IB-169 was resolved by **DD-110** — the two audits (`/audit-artifacts`, renamed from `/audit-system`, and `/system-audit`) were disambiguated, not consolidated, with both homes moved under `operations/`. Post-collapse "MetaSystem vs IL" framing was reconciled to the one-engine three-altitude model and the two consumer-abstractions maps merged into one.

**Session 125 (governance-health + knowledge-caching) landed.** Phase 1: the DD/IB corpus is structurally sound (no contradictions, all 9 supersessions now machine-traceable, all live-era DDs commit-backed). Applied four gated hygiene fixes (stale superseded-list removal from CLAUDE.md; canonical `supersedes` backfill; DD-49→DD-109 annotations; IB-102/IB-145 re-anchor). Phase 2 (propose-only): the caching question resolved decisively — **~88% of DD wisdom is correctly *not* separately cached** (governance fact or operationalized in one owning skill). Delivered a four-part selection test + exclusion rules + anti-redundancy invariant; cached DD-wisdom is Owner-owned; no cache-every-DD mechanism (Rule 11). Reports: `operations/system-audits/2026-06-21-governance-health-audit.md`, `project-management/design-notes/2026-06-21-dd-wisdom-caching-policy.md`.

**Active focus / next session (126):** **knowledge-architecture sweep** (Nick chose "all of these", execution allowed, gate content). Dependency order: (1) execute the caching-policy gates — DD-37's five principles → CLAUDE.md/agent-rules; fix `principles.md` drift (rename → `dbdo-pipeline.md`, re-anchor DD-45→DD-103, de-federate diagram); (2) extracts↔knowledge model choice (1a vs 1b) + promote-or-prune the ~121-file staging residue; (3) IB-170 concept-doc rationalization (follows the substrate decision); (4) held item F (normalize/retire `ib_items` reverse-link). Handoff: `operations/handoffs/handoff-prompt-session-126-knowledge-architecture-sweep.md`.

---

## What Changed This Session (125)

A two-phase governance-health + knowledge-caching audit, gate between phases.

- **Phase 1 — governance-health fixes** (`b113c8d`, pushed): DD/IB corpus is structurally sound — no contradictions, no filename/id mismatches, every Superseded DD resolves to a Binding decision, every live-era DD commit-backed. Applied four Nick-approved hygiene fixes: (A) removed the stale "Superseded: DD-35/43/48" hardcoded list from `CLAUDE.md` → status-filter instruction; (B) backfilled the schema-canonical `supersedes` field on DD-45 (→DD-43) and DD-57 (→DD-48), so all 9 supersessions are machine-traceable (DD-65 piecewise per its body); (C) annotated 8 live-DD citations of archived **DD-49** with "→ DD-109" (its re-home); (D) re-pointed IB-102 source_dd DD-35→DD-104 and nulled IB-145's stale DD-45 (kept Queued). Held: F (`ib_items` normalization). Report: `operations/system-audits/2026-06-21-governance-health-audit.md`.
- **Phase 2 — DD-wisdom caching policy** (`0b6d480`, pushed, propose-only): coverage map + selection criteria + Owner/Librarian wiring. **Headline: ~88% of DD wisdom is correctly NOT separately cached** (governance fact, or operationalized in one owning skill — the remedy there is *the skill cites its source DD*, not a parallel `knowledge/` copy). Four-part selection test (cross-cutting / reference-shaped / engine-self-knowledge / stable) + exclusion rules + anti-redundancy invariant (cached docs must anchor to a **Binding** DD and be the single home). **Cached DD-wisdom is Owner-owned** — no new agent surface. Genuine gap: **DD-37**'s five foundational principles, cached nowhere. Drift found: `knowledge/reference/principles.md` is mislabeled (it's the DBDO pipeline), anchored to **Superseded DD-45**, and still diagrams the dead federation. DD-62/DD-74 = watch, don't act. Note: `project-management/design-notes/2026-06-21-dd-wisdom-caching-policy.md`.
- **Stale handoff warning corrected:** the session-124 "10 unpushed commits" note was already resolved — `main` was in sync at start; session 125's 2 commits are now also pushed.

### Open gates carried forward (Nick's call → session 126 sweep)
- Caching-policy gates: DD-37 → CLAUDE.md/agent-rules; fix `principles.md` drift (rename → `dbdo-pipeline.md`, re-anchor DD-45→DD-103, de-federate).
- extracts↔knowledge model: **1a rename-in-place** (recommended) vs **1b relocate**; staging-residue promote-or-prune (~121 files).
- IB-170 concept-doc placement — follows the substrate decision.
- Held item F — `ib_items` reverse-link normalization/retirement.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

1. **`[next]` Knowledge-architecture sweep (session 126).** Nick chose "all of these," dependency order: (a) execute caching-policy gates — DD-37 → CLAUDE.md/agent-rules; fix `principles.md` drift (rename → `dbdo-pipeline.md`, re-anchor DD-45→DD-103, de-federate); (b) extracts↔knowledge 1a/1b + promote-or-prune the ~121-file residue; (c) IB-170 concept-doc rationalization (follows b); (d) held item F (`ib_items` normalization). Handoff: `operations/handoffs/handoff-prompt-session-126-knowledge-architecture-sweep.md`. Inputs: caching-policy note (`2026-06-21-dd-wisdom-caching-policy.md`) + reconciliation note (`2026-06-20-extracts-knowledge-reconciliation.md`).
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
