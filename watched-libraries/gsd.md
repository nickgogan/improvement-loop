---
name: "GSD (Get Shit Done)"
type: "watched-library"
repo_url: "https://github.com/gsd-build/get-shit-done"
description: "Lightweight meta-prompting, context engineering and spec-driven development system for Claude Code"
spectrum_position: "wholesale"
what_we_use: "Primary build orchestration — spec-driven phases, context clearing, git branch management, cost tracking, stuck-loop detection, crash recovery"
local_derivations:
  - ".claude/skills/"
last_evaluated_version: "v1.34.2"
last_evaluated_date: "2026-04-07"
maintainer: "gsd-build (TACHES / glittercowboy)"
status: "active"
tags:
  - "orchestration"
  - "claude-code"
  - "context-engineering"
related_findings:
  - "gsd-get-shit-done-plugin.md"
  - "gsd-global-learnings-store-cross-session-persistence.md"
  - "gsd-queryable-codebase-intelligence-store.md"
  - "gsd-gates-taxonomy-four-canonical-types.md"
  - "gsd-execution-context-profiles-mode-switching.md"
  - "gsd-stall-detection-revision-loop-escalation.md"
  - "gsd-prompt-injection-scanner-hardening.md"
related_sources:
  - "gsd-v1340-v1342-changelog.md"
date_added: "2026-04-07"
---

## What It Does

A Claude Code plugin that manages spec-driven development with discuss→plan→execute phases. Handles context clearing between tasks, git branch management, atomic commits, cost/token tracking, stuck-loop detection, and crash recovery. Cross-platform (Claude Code, OpenCode, Gemini CLI, Kilo, Codex). ~48.3K GitHub stars. Used by engineers at Amazon, Google, Shopify, Webflow.

## What We Use From It

Full build orchestration layer — GSD IS the execution engine for MetaSystem projects. Its spec-driven phases, context management, and git discipline align with MetaSystem's verify-before-build principle. MetaSystem's governance and constitutional constraints overlay GSD's execution model.

## Spectrum Rationale

Wholesale adoption with governance overlay. GSD's execution model is excellent and its opinions about phased development, context management, and git discipline match MetaSystem's values. MetaSystem overlays its own governance rules (DDs, human gates, constitutional constraints) as a thin wrapper, but the core GSD engine runs as-is. Updates are absorbed directly.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-07 | v1.33.0 | Initial evaluation. Discuss/plan/execute phases, wave-based parallel execution, workstream management. |
| 2026-04-07 | v1.34.2 | Global Learnings Store, Queryable Codebase Intelligence, 6 new commands, Execution Context Profiles, Gates taxonomy, prompt injection hardening. |
