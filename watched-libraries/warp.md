---
name: "Warp"
url: "https://github.com/warpdotdev/warp"
stars: "~25k"
spectrum_position: "study"
spectrum_rationale: "Agentic development environment with mature agent skill system (.agents/skills/), feature flag promotion workflow, skills-lock.json for shareable skill packages, and Oz agent API for multi-agent orchestration. Directly relevant to skill architecture and agent team coordination patterns."
current_version: "latest (commit a530563)"
last_checked: "2026-05-24"
tracking_focus:
  - "Agent skills architecture: core/specialized pattern, SKILL.md format, skills-lock.json"
  - "Feature flag lifecycle: add → dogfood → preview → stable → remove"
  - "Oz agent API: multi-agent orchestration, SSE-based communication"
  - "Issue triage and PR review skills: automated quality gates"
tags:
  - "agentic-ide"
  - "skills-system"
  - "feature-flags"
  - "multi-agent"
  - "rust"
date_added: "2026-05-24"
---

# Warp

Agentic development environment (Rust-based terminal) by warpdotdev. Open-sourced with OpenAI sponsorship. 3299 Rust source files, 5317 total files. Includes built-in coding agent, Oz agent platform, and rich skill/workflow system.

## Why We Watch

Warp has one of the most mature agent skill architectures in production: 15+ skills in `.agents/skills/`, a `skills-lock.json` managed by `npx skills` for portable/shareable skill packages, and a core/specialized skill pattern where repo-local skills "specialize" generic core skills. The feature flag lifecycle (add → dogfood → preview → stable → remove) is a production-grade deployment pattern.

## Key Architectural Features

- **Agent skills**: `.agents/skills/<name>/SKILL.md` — frontmatter with `name`, `description`, `specializes` field for inheritance. Core skills live in `common-skills` repo; local skills override specific categories.
- **Skills-lock.json**: Lock file for shared agent skills across repos. Managed by `npx skills` CLI. Install targets: project or global.
- **Feature flag lifecycle**: 5-stage promotion (runtime flags → compile-time features → default). Each stage has explicit file changes and validation steps.
- **Oz agent API**: External agents connect via SSE, can @mention each other, manage kanban tasks, produce artifacts. See oz-workspace for reference implementation.
- **Warp workflows**: `.warp/workflows/` YAML-based automation (similar to GitHub Actions but for terminal workflows).

## Spectrum Notes

Full study — the skills architecture (core/specialized pattern, lock file, install targets) and feature flag lifecycle are production patterns worth extracting. The Oz multi-agent coordination model is relevant to our agent team research.
