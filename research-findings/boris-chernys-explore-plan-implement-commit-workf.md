---
notion_id: 32b1e08b-9b34-813e-9f55-e3fdd152e994
name: Boris Cherny's Explore-Plan-Implement-Commit Workflow
summary: 'Claude Code creator''s workflow: Explore -> Plan -> Implement -> Commit with verification-driven development. Claims 2-3x multiplier. CLAUDE.md kept under 2.5K tokens. 5 parallel agents. 0% hand-written
  code since Nov 2025.'
implementation_notes: null
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Already Adopted
priority: Not Flagged
applicability:
- S3 (Claude Code Build)
adopted_in:
- S3 (Claude Code Build)
sources:
- anthropic-didnt-build-a-new-browser-they-did-somet.md
- anthropic-claude-code-best-practices.md
proposals: null
date_discovered: '2026-03-15'
last_updated: '2026-04-19'
related_findings:
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: enabled-by
pipeline_status: raw
consumed_by: []
---
# Boris Cherny's Explore-Plan-Implement-Commit Workflow

## What It Is
A four-phase workflow developed by Boris Cherny, creator of Claude Code: Explore (read the codebase, gather context), Plan (write a concrete plan before touching files), Implement (execute against the plan with verification at each step), Commit (verify and commit completed work). Key constraints: CLAUDE.md kept under 2.5K tokens using just-in-time reference loading for depth, up to 5 parallel agents running simultaneously, and verification-driven development at each phase gate.

## Why It Matters
The workflow imposes structure that prevents the most costly failure mode in AI-assisted coding: premature implementation without adequate planning. The Plan phase gate alone catches the majority of expensive rework. Cherny reports 0% hand-written code since November 2025 and claims a 2-3x productivity multiplier over unstructured prompting.

## Why People Are Using It
The pattern carries direct authority — it comes from the Claude Code creator's own practice. It has been encoded into the vault's CLAUDE.md and boris-playbook.md reference file, making it the primary workflow standard for S3. Independent practitioners have converged on similar phase-gated patterns, confirming its general validity.

## Potential Improvements
The workflow could be parameterized for different project types — household automation tasks, coding projects, and research tasks each have different optimal phase durations and verification criteria. A lightweight checklist embedded in CLAUDE.md could make the phase transitions explicit and auditable.

## Potential Failure Modes
Skipping the Plan phase under time pressure leads to expensive rework — the most common failure mode. Overly long Explore phases can consume context budget before implementation begins. With 5 parallel agents, coordination overhead and merge conflicts can erode the productivity multiplier if work decomposition is coarse.
