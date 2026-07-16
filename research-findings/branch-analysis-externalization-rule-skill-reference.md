---
name: Branch Analysis — the Externalization Decision Rule for Skill Reference Material
summary: 'Plain English: everyone agrees SKILL.md should be small and reference material should

  move to separate files — but nobody says *which* material moves. Pocock supplies the

  operative test: enumerate the skill''s branches (the distinct ways it can be used), then

  keep reference material used on every branch inline and move material used on only some

  branches behind context pointers ("external references"). Underneath sits a two-unit

  anatomy — every skill is steps (the procedure) plus reference (supporting material a step

  needs); either unit can be empty. His to-PRD skill has one branch, so both its reference

  blocks (test-seam explainer, PRD template) stay inline; domain-modeling has 2-3 branches

  (glossary update, ADR creation, or neither), so both templates move behind pointers.'
implementation_notes: 'Rubric-relevant for /assess-skill (structure criteria): today''s checks say "keep SKILL.md

  small / use progressive disclosure"; this gives the checkable refinement — "is any inline

  reference block used on only some branches?" (should be external) and its inverse "is any

  every-branch reference externalized?" (pays a pointless read round-trip). Nick-gated

  restructure Phase 2 decides substrate entry.'
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- IL (assess-skill/design-skill substrate)
- General
adopted_in: []
sources:
- building-great-agent-skills-the-missing-manual.md
related_findings:
- file: skill-as-directory-progressive-disclosure-three-levels.md
  rel: extends
- file: skill-authoring-four-guidelines.md
  rel: extends
- file: reference-only-skill-shape-for-afk-agents.md
  rel: extended-by
- file: skill-pruning-failure-modes-noop-deletion-test.md
  rel: extended-by
- file: disclosure-granularity-decision-rubric.md
  rel: same-problem
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
---

# Branch Analysis — the Externalization Decision Rule for Skill Reference Material

## What It Is

A decision rule for skill structure, built on a two-unit anatomy:

- **Steps** — the step-by-step procedure the skill walks through.
- **Reference** — supporting material the steps need (templates, explainers, standards).

A skill can be steps-only, reference-only, or both. The structural question is where each
piece of reference lives, and the rule is **branch analysis**: enumerate the branches — the
distinct ways the skill can be used or the mutually exclusive things it can do — and:

- Reference used on **every branch** stays inline in SKILL.md (externalizing it just adds
  a read round-trip that always happens).
- Reference used on **only some branches** moves behind a context pointer — a one-line "if
  you need X, read `<file>`" pointing at a markdown file bundled in the skill folder (an
  *external reference*).

Worked examples: `to-PRD` (three steps: find context → confirm test seams with user →
write PRD) has one branch; its test-seam explainer and PRD template are needed every run,
so both belong inline. `domain-modeling` does two different things (update a context.md
glossary; create ADRs) or neither — 2-3 branches — so the ADR and context.md templates move
behind pointers.

## Why It Matters

Progressive disclosure findings in the KB establish the *mechanism* (three-level loading,
references/ folders) and the *imperative* (keep SKILL.md under budget); Anthropic's
"structure for scale" guideline gestures at it ("if certain contexts are mutually
exclusive... keep the paths separate"). Branch analysis converts that into a per-block,
binary decision an auditor can apply to any skill without judgment calls: list branches,
tag each reference block with the branches that use it, externalize the partial ones. That
is precisely the shape `/assess-skill` structure checks want — and the same enumeration
doubles as a `/design-skill` construction step before any reference file is created.

## Why People Are Using It

Pocock cites it as the main answer to "how do you get your skills so small," alongside the
pruning discipline. Encoded in his writing-great-skills meta-skill; his repo (~160K stars)
applies it throughout.

## Potential Alternatives

Size-threshold-only rules ("split when over 500 lines") — say when to split, not what.
Always-externalize conventions (every template in references/) — clean but pays read
round-trips on single-branch skills. Usage-telemetry-driven splitting (observe which
sections actually load) — stronger evidence, much heavier machinery.

## Potential Improvements

Branch annotation as skill metadata (declare branches in frontmatter; lint reference
placement against them). Interaction with compaction budgets: inline reference counts
against the skill's surviving first-5K tokens, which sharpens the case for externalizing
partial-branch material.

## Potential Failure Modes

- **Branch miscounting**: treating input variations as branches (over-externalizing) or
  missing genuinely exclusive modes (under-externalizing).
- **Pointer non-follow**: an external reference is a context pointer, and models sometimes
  decline to follow pointers — critical every-branch material behind a pointer is a
  reliability bug, which is exactly why the rule keeps it inline.
- **Drift across files**: externalized templates version separately from the steps that
  use them; single-source-of-truth discipline has to span the skill folder, not just
  SKILL.md.
