---
title: "Artifact Identification Report"
type: "report"
target_system:
  - "improvement-loop"
created: "2026-04-26"
scope: "P1 raw findings (full batch) — IB-150 acceptance test pre-stage"
findings_scanned: 27
findings_filtered: 10
---

# Artifact Identification Report — 2026-04-26

**Scope:** P1 raw findings (`pipeline_status: raw` AND `priority` startswith `P1`)
**Findings scanned:** 27 | **Filtered out:** 10 (dedup: 10, weak: 0, adopted: 0)
**Classified:** 17

> **State note for Nick (NOT a contract violation; flagged for cleanup):** 10 of the 27 enumerated findings already have staged extracts in `extracts/` but their `pipeline_status` was never back-annotated to `extracted`. They were correctly excluded by the dedup filter. The bookkeeping bug is that `/extract-artifacts` Step 5 (back-annotation) failed silently in some prior session(s). Affected source_findings: `claude-code-hooks-for-automatic-session-memory`, `claude-code-ultra-plan-three-mode-planning`, `compounding-knowledge-loop-internal-data`, `git-status-context-injection-token-hygiene`, `ide-first-claude-code-with-deterministic-hooks`, `karpathy-llm-knowledge-base-obsidian-rag`, `progressive-search-wide-then-narrow`, `teach-orchestrator-to-delegate-pattern`, `test-output-design-for-llm-context`, `token-waste-taxonomy-and-two-mode-workflow`. Suggest filing as IB (priority TBD) — separate from the IB-150 acceptance test.

## Summary

| Form | Count | % | Auto | Guided | HITL |
|------|-------|---|------|--------|------|
| pattern | 13 | 76% | 11 | 2 | 0 |
| rule | 2 | 12% | 1 | 1 | 0 |
| template | 1 | 6% | 0 | 1 | 0 |
| skill | 1 | 6% | 1 | 0 | 0 |
| agent | 0 | 0% | 0 | 0 | 0 |
| **Total** | **17** | **100%** | **13** | **4** | **0** |

Pattern dominance (76%) is below the 92% calibration baseline — the P1 raw batch has slightly higher mechanism density than the calibration corpus, consistent with these findings being practitioner-derived production techniques rather than theoretical patterns.

**Curator priority review (Step 3.5):** No revisions warranted. All 17 findings entered at P1 with form-classification confidence consistent with that priority (HIGH or MED on Strong/Medium evidence). No KB-wide signal surfaced during this pass that contradicted Researcher triage.

**Guide routing (Step 6):** All 13 pattern findings map to existing guide clusters. Zero unrouted. No candidate-cluster threshold crossed.

| Pattern Finding | Category | Guide |
|---|---|---|
| ace-agentic-context-engineering-rag-based | Memory Architecture | G7 |
| claude-code-context-management-decision-matrix-five-tools | Context Engineering | G2 |
| cli-first-tool-integration-less-overhead-than-mcp | Tool Integration | G5 |
| context-warrant-justified-data-package | Governance | G9 |
| factorial-design-eval-systematic-context-variati | Evaluation | G4 |
| five-context-management-techniques-in-claude-code | Context Engineering | G2 |
| memorymd-cross-session-preference-persistence | Memory Architecture | G7 |
| model-tier-routing-expensive-orchestrator-cheap-s | Orchestration | G3 |
| orchestrated-execution-one-task-per-sub-agent-wit | Orchestration | G3 |
| policy-as-data-machine-readable-constraints | Governance | G9 |
| specialized-harness-engineering-deterministic-rail | Orchestration | G3 |
| superpowers-plugin-spec-driven-sub-agent-orchestra | Orchestration | G3 |
| test-driven-development-as-counterweight-to-agenti | Evaluation | G4 |

## Candidates

### HITL — Needs Human Decision

_(none — no LOW-confidence classifications in this batch)_

### GUIDED — Review Recommended

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 1 | [[claudemd-minimum-viable-rule-only-add-globally]] | rule | MED | pattern | PENDING |
| 2 | [[memorymd-cross-session-preference-persistence]] | pattern | MED | template | PENDING |
| 3 | [[orchestrated-execution-one-task-per-sub-agent-wit]] | pattern | MED | rule | PENDING |
| 4 | [[task-to-file-routing-table-in-context-files]] | template | MED | pattern | PENDING |

### AUTO — Ready for Extraction

