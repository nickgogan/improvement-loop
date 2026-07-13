---
title: "Proposal log — promotion audit trail"
type: "resource"
target_system:
  - "improvement-loop"
created: "2026-07-13"
---

# Proposal Log

Append-only audit of every promotion attempt out of `lessons.md` (IB-176; design note
§2). One entry per proposal, applied or declined — a declined proposal is signal
(often: owning surface misidentified), not failure. Rollback = git revert + a new
P-row; history is never rewritten. Applying commits carry `Refs: ops-self L-<seq>`.

**Entry contract:**

- Header: `## P-<seq> · YYYY-MM-DD · L-<seq> · applied|declined`
- Body fields: **Proposal** (one line), **Surface** (file edited), **Diff summary**,
  **Grade** (binary rubric from the fresh-context assessor: grounded / minimal /
  effective / non-regressive), **Ruling** (Nick's decision + any note).

## Entries
