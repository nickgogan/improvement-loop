---
title: "Governance Cycle Workflow"
type: "workflow"
target_system:
  - "improvement-loop"
agent: "owner"
created: "2026-04-19"
updated: "2026-04-19"
tags:
  - "workflow"
  - "owner"
  - "governance"
---

# Governance Cycle

Periodic refresh of IL governance alignment with MetaSystem source governance. Run when MetaSystem governance changes, or periodically to detect drift.

## Trigger

- MetaSystem governance files updated (constitution, values, principles, vocabulary, fractal pattern)
- New DD created that affects IL operations
- Scheduled periodic review (monthly or at milestone boundaries)

## Flow

```
[1] /translate-governance --check-only
         │
         ├─ No drift ──→ Done (log check in SL)
         │
         └─ Drift detected
              │
     [2] /translate-governance (full run)
              │
         Governance docs updated
              │
     [3] /system-health --focus governance
              │
         Verify translations are consistent
              │
     [4] /maintain-docs --update
              │
         Fix CLAUDE.md or agent.md
         references if governance changes
         affected them
              │
     [5] SL entry for governance refresh
```

## Decision Points

| Point | Question | Answer |
|-------|----------|--------|
| After Step 1 | Is drift detected? | No → log clean check, stop. Yes → continue. |
| After Step 2 | Did translations require new governance docs (not just updates)? | New docs → Proposal-First, present to Nick. Updates → Guarded, proceed. |
| After Step 3 | Are there cascading drift issues beyond governance? | Yes → expand to full `/system-audit`. No → continue to Step 4. |

## Human Gates

- **New governance documents** (not updates to existing): Proposal-First — present draft, wait for approval
- **Changes that affect agent constitutions**: Proposal-First — constitution changes shape all future agent behavior