| # | Finding | Form | Confidence | Co-occurrence | Status |
|---|---------|------|------------|---------------|--------|
| 5 | [[ace-agentic-context-engineering-rag-based]] | pattern | HIGH | agent | PENDING |
| 6 | [[claude-code-context-management-decision-matrix-five-tools]] | pattern | HIGH | — | PENDING |
| 7 | [[cli-first-tool-integration-less-overhead-than-mcp]] | pattern | HIGH | — | PENDING |
| 8 | [[context-warrant-justified-data-package]] | pattern | HIGH | rule | PENDING |
| 9 | [[explicit-permission-allow-listing-for-agent-resou]] | rule | HIGH | pattern | PENDING |
| 10 | [[factorial-design-eval-systematic-context-variati]] | pattern | HIGH | — | PENDING |
| 11 | [[five-context-management-techniques-in-claude-code]] | pattern | HIGH | — | PENDING |
| 12 | [[iterative-refinement-loop-with-quality-gate]] | skill | HIGH | — | PENDING |
| 13 | [[model-tier-routing-expensive-orchestrator-cheap-s]] | pattern | HIGH | — | PENDING |
| 14 | [[policy-as-data-machine-readable-constraints]] | pattern | HIGH | rule | PENDING |
| 15 | [[specialized-harness-engineering-deterministic-rail]] | pattern | HIGH | — | PENDING |
| 16 | [[superpowers-plugin-spec-driven-sub-agent-orchestra]] | pattern | HIGH | skill | PENDING |
| 17 | [[test-driven-development-as-counterweight-to-agenti]] | pattern | HIGH | — | PENDING |

## Details

### 1. claudemd-minimum-viable-rule-only-add-globally

- **Assigned form:** rule
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** binary-include-exclude, deterministic-self-test, enforcement-boundary-named
- **Co-occurrence:** pattern
- **Rationale:** The center of gravity is the specific enforcement criterion — "only include a line you would manually type in nearly every session" — which is a deterministic binary check at the CLAUDE.md authoring boundary. The mechanism IS the insight: the self-test heuristic that gates inclusion. Pattern is a co-occurrence (the broader "context rot" philosophy) but is not the center of gravity. Confidence is MED because "virtually every session" introduces judgment rather than fully mechanical evaluation, making this borderline rule/pattern.
- **Status:** APPROVED

### 2. memorymd-cross-session-preference-persistence

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** reusable-shape, instantiation-varies, design-approach, template-co-occurrence-plausible
- **Co-occurrence:** template
- **Rationale:** The center of gravity is the design shape: place a self-updating file alongside the system prompt to accumulate cross-session corrections and preferences. The specific file name (memory.md), the exact CLAUDE.md instruction snippet, and the update trigger are instantiations — someone could apply this shape with a different file name, format, or harness. This answers "how should I structure cross-session memory?" not "here is the exact scaffold to fill in." MED confidence because the CLAUDE.md instruction snippet in the body has template character (backbone with role/update-trigger/section variables) and could be codified as a template downstream.
- **Status:** APPROVED.

### 3. orchestrated-execution-one-task-per-sub-agent-wit

- **Assigned form:** pattern
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** design-approach, how-to-structure, failure-mode-insight, rule-co-occurrence-plausible
- **Co-occurrence:** rule
- **Rationale:** The center of gravity is the design shape: assign one task per sub-agent and build explicit wiring verification into each wave boundary to prevent integration failures. The finding answers "how should I structure sub-agent orchestration?" — not "here is a procedure to invoke" or "here is a binary constraint." The wiring verification step has some rule character (mandatory check at wave-completion boundary), which is why MED confidence applies, but the finding frames it as an architectural principle with a failure-mode rationale (code islands), not as a deterministic enforced gate. Excludes skill (no defined inputs/outputs or explicit invocation), excludes rule as primary (the broader design approach is the insight, not the specific verification check), excludes template and agent.
- **Status:** APPROVED.

### 4. task-to-file-routing-table-in-context-files

- **Assigned form:** template
- **Confidence:** MED
- **Tier:** guided
- **Reason codes:** named-variables, fillable-backbone, repeatable-generation, per-workspace-variation
- **Co-occurrence:** pattern
- **Rationale:** The center of gravity is the specific scaffold — a four-column markdown table (Task | Read These Files | Skip These Files | Skills Needed) embedded in a workspace context file, where each row is a named-variable slot. The rubric template/pattern test passes: writing the insight in {{VARIABLE}} → body form ({{TASK_TYPE}} | {{FILES_TO_READ}} | {{FILES_TO_SKIP}} | {{SKILLS_NEEDED}}) preserves the full value without loss, meaning the scaffold IS the insight. Confidence is MED because there is no formal generator — only a markdown backbone with variation per workspace — which places this at the medium tier per rubric §4; the broader selective-loading design approach is a plausible pattern co-occurrence.
- **Status:** APPROVED.

