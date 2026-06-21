# Improvement Loop — Progress

**Last Updated:** 2026-06-21 (session 126)

## Current Focus

**The engine collapse is fully landed on `main`.** The `engine-collapse-phase-1` branch was merged (`--no-ff`, `199a6ee`), pushed to `origin/main`, and deleted — **`main` is now the live line.** The federation collapsed into one self-evolving engine (Household OS → Notion, Claude Build retired, `meta-system` shell dissolved); the engine is fractal-complete with three altitudes (research → per-artifact assess/design → whole-system composition) and a root-level `CHARTER.md`.

**Phase 2 progress.** Slices 1–2 (sessions 120–121) defined the **schematic** form (DD-107) and brought it into `/detect-drift`. Session 122 finished **§Phase 2 item 2** (made the Dimension 7/9 → schematic re-evaluation wiring explicit; added schematics as a `/solicit-proposals` reflection input) and **item 3** (two consumer-facing seed schematics — `project-coding-workcell`, `scheduled-operations-assistant`; the library now spans research/operations/audit/coding, 4 seeds, `/detect-drift` clean). Remaining Phase-2 items stay demand-gated (execution-surface axis, Builder-mode matching).

**First `/system-audit` (session 122)** ran post-collapse: 0 Critical, structurally sound. All findings remediated this session — **DD-108** (Owner files DDs as mechanics; Nick gates content), **DD-109** (re-home system-scoped-skills / skills-as-atomic-unit into live governance), agent + skill contract fixes, post-collapse framing fixes, and all 148 system-log entries normalized to canonical `date:`. Report: `operations/audit-reports/2026-06-18-system-audit.md`.

**Session 123 (governance hygiene + audit-home disambiguation) landed.** The stale-IB sweep cleared 15 post-collapse items; the open backlog is now small and engine-relevant. IB-169 was resolved by **DD-110** — the two audits (`/audit-artifacts`, renamed from `/audit-system`, and `/system-audit`) were disambiguated, not consolidated, with both homes moved under `operations/`. Post-collapse "MetaSystem vs IL" framing was reconciled to the one-engine three-altitude model and the two consumer-abstractions maps merged into one.

**Session 125 (governance-health + knowledge-caching) landed.** Phase 1: the DD/IB corpus is structurally sound (no contradictions, all 9 supersessions now machine-traceable, all live-era DDs commit-backed). Applied four gated hygiene fixes (stale superseded-list removal from CLAUDE.md; canonical `supersedes` backfill; DD-49→DD-109 annotations; IB-102/IB-145 re-anchor). Phase 2 (propose-only): the caching question resolved decisively — **~88% of DD wisdom is correctly *not* separately cached** (governance fact or operationalized in one owning skill). Delivered a four-part selection test + exclusion rules + anti-redundancy invariant; cached DD-wisdom is Owner-owned; no cache-every-DD mechanism (Rule 11). Reports: `operations/system-audits/2026-06-21-governance-health-audit.md`, `project-management/design-notes/2026-06-21-dd-wisdom-caching-policy.md`.

**Session 126 (knowledge-architecture sweep) landed (`867e2a7`, pushed).** All four tasks executed: DD-37's five principles cached into `governance/agent-rules.md`; `principles.md` → `dbdo-pipeline.md` (re-anchored DD-45→DD-103, de-federated). **DD-111** recognizes `extracts/guides`+`extracts/patterns` as Librarian substrate (amends DD-39/DD-80, rename-in-place); the residue (`rules/skills/templates/agents`, ~123 files) is designated an explicit **harvest archive** (external best-practice, not engine artifacts; no moves/deletes). **DD-112** + **IB-170 resolved**: concept-doc home rule (`knowledge/reference/` = self-knowledge; `operations/references/` = operational reference incl. all concept docs); `harness.md` relocated to `librarian/`, runtime-sense → `runtime-environment.md`. `ib_items` normalized (YAML list; DD-43's 9 dead URLs → real back-refs).

