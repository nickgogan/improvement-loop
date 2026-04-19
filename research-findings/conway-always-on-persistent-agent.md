---
name: 'Conway: Always-On Persistent Agent Environment'
summary: Leaked from Claude Code source, Conway is Anthropic's unannounced standalone agent sidebar with its own extension format (CNW.zip), automatic triggers (webhooks that wake the agent), browser control,
  and connectors to external services. It represents the 'always-on agent' layer — persistent, event-driven, and accumulating behavioral context over time.
implementation_notes: Conway is not yet launched. Monitor for release. The extension format and trigger system are the key architectural signals.
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- conway-anthropics-always-on-agent.md
related_findings:
- file: ide-first-claude-code-with-deterministic-hooks.md
  rel: same-problem
- file: kairos-autonomous-background-daemon.md
  rel: same-problem
- file: scheduled-task-dashboard-observability-layer.md
  rel: same-problem
- file: proprietary-extension-layer-on-open-protocol.md
  rel: enables
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-19'
pipeline_status: synthesized
consumed_by:
- agent-design-patterns.md
---
# Conway: Always-On Persistent Agent Environment

## What It Is
Conway is a standalone agent environment found in the Claude Code source code leak. It operates as a sidebar in the Claude interface with three core areas: search, chat, and system. The system section includes: (1) Extensions directory — installable add-ons (custom tools, interface panels, information handlers) packaged as CNW.zip files. (2) Connectors and tools — services plugged into the agent, including Chrome browser connection. (3) Automatic triggers — public web addresses that external services can ping to wake the agent, with toggleable permissions. Conway is designed to run continuously, monitoring email, Slack, calendar, and other sources. It learns behavioral patterns over time — which emails matter, which Slack threads need responses, how to prep for meetings. It is not yet publicly launched.

## Why It Matters
Conway represents the "persistence layer" that all three major labs (Anthropic, OpenAI, Google) are racing to own. The agent that accumulates 6 months of behavioral context creates switching costs that dwarf traditional data lock-in. This is the "Active Directory play" — the piece that makes the entire platform stack sticky.

## Why People Are Using It
Not yet available. The analysis comes from studying the leaked source code and extrapolating from Anthropic's Q1 2026 strategy: Claude Code (developers) → Co-work (enterprise non-technical) → Marketplace (distribution) → Conway (persistence). Each piece pushes toward platform lock-in.

## Potential Alternatives
- OpenAI's equivalent persistent agent (expected)
- Google Gemini's always-on assistant (expected)
- Self-built persistent agent using Open Brain or similar open-source approach
- Building your own behavioral context layer that is provider-portable

## Potential Improvements
- Open behavioral context export format
- Cross-provider behavioral context portability standard
- User-controlled learning boundaries (what the agent can and cannot observe)

## Potential Failure Modes
- Conway may be partially wrong ~30% of the time — the value comes from speed, not accuracy
- Behavioral pattern learning requires months of training before becoming useful
- Privacy concerns around always-on monitoring of email, Slack, and calendar
- No existing legal framework for "intelligence portability" if you want to switch providers
