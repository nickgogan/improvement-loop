---
name: MCP Enterprise Governance Gaps
summary: MCP lacks standardized audit trails, cost attribution, rate limiting, multi-tenancy isolation, gateway behavior, and portable configuration. Organizations deploying MCP at scale are independently
  inventing custom solutions for each gap. The 2026 roadmap explicitly prioritizes closing these gaps.
implementation_notes: These gaps affect MetaSystem indirectly -- our scale is small. But they explain why enterprise MCP adoption lags developer adoption and why custom middleware is currently required
  for production deployments. Monitor the SEP (Specification Enhancement Proposal) process for resolution.
category: Governance
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- mcp-everything-your-team-needs-to-know-workos.md
- cursor-ai-mcp-server-configuration-setup-auth-best.md
related_findings:
- file: governance-memory-append-only-audit-layer.md
  rel: same-problem
- file: mcp-session-scoped-authorization.md
  rel: same-problem
- file: tool-gateway-security-boundary.md
  rel: same-problem
- file: agent-identity-governance-enforcement-layer.md
  rel: same-problem
- file: structured-streaming-events-observability.md
  rel: enabled-by
- file: agent-sprawl-anti-pattern-microservices-redux.md
  rel: same-problem
- file: unified-tracing-opentelemetry-for-agents.md
  rel: enables
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: "raw"
consumed_by: []
---
# MCP Enterprise Governance Gaps

## What It Is
Five critical gaps in the MCP protocol for enterprise deployment:

1. **Cost Attribution & Rate Limiting:** No standardized mechanisms for capping agent usage or attributing costs. Emerging payment protocols (x402, Stripe MPP) address some concerns but organizational cost governance remains unsolved.
2. **Observability & Audit Trails:** No standardized logging, SIEM integration, or compliance infrastructure. Organizations independently build custom APM hookpoints.
3. **Multi-Tenancy:** No standard patterns for tenant isolation or tenant-specific policy enforcement in SaaS MCP servers.
4. **Gateway Behavior:** Authorization propagation, session affinity, and inspection boundaries undefined when running behind API gateways, security proxies, or load balancers.
5. **Portable Configuration:** No standard for exporting/importing MCP server configurations across clients.

## Why It Matters
These gaps block enterprise adoption. Each organization reimplements similar capabilities independently, wasting engineering effort and creating fragmented solutions. The 2026 roadmap explicitly prioritizes structured audit trails, enterprise auth integration, gateway patterns, and configuration portability.

## Why People Are Using It
Despite gaps, MCP adoption continues because the N+M integration economics are compelling. Organizations accept the governance debt and build custom middleware at organizational boundaries.

## Potential Improvements
The Linux Foundation governance model (Agentic AI Foundation) with Working Groups (Transports, Auth, Registry) and Specification Enhancement Proposals (SEPs) is the mechanism for resolution. Most enterprise features expected as extensions rather than core spec changes.

## Potential Failure Modes
Slower decision-making as consensus requirements increase under foundation governance. Custom solutions may calcify into incompatible pseudo-standards before official specs ship.
