---
title: "IL Governance Proposals"
id: "il-governance-proposals-index"
type: "index"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-22"
updated: "2026-04-22"
author: "owner"
source_dd:
  - "DD-44"
  - "DD-86"
  - "DD-91"
tags:
  - "governance"
  - "proposals"
  - "moc"
  - "improvement-loop"
aliases:
  - "IL proposals catalog"
---

# IL Governance Proposals

Destination for **agent-initiated** proposals in the Improvement Loop — output from `/solicit-proposals` rounds and ad-hoc agent-initiated proposals (per DD-91's dual proposal pathways).

## What belongs here

- **Solicitation-round proposals** — per-agent proposal drafts from `/solicit-proposals` rounds. Trigger: `owner-solicited`.
- **Ad-hoc agent-initiated proposals** — proposals an agent writes outside a round when it notices a gap. Trigger: `agent-initiated`.

## What does NOT belong here

- **Owner + Nick collaborative governance work** → DDs (new or amended) directly. No proposal layer.
- **Deliberative specifications** (substrate audits, read contracts, tracking mechanisms, rubrics, lifecycle specs) → `project-management/design-notes/`.
- **Ratified governance rules** → `governance/` root.
- **Ratified DDs** → `project-management/design-decisions/`.
- **Runtime event output** → `operations/`.

## Governance

Nick gates every proposal before it becomes binding. Accepted proposals convert to IB items (work) or feed into DDs (governance). Stages: `proposed` → `accepted` / `rejected` / `superseded` / `applied`.

## Current contents

Empty. First agent-initiated proposals expected from the first `/solicit-proposals` round (session 53 or later).

## Cross-references

- DD-91 (reflections-to-proposals architecture) — defines the dual pathways into this folder
- Design notes (deliberative substrate): `project-management/design-notes/`
- Design Decisions: `project-management/design-decisions/`
- Parent governance index: `governance/_index.md`
- Governing DDs: DD-44 (DD immutability), DD-86 (Owner Autonomy Table), DD-91 (reflections architecture)
