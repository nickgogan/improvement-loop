---
title: "Query log — demand ledger"
type: "resource"
target_system:
  - "improvement-loop"
created: "2026-07-13"
---

# Query Log — Demand Ledger

One row per incoming intent (IB-176; design note §3). Raw capture lands in the
gitignored `.query-capture.jsonl` buffer via the `UserPromptSubmit` hook;
`/self-improve` scan mode distills buffer lines into rows here. Multi-intent queries
get one row each. Outcome: `served` (routed and answered), `partial` (answered with
gaps or ad-hoc workarounds), `unserved` (no surface could serve it).

Recurring `partial`/`unserved` themes surface in scan mode and become IB proposals
through the promotion gate. The ledger doubles as the ground-truth routing corpus for
the future implicit-routing harness.

| Seq | Date | Query gist | Route | Why | Outcome |
|---|---|---|---|---|---|
