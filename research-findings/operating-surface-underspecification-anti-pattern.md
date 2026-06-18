---
name: "Operating Surface Underspecification Anti-Pattern"
summary: "Most teams building agent products are overfocused on model selection and underspecified on the operating surface around the model. They know which LLM they want but do not know: which tools the agent can or should see, what the interaction model is for user approval, or how to enforce and validate multi-agent coordination. The actual work of building production agents lives in these operating-surface questions, not in model choice."
implementation_notes: "MetaSystem has invested heavily in operating-surface specification (DD-29 human gate, DD-30 read/write boundaries, agent constitutions, skill contracts, MCP server configuration). This finding validates that investment. The risk for MetaSystem is the inverse: over-specifying the operating surface to the point of rigidity. The finding also applies when evaluating external agent products: check whether they specify their operating surface or only their model."
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Partially Adopted"
priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "google-io-mcp-a2a-agui-protocol-stack.md"
related_findings:
  - file: "supervision-debt-anti-pattern.md"
    rel: "same-problem"
  - file: "agent-sprawl-anti-pattern-microservices-redux.md"
    rel: "same-problem"
  - file: "agentic-infrastructure-pilot-to-production.md"
    rel: "same-problem"
  - file: "six-layer-agent-infrastructure-stack.md"
    rel: "same-problem"
  - file: "minimal-agent-harness-skeleton-three-primitives.md"
    rel: "same-problem"
proposals: null
date_discovered: "2026-05-25"
last_updated: "2026-05-25"
pipeline_status: "synthesized"
consumed_by:
  - "templates/operating-surface-specification-template.md"
  - agent-design-patterns.md
tags:
  - "session-95-reextract"
  - "agent-design"
  - "anti-pattern"
---

# Operating Surface Underspecification Anti-Pattern

## What It Is

An observed pattern in teams building AI agent products: they invest heavily in model selection (which LLM, which parameters, which fine-tuning) while leaving the operating surface around the model underspecified. Three specific gaps:

1. **Tool surface undefined:** Teams have a prototype that can call APIs, but they have not decided which tools the agent can or should see in production. Tool access is treated as an implementation detail rather than a design decision.

2. **Interaction model missing:** Teams can imagine agents doing work, but they have not designed the interaction model for user approval. When and how does a human approve, deny, edit, or steer agent work?

3. **Coordination unenforceable:** Teams can imagine multiple agents coordinating, but they have no mechanism to enforce or validate that coordination -- no contracts, no observability, no failure handling.

The anti-pattern: "most teams are overfocused on model selection, and they're very underspecified on the operating surface around the model."

## Why It Matters

Model selection is a necessary but small fraction of the design surface for a production agent system. The operating surface -- tools, permissions, approval flows, coordination contracts, observability -- is where production failures occur. A well-chosen model with an underspecified operating surface will fail in production. A mediocre model with a well-specified operating surface will be governable and improvable.

The finding maps directly to the three-question protocol framework: teams answer "which model?" (not one of the three questions) while leaving "what can it use?", "who can it work with?", and "how does the human stay in control?" unaddressed.

For MetaSystem: this anti-pattern is one that MetaSystem has largely avoided through heavy governance investment (DDs, constitutions, skill contracts, permission systems). The finding validates the approach but also serves as a diagnostic: when evaluating external agent frameworks or products, check whether they specify their operating surface. If they lead with model selection, they likely have this anti-pattern.

## Why People Are Using It

Described in a Google I/O 2025 protocol analysis. The author observes this as the common failure mode across build teams: model selection gets executive attention and engineering investment, while operating-surface questions get deferred to "later" or "implementation phase."

## Potential Improvements

- Develop an "operating surface specification template" that teams fill out before writing agent code: tool inventory, permission model, approval flow, coordination contracts, observability requirements
- Make operating-surface specification a gate for agent deployment (no production agents without a completed spec)
- When evaluating agent frameworks, score them on operating-surface support (tool scoping, approval flows, tracing) not just model integration

## Potential Failure Modes

- Over-specification: teams that internalize this finding may spend excessive time specifying operating surfaces for simple agents that would be better served by rapid iteration
- Specification drift: the operating surface is defined at design time but not maintained as the agent's capabilities evolve
- False completeness: having a specification document does not guarantee enforcement -- the specification must be machine-enforced, not just documented
- The anti-pattern can hide inside "agile" approaches: "we'll specify the operating surface iteratively" often means "we'll never specify it"
