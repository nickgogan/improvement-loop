---
title: "A2 — Substrate inventory: empirical accumulation surfaces"
type: "resource"
target_system:
  - "improvement-loop"
created: "2026-07-16"
---

# A2 — Substrate Inventory: Empirical Accumulation Surfaces

Mechanical characterization of every surface in the engine that accumulates data over
time (per-session or per-event writes), as design input for the E1 memory-architecture
spec. No design recommendations — inventory only. Snapshot taken 2026-07-16.

---

## 1. `operations/self/` — the shipped self-improve store (IB-176)

The one surface in the engine explicitly designed as a memory system. Four markdown
files plus a gitignored raw-capture buffer, validated by a pre-commit hook.

### 1a. `lessons.md` — append-only lesson store

| Field | Value |
|---|---|
| **What it is** | Operational lessons — failures/gaps with a rule that prevents recurrence |
| **Entry count** | 9 lessons (L-1…L-9), per the 2026-07-13 retro's store-health line; file currently at 97 lines |
| **Schema** | Header: `## L-<seq> · YYYY-MM-DD · high|normal · open|promoted|declined|pruned`. Body fields (all required): **Lesson**, **Owning surface**, **Source**, **Occurrences** (comma-separated dates) |
| **Writer** | `/self-improve` capture mode (event-time append) and the `/session-handoff` lessons-check sweep (session-close). Manual entries possible but not the default path |
| **Cadence** | Event-driven (capture) + session-close (handoff sweep) |
| **Validation** | `store_check.py` (pre-commit hook, check 4) — blocks on malformed headers, missing required fields, non-ascending `L-<seq>`, dangling `Q-<seq>` references |
| **Sample entry** | `## L-1 · 2026-07-13 · high · promoted` — "Skills shipped with autonomous-write defaults violating G9.I6 ... every skill write path needs a default-off flag" — Owning surface: 4 named SKILL.md files — Source: two named System Log entries — Occurrences: `2026-06-12` |

### 1b. `query-log.md` — demand ledger

| Field | Value |
|---|---|
| **What it is** | One row per incoming intent, tracking whether the system could serve it |
| **Entry count** | 1 row (Q-1) as of the 2026-07-13 retro; file at 23 lines |
| **Schema** | 6-column markdown table: `Seq \| Date \| Query gist \| Route \| Why \| Outcome`. Outcome ∈ `served \| partial \| unserved` |
| **Writer** | `/self-improve` scan mode distills the raw capture buffer (`.query-capture.jsonl`) into rows here; not written directly |
| **Cadence** | Periodic (scan-mode runs), sourced from a per-prompt raw buffer |
| **Sample entry** | `Q-1 \| 2026-07-13 \| "continue" — proceed with next unit of work \| PROGRESS.md wake-up idiom → IB-176 build \| session cold-start; hook not yet active to capture it \| served` |

### 1c. `proposal-log.md` — promotion audit trail

| Field | Value |
|---|---|
| **What it is** | Append-only record of every promotion attempt out of `lessons.md`, applied or declined |
| **Entry count** | 3 entries (P-1…P-3), all `applied`; file at 44 lines |
| **Schema** | Header: `## P-<seq> · YYYY-MM-DD · L-<seq> · applied\|declined`. Body fields: **Proposal**, **Surface**, **Diff summary**, **Grade** (binary rubric: grounded/minimal/effective/non-regressive from a fresh-context assessor), **Ruling** |
| **Writer** | `/self-improve` promote mode, after the draft → shadow-sandbox → fresh-context grade → Nick-gate pipeline |
| **Cadence** | Event-driven, gated on threshold-crossing lessons (normal severity N≥2 occurrences, high N≥1) |
| **Sample entry** | `## P-1 · 2026-07-13 · L-1 · applied` — G9.I6 write-gate remediation across 4 skills; Grade all-yes, 1 revise cycle; Ruling: applied under delegated-judgment grant |

### 1d. `retro-latest.md` — most recent scan-mode report

