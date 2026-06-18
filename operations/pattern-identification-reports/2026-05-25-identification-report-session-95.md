---
title: "Artifact Identification Report — Session 95 Re-Extraction"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-05-25"
scope: "100 new findings from session 95 re-extraction of 15 under-extracted video sources (90 classified after filtering)"
findings_scanned: 101
findings_filtered: 11
---

# Artifact Identification Report — 2026-05-25

**Scope:** Session 95 re-extraction findings (tagged `session-95-reextract`)
**Findings scanned:** 101 | **Filtered out:** 11 (dedup: 0, weak/anecdotal: 6, adopted: 5)
**Classified:** 90

## Summary

| Form | Count (pre-review) | Count (post-review) | Auto | Guided |
|------|---------------------|---------------------|------|--------|
| pattern | 75 | 83 | 54 | 29 |
| rule | 10 | 6 | 4 | 2 |
| skill | 4 | 1 | 1 | 0 |
| template | 1 | 0 | 0 | 0 |
| agent | 0 | 0 | 0 | 0 |

**Tier totals:** 59 auto, 31 guided, 0 hitl
**Review outcome (session 96):** 23 APPROVED, 8 REDIRECTED (4 rules→pattern, 3 skills→pattern, 1 template→pattern)

Guide routing: All 90 classified findings map to existing guide clusters via their category → dimension → guide mapping. 0 unrouted.

## Candidates

### GUIDED — Review Recommended (31)

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 1 | agent-description-auto-dispatch-routing | pattern | MED | rule | APPROVED |
| 2 | ai-delegated-knowledge-organization | pattern | MED | skill | APPROVED |
| 3 | ai-shepherding-anti-pattern-manual-workflow-sequencing | pattern | MED | rule | APPROVED |
| 4 | context-assembly-cost-as-strategy-blocker | pattern | MED | — | APPROVED |
| 5 | cross-system-permission-composition-audit-gap | pattern | MED | rule | APPROVED |
| 6 | description-based-workflow-routing-lazy-dispatch | pattern | MED | skill | APPROVED |
| 7 | error-aware-backtracking-as-compound-error-mitigation | pattern | MED | rule | APPROVED |
| 8 | external-ticket-as-brainstorm-seed | pattern | MED | skill | APPROVED |
| 9 | file-search-outperforms-rag-for-small-corpora | pattern | MED | rule | APPROVED |
| 10 | html-mockup-generation-as-brainstorm-artifact | pattern | MED | skill | APPROVED |
| 11 | implementation-is-strategy-for-agentic-systems | pattern | MED | rule | APPROVED |
| 12 | interactive-debug-panel-event-type-filtering | pattern | MED | skill | APPROVED |
| 13 | monitoring-agent-failure-detection-autonomous-repair | pattern | MED | agent | APPROVED |
| 14 | pattern-scale-signals-systemic-not-individual-failure | pattern | MED | rule | APPROVED |
| 15 | per-query-production-eval-pipeline | pattern | MED | rule | APPROVED |
| 16 | permission-compounding-across-agent-delegation-chains | pattern | MED | rule | APPROVED |
| 17 | pr-acceptance-rate-harness-multiplier-evidence | pattern | MED | — | APPROVED |
| 18 | scheduled-skill-chaining-with-file-based-activation | pattern | MED | skill | APPROVED |
| 19 | skills-portability-across-sdk-and-framework-boundaries | pattern | MED | — | APPROVED |
| 20 | supervision-debt-anti-pattern | pattern | MED | — | APPROVED |
| 21 | tdd-step-ordering-in-plan-tasks | pattern | MED | template | APPROVED |
| 22 | credential-setup-outside-llm-context-window | rule | MED | pattern | APPROVED |
| 23 | mcp-high-trust-design-assumption | ~~rule~~ pattern | MED | — | REDIRECTED |
| 24 | plan-implement-session-separation-bias-removal | ~~rule~~ pattern | MED | — | REDIRECTED |
| 25 | tool-access-as-security-boundary-not-feature-toggle | ~~rule~~ pattern | MED | — | REDIRECTED |
| 26 | total-organizational-legibility-as-ai-prerequisite | ~~rule~~ pattern | MED | — | REDIRECTED |
| 27 | untyped-links-as-token-waste-anti-pattern | rule | MED | pattern | APPROVED |
| 28 | html-first-prototyping-with-parameter-tuning | ~~skill~~ pattern | MED | — | REDIRECTED |
| 29 | nl-description-to-agent-spec-creation-loop | ~~skill~~ pattern | MED | — | REDIRECTED |
| 30 | three-question-protocol-selection-framework | ~~skill~~ pattern | MED | — | REDIRECTED |
| 31 | html-pr-explainer-with-margin-annotations | ~~template~~ pattern | MED | — | REDIRECTED |

