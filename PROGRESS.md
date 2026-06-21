# Improvement Loop — Progress

**Last Updated:** 2026-06-21 (session 127)

## Current Focus

**The engine collapse is fully landed on `main`.** The `engine-collapse-phase-1` branch was merged (`--no-ff`, `199a6ee`), pushed to `origin/main`, and deleted — **`main` is now the live line.** The federation collapsed into one self-evolving engine (Household OS → Notion, Claude Build retired, `meta-system` shell dissolved); the engine is fractal-complete with three altitudes (research → per-artifact assess/design → whole-system composition) and a root-level `CHARTER.md`.

**Phase 2 progress.** Slices 1–2 (sessions 120–121) defined the **schematic** form (DD-107) and brought it into `/detect-drift`. Session 122 finished **§Phase 2 item 2** (made the Dimension 7/9 → schematic re-evaluation wiring explicit; added schematics as a `/solicit-proposals` reflection input) and **item 3** (two consumer-facing seed schematics — `project-coding-workcell`, `scheduled-operations-assistant`; the library now spans research/operations/audit/coding, 4 seeds, `/detect-drift` clean). Remaining Phase-2 items stay demand-gated (execution-surface axis, Builder-mode matching).

**First `/system-audit` (session 122)** ran post-collapse: 0 Critical, structurally sound. All findings remediated this session — **DD-108** (Owner files DDs as mechanics; Nick gates content), **DD-109** (re-home system-scoped-skills / skills-as-atomic-unit into live governance), agent + skill contract fixes, post-collapse framing fixes, and all 148 system-log entries normalized to canonical `date:`. Report: `operations/audit-reports/2026-06-18-system-audit.md`.

**Session 123 (governance hygiene + audit-home disambiguation) landed.** The stale-IB sweep cleared 15 post-collapse items; the open backlog is now small and engine-relevant. IB-169 was resolved by **DD-110** — the two audits (`/audit-artifacts`, renamed from `/audit-system`, and `/system-audit`) were disambiguated, not consolidated, with both homes moved under `operations/`. Post-collapse "MetaSystem vs IL" framing was reconciled to the one-engine three-altitude model and the two consumer-abstractions maps merged into one.

**Session 125 (governance-health + knowledge-caching) landed.** Phase 1: the DD/IB corpus is structurally sound (no contradictions, all 9 supersessions now machine-traceable, all live-era DDs commit-backed). Applied four gated hygiene fixes (stale superseded-list removal from CLAUDE.md; canonical `supersedes` backfill; DD-49→DD-109 annotations; IB-102/IB-145 re-anchor). Phase 2 (propose-only): the caching question resolved decisively — **~88% of DD wisdom is correctly *not* separately cached** (governance fact or operationalized in one owning skill). Delivered a four-part selection test + exclusion rules + anti-redundancy invariant; cached DD-wisdom is Owner-owned; no cache-every-DD mechanism (Rule 11). Reports: `operations/system-audits/2026-06-21-governance-health-audit.md`, `project-management/design-notes/2026-06-21-dd-wisdom-caching-policy.md`.

**Session 126 (knowledge-architecture sweep) landed (`867e2a7`, pushed).** All four tasks executed: DD-37's five principles cached into `governance/agent-rules.md`; `principles.md` → `dbdo-pipeline.md` (re-anchored DD-45→DD-103, de-federated). **DD-111** recognizes `extracts/guides`+`extracts/patterns` as Librarian substrate (amends DD-39/DD-80, rename-in-place); the residue (`rules/skills/templates/agents`, ~123 files) is designated an explicit **harvest archive** (external best-practice, not engine artifacts; no moves/deletes). **DD-112** + **IB-170 resolved**: concept-doc home rule (`knowledge/reference/` = self-knowledge; `operations/references/` = operational reference incl. all concept docs); `harness.md` relocated to `librarian/`, runtime-sense → `runtime-environment.md`. `ib_items` normalized (YAML list; DD-43's 9 dead URLs → real back-refs).

