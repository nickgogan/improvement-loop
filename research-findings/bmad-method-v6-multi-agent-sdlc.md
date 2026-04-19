---
name: 'BMAD Method v6: Multi-Agent SDLC Framework'
summary: Breakthrough Method for Agile AI-Driven Development — 26 specialized agents, 68 workflows, 4-phase SDLC (Analysis→Planning→Solutioning→Implementation). Docs-as-code with context sharding (90% token
  savings). Scale-adaptive flows (Quick for bugs, Enterprise for platforms). Step-file system for agent pause/resume.
implementation_notes: BMAD's agent team model parallels MetaSystem's DD-60 (composable agent teams). Context sharding via atomic story files maps to MetaSystem's fractal pattern. The docs-as-code approach
  aligns with DD-63 (artifact-chain communication).
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- bmad-v6-is-finally-here.md
- bmad-method-masterclass.md
proposals: null
date_discovered: '2026-04-07'
last_updated: '2026-04-09'
related_findings:
- file: yaml-template-dual-structure.md
  rel: enables
- file: scrum-master-story-contextualization.md
  rel: enables
- file: business-analyst-upstream-quality-gate.md
  rel: enables
- file: qa-agent-independent-compliance-review.md
  rel: enables
- file: yaml-templates-with-embedded-elicitation-instructions.md
  rel: enables
- file: document-sharding-for-context-efficiency.md
  rel: enables
- file: new-chat-per-agent-step-context-hygiene.md
  rel: enables
- file: correct-course-mid-project-pivot-command.md
  rel: enables
- file: archon-yaml-defined-harness-workflows.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
---
# BMAD Method v6: Multi-Agent SDLC Framework

## What It Is
A full SDLC framework where specialized AI agents handle each project phase. 12+ agent roles (Analyst, PM, Architect, Scrum Master, Developer, QA). Four phases: Analysis & Discovery, Planning (PRD), Solutioning (Architecture, Epics/Stories), Implementation (Sprint Planning, Story Dev, Code Review). Docs-as-code: PRDs, architecture docs, and story files ARE the source of truth, not code. Context sharding breaks docs into atomic files, saving 90% tokens. Quick Flow skips full planning for bugs/refactors. Step-file system enables agent pause/resume across sessions.

V6 scope expansion: renamed from "Breakthrough Method for Agile AI-Driven Development" to "Build More Architect Dreams" — now covers therapy, entertainment, creative writing, legal, medical, and business planning beyond software development. Party mode: BMAD Core feature for real-time multi-agent collaboration. Module marketplace with quality + security vetting (announced, launching in 2-3 weeks as of source date). BMAD Help: context-aware adaptive routing that inspects installed modules, checks project state, and adapts recommendations — can recommend skipping phases based on context (e.g., skip brainstorming if the idea is already solid). Agent-first vs skill-first dual invocation: load an agent persona and chat interactively OR jump directly to a skill/workflow command. AI-as-facilitator philosophy: "AI is not Google... the AI is a facilitator."

The masterclass reveals the core agent roster in detail: Business Analyst (Mary, 20 brainstorming techniques + project brief generation), Product Manager (PRD with functional/non-functional reqs, epics, stories), Product Owner (optional checklist for story-architecture alignment), Architect (sequence diagrams via Mermaid, tech stack table, data models, coding standards, source tree), Scrum Master (detailed developer stories from epics), Developer (James, step-by-step story implementation with sharded context), QA (Quinn, compliance and bug review). The "secret sauce" is the BA agent — Brian claims Mary is "the most special agent in the whole BMAD method." Individual patterns documented as standalone findings: document-sharding-for-context-efficiency.md, advanced-elicitation-techniques-library.md, new-chat-per-agent-step-context-hygiene.md, business-analyst-upstream-quality-gate.md.

## Why It Matters
Solves the "vibe coding" problem at scale — agents follow structured SDLC instead of improvising. 43.7K GitHub stars indicate significant adoption. The context sharding approach directly addresses the token budget problem for large projects.

## Why People Are Using It
One-command install (npx bmad-method install). Modular ecosystem with marketplace for custom agents and workflows. Active development with Playwright integration for E2E testing. Scale-adaptive — Quick Flow for small changes, Enterprise Flow for platforms.

## Potential Alternatives
GSD (lighter weight, Claude Code-specific). Superpowers (skill-based, less prescriptive SDLC). Manual spec-first workflows with CLAUDE.md governance.

## Potential Improvements
Integration with existing governance systems like MetaSystem's DD/IB tracking. Custom module creation via bmad-builder. Tighter integration with IDE-based Claude Code workflows.

## Potential Failure Modes
26 agents may be overkill for small projects or solo developers. Context switching between fresh chats loses cross-phase insights. Enterprise Flow overhead for simple features. Docs-as-code requires discipline to keep documentation synchronized with implementation.
