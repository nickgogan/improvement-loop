---
name: "Context-Before-Loop Initialization Sequence"
summary: "Agent harness loads project context (CLAUDE.md) and capability context (skills registry) before the first loop iteration runs. This is a boot sequence design decision: the agent is oriented to the project and equipped with reusable behaviors before it processes the first user message. The alternative — loading context on-demand during the loop — trades boot latency for first-turn completeness."
implementation_notes: null
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Already Adopted"
priority: "Not Flagged"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in:
  - "S3 (Claude Code Build)"
sources:
  - "claude-code-architecture-under-the-hood.md"
related_findings:
  - file: "context-file-taxonomy-claudemd-soulmd-agentsmd.md"
    rel: "extends"
  - file: "progressive-skill-loading.md"
    rel: "same-problem"
  - file: "layered-prompt-assembly-stable-segment-caching.md"
    rel: "enables"
  - file: "pluggable-context-engine.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "raw"
tags:
  - "session-95-reextract"
---

# Context-Before-Loop Initialization Sequence

## What It Is

A harness design pattern where the agent loads two categories of context before the reasoning loop begins:

1. **Project context** — CLAUDE.md from the repository. Project conventions, preferences, constraints, folder structure guidance. The agent reads this at boot and carries it throughout the session. Functions as "the onboarding doc for the agent."

2. **Capability context** — Skills registry. Reusable instruction sets for specific tasks (code review, documentation writing, security scanning). In the original TypeScript source, these are bundled in a registry; in the Rust port, they are read from local SKILL.md files.

The initialization sequence is: **load context → start loop → (model decides → tool runs → result returns → repeat)**

This means the agent's first tool-call decision is made with full project awareness and full capability awareness. The model knows what project it's in and what skills it has before processing the first user message.

## Why It Matters

The timing of context loading relative to the loop has composition implications:

**Context-before-loop (this pattern):**
- First response is project-aware — no "cold start" where the agent asks about project structure
- Skills are available from the first turn — the agent can immediately route to specialized behaviors
- Boot latency increases (loading context before the first response)
- Context budget is partially consumed before user interaction begins

**Context-during-loop (alternative):**
- Faster first response (no boot overhead)
- Context loaded only when needed (on-demand)
- First turns may be uninformed — agent may make assumptions that project context would have corrected
- Requires the agent to recognize when it needs context and explicitly load it

The existing KB covers WHAT gets loaded (context file taxonomy) and HOW it's loaded (progressive skill loading). This finding covers WHEN — the boot sequence ordering that determines whether the agent starts informed or starts fast.

## Why People Are Using It

Claude Code's architecture loads CLAUDE.md and skills before the first loop iteration. The video analyst describes this as "before any of this starts, the agent loads context" — the loading is explicitly sequenced before the loop, not interleaved with it.

The progressive-skill-loading finding documents a hybrid approach (DeerFlow): load skill summaries at boot, load full skill content on-demand. This is a refinement of the context-before-loop pattern that reduces boot latency while preserving first-turn awareness.

## Potential Improvements

- Profile the boot sequence to quantify the latency cost of context-before-loop vs. the quality cost of context-during-loop. For short tasks, boot overhead may dominate. For long tasks, first-turn quality matters more.
- Implement tiered boot loading: essential context (CLAUDE.md, active project state) at boot, secondary context (skills, reference files) on-demand.

## Potential Failure Modes

- **Boot bloat** — Loading too much context before the loop starts, consuming budget before the user's actual task is known. The progressive-skill-loading finding directly addresses this.
- **Stale boot context** — Context loaded at boot may become stale during long sessions. CLAUDE.md loaded at minute 0 may not reflect changes made by the agent at minute 30.
- **Missing context not detected** — If CLAUDE.md doesn't exist or is malformed, the agent starts the loop without project awareness but may not know it's missing. Graceful degradation vs. hard failure is a design choice.