### 5. ace-agentic-context-engineering-rag-based

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** multi-component-shape, instantiation-not-center, role-count-gt-1-dd76
- **Co-occurrence:** agent
- **Rationale:** The center of gravity is the reusable design shape: retrieve relevant behavioral rules per task, reflect on execution to extract lessons, curate a vote-weighted store. The three components (Generator/Reflector/Curator) are instantiations of this shape — someone could implement the same approach with different architectures or role names. Agent is excluded because role count > 1 (DD-76) and because no single named role's cognitive disposition is the insight; the compositional shape is. Skill is excluded because there are no ordered steps with defined inputs/outputs per invocation.
- **Status:** APPROVED

### 6. claude-code-context-management-decision-matrix-five-tools

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** decision-framework-with-tradeoffs, it-depends-character, instantiation-not-center
- **Co-occurrence:** —
- **Rationale:** The center of gravity is a decision framework that maps named situations to context management primitives — a reusable shape answering "how should I structure context management decisions?" with explicit tradeoffs per situation. The five specific primitives (Continue, /rewind, /compact, /clear, Subagents) are instantiations; the insight survives replacement with different tools. Skill is excluded because there are no ordered steps with defined inputs/outputs. Rule is excluded because the matrix is graded/situational, not a binary MUST/MUST NOT at a boundary.
- **Status:** APPROVED

### 7. cli-first-tool-integration-less-overhead-than-mcp

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** decision-heuristic-with-tradeoffs, instantiation-not-center, it-depends-character
- **Co-occurrence:** —
- **Rationale:** The center of gravity is the design heuristic: prefer CLI over MCP in terminal-native environments when a CLI exists, because CLIs share the agent's environment natively while MCP adds process, protocol, and initialization overhead. The Playwright example is an instantiation; the insight applies across any tool category with both CLI and MCP options. Rule is excluded because this is a preference with tradeoffs (CLI when available, MCP when no CLI exists), not a binary MUST/MUST NOT. Skill is excluded because there are no ordered steps or defined invocation.
- **Status:** APPROVED

### 8. context-warrant-justified-data-package

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable-shape, composable, instantiation-not-center, it-depends-character
- **Co-occurrence:** rule
- **Rationale:** The center of gravity is the design shape: a formally justified, minimum-necessary, freshness-enforced context assembly step that executes before any agent decision. The four properties and the specific 11-step position are instantiations — the finding itself notes MetaSystem could apply this with different implementation details. Rule is a co-occurrence (specific invariants could be extracted from the four properties) but is not the center of gravity; the shape of "how to structure context assembly for auditability" is. Skill is excluded because there are no ordered steps with defined inputs/outputs per invocation.
- **Status:** APPROVED

### 9. explicit-permission-allow-listing-for-agent-resou

- **Assigned form:** rule
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** binary-allow-deny, deterministic-check, enforcement-boundary-named, no-cognitive-judgment
- **Co-occurrence:** pattern
- **Rationale:** The center of gravity is the specific enforcement mechanism: whenever an agent attempts access to a pre-unauthorized resource, it MUST prompt for explicit user approval before proceeding — a binary allow/deny check at the resource-access boundary requiring no cognitive judgment. The mechanism IS the insight, not an example of a broader shape. Pattern (principle of least privilege, defense-in-depth) is a co-occurrence but not the center of gravity. Skill is excluded because there are no ordered steps with outputs; the action is immediate (prompt, allow/deny).
- **Status:** APPROVED

### 10. factorial-design-eval-systematic-context-variati

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable-shape, tradeoffs-present, instances-vary, design-approach
- **Co-occurrence:** —
- **Rationale:** The center of gravity is the design shape: structure eval libraries with stable variation types as sections and domain-specific scenarios as content, rather than single-scenario testing. The specific 16 variations (social cues, extreme risk, etc.) are instantiations of this shape, not the insight itself — someone could apply the factorial approach across any domain without those exact variation types. No ordered steps with defined inputs/outputs (excludes skill), no binary constraint at a named boundary (excludes rule), no named-variable scaffold (excludes template), no single named role (excludes agent).
- **Status:** APPROVED

### 11. five-context-management-techniques-in-claude-code

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** heuristic-decision-framework, tradeoffs-present, it-depends-character, trap-1-tiers-are-heuristics
- **Co-occurrence:** —
- **Rationale:** The center of gravity is the decision framework: a tiered taxonomy of context management options with explicit cost/quality tradeoffs and a preference ordering. The five techniques are the heuristic landscape, not an ordered procedure to invoke — applying TRAP 1 directly (tiers with tradeoffs → pattern, not skill). The preference ordering is advisory, not deterministic, and the choice among techniques depends on session context. No ordered procedural steps, no binary constraint, no scaffold, no single named role — all non-pattern forms excluded.
- **Status:** APPROVED

### 12. iterative-refinement-loop-with-quality-gate

