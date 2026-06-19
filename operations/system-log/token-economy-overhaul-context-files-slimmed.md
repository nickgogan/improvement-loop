---
notion_id: null
log_entry: "Token economy overhaul: CLAUDE.md slimmed 164 to 62 lines, 3 governance rules added"
actor: "Agent: Claude"
area: null
change_type: "Architectural Decision"
milestone: null
rationale: "Stripped hardcoded counts from 12+ files. CLAUDE.md reduced from 164 to 62 lines. Added 3 governance rules: _index.md updates are not blocking, PROGRESS.md updated once at session end, no hardcoded counts. Every token in context files costs budget on every invocation, and the maintenance burden of keeping counts accurate was unsustainable."
source_dd: "DD-74"
target_system: "improvement-loop"
timestamp: "2026-04-07T00:00:00.000Z"
---

## What Changed

- Removed hardcoded counts from 12+ files across the workspace
- CLAUDE.md reduced from 164 to 62 lines
- Added governance rule: `_index.md` updates are not blocking
- Added governance rule: PROGRESS.md updated once at session end
- Added governance rule: no hardcoded counts in prose or tables

## Affected Items

- `CLAUDE.md` — slimmed from 164 to 62 lines
- `.claude/rules/governance.md` — 3 new rules added
- Multiple `_index.md` and context files — counts removed
