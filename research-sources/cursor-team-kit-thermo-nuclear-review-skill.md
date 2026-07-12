---
name: "Cursor team-kit — thermo-nuclear-code-quality-review SKILL.md (skill-design exemplar)"
source_type: "Documentation"
status: "Done"
key_takeaways: |-
  Rejected for roster adoption (overlaps harness /code-review, targets app-code diffs) but
  unusually pattern-dense as a skill-design exemplar for the assess-skill/design-skill
  substrate. Demonstrates a full strictness-escalation architecture: core prompt → numbered
  non-negotiable standards → per-change review questions → aggressive-flag list → preferred
  remedies → tone calibration via literal example phrases → prioritized output ordering →
  explicit approval bar separating "presumptive blockers" from waivable concerns. Hard
  quantitative blocker (PR pushing a file past 1000 lines = presumptive rejection). Uses
  disable-model-invocation: true frontmatter — explicit-invocation-only pattern for
  intentionally harsh modes, itself KB-worthy. Pushes reviewer to hunt "code judo" moves:
  behavior-preserving restructurings that delete whole layers rather than polish them.
  Fully portable prompt-only skill, no model coupling. Upstream: cursor/plugins main,
  last commit 2026-05-28.
relevance: "High"
added_by: "Agent (Link-Intake Triage)"
tags:
  - skill-design
  - prompt-craft
  - code-review
  - review-agent-design
url: "https://github.com/cursor/plugins/blob/main/cursor-team-kit/skills/thermo-nuclear-code-quality-review/SKILL.md"
authority:
  - "cursor.md"
findings:
  - "strictness-escalation-skill-architecture.md"
  - "code-judo-review-posture.md"
  - "skill-invocation-control-side-effect-guard.md"
date_added: "2026-07-11"
date_processed: "2026-07-11"
date_published: "2026-05-21"
---

Queued for `/research-loop` extraction by the 2026-07-11 link-intake triage
(`operations/research-reports/2026-07-11-link-intake-triage.md`, link #10).
