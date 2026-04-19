---
name: "OpenClaw"
type: "watched-library"
repo_url: "https://github.com/openclaw/openclaw"
description: "Open-source AI assistant — any OS, any platform"
spectrum_position: "cherry-pick"
what_we_use: "SOUL.md agent constitution pattern, memory file taxonomy (SOUL.md/USER.md/MEMORY.md/HEARTBEAT.md/AGENTS.md/TOOLS.md), ClawHub skill directory architecture"
local_derivations: []
last_evaluated_version: "v2026.4.5"
last_evaluated_date: "2026-04-07"
maintainer: "openclaw"
status: "active"
tags:
  - "claude-code"
  - "context-engineering"
  - "memory"
  - "tools"
related_findings:
  - "soul-md-agent-constitution-pattern.md"
  - "context-file-taxonomy-claude-md-soul-md-agents-md-etc.md"
related_sources:
  - "openclaw-soul-md-explained.md"
date_added: "2026-04-07"
---

## What It Does

An open-source AI coding assistant that runs on any OS/platform. Features ClawHub skill directory, headless CLI for Agent Client Protocol sessions, and a massive extension ecosystem. ~346K GitHub stars (most-starred project on GitHub as of April 2026). Extremely rapid release cadence (13 releases in March 2026 alone).

## What We Use From It

SOUL.md pattern — separating agent identity (personality, values, instructions, restrictions) from capabilities (skills, tools). Memory file taxonomy (SOUL.md for identity, USER.md for user info, MEMORY.md for logs, HEARTBEAT.md for proactive tasks, AGENTS.md for rules, TOOLS.md for tool conventions). These patterns inform MetaSystem's context file architecture.

## Spectrum Rationale

Cherry-pick. OpenClaw is a direct competitor to Claude Code — we don't adopt it as a platform. But its context file taxonomy and SOUL.md constitution pattern are valuable design patterns we can extract and adapt for MetaSystem's own agent identity and memory architecture. The patterns are framework-agnostic.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-07 | v2026.4.5 | Initial evaluation. SOUL.md pattern, 6-file memory taxonomy, ClawHub architecture. |