| Field | Value |
|---|---|
| **What it is** | Single-file (overwritten each run, not append-only) snapshot of the last `/self-improve scan` pass |
| **Entry count** | 1 (the file itself; no internal row count — it's a report, not a ledger) |
| **Schema** | Free-form report: Sources read, Distill triage notes, PROMOTE flags, Store health (counts) |
| **Writer** | `/self-improve` scan mode |
| **Cadence** | Overwritten on each scan run (currently one run: 2026-07-13, the one-time SL distill) |
| **Sample content** | "Store health — `store_check.py --status` at write time: lessons 9 total / 9 open · queries 1 · proposals 0. Growth bound (50 open) far off." |

### 1e. `.query-capture.jsonl` — raw capture buffer (gitignored)

| Field | Value |
|---|---|
| **What it is** | Mechanical, no-judgment append of every user prompt, one JSON line per prompt |
| **Entry count** | 42 lines at time of inventory (grows continuously; truncated when scan mode distills it) |
| **Schema** | `{"ts": ISO8601, "session_id": str, "prompt": str}` — raw prompt text, including task-notification wrapper text for background-agent completions |
| **Writer** | `UserPromptSubmit` hook — `operations/kb-maintenance-scripts/hooks/capture_query.py`, registered in the tracked `.claude/settings.json` at workspace root. Fires on every prompt submission; fails silently (never blocks the session) |
| **Cadence** | Per-prompt, continuous |
| **Note** | This is the first concrete instance of "harness-enforced, not agent-remembers" capture in the engine — a hook, not a skill step |

### Supporting script: `store_check.py`

Location: `operations/kb-maintenance-scripts/store_check.py`. Deterministic (no LLM)
schema validator run as pre-commit check 4 whenever `operations/self/` files are staged.
Blocking checks: header regex conformance, required-field presence, ascending/unique
sequence numbers, cross-file reference integrity (`Q-<seq>` in lessons must exist in
query-log). Advisory (non-blocking) checks: PROMOTE-threshold flags, growth-bound
notice (>50 open lessons). Also runs in `--status` mode (counts only) for the
`/self-improve status` skill command.

---

## 2. System Log corpus — frozen, read-only feedstock

| Field | Value |
|---|---|
| **Location** | `operations/system-log/` |
| **Status** | Closed archive (README.md, dated 2026-07-13) — retired as a producer at session 138 (DD-116). No standing reader; historical reads via `/sl` only |
| **Entry count** | 153 dated entries + 1 `README.md` (not a log entry) |
| **Date range** | 2026-03-01 → 2026-06-21 (~3.5 months of session activity, era-spanning multiple governance regimes) |
| **Size** | 1.2 MB on disk; ~110,000 words / ~880,000 characters total — roughly 140,000–220,000 tokens depending on tokenizer, across 153 files |
| **Frontmatter schema** | Not uniform — the corpus spans at least two schema eras. Older/majority schema (139 of 153 files): `notion_id, log_entry, actor, area, change_type, milestone, rationale, source_dd, target_system, date` (Notion-migrated rows, dating to the pre-DD-59 Notion-backed System Log). Newer/minority schema (~53 files): `type, title, tags, session, telemetry` style entries reflecting later session-log conventions. `date` (150/153) and `target_system` (143/153) are the most consistent fields; `notion_id` is `null` for post-migration entries |
| **Body shape** | Free-form markdown after frontmatter — typically `## What Changed` (bullet list) plus, in later entries, a `## Revisit Trigger` section |
| **Sample — early (2026-03-01)** | `ib-09-system-log-db-created.md` — `change_type: "Implementation"`, `milestone: "M2"`, `rationale: "DD-11 mandates audit trails as a system primitive..."` — body: "Created System Log database inline on System Log spec page with 8 properties..." |
| **Sample — late (2026-06-21)** | `session-127-harness-whole-system-invariants-confirmed-deferred.md` — `change_type: "Decision"`, `source_dd: "DD-104"` — rationale cites a specific evidence test (rule 11, 2–3+ audit recurrence) applied to conclude no backfill was warranted; body has `## What Changed` + `## Revisit Trigger` sections |
| **Downstream state** | Already distilled once (2026-07-13, 3 parallel miner subagents): calibration numbers routed to `operations/references/calibration-registry.md` (17 consumer-keyed sections, 148 lines); lesson-shaped residue routed to `operations/self/lessons.md` (L-1…L-9). This inventory did not modify the corpus. |

---

## 3. Session-run / tool-call / operations log data on disk

### 3a. `operations/` report subfolders (non-`self`, non-`system-log`)

| Subfolder | File count | Shape | Cadence observed |
|---|---|---|---|
| `research-reports/` | 65 files, 812 KB | Dated markdown reports (`YYYY-MM-DD-<report-type>.md`): calibration, delta, crosslink, linkage-repair, pass2-extraction, source-quality-audit, source-triage, priority-reassessment, etc. | Per research-loop / reassessment run, roughly weekly-to-biweekly across the corpus's active period (earliest 2026-04-07) |
| `pattern-identification-reports/` | 14 files | Output of `/identify-artifacts` — classification reports | Per identify-artifacts run |
| `extraction-reports/` | 1 file | Output of `/extract-artifacts` | Ad hoc |
| `artifact-audits/` | 6 files (3 dated subdirectories + `runs.md` index) | `/audit-artifacts` whole-system audit runs, one dated dir per run (`2026-06-12`, `2026-07-12`, `2026-07-13`) plus a `runs.md` log of run metadata | Periodic, ~monthly cadence observed |
| `system-audits/` | 2 files | `/system-audit` full consistency-check reports (`2026-06-18`, `2026-06-21`) | Periodic |
| `drift-reports/` | 2 files | `/detect-drift` source-drift scan output (`2026-04-26`, `2026-07-13`) | Sparse/ad hoc |
| `extension-proposals/` | 5 files | Codifier-authored extension proposals (DD-97/DD-101 pipeline) | Per corpus-scan consolidation event |
| `split-proposals/` | 10 files | Guide-split proposals (DD-98) | Per guide-refresh run |
| `version-bump-proposals/` | 1 file | DD-100 version-bump proposal | Ad hoc |
| `kb-maintenance-scripts/` | 10 files | Python tooling (not accumulation data itself — includes `store_check.py`, `hooks/capture_query.py`, frontmatter/foundations validators) | N/A — code, not data |
| `references/` | 33 files | Registries and rubrics: `calibration-registry.md` (148 lines, 17 consumer-keyed sections — itself an accumulation surface, distilled from SL), `model-capability-registry.md`, `research-dimensions.md`, `form-classification-rubric.md`, `guide-routing-table.md`, `consumer-abstractions-map.md`, `link-intake-protocol.md`, plus a `librarian/` subdirectory | Periodic refresh, not per-session append |
| `plans/` | 1 file | `2026-07-12-engine-restructure-program.md` (18 KB) — the live restructure-program plan document | One long-lived document, edited in place across sessions, not append-only |

None of these subfolders is a uniform per-session log; each is a report type produced
by a specific skill's run, dated in the filename, and left in place (no rotation or
pruning observed).

