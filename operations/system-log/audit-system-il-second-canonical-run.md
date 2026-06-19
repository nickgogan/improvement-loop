---
id: "audit-system-il-second-canonical-run"
title: "/audit-system second canonical run on IL; 4 G9.I6 violations surfaced; audit-trail patch + MOC pre-filter shipped; design contract → stable"
date: "2026-06-12"
session: 115
system: "meta-system"
type: "milestone"
agents:
  - "Owner"
tags:
  - "step-g"
  - "audit-system"
  - "il-audit"
  - "second-canonical-run"
  - "g9-i6"
  - "moc-classifier"
  - "audit-trail"
  - "rule-11"
related_artifacts:
  - ".claude/skills/audit-system/SKILL.md"
  - "project-management/design-notes/2026-06-12-audit-system-design-contract.md"
  - "audit-reports/2026-06-12/manifest.md"
  - "../../improvement-loop/audit-reports/2026-06-12/manifest.md"
  - "../../improvement-loop/audit-reports/2026-06-12/findings.md"
  - "../../improvement-loop/audit-reports/2026-06-12/summary.md"
roadmap_step: "Cross-system Step G (audit-system stable; design-harness next)"
---

# `/audit-system` v1 second canonical run — IL audit

Session 115 ran `/audit-system systems/improvement-loop/ --write`. 43 artifacts
across 3 shapes (32 skills, 4 fractal agents, 7 CLAUDE.md), bin-packed into 9
parallel Librarian subagents at the 250k-token ceiling. ~7 minutes wall-clock
for full dispatch + aggregation.

## Outcomes by deliverable

### 1. IL audit reports written

`systems/improvement-loop/audit-reports/2026-06-12/{manifest,findings,summary}.md`
landed. Coverage: 36 of 43 artifacts assessed (24 verbatim from persisted
output, 12 structured digests from visible-stream output). 7 unassessed due to
bin 2 and bin 4 partial output (see §"v2 candidate" below).

### 2. Critical findings in IL

**4 G9.I6 violations (deployment-blocking)**:

- `promote-findings`: `--auto` flag autonomously promotes all non-duplicate
  findings into the live KB. No dry-run, no confirmation. HARD-BLOCKING.
  Highest-violation skill in the audit (8 Violated outcomes).
- `translate-governance`: Rule 1 explicitly encodes "do not wait for approval
  before writing" — act-then-report inverts HITL ordering on governance-source
  files.
- `research-loop`: writes new findings/sources/authorities without any
  in-procedure HITL gate; external review is unenforced.
- `watch-upstream`: Step 4 executes `Edit` on watched-libraries automatically
  after Step 2 subagent triage; no human gate between triage and execution.

**2 runtime-failure risks** (allowed-tools / procedure mismatch):

- `dimension-rebalance`: `Write` called in Step 5B but absent from `allowed-tools`.
- `identify-artifacts`: `Edit` needed for Step 7 finding frontmatter updates but
  absent from `allowed-tools`.

**3 G9.I6 SATISFIED exemplars** (imitate these): `finding-crosslink`,
`cleanup-cache`, `compare-repos`.

These findings are IL Owner stewardship items — MetaSystem does not cross
system boundaries to fix them. Filed for IL Owner attention.

### 3. Audit-trail patch (resolves session-114 finding #22)

`/audit-system` SKILL.md Step 7 now appends a one-line run-record to
`<target>/audit-reports/runs.md` on each `--write` invocation:

```
2026-06-12  session-115  artifacts=43  bins=9  critical=4  missing=7  variant=il-audit
```

Rule-11-minimal: one line per run, no schema enforcement, no rotation. File
created on first write with header `# Audit run log — append-only`.

### 4. MOC pre-filter committed (rule-11 trigger met)

Recurrence evidence: session-114 MetaSystem (3 confirmed MOCs) + session-115 IL
(3 confirmed + 3 strongly-suspected MOCs in unaudited bin 4 — word counts
55–78, sub-100). Cumulative ≥6 MOC-shape CLAUDE.md latents across 2 systems.

SKILL.md now includes a §"MOC pre-filter for CLAUDE.md" that runs at discovery
time. A CLAUDE.md is skipped (recorded as MOC in manifest, not dispatched) if
**either**:
1. Frontmatter has `type: "index"`, OR
2. Body word count < 100 (excluding frontmatter).

`--include-mocs` flag overrides the filter. Wired through `argument-hint` →
Step 0 parse → Step 1 filter → Step 2 sizing (excludes skipped) → Step 4
`## Skipped — MOC` manifest block → Step 5 dispatch (skipped artifacts not in
any bin).

### 5. Design contract stage advanced `stable-after-il-test → stable`

Two systems audited at scale, two patches landed, real findings surfaced,
exemplar skills identified. The contract is stable. Updated stage and Status
section.

## v2 candidate (not patched this session)

**Partial-output regression in bins 2 and 4**: each emitted only 1 of N
expected sentinel-delimited reports. Pattern: the LAST artifact in dispatch
order was the one received; earlier artifacts in the same bin were lost.

Hypothesis: bins containing the largest-output skills (extract-artifacts
10,314 words, synthesize-guide 7,228 words, repo-analyzer 3,049 words, plus
the substantive IL CLAUDE.md root at 1,957 words) hit the subagent's
single-message output budget. The subagent likely emitted progress per
artifact, and only the final message survived the orchestrator's read.

Spawn-payload tweaks alone are unlikely to fix this. The substantive v2 fix
is a per-bin total-output budget — bin packing must constrain expected report
volume, not just input footprint. Logged in design contract; revisit if
recurrence on the next audit target (e.g., MetaSystem in incubator/, or a
graduated incubator system).

## What is not done this session

- **No `/design-harness` work**. Sequenced after `/audit-system` ships stable
  (achieved this session). Session 116+ scope.
- **No cross-boundary writes to IL substrate**. IL findings are filed; IL Owner
  stewards remediation.
- **No new DDs**. Surface candidates only — Nick gates DD filing.
- **No promotion of rules 10/11/12 to MetaSystem constitution**. Held for
  second cross-system instance per session-114 deferral.

## Key references

| Artifact | Path |
|---|---|
| Patched SKILL.md | `.claude/skills/audit-system/SKILL.md` |
| Design contract | `project-management/design-notes/2026-06-12-audit-system-design-contract.md` |
| IL audit reports | `../../improvement-loop/audit-reports/2026-06-12/` |
| MetaSystem audit reports (session 114) | `audit-reports/2026-06-12/` |
| Session 114 SL entry | `operations/system-log/audit-system-skill-shipped-metasystem-smoke-test.md` |
