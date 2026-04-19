---
title: "Artifact Identification Report — P2 Findings"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-04-19"
scope: "All P2 (Design Required) findings"
findings_scanned: 120
findings_filtered: 0
---

# Artifact Identification Report — 2026-04-19

**Scope:** All P2 (Design Required) findings
**Findings scanned:** 120 | **Filtered out:** 0 (dedup: 0, weak: 0, adopted: 0)
**Classified:** 120

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | 100 | 83.3% | 52 | 48 | 0 |
| skill | 9 | 7.5% | 5 | 4 | 0 |
| rule | 6 | 5.0% | 4 | 2 | 0 |
| template | 3 | 2.5% | 1 | 2 | 0 |
| agent | 2 | 1.7% | 1 | 1 | 0 |
| **Total** | **120** | **100%** | **63** | **57** | **0** |

**Comparison to P1 run:** P1 was 92% pattern (69/75). P2 is 83.3% pattern (100/120) — more non-pattern forms emerged, consistent with P2 findings being more mechanism-specific. Non-pattern count: P1 had 6 (8%), P2 has 20 (16.7%).

**Synthesis status (2026-04-19):** All 100 pattern findings consumed by guide synthesis. 48 GUIDED patterns marked SYNTHESIZED. 52 AUTO patterns consumed via guide re-synthesis (status remains APPROVED — extraction was via guide, not individual artifact). G3 split into G3+G3b. G9 and G10 graduated from unrouted/scattered.

**Guide routing:** 100 pattern findings checked against guide routing table. ~85 map to existing G1-G8 clusters. 2 candidate clusters detected:
- **Governance** — 8+ P2 pattern findings join 2 existing P1 findings (10+ total). Exceeds 5-finding graduation threshold. Candidate for G9.
- **Agent Design** — 10+ P2 pattern findings. Currently "scattered" across G1/G3/G7. Candidate for dedicated guide G10.

---

## Candidates

### GUIDED — Review Recommended (57 findings)

