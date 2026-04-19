---
title: "Artifact Identification Report"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-04-19"
scope: "All P1 findings (full run, session 24)"
findings_scanned: 76
findings_filtered: 1
---

# Artifact Identification Report — 2026-04-19 (Run 3 — Full P1)

**Scope:** All P1 findings (full production run, session 24)
**Findings scanned:** 76 | **Filtered out:** 1 (dedup: 0, weak: 0, adopted: 1 — hybrid-upfront-and-jit-context-architecture)
**Classified:** 75

**Note:** Session 23 reported 19 P1 findings — this was a quoted-grep bug (`"P1 (Implement Now)"` missed unquoted YAML values). Actual P1 count is 76.

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | 69 | 92.0% | 48 | 21 | 0 |
| rule | 3 | 4.0% | 2 | 1 | 0 |
| skill | 1 | 1.3% | 1 | 0 | 0 |
| template | 1 | 1.3% | 1 | 0 | 0 |
| agent | 0 | 0% | 0 | 0 | 0 |

**Human review applied:** 2 findings redirected after Nick's review: `intent-engineering-framework` template→pattern (codify the shape first, extract templates downstream), `progressive-search` skill→pattern (starts as a design approach). `system-event-logging` confirmed as rule.

**Distribution analysis:** 92.0% pattern matches calibration baseline (92%). Non-pattern forms: 3 rules, 1 skill, 1 template. Zero agents — every multi-role finding correctly resolved to pattern via DD-76.

## Candidates

### GUIDED — Review Recommended (21)

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 1 | [[ace-delta-updates-over-monolithic-rewrites]] | pattern | MED | — | PENDING |
| 2 | [[agent-context-kiss-commandments-minimum-viable]] | pattern | MED | — | PENDING |
| 3 | [[claude-code-hooks-for-automatic-session-memory]] | pattern | MED | skill | PENDING |
| 4 | [[context-enrichment-for-task-clarity]] | pattern | MED | — | PENDING |
| 5 | [[context-rot-silent-killer-and-mitigations]] | pattern | MED | — | PENDING |
| 6 | [[document-sharding-for-context-efficiency]] | pattern | MED | — | PENDING |
| 7 | [[git-status-context-injection-token-hygiene]] | pattern | MED | — | PENDING |
| 8 | [[gstack-four-layer-prompt-injection-defense]] | pattern | MED | — | PENDING |
| 9 | [[independent-eval-and-scoped-authority-commandments]] | pattern | MED | — | PENDING |
| 10 | [[intent-engineering-framework-seven-part-agent-inten]] | pattern | MED | — | REDIRECTED |
| 11 | [[pass-at-k-vs-pass-caret-k-eval-metrics]] | pattern | MED | — | PENDING |
| 12 | [[programmatic-tool-calling-code-orchestrated-tool-use]] | pattern | MED | — | PENDING |
| 13 | [[progressive-search-wide-then-narrow]] | pattern | MED | — | REDIRECTED |
| 14 | [[review-bandwidth-as-organizational-bottleneck]] | pattern | MED | — | PENDING |
| 15 | [[spec-first-agent-briefs-prompt-craft-context-inten]] | pattern | MED | — | PENDING |
| 16 | [[system-event-logging-actions-not-words]] | rule | MED | — | PENDING |
| 17 | [[task-specific-model-routing-table-march-2026-bench]] | pattern | MED | — | PENDING |
| 18 | [[test-output-design-for-llm-context]] | pattern | MED | — | PENDING |
| 19 | [[three-tier-grading-hierarchy]] | pattern | MED | — | PENDING |
| 20 | [[ultra-review-multi-agent-bug-hunting-fleet]] | pattern | MED | — | PENDING |
| 21 | [[verification-agent-seven-prompt-patterns]] | pattern | MED | — | PENDING |

