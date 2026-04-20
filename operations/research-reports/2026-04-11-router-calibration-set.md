---
title: "Form Router Calibration Set"
type: "reference"
category: "knowledge-management"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-04-11"
updated: "2026-04-11"
author: "claude"
tags:
  - "form-router"
  - "calibration"
  - "proposer-architect-pipeline"
aliases:
  - "Router calibration 50"
---

# Form Router Calibration Set

Hand-classified reference set for Form Router calibration. **Target: 50 findings** (5 anchors from the session 20–21 paper exercises + 45 new classifications).

Purpose: (a) stress-test the rubric at real volume, surface gaps, amend the rubric in place; (b) derive logprob thresholds for `HIGH` / `MEDIUM` / `LOW` confidence once automated; (c) serve as ground-truth for Router regression testing.

**Source rubric:** [[form-classification-rubric]] (in `systems/improvement-loop/operations/references/`)

**Status:** complete. 50 findings classified across 4 batches. 2 rubric amendments applied.

---

## Sampling strategy

**Stratified across 11 categories**, weighted so smaller categories get at least 2 findings (guarantees rare-form coverage — templates are expected to cluster in small categories).

| Category | P1 pool | P2 pool | Target | Rationale |
|---|---|---|---|---|
| Orchestration | 14 | 28 | 8 | largest pool |
| Context Engineering | 19 | 16 | 7 | largest pool |
| Evaluation | 15 | 19 | 7 | incl. 1 anchor |
| Agent Design | 2 | 14 | 5 | incl. 1 anchor |
| Tool Integration | 8 | 10 | 5 | incl. 3 anchors |
| Prompt Craft | 4 | 10 | 4 | mid pool |
| Memory Architecture | 3 | 8 | 3 | small pool |
| Governance | 2 | 8 | 3 | small pool |
| Intent Engineering | 5 | 3 | 3 | small pool |
| Sandboxing | 4 | 2 | 3 | small pool |
| Model Selection | 2 | 1 | 2 | smallest pool |
| **Total** | **78** | **119** | **50** | |

**Batch size: 15 per session.** Session 1 covers 5 anchors (pre-classified) + 10 new = 15. Sessions 2 and 3 cover 15 each. Session 4 covers the final 10. Expected total: 3 working sessions after this staging doc. A session can amend the rubric in place if gaps surface; flag amendments in the `notes` column.

**Exclusions:** the 5 already-walked findings are included as anchors (not re-classified) to provide reference rows.

---

## Classification columns

Each row captures:

| Column | Definition |
|---|---|
| `#` | Row number |
| `id` | Finding file stem |
| `category` | Category from finding frontmatter |
| `pri` | P1 / P2 |
| `candidate` | Proposer's candidate form (or `-` if not set) |
| `assigned` | Router's assigned form (the answer) |
| `conf` | HIGH / MED / LOW |
| `tier` | auto / guided / hitl |
| `override` | Y / N |
| `reason_codes` | Compact reason codes (max 3) |
| `notes` | Rubric gaps, ambiguity, amendments triggered |

---

## Anchors (pre-classified from session 20–21 exercises)

| # | id | category | pri | candidate | assigned | conf | tier | override | reason_codes | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | think-tool-scratchpad-for-mid-chain-reasoning | Tool Integration | P1 | pattern | pattern | HIGH | auto | N | reusable_shape, multi_source, no_procedure | session 20 exercise |
| 2 | programmatic-tool-calling-code-orchestrated-tool-use | Tool Integration | P1 | pattern | pattern | HIGH | auto | N | compositional_primitive, cross_vendor | session 20 exercise |
| 3 | mcp-as-code-api-progressive-tool-discovery | Tool Integration | P1 | pattern | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs | session 20 exercise |
| 4 | specialized-parallel-agent-roles | Agent Design | P2 | agent | pattern | MED | guided | Y | shape_not_role, role_count_gt_1, cross_source_role_divergence | session 21 — override-to-pattern stress test |
| 5 | agentic-harness-self-assessment-skill | Evaluation | P2 | skill | skill | HIGH | guided | N | defined_inputs_outputs, ordered_procedure, two_modes_param | session 21 — GUIDED because skill wraps uncodified framework |

---

## Batch 1 — 10 new findings (first working session)

Mix across categories; leans toward expected form diversity to exercise the rubric broadly.

