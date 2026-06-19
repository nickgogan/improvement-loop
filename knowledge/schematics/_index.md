---
title: "Schematic Library"
id: "schematics-index"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-06-18"
updated: "2026-06-18"
author: "claude"
source_dd:
  - "DD-104"
  - "DD-107"
tags:
  - "catalog"
  - "schematic"
  - "moc"
aliases:
  - "Schematics MOC"
  - "Schematic Library"
---

# Schematics

The engine's **top-altitude content** (DD-104): evidence-grounded `demand → configuration`
blueprints for agentic systems. A schematic answers "for *this* kind of need, here is a
configuration that works, why it works, and how you'd know it's working." Each carries a
**required evaluation/feedback layer** — the part that makes a configuration self-evolving
rather than a static recipe (DD-107).

## How Schematics Get Here

Schematics are **curated, not pipeline-extracted** (DD-107). They are authored by capturing a
**recurring named cluster** — a configuration the engine has seen work two or more times — not
by walking the full axis cross-product (the design space is sparse). The flow:

1. A cluster recurs (in research, in builds, in the engine's own operation).
2. Someone drafts it against `knowledge/templates/schematic-template.md`.
3. `grounded_in` links are filled with real findings; the evaluation/feedback layer is mandatory.
4. Nick gates promotion (DD-29). Validated schematics become `composed_of` material for new builds.

## Catalog

| Schematic | Altitude | Maturity | Function |
|-----------|----------|----------|----------|
| [[research-scanning-agent\|Research-Scanning Agent]] | middle | seed | research |
| [[codebase-audit-workcell\|Codebase-Audit Workcell]] | top | seed | audit |

## Dataview Query

```dataview
TABLE altitude, maturity, target_system, stage
FROM "systems/improvement-loop/knowledge/schematics"
WHERE type = "schematic"
SORT updated DESC
```