### AUTO — Ready for Extraction (54)

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 22 | [[acceptance-criteria-as-verifiable-eval-anchor]] | pattern | HIGH | — | PENDING |
| 23 | [[ace-agentic-context-engineering-evolving-playbook]] | pattern | HIGH | — | PENDING |
| 24 | [[advisor-executor-api-pattern]] | pattern | HIGH | — | PENDING |
| 25 | [[agent-self-reporting-unreliability-independent-eval]] | rule | HIGH | — | PENDING |
| 26 | [[autonomy-gradient-not-binary-delegation]] | pattern | HIGH | — | PENDING |
| 27 | [[binary-eval-assertion-design-deterministic-plus-ll]] | pattern | HIGH | — | PENDING |
| 28 | [[capability-saturation-threshold-45-percent]] | pattern | HIGH | — | PENDING |
| 29 | [[claude-code-12-agent-primitives]] | pattern | HIGH | — | PENDING |
| 30 | [[claude-code-auto-mode-ai-driven-permission-classif]] | pattern | HIGH | — | PENDING |
| 31 | [[claude-code-loop-in-session-cron-scheduling]] | pattern | HIGH | — | PENDING |
| 32 | [[claude-code-skills-20-four-mode-skill-lifecycle-wi]] | pattern | HIGH | — | PENDING |
| 33 | [[claude-code-ultra-plan-three-mode-planning]] | pattern | HIGH | — | PENDING |
| 34 | [[compounding-knowledge-loop-internal-data]] | pattern | HIGH | — | PENDING |
| 35 | [[context-curation-over-context-stuffing]] | pattern | HIGH | — | PENDING |
| 36 | [[context-file-instruction-bloat-eth-zurich]] | pattern | HIGH | — | PENDING |
| 37 | [[context-pollution-same-window-verification-bias]] | pattern | HIGH | — | PENDING |
| 38 | [[context-rot-attention-budget-depletion]] | pattern | HIGH | — | PENDING |
| 39 | [[effort-scaling-rules-embedded-in-orchestrator]] | pattern | HIGH | — | PENDING |
| 40 | [[eval-awareness-autonomous-benchmark-identification]] | pattern | HIGH | — | PENDING |
| 41 | [[extract-deep-plan-prompt-as-custom-skill]] | skill | HIGH | — | PENDING |
| 42 | [[file-based-task-locking-parallel-agents]] | pattern | HIGH | — | PENDING |
| 43 | [[fundamental-limits-of-single-vector-embedding-retr]] | pattern | HIGH | — | PENDING |
| 44 | [[gpt-54-tool-search-deferred-tool-loading]] | pattern | HIGH | — | PENDING |
| 45 | [[ground-truth-environmental-feedback-loops]] | pattern | HIGH | — | PENDING |
| 46 | [[health-metrics-vs-hard-constraints-distinction]] | pattern | HIGH | — | PENDING |
| 47 | [[ide-first-claude-code-with-deterministic-hooks]] | pattern | HIGH | — | PENDING |
| 48 | [[incremental-one-feature-per-session-pattern]] | pattern | HIGH | — | PENDING |
| 49 | [[infrastructure-noise-agentic-eval-confounding]] | pattern | HIGH | — | PENDING |
| 50 | [[karpathy-llm-knowledge-base-obsidian-rag]] | pattern | HIGH | — | PENDING |
| 51 | [[l-d-hypothesis-information-loss-across-agent-bound]] | pattern | HIGH | — | PENDING |
| 52 | [[legitimate-multi-agent-domains-taxonomy]] | pattern | HIGH | — | PENDING |
| 53 | [[mcp-as-code-api-progressive-tool-discovery]] | pattern | HIGH | — | PENDING |
| 54 | [[model-agnostic-prompting-three-properties]] | pattern | HIGH | — | PENDING |
| 55 | [[os-level-agent-sandboxing-filesystem-network-isolation]] | pattern | HIGH | — | PENDING |
| 56 | [[planner-executor-deterministic-guardrails]] | pattern | HIGH | — | PENDING |
| 57 | [[poka-yoke-error-proof-tool-interfaces]] | pattern | HIGH | — | PENDING |
| 58 | [[prompt-caching-for-stable-agent-context]] | pattern | HIGH | — | PENDING |
| 59 | [[reasoning-model-anti-pattern-prescribed-reasoning]] | rule | HIGH | — | PENDING |
| 60 | [[review-obsolescence-as-design-goal]] | pattern | HIGH | — | PENDING |
| 61 | [[scrum-master-story-contextualization]] | pattern | HIGH | — | PENDING |
| 62 | [[session-persistence-crash-resilient]] | pattern | HIGH | — | PENDING |
| 63 | [[specialization-theater-anti-pattern]] | pattern | HIGH | — | PENDING |
| 64 | [[task-contract-pattern-schema-first-agent]] | pattern | HIGH | — | PENDING |
| 65 | [[teach-orchestrator-to-delegate-pattern]] | pattern | HIGH | — | PENDING |
| 66 | [[tech-stack-pinning-table-for-drift-prevention]] | template | HIGH | — | PENDING |
| 67 | [[think-tool-scratchpad-for-mid-chain-reasoning]] | pattern | HIGH | — | PENDING |
| 68 | [[tiered-permission-system-bash-safety]] | pattern | HIGH | — | PENDING |
| 69 | [[token-waste-taxonomy-and-two-mode-workflow]] | pattern | HIGH | — | PENDING |
| 70 | [[tool-registry-metadata-first-design]] | pattern | HIGH | — | PENDING |
| 71 | [[tool-shaped-object-evaluation-lens]] | pattern | HIGH | — | PENDING |
| 72 | [[two-level-verification-agent-run-plus-harness-inte]] | pattern | HIGH | — | PENDING |
| 73 | [[volume-over-quality-eval-principle]] | pattern | HIGH | — | PENDING |
| 74 | [[workflow-state-vs-conversation-state]] | pattern | HIGH | — | PENDING |
| 75 | [[worktree-isolation-for-parallel-agent-sessions]] | pattern | HIGH | — | PENDING |

