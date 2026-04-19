---
notion_id: 32b1e08b-9b34-8121-a381-ed1ea3a97801
name: Sender Allowlist for Messaging-Interface Security
summary: Claude Code's channel plugins implement a sender allowlist that silently drops all messages from unauthorized IDs, preventing prompt injection via public Telegram bots while preserving the full
  Claude Code security model.
implementation_notes: null
category: Sandboxing
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- claude-codes-leak-changes-everything.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
related_findings:
- file: claude-code-channels-telegramdiscord-as-agent-inte.md
  rel: enabled-by
---
# Sender Allowlist for Messaging-Interface Security

## What It Is
When a Claude Code channel plugin is configured, it creates a `sender_allow_list` (or equivalent policy) containing the specific Telegram user ID or Discord user ID of the authorized operator. All other incoming messages are silently dropped before the agent ever sees them. This means even if the Telegram bot link is shared accidentally, random users cannot inject instructions into the running agent. The allowlist is configured automatically during `/telegram:configure` based on the initial token setup.

## Why It Matters
Messaging interfaces are a natural attack surface for prompt injection — malicious users could send crafted messages attempting to override system instructions or extract data. The allowlist reduces the attack surface to a fixed set of known identities, which is a meaningful security improvement over open HTTP webhooks or public bot endpoints.

## Why People Are Using It
Anthropic's native implementation specifically calls out security as a first-class concern on the Channels docs page. Third-party tools like OpenClaw had documented security vulnerabilities (no sender restriction by default). The allowlist gives practitioners a path to mobile agent access without opening significant new attack vectors.

## Potential Alternatives
API key authentication on HTTP webhooks, VPN-restricted endpoints, Cloudflare Access in front of agent APIs, encrypted message signing.

## Potential Improvements
Role-based allowlists (some users can read status, others can trigger tasks). Integration with hardware security keys for high-privilege task authorization.

## Potential Failure Modes
Allowlist misconfiguration (adding wrong IDs). If the Telegram bot token is compromised, the allowlist can be bypassed by an attacker who can impersonate allowed IDs. No end-to-end encryption on message content by default.
