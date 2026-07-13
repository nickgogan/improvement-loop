---
name: "BMAD Method"
type: "watched-library"
repo_url: "https://github.com/bmad-code-org/BMAD-METHOD"
description: "Breakthrough Method for Agile AI-Driven Development — multi-agent SDLC framework"
spectrum_position: "cherry-pick"
what_we_use: "Agent team model patterns, docs-as-code approach, context sharding techniques, scale-adaptive flow design"
local_derivations:
  - "systems/improvement-loop/knowledge/patterns/capability-type-selection.md"
last_evaluated_version: "v6.10.0"
last_evaluated_date: "2026-07-13"
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

## Upstream Delta: v6.2.2 → v6.10.0 (2026-04-07 → 2026-07-13)

Eight minor versions in ~3 months (v6.3.0 Apr 10 → v6.10.0 Jul 3). Confirmed via GitHub releases page, 2026-07-13. The everything-as-skill architecture held; on top of it BMAD added reasoning skills, governance primitives, and rebuilt product-layer skills — all three areas the restructure-program direction note asks about.

Changes that touch `what_we_use` and the direction-note asks:

- **High-level/critical-thinking skills (direction-note ask) — several new:** `bmad-forge-idea` (Socratic pressure-testing of half-formed ideas, v6.9.0), `bmad-investigate` (forensic investigation with evidence grading, v6.7.0), `bmad-prfaq` (Amazon Working Backwards, 5-stage, v6.3.0), and party-mode reborn with an anti-consensus room + persistent memory (v6.9.0/v6.10.0). This is exactly the critical-thinking skill layer that did not exist at v6.2.2.
- **Governance layer (direction-note ask):** decision-log pattern now canonical across workflows (v6.7.0); canonical memlog (`_bmad/scripts/memlog.py`) as a shared working-memory primitive across the suite (v6.9.0); four-layer TOML config resolver with `bmad-customize` guided override authoring (v6.4.0); `bmad-checkpoint-preview` for guided human review of commits/branches/PRs (v6.3.0).
- **Product layer (direction-note ask) rebuilt:** `bmad-spec` distills intent into a five-field kernel (Problem, Capabilities, Constraints, Non-goals, Success signal) (v6.8.0); `bmad-prd`/`bmad-product-brief` restructured around three intents Create/Update/Validate (v6.7.0); `bmad-ux` moved to a two-spine contract (DESIGN.md + EXPERIENCE.md) (v6.8.0); `bmad-architecture` rewritten around a lean `ARCHITECTURE-SPINE.md` source of truth (v6.9.0).
- **Agent-team model changed:** three personas (Barry, Quinn, Bob) consolidated into one Developer agent, Amelia (v6.3.0) — directly revises the agent-team composition pattern we cherry-picked.
- **Autonomous dev loop:** `bmad-loop` installable module for unattended dev-loop orchestration with adversarial review; `bmad-dev-auto` unattended worker driven by a spec-frontmatter state machine; `bmad-automator` deprecated (v6.10.0).
- Lower relevance: platform support expanded to 42 systems on the `.agents/skills/` standard (v6.5.0); stable/next release channels (v6.4.0); web bundles for Gemini Gems/Custom GPTs (v6.8.0); marketplace registry retired (v6.7.0).

**Recommendation:** a `/repo-analyzer` re-run IS warranted before restructure-program Phases 4/5 — the stored v6.2.2 analysis predates the entire critical-thinking skill layer, the decision-log/memlog governance primitives, and the rebuilt product-layer skills, which are precisely the surfaces the direction note wants evaluated. (Recommended only; not run in this pass.)

## Change Log

| Date | Version | Notes |
|------|---------|-------|
| 2026-04-07 | v6 (stable) | Initial evaluation. 26 agents, 68 workflows, step-file system, Playwright integration. |
| 2026-04-07 | v6.2.2 | Everything-as-skill architecture (SKILL.md entrypoints), YAML/XML workflows removed, outcome-based skill design, 13-column dependency graph, Qoder/Ona platform support. |
| 2026-07-13 | v6.10.0 | /watch-upstream refresh (named-deps gap-check). New reasoning skills (forge-idea, investigate, prfaq, anti-consensus party-mode), decision-log + memlog governance primitives, spec/prd/ux/architecture product-layer rebuilds, persona consolidation to Amelia, bmad-loop autonomous dev. See Upstream Delta section. /repo-analyzer re-run recommended before Phases 4/5. |
