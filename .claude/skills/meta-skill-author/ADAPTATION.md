# Engine adaptation — meta-skill-author in MetaSystem

> **Downstream copy.** Upstream source: `nickgogan/CareerBuddy`
> `.github/skills/meta-skill-author` @ **1.15.0** per its CHANGELOG (imported
> 2026-07-12, session 133). Upstream inconsistency noted at import: upstream
> SKILL.md `metadata.version` lags at 1.14.0 — report upstream on next exchange.
> Import discipline: the skill's own §4.0 Port model — Claude Code is stage-2 target;
> per `adapters/claude.md`, Claude Code is the reference implementation and provides
> every `capability-contract.yaml` row natively, so the whole package imports intact.
> The SKILL.md body is kept **upstream-diffable**: engine-specific rules live here, not
> inline. Re-derive check: diff against upstream before adopting upstream releases.

## What was changed at import (complete list)

1. `agents/{grader,comparator,analyzer}.md` — the authoritative-rubric pointer
   `<REPO>/.github/skills/meta-skill-author/…` rewritten to
   `<REPO>/systems/improvement-loop/.claude/skills/meta-skill-author/…`.
2. `SKILL.md` frontmatter — `allowed-tools` gains `Bash(bash*)` (upstream's
   `Bash(python*)` never covered its own `scripts/validate.sh`, a bash script);
   `metadata.upstream` + `metadata.imported` provenance fields added.
3. This file.

Nothing else was modified. Platform mentions of GitHub Copilot / `.github/` layouts in
the body, adapters, and references are cross-platform method content, not workspace
bindings — left intact.

## Engine-context overlay (how this skill runs here)

- **Home & registration:** engine-scoped at
  `systems/improvement-loop/.claude/skills/` (DD-109). Registered in the engine
  CLAUDE.md skills listing.
- **Capability mapping (contract → this harness):** human-approval-channel = Nick
  inline (required — the spec-first gate is DD-29/human-gate aligned by construction);
  script-execution = Bash tool; fresh-context-scoring = subagents (`context: fork` /
  Agent tool); versioned-checkpoints = git; reference-bundle-attachment = L3
  progressive disclosure.
- **Generator-assessor separation (§3.1) meets engine rule 10:** the Grader/Comparator/
  Analyzer subagent specs in `agents/` satisfy rule 10 natively. Where the engine
  already has a dedicated assessor, prefer it: `/assess-skill` for Contract-derived
  audits of engine/consumer skills, `/prompt-evaluator` for the four-discipline rubric
  (§2.2's four disciplines are the same four — Prompt Craft, Context, Intent,
  Specification). This package's `references/audit-rubric.md` remains authoritative for
  its *own* modes' scoring anchors.
- **Frontmatter authoring here follows DD-114** (block-scalar convention; the pre-commit
  YAML linter enforces) on top of §1.4's rules.
- **Governance tier:** skills are executable policy; §5.2's hard rule (governance
  mutations = human-required) maps to the engine's Nick-gate. Local commits at
  checkpoints are fine; push is Nick-gated (workspace rule).

## Known overlap (flagged for the Phase 2 substrate audit — not resolved here)

`meta-skill-author` (Design/Eval/Improve/Port, platform-generalist, eval-loop tooling)
overlaps the Librarian pair `/design-skill` + `/assess-skill` (KB-grounded,
Contract-derived, engine-native). Both stand until the restructure program's Phase 2
audit rules on consolidation vs. composition (candidate ruling: meta-skill-author owns
eval/port tooling; Librarian pair owns KB-grounded design/audit; Design-mode drafts get
a `/assess-skill` pass). Do not merge or retire either side without Nick's gate.
Plan of record: `operations/plans/2026-07-12-engine-restructure-program.md`.

## First acceptance target

Redesign/improve the YouTube-intake capability (`/transcript-fetcher`, and its seam
with `/research-loop` Pass 2) via Design/Improve mode — Nick's directive, 2026-07-12.
