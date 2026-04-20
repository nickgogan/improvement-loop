---
notion_id: 3351e08b-9b34-81bc-bc22-f19195d00fcc
name: Google A2A Protocol -- Agent-to-Agent Interoperability Standard
summary: 'A2A (Agent-to-Agent) protocol at Linux Foundation with 50+ enterprise partners. Complements MCP: MCP = agent-to-resource, A2A = agent-to-agent. Agent Card (`/.well-known/agent.json`) as machine-discoverable
  capability declaration with authentication requirements and optional skill + pricing info. Enables cross-organizational agent delegation. Python + JavaScript SDKs available.'
implementation_notes: 'MCP + A2A = complete agent interoperability stack. With A2A, an orchestrator can discover and delegate to specialist agents it has never seen before using Agent Cards. Pricing info
  in Agent Cards enables cost-aware multi-agent routing. Source: https://www.digitalapplied.com/blog/google-a2a-protocol-agent-to-agent-communication-guide'
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- google-a2a-protocol-guide-digital-applied.md
proposals: []
date_discovered: '2026-04-01'
last_updated: '2026-04-08'
related_findings:
- file: mcp-ecosystem-critical-mass-97m-installs.md
  rel: enabled-by
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
---
# Google A2A Protocol -- Agent-to-Agent Interoperability Standard

## What It Is
Standard for AI agents to communicate, delegate tasks to, and receive results from other AI agents across organizational and vendor boundaries. Now at Linux Foundation with 50+ enterprise launch partners (Salesforce, SAP, ServiceNow, Workday, Atlassian, MongoDB, LangChain, CrewAI).

**Complementary to MCP:** MCP = agent-to-resource (tools, APIs, databases). A2A = agent-to-agent peer communication and delegation.

**Agent Card** (`/.well-known/agent.json`): Machine-discoverable JSON declaring identity, supported modalities (text/JSON/files/audio/video/streaming), authentication requirements (OAuth 2.0, API keys, service account tokens), and optional skill + pricing info.

**Task Lifecycle State Machine (6 states):**
1. `submitted` — Task accepted, processing hasn't started
2. `working` — Active processing, agent streams incremental results via Server-Sent Events
3. `input-required` — Agent needs clarification/authorization (human-in-the-loop support)
4. `completed` — Success with typed artifacts (ID, MIME type, inline or external data)
5. `failed` — Error with details for retry/escalation decisions
6. `cancelled` — Terminated by client or server; partial results may be included

**Security principle — Least Privilege:** When agent A delegates to agent B, agent B operates with its own credentials, not the original user's. Requires careful per-agent permission scoping.

## Why It Matters
Enables cross-vendor agent ecosystems, runtime capability discovery, and cost-aware multi-agent routing. The `input-required` state natively supports human-in-the-loop workflows for autonomous agents that need authorization at specific steps. Python + JavaScript SDKs available.

## Why People Are Using It
50+ enterprise launch partners including the core of enterprise application infrastructure (Salesforce, SAP, ServiceNow, Workday). Linux Foundation governance. Consulting firms (Deloitte, Accenture, KPMG, McKinsey) actively building on it.

## Potential Failure Modes
- **Schema evolution:** No standard for backward compatibility when agent capabilities change; custom versioning required
- **No centralized registry:** Protocol defines capability declaration but no discovery infrastructure; teams manage own agent registries
- **Billing/metering gap:** Agent Cards support pricing declarations but no standard usage tracking
- **Distributed tracing immature:** Multi-agent workflow observability requires manual instrumentation and task ID correlation