### 3b. Hooks

Two hook registrations found, both in the tracked workspace-root `.claude/settings.json`
(`/Users/nickgogan/MetaSystem/.claude/settings.json`):

- **`UserPromptSubmit` → `capture_query.py`** — the query-capture hook feeding
  `operations/self/.query-capture.jsonl` (detailed in §1e above). This is the only
  hook found that writes accumulation data.
- **`pre-commit` (git hook, not a Claude Code hook)** — symlinked from
  `.git/hooks/pre-commit` to the tracked
  `operations/kb-maintenance-scripts/hooks/pre-commit`. Runs four checks on commit
  (frontmatter YAML validity, FOUNDATIONS.md sync, PROGRESS.md line-budget, and
  `store_check.py` over `operations/self/`). This is a *gate*, not an accumulation
  surface — it validates but does not itself write data.

No IL-scoped `.claude/` directory (`systems/improvement-loop/.claude/`) contains hooks
or settings — only `skills/` (41 skill directories). All hook registration lives at
the workspace root.

### 3c. `HISTORY.md`

| Field | Value |
|---|---|
| **Location** | `systems/improvement-loop/HISTORY.md` |
| **What it is** | Keep-a-Changelog-style, newest-first record of shipped sessions/milestones, with commit ranges |
| **Entry count** | 279 lines total; sessions 1–116 collapsed into era summaries, sessions 133 onward get per-session entries (Conventional Commits from session 133) |
| **Schema** | `## Session <N> — <date> — <headline> (<commit range>)` followed by a bolded **Outcome** paragraph and bullet detail | 
| **Writer** | `/session-handoff` skill exclusively (reconcile-in-place; workspace Process Rule 2 — no manual mid-session edits) |
| **Cadence** | Session-close, one entry per closed session (or backfilled batch, as with session 147 "closed without handoff") |
| **Sample** | Session 148 entry (current head): "the engine has its kernel documents... and plan checkpoint #2 is ruled: harness-first" — five detailed sub-bullets on constitution/PRD/actors/Block-0/Block-E outcomes |