| # | Finding | Form | Conf | Co-occurrence | Status |
|---|---------|------|------|---------------|--------|
| 1 | [[anthropic-managed-agents-platform]] | pattern | MED | — | SYNTHESIZED |
| 2 | [[multi-day-autonomous-scientific-computing-workflow]] | pattern | MED | — | SYNTHESIZED |
| 3 | [[tool-use-examples-sample-calls-in-definitions]] | pattern | MED | — | SYNTHESIZED |
| 4 | [[credential-isolation-bundled-auth-vault-proxy]] | pattern | MED | — | SYNTHESIZED |
| 5 | [[inter-agent-web-contamination-eval-artifact-persist]] | pattern | MED | rule | SYNTHESIZED |
| 6 | [[dynamic-tool-pool-assembly-transcript-compaction]] | pattern | MED | — | SYNTHESIZED |
| 7 | [[non-deterministic-tool-contract-model]] | pattern | MED | — | SYNTHESIZED |
| 8 | [[capability-vs-regression-eval-lifecycle]] | pattern | MED | — | SYNTHESIZED |
| 9 | [[response-format-enum-for-adaptive-verbosity]] | pattern | MED | rule | SYNTHESIZED |
| 10 | [[brevity-constraints-reverse-llm-performance]] | pattern | MED | rule | SYNTHESIZED |
| 11 | [[conway-always-on-persistent-agent]] | pattern | MED | — | SYNTHESIZED |
| 12 | [[behavioral-context-portability-intelligence-lock-in]] | pattern | MED | — | SYNTHESIZED |
| 13 | [[sdk-vs-framework-decision-for-agent-building]] | pattern | MED | — | SYNTHESIZED |
| 14 | [[agent-teams-shared-communication-channel]] | pattern | MED | — | SYNTHESIZED |
| 15 | [[advanced-elicitation-techniques-library]] | pattern | MED | template | SYNTHESIZED |
| 16 | [[governance-memory-append-only-audit-layer]] | pattern | MED | rule | SYNTHESIZED |
| 17 | [[reasoning-token-overhead-from-context-files]] | pattern | MED | — | SYNTHESIZED |
| 18 | [[scalpel-local-parse-then-llm-cost-optimization]] | pattern | MED | — | SYNTHESIZED |
| 19 | [[mcp-evaluation-primitives-deepeval-metrics]] | pattern | MED | skill | SYNTHESIZED |
| 20 | [[skill-as-script-wrapper-for-complex-pipelines]] | pattern | MED | — | SYNTHESIZED |
| 21 | [[oneshot-infrastructure-setup-prompt-pattern]] | pattern | MED | template | SYNTHESIZED |
| 22 | [[compound-review-debt-from-deferred-inspection]] | pattern | MED | — | SYNTHESIZED |
| 23 | [[ide-context-streaming-silent-token-tax]] | pattern | MED | — | SYNTHESIZED |
| 24 | [[index-file-navigation-as-rag-replacement]] | pattern | MED | — | SYNTHESIZED |
| 25 | [[frontier-release-compression-march-2026]] | pattern | MED | — | SYNTHESIZED |
| 26 | [[emergent-agentic-behaviors-from-outcome-rl]] | pattern | MED | — | SYNTHESIZED |
| 27 | [[biomimetic-memory-auto-recall-over-tool-based]] | pattern | MED | — | SYNTHESIZED |
| 28 | [[claude-code-long-term-memory-via-pre-prompt-recall]] | pattern | MED | skill | SYNTHESIZED |
| 29 | [[critic-verifier-loop-with-termination]] | pattern | MED | rule | SYNTHESIZED |
| 30 | [[cot-fails-without-inductive-generalization]] | pattern | MED | rule | SYNTHESIZED |
| 31 | [[ai-developer-descent-into-madness-anti-pattern]] | pattern | MED | rule | SYNTHESIZED |
| 32 | [[test-input-coverage-design-15-30-sweet-spot]] | pattern | MED | — | SYNTHESIZED |
| 33 | [[stop-rules-as-execution-boundaries]] | pattern | MED | rule | SYNTHESIZED |
| 34 | [[mcp-ecosystem-critical-mass-97m-installs]] | pattern | MED | — | SYNTHESIZED |
| 35 | [[ace-execution-feedback-no-labels-required]] | pattern | MED | — | SYNTHESIZED |
| 36 | [[new-chat-per-agent-step-context-hygiene]] | pattern | MED | — | SYNTHESIZED |
| 37 | [[claudemd-as-knowledge-base-traversal-guide]] | pattern | MED | — | SYNTHESIZED |
| 38 | [[transitional-lock-in-risk-and-shim-assessment]] | pattern | MED | template | SYNTHESIZED |
| 39 | [[task-complexity-tiering-quick-campaign-deep-build]] | pattern | MED | — | SYNTHESIZED |
| 40 | [[gsd-stall-detection-revision-loop-escalation]] | pattern | MED | rule | SYNTHESIZED |
| 41 | [[four-tier-agent-memory-model-with-write-policy]] | pattern | MED | skill | SYNTHESIZED |
| 42 | [[staged-delivery-for-review-digestibility]] | pattern | MED | — | SYNTHESIZED |
| 43 | [[reviewer-skill-elevation-for-agentic-output]] | pattern | MED | — | SYNTHESIZED |
| 44 | [[gsd-queryable-codebase-intelligence-store]] | pattern | MED | — | SYNTHESIZED |
| 45 | [[dual-ingestion-funnel-human-clip-plus-llm-research]] | pattern | MED | — | SYNTHESIZED |
| 46 | [[model-specific-context-file-sensitivity]] | pattern | MED | — | SYNTHESIZED |
| 47 | [[soul-md-agent-constitution-pattern]] | pattern | MED | template | SYNTHESIZED |
| 48 | [[structured-streaming-events-observability]] | pattern | MED | template | SYNTHESIZED |
| 49 | [[cross-model-verification-for-bug-finding]] | skill | MED | — | APPROVED |
| 50 | [[thinking-models-mental-framework-commands-for-codi]] | skill | MED | — | APPROVED |
| 51 | [[agentic-harness-self-assessment-skill]] | skill | HIGH | — | APPROVED |
| 52 | [[post-session-hooks-autonomous-version-control]] | skill | MED | — | APPROVED |
| 53 | [[file-read-deduplication-pattern]] | rule | MED | — | APPROVED |
| 54 | [[bmad-deterministic-skill-validator]] | pattern | MED | — | REDIRECTED |
| 55 | [[gsd-execution-context-profiles-mode-switching]] | template | MED | — | APPROVED |
| 56 | [[one-shot-prd-prompt-for-system-bootstrap]] | template | MED | pattern | APPROVED |
| 57 | [[initializer-agent-scaffolding-pattern]] | agent | MED | skill | APPROVED |

