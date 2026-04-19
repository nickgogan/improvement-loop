---
name: "Superpowers"
type: "watched-library"
repo_url: "https://github.com/obra/superpowers"
description: "Agentic skills framework and software development methodology"
spectrum_position: "thin-wrapper"
what_we_use: "TDD enforcement pattern, skill auto-activation model, 7-phase workflow structure, subagent orchestration with two-stage review"
local_derivations: []
last_evaluated_version: "v5.0.7"
last_evaluated_date: "2026-04-07"
maintainer: "obra (Jesse Vincent / Prime Radiant)"
status: "active"
tags:
  - "orchestration"
  - "skills"
  - "evaluation"
  - "claude-code"
related_findings:
  - "superpowers-plugin-spec-driven-sub-agent-orchestration.md"
related_sources:
  - "claude-code-plus-superpowers-tutorial.md"
date_added: "2026-04-07"
---

## What It Does

A composable skills framework for Claude Code with 14 enforced skills covering TDD, systematic debugging, git worktrees, parallel subagents, brainstorming, planning, code review, and finishing. Skills auto-activate based on context. Officially in the Anthropic marketplace. 7-phase workflow: brainstorm→plan→worktree→execute→review→test→finish. ~42K GitHub stars.

## What We Use From It

TDD enforcement pattern (RED-GREEN-REFACTOR with deletion of pre-test code). Skill auto-activation model (context-aware triggers rather than manual invocation). Subagent orchestration pattern (main agent plans, subagents implement, reviewer checks). Two-stage review (spec compliance then quality). These patterns inform MetaSystem's agent templates and quality tier design (DD-62).

## Spectrum Rationale

Thin wrapper. Superpowers' skill-based approach and TDD discipline are valuable, but its 7-phase workflow partially conflicts with MetaSystem's milestone-gated development loop (DD-61) and GSD's execution model. We use it alongside GSD (not instead of) by activating specific skills we need. The wrapper maps Superpowers' phases to MetaSystem's governance gates.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-07 | v5.0.7 | Initial evaluation. 14 skills, 7-phase workflow, marketplace-accepted. |
