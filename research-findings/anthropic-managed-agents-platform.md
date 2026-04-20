---
name: Anthropic Managed Agents Platform
summary: Anthropic's managed agents platform provides hosted agent environments with OAuth credential vaults, MCP tool integration, and session debugging. Claude Routines (claude.ai/code/routines) extends
  this with first-party scheduling (hourly/daily/custom), webhook triggers, API triggers, GitHub event triggers, and a calendar/grid dashboard showing all scheduled runs. Multiple triggers per routine are
  supported. Agents are created from natural language descriptions and tested interactively before deployment.
implementation_notes: "Claude Routines is Anthropic's literal 1:1 replacement for n8n/Make.com — same event→logic→output pattern, natural language instead of drag-and-drop nodes. Directly applicable for\
  \ MetaSystem improvement loop scheduled skills (watch-upstream, research-loop). Connectors (Gmail, Slack) are added via OAuth in Claude Code Settings > Connectors."
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- anthropic-managed-agents-platform.md
- anthropic-managed-agents-decoupling.md
- claude-routines-scheduled-automations-webhooks.md
related_findings:
- file: claude-code-ultra-plan-three-mode-planning.md
  rel: same-problem
- file: ultra-review-multi-agent-bug-hunting-fleet.md
  rel: enables
- file: claude-routines-webhook-triggered-pipeline-chaining.md
  rel: enables
- file: hands-off-routine-prompt-precision-pattern.md
  rel: companion
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-20'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---

## What It Is
Anthropic's managed agents platform (platform.claude.com / claude.ai/code/routines) lets developers create, test, and deploy agents that run on Anthropic's infrastructure. Key capabilities:

1. **Natural language agent creation** — describe what the agent should do; platform generates a spec
2. **OAuth credential vault** — stores API keys and manages authentication (Gmail, Slack, etc.) without exposing credentials to the agent
3. **Hosted environments with scoped permissions** — each agent gets an isolated environment with explicit network access controls
4. **Interactive testing with debug panels** — transcript view and raw API event logs for every tool call; "Run Now" button for live testing
5. **Session analytics** — token usage, cost tracking, rate-limited requests
6. **MCP tool integration**
7. **Claude Routines** — first-party scheduling layer at claude.ai/code/routines: schedule (hourly/daily/custom cron), webhook trigger, API trigger, GitHub event trigger. Multiple triggers per routine supported. Calendar and grid dashboard shows all scheduled runs with next-execution times.
8. **Model and environment selection** — choose model (e.g., Opus 4.6 1M) and Claude environment (with custom env vars / credentials) per routine

## Why It Matters
This moves agent deployment from "bring your own infrastructure" to "platform as a service." The credential vault and permission scoping make it viable for business automation. It's Anthropic's play for the automation market currently dominated by n8n, Make.com, and Zapier.

## Why People Are Using It
Practitioners building client automations report drastically reduced setup time — no manual API key management, no hosting configuration. The test-iterate-deploy loop is contained within a single interface.

## Potential Alternatives
- Self-hosted agents via Claude Agent SDK (more control, more setup)
- n8n/Make.com/Zapier for no-code automation (visual workflows, existing ecosystem)
- OpenAI Codex CLI for similar hosted execution

## Potential Improvements
- Visual workflow builder (predicted to come soon)
- Multi-model support within managed agents
- Team collaboration and shared agent libraries

## Potential Failure Modes
- Vendor lock-in — agents built on managed infrastructure are not portable
- Cost uncertainty at scale — hosted environments may become expensive
- Limited to Sonnet 4.6 (no model choice at time of recording)
