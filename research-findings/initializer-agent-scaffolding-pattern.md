---
name: Initializer Agent Scaffolding Pattern
summary: A specialized first-session agent that expands a high-level prompt into a comprehensive feature list, creates progress tracking artifacts, and commits a clean baseline -- ensuring all subsequent
  coding sessions have structured state to orient from.
implementation_notes: MetaSystem's /bootstrap skill is a partial implementation. Could be extended with auto-generated feature lists and progress tracking files for new projects.
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- anthropic-effective-harnesses-long-running-agents.md
related_findings:
- file: progress-md-session-bridge.md
  rel: enables
- file: ralph-wiggum-execution-pattern.md
  rel: same-problem
- file: incremental-one-feature-per-session-pattern.md
  rel: enables
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: extracted
consumed_by:
- agents/initializer-agent-scaffolding.md
---

## What It Is

A dedicated first-session agent with a specialized prompt that sets up foundational scaffolding before any coding begins. It expands the user's high-level prompt into a comprehensive, granular feature requirements list (e.g., 200+ features for a complex app, each marked as "failing"), creates supporting artifacts like `claude-progress.txt` for state tracking, runs an `init.sh` script to bootstrap the environment, and commits an initial git state as a clean baseline. This agent runs only once; all subsequent sessions use a different "coding agent" prompt.

## Why It Matters

Without structured initialization, agents either attempt to one-shot the entire task (exhausting context with half-implemented features) or prematurely declare completion after seeing partial progress. The initializer solves both by creating an explicit, exhaustive scope definition that subsequent agents can work through incrementally.

## Why People Are Using It

Anthropic documents this as the foundation of their harness for long-running agents. The pattern addresses the core failure mode of autonomous coding: agents that don't know what "done" looks like. By making every feature explicit and marking them as "failing," the system creates an unambiguous progress signal.

## Potential Improvements

Dynamic feature decomposition where the initializer adjusts granularity based on task complexity. Integration with existing project management tools (IB items, roadmaps) rather than flat feature lists.

## Potential Failure Modes

Over-decomposition -- generating hundreds of trivial features that create overhead. Under-decomposition -- features too coarse to track meaningful progress. The initializer agent may misinterpret the user's intent, creating a feature list that diverges from actual requirements.

## Extraction Note — 2026-04-19
Extracted as **agent**: [[initializer-agent-scaffolding]] in `extracts/agents/`