## Non-Pattern Details

### Rules (3)

#### 25. agent-self-reporting-unreliability-independent-eval
- **Assigned form:** rule
- **Confidence:** HIGH | **Tier:** auto
- **Reason codes:** must-never-language, deterministic-check, enforcement-boundary, binary-pass-fail
- **Rationale:** Binary constraint: agent self-report MUST NOT substitute for independent evaluation. Deterministic check — does your eval depend on agent self-report? Clear enforcement boundary at eval architecture design. No tradeoffs; the $14K case study confirms the conclusion is unambiguous.
- **Status:** APPROVED

#### 51. reasoning-model-anti-pattern-prescribed-reasoning
- **Assigned form:** rule
- **Confidence:** HIGH | **Tier:** auto
- **Reason codes:** must-not, deterministic-check, binary-pass-fail, enforcement-boundary, anti-pattern-expressible-as-check
- **Rationale:** Five techniques categorically forbidden on reasoning models. Deterministic check possible (string match for CoT markers). Satisfies every rule inclusion criterion. Rubric anti-pattern clause applies directly.
- **Status:** APPROVED

#### 16. system-event-logging-actions-not-words
- **Assigned form:** rule
- **Confidence:** MED | **Tier:** guided
- **Reason codes:** deterministic-check, enforcement-boundary
- **Rationale:** Core claim is a binary enforcement boundary: log what the agent DID not just said — deterministic pass/fail at audit time. MED because tradeoff language (volume, privacy) and "easy to add now" framing give it mild pattern pull.
- **Status:** APPROVED

### Skills (2)

#### 41. extract-deep-plan-prompt-as-custom-skill
- **Assigned form:** skill
- **Confidence:** HIGH | **Tier:** auto
- **Reason codes:** ordered-steps, defined-inputs-outputs, explicit-invocation, stateless
- **Rationale:** The extraction-and-packaging procedure IS the insight — without the procedure there is no value. Defined I/O (system prompt in, packaged skill out). Fails the pattern litmus test: insight does not survive removal of the mechanism.
- **Status:** APPROVED

