---
name: Three-Layer Context Chain Loading
summary: GSD's command→workflow→agent @-reference chain pre-assembles complete context through three layers of dynamic injection — commands reference workflows, workflows reference docs, agents read project
  CLAUDE.md and skills — giving agents full context without needing to discover what to load.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources: []
related_findings:
- file: skill-chaining-composing-workflows-from-modular-s.md
  rel: same-problem
- file: push-vs-pull-context-loading.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-08'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Three-Layer Context Chain Loading

## What It Is
GSD implements a three-layer push-model context loading chain. Commands are the entry points loaded by the harness. Each command `@`-references one or more workflow files, which in turn `@`-reference reference documents. Agents further read the user's project CLAUDE.md and skills. The harness resolves the full chain before the agent sees any of it, producing a pre-assembled context package. This is a push model: the orchestrator decides what context the agent needs and delivers it complete.

## Why It Matters
Context completeness is a precondition for reliable agent behavior. If an agent must discover what to load, it can miss critical context — especially context it does not know exists. The three-layer chain guarantees that every command brings its full dependency tree of workflows, reference docs, and project-specific configuration into the agent's context window before execution begins.

## Why People Are Using It
Observed in [GSD](https://github.com/gsd-build/get-shit-done) v1.33.0 — see [[gsd-analysis]] for structural details. GSD's workflow topology routes every user command through this chain, ensuring agents operating in discuss, plan, execute, and verify phases always have the relevant workflow instructions and reference materials loaded. The pattern eliminates the failure mode where an agent starts work without knowing the full set of constraints or procedures.

## Potential Alternatives
Pull-model context loading (Superpowers) where the agent self-activates skills on demand. Progressive disclosure (BMAD) where metadata loads first, full instructions on demand. Static monolithic CLAUDE.md that packs everything into a single file. MCP-based context retrieval where agents query a context server.

## Potential Improvements
Chain depth visibility — a manifest showing what was loaded and from where, so humans can audit what the agent actually received. Conditional loading where branches of the chain are skipped based on task type, reducing context bloat for simple operations. Token budget awareness so the chain resolver can prune low-priority references when approaching context limits.

## Potential Failure Modes
Context bloat — deep chains can load substantial amounts of text, consuming context window capacity that would be better used for task execution. Stale references — if a workflow file is updated but the command file's reference is not, the agent gets outdated instructions. Circular references between files could cause infinite resolution loops if the harness does not detect cycles.
