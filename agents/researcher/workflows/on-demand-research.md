---
title: "On-Demand Research Workflow"
type: "workflow"
target_system:
  - "improvement-loop"
agent: "researcher"
created: "2026-04-19"
updated: "2026-04-19"
tags:
  - "workflow"
  - "researcher"
  - "research-query"
  - "on-demand"
---

# On-Demand Research

Targeted research for a specific question. The second intake pathway (DD-83), complementing the periodic scan.

## Trigger

- Nick asks "research X", "investigate Y", "what's the state of the art on Z"
- Librarian flags a KB gap and Nick wants it filled
- Design review surfaces a question the KB can't answer

## Flow

```
[1] /research-query "<question>"
         │
         Parse question
         Check dimension fit
         Scan existing KB coverage
         │
         ├─ Fits a dimension ──→ Research via Perplexity
         │
         └─ Doesn't fit ──→ Ask Nick: persist or one-off report?
                                │
                           ┌────┴────┐
                           │         │
                      One-off    Persist (may need new dimension)
                           │         │
                      Report only    Propose dimension, get approval
                           │         │
                           └────┬────┘
                                │
                         Research via Perplexity
                         Write report to operations/research-reports/
                                │
                    ─── PERSISTENCE GATE ───
                                │
                           ┌────┴────┐
                           │         │
                      Don't persist    Persist to KB
                           │              │
                      Done (report     Write findings + sources
                      is the output)   Update _index files
                                          │
                                     Findings enter pipeline
                                     (pipeline_status: raw)
```

## Decision Points

| Point | Question | Answer |
|-------|----------|--------|
| Step 1 | Does topic fit current dimensions? | Yes → proceed. No → ask Nick about persistence strategy. |
| Persistence gate | Persist findings to KB? | User decides. Pre-decided if Nick said "just a report" or "persist these". |
| Post-persistence | High-value sources found? | Flag in report for potential full `/research-loop` processing. |

## Human Gates

- **Dimension mismatch**: Nick decides whether to persist outside existing dimensions
- **Persistence decision**: Nick approves KB writes from on-demand queries (DD-83)

## Relationship to Periodic Scan

- `/research-query` produces findings identical in format to `/research-loop`
- On-demand findings enter the same pipeline (raw → identify → extract → deploy)
- On-demand reports may surface topics worth filing as IB items or as follow-up queries in the research-dimensions registry
