---
name: Brainstorming as Mandatory Design Gate
summary: Superpowers enforces brainstorming before ANY implementation via HARD-GATE XML tags — no code, no scaffolding, no implementation actions until a design is presented and approved. 'This Is Too Simple
  To Need A Design' is explicitly listed as an anti-pattern.
implementation_notes: null
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: superpowers-plugin-spec-driven-sub-agent-orchestra.md
  rel: extends
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Brainstorming as Mandatory Design Gate

## What It Is
Superpowers enforces a mandatory brainstorming phase before any implementation using `<HARD-GATE>` XML tags in the skill definition: "Do NOT invoke any implementation skill, write any code, scaffold any project, or take any implementation action until you have presented a design and the user has approved it." This applies to every project regardless of perceived simplicity. The brainstorming follows specific rules: one question at a time, YAGNI ruthlessly applied, and "This Is Too Simple To Need A Design" is explicitly listed as an anti-pattern that must be resisted.

## Why It Matters
Premature implementation is one of the most common agent failure modes. Agents that jump to code before understanding the full scope produce work that must be reworked or discarded. The HARD-GATE is structural enforcement of "think before build" — not a suggestion or guideline, but a mechanically enforced constraint using XML tags that the agent cannot skip without explicit violation. The anti-pattern callout is notable: it anticipates the specific rationalization ("this is simple enough to skip design") and blocks it.

## Why People Are Using It
Observed in [Superpowers](https://github.com/obra/superpowers) v5.0.7 — see [[superpowers-analysis]] for structural details. The brainstorming phase produces a design that the human partner must approve before implementation begins. This creates a mandatory human gate at the design level — not just at the code review level. Compare: GSD's discuss-phase is optional and focuses on HOW (implementation approach), not WHAT (design); BMAD's brainstorming is user-activated (not mandatory for every task).

## Potential Alternatives
GSD's optional discuss-phase for implementation clarification. Plan-mode-first convention (MetaSystem's current approach via CLAUDE.md instruction). Pre-implementation checklists that the agent self-verifies. Human review only at PR time (post-implementation gate). Spec-first workflows where the spec is written before implementation but design exploration is not mandatory.

## Potential Improvements
Graduated gate strictness — trivial tasks (typo fixes, config changes) could use a lighter gate than feature work. Design template that structures the brainstorming output for consistent review. Time-boxing the brainstorming phase to prevent analysis paralysis on well-understood tasks. Integration with the rationalization prevention pattern to catch agents attempting to justify skipping the gate.

## Potential Failure Modes
Overhead on trivial tasks — mandatory brainstorming for a one-line config change adds friction without value. The human partner may rubber-stamp designs to move faster, defeating the gate's purpose. If the agent produces low-quality designs (vague or obvious), the brainstorming phase becomes ritual rather than substance. The XML-tag enforcement depends on the model respecting XML boundaries, which is not guaranteed across model versions.
