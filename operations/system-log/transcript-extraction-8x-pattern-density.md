---
notion_id: null
log_entry: "Transcript-based extraction yields 8.4x pattern density vs. summary-based"
actor: "Nick + Agent: Claude"
area: null
change_type: "Operational Learning"
milestone: null
rationale: "Calibration of 16 YouTube transcripts against existing KB revealed a 46.5% miss rate from Perplexity-summary-based extraction. Transcript-based re-extraction identified 17.6 patterns per video vs 2.1 from summaries (8.4x increase). Implementation details are the #1 miss category at 31%. This fundamentally changes how the research pipeline should operate — transcript-first extraction is now mandatory for high-value sources."
source_dd: null
target_system: "Improvement Loop"
timestamp: "2026-04-07T00:00:00.000Z"
---

## What Changed

- Measured extraction quality gap: Perplexity summaries capture headline concepts but strip implementation details (configs, file paths, operational constraints, workflow mechanics)
- Established content-type miss hierarchy: implementation details (31%) > named patterns (23%) > tool names (15%) > process/methodology (15%) > specific numbers (9%) > architectural concepts (7%)
- Codified "transcript-first for high-value sources" as a permanent principle in IL CLAUDE.md cognitive disposition
- Identified optimal pipeline: summary for triage → transcript for deep extraction → human review for priority triage

## Affected Items

- `systems/improvement-loop/operations/loop-reports/2026-04-07-calibration-report.md` — full calibration data
- `systems/improvement-loop/CLAUDE.md` — transcript-first principle added to cognitive disposition
- `.claude/skills/research-loop/SKILL.md` — pending update to formalize two-pass extraction
