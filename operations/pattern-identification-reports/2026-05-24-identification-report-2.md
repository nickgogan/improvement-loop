---
title: "Artifact Identification Report"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-05-24"
scope: "P2 raw backlog — 64 findings (1 adopted filtered)"
findings_scanned: 65
findings_filtered: 1
---

# Artifact Identification Report — 2026-05-24 (P2 Backlog)

**Scope:** All raw P2 findings (backlog clearance)
**Findings scanned:** 65 | **Filtered out:** 1 (dedup: 0, weak: 0, adopted: 1 — self-evolving-loop-pattern)
**Classified:** 64

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | 57 | 89% | 28 | 27 | 2 |
| skill | 5 | 8% | 2 | 3 | 0 |
| rule | 2 | 3% | 1 | 1 | 0 |
| template | 0 | 0% | 0 | 0 | 0 |
| agent | 0 | 0% | 0 | 0 | 0 |

**Curator priority revisions:** 2 proposed demotions (P2→P3).

**Guide routing:** 57 pattern findings mapped to guide clusters, 0 unrouted.

**DD-98 observations:** No new split triggers fired from this batch (findings not yet synthesized into guides; cluster counts unchanged until next `/synthesize-guide` run). Prior observations from report-1 still active.

**DD-99 observations:** Unrouted bucket remains empty. No graduation trigger.

**Co-occurrences noted:** 5 (template ×1, skill ×1, rule ×3).

## Candidates

### HITL — Needs Human Decision

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 61 | [[sweci-benchmark-ai-fails-at-code-maintenance]] | pattern | LOW | — | APPROVED |
| 64 | [[two-layer-ci-plus-llm-review-gate]] | pattern | LOW | rule | APPROVED |

### GUIDED — Review Recommended

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 1 | [[actor-passport-schema-bound-identity]] | pattern | MED | template | APPROVED |
| 2 | [[agent-generated-codebase-walkthrough-for-onboarding]] | skill | MED | — | APPROVED |
| 4 | [[autoplan-auto-decision-pipeline]] | pattern | MED | — | APPROVED |
| 5 | [[autoresearch-loop-autonomous-metric-driven]] | pattern | MED | skill | APPROVED |
| 8 | [[claude-code-channels-telegramdiscord-as-agent-inte]] | skill | MED | — | APPROVED |
| 10 | [[claude-code-monitor-tool-event-driven-background]] | pattern | MED | — | APPROVED |
| 11 | [[claude-dispatch-native-mobile-to-local-agent-orch]] | pattern | MED | — | APPROVED |
| 17 | [[dark-factory-ai-only-codebase-management]] | pattern | MED | — | APPROVED |
| 18 | [[data-agent-benchmark-dab-cross-dbms-pipeline-eval]] | pattern | MED | — | APPROVED |
| 19 | [[end-to-end-sequential-bug-fix-pipeline]] | skill | HIGH | — | APPROVED |
| 20 | [[event-schema-noun-verb-contract]] | rule | MED | — | APPROVED |
| 21 | [[four-layer-agent-evaluation-architecture]] | pattern | HIGH | — | APPROVED |
| 24 | [[goal-backward-verification]] | pattern | MED | — | APPROVED |
| 27 | [[gsd-get-shit-done-plugin]] | pattern | MED | — | APPROVED |
| 32 | [[intent-based-meta-routing-skill]] | pattern | MED | — | APPROVED |
| 35 | [[metaprompting-karpathy-autoresearch-for-build]] | pattern | MED | — | APPROVED |
| 36 | [[monitor-vs-loop-event-driven-vs-time-driven]] | pattern | MED | — | APPROVED |
| 40 | [[passport-object-decision-governance-binding]] | pattern | MED | — | APPROVED |
| 42 | [[playwright-cli-for-browser-automation]] | pattern | MED | — | APPROVED |
| 43 | [[policy-as-data-runtime-governance-pattern]] | pattern | MED | — | APPROVED |
| 44 | [[production-database-wipeout-agent-context]] | pattern | MED | — | APPROVED |
| 45 | [[project-specific-custom-skills-for-repeated-task]] | pattern | MED | — | APPROVED |
| 46 | [[prompt-injection-risk-from-trusted-vs-untrusted]] | pattern | MED | — | APPROVED |
| 48 | [[runtime-governance-gap-buildtime-to-production]] | pattern | MED | — | APPROVED |
| 49 | [[runtime-threshold-management-truth-conditions]] | pattern | MED | — | APPROVED |
| 51 | [[scheduled-task-dashboard-observability-layer]] | pattern | MED | — | APPROVED |
| 52 | [[self-improving-skill-lessons-log]] | pattern | MED | — | APPROVED |
| 53 | [[shell-injection-vector-taxonomy-agent-bash-security]] | pattern | MED | — | APPROVED |
| 56 | [[skills-inside-workspace-contextual-skill]] | pattern | MED | — | APPROVED |
| 57 | [[star-commands-for-explicit-output-format-override]] | pattern | MED | — | APPROVED |
| 60 | [[subagent-exploration-mode-parallel-codebase-mappi]] | pattern | MED | — | APPROVED |
| 63 | [[tool-model-io-contracts-with-preconditions]] | pattern | MED | rule | APPROVED |

