---
notion_id: 32b1e08b-9b34-81e6-b884-f3d79cde584a
name: 'Claude Code Channels: Telegram/Discord as Agent Interface'
summary: Claude Code's official Channels feature turns Telegram and Discord into persistent interfaces for a locally-running Claude Code session, allowing task dispatch and file delivery from mobile while
  maintaining the full skill library and security model of the local installation.
implementation_notes: null
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- claude-codes-leak-changes-everything.md
- interactive-html-artifacts-claude-code-bun.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-20'
related_findings:
- file: happy-engineering-mobile-claude-code-via-remote.md
  rel: same-problem
- file: sender-allowlist-for-messaging-interface-security.md
  rel: enables
- file: bun-hot-reload-interactive-html-artifact-feedback-loop.md
  rel: enables
pipeline_status: "extracted"
consumed_by:
  - "skills/claude-code-channels-messaging-apps-as-agent-interface.md"
---
# Claude Code Channels: Telegram/Discord as Agent Interface

## What It Is
Claude Code Channels is an officially supported plugin system that creates a bidirectional channel between messaging apps and a running Claude Code session. Incoming messages trigger the agent to execute tasks; outgoing messages include task results and delivered files. Setup: create a Telegram bot via BotFather, copy the token, run `/telegram:configure <token>` in Claude Code, then launch with `claude --channels plugin:telegram@claude-plugins-official`.

## Why It Matters
Removes the requirement to be at a desktop to dispatch long-running agent tasks. Enables asynchronous task patterns: trigger a lead scrape or thumbnail generation from a phone, receive the CSV or image result minutes later.

## Why People Are Using It
Humans already use Telegram/Discord to communicate with people; extending that to agents lowers the cognitive context-switch cost of delegating work. Multiple creators built third-party versions of this -- indicating strong unmet demand that Anthropic has now addressed officially.

## Custom Channel Plugin: HTML Artifact as Live Frontend
Beyond Telegram/Discord, the Channels feature supports building custom channel plugins. A practitioner used this to wire a local HTML artifact directly to Claude Code: the artifact runs on a local port (launched with `claude --dangerously-load-development-channels server:<name>`), users pin comments in the UI, and each pinned comment is automatically sent back to Claude Code as a new message — no clipboard export step required. Claude Code then queries MCP servers (e.g., PostHog, Stripe), updates the artifact file, and the browser hot-reloads. This creates a pattern where the artifact serves dual roles: operational dashboard (reading and exploring data) and conversational surface (editing the dashboard itself). The artifact becomes a custom frontend with Claude Code as the backend.

## Potential Alternatives
OpenClaw/Claudebot (third-party Telegram wrappers, now largely superseded), Claude Dispatch for co-work, web-based agent dashboards, scheduled cron-triggered agents.

## Potential Improvements
Currently requires local machine to stay awake. Integration with additional messaging platforms (WhatsApp, Slack) would expand reach.

## Potential Failure Modes
Machine sleep/lock stops the agent. Git conflicts if two machines both commit. Security risk if sender allowlist is not properly configured.

## Extraction Note — 2026-05-25
Extracted as **skill**: [[claude-code-channels-messaging-apps-as-agent-interface]] in `extracts/skills/`
