---
title: "Tool vs. Capability Classification and Stage-Map Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "two-layer-plugin-model-tools-vs-capabilities"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent systems being designed or refactored with more than one type of extension or plugin"
    - "skill registries where some entries are single-call functions and others are multi-step pipelines"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "low — reclassifying extensions between Tool and Capability affects dispatch logic, error handling, and observability config; requires updates to registration and orchestration layers"
  auditability: "high when Tool and Capability registries are separate and each Capability's stage list is declared; low when both are in a unified undifferentiated registry"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: "Implementation notes in source finding note that MetaSystem's skill system blurs this distinction — skills range from single-shot to multi-stage. The template is the design artifact for formalizing the distinction."
contract:
  preconditions: "An agent system has at least two distinct extension types: at least one that is a single-function invocation and at least one that is a multi-step pipeline owning the full turn. The system is being designed or the existing registry is being refactored."
  invariants: "Every extension is classified as either Tool or Capability before registration. Tools are invoked once per LLM decision; they do not own the turn. Capabilities own the full turn until they emit a final result; they sequence their own stages. Tool and Capability registries are separate; the orchestrator routes to them via distinct dispatch paths. All Capabilities declare their named stages at registration time."
  governance: "Owner: the extension registration layer and the orchestrator that dispatches to it. New extensions must be classified before registration — the registry does not accept unclassified entries. The decision rule (single-call vs multi-stage) is the authoritative classification criterion; edge cases are escalated to the system architect, not resolved by the registering agent."
  recovery: "If an extension is misclassified (a multi-stage pipeline registered as a Tool) → reclassify and re-register; audit any sessions where the misclassified extension was invoked and review the error-handling and cost-attribution records. If the boundary between Tool and Capability is disputed for a given extension → default to Capability (the more constrained classification); document the edge case for future decision rule refinement."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-design"
  - "orchestration"
  - "tools"
  - "capabilities"
  - "plugin-model"
---

# Tool vs. Capability Classification and Stage-Map Template

**Source:** [[two-layer-plugin-model-tools-vs-capabilities]]
**Form:** template
**Extraction date:** 2026-05-25

A two-part template for classifying agent extensions and documenting multi-stage Capability pipelines. Use Part A (Classification Worksheet) for every new extension. Use Part B (Capability Stage Map) for extensions that classify as Capabilities.

---

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{EXTENSION_NAME}}` | Canonical name (lowercase-hyphenated) | `deep-research` |
| `{{EXTENSION_DESCRIPTION}}` | Plain-English description of what it does | `Research a question by rephrasing, decomposing, searching, and synthesizing` |
| `{{INVOCATION_TRIGGER}}` | What causes this extension to be invoked | `LLM selects it from registry` / `Orchestrator routes to it based on user intent` |
| `{{SINGLE_CALL_RESULT}}` | For Tools: what the single call returns | `JSON array of search results` |
| `{{TURN_OWNERSHIP}}` | Does this extension own the full response turn? | `yes` / `no` |
| `{{STAGE_N_NAME}}` | Name of stage N in the Capability pipeline | `rephrasing`, `decomposing`, `researching`, `reporting` |
| `{{STAGE_N_INPUT}}` | Input to stage N | `original user query` |
| `{{STAGE_N_OUTPUT}}` | Output of stage N | `list of refined sub-questions` |
| `{{STAGE_N_FAILURE_MODE}}` | What can go wrong at stage N | `sub-question list empty — query too ambiguous` |
| `{{OUTPUT_ENVELOPE_SCHEMA}}` | Shared output schema all Capabilities must produce | `schemas/capability-result.json` |
| `{{EVENT_BUS_EVENTS}}` | Events emitted on the shared bus per stage | `research.rephrasing.complete`, `research.decomposing.complete` |

---

## Body

### Part A — Classification Worksheet

Fill this out for every new extension before registration.

```
Extension name:       {{EXTENSION_NAME}}
Description:          {{EXTENSION_DESCRIPTION}}
Invocation trigger:   {{INVOCATION_TRIGGER}}

Decision rule:
  Does this extension complete its work in a single function call?
    → YES: classify as TOOL
    → NO (requires multiple sequential steps, owns the turn until done): classify as CAPABILITY

Classification:       [ ] Tool   [ ] Capability

If Tool:
  Single-call return value: {{SINGLE_CALL_RESULT}}
  Turn ownership: no
  Error handling: retry once on failure; surface error to LLM for re-invocation decision
  Observability: log one call event (name, inputs, outputs, latency)

If Capability:
  Turn ownership: yes — the Capability controls the loop until emit_capability_result() is called
  Error handling: stage-level — see Stage Map below
  Observability: emit per-stage events on shared bus — see Stage Map below
  → Complete Part B: Capability Stage Map
```

**Context-gated vs user-toggleable (Tools only):**

```
Is this Tool always available when its context conditions are met?
  → YES: context-gated tool (activated/deactivated by harness based on context signals)
  → NO (user can enable/disable): user-toggleable tool (surfaced in settings UI)

