---
title: "Reference Catalog"
id: "reference-index"
type: "governance"
category: "governance"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-05"
updated: "2026-04-05"
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

Active read-only context material for operating within the Household OS. These are reference documents — not governance (see [[governance]]) or reusable patterns (see [[patterns]]).

## How Reference Material Gets Here

1. **Improvement Loop** produces distilled reference from research findings
2. **Nick** captures reference material from operational experience
3. **Build sessions** produce context docs worth preserving

## Catalog

| Reference | Category | Systems | Stage |
|-----------|----------|---------|-------|
| [[consumer-abstractions-map]] | consumer-abstractions | meta-system | active |
| [[harness]] | concept (§Construction) | meta-system | draft |

## Dataview Query

```dataview
TABLE category, target_system, stage
FROM "systems/improvement-loop/knowledge/reference"
WHERE type = "resource"
SORT updated DESC
```
