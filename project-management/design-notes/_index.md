---
title: "IL Design Notes"
id: "il-design-notes-index"
type: "index"
category: "design-notes"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-22"
updated: "2026-07-12"
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

**Deliberation in progress or awaiting its gate** — and nothing that anything live delegates to by path:

- **Substrate audits** — per-class verdict proposals awaiting/under gate execution.
- **Classification rubrics and lifecycle specs** — while being decided.
- **Pipeline-mechanics proposals** — structural-change proposals (e.g., pipeline collapse).
- **Direction notes** — living North-Star capture (e.g., agentic-os-direction) until a later phase pins scope.

## What does NOT belong here

- **Living operational reference** — anything skills, concept docs, or workflows delegate to by path (read contracts, use-case registries, boundary-case taxonomies, spot-check evidence) → `operations/references/` (DD-112 home rule). This folder held several of those until 2026-07-12; they were re-homed or distilled by the substrate-audit sweep (gate G6).
- **Fully-ratified deliberation** — once every surviving decision lives in DDs or shipped artifacts, the note is provenance and moves to `archive/design-notes/` (filenames preserved, no stubs; DD/HISTORY citations keep resolving at the archive path).
- **Runtime event output** (research-reports, loop-reports, identification reports) → `operations/`.
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
