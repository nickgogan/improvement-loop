---
id: "il-stream-0-step-e-ask-kb-compare-repos-authored"
title: "IL Stream 0 Step E — /ask-kb and /compare-repos authored under Librarian ownership"
date: "2026-06-11"
session: 111
system: "improvement-loop"
type: "milestone"
agents:
  - "Librarian"
  - "Owner"
tags:
  - "stream-0"
  - "librarian"
  - "ask-kb"
  - "compare-repos"
  - "repo-analyzer-deprecation"
  - "rule-10"
  - "rule-11"
  - "rule-12"
related_artifacts:
  - ".claude/skills/ask-kb/SKILL.md"
  - ".claude/skills/compare-repos/SKILL.md"
  - ".claude/skills/repo-analyzer/SKILL.md"
  - "agents/librarian/agent.md"
  - "CLAUDE.md"
  - "operations/references/consumer-abstractions-map.md"
roadmap_step: "Stream 0 Step E"
---

# IL Stream 0 Step E — `/ask-kb` and `/compare-repos` Authored

## Summary

Cross-system roadmap step E landed. Both Librarian-owned skills authored as
first-class IL skills, both operationalizing existing substrate without new
concept docs. `/repo-analyzer --compare` deprecated and consolidated into
`/compare-repos` to enforce the Researcher (per-repo) vs Librarian
(cross-repo) disposition split. No new IB items; no DD created; no new
governance rules.

## Gate Decisions

Three open decisions were proposed with rule 11 / rule 10 evidence and
gated by Nick. Recommended answers were accepted on all three.

### Decision 1 — Concept-doc treatment

**Ruling: No new concept docs in `operations/references/librarian/`.**

Rationale (rule 11):

- The bilingual concept-doc pattern (`skill.md`, `agent.md`) is specifically
  for **artifact-type substrate** read bilingually by `/assess-*` and
  `/design-*` operations. Neither `/ask-kb` nor `/compare-repos` is an
  artifact-type operation; both are query/analysis operations on the KB.
- `consumer-abstractions-map.md` inventories the abstractions IL maintains
  substrate for. KB-query and cross-repo-comparison are not in the map
  and carry no consumer demand signal for promotion.
- `/ask-kb` substrate fully exists in `agents/librarian/agent.md` —
  Teacher and Builder mode definitions, triggers, cognitive approaches,
  output shapes, and example interactions. The skill operationalizes
  that, not new substrate.
- `/compare-repos` substrate exists in `/repo-analyzer` Step 10 —
  comparison matrix shape, pattern clusters, findings candidates
  structure. The skill consolidates and extends it; no abstraction over
  the structure is warranted.

**Rule 12 implication:** Without concept docs there is no §Composition /
§Construction pair to maintain. Rule 12 non-applicable for either skill.

### Decision 2 — Rule 10 applicability (generator-assessor separation)

**Ruling: Rule 10 does not apply to either skill.**

Rationale:

- Rule 10 fires on "constructive skill that includes a quality check" —
  the constructive operation produces an artifact with a spec to be
  assessed against (e.g., `/design-skill` produces a SKILL.md with the
  `/assess-skill` audit rubric).
- `/ask-kb` is read-only synthesis. No artifact spec; no assessor peer.
  Internal invariants (citation grounding, gap honesty, KB-scope
  discipline) live in the skill's Rules section, not as external
  assessor concerns.
- `/compare-repos` produces an analytical comparison report, not a
  deployable artifact-type artifact. Its quality concerns (citation
  fidelity, pattern threshold discipline, contradiction handling) are
  internal procedural rules.

**Implication:** No `/assess-kb-query` or `/assess-comparison` peer is
warranted. No new assessor-skill IB items.

### Decision 3 — `/repo-analyzer --compare` disposition

**Ruling: Deprecate `--compare` mode; consolidate to `/compare-repos`.**

Rationale:

- Disposition mismatch in current `/repo-analyzer --compare`:
  `/repo-analyzer` is a Researcher skill (structural cartographer,
  descriptive, not prescriptive). Cross-repo comparison with
  consumer-oriented synthesis is a Librarian Builder-mode operation.
- Clean split:
  - `/repo-analyzer`: per-repo structural analysis only (Researcher).
  - `/compare-repos`: cross-repo synthesis + Librarian Builder-mode
    recommendations on top of `/repo-analyzer`'s per-repo output
    (Librarian).
- Migration cost is low: comparison Step 10 structure migrates wholesale
  into `/compare-repos`. The `--compare` flag in `/repo-analyzer` now
  short-circuits with a redirect message.

## Changes Landed

### New files

- `systems/improvement-loop/.claude/skills/ask-kb/SKILL.md` — first-class
  Librarian KB-query surface. Teacher/Builder mode selected by query
  shape (or `--mode` override). Read-only; cites every claim; surfaces
  gaps and contradictions honestly. No assessor delegation.
- `systems/improvement-loop/.claude/skills/compare-repos/SKILL.md` —
  Librarian cross-repo synthesis. Reads per-repo `*-analysis.md`,
  watched-library entries, and relevant findings. Produces structural
  matrix, pattern clusters, findings candidates; optional Builder-mode
  recommendation set on `--focus`. Write to
  `watched-libraries/analysis/cross-repo-comparison.md` is opt-in via
  `--write` and approval-gated.

### Edited files

- `systems/improvement-loop/.claude/skills/repo-analyzer/SKILL.md` —
  `--compare` removed from primary `argument-hint`; retained in
  Arguments table as DEPRECATED with redirect to `/compare-repos`;
  Step 0 short-circuits on `--compare`; Step 10 marked deprecated with
  reference-only retention.
- `systems/improvement-loop/CLAUDE.md` — Librarian Skills table extended
  with `/ask-kb` and `/compare-repos` (drift-prevention from session 110
  pattern).
- `systems/improvement-loop/agents/librarian/agent.md` — Skill Inventory
  table extended; "Future skill candidates" section removed (both
  candidates now active).
- `PROGRESS.md` (workspace) — step E marked Done; step F marked In
  progress (next session 112). Priority queue item 1 advanced to step F.
- `systems/improvement-loop/PROGRESS.md` — Current Focus updated to
  step F; session 111 close summary added.

## Rules Surfaced / Reinforced

- **Rule 11 in action.** Both skills could have superficially justified
  new concept docs by symmetry with the `/design-*` and `/assess-*`
  pattern. Rule 11 forced an evidence test (recurring concrete problem
  observed 2-3+, multi-consumer benefit, observable cost of absence).
  None met the bar. Decision: tolerate the asymmetry; concept docs are
  for artifact-type substrate, not for query/analysis operations.
- **Rule 10 scope clarified.** Generator-assessor separation applies to
  *constructive operations producing artifacts with deployable specs*,
  not to read-only synthesis or analytical reporting. The skill's
  internal invariants (citation grounding, etc.) are not the same as an
  external audit rubric.
- **Disposition-driven skill ownership.** The `/repo-analyzer --compare`
  case shows that mode flags can hide cognitive-disposition mismatches.
  Splitting Researcher (per-repo descriptive) from Librarian (cross-repo
  Builder-mode prescriptive synthesis) is cleaner per-skill and clearer
  for consumers.

## Outstanding / Logged-for-Future

No new IB items filed. Pre-existing logged-for-future items unchanged.

## Boundary-Case Encounters

None logged this session.

## Next

Roadmap step F — MetaSystem structural setup, instantiate MetaSystem
Owner (IB-167), create MetaSystem capability roadmap. Session 112
handoff to be generated via `/session-handoff`.
