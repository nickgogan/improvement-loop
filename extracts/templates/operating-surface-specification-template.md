---
title: "Operating Surface Specification Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "operating-surface-underspecification-anti-pattern"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "anyone designing a new agent before writing agent code"
    - "teams reviewing whether an existing agent has a specified operating surface"
    - "agent framework evaluators scoring whether a platform supports operating-surface specification"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "trivial — produces a specification document; revision is a document edit with no migration cost"
  auditability: "high when the spec is a versioned document linked to the agent it specifies; low when operating surface decisions are scattered across code comments and tickets"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Partially Adopted"
    notes: "MetaSystem has invested heavily in operating-surface specification (human-gate governance, read/write boundaries, agent constitutions, skill contracts). This template formalizes the three-gap analysis into a reusable spec structure."
contract:
  preconditions: "A new agent is being designed, or an existing agent's operating surface is being reviewed. The specifier can describe what the agent is intended to do."
  invariants: "All three gaps (tool surface, interaction model, coordination enforcement) are addressed before the spec is considered complete. The spec is written before agent code is written. A human reviews and approves the spec before implementation begins."
  governance: "Owner: The agent designer or team lead responsible for the agent. The spec is a prerequisite for agent implementation — no production agent without a completed spec. When the agent's capabilities change, the spec is updated before the change is deployed."
  recovery: "If a section cannot be completed at design time → mark it as 'TBD — deferred to iteration N'; do not leave it blank. If the spec diverges from the implemented agent → update the spec; treat divergence as specification drift and log it. If the spec is completed but enforcement mechanisms are not yet implemented → document the gap as an accepted risk with a target remediation date."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-design"
  - "operating-surface"
  - "specification"
---

# Operating Surface Specification Template

**Source:** [[operating-surface-underspecification-anti-pattern]]
**Form:** template
**Extraction date:** 2026-05-25

## Variables

| Variable | Description |
|----------|-------------|
| `{{AGENT_NAME}}` | Name of the agent being specified |
| `{{AGENT_PURPOSE}}` | One-sentence description of what the agent does |
| `{{SPECIFIER}}` | Name or role of the person completing the spec |
| `{{SPEC_DATE}}` | Date the spec is written |
| `{{ITERATION}}` | Version or iteration number of this spec |

---

## Body

