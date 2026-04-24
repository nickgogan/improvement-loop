---
name: "Subagent Scope Priority Ladder (Managed > CLI > Project > User > Plugin)"
summary: "Anthropic Claude Code resolves subagent definitions through a deterministic 5-level override ladder — organization-wide managed settings beat CLI-flag definitions beat project-scoped beat user-scoped beat plugin-scoped. Same-name conflicts resolve in one direction only. Plain English: IT ops can override what developers pick; developers can override what plugins pick; plugins lose every conflict. The priority order is the governance backbone for subagent standardization across an org."
implementation_notes: "For MetaSystem: the Librarian and Owner are currently available only at user scope (~/.claude/agents/) and project scope (.claude/agents/). If MetaSystem ever runs in multi-user contexts, the project-vs-user-vs-plugin precedence matters. The pattern also formalizes how to distribute opinionated defaults — publish as plugin, override locally."
category: "Governance"
evidence_strength: "Strong (documented, first-party Anthropic canonical spec)"
adoption_status: "Partially Adopted"
priority: P2
applicability:
  - "General"
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "anthropic-claude-code-subagents-docs.md"
related_findings:
  - file: three-tier-vault-architecture-global-shared-local.md
    rel: same-problem
  - file: tiered-context-injection-over-monolithic-files.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-24"
pipeline_status: classified
consumed_by: []
---

## What It Is

A five-level deterministic precedence order for subagent definition resolution in Claude Code. When multiple subagent definitions share the same name, Claude Code picks exactly one using this table (1 = highest priority):

| Priority | Location | Scope | How deployed |
|---|---|---|---|
| 1 | Managed settings | Organization-wide | Managed settings deployment |
| 2 | `--agents` CLI flag | Current session | JSON at launch |
| 3 | `.claude/agents/` | Current project | Committed to repo |
| 4 | `~/.claude/agents/` | All the user's projects | Personal install |
| 5 (lowest) | Plugin's `agents/` directory | Where plugin is enabled | Plugin install |

Override semantics are strict: higher priority wins. No merging, no partial override, no "user extends project." The CLI command `claude agents` reports which agents are active and which are overridden.

Three load-bearing properties:

1. **Organization admins override developers.** Managed settings (priority 1) can enforce e.g. a security-vetting subagent on every session regardless of what developers prefer.
2. **Developers override plugins.** If a plugin ships a "code-reviewer" subagent with permissive defaults, a project can ship its own "code-reviewer" (priority 3) and the plugin version is silently shadowed.
3. **Plugins are guest-citizens.** Plugin subagents cannot set `hooks`, `mcpServers`, or `permissionMode` for security — even within their priority level, they have a capped capability surface.

## Why It Matters

Subagent governance scales with the precedence model. Without priority ordering, same-name conflicts produce undefined behavior or require per-team conventions. With this ladder, defaults are enforceable top-down (managed), customizable mid-stack (project/user), and extensible bottom-up (plugin) with clean semantics.

For MetaSystem:
- **Pattern applies to IL skill distribution too.** The IL's skills live at system scope (`systems/improvement-loop/.claude/skills/`); MetaSystem workspace skills live at project root (`.claude/skills/`). If ever distributed as plugin-packaged skills for other users, the plugin-lowest-priority semantic means local overrides stay intact.
- **Governance primitive for fractal system.** The ladder is a specific instance of the tiered-context pattern MetaSystem already uses (`three-tier-vault-architecture` for memory, `tiered-context-injection` for rules). Subagents add a fourth dimension with same structure.
- **Enforcement without lock-in.** Managed-settings priority means security teams can require specific subagents for all sessions while developers retain full control over everything else. Distinct from "all-or-nothing" enforcement models.

## Why People Are Using It

Documented canonically at [Anthropic's Claude Code subagents docs](https://code.claude.com/docs/en/sub-agents) — see [[anthropic-claude-code-subagents-docs]] for the source. The five-level ladder is stated explicitly in the doc's scope section with an accompanying table. The CLI reporter `claude agents` surfaces which agents are active and which are overridden by higher-priority definitions, making the ladder's effects visible at inspection time.

Built-in Claude Code subagents (Explore, Plan, general-purpose) sit implicitly at the top of the ladder — they exist without user configuration and inherit the parent conversation's permissions with additional tool restrictions. Users cannot remove them directly but can deny them via `permissions.deny: ["Agent(Explore)"]` (which operates orthogonal to the priority ladder).

## Potential Alternatives

- **Single-scope agent definitions.** Everyone ships in one place; no priority conflicts. Loses the "organization can enforce defaults" property.
- **Merge-on-conflict semantics.** When two definitions collide, merge fields. Harder to reason about; subtle bugs from accidental merges.
- **Namespace per scope** (`project:code-reviewer` vs `user:code-reviewer`). No conflicts possible; also no overrides. Loses the "later-definition wins" ergonomics.
- **Last-wins temporal ordering.** Whichever definition loads last wins. Priority becomes load-order dependent; hard to govern.
- **Explicit override declaration.** Each definition states "overrides: user/plugin/..." explicitly. More control; more ceremony.

## Potential Improvements

- **Diff-on-override tooling.** When a higher-priority definition shadows a lower-priority one, surface the diff so the user knows what they're missing.
- **Opt-in merge for specific fields.** `tools` is safe to merge (union allowlists); `prompt` is not (semantic conflict). A typed per-field merge policy would expand the ladder's capability without losing determinism.
- **Override audit log.** Record every time a definition was shadowed; governance review can spot cases where the wrong version is winning.
- **Priority for single fields.** `model: inherit` could mean "inherit from the next-lower priority definition" rather than "inherit from the main conversation," enabling finer-grained overrides.

## Potential Failure Modes

- **Silent shadowing.** A plugin's subagent is shadowed by a project definition without any indication. User expects plugin behavior; gets project behavior. Mitigation: `claude agents` command surfaces shadowing; make this visible at invocation too.
- **Managed-settings lockout.** Managed priority-1 can enforce bad defaults if the org admin doesn't maintain them. No local escape hatch. Mitigation: clear managed-settings review process; per-project exceptions require admin sign-off.
- **Stale user-level agents.** Personal `~/.claude/agents/` directories accumulate old definitions; new project-level definitions correctly override them, but the user doesn't realize their old version is obsolete. Mitigation: periodic cleanup; per-agent timestamps; UI hints.
- **Plugin capability cap surprises.** Plugin authors don't know their subagents are stripped of `hooks` / `mcpServers` / `permissionMode` silently. Mitigation: plugin validation surfaces these fields-being-ignored at install.
- **Priority-1 proliferation.** Everything migrates to managed settings to "enforce" it, but managed settings lose flexibility. Mitigation: reserve priority 1 for genuinely organization-scope defaults; keep project scope as the default home.