### AUTO — Ready for Extraction

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 3 | [[agent-memory-architecture-multi-agent-layered]] | pattern | HIGH | — | APPROVED |
| 6 | [[bidirectional-prompting-for-spec-creation]] | pattern | HIGH | — | APPROVED |
| 7 | [[builder-validator-chain-pattern]] | pattern | HIGH | — | APPROVED |
| 9 | [[claude-code-max-plan-subsidy-vs-api-cost-tool]] | pattern | HIGH | — | APPROVED |
| 12 | [[claude-p-headless-mode-as-openclaw-replacement]] | pattern | HIGH | — | APPROVED |
| 13 | [[context-gap-task-vs-job]] | pattern | HIGH | — | APPROVED |
| 14 | [[context-order-diversity-for-bug-detection]] | pattern | HIGH | — | APPROVED |
| 15 | [[credential-isolation-bundled-auth-vault-proxy]] | pattern | HIGH | — | APPROVED |
| 16 | [[cursor-claude-code-ide-composition]] | pattern | HIGH | — | APPROVED |
| 22 | [[four-zone-agent-architecture-framework]] | pattern | HIGH | — | APPROVED |
| 23 | [[framework-tension-taxonomy-superpowers-gsd-gstack]] | pattern | HIGH | — | APPROVED |
| 25 | [[governance-ontology-semantic-foundation]] | pattern | HIGH | — | APPROVED |
| 26 | [[governed-dependency-chain-build-order]] | pattern | HIGH | — | APPROVED |
| 28 | [[harness-engineering-third-evolution]] | pattern | HIGH | — | APPROVED |
| 29 | [[headless-multi-pass-iterative-review]] | skill | HIGH | — | APPROVED |
| 30 | [[hook-based-enforcement-for-agent-outputs]] | rule | HIGH | — | APPROVED |
| 31 | [[hybrid-retrieval-pattern-semantic-lexical-graph]] | pattern | HIGH | — | APPROVED |
| 33 | [[karpathy-autoresearch-self-improvement-loop]] | pattern | HIGH | — | APPROVED |
| 34 | [[march-of-nines-compounding-reliability-math-for-m]] | pattern | HIGH | — | APPROVED |
| 37 | [[notebooklm-python-api-programmatic-access-beyond]] | pattern | HIGH | — | APPROVED |
| 38 | [[org-redesign-for-agentic-throughput-high-speed-rail]] | pattern | HIGH | — | APPROVED |
| 39 | [[parallel-claude-code-instances-per-workspace]] | pattern | HIGH | — | APPROVED |
| 41 | [[planning-session-bias-separate-context-windows]] | pattern | HIGH | — | APPROVED |
| 47 | [[ralph-wiggum-execution-pattern]] | skill | HIGH | — | APPROVED |
| 50 | [[sandbox-architecture-by-threat-model-microvm-vs-container]] | pattern | HIGH | — | APPROVED |
| 54 | [[skill-self-improvement-three-approaches]] | pattern | HIGH | — | APPROVED |
| 55 | [[skills-as-markdown-sop-files-encode-processes]] | pattern | HIGH | — | APPROVED |
| 58 | [[stop-rules-as-execution-boundaries]] | pattern | HIGH | — | APPROVED |
| 59 | [[sub-agent-context-isolation-for-parallel-complex]] | pattern | HIGH | — | APPROVED |
| 62 | [[tiered-review-escalation-strategy]] | pattern | HIGH | — | APPROVED |

