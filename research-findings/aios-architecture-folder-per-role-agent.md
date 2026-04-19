---
notion_id: 32b1e08b-9b34-81a4-8bf9-ce4ddb90e4f7
name: 'AIOS Architecture: Folder-Per-Role Agent Organization'
summary: Structuring agent deployments as a folder hierarchy (top-level company/client folder, sub-folders for each role/department, each with its own CLAUDE.md, skills, memory.md, and scoped MCPs) creates
  an 'AI Operating System' that scales from a personal assistant to a full AI-run company.
implementation_notes: null
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- building-ai-agents-that-actually-work-full-course.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-08'
related_findings:
- file: specialization-theater-anti-pattern.md
  rel: contradicts
- file: global-vs-project-level-skill-and-context.md
  rel: same-problem
pipeline_status: "raw"
consumed_by: []
---
# AIOS Architecture: Folder-Per-Role Agent Organization

## What It Is
The AIOS architecture organizes agent contexts as a file system: a workspace folder per company/client, sub-folders for each department role (executive assistant, head of marketing, content team, head of sales), each with its own context files, skills, memory, and MCP scoping. A top-level orchestrator context file references all sub-agents. Each role has role-specific CLAUDE.md instructions ('You are my head of marketing. You speak like this. These are your tasks.'). Switching between roles means switching the active folder in the IDE.

## Why It Matters
The folder-based architecture is portable (works in Claude Code, Co-work, Codeex, OpenClaw, Manis — all harnesses), version-controllable (git), inspectable (plain markdown files), and future-proof (not locked to any single harness's proprietary memory format). The author frames this as the 'real future-proof AI stack.'

## Why People Are Using It
Founders, agency operators, and consultants managing multiple client engagements and business functions are the primary adopters. The architecture scales from a single executive assistant to full multi-department agent teams without requiring new tooling.

## Potential Alternatives
Harness-specific organization (Claude Projects, OpenClaw's agent hub, Manis workspaces); centralized system prompts without folder isolation; Notion-based agent OS (as described in video 19).

## Potential Improvements
Automated initialization scripts that scaffold the full AIOS folder structure for a new role, given a role description and a list of connected tools, would accelerate setup for non-technical users.

## Potential Failure Modes
As the folder structure grows to dozens of roles and hundreds of skills, navigation and maintenance become non-trivial. Without version control discipline, skills and context files diverge and become inconsistent. The architecture requires the local machine to always be accessible, which is a constraint for mobile-first or distributed teams.
