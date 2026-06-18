---
name: "SDK-to-Framework Graduation Path"
summary: "A practitioner-validated migration pattern: prototype agents on batteries-included SDKs (Claude Agent SDK, Codex SDK) to test tooling, skills, and MCP integrations quickly, then graduate to a framework (Pydantic AI, LangGraph) when the agent needs to scale to multiple users, achieve sub-second response times, or reduce token costs. Skills and MCP servers carry over; the agent loop and state management must be rebuilt."
implementation_notes: null
category: "Agentic Systems"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "sdk-vs-framework-decision-ai-agents.md"
related_findings:
  - file: sdk-vs-framework-decision-for-agent-building.md
    rel: extends
  - file: start-simple-migrate-when-forced-pragmatic-architecture.md
    rel: same-problem
  - file: skills-portability-across-sdk-and-framework-boundaries.md
    rel: enables
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "templates/sdk-to-framework-graduation-decision-checklist.md"
  - building-agentic-systems.md
tags:
  - "session-95-reextract"
---

## What It Is

A two-phase agent development lifecycle observed in practitioner workflows:

**Phase 1 -- SDK Prototyping:** Build the agent on the Claude Agent SDK or Codex SDK. Test the tooling (skills, MCP servers, sub-agents). Validate the agent's capabilities and workflow. Iterate rapidly with minimal infrastructure code. Use your subscription for near-zero marginal cost.

**Phase 2 -- Framework Graduation:** When the agent needs to serve multiple users, meet latency requirements (sub-second), reduce token costs, or provide production observability, rebuild the agent loop using a framework like Pydantic AI or LangGraph. Carry over skills and MCP server integrations. Rebuild conversation history management, state management, and the agent loop from scratch.

The graduation triggers are concrete:
1. **Multi-user deployment** -- subscription ToS restricts SDK to single user
2. **Speed requirements** -- SDK's reasoning overhead makes sub-second responses impossible
3. **Cost sensitivity** -- API-key usage at scale makes SDK-based agents prohibitively expensive
4. **Observability needs** -- production agents need custom conversation history storage and monitoring

Cole Medin demonstrates this: using Claude Code to build a Pydantic AI agent with skills support, effectively using the SDK as a development tool to build the framework agent.

## Why It Matters

The SDK-vs-framework decision is not a permanent architectural choice but a lifecycle stage. Treating it as a binary decision leads to either over-engineering (using frameworks for personal tools) or under-engineering (using SDKs for production systems). The graduation path makes the two approaches complementary rather than competitive.

The key insight: skills and MCP servers are the portable assets that survive graduation. The agent loop, state management, and conversation history are the disposable infrastructure that gets rebuilt. This means investing in high-quality skills and MCP servers is the highest-ROI activity for agent development, regardless of current infrastructure choice.

## Why People Are Using It

- Faster time-to-first-prototype: SDK eliminates infrastructure setup
- Skills and MCP servers carry over to framework implementations
- Clear graduation triggers prevent premature optimization
- Coding agents (Claude Code) can help build the framework agent during graduation
- Risk reduction: validate the agent's value before investing in production infrastructure

## Potential Improvements

- SDK "export to framework" tooling that generates equivalent Pydantic AI code
- Migration guides that document which SDK features map to which framework patterns
- Automated graduation detection: SDK monitoring that flags when triggers are approaching

## Potential Failure Modes

- Building too much on the SDK before graduation, making the rewrite expensive
- Skills that work in SDK but silently break in framework due to implicit SDK dependencies
- Graduation delay: continuing to use SDK in production because "it works" despite ToS violations or cost overruns
- Over-graduating: migrating to framework for a personal tool that never needed to scale
