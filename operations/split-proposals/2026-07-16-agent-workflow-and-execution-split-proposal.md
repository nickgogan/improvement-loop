---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-07-16"
source_guide: "agent-workflow-and-execution"
finding_count: 37
practitioner_question_count: 2
session: 147
sl: "session-147 (SL retired as producer per session-138 ruling; git is the session record)"
---

# Split Proposal — Agent Workflow and Execution

## Source guide identity

- **Guide stem:** `agent-workflow-and-execution`
- **Current title:** "Agent Workflow and Execution"
- **Finding count:** 37 (post-resolution; ≥25)
- **Routing-table row:** G3b in `operations/references/guide-routing-table.md` (Synthesis Status table + cluster-identity table, "How do I run agents in production?", stage: operate, dimension: Orchestration)

## Practitioner-question analysis

The source cluster covers 2 distinct practitioner questions:

1. **Q1:** "How do I make production agent workflows reliable, observable, and reviewable?"
   - Execution mechanics for supervised production operation: plan/execute separation, workflow state, persistence, cost control, observability, degradation, course correction, review bandwidth, and workflow routing/dispatch.
   - Findings clustering against Q1: [[planner-executor-deterministic-guardrails]], [[workflow-state-vs-conversation-state]], [[session-persistence-crash-resilient]], [[session-as-append-only-event-log]], [[skill-vs-process-distinction-deterministic-rails]], [[gsd-stall-detection-revision-loop-escalation]], [[structured-streaming-events-observability]], [[unified-tracing-opentelemetry-for-agents]], [[review-pipeline-bottleneck-and-quality-at-source]], [[staged-delivery-for-review-digestibility]], [[task-complexity-tiering-quick-campaign-deep-build]], [[sprint-contract-negotiation-pattern]], [[cloud-local-plan-handoff-teleport-pattern]], [[bmad-help-adaptive-module-routing]], [[token-budget-pre-turn-projection]], [[org-redesign-for-agentic-throughput-high-speed-rail]], [[correct-course-mid-project-pivot-command]], [[self-improvement-dispatch-table-route-never-reimplement]], [[description-based-workflow-routing-lazy-dispatch]], [[cross-project-workflow-portability-register-and-run]], [[concept-family-explorer-five-neighborhood-gap-mapping]]
2. **Q2:** "How do I run agents unattended — scheduled, headless, and autonomous?"
   - Removing the human from the loop: scheduling surfaces, headless composition, skill/routine chaining, autonomous pipeline anatomy, autonomy levels, and portfolio monitoring of recurring runs.
   - Findings clustering against Q2: [[claude-code-loop-in-session-cron-scheduling]], [[headless-cron-composition-autonomous-scheduled-workflows]], [[scheduled-skill-chaining-with-file-based-activation]], [[claude-routines-webhook-triggered-pipeline-chaining]], [[build-loop-skill-autonomous-phase-driver]], [[dark-factory-ai-only-codebase-management]], [[multi-day-autonomous-scientific-computing-workflow]], [[headless-multi-pass-iterative-review]], [[ecosystem-monitoring-meta-loop]], [[scheduled-task-dashboard-observability-layer]], [[github-label-as-workflow-state]], [[end-to-end-sequential-bug-fix-pipeline]]

Note: the routing/dispatch sub-theme (5 findings inside Q1) is currently a Step within Q1's territory, not a third question; if it keeps accreting findings it may bifurcate out of Q1 on a later regen.

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `production-agent-execution` — practitioner question: "How do I make production agent workflows reliable, observable, and reviewable?"
- **Destination B:** `autonomous-scheduled-agent-operation` — practitioner question: "How do I run agents unattended — scheduled, headless, and autonomous?"

