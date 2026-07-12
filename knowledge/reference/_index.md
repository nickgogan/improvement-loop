---
title: "Reference Catalog"
id: "reference-index"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "2026-04-05"
updated: "2026-07-12"
author: "claude"
source_dd:
  - "DD-45"
tags:
  - "catalog"
  - "reference"
  - "moc"
aliases:
  - "Reference MOC"
  - "Resources"
---

# Reference

Active read-only context material for operating the engine — design-wisdom (fractal pattern, DBDO pipeline, vocabulary) and distilled reference from research findings. These are reference documents — not governance (see [[governance]]) or reusable patterns (see [[patterns]]).

## Dataview Query

```dataview
TABLE category, target_system, stage
FROM "systems/improvement-loop/knowledge/reference"
WHERE file.name != "_index"
SORT updated DESC
```
