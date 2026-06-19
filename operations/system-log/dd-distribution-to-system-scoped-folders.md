---
notion_id: null
log_entry: "Design Decisions distributed to system-scoped folders"
actor: "Nick + Agent: Claude"
area: null
change_type: "Design Decision"
milestone: null
rationale: "Enforcing boundary isolation between systems. Each system's project-management agent should only access its own DDs. Moved 54 DDs from root design-decisions/ to 4 system-scoped project-management/design-decisions/ folders. Created DD-55 to formalize."
source_dd: "DD-55, DD-47, DD-50, DD-42, DD-52"
target_system: "improvement-loop"
timestamp: "2026-04-05T00:00:00.000Z"
---

## What Changed

- **54 Design Decisions** moved from root `design-decisions/` to system-scoped folders:
  - 28 DDs (DD-01–DD-28) → `systems/s2-operations/project-management/design-decisions/`
  - 3 DDs (DD-33, DD-34, DD-49) → `incubator/claude-build/project-management/design-decisions/`
  - 6 DDs (DD-29–DD-31, DD-36, DD-39, DD-41) → `systems/improvement-loop/project-management/design-decisions/`
  - 17 DDs (DD-32, DD-35, DD-37–DD-38, DD-40, DD-42–DD-48, DD-50–DD-54) → `systems/meta-system/project-management/design-decisions/`
- Root `design-decisions/` folder deleted
- DD-55 created to formalize this distribution pattern
- Created `_index.md` in each destination folder
- Created `project-management/` folders for s2-operations and improvement-loop (previously missing)
- Updated 8+ reference files: CLAUDE.md, governance.md, dd/SKILL.md, track/SKILL.md, claude-build/CLAUDE.md, s1-schema/README.md, notion-safety.md
- Updated DD-47 and DD-50 body text to reflect new locations

## Affected Items

| Item | Change |
|------|--------|
| DD-55 | Created — formalizes distribution pattern |
| DD-47 | Body updated — workspace layout table, governance database section, context flow |
| DD-50 | Body updated — authoritative location table, agent callout |
| CLAUDE.md (root) | Updated — workspace structure, data architecture, constitutional facts, navigation |
| .claude/rules/governance.md | Updated — data access rules |
| .claude/skills/dd/SKILL.md | Rewritten — multi-folder path map, create/read/list/update logic |
| .claude/skills/track/SKILL.md | Updated — DD path map, create/read/list/summary logic |
| incubator/claude-build/CLAUDE.md | Updated — data sources, reference system, DD counts |
| systems/s1-schema/README.md | Updated — promoted databases table, authoritative sources |
| incubator/claude-build/.claude/rules/notion-safety.md | Updated — DD path references |