### 3d. Git log shape

| Field | Value |
|---|---|
| **Total commits** | 320 |
| **Date range** | 2026-04-19 → 2026-07-16 (first commit in the visible history to latest) |
| **Conventional Commits adoption** | Partial — 79 commits match a recognized `type(scope):` or `type:` prefix (`docs:` 36, `feat:` 22, `fix:` 8, `chore:` 6, `kb:` 4, `refactor:` 3); the remainder predate the session-133 Conventional-Commits convention noted in `HISTORY.md` |
| **`Refs:` footer** | 73 commits carry a `Refs: <scope-slug>` footer naming the roadmap scope advanced (e.g. `Refs: phase4-interview`, `Refs: gate-clearance`) |
| **Co-author trailer** | Recent commits carry `Co-Authored-By: Claude <model> <noreply@anthropic.com>` — model identity varies by commit (`Claude Fable 5`, `Claude Opus 4.8 (1M context)` observed) |
| **Body shape** | Recent commits use structured bullet bodies summarizing multi-file changes, often citing specific artifact counts (e.g. "9 stale guides re-synthesized... ~140 findings back-annotated") |

### 3e. Research KB volumes (context, not itself an "operations" surface)

For scale reference: `research-findings/` holds 966 files, `research-sources/` 248,
`research-authorities/` 91. Governance: `project-management/design-decisions/` 90 DDs,
`project-management/implementation-backlog/` 77 IB items. These are the engine's
primary content stores, distinct from the operational/session-accumulation surfaces
this inventory targets, but they are themselves append/edit-over-time surfaces fed by
the research and codification pipelines.

---

## 4. Other accumulation-shaped surfaces found

### 4a. `agents/*/reflections/` — agent self-reflections

