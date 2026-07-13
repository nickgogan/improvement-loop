---
name: "Superpowers"
type: "watched-library"
repo_url: "https://github.com/obra/superpowers"
description: "Agentic skills framework and software development methodology"
spectrum_position: "thin-wrapper"
what_we_use: "TDD enforcement pattern, skill auto-activation model, 7-phase workflow structure, subagent orchestration with two-stage review"
local_derivations: []
last_evaluated_version: "v6.1.1"
last_evaluated_date: "2026-07-13"
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

## Upstream Delta: v5.0.7 → v6.1.1 (2026-04-07 → 2026-07-13)

One major release (v6.0.0, 2026-06-16) plus stabilization patches through v6.1.1 (2026-07-02). Confirmed via GitHub releases page, 2026-07-13.

Changes that touch `what_we_use`:

- **Two-stage review is gone upstream.** v6.0.0 rewrote Subagent-Driven Development: a single unified reviewer per task returns spec-compliance and quality verdicts in one pass, replacing the two sequential reviewers. Our `what_we_use` ("two-stage review") and the related finding now describe a superseded architecture. Upstream's eval numbers: ~50% fewer tokens, ~2x faster than v5.x.
- **Subagent orchestration hardened:** plans carry a Global Constraints block + per-task Interfaces block; pre-flight plan read before the first task; whole-branch review at the end instead of per-task; diffs/briefs/reports exchanged as files (not pasted) in a self-ignoring `.superpowers/sdd/` workspace (v6.0.3); dispatches require explicit model specification; review is read-only and controllers cannot override reviewer findings. Strong overlap with our file-mediated handoff protocol — corroborating pattern.
- **Brainstorming HARD-GATE / thinking skills (direction-note ask): no documented changes.** Release notes since v5.0.7 mention no changes to brainstorming-skill enforcement or new thinking skills; brainstorming changes are companion-app security hardening only (per-session auth key, sandbox enforcement, 4h idle timeout). TDD unchanged except implementer reports now include red/green evidence.
- **Vendor-neutral skill language:** skills rewritten to generic action vocabulary ("dispatch subagent") with per-harness tool-mapping references; "Claude Search Optimization" renamed "Skill Discovery Optimization"; bootstrap compressed for per-session token cost (v6.1.0).
- Lower relevance: three new harnesses (Kimi Code, Pi, Antigravity); Gemini CLI support removed (Google EOL); behavior tests moved to a separate `evals/` repo using a "drill" framework (real sessions + LLM judging).

**Recommendation:** a `/repo-analyzer` re-run IS warranted before restructure-program Phases 4/5 — but not for the direction-note asks. The brainstorming HARD-GATE and thinking-skill surfaces are unchanged upstream, so the stored analysis remains valid for those questions. What is stale is the SDD review/orchestration architecture in `what_we_use`: the two-stage-review pattern we recorded (and cite in DD-62 quality-tier design) was replaced by the unified-reviewer + file-mediated-artifact model in v6.0.0. If Phases 4/5 touch review/orchestration patterns, refresh first; if they only need brainstorming/thinking skills, the v5.0.7 analysis still answers them.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-07 | v5.0.7 | Initial evaluation. 14 skills, 7-phase workflow, marketplace-accepted. |
| 2026-07-13 | v6.1.1 | /watch-upstream refresh (named-deps gap-check). v6.0.0 SDD rewrite: unified single reviewer replaces two-stage review, file-mediated diffs/briefs, Global Constraints + Interfaces plan blocks, read-only review; vendor-neutral skill language; brainstorming HARD-GATE unchanged. See Upstream Delta section. /repo-analyzer re-run recommended if Phases 4/5 rely on review/orchestration patterns. |
