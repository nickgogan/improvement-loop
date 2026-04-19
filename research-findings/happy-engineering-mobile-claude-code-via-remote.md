---
notion_id: 32b1e08b-9b34-81a5-a10a-c053955be632
name: 'Happy Engineering: Mobile Claude Code via Remote Terminal'
summary: Happy Engineering (happy.engineering) is a free, open-source tool that creates a remote terminal connection to your local machine from mobile, giving full Claude Code access (including all plugins)
  from iOS/Android — unlike the limited official Claude mobile app.
implementation_notes: null
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- how-to-make-claude-code-less-dumb.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: claude-code-channels-telegramdiscord-as-agent-inte.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Happy Engineering: Mobile Claude Code via Remote Terminal

## What It Is
Happy Engineering creates a persistent remote shell connection to your local machine accessible from a mobile app (iOS, Android) or web browser. Once installed (via a single terminal command), mobile sessions run as actual terminal sessions on your local computer — not in a sandboxed mobile environment. This means all Claude Code plugins (Superpowers, Context7, Sequential Thinking), local files, and API credentials are available identically to the desktop experience. Sessions persist — you can start a task on mobile and resume on desktop seamlessly.

## Why It Matters
The official Claude mobile app has ~10% of desktop functionality: no local file access, most websites blocked from scraping, no plugin support. Happy Engineering enables full-capability mobile access, which Michia says has become a game changer for shipping code from anywhere.

## Why People Are Using It
Free and open source. Michia calls it a daily-use tool that enables him to 'ship new features on a date with his wife' — the social signal is that true mobile parity with desktop Claude Code is now achievable.

## Potential Alternatives
Official Claude mobile app (limited), SSH into a remote server running Claude Code, VS Code Remote Tunnels, Tailscale SSH.

## Potential Improvements
Requires the local machine to be on and connected. A cloud-hosted version of the full toolchain would remove this dependency.

## Potential Failure Modes
Local machine must be powered on and have a stable internet connection. Security implications of exposing a remote shell to a mobile device — requires careful network security configuration.
