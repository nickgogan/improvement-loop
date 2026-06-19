---
notion_id: null
log_entry: "Implementation Backlog items distributed to system-scoped folders"
actor: "Nick + Agent: Claude"
area: null
change_type: "Design Decision"
milestone: null
rationale: "Enforcing boundary isolation between systems. Each system's project-management agent should only access its own IB items. Moved 146 IB items from root implementation-backlog/ to 4 system-scoped project-management/implementation-backlog/ folders. Created DD-56 to formalize. Follows the DD-55 precedent for Design Decision distribution."
source_dd: "DD-56, DD-55, DD-47, DD-50, DD-42, DD-52"
target_system: "improvement-loop"
date: "2026-04-05"
---

## What Changed

- **146 Implementation Backlog items** moved from root `implementation-backlog/` to system-scoped folders:
  - 95 IB items → `systems/s2-operations/project-management/implementation-backlog/` (includes 12 items with null target_system, all UB3/Notion operational tasks)
  - 7 IB items → `incubator/claude-build/project-management/implementation-backlog/`
  - 7 IB items → `systems/improvement-loop/project-management/implementation-backlog/`
  - 37 IB items → `systems/meta-system/project-management/implementation-backlog/`
- Root `implementation-backlog/` folder deleted
- DD-56 created to formalize this distribution pattern
- Created `_index.md` in each destination folder
- Updated 8+ reference files: CLAUDE.md, governance.md, ib/SKILL.md, track/SKILL.md, claude-build/CLAUDE.md, s1-schema/README.md, notion-safety.md
- Updated DD-55 _index.md count and added DD-56 row

## Affected Items

| Item | Change |
|------|--------|
| DD-56 | Created — formalizes IB distribution pattern |
| DD-47 | Amended — workspace layout table, IB no longer at root |
| DD-50 | Amended — data access rules, IB location updated |
| CLAUDE.md (root) | Updated — workspace structure, data architecture, constitutional facts, navigation |
| .claude/rules/governance.md | Updated — data access rules for IB |
| .claude/skills/ib/SKILL.md | Rewritten — multi-folder path map, create/read/list/update/done logic |
| .claude/skills/track/SKILL.md | Updated — IB path map, create/read/list/summary logic |
| incubator/claude-build/CLAUDE.md | Updated — data sources, reference system, DD counts |
| systems/s1-schema/README.md | Updated — promoted databases table, authoritative sources |
| incubator/claude-build/.claude/rules/notion-safety.md | Updated — IB path references |
