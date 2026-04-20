---
name: Zero Framework Cognition (ZFC)
summary: Architectural principle keeping all cognitive/heuristic logic in LLM prompts, not in application code. Code handles state transitions, SQL queries, and data flow; LLMs handle all decisions. No
  hardcoded sequential logic in AI decision paths.
implementation_notes: null
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: framework-abstraction-tax-for-agents.md
  rel: extends
proposals: null
date_discovered: '2026-04-19'
last_updated: '2026-04-19'
---

## What It Is

A named architectural principle: all cognitive logic (heuristics, decision-making, task routing, prioritization) lives in LLM prompts, never in application code. Application code is "dumb orchestration" — state transitions, database queries, dependency graph traversal, I/O. The explicit constraint: "No hardcoded sequential logic in AI decision code." This inverts the typical pattern where code implements decision trees and the LLM fills in gaps.

## Why It Matters

Extends the "framework abstraction tax" observation (existing KB finding) from a warning into a design principle. If frameworks add overhead and rigidity, ZFC is the logical endpoint: minimize the framework to pure plumbing and let the LLM handle all flexibility. This makes the system more adaptable (prompt changes vs. code changes) but requires the LLM to be reliable enough to handle the cognitive load.

## Why People Are Using It

Observed in [Beads](https://github.com/gastownhall/beads) v1.0.2 — see [[beads-analysis]] for structural details. Beads explicitly documents ZFC in its CONTRIBUTING.md as an architectural constraint enforced via code review. The Go codebase handles state machines, SQL, and graph operations; all routing and decision-making is delegated to the LLM via the `bd` CLI's agent instructions.

## Potential Alternatives

- Hybrid approach: code handles well-understood decisions, LLM handles ambiguous ones
- Traditional decision trees with LLM fallback
- Full framework orchestration (LangGraph, CrewAI)

## Potential Improvements

Could be paired with a "cognitive boundary" specification that explicitly marks which decisions are LLM-owned vs. code-owned, preventing drift.

## Potential Failure Modes

- LLM inconsistency on repeatable decisions (same input, different output)
- Debugging difficulty — cognitive logic is in prompts, not traceable code
- Performance cost — every decision requires an LLM call instead of a code branch
