---
name: Context Infrastructure Seven-Level Maturity Model
summary: A structured progression model for AI agent context infrastructure with seven levels — from manual chat context (L1) through Claude chat projects (L2), portable skills (L3), file access with CLAUDE.md
  (L4), co-work projects by area (L5), centralized second brain/personal OS (L6), to full business OS with team sync and permissions (L7). Each level resolves the primary limitation of the previous.
implementation_notes: The model maps directly onto MetaSystem's architecture — MetaSystem already operates at approximately L6/L7 (Obsidian vault, CLAUDE.md routing, system-scoped folders). The model provides
  a useful vocabulary for explaining the design to new contributors and for identifying the specific transition point being targeted in any upgrade.
category: Agentic Systems
evidence_strength: Medium (practitioner-documented)
adoption_status: Already Adopted
priority: P2 (Design Required)
applicability:
- General
- S3 (Claude Code Build)
adopted_in:
- General / Cross-System
sources:
- seven-levels-context-infrastructure-ai-agents.md
proposals: []
date_discovered: '2026-04-19'
last_updated: '2026-04-20'
related_findings:
- file: claudemd-as-knowledge-base-traversal-guide.md
  rel: extends
- file: obsidian-as-transparent-frontend-vs-rag-black-box.md
  rel: extends
- file: index-file-navigation-as-rag-replacement.md
  rel: extends
- file: skills-as-pointers-to-second-brain-files.md
  rel: extends
- file: scheduled-tasks-for-real-time-context-maintenance.md
  rel: extends
- file: obsidian-relay-plugin-for-team-context-sync.md
  rel: extends
pipeline_status: synthesized
consumed_by:
  - "building-agentic-systems.md"
  - artifact: reach-l6-before-l7
    type: extracted-artifact
    form: rule
    date: 2026-04-27
    session: 83
---
# Context Infrastructure Seven-Level Maturity Model

## What It Is
A maturity ladder for how individuals and teams leverage context with AI agents:

- **L1 — Manual chat context**: Copying/pasting context into each new chat. No persistence. High friction.
- **L2 — Claude chat projects**: Context files stored once per project. Isolated chat windows. Agent cannot self-update context files.
- **L3 — Portable skills**: SKILL.md + reference folder. Usable in any chat. Testable with built-in evals. Shareable via zip or org skills. Schedulable.
- **L4 — File access + CLAUDE.md**: Agent reads/writes local files. Context grows naturally. CLAUDE.md provides navigation routing. Enables strategic AI collaboration beyond pre-defined workflows.
- **L5 — Co-work projects by area**: Projects pre-bind to area-specific folders (YouTube, Sales, Operations). Project-level memory and rules per area. Chat history scoped per area.
- **L6 — Centralized second brain / personal OS**: All context in one Obsidian vault. Persistent, cross-provider, cross-area. Scheduled tasks add real-time context. Skills reference vault files instead of embedding copies.
- **L7 — Business OS**: Second brain synced across team via Relay plugin (or GitHub/Obsidian Sync). Permission settings control read/write access per folder. One context operator owns the layer.

The model distinguishes two architectural inflection points: L3 (from static to portable/testable) and L6 (from distributed to centralized). The business recommendation is to reach L6 personally before attempting L7.

## Why It Matters
The model provides a shared vocabulary for diagnosing where a team sits on the infrastructure curve and what the next targeted upgrade should be. Without this framing, teams often implement piecemeal improvements (better prompts, more projects) without addressing the underlying structural limitation. Context compounds — earlier investment yields disproportionately higher agent quality over time.

## Why People Are Using It
Beni (business AI practitioner, 60+ skills across business processes) presented this as a practitioner framework derived from running AI as a primary operating system for himself and his team. The model aligns with patterns independently observed by Karpathy (index file navigation), Anthropic (skills + evals), and other practitioners.

## Potential Failure Modes
Treating the model as prescriptive rather than descriptive — teams may skip levels that are appropriate for their scale. L7 without L6 foundation creates synchronization complexity before context quality is established. The model doesn't address context quality (what goes in), only context structure (how it's organized and accessed).

## Extraction Note — 2026-04-27

Extracted as **rule**: [[reach-l6-before-l7]] in `extracts/rules/`. Harvested from the G11 (building-agentic-systems) queue per IB-164 / DD-101 promotion path.
