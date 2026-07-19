---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-07-19"
source_guide: "building-agent-evaluation-suites"
finding_count: 77
practitioner_question_count: 2
session: 152
sl: "session-152 (SL retired as producer per session-138 ruling; git is the session record)"
---

# Split Proposal — Building Agent Evaluation Suites

Reaffirms and supersedes the 2026-07-16 (session-147) proposal for the same guide. The
bifurcation is unchanged; this regen adds 4 P2 Evaluation findings (73 → 77), all of
which route cleanly under the existing A/B seam. Emitted as a DD-98 side-channel artifact
only — the session-152 regen proceeded against the existing single-guide structure and was
not blocked.

## Source guide identity

- **Guide stem:** `building-agent-evaluation-suites`
- **Current title:** "Building Agent Evaluation Suites"
- **Finding count:** 77 (post-resolution; ≥25 — largest cluster in the corpus)
- **Routing-table row:** G4 in `operations/references/guide-routing-table.md` (Synthesis Status table)

## Practitioner-question analysis

Unchanged from session 147: the cluster spans two distinct reader questions. The session-152
intake (+4 findings) reinforces the same seam — three of the four are verification-architecture
material (Q1), one is improvement-loop material (Q2).

1. **Q1: "How do I verify my agent's output actually works?"**
   Eval-suite design (assertions, metrics, test inputs), verification architectures
   (builder-validator, dual-blind, holdout, goal-backward, cross-model, fleet review),
   production evaluation, deploy gating, benchmark/infrastructure discipline, quality gates.

2. **Q2: "How do I use evals to drive autonomous improvement of my agent and its skills?"**
   Eval-driven improvement loops (keep/revert, convergence contracts, execution-feedback
   signals, converting review feedback into durable checks), skill lifecycle evaluation
   (triggering/functional/performance tiers, description optimization, with/without baselines,
   smells triage, adopt-only-with-evidence).

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `verifying-agent-output` — practitioner question: "How do I verify my agent's output actually works?"
- **Destination B:** `eval-driven-improvement-loops` — practitioner question: "How do I use evals to drive autonomous improvement of my agent and its skills?"