| # | id | category | pri | candidate | assigned | conf | tier | override | reason_codes | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 6 | planner-executor-deterministic-guardrails | Orchestration | P1 | - | pattern | HIGH | auto | N | reusable_shape, multi_source, forces_tradeoffs | |
| 7 | effort-scaling-rules-embedded-in-orchestrator | Orchestration | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, no_binary_gate | "Rules" in name are heuristics, not binary constraints. No enforcement boundary. |
| 8 | task-contract-pattern-schema-first-agent | Orchestration | P1 | - | pattern | HIGH | auto | N | reusable_shape, multi_source, compositional_primitive | Describes the approach of using contracts, not a contract scaffold. |
| 9 | context-rot-attention-budget-depletion | Context Engineering | P1 | - | pattern | MED | guided | N | problem_framing, single_source, instantiation_ambiguous | Problem framing / mental model; instantiation unclear. What would the codified artifact look like? |
| 10 | hybrid-upfront-and-jit-context-architecture | Context Engineering | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, no_procedure | Already Adopted validates shape. |
| 11 | binary-eval-assertion-design-deterministic-plus-ll | Evaluation | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, compositional_primitive | Dual-layer architecture, not a procedure. |
| 12 | three-tier-grading-hierarchy | Evaluation | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, no_procedure | Preference ordering, not binary constraint. |
| 13 | poka-yoke-error-proof-tool-interfaces | Tool Integration | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, co_occurrence_rule | Pattern/rule co-occurrence. Center of gravity is design philosophy. Specific invariants (e.g. absolute filepath) are downstream rules harvestable by /extract-artifacts. |
| 14 | ground-truth-environmental-feedback-loops | Agent Design | P1 | - | pattern | HIGH | auto | N | reusable_shape, multi_source, forces_tradeoffs | |
| 15 | model-agnostic-prompting-three-properties | Prompt Craft | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, litmus_framework | Three properties are a design heuristic for technique selection, not binary enforcement rules. |

## Batch 2 — 15 new findings

| # | id | category | pri | candidate | assigned | conf | tier | override | reason_codes | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 16 | workflow-state-vs-conversation-state | Orchestration | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, no_procedure | |
| 17 | file-based-task-locking-parallel-agents | Orchestration | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, compositional_primitive | |
| 18 | agent-type-system-six-roles | Orchestration | P2 | - | pattern | HIGH | auto | N | reusable_shape, role_count_gt_1, shape_not_role | 6 roles = system of roles → pattern. DDc-2 applies. |
| 19 | archon-yaml-defined-harness-workflows | Orchestration | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, co_occurrence_template | Template co-occurrence. Finding describes DAG-based hybrid workflow approach, not the YAML scaffold. |
| 20 | prompt-caching-for-stable-agent-context | Context Engineering | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, no_procedure | |
| 21 | tech-stack-pinning-table-for-drift-prevention | Context Engineering | P1 | - | template | HIGH | auto | N | named_variables, build_artifact, repeatable_generation | First template classification. Fillable scaffold (tech/version/rationale table) with clear generation and consumption pattern. |
| 22 | claudemd-as-knowledge-base-traversal-guide | Context Engineering | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, no_procedure | Guide-shaped risk noted but guides out of Router scope. |
| 23 | new-chat-per-agent-step-context-hygiene | Context Engineering | P2 | - | pattern | MED | guided | N | reusable_shape, forces_tradeoffs, discipline_not_gate | Rule-shaped constraint embedded in pattern-shaped framing. Center of gravity is the design discipline. |
| 24 | pointers-over-copies-in-context-files | Context Engineering | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, it_depends_character | Tradeoffs explicit: some info genuinely belongs inline. |
| 25 | two-level-verification-agent-run-plus-harness-inte | Evaluation | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, compositional_primitive | |
| 26 | volume-over-quality-eval-principle | Evaluation | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, design_principle | Priority ordering, not binary constraint. |
| 27 | llm-as-judge-pattern-for-verification-agents | Evaluation | P2 | - | pattern | HIGH | auto | N | reusable_shape, multi_source, forces_tradeoffs | |
| 28 | critic-verifier-loop-with-termination | Agent Design | P2 | - | pattern | HIGH | auto | N | reusable_shape, role_count_gt_1, forces_tradeoffs | Two roles (generator + critic). DDc-2 applies. |
| 29 | soul-md-agent-constitution-pattern | Agent Design | P2 | - | pattern | MED | guided | N | reusable_shape, forces_tradeoffs, co_occurrence_template | Template co-occurrence. Primary contribution is identity-capability separation architecture, not the SOUL.md scaffold. |
| 30 | self-improving-agent-prompt-tool-diagnosis | Agent Design | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, compositional_primitive | |

## Batch 3 — 15 new findings

