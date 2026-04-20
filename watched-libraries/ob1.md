---
name: "OB1 (Open Brain)"
type: "watched-library"
repo_url: "https://github.com/NateBJones-Projects/OB1"
description: "Persistent AI memory system — one Supabase database (pgvector), one MCP protocol, any AI client. Community-driven repo of extensions, recipes, skills, schemas, dashboards, and integrations for building a personal/business OS on top of a shared brain"
spectrum_position: "cherry-pick"
what_we_use: "Skill template architecture, recipe composition patterns, extension learning path design, automated PR review agent, community contribution governance, personal OS domain extensions"
local_derivations: []
last_evaluated_version: "latest"
last_evaluated_date: "2026-04-20"
maintainer: "NateBJones (Nate B. Jones)"
status: "active"
tags:
  - "agentic-os"
  - "personal-os"
  - "memory"
  - "skills"
  - "mcp"
  - "supabase"
  - "community"
related_findings: []
related_sources: []
date_added: "2026-04-20"
---

## What It Does

A persistent AI memory system and personal OS platform built on Supabase (PostgreSQL + pgvector) with MCP protocol. Any AI client (Claude, ChatGPT, Cursor, Claude Code, Codex) can plug into the same shared brain. The repo is a community-driven collection of extensions, recipes, skills, schemas, dashboards, and integrations that build on top of the core Open Brain database.

Key capabilities:
- **One shared brain**: Single Supabase database with vector search, accessible by any AI client via MCP
- **Progressive extension learning path**: 6 curated extensions (household knowledge → home maintenance → calendar → meals → CRM → job hunt) that compound — each builds on prior extensions
- **Community recipe ecosystem**: 25+ standalone recipes for data import (ChatGPT, Gmail, Twitter, Instagram, Obsidian vault), workflow automation (Panning for Gold, Life Engine, Daily Digest), and intelligence workflows
- **Skill packs**: Portable plain-text AI skills (auto-capture, meeting synthesis, competitive analysis, world model diagnostic, n-agentic harnesses) designed to work across multiple AI clients
- **Automated PR review**: GitHub Actions CI + Claude Code admin review skill for quality gating
- **Remote MCP pattern**: All extensions deploy as Supabase Edge Functions, never local servers

## What We Use From It

Cherry-pick patterns:
1. **Skill template architecture** — simple frontmatter schema (name, description, author, version) + Problem/Trigger/Process/Output/Notes sections. Portable across AI clients.
2. **Recipe composition pattern** — standalone capability builds with `requires_skills` dependency declarations linking to canonical skill packs
3. **Extension progressive learning path** — curated 6-build sequence with compounding integrations (CRM knows about captured thoughts, meal planner checks who's home)
4. **Self-improving skill lessons log** — Panning for Gold skill includes a Lessons Log table and Phase 4 "self-improvement" step that updates the skill file after every use
5. **Automated PR review agent** — two-layer review: GitHub Actions CI for mechanical checks (15 rules) + Claude Code admin skill for security deep scan, mission fit, naming consistency
6. **Community contribution governance** — curated vs open categories, contributor ladder (member → contributor → regular → maintainer), non-technical contribution path
7. **Personal OS domain extensions** — household knowledge, home maintenance, family calendar, meal planning, professional CRM, job hunt pipeline — real-world domain modeling for agentic OS

## Spectrum Rationale

Cherry-pick. OB1's core architecture (Supabase + MCP remote Edge Functions) is fundamentally different from MetaSystem's file-first Obsidian vault approach. But the skill/recipe/extension patterns, community governance model, self-improving skill design, and personal OS domain coverage are rich sources of research findings for Context Engineering, Agent Design, Governance, and Agentic OS dimensions.
