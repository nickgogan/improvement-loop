---
name: "BMAD Method"
type: "watched-library"
repo_url: "https://github.com/bmad-code-org/BMAD-METHOD"
description: "Breakthrough Method for Agile AI-Driven Development — multi-agent SDLC framework"
spectrum_position: "cherry-pick"
what_we_use: "Agent team model patterns, docs-as-code approach, context sharding techniques, scale-adaptive flow design"
local_derivations:
  - "systems/meta-system/knowledge/patterns/capability-type-selection.md"
last_evaluated_version: "v6.2.2"
last_evaluated_date: "2026-04-07"
maintainer: "bmad-code-org (Brian / bmadcode)"
status: "active"
tags:
  - "orchestration"
  - "multi-agent"
  - "skills"
related_findings:
  - "bmad-method-v6-multi-agent-sdlc.md"
  - "bmad-outcome-based-skill-rewrite-pattern.md"
  - "bmad-dependency-graph-module-ordering.md"
  - "bmad-deterministic-skill-validator.md"
  - "skills-as-markdown-sop-files-encode-processes.md"
related_sources:
  - "bmad-v6-is-finally-here.md"
  - "bmad-method-masterclass.md"
date_added: "2026-04-07"
---

## What It Does

A comprehensive SDLC framework with 26 specialized agents, 68 workflows, and a 4-phase development cycle (Analysis→Planning→Solutioning→Implementation). Uses docs-as-code with context sharding. Includes BMad Builder for custom modules, marketplace ecosystem, and Playwright integration for E2E testing. ~43.7K GitHub stars.

## What We Use From It

Agent team composition patterns (how to define agent roles with specific personas, context permissions, and handoff protocols). Docs-as-code approach (PRDs/architecture as source of truth). Context sharding (atomic story files saving 90% tokens). Scale-adaptive flows (Quick vs Enterprise). We do NOT adopt the framework wholesale — MetaSystem has its own governance model.

## Spectrum Rationale

Cherry-pick. BMAD's opinions about agent roles, workflow phases, and docs-as-code are valuable patterns, but they conflict with MetaSystem's constitutional constraints, fractal structure, and governance model. We extract patterns (agent team composition, context sharding, docs-as-code) and rewrite them for our context. The BMAD ecosystem (5 repos: BMAD-METHOD, bmad-builder, bmad-method-test-architecture-enterprise, bmad-module-creative-intelligence-suite, bmad-module-template) is tracked as one unit.

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-07 | v6 (stable) | Initial evaluation. 26 agents, 68 workflows, step-file system, Playwright integration. |
| 2026-04-07 | v6.2.2 | Everything-as-skill architecture (SKILL.md entrypoints), YAML/XML workflows removed, outcome-based skill design, 13-column dependency graph, Qoder/Ona platform support. |
