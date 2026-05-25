---
name: Brain-Hands Decoupling Architecture
summary: Decouple agent 'brains' (LLM + harness) from 'hands' (sandboxes, tools, execution environments) via a uniform execute(name, input) -> string interface. Enables independent scaling, failure isolation,
  lazy provisioning (60-90% TTFT reduction), and many-brains/many-hands topologies.
implementation_notes: MetaSystem's skill architecture partially decouples brain from hands (skills are tools). The key gap is that our tools are co-located with the brain -- no independent scaling or failure
  isolation.
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-managed-agents-decoupling.md
- claude-code-architecture-under-the-hood.md
related_findings:
- file: anthropic-managed-agents-platform.md
  rel: extends
- file: durable-workflow-engine-for-agent-systems.md
  rel: same-problem
- file: session-persistence-crash-resilient.md
  rel: same-problem
- file: tool-gateway-security-boundary.md
  rel: same-problem
- file: session-as-append-only-event-log.md
  rel: enables
- file: acp-spawn-cross-tool-delegation.md
  rel: same-problem
- file: subagent-as-uniform-tool-interface.md
  rel: extends
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- agent-architecture-decisions.md
---

## What It Is

Anthropic's managed agents platform virtualizes three agent components -- session (append-only event log), harness (the agentic loop calling Claude and routing tool calls), and sandbox (execution environment) -- into stable interfaces analogous to OS abstractions (process, file). The critical decoupling: brains interact with hands via a uniform `execute(name, input) -> string` interface. Hands can be containers, phones, emulators, MCP servers, or custom tools -- the brain doesn't care. This enables: (1) Many brains: stateless harnesses scale horizontally without per-brain container overhead, (2) Many hands: a single brain reasons over multiple execution environments, and (3) Failure isolation: sandbox crashes are treated as tool errors, not session-ending failures.

## Why It Matters

Monolithic agent containers create "pets" -- named, irreplaceable instances where failure cascades across all components. Decoupling creates "cattle" -- interchangeable, disposable instances where any component can fail and be replaced independently. The performance impact is dramatic: lazy sandbox provisioning (only on first tool call) drops p50 TTFT by ~60% and p95 by >90%, since inference starts immediately after pulling session events rather than waiting for container provisioning.

## Why People Are Using It

Anthropic's production managed agents platform. The architecture solves concrete scaling problems: VPC resources no longer require network peering (brains connect to hands remotely), and the many-brains topology eliminates upfront provisioning overhead for non-sandbox sessions.

## Potential Improvements

Dynamic hand allocation based on task requirements. Hand pooling across brains for resource efficiency. Quality-of-service tiers for different hand types.

## Potential Failure Modes

Network latency between decoupled brain and hands. Complexity of managing distributed state across independent components. The uniform execute interface may lose expressiveness for tools that need streaming or bidirectional communication.
