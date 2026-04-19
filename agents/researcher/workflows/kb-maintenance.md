---
title: "KB Maintenance Workflow"
type: "workflow"
target_system:
  - "improvement-loop"
agent: "researcher"
created: "2026-04-19"
updated: "2026-04-19"
tags:
  - "workflow"
  - "researcher"
  - "kb-maintenance"
  - "linkage"
---

# KB Maintenance

Integrity maintenance for the research knowledge base. Run after bulk extraction sessions, backfills, or when the Owner flags KB integrity issues.

## Trigger

- After bulk source processing (10+ sources in one session)
- Owner's `/system-health` or `/system-audit` flags KB integrity issues
- Dimension changes requiring finding reclassification
- Periodic maintenance (quarterly)

## Flow

```
[1] /linkage-repair
         │
         Audit source↔finding bidirectional links
         Fix orphaned sources, unlinked findings, broken refs
         │
[2] /finding-crosslink
         │
         Detect missing cross-links between related findings
         Create enables/contradicts/extends/same-problem links
         │
[3] Dimension changes pending?
         │
         ├─ No ──→ Done
         │
         └─ Yes
              │
         [4] /dimension-rebalance
              │
              Review all findings against new dimension
              Propose reclassifications
              │
         ─── HUMAN GATE: Nick approves reclassifications ───
              │
              Apply approved changes
```

## Decision Points

| Point | Question | Answer |
|-------|----------|--------|
| After Step 2 | Were new dimensions added recently? | Yes → run dimension-rebalance. No → done. |
| Step 4 | How many findings affected? | Bulk reclassification (10+) → Proposal-First. Few (1-3) → Guarded. |

## Human Gates

- **Dimension reclassification**: Proposal-First — reclassification affects downstream routing
- **Finding promotion** from repo analyses: Proposal-First — creates new pipeline entries
