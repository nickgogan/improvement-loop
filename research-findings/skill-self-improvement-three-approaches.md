---
name: "Skill Self-Improvement — Three Independent Approaches"
summary: "Three repos independently implement skill-level self-improvement with distinct mechanisms: OB1 (lessons log + self-modification), gstack (external learnings JSONL), Superpowers (meta-skill for skill authorship). Convergence on 'skills should improve' without convergence on mechanism suggests the problem is real but the solution space is open."
implementation_notes: "MetaSystem skills don't self-improve. Three approaches to evaluate: (1) OB1-style lessons log per skill (most direct), (2) gstack-style shared learnings store (cross-skill), (3) Superpowers-style meta-generation (framework-level). Consider combining: shared learnings for cross-cutting patterns + per-skill lessons for skill-specific failures."
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: "self-improving-skill-lessons-log.md"
    rel: "extends"
  - file: "meta-skill-for-skill-authorship.md"
    rel: "same-problem"
  - file: "self-evolving-loop-pattern.md"
    rel: "same-problem"
  - file: "gsd-global-learnings-store-cross-session-persistence.md"
    rel: "same-problem"
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: "synthesized"
consumed_by:
  - agent-design-patterns.md
---

## What It Is
A cross-repo pattern where three independent implementations address the same problem — how should skills get better over time? — with three distinct mechanisms:

1. **OB1 — Self-modification with lessons log.** Skills include a Phase 4 "self-improvement" step and a persistent Lessons Log table. After every invocation, the skill evaluates what went wrong (lost work, token waste, user corrections) and directly edits its own file. The Panning for Gold skill has 6 production-learned lessons across 13+ sessions.

2. **gstack — External learnings JSONL.** A `/learn` skill captures insights into an append-only JSONL file. At session start, the shell preamble searches this file for relevant learnings. Skills themselves don't change — the improvement lives in a separate knowledge store that all skills can access.

3. **Superpowers — Meta-skill for skill authorship.** A `writing-skills/` directory contains a skill that teaches agents how to write skills, applying persuasion principles and Anthropic best practices. This enables framework self-extension rather than individual skill improvement.

## Why It Matters
Most agent skill systems are static — skills are written once and only change when a human edits them. These three approaches break that assumption from different angles: OB1 changes the skill directly (fastest feedback loop), gstack builds a shared knowledge base (broadest applicability), Superpowers generates new skills (highest leverage but no individual improvement). The convergence on the problem ("skills should improve") without convergence on the mechanism suggests this is a genuine unmet need in the ecosystem.

## Why People Are Using It
Observed across three independent repos: [OB1](https://github.com/NateBJones-Projects/OB1) (see [[ob1-analysis]]), gstack (see [[gstack-analysis]]), and Superpowers (see [[superpowers-analysis]]). OB1's approach is the most production-tested — 6 lessons from real sessions, including a complete Phase 0.5 (Speaker Consolidation) added after a transcript misattribution incident. gstack's approach is the simplest to implement. Superpowers' approach is the most architecturally ambitious.

## Potential Alternatives
- **System-level improvement loops** (MetaSystem's IL, OpenAI self-evolving agents): Operate at system scope. Better for cross-cutting improvements but too slow for individual skill failures.
- **Version-controlled skill evolution** (manual): Human edits skills based on experience. Works but doesn't capture the failures that happen between human reviews.

## Potential Improvements
- **Hybrid approach**: Shared learnings store for cross-cutting patterns (gstack-style) + per-skill lessons log for skill-specific failures (OB1-style) + meta-skill for generating new skills from accumulated learnings (Superpowers-style).
- **Automated lesson promotion**: When a lesson appears in 3+ skills' logs, promote it to a shared rule.
- **Regression detection**: Check whether previously-learned lessons are being violated.

## Potential Failure Modes
- Self-modifying skills can introduce errors (OB1 risk)
- External learnings stores can grow unbounded without relevance filtering (gstack risk)
- Meta-skills generate skills without operational experience (Superpowers risk)
- All three approaches assume the skill environment is stable — major platform changes may invalidate accumulated lessons
