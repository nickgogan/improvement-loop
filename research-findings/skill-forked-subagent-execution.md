---
name: 'Skill-as-Forked-Subagent Execution Mode (context: fork)'
summary: 'Claude Code skills can run in an isolated subagent context via `context: fork` + `agent: <type>` frontmatter. The skill content becomes the subagent''s prompt; the named agent type (Explore, Plan,
  general-purpose, or any custom .claude/agents/ subagent) provides the system prompt and tool set. The fork has no access to the main conversation history. This is the inverse of the subagent-with-`skills`-field
  pattern (subagent loads pre-injected skills as reference material).'
implementation_notes: 'Frontmatter pattern: context: fork + agent: Explore (or Plan, general-purpose, or custom subagent name). Skills targeted at fork mode must include explicit task instructions, not
  just guidelines — the warning is explicit: ''context: fork only makes sense for skills with explicit instructions. If your skill contains guidelines like "use these API conventions" without a task, the
  subagent receives the guidelines but no actionable prompt, and returns without meaningful output.'' Built-in Explore and Plan agents skip CLAUDE.md and git status to keep context small. The PR-summary
  example uses context: fork + agent: Explore for read-only PR analysis. The skill becomes the prompt, the agent provides the harness.'
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-claude-code-skills-docs.md
related_findings:
- file: claude-code-skill-frontmatter-extensions.md
  rel: extends
- file: skill-dynamic-context-injection-shell-prerender.md
  rel: same-problem
- file: subagent-persistent-memory-directory.md
  rel: same-problem
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-07-13'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
---

# Skill-as-Forked-Subagent Execution Mode

## What It Is

A Claude Code skill can declare itself to run in an isolated subagent context:

```yaml
---
name: deep-research
description: Research a topic thoroughly
context: fork
agent: Explore
---
```

When invoked, Claude Code spawns a subagent whose:
- **System prompt** = the subagent's own definition (built-in `Explore`, `Plan`, `general-purpose`, or custom `.claude/agents/<name>.md`).
- **Task** = the rendered SKILL.md body (with all string substitutions and dynamic-context-injection already resolved).
- **Context** = no access to the main conversation history.

Results are summarized and returned to the main conversation.

The pattern composes with subagents in the opposite direction too: a custom subagent's frontmatter can include `skills: skill1, skill2` to preload skills as reference material at startup.

## Why It Matters

This unifies three previously distinct primitives in Claude Code:
1. **Skills** (loadable capability packages).
2. **Subagents** (isolated execution environments with custom system prompts and tools).
3. **Slash commands** (named invocations).

Before this convergence, each had its own configuration shape and lifecycle. The combination lets the skill author write the task once, choose where it runs (in the main conversation inline, or in an isolated subagent fork), and choose the execution environment (which agent type's system prompt + tools to use).

The clearest use cases the docs name:
- **Research/exploration**: `context: fork + agent: Explore` runs read-only codebase analysis without polluting the main conversation.
- **Planning**: `context: fork + agent: Plan` for design work without committing implementation steps to the main thread.
- **Custom domain agents**: skill = task, custom subagent = persona/tools — same skill can be re-routed to a different agent later by changing one line.

## Why People Are Using It

Built into Claude Code as a first-class feature. The PR-summary example in the docs uses it explicitly. The unification of slash commands and skills (announced in the canonical docs as "custom commands have been merged into skills") means existing `.claude/commands/*.md` files already work with the new pattern by just adding `context: fork`.

## Potential Alternatives

Skill-only invocation (skill runs in main conversation; gets full history but pollutes context). Subagent-only invocation (separate file, separate lifecycle, can't share authoring with skills). External agent runners (e.g., spawning a script that calls another Claude session — heavier, slower). Tool-call routing to a backend agent service (heavier infrastructure).

## Potential Improvements

Per-invocation tool subsets (the agent provides defaults, the skill could augment). Pipelined skill-fork compositions (skill A spawns a fork, the result feeds into skill B). Cross-fork result aggregation (run the same skill against multiple targets, collect outputs). Authoring guidance for choosing fork vs. inline is currently thin — the docs offer the warning about needing explicit instructions, but no rubric for "when is a fork worth it."

## Potential Failure Modes

**Guidelines-only skill targeting fork.** Explicit warning in the docs: "If your skill contains guidelines like 'use these API conventions' without a task, the subagent receives the guidelines but no actionable prompt, and returns without meaningful output." Reference-content skills should not target fork mode.

**Lost main-conversation context.** The fork has no access to the main thread's history. A skill that assumed the user just said something — "fix the bug we just discussed" — fails in fork mode. Authors must encode all needed context into the skill body or dynamic context injection.

**Agent-type drift.** A skill targeting `agent: Explore` works while Explore's behavior is stable; if Explore's default toolset changes, the skill behavior changes silently.

**Subagent invocation cost.** Each fork is a new context — model cost is real. A skill that forks for every invocation is heavier than inline by the cost of subagent startup.

**Custom agent name mismatch.** A skill referencing `agent: my-custom-reviewer` fails silently if the subagent is renamed or absent in this project.

**CLAUDE.md skipped on Explore/Plan.** Built-in Explore and Plan agents skip CLAUDE.md to keep their context small. A skill that assumes the project's CLAUDE.md conventions are loaded will misbehave on those agents.

## In-the-Wild Corroboration — Archon v0.5.0 (2026-07-13)

First production usage observed in the watched-library set beyond Anthropic's own docs: Archon v0.5.0's repo skills `rulecheck` and `triage` declare `agent:` + `context: fork` — the skill is the trigger/argument surface, the referenced `.claude/agents/` definition supplies persona and constraints, and the fork isolates the run from the main conversation. The same skill set exercises the adjacent frontmatter surface this pattern composes with: skill-level `hooks:` (a Stop-hook prompt evaluator in `save-task-list`), `disable-model-invocation` (human-trigger-only skills), and `allowed-tools` scoping (`Bash(gh *)` in `triage`). Archon's skills doubled 7 → 14 in one release with these mechanisms carrying the new review/triage automation. See [[archon-analysis]] for structural details.
