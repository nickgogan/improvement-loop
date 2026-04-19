---
name: Tier 1 + Tier 2 Source Extraction Report
date: "2026-04-07"
type: delta-report
---

# Tier 1 + Tier 2 Source Extraction Report — 2026-04-07

## Summary
| Metric | Before | After | Delta |
|--------|--------|-------|-------|
| Total findings | 220 | 279 | +59 |
| Sources with filename findings | 56 | 64 | +8 |
| Sources with zero findings | 16 | 8 | -8 |
| Sources processed this pass | 0 | 23 | +23 |

## Extraction by Batch

### Tier 1A — Articles (20 new, 6 updated)

**MCP: Everything Your Team Needs to Know -- WorkOS (6 new)**
- `mcp-n-plus-m-integration-economics.md` — N+M protocol economics (P3)
- `mcp-session-scoped-authorization.md` — OAuth 2.1 session-scoped tokens (P3)
- `mcp-async-task-model.md` — Call-now-fetch-later pattern (P3)
- `mcp-enterprise-governance-gaps.md` — 5 missing enterprise capabilities (P3)
- `mcp-elicitation-for-user-input.md` — Protocol-level mid-execution input (P3)
- `mcp-server-cards-discovery.md` — Decentralized discovery via .well-known (P3)

**Multi-Agent Orchestration Playbook -- Nick Gupta (8 new)**
- `task-contract-pattern-schema-first-agent.md` — Schema-first contracts (P1)
- `durable-workflow-engine-for-agent-systems.md` — Temporal-style crash-safe execution (P2)
- `tool-gateway-security-boundary.md` — Centralized gateway with allowlist (P2)
- `planner-executor-deterministic-guardrails.md` — Planning probabilistic, execution deterministic (P1)
- `critic-verifier-loop-with-termination.md` — Generate-critique-patch with termination (P2)
- `context-rot-silent-killer-and-mitigations.md` — Silent Killer #1 with 4 mitigations (P1)
- `agent-cost-blowup-mitigation-strategies.md` — Silent Killer #2: budgets, caching, fast-fail (P2)
- `unified-tracing-opentelemetry-for-agents.md` — End-to-end tracing with error taxonomy (P2)

**Anthropic Prompt Evaluation Framework (3 new, 1 updated)**
- `volume-over-quality-eval-principle.md` — More tests with automated grading > fewer with human (P1)
- `three-tier-grading-hierarchy.md` — Code-based > LLM-based > Human grading (P1)
- `multidimensional-success-criteria-smart.md` — 8-dimension SMART eval criteria (P2)
- Updated: `four-discipline-prompt-evaluator.md`

**Agent Orchestrators Are Bad (3 new, 2 updated)**
- `capability-saturation-threshold-45-percent.md` — Diminishing returns past 45% baseline (P1)
- `specialization-theater-anti-pattern.md` — Agent teams mirroring org structure (P1)
- `legitimate-multi-agent-domains-taxonomy.md` — 4 legitimate domains (P1)
- Updated: `l-d-hypothesis-information-loss-across-agent-bound.md`, `tool-shaped-object-evaluation-lens.md`

### Tier 1B — Papers + Blogs (14 new, 2 updated)

**ARTIST arXiv (4 new, 1 updated)**
- `outcome-based-reward-design-for-tool-agents.md` — Outcome RL for tool use (P3)
- `prompt-only-tool-use-ceiling.md` — Ceiling on prompt-based tool use (P3)
- `loss-masking-deterministic-tool-outputs.md` — Mask loss on tool outputs (P3)
- `emergent-agentic-behaviors-from-outcome-rl.md` — Emergent behaviors from RL (P2)
- Updated: `rl-trained-autonomous-tool-selection-artist-pattern.md`

**HyperAgents arXiv (3 new)**
- `metacognitive-self-modification-hyperagents.md` — Self-modifying agent architectures (P3)
- `cross-domain-transfer-of-meta-improvements.md` — Transfer across domains (P3)
- `editable-optimizer-eliminates-domain-lock.md` — Editable optimizer pattern (P3)

**ARC-AGI-3 (3 new)**
- `arc-agi-3-zero-percent-abstract-reasoning.md` — All frontier models 0% (P2)
- `cot-fails-without-inductive-generalization.md` — CoT fails on novel patterns (P2)
- `benchmark-signal-mismatch-optimization-gap.md` — Benchmark optimization gap (P2)

**March 2026 AI Roundup (4 new)**
- `mcp-ecosystem-critical-mass-97m-installs.md` — MCP at 97M installs (P2)
- `frontier-release-compression-march-2026.md` — Release cadence compression (P2)
- `open-source-model-parity-mistral-small-4.md` — Open-source catching up (P3)
- `agentic-infrastructure-pilot-to-production.md` — Production transition (P2)

### Tier 1 Videos (1 new, 1 updated)

**Layers That Won't Exist (1 new)**
- `eval-driven-development-autonomous-quality.md` — Eval-driven dev as builder skill (P2)
- Updated: `six-layer-agent-infrastructure-stack.md`

