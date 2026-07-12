---
title: "Pattern Catalog"
id: "patterns-index"
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
  - "pattern"
  - "moc"
aliases:
  - "Patterns MOC"
---

# Patterns

Cross-system patterns distilled from operational experience and the [[improvement-loop]]. Each pattern documents a reusable approach to a recurring problem.

## How Patterns Get Here

1. **Pipeline extraction** — pattern-classified findings route to guide synthesis (DD-81); deployed patterns land here via the Nick-gated deploy stage
2. **Nick** observes operations and codifies patterns directly
3. **Governance re-homes** — methodology content distilled out of DDs (e.g., DD-120)

## Catalog (live view)

```dataview
TABLE category, target_system, stage
FROM "systems/improvement-loop/knowledge/patterns"
WHERE type = "pattern"
SORT updated DESC
```