#### 13. progressive-search-wide-then-narrow
- **Assigned form:** pattern (REDIRECTED from skill)
- **Confidence:** MED | **Tier:** guided
- **Reason codes:** ordered-steps, explicit-invocation, stateless, defined-io
- **Rationale:** Sonnet classified as skill (ordered broad→narrow steps). Nick redirected to pattern: the insight is a reusable research strategy shape ("start broad, narrow progressively") that can be instantiated differently across contexts. The specific step sequence is one instantiation. Starts as a design approach; skills can be derived downstream.
- **Status:** REDIRECTED

### Templates (2)

#### 66. tech-stack-pinning-table-for-drift-prevention
- **Assigned form:** template
- **Confidence:** HIGH | **Tier:** auto
- **Reason codes:** scaffold, named-variables, repeatable-generation, build-artifact
- **Rationale:** Fillable scaffold — tech/version/rationale table loaded on every execution. Named variables and repeatable generation are defining signals. The form is a concrete artifact, not a reusable design shape.
- **Status:** APPROVED

#### 10. intent-engineering-framework-seven-part-agent-inten
- **Assigned form:** pattern (REDIRECTED from template)
- **Confidence:** MED | **Tier:** guided
- **Reason codes:** scaffold, named-variables, repeatable-generation
- **Rationale:** Sonnet classified as template (seven named slots producing a repeatable artifact). Nick redirected to pattern: the meta-insight ("intent determines behavior when instructions run out") is the center of gravity. The seven-part scaffold is a downstream template harvestable by `/extract-artifacts`. Codify the shape first, extract templates later.
- **Calibration note:** Calibration set (row 44) agrees — pattern (HIGH/auto). "Framework trap noted."
- **Status:** APPROVED

## Calibration Cross-Check

19 of 75 findings appear in the 50-finding calibration set. Results:

| Finding | This Run | Calibration | Match |
|---------|----------|-------------|-------|
| acceptance-criteria | pattern HIGH | pattern HIGH | YES |
| advisor-executor-api | pattern HIGH | pattern HIGH | YES |
| binary-eval-assertion | pattern HIGH | pattern HIGH | YES |
| context-rot-attention | pattern HIGH | pattern MED | YES (form) |
| effort-scaling-rules | pattern HIGH | pattern HIGH | YES |
| extract-deep-plan | skill HIGH | skill HIGH | YES |
| file-based-task-locking | pattern HIGH | pattern HIGH | YES |
| fundamental-limits-embedding | pattern HIGH | — | N/A |
| intent-engineering-framework | template MED | pattern HIGH | **DISAGREE** |
| model-agnostic-prompting | pattern HIGH | pattern HIGH | YES |
| os-level-sandboxing | pattern HIGH | pattern HIGH | YES |
| planner-executor | pattern HIGH | pattern HIGH | YES |
| poka-yoke | pattern HIGH | pattern HIGH | YES |
| prompt-caching | pattern HIGH | pattern HIGH | YES |
| reasoning-model-anti-pattern | rule HIGH | rule MED | YES (form) |
| task-contract-pattern | pattern HIGH | pattern HIGH | YES |
| tech-stack-pinning | template HIGH | template HIGH | YES |
| think-tool-scratchpad | pattern HIGH | pattern HIGH | YES |
| three-tier-grading | pattern MED | pattern HIGH | YES (form) |
| tiered-permission | pattern HIGH | pattern HIGH | YES |
| volume-over-quality | pattern HIGH | pattern HIGH | YES |
| workflow-state | pattern HIGH | pattern HIGH | YES |
| worktree-isolation | — | — | N/A |

**18/19 form match (94.7%).** One disagreement (`intent-engineering-framework`) flagged for human review.
