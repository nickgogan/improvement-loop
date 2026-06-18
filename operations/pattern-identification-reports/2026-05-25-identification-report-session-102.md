---
title: "Artifact Identification Report"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-05-25"
scope: "All unprocessed findings (no pipeline_status set), excluding Already Adopted and Weak evidence"
findings_scanned: 20
findings_filtered: 5
---

# Artifact Identification Report — 2026-05-25 (Session 102)

**Scope:** All findings without `pipeline_status` — 20 found, 5 filtered (0 dedup, 0 weak, 5 adopted)
**Classified:** 15

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | 12 | 80% | 9 | 3 | 0 |
| rule | 2 | 13% | 1 | 1 | 0 |
| template | 0 | 0% | 0 | 0 | 0 |
| skill | 1 | 7% | 1 | 0 | 0 |
| agent | 0 | 0% | 0 | 0 | 0 |

**Co-occurrences noted:** 4 (agent-state-machine: rule; cross-repo-issue-routing: skill; loop-detection: skill; semantic-memory-decay: skill)

**Curator priority review:** No revisions proposed. Researcher triage was consistent with KB-wide signal.

**Guide routing:** 12 pattern findings mapped to existing guide clusters (G2: 4, G3: 2, G6: 3, G10: 3). 0 unrouted.

**DD-98 split-trigger status:** G2 (64+ findings), G3 (42+), G9 (38+) — split proposals already at nick-gate from prior sessions. G4 (46), G10 (37), G11 (30), G7 (27) all above count threshold but remain single-question clusters. Monitor for question bifurcation on next cycle.

**DD-99 graduation-trigger status:** Unrouted bucket empty. No-op.

---

## Candidates

### GUIDED — Review Recommended

| # | Finding | Form | Confidence | Co-occurrence | Route | Status |
|---|---------|------|------------|---------------|-------|--------|
| 1 | [[agent-state-machine-with-witness-monitoring]] | pattern | MED | rule | G10 | PENDING |
| 2 | [[cross-repo-issue-routing]] | pattern | MED | skill | G3 | PENDING |
| 3 | [[loop-detection-hash-based-sliding-window]] | rule | MED | skill | G4 | PENDING |
| 4 | [[semantic-memory-decay-compaction]] | pattern | MED | skill | G2 | PENDING |

### AUTO — Ready for Extraction

| # | Finding | Form | Confidence | Co-occurrence | Route | Status |
|---|---------|------|------------|---------------|-------|--------|
| 5 | [[agent-lifecycle-formalization-spectrum]] | pattern | HIGH | — | G10 | PENDING |
| 6 | [[all-in-one-sandbox-architecture]] | pattern | HIGH | — | G6 | PENDING |
| 7 | [[database-as-shared-memory-coordination]] | pattern | HIGH | — | G3 | PENDING |
| 8 | [[hook-based-transparent-memory-injection]] | pattern | HIGH | — | G2 | PENDING |
| 9 | [[memory-decay-compaction-convergence]] | pattern | HIGH | — | G2 | PENDING |
| 10 | [[memory-field-immutability-via-merge-operations]] | rule | HIGH | — | G9 | PENDING |
| 11 | [[skill-security-scanner-fail-closed]] | skill | HIGH | — | G9 | PENDING |
| 12 | [[three-sandbox-architectures-comparison]] | pattern | HIGH | — | G6 | PENDING |
| 13 | [[three-tier-sandbox-provisioner]] | pattern | MED | overlap w/ #12 | G6 | PENDING |
| 14 | [[two-threshold-compaction-strategy]] | pattern | HIGH | — | G2 | PENDING |
| 15 | [[zero-framework-cognition-zfc]] | pattern | HIGH | — | G10 | PENDING |

---

## Details

### 1. agent-state-machine-with-witness-monitoring

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** specific-mechanism-present, shape-is-the-insight, separation-of-concerns-design-approach
- **Co-occurrence:** rule (specific constraint: agents cannot set themselves to dead — only Witness can)
- **Rationale:** Center of gravity is the reusable design shape "separate monitoring from execution so an external authority can detect terminal states the agent cannot self-report." The FSM states and Witness implementation are one instantiation; the principle applies across different mechanisms. MED confidence because the "agents cannot declare themselves dead" constraint has strong rule character.
- **Guide route:** G10 (Agent Design Patterns) via Agent Design dimension
- **Status:** PENDING