## Guide Cluster Routing (pattern findings only)

| Guide | New Pattern Findings | Would Grow To |
|-------|---------------------|---------------|
| G1 (Writing Agent Specs) | 4 | ~11 |
| G2 (Managing Agent Context) | 3 | ~51 |
| G3 (Agent Architecture) | 12 | ~36 |
| G3b (Agent Workflow/Execution) | 5 | ~25 |
| G4 (Building Evals) | 9 | ~41 |
| G5 (Designing Tools) | 6 | ~22 |
| G6 (Agent Safety) | 4 | ~9 |
| G7 (Session Persistence) | 1 | ~28 |
| G8 (Prompt Engineering) | 3 | ~19 |
| G9 (Agent Governance) | 8 | ~24 |
| G10 (Agent Design Patterns) | 3 | ~19 |
| G11 (Building Agentic Systems) | 0 | 30 |

## Curator Priority Revisions

### Proposed Demotions (P2 → P3)

#### 61. sweci-benchmark-ai-fails-at-code-maintenance

- **Current priority:** P2 (Researcher triage)
- **Proposed priority:** P3 (Monitor)
- **Revision rationale:** LOW classification confidence — the finding is empirical calibration data (a benchmark result), not a reusable design shape. The extractable pattern ("treat maintenance as distinct from generation") is implied, not articulated. Better left as evidence for other patterns than codified directly.
- **Priority-revision status:** APPROVED

#### 64. two-layer-ci-plus-llm-review-gate

- **Current priority:** P2 (Researcher triage)
- **Proposed priority:** P3 (Monitor)
- **Revision rationale:** No linked source file (`sources: []`), single observed instance (OB1 repo only), and LOW classification confidence. The architectural shape (deterministic + judgment layers) is sound but evidence is too thin for P2 codification. Additional independent corroboration needed.
- **Priority-revision status:** APPROVED

## Details

### 1. actor-passport-schema-bound-identity
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** design-approach, composable-downstream, multi-component-schema
- **Co-occurrence:** template
- **Rationale:** Design approach of wrapping every actor in a structured identity artifact validated at runtime. Insight is the shape ("make agency bound and verifiable"), not the scaffold.
- **Guide cluster:** G9

### 2. agent-generated-codebase-walkthrough-for-onboarding
- **Assigned form:** skill
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** ordered-steps, defined-input-output, explicit-invocation, stateless-per-run
- **Rationale:** Specific procedure: agent reads codebase and produces structured walkthrough document with defined I/O.

### 3. agent-memory-architecture-multi-agent-layered
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, forces-tradeoffs, composable-downstream, no-ordered-procedure
- **Rationale:** Reusable architectural shape: decouple agents through structured memory layers. Instances vary (LangGraph, CrewAI, MetaSystem).
- **Guide cluster:** G2

### 4. autoplan-auto-decision-pipeline
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** design-approach, forces-tradeoffs, multi-role-system-dd76
- **Rationale:** Design approach of automating clear decisions and surfacing only "taste decisions" to human gate. DD-76: multiple roles, no single canonical instance.
- **Guide cluster:** G3

