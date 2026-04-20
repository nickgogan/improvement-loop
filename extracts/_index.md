---
title: "Extracted Artifacts"
type: "index"
target_system:
  - "improvement-loop"
created: "2026-04-19"
updated: "2026-04-20"
---

# Extracted Artifacts

Staged artifacts produced by `/extract-artifacts` from research findings. Each artifact is classified into one of 5 forms and carries a ContractSpec (DD-78). Artifacts here are **not yet deployed** — deployment to enforcement locations (`.claude/rules/`, `meta-system/knowledge/`, etc.) is a separate human-gated act.

**Pipeline position:** Research Finding -> `/extract-artifacts` -> **here** -> [human deploy] -> enforcement location

**Design Decision:** DD-80 (pipeline simplification)

## Subdirectories

| Directory | Form | Deployment Target |
|-----------|------|-------------------|
| `rules/` | Binary constraint enforced at a boundary | `.claude/rules/` or `{system}/governance/` |
| `templates/` | Scaffold with variables and a body | `meta-system/knowledge/templates/` |
| `agents/` | Persona with cognitive disposition and durable scope | `meta-system/knowledge/templates/agent-templates/` |
| `skills/` | Procedure with inputs/outputs/steps | `.claude/skills/` |
| `patterns/` | Sub-patterns derived from parent patterns | `meta-system/knowledge/patterns/` |
| `guides/` | End-directed guides synthesized from pattern clusters | `meta-system/knowledge/guides/` |

## Catalog

