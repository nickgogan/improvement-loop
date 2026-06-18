---
title: "Three-Question Protocol Selection for Agent Systems"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "three-question-protocol-selection-framework"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent workflow designers selecting integration protocols"
    - "agent harness architects evaluating which protocol layers to adopt"
    - "teams evaluating whether a new agent protocol is relevant to their system"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "trivial — decision framework applied at design time; no migration cost to change which questions are used"
  auditability: "high when protocol selection decisions are recorded in design docs with explicit answers to each question; low when protocol choices are implicit"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "MetaSystem answers Q1 (MCP servers in use) and Q2 (subagent architecture covers coordination). Q3 (human control protocol) is partially addressed via human-gate governance but without a formal protocol."
contract:
  preconditions: "A new agent workflow or protocol adoption is under design. The designer can describe the workflow in terms of what the agent does, who else it works with, and what human control is required."
  invariants: "Protocol selection is driven by workflow requirements, not technology features. Each of the three core questions is answered explicitly before a protocol is adopted or rejected. Protocols are only adopted when the corresponding question has a 'yes' answer."
  governance: "Owner: Any design decision, agent specification, or architecture doc that governs protocol adoption. Each doc that adds or removes a protocol layer must record which of the three questions drove the decision. Audit: for any protocol in use, identify which question it answers; if no question maps to it, treat as unvalidated."
  recovery: "If a protocol was adopted without answering the corresponding question → document the retroactive answer; if the answer is 'no,' evaluate whether the protocol is earning its complexity cost. If a new protocol is proposed → apply the three questions before evaluating features; if no question maps, defer adoption until a workflow need is demonstrated."
tags:
  - "extracted-artifact"
  - "rule"
  - "protocol-selection"
  - "agent-design"
  - "decision-framework"
---

# Three-Question Protocol Selection for Agent Systems

**Source:** [[three-question-protocol-selection-framework]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

A new agent workflow is being designed, or a protocol adoption decision is being made. The design space includes options across tool integration, agent coordination, and human control — and there is risk of adopting protocols based on feature interest rather than workflow need.

Scope of application: any agent system design that involves selecting integration protocols or infrastructure layers. Single-agent systems with no delegation and no external tool integration may not need formal protocol selection, but the questions still serve as a diagnostic.

## Action

**Required:** Before adopting or rejecting any agent protocol layer, answer the three core questions:

1. **What can the agent use?** — If the workflow requires the agent to discover and invoke external tools, data sources, or services, a tool-integration protocol is needed (e.g., MCP). If no external tool access is required, skip this layer.
2. **Who else can the agent work with?** — If the workflow requires delegating to another agent across a product or organizational boundary, an agent coordination protocol is needed (e.g., A2A). If all coordination is internal, skip this layer.
3. **How does the human stay in control while the agent is working?** — If the workflow involves long-running or consequential agent actions, a human interaction protocol is needed (e.g., an approval/interrupt layer). If the task is fully autonomous with no required human touchpoints, document that explicitly.

**Forbidden:** Adopting a protocol because it is new, well-marketed, or used by others without mapping it to one of the three questions. Skipping the three-question check and selecting protocols based on feature lists or ecosystem participation.

## Boundary

Enforced at the design-time decision point for protocol adoption. The rule applies when:
- a new agent workflow is being specified, or
- an existing workflow is evaluating adding a protocol layer.

The rule does not govern implementation-level protocol details (e.g., MCP server configuration, API shapes) — it governs the selection decision only.

## Enforcement

- **Mechanism:** Design decisions and architecture docs that govern protocol adoption must record explicit answers to each of the three questions. A protocol without a mapped question is unvalidated.
- **Check (deterministic):** For each protocol in use: `(question_mapped == true) AND (question_answered_yes == true)`. Any protocol where the mapped question is answered "no" is a candidate for removal.
- **Violation response:**
  - *Protocol adopted without mapped question:* retroactively document which question it answers; if none, flag for removal review.
  - *Three questions skipped:* halt protocol adoption; complete the question answers first.
  - *New protocol proposed with no workflow need:* defer until a "yes" answer to one of the questions can be demonstrated.
- **Enforcement location:** Design decision records, agent specification templates, and architecture review checklists.

## Rationale

The agent protocol space has a standards-war dynamic: new acronyms, new diagrams, new claims that a previously missing piece has been solved. Without a need-driven filter, teams accumulate protocol infrastructure that adds complexity without answering real workflow requirements.

The three-question framework grounds protocol selection in workflow requirements rather than technology features. It converts the question "should we adopt protocol X?" into "does our workflow require X's capability?" — a question answerable without deep protocol expertise.

The framework is protocol-neutral in principle: the three questions remain useful even as the specific protocols (MCP, A2A, AGUI) evolve or are superseded. A team using a different stack applies the same questions with different protocol names in the answers.

Origin: Google I/O 2025 protocol landscape analysis. Presented as a diagnostic for build teams navigating the six-protocol landscape without getting lost in the standards competition.

## Failure Modes

- **Cross-layer coupling.** Real workflows may need integration across layers (e.g., an agent that both uses tools and coordinates with other agents). The framework does not specify how to handle cross-layer dependencies. Mitigation: answer all three questions independently before looking at cross-layer interaction.
- **Contested-layer gap.** Three additional questions cover specialized layers (structured UI, authorized payments, autonomous resource purchase). If these become core requirements, the three-question framing is incomplete. Mitigation: treat the extended questions (4–6) as a supplementary checklist for domain-specific workflows.
- **Framework bias toward current dominant protocols.** The three questions were formulated with MCP/A2A/AGUI as the reference stack. A team on a different stack may find the mapping less direct. Mitigation: apply the questions as capability requirements, not protocol names; fill in the protocol that answers each question for your stack.
- **"Yes to all three" avoidance.** Teams may answer "yes" to all three questions to justify adopting the full stack without genuine workflow need. Mitigation: require concrete workflow evidence for each "yes" answer, not inference from future capability.

## Contract

### Preconditions
A new agent workflow or protocol adoption is under design. The designer can describe the workflow in terms of what the agent does, who else it works with, and what human control is required.

### Invariants
Protocol selection is driven by workflow requirements, not technology features. Each of the three core questions is answered explicitly before a protocol is adopted or rejected. Protocols are only adopted when the corresponding question has a "yes" answer.

### Governance
Owner: Any design decision, agent specification, or architecture doc that governs protocol adoption. Each doc that adds or removes a protocol layer must record which of the three questions drove the decision. Audit: for any protocol in use, identify which question it answers; if no question maps to it, treat as unvalidated.

### Recovery
If a protocol was adopted without answering the corresponding question → document the retroactive answer; if the answer is "no," evaluate whether the protocol is earning its complexity cost. If a new protocol is proposed → apply the three questions before evaluating features; if no question maps, defer adoption until a workflow need is demonstrated.
