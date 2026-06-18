---
title: "Artifact Identification Report"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-05-24"
scope: "P1 + P2 findings from sessions 89-90 (19 findings)"
findings_scanned: 19
findings_filtered: 0
---

# Artifact Identification Report — 2026-05-24

**Scope:** P1 + P2 findings from sessions 89-90 (6 P1 + 13 P2)
**Findings scanned:** 19 | **Filtered out:** 0 (dedup: 0, weak: 0, adopted: 0)
**Classified:** 19

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | 14 | 73.7% | 12 | 2 | 0 |
| rule | 3 | 15.8% | 2 | 1 | 0 |
| skill | 2 | 10.5% | 1 | 1 | 0 |
| template | 0 | 0% | 0 | 0 | 0 |
| agent | 0 | 0% | 0 | 0 | 0 |

**Curator priority revisions:** None proposed. All Researcher-assigned priorities hold under KB-wide review.

**Guide routing:** 14 pattern findings mapped to guide clusters, 0 unrouted.

**DD-98 observations:**
- G2 (Managing Agent Context) at 44+ findings (4 new patterns this session); above count threshold. Covers ≥2 practitioner questions ("How do I prevent context degradation?" vs "How do I optimize context cost/structure?"). Both thresholds met — split proposal warranted on next `/synthesize-guide` run when G2 is re-synthesized. Deferred from this session because G2 was not re-synthesized this cycle.
- G11 (Building Agentic Systems) at 29+ findings (1 new pattern this session); above count threshold. Already flagged in PROGRESS.md logged-for-future. Monitor on next re-synthesis.
- G4 (Building Agent Evaluation Suites) at 32 findings; remains single-question ("How do I verify my agent actually works?"). Monitor for question bifurcation.
- G7 (Session Persistence and Memory) at 27 findings; touches 2 practitioner questions ("How do I persist session state?" vs "How do I implement scalable agent memory?") but both conditions were already met at last synthesis. Monitor on next re-synthesis.

**DD-99 observations:** Unrouted bucket remains empty. No graduation trigger.

## Candidates

### GUIDED — Review Recommended

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 1 | [[runtime-self-modification-via-extension-api]] | pattern | MED | — | APPROVED |
| 9 | [[supply-chain-hardening-for-agent-packages]] | skill | MED | — | APPROVED |
| 16 | [[agui-human-control-layer-not-ui]] | pattern | MED | — | APPROVED |
| 18 | [[context-degradation-40-50-percent-threshold]] | rule | MED | — | APPROVED |

### AUTO — Ready for Extraction

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 2 | [[core-specialized-skill-inheritance-pattern]] | pattern | HIGH | — | APPROVED |
| 3 | [[screen-as-permissions-model-agent-bypass-failure]] | rule | HIGH | — | APPROVED |
| 4 | [[mcp-tool-description-prompt-injection-attack]] | rule | HIGH | — | APPROVED |
| 5 | [[auxiliary-model-slot-architecture]] | pattern | HIGH | — | APPROVED |
| 6 | [[bounded-tiered-memory-inference-driven-curation]] | pattern | HIGH | — | APPROVED |
| 7 | [[session-tree-as-first-class-abstraction]] | pattern | HIGH | — | APPROVED |
| 8 | [[tool-call-event-interception-pattern]] | pattern | HIGH | — | APPROVED |
| 10 | [[skills-lock-portable-agent-skills]] | pattern | HIGH | — | APPROVED |
| 11 | [[feature-flag-lifecycle-deployment-governance]] | skill | HIGH | — | APPROVED |
| 12 | [[oz-multi-agent-room-model]] | pattern | HIGH | — | APPROVED |
| 13 | [[write-time-vs-query-time-synthesis-kb-poisoning]] | pattern | HIGH | — | APPROVED |
| 14 | [[orchestrator-headless-dispatch-context-isolation]] | pattern | HIGH | — | APPROVED |
| 15 | [[five-layer-recursive-ai-loop-architecture]] | pattern | HIGH | — | APPROVED |
| 17 | [[two-layer-plugin-model-tools-vs-capabilities]] | pattern | HIGH | — | APPROVED |
| 19 | [[layered-prompt-assembly-stable-segment-caching]] | pattern | HIGH | — | APPROVED |

## Details

### 1. runtime-self-modification-via-extension-api

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** reusable-shape, surface-trap-mechanism-is-example, no-ordered-steps, no-single-role
- **Co-occurrence:** —
- **Rationale:** Center of gravity is the architectural shape "expose a typed extension API so the agent can register capabilities at runtime," not the specific Pi harness implementation. The mechanisms (jiti, TypeScript modules, 30+ events) are evidence of the shape. MED confidence because the shape is clear but single-source (Pi harness only) and the boundary between pattern and template (for an extension API schema) is slightly ambiguous.
- **Status:** PENDING
- **Guide cluster:** G10 (Agent Design Patterns)