| # | id | category | pri | candidate | assigned | conf | tier | override | reason_codes | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 31 | graceful-degradation-modes-for-agent-failure | Orchestration | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, compositional_primitive | Four degradation modes as design vocabulary. |
| 32 | success-rate-eval-over-binary-pass-fail | Evaluation | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, design_principle | Statistical approach to eval, not a constraint. |
| 33 | post-session-hooks-autonomous-version-control | Tool Integration | P2 | - | pattern | MED | guided | N | reusable_shape, forces_tradeoffs, co_occurrence_rule | Rule co-occurrence. Specific hook config is a rule; finding's center of gravity is the practice and tradeoffs. |
| 34 | reasoning-model-anti-pattern-prescribed-reasoning | Prompt Craft | P1 | - | rule | MED | guided | N | constraint_language, enforcement_boundary, partially_deterministic | First rule classification. Anti-pattern = natural rule language. Some checks deterministic (string match for CoT), others require judgment. Amend 2. |
| 35 | extract-deep-plan-prompt-as-custom-skill | Prompt Craft | P1 | - | skill | HIGH | auto | N | defined_inputs_outputs, ordered_procedure, explicit_invocation | 4-agent pipeline (planner→critic→refiner→finalizer). No framework trap — pipeline is well-defined, not an opinionated taxonomy. |
| 36 | yaml-template-dual-structure | Prompt Craft | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, meta_pattern | Meta-pattern: design principle for template authoring (embed coaching alongside schema). Template-of-templates would be overly meta. |
| 37 | karpathy-llm-knowledge-base-obsidian-rag | Memory Architecture | P1 | - | pattern | HIGH | auto | N | reusable_shape, multi_source, forces_tradeoffs | Compiler pipeline architecture. |
| 38 | four-tier-agent-memory-model-with-write-policy | Memory Architecture | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, compositional_primitive | Tiered architecture + write policy governance. |
| 39 | memory-cross-layer-promotion-governance | Memory Architecture | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, co_occurrence_rule | Rule co-occurrence. Specific constraint ('every promotion must be policy-gated') is a rule. Finding describes broader governance architecture. |
| 40 | review-obsolescence-as-design-goal | Governance | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, design_principle | Design principle, not a constraint. |
| 41 | agent-identity-governance-enforcement-layer | Governance | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, compositional_primitive | Architecture pattern with time-boxed decision lanes. |
| 42 | trust-calibration-progressive-autonomy-ramp | Governance | P2 | - | pattern | HIGH | auto | N | reusable_shape, multi_source, forces_tradeoffs | Per-task-type ramp, not global. |
| 43 | acceptance-criteria-as-verifiable-eval-anchor | Intent Engineering | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, compositional_primitive | Three-component discipline (criteria + eval cases + iteration anchor). |
| 44 | intent-engineering-framework-seven-part-agent-inten | Intent Engineering | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, compositional_primitive | Framework trap noted. 7-part structure should be codified as pattern before downstream templates wrap it. |
| 45 | stop-rules-as-execution-boundaries | Intent Engineering | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, meta_pattern | Meta-pattern: design principle for stop rules (3 types + enforcement layers). Specific stop rules are downstream rules. |

## Batch 4 — 5 new findings (closeout)

| # | id | category | pri | candidate | assigned | conf | tier | override | reason_codes | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 46 | tiered-permission-system-bash-safety | Sandboxing | P1 | - | pattern | HIGH | auto | N | reusable_shape, multi_source, forces_tradeoffs | Three-tier trust architecture + command pre-classification. |
| 47 | os-level-agent-sandboxing-filesystem-network-isolation | Sandboxing | P1 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, compositional_primitive | OS-primitive isolation on two dimensions (filesystem + network). |
| 48 | credential-isolation-bundled-auth-vault-proxy | Sandboxing | P2 | - | pattern | HIGH | auto | N | reusable_shape, forces_tradeoffs, compositional_primitive | Two complementary isolation patterns (bundled auth + vault proxy). |
| 49 | advisor-executor-api-pattern | Model Selection | P1 | - | pattern | HIGH | auto | N | reusable_shape, role_count_gt_1, forces_tradeoffs | Two-role system (advisor + executor). DDc-2 applies. |
| 50 | task-specific-model-routing-table-march-2026-bench | Model Selection | P1 | - | pattern | HIGH | auto | N | reusable_shape, multi_source, forces_tradeoffs | Template co-occurrence. Current table is ephemeral (changes per benchmark cycle); approach of task-specific routing is the durable pattern. |

---

## Procedure (per finding)

1. Read the finding file.
2. Read its inclusion-signals section in the rubric for each of the 5 forms.
3. Apply exclusion tests — which forms are ruled out?
4. Score the remaining forms; pick one.
5. Write `assigned`, `conf`, `tier`, `override` (Y if candidate disagrees with assigned), `reason_codes` (up to 3, from the rubric vocabulary).
6. If the finding exposed a rubric gap — an inclusion signal that should exist, a new exclusion test, a reason code that should be canonical — note it in the `notes` column AND amend the rubric in place (this is the point of the exercise).
7. Mark `candidate` from the finding's `candidate_form` field if present; if not present, write `-`.