Per-finding routing (every finding routed; no implicit handling per DD-98 §Rules #4):

| Finding | Disposition |
|---------|-------------|
| [[planner-executor-deterministic-guardrails]] | A |
| [[workflow-state-vs-conversation-state]] | A |
| [[session-persistence-crash-resilient]] | A |
| [[session-as-append-only-event-log]] | A |
| [[skill-vs-process-distinction-deterministic-rails]] | A |
| [[gsd-stall-detection-revision-loop-escalation]] | A |
| [[structured-streaming-events-observability]] | A |
| [[unified-tracing-opentelemetry-for-agents]] | A |
| [[review-pipeline-bottleneck-and-quality-at-source]] | A |
| [[staged-delivery-for-review-digestibility]] | A |
| [[task-complexity-tiering-quick-campaign-deep-build]] | A |
| [[sprint-contract-negotiation-pattern]] | A |
| [[cloud-local-plan-handoff-teleport-pattern]] | A |
| [[bmad-help-adaptive-module-routing]] | A |
| [[token-budget-pre-turn-projection]] | A |
| [[org-redesign-for-agentic-throughput-high-speed-rail]] | A |
| [[correct-course-mid-project-pivot-command]] | A |
| [[self-improvement-dispatch-table-route-never-reimplement]] | A |
| [[description-based-workflow-routing-lazy-dispatch]] | A |
| [[cross-project-workflow-portability-register-and-run]] | A |
| [[concept-family-explorer-five-neighborhood-gap-mapping]] | A |
| [[claude-code-loop-in-session-cron-scheduling]] | B |
| [[headless-cron-composition-autonomous-scheduled-workflows]] | B |
| [[scheduled-skill-chaining-with-file-based-activation]] | B |
| [[claude-routines-webhook-triggered-pipeline-chaining]] | B |
| [[build-loop-skill-autonomous-phase-driver]] | B |
| [[dark-factory-ai-only-codebase-management]] | B |
| [[multi-day-autonomous-scientific-computing-workflow]] | B |
| [[headless-multi-pass-iterative-review]] | B |
| [[ecosystem-monitoring-meta-loop]] | B |
| [[scheduled-task-dashboard-observability-layer]] | B |
| [[github-label-as-workflow-state]] | B |
| [[end-to-end-sequential-bug-fix-pipeline]] | B |
| [[durable-workflow-engine-for-agent-systems]] | shared (route to both — durable execution underpins supervised long-running workflows AND unattended pipelines) |
| [[archon-yaml-defined-harness-workflows]] | shared (route to both — the YAML DAG substrate carries both supervised and autonomous execution) |
| [[agent-cost-blowup-mitigation-strategies]] | shared (route to both — budgets/caps apply to interactive workflows and are existential for unattended ones) |
| [[graceful-degradation-modes-for-agent-failure]] | shared (route to both — degradation modes are the failure contract in both operating regimes) |

Bifurcation precision: 33/37 (89%) routed cleanly; 4/37 (11%) shared; 0 contested.

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture (no `## Nick's Annotations` section, no `<!-- PRESERVE -->` regions — verified at Step 0.5 of the 2026-07-16 regen).

## Routing-table impact

- **Source guide:** proposed deprecation (`stage: deprecated`) post-split.
- **New rows:**
  - `production-agent-execution` — question "How do I make production agent workflows reliable, observable, and reviewable?", stage: operate, dimension: Orchestration, lifecycle stage = `draft`.
  - `autonomous-scheduled-agent-operation` — question "How do I run agents unattended — scheduled, headless, and autonomous?", stage: operate, dimension: Orchestration, lifecycle stage = `draft`.
- **Dimension → Guide mapping changes:** Orchestration's operate-stage routing splits across both destinations; trigger keywords partition (workflow, execution, cost, degradation, stall detection, observability, tracing, sprint contract → A; scheduled, headless, cron, routine, autonomous, dark factory, unattended, loop portfolio → B; durable workflow → both).

## Codifier recommendation

**Recommendation:** proceed with split as proposed

**Rationale:** Bifurcation is clean (89% single-destination, 0 contested, only 4 deliberately-shared substrate findings), both destinations are viable guide-sized clusters (21 and 12 findings), and there are no preserved surfaces to dispose. The Q2 cluster grew from 3 to 12 findings in this regen — the two reader intents (harden a supervised workflow vs. remove the human from the loop) are diverging, not converging.

## Notes

- The G3 pass (session 147) routed 12 Orchestration findings into this cluster; this regen absorbed them plus 5 swept additions, which is what pushed the cluster over both thresholds simultaneously.
- If Nick prefers a smaller step, an alternative is to defer and re-evaluate at the next regen; the guide remains coherent as a single document today (Steps 1-8 serve Q1, Steps 9-10 serve Q2, Step 11 serves Q1's routing sub-theme).