### 2. cross-repo-issue-routing

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** mechanism-as-example, design-approach-is-insight
- **Co-occurrence:** skill (hydration command is procedural)
- **Rationale:** Center of gravity is the design approach "enable work to flow across repository boundaries via explicit routing configuration." The config-file routing and hydration command are one instantiation. MED because the hydration command is procedural enough for a co-occurring skill.
- **Guide route:** G3 (Agent Architecture Decisions) via Orchestration dimension
- **Status:** PENDING

### 3. loop-detection-hash-based-sliding-window

- **Assigned form:** rule
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** deterministic-check, boundary-enforced, two-stage-enforcement, specific-thresholds
- **Co-occurrence:** skill (the two-stage warn→stop response has procedural character)
- **Rationale:** Center of gravity is a set of binary, deterministic constraints enforced at a middleware boundary: warn at 3, hard-stop at 5, cap at 50 per tool type. Each threshold is a mechanical pass/fail check. MED because the two-stage response could also be read as a skill procedure.
- **Guide route:** G4 (Building Agent Evaluation Suites) via Evaluation dimension
- **Status:** PENDING

### 4. semantic-memory-decay-compaction

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** reusable-shape, tradeoffs-explicit, no-canonical-procedure
- **Co-occurrence:** skill (scoring mechanics could be read as a procedure)
- **Rationale:** Center of gravity is the design approach — decay-weighted scoring to determine compaction survival. Applicable across storage backends and agent types. MED because the scoring mechanics (decay weights, survival thresholds) are specific enough that a practitioner could read them procedurally.
- **Guide route:** G2 (Managing Agent Context) via Context Engineering dimension
- **Status:** PENDING

### 5. agent-lifecycle-formalization-spectrum

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multi-source-convergence, shape-stable-instances-vary, it-depends-character
- **Co-occurrence:** —
- **Rationale:** Cross-repo comparison (4 repos: Beads, Paperclip, OpenClaw, DeerFlow). The shape "agent lifecycle needs explicit formalization beyond binary running/done" is confirmed across repos but each addresses a different facet. Classic pattern signal — shape converges, instances diverge.
- **Guide route:** G10 (Agent Design Patterns) via Agent Design dimension
- **Status:** PENDING

### 6. all-in-one-sandbox-architecture

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** explicit-tradeoffs, it-depends-character, design-approach-not-procedure
- **Co-occurrence:** —
- **Rationale:** Center of gravity is the tradeoff: collapse all agent-facing services into one container, trading isolation for simplicity. Explicit forces and consequences. No ordered steps, no named role, no binary constraint.
- **Guide route:** G6 (Agent Safety and Permissions) via Sandboxing dimension
- **Status:** PENDING

### 7. database-as-shared-memory-coordination

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** third-paradigm-design-approach, explicit-tradeoffs, it-depends-character
- **Co-occurrence:** —
- **Rationale:** A coordination paradigm: use a versioned database as shared memory between agents instead of message queues or direct communication. Explicit tradeoffs (ACID vs. bottleneck risk). Specific Dolt implementation is an instantiation, not the insight.
- **Guide route:** G3 (Agent Architecture Decisions) via Orchestration dimension
- **Status:** PENDING

### 8. hook-based-transparent-memory-injection

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable-shape, composable, it-depends-character
- **Co-occurrence:** —
- **Rationale:** Three-hook lifecycle shape (SessionStart→bootstrap, UserPromptSubmit→recall, Stop→capture) for transparent memory. Applicable across memory backends and agent frameworks. The insight is the architectural shape, not any specific mechanism.
- **Guide route:** G2 (Managing Agent Context) via Context Engineering dimension
- **Status:** PENDING

