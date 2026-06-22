# Improvement Loop — Progress

**Last Updated:** 2026-06-22 (session 128 closed → 129 handoff)

## Current Focus

**The engine collapse is fully landed on `main`.** The `engine-collapse-phase-1` branch was merged (`--no-ff`, `199a6ee`), pushed to `origin/main`, and deleted — **`main` is now the live line.** The federation collapsed into one self-evolving engine (Household OS → Notion, Claude Build retired, `meta-system` shell dissolved); the engine is fractal-complete with three altitudes (research → per-artifact assess/design → whole-system composition) and a root-level `CHARTER.md`.

**Phase 2 progress.** Slices 1–2 (sessions 120–121) defined the **schematic** form (DD-107) and brought it into `/detect-drift`. Session 122 finished **§Phase 2 item 2** (made the Dimension 7/9 → schematic re-evaluation wiring explicit; added schematics as a `/solicit-proposals` reflection input) and **item 3** (two consumer-facing seed schematics — `project-coding-workcell`, `scheduled-operations-assistant`; the library now spans research/operations/audit/coding, 4 seeds, `/detect-drift` clean). Remaining Phase-2 items stay demand-gated (execution-surface axis, Builder-mode matching).

**First `/system-audit` (session 122)** ran post-collapse: 0 Critical, structurally sound. All findings remediated this session — **DD-108** (Owner files DDs as mechanics; Nick gates content), **DD-109** (re-home system-scoped-skills / skills-as-atomic-unit into live governance), agent + skill contract fixes, post-collapse framing fixes, and all 148 system-log entries normalized to canonical `date:`. Report: `operations/audit-reports/2026-06-18-system-audit.md`.

**Session 123 (governance hygiene + audit-home disambiguation) landed.** The stale-IB sweep cleared 15 post-collapse items; the open backlog is now small and engine-relevant. IB-169 was resolved by **DD-110** — the two audits (`/audit-artifacts`, renamed from `/audit-system`, and `/system-audit`) were disambiguated, not consolidated, with both homes moved under `operations/`. Post-collapse "MetaSystem vs IL" framing was reconciled to the one-engine three-altitude model and the two consumer-abstractions maps merged into one.

**Session 125 (governance-health + knowledge-caching) landed.** Phase 1: the DD/IB corpus is structurally sound (no contradictions, all 9 supersessions now machine-traceable, all live-era DDs commit-backed). Applied four gated hygiene fixes (stale superseded-list removal from CLAUDE.md; canonical `supersedes` backfill; DD-49→DD-109 annotations; IB-102/IB-145 re-anchor). Phase 2 (propose-only): the caching question resolved decisively — **~88% of DD wisdom is correctly *not* separately cached** (governance fact or operationalized in one owning skill). Delivered a four-part selection test + exclusion rules + anti-redundancy invariant; cached DD-wisdom is Owner-owned; no cache-every-DD mechanism (Rule 11). Reports: `operations/system-audits/2026-06-21-governance-health-audit.md`, `project-management/design-notes/2026-06-21-dd-wisdom-caching-policy.md`.

**Session 126 (knowledge-architecture sweep) landed (`867e2a7`, pushed).** All four tasks executed: DD-37's five principles cached into `governance/agent-rules.md`; `principles.md` → `dbdo-pipeline.md` (re-anchored DD-45→DD-103, de-federated). **DD-111** recognizes `extracts/guides`+`extracts/patterns` as Librarian substrate (amends DD-39/DD-80, rename-in-place); the residue (`rules/skills/templates/agents`, ~123 files) is designated an explicit **harvest archive** (external best-practice, not engine artifacts; no moves/deletes). **DD-112** + **IB-170 resolved**: concept-doc home rule (`knowledge/reference/` = self-knowledge; `operations/references/` = operational reference incl. all concept docs); `harness.md` relocated to `librarian/`, runtime-sense → `runtime-environment.md`. `ib_items` normalized (YAML list; DD-43's 9 dead URLs → real back-refs).

