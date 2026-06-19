---
notion_id: null
log_entry: "Two-pass extraction codified, dimensions expanded from 5 to 9, rebalance executed"
actor: "Agent: Claude"
area: null
change_type: "Architectural Decision"
milestone: null
rationale: "Codified Pass 1 (headline triage) / Pass 2 (transcript deep extraction) model in research-loop skill. Added 4 new dimensions: Orchestration, Evaluation, Sandboxing, Governance (5 to 9 total). Executed dimension rebalance with 8 reclassifications and 2 splits. Created transcript-fetcher and dimension-rebalance skills. Calibration proved 46.5% miss rate with single-pass extraction. Orchestration (31.6% of findings) had no home dimension."
source_dd: "DD-67"
target_system: "improvement-loop"
date: "2026-04-07"
---

## What Changed

- Codified two-pass extraction model (Pass 1: headline triage, Pass 2: transcript deep extraction)
- Added 4 new research dimensions: Orchestration, Evaluation, Sandboxing, Governance
- Executed dimension rebalance: 8 reclassifications, 2 splits
- Created `/transcript-fetcher` skill
- Created `/dimension-rebalance` skill

## Affected Items

- `.claude/skills/research-loop/SKILL.md` — two-pass model added
- `.claude/skills/transcript-fetcher/` — created
- `.claude/skills/dimension-rebalance/` — created
- `knowledge/research-dimensions.md` — expanded from 5 to 9 dimensions
- `research-findings/` — 10 files reclassified or split
