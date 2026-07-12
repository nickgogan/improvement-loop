---
name: 'Platform Capability Matrix with Explicit Unknowns as First-Class Values'
summary: 'Maintain a side-by-side matrix of harness capabilities (skill format, auto-load mechanism, activation modes, tool permissioning, subagent execution, context-file conventions, HITL primitives, validation tooling, distribution) across all target platforms — where every cell is either finding-cited evidence or the explicit literal "Unknown — verify against [platform] docs", never an inference. The matrix pairs with an adapter-strategy selection table mapping situation to porting mechanism (symlink, plugin wrapper, template generation, mirroring, duplication) and a "false portability" warning: skill content can port while skill effectiveness silently doesn''t.'
implementation_notes: 'Relevant to the portable-governance-kernel vision as the artifact shape for tracking where kernel pieces can actually run: the discipline of explicit Unknowns is the transferable part (matches the engine''s model-capability-registry rule — claims must be grounded, never invented). Maintenance cost is real (each platform release can stale cells), which argues for Watch rather than immediate adoption while the engine remains Claude-Code-only. The imported /meta-skill-author toolchain carries this matrix as platform-matrix.md; its overlap with /design-skill and /assess-skill is a flagged open question for the restructure program''s Phase 2 audit.'
category: Agent Design
evidence_strength: Medium (practitioner-documented, single production system)
adoption_status: Not Yet Started
priority: P3 (Watch)
applicability:
- General
adopted_in: []
sources:
- careerbuddy-meta-skill-author-references.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings: []
pipeline_status: raw
consumed_by: []
tags:
- cross-platform
- portability
- capability-matrix
- harness
---

# Platform Capability Matrix with Explicit Unknowns as First-Class Values

## Why It Matters

Cross-platform porting decisions usually run on remembered folklore about what Cursor or Copilot supports — and LLM-assisted authoring makes it worse, because a model will happily fill capability gaps with plausible inference. A capability matrix whose empty cells literally say "Unknown — verify against [platform] docs" converts that failure mode into a to-do list: every porting decision either stands on cited evidence or visibly names the verification debt it's taking on. The pattern is the epistemic discipline, not the specific table.

## What It Is

CareerBuddy's `platform-matrix.md`: a ~14-row × 5-platform comparison (Claude Code, Cursor, GitHub Copilot, OpenAI Codex, Perplexity) covering native skill format, auto-load mechanism (eager vs. lazy/progressive description loading), activation modes, frontmatter standard vs. extensions, tool permissioning, forked/subagent execution, reference-file loading, context-file taxonomy (CLAUDE.md / AGENTS.md / .cursorrules), HITL approval primitives, validation commands, skill hierarchy/override rules, and distribution mechanisms. Three cell value types: finding-cited fact, explicitly-tagged inference, or the literal Unknown marker. A closing section separates "confirmed by findings" evidence per platform from the open-standard floor all conformant platforms must support.

## How It Works

- **Portable floor first:** the matrix derives a guaranteed-everywhere layer (open-standard frontmatter, five-element body, progressive disclosure, pointers-over-copies) and an explicit "what does NOT port" list (all ~13 Claude Code extension fields, `$ARGUMENTS`, dynamic `` !`cmd` `` injection).
- **Adapter-strategy selection table:** two platforms with identical context-loading → symlink (`AGENTS.md -> CLAUDE.md`); different command/skill formats → plugin wrapper + runtime delegation (MemPalace: harness-agnostic instruction source + <40-line wrappers carrying only packaging metadata); 3–8 platforms with stable schema → template generation (gstack: `.tmpl` sources build 41 skills across 8 hosts); small count, max fidelity → per-platform mirroring; content duplication → "not recommended at scale."
- **Unresolved tensions are documented as unresolved** rather than force-resolved: eager vs. lazy description loading coexist across harnesses (rule: write descriptions that work under both); deterministic keyword routing suits stable catalogs < 15 skills, LLM description-matching suits growing libraries.
- **False-portability warning:** skill *content* ports while *effectiveness* may depend on platform features (file watching, subagent spawning) that don't exist on the target — porting requires per-platform behavioral validation, not just format translation.

## How It Could Fail

The matrix is a depreciating asset: platform release cadence stales cells fast, and a confidently wrong cell is worse than an Unknown. It needs a refresh trigger (per platform release, or scheduled) and ruthless scope — tracking every capability for every platform turns the aid into a maintenance sink.