**Session 127 (sweep-residuals + in-round YAML hygiene sweep) landed (`011fa8c`, `574f0f7`, `169ba98`, pushed).** Both session-126 residuals closed, then the frontmatter/YAML hygiene sweep was pulled forward and run in-round. (1) **Harness whole-system invariants confirmed deferred** per Rule 11 — evidence test unmet; dated note in `harness.md` §Composition, no backfill. (2) **DD-113: DD↔IB linkage forward-only via `source_dd`** (option B1) — uniform YAML list across 63 IBs, 4 non-lossy reconciliations, `ib_items` removed from 81 DDs, `_schema.yaml` + `/dd`/`/track`/`/governance-audit` repointed, reverse view query-derived. (3) **Frontmatter/YAML hygiene sweep** — full-corpus PyYAML scan found **40 parse failures** (3 classes: unquoted prose scalars with `: `, mixed-indent lists, multi-line scalars with colon-in-continuation); a field-aware fixer rewrote only the offending field per file (block scalars / normalized lists, content verbatim); 0 failures remain; 4 findings backfilled `pipeline_status: raw`; schema-conformance otherwise clean.

**Session 128 (upstream YAML prevention + foundations spine + PROGRESS consolidation) landed (`4ce12d9`, `d799777`, pushed).** (1) **DD-114** — upstream frontmatter/YAML prevention: block-scalar authoring convention added to the 7 producers that hand-write frontmatter (`research-loop`, `research-query`, `promote-findings`, `watch-blogs`, `/sl`, `/dd`, `/ib`); new `validate_frontmatter.py` + git pre-commit hook (binary YAML-parse check; distinct from the removed heuristic read-guard). Nick chose option a+c; `kb_parser` verified load-bearing (not removed). (2) **DD-115** — `governance/FOUNDATIONS.md`, a generated spine map of the ~20 foundational DDs: tagged `foundational: true`, `generate_foundations.py` (+`--check`), CLAUDE.md pointers (referenced, not inlined — DD-74), pre-commit staleness check; inclusion/exclusion criteria (C1–C5 / X1–X5 + ~20 displacement cap) codified to guard drift. (3) The `il-published` subtree mirror (DD-84) was ~2 months stale; refreshed via `git subtree push` (`511b147`). (4) **PROGRESS consolidation** — the vestigial root `PROGRESS.md` (stale since session 118) reduced to a pointer; this IL file is the single canonical PROGRESS; `/session-handoff` patched to target it unambiguously.

