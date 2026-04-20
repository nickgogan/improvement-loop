---
name: "OpenClaw Wrapper Ecosystem Survey (2026)"
summary: "Survey of OpenClaw-derivative products (Manus/Meta, Perplexity Personal Computer, NemoClaw/NVIDIA, Claude Dispatch, hosted wrappers) all competing on installation friction and security but uniformly failing to address the context gap — the human's inability to articulate their tacit expertise to feed the agent."
implementation_notes: null
category: "Orchestration"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P3 (Monitor)"
applicability:
  - "General"
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "agent-cold-start-tacit-knowledge-elicitation.md"
related_findings:
  - file: agent-management-tool-landscape-2026.md
    rel: same-problem
  - file: tacit-knowledge-as-agent-delegation-barrier.md
    rel: same-problem
  - file: claude-p-headless-mode-as-openclaw-replacement.md
    rel: same-problem
  - file: five-pillar-agentic-os-framework.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: classified
consumed_by: []
---
# OpenClaw Wrapper Ecosystem Survey (2026)

## What It Is
OpenClaw (~250K GitHub stars, most-copied product of 2026) has spawned a constellation of derivative products. As of early 2026, the major entrants are:

**OpenClaw (original):** Runs locally on any hardware, connects to any LLM, supports Telegram/WhatsApp/iMessage/Slack/phone-call. Free, infinitely configurable. Cold start entirely user-managed — appropriate for developers who can write markdown.

**Manus (acquired by Meta):** Desktop app or cloud VM. Automatically decomposes queries into sub-agents. Easier to install (~10-15 min), more secure. Key limitation: no deep personal context configuration, so agents stay generic.

**Perplexity Personal Computer:** Most ambitious play. Dedicated Mac Mini (physical hardware Perplexity bulk-purchased from Apple) connected to Perplexity cloud. Project manager AI routes tasks across 20 frontier models. CEO Aravindan Srinivas framing: "A traditional OS takes instructions; an AI OS takes objectives." Limitation: once objectives require personal life/judgment context never written down, the system fails identically to all others.

**NemoClaw (NVIDIA):** Enterprise security wrapper for OpenClaw, launched at GTC by Jensen Huang. Runs agents in sandboxes using OpenShell for privacy guardrails and Neotron for model output. Solves the security problem thoroughly. Explicitly punts the context-provisioning problem to the enterprise — which also doesn't know how to solve it.

**Claude Dispatch (Anthropic):** Pairs phone with Mac for mobile agent control via any messaging app. Addresses mobile-first use cases. Limitation: 15-paragraph text introductions to agents still fail because context transfer requires more than conversational text — it requires structured knowledge.

**Hosted wrappers (startclaw, myclaw, simpleclaw, uniclaw, etc.):** Dozens launching weekly. One-click deploy, preconfigured personas, managed infrastructure. Some sell $49 pre-written markdown file packs (soul.md + heartbeat.md + user.md) — a business model that exists because context-provisioning is the real bottleneck.

All players compete on: installation ease, UI, model selection, security, pricing, cloud vs. local. None address the core problem: getting the human to articulate their tacit operational expertise in a form the agent can use.

## Why It Matters
The competitive landscape clarifies what the actual moat is in the agent era: not infrastructure, not models, not UX — it's the quality of context the human can provide. Every product in this survey faces the same wall once past installation. Understanding this helps avoid over-investing in framework selection or platform switching as a solution to agent underperformance.

## Why People Are Using It
Useful for orientation when evaluating which OpenClaw variant to adopt. The key takeaway: the choice of platform is low-leverage. The choice of how much contextual knowledge to invest in upfront is high-leverage regardless of platform.

## Potential Improvements
This landscape will evolve rapidly. The first product that systematically addresses context elicitation (rather than just installation) will differentiate significantly. Watch for: structured onboarding flows with interview-style context extraction, personal knowledge stores as standard infrastructure, expertise-elicitation agents as a first-run experience.

## Potential Failure Modes
The survey becomes stale quickly (monthly churn in the ecosystem). The categories may blur as products add features. The framing ("all fail at context gap") may overstate the case — Manus and Perplexity Personal Computer users who invest in context provisioning do report strong results; the issue is that the products don't require or guide that investment.