Per-finding routing (every finding routed; no implicit handling per DD-98 §Rules #4). The
73 pre-existing rows carry over from the session-147 proposal unchanged; the 4 new rows are
marked **(new s152)**.

| Finding | Disposition |
|---------|-------------|
| [[agent-self-reporting-unreliability-independent-eval]] | A |
| [[binary-eval-assertion-design-deterministic-plus-ll]] | A |
| [[claude-code-skills-20-four-mode-skill-lifecycle-wi]] | B |
| [[context-pollution-same-window-verification-bias]] | A |
| [[eval-awareness-autonomous-benchmark-identification]] | A |
| [[independent-eval-and-scoped-authority-commandments]] | A |
| [[infrastructure-noise-agentic-eval-confounding]] | A |
| [[pass-at-k-vs-pass-caret-k-eval-metrics]] | A |
| [[system-event-logging-actions-not-words]] | A |
| [[three-tier-grading-hierarchy]] | A |
| [[tool-shaped-object-evaluation-lens]] | A |
| [[two-level-verification-agent-run-plus-harness-inte]] | A |
| [[ultra-review-multi-agent-bug-hunting-fleet]] | A |
| [[verification-agent-seven-prompt-patterns]] | A |
| [[volume-over-quality-eval-principle]] | A |
| [[inter-agent-web-contamination-eval-artifact-persist]] | A |
| [[capability-vs-regression-eval-lifecycle]] | shared (route to both — suite lifecycle governs A's regression suites and B's graduation rules) |
| [[mcp-evaluation-primitives-deepeval-metrics]] | A |
| [[test-input-coverage-design-15-30-sweet-spot]] | A |
| [[ace-execution-feedback-no-labels-required]] | B |
| [[bmad-deterministic-skill-validator]] | A |
| [[llm-as-judge-pattern-for-verification-agents]] | A |
| [[benchmark-signal-mismatch-optimization-gap]] | A |
| [[eval-driven-development-autonomous-quality]] | B |
| [[success-rate-eval-over-binary-pass-fail]] | A |
| [[gstack-review-army-parallel-specialist-dispatch]] | A |
| [[four-layer-production-eval-stack-with-golden-traces]] | A |
| [[gsd-gates-taxonomy-four-canonical-types]] | A |
| [[multidimensional-success-criteria-smart]] | A |
| [[arc-agi-3-zero-percent-abstract-reasoning]] | A |
| [[ensemble-eval-majority-required-for-success]] | A |
| [[production-configuration-baseline-discipline]] | A |
| [[builder-validator-chain-pattern]] | A |
| [[context-order-diversity-for-bug-detection]] | A |
| [[four-layer-agent-evaluation-architecture]] | A |
| [[goal-backward-verification]] | A |
| [[karpathy-autoresearch-self-improvement-loop]] | B |
| [[march-of-nines-compounding-reliability-math-for-m]] | A |
| [[per-query-production-eval-pipeline]] | A |
| [[production-database-wipeout-agent-context]] | A |
| [[tdd-step-ordering-in-plan-tasks]] | A |
| [[tiered-review-escalation-strategy]] | A |
| [[data-agent-benchmark-dab-cross-dbms-pipeline-eval]] | A |
| [[factorial-design-eval-systematic-context-variati]] | A |
| [[holdout-validation-pattern-blind-regression]] | A |
| [[test-driven-development-as-counterweight-to-agenti]] | A |
| [[iterative-refinement-loop-with-quality-gate]] | B |
| [[generator-assessor-separation-in-skill-iteration]] | shared (route to both — the architectural invariant under A's verifier isolation and B's grader/comparator roles) |
| [[dual-verification-trajectory-vs-output-correctness]] | A |
| [[repeated-sampling-scaling-law-and-verifier-ceiling]] | A |
| [[with-without-skill-ab-baseline-measurement]] | B |
| [[confirm-failure-first-tdd-agent-discipline]] | A |
| [[agentic-harness-self-assessment-skill]] | A |
| [[balanced-positive-negative-eval-sets]] | A |
| [[convergence-loop-optimizer-family-contract]] | B |
| [[cross-model-verification-for-bug-finding]] | A |
| [[deterministic-store-checker-runtime-threshold-flags]] | A |
| [[enumerate-dont-fix-hostile-reviewer-prompt]] | A |
| [[eval-driven-tool-iteration-loop]] | B |
| [[eval-rubric-carve-outs-subjective-and-script-core-skills]] | shared (route to both — re-anchors A's assertion-design rules and B's skill-audit rubrics) |
| [[five-point-agent-health-checklist]] | A |
| [[harness-cost-readout-unreliability-independent-log-accounting]] | A |
| [[hook-based-enforcement-for-agent-outputs]] | A |
| [[loop-detection-hash-based-sliding-window]] | A |
| [[no-mistakes-post-implementation-validation-pipeline]] | A |
| [[persona-clone-review-board]] | A |
| [[qa-agent-independent-compliance-review]] | A |
| [[self-evolving-loop-pattern]] | B |
| [[skill-description-optimization-loop-held-out-test]] | B |
| [[skill-popularity-vs-measured-efficacy]] | B |
| [[skill-smells-triage-layer-before-full-audit]] | B |
| [[skill-testing-three-tier-trigger-functional-perf]] | B |
| [[task-risk-gradient-for-verification-depth]] | A |
| [[evals-folder-as-first-class-deploy-gate]] | A **(new s152)** — deploy-time eval gate is a verification mechanism |
| [[review-outcome-not-diff-for-agent-changes]] | A **(new s152)** — review-design pattern for verifying batched agent changes |
| [[pre-code-validation-contracts-dual-blind-validators]] | A **(new s152)** — verification architecture (contract-first + dual blind validators) |
| [[garbage-collection-day-persona-review-agents]] | B **(new s152)** — converting review feedback into durable automated checks is improvement-loop material |

Routing summary: 60 → A, 14 → B, 3 shared, 0 contested. Bifurcation precision: 96% routed cleanly (unchanged from session 147).

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture (no `## Nick's Annotations`, no
`<!-- PRESERVE -->` regions as of the 2026-07-19 capture). A split carries no preservation
complexity.

## Routing-table impact

- **Source guide:** proposed deprecation (`stage: deprecated`) post-split, following the G2 → G2a/G2b precedent (source archived, row marked deprecated).
- **New rows:**
  - `verifying-agent-output` — question: "How do I verify my agent's output actually works?", stage: verify, dimension: Evaluation, lifecycle stage = `draft`.
  - `eval-driven-improvement-loops` — question: "How do I use evals to drive autonomous improvement of my agent and its skills?", stage: verify/operate, dimension: Evaluation, lifecycle stage = `draft`.
- **Dimension → Guide mapping changes:** Evaluation's primary guide becomes the A/B pair (mirror the Context Engineering G2a/G2b row shape). Secondary mapping "Safety inherits independent-eval findings" stays pointed at A. B becomes a secondary guide for Tools (eval-driven tool iteration) — note only; no Tools-row change required until demand shows.

## Codifier recommendation

**Recommendation:** proceed with split as proposed

**Rationale:** Reaffirms the session-147 call. Bifurcation remains clean (96% single-destination,
3 shared, 0 contested) and the +4 intake reinforces rather than muddies the seam. The source guide
is the corpus's largest (77 findings, ~1300 lines) and carries the improvement-loop material as two
overloaded steps (8/8b) that would become B's spine; the two questions have different readers
(suite designer vs. loop builder). No preserved-section complexity exists. This proposal has now
fired at two consecutive regens — the volume is not receding, which strengthens the case for acting
before the next staleness crossing.

## Notes

- The session-152 regen of the source guide proceeded against the existing single-guide structure per DD-98 (proposal is a side-channel; regen not blocked).
- Supersedes `2026-07-16-building-agent-evaluation-suites-split-proposal.md` (same bifurcation, +4 findings). Nick reads the latest.
- The harvest queue (`building-agent-evaluation-suites.harvest-queue.md`) transfers with the split per destination of each row's source finding if the split executes.