Tool availability type:   [ ] Context-gated   [ ] User-toggleable
Context condition (if context-gated): ___________________________
Settings label (if user-toggleable): ___________________________
```

---

### Part B — Capability Stage Map

Complete this for every extension classified as a Capability.

```yaml
capability:
  name: {{EXTENSION_NAME}}
  description: {{EXTENSION_DESCRIPTION}}
  output_envelope: {{OUTPUT_ENVELOPE_SCHEMA}}
  event_bus_prefix: "{{EXTENSION_NAME}}"

  stages:
    - name: {{STAGE_1_NAME}}
      input: {{STAGE_1_INPUT}}
      output: {{STAGE_1_OUTPUT}}
      failure_mode: {{STAGE_1_FAILURE_MODE}}
      recovery: "..."
      event_emitted: "{{EXTENSION_NAME}}.{{STAGE_1_NAME}}.complete"

    - name: {{STAGE_2_NAME}}
      input: {{STAGE_2_INPUT}}
      output: {{STAGE_2_OUTPUT}}
      failure_mode: {{STAGE_2_FAILURE_MODE}}
      recovery: "..."
      event_emitted: "{{EXTENSION_NAME}}.{{STAGE_2_NAME}}.complete"

    # Repeat for each stage. Minimum 2 stages; if only 1 stage is needed, re-classify as Tool.

  terminal_stage: {{FINAL_STAGE_NAME}}
  result_call: "emit_capability_result(output_envelope)"
```

---

## Usage

**When to use this template:**
- Designing or registering a new extension in an agent system with mixed single-call and multi-step behaviors.
- Refactoring an existing unified skill registry into separate Tool and Capability registries.
- Documenting the stage structure of an existing multi-step pipeline for observability and error-handling purposes.

**Authoring sequence:**
1. Fill out Part A for the new extension. The decision rule is: single-call = Tool; multi-stage that owns the turn = Capability.
2. If Tool: complete the context-gated vs user-toggleable classification. Register in the Tool registry.
3. If Capability: complete Part B (Stage Map). Define per-stage inputs, outputs, failure modes, and recovery. Register in the Capability registry.
4. Verify that the extension's output conforms to the shared output envelope schema.
5. Verify that per-stage events are named consistently (`{{extension}}.{{stage}}.complete`).

**Design checklist:**
- [ ] Classification decision (Tool vs Capability) is documented with the decision rule answer.
- [ ] For Tools: turn ownership is no; error handling is single-retry.
- [ ] For Capabilities: all stages are named with explicit inputs, outputs, and failure modes.
- [ ] For Capabilities: terminal stage calls `emit_capability_result()` with the shared output envelope.
- [ ] For Capabilities: per-stage events follow the naming convention.
- [ ] Extension is registered in the correct registry (Tool or Capability) — not a unified undifferentiated list.

---

## Variation Axis

| Dimension | Tool | Capability |
|-----------|------|-----------|
| Invocation | LLM selects on demand | Orchestrator routes based on intent classification |
| Turn ownership | No — LLM retains control | Yes — Capability owns until `emit_capability_result()` |
| Error handling | Retry once; surface to LLM | Per-stage recovery; may require stage rollback |
| Cost estimation | Predictable (one call) | Accumulates across stages; budget declared at registration |
| Observability | One call log entry | Per-stage event on shared bus |
| Registry | Tool registry | Capability registry |
| Availability model | Context-gated or user-toggleable | Always routed by orchestrator; not user-toggleable |

**Edge case: complex tools.** A tool with internal retry logic starts to behave like a mini-capability. Classification rule: if the retry logic is internal and the LLM sees only a single call and result, it remains a Tool. If the retry loop is visible to the orchestrator as distinct steps, reclassify as a Capability.

---

## Contract

### Preconditions
An agent system has at least two distinct extension types: at least one that is a single-function invocation and at least one that is a multi-step pipeline owning the full turn. The system is being designed or the existing registry is being refactored.

### Invariants
Every extension is classified as either Tool or Capability before registration. Tools are invoked once per LLM decision; they do not own the turn. Capabilities own the full turn until they emit a final result; they sequence their own stages. Tool and Capability registries are separate; the orchestrator routes to them via distinct dispatch paths. All Capabilities declare their named stages at registration time.

### Governance
Owner: the extension registration layer and the orchestrator that dispatches to it. New extensions must be classified before registration — the registry does not accept unclassified entries. The decision rule (single-call vs multi-stage) is the authoritative classification criterion; edge cases are escalated to the system architect, not resolved by the registering agent.

### Recovery
If an extension is misclassified (a multi-stage pipeline registered as a Tool) → reclassify and re-register; audit any sessions where the misclassified extension was invoked and review the error-handling and cost-attribution records. If the boundary between Tool and Capability is disputed for a given extension → default to Capability (the more constrained classification); document the edge case for future decision rule refinement.