### 2. core-specialized-skill-inheritance-pattern

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable-shape, explicit-forces-tradeoffs, multiple-known-uses, no-ordered-steps, no-single-role
- **Co-occurrence:** —
- **Rationale:** The insight is a compositional shape: two-layer inheritance where shared logic lives in core skills and per-repo customization is scoped to declared-overridable slots. Finding explicitly names competing forces (portability vs customization). No ordered procedure, no binary constraint, no single role. Strong production evidence from Warp.
- **Status:** PENDING
- **Guide cluster:** G10 (Agent Design Patterns)

### 3. screen-as-permissions-model-agent-bypass-failure

- **Assigned form:** rule
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** binary-constraint, boundary-enforced, deterministic-check, no-judgment-required, anti-pattern-natural-rule
- **Co-occurrence:** —
- **Rationale:** Binary invariant: APIs MUST NOT treat UI screen traversal as an implicit permissions boundary when agents may call them programmatically. Deterministic check at API design/deploy boundary — no cognitive judgment needed to verify endpoint authentication. The Lilly/McKinsey incident is evidence, not the shape; the constraint is the insight.
- **Status:** PENDING

### 4. mcp-tool-description-prompt-injection-attack

- **Assigned form:** rule
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** binary-constraint, boundary-enforced, deterministic-check, anti-pattern-natural-rule, no-procedure-required
- **Co-occurrence:** —
- **Rationale:** Hard constraint: tool descriptions exposed via MCP MUST be treated as untrusted input and gated with scopes, approval flows, and audit trails. Deterministic check at the tool-call boundary. The four required mitigations are enforcement mechanisms, not a procedure.
- **Status:** PENDING

### 5. auxiliary-model-slot-architecture

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable-shape, explicit-forces-tradeoffs, no-ordered-steps, no-single-role, surface-trap-mechanism-is-example
- **Co-occurrence:** —
- **Rationale:** Design approach: declare named model slots in config so different task types route to appropriately-priced models. The YAML schema and specific slot names are instantiation examples. Explicitly names the quality-vs-cost force. Excluded as template (insight is the routing philosophy, not a fillable scaffold).
- **Status:** PENDING
- **Guide cluster:** G10 (Agent Design Patterns)

### 6. bounded-tiered-memory-inference-driven-curation

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable-shape, explicit-forces-tradeoffs, no-ordered-steps, no-single-role, surface-trap-mechanism-is-example
- **Co-occurrence:** —
- **Rationale:** Architectural shape: tiered memory with hard ceilings, inference-driven writes, and curator eviction. Any agent system could adopt this without MEMORY.md, USER.md, or SQLite FTS5 specifically. The three innovations describe design forces and resolutions, not a procedure.
- **Status:** PENDING
- **Guide cluster:** G2 (Managing Agent Context)

### 7. session-tree-as-first-class-abstraction

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable-shape, explicit-forces-tradeoffs, no-ordered-steps, no-single-role
- **Co-occurrence:** —
- **Rationale:** Structural shape: model sessions as a tree rather than linear transcript, enabling branching, compaction, and navigation. The git analogy confirms the "it depends" character. Forces (linear history degrades context; tree preserves optionality) are explicit and the shape transfers to any session management system.
- **Status:** PENDING
- **Guide cluster:** G2 (Managing Agent Context)

### 8. tool-call-event-interception-pattern

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable-shape, composable, tradeoffs-present, surface-structure-trap
- **Co-occurrence:** —
- **Rationale:** Reusable architectural shape — an interception point in a pipeline where handlers chain, mutate, and block — not a specific procedure or binary constraint. The mechanism (tool_call event, mutable event.input) is an example of the broader interception pattern. Tradeoffs (no re-validation after mutation, composability, bidirectionality) confirm pattern-level abstraction.
- **Status:** PENDING
- **Guide cluster:** G5 (Designing Agent Tools)

### 9. supply-chain-hardening-for-agent-packages

- **Assigned form:** skill
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** ordered-steps, explicit-inputs-outputs, stateless-per-run, failure-modes-present
- **Co-occurrence:** —
- **Rationale:** Describes a concrete, ordered set of practices (pin versions, set min-release-age, generate shrinkwrap, add lockfile guard, disable lifecycle scripts, run verification) with defined inputs (dependency manifest) and outputs (hardened lockfile state). The mechanism IS the insight, not an example. MED confidence because the steps have some policy/judgment flavor rather than being purely mechanical.
- **Status:** PENDING

### 10. skills-lock-portable-agent-skills

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable-shape, composable, multiple-known-uses, surface-structure-trap
- **Co-occurrence:** —
- **Rationale:** Design approach of applying dependency-management semantics (lock file, version pinning, conflict detection, reproducible installs) to agent skills — a transferable shape applicable beyond Warp's specific implementation. Someone can apply this with entirely different tooling, confirming pattern over skill or rule.
- **Status:** PENDING
- **Guide cluster:** G5 (Designing Agent Tools)