**Superpowers, Claude Limit Burns, BMad V6, SOUL.md — 0 new** (KB already comprehensive)

### Tier 2A — Articles + Papers (14 new, 3 updated)

**Every Layer of Review (3 new, 2 updated)**
- `review-obsolescence-as-design-goal.md` — Make review comments impossible in future (P1)
- `ai-developer-descent-into-madness-anti-pattern.md` — Agent-to-check-agent recursion (P2)
- `competitive-module-development-parallel-teams.md` — Parallel teams, select best (P3)
- Updated: `review-pipeline-bottleneck-and-quality-at-source.md`, `org-redesign-for-agentic-throughput-high-speed-rail.md`

**ETH Zurich Context Files (3 new, 1 updated)**
- `context-file-instruction-bloat-eth-zurich.md` — LLM-generated files -3% success, +20% cost; 60-line sweet spot (P1)
- `tiered-context-injection-over-monolithic-files.md` — Operation-scoped subsets reduce context 60-80% (P2)
- `pointers-over-copies-in-context-files.md` — file:line references over embedding (P2)
- Updated: `context-file-taxonomy-claudemd-soulmd-agentsmd.md`

**ACE ICLR 2026 (2 new)**
- `ace-delta-updates-over-monolithic-rewrites.md` — Incremental deltas, 86.9% latency reduction (P1)
- `ace-execution-feedback-no-labels-required.md` — Self-improvement from execution signals (P2)

**OpenClaude / Hindsight (3 new)**
- `biomimetic-memory-auto-recall-over-tool-based.md` — Auto-inject vs tool-based recall (P2)
- `memory-bank-isolation-per-agent-per-project.md` — Dynamic bank IDs for isolation (P3)
- `structured-fact-extraction-from-conversations.md` — Typed fact extraction (P2)

**Intent Engineering Framework (3 new)**
- `autonomy-gradient-not-binary-delegation.md` — Four-level autonomy by blast radius (P1)
- `health-metrics-vs-hard-constraints-distinction.md` — Steering vs hard constraints (P1)
- `stop-rules-as-execution-boundaries.md` — Halt, escalate, completion conditions (P2)

### Tier 2B — Articles (10 new, 1 updated)

**Self-Improving Skills / MindStudio (2 new)**
- `binary-eval-assertion-design-deterministic-plus-ll.md` — Dual-layer assertions (P1)
- `test-input-coverage-design-15-30-sweet-spot.md` — 15-30 test inputs sweet spot (P2)

**Every AI Prompting Technique (2 new)**
- `design-evaluate-dual-phase-prompting-framework.md` — Design + Evaluate phases (P2)
- `model-agnostic-prompting-three-properties.md` — Three model-agnostic properties (P1)

**Prompting After Feb 2026 (2 new)**
- `acceptance-criteria-as-verifiable-eval-anchor.md` — Verifiable acceptance criteria (P1)
- `context-curation-over-context-stuffing.md` — Curate don't stuff (P1)

**4-Layer Memory Stack (2 new, 1 updated)**
- `memory-cross-layer-promotion-governance.md` — Policy-gated promotion between tiers (P2)
- `governance-memory-append-only-audit-layer.md` — Append-only audit layer (P2)
- Updated: `four-layer-enterprise-memory-stack.md`

**AI Agent Prompt Engineering / Inflectra (2 new)**
- `five-layer-agent-prompt-architecture.md` — 5-layer prompt architecture (P2)
- `success-rate-eval-over-binary-pass-fail.md` — Success rate over pass/fail (P2)

## Priority Distribution of New Findings

| Priority | Count |
|----------|-------|
| P1 (Implement Now) | 16 |
| P2 (Design Required) | 27 |
| P3 (Monitor) | 16 |

## Category Distribution of New Findings

| Category | New | Total KB |
|----------|-----|----------|
| Orchestration | 9 | 68 |
| Context Engineering | 6 | 49 |
| Tool Integration | 7 | 38 |
| Evaluation | 12 | 36 |
| Prompt Craft | 4 | 24 |
| Memory Architecture | 4 | 20 |
| Intent Engineering | 4 | 14 |
| Agent Design | 9 | 12 |
| Model Selection | 2 | 8 |
| Governance | 2 | 6 |

## Remaining Unlinked Sources (8)

These sources still have zero findings and were not in the extraction scope:
1. `cursor-ai-mcp-server-configuration-setup-auth-best.md`
2. `deepeval-mcp-evaluation-quickstart.md`
3. `gemini-vs-gpt-vs-claude-benchmark-comparison-lorka.md`
4. `hitl-agentic-ai-strataio-2026-guide.md`
5. `openai-self-evolving-agents-cookbook.md`
6. `prompting-best-practices-nick-gogan.md`
7. `ai-agents-in-enterprise-webinar-march-31-2026.md`
8. `ai-agents-in-production-2026-nick-gupta-linkedin.md`