```markdown
# Operating Surface Specification — {{AGENT_NAME}}

**Agent:** {{AGENT_NAME}}
**Purpose:** {{AGENT_PURPOSE}}
**Specifier:** {{SPECIFIER}}
**Date:** {{SPEC_DATE}}
**Iteration:** {{ITERATION}}

---

## Q1 — Tool Surface: What can this agent use?

_Answer this question before asking what model the agent should use._

### Tool inventory

List every tool, API, data source, or MCP server the agent is allowed to access in production.

| Tool / Surface | Purpose | Access type | Scoping notes |
|----------------|---------|-------------|---------------|
| [fill in] | [fill in] | Read / Write / Read-Write | [any access restrictions] |

### Tool boundaries

What is the agent explicitly NOT allowed to use, even if technically accessible?

- [fill in — e.g., "No access to billing APIs", "No write access to user profile data"]

### Tool selection rationale

Why does this agent need these tools and not others?

[Fill in: 1-3 sentences justifying the tool set. If you cannot justify a tool, remove it.]

---

## Q2 — Interaction Model: How does the human stay in control while the agent is working?

_Answer this question before deciding how autonomous the agent should be._

### Human touchpoints

For each significant agent action, specify whether human approval is required, optional, or not needed.

| Action / decision type | Approval required? | Approval mechanism | Who approves? |
|-----------------------|-------------------|-------------------|---------------|
| [fill in] | Required / Optional / Not needed | [e.g., explicit confirm, review gate, async notification] | [fill in] |

### Interrupt and override model

How does a human stop, redirect, or override the agent mid-execution?

- Interrupt mechanism: [fill in — e.g., "Cancel button in UI", "Kill-switch hook", "Session termination"]
- Override mechanism: [fill in — e.g., "Human edits the plan artifact before implementation session starts"]
- Escalation path: [fill in — e.g., "Agent halts and surfaces a decision point when confidence is below threshold"]

### Autonomy level

Based on the touchpoints above, classify the agent's autonomy level:

- [ ] **Fully supervised** — every action requires human approval
- [ ] **Human-in-the-loop** — significant actions require approval; routine actions are autonomous
- [ ] **Human-on-the-loop** — agent acts autonomously; human can review and intervene
- [ ] **Fully autonomous** — no human touchpoints (requires explicit justification below)

Justification if fully autonomous:
[Fill in or delete]

---

## Q3 — Coordination Enforcement: Who else can this agent work with, and how is that enforced?

_Answer this question before designing multi-agent workflows._

### Coordination surface

Does this agent delegate to, or receive delegation from, other agents?

- [ ] This agent operates alone — no multi-agent coordination.
- [ ] This agent delegates subtasks to other agents. (List them below.)
- [ ] This agent receives tasks from an orchestrator. (Name it below.)
- [ ] Both of the above.

| Coordination partner | Direction | Protocol / mechanism | What can be delegated? |
|---------------------|-----------|---------------------|----------------------|
| [fill in] | Delegates to / Receives from | [e.g., subagent call, A2A protocol, file handoff] | [fill in] |

### Coordination contracts

For each coordination relationship, what are the contracts?

- Input contract: [What must the delegating agent provide? Format, completeness requirements?]
- Output contract: [What must the receiving agent produce? Format, acceptance criteria?]
- Failure handling: [What happens if the coordination fails or produces bad output?]

### Observability

How is coordination validated and monitored?

- Logging: [fill in — e.g., "Each agent logs its inputs and outputs to a shared operations log"]
- Validation: [fill in — e.g., "Output from subagent is schema-validated before orchestrator accepts it"]
- Failure handling: [fill in — e.g., "Orchestrator retries once; on second failure, escalates to human"]

---

## Spec Completeness Check

Before submitting for human review, confirm:

- [ ] Q1 completed: tool inventory has at least one entry; boundaries are stated
- [ ] Q2 completed: every significant action has an approval classification; interrupt mechanism is named
- [ ] Q3 completed: coordination surface is classified (even if "none"); contracts exist for each coordination relationship
- [ ] No sections left blank (TBD entries are acceptable but must be dated and assigned)
- [ ] Human reviewer named: [fill in]
- [ ] Target review date: [fill in]

---

## Revision Log

| Date | Iteration | What changed | Why |
|------|-----------|-------------|-----|
| {{SPEC_DATE}} | {{ITERATION}} | Initial spec | [fill in] |
```

---

## Usage

1. Fill in all `{{VARIABLES}}` before starting.
2. Answer Q1, Q2, and Q3 in order. The questions are sequenced intentionally — tool surface constrains interaction model, which constrains coordination.
3. If a section cannot be completed, mark it "TBD — [reason] — target date: [date]" rather than leaving it blank.
4. Complete the Spec Completeness Check before submitting for human review.
5. Human approval is required before implementation begins.
6. Update the spec (and revision log) when the agent's capabilities change.

---

## Variation Axis

| Variation | When to use |
|-----------|-------------|
| **Minimal (Q1 only)** | For simple single-action agents with no approval flow and no coordination — fill in Q1 and mark Q2/Q3 as "N/A — single action, fully autonomous" with justification |
| **Evaluation scorecard** | When evaluating an external agent framework — answer the three questions as "does this framework support X?" rather than "what does this agent do?"; score each dimension |
| **Retrospective** | For agents already in production without a spec — fill in the template to describe current behavior; gaps between current state and template requirements are remediation items |
| **Multi-agent system** | For systems with multiple coordinating agents — complete one spec per agent; link specs via the coordination surface section |

---

## Contract

### Preconditions
A new agent is being designed, or an existing agent's operating surface is being reviewed. The specifier can describe what the agent is intended to do.

### Invariants
All three gaps (tool surface, interaction model, coordination enforcement) are addressed before the spec is considered complete. The spec is written before agent code is written. A human reviews and approves the spec before implementation begins.

### Governance
Owner: The agent designer or team lead responsible for the agent. The spec is a prerequisite for agent implementation — no production agent without a completed spec. When the agent's capabilities change, the spec is updated before the change is deployed.

### Recovery
If a section cannot be completed at design time → mark it as "TBD — deferred to iteration N"; do not leave it blank. If the spec diverges from the implemented agent → update the spec; treat divergence as specification drift and log it. If the spec is completed but enforcement mechanisms are not yet implemented → document the gap as an accepted risk with a target remediation date.
