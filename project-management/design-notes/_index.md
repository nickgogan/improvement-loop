---
title: "IL Design Notes"
id: "il-design-notes-index"
type: "index"
category: "design-notes"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-22"
updated: "2026-04-23"
author: "owner"
source_dd:
  - "DD-52"
  - "DD-82"
  - "DD-86"
tags:
  - "design-notes"
  - "deliberative"
  - "project-management"
  - "moc"
  - "improvement-loop"
---

# Improvement Loop — Design Notes

Deliberative specifications for IL pipeline mechanics, substrate architecture, read contracts, and classification rubrics. Not runtime event output (that lives in `operations/`); not ratified governance (that lives in `governance/`); not tracked work items (those live in `implementation-backlog/`). Design notes are the "what we're deciding and why" substrate.

## What belongs here

- **Substrate audits** — how dimensions, patterns, guides, and the Librarian relate.
- **Read contracts** — query-execution protocols for agents.
- **Use-case registries** — canonical enumerations of consumer demand (e.g., Librarian use cases).
- **Classification rubrics** — decision specs (Form Router, artifact acceptance).
- **Lifecycle specs** — artifact-state transition specifications.
- **Pipeline-mechanics proposals** — structural-change proposals (e.g., pipeline collapse).
- **Spot-check reports** — empirical validation of proposed mechanisms.

## What does NOT belong here

- **Runtime event output** (SL entries, handoffs, research-reports, loop-reports, identification reports) → `operations/`.
- **Ratified governance rules** (boundary, pipeline, agent, knowledge rules) → `governance/`.
- **Owner-authored governance-rule proposals** (tracking mechanisms, DD proposals, amendments) → `governance/proposals/`.
- **Tracked work items** → `project-management/implementation-backlog/`.
- **Ratified decisions** → `project-management/design-decisions/`.

## Governance

Owner-governed folder; any agent may author here. Shape governs placement, not author (see DD-89 for the four-zone architecture that frames this rule).

## Discovery

Browse the folder directly or filter by frontmatter (`author`, `stage`, tags). Files are dated (`YYYY-MM-DD-slug.md`); chronological order reflects authorship order.

## Provenance

The first seven design notes in this folder were migrated from `operations/design-notes/` on 2026-04-22 during session 50, when the Owner proposed the four-zone architecture (ratified as DD-89). The `operations/design-notes/` folder was deprecated and removed. Session-51 files were authored natively under the new convention. The 2026-04-22 boundary-case-tracking note was relocated from `governance/proposals/` during session 52 after DD-89's proposals-folder scope was clarified to agent-initiated output only.

## Cross-References

- Four-zone architecture: DD-89
- Design Decisions: `project-management/design-decisions/`
- Implementation Backlog: `project-management/implementation-backlog/`
- Governing DDs: DD-52 (fractal pattern), DD-86 (Owner responsibility)
