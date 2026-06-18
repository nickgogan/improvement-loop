---
name: "Greenfield vs Brownfield Framework Selection Heuristic"
summary: "Practitioner heuristic for framework composition: greenfield projects warrant the full stack (gstack planning + GSD phase decomposition + Superpowers TDD execution); brownfield projects should use only one or two frameworks (e.g., Superpowers alone for single features, gstack + Superpowers for semi-large additions). The rationale: greenfield projects benefit from the full brainstorm-to-execute pipeline because there is no existing architecture to constrain decisions, while brownfield work has existing context that makes full-stack planning overhead wasteful."
implementation_notes: null
category: "Agentic Systems"
evidence_strength: "Anecdotal"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "gstack-gsd-superpowers-orchestrator-headless.md"
related_findings:
  - file: "multi-framework-orchestration-power-stack.md"
    rel: "extends"
  - file: "framework-tension-taxonomy-superpowers-gsd-gstack.md"
    rel: "extends"
  - file: "effort-scaling-rules-embedded-in-orchestrator.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "raw"
consumed_by: []
tags:
  - "session-95-reextract"
---

# Greenfield vs Brownfield Framework Selection Heuristic

## What It Is

A practitioner-articulated decision framework for choosing how many orchestration frameworks to compose based on project type:

| Project Type | Recommended Stack | Rationale |
|---|---|---|
| **Greenfield (from scratch, large)** | gstack + GSD + Superpowers (full stack) | No existing architecture constrains decisions; full brainstorm-to-execute pipeline adds maximum value |
| **Brownfield (existing codebase, single feature)** | Superpowers alone | Existing architecture provides context; only execution discipline is needed |
| **Brownfield (semi-large addition)** | gstack + Superpowers | Some planning needed for design decisions, but existing codebase doesn't need full phase decomposition |

The key insight: framework composition overhead is only justified when the project's uncertainty warrants it. Greenfield projects have maximum uncertainty (no architecture, no patterns, no conventions), so they benefit from the full planning-decomposition-execution pipeline. Brownfield projects have existing structure that reduces uncertainty, so lighter-weight composition is appropriate.

The heuristic also implicitly suggests that GSD (phase decomposition for context isolation) is most valuable for large projects -- small feature additions don't need context isolation because they fit in a single session.

## Why It Matters

Most framework composition guidance assumes a single "best" configuration. This heuristic provides a graduated selection model: match framework investment to project uncertainty. This prevents the common failure mode of over-engineering small tasks with full orchestration stacks (high ceremony for low complexity) or under-engineering large builds with insufficient planning (jumping to code on a greenfield project).

For MetaSystem, this maps to a question: when should `/gsd-autonomous` (full pipeline) be used vs. `/gsd-fast` or `/gsd-quick` (reduced pipeline)? The heuristic suggests that the distinguishing factor is project novelty, not project size alone.

## Why People Are Using It

Stated as explicit practitioner guidance in the demo video (Eric Tech). Not yet validated with controlled comparisons. The recommendation is experience-based: practitioners who used the full stack on brownfield projects found it wasteful; those who skipped planning on greenfield projects found they had to redo work.

## Potential Improvements

- Add a third dimension beyond greenfield/brownfield: project duration. Short greenfield projects (hours) may not warrant full stack even though they're from scratch
- Define concrete thresholds for "large" and "semi-large" (e.g., by estimated phase count, file count, or token budget)
- Include a decision tree format that agents can follow automatically, rather than relying on practitioner judgment

## Potential Failure Modes

- **Misclassification.** The greenfield/brownfield distinction is not binary -- a project adding a major new subsystem to an existing codebase has greenfield characteristics within a brownfield context. The heuristic provides no guidance for this common case.
- **Overhead blindness.** Teams may default to the full stack "just in case" for any project with ambiguity, negating the efficiency gains of the lighter options.
- **Framework coupling.** Once a team builds muscle memory around the full stack, they may resist dropping down to a simpler configuration even when appropriate.
