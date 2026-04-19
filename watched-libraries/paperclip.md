---
name: "Paperclip"
type: "watched-library"
repo_url: "https://github.com/paperclipai/paperclip"
description: "Open-source orchestration for zero-human companies"
spectrum_position: "cherry-pick"
what_we_use: "Multi-agent governance patterns — org charts, budget tracking, goal ancestry, approval gates, versioned config with rollback"
local_derivations: []
last_evaluated_version: "v2026.403.0"
last_evaluated_date: "2026-04-07"
maintainer: "paperclipai (@dotta)"
status: "active"
tags:
  - "orchestration"
  - "multi-agent"
related_findings: []
related_sources: []
date_added: "2026-04-07"
---

## What It Does

A Node.js server and React UI that orchestrates teams of AI agents to run a business. Provides org charts, budgets, governance, goal ancestry (agents see the "why" behind every task), approval gates, versioned config changes, and rollback capabilities. ~49K GitHub stars. Full plugin system since v2026.318.0.

## What We Use From It

Multi-agent governance patterns — particularly goal ancestry (tracing why an agent is doing something), approval gates (parallels to MetaSystem's human gates), and budget tracking per agent. These patterns inform MetaSystem's composable agent team model (DD-60) and milestone-gated development loop (DD-61).

## Spectrum Rationale

Cherry-pick. Paperclip operates at a different layer (multi-agent company orchestration) than MetaSystem (knowledge governance and build system). Its governance patterns (goal ancestry, approval gates, versioned config) are extractable design patterns, but the platform itself doesn't apply to MetaSystem's use case.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-07 | v2026.403.0 | Initial evaluation. Org charts, goal ancestry, approval gates, plugin system. |
