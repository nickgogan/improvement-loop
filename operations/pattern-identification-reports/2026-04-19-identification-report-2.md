---
title: "Artifact Identification Report"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-04-19"
scope: "6 named P1 findings (test batch — re-validation after subagent prompt improvement)"
findings_scanned: 6
findings_filtered: 0
---

# Artifact Identification Report — 2026-04-19 (Run 2)

**Scope:** 6 named P1 findings (test batch — re-validation after subagent prompt improvement, session 24)
**Findings scanned:** 6 | **Filtered out:** 0 (dedup: 0, weak: 0, adopted: 0)
**Classified:** 6

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | 5 | 83% | 4 | 1 | 0 |
| rule | 0 | 0% | 0 | 0 | 0 |
| template | 1 | 17% | 1 | 0 | 0 |
| skill | 0 | 0% | 0 | 0 | 0 |
| agent | 0 | 0% | 0 | 0 | 0 |

## Calibration Comparison

Sonnet subagent prompt was improved in this session (center-of-gravity test, mandatory classification procedure, worked trap examples, self-check). Re-run of the same 6-finding test batch. **6/6 match (100%), up from 4/6 (67%).**

| Finding | Sonnet (Run 2) | Calibration | Match | Prev Run |
|---|---|---|---|---|
| tech-stack-pinning-table | template | template | YES | YES |
| poka-yoke | pattern (rule co-occ) | pattern (rule co-occ) | YES | YES |
| effort-scaling-rules | pattern (rule co-occ) | pattern | **YES (FIXED)** | DISAGREE |
| think-tool-scratchpad | pattern (skill co-occ) | pattern | **YES (FIXED)** | DISAGREE |
| ground-truth-feedback | pattern | pattern | YES | YES |
| file-based-task-locking | pattern (skill co-occ) | pattern | YES | YES |

**Fix analysis:**
- `effort-scaling-rules`: Sonnet correctly identified tiers as heuristics with tradeoffs, not binary constraints. Cited Trap 1. Assigned MED/guided (reasonable — rule co-occurrence is genuine). Previously classified as rule/HIGH/auto.
- `think-tool-scratchpad`: Sonnet correctly identified tool spec as instantiation of broader shape. Cited Trap 2 and the rubric's prior-session exemplar. Assigned pattern/HIGH/auto with skill co-occurrence. Previously classified as skill/HIGH/auto.

## Candidates

### GUIDED — Review Recommended

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 1 | [[effort-scaling-rules-embedded-in-orchestrator]] | pattern | MED | rule | PENDING |

### AUTO — Ready for Extraction

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 2 | [[tech-stack-pinning-table-for-drift-prevention]] | template | HIGH | rule | PENDING |
| 3 | [[poka-yoke-error-proof-tool-interfaces]] | pattern | HIGH | rule | PENDING |
| 4 | [[think-tool-scratchpad-for-mid-chain-reasoning]] | pattern | HIGH | skill | PENDING |
| 5 | [[ground-truth-environmental-feedback-loops]] | pattern | HIGH | — | PENDING |
| 6 | [[file-based-task-locking-parallel-agents]] | pattern | HIGH | skill | PENDING |

## Details

### 1. effort-scaling-rules-embedded-in-orchestrator

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** design-approach, mechanism-as-example, trap-1-heuristic-not-rule, tradeoffs-implied
- **Co-occurrence:** rule
- **Rationale:** The center of gravity is the design approach of embedding scaling guidance directly in the lead agent prompt to transform naive orchestration into intelligent resource allocation. The three-tier table with specific subagent and call counts is an instantiation (Anthropic's specific calibration), not the insight itself — someone could apply this finding's core insight with entirely different tier boundaries. Per Trap 1, tiers with threshold numbers look like rules but function as heuristics requiring periodic recalibration. Exclusion: not a rule because the tiers are not a deterministic binary check at a named enforcement boundary and require contextual judgment to apply.
- **Calibration match:** YES (FIXED — previously classified as rule)
- **Status:** PENDING

### 2. tech-stack-pinning-table-for-drift-prevention

- **Assigned form:** template
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** explicit-scaffold, named-variables, repeatable-generation, build-artifact
- **Co-occurrence:** rule (constraint: use pinned versions)
- **Rationale:** The center of gravity is the pinning table itself — a structural backbone with named slots (technology, version number) that gets generated once and loaded on every dev agent execution. The insight is not 'how to think about drift prevention' (pattern) but the specific fillable scaffold that enforces it. Exclusion: not a pattern because the insight is the pre-filled structure with variables, not a design philosophy; not a rule because the table is not itself a binary pass/fail check at a boundary.
- **Calibration match:** YES (template, row 21)
- **Status:** PENDING

### 3. poka-yoke-error-proof-tool-interfaces

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, tradeoffs-present, multiple-instantiations, it-depends-character
- **Co-occurrence:** rule (specific invariants like "absolute filepath" are downstream rules)
- **Rationale:** The center of gravity is the reusable design approach: restructure tool interfaces so errors are structurally impossible rather than instruction-prevented. The SWE-bench absolute filepath example is one instantiation of a broader shape applicable across any tool interface design decision. Explicit tradeoffs (over-constraining reduces flexibility). Exclusion: not a rule because no single deterministic binary check at a named boundary is specified — the insight is the design philosophy.
- **Calibration match:** YES (pattern with rule co-occurrence, row 13)
- **Status:** PENDING

### 4. think-tool-scratchpad-for-mid-chain-reasoning

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, mechanism-as-instantiation, prior-session-exemplar, trap-2-tool-spec
- **Co-occurrence:** skill
- **Rationale:** Per the rubric exemplar and Trap 2: the think tool spec (single `thought` parameter, no side effects) is an instantiation of the reusable shape 'reserve an ephemeral scratchpad as a distinct tool.' The core insight — distinct from extended thinking, activates mid-chain on new information, requires domain-specific prompting — is a design approach applicable across domains with different implementations. Exclusion: not a skill because the tool spec is an example of the shape, not the shape itself.
- **Calibration match:** YES (FIXED — previously classified as skill)
- **Status:** PENDING

### 5. ground-truth-environmental-feedback-loops

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, tradeoffs-present, it-depends-character, no-ordered-procedure
- **Co-occurrence:** —
- **Rationale:** The center of gravity is the design approach: agents must anchor decision-making to concrete environmental feedback rather than self-assessment, because LLMs confabulate about their own progress. Explicit tradeoffs: over-reliance makes agents conservative; test quality becomes ceiling on agent quality. Exclusion: not a rule (no deterministic binary check at a boundary); not a skill (no ordered steps with defined I/O).
- **Calibration match:** YES (pattern, row 14)
- **Status:** PENDING

### 6. file-based-task-locking-parallel-agents

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, mechanism-as-instantiation, composable, it-depends-character
- **Co-occurrence:** skill
- **Rationale:** The center of gravity is the coordination shape: parallel agents self-select and lock tasks via shared filesystem state, eliminating orchestrators. The Docker/git/current_tasks/ implementation is one instantiation; the shape is applicable across different backends. The per-agent workflow (acquire, pull, work, push, release) is an example procedure within the pattern, not the insight. Exclusion: not a skill because the procedure is an example; not a rule because no binary pass/fail enforcement boundary.
- **Calibration match:** YES (pattern, row 17)
- **Status:** PENDING
