---
notion_id: 32b1e08b-9b34-8190-9c9a-e15572a38670
name: Three-Layer Folder-as-Workspace Architecture
summary: 'A three-layer folder structure (Layer 1: global router CLAUDE.md; Layer 2: workspace-specific context files; Layer 3: actual work files) allows Claude Code to self-orient within any domain by
  reading progressively narrower context rather than loading everything at once or being pre-programmed as a domain-specific agent.'
implementation_notes: null
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- stop-building-ai-agents-use-this-folder-system-ins.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: skills-inside-workspace-contextual-skill.md
  rel: enabled-by
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
pipeline_status: synthesized
consumed_by:
- managing-agent-context.md
---
# Three-Layer Folder-as-Workspace Architecture

## What It Is
Layer 1 (Map): A root CLAUDE.md file that the agent always reads first. Contains the global folder structure, naming conventions, what's in each workspace, and routing rules. 'Think of it as the floor plan on the wall.' Layer 2 (Rooms): Each workspace subdirectory (e.g., writing_room/, production/, community/) contains its own context markdown file specifying what that workspace does, what files to load for specific tasks, what to skip, and which skills/MCP servers to invoke. Layer 3 (Workspace): The actual working files — drafts, scripts, outputs — organized by the naming conventions defined in Layer 1. The agent reads Layer 1 always, descends into the relevant Layer 2 file when working in a workspace, and reads only the Layer 3 files it needs for the current task.

## Why It Matters
Standard agent frameworks require pre-programming domain-specific behavior (writing agent, production agent, community agent, etc.). The three-layer system makes Claude Code itself the universal agent that adapts behavior by reading context files. This is more maintainable (edit a markdown file, not code), more composable (mix and match skills), and more legible (a human can read what the agent will do before it does it).

## Why People Are Using It
Eliminates the proliferation of separate agent scripts for each task domain. Works in the Claude Code native interface without any framework dependencies — just files and folders. Scales naturally: add a new workspace by adding a folder and a context file. Jake runs multiple parallel Claude Code instances, each operating in a different workspace folder simultaneously.

## Potential Alternatives
Pre-configured agent frameworks (CrewAI, LangGraph, AutoGen), single giant system prompt with all domain instructions, separate Claude projects per domain. All involve more setup overhead and less flexibility.

## Potential Improvements
Dynamic Layer 2 routing: if the task involves multiple workspaces, the router should automatically chain context files. AI-generated context files from a description of the workspace's purpose.

## Potential Failure Modes
CLAUDE.md proliferation: each folder having its own CLAUDE.md creates navigation overhead. Stale context files that no longer reflect actual folder contents. Agent reads wrong context file if the routing table in Layer 1 is ambiguous.