### 5. autoresearch-loop-autonomous-metric-driven
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** design-approach, forces-tradeoffs, composable-downstream
- **Co-occurrence:** skill
- **Rationale:** Autonomous metric-driven hypothesis→experiment→measure→keep/discard loop. Insight is the loop shape, not the specific implementation.
- **Guide cluster:** G3

### 6. bidirectional-prompting-for-spec-creation
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, heuristic-decision-framework, forces-tradeoffs
- **Rationale:** Alternating questions between user and LLM before implementation to surface implicit assumptions.
- **Guide cluster:** G8

### 7. builder-validator-chain-pattern
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, forces-tradeoffs, composable-downstream, multi-role-system-dd76
- **Rationale:** Separating artifact creation and review into independent agents with coordinator. DD-76: two roles, no single instance.
- **Guide cluster:** G4

### 8. claude-code-channels-telegramdiscord-as-agent-inte
- **Assigned form:** skill
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** ordered-steps, defined-input-output, explicit-invocation, specific-mechanism
- **Rationale:** Specific procedure for wiring messaging app to Claude Code session with defined steps.

### 9. claude-code-max-plan-subsidy-vs-api-cost-tool
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** explicit-forces-tradeoffs, design-approach, no-ordered-steps
- **Rationale:** Decision framework for tool selection based on cost economics. Philosophy level.
- **Guide cluster:** G3

### 10. claude-code-monitor-tool-event-driven-background
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** design-approach, forces-tradeoffs, mechanism-as-example
- **Rationale:** Event-driven filtered streaming vs blocking vs exit-only notification — design shape for background process monitoring.
- **Guide cluster:** G5

### 11. claude-dispatch-native-mobile-to-local-agent-orch
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** design-approach, forces-tradeoffs, reusable-architecture-shape
- **Rationale:** Remote trigger → local execution → async delivery with credential isolation. Shape generalizes beyond specific product.
- **Guide cluster:** G3

### 12. claude-p-headless-mode-as-openclaw-replacement
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, forces-tradeoffs, composable
- **Rationale:** Headless CLI invocation as programmable agent primitive. Shape reusable across any agent use case.
- **Guide cluster:** G5

### 13. context-gap-task-vs-job
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** explicit-forces-tradeoffs, design-approach, multiple-sources, composable
- **Rationale:** Canonical framework distinguishing bounded tasks from open-ended jobs. Philosophy-level.
- **Guide cluster:** G1

### 14. context-order-diversity-for-bug-detection
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, forces-tradeoffs, composable, multiple-related-findings
- **Rationale:** Diversify context traversal entry points across parallel agents for orthogonal coverage.
- **Guide cluster:** G4

### 15. credential-isolation-bundled-auth-vault-proxy
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, forces-tradeoffs, composable, production-tested
- **Rationale:** Keep credentials physically out of agent sandbox reach. Architectural isolation philosophy.
- **Guide cluster:** G6

### 16. cursor-claude-code-ide-composition
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, forces-tradeoffs, composable
- **Rationale:** Composition architecture: assign each IDE layer a clear role, centralize MCP config.
- **Guide cluster:** G5

### 17. dark-factory-ai-only-codebase-management
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** multi-role-system, design-approach, architecture-shape
- **Rationale:** Fully autonomous SDLC shape with 5-level maturity taxonomy. Two sources but same ecosystem.
- **Guide cluster:** G3

### 18. data-agent-benchmark-dab-cross-dbms-pipeline-eval
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** evaluation-methodology-shape, design-approach, single-source
- **Rationale:** Design approach for evaluating cross-DBMS agent pipelines. Single arxiv source.
- **Guide cluster:** G4

### 19. end-to-end-sequential-bug-fix-pipeline
- **Assigned form:** skill
- **Confidence:** HIGH
- **Tier:** guided
- **Reason codes:** ordered-steps-with-defined-io, explicit-invocation, stateless-per-run, has-failure-modes
- **Rationale:** 9-stage procedure with defined input (Jira ticket) and output (deployed fix). GUIDED because wraps undocumented pipeline pattern.

