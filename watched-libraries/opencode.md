---
name: "opencode"
type: "watched-library"
repo_url: "https://github.com/anomalyco/opencode"
description: "Leading open-source terminal coding agent (canonical opencode; SST org renamed to Anomaly Co)"
spectrum_position: "study"
what_we_use: "Nothing adopted yet — study target. Agent-context file surface (AGENTS.md, CONTEXT.md, .opencode/), specs/ directory, harness/loop design as a Claude Code comparison point"
local_derivations: []
last_evaluated_version: "dev branch HEAD (2026-07-11)"
last_evaluated_date: "2026-07-11"
maintainer: "anomalyco (formerly SST)"
status: "active"
tags:
  - "harness"
  - "coding-agent"
  - "context-engineering"
  - "loop-engineering"
related_findings: []
related_sources: []
date_added: "2026-07-11"
---

## What It Does

The open-source AI coding agent for the terminal — the largest-starred coding-agent repo
(~184k stars, MIT, TypeScript monorepo; extremely active, pushed daily), now also shipping a
beta desktop app. Monorepo carries packages/, sdks/, specs/, infra/, and its own agent-context
files (AGENTS.md, CONTEXT.md, `.opencode/` config dir).

**Provenance note:** this is the canonical opencode under its current home — the SST org renamed
to Anomaly Co (npm `opencode-ai`, opencode.ai). The archived 13.4k-star `opencode-ai/opencode`
is the separate pre-dispute project; don't confuse the two.

## What We Use From It

Study target — nothing adopted. Primary reference harness for the tool/harness-design and
loop-engineering dimensions, and a comparison point for the agentic-OS harness layer. Its
in-repo agent-context surface (AGENTS.md, CONTEXT.md, `.opencode/`, specs/) is exactly the
structure `/repo-analyzer` mines.

## Spectrum Rationale

Study. Like OpenClaw, it competes with Claude Code as a platform, so we don't adopt it — but as
the most widely used open coding agent its harness architecture, context-file conventions, and
spec-driven workflow are high-signal study material for our harness-layer formalization.
`/repo-analyzer` pass queued (link-intake triage 2026-07-11).

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-07-11 | dev HEAD | Initial entry from link-intake triage pilot. Provenance verified (SST → Anomaly Co rename). /repo-analyzer pass queued. |
