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

## L-1 · 2026-07-13 · high · promoted
- **Lesson:** Skills shipped with autonomous-write defaults violating G9.I6 (`promote-findings --auto` to live KB, `translate-governance` act-then-report on governance files, `research-loop` finding writes, `watch-upstream` auto-Edit) — every skill write path needs a default-off flag or an explicit in-procedure gate; the 2026-06-12 audit filed remediation but it was never confirmed applied.
- **Owning surface:** `systems/improvement-loop/.claude/skills/{promote-findings,translate-governance,research-loop,watch-upstream}/SKILL.md`
- **Source:** SL `audit-system-il-second-canonical-run.md` + `audit-system-skill-shipped-metasystem-smoke-test.md` (2026-06-12); SL distill 2026-07-13
- **Occurrences:** 2026-06-12

## L-2 · 2026-07-13 · high · promoted
- **Lesson:** WebFetch-first repo location let a malware/impostor domain (mempalace.tech) and a parody repo nearly enter the KB — locate repos via `gh search repos` / `gh api` first, WebFetch second; never let an unverified domain into durable artifacts. Rule not yet in the skill's locate phase.
- **Owning surface:** `systems/improvement-loop/.claude/skills/repo-analyzer/SKILL.md`
- **Source:** SL `session-57-researcher-mempalace-supermemory.md` (2026-04-23; mis-reference originated s56)
- **Occurrences:** 2026-04-22, 2026-04-23

## L-3 · 2026-07-13 · normal · open
- **Lesson:** `allowed-tools` drifts from procedure steps, creating runtime-failure risk — `identify-artifacts` Step 7 back-annotation needs Edit (grant: Read Grep Glob Write Agent); `dimension-rebalance` Step 5B needs Write (grant: Read Grep Glob Edit). Both verified still missing 2026-07-13. Check allowed-tools against every procedure step when editing a SKILL.md.
- **Owning surface:** `systems/improvement-loop/.claude/skills/identify-artifacts/SKILL.md`, `systems/improvement-loop/.claude/skills/dimension-rebalance/SKILL.md`
- **Source:** SL `audit-system-il-second-canonical-run.md` (2026-06-12); grants re-verified in SL distill 2026-07-13
- **Occurrences:** 2026-06-12

## L-4 · 2026-07-13 · normal · promoted
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

## L-10 · 2026-07-16 · normal · open
- **Lesson:** `/detect-drift`'s predicate (finding `last_updated` > artifact `extraction_date`) permanently re-flags artifacts already re-extracted via `--update`, because DD-117 preserves `extraction_date` and records currency in `last_change_session`/`last_change_report` — the currency baseline must be max(extraction_date, last_change_report date), and orchestrators must check `last_change_*` before dispatching re-runs from a dated drift report (session 147 dispatched 6 redundant re-extraction subagents; 7 artifacts got erroneous date bumps, reverted pre-commit).
- **Owning surface:** `systems/improvement-loop/.claude/skills/detect-drift/SKILL.md`
- **Source:** session 147 (2026-07-16); drift report `operations/drift-reports/2026-07-13-source-drift.md` vs session-146 re-extractions (commits 242700e, b986afd)
- **Occurrences:** 2026-07-16

## L-11 · 2026-07-16 · normal · open
- **Lesson:** Presenting a kernel-doc section for gate approval as chat-only text failed — Nick reviews in the IDE and asked "where is the file? I need to read it." Gate-reviewed drafts must exist in the target file (clearly marked DRAFT with per-section status) before the approval question is asked; chat is not a review surface.
- **Owning surface:** `systems/improvement-loop/.claude/skills/vision-to-plan/SKILL.md` (section-drafting step)
- **Source:** session 148 (2026-07-16), Phase 4 interview Block A2 first gate
- **Occurrences:** 2026-07-16

## L-12 · 2026-07-18 · normal · open
- **Lesson:** A capability design note was presented as final on mechanism verification alone; Nick ruled the true evaluation is building the initial version and scoring its output against available ground truth ("the closer the discovery pass matches the links there, the more correct the skill" — the hand-curated LINKS.md batch). When a design's output has a checkable ground-truth corpus, the design step includes a v0 empirical eval before finalization; the eval also calibrated the spec (strict filter bar via six exemplar verdicts) in a way static review could not.
- **Owning surface:** `systems/improvement-loop/.claude/skills/design-skill/SKILL.md` (Phase 5 audit is static-only today)
- **Source:** session 150 (2026-07-18), YT-retrieval interlude; eval at `operations/research-reports/2026-07-18-watch-youtube-eval.md`
- **Occurrences:** 2026-07-18

## L-13 · 2026-07-19 · normal · open
- **Lesson:** zsh does not word-split unquoted scalar variables — a `for x in $list` loop runs once with the whole string, and passing `$files` unquoted hands one giant argument to the first command. Two same-session failures: a per-video dedup grep silently degenerated into one no-op query (a subtler case would have passed a false "no duplicates"), and a batch validation printed a phantom FAIL list. Rule: in this harness's Bash tool, iterate via `echo "$list" | tr ' ' '\n' | while read -r x` (or `find ... | while read`), never bare `$var` expansion.
- **Owning surface:** orchestrator shell practice (no skill file owns it yet; promotion target would be a workspace CLAUDE.md/rules line if it recurs across sessions)
- **Source:** session 151 (2026-07-18/19), wave-4 link-intake — dedup loop + staged-file validation loop, both re-run correctly in-session
- **Occurrences:** 2026-07-18

## L-14 · 2026-07-19 · normal · open
- **Lesson:** Pass 2 extraction planning derived from triage intake-path labels missed a video whose accepted verdict was "watched-library registration" but which carried a novel-pattern estimate (~3) — the patterns live in the transcript, not the repo registration. Caught at the registration-drafting step and fixed with a sixth extractor. Rule: any accepted verdict with a novel-pattern estimate ≥1 gets an extraction slot, regardless of intake path.
- **Owning surface:** `systems/improvement-loop/.claude/skills/link-intake/SKILL.md` (KB-ONLY metadata contract feeding Pass 2 planning)
- **Source:** session 151 (2026-07-18), wave-4 Pass 2 — Vercel Eve video (m8VC2SV2igM), batch-e dispatch
- **Occurrences:** 2026-07-18

## L-15 · 2026-07-19 · normal · open
- **Lesson:** `/extract-artifacts` Step 4.8's queue write-back can leave a row's Status field inconsistent with its own Resolution and the on-disk artifact — two independent instances: a session-146 extraction left `deletion-test-for-no-op-instructions`'s row at `nick-approved` (found and reconciled s152), and a session-152 batch lane wrote `Resolution: extracted to [[…]]` on three autonomous-queue rows while leaving Status `nick-approved`. Rule: after any batch of harvest-row promotions, run a deterministic consistency check (`Resolution: extracted…` ⇒ `Status: extracted`; artifact-on-disk ⇒ terminal Status) before committing; the write-back's summary-table and detail-block edits are two surfaces that must be verified together.
- **Owning surface:** `systems/improvement-loop/.claude/skills/extract-artifacts/SKILL.md` (Step 4.8 write-back)
- **Source:** session 152 (2026-07-19), harvest-queue sweep — autonomous-scheduled-agent-operation lane partial write-back (fixed pre-commit, dd9266b) + s146 drift on defending-agent-context row
- **Occurrences:** 2026-07-19
