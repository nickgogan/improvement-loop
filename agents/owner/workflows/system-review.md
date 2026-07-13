---
title: "System Review Workflow"
type: "workflow"
target_system:
  - "improvement-loop"
agent: "owner"
created: "2026-04-19"
updated: "2026-04-19"
tags:
  - "workflow"
  - "owner"
  - "audit"
  - "health"
---

# System Review

End-to-end system review: quick health check, feedback processing, optional deep audit, and remediation. Run at session start for orientation or periodically for maintenance.

## Trigger

- Session start without a specific task (Owner provides orientation)
- User asks "is the system in good shape?"
- Post-structural-change verification (new agents, skills, or governance)
- Milestone boundary check

## Flow

```
[1] /system-health (quick diagnostic)
         │
         ├─ Healthy ──→ Process any pending feedback [3]
         │
         └─ Issues detected
              │
         ┌────┴────┐
         │         │
    Minor drift   Multiple/systemic issues
         │         │
    [2a] /maintain-docs --update    [2b] /system-audit (full)
         │                                │
         Fix factual drift               Written audit report
         │                                │
         └──────────┬─────────────────────┘
                    │
         [3] /self-improve scan
                    │
              Buffer distilled, feedback triaged,
              lessons swept, PROMOTE flags emitted
                    │
         [4] Remediation
              │
              ├─ Guarded fixes: apply directly
              ├─ Proposal-First items: present to Nick
              └─ Human-Required items: log for Nick
                    │
         [5] SL entry for review session
```

## Decision Points

| Point | Question | Answer |
|-------|----------|--------|
| After Step 1 | How many issues? | 0 → skip to feedback. 1-3 minor → `/maintain-docs --update`. 4+ or systemic → `/system-audit`. |
| After Step 2 | Are issues remediated by doc fixes alone? | Yes → proceed to feedback. No → escalate remaining items. |
| After Step 3 | Are feedback items related to audit findings? | Yes → combine into a single remediation plan. No → handle separately. |

## Human Gates

- **Structural proposals** from audit findings: Proposal-First
- **DD-requiring issues**: Human-Required — log and present
- **Guarded fixes** (doc updates, reference corrections): apply directly, report after
