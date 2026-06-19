---
notion_id: null
log_entry: "Source-to-finding misattribution discovered — title-based matching is unreliable"
actor: "Agent: Claude"
area: null
change_type: "Operational Learning"
milestone: null
rationale: "During transcript re-extraction calibration, discovered that Video 4 ('Stop Using Claude Code in Terminal' by Simon Scrapes) was linked to finding 'ide-first-claude-code-with-deterministic-hooks.md'. The transcript contains neither IDE-first advocacy nor deterministic hooks — the video is about a web dashboard command center. The finding was matched based on the video title, not actual content. This reveals a process vulnerability: summary-based extraction can match the wrong pattern when titles are misleading. The finding now has zero sources and needs re-sourcing."
source_dd: null
target_system: "improvement-loop"
timestamp: "2026-04-07T00:00:00.000Z"
---

## What Changed

- Identified that `stop-using-claude-code-in-terminal.md` (source) was incorrectly linked to `ide-first-claude-code-with-deterministic-hooks.md` (finding)
- Root cause: summary-based extraction matched on video title semantics rather than actual transcript content
- Fixed: source re-linked to `goal-first-agent-management-abstraction.md` (correct finding for actual content)
- `ide-first-claude-code-with-deterministic-hooks.md` now has zero sources — content is valid but origin unknown
- Learning: title-based matching during triage is a known failure mode. Transcript-based verification should be part of the extraction quality gate.

## Affected Items

- `systems/improvement-loop/research-sources/stop-using-claude-code-in-terminal.md` — findings array corrected
- `systems/improvement-loop/research-findings/ide-first-claude-code-with-deterministic-hooks.md` — sources emptied
- `systems/improvement-loop/research-findings/goal-first-agent-management-abstraction.md` — already correctly sourced
