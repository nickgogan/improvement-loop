---
name: Skill Hierarchy — Enterprise > Personal > Project, Plugin as Separate Namespace
summary: Claude Code resolves skill names across four sources with an override hierarchy: Enterprise (managed settings, overrides all) > Personal (~/.claude/skills/) > Project (.claude/skills/). Plugin skills use a `plugin-name:skill-name` namespace and cannot conflict with the unnamespaced levels. Project skills load from .claude/skills/ at any parent directory up to repo root, plus on-demand from nested subdirectories under the starting dir. Skills from --add-dir are loaded automatically as an exception to the file-access-only rule.
implementation_notes: "Skill+command name conflict: skill wins. Plugin namespace: my-plugin:review never conflicts with project-level review. Project skills auto-discover from parents (so starting in a subdir still gets repo-root skills) and on-demand from nested subdirs you're editing in (monorepo support). The --add-dir flag is an explicit exception: file access permissions DON'T load skills, but --add-dir DOES. Settings-level additionalDirectories don't load skills. Live change detection works for SKILL.md text only; plugin sub-resources (hooks/, .mcp.json, agents/, output-styles/) need /reload-plugins."
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-claude-code-skills-docs.md"
related_findings:
  - file: "claude-code-skill-frontmatter-extensions.md"
    rel: "same-problem"
  - file: "memory-bank-isolation-per-agent-per-project.md"
    rel: "same-problem"
  - file: "subagent-persistent-memory-directory.md"
    rel: "same-problem"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Skill Hierarchy — Enterprise > Personal > Project, Plugin as Separate Namespace

## What It Is

Claude Code looks for skills at four levels with a strict override order:

| Location | Path | Scope | Override Priority |
|---|---|---|---|
| Enterprise | Managed settings | All users in organization | Highest |
| Personal | `~/.claude/skills/<name>/SKILL.md` | All your projects | High |
| Project | `.claude/skills/<name>/SKILL.md` | This project only | Lower |
| Plugin | `<plugin>/skills/<name>/SKILL.md` | Where plugin enabled | Namespaced |

Names colliding across unnamespaced levels resolve by priority — enterprise overrides personal, personal overrides project. Plugin skills get a `plugin-name:skill-name` invocation namespace and cannot collide with the unnamespaced names.

Project skills have two extra discovery rules:
- **Walk up to repo root.** `.claude/skills/` in the starting directory AND every parent directory up to the repo root all contribute. Starting Claude in a subdir still picks up skills defined at the root.
- **Nested on-demand.** When working on files in `packages/frontend/`, Claude Code discovers skills in `packages/frontend/.claude/skills/` on demand. Supports monorepo per-package skills.

The `--add-dir` flag and `/add-dir` command grant file access but are an explicit exception for skills: skills *are* loaded from `--add-dir` directories. The settings-level `permissions.additionalDirectories` is not — file access only, no skill loading.

## Why It Matters

This is the harness-level expression of system-scoped governance — exactly the problem MetaSystem solves at a different layer with system-scoped DDs and IB items. The same skill name can have different content depending on enterprise policy, user preference, or project shape, and the resolution is deterministic by priority.

The walk-up + nested rules together mean monorepo and root-level skills compose naturally — package-specific skills coexist with repo-wide ones, with directory ancestry providing the scope. This is more sophisticated than file-watching in most editors and more flexible than a flat registry.

The skills-as-load-bearing exception to `--add-dir` shows that Anthropic considers skills more like configuration than data. Other `.claude/` resources (subagents, commands, output styles) are explicitly NOT loaded from added directories.

## Why People Are Using It

Built into Claude Code from the unified skills+commands release. Enterprise-tier skill deployment shipped December 18, 2025 (per the Complete Guide PDF). Plugin marketplaces (e.g., `/plugin marketplace add anthropics/skills`) leverage the plugin-namespace property to ship skill bundles without name collision.

## Potential Alternatives

Flat skill registry (no priority — last-loaded wins, brittle). Project-only skills (no personal-level reuse — every project re-defines everything). Personal-only skills (no project specialization). Tag-based selection ("skills tagged 'deployment' available in this project") — less predictable. External registry service.

## Potential Improvements

Per-skill override tracking — when a project skill overrides a personal skill, the personal skill's existence and its differences should be discoverable. Skill versioning with version-aware resolution. Cross-priority skill composition (project skill *extends* personal skill rather than overrides). The current model is replace-on-name-match; partial overrides would let project skills augment personal ones.

## Potential Failure Modes

**Silent override.** A project-level `summarize-changes` skill overrides a personal one without warning. The user is using the project version without realizing it.

**Override-by-name without override-by-content.** Two skills sharing a name can have wildly different behavior. The user types `/foo` and gets whichever wins resolution, with no indication of which.

**Personal vs project drift.** A user iterates on a personal skill, then opens a project that has its own version — the project version doesn't get the personal updates.

**Monorepo nested discovery surprises.** Skills in `packages/X/.claude/skills/` load when editing files in that subtree but not from outside. Cross-package consistency is on the author.

**`--add-dir` skill loading vs. additionalDirectories settings.** Inconsistent treatment is a footgun. The same skill in the same place loads via `--add-dir` but not via `permissions.additionalDirectories` settings. The docs note this exception explicitly; users have to read carefully.

**Workspace trust as load-bearing.** Project skills' `allowed-tools` only take effect after the workspace trust dialog is accepted. A skill checked in with broad `allowed-tools` is a security concern until trust is granted — and then is fully empowered.