### 11. feature-flag-lifecycle-deployment-governance

- **Assigned form:** skill
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** ordered-steps, explicit-inputs-outputs, stateless-per-run, failure-modes-present
- **Co-occurrence:** —
- **Rationale:** Explicitly a 5-stage promotion lifecycle with defined file-change recipes per stage, validation steps, and follow-up actions — ordered steps with inputs (current flag stage) and outputs (promoted flag state). The body directly describes this as a "recipe-style skill definition." The stages are deterministic transitions, not heuristic tradeoffs.
- **Status:** PENDING

### 12. oz-multi-agent-room-model

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable-shape, multi-role-system, tradeoffs-present, dd76-role-count
- **Co-occurrence:** —
- **Rationale:** Multi-agent coordination architecture — rooms as bounded contexts, @mention communication, per-room kanban, typed artifacts. Involves multiple roles (human observers, configurable agents, room scope). DD-76 biases role count > 1 toward pattern. The insight is the architectural shape (room as coordination boundary).
- **Status:** PENDING
- **Guide cluster:** G3 (Agent Architecture Decisions)

### 13. write-time-vs-query-time-synthesis-kb-poisoning

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** tradeoffs-present, reusable-shape, competing-forces, answers-how-to-structure
- **Co-occurrence:** —
- **Rationale:** Classic pattern structure: competing forces between write-time synthesis (speed, amortized cost, poisoning risk) and query-time synthesis (chain of custody, freshness, higher per-query cost). Context-dependent resolution, consequences enumerated on both sides. The specific KB poisoning mechanism is evidence, not the center of gravity.
- **Status:** PENDING
- **Guide cluster:** G2 (Managing Agent Context)

### 14. orchestrator-headless-dispatch-context-isolation

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** shape-not-steps, tradeoffs-present, composable, multiple-uses
- **Co-occurrence:** —
- **Rationale:** Structural arrangement — thin orchestrator plus isolated headless subprocesses — answering "how should I structure long-running autonomous workflows?" The mechanism (claude -p subprocess) is an example; the reusable shape is context isolation via process boundary. Explicit tradeoffs (coordination state vs work context accumulation).
- **Status:** PENDING
- **Guide cluster:** G2 (Managing Agent Context)

### 15. five-layer-recursive-ai-loop-architecture

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** shape-not-steps, tradeoffs-present, composable, multiple-uses
- **Co-occurrence:** —
- **Rationale:** Five layers define an architectural shape for self-improving systems, not an ordered procedure with defined I/O. Each layer is a composable design element with consequences for omission. The insight is the structural relationship between layers. YC evidence demonstrates real-world application.
- **Status:** PENDING
- **Guide cluster:** G11 (Building Agentic Systems)

### 16. agui-human-control-layer-not-ui

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** shape-not-steps, tradeoffs-present, mechanism-as-example
- **Co-occurrence:** —
- **Rationale:** Design principle — encode human control points explicitly in agentic systems rather than treating them as a UI concern — with AGUI as one instantiation. The "supervision debt" framing signals competing forces. MED confidence because grounded in a single named protocol rather than multiple independent uses.
- **Status:** PENDING
- **Guide cluster:** G3 (Agent Architecture Decisions)

### 17. two-layer-plugin-model-tools-vs-capabilities

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** shape-not-steps, tradeoffs-present, composable, mechanism-as-example
- **Co-occurrence:** —
- **Rationale:** Answers "how should I structure agent extensions?" by distinguishing LLM-directed (tools) from system-directed (capabilities) invocation. The named stages and ChatOrchestrator are examples instantiating the broader shape. Tradeoffs around observability, error handling, and cost estimation are explicit.
- **Status:** PENDING
- **Guide cluster:** G10 (Agent Design Patterns)

### 18. context-degradation-40-50-percent-threshold

- **Assigned form:** rule
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** binary-constraint, enforcement-boundary, deterministic-check
- **Co-occurrence:** —
- **Rationale:** Subagent classified as rule — the actionable core is a boundary constraint: treat 40% context utilization as the planning ceiling. **Curator note:** this may be a Trap 1 case ("rules that are actually heuristics"). The threshold is a practitioner observation, not a controlled measurement. Task-dependent degradation makes the check non-deterministic. Consider redirecting to pattern if the heuristic framing is stronger than the constraint framing.
- **Status:** PENDING

### 19. layered-prompt-assembly-stable-segment-caching

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** shape-not-steps, tradeoffs-present, composable, multiple-uses
- **Co-occurrence:** —
- **Rationale:** Compositional architecture — ordered prompt layers with a stable/ephemeral boundary aligned to cache control markers. The insight is decoupling the caching boundary from the prompt structure boundary. The specific modules (prompt_caching.py) are examples; the shape applies with any provider caching mechanism. Explicit tradeoffs (cost/latency vs cache invalidation risk).
- **Status:** PENDING
- **Guide cluster:** G8 (Model-Resilient Prompt Engineering)
