---
title: "Scheduled Workflows Require Human Checkpoint Before Publish"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "five-pillar-agentic-os-framework"
identification_report: "building-agentic-systems.harvest-queue.md::five-pillar-agentic-os-framework::rule::scheduled-workflows-require-human-checkpoint"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "scheduled jobs (cron, time-window loops, agent.scheduledTask, routine engines)"
    - "automated agent tasks that produce externally-visible output"
    - "autonomous publishing systems (content generators, briefing senders, social-media posters, outbound communicators)"
  platform_coupling: "agnostic"
  autonomy: "supervised — autonomy stops at the publish boundary"
  stage: "operate"
  reversibility: "low at publish time — once external publish has occurred (post sent, message delivered, document broadcast), retraction is partial at best; checkpoint placement before publish keeps reversibility high inside the pipeline"
  auditability: "high when the human-gate step writes a decision artifact (approved/rejected with timestamp); low when the gate is a silent boolean flag with no log trail"
  evidence_strength: "Medium (practitioner-validated)"
  adoption:
    status: "Practitioner-Validated"
    notes: "Source practitioner ran scheduled workflows fully autonomous, observed ~20% failure rate (drift, hallucination, off-brand output), and shifted to '80% automated + human checkpoint before publish.' OB1 and Life Engine implementations adopt the same pattern. Threshold is domain-dependent — content generation has different failure modes than data analysis or code generation, so the 20% figure is illustrative, not universal."
contract:
  preconditions: "A scheduled or automated workflow exists. The workflow has at least one step with externally-visible side effects (publish, send, broadcast, post, deliver, commit-to-shared-state, notify-third-party). The scheduling mechanism (cron, time-window loop, routine engine, recurring agent task) can be configured to halt at an intermediate step and resume on human signal."
  invariants: "Every scheduled workflow with externally-visible side effects MUST include an explicit human-gate step before the externally-visible publish action. The human-gate step MUST: (a) produce a draft or staged artifact in a location the human can review, (b) halt downstream publish until a recorded human decision exists, (c) log approve/reject with timestamp and reviewer identity. Fully-autonomous publish is forbidden for any workflow whose output crosses an externally-visible boundary."
  governance: "Owner: any skill, agent, or routine definition that schedules recurring work. The rule must be expressible as a structural check on the scheduled-task definition — does the task graph contain an explicit human-gate node before any publish-class action? File-based active/inactive flags are an acceptable kill-switch mechanism but are NOT a substitute for the per-execution human checkpoint. `/assess-skill` and `/assess-agent` validate that scheduling-capable artifacts declare a checkpoint contract. Exemption (closed-loop workflows with no externally-visible side effects, e.g., internal data summarization that lands in a draft folder) must be declared explicitly in the artifact."
  recovery: "If a scheduled workflow is found to publish without a checkpoint → disable the workflow (set inactive flag), retract or annotate any auto-published output where retraction is possible, redesign with explicit gate, re-enable. If the human checkpoint is consistently rubber-stamped (>95% approval over a meaningful window) → review whether the failure modes have actually been engineered out, or whether the gate has degraded to ceremony; do not silently remove the gate. If the checkpoint introduces unacceptable latency → narrow the publish surface (smaller batches, more granular gates) rather than removing the gate."
tags:
  - "extracted-artifact"
  - "rule"
  - "scheduled-workflows"
  - "human-gate"
  - "agentic-os"
  - "publish-boundary"
  - "automation-safety"
---

# Scheduled Workflows Require Human Checkpoint Before Publish

