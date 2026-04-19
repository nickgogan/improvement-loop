---
notion_id: 32b1e08b-9b34-819b-8f14-f6e31be28f4e
name: 'GWS CLI: Full Google Workspace Control from Claude Code'
summary: GWS CLI is an open-source terminal tool that gives Claude Code access to Gmail, Docs, Sheets, and Drive — enabling agents to read/send email, create/edit documents, and manipulate spreadsheets
  with built-in Google Workspace Armor for prompt injection protection.
implementation_notes: null
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- 10-cli-tools-that-make-claude-code-unstoppable.md
- googleworkspace-cli-one-cli-for-all-of-google-work.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-08'
related_findings:
- file: dynamic-discovery-architecture-self-updating-cli-f.md
  rel: enabled-by
pipeline_status: "raw"
consumed_by: []
---
# GWS CLI: Full Google Workspace Control from Claude Code

## What It Is
GWS CLI (gws) is an open-source Rust-based terminal tool that provides unified access to all of Google Workspace — Drive, Gmail, Calendar, Sheets, Docs, Chat, Admin, Script, Workflow, Events, and ModelArmor. Its defining architectural feature is dynamic command generation: it reads Google's Discovery Service at runtime and builds its entire command surface automatically, so when Google adds a new API endpoint, gws picks it up without a release. Ships 100+ agent skills (SKILL.md files) including 50 curated recipes, installable via `npx skills add`. Helper commands (prefixed with +) provide high-level shortcuts: +send, +reply, +triage, +agenda, +standup-report, +meeting-prep, +email-to-task, +weekly-digest, and more.

## Why It Matters
Google Workspace is the primary productivity suite for many organizations. A single CLI with structured JSON output and 100+ agent skills means coding agents can manage email, documents, spreadsheets, calendar, and Drive without custom API integrations. The Discovery Service architecture ensures the tool never goes stale — a major advantage over static API wrappers. Security is first-class: credentials encrypted at rest (AES-256-GCM), Model Armor integration for prompt injection scanning (warn or block modes), and multiple auth workflows (OAuth2, service accounts, pre-obtained tokens, headless/CI).

## Why People Are Using It
One install replaces separate integrations for Gmail, Drive, Sheets, Calendar, and Docs. Structured JSON output is immediately parseable by AI agents. Helper commands like +standup-report (today's meetings + open tasks) and +meeting-prep (agenda, attendees, linked docs) provide immediate workflow value. The gws-shared skill includes an install block so OpenClaw auto-installs the CLI. Gemini CLI extension support extends reach beyond Claude Code.

## Potential Alternatives
Google Workspace MCP servers. Zapier/Make/n8n for no-code automation. Direct Google API integration via Python. Gmail/Drive MCPs. Individual service-specific CLI tools. Perplexity's own Google connectors for basic operations.

## Potential Improvements
Structured permission scopes mapped to specific workflow needs (read-only email scope). AI-assisted skill selection from the 100+ skill library. Verified OAuth app status to remove the 25-scope limit for testing mode. Stable v1.0 release (currently under active development with breaking changes expected).

## Potential Failure Modes
Active development means breaking changes before v1.0. Prompt injection via malicious email content reaching the agent. Over-broad OAuth permissions allowing unintended email sends or document modifications. Google Workspace admin restrictions may block CLI OAuth flows in corporate environments. Discovery Service dependency means an outage at Google's end breaks command building. Not an officially supported Google product — could be deprecated.