### 20. event-schema-noun-verb-contract
- **Assigned form:** rule
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** constraint-language, deterministic-check, mandatory-fields-enforcement
- **Rationale:** Binary structural constraint: agents may only trigger events defined in schema. MED because schema-building instructions blur the boundary.

### 21. four-layer-agent-evaluation-architecture
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** guided
- **Reason codes:** multi-layer-composable-design, tradeoffs-per-layer, multiple-sources
- **Rationale:** 4-layer evaluation architecture addressing different failure modes. GUIDED due to evidence-strength mid-file update.
- **Guide cluster:** G4

### 22. four-zone-agent-architecture-framework
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** compositional-vocabulary, forces-per-zone, strong-production-tested
- **Rationale:** Four zones that make any agent debuggable and rebuildable from spec. Structural decomposition vocabulary.
- **Guide cluster:** G3

### 23. framework-tension-taxonomy-superpowers-gsd-gstack
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** decision-framework-shape, tension-tradeoffs, multiple-sources
- **Rationale:** Maps constraint space across three frameworks. Heuristic decision framework.
- **Guide cluster:** G3

### 24. goal-backward-verification
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** verification-philosophy, trust-model, composable
- **Rationale:** Verification philosophy: start from desired outcome, work backward, distrust self-reports. Single source.
- **Guide cluster:** G4

### 25. governance-ontology-semantic-foundation
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, forces-tradeoffs, composable-downstream
- **Rationale:** Define canonical nouns and disambiguation rules as foundational layer.
- **Guide cluster:** G9

### 26. governed-dependency-chain-build-order
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, forces-tradeoffs, composable-downstream
- **Rationale:** Sequentially dependent construction order for governed multi-agent systems.
- **Guide cluster:** G9

### 27. gsd-get-shit-done-plugin
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** design-approach, forces-tradeoffs, composable, single-source
- **Rationale:** Wave-based parallel execution with inter-wave validation. Single source.
- **Guide cluster:** G3

### 28. harness-engineering-third-evolution
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, forces-tradeoffs, multiple-adoption-signals
- **Rationale:** Evolutionary progression: prompt → context → harness engineering. Convergent adoption.
- **Guide cluster:** G3

### 29. headless-multi-pass-iterative-review
- **Assigned form:** skill
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** ordered-steps, defined-inputs-outputs, explicit-invocation, stateless-per-run
- **Rationale:** Run N review passes via headless `claude -p` with fresh context each, aggregate findings.

### 30. hook-based-enforcement-for-agent-outputs
- **Assigned form:** rule
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** binary-constraint, deterministic-check, named-enforcement-boundary
- **Rationale:** Binary hard-gate at PostToolUse boundary. Rubric's own walked candidate for rule form.

### 31. hybrid-retrieval-pattern-semantic-lexical-graph
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, forces-tradeoffs, composable, multiple-adoption-signals
- **Rationale:** Combine three retrieval modes for complete query coverage.
- **Guide cluster:** G2

### 32. intent-based-meta-routing-skill
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** design-approach, surface-structure-trap, single-source
- **Rationale:** Intent classification via routing table in markdown, not code. Surface-structure trap: the SKILL.md is an example, not the pattern.
- **Guide cluster:** G1

### 33. karpathy-autoresearch-self-improvement-loop
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multiple-known-uses, explicit-tradeoffs, no-ordered-procedure, composable
- **Rationale:** Make-one-change→test→keep/revert loop shape for autonomous self-improvement.
- **Guide cluster:** G4

### 34. march-of-nines-compounding-reliability-math-for-m
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** heuristic-decision-framework, explicit-tradeoffs, two-sources
- **Rationale:** Mathematical heuristic for reasoning about multi-step reliability. 0.9^N framing.
- **Guide cluster:** G4

### 35. metaprompting-karpathy-autoresearch-for-build
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** single-source, sibling-overlap
- **Rationale:** Generate→test→iterate loop for prompt optimization. Overlaps with finding #33.
- **Guide cluster:** G8