| Artifact | Form | Source Finding | Date | Deployed |
|----------|------|---------------|------|----------|
| [Acceptance Criteria as Verifiable Eval Anchor](patterns/acceptance-criteria-as-verifiable-eval-anchor.md) | pattern | [[acceptance-criteria-as-verifiable-eval-anchor]] | 2026-04-19 | No |
| [Agentic Context Engineering -- Evolving Playbook](patterns/ace-agentic-context-engineering-evolving-playbook.md) | pattern | [[ace-agentic-context-engineering-evolving-playbook]] | 2026-04-19 | No |
| [Adversarial Verification Agent Prompt Patterns](patterns/adversarial-verification-agent-prompt-patterns.md) | pattern | [[verification-agent-seven-prompt-patterns]] | 2026-04-19 | No |
| [Advisor-Executor API Pattern](patterns/advisor-executor-api-pattern.md) | pattern | [[advisor-executor-api-pattern]] | 2026-04-19 | No |
| [Agent Self-Reporting Unreliability](rules/agent-self-reporting-unreliability-independent-eval.md) | rule | [[agent-self-reporting-unreliability-independent-eval]] | 2026-04-19 | No |
| [Autonomy Gradient (Not Binary Delegation)](patterns/autonomy-gradient-not-binary-delegation.md) | pattern | [[autonomy-gradient-not-binary-delegation]] | 2026-04-19 | No |
| [Binary Eval Assertion Design](patterns/binary-eval-assertion-design-deterministic-plus-llm.md) | pattern | [[binary-eval-assertion-design-deterministic-plus-ll]] | 2026-04-19 | No |
| [Capability Saturation Threshold](patterns/capability-saturation-threshold.md) | pattern | [[capability-saturation-threshold-45-percent]] | 2026-04-19 | No |
| [Code-Orchestrated Tool Execution](patterns/programmatic-tool-calling-code-orchestrated-tool-use.md) | pattern | [[programmatic-tool-calling-code-orchestrated-tool-use]] | 2026-04-19 | No |
| [Compounding Knowledge Loop](patterns/compounding-knowledge-loop.md) | pattern | [[compounding-knowledge-loop-internal-data]] | 2026-04-19 | No |
| [Context Curation Over Context Stuffing](patterns/context-curation-over-stuffing.md) | pattern | [[context-curation-over-context-stuffing]] | 2026-04-19 | No |
| [Context Enrichment for Task Clarity](patterns/context-enrichment-for-task-clarity.md) | pattern | [[context-enrichment-for-task-clarity]] | 2026-04-19 | No |
| [Context-Isolated Verification](patterns/context-isolated-verification.md) | pattern | [[context-pollution-same-window-verification-bias]] | 2026-04-19 | No |
| [Context Rot and Attention Budget Depletion](patterns/context-rot-attention-budget-depletion.md) | pattern | [[context-rot-attention-budget-depletion]] | 2026-04-19 | No |
| [Context Rot Detection and Mitigation](patterns/context-rot-detection-and-mitigation.md) | pattern | [[context-rot-silent-killer-and-mitigations]] | 2026-04-19 | No |
| [Deep Plan — 4-Agent Pipeline](skills/deep-plan-four-agent-pipeline.md) | skill | [[extract-deep-plan-prompt-as-custom-skill]] | 2026-04-19 | No |
| [Deferred Tool Loading](patterns/deferred-tool-loading.md) | pattern | [[gpt-54-tool-search-deferred-tool-loading]] | 2026-04-19 | No |
| [Delta Updates over Monolithic Rewrites](patterns/delta-updates-over-monolithic-rewrites.md) | pattern | [[ace-delta-updates-over-monolithic-rewrites]] | 2026-04-19 | No |
| [Document Sharding for Context Efficiency](patterns/document-sharding-for-context-efficiency.md) | pattern | [[document-sharding-for-context-efficiency]] | 2026-04-19 | No |
| [Dual-Metric Agent Reliability Evaluation](patterns/pass-at-k-vs-pass-caret-k-eval-metrics.md) | pattern | [[pass-at-k-vs-pass-caret-k-eval-metrics]] | 2026-04-19 | No |
| [Effort Scaling Rules Embedded in Orchestrator](patterns/effort-scaling-rules-embedded-in-orchestrator.md) | pattern | [[effort-scaling-rules-embedded-in-orchestrator]] | 2026-04-19 | No |
| [Eval Awareness: Autonomous Benchmark Identification](patterns/eval-awareness-autonomous-benchmark-identification.md) | pattern | [[eval-awareness-autonomous-benchmark-identification]] | 2026-04-19 | No |
| [File-Based Task Locking for Parallel Agents](patterns/file-based-task-locking-parallel-agents.md) | pattern | [[file-based-task-locking-parallel-agents]] | 2026-04-19 | No |
| [Four-Layer Prompt Injection Defense](patterns/four-layer-prompt-injection-defense.md) | pattern | [[gstack-four-layer-prompt-injection-defense]] | 2026-04-19 | No |
| [Four-Mode Skill Lifecycle](patterns/four-mode-skill-lifecycle.md) | pattern | [[claude-code-skills-20-four-mode-skill-lifecycle-wi]] | 2026-04-19 | No |
| [Fundamental Limits of Single-Vector Embedding Retrieval](patterns/fundamental-limits-of-single-vector-embedding-retrieval.md) | pattern | [[fundamental-limits-of-single-vector-embedding-retr]] | 2026-04-19 | No |
| [Git Status Context Injection Token Hygiene](patterns/git-status-context-injection-token-hygiene.md) | pattern | [[git-status-context-injection-token-hygiene]] | 2026-04-19 | No |
| [Ground-Truth Environmental Feedback Loops](patterns/ground-truth-environmental-feedback-loops.md) | pattern | [[ground-truth-environmental-feedback-loops]] | 2026-04-19 | No |
| [Health Metrics vs. Hard Constraints](patterns/health-metrics-vs-hard-constraints.md) | pattern | [[health-metrics-vs-hard-constraints-distinction]] | 2026-04-19 | No |
| [Hook-Based Automatic Session Memory](patterns/hook-based-automatic-session-memory.md) | pattern | [[claude-code-hooks-for-automatic-session-memory]] | 2026-04-19 | No |
| [IDE-First Workflow with Deterministic Hooks](patterns/ide-first-with-deterministic-hooks.md) | pattern | [[ide-first-claude-code-with-deterministic-hooks]] | 2026-04-19 | No |
| [In-Session Cron Scheduling](patterns/in-session-cron-scheduling.md) | pattern | [[claude-code-loop-in-session-cron-scheduling]] | 2026-04-19 | No |
| [Independent Evaluation and Scoped Authority](patterns/independent-eval-and-scoped-authority.md) | pattern | [[independent-eval-and-scoped-authority-commandments]] | 2026-04-19 | No |
| [Infrastructure Noise as Eval Confound](patterns/infrastructure-noise-eval-confound-control.md) | pattern | [[infrastructure-noise-agentic-eval-confounding]] | 2026-04-19 | No |
| [Instruction Bloat and Minimal Context Files](patterns/instruction-bloat-minimal-context-files.md) | pattern | [[context-file-instruction-bloat-eth-zurich]] | 2026-04-19 | No |
| [Intent Engineering Seven-Part Specification](patterns/intent-engineering-seven-part-specification.md) | pattern | [[intent-engineering-framework-seven-part-agent-inten]] | 2026-04-19 | No |
| [LLM-Compiled Knowledge Base over Vector RAG](patterns/llm-compiled-knowledge-base-over-vector-rag.md) | pattern | [[karpathy-llm-knowledge-base-obsidian-rag]] | 2026-04-19 | No |
| [Minimum Viable Agent Context](patterns/minimum-viable-agent-context.md) | pattern | [[agent-context-kiss-commandments-minimum-viable]] | 2026-04-19 | No |
| [Model-Agnostic Prompting -- Three Properties](patterns/model-agnostic-prompting-three-properties.md) | pattern | [[model-agnostic-prompting-three-properties]] | 2026-04-19 | No |
| [Multi-Agent Domain Taxonomy — Task Routing](patterns/multi-agent-domain-taxonomy-task-routing.md) | pattern | [[legitimate-multi-agent-domains-taxonomy]] | 2026-04-19 | No |
| [Multi-Agent Find-Verify-Dedup Pipeline](patterns/multi-agent-find-verify-dedup-pipeline.md) | pattern | [[ultra-review-multi-agent-bug-hunting-fleet]] | 2026-04-19 | No |
| [One Feature Per Session](patterns/one-feature-per-session.md) | pattern | [[incremental-one-feature-per-session-pattern]] | 2026-04-19 | No |
| [OS-Level Agent Sandboxing](patterns/os-level-agent-sandboxing-filesystem-network-isolation.md) | pattern | [[os-level-agent-sandboxing-filesystem-network-isolation]] | 2026-04-19 | No |
| [Planner-Executor with Deterministic Guardrails](patterns/planner-executor-deterministic-guardrails.md) | pattern | [[planner-executor-deterministic-guardrails]] | 2026-04-19 | No |
| [Poka-Yoke Error-Proof Tool Interfaces](patterns/poka-yoke-error-proof-tool-interfaces.md) | pattern | [[poka-yoke-error-proof-tool-interfaces]] | 2026-04-19 | No |
| [Progressive Search: Wide-Then-Narrow](patterns/progressive-search-wide-then-narrow.md) | pattern | [[progressive-search-wide-then-narrow]] | 2026-04-19 | No |
| [Progressive Tool Discovery via Filesystem](patterns/progressive-tool-discovery-via-filesystem.md) | pattern | [[mcp-as-code-api-progressive-tool-discovery]] | 2026-04-19 | No |
| [Prompt Caching for Stable Agent Context](patterns/prompt-caching-for-stable-agent-context.md) | pattern | [[prompt-caching-for-stable-agent-context]] | 2026-04-19 | No |
| [Reasoning-Blind Permission Classifier](patterns/reasoning-blind-permission-classifier.md) | pattern | [[claude-code-auto-mode-ai-driven-permission-classif]] | 2026-04-19 | No |
| [Reasoning Model Anti-Pattern](rules/reasoning-model-anti-pattern-prescribed-reasoning.md) | rule | [[reasoning-model-anti-pattern-prescribed-reasoning]] | 2026-04-19 | No |
| [Review Bandwidth Bottleneck Management](patterns/review-bandwidth-as-organizational-bottleneck.md) | pattern | [[review-bandwidth-as-organizational-bottleneck]] | 2026-04-19 | No |
| [Review Obsolescence as Design Goal](patterns/review-obsolescence-as-design-goal.md) | pattern | [[review-obsolescence-as-design-goal]] | 2026-04-19 | No |
| [Scrum Master Story Contextualization](patterns/scrum-master-story-contextualization.md) | pattern | [[scrum-master-story-contextualization]] | 2026-04-19 | No |
| [Session Persistence as Crash-Resilient State](patterns/session-persistence-crash-resilient.md) | pattern | [[session-persistence-crash-resilient]] | 2026-04-19 | No |
| [Single-Agent Default — L > D](patterns/single-agent-default-l-greater-than-d.md) | pattern | [[l-d-hypothesis-information-loss-across-agent-bound]] | 2026-04-19 | No |
| [Spec-First Agent Briefs](patterns/spec-first-agent-briefs-prompt-craft-context-inten.md) | pattern | [[spec-first-agent-briefs-prompt-craft-context-inten]] | 2026-04-19 | No |
| [Specialization Theater Anti-Pattern](patterns/specialization-theater-anti-pattern.md) | pattern | [[specialization-theater-anti-pattern]] | 2026-04-19 | No |
| [System Event Logging — Actions Not Words](rules/system-event-logging-actions-not-words.md) | rule | [[system-event-logging-actions-not-words]] | 2026-04-19 | No |
| [Task Contract Pattern: Schema-First](patterns/task-contract-pattern-schema-first-agent.md) | pattern | [[task-contract-pattern-schema-first-agent]] | 2026-04-19 | No |
| [Task-Specific Model Routing Table](patterns/task-specific-model-routing-table.md) | pattern | [[task-specific-model-routing-table-march-2026-bench]] | 2026-04-19 | No |
| [Teach Orchestrator to Delegate](patterns/teach-orchestrator-to-delegate-pattern.md) | pattern | [[teach-orchestrator-to-delegate-pattern]] | 2026-04-19 | No |
| [Tech Stack Pinning Table](templates/tech-stack-pinning-table.md) | template | [[tech-stack-pinning-table-for-drift-prevention]] | 2026-04-19 | No |
| [Test Output Design for LLM Context](patterns/test-output-design-for-llm-context.md) | pattern | [[test-output-design-for-llm-context]] | 2026-04-19 | No |
| [Think Tool Scratchpad for Mid-Chain Reasoning](patterns/think-tool-scratchpad-for-mid-chain-reasoning.md) | pattern | [[think-tool-scratchpad-for-mid-chain-reasoning]] | 2026-04-19 | No |
| [Three-Mode Cloud Planning](patterns/three-mode-cloud-planning.md) | pattern | [[claude-code-ultra-plan-three-mode-planning]] | 2026-04-19 | No |
| [Three-Tier Agent Primitive Architecture](patterns/three-tier-agent-primitive-architecture.md) | pattern | [[claude-code-12-agent-primitives]] | 2026-04-19 | No |
| [Three-Tier Eval Grading Hierarchy](patterns/three-tier-grading-hierarchy.md) | pattern | [[three-tier-grading-hierarchy]] | 2026-04-19 | No |
| [Tiered Permission System with Bash Safety](patterns/tiered-permission-system-bash-safety.md) | pattern | [[tiered-permission-system-bash-safety]] | 2026-04-19 | No |
| [Token Waste Taxonomy and Two-Mode Workflow](patterns/token-waste-taxonomy-and-two-mode-workflow.md) | pattern | [[token-waste-taxonomy-and-two-mode-workflow]] | 2026-04-19 | No |
| [Tool-Shaped Object Evaluation Lens](patterns/tool-shaped-object-evaluation-lens.md) | pattern | [[tool-shaped-object-evaluation-lens]] | 2026-04-19 | No |
| [Tool Registry with Metadata-First Design](patterns/tool-registry-metadata-first-design.md) | pattern | [[tool-registry-metadata-first-design]] | 2026-04-19 | No |
| [Two-Level Verification (Agent + Harness)](patterns/two-level-verification-agent-run-plus-harness-integrity.md) | pattern | [[two-level-verification-agent-run-plus-harness-inte]] | 2026-04-19 | No |
| [Volume Over Quality Eval Principle](patterns/volume-over-quality-eval-principle.md) | pattern | [[volume-over-quality-eval-principle]] | 2026-04-19 | No |
| [Workflow State vs. Conversation State](patterns/workflow-state-vs-conversation-state.md) | pattern | [[workflow-state-vs-conversation-state]] | 2026-04-19 | No |
| [Worktree Isolation for Parallel Agent Sessions](patterns/worktree-isolation-for-parallel-agent-sessions.md) | pattern | [[worktree-isolation-for-parallel-agent-sessions]] | 2026-04-19 | No |
| [Agentic Harness Self-Assessment (Design + Evaluation)](skills/agentic-harness-self-assessment.md) | skill | [[agentic-harness-self-assessment-skill]] | 2026-04-19 | No |
| [Balanced Positive and Negative Eval Sets](rules/balanced-positive-negative-eval-sets.md) | rule | [[balanced-positive-negative-eval-sets]] | 2026-04-19 | No |
| [Correct Course: Mid-Project Pivot Command](skills/correct-course-mid-project-pivot.md) | skill | [[correct-course-mid-project-pivot-command]] | 2026-04-19 | No |
| [Cross-Model Verification for Bug Finding](skills/cross-model-verification-for-bug-finding.md) | skill | [[cross-model-verification-for-bug-finding]] | 2026-04-19 | No |
| [Eval-Driven Tool Iteration Loop](skills/eval-driven-tool-iteration-loop.md) | skill | [[eval-driven-tool-iteration-loop]] | 2026-04-19 | No |
| [Execution Context Profiles — Mode Switching](templates/execution-context-profiles-mode-switching.md) | template | [[gsd-execution-context-profiles-mode-switching]] | 2026-04-19 | No |
| [File Read Deduplication](rules/file-read-deduplication.md) | rule | [[file-read-deduplication-pattern]] | 2026-04-19 | No |
| [Five Commandments for Agent Deployment](skills/five-commandments-agent-deployment.md) | skill | [[five-commandments-for-agent-deployment-audit-first]] | 2026-04-19 | No |
| [Fix Data and Schema Before Automating](rules/fix-data-schema-before-automating.md) | rule | [[fix-data-schema-before-automating]] | 2026-04-19 | No |
| [Initializer Agent Scaffolding](agents/initializer-agent-scaffolding.md) | agent | [[initializer-agent-scaffolding-pattern]] | 2026-04-19 | No |
| [One-Shot PRD Prompt for System Bootstrap](templates/one-shot-prd-prompt-for-system-bootstrap.md) | template | [[one-shot-prd-prompt-for-system-bootstrap]] | 2026-04-19 | No |
| [Post-Session Hooks for Autonomous Version Control](skills/post-session-hooks-autonomous-version-control.md) | skill | [[post-session-hooks-autonomous-version-control]] | 2026-04-19 | No |
| [Pre-Compression Identity Pinning](rules/pre-compression-identity-pinning.md) | rule | [[pre-compression-identity-pinning]] | 2026-04-19 | No |
| [Prompt Injection Scanner Hardening](skills/prompt-injection-scanner-hardening.md) | skill | [[gsd-prompt-injection-scanner-hardening]] | 2026-04-19 | No |
| [QA Agent — Independent Compliance Reviewer](agents/qa-agent-independent-compliance-review.md) | agent | [[qa-agent-independent-compliance-review]] | 2026-04-19 | No |
| [Stupid Button: Token Waste Self-Audit Diagnostic](skills/stupid-button-token-audit-diagnostic.md) | skill | [[stupid-button-six-question-token-audit-diagnostic]] | 2026-04-19 | No |
| [Thinking Models: Mental Framework Commands](skills/thinking-models-mental-framework-commands.md) | skill | [[thinking-models-mental-framework-commands-for-codi]] | 2026-04-19 | No |
| [Token Budget Pre-Turn Projection](rules/token-budget-pre-turn-projection.md) | rule | [[token-budget-pre-turn-projection]] | 2026-04-19 | No |
| [YAML Templates with Embedded Elicitation](templates/yaml-templates-with-embedded-elicitation.md) | template | [[yaml-templates-with-embedded-elicitation-instructions]] | 2026-04-19 | No |
| [Writing Agent Specifications](guides/writing-agent-specifications.md) | guide | 7 findings (P1 only) | 2026-04-19 | No |
| [Agent Safety and Permissions](guides/agent-safety-and-permissions.md) | guide | 5 findings (P1 only) | 2026-04-19 | No |
| [Managing Agent Context](guides/managing-agent-context.md) | guide | 26 findings (13 P1 + 13 P2) | 2026-04-19 | No |
| [Agent Architecture Decisions](guides/agent-architecture-decisions.md) | guide | 21 findings (split from 41; topology/composition) | 2026-04-19 | No |
| [Agent Workflow and Execution](guides/agent-workflow-and-execution.md) | guide | 20 findings (split from G3; execution/operations) | 2026-04-19 | No |
| [Building Agent Evaluation Suites](guides/building-agent-evaluation-suites.md) | guide | 30 findings (15 P1 + 15 P2) | 2026-04-19 | No |
| [Designing Agent Tools](guides/designing-agent-tools.md) | guide | 14 findings (6 P1 + 8 P2) | 2026-04-19 | No |
| [Session Persistence and Memory](guides/session-persistence-and-memory.md) | guide | 14 findings (6 P1 + 8 P2) | 2026-04-19 | No |
| [Model-Resilient Prompt Engineering](guides/model-resilient-prompt-engineering.md) | guide | 15 findings (5 P1 + 10 P2) | 2026-04-19 | No |
| [Agent Governance and Trust](guides/agent-governance-and-trust.md) | guide | 10 findings (2 P1 + 8 P2) | 2026-04-19 | No |
| [Agent Design Patterns](guides/agent-design-patterns.md) | guide | 11 findings (11 P2) | 2026-04-19 | No |
| [Surgical Change Constraint — Agent Scope Boundary](rules/surgical-change-agent-scope.md) | rule | [[surgical-change-constraint-agent-scope]] | 2026-04-20 | No |
| [Multi-Agent Proportional Content Summarization to Obsidian](skills/multi-agent-proportional-content-summarization.md) | skill | [[multi-agent-proportional-content-summarization]] | 2026-04-20 | No |
