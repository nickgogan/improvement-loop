---
notion_id: 32b1e08b-9b34-817f-8586-d854f6db5e80
name: Context File Taxonomy (CLAUDE.md, SOUL.md, AGENTS.md, etc.)
summary: A growing taxonomy of markdown context files for agent systems — CLAUDE.md (project), SOUL.md (philosophy/values), AGENTS.md (tool-agnostic), PROGRESS.md (session bridge), MEMORY.md (semantic retrieval),
  RULES.md (hard constraints). ETH Zurich 2026 research found auto-generated files hurt performance versus manually curated ones.
implementation_notes: null
category: Context Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
proposer_priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in:
- S3 (Claude Code Build)
sources:
- openclaw-soul-md-explained.md
- eth-zurich-context-files-paper-march-2026.md
proposals: []
date_discovered: '2026-03-15'
last_updated: '2026-04-19'
related_findings:
- file: context-file-instruction-bloat-eth-zurich.md
  rel: same-problem
- file: pre-compression-identity-pinning.md
  rel: enables
- file: soul-md-agent-constitution-pattern.md
  rel: extended-by
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
- file: agent-memory-architecture-multi-agent-layered.md
  rel: same-problem
- file: tiered-context-injection-over-monolithic-files.md
  rel: enables
pipeline_status: raw
consumed_by: []
---
# Context File Taxonomy (CLAUDE.md, SOUL.md, AGENTS.md, etc.)

## What It Is
A structured taxonomy of markdown files used to inject persistent context into Claude and other coding agents. Each file serves a distinct role: CLAUDE.md holds project-level instructions, SOUL.md encodes values and philosophy, AGENTS.md provides tool-agnostic conventions, PROGRESS.md bridges sessions, MEMORY.md supports semantic retrieval, and RULES.md enforces hard constraints. The files are loaded by the agent at session start.

## Why It Matters
Without structured context files, agents lose continuity between sessions and must re-derive project conventions from scratch. This taxonomy makes agent behavior consistent and persistent across runs. ETH Zurich 2026 research confirmed that manually written, concise files outperform auto-generated ones — quality over quantity.

## Why People Are Using It
The OpenClaw ecosystem and Claude Code community have converged on this taxonomy as a practical solution to agent amnesia. Practitioners building multi-session agent workflows depend on these files to preserve decisions, constraints, and philosophy without re-prompting. The pattern has become a de facto standard in advanced Claude Code setups. OpenClaw's full SOUL.md specification defines a layered prompt stack (SOUL → tools → memory → skills → overlays) with a template structure capped at ~20K chars. Companion files include USER.md, MEMORY.md, HEARTBEAT.md, AGENTS.md, and TOOLS.md — each serving a distinct role in the agent context architecture.

## Potential Improvements
Files can be added incrementally as friction is discovered rather than pre-designing the full taxonomy upfront. A minimal starting set (CLAUDE.md + SOUL.md + PROGRESS.md) reduces Day 1 overhead while leaving room to grow. Future tooling could help validate file quality and detect redundancy across files.

## Potential Failure Modes
Proliferating too many context files wastes tokens — Claude loads all of them even when most are irrelevant to the current task. The 27-file architectures seen in consultant setups are designed for managing multiple clients; a single household context is far simpler. Auto-generated files in particular tend to be verbose and low-signal.
