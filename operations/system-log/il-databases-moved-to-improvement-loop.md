---
log_entry: "IL-owned databases moved from s1-schema to improvement-loop/"
actor: "Nick + Agent: Claude"
area: null
change_type: "Implementation"
milestone: "M3"
rationale: "Nick identified that the four IL-owned databases (improvement-proposals, research-findings, research-sources, research-authorities) belong with the Improvement Loop, not inside the Notion mirror. Moved to improvement-loop/ at workspace root. s1-schema/databases/ is now empty."
source_dd: "DD-47"
target_system: "improvement-loop"
timestamp: "2026-04-04T00:00:00.000Z"
---

# IL-owned databases moved from s1-schema to improvement-loop/

## Moved
- `improvement-proposals/` → `systems/improvement-loop/improvement-proposals/`
- `research-findings/` → `systems/improvement-loop/research-findings/`
- `research-sources/` → `systems/improvement-loop/research-sources/`
- `research-authorities/` → `systems/improvement-loop/research-authorities/`

## References Updated
- Root CLAUDE.md, .claude/rules/governance.md, meta-system/CLAUDE.md, systems/s1-schema/README.md
