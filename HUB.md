---
title: "Improvement Loop Hub"
type: "hub"
target_system:
  - "improvement-loop"
tags:
  - hub
  - navigation
  - improvement-loop
---

# Improvement Loop Hub

Research intelligence layer — intake, classification, extraction, and consumption.

---

## Agents

| Agent | Role | Skills | Definition |
|-------|------|--------|------------|
| Researcher | Intake & KB maintenance | 12 | [[agents/researcher/agent]] |
| Codifier | Classification, extraction, synthesis | 3 | [[agents/codifier/agent]] |
| Librarian | KB queries & design guidance | 0 (read-only) | [[agents/librarian/agent]] |

---

## Pipeline Status

```dataview
TABLE WITHOUT ID
  pipeline_status AS "Stage",
  length(rows) AS "Count"
FROM "systems/improvement-loop/research-findings"
WHERE pipeline_status != null
GROUP BY pipeline_status
```

---

## Design Decisions

```dataview
TABLE decision_id AS "ID", decision AS "Decision", status AS "Status"
FROM "systems/improvement-loop/project-management/design-decisions"
WHERE decision_id != null
SORT decision_id DESC
```

---

## Implementation Backlog

```dataview
TABLE WITHOUT ID file.name AS "Item", title AS "Title", status AS "Status"
FROM "systems/improvement-loop/project-management/implementation-backlog"
WHERE status != "Done"
SORT file.name ASC
```

---

## Guides (Staged)

```dataview
TABLE WITHOUT ID file.name AS "Guide", title AS "Title"
FROM "systems/improvement-loop/extracts/guides"
SORT file.name ASC
```

---

## Research Dimensions

| Dimension | Primary Guide |
|-----------|--------------|
| Context Engineering | G2 — Managing Agent Context |
| Model | G8 — Model-Resilient Prompt Engineering |
| Prompt | G8 — Model-Resilient Prompt Engineering |
| Tools | G5 — Designing Agent Tools |
| Intent | G1 — Writing Agent Specifications |
| Orchestration | G3 — Agent Architecture Decisions |
| Evaluation | G4 — Building Agent Evaluation Suites |
| Sandboxing | G6 — Agent Safety and Permissions |
| Governance | G9 — Agent Governance and Trust |
| Agent Design | G10 — Agent Design Patterns |

---

## Quick Links

| Resource | Path |
|----------|------|
| Guide Routing Table | [[operations/knowledge/guide-routing-table]] |
| Research Dimensions | [[operations/knowledge/research-dimensions]] |
| Handoff Protocol | [[agents/handoff-protocol]] |
| IL CLAUDE.md | [[CLAUDE]] |
| Research Reports | `operations/research-reports/` |
| Next Scan Notes | [[operations/next-scan-notes]] |
