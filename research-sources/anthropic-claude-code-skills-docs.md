---
name: Extend Claude with skills — Claude Code Docs
source_type: Documentation
status: Done
key_takeaways: 'Canonical Claude Code-specific skills documentation. Documents Claude Code''s extensions to the Agent Skills open standard: invocation control (disable-model-invocation, user-invocable),
  subagent execution (context: fork + agent:), dynamic context injection (`!`backtick shell pre-rendering), and an expanded frontmatter set (when_to_use, argument-hint, arguments, allowed-tools, disallowed-tools,
  model, effort, hooks, paths, shell). Specifies the skill hierarchy (enterprise > personal > project; plugin separate namespace), live change detection, automatic discovery from parent and nested directories,
  and skill descriptions budgeted at 1% of context window with 1536-char cap. Documents skill content lifecycle: rendered SKILL.md enters as a single message and stays; auto-compaction preserves first 5K
  tokens per skill within a 25K combined budget. Documents permission model: Skill(name) and Skill(name *) syntax, skillOverrides settings with on/name-only/user-invocable-only/off states. ''Custom commands
  have been merged into skills'' — slash commands and skills are now one primitive.'
relevance: High
added_by: Nick
tags:
- skills
- claude-code
- context-engineering
- agent-design
- tools
- session-management
url: https://code.claude.com/docs/en/skills
authority:
- anthropic.md
findings:
- claude-code-skill-frontmatter-extensions.md
- skill-content-lifecycle-context-budget.md
- skill-description-budget-context-overflow.md
- skill-dynamic-context-injection-shell-prerender.md
- skill-forked-subagent-execution.md
- skill-hierarchy-enterprise-personal-project-plugin.md
- skill-invocation-control-side-effect-guard.md
- skill-live-change-detection-hot-reload.md
- skill-md-frontmatter-as-discovery-trigger-primitive.md
- skill-security-audit-obligation.md
- slash-commands-merged-into-skills.md
date_added: '2026-06-11'
date_processed: '2026-06-11'
date_published: null
---

# Extend Claude with skills (Claude Code Docs)

Claude Code-specific extension of the Agent Skills open standard. The most authoritative source on the harness-level surface area that Claude Code adds on top of the cross-platform standard. Documents 13+ frontmatter fields beyond the spec's required two, plus the runtime mechanics (hot reload, post-compaction preservation, permission model, override settings).

Notably reframes the relationship to existing slash-command primitives: `.claude/commands/<name>.md` and `.claude/skills/<name>/SKILL.md` both produce `/<name>` and are interchangeable for the simple case; skills add bundled-file support, invocation-control frontmatter, and auto-loading. This unifies what were two configuration primitives into one.

Documents the post-compaction preservation rule explicitly: "Auto-compaction carries invoked skills forward within a token budget. When the conversation is summarized to free context, Claude Code re-attaches the most recent invocation of each skill after the summary, keeping the first 5,000 tokens of each. Re-attached skills share a combined budget of 25,000 tokens."