**Active focus / next session (127):** **sweep-residuals cleanup** (execution allowed, gate content + push). Two judgment-call residuals from session 126: (1) the **Rule-12 §Composition debt** on the whole-system `harness.md` — apply the Rule-11 evidence test (add whole-system invariants only if evidence warrants; "confirm deferred" is a valid outcome); (2) the **`ib_items`/`source_dd` asymmetry** — `source_dd` is scalar and under-captures multi-DD links; decide retire-`ib_items` vs make-`source_dd`-a-list vs leave-as-is. Handoff: `operations/handoffs/handoff-prompt-session-127-sweep-residuals-cleanup.md`.

---

## What Changed This Session (126)

A four-task knowledge-architecture sweep (Nick gated each decision; mechanics ran freely). One commit `867e2a7`, pushed.

- **Task 1 — DD-37 cached + DBDO-pipeline drift fixed:** folded DD-37's five foundational design principles into `governance/agent-rules.md` as a constitution-altitude preamble; renamed `knowledge/reference/principles.md` → `dbdo-pipeline.md` (it was the DBDO pipeline, mislabeled), re-anchored `source_dd` DD-45(Superseded)→DD-103, de-federated the feedback-loop diagram, repointed live consumers (`pipeline-rules.md`, `translate-governance` SKILL, `_index.md`).
- **Task 2 — extracts substrate framing (DD-111, rename-in-place):** `extracts/guides`+`extracts/patterns` recognized as the Librarian's substrate library (amends DD-39/DD-80, zero file moves). The staging residue (`rules/skills/templates/agents`, ~123 files) designated an explicit **harvest archive** — distilled external best-practice, not engine artifacts; promotion is per-item Nick-gated (DD-29). No moves, no deletes.
- **Task 3 — concept-doc home rule (DD-112, resolves IB-170):** `knowledge/reference/` = engine self-knowledge; `operations/references/` = operational reference incl. all concept docs. Relocated `harness.md` → `operations/references/librarian/` (whole-system unit); renamed the runtime-sense doc → `runtime-environment.md`; repointed `consumer-abstractions-map.md` (×4) + both `_index.md` files. Agent-helper-files question: no change (Rule 11).
- **Task 4 — `ib_items` normalized:** standardized to YAML list; DD-43's 9 dead Notion URLs → real `source_dd` back-refs (IB-113…121); dropped non-existent refs (IB-140/141/143); nulled DD-54/DD-64. *Residual:* the forward(`source_dd` scalar)/reverse(`ib_items`) asymmetry remains by design (Nick chose normalize, not retire).

### Open residuals carried forward (Nick's call → session 127)
- **Rule-12 §Composition debt** on the whole-system `harness.md` — apply the Rule-11 evidence test; "confirm deferred" is a valid outcome.
- **`ib_items`/`source_dd` asymmetry** — retire `ib_items` (adopt `source_dd` SSOT) vs make `source_dd` a list vs leave-as-is.
- Watch-only: DD-62 (Explore/Harden), DD-74 (token budget) — future cache candidates, wait for recurring demand.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

1. **`[next]` Sweep-residuals cleanup (session 127).** Two judgment-call residuals from the session-126 sweep (execution allowed, gate content + push): (a) the **Rule-12 §Composition debt** on the whole-system `harness.md` (`operations/references/librarian/harness.md`) — apply the Rule-11 evidence test; adding whole-system invariants only if warranted, "confirm deferred" a valid outcome; (b) the **`ib_items`/`source_dd` asymmetry** — `source_dd` is scalar and under-captures multi-DD links; decide retire-`ib_items` (adopt `source_dd` SSOT) vs make-`source_dd`-a-list vs leave-as-is. Handoff: `operations/handoffs/handoff-prompt-session-127-sweep-residuals-cleanup.md`. Context: DD-111, DD-112 (session 126).
   - ✅ **Knowledge-architecture sweep (session 126) — DONE:** DD-111, DD-112 filed; IB-170 resolved; DD-37 cached; `dbdo-pipeline.md` drift fixed; `ib_items` normalized (`867e2a7`).
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
