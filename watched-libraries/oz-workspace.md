---
name: "Oz Workspace"
url: "https://github.com/warpdotdev/oz-workspace"
stars: "~500"
spectrum_position: "cherry-pick"
spectrum_rationale: "Reference implementation of Warp's Oz multi-agent API. Shows rooms + agents + kanban + artifacts + notifications pattern. Relevant for multi-agent coordination but not primary architecture source."
current_version: "latest (commit d9390e8)"
last_checked: "2026-05-24"
tracking_focus:
  - "Multi-agent room model: agents assigned to rooms, @mention communication"
  - "Artifact production: agents create PRs, plans, documents"
  - "Real-time coordination: SSE-based updates, agent-to-agent communication"
  - "Task management: per-room kanban (backlog → in progress → done)"
tags:
  - "multi-agent"
  - "collaborative-workspace"
  - "sse"
  - "next-js"
date_added: "2026-05-24"
---

# Oz Workspace

Open-source collaborative AI agent workspace built on Warp's Oz API. Next.js 16 + Prisma 7 + SQLite/Turso + SSE. Reference implementation for the Oz multi-agent platform.

## Why We Watch

Shows a production multi-agent coordination pattern: rooms as bounded contexts, agents with system prompts + skills + MCP servers, real-time SSE communication, agent-produced artifacts (PRs, plans, docs), per-room kanban for task tracking, and inbox notifications. The "rooms" concept maps to our bounded-context agent model.

## Key Concepts

- **Rooms**: Chat channels where humans and agents collaborate on a topic
- **Agents**: Configurable with system prompt, skills, MCP servers, associated repo
- **Tasks**: Per-room kanban board (backlog → in progress → done) that agents self-manage
- **Artifacts**: Documents, PRs, and plans generated during agent work
- **Notifications**: Inbox alerts from agents (e.g., "PR ready for review")

## Spectrum Notes

Cherry-pick — the multi-agent coordination pattern (rooms, @mentions, shared kanban) is interesting but the implementation is early-stage (single commit). Watch for maturation.
