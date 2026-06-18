---
name: Skill Live Change Detection (Hot Reload Inside a Session)
summary: Claude Code watches skill directories for file changes. Adding, editing, or removing a SKILL.md under ~/.claude/skills/, the project .claude/skills/, or an --add-dir directory takes effect within the current session — no restart required. Creating a NEW top-level skills directory that didn't exist at session start still requires a restart so the new directory can be watched. Plugin sub-resources (hooks/, .mcp.json, agents/, output-styles/) need /reload-plugins to take effect; SKILL.md text changes live-reload.
implementation_notes: "Authoring workflow implication: iterate on a skill in-session, see changes immediately. This shortens the inner loop dramatically — no /reload, no restart between edits. The exceptions are subtle: a brand-new top-level skills directory needs restart (the watcher wasn't started for that path); plugin-bundled hooks/MCP/agents need /reload-plugins; live change detection covers SKILL.md TEXT only (not, for instance, scripts/ contents during the same session — though those load fresh each invocation anyway since they're not in context)."
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-claude-code-skills-docs.md"
related_findings:
  - file: "skill-md-frontmatter-as-discovery-trigger-primitive.md"
    rel: "extends"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Skill Live Change Detection (Hot Reload Inside a Session)

## What It Is

Claude Code watches three classes of skill directories during a session:
- `~/.claude/skills/` (personal)
- `.claude/skills/` in the project tree
- `.claude/skills/` inside any `--add-dir` directory

File changes inside these watched directories — adding a new SKILL.md, editing an existing one, removing one — take effect immediately without restarting Claude Code. The watch is on SKILL.md TEXT only.

Exceptions:
- **New top-level skills directory** — if the directory didn't exist when the session started, the watcher wasn't created for it; restart Claude Code to start watching.
- **Plugin sub-resources** — `hooks/`, `.mcp.json`, `agents/`, `output-styles/` inside a plugin-shaped skill need `/reload-plugins` to take effect.

## Why It Matters

The inner authoring loop for skills is "edit SKILL.md, test invocation, observe behavior, iterate." Without hot reload, every edit requires `/reload` or session restart — minutes of friction per iteration. With hot reload, the loop is seconds.

This makes interactive skill authoring practical. The skill-creator skill's recommended workflow — draft, run test prompts, observe, improve — assumes this property. Without it, the iteration cadence collapses to ~1 round per session.

The fact that the watcher is per-directory (not recursive from any root) explains the named exceptions: the watcher has to be created for each directory at session start. Creating a brand-new top-level skills directory in mid-session simply doesn't have a watcher running for it.

## Why People Are Using It

Built into Claude Code. The Complete Guide PDF cites "15-30 minutes to build and test your first working skill using the skill-creator" — a target that implicitly assumes hot reload to fit the iteration count.

## Potential Alternatives

Restart-required reload (cumbersome — kills the inner loop). Manual `/reload` after every edit (better but still friction). Watch-on-everything-everywhere (heavier, harder to scope). Skill-as-database (re-read every invocation from disk — simpler but loses the "in-context message" lifecycle).

## Potential Improvements

Hot reload for new top-level skills directories (the watcher could be created lazily). Watch indication in the UI — show which skills are live-loaded vs. need restart. Per-edit telemetry — surface that a recent edit didn't actually update the active skill (e.g., the user typo'd outside the watched dir). Per-skill version history within a session for rollback during authoring.

## Potential Failure Modes

**Edit didn't take effect because the directory wasn't watched.** Creating `~/.claude/skills/` mid-session for the first time doesn't auto-watch; the user edits a skill there and wonders why nothing changes. Restart fixes it.

**Plugin sub-resources silently stale.** A plugin-shaped skill edits its `hooks/post-write.sh`; the hook isn't refreshed until `/reload-plugins`. The user thinks the new hook ran when it didn't.

**Editor write-temp-then-rename behaviors.** Some editors save by writing a temp file and renaming over the target. Depending on watcher implementation, this can drop or duplicate events. Whether Claude Code's watcher handles this cleanly is unstated.

**Hot reload doesn't fix already-loaded content.** Editing a skill mid-session doesn't update the rendered SKILL.md that's already in the conversation. You need to re-invoke the skill to pick up the new content. The hot reload affects discovery and next invocation, not the live message in context.

**Live reload as security surface.** A malicious process editing skills mid-session can change behavior without warning. Workspace trust is the defense; live reload doesn't re-prompt for trust.
