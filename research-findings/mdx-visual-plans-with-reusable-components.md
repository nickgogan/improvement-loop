---
name: "MDX Visual Plans with Reusable Components (/visual-plan)"
summary: |-
  Builder.io's open-source /visual-plan skill renders agent plans as MDX built from a
  library of reusable interactive components — pan/zoomable wireframes, diagrams,
  commentable API specs, schema-change views, annotated code — instead of markdown walls
  or one-off generated HTML. Reusable components give consistency across runs, models,
  and agents ("not random HTML slop every time"), look sane checked into a repo, and are
  customizable/forkable. The human comments on wireframes and answers open questions
  visually before the agent works.
implementation_notes: |-
  Strongest input yet for the parked governance-visualization session (IB-175): Nick has
  flagged that prose-heavy DDs/plans make human gating expensive, and this is a working
  open-source answer — plans rendered from a bounded component library rather than
  freeform HTML. The /visual-plan repo is a watched-library candidate (Nick's call, not
  actioned here). Adopting an MDX toolchain on first occurrence would fail
  abstractions-earn-their-keep; extract the pattern, defer the toolchain.
category: "Tool Integration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "introducing-visual-plan-rich-plans-for-claude-code-codex.md"
related_findings:
  - file: "plan-level-as-engineering-reasoning-abstraction.md"
    rel: "extends"
  - file: "html-output-as-human-in-the-loop-restorer.md"
    rel: "extends"
  - file: "html-mockup-generation-as-brainstorm-artifact.md"
    rel: "same-problem"
  - file: "visual-recap-post-execution-mirror-artifact.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-07-13"
last_updated: "2026-07-13"
pipeline_status: "raw"
consumed_by: []
---

# MDX Visual Plans with Reusable Components (/visual-plan)

## What It Is

A skill (plus CLI and GitHub Action, all open source) that makes Claude Code / Codex
generate plans as MDX documents composed from reusable interactive components:

- pan-and-zoomable wireframes the human can comment on and iterate before execution
- diagrams and schema-design-change views
- interactive, commentable API specs
- annotated code blocks

The explicit format progression is markdown → HTML → **MDX**. The author credits the
"HTML is better than markdown" insight (Derrick, Anthropic) but identifies HTML's
failure modes: slow and verbose to generate, ugly checked into a repo, and structurally
different every time — "generating honestly kind of HTML slop every time." Reusable
components fix all three: faster generation, repo-friendly raw files, and consistency
even when you change agents or models. The component library is customizable and
forkable.

Workflow: review the wireframe first, comment, iterate, answer open questions visually
— then let the agent work.

## Why It Matters

This is the concrete mechanism for plan-level reasoning: the plan artifact becomes
navigable and visual enough that the human gate actually engages with it, at exactly
the point (pre-execution) where catching "that's not what I had in mind" is cheapest.
The reusable-component constraint is the novel part relative to the existing
HTML-output findings — it bounds generation variance, which is what makes the format
sustainable across models and reviewable as diffs.

For the engine: DDs, identification reports, and plans are all prose-heavy markdown
that Nick must gate. A bounded component vocabulary for those artifacts is the same
move at governance altitude.

## Why People Are Using It

Builder.io ships it as their own working workflow, open-sourced with skills, a
generation app, CLI installer, and GitHub Action. The author reports it changed how he
reviews agent work: "I found this to be a much more intuitive interface for me to
reason about what the agent's doing."

## Potential Alternatives

- Plain HTML output per artifact (Derrick's pattern) — simpler, no toolchain, but
  unbounded variance and poor repo ergonomics.
- Static markdown with embedded Mermaid diagrams — zero new dependencies, far less
  interactive.
- Dedicated design tools (Figma links) — higher fidelity, but outside the agent loop
  and not generated from the plan itself.

## Potential Improvements

- Domain-specific component libraries (e.g., governance components: decision cards,
  supersession chains, scope maps) rather than only UI/API components.
- Component-level diffing so plan revisions render as visual deltas.

## Potential Failure Modes

- **Toolchain tax.** MDX requires a renderer; an Obsidian/markdown-native corpus can't
  consume it without a build step.
- **Component library maintenance.** The consistency benefit lasts only while the
  component vocabulary matches what plans need; a stale library pushes the agent back
  to freeform generation.
- **Pretty-plan illusion.** A polished wireframe can over-signal certainty about
  behavior the plan hasn't actually specified.
