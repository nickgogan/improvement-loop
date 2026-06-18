---
name: Slash Commands Merged Into Skills (Unified Invocation Primitive)
summary: In Claude Code, custom slash commands have been merged into skills. A file at `.claude/commands/deploy.md` and a skill at `.claude/skills/deploy/SKILL.md` both produce `/deploy` and work the same way. Existing `.claude/commands/` files continue to work. Skills add optional features that commands lack: a directory for supporting files, invocation-control frontmatter (disable-model-invocation, user-invocable), and the ability for Claude to load them automatically when relevant.
implementation_notes: "Migration path: existing slash commands keep working; new authoring should prefer skills for non-trivial cases. Single-file invocations stay as commands; anything needing references/, scripts/, or assets/ becomes a skill. The unification means slash commands inherit the skill ecosystem — hierarchy resolution (enterprise > personal > project, plugin namespace), dynamic context injection, frontmatter extensions, eval workflows. Conversely, skills inherit the command UX — type `/skill-name` to invoke directly, argument-hint shows on autocomplete, $ARGUMENTS substitution. The skill+command name collision is resolved by skill-wins. A few built-in commands — /init, /review, /security-review — are also exposed through the Skill tool; others like /compact are not."
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Already Adopted
priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in:
  - "Improvement Loop"
  - "General / Cross-System"
sources:
  - "anthropic-claude-code-skills-docs.md"
related_findings:
  - file: "skill-md-frontmatter-as-discovery-trigger-primitive.md"
    rel: "extends"
  - file: "claude-code-skill-frontmatter-extensions.md"
    rel: "extends"
  - file: "skill-hierarchy-enterprise-personal-project-plugin.md"
    rel: "extends"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Slash Commands Merged Into Skills (Unified Invocation Primitive)

## What It Is

In Claude Code, custom slash commands and skills are now one configuration primitive. The two file layouts produce identical behavior at the simple end:

| Layout | Command name | Auto-load by Claude | Supports bundled files | Frontmatter options |
|---|---|---|---|---|
| `.claude/commands/deploy.md` | `/deploy` | No (legacy) | No | Limited |
| `.claude/skills/deploy/SKILL.md` | `/deploy` | Yes (via description) | Yes (`scripts/`, `references/`, etc.) | Full skill frontmatter |

Existing `.claude/commands/*.md` files keep working. The skill version is a superset.

The merge also unifies the discovery and override pipeline: enterprise > personal > project resolution, plugin namespacing, live change detection, automatic discovery from parent and nested directories — all the skill rules apply to what were previously two separate primitives.

A subset of built-in commands — `/init`, `/review`, `/security-review` — are also exposed through the Skill tool, callable like skills. Others like `/compact` are not.

## Why It Matters

Before the merge, "I want a reusable named workflow with a directory of supporting files" required a custom subagent or a hand-built skill outside the slash-command system, while "I want a quick named action" was a slash command. Two surfaces, two file layouts, two configuration shapes.

The merge eliminates that distinction. A new author can start with `/deploy.md` and grow it into a directory-shaped skill without renaming, re-registering, or migrating. The growth path is gradual:
- Start: single SKILL.md with `disable-model-invocation: true` for a user-triggered action.
- Grow: add `scripts/`, `references/`, `assets/` as the workflow gets richer.
- Mature: add `context: fork + agent:` for isolated execution, `paths:` for auto-trigger gating, `allowed-tools:` for permission pre-grants.

The reverse case is also useful: any existing `.claude/commands/*.md` file becomes auto-loadable just by moving it to `.claude/skills/<name>/SKILL.md` and adding a description. No code change in the command.

## Why People Are Using It

Built into current Claude Code. The bundled skills (`/run`, `/verify`, `/code-review`, `/debug`, `/loop`, `/claude-api`) are skill-shaped. The MetaSystem workspace already uses both surfaces (see existing `.claude/commands/` and `systems/improvement-loop/.claude/skills/`).

## Potential Alternatives

Two separate primitives (the pre-merge state — works but doubles the configuration surface). Subagents as the only complex case (heavier per-use, separate file shape). External skill servers (architecturally heavier, requires infrastructure). MCP servers as the workflow primitive (already exists; serves a different purpose — protocol-level external tool integration vs. local instruction packaging).

## Potential Improvements

Migration tooling: `claude skills migrate-from-commands` to walk `.claude/commands/` and offer skill-ification with descriptions. Per-skill telemetry: "this command/skill was invoked N times by Claude, M times by user" to inform invocation-control decisions. Slash command deprecation warnings when a new feature is requested that only skills support (e.g., trying to add `scripts/` to a command).

## Potential Failure Modes

**Name collision skill-wins surprise.** A long-existing `.claude/commands/foo.md` becomes shadowed by a new `.claude/skills/foo/SKILL.md`. Both still exist on disk; only the skill runs. Source-of-truth is ambiguous from `ls` alone.

**Migration loss.** Moving from a command to a skill without adding a meaningful `description` makes the skill auto-loadable on weak match — Claude may start triggering it when not intended. The "should I let Claude auto-load this" decision is forced at migration time but easy to overlook.

**Built-in command exposure asymmetry.** `/init`, `/review`, `/security-review` are Skill-tool-exposed; `/compact` is not. Authors building rules over the Skill tool need to remember which built-ins are and aren't reachable that way.

**Authoring convention drift.** Two reasonable patterns ("everything is a skill" vs. "trivial things stay as commands") will both persist in real projects. Code review and onboarding need to address it.

**Documentation lag.** Sources that pre-date the merge still describe commands and skills as separate concepts. Consumers learning from older material may build the wrong mental model.
