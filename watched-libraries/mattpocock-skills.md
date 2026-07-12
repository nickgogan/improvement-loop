---
name: "mattpocock/skills"
type: "watched-library"
repo_url: "https://github.com/mattpocock/skills"
description: |-
  Matt Pocock's public .claude directory — "Skills for Real Engineers." Workflow-
  enforcement skill library for Claude Code (wayfinder, research, implement, to-spec,
  to-tickets, tdd, code-review, writing-great-skills) shipped as a versioned plugin
spectrum_position: "study"
what_we_use: |-
  Nothing adopted as code — study target. His skill-authoring techniques are already
  in the KB as the Pocock-pair findings (leading words, deletion test, branch
  externalization, leg-work amplification, wayfinder topology, two-axis review) and
  feed the /design-skill and /assess-skill substrate
local_derivations: []
last_evaluated_version: "v1.1.0 (2026-07-08)"
last_evaluated_date: "2026-07-12"
maintainer: "mattpocock (Matt Pocock)"
status: "active"
tags:
  - "skills"
  - "claude-code"
  - "prompt-engineering"
  - "workflow-enforcement"
related_findings:
  - "leading-words-lexical-steering-reasoning-trace-verification.md"
  - "leg-work-amplification-hiding-future-steps.md"
  - "fowler-code-smell-names-as-prior-invocation.md"
  - "wayfinder-issue-tracker-decision-map.md"
  - "two-axis-parallel-code-review-standards-vs-spec.md"
  - "reference-only-skill-shape-for-afk-agents.md"
  - "branch-analysis-externalization-rule-skill-reference.md"
  - "skill-pruning-failure-modes-noop-deletion-test.md"
  - "skill-invocation-control-side-effect-guard.md"
  - "meta-skill-for-skill-authorship.md"
related_sources:
  - "pocock-skills-v1-1-wayfinder-research-implement.md"
  - "building-great-agent-skills-the-missing-manual.md"
date_added: "2026-07-12"
---

## What It Does

Matt Pocock's personal `.claude` directory made public (MIT, ~166.7k stars as of
2026-07-12, Shell/JavaScript, shipped as a Claude Code plugin with changesets and
releases). Unlike capability-extension skill packs, it is a workflow-enforcement library:
engineering skills split into user-invoked (wayfinder, to-spec, to-tickets, implement,
triage, grill-with-docs) and model-invoked (research, tdd, prototype, diagnosing-bugs,
domain-modeling, codebase-design, code-review), plus productivity skills including the
`writing-great-skills` meta-skill. v1.1.0 (2026-07-08) added /wayfinder (issue-tracker
decision maps for efforts too big for one session), /research (background primary-source
investigation leaving a cited markdown note), and /implement, and renamed to-PRD → to-spec,
to-issues → to-tickets.

## What We Use From It

Study target — nothing adopted as code. The value already extracted is the technique
layer: the ten Pocock-pair findings from his AI Engineer talk ("Building Great Agent
Skills: The Missing Manual") and the v1.1 release video cover leading-words lexical
steering, the no-op deletion test, branch-analysis reference externalization, leg-work
amplification, user-vs-model invocation control, the wayfinder planning topology, two-axis
parallel code review, and reference-only skill shape for AFK agents. These feed the
engine's /design-skill and /assess-skill substrate. The repo itself remains the ground
truth for how those techniques are operationalized in shipped SKILL.md files.

## Spectrum Rationale

Study. The engine authors its own skills through /design-skill + /assess-skill (and the
imported /meta-skill-author toolchain), so we mine his implementations rather than install
his plugin. Highest-signal single-author skill corpus on the watch list: every finding
technique has a corresponding shipped SKILL.md to diff against. Re-evaluate on major
version bumps; his `writing-great-skills` meta-skill overlaps our skill-authorship
substrate and is the first diff target.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-07-12 | v1.1.0 | Initial entry, Nick-approved (session 137). Repo verified via GitHub API: 166,682 stars, MIT. Cross-linked to both Pocock sources and the 10 Pocock-pair findings. |