**Source:** [[five-pillar-agentic-os-framework]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A scheduled or automated workflow (cron job, time-window proactive loop, routine, recurring agent task) executes a sequence of steps culminating in at least one action with externally-visible side effects — publish to a public surface, send a message via channel tools, post to social, broadcast a briefing, deliver a document, notify a third party, or otherwise cross the boundary from internal state into externally-observable output.

Scope of application: workflows whose output crosses an externally-visible boundary. Closed-loop workflows that operate purely on internal state (e.g., reindexing a private knowledge base, generating a draft that lands in a private review folder with no notification) are outside scope.

## Action

**Required:** The workflow MUST include an explicit human-gate step positioned before any externally-visible publish action. The gate MUST:
- Produce a staged draft or queued artifact in a location the reviewer can access (review folder, draft queue, "ready for approval" board).
- Halt the workflow's downstream publish step until a recorded human decision exists (approve / reject / edit-and-approve).
- Log the decision with timestamp and reviewer identity so the gate is auditable.

**Forbidden:** Fully-autonomous publish — i.e., a workflow path from scheduled trigger to externally-visible side effect with no human decision step in between. Treating a file-based active/inactive flag (kill switch) as a substitute for the per-execution checkpoint. A kill switch governs *whether the job runs*; the checkpoint governs *whether each run's output is published*. They are independent.

**Permitted alternatives** (acceptable checkpoint mechanisms):
- File-based active/inactive flag for the *workflow as a whole* (kill switch), in addition to a per-execution checkpoint.
- Draft queue with explicit human approval before publish (e.g., LinkedIn posts staged in a review folder).
- Staging into a review channel where the human pulls approved items forward.
- Two-step protocol where the agent posts a "ready for review" notification and waits for explicit "publish" instruction.

## Boundary

The rule applies at the transition between any internal step of a scheduled workflow and any step that crosses the externally-visible boundary. It does NOT apply to:
- Internal-only steps (data fetch, analysis, draft generation, log writes).
- Closed-loop workflows whose terminal step lands in a human review surface that is itself not externally visible.
- Manually-triggered runs of the same workflow logic — the scheduling mechanism is the trigger this rule attaches to; ad-hoc invocations are governed by the broader human-gate principle in DD-29 but are out of this rule's specific scope.

## Enforcement

- **Mechanism:** Structural check on the scheduled-task definition. The task graph (or its declarative equivalent — cron entry + procedure, routine config, agent.scheduledTask spec) must contain an explicit human-gate node positioned before any publish-class action. The check inspects: (a) does the task definition declare a publish-class step? (b) if yes, is there a gate-class step preceding it? (c) does the gate-class step write a decision artifact?
- **Check (deterministic):** For each scheduled task `T`: `has_publish_step(T) → has_preceding_gate_step(T) AND gate_writes_decision_artifact(T)`. Any task where the antecedent is true and the consequent fails → violation.
- **Violation response:**
  - *Workflow publishes without gate:* disable (flip inactive flag), retract or annotate any auto-published output where retraction is possible, redesign with explicit gate, re-enable.
  - *Gate exists but doesn't halt publish:* treat as no-gate; the gate is decorative until publish is conditional on the recorded decision.
  - *Gate is consistently rubber-stamped (>95% approve over a meaningful window):* do NOT silently remove the gate; investigate whether the failure modes that motivated the gate have been engineered out, or whether the gate has degraded to ceremony.
- **Cannot be self-certified at runtime:** the agent running the workflow cannot certify its own publish; the gate must be a layer the workflow cannot bypass — a human signal, an external approval system, or at minimum a file-write that a separate process consumes before publish proceeds.

## Rationale

The source practitioner began with a fully-autonomous content-publishing workflow (weekly digest pulling videos → analyzing → generating LinkedIn posts → posting). Direct observation: ~20% failure rate at full autonomy — off-brand output, hallucinated facts, drift from intended voice, occasional surfacing of inappropriate content. The shift to "80% automated + human checkpoint before publish" — the agent generates and stages, the human approves and publishes — eliminated the failure class without sacrificing the time savings.

The 20% figure is the load-bearing evidence: it is an empirically-observed failure rate at full autonomy on a real recurring workflow, not a theoretical concern. The conclusion is asymmetric — when failure means externally-visible bad output (off-brand post, wrong fact under your name, message to wrong audience), the cost of one failure exceeds the cumulative cost of a per-execution checkpoint over many successful runs.

This aligns with MetaSystem's DD-29 (human-gate-at-every-stage) governance invariant. DD-29 is a system-level governance rule; this artifact is its concrete operational form for the *scheduled workflow* shape. The two are complementary: DD-29 says no autonomous modification of live systems; this rule says the same principle attaches to any externally-visible publish boundary inside a scheduled workflow.

The rule is positive-space: instead of enumerating the failure modes that motivated it (off-brand output, hallucinated facts, voice drift, audience errors), the positive invariant is "explicit human gate before publish." One rule; bounded enforcement.

## Failure Modes

- **Kill switch confused with checkpoint.** The active/inactive flag toggles whether the workflow runs at all; it does not gate per-execution publish. Mitigation: require both — kill switch governs the workflow lifecycle, checkpoint governs each execution's output.
- **Gate exists but is not load-bearing.** The agent writes a draft, sends a "ready for review" notification, and then publishes anyway after a fixed timeout. This is fully-autonomous publish dressed up as a gate. Mitigation: publish must be conditional on a recorded human approval artifact; absent the artifact, no publish.
- **Rubber-stamp degradation.** Over time, the human checkpoints every run with no real review. The gate becomes ceremony, the failure modes return undetected. Mitigation: do not silently remove the gate; instead, audit whether the failure modes have been engineered out, narrow the publish surface so each gate has higher signal, or batch reviews to make each decision substantive.
- **Threshold mistransfer.** The 20% failure rate is from a content-generation domain. Other domains (data analysis, code generation, internal-only operations) have different failure profiles. Mitigation: the rule's invariant is the gate's existence at any publish boundary, not the 20% threshold; the threshold motivates the rule but is not its content.
- **Overzealous application.** Applying the rule to closed-loop internal workflows (reindex, internal summary, draft-to-private-folder) creates friction with no safety benefit. Mitigation: scope is *externally-visible side effects*; closed-loop workflows are explicitly out of scope.

## Contract

### Preconditions
A scheduled or automated workflow exists. The workflow has at least one step with externally-visible side effects (publish, send, broadcast, post, deliver, commit-to-shared-state, notify-third-party). The scheduling mechanism (cron, time-window loop, routine engine, recurring agent task) can be configured to halt at an intermediate step and resume on human signal.

### Invariants
Every scheduled workflow with externally-visible side effects MUST include an explicit human-gate step before the externally-visible publish action. The human-gate step MUST: (a) produce a draft or staged artifact in a location the human can review, (b) halt downstream publish until a recorded human decision exists, (c) log approve/reject with timestamp and reviewer identity. Fully-autonomous publish is forbidden for any workflow whose output crosses an externally-visible boundary.

### Governance
Owner: any skill, agent, or routine definition that schedules recurring work. The rule must be expressible as a structural check on the scheduled-task definition — does the task graph contain an explicit human-gate node before any publish-class action? File-based active/inactive flags are an acceptable kill-switch mechanism but are NOT a substitute for the per-execution human checkpoint. `/assess-skill` and `/assess-agent` validate that scheduling-capable artifacts declare a checkpoint contract. Exemption (closed-loop workflows with no externally-visible side effects, e.g., internal data summarization that lands in a draft folder) must be declared explicitly in the artifact.

### Recovery
If a scheduled workflow is found to publish without a checkpoint → disable the workflow (set inactive flag), retract or annotate any auto-published output where retraction is possible, redesign with explicit gate, re-enable. If the human checkpoint is consistently rubber-stamped (>95% approval over a meaningful window) → review whether the failure modes have actually been engineered out, or whether the gate has degraded to ceremony; do not silently remove the gate. If the checkpoint introduces unacceptable latency → narrow the publish surface (smaller batches, more granular gates) rather than removing the gate.
