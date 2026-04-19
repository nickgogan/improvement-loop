---
notion_id: null
log_entry: "Research dimensions externalized from skill body to registry file"
actor: "Agent: Claude"
area: null
change_type: "Architectural Decision"
milestone: null
rationale: "Moved 5 dimension queries from the research-loop skill body into an external registry at knowledge/research-dimensions.md. The skill now reads the registry at scan start and proposes refinements at scan end. This decouples dimension evolution from skill definition changes, allowing dimensions to be added, renamed, or retired without modifying the skill itself."
source_dd: "DD-68"
target_system: "Improvement Loop"
timestamp: "2026-04-07T00:00:00.000Z"
---

## What Changed

- Extracted 5 research dimension queries from research-loop skill into `knowledge/research-dimensions.md`
- Skill updated to read registry at scan start, propose refinements at scan end
- Dimension evolution now independent of skill versioning

## Affected Items

- `knowledge/research-dimensions.md` — created
- `.claude/skills/research-loop/SKILL.md` — updated to reference registry
