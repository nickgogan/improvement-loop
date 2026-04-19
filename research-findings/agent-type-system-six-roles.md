---
name: Agent Type System (Six Built-In Roles with Explicit Constraints)
summary: A formal agent type system where each role (Explore, Plan, Verify, Guide, General Purpose, Status Line Setup) has its own system prompt, allowed tool set, and explicit behavioral constraints to
  prevent cross-role contamination.
implementation_notes: MetaSystem's DD-60 (composable agent teams) defines PO, Architect, TPM, Engineer, Tester roles. Mapping these to formal type constraints with tool allow-lists would strengthen the
  pattern.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropics-2-5-billion-leak-12-critical-pieces.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
related_findings:
- file: dynamic-tool-pool-assembly-transcript-compaction.md
  rel: enables
- file: two-level-verification-agent-run-plus-harness-inte.md
  rel: enables
- file: agent-cost-blowup-mitigation-strategies.md
  rel: same-problem
- file: explicit-permission-allow-listing-for-agent-resou.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
---
# Agent Type System (Six Built-In Roles with Explicit Constraints)

## What It Is
Six built-in agent types: Explore (can't edit files), Plan (doesn't execute code), Verify, Guide, General Purpose, Status Line Setup. Each type has its own prompt, allowed tools, and explicit constraints. The type system prevents cross-role contamination — an Explore agent physically cannot edit files.

## Why It Matters
Without role constraints, agents drift toward general-purpose behavior. Type enforcement ensures agents stay in their lane, improving reliability and predictability.

## Why People Are Using It
Anthropic's production Claude Code. The pattern maps to the broader multi-agent role separation trend (also seen in BMAD Method, DD-60).

## Potential Alternatives
Prompt-only role separation (no tool enforcement). Single general-purpose agent with mode switching. Custom role definitions per project.

## Potential Improvements
User-extensible type system. Role composition (combining capabilities from multiple types). Dynamic type switching within a session.

## Potential Failure Modes
Too-rigid types that don't cover real workflows. Type proliferation that fragments agent capabilities. Users bypassing type constraints to get work done.