### AUTO — Ready for Extraction (63 findings)

| # | Finding | Form | Conf | Co-occurrence | Status |
|---|---------|------|------|---------------|--------|
| 58 | [[llm-as-judge-pattern-for-verification-agents]] | pattern | HIGH | — | APPROVED |
| 59 | [[tool-gateway-security-boundary]] | pattern | HIGH | — | APPROVED |
| 60 | [[durable-workflow-engine-for-agent-systems]] | pattern | HIGH | — | APPROVED |
| 61 | [[harness-simplification-as-models-improve]] | pattern | HIGH | — | APPROVED |
| 62 | [[self-improving-agent-prompt-tool-diagnosis]] | pattern | HIGH | — | APPROVED |
| 63 | [[agent-clarification-over-assumption-pattern]] | pattern | HIGH | — | APPROVED |
| 64 | [[specialized-parallel-agent-roles]] | pattern | HIGH | — | APPROVED |
| 65 | [[human-on-the-loop-hotl-autonomy-tiering-framework]] | pattern | HIGH | — | APPROVED |
| 66 | [[benchmark-signal-mismatch-optimization-gap]] | pattern | HIGH | — | APPROVED |
| 67 | [[trust-calibration-progressive-autonomy-ramp]] | pattern | HIGH | — | APPROVED |
| 68 | [[session-as-append-only-event-log]] | pattern | HIGH | — | APPROVED |
| 69 | [[brain-hands-decoupling-architecture]] | pattern | HIGH | — | APPROVED |
| 70 | [[eval-driven-development-autonomous-quality]] | pattern | HIGH | — | APPROVED |
| 71 | [[sprint-contract-negotiation-pattern]] | pattern | HIGH | — | APPROVED |
| 72 | [[search-over-list-tool-design-pattern]] | pattern | HIGH | — | APPROVED |
| 73 | [[archon-yaml-defined-harness-workflows]] | pattern | HIGH | — | APPROVED |
| 74 | [[success-rate-eval-over-binary-pass-fail]] | pattern | HIGH | — | APPROVED |
| 75 | [[negative-constraints-as-probabilistic-output-collapse]] | pattern | HIGH | — | APPROVED |
| 76 | [[gstack-review-army-parallel-specialist-dispatch]] | pattern | HIGH | — | APPROVED |
| 77 | [[four-layer-production-eval-stack-with-golden-traces]] | pattern | HIGH | — | APPROVED |
| 78 | [[deep-plan-multi-agent-exploration-pattern]] | pattern | HIGH | — | APPROVED |
| 79 | [[bmad-method-v6-multi-agent-sdlc]] | pattern | HIGH | — | APPROVED |
| 80 | [[agent-sprawl-anti-pattern-microservices-redux]] | pattern | HIGH | — | APPROVED |
| 81 | [[skill-vs-process-distinction-deterministic-rails]] | pattern | HIGH | — | APPROVED |
| 82 | [[four-layer-enterprise-memory-stack]] | pattern | HIGH | — | APPROVED |
| 83 | [[tiered-context-injection-over-monolithic-files]] | pattern | HIGH | — | APPROVED |
| 84 | [[agent-cost-blowup-mitigation-strategies]] | pattern | HIGH | — | APPROVED |
| 85 | [[agent-identity-governance-enforcement-layer]] | pattern | HIGH | — | APPROVED |
| 86 | [[graceful-degradation-modes-for-agent-failure]] | pattern | HIGH | — | APPROVED |
| 87 | [[structured-fact-extraction-from-conversations]] | pattern | HIGH | — | APPROVED |
| 88 | [[gsd-gates-taxonomy-four-canonical-types]] | pattern | HIGH | — | APPROVED |
| 89 | [[yaml-template-dual-structure]] | pattern | HIGH | — | APPROVED |
| 90 | [[notebooklm-as-external-knowledge-base-for-context]] | pattern | HIGH | — | APPROVED |
| 91 | [[agent-architecture-layer-impermanence]] | pattern | HIGH | — | APPROVED |
| 92 | [[bmad-help-adaptive-module-routing]] | pattern | HIGH | — | APPROVED |
| 93 | [[agent-type-system-six-roles]] | pattern | HIGH | — | APPROVED |
| 94 | [[multidimensional-success-criteria-smart]] | pattern | HIGH | — | APPROVED |
| 95 | [[google-a2a-protocol-agent-to-agent-interoperabilit]] | pattern | HIGH | — | APPROVED |
| 96 | [[five-layer-agent-prompt-architecture]] | pattern | HIGH | — | APPROVED |
| 97 | [[design-evaluate-dual-phase-prompting-framework]] | pattern | HIGH | — | APPROVED |
| 98 | [[arc-agi-3-zero-percent-abstract-reasoning]] | pattern | HIGH | — | APPROVED |
| 99 | [[agentic-infrastructure-pilot-to-production]] | pattern | HIGH | — | APPROVED |
| 100 | [[unified-tracing-opentelemetry-for-agents]] | pattern | HIGH | — | APPROVED |
| 101 | [[pointers-over-copies-in-context-files]] | pattern | HIGH | — | APPROVED |
| 102 | [[memory-cross-layer-promotion-governance]] | pattern | HIGH | — | APPROVED |
| 103 | [[review-pipeline-bottleneck-and-quality-at-source]] | pattern | HIGH | — | APPROVED |
| 104 | [[six-layer-agent-infrastructure-stack]] | pattern | HIGH | — | APPROVED |
| 105 | [[prompt-as-policy-version-control-and-cicd-for-agen]] | pattern | HIGH | — | APPROVED |
| 106 | [[gstack-specialist-role-architecture]] | pattern | HIGH | — | APPROVED |
| 107 | [[gsd-global-learnings-store-cross-session-persistence]] | pattern | HIGH | — | APPROVED |
| 108 | [[bmad-outcome-based-skill-rewrite-pattern]] | pattern | HIGH | — | APPROVED |
| 109 | [[cloud-local-plan-handoff-teleport-pattern]] | pattern | HIGH | — | APPROVED |
| 110 | [[eval-driven-tool-iteration-loop]] | skill | HIGH | — | APPROVED |
| 111 | [[correct-course-mid-project-pivot-command]] | skill | HIGH | — | APPROVED |
| 112 | [[stupid-button-six-question-token-audit-diagnostic]] | skill | HIGH | — | APPROVED |
| 113 | [[gsd-prompt-injection-scanner-hardening]] | skill | HIGH | — | APPROVED |
| 114 | [[five-commandments-for-agent-deployment-audit-first]] | skill | HIGH | — | APPROVED |
| 115 | [[balanced-positive-negative-eval-sets]] | rule | HIGH | — | APPROVED |
| 116 | [[token-budget-pre-turn-projection]] | rule | HIGH | — | APPROVED |
| 117 | [[pre-compression-identity-pinning]] | rule | HIGH | — | APPROVED |
| 118 | [[fix-data-schema-before-automating]] | rule | HIGH | — | APPROVED |
| 119 | [[yaml-templates-with-embedded-elicitation-instructions]] | template | HIGH | — | APPROVED |
| 120 | [[qa-agent-independent-compliance-review]] | agent | HIGH | — | APPROVED |

