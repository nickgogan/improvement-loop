---
name: "Memory-File-to-Skill Migration (Cutting the Always-Loaded Token Tax)"
summary: |-
  Plain English: memory files (CLAUDE.md / AGENTS.md) load into every session whether the
  session needs them or not — so anything only *conditionally* useful in there is a
  standing token tax. Kun Chen's discipline: keep the global memory file minimal (~27
  lines of true always-on preferences); let the project memory file grow organically via
  correct-and-remember ("every time the agent does something wrong, ask it to store the
  learning"); then periodically migrate conditionally-useful sections (e.g., end-to-end
  testing instructions, only needed when the agent changes code) out of the memory file
  into skills, whose progressive disclosure loads only a one-line description until
  actually invoked. The agent performs the migration itself ("extract the E2E testing
  instructions from AGENTS.md into a project-level skill"); Anthropic's skill-creator
  skill teaches harnesses that lack the concept.
implementation_notes: |-
  A concrete maintenance rule for the engine's CLAUDE.md surfaces, complementing
  /simplify-context: the test for each memory-file section is "is this needed by every
  session, or only conditionally?" — conditional content migrates to a skill. Companion
  mechanic worth noting for agent-agnosticism: CLAUDE.md and AGENTS.md as symlinks to one
  file, so the same memory serves every harness.
  Caveat (reassessment 2026-07-13, Nick-accepted; P2 kept, no drop): Archon v0.5.0's
  rules-layer collapse (rules-layer-collapse-monolithic-context-counter-signal) is a
  live counter-signal; note however that its two monolithic mirror files have already
  observably drifted, which is evidence for, not against, this finding's discipline —
  and the finding feeds the IB-176 memory build now.
category: "Context Engineering"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "IL (CLAUDE.md maintenance, /simplify-context)"
  - "General"
adopted_in: []
sources:
  - "l8-principals-agentic-engineering-workflow.md"
related_findings:
  - file: "push-vs-pull-context-loading.md"
    rel: "extends"
  - file: "skill-as-directory-progressive-disclosure-three-levels.md"
    rel: "enabled-by"
  - file: "memorymd-cross-session-preference-persistence.md"
    rel: "same-problem"
  - file: "rules-layer-collapse-monolithic-context-counter-signal.md"
    rel: "contradicts"
proposals: null
date_discovered: "2026-07-12"
last_updated: "2026-07-13"
pipeline_status: "synthesized"
consumed_by:
  - "defending-agent-context.md"
  - "session-persistence-and-memory.md"
---

## What It Is

A lifecycle discipline for agent memory files, in three moves:

1. **Global memory stays minimal.** Everything in it enters every session's system prompt
   across all projects — Chen holds his to ~27 lines of genuinely universal preferences
   and bias corrections. "If we have too much content in this file, it will silently use
   a lot of our tokens."
2. **Project memory accumulates by correction.** Rather than authoring it up front, each
   time the agent errs, the fix is stored as a learning in the project memory file — the
   file becomes "the collective learning of all the agent sessions in this project." It
   bloats by design.
3. **Conditional content migrates to skills.** Periodically, sections only needed for
   some session types (testing procedures, deployment steps) are extracted into skills.
   Progressive disclosure then loads just the description line at startup and the full
   content only on invocation. The migration itself is delegated to the agent, which
   rewrites the memory file and creates the skill in one step.

## Why It Matters

This is the operational answer to memory-file bloat — the known failure mode of the
correct-and-remember pattern. Push-loaded memory and pull-loaded skills are usually
framed as an architectural either/or; this treats them as *lifecycle stages of the same
content*: knowledge enters through the memory file (cheap to capture) and graduates to a
skill once its conditionality is clear (cheap to carry). The always-loaded surface stays
small without losing any accumulated learning.

## Why People Are Using It

Chen runs this across all his projects with an explicitly harness-agnostic setup
(CLAUDE.md symlinked to AGENTS.md so one memory file serves Claude Code, Codex, Pi, and
opencode). Anthropic's skill-creator skill exists precisely to make step 3 delegable on
harnesses that don't natively know how to author skills.

## Potential Alternatives

- Rule/import mechanisms with conditional loading (path-scoped rules) — solve
  conditionality without skills, but only along predefined axes like directory
- Bounded/tiered memory systems with inference-driven curation — heavier machinery for
  the same tax

## Potential Improvements

- A periodic audit trigger (e.g., memory file exceeds N lines → run a migration pass)
  instead of relying on felt pain
- Migration provenance: note in the skill which memory-file learnings it absorbed, so
  corrections keep flowing to the right home

## Potential Failure Modes

- Over-migration: content the agent actually needs every session gets hidden behind a
  skill description it fails to invoke — the inverse tax (missed context) is worse than
  the token tax
- Skill sprawl: many micro-skills with overlapping descriptions degrade skill selection
- The agent-performed migration can drop nuance from the original learning; the diff
  needs review like any other change
