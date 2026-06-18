---
title: "Declare Model Slots in Config, Not Runtime Heuristics"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "auxiliary-model-slot-architecture"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent systems that invoke more than one model or model tier across different subtask types"
    - "skill and harness configuration where model selection is currently handled by prompt-level logic or runtime conditionals"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "low — changing slot assignments requires config file edits and a session restart; no data migration cost but behavioral changes are immediate on next run"
  auditability: "high — named slots in static config are diffable and auditable; runtime heuristics are not"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Not Yet Started"
    notes: "Implementation notes in source finding identify GSD skill system as the primary adoption candidate: current agent-level model profiles (quality/balanced/budget) would be refined to task-level named slots."
contract:
  preconditions: "The system uses more than one model or model tier. At least one subtask type (e.g., compression, summarization, title generation) has materially lower quality requirements than the primary reasoning task."
  invariants: "All model assignments are declared as named slots in a static configuration file before any session begins. No prompt-level logic, runtime if-branches, or agent-authored overrides determine which model handles a subtask — that decision is made at config-authoring time by the builder. The slot taxonomy (the set of named task types) is explicit and versioned alongside the agent config. Default slot behavior (unspecified slots fall back to the main model) is declared, not assumed."
  governance: "Owner: the agent or harness configuration file that declares the slot taxonomy. Any skill or agent specification that invokes a model must reference a named slot, not a literal model name. When a new subtask type is added to the system, a slot assignment must be declared in config before the subtask is activated. The slot taxonomy is reviewed during major agent redesigns, not on every task addition."
  recovery: "If a subtask is invoked and its slot is unspecified → fall back to the main model slot and log the missing-slot event. If a declared slot references a model that is unavailable → fall back to the main model slot; surface the unavailability as a startup warning. If runtime heuristics are discovered in prompt layers that override declared slots → flag as a governance violation; remove the heuristic and declare the intended behavior as a named slot."
tags:
  - "extracted-artifact"
  - "rule"
  - "agent-design"
  - "model-selection"
  - "configuration"
---

# Declare Model Slots in Config, Not Runtime Heuristics

**Source:** [[auxiliary-model-slot-architecture]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent system uses more than one model or model tier. The current design either (a) selects models via prompt-level runtime logic ("if this is a summarization task, use the cheaper model"), (b) delegates model choice to the agent at inference time, or (c) applies a single model to all subtasks regardless of quality requirements.

## Action

**Required:** Declare all model assignments as named slots in a static configuration file. Each slot corresponds to a task type (e.g., `main`, `compression`, `summarization`, `title`, `vision`, `approval`). Each slot specifies the model to use and optionally a fallback. The configuration is the authoritative source for model selection — not the prompt, not the agent's runtime judgment.

**Forbidden:** Embedding model selection logic in prompt instructions ("use Haiku for summarization"). Allowing an agent to choose which model to invoke at inference time based on self-assessed task complexity. Using literal model names in skill or agent files outside the config schema.

## Boundary

Applies at the design time of any agent or skill system that invokes models. The rule governs the configuration authoring step, not the inference step. Once config is authored, the runtime simply reads slots — no further governance is needed at inference time.

## Enforcement

- **Mechanism:** Skill and agent files reference slot names (e.g., `model_slot: compression`), not model names. The config file maps slot names to models. A config-linting step can verify all referenced slots are declared.
- **Check (deterministic):** `(all_subtask_types_have_declared_slots == true) AND (no_model_names_in_prompt_layers == true) AND (fallback_behavior_declared == true)`. Any branch false → governance violation.
- **Violation response:** Flag any prompt layer containing a model name as a governance violation. Require the builder to extract the assignment into config and replace the inline reference with a slot name.
- **Cannot be self-certified:** A static config linter or pre-session validation step enforces this; the agent cannot certify its own compliance because the rule governs the config authored before the agent runs.

## Rationale

Runtime model selection heuristics are prompt logic that becomes invisible to maintainers — it is not diffable, not auditable, and drifts as model names change. Named slots in static config are a single source of truth: the builder decides once, per subtask type, which quality tier is appropriate. This decision is explicit, versioned, and reviewable.

The production evidence (Hermes YAML config with 8 named slots) shows this is tractable: the slot taxonomy does not need to be exhaustive at launch. Unspecified slots fall back to the main model, so builders add slots incrementally as cost/quality tradeoffs are identified.

The failure mode the rule prevents: an agent routing its own subtasks to cheaper models based on self-assessed complexity. This conflates task execution with resource allocation — a builder decision, not an agent decision.

## Failure Modes

- **Slot taxonomy mismatch.** The system adds a new subtask type but no slot is declared; the task silently routes to the main model at higher cost than intended. Mitigation: log missing-slot events as startup warnings; treat them as configuration gaps, not silent fallbacks.
- **Over-splitting.** Too many fine-grained slots (one per prompt variant) creates configuration overhead that exceeds the cost savings. Mitigation: start with 3-5 high-contrast slots (main, cheap-batch, vision); add slots only when a cost/quality gap is demonstrated.
- **Model name drift.** A slot references a model name that is retired. Mitigation: model names in config are validated at session startup against available providers; startup fails loudly on unresolvable slots.
- **Heuristic leakage.** A skill adds a conditional model-selection comment that is interpreted as instruction by the agent. Mitigation: skill review checklist includes a scan for inline model names; the config linter flags them.

## Contract

### Preconditions
The system uses more than one model or model tier. At least one subtask type (e.g., compression, summarization, title generation) has materially lower quality requirements than the primary reasoning task.

### Invariants
All model assignments are declared as named slots in a static configuration file before any session begins. No prompt-level logic, runtime if-branches, or agent-authored overrides determine which model handles a subtask — that decision is made at config-authoring time by the builder. The slot taxonomy (the set of named task types) is explicit and versioned alongside the agent config. Default slot behavior (unspecified slots fall back to the main model) is declared, not assumed.

### Governance
Owner: the agent or harness configuration file that declares the slot taxonomy. Any skill or agent specification that invokes a model must reference a named slot, not a literal model name. When a new subtask type is added to the system, a slot assignment must be declared in config before the subtask is activated. The slot taxonomy is reviewed during major agent redesigns, not on every task addition.

### Recovery
If a subtask is invoked and its slot is unspecified → fall back to the main model slot and log the missing-slot event. If a declared slot references a model that is unavailable → fall back to the main model slot; surface the unavailability as a startup warning. If runtime heuristics are discovered in prompt layers that override declared slots → flag as a governance violation; remove the heuristic and declare the intended behavior as a named slot.
