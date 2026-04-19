---
notion_id: 32b1e08b-9b34-813d-9c5e-dcd189db688d
name: 'Claude Dispatch: Native Mobile-to-Local Agent Orchestration'
summary: Claude Dispatch lets users send commands from the Claude mobile app to a Co-work instance running on their local desktop, enabling remote trigger of skills, multi-task parallelism, and asynchronous
  result delivery — all without exposing credentials to third-party services.
implementation_notes: null
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- claude-codes-leak-changes-everything.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: skills-cli-tools-as-mobile-triggerable-modules.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Claude Dispatch: Native Mobile-to-Local Agent Orchestration

## What It Is
Claude Dispatch creates a communication bridge between the Claude iOS/Android app and Claude Co-work on a desktop machine. The user sends a message from their phone (e.g., 'run the lead scraper skill, 200 agency owners in California') and Dispatch relays it to the local Co-work instance, which executes the task using locally-configured skills and MCP connectors. Results are reported back to the phone. Multiple concurrent tasks can be launched from the phone, each spawning a separate Co-work tab labeled 'dispatch: [task name]'. The phone acts as a walkie-talkie; the local machine does the compute.

## Why It Matters
Previously, mobile agent control required third-party tools like OpenClaw (Telegram/WhatsApp bots), which exposed API keys and credentials to potentially insecure services. Dispatch provides the same UX (text your agent from your phone) with Anthropic-managed sandboxing, explicit allow-listing of resource access, and flat-fee subscription pricing instead of per-API-call billing.

## Why People Are Using It
The author reports running lead scrapers, inbox cleaners, and thumbnail generation workflows entirely from his phone while away from his desk. The ability to run multiple skills in parallel from a mobile interface and receive asynchronous results is the primary draw. Security-conscious practitioners and business users prefer Dispatch over OpenClaw for production deployments.

## Potential Alternatives
OpenClaw / OpenAI-sponsored replacement (Peter Steinberger project); Telegram-based local agent runners; scheduled cron jobs; running Co-work on an always-on machine (Mac Mini) without mobile control.

## Potential Improvements
The author anticipates Telegram integration. Future versions will likely add push notification support for skill completion events. Persistent multi-day workflows would benefit from deeper mobile UX for monitoring state.

## Potential Failure Modes
Requires the local computer to remain awake and connected — any sleep/network interruption breaks the dispatch loop. Skill execution failure on the local machine is not always gracefully surfaced on the mobile side. Currently limited to Co-work, not Claude Code.