---

## Details

### GUIDED — Pattern (48 findings)

#### 1. anthropic-managed-agents-platform
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Product-level description; pattern by exclusion — the extractable insight is "managed-platform-as-a-service as deployment shape with vendor lock-in tradeoffs."

#### 2. multi-day-autonomous-scientific-computing-workflow
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Shape is the shift from conversational oversight to objective specification with persistent memory + test oracle. MED because four specific components create plausible skill reading.

#### 3. tool-use-examples-sample-calls-in-definitions
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Design approach for tool definition authoring with "it depends" character (complex schemas benefit, simple tools don't). Single-source (Anthropic beta).

#### 4. credential-isolation-bundled-auth-vault-proxy
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Architectural isolation shape with two named instantiations. Single source; rule co-occurrence plausible ("credentials MUST NOT be accessible from sandbox").

#### 5. inter-agent-web-contamination-eval-artifact-persist
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** rule
- **Rationale:** Structural phenomenon (eval queries create persistent contamination). Four mitigations signal shape, not single rule. Single-source.

#### 6. dynamic-tool-pool-assembly-transcript-compaction
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Two bundled context-optimization techniques at heuristic level. MED because the bundling creates ambiguity (could be two patterns).

#### 7. non-deterministic-tool-contract-model
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Philosophy-level reframing ("UX design, not API design"). Single practitioner source.

#### 8. capability-vs-regression-eval-lifecycle
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Two eval modes with graduation lifecycle. Single source (Anthropic demystifying evals).

#### 9. response-format-enum-for-adaptive-verbosity
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** rule
- **Rationale:** Reusable design shape for verbosity control. Sits at mechanism level; a reviewer could read the specific enum instruction as a rule.

#### 10. brevity-constraints-reverse-llm-performance
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** rule
- **Rationale:** Philosophy-level: verbosity-accuracy tradeoff mechanism. The specific constraint recommendation is a plausible downstream rule.

#### 11. conway-always-on-persistent-agent
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Persistent event-driven behavioral accumulation as platform strategy. Single-source (leaked code analysis).

#### 12. behavioral-context-portability-intelligence-lock-in
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Novel lock-in category at philosophy level. Single-source; no convergent adoption.

#### 13. sdk-vs-framework-decision-for-agent-building
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Decision heuristic with two diagnostic questions. Single source.

#### 14. agent-teams-shared-communication-channel
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Architectural shape: add shared channel to isolated multi-agent topology. Single practitioner source.

#### 15. advanced-elicitation-techniques-library
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** template
- **Rationale:** 18 techniques as instances of "structured second-pass reasoning." Template co-occurrence from YAML embedding.

#### 16. governance-memory-append-only-audit-layer
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** rule
- **Rationale:** Governance layer architecture with forces/tradeoffs. Rule co-occurrence real ("append-only" = constraint).

#### 17. reasoning-token-overhead-from-context-files
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Empirical principle (14-22% reasoning overhead). Single source (ETH Zurich).

#### 18. scalpel-local-parse-then-llm-cost-optimization
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Generalizable design approach (local models for structure, LLM for semantics). Single practitioner source.

#### 19. mcp-evaluation-primitives-deepeval-metrics
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** skill
- **Rationale:** Reusable evaluation shape (define+capture+judge). Mechanism-level detail creates skill pull.

#### 20. skill-as-script-wrapper-for-complex-pipelines
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Surface-structure trap resolved: finding about skills is itself a pattern. Single source.

#### 21. oneshot-infrastructure-setup-prompt-pattern
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** template
- **Rationale:** Approach of front-loading setup decisions. Template alternative plausible but no fillable backbone provided.

#### 22. compound-review-debt-from-deferred-inspection
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Heuristic-level: why deferred review compounds cost. Single source.

#### 23. ide-context-streaming-silent-token-tax
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Context-management heuristic. Anti-pattern language but no deterministic boundary check.

#### 24. index-file-navigation-as-rag-replacement
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Structural approach to knowledge retrieval. Single primary source (Karpathy).

#### 25. frontier-release-compression-march-2026
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Observation-heavy; pattern element (task-specific routing heuristic) is implicit.

#### 26. emergent-agentic-behaviors-from-outcome-rl
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Design principle: leave space for emergent behaviors. Single source (ARTIST paper).

#### 27. biomimetic-memory-auto-recall-over-tool-based
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Design principle about memory retrieval placement. Single source ecosystem.

#### 28. claude-code-long-term-memory-via-pre-prompt-recall
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** skill
- **Rationale:** Implementation pattern with configurable parameters. No explicit invocation; skill-boundary adjacent.

#### 29. critic-verifier-loop-with-termination
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** rule
- **Rationale:** Compositional loop structure. Termination conditions have rule-level specificity.

#### 30. cot-fails-without-inductive-generalization
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** rule
- **Rationale:** Heuristic boundary on CoT applicability. "Novel abstraction" check requires judgment (not deterministic), excluding rule.

#### 31. ai-developer-descent-into-madness-anti-pattern
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** rule
- **Rationale:** 8-step failure cycle is structural anti-pattern shape. The diagnostic ("if agent-checks-agent, redesign") is an expressible boundary rule.

#### 32. test-input-coverage-design-15-30-sweet-spot
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Heuristic decision framework. 15-30 is an instance number, not a binary constraint.

#### 33. stop-rules-as-execution-boundaries
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** rule
- **Rationale:** Teaches a class of constraints (halt/escalate/complete), not one specific check.

#### 34. mcp-ecosystem-critical-mass-97m-installs
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Strategic observation. Pattern by exclusion — design implication ("treat MCP as baseline") is real but finding is observational.

#### 35. ace-execution-feedback-no-labels-required
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Generalizable shape (binary execution signals as feedback). Framework-specific anchoring (ACE).

#### 36. new-chat-per-agent-step-context-hygiene
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Reusable discipline-shape. Single practitioner source (BMad Method).

#### 37. claudemd-as-knowledge-base-traversal-guide
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Design approach for CLAUDE.md structuring. Single source (Karpathy/Chase AI).

#### 38. transitional-lock-in-risk-and-shim-assessment
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** template
- **Rationale:** Decision framework (shim vs native). Template alternative from potential decision matrix.

#### 39. task-complexity-tiering-quick-campaign-deep-build
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Three-tier classification shape. Single source.

#### 40. gsd-stall-detection-revision-loop-escalation
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** rule
- **Rationale:** Trajectory-monitoring heuristic. Rule possible once invariant thresholds are formalized.

#### 41. four-tier-agent-memory-model-with-write-policy
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** skill
- **Rationale:** Architectural shape with write policy steps that could be extracted as a skill.

#### 42. staged-delivery-for-review-digestibility
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Reviewer-calibrated delivery shape. Single source.

#### 43. reviewer-skill-elevation-for-agentic-output
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Philosophy-level: reviewer role evolution. Single source.

#### 44. gsd-queryable-codebase-intelligence-store
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Persistent queryable intelligence layer. Single source (GSD changelog).

#### 45. dual-ingestion-funnel-human-clip-plus-llm-research
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Parallel ingestion shape. Single source, partially adopted in MetaSystem.

#### 46. model-specific-context-file-sensitivity
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided
- **Rationale:** Design heuristic: one-size-fits-all context strategies fail. Single source (ETH Zurich).

#### 47. soul-md-agent-constitution-pattern
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** template
- **Rationale:** Identity-separation architecture. Template co-occurrence from 4-section anatomy (SOUL.md scaffold).

#### 48. structured-streaming-events-observability
- **Assigned form:** pattern | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** template
- **Rationale:** Typed event architecture. Event taxonomy is template-adjacent.

### GUIDED — Skill (4 findings)

#### 49. cross-model-verification-for-bug-finding
- **Assigned form:** skill | **Confidence:** MED | **Tier:** guided
- **Rationale:** 3+3 parallel pipeline with defined I/O and failure modes. MED because cognitive disposition about disagreement signals is baked into design. Source calls it "fleet review skill."

#### 50. thinking-models-mental-framework-commands-for-codi
- **Assigned form:** skill | **Confidence:** MED | **Tier:** guided
- **Rationale:** 12 slash commands with explicit invocation, ordered steps per model. Framework-shaped skill trap (§2 tier note): wraps TACHES 12-primitive taxonomy → drops to guided.

#### 51. agentic-harness-self-assessment-skill
- **Assigned form:** skill | **Confidence:** HIGH | **Tier:** guided
- **Rationale:** All four skill markers met (I/O, steps, invocation, stateless). HIGH confidence on form, but wraps 12-primitive framework → drops to guided per §2 tier note.

#### 52. post-session-hooks-autonomous-version-control
- **Assigned form:** skill | **Confidence:** MED | **Tier:** guided
- **Rationale:** Procedure (hook → git add → commit → push) with defined trigger and output. MED because steps are implied rather than fully enumerated.

### GUIDED — Rule (2 findings)

#### 53. file-read-deduplication-pattern
- **Assigned form:** rule | **Confidence:** MED | **Tier:** guided
- **Rationale:** Deterministic invariant (file seen AND unchanged → return stub) at file-read boundary. MED because the finding also describes "when and why" across cases, the one rule-exclusion that pulls toward pattern.

#### 54. bmad-deterministic-skill-validator
- **Assigned form:** ~~rule~~ → **pattern** (REDIRECTED) | **Confidence:** MED | **Tier:** guided
- **Rationale:** 19 deterministic rules at CI boundary replacing LLM review. MED because multi-rule taxonomy blurs toward pattern; individual rules are the clean rule-form instantiations. **Redirected:** describes a class of rules (deterministic validation replacing LLM review), not a single enforceable constraint. Routes to guide synthesis with other pattern findings.

### GUIDED — Template (2 findings)

#### 55. gsd-execution-context-profiles-mode-switching
- **Assigned form:** template | **Confidence:** MED | **Tier:** guided
- **Rationale:** Scaffold with explicit variation axis (dev/research/review modes), named config slot. MED because no formal generator documented; pattern alternative viable.

#### 56. one-shot-prd-prompt-for-system-bootstrap
- **Assigned form:** template | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** pattern
- **Rationale:** PRD scaffold with named slots. Two independent implementations (Karpathy, Cole Medin). MED because "PRD-as-prompt" concept is also pattern-shaped.

### GUIDED — Agent (1 finding)

#### 57. initializer-agent-scaffolding-pattern
- **Assigned form:** agent | **Confidence:** MED | **Tier:** guided | **Co-occurrence:** skill
- **Rationale:** Single named role with distinct first-session identity. DD-76 does not apply (role count = 1). MED because procedural elements (expand → create → init → commit) create skill tension.

### AUTO — Pattern (52 findings)

#### 58–109. Pattern AUTO findings

All 52 pattern AUTO findings were classified with HIGH confidence. They share these characteristics: multiple independent sources, explicit forces/tradeoffs, no ordered procedure, no binary constraint, no fillable scaffold, no single named persona. Key highlights:

- **DD-76 applied** (role count > 1 → pattern): specialized-parallel-agent-roles, gstack-review-army, deep-plan-multi-agent, bmad-method-v6, google-a2a-protocol, agent-type-system-six-roles, gstack-specialist-role-architecture
- **Anti-pattern findings correctly routed to pattern** (not rule): agent-sprawl (sociotechnical, no deterministic check), agent-architecture-layer-impermanence (philosophical)
- **Self-described patterns confirmed**: sprint-contract-negotiation, bmad-outcome-based-skill-rewrite, cloud-local-plan-handoff

### AUTO — Skill (5 findings)

#### 110. eval-driven-tool-iteration-loop
- **Assigned form:** skill | **Confidence:** HIGH | **Tier:** auto
- **Rationale:** Three-phase procedure with defined inputs (prototype tools + tasks), outputs (improved tools), and steps. Strong production evidence (Slack MCP).

#### 111. correct-course-mid-project-pivot-command
- **Assigned form:** skill | **Confidence:** HIGH | **Tier:** auto
- **Rationale:** Explicit invocation (`correct course` command), 5 ordered steps, defined output (revised backlog), stateless per run.

#### 112. stupid-button-six-question-token-audit-diagnostic
- **Assigned form:** skill | **Confidence:** HIGH | **Tier:** auto
- **Rationale:** All four skill markers. Six questions as sequential diagnostic. Three implementation tiers = parameterization.

#### 113. gsd-prompt-injection-scanner-hardening
- **Assigned form:** skill | **Confidence:** HIGH | **Tier:** auto
- **Rationale:** Four-layer detection procedure (Unicode → encoding → structural → entropy) with defined I/O and enforcement boundary. Rule co-occurrence noted ("content must pass scanner").

#### 114. five-commandments-for-agent-deployment-audit-first
- **Assigned form:** skill | **Confidence:** HIGH | **Tier:** auto
- **Rationale:** 5-step sequential checklist with defined input state and output, failure modes per step, explicit invocation (pre-deployment gate).

### AUTO — Rule (4 findings)

#### 115. balanced-positive-negative-eval-sets
- **Assigned form:** rule | **Confidence:** HIGH | **Tier:** auto
- **Rationale:** Binary constraint: eval sets must include negative cases. Deterministic check (present? yes/no) at eval design gate. Production failure evidence (Claude.ai web search).

#### 116. token-budget-pre-turn-projection
- **Assigned form:** rule | **Confidence:** HIGH | **Tier:** auto
- **Rationale:** Binary invariant: if projected cost > budget, halt before API call. Deterministic formula at pre-turn boundary. No judgment required.

#### 117. pre-compression-identity-pinning
- **Assigned form:** rule | **Confidence:** HIGH | **Tier:** auto
- **Rationale:** Binary: identity file MUST be pinned at context top and re-injected at session start/compression. Deterministic check (pinned or not).

#### 118. fix-data-schema-before-automating
- **Assigned form:** rule | **Confidence:** HIGH | **Tier:** auto
- **Rationale:** Pre-automation gate: schema MUST be established before agent access. Deterministic check (schema defined? validation built?). Constraint language throughout.

### AUTO — Template (1 finding)

#### 119. yaml-templates-with-embedded-elicitation-instructions
- **Assigned form:** template | **Confidence:** HIGH | **Tier:** auto
- **Rationale:** YAML scaffold with two interleaved layers — document outline (section variables) + embedded agent instructions (body per section). Insight fully capturable as {{section_name}} → [structure + instruction]. All template inclusion signals met.

### AUTO — Agent (1 finding)

#### 120. qa-agent-independent-compliance-review
- **Assigned form:** agent | **Confidence:** HIGH | **Tier:** auto
- **Rationale:** Single named role (Quinn) with specific disposition (fresh-context independence), consistent scope and name across sources (BMad v6 + masterclass). DD-76 does not trigger (role count = 1). "How it thinks" is the core insight.

---

## Guide Routing Check (DD-81)

100 pattern findings checked against the guide routing table.

### Routed findings (~85)

Most P2 pattern findings map cleanly to existing G1-G8 clusters via their research dimension:
- **G1 (Writing Agent Specifications)** — Intent Engineering findings
- **G2 (Managing Agent Context)** — Context Engineering findings
- **G3 (Agent Architecture Decisions)** — Orchestration findings
- **G4 (Building Agent Evaluation Suites)** — Evaluation findings
- **G5 (Designing Agent Tools)** — Tool Integration findings
- **G6 (Agent Safety and Permissions)** — Sandboxing findings
- **G7 (Session Persistence and Memory)** — Memory Architecture findings
- **G8 (Model-Resilient Prompt Engineering)** — Prompt Craft and Model Selection findings

### Candidate clusters detected

**Governance (candidate G9):** 8+ P2 pattern findings: tool-gateway-security-boundary, human-on-the-loop-hotl-autonomy-tiering-framework, trust-calibration-progressive-autonomy-ramp, behavioral-context-portability-intelligence-lock-in, governance-memory-append-only-audit-layer, compound-review-debt-from-deferred-inspection, reviewer-skill-elevation-for-agentic-output, agent-identity-governance-enforcement-layer. Combined with 2 existing P1 findings = 10+ total. **Exceeds 5-finding graduation threshold.**

**Agent Design (candidate G10):** 10+ P2 pattern findings: harness-simplification-as-models-improve, self-improving-agent-prompt-tool-diagnosis, agent-clarification-over-assumption-pattern, specialized-parallel-agent-roles, conway-always-on-persistent-agent, five-layer-agent-prompt-architecture, ai-developer-descent-into-madness-anti-pattern, soul-md-agent-constitution-pattern, emergent-agentic-behaviors-from-outcome-rl, agentic-infrastructure-pilot-to-production. Currently "scattered" across G1/G3/G7. **Warrants dedicated guide.**

### Unrouted bucket updates needed

No unrouted bucket updates are needed at this time — all pattern findings map to either an existing cluster or one of the two candidate clusters above.
