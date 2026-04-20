---
name: Template-Generated Skills with Multi-Host Variants
summary: SKILL.md files generated from .tmpl templates via gen-skill-docs.ts. Templates are source of truth; SKILL.md is a build artifact. Host configs for 8 platforms define preamble, allowed-tools, and
  tool aliases. 38 templates produce 41 skills.
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: multi-ide-portability-via-installer-templates.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---

# Template-Generated Skills with Multi-Host Variants

## What It Is
gstack's SKILL.md files are generated from `.tmpl` template files via `gen-skill-docs.ts`. Templates are the source of truth — SKILL.md is a build artifact, not a hand-authored file. Host configs for 8 platforms (Claude, Codex, Cursor, Factory, Kiro, OpenClaw, OpenCode, Slate) define preamble content, allowed-tools, and tool aliases per platform. The same skill template generates platform-specific SKILL.md variants. 38 templates produce 41 skills across the supported hosts.

## Why It Matters
Hand-authored skill files diverge across platforms over time. Template generation ensures consistency — a change to the template propagates to all host variants automatically. This treats skills as compiled artifacts with a single source of truth, reducing maintenance burden and preventing drift between platform-specific versions.

## Why People Are Using It
Observed in [gstack](https://github.com/garrytan/gstack) v0.15.16.0 — see [[gstack-analysis]] for structural details. Treats skills as compiled artifacts rather than hand-authored files. Template generation ensures consistency across host variants. Changes to a skill only need to happen in the template — all host variants regenerate automatically.

## Potential Alternatives
Hand-authored SKILL.md per platform (simple but diverges). Shared SKILL.md with conditional sections. Runtime adaptation instead of build-time generation. Platform abstraction layer that hides host differences.

## Potential Improvements
Incremental generation (only rebuild changed templates). Host capability detection to auto-select appropriate template variant. Validation that generated SKILL.md matches host constraints.

## Potential Failure Modes
Template complexity growing to accommodate all 8 hosts. Generated files being manually edited (bypassing the template, causing drift). Host config staleness when platforms update their tool APIs. Build step forgotten after template changes, deploying stale SKILL.md.
