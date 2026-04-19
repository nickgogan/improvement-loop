---
title: "Watched Library Analyses"
id: "watched-library-analyses-index"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-04-07"
updated: "2026-04-07"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "catalog"
  - "repo-analysis"
  - "watched-library"
aliases:
  - "Repo Analysis MOC"
---

# Watched Library Analyses

Structural analysis docs produced by `/repo-analyzer`. Each entry covers 5 dimensions: structural inventory, context file map, workflow topology, governance model, and cross-agent protocol.

## Catalog

| Library | Version Analyzed | Date | Dimensions |
|---------|-----------------|------|------------|
| [[gsd-analysis\|GSD]] | v1.33.0 | 2026-04-07 | all |
| [[superpowers-analysis\|Superpowers]] | v5.0.7 | 2026-04-08 | all |
| [[bmad-method-analysis\|BMAD Method]] | v6.2.2 | 2026-04-08 | all |
| [[openclaw-analysis\|OpenClaw]] | v2026.4.5 | 2026-04-08 | all |
| [[paperclip-analysis\|Paperclip]] | v2026.403.0 | 2026-04-08 | all |
| [[gstack-analysis\|gstack]] | v0.15.16.0 | 2026-04-08 | all |
| [[mem0-analysis\|mem0]] | v1.0.11 | 2026-04-08 | all |
| [[archon-analysis\|Archon]] | v0.3.2 | 2026-04-09 | all |
| [[n8n-analysis\|n8n]] | v2.16.0 | 2026-04-09 | all |
| [[langgraph-analysis\|LangGraph]] | v1.1.6 | 2026-04-09 | all |
| [[beads-analysis\|Beads]] | v1.0.2 | 2026-04-19 | all |
| [[openviking-analysis\|OpenViking]] | latest | 2026-04-19 | all |
| [[sandbox-analysis\|AIO Sandbox]] | v1.0.0.150 | 2026-04-19 | all |
| [[deer-flow-analysis\|DeerFlow]] | v2.0 | 2026-04-19 | all |

## Cross-Repo Comparison

[[cross-repo-comparison|Cross-Repo Structural Comparison]] — All 14 repos compared across 6 dimensions. Regenerated 2026-04-09 (pending update with new batch).

## Dataview Query

```dataview
TABLE analyzed_version, analyzed_date, dimensions_analyzed
FROM "systems/improvement-loop/watched-libraries/analysis"
WHERE type = "analysis" AND id != "watched-library-analyses-index"
SORT analyzed_date DESC
```