### AUTO — Ready for Extraction (59)

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 32 | agent-action-reversibility-as-design-requirement | pattern | HIGH | rule | PENDING |
| 33 | agent-as-hosted-backend-passthrough-architecture | pattern | HIGH | — | PENDING |
| 34 | agent-aware-api-surface-design | pattern | HIGH | rule | PENDING |
| 35 | agent-environment-vault-triple-lifecycle-mismatch | pattern | HIGH | — | PENDING |
| 36 | agent-infrastructure-glue-code-elimination-via-sdk | pattern | HIGH | — | PENDING |
| 37 | agentic-rag-multi-strategy-retrieval-2026 | pattern | HIGH | — | PENDING |
| 38 | ai-as-primary-reader-design-principle | pattern | HIGH | — | PENDING |
| 39 | anti-slop-reliability-standard-first-try-quality | pattern | HIGH | — | PENDING |
| 40 | atomic-agent-provisioning-bundle-create-pattern | pattern | HIGH | — | PENDING |
| 41 | built-in-sub-agent-triad-explore-plan-general | pattern | HIGH | — | PENDING |
| 42 | coding-agent-sdk-as-non-coding-agent-foundation | pattern | HIGH | — | PENDING |
| 43 | coordination-cost-vs-flexibility-tradeoff-agent-delegation | pattern | HIGH | — | PENDING |
| 44 | cross-project-workflow-portability-register-and-run | pattern | HIGH | — | PENDING |
| 45 | default-workflow-library-as-adoption-accelerator | pattern | HIGH | — | PENDING |
| 46 | environment-grounded-context-as-output-quality-multiplier | pattern | HIGH | — | PENDING |
| 47 | execution-topology-as-runtime-selection | pattern | HIGH | — | PENDING |
| 48 | finite-training-generalization-via-error-recovery | pattern | HIGH | — | PENDING |
| 49 | five-pattern-complexity-escalation-ladder | pattern | HIGH | — | PENDING |
| 50 | format-constrained-improvisation-tax | pattern | HIGH | — | PENDING |
| 51 | headless-cron-composition-autonomous-scheduled-workflows | pattern | HIGH | — | PENDING |
| 52 | html-information-density-eight-primitives-vs-markdown-four | pattern | HIGH | — | PENDING |
| 53 | html-output-as-human-in-the-loop-restorer | pattern | HIGH | — | PENDING |
| 54 | hub-and-spoke-10-agent-ceiling-with-queueing | pattern | HIGH | — | PENDING |
| 55 | human-to-ai-knowledge-architecture-migration | pattern | HIGH | — | PENDING |
| 56 | knowledge-graph-as-persistent-institutional-memory | pattern | HIGH | — | PENDING |
| 57 | lossy-compression-boundary-headless-return | pattern | HIGH | — | PENDING |
| 58 | meta-agent-prompt-generation-bootstrap-pattern | pattern | HIGH | — | PENDING |
| 59 | meta-workflow-builder-self-extending-harness | pattern | HIGH | — | PENDING |
| 60 | multi-adapter-workflow-invocation-cli-web-chat-github | pattern | HIGH | — | PENDING |
| 61 | oauth-first-zero-touch-credential-onboarding | pattern | HIGH | — | PENDING |
| 62 | operating-surface-underspecification-anti-pattern | pattern | HIGH | — | PENDING |
| 63 | output-format-token-cost-reframed-by-context-window-size | pattern | HIGH | — | PENDING |
| 64 | parallel-independent-workflow-execution-at-scale | pattern | HIGH | — | PENDING |
| 65 | per-function-recursive-loop-composition | pattern | HIGH | template | PENDING |
| 66 | per-node-context-scoping-skills-mcps-commands | pattern | HIGH | — | PENDING |
| 67 | phase-queue-state-file-as-orchestrator-memory | pattern | HIGH | — | PENDING |
| 68 | progressive-diorization-pipeline-raw-to-breadcrumb | pattern | HIGH | — | PENDING |
| 69 | protocol-substrate-shapes-customer-experience | pattern | HIGH | — | PENDING |
| 70 | review-triggered-remediation-dispatch | pattern | HIGH | — | PENDING |
| 71 | sdk-to-framework-graduation-path | pattern | HIGH | — | PENDING |
| 72 | self-contained-phase-prompt-pattern | pattern | HIGH | — | PENDING |
| 73 | self-improving-knowledge-artifact-living-document | pattern | HIGH | — | PENDING |
| 74 | shared-context-folder-as-cross-skill-update-multiplier | pattern | HIGH | — | PENDING |
| 75 | skill-phase-pipeline-shared-session-orchestrator | pattern | HIGH | — | PENDING |
| 76 | standardized-io-as-infrastructure-scaling-prerequisite | pattern | HIGH | — | PENDING |
| 77 | subagent-as-uniform-tool-interface | pattern | HIGH | — | PENDING |
| 78 | summary-gate-agent-traversal-pattern | pattern | HIGH | — | PENDING |
| 79 | taste-and-craft-as-post-llm-differentiator | pattern | HIGH | — | PENDING |
| 80 | text-vs-visual-comprehension-gap-agent-platforms | pattern | HIGH | — | PENDING |
| 81 | three-layer-core-agent-protocol-stack | pattern | HIGH | — | PENDING |
| 82 | three-tier-orchestration-hierarchy-scheduler-worker-framework | pattern | HIGH | — | PENDING |
| 83 | tiered-interaction-model-quick-ask-vs-supervisor | pattern | HIGH | — | PENDING |
| 84 | token-economics-as-architecture-driver | pattern | HIGH | — | PENDING |
| 85 | visible-quality-as-trust-proxy-for-invisible-work | pattern | HIGH | — | PENDING |
| 86 | build-loop-skill-autonomous-phase-driver | skill | HIGH | — | PENDING |
| 87 | instant-agent-revocation-kill-switch-pattern | rule | HIGH | — | PENDING |
| 88 | scoped-environment-network-allowlist-governance | rule | HIGH | — | PENDING |
| 89 | secure-by-default-posture-as-organizational-invariant | rule | HIGH | — | PENDING |
| 90 | subscription-tos-single-user-boundary-for-agent-sdks | rule | HIGH | — | PENDING |