**Session 127 (sweep-residuals cleanup) landed (`011fa8c`, pushed).** Both session-126 residuals closed. (1) **Harness whole-system invariants confirmed deferred** per Rule 11 — evidence test unmet (`operations/artifact-audits/runs.md` logs one audit, none since collapse); dated note added to `harness.md` §Composition, no backfill. (2) **DD-113 filed: DD↔IB linkage is now forward-only via `source_dd`** (option B1) — `source_dd` converted to uniform YAML list across 63 IB files (conforms to existing schema `array[string]`), 4 non-lossy reconciliations folding prior reverse claims forward, `ib_items` removed from 81 DDs, `_schema.yaml` updated, `/dd`+`/track`+`/governance-audit` repointed. Reverse view now query-derived.

**Active focus / next session (128):** **frontmatter / YAML hygiene sweep** (execution allowed, gate content + push). Seed defect: IB-157's `notes` field fails YAML parse (nested unescaped quotes). Session 127 parse-checked only IB+DD; sweep the rest (findings, sources, authorities, SL, design-notes) for parse failures + schema-conformance drift. Handoff: `operations/handoffs/handoff-prompt-session-128-frontmatter-hygiene-sweep.md`.

---

## What Changed This Session (127)

Two judgment-call residuals from session 126 closed (Nick gated each decision; mechanics ran freely). Commit `011fa8c` (work) + session-close commit, pushed.

- **Task 1 — harness whole-system invariants confirmed deferred (Rule 11):** applied the evidence test (2–3+ audits surfacing the same drift) — unmet. `operations/artifact-audits/runs.md` logs a single audit (session-115); the only other targeted the since-dissolved MetaSystem; none since. The §Composition thinness is correct, not rule-12 debt — `harness.md`'s own rule-12 self-check already reads "substantially satisfied." Added a dated confirmation note to `harness.md` §Composition + SL entry. No backfill.
- **Task 2 — DD-113: DD↔IB linkage made forward-only via `source_dd` (option B1):** evidence was active divergence (IB-147/146 forward→DD-45 while pipeline DDs claimed them in reverse) + schema drift in both fields. `source_dd` rewritten to uniform YAML list across 63 IB files (conforms to the schema's existing `array[string]`); 4 non-lossy reconciliations (IB-142/146/147/170) folded prior reverse claims into the forward link; `ib_items` removed from 81 DDs; `_schema.yaml` updated (SSOT + do-not-reintroduce note); `/dd`, `/track`, `/governance-audit` repointed. Reverse view now query-derived (`rg DD-X` on IB `source_dd`, or `/ib --dd DD-X`).

### Surfaced this session (carried to session 128)
- **IB-157 `notes` YAML parse failure** (pre-existing nested-quote bug) — seed defect for the session-128 frontmatter/YAML hygiene sweep. Only IB+DD were parse-checked; the rest of the corpus is unswept.
- Watch-only: DD-62 (Explore/Harden), DD-74 (token budget) — future cache candidates, wait for recurring demand.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

1. **`[next]` Frontmatter / YAML hygiene sweep (session 128).** Execution allowed, gate content + push. Seed defect: IB-157's `notes` field fails YAML parse (nested unescaped quotes). Session 127 parse-checked only IB+DD (1 failure of 152); sweep the rest (findings, sources, authorities, SL, design-notes, extracts) for parse failures + schema-conformance drift against `_schema.yaml`. Rule 11 governs schema additions. Handoff: `operations/handoffs/handoff-prompt-session-128-frontmatter-hygiene-sweep.md`.
   - ✅ **Sweep-residuals cleanup (session 127) — DONE:** harness invariants confirmed deferred (Rule 11, no backfill); DD-113 filed (forward-only DD↔IB linkage via `source_dd`); `ib_items` retired from 81 DDs; `source_dd` made uniform YAML list across 63 IBs (`011fa8c`).
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
