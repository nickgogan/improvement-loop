---
name: 'Claude Code Ultra Plan: Three-Mode Cloud Planning'
summary: 'Ultra Plan is a cloud-based planning mode for Claude Code that offloads research and planning to Anthropic''s servers. Three server-controlled modes: simple (basic), visual (ASCII/Mermaid diagrams),
  and deep (multi-agent exploration with critique pass — agents analyze existing code, identify files/risks/dependencies, and review for missing steps).'
implementation_notes: Directly actionable — available in Claude Code now. Deep plan mode's multi-agent critique pass aligns with MetaSystem's verify-before-build principle.
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- anthropic-just-dropped-ultra-plan.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
related_findings:
- file: extract-deep-plan-prompt-as-custom-skill.md
  rel: enables
- file: anthropic-managed-agents-platform.md
  rel: same-problem
pipeline_status: "raw"
consumed_by: []
---
# Claude Code Ultra Plan: Three-Mode Cloud Planning

## What It Is
A planning mode that transfers planning from local terminal to Anthropic's cloud. Three internal strategies (server-selected): Simple plan (basic task breakdown), Visual plan (generates ASCII and Mermaid diagrams alongside standard plans), Deep plan (multi-agent exploration with separate agents for code architecture analysis, file identification, risk/dependency detection, and plan review with missing step/mitigation checks). Users can comment inline on proposed plans and teleport back to local terminal for execution.

Blast-radius task heuristic determines which tasks benefit from ultra-plan mode vs standard execution. Binary readable strings discovery uses deterministic string detection to avoid sending non-readable content to the LLM.

Cloud planning is consistently 2x faster across 10 matched comparisons. Dual execution path post-approval: "implement here" (current session) OR "start new session" with the plan. Local-to-Ultra refinement: option to "Refine with Ultra plan" transports a local plan to cloud for validation. A/B/C testing infrastructure: Anthropic uses remote config to assign users to variants and measures acceptance rates; the same infrastructure can route to unreleased models for plan quality evaluation. Parallel multitasking: spin up multiple Ultra Plans simultaneously and review all in the web UI. Plan isolation: cloud plans can be discarded without polluting local conversation context. Cloud execution: plans can execute directly on cloud without returning to the terminal.

## Why It Matters
Cloud planning is faster than local processing. Deep plan mode provides built-in multi-agent critique before implementation starts — catching issues that single-agent planning misses. The critique pass aligns with "verify before build" principles.

## Why People Are Using It
Ray Amjad demonstrates the full workflow including inline commenting on proposed plans and seamless transition back to local terminal. Available now in Claude Code without additional setup.

## Potential Alternatives
Local plan mode (slower but private). GSD plan-phase. Manual planning with spec documents. Superpowers brainstorming phase.

## Potential Improvements
User-selectable mode (currently server-controlled — users can't force deep plan). Integration with project-specific context for more targeted planning. Plan versioning and diff between iterations.

## Potential Failure Modes
Cloud dependency — requires internet connection. Privacy concerns for sensitive or proprietary codebases being sent to Anthropic's servers. Server-controlled mode selection may not match user intent — simple tasks may get deep plans and vice versa.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[three-mode-cloud-planning]] in `extracts/patterns/`
