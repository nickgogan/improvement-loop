---
title: "Label Agent Outputs as Act-On-This vs Interpret-First"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "interpretive-boundary-layer-fact-vs-judgment"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agents and tools that surface outputs to human decision-makers"
    - "output schemas for any agent that produces recommendations, summaries, trend analyses, or prioritizations"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "low — once an output schema includes the classification field, removing it requires coordinating all downstream consumers that rely on the label"
  auditability: "high when the classification is a mandatory field on every output object and can be filtered or counted; low when classification is conveyed by UI styling alone"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "An agent produces output that reaches a human decision-maker. The output may contain a mix of factual status information and inferential recommendations, trend analyses, or prioritizations."
  invariants: "Every output object carries an explicit binary classification: 'act-on-this' (factual, verified, low-risk) or 'interpret-first' (inferential, causal claim, novel pattern, or judgment call). The classification is a first-class field in the output schema — not a UI decoration applied after the fact. No output reaching a human decision-maker is presented without a classification."
  governance: "Owner: the agent specification or output schema that defines what the agent produces. The classification field is a required field in any output schema that reaches human decision-makers — not optional, not inferred from context. Consumer-side audit checks that every agent-produced output object includes the field. The agent may propose the classification; the agent cannot override a human correction to it."
  recovery: "If an output is produced without a classification field → treat as 'interpret-first' by default; do not allow it to drive action until classified. If boundary drift is detected (outputs initially classified 'interpret-first' are now being treated as 'act-on-this') → flag for reclassification; do not resolve by reclassifying upward without review. If interpretation fatigue reduces the signal value of 'interpret-first' labels → reduce the volume of inferential outputs, not the strictness of the classification."
tags:
  - "extracted-artifact"
  - "rule"
  - "governance"
  - "agent-outputs"
  - "decision-quality"
---

# Label Agent Outputs as Act-On-This vs Interpret-First

**Source:** [[interpretive-boundary-layer-fact-vs-judgment]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent produces output that reaches a human decision-maker. The output may contain a mix of types: factual status reports, metric thresholds, dependency flags (low-risk, high-confidence) alongside trend analyses, prioritizations, correlations, and inferences (high-uncertainty, judgment-dependent).

When both types are presented at the same confidence level, the organization treats high-confidence and low-confidence outputs identically — which silently degrades decision quality. The failure is not in individual outputs; it is in the architecture that presents them without differentiation.

## Action

**Required:** Every agent output object that reaches a human decision-maker must carry an explicit binary classification:

- **"act-on-this"** — factual, verified, low-risk; the system is operating within its established competence; status rollup, threshold crossed with clear historical precedent, dependency flag
- **"interpret-first"** — inferential; involves a judgment call, causal claim, trend interpretation, novel pattern, or prioritization; the system is making an inference it is not reliably equipped to resolve

The classification is a mandatory field in the output schema — not a UI treatment applied after the fact, not inferred from context by the consumer.

**Forbidden:** Producing output that reaches human decision-makers without a classification field. Allowing both factual and inferential outputs to be presented at the same visual salience without differentiation. Treating the classification as optional or decorative.

## Boundary

Enforced at the output schema definition for any agent whose outputs reach human decision-makers. Applies to the schema level — every output object must carry the field.

Does not apply to purely internal agent-to-agent outputs that never reach a human decision-maker in the pipeline.

## Enforcement

- **Mechanism:** The classification is a required field in the output schema. Any output object missing the field is malformed. Schema validation at the output boundary rejects unclassified outputs before they reach decision-makers.
- **Check (deterministic):** `output.classification IN ('act-on-this', 'interpret-first')` for every output object reaching a human. Missing or invalid value → schema validation failure.
- **Violation response:**
  - *Missing classification:* default to 'interpret-first'; block the output from driving action until explicitly classified.
  - *Boundary drift (interpret-first treated as act-on-this):* flag; require explicit reclassification review before allowing the output to drive automated action.
  - *Interpretation fatigue:* audit the agent's output volume and inferential ratio; reduce inferential output volume rather than weakening classification standards.
- **Cannot be self-certified:** The agent may assign the classification, but humans can override it. The classification field must be surfaced to human reviewers, not hidden in metadata.

## Rationale

All three org world-model architectures (vector DB, structured ontology, signal fidelity) share this blind spot. The interpretive boundary layer is the meta-solution that applies to all of them.

When an organization begins treating agent output the way they treat a trusted director's analysis, the damage is structural: a slow degradation of decision quality that manifests as bad luck or market shifts rather than "the agent was making editorial choices it was not equipped to make." The three concrete failure modes — a seasonal dip flagged as significant, a correlation mistaken for causation, information drift where absence of signal goes unnoticed — all share the same root: the consumer could not distinguish "the system knows this" from "the system inferred this."

The classification is architectural, not cosmetic. It must be designed into the output schema before the first human-facing output is produced.

## Failure Modes

- **Boundary drift over time.** Outputs initially classified 'interpret-first' become treated as 'act-on-this' through organizational habituation. Mitigation: track overrides; flag when a previously-inferential output class begins driving action without reclassification.
- **False precision.** Drawing the boundary creates a sense of safety that is not warranted if the classification itself is wrong. Mitigation: the classification is a starting point for review, not a guarantee of correctness.
- **Interpretation fatigue.** Too many 'interpret-first' labels overwhelm humans who start ignoring them — defeating the purpose. Mitigation: the problem is output volume, not classification standards; reduce inferential outputs rather than widening the 'act-on-this' class.
- **Classification as a judgment call.** Deciding what counts as a factual output vs. an inferential output is itself a judgment call, and agents may mis-classify. Mitigation: humans can override classifications; the field must be surfaced for review, not hidden.

## Contract

### Preconditions
An agent produces output that reaches a human decision-maker. The output may contain a mix of factual status information and inferential recommendations, trend analyses, or prioritizations.

### Invariants
Every output object carries an explicit binary classification: 'act-on-this' (factual, verified, low-risk) or 'interpret-first' (inferential, causal claim, novel pattern, or judgment call). The classification is a first-class field in the output schema — not a UI decoration applied after the fact. No output reaching a human decision-maker is presented without a classification.

### Governance
Owner: the agent specification or output schema that defines what the agent produces. The classification field is a required field in any output schema that reaches human decision-makers — not optional, not inferred from context. Consumer-side audit checks that every agent-produced output object includes the field. The agent may propose the classification; the agent cannot override a human correction to it.

### Recovery
If an output is produced without a classification field → treat as 'interpret-first' by default; do not allow it to drive action until classified. If boundary drift is detected (outputs initially classified 'interpret-first' are now being treated as 'act-on-this') → flag for reclassification; do not resolve by reclassifying upward without review. If interpretation fatigue reduces the signal value of 'interpret-first' labels → reduce the volume of inferential outputs, not the strictness of the classification.
