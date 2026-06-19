---
notion_id: "32c1e08b-9b34-812a-be04-f4b03b0dd50c"
log_entry: "DD-42 amended: System Log added to promoted databases, hierarchy updated for Governance/Architecture split"
actor: "Agent: Claude"
area: null
change_type: "Design Decision"
milestone: "M2"
rationale: "System Log meets all three DD-42 promotion criteria (cross-system scope, active state, high write frequency). System Governance extracted from Architecture to be a peer section under System Documentation. Design Decision Guidelines moved from System Governance to be a peer of Implementation under System Documentation. DD-42 page updated with corrected Promoted Databases table, What Stays table, Three-Layer Model, decision rule commentary, and Resulting Hierarchy."
source_dd:
  - "https://www.notion.so/32b1e08b9b3481cab43fc07b1b9ecc75"
target_system: "Cross-System"
timestamp: "2026-03-23T16:46:21.373Z"
---

# DD-42 amended: System Log added to promoted databases, hierarchy updated for Governance/Architecture split

## Affected Items

| Name | URL |
|------|-----|
| Operational Database Placement (DD-42) spec page | 32b1e08b-9b34-81f0-b670-e83b7bf87cba |
| DD-42 database entry | 32b1e08b-9b34-81ca-b43f-c07b1b9ecc75 |

## Source Pages

| Name | URL |
|------|-----|
| DD-42 spec page | 32b1e08b-9b34-81f0-b670-e83b7bf87cba |

## Amendment Summary
DD-42 amended to reflect three structural changes:
1. **System Log added to Promoted Databases table** --- was previously excluded as "historical/append-only" but meets all three promotion criteria in practice
2. **System Governance extracted from Architecture** --- now a peer section under System Documentation, not a child of Architecture. Architecture is now purely about system designs.
3. **Design Decision Guidelines moved** --- from System Governance to a peer of Implementation under System Documentation. It's methodology, not governance.
4. **Decision rule commentary updated** --- added explanation of why System Log was originally excluded and why the exclusion was wrong
5. **Resulting Hierarchy updated** --- reflects current full structure including Governance and DDG positions

## Affected IB Items
None directly --- this is a documentation and structural alignment change.
