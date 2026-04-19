---
name: gstack Specialist Role Architecture and 5-Layer Governance
summary: gstack replaces single general-purpose agent with specialist role pipeline (CEO, Engineer, QA, Designer, Release Engineer). The 5-layer governance system (Role Focus, Data Flow, Quality Control,
  Boil the Lake, Keep Simple) makes role adherence robust. Garry Tan (YC CEO) created it.
implementation_notes: The 5-layer governance and 'Boil the Lake' principle are independently valuable patterns. Design which roles map to MetaSystem's agent systems.
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- these-3-frameworks-make-claude-code-unstoppable.md
proposals: null
date_discovered: '2026-04-07'
last_updated: 2026-04-08
related_findings:
- file: agent-architecture-layer-impermanence.md
  rel: contradicts
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
---

## What It Is

gstack is a Claude Code framework built by Garry Tan (CEO of Y Combinator) that replaces a single general-purpose agent with a pipeline of **specialist role agents**. Rather than having one Claude instance handle planning, building, and QA, gstack defines distinct roles that activate at different stages:

- **CEO** — high-level planning, architecture review, final sign-off
- **Engineer / Engineer Manager** — implementation and technical decisions
- **QA / QA Lead** — browser testing (Playwright), bug reporting, testing checklists
- **Designer** — UI/UX decisions
- **Release Engineer** — deployment and release management
- **Reviewer** — cross-role review and synthesis

Each role operates with **blinders**: it only handles the responsibilities of its role and ignores everything outside its scope.

### The 5-Layer Governance System

This is what distinguishes gstack from simple role prompting. The five layers enforce role integrity:

| Layer | Name | Description |
|-------|------|-------------|
| 1 | **Role Focus** | Blinders — agent only handles its defined responsibilities. QA lead focuses on user flow, bug report, testing checklist; ignores database schema. |
| 2 | **Data Flow** | Sequential handoffs — each agent's work is built on the prior agent's output. Reviewer output → QA lead input. |
| 3 | **Quality Control** | Completion checklist — tracks which roles have completed their review (CEO ✓, Engineer Manager ✓, etc.) before advancing. |
| 4 | **Boil the Lake** | Scope discipline — finish only what you can do perfectly. Small tasks completed 100%; large out-of-scope items deferred rather than attempted half-baked. |
| 5 | **Keep Simple** | Output format — summarize to: "what I found, why it matters, what to do next." Explain at a 16-year-old level. No jargon dumps. |

### Role Analogies for the Power Stack

From Eric Tech's "3 Frameworks" video, the three tools map to a corporate team:

- **gstack** = "exec team" — sets strategy, reviews architecture, coordinates specialist perspectives
- **GSD** = "project manager" — breaks down work, scopes milestones, manages execution cadence
- **Superpowers** = "senior engineer" — heads-down execution with disciplined craft

### Single-Lens vs Multi-Lens Distinction

Superpowers operates as **one disciplined tech lead** following the SDLC — a single lens applied consistently. gstack switches between **multiple specialist lenses**, including non-engineering perspectives (CEO strategic planning, QA browser testing, Designer UI review). This multi-lens switching is the key differentiator: gstack brings breadth of perspective, Superpowers brings depth of execution discipline.

## Why It Matters

Generic role prompting ("act as a QA engineer") is notoriously fragile — models tend to drift back toward generalist behavior. The 5-layer governance system is a structural attempt to make role adherence robust rather than relying on prompt phrasing alone. The sequential data flow (Layer 2) and completion checklists (Layer 3) add coordination overhead but provide verifiable handoff points.

For multi-agent systems more broadly, the "boil the lake" principle (Layer 4) is independently valuable: it encodes a preference for perfect completion of small tasks over partial completion of large ones, which reduces the "half-baked output" failure mode common in agentic workflows.

## Why People Are Using It

- Built by Garry Tan (Y Combinator CEO) — Tier 1 authority, high credibility signal
- GitHub: https://github.com/garrytan/gstack
- Covered in source-001 with detailed architectural breakdown
- Addresses a known failure mode: role-prompted agents drifting toward generalism
- Playwright integration for QA testing is concrete and production-relevant

## Potential Alternatives

| Alternative | Description | When to Prefer |
|-------------|-------------|----------------|
| Superpowers | Single disciplined engineer persona with TDD | When role diversity isn't needed; simpler projects |
| Custom CLAUDE.md role sections | Manual role definitions in system prompt | Lighter-weight; no framework dependency |
| CrewAI / LangGraph agent roles | Framework-level role orchestration | When building outside Claude Code; more complex agent graphs |

## Potential Improvements

- Define a standard role set for our specific agentic systems (e.g., Notion agent: Planner, Executor, Reviewer)
- Automate Layer 3 (Quality Control checklists) in the session handoff MD file
- Combine with GSD's context management: each role gets its own fresh session (role switch = context reset)
- Extend "Boil the Lake" principle to Perplexity skill design: each skill completes exactly its responsibility, nothing more

## Potential Failure Modes

- **Role boundary ambiguity**: In practice, the line between CEO and Engineer Manager is fuzzy; unclear ownership leads to gaps or duplication
- **Sequential bottleneck**: Data flow (Layer 2) means roles cannot run in parallel; overall pipeline is as slow as its slowest role
- **Checklist theater**: Layer 3 completion checklists can become checkbox-ticking rather than genuine quality gates
- **Framework rigidity**: Preset roles may not map cleanly onto non-standard project types
- **Governance overhead**: 5 layers add significant prompt complexity; may not be worth it for simple tasks
