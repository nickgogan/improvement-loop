---
title: "Separate Planning and Implementation Sessions"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "planning-session-bias-separate-context-windows"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent workflows that include both a planning phase and an implementation phase"
    - "any agent harness or skill that transitions from specification to execution"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — workflow-level instruction; removal is a deletion with no migration cost"
  auditability: "high when plan artifacts are written to files and session boundaries are logged; low when plan context remains only in conversation history"
  evidence_strength: "Medium (practitioner-documented)"
  adoption:
    status: "Partially Adopted"
    notes: "MetaSystem uses separate sessions for different tasks. The rule makes the bias-prevention rationale explicit and mandates the plan artifact as the only shared context."
contract:
  preconditions: "An agent workflow contains a planning phase that produces a specification or plan, and a subsequent implementation phase that executes against it. The planning phase has produced a plan document or artifact."
  invariants: "The planning session ends before implementation begins. The plan is written to a persistent file artifact before the implementation session starts. The implementation session reads only the plan artifact — not the planning conversation history. Implementation does not begin without a written plan artifact."
  governance: "Owner: Any skill, agent definition, or CLAUDE.md section that specifies multi-phase workflows. The rule must be explicitly stated in those prompt layers — 'end the planning session and write a plan artifact before starting the implementation session.' Skills that orchestrate plan→implement sequences declare compliance with this rule. Audit: check that plan artifacts exist in the designated artifact directory before implementation sessions run."
  recovery: "If implementation is begun in the same session as planning → halt; write the current plan state to a file artifact; end the session; start a fresh implementation session reading from the artifact. If the plan artifact is incomplete or ambiguous → return to a planning session to complete it before resuming implementation. If the implementation session deviates from the plan → treat deviation as a signal to update the plan artifact, not to continue ad hoc."
tags:
  - "extracted-artifact"
  - "rule"
  - "session-management"
  - "planning-bias"
  - "agent-design"
---

# Separate Planning and Implementation Sessions

**Source:** [[planning-session-bias-separate-context-windows]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent workflow contains both a planning phase and an implementation phase — the agent is about to transition from generating a plan to executing against it. This transition is taking place within the same session context.

Scope of application: any workflow where an agent produces a plan or specification and then executes on it. Single-task instructions with no internal plan-then-execute structure are exempt.

## Action

**Required:** End the planning session after writing the plan to a persistent file artifact. Start a fresh implementation session that reads only the plan file. The plan artifact is the sole bridge between sessions — not conversation history, not inline summaries.

**Forbidden:** Beginning implementation in the same session as planning without an intervening session boundary. Passing planning context to the implementation session via conversation continuation rather than a file artifact. Treating the planning conversation itself as the spec.

## Boundary

Enforced at the transition between the planning phase and the implementation phase. The rule fires when:
- a plan has been produced, and
- implementation is about to begin.

The rule does not apply to single-instruction tasks, exploratory sessions without a defined plan→implement structure, or retrospective reviews of completed work.

## Enforcement

- **Mechanism:** The planning session must produce a named plan artifact in a designated directory before the session ends. Downstream implementation sessions reference the artifact path, not conversation context.
- **Check (deterministic):** `(plan_artifact_written == true) AND (implementation_session_is_fresh == true) AND (implementation_reads_artifact == true)`. Any branch false → violation.
- **Violation response:**
  - *Implementation started in planning session:* halt implementation; write plan artifact; start fresh session.
  - *Plan artifact missing:* do not start implementation; complete the plan artifact first.
  - *Implementation session reads conversation history instead of artifact:* restart with artifact-only context.
- **Cannot be self-certified:** Preferably enforced by harness-level session boundaries (separate nodes in a workflow graph, separate Claude Code sessions) rather than in-session instruction following.

## Rationale

Running planning and implementation in the same session causes planning bias: the agent becomes anchored to its own earlier reasoning and defends its decisions rather than executing cleanly against a spec. This is distinct from general context-length degradation — the bias occurs even in short sessions because the agent has generated the plan and is not neutral about it.

The practitioner origin (Archon): planning nodes produce an artifact to the `artifact_dir`; implementation nodes start fresh sessions that read the artifact via their prompt. Boris Cherny's Explore → Plan → Implement → Commit workflow encodes the same phase separation. GStack's three-stage pipeline (Office Hours, Spec Team, Auto-Plan — ~600k tokens across three separate sessions) demonstrates the principle scaling to complex brownfield feature work.

A fresh session reads the plan document neutrally. The plan becomes a specification rather than a continuation of conversation. The separation produces cleaner implementation against a stable contract.

## Failure Modes

- **Incomplete plan artifact.** If the plan is thin or ambiguous, the fresh implementation session has worse context than a biased single session. Mitigation: the plan artifact must include acceptance criteria and enough detail for implementation without returning to the planning session.
- **Plan quality bottleneck.** Garbage plan → garbage implementation with no self-correction capability. Mitigation: treat plan artifact quality as a first-class deliverable; use explicit plan templates.
- **Session overhead avoidance.** The friction of creating worktrees, writing artifacts, and starting fresh sessions causes teams to skip the separation. Mitigation: automate artifact writing as the last step of every planning session; make session start lightweight.
- **Plan artifact stale before implementation ends.** If implementation discovers plan errors, the plan artifact needs to be updated — not silently overridden. Mitigation: treat plan→artifact updates as explicit versioned edits, not silent deviation.

## Contract

### Preconditions
An agent workflow contains a planning phase that produces a specification or plan, and a subsequent implementation phase that executes against it. The planning phase has produced a plan document or artifact.

### Invariants
The planning session ends before implementation begins. The plan is written to a persistent file artifact before the implementation session starts. The implementation session reads only the plan artifact — not the planning conversation history. Implementation does not begin without a written plan artifact.

### Governance
Owner: Any skill, agent definition, or CLAUDE.md section that specifies multi-phase workflows. The rule must be explicitly stated in those prompt layers — "end the planning session and write a plan artifact before starting the implementation session." Skills that orchestrate plan→implement sequences declare compliance with this rule. Audit: check that plan artifacts exist in the designated artifact directory before implementation sessions run.

### Recovery
If implementation is begun in the same session as planning → halt; write the current plan state to a file artifact; end the session; start a fresh implementation session reading from the artifact. If the plan artifact is incomplete or ambiguous → return to a planning session to complete it before resuming implementation. If the implementation session deviates from the plan → treat deviation as a signal to update the plan artifact, not to continue ad hoc.