### 9. memory-decay-compaction-convergence

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multi-source-convergence, reusable-shape, composable, tradeoffs-explicit
- **Co-occurrence:** —
- **Rationale:** Cross-repo convergence (3 repos: OpenViking, Paperclip, DeerFlow) independently implementing semantically-aware compaction. Shape is stable (multi-strategy approach combining when/how-often/where), instantiations diverge. 9 related findings in KB.
- **Guide route:** G2 (Managing Agent Context) via Context Engineering dimension
- **Status:** PENDING

### 10. memory-field-immutability-via-merge-operations

- **Assigned form:** rule
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** deterministic-check, boundary-enforced, binary-constraint, schema-layer-enforcement
- **Co-occurrence:** —
- **Rationale:** Schema-level enforcement: each field declares its merge_op (immutable/upsert/append) and the storage layer enforces it deterministically. Binary constraint at a named boundary (storage layer). Not a design heuristic — a hard gate.
- **Guide route:** G9 (Agent Governance and Trust) via Governance dimension
- **Status:** PENDING

### 11. skill-security-scanner-fail-closed

- **Assigned form:** skill
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** ordered-steps, defined-io, explicit-invocation, stateless-per-run, failure-modes
- **Co-occurrence:** —
- **Rationale:** Concrete procedure: receive skill content → invoke LLM classifier → receive allow/warn/block → enforce outcome → log to JSONL. Defined inputs (skill file), defined outputs (classification + audit), named failure mode (model failure → block). The fail-closed default is a design decision within the procedure, not a standalone rule.
- **Guide route:** G9 (Agent Governance and Trust) via Governance dimension
- **Status:** PENDING

### 12. three-sandbox-architectures-comparison

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** recurring-problem-competing-forces, it-depends-character, multiple-known-uses
- **Co-occurrence:** —
- **Rationale:** Maps three architectures (worktree, monolithic container, graduated provisioner) to a tradeoff spectrum across complexity, isolation, and operational maturity. Cross-repo (4 repos). The insight is the comparative structure itself — someone applies this by selecting the right tier, not by following steps.
- **Guide route:** G6 (Agent Safety and Permissions) via Sandboxing dimension
- **Status:** PENDING

### 13. three-tier-sandbox-provisioner

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided (placed in auto section for proximity to #12)
- **Reason codes:** recurring-problem-competing-forces, composable, it-depends-character
- **Co-occurrence:** overlap with three-sandbox-architectures-comparison — may merge at extraction
- **Rationale:** Graduated isolation behind a unified interface. Separates "how isolated?" from "what does the agent do?" Provider-as-configuration is the insight. MED because this is a single-source instantiation of the broader three-architecture pattern; may be better subsumed into #12 at extraction.
- **Guide route:** G6 (Agent Safety and Permissions) via Sandboxing dimension
- **Status:** PENDING

### 14. two-threshold-compaction-strategy

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** recurring-problem-competing-forces, it-depends-character, tradeoffs-explicit, composable
- **Co-occurrence:** —
- **Rationale:** Two thresholds create a buffer zone between safe archival and forced compaction, solving the cliff problem. The insight is the structural relationship between thresholds, not a procedure. Threshold values vary by context size and latency budget.
- **Guide route:** G2 (Managing Agent Context) via Context Engineering dimension
- **Status:** PENDING

### 15. zero-framework-cognition-zfc

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach-philosophy, recurring-problem-competing-forces, composable
- **Co-occurrence:** —
- **Rationale:** Architectural philosophy: cognitive logic in prompts, application code as dumb plumbing. The "no hardcoded sequential logic" constraint looks rule-like on the surface but has no enforcement boundary or deterministic check — it's a design heuristic applied at architecture time.
- **Guide route:** G10 (Agent Design Patterns) via Agent Design dimension
- **Status:** PENDING

---

## Filtered (Already Adopted — skipped)

| Finding | Reason |
|---------|--------|
| agent-harness-distributed-system-mental-model | Already Adopted |
| context-before-loop-initialization-sequence | Already Adopted |
| context-first-build-sequencing-for-agentic-systems | Already Adopted |
| minimal-agent-harness-skeleton-three-primitives | Already Adopted |
| platform-native-harness-over-agent-frameworks | Already Adopted |
