---
title: "Artifact Identification Report"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-04-19"
scope: "6 named P1 findings (test batch — validation against calibration set)"
findings_scanned: 6
findings_filtered: 0
---

# Artifact Identification Report — 2026-04-19

**Scope:** 6 named P1 findings (test batch — validation against session 22 calibration set)
**Findings scanned:** 6 | **Filtered out:** 0 (dedup: 0, weak: 0, adopted: 0)
**Classified:** 6

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | 3 | 50% | 3 | 0 | 0 |
| rule | 1 | 17% | 1 | 0 | 0 |
| template | 1 | 17% | 1 | 0 | 0 |
| skill | 1 | 17% | 1 | 0 | 0 |
| agent | 0 | 0% | 0 | 0 | 0 |

## Calibration Comparison

This test batch included findings with known classifications from the session 22 calibration set. Sonnet matched 4/6 (67%). Two disagreements noted below with calibration rationale.

| Finding | Sonnet | Calibration | Match |
|---|---|---|---|
| tech-stack-pinning-table | template | template | Yes |
| poka-yoke | pattern (rule co-occ) | pattern (rule co-occ) | Yes |
| effort-scaling-rules | rule | pattern | **DISAGREE** |
| think-tool-scratchpad | skill | pattern | **DISAGREE** |
| ground-truth-feedback | pattern | pattern | Yes |
| file-based-task-locking | pattern (skill co-occ) | pattern | Yes |

**Disagreement analysis:**
- `effort-scaling-rules`: Sonnet read the three tiers as deterministic allocation constraints (rule). Calibration classified as pattern because the "rules" are heuristics with tradeoffs (static rules may under-allocate, need periodic recalibration). The center of gravity is the design approach of embedding scaling guidance, not the specific tier numbers.
- `think-tool-scratchpad`: Sonnet read the tool definition and invocation pattern as a skill (defined input, explicit invocation, stateless). Calibration classified as pattern because the insight is the reusable shape ("reserve an ephemeral scratchpad as a distinct tool") with instances that vary across domains. The tool spec is an instantiation, not the finding's center of gravity.

## Candidates

### AUTO — Ready for Extraction

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 1 | [[tech-stack-pinning-table-for-drift-prevention]] | template | HIGH | rule | PENDING |
| 2 | [[poka-yoke-error-proof-tool-interfaces]] | pattern | HIGH | rule | PENDING |
| 3 | [[effort-scaling-rules-embedded-in-orchestrator]] | rule | HIGH | template | PENDING |
| 4 | [[think-tool-scratchpad-for-mid-chain-reasoning]] | skill | HIGH | — | PENDING |
| 5 | [[ground-truth-environmental-feedback-loops]] | pattern | HIGH | — | PENDING |
| 6 | [[file-based-task-locking-parallel-agents]] | pattern | HIGH | skill | PENDING |

## Details

### 1. tech-stack-pinning-table-for-drift-prevention

- **Assigned form:** template
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** explicit-scaffold, named-variables, repeatable-generation, build-artifact
- **Co-occurrence:** rule (constraint: use pinned versions)
- **Rationale:** The finding describes a concrete scaffold (a table with named variables: technology name, version number) that the Architect agent generates and the dev agent consumes via a load-always-files config. The output is a governance artifact loaded per execution — repeatable generation with a fillable backbone. Rule is excluded because the constraint is enforced via the artifact structure, not a binary pass/fail check at a named boundary. Skill is excluded because there are no ordered steps — the focus is on the scaffold shape.
- **Calibration match:** Yes (template, row 21)
- **Status:** PENDING

### 2. poka-yoke-error-proof-tool-interfaces

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** recurring-problem, competing-forces, design-approach, composable, no-ordered-steps
- **Co-occurrence:** rule (specific invariants like "absolute filepath" are downstream rules)
- **Rationale:** Frames a recurring design problem (tool errors from ambiguous arguments) with explicit competing forces: usability vs. correctness. The insight is a design philosophy ("make errors structurally impossible") applicable across any tool interface, not a single deterministic boundary check. Multiple instantiations possible.
- **Calibration match:** Yes (pattern with rule co-occurrence, row 13)
- **Status:** PENDING

### 3. effort-scaling-rules-embedded-in-orchestrator

- **Assigned form:** rule
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** must-language, deterministic-check, named-boundary, binary-pass-fail, no-cognitive-disposition
- **Co-occurrence:** template (the tiered table could be a scaffold)
- **Rationale:** Sonnet read the three tiers as deterministic allocation constraints embedded in the orchestrator prompt. Each tier is a check against query complexity — the orchestrator either complies or doesn't.
- **Calibration note:** Calibration classified as **pattern** (row 7). Reasoning: "rules" in name are heuristics, not binary constraints. No enforcement boundary. The center of gravity is the design approach of embedding scaling guidance with tradeoffs (static rules may under-allocate, need recalibration).
- **Status:** PENDING

### 4. think-tool-scratchpad-for-mid-chain-reasoning

- **Assigned form:** skill
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** explicit-invocation, defined-inputs-outputs, ordered-steps, stateless-per-run, no-side-effects
- **Co-occurrence:** —
- **Rationale:** Sonnet read the think tool as explicitly invoked between other tool calls, taking a single thought string as input, stateless per invocation, with a clear procedural role in a tool chain.
- **Calibration note:** Calibration classified as **pattern** (anchor row 1). Reasoning: the insight is the reusable shape ("reserve an ephemeral scratchpad as a distinct tool") with instances that vary across domains. The tool spec is an instantiation of the pattern, not the pattern itself.
- **Status:** PENDING

### 5. ground-truth-environmental-feedback-loops

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** recurring-problem, competing-forces, design-approach, composable, multiple-instantiations
- **Co-occurrence:** —
- **Rationale:** Addresses a recurring architectural problem (self-assessment vs. environmental ground truth) with explicit tradeoffs: autonomy vs. accuracy. The solution shape is composable across agent designs. Not a binary check (judgment required for which feedback sources are relevant).
- **Calibration match:** Yes (pattern, row 14)
- **Status:** PENDING

### 6. file-based-task-locking-parallel-agents

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** recurring-problem, competing-forces, composable, multiple-instantiations, design-approach
- **Co-occurrence:** skill (the per-agent workflow: acquire, pull, work, push, release)
- **Rationale:** Addresses coordination in parallel agent systems. The insight is the structural design choice (filesystem coordination over orchestration), not the ordered procedure. Specific paths, container counts, and task selection are project-specific instantiations.
- **Calibration match:** Yes (pattern, row 17)
- **Status:** PENDING
