---
name: Skill-Description Budget and Context-Overflow Triage
summary: Claude Code allocates ~1% of the model's context window to skill descriptions in the system prompt (configurable via skillListingBudgetFraction or SLASH_COMMAND_TOOL_CHAR_BUDGET). Per-entry combined
  description + when_to_use is capped at 1,536 characters (maxSkillDescriptionChars). When the budget overflows, descriptions for least-used skills are dropped first, names always retained. Skills can be
  set to "name-only" or "off" in skillOverrides to free budget. /doctor diagnoses overflow.
implementation_notes: 'Concrete numbers for a skill-rich session: at 1% of 1M-token context = 10K chars across all skill descriptions. With 1,536-char per-entry cap, that''s ~6-7 ''full'' descriptions.
  Past that, skills are listed name-only or descriptions truncated. The truncation is graceful (least-recently-used dropped first) but can strip the keywords Claude needs for matching. Operational discipline:
  trim description+when_to_use at the source, put the highest-signal use case first, and use skillOverrides to silence background-knowledge skills.'
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-claude-code-skills-docs.md
- hub-and-spoke-context-hub.md
related_findings:
- file: skill-md-frontmatter-as-discovery-trigger-primitive.md
  rel: extends
- file: skill-content-lifecycle-context-budget.md
  rel: same-problem
- file: hub-and-spoke-two-tier-skill-taxonomy.md
  rel: same-problem
- file: trigger-skip-grammar-peer-deferral-graph.md
  rel: extended-by
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
- rules/skill-description-char-caps.md
---

# Skill-Description Budget and Context-Overflow Triage

## What It Is

Skill descriptions sit in Claude Code's system prompt on every turn. Three configurable knobs govern how many fit:

- **`skillListingBudgetFraction`** (default `0.01` = 1% of context window) — total character budget for all skill descriptions combined.
- **`SLASH_COMMAND_TOOL_CHAR_BUDGET`** — environment-variable override for a fixed character budget.
- **`maxSkillDescriptionChars`** (default 1,536) — per-entry cap on `description` + `when_to_use` combined.

When the total budget overflows: names are always included, descriptions for least-recently-used skills are dropped first. Per-skill overrides (`skillOverrides` setting) can demote skills to `"name-only"` (name listed, description hidden), `"user-invocable-only"` (hidden from Claude entirely but still in `/` menu), or `"off"` (hidden everywhere).

`/doctor` diagnoses budget overflow and identifies affected skills.

## Why It Matters

This is the harness-level constraint that determines how many skills can coexist before triggering accuracy degrades. The math is concrete:
- At 1% of a 200K context window: ~2K chars across all descriptions.
- At 1% of 1M context: ~10K chars.
- At 1,536-char cap per entry: ~6-7 "full" descriptions fit in 10K.

Past the cap, descriptions get truncated and the keywords needed for skill matching may be stripped before Claude sees them. The skill seems to undertrigger but the actual cause is invisible.

Operationally this turns description authoring into a context-budgeting problem. "Put the key use case first" isn't aesthetic guidance — it's a survival rule when descriptions get truncated.

## Why People Are Using It

Documented in the Claude Code skills page Troubleshooting section. The fact that this knob is settable (and the cap is named in settings) is itself evidence that the failure mode happens at scale. The recommended diagnostic flow — `/doctor` to find overflow, set low-priority entries to `"name-only"` in `skillOverrides`, raise `skillListingBudgetFraction` for known-heavy sessions — implies real operational pressure.

## Potential Alternatives

Unlimited description budget (worse for short-context models). Names-only listing (loses semantic matching). External skill router (separate model that decides which skills to surface — adds latency and another failure mode). Lazy skill listing where descriptions are loaded on-demand (loses the always-loaded discovery property). Description-as-embedding match outside the prompt (more expressive but requires infrastructure).

## Potential Improvements

Per-project skill prioritization (this project leans on these 3 skills; preserve their descriptions). Skill clustering so related skills share a description budget. Compressed/condensed description rendering when budget is tight. A standardized description schema with a forced "trigger keywords" suffix that gets preserved even on truncation.

## Field Corroboration — Enterprise Context-Hub Two-Tier Caps (added 2026-07-12)

A private enterprise context-hub system (production skill library at a large enterprise;
author-shared writeup, repo private) independently converges on the same 1,536-char
number as a **hard authoring cap**, enforced by its whole-tree audit tooling on a
two-tier scale:

| Tier | Threshold | Severity | Rationale |
|---|---|---|---|
| Soft | > 1000 chars | Medium finding | Description is getting expensive (also an export/index cap in their stack) |
| Hard | > 1536 chars | High finding | Harness truncation risk — the router text may be cut |

Their sharpened version of the truncation failure mode: descriptions there end with
`SKIP: <case> → <sibling-id>` peer-deferral clauses, and truncation cuts the *tail* — so
what silently dies first is exactly the collision protection. That is why exceeding 1536
is treated as High severity rather than a style nit, and why their generated-artifact
contract requires new descriptions to fit ≤1000 chars at creation time.

Notably, the "skill clustering so related skills share a description budget" idea listed
under Potential Improvements above is exactly what that system ships as its hub-and-spoke
taxonomy (see `hub-and-spoke-two-tier-skill-taxonomy.md`): families of ≥8 skills
consolidate behind one hub description, and spokes are never indexed at all.

## Potential Failure Modes

**Silent undertriggering from truncation.** A skill present in the listing but with the critical "use when X" phrase truncated will appear to undertrigger for no obvious reason.

**Cascading description bankruptcy.** Adding one new skill triggers truncation of older descriptions, which silently degrades unrelated skill triggering accuracy.

**Project skills vs personal skills compete.** When personal skills override project skills under the budget cap, project-specific behavior is lost first.

**Override settings as load-bearing.** Once `skillOverrides` is used to manage budget, it becomes a config surface that has to be maintained. Skills added to a project may not be discovered until override settings are updated.

**`/doctor` is reactive, not preventive.** The user has to notice degraded behavior before checking the diagnostic. There's no automatic warning when the budget gets tight.

## Extraction Note — 2026-07-19
Extracted as **rule**: [[skill-description-char-caps]] in `extracts/rules/`
