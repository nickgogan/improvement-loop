---
title: "Agentic Harness Self-Assessment Skill (Design + Evaluation Modes)"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "agentic-harness-self-assessment-skill"
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic coding systems undergoing harness design or architecture review"
    - "teams assessing whether their agent harness covers foundational primitives"
    - "greenfield agent builders selecting a minimum viable primitive set"
  platform_coupling: "specific:claude-code"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "trivial — skill invocation produces a report or recommendation; no system state is modified"
  auditability: "medium — assessment output is human-readable and cites specific primitives; quality depends on codebase read coverage"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "For Design Mode: agent description is sufficiently concrete. For Evaluation Mode: codebase is accessible and readable; the 12-primitive framework definition is available as reference."
  invariants: "Single-agent architecture is the default recommendation unless explicit justification for orchestration. Every finding in Evaluation Mode is accompanied by a concrete remediation and a confirmatory test specification."
  governance: "Owner: MetaSystem / Claude Build system. Skill sourced from Nate B Jones (external); internal adaptation requires a DD if the primitive framework or assessment dimensions change."
  recovery: "If the codebase is unreadable: halt Evaluation Mode, return a partial findings report with explicit incompleteness flag. If simplicity bias conflicts with stated requirements: present both the lean recommendation and an alternative."
tags:
  - "extracted-artifact"
  - "skill"
---

# Agentic Harness Self-Assessment Skill (Design + Evaluation Modes)

**Source:** [[agentic-harness-self-assessment-skill]]
**Form:** skill
**Extraction date:** 2026-04-19

## Purpose

A Claude Code skill that operationalizes the 12-primitive framework from the Claude Code leak into an interactive assessment tool. Two modes: Design Mode for greenfield harness design; Evaluation Mode for auditing an existing harness codebase. Biased toward lean, solo-maintainable architecture; resists premature multi-agent orchestration.

## Inputs

**Design Mode:**
- Natural language description of the agent to be built
- Constraints: team size, maintenance capacity, operational environment
- (Optional) Existing partial design or requirements document

**Evaluation Mode:**
- Path to the harness codebase under assessment
- Read access to all relevant source files
- (Optional) Scope filter: specific dimensions or primitives to evaluate

## Outputs

**Design Mode:**
- Recommended harness architecture shape
- Minimum useful primitive set for the described agent
- Phased implementation sequence
- Verification criteria for each implementation phase

**Evaluation Mode:**
- Findings ordered by severity across all assessed dimensions
- Architecture completeness score per dimension
- Safety and permissions coverage assessment
- Prioritized upgrade path
- Test specifications that confirm each fix works

## Steps

**Design Mode**

1. **Intake.** Receive agent description and constraints. Identify the agent's primary task, expected autonomy level, and operational environment.
2. **Architecture shape recommendation.** Based on the 12-primitive framework, recommend a harness shape. Default to single-agent unless compelling justification for complexity.
3. **Primitive selection.** Identify the minimum useful set of primitives for this agent.
4. **Phased implementation plan.** Sequence primitives into phases ordered by foundational dependency and risk reduction.
5. **Verification criteria.** For each phase, define explicit criteria that confirm the phase is complete and correct.

**Evaluation Mode**

1. **Codebase intake.** Read the harness codebase. Identify the architecture shape in use. Map observable implementation to the 12-primitive framework.
2. **Dimension assessment.** Evaluate each dimension: architecture completeness, safety and permissions, state and durability, error handling, observability, and extensibility.
3. **Finding classification.** Classify each gap or weakness by severity: critical (blocks safe operation), major (degrades reliability or safety), minor (improvement opportunity).
4. **Upgrade path.** Order findings by severity. For each finding, specify the concrete remediation and the test that confirms the fix.
5. **Output assembly.** Produce the prioritized findings report and test specification list.

## Failure Modes

- **Opinionated bias conflicts with legitimate complexity.** The skill biases toward simplicity. Genuinely complex requirements may be underserved.
- **Interpretation dependency.** Recommendations reflect one analyst's interpretation, not official Anthropic guidance.
- **Codebase readability limits.** Evaluation Mode quality is bounded by ability to read and understand the harness.
- **Primitive framework drift.** The 12-primitive framework is sourced from a leaked document; it may not reflect current Anthropic internal architecture.

## Contract

### Preconditions
For Design Mode: agent description is sufficiently concrete. For Evaluation Mode: codebase is accessible and readable; the 12-primitive framework definition is available as reference.

### Invariants
Single-agent architecture is the default recommendation unless explicit justification for orchestration. Every finding in Evaluation Mode is accompanied by a concrete remediation and a confirmatory test specification.

### Governance
Owner: MetaSystem / Claude Build system. Skill sourced from Nate B Jones (external); internal adaptation requires a DD if the primitive framework or assessment dimensions change.

### Recovery
If the codebase is unreadable: halt Evaluation Mode, return a partial findings report with explicit incompleteness flag. If simplicity bias conflicts with stated requirements: present both the lean recommendation and an alternative.
