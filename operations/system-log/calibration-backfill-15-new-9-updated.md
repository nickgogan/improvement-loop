---
notion_id: null
log_entry: "Calibration backfill: 15 new findings created, 9 existing updated, 10 sources re-linked"
actor: "Agent: Claude"
area: null
change_type: "Implementation"
milestone: null
rationale: "Following the calibration exercise that identified 131 missed and 57 vague patterns across 16 transcripts, backfilled the top-priority gaps. Created 15 Tier 1 new findings (4 P1, 7 P2, 4 P3) covering prompt caching, verification agent patterns, file read dedup, data/schema-first, negative constraints, goal-first management, skill vs process distinction, one-shot PRD bootstrap, YAML template dual structure, tech stack pinning, identity pinning, deep plan extraction, llms.txt, BMAD marketplace, and six-layer infrastructure stack. Updated 9 existing findings with transcript-derived specifics. Updated 10 source entries with 15 new finding linkages."
source_dd: null
target_system: "improvement-loop"
timestamp: "2026-04-07T00:00:00.000Z"
---

## What Changed

- Created 15 new research findings (Tier 1 from calibration backfill priority list)
- Updated 9 existing findings with transcript-derived specifics: token waste taxonomy, hooks, Karpathy KB, BMAD v6, Superpowers, Ultra Plan, SOUL.md, gstack, GSD
- Updated 10 source entries with 15 new finding linkages
- Updated findings `_index.md` with 15 new rows
- Fixed Video 4 misattribution: re-linked source to `goal-first-agent-management-abstraction.md`
- KB grew from ~170 to ~185 findings

## Affected Items

- `systems/improvement-loop/research-findings/` — 15 new files, 9 edited
- `systems/improvement-loop/research-sources/` — 10 edited
- `systems/improvement-loop/research-findings/_index.md` — updated
