---
name: "Re-route Librarian composition tables from archived G3b to its DD-122 split destinations"
id: "IB-181"
source_dd: "DD-122"
status: "Backlog"
target_system: "improvement-loop"
priority: "P2"
type: "Maintenance"
notes: >-
  Surfaced by the 2026-07-22 rule-10 assess pass over the eval packages (report:
  operations/artifact-audits/2026-07-22-eval-packages-assess.md): the Librarian
  reference layer's audit.md/skill.md composition tables still route to the
  archived G3b guide instead of its DD-122 split destinations. Work: sweep the
  Librarian concept docs (audit.md, skill.md, and any other composition tables or
  guide-routing rows) for G3b slug references; re-point each to the correct split
  destination per DD-122's finding-routing table; verify /assess-skill and
  /design-skill compose the new slugs. Owner/Codifier-shaped substrate
  maintenance, not an audit-target defect.
milestone: null
---

# IB-181: Librarian composition tables — G3b → DD-122 split destinations

See `notes:` frontmatter. Evidence: the 2026-07-22 eval-packages assess report
(§surfaced substrate items). Related: DD-122 (the G3b split ruling), the
guide-routing-table, `/assess-skill` + `/design-skill` (consumers of the
composition tables).
