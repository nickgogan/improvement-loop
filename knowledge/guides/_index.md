---
title: "Guides Catalog"
id: "guides-index"
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
  - "guide"
  - "moc"
aliases:
  - "Guides MOC"
  - "Guidelines"
---

# Guides

How-to documentation and playbooks — when and how to use specific tools, techniques, and architectural components across the Household OS.

## How Guides Get Here

1. **Improvement Loop** evaluates tool usage and produces recommendations (DD-46)
2. **Nick** documents operational guides from direct experience
3. **Build sessions** surface reusable guidance worth codifying

## Catalog

| Guide | Category | Systems | Stage |
|-------|----------|---------|-------|
| [[research-to-codification-pipeline|Research-to-Codification Pipeline]] | knowledge-management | cross-system | active |
| [[skill-authoring-guide|Skill Authoring Best Practices]] | agent-design | cross-system | active |

## Dataview Query

```dataview
TABLE category, target_system, stage
FROM "systems/improvement-loop/knowledge/guides"
WHERE type = "guideline"
SORT updated DESC
```
