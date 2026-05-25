---
name: SDK vs Framework Decision Framework for Agent Building
summary: 'Two-question decision framework for choosing between batteries-included SDKs (Claude Agent SDK, Codex SDK) and traditional frameworks (Pydantic AI, LangGraph): (1) Who uses it — just you or multiple
  people? (2) What''s your tolerance for speed and scale? SDKs are slower, more token-heavy, and non-deterministic but drastically simpler. Frameworks are faster, cheaper, and scalable but require more
  setup.'
implementation_notes: 'The subscription ToS restriction is critical: if multiple people use your agent, you MUST use API keys, not subscription — costs jump 10-50x.'
category: Tool Integration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
- S3 (Claude Code Build)
adopted_in: []
sources:
- sdk-vs-framework-decision-ai-agents.md
related_findings:
- file: claude-p-headless-mode-as-openclaw-replacement.md
  rel: same-problem
- file: coding-agent-sdk-as-non-coding-agent-foundation.md
  rel: extended-by
- file: skills-portability-across-sdk-and-framework-boundaries.md
  rel: extended-by
- file: sdk-to-framework-graduation-path.md
  rel: extended-by
- file: subscription-tos-single-user-boundary-for-agent-sdks.md
  rel: extended-by
- file: agent-infrastructure-glue-code-elimination-via-sdk.md
  rel: extended-by
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---

## What It Is
A practitioner-tested decision framework for the SDK vs. framework choice when building AI agents in 2026. Claude Agent SDK and Codex SDK provide batteries-included foundations: built-in tool registries, sub-agent support, conversation history management, skills, MCP servers, and hooks. Traditional frameworks (Pydantic AI, LangGraph, n8n) require more setup but offer sub-second response times, full control over conversation history, and much lower token usage. Three key SDK limitations: (1) Significantly slower due to reasoning overhead from built-in tooling. (2) More token-heavy and costly. (3) More non-deterministic — less control over exact agent behavior. The decision reduces to two questions: Who uses it? (Just you → SDK; multiple people → framework) What's your speed/scale tolerance? (Delay OK → SDK; needs to be fast → framework).

## Why It Matters
The ecosystem is bifurcating. Many practitioners are abandoning traditional frameworks for SDKs without understanding the tradeoffs. The subscription ToS restriction is the hidden killer: using your Anthropic subscription for a multi-user agent violates terms of service, forcing API key usage at 10-50x the cost.

## Why People Are Using It
Practitioners report building entire agent systems in single TypeScript files with the Claude Agent SDK — dramatically less code than equivalent Pydantic AI implementations. But they also report transitioning back to frameworks when scaling to production.

## Potential Alternatives
- Start with SDK for prototyping, migrate to framework for production
- Hybrid: use SDK for personal tools, framework for deployed agents
- Build custom lightweight agent loop (minimal overhead, maximum control)

## Potential Improvements
- SDK cost optimization as providers compete
- SDKs adding more control over determinism and token usage
- Framework-SDK bridges that let you use SDK features within a framework

## Potential Failure Modes
- Building on SDK then discovering ToS violation when deploying to team
- Over-engineering with frameworks when the SDK would suffice for personal use
- Assuming SDK and framework produce equivalent outputs (they don't — SDK is more verbose)