## Details

### Non-Pattern Classifications (15 findings — review these first)

#### Rules (10)

**87. instant-agent-revocation-kill-switch-pattern** — rule HIGH auto
- Four non-negotiable requirements (immediate, console-accessible, granular, auditable) with binary diagnostic test. Enforcement boundary: identity/credential layer.

**88. scoped-environment-network-allowlist-governance** — rule HIGH auto
- Hosted agent environments MUST declare explicit network allowlists; default MUST be deny-all. Enforcement boundary: environment provisioning.

**89. secure-by-default-posture-as-organizational-invariant** — rule HIGH auto
- Systems MUST default to deny when security is not configured. Binary test: what happens when nobody touches security settings?

**90. subscription-tos-single-user-boundary-for-agent-sdks** — rule HIGH auto
- SDK subscription plans MUST NOT serve multiple users. Deterministic legal/deployment boundary.

**22. credential-setup-outside-llm-context-window** — rule MED guided
- Credentials MUST NOT enter the LLM context window. Co-occurrence with pattern (vault proxy vs. separate terminal alternatives).

**23. mcp-high-trust-design-assumption** — rule MED guided
- Never treat MCP standardization as equivalent to security; always layer separate enforcement. Co-occurrence with pattern (MCP-for-discovery architecture).

**24. plan-implement-session-separation-bias-removal** — rule MED guided
- Planning and implementation should happen in different sessions. Exceptions for small tasks weaken binary character.

**25. tool-access-as-security-boundary-not-feature-toggle** — rule MED guided
- MCP server enablement is a security boundary crossing requiring four mitigations. Co-occurrence with pattern.

**26. total-organizational-legibility-as-ai-prerequisite** — rule MED guided
- "If it is not recorded, it did not happen to your intelligence." Binary prerequisite for self-improving loops.

**27. untyped-links-as-token-waste-anti-pattern** — rule MED guided
- Untyped links in AI-read KBs are wrong; typed links are correct. Enforcement at link-creation boundary.

#### Skills (4)

**86. build-loop-skill-autonomous-phase-driver** — skill HIGH auto
- 7-step procedure with explicit I/O (phase-queue state file → all phases complete). Triggerable as single command.

