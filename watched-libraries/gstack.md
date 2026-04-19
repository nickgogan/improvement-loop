---
name: "gstack"
type: "watched-library"
repo_url: "https://github.com/garrytan/gstack"
description: "23 opinionated tools for Claude Code — CEO, Designer, Eng Manager, Release Manager, Doc Engineer, QA"
spectrum_position: "cherry-pick"
what_we_use: "Role-based specialist tool patterns, Conductor parallel session orchestration, design system generation approach"
local_derivations: []
last_evaluated_version: "v0.15.16.0"
last_evaluated_date: "2026-04-07"
maintainer: "garrytan (Garry Tan)"
status: "active"
tags:
  - "claude-code"
  - "orchestration"
  - "skills"
  - "tools"
related_findings:
  - "gstack-review-army-parallel-specialist-dispatch.md"
  - "gstack-four-layer-prompt-injection-defense.md"
  - "gstack-tabsession-per-tab-state-isolation.md"
  - "gstack-dx-review-developer-experience-audit.md"
  - "session-persistence-crash-resilient.md"
  - "self-evolving-loop-pattern.md"
related_sources:
  - "gstack-v01590-v015160-changelog.md"
date_added: "2026-04-07"
---

## What It Does

A Claude Code skill pack with 23 role-based specialist tools (CEO product review, design system creation, engineering management, release management, documentation, QA testing). Includes AI-controlled Chromium browser with anti-bot stealth, automated docs updates, and Conductor tool for parallel Claude Code sessions with isolated workspaces. ~65.3K GitHub stars. TypeScript (79.6%) + Go (18.3%).

## What We Use From It

Role-based specialist tool design (how to make one agent act as different team members). Conductor pattern for parallel Claude Code sessions. Design system generation approach (competitor analysis → design system → style guide). These patterns inform MetaSystem's agent templates (DD-60, DD-64).

## Spectrum Rationale

Cherry-pick. gstack is highly opinionated (Garry Tan's personal workflow) and includes capabilities (browser automation, deployment, CEO review) that don't apply to MetaSystem's knowledge governance focus. The role-based tool patterns and Conductor orchestration are extractable design patterns.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-07 | v0.15.9.0 | Initial evaluation. 23 tools, Conductor, multi-agent browser platform. |
| 2026-04-07 | v0.15.16.0 | Session Intelligence Layer (checkpoint/health/recovery), Review Army parallel specialists, 4-layer prompt injection defense, recursive self-improvement, OpenClaw skills, TabSession, 31 total skills. |
