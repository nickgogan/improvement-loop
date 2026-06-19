---
notion_id: null
log_entry: "S1-Schema and S2-Operations merged into Household OS"
actor: "Nick + Agent: Claude"
area: null
change_type: "Design Decision"
milestone: null
rationale: "S1-Schema was a read-only Notion extraction mirror. S2-Operations was the running Notion system. Both concerned the same product — the Household Operating System. Merging them into a single system called Household OS reflects reality: the product is the system, not the implementation layer. S-numbers are retired in favor of descriptive names."
source_dd: "DD-57, DD-58, DD-48"
target_system: "improvement-loop"
date: "2026-04-05"
---

## What Changed

- **S1-Schema and S2-Operations merged** into `incubator/household-os/` as a single system called Household OS
- **S-number scheme retired** — systems now use descriptive names (DD-57 supersedes DD-48)
- **Three-system model established:** Household OS, Claude Build, Improvement Loop
- **Constitution rewritten** — system definitions, boundary rules, and ownership matrix updated for 3 systems
- **Household OS CLAUDE.md created** — system-level agent context for the new unified system

### Content Migration

| Source | Destination |
|--------|-------------|
| `systems/s1-schema/pages/architecture/` | `incubator/household-os/knowledge/reference/architecture/` |
| `systems/s1-schema/pages/system-governance/` | `incubator/household-os/knowledge/reference/system-governance/` |
| `systems/s1-schema/pages/implementation-guides/` | `incubator/household-os/knowledge/reference/implementation-guides/` |
| `systems/s1-schema/schemas/` | `incubator/household-os/knowledge/reference/schemas/` |
| `systems/s1-schema/` (manifest, empty DBs) | `incubator/household-os/archive/s1-extraction/` |
| `systems/s2-operations/project-management/design-decisions/` | `incubator/household-os/project-management/design-decisions/` |
| `systems/s2-operations/project-management/implementation-backlog/` | `incubator/household-os/project-management/implementation-backlog/` |

### Governance Artifacts Created/Modified

| Item | Change |
|------|--------|
| DD-48 | Status changed from Binding to Superseded; note added referencing DD-57 |
| DD-57 | Created — retires S-number scheme, establishes descriptive naming |
| DD-58 | Created — formalizes S1+S2 merge into Household OS |
| Constitution | Rewritten — 3-system definitions, updated boundary rules, updated ownership matrix |
| Household OS CLAUDE.md | Created — system-level agent context |
| Cross-system DD `_index.md` | Updated — DD-48 status, DD-57 and DD-58 rows added |
