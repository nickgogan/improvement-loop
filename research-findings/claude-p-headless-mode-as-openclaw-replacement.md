---
notion_id: 32b1e08b-9b34-8145-b814-c2be43f3d697
name: claude -p (Headless Mode) as OpenClaw Replacement
summary: '`claude -p` runs Claude Code non-interactively in a bash script, giving full programmatic control over all four agent zones, using Claude Max plan tokens — making it cheaper and more transparent
  than OpenClaw while matching its capabilities.'
implementation_notes: null
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- claude-codes-leak-changes-everything.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-09'
related_findings:
- file: sdk-vs-framework-decision-for-agent-building.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# claude -p (Headless Mode) as OpenClaw Replacement

## What It Is
`claude -p` is Claude Code's headless/non-interactive mode, invokable from any bash script with a prompt as an argument. Key flags: `--append-system-prompt` adds to Claude's default system prompt without replacing it; `--system-prompt` replaces it entirely (can be combined with `--tools '[]'` to strip all tools for a near-raw API call while still on the Max plan); `--resume` enables session persistence so the agent remembers context across invocations; `--tools` controls which tools are available. This allows developers to build agents with full control over trigger, context, tools, and output — all in bash — without any proprietary agent platform. The email agent demo in the video shows a Telegram-triggered, cron-augmented agent that fetches and summarizes emails, built entirely with `claude -p` in a bash script with a system prompt, IMAP fetch script, and session persistence.

## Why It Matters
OpenClaw automates browser actions costing $1-3 per run and takes minutes; the equivalent `claude -p` agent runs in seconds and costs a fraction using Max plan. More importantly, every line of the agent is readable and modifiable by the developer — there are no abstraction layers and no black-box behaviors.

## Why People Are Using It
Max plan users get dramatically subsidized API usage inside Claude Code. Building agents in bash means no framework lock-in, no dependency management, and full auditability.

## Potential Alternatives
OpenClaw (more autonomous but black-box and expensive). Direct Anthropic API calls (more flexible but loses Max plan subsidy). LangChain/CrewAI (more tooling but adds abstraction).

## Potential Improvements
A library of reusable `claude -p` agent templates (email, calendar, news, code review) would accelerate adoption. Integration with systemd or PM2 for daemonized agent deployment.

## Potential Failure Modes
`--resume` session persistence can accumulate context rot over time — a `reset` command should be built into any persistent agent. Stripping system prompts entirely (`--system-prompt` with empty string) removes Claude's safety behaviors — use with caution. Agents relying on Max plan cannot scale beyond one user's account.