**Active focus / next session (129):** **agent-vs-skill workflow — discuss/design first, gate before building.** Design the create/update-an-agent workflow and the agent-vs-skill-vs-something-else decision (stress-test whether that's the right axis); then reconcile the `knowledge/` "policy masquerading as patterns" docs (seed: `knowledge/patterns/capability-type-selection.md`) and revisit DD-109. Handoff: `operations/handoffs/handoff-prompt-session-129-agent-vs-skill.md`. **Open for Nick:** fold the subtree publish into session-close (mirror keeps drifting) or retire the mirror.

---

## What Changed This Session (128)

Upstream YAML prevention, the foundations spine map, the mirror refresh, and PROGRESS consolidation (Nick gated each decision; mechanics ran freely). Commits `4ce12d9`, `d799777` — pushed; mirror `511b147`; session-close commit local.

- **DD-114 — upstream frontmatter/YAML prevention:** traced the producers (every active intake/governance skill hand-writes frontmatter with inline quoted prose scalars — the session-127 defect source; `kb_parser.write_frontmatter` uses `yaml.dump` and was never the culprit). Added a block-scalar authoring convention to `_schema.yaml` and the 7 producers; built `validate_frontmatter.py` + a tracked git pre-commit hook (binary YAML-parse check). Nick authorized option a (convention) + c (linter). Verified `kb_parser` is load-bearing (3 importers) and `write_frontmatter` is intentionally retained — no cleanup.
- **DD-115 — FOUNDATIONS.md generated spine map:** ran a 3-lens Perplexity council (architect/maintainer/skeptic) → generated view over canonical DDs, never a hand-authored digest. Tagged 20 spine DDs `foundational: true`; `generate_foundations.py` (+`--check`) emits `governance/FOUNDATIONS.md`; pointers from both CLAUDE.md files; pre-commit extended with a staleness check. Nick asked for explicit anti-drift criteria → codified the litmus test + C1–C5 include-roles + X1–X5 exclude-rules + the ~20 displacement cap, in DD-115 and the FOUNDATIONS header.
- **Mirror refresh:** diagnosed the "no updates in 2 months" report — it was the `il-published` mirror (`nickgogan/improvement-loop`, DD-84 manual subtree mirror), not the live `origin`/MetaSystem repo. Refreshed via `git subtree push` (`7ded114..511b147`).
- **PROGRESS consolidation:** discovered the root `PROGRESS.md` was a stale duplicate (untouched since session 118); this IL file is canonical. Migrated the still-live carryover from root (Logged-for-future items + the MongoDB sizing-engine pilot), reduced root to a pointer, and patched `/session-handoff` to target the system PROGRESS unambiguously.

### Surfaced this session (carried to session 129)
- **Agent-vs-skill workflow** is the next topic; `knowledge/patterns/capability-type-selection.md` is the seed (policy-in-disguise) and DD-109 is revisited there.
- **Mirror drift** — decide whether to automate the subtree push at session-close or retire the mirror.
- Watch-only: DD-62 (Explore/Harden), DD-74 (token budget) — future cache candidates, wait for recurring demand.

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

1. **`[next]` Agent-vs-skill workflow (session 129) — discuss/design first, gate before building.** Design the create/update-an-agent workflow and the agent-vs-skill-vs-something-else decision; stress-test whether that's even the right axis. Then reconcile the `knowledge/` "policy masquerading as patterns" docs (seed: `knowledge/patterns/capability-type-selection.md`; siblings: `research-to-codification-pipeline.md`, `upstream-dependency-spectrum.md`) and revisit **DD-109**. Handoff: `operations/handoffs/handoff-prompt-session-129-agent-vs-skill.md`.
   - ✅ **Upstream YAML prevention (session 128) — DONE:** DD-114 (block-scalar convention in 7 producers + `validate_frontmatter.py` + pre-commit hook); `kb_parser` verified load-bearing (`4ce12d9`).
   - ✅ **FOUNDATIONS.md spine map (session 128) — DONE:** DD-115 (20 DDs tagged; `generate_foundations.py`; criteria codified; CLAUDE.md pointers; staleness check) (`d799777`).
   - ✅ **Frontmatter/YAML hygiene sweep (session 127) — DONE:** 40 parse failures fixed corpus-wide; 0 remain (`169ba98`).
   - ✅ **Sweep-residuals cleanup (session 127) — DONE:** DD-113 (forward-only DD↔IB linkage via `source_dd`); `ib_items` retired from 81 DDs (`011fa8c`).
   - ✅ **Knowledge-architecture sweep (session 126) — DONE:** DD-111, DD-112; IB-170 resolved; DD-37 cached (`867e2a7`).
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
4. **`[trigger: /design-harness ships]` MongoDB sizing-engine — pilot consumer for `/design-harness`.** Real project: a comparison harness across Excel calculator + SAGE + consulting tool, with forecasting layered on top for sales-leader cost modeling. Architecture validated session 113 via Librarian (Variant B+C; single orchestrating agent + deterministic adapters; forecasting as a separate agent on the comparison output; LLM never does the math). Locked: deviation semantics TBD (Nick to draft a 1-page spec); empirical-vs-theoretical = surface both with labels; forecasting separate; determinism boundary at the adapter layer. Run `/design-harness` against this as the first canonical pilot once it ships. (Migrated from root PROGRESS, session 128.)
5. **Six Memongo improvement surfaces** — captured in `watched-libraries/memongo.md`; forward-looking work for Nick's own code. (Migrated from root PROGRESS.)
6. **Add JR and a colleague as GitHub collaborators** — `[trigger]` needs usernames. Relevant to sharing the `il-published` mirror. (Migrated from root PROGRESS.)
7. **Obsidian Workspaces plugin configuration** — `[trigger]` requires Obsidian UI. (Migrated from root PROGRESS.)
8. **Dataview plugin installation** — `[trigger]` requires Obsidian UI; enables the live-view `_index.md` files governance Process Rule 1 permits. (Migrated from root PROGRESS.)
9. **Temp directory cleanup** — `/tmp/metasystem-repo-cache/` (and `watched-libraries/_tmp/repo-cache/`); `/cleanup-cache` covers the latter. (Migrated from root PROGRESS.)
