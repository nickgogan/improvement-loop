---
title: "Guides Catalog"
id: "guides-index"
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
  - "guide"
  - "moc"
aliases:
  - "Guides MOC"
  - "Guidelines"
---

# Guides

Authored how-to documentation for operating the engine. This class is dissolution-bound
(substrate audit, gate G8): the pipeline guide folds into the kernel's *how-it-works* doc and
the skill-authoring reference re-homes into the kernel's harness-description doc when the
restructure program's Phase 4/5 defines them. Synthesized research guides live in
`extracts/guides/` (DD-111), not here.

```dataview
TABLE category, target_system, stage
FROM "systems/improvement-loop/knowledge/guides"
WHERE type = "guideline"
SORT updated DESC
```
