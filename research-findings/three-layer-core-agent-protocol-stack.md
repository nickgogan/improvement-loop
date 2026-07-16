---
name: Three-Layer Core Agent Protocol Stack (MCP + A2A + AGUI)
summary: 'MCP (tool/data access), A2A (agent coordination), and AGUI (human control) form the three-layer core protocol stack for production agentic systems. Each layer answers one fundamental question
  about agent operation. The stack composes vertically: MCP gets the agent close to the work, A2A enables delegated expertise across boundaries, AGUI ensures humans can observe, approve, and steer. Teams
  that ship agents without all three layers accumulate supervision debt, coordination debt, or integration debt respectively.'
implementation_notes: 'MetaSystem covers Layer 1 (MCP servers for Perplexity, Context7, Notion, etc.) and partially covers Layer 3 (DD-29 human gate, conversational approval). Layer 2 (A2A) is not needed
  because MetaSystem''s multi-agent architecture is intra-system subagent delegation, not cross-organizational. The composition insight matters: these layers are complementary, not alternatives. Adopting
  one without planning for the others creates debt.'
category: Orchestration
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- google-io-mcp-a2a-agui-protocol-stack.md
related_findings:
- file: agui-human-control-layer-not-ui.md
  rel: extends
- file: google-a2a-protocol-agent-to-agent-interoperabilit.md
  rel: extends
- file: mcp-ecosystem-critical-mass-97m-installs.md
  rel: extends
- file: six-layer-agent-infrastructure-stack.md
  rel: same-problem
- file: mcp-n-plus-m-integration-economics.md
  rel: extends
proposals: null
date_discovered: '2026-05-25'
last_updated: '2026-05-25'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
tags:
- session-95-reextract
- orchestration
- protocols
---

# Three-Layer Core Agent Protocol Stack (MCP + A2A + AGUI)

## What It Is

A composition model for the three protocols that form the emerging standard stack for production agent systems:

| Layer | Protocol | Function | Question Answered |
|-------|----------|----------|-------------------|
| **Tool/Data** | MCP | Agent discovers and invokes systems where work lives | What can the agent use? |
| **Coordination** | A2A | Agent discovers and delegates to other agents across boundaries | Who can the agent work with? |
| **Human Control** | AGUI | Long-running agent shares state, events, approvals with user app | How does the human stay in control? |

The key insight is **composition, not competition**. These three protocols are not alternatives competing for the same slot -- they occupy distinct, complementary layers. MCP won adoption first because it solves the most immediate pain (agent has no access to tools). A2A addresses the next pain (agent cannot delegate to specialists). AGUI addresses the third (humans cannot observe or steer agent work).

Three additional protocols (A2UI for structured rendering, AP2 for authorized payments, X42 for programmatic machine payments) occupy contested or domain-specific layers that have not yet stabilized into the core stack.

## Why It Matters

The composition model matters because teams tend to adopt layers incrementally and discover the missing layers through failure:

1. **Wire model to tools** (MCP) --> agent can now do work
2. **Discover agent needs specialist capabilities** (A2A) --> agent can now delegate
3. **Discover agent is doing unexpected things in production** --> "Oh no, we need approval buttons, logs, a progress spinner" (AGUI)

Each missing layer creates a specific type of debt: integration debt (no MCP), coordination debt (no A2A), or supervision debt (no AGUI). The most dangerous is supervision debt because it manifests only after the agent is doing real work with real consequences.

The composition also implies a maturity model: MCP-only is a valid starting point for simple workflows, MCP+A2A for multi-agent workflows, and the full stack for production systems with human oversight requirements.

## Why People Are Using It

Google I/O 2025 featured multiple protocols from this stack. MCP has 14,000+ servers. A2A launched with 50+ enterprise partners (Atlassian, Box, PayPal, Workday, etc.). AGUI is integrated with LangGraph, CrewAI, Amazon Bedrock Agent Core, Pydantic AI, Mastra, and CopilotKit. The convergence across multiple vendors suggests this is not a single-vendor play but an industry consensus.

## Potential Improvements

- Define clear criteria for when each layer is "needed" vs. "optional" based on workflow characteristics
- Map the three-layer stack to MetaSystem's existing architecture to identify which layers are partially vs. fully covered
- Track whether the three contested layers (A2UI, AP2, X42) stabilize into the core stack or remain domain-specific

## Potential Failure Modes

- The stack assumes protocols compose cleanly; in practice, integration between layers may introduce its own complexity (e.g., AGUI approval gates on A2A delegations)
- Over-engineering: a single-user, single-agent system with a small tool set may not need A2A or AGUI at all; applying the full stack adds overhead
- Protocol lock-in: building on all three layers creates switching costs if any protocol loses to a competitor
- The "core vs. contested" distinction may not hold -- payment protocols (AP2/X42) may become core for commerce-oriented agents
