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

## P-1 · 2026-07-13 · L-1 · applied
- **Proposal:** G9.I6 write-gate remediation across the four autonomous-write skills flagged by the 2026-06-12 audit.
- **Surface:** `.claude/skills/{promote-findings,translate-governance,research-loop,watch-upstream}/SKILL.md`
- **Diff summary:** promote-findings — `--auto` collapses per-candidate selection into one batch-confirmation gate (arguments row, Step 3, Rule 1, disposition bullet); translate-governance — Rule 1 flipped Guarded/act-then-report → Proposal-first, Step 4 presents planned docs before Write/Edit; research-loop — findings-write gate at Pass 1 Step 3 (inherited by Pass 2 + arXiv) and at Periodic Web Scan Step 4 (agent-discovered URLs: sources gated too; user-supplied URLs authorize their own source entries); watch-upstream — explicit-approval gate between Step 3 triage and Step 4 edits (no approval = `--dry-run` behavior).
- **Grade:** grounded yes / minimal yes / effective yes / non-regressive yes (fresh-context assessor; 1 revise cycle — cycle-1 grade caught the ungated Periodic Web Scan write path).
- **Ruling:** applied — ruled by the agent under Nick's delegated-judgment grant (this session, "trusting your judgement"); skill surfaces only, no governance files touched.

## P-2 · 2026-07-13 · L-2 · applied
- **Proposal:** gh-first repo location rule in `/repo-analyzer`'s locate phase.
- **Surface:** `.claude/skills/repo-analyzer/SKILL.md`
- **Diff summary:** Step 0 item 3 extended — missing/ad-hoc `repo_url` is located via `gh search repos` / `gh api` with owner/description/stars identity check before any WebFetch; unverified domains never enter durable artifacts (mempalace.tech incident cited).
- **Grade:** grounded yes / minimal yes / effective yes / non-regressive yes (fresh-context assessor, no revise cycles).
- **Ruling:** applied — ruled by the agent under Nick's delegated-judgment grant (this session).

## P-3 · 2026-07-13 · L-4 · applied
- **Proposal:** tallies-from-enumeration rule at `/identify-artifacts` report assembly.
- **Surface:** `.claude/skills/identify-artifacts/SKILL.md`
- **Diff summary:** Step 4 gains item 5 — Summary-table tallies and header counts computed from the assembled enumeration at write time, never serialized from memory; downstream consumers filter by marker (Status, tier), not by count.
- **Grade:** grounded yes / minimal yes / effective yes / non-regressive yes (fresh-context assessor, no revise cycles).
- **Ruling:** applied — ruled by the agent under Nick's delegated-judgment grant (this session).