### 36. monitor-vs-loop-event-driven-vs-time-driven
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** advisory-not-hard-gate, heuristic-decision-framework, single-source
- **Rationale:** Decision heuristic for choosing between event-driven and time-driven execution.
- **Guide cluster:** G5

### 37. notebooklm-python-api-programmatic-access-beyond
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multiple-sources, explicit-tradeoffs, compositional-shape
- **Rationale:** NotebookLM-as-brain / Claude-as-executor RAG shape. Four sources confirm.
- **Guide cluster:** G5

### 38. org-redesign-for-agentic-throughput-high-speed-rail
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multiple-sources, explicit-tradeoffs, solution-shape
- **Rationale:** High-speed-rail topology: humans at handoff points, agents on dedicated infrastructure.
- **Guide cluster:** G3

### 39. parallel-claude-code-instances-per-workspace
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multiple-sources, explicit-tradeoffs, filesystem-as-coordination
- **Rationale:** Filesystem-as-message-passing concurrency shape. Two production-tested sources.
- **Guide cluster:** G3

### 40. passport-object-decision-governance-binding
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** single-source, artifact-shape-clear, template-surface-structure-trap
- **Rationale:** Passport object as compositional primitive for governance audit trails. Single source.
- **Guide cluster:** G9

### 41. planning-session-bias-separate-context-windows
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multiple-sources, explicit-forces-tradeoffs, composable
- **Rationale:** Separate planning and implementation into distinct context windows. Three independent sources.
- **Guide cluster:** G10

### 42. playwright-cli-for-browser-automation
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** single-source, tool-selection-heuristic, tradeoffs-present
- **Rationale:** Tool-selection design approach: prefer accessibility-tree headless automation.
- **Guide cluster:** G5

### 43. policy-as-data-runtime-governance-pattern
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** single-source, named-design-shape, composable
- **Rationale:** Decouple governance rules into versioned policy bundles queried at runtime.
- **Guide cluster:** G9

### 44. production-database-wipeout-agent-context
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** single-source, problem-framing-shape, failure-mode-motivates-design
- **Rationale:** Problem-framing: agent competence and agent safety are independent properties.
- **Guide cluster:** G4

### 45. project-specific-custom-skills-for-repeated-task
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** single-source, design-recommendation, heuristic-level
- **Rationale:** Repeated project-specific workflows should be encoded as named custom skills.
- **Guide cluster:** G1

### 46. prompt-injection-risk-from-trusted-vs-untrusted
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** two-sources, session-isolation-shape, rule-co-occurrence
- **Rationale:** Browser agents must isolate sensitive sessions from general web browsing. Architectural, not mechanical.
- **Guide cluster:** G6

### 47. ralph-wiggum-execution-pattern
- **Assigned form:** skill
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** explicit-ordered-steps, defined-io, explicit-invocation, multiple-tier1-sources
- **Rationale:** Named bash loop: spawn headless Claude per iteration, 5 ordered steps per pass. Multiple Anthropic sources.

### 48. runtime-governance-gap-buildtime-to-production
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** single-source, problem-framing-shape, no-solution
- **Rationale:** Named problem-framing: policy-as-code creates architectural mismatch with continuous agents.
- **Guide cluster:** G9

### 49. runtime-threshold-management-truth-conditions
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** multi-component-architecture, competing-forces, composable
- **Rationale:** Two-layer runtime governance design: threshold pressure-valve + truth verification.
- **Guide cluster:** G9

### 50. sandbox-architecture-by-threat-model-microvm-vs-container
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** competing-forces, it-depends, multiple-sources
- **Rationale:** Map sandbox choice to threat model. Two independent sources converge on the framing.
- **Guide cluster:** G6

### 51. scheduled-task-dashboard-observability-layer
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** architectural-shape, composable, single-implementation-source
- **Rationale:** Centralized observability layer above scheduling primitives. Tool-specific anchor.
- **Guide cluster:** G3b

