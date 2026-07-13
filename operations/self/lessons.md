---
title: "Lessons — append-only operational lesson store"
type: "resource"
target_system:
  - "improvement-loop"
created: "2026-07-13"
---

# Lessons

Append-only lesson store (IB-176; design:
`project-management/design-notes/2026-07-13-memory-system-design.md` §2). Written by
`/self-improve` capture mode and the `/session-handoff` lessons-check sweep. Validated
by `store_check.py` in the pre-commit hook.

**Entry contract:**

- Header: `## L-<seq> · YYYY-MM-DD · high|normal · open|promoted|declined|pruned`
- Body fields (all required): **Lesson** (one line — what went wrong and the rule that
  prevents it), **Owning surface** (which file, if edited, prevents recurrence),
  **Source** (session ref, commit sha, artifact path, or `Q-<seq>`), **Occurrences**
  (comma-separated dates).
- Identity = (owning surface, failure pattern). Recurrence appends a date to
  Occurrences — never a duplicate entry.
- Untraceable lesson = invention: no Source, no entry.
- Retirement is a status change (`pruned`/`declined`), never deletion — git is the
  archive.
- Severity: `high` = data loss, governance breach, or user-visible failure (promotes
  at N=1); `normal` promotes at N=2. Severity is never silently lowered.

## Entries

## L-1 · 2026-07-13 · high · open
- **Lesson:** Skills shipped with autonomous-write defaults violating G9.I6 (`promote-findings --auto` to live KB, `translate-governance` act-then-report on governance files, `research-loop` finding writes, `watch-upstream` auto-Edit) — every skill write path needs a default-off flag or an explicit in-procedure gate; the 2026-06-12 audit filed remediation but it was never confirmed applied.
- **Owning surface:** `systems/improvement-loop/.claude/skills/{promote-findings,translate-governance,research-loop,watch-upstream}/SKILL.md`
- **Source:** SL `audit-system-il-second-canonical-run.md` + `audit-system-skill-shipped-metasystem-smoke-test.md` (2026-06-12); SL distill 2026-07-13
- **Occurrences:** 2026-06-12

## L-2 · 2026-07-13 · high · open
- **Lesson:** WebFetch-first repo location let a malware/impostor domain (mempalace.tech) and a parody repo nearly enter the KB — locate repos via `gh search repos` / `gh api` first, WebFetch second; never let an unverified domain into durable artifacts. Rule not yet in the skill's locate phase.
- **Owning surface:** `systems/improvement-loop/.claude/skills/repo-analyzer/SKILL.md`
- **Source:** SL `session-57-researcher-mempalace-supermemory.md` (2026-04-23; mis-reference originated s56)
- **Occurrences:** 2026-04-22, 2026-04-23

## L-3 · 2026-07-13 · normal · open
- **Lesson:** `allowed-tools` drifts from procedure steps, creating runtime-failure risk — `identify-artifacts` Step 7 back-annotation needs Edit (grant: Read Grep Glob Write Agent); `dimension-rebalance` Step 5B needs Write (grant: Read Grep Glob Edit). Both verified still missing 2026-07-13. Check allowed-tools against every procedure step when editing a SKILL.md.
- **Owning surface:** `systems/improvement-loop/.claude/skills/identify-artifacts/SKILL.md`, `systems/improvement-loop/.claude/skills/dimension-rebalance/SKILL.md`
- **Source:** SL `audit-system-il-second-canonical-run.md` (2026-06-12); grants re-verified in SL distill 2026-07-13
- **Occurrences:** 2026-06-12

## L-4 · 2026-07-13 · normal · open
- **Lesson:** Report summary tallies serialized from memory rather than recomputed from the authoritative enumeration block miscount — compute tallies from the enumeration at write time; filter by marker, not by count.
- **Owning surface:** `systems/improvement-loop/.claude/skills/identify-artifacts/SKILL.md` (report-assembly step; same rule for any report-emitting skill)
- **Source:** SL `session-62-codifier-ib-149-reassess.md` (2026-04-24), `session-76-codifier-phase-3-ib-execution.md` (2026-04-26)
- **Occurrences:** 2026-04-24, 2026-04-26

## L-5 · 2026-07-13 · normal · open
- **Lesson:** Multi-artifact subagent bins with large expected report volume emitted only the last sentinel-delimited report (7 of 43 artifact reports lost) — bin packing must budget expected output volume, not just input footprint. Known unfixed v2 candidate.
- **Owning surface:** `systems/improvement-loop/.claude/skills/audit-artifacts/SKILL.md`
- **Source:** SL `audit-system-il-second-canonical-run.md` (2026-06-12)
- **Occurrences:** 2026-06-12

## L-6 · 2026-07-13 · normal · open
- **Lesson:** Agent-proposed tasks carried forward in handoffs/backlogs look identical to Nick-sanctioned ones and accumulate formalization weight (Bucket D rolled 3 handoffs before being killed) — carried-forward work must cite its origin and be premise-checked before expensive execution. Rule lives in agent memory but not in the carry-forward surface itself.
- **Owning surface:** `.claude/skills/session-handoff/SKILL.md` (owns the PROGRESS.md carry-forward surface)
- **Source:** SL `session-60-researcher-killed-bucket-d-deleted-next-scan-notes.md` (2026-04-23)
- **Occurrences:** 2026-04-23

## L-7 · 2026-07-13 · normal · open
- **Lesson:** Parallel/aborted sessions left untracked artifacts, a mis-slugged rule file, and numbering collisions needing dedicated reconciliation — at session start, reconcile working-tree state against the last commit before producing new artifacts.
- **Owning surface:** `.claude/skills/session-handoff/SKILL.md` (session boundary owner)
- **Source:** SL sessions 81/83/84 entries (2026-04-27)
- **Occurrences:** 2026-04-27 (three sessions, same day)

## L-8 · 2026-07-13 · normal · open
- **Lesson:** An IL-scoped DD was propagated to workspace-root governance and reverted — check a DD's declared `target_system` against the intended rule's blast radius before editing, as a pre-flight step.
- **Owning surface:** `systems/improvement-loop/.claude/skills/translate-governance/SKILL.md`
- **Source:** SL `session-55-owner-workspace-governance-propagation.md` addendum (2026-04-22)
- **Occurrences:** 2026-04-22

## L-9 · 2026-07-13 · normal · open
- **Lesson:** `/extract-artifacts` Step 5 back-annotation silently failed once (10 findings stuck `raw` with extracts written) — deliberately not hardened per tolerate-one-off; ruled trigger: on second occurrence, file a hardening IB.
- **Owning surface:** `systems/improvement-loop/.claude/skills/extract-artifacts/SKILL.md` (Step 5)
- **Source:** SL `session-66-codifier-ib-150-acceptance-test.md` (2026-04-26; incident from 2026-04-19 batch)
- **Occurrences:** 2026-04-19