**Rubric amendment protocol:** when amending the rubric during classification, also note the amendment's row number here so the calibration set tracks rubric version drift. If a late classification conflicts with an early one under a new amendment, re-visit the early classification.

---

## Rollup (populated as classifications complete)

| Form | Count | % | Notes |
|---|---|---|---|
| pattern | 46 | 92% | Default form, as predicted by rubric finding #5 |
| skill | 2 | 4% | 1 anchor (row 5), 1 batch 3 (row 35) |
| rule | 1 | 2% | 1 batch 3 (row 34) — anti-pattern framing |
| template | 1 | 2% | 1 batch 2 (row 21) — fillable scaffold |
| agent | 0 | 0% | DDc-2 bias toward pattern confirmed across all batches |

| Tier | Count | % |
|---|---|---|
| auto | 43 | 86% |
| guided | 7 | 14% |
| hitl | 0 | 0% |

| Override | Count | % |
|---|---|---|
| Y | 1 | 2% |
| N | 49 | 98% |

**Override rate:** 2% (1/50) — below 5–15% target. Non-diagnostic: 45 of 50 candidates are `-` (no proposer candidate set). Override measurement only activates when the proposer has made a call. The anchor override (row 4, agent→pattern) is the sole contributor.

**Form distribution analysis (all batches):**
- Batch 1 (10): 10 pattern. All P1, Strong evidence — well-established design approaches.
- Batch 2 (15): 14 pattern, 1 template. Template (row 21) is a fillable scaffold with named variables.
- Batch 3 (15): 13 pattern, 1 rule, 1 skill. Rule (row 34) is an anti-pattern finding; skill (row 35) describes a specific procedural artifact.
- Batch 4 (5): 5 pattern. Sandboxing + model selection categories are architecture-level, naturally pattern-shaped.
- Pattern dominance (92%) validates rubric finding #5. Non-pattern forms emerge only when findings describe specific mechanisms (rule), fillable scaffolds (template), or procedural artifacts (skill).
- Rule co-occurrence noted in 6 findings (rows 13, 23, 33, 39, 45, and the anchor row 4's agent→pattern override) — specific constraints or roles embedded in pattern-level findings. Strongly supports the hypothesis that rules are primarily downstream artifacts from `/extract-artifacts`.
- Template co-occurrence noted in 4 findings (rows 19, 29, 36, 50) — scaffold structures embedded in pattern-level findings. Templates similarly tend to be downstream artifacts.
- Zero agent classifications. Every multi-role finding resolved to pattern via DDc-2 (rows 18, 28, 49). Single-role findings with specific dispositions did not appear in this sample.

**Calibration set complete.** 50/50 findings classified. 2 rubric amendments applied.

---

## Rubric amendments log (populated as batches run)

### Amendment 1 — Confidence measures form-classification certainty, not evidence strength

- **Triggered by:** Batch 1, rows 6–15 (multiple single-source findings with unambiguous form classification)
- **Rubric section:** Top-level, after tier dispatch logic (new paragraph before §1)
- **Before:** Confidence signals in §1–§5 reference "multiple independent known uses" for HIGH, conflating evidence strength with form-classification certainty
- **After:** Added clarification that `router_confidence` measures form-classification certainty specifically. Evidence strength is captured by the finding's existing `evidence_strength` field and gates `priority`, not `router_confidence`. A single-source finding can be HIGH confidence if the form is unambiguous.
- **Impact on classifications:** Row 9 remains MED (genuine form ambiguity — problem framing vs solution shape, not evidence thinness). Rows 7, 10, 12, 13, 15 are HIGH despite single sources because no other form is a plausible fit.

### Amendment 2 — Anti-pattern findings as natural rule candidates

- **Triggered by:** Batch 3, row 34 (reasoning-model-anti-pattern-prescribed-reasoning)
- **Rubric section:** §3 Rule, inclusion signals
- **Before:** Rule inclusion signals describe "must / must not / always / never" language but don't explicitly mention anti-pattern findings
- **After:** Added: "Anti-pattern findings ('never do X', 'this technique degrades performance') are natural rule candidates when the anti-pattern is expressible as a deterministic check at a named boundary."
- **Impact on classifications:** Row 34 classified as rule (MED, guided). No retroactive impact on prior classifications — no earlier findings had anti-pattern framing at the mechanism level.

---

## Links

- Rubric: [[2026-04-11-form-classification-rubric]]
- Session 20 pattern exercises (in PROGRESS.md): anchors 1–3
- Session 21 rule/template/skill/agent exercises (this handoff): anchors 4–5 and rubric
- IB candidates from rubric: IBc-1 (this doc), IBc-2 (`/rubric-apply` dry-run skill)
