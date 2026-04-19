---
title: "IDE-First Workflow with Deterministic Hooks"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "ide-first-claude-code-with-deterministic-hooks"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Claude Code is running within an IDE (Cursor, VS Code) rather than bare terminal. The .claude/ configuration directory exists with settings.json support for hooks. Rules that are candidates for hook conversion have been identified — they are deterministic (no context-dependent judgment required) and enforceable via command interception."
  invariants: "Every deterministic rule is enforced via a hook, not a CLAUDE.md instruction. Hooks fire on every matching event — they cannot be skipped, ignored, or overridden by the model. CLAUDE.md retains only context-dependent guidance that requires model judgment. No rule exists in both CLAUDE.md and a hook simultaneously."
  governance: "Nick owns the hook configuration and decides which rules to convert from CLAUDE.md to hooks. Agents may propose hook conversions but must not modify settings.json autonomously. New hooks require testing before deployment."
  recovery: "If a hook blocks a legitimate action (false positive), the user overrides manually and the hook rule is reviewed for refinement. If a CLAUDE.md rule is discovered to be deterministic but not yet converted to a hook, flag it for conversion in the next maintenance pass. If the IDE environment is unavailable and the agent falls back to terminal, document which hook-enforced rules are temporarily unenforced."
tags:
  - "extracted-artifact"
  - "pattern"
---

# IDE-First Workflow with Deterministic Hooks

**Source:** [[ide-first-claude-code-with-deterministic-hooks]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Terminal-based Claude Code workflows lack visibility into file state, configuration, and context. CLAUDE.md rules consume context tokens on every turn and are probabilistic — the model may ignore them. As the rule set grows, token cost increases and compliance becomes less reliable. There is no mechanism to guarantee that a specific rule is always followed.

## Forces

- **Determinism vs. judgment.** Some rules are absolute ("always use pnpm, never npm") and require no context-dependent reasoning. Others ("prefer concise output") require judgment. Mixing both in the same enforcement mechanism (prompt instructions) degrades both.
- **Token cost vs. rule coverage.** Every CLAUDE.md rule costs tokens on every turn. More rules means more cost and more competition for model attention, even for rules that could be enforced without consuming any context.
- **Flexibility vs. rigidity.** Hooks are deterministic — they always fire and cannot be overridden by the model. This is exactly right for some rules and exactly wrong for others that need context-sensitive application.
- **Portability vs. capability.** IDE-specific features (Markdown preview, sidebar navigation, multi-model testing) increase capability but create environment dependency.

## Solution

Split agent rules into two enforcement layers based on whether they require model judgment:

**Layer 1: Deterministic hooks (orchestration layer).**
Pre-tool-use hooks intercept commands and enforce rules without consuming any context tokens. They always fire, cannot be ignored by the model, and cost zero tokens.

- **Command substitution:** Block `npm` and redirect to `pnpm`. Block `rm -rf` on protected paths.
- **Path enforcement:** Prevent file modifications outside the agent's designated system boundary.
- **Tool gating:** Require confirmation before running destructive operations.

Hooks are configured in `.claude/settings.json` and fire at the infrastructure level, before the model's chosen command reaches the shell.

**Layer 2: Contextual guidance (prompt layer).**
CLAUDE.md retains only rules that require context-dependent judgment — preferences, cognitive dispositions, architectural guidance. These benefit from model reasoning and cannot be reduced to deterministic command interception.

**IDE integration complements both layers:**
- Markdown preview for .claude/ configuration files and documentation.
- Sidebar navigation for file discovery across the fractal structure.
- Multi-model testing (switch between Claude, GPT, etc.) for validation.
- Visual diff and file state visibility that terminal lacks.

**Key mechanics:**

1. **Audit CLAUDE.md rules.** For each rule, ask: "Can this be enforced by intercepting a specific command or tool call?" If yes, convert to a hook.
2. **Configure hooks in settings.json.** Use `pre_tool_use` hooks for command interception and substitution.
3. **Remove converted rules from CLAUDE.md.** A rule should exist in one enforcement layer, not both — dual enforcement wastes tokens and creates maintenance overhead.
4. **Test hooks before deployment.** Verify that hooks fire correctly, don't block legitimate actions, and handle edge cases (e.g., the blocked command appearing as a substring of a valid command).

## Consequences

**Positive:**
- Deterministic rule enforcement — hooks always fire, regardless of model attention or instruction-following quality.
- Zero token cost for hook-enforced rules — context budget is freed for task-relevant content.
- Cleaner CLAUDE.md — only context-dependent guidance remains, improving model focus on rules that actually need judgment.
- IDE visibility provides immediate feedback loops that terminal workflows lack.

**Negative:**
- Over-hooking creates rigid workflows that cannot adapt to legitimate edge cases.
- Hook configuration is an engineering task — each hook must be written, tested, and maintained.
- IDE dependency reduces portability. If the agent must fall back to terminal, hook-enforced rules may still apply (via settings.json) but IDE-specific benefits are lost.
- Some rules occupy a gray zone between deterministic and contextual — classifying them requires judgment.

## Known Uses

- **Nate B Jones "The Claude Code Feature Senior Engineers KEEP MISSING"** (YouTube, 2026): Documents hooks in skills, subagents, and custom slash commands as the foundation for "specialized self-validating agents."
- **Anthropic Claude Code Best Practices** (2026): Endorses moving deterministic rules from CLAUDE.md to hooks for guaranteed enforcement.
- **MetaSystem current environment:** Cursor + Claude Code with .claude/ configuration. Some hooks already in use (pre-tool-use). CLAUDE.md contains rules that are candidates for hook conversion.

## Contract

### Preconditions

- Claude Code is running within an IDE (Cursor, VS Code) rather than bare terminal.
- The `.claude/` configuration directory exists with `settings.json` support for hooks.
- Rules that are candidates for hook conversion have been identified — they are deterministic (no context-dependent judgment required) and enforceable via command interception.

### Invariants

- Every deterministic rule is enforced via a hook, not a CLAUDE.md instruction.
- Hooks fire on every matching event — they cannot be skipped, ignored, or overridden by the model.
- CLAUDE.md retains only context-dependent guidance that requires model judgment.
- No rule exists in both CLAUDE.md and a hook simultaneously.

### Governance

- Nick owns the hook configuration and decides which rules to convert from CLAUDE.md to hooks.
- Agents may propose hook conversions but must not modify `settings.json` autonomously.
- New hooks require testing before deployment.

### Recovery

- If a hook blocks a legitimate action (false positive), the user overrides manually and the hook rule is reviewed for refinement.
- If a CLAUDE.md rule is discovered to be deterministic but not yet converted to a hook, flag it for conversion in the next maintenance pass.
- If the IDE environment is unavailable and the agent falls back to terminal, document which hook-enforced rules are temporarily unenforced and rely on prompt-layer fallback until the environment is restored.