### 52. self-improving-skill-lessons-log
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** design-approach, composable, borderline-skill
- **Rationale:** Embed self-improvement phase and persistent lessons log into skill structure. Design approach.
- **Guide cluster:** G10

### 53. shell-injection-vector-taxonomy-agent-bash-security
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** taxonomy-as-design-approach, informs-rules-downstream
- **Rationale:** Enumerated taxonomy of injection vectors. The taxonomy is the shape; specific rules are downstream.
- **Guide cluster:** G6

### 54. skill-self-improvement-three-approaches
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** dd76-role-count, multiple-repos, competing-mechanisms
- **Rationale:** Three implementations converge on problem, diverge on mechanism. Classic DD-76 trigger.
- **Guide cluster:** G10

### 55. skills-as-markdown-sop-files-encode-processes
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multiple-sources, explicit-tradeoffs, production-migration
- **Rationale:** Represent agent processes as markdown SOP files. BMAD v6.1.0 production migration evidence.
- **Guide cluster:** G3

### 56. skills-inside-workspace-contextual-skill
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** competing-forces, single-source
- **Rationale:** Contextual routing table vs global loading based on scale.
- **Guide cluster:** G5

### 57. star-commands-for-explicit-output-format-override
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** single-source, design-approach, mechanism
- **Rationale:** Named-dispatch mechanism for output mode override. Single-source.
- **Guide cluster:** G8

### 58. stop-rules-as-execution-boundaries
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multiple-independent-sources, explicit-tradeoffs, three-category-taxonomy
- **Rationale:** Execution boundaries declared in three categories before deployment. Multiple sources.
- **Guide cluster:** G1

### 59. sub-agent-context-isolation-for-parallel-complex
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multiple-sources, explicit-tradeoffs, composable-primitive
- **Rationale:** Isolate each analysis unit in its own context window, run in parallel, aggregate.
- **Guide cluster:** G3

### 60. subagent-exploration-mode-parallel-codebase-mappi
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** single-source, two-mode-parameterization
- **Rationale:** Exploration topology with Mapping vs Tracing sub-modes. Single-source.
- **Guide cluster:** G3

### 61. sweci-benchmark-ai-fails-at-code-maintenance
- **Assigned form:** pattern
- **Confidence:** LOW
- **Tier:** hitl
- **Reason codes:** empirical-evidence-not-shape, no-reusable-structure, single-source
- **Rationale:** Primarily a benchmark result, not a reusable design shape. Pattern is implied but not articulated.
- **Current priority:** P2 (Researcher triage)
- **Proposed priority:** P3 (Monitor)
- **Revision rationale:** LOW confidence — empirical calibration data, not a codifiable design shape. Better as evidence for other patterns.
- **Priority-revision status:** APPROVED
- **Guide cluster:** G4

### 62. tiered-review-escalation-strategy
- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multiple-sources, explicit-tradeoffs, composable-decision-framework
- **Rationale:** Cost-of-review should scale with risk-of-change. Well-established engineering analog.
- **Guide cluster:** G4

### 63. tool-model-io-contracts-with-preconditions
- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** single-source, three-element-contractual-structure, rule-co-occurrence
- **Co-occurrence:** rule
- **Rationale:** Three-element contractual structure governing external side effects. Rule ("preconditions must block") is harvestable downstream.
- **Guide cluster:** G9

### 64. two-layer-ci-plus-llm-review-gate
- **Assigned form:** pattern
- **Confidence:** LOW
- **Tier:** hitl
- **Reason codes:** no-source-file, single-instance, rule-co-occurrence
- **Co-occurrence:** rule
- **Rationale:** Separate deterministic checks from judgment checks. Shape is clear but evidence is thin.
- **Current priority:** P2 (Researcher triage)
- **Proposed priority:** P3 (Monitor)
- **Revision rationale:** No linked source file, single observed instance (OB1 only). Evidence too thin for P2 codification.
- **Priority-revision status:** APPROVED
- **Guide cluster:** G9
