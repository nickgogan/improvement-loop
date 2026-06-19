# Improvement Loop — Progress

**Last Updated:** 2026-06-19 (session 122)

## Current Focus

**The engine collapse is fully landed on `main`.** The `engine-collapse-phase-1` branch was merged (`--no-ff`, `199a6ee`), pushed to `origin/main`, and deleted — **`main` is now the live line.** The federation collapsed into one self-evolving engine (Household OS → Notion, Claude Build retired, `meta-system` shell dissolved); the engine is fractal-complete with three altitudes (research → per-artifact assess/design → whole-system composition) and a root-level `CHARTER.md`.

**Phase 2 progress.** Slices 1–2 (sessions 120–121) defined the **schematic** form (DD-107) and brought it into `/detect-drift`. Session 122 finished **§Phase 2 item 2** (made the Dimension 7/9 → schematic re-evaluation wiring explicit; added schematics as a `/solicit-proposals` reflection input) and **item 3** (two consumer-facing seed schematics — `project-coding-workcell`, `scheduled-operations-assistant`; the library now spans research/operations/audit/coding, 4 seeds, `/detect-drift` clean). Remaining Phase-2 items stay demand-gated (execution-surface axis, Builder-mode matching).

**First `/system-audit` (session 122)** ran post-collapse: 0 Critical, structurally sound. All findings remediated this session — **DD-108** (Owner files DDs as mechanics; Nick gates content), **DD-109** (re-home system-scoped-skills / skills-as-atomic-unit into live governance), agent + skill contract fixes, post-collapse framing fixes, and all 148 system-log entries normalized to canonical `date:`. Report: `operations/audit-reports/2026-06-18-system-audit.md`.

**Active focus / next session (123):** **governance & backlog hygiene** — sweep stale post-collapse IB items (several still reference the dissolved meta-system / retired Claude Build), reconcile remaining drift, re-sequence this priority queue. Execution scope. See `operations/handoffs/handoff-prompt-session-123-governance-hygiene.md`.

---

## What Changed This Session (122)

- **Phase 2 item 2 finished** (`72af64c`, `ef59068`): made the Dimension 7 (Evaluation) / Dimension 9 (Governance) → schematic re-evaluation wiring explicit in `schematics/_index.md` + `research-dimensions.md`; added a "schematic currency" check to the `/solicit-proposals` reflection prompt.
- **Phase 2 item 3 — two seed schematics** (`78c8c24`): `project-coding-workcell` (top) and `scheduled-operations-assistant` (middle), consumer-facing blueprints the engine designs but doesn't run. 14 groundings resolve; `/detect-drift` clean on 4 schematics.
- **First post-collapse `/system-audit`** (`0ad7897`): 0 Critical; baseline report written.
- **Audit fully remediated** (`24c0302`, `e0aec07`, `6392510`, `2ab8f79`, `26cc968`, `0224035`): agent + skill contract drift; post-collapse framing in governance/CLAUDE.md; **DD-108** (Owner DD-authority reconciliation); **DD-109** (re-home DD-49/DD-34 conventions); all 148 SL entries normalized to canonical `date:`; **IB-169** filed for the audit-report-homes question. All pushed to `origin/main`.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

1. **`[next]` Governance & backlog hygiene (session 123).** Sweep stale post-collapse IB items (candidates flagged session 122: IB-136, IB-137, IB-142, IB-146, IB-147, IB-167, IB-168 — meta-system / Claude-Build-era; verify each and mark Done/superseded or rewrite for the single engine), reconcile remaining drift, re-sequence this queue. Execution scope. Handoff: `operations/handoffs/handoff-prompt-session-123-governance-hygiene.md`.
2. **Phase 2 — schematics + evaluation/feedback layer** (gated slices; plan of record: `project-management/design-notes/2026-06-18-engine-collapse-restructure-plan.md` §Phase 2).
   - ✅ **Slices 1–2 (sessions 120–121):** schematic form (DD-107) + `/detect-drift` integration.
   - ✅ **Item 2 (session 122):** D7/D9 → schematic re-evaluation wiring made explicit; schematics as `/solicit-proposals` input.
   - ✅ **Item 3 (session 122):** 2 seed schematics (`project-coding-workcell`, `scheduled-operations-assistant`).
   - **`[deferred]` Item 4 — Builder-mode demand→schematic matching** (`/ask-kb`) — now more plausible with a 4-seed library; revisit when exercising it is useful.
   - **`[deferred]` Execution-surface Librarian axis** — weak demand per consumer-abstractions-map (Rule 11); revisit at 2–3+ requests.
   - **`[trigger]` More seed schematics** — when exercising the form against more demand is useful.
3. **`[nick-gate]` IB-169 — consolidate the two audit-report homes** (`/audit-system` → `audit-reports/` vs `/system-audit` → `operations/audit-reports/`). Discuss-first (P3); Nick to settle.

---

## Logged-for-future

Trigger-gated carryover. Don't action unless trigger fires.

1. Place the engine on an actual harness, not just relying on the agent to invoke the right skills in the right order every time. (Aligns with the supervised-autonomy trajectory in DD-108 — URLs-in / queries-in under Nick's oversight.)
2. **`[deferred]` G3 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-architecture-decisions-split-proposal.md`. At 42 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45.
3. **`[deferred]` G9 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-governance-and-trust-split-proposal.md`. At 38 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45 or enforcement cluster hits 10.
