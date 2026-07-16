---
name: Skill Content Lifecycle — One-Shot Render, Sticky Across Turns, 5K/25K Post-Compaction Budget
summary: When a skill is invoked in Claude Code, its rendered SKILL.md enters the conversation as a single message and stays there for the rest of the session. Claude Code does not re-read the skill file
  on subsequent turns. Auto-compaction preserves the most recent invocation of each skill — first 5K tokens per skill, capped at a 25K combined budget across all preserved skills, with the oldest invocations
  dropped first when over budget. This creates a durable but fixed-budget skill memory inside an active session.
implementation_notes: 'Practical implications: (1) Skill body should be written as standing instructions, not one-time setup steps, because Claude re-reads it across turns from context, not from disk. (2)
  If a skill ''stops influencing behavior'' after the first response, the content is usually still present — the model is choosing other tools/approaches. Strengthen description/instructions, or use hooks
  for deterministic enforcement. (3) After compaction, re-invoke a skill to restore its full content if you need everything beyond the first 5K tokens preserved. (4) Designing skills to fit comfortably
  within 5K post-compaction tokens means the lead-most-important guidance must come first in SKILL.md.'
category: Context Engineering
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
- file: skill-as-directory-progressive-disclosure-three-levels.md
  rel: extends
- file: skill-description-budget-context-overflow.md
  rel: same-problem
- file: two-threshold-compaction-strategy.md
  rel: same-problem
- file: proactive-compaction-before-intelligence-degradation.md
  rel: same-problem
- file: reference-only-skill-shape-for-afk-agents.md
  rel: same-problem
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-07-12'
pipeline_status: synthesized
consumed_by:
- structuring-agent-context.md
---

# Skill Content Lifecycle — One-Shot Render, Sticky Across Turns, 5K/25K Post-Compaction Budget

## What It Is

In Claude Code, when a skill is invoked (by you typing `/skill-name`, by Claude deciding to load it, or by a subagent preloading it), the rendered SKILL.md enters the conversation as a single message. That message stays in context for the rest of the session — Claude Code does not re-read the file on subsequent turns. Any dynamic context injection (`!`backtick commands) is resolved once, at activation time.

Auto-compaction has a separate, named rule for skills: when conversation is summarized to free context, Claude Code "re-attaches the most recent invocation of each skill after the summary, keeping the first 5,000 tokens of each. Re-attached skills share a combined budget of 25,000 tokens. Claude Code fills this budget starting from the most recently invoked skill, so older skills can be dropped entirely after compaction if you have invoked many in one session."

In short:
- **In-session**: skill body persists across turns once loaded.
- **At compaction**: most recent invocation preserved per skill, first 5K tokens each, 25K total cap, LRU drop policy.
- **To restore beyond 5K**: re-invoke the skill after compaction.

## Why It Matters

This is the harness-level rule that determines what skill authoring should optimize for. Specifically:

- **Front-load critical guidance.** Anything past the first 5K tokens of a skill body is at risk after compaction. The most important instructions must be at the top.
- **Standing instructions, not one-time setup.** Because the skill is re-read from context (not disk) on every turn, instructions should apply throughout the task, not assume a single execution pass.
- **Session shape constrains skill design.** A session that loads 6+ skills will see older skills dropped at compaction. Sessions that lean on many skills should treat compaction as a soft state-loss event for older invocations.
- **Re-invocation as recovery primitive.** If a skill seems to have stopped influencing behavior post-compaction, the fix is to re-invoke it. This is a manual operation today.

## Why People Are Using It

Documented in Anthropic's Claude Code skills page (code.claude.com/docs/en/skills) under "Skill content lifecycle." Production Claude Code mechanism; bills as the canonical lifecycle for invoked skills. The 5K/25K numbers are concrete enough to optimize against.

## Potential Alternatives

Skill content re-read on every turn (heavier I/O, fresh dynamic context each turn — what `.cursorrules` does, and what skills explicitly do not do). No preservation through compaction (skills dropped entirely on summary — gone after a single long session). Larger per-skill cap (better for large skills, worse for skill-rich sessions). Dynamic per-skill priorities (preserve frequently-used skills regardless of recency — currently LRU).

## Potential Improvements

Per-skill authoring guidance: "this skill survives compaction with the first 5K tokens — structure accordingly." Skill priority pinning so critical skills don't get dropped at compaction. A `/skills status` introspection command to show what's currently preserved. The current LRU policy is reasonable but coarse.

## Potential Failure Modes

**Critical guidance buried past 5K tokens.** A 12K-token SKILL.md has its last ~7K silently dropped after compaction. Behavior changes mid-session in ways that look like model drift but are actually content drift.

**Skill-heavy session degradation.** A session that loads 8 skills (8 × 5K = 40K, above 25K budget) loses the oldest 3 entirely after compaction. The user expects them to still be in effect.

**One-time setup instructions.** A skill body that says "First, do X" assumes execution order. But the body is re-read every turn from context — Claude may treat "first, do X" as still applicable on turn 12. Skills should phrase guidance as invariants ("always do X", "never do Y") rather than ordered steps.

**Lossy dynamic context.** `!`backtick injections capture state at activation time. If the underlying state changes (git diff evolves, PR comments are added), the skill doesn't see the new state until re-invoked.

**Diagnosis is not in the loop.** A user noticing reduced skill effectiveness has no obvious signal whether (a) the skill content was dropped, (b) descriptions are below the budget cap, (c) the model is choosing other approaches, or (d) something else. The skills page suggests using `/doctor` and re-invoking; the diagnostic surface is thin.
