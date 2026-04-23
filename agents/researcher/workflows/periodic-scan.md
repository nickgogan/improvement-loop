---
title: "Periodic Scan Workflow"
type: "workflow"
target_system:
  - "improvement-loop"
agent: "researcher"
created: "2026-04-19"
updated: "2026-04-19"
tags:
  - "workflow"
  - "researcher"
  - "research-loop"
  - "scan"
---

# Periodic Scan

Full research scan cycle across dimensions. The Researcher's primary workflow for discovering new patterns and maintaining KB currency.

## Trigger

- Monthly scheduled scan
- Nick requests "run a full scan" or "scan [dimension]"
- Significant time elapsed since last delta report

## Flow

```
[1] /research-loop [scope]
         │
         Read dimensions registry
         Search across dimensions via Perplexity
         Process sources, extract findings
         Deduplicate against KB
         │
         Produces: delta report, new/updated findings, source entries
         │
    ─── HUMAN GATE: Nick reviews delta report ───
         │
         ├─ High-value video sources identified?
         │        │
         │   [2] /transcript-fetcher
         │        │
         │   [3] /research-loop (Pass 2 deep extraction)
         │        │
         │        Produces: additional findings from transcripts
         │
         ├─ Watched libraries need checking?
         │        │
         │   [4] /watch-upstream
         │        │
         │        Produces: change triage report
         │
         ├─ Watched blogs need checking?
         │        │
         │   [5] /watch-blogs
         │        │
         │        Produces: new post triage report
         │
         └─ KB integrity concerns?
                  │
             [6] /linkage-repair + /finding-crosslink
                  │
                  Produces: repaired links, new cross-links
```

## Decision Points

| Point | Question | Answer |
|-------|----------|--------|
| Step 1 scope | Full or focused scan? | User specifies: `full`, single dimension, or `arxiv`. Default: full. |
| After Step 1 | Any P1/P2 video sources? | Yes → transcript fetch + Pass 2. No → skip. |
| After Step 1 | Watch lists stale? | Check last triage dates. If >1 month → run watch skills. |
| After Step 3 | KB link integrity? | If bulk extraction done → run linkage-repair. Otherwise skip. |

## Human Gates

- **After delta report**: Nick reviews findings, adjusts priorities, approves/rejects
- **Before Pass 2**: Nick confirms which videos warrant deep extraction
- **P1 findings**: Nick reviews before they flow to the Codifier

## Cadence

- **Full scan**: Monthly recommended
- **Dimension-focused**: Ad hoc, driven by project needs
- **arXiv scan**: Quarterly or when academic research is relevant
- **Watch-list triage**: Monthly, aligned with full scan
