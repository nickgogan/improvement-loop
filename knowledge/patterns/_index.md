---
title: "Pattern Catalog"
id: "patterns-index"
type: "governance"
category: "governance"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-05"
updated: "2026-04-07"
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

1. **Improvement Loop** researches and proposes patterns (DD-46)
2. **Nick** observes operations and codifies patterns directly
3. **Agents** extract patterns from build sessions

## Catalog

| Pattern | Category | Systems | Stage |
|---------|----------|---------|-------|
| [[capability-type-selection|Capability Type Selection]] | agent-design | cross-system | active |
| [[upstream-dependency-spectrum|Upstream Dependency Spectrum]] | system-design | cross-system | active |

## Dataview Query

```dataview
TABLE category, target_system, stage
FROM "systems/improvement-loop/knowledge/patterns"
WHERE type = "pattern"
SORT updated DESC
```