**28. html-first-prototyping-with-parameter-tuning** — skill MED guided
- Three ordered steps (sketch HTML, tune with sliders, copy parameters). Co-occurrence with pattern (HTML as universal prototype medium).

**29. nl-description-to-agent-spec-creation-loop** — skill MED guided
- 8-step loop: describe → generate spec → review → provision → test → observe → modify → redeploy. Co-occurrence with pattern (spec-as-durable-artifact).

**30. three-question-protocol-selection-framework** — skill MED guided
- Ordered checklist of 3 questions applied per workflow to select protocols. Co-occurrence with pattern (the three-layer stack).

#### Templates (1)

**31. html-pr-explainer-with-margin-annotations** — template MED guided
- Repeatable scaffold with named variables (diff content, annotations, severity colors, jump links). Co-occurrence with pattern (HTML-as-review-restorer).

## Session 96 Review — Redirection Rationale

**Reviewer:** Codifier (session 96)
**Rubric applied:** `operations/references/form-classification-rubric.md`
**Principle:** Center-of-gravity test — the form should capture the finding's primary insight, not its secondary expressions.

### Redirected Rules → Pattern (4)

| # | Finding | Reason |
|---|---------|--------|
| 23 | mcp-high-trust-design-assumption | Architectural insight ("MCP for discovery, separate enforcement layer") is a compositional primitive. The "never conflate standardization with security" is a mindset requiring judgment, not a deterministic check at a boundary. |
| 24 | plan-implement-session-separation-bias-removal | Explicit exceptions for small tasks destroy binary character. Insight is the design approach (session separation to eliminate planning bias) with tradeoffs — pattern's "it depends" character. |
| 25 | tool-access-as-security-boundary-not-feature-toggle | Four mitigations framework + mental model shift. No single deterministic check; requires architectural assessment. Answers "how should I structure tool access governance?" |
| 26 | total-organizational-legibility-as-ai-prerequisite | Philosophical prerequisite about organizational design. No enforcement boundary, no deterministic check. Answers "how should I think about organizing for AI?" |

### Redirected Skills → Pattern (3)

| # | Finding | Reason |
|---|---------|--------|
| 28 | html-first-prototyping-with-parameter-tuning | 3 steps are an instantiation of "HTML as universal parameter-capture tool." Insight is the design principle, not the procedure. Multiple implementations could follow different steps. |
| 29 | nl-description-to-agent-spec-creation-loop | 8-step loop is platform-specific (Anthropic managed agents). Generalizable insight is the NL→spec→test→refine design approach — a compositional primitive for agent creation UX. |
| 30 | three-question-protocol-selection-framework | Three questions are conceptual lenses requiring significant cognitive judgment, not mechanical steps. Decision framework for protocol selection = pattern. |

### Redirected Template → Pattern (1)

| # | Finding | Reason |
|---|---------|--------|
| 31 | html-pr-explainer-with-margin-annotations | Template form (`{{DIFF}} + {{ANNOTATIONS}} → HTML`) loses the insight — why margin annotations + severity colors + jump links improve review quality. The design principle is the value, not the scaffold. |

### Approved Non-Pattern Findings (for extraction)

Post-review, 7 findings remain non-pattern (6 rules + 1 skill):
- **Rules:** #22 credential-setup-outside-llm-context-window (MED), #27 untyped-links-as-token-waste-anti-pattern (MED), #87 instant-agent-revocation-kill-switch-pattern (HIGH), #88 scoped-environment-network-allowlist-governance (HIGH), #89 secure-by-default-posture-as-organizational-invariant (HIGH), #90 subscription-tos-single-user-boundary-for-agent-sdks (HIGH)
- **Skills:** #86 build-loop-skill-autonomous-phase-driver (HIGH)

---

## Filtered Findings (11)

### Already Adopted (5)
- agent-harness-distributed-system-mental-model
- context-before-loop-initialization-sequence
- context-first-build-sequencing-for-agentic-systems
- minimal-agent-harness-skeleton-three-primitives
- platform-native-harness-over-agent-frameworks

### Weak/Anecdotal Evidence (6)
- brain-boundary-architecture-humans-at-periphery
- copilot-to-autonomous-leap-design-milestone
- greenfield-brownfield-framework-selection-heuristic
- role-voting-for-autonomous-design-decisions
- token-budget-as-headcount-replacement-resource-model
- typed-edge-knowledge-graph-token-reduction
