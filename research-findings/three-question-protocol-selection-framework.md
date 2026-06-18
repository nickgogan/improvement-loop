---
name: "Three-Question Protocol Selection Framework for Agent Systems"
summary: "Decision framework for selecting which agent protocols apply to a given workflow: (1) What can the agent use? (MCP — tool/data layer), (2) Who else can the agent work with? (A2A — coordination layer), (3) How does the human stay in control? (AGUI — human interaction layer). Each question maps to exactly one protocol layer. Additional questions extend to contested layers: structured UI (A2UI), authorized payments (AP2), and programmatic resource purchase (X42)."
implementation_notes: "MetaSystem can apply these three questions as a checklist when designing any new agent workflow. Question 1 is answered (MCP servers in use). Question 2 is answered (subagent architecture, no cross-org delegation needed). Question 3 is partially answered (DD-29 human gate, but no formal control protocol). The framework also applies when evaluating whether a new protocol is worth adopting: does it answer one of these three questions better than the current solution?"
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "google-io-mcp-a2a-agui-protocol-stack.md"
related_findings:
  - file: "agui-human-control-layer-not-ui.md"
    rel: "enabled-by"
  - file: "google-a2a-protocol-agent-to-agent-interoperabilit.md"
    rel: "enabled-by"
  - file: "mcp-ecosystem-critical-mass-97m-installs.md"
    rel: "enabled-by"
  - file: "six-layer-agent-infrastructure-stack.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "rules/three-question-protocol-selection-for-agent-systems.md"
  - agent-design-patterns.md
tags:
  - "session-95-reextract"
  - "orchestration"
  - "decision-framework"
---

# Three-Question Protocol Selection Framework for Agent Systems

## What It Is

A practitioner decision framework that reduces the agent protocol landscape to three core questions. Each question maps to one protocol layer in the emerging standard stack:

1. **What can the agent use?** --> MCP (tool and data layer). The protocol an agent uses to discover and invoke the systems where work lives.
2. **Who else can the agent work with?** --> A2A (agent coordination layer). The protocol one agent uses to discover and delegate to another agent across product or company boundaries.
3. **How does the human stay in control while the agent is working?** --> AGUI (human interaction layer). The protocol that lets a long-running backend agent share state, events, approvals, and interruptions with a user-facing app.

Three additional questions extend to contested/domain-specific layers:
4. Does the workflow need structured UI beyond text? (A2UI)
5. Does the agent need to authorize a transaction? (AP2)
6. Does the agent need to autonomously pay for a resource? (X42)

The first three questions are presented as the "core stack" -- protocols that most agent products will need. The remaining three are narrower, still contested, or very domain-specific.

## Why It Matters

The agent protocol space has a standards-war problem: new acronyms, new diagrams, new claims that a missing piece has been solved. This framework cuts through the noise by grounding protocol selection in workflow requirements rather than technology features. Instead of asking "should we adopt X protocol?", teams ask "does our workflow require delegated expertise outside the primary agent?" If yes, look at A2A. If no, skip it.

For MetaSystem: the three questions provide a structured way to evaluate whether new protocols are relevant. Currently, Q1 (MCP) is addressed, Q2 (A2A) is addressed architecturally via subagent delegation (no cross-org needs), and Q3 (AGUI) is partially addressed via DD-29's human gate but without a formal protocol.

## Why People Are Using It

Presented in a Google I/O analysis video covering the six-protocol landscape. The framework is designed for build teams shipping AI agent products who need to decide which substrate protocols to invest in without getting lost in the standards scrum.

## Potential Improvements

- Extend the framework with a "when to skip" heuristic for each question (e.g., "A single product with a small set of tools may not need agent coordination at all")
- Add a maturity dimension: MCP is production-ready (14,000+ servers), A2A is early-production (50+ launch partners), AGUI is pre-production (concept-validated)
- Map each question to specific MetaSystem design decisions for internal use

## Potential Failure Modes

- Framework assumes cleanly separable protocol layers; real systems may need cross-layer integration that the framework does not address
- The "contested layers" (questions 4-6) may stabilize into core requirements, making the three-question framing incomplete
- Framework biases toward the MCP/A2A/AGUI stack specifically rather than being protocol-neutral; a team using a different stack might find the mapping less useful
