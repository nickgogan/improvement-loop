---
notion_id: null
log_entry: "Session 61: _index.md pattern cleanup sweep — 49 → 22 files"
actor: "Agent: Claude (Nick-sanctioned sweep from session-60 handoff)"
area: null
change_type: "Governance Infrastructure"
milestone: null
rationale: "Separating state into _index.md catalogs forced per-session maintenance — ledger tables drifted between sessions and catalog rows duplicated frontmatter. Deleting the catalogs where frontmatter already carries the information makes the artifact itself the source of truth and removes the maintenance tax."
source_dd: null
target_system: "improvement-loop"
date: "2026-04-23"
---

## What Changed

### Phase 1 — Deleted 12 ledger/catalog files

All four systems' IB and DD status tables, plus the four IL research-KB catalogs and archived-proposals catalog:

- `{IL,meta-system,household-os,claude-build}/project-management/{implementation-backlog,design-decisions}/_index.md` (8 files)
- `systems/improvement-loop/research-{findings,sources,authorities}/_index.md` (3 files)
- `systems/improvement-loop/archive/improvement-proposals/_index.md` (1 file)

### Phase 2 — Simplified 2 files

- `systems/improvement-loop/extracts/_index.md` — dropped 117-row artifact catalog; kept form → deployment-target map
- `systems/improvement-loop/project-management/design-notes/_index.md` — dropped row catalog; kept narrative

### Phase 3 — Renamed 16 narrative `_index.md` → `CLAUDE.md`

Folder READMEs where no sibling CLAUDE.md existed: reflections folders for all 4 IL agents, IL + meta-system governance proposals, meta-system `{agents,app,archive}`, claude-build governance, household-os `knowledge/reference/{architecture,implementation,system-governance}`, and `project-management/` CLAUDE.md for all 3 systems.

### Phase 4 — Stripped drifting columns

Removed `Count` column from structure tables in `incubator/claude-build/operations/_index.md` and `systems/meta-system/operations/_index.md`.

### Phase 5 — Edited skills

Cross-system: `.claude/skills/{ib,dd,track}/SKILL.md` — replaced "Update counts in CLAUDE.md and the destination folder's `_index.md`" with "Update counts in CLAUDE.md" (frontmatter is the source of truth). `.claude/skills/bootstrap/SKILL.md` — scaffold loop now creates `CLAUDE.md` per folder instead of `_index.md`.

IL: removed writes to deleted `_index.md` files from `research-loop`, `promote-findings`, `research-query`, `dimension-rebalance`, `extract-artifacts`, `synthesize-guide`. Updated `maintain-docs`, `system-audit`, `system-health` to stop auditing against `_index.md` as a drift surface.

### Phase 6 — Fixed active-file reference leaks

- `incubator/claude-build/CLAUDE.md` — reference rows redirected from `_index.md` to folder + `/track` filters
- `incubator/claude-build/.claude/rules/notion-safety.md` — same
- `systems/improvement-loop/operations/references/librarian/coverage.md` — Phase 1 load-indices section rewritten to filter frontmatter
- `.claude/rules/governance.md` — process rule #1 rewritten: "Frontmatter is the source of truth"
- `systems/improvement-loop/extracts/guides/model-resilient-prompt-engineering.md` — single-line prompt scaffold updated

### Phase 7 — Verified

49 → 22 `_index.md` files. 93 residual active-file references across 48 files; the majority are historical (design-notes from session 46-47), published guides discussing the pattern, or illustrative mentions in skill calibration notes. Kept `_index.md` files fall into three groups:

| Group | Count | Treatment |
|-------|-------|-----------|
| Dataview-driven (watched-blogs, watched-libraries, knowledge/{patterns,guides,reference,templates}) | 11 | Kept — self-updating queries |
| Load-bearing substrate (IL librarian ref, IL + meta-system governance narratives, household-os s1-extraction archive) | 4 | Kept — narrative-heavy, not ledger |
| Stable structure maps (project-management, operations, agents, app) | 5 | Kept — 2-3 row file enumerations, not drift-prone |
| Phase-2 simplified (extracts, design-notes) | 2 | Kept — narrative only, no catalog |

## Follow-ups for Nick

Four Design Decisions still reference `_index.md` as a governance requirement. Per DD-44, they need supersession or amendment rather than in-place edits:

- **DD-55** ("Each destination folder has an `_index.md` listing its DDs") — now violated for IB/DD folders.
- **DD-56** (same rule for IB) — same.
- **DD-65** (IL KB update rule — "After any create/update: Update the corresponding `_index.md`") — violated.
- **DD-74** (context file hygiene) — the "`_index.md` Is Not Blocking" section is now obsolete. Rule is stronger: most `_index.md` catalogs no longer exist.

**IB-142** (meta-system agents) describes a vault-curator agent whose scope included "maintains `_index.md` catalogs" — scope revision needed before the work is picked up.

Historical references in design-notes (2026-04-20), immutable DDs (DD-91), and deployed guides were left untouched per the handoff's guidance.

## Affected Skills

Six IL skills had `_index.md` write steps removed (`research-loop`, `promote-findings`, `research-query`, `dimension-rebalance`, `extract-artifacts`, `synthesize-guide`). Four cross-system skills (`ib`, `dd`, `track`, `bootstrap`) and three Owner skills (`maintain-docs`, `system-audit`, `system-health`) updated to reflect new reality.

## Artifacts

- Handoff: `operations/handoff-prompts/handoff-prompt-index-md-full-cleanup.md` (session-60 authored, this session executed)
- Session-60 precursor SL: `systems/improvement-loop/operations/system-log/session-60-researcher-killed-bucket-d-deleted-next-scan-notes.md`