- **Assigned form:** skill
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** defined-inputs-outputs, ordered-steps, stateless-per-invocation, failure-modes-described
- **Co-occurrence:** —
- **Rationale:** The center of gravity IS the mechanism: a bounded self-evaluation loop with specified inputs (draft, scoring criteria, threshold), outputs (refined draft or capped final), ordered steps (draft → score → check → rewrite → re-score → loop → cap), and explicit failure-mode handling (max-iteration cap). Unlike TRAP 2, the procedure here is not an example of a broader design approach — the iteration cap, threshold check, and scoring dimensions are the point. Excludes pattern (the specific procedure is the insight, not a reusable shape); excludes rule (multi-step loop, not a binary boundary gate); excludes template and agent by absence of scaffold variables and named persona.
- **Status:** APPROVED

### 13. model-tier-routing-expensive-orchestrator-cheap-s

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** reusable-shape, tradeoffs-present, instantiation-varies, design-approach
- **Co-occurrence:** —
- **Rationale:** The center of gravity is the design approach: match model tier to cognitive demand — premium models for orchestration (nuanced judgment, user interaction, synthesis) and cheaper models for narrow sub-agent tasks (well-scoped, schema-defined). The specific models (Gemini 2.5 Pro, Flash) are instantiations; the insight transfers across any multi-model architecture. Tradeoffs are explicit (cost vs. quality at each tier). No ordered steps (excludes skill), no binary gate (excludes rule), no named-variable scaffold (excludes template), no single named role (excludes agent).
- **Status:** APPROVED

### 14. policy-as-data-machine-readable-constraints

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, forces-and-tradeoffs, mechanisms-are-instantiations, no-procedure, no-single-role
- **Co-occurrence:** rule
- **Rationale:** The center of gravity is the design philosophy of encoding governance rules as machine-readable data structures evaluated at runtime, rather than prose read by agents — the distinction between governance-as-documentation and governance-as-enforcement. The three rule categories and dependency-chain position are instantiations of this shape, not the shape itself; someone could apply the core insight with entirely different category structures. Rule is excluded because the finding describes when and why enforcement matters across cases (a pattern), not a single deterministic binary constraint at a named boundary.
- **Status:** APPROVED

### 15. specialized-harness-engineering-deterministic-rail

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, composable-shape, mechanisms-are-instantiations, tradeoffs-explicit, no-procedure
- **Co-occurrence:** —
- **Rationale:** The center of gravity is the architectural shape — wrap LLM workflows in a purpose-built harness with phase gates, isolated sub-agents, structured output validation, and state management to convert probabilistic behavior into near-determinism. The six numbered components (phase-gating, schemas, sub-agent delegation, Supabase state, virtual file system, model-tier routing) are instantiations of this shape; the shape can be instantiated with different databases, languages, or gating mechanisms. Skill is excluded because the six components describe an architecture, not an ordered procedure with defined inputs/outputs and explicit invocation; template and rule are excluded for lack of scaffold variables and binary constraint respectively.
- **Status:** APPROVED, though I believe harnesses actually lie on a spectrum from entierly LLM-initiated & driven via just prompts (in the form of skills and handoff prompts) to mostly deterministic where workflows are instantiated and wired together with code.

### 16. superpowers-plugin-spec-driven-sub-agent-orchestra

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-approach, hard-gate-shape, multiple-roles-dd76, mechanisms-are-instantiations, no-single-role
- **Co-occurrence:** skill
- **Rationale:** The center of gravity is the design shape — enforce a mandatory spec-approval hard gate before any implementation begins, then dispatch specialized sub-agents per phase (implementation, review, testing). The seven Superpowers steps are an instantiation; the core insight (spec-first with a blocking gate) applies to any orchestration framework. DD-76 applies: the finding describes multiple roles (orchestrator plus sub-agents for implementation, review, and testing), biasing away from agent toward pattern. Skill is excluded because the workflow is stateful across git worktrees (not stateless per run) and has no explicit inputs/outputs; agent is excluded by DD-76 role-count rule.
- **Status:** APPROVED

### 17. test-driven-development-as-counterweight-to-agenti

- **Assigned form:** pattern
- **Confidence:** HIGH
- **Tier:** auto
- **Reason codes:** design-philosophy, forces-and-tradeoffs, no-procedure, no-scaffold, no-single-role
- **Co-occurrence:** —
- **Rationale:** The center of gravity is the design philosophy that TDD must be elevated to the primary trust and quality-gate mechanism in agentic coding — beyond its traditional role — because LLM output randomness makes it impossible to read every generated line; tests are the counterweight. The finding argues why and how to think about TDD in this context, not a specific procedure for writing tests or a binary rule mandating them. Skill is excluded because there are no ordered steps with defined inputs/outputs; rule is excluded because the finding is advisory and contextual (elevated importance across cases) rather than a deterministic binary check at a named boundary.
- **Status:** APPROVED