| Field | Value |
|---|---|
| **Location** | `agents/{owner,researcher,codifier,librarian}/reflections/` — one folder per agent |
| **What it is** | Agent-private, append-only, one-file-per-reflection-event self-assessments, fed into `/solicit-proposals` rounds |
| **Entry count** | 1 actual reflection file total across all four agents — `agents/codifier/reflections/2026-04-27-codifier-reflection.md`. The other three folders contain only a `CLAUDE.md` contract file each and are otherwise empty (owner's `CLAUDE.md` states "Currently empty. First reflection lands in session 52 or later.") |
| **Schema** | Frontmatter: `title, type: "agent-reflection", agent, target_system, period_covered {from, to}, trigger {kind, skill_run}, focus_areas, source_activity {sessions, artifacts}, proposals_derived, stage, tags`. Body: free-form numbered sections (the codifier sample used §3 Effectiveness, §4 Efficiency, §5 Help I could use, §8 Candidate proposals) |
| **Writer** | The agent itself, self-initiated or `/solicit-proposals`-triggered |
| **Cadence** | Documented freshness policy (owner's CLAUDE.md): "fresh" if `updated` within 21 days OR 3 agent sessions, whichever is shorter; re-reflect on staleness or material focus-area shift. In practice: one round has fired in the engine's history |
| **Privacy** | Declared agent-private by convention (not filesystem permission) — other agents don't read another agent's reflections folder |
| **Sample** | The codifier's 2026-04-27 reflection is a substantial (multi-thousand-word) calibration analysis over sessions 81–84, distinguishing signal strength by gate type (per-row / drafting-step / at-rest / autonomy-only) and explicitly declining to file 3 candidate proposals for lack of trigger evidence |

### 4b. `feedback/` folder

| Field | Value |
|---|---|
| **Location** | `systems/improvement-loop/feedback/` |
| **What it is** | Declared purpose (per engine `CLAUDE.md`): "Feedback items for improving the IL system" — one of the sources `/self-improve` scan mode is documented to sweep |
| **Entry count** | 0 — folder is currently empty |
| **Note** | The 2026-07-13 retro (`retro-latest.md`) confirms this: "`feedback/`: empty. Nothing to triage." This is a designated surface with no accumulated content yet |

### 4c. `calibration-registry.md` (already noted in §3a references/)

Worth flagging separately as an accumulation-shaped artifact rather than a static
reference: 17 consumer-keyed sections (148 lines), each holding empirical calibration
numbers (e.g., extraction density ratios, crosslink error rates, throughput figures)
distilled from the System Log corpus and tagged with the consuming skill. It is
currently a one-time distillation output, not a live per-event ledger, but its shape
(keyed rows accumulating numeric evidence per consumer) is structurally similar to
the query-log/lessons pattern.

---

## Surfaces at a Glance

| Surface | Location | Writer | Cadence | Volume (snapshot) | Append-only? | Schema rigor |
|---|---|---|---|---|---|---|
| Lesson store | `operations/self/lessons.md` | `/self-improve` capture + `/session-handoff` sweep | Event + session-close | 9 entries, 97 lines | Yes (status-flip, no delete) | Strict — regex-enforced header + required fields, pre-commit blocking |
| Demand ledger | `operations/self/query-log.md` | `/self-improve` scan (distills buffer) | Periodic (scan runs) | 1 row, 23 lines | Yes | Strict — 6-column contract, pre-commit blocking |
| Promotion audit trail | `operations/self/proposal-log.md` | `/self-improve` promote | Event (threshold-gated) | 3 entries, 44 lines | Yes | Strict — header regex + cross-ref to lessons, pre-commit blocking |
| Scan retro | `operations/self/retro-latest.md` | `/self-improve` scan | Overwritten per scan run | 1 report (55 lines), 1 run to date | No (overwrite) | Free-form |
| Raw query buffer | `operations/self/.query-capture.jsonl` | `UserPromptSubmit` hook (`capture_query.py`) | Per-prompt, continuous | 42 lines (gitignored, grows/truncates) | Yes until distilled | Fixed 3-field JSON, no validation |
| System Log corpus | `operations/system-log/` | (historical; retired 2026-07-13) | Was per-session; now frozen | 153 entries, 1.2 MB, ~140–220K tokens | Yes (closed, read-only) | Non-uniform — 2+ schema eras |
| Research reports | `operations/research-reports/` | Research-loop/reassessment skills | Per run (~weekly-biweekly historically) | 65 files, 812 KB | Yes (new file per run) | Per-report-type convention, not enforced |
| Artifact/system audits | `operations/{artifact,system}-audits/` | `/audit-artifacts`, `/system-audit` | Periodic (~monthly) | 6 + 2 files | Yes (dated dirs/files) | Free-form per skill |
| Drift reports | `operations/drift-reports/` | `/detect-drift` | Sparse/ad hoc | 2 files | Yes | Free-form |
| Calibration registry | `operations/references/calibration-registry.md` | One-time SL distill (manual so far) | Ad hoc refresh | 17 sections, 148 lines | Append/refresh, not per-event | Structured but not validated |
| HISTORY.md | `systems/improvement-loop/HISTORY.md` | `/session-handoff` only | Session-close | 279 lines, sessions 133+ per-session | Yes (newest-first insert) | Convention (Keep-a-Changelog), not schema-enforced |
| Git log | `.git` | git commits | Per commit | 320 commits since 2026-04-19; 79 Conventional-Commits-typed; 73 with `Refs:` footer | Yes (immutable) | Partial convention adoption, no enforcement found beyond human/agent discipline |
| Agent reflections | `agents/*/reflections/` | Agent self-initiated / `/solicit-proposals` | Documented 21-day/3-session freshness policy; observed: 1 round ever | 1 file (codifier only); 3 of 4 agents empty | Yes (one file per event) | Structured frontmatter contract, not validated by tooling |
| Feedback folder | `feedback/` | (undefined producer — declared destination only) | N/A | 0 items | N/A | N/A — empty |

