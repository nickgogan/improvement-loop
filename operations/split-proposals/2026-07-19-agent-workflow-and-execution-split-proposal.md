---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-07-19"
source_guide: "agent-workflow-and-execution"
finding_count: 42
practitioner_question_count: 2
session: 152
sl: "session-152 (SL retired as producer per session-138 ruling; git is the session record)"
---

# Split Proposal — Agent Workflow and Execution

**Second consecutive firing.** The DD-98 trigger fired at 37 findings on 2026-07-16 (session 147, `2026-07-16-agent-workflow-and-execution-split-proposal.md`, recommendation *proceed*). This regen adds 5 wave-4 findings (→42), 4 of which land in the unattended/autonomous half — the bifurcation is sharper, not softer, than at the prior gate. Nick has not yet ruled the prior proposal; this supersedes it as the current-state view.

## Source guide identity

- **Guide stem:** `agent-workflow-and-execution`
- **Current title:** "Agent Workflow and Execution"
- **Finding count:** 42 (post-resolution; ≥25)
- **Routing-table row:** G3b in `operations/references/guide-routing-table.md` ("How do I run agents in production?", stage: operate, dimension: Orchestration)

## Practitioner-question analysis

The source cluster covers 2 distinct practitioner questions:

1. **Q1:** "How do I make production agent workflows reliable, observable, and reviewable?"
   - Execution mechanics for supervised production operation: plan/execute separation, workflow state, persistence, cost control, observability, degradation, course correction, review bandwidth, quality-at-source, and workflow routing/dispatch.
   - Wave-4 addition into Q1: [[lint-test-failures-as-remediation-prompts]] (quality-at-source authoring — failure messages as prompts).
2. **Q2:** "How do I run agents unattended — scheduled, headless, and autonomous?"
   - Removing the human from the loop: scheduling surfaces, trigger shapes, headless composition, skill/routine chaining, loop-contract governance, autonomous pipeline anatomy, autonomy levels, and portfolio monitoring.
   - Wave-4 additions into Q2: [[loop-trigger-taxonomy-poll-then-wake-combo]], [[loop-contract-anatomy-and-evolve-session-cadence]], [[pre-merge-reconciliation-queue]] — all three are unattended-operation material, which is what pushed the divergence.

Note: the routing/dispatch sub-theme (Step 11, ~5 findings inside Q1) remains a Step within Q1's territory, not yet a third question.

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `production-agent-execution` — "How do I make production agent workflows reliable, observable, and reviewable?"
- **Destination B:** `autonomous-scheduled-agent-operation` — "How do I run agents unattended — scheduled, headless, and autonomous?"

Per-finding routing (only deltas from the 2026-07-16 proposal shown in full; the 37 prior dispositions carry over unchanged):

| Finding | Disposition |
|---------|-------------|
| [[lint-test-failures-as-remediation-prompts]] | A (quality-at-source authoring standard for supervised execution) |
| [[loop-trigger-taxonomy-poll-then-wake-combo]] | B (how a scheduled loop wakes; the scheduling-gap material) |
| [[loop-contract-anatomy-and-evolve-session-cadence]] | B (per-loop governance/memory for recurring autonomous loops) |
| [[pre-merge-reconciliation-queue]] | B (operating model for many concurrent autonomous writers) |
| [[durable-checkpointed-sessions-as-framework-default]] | shared (durable execution underpins supervised long-running workflows AND unattended pipelines; mirrors [[durable-workflow-engine-for-agent-systems]]) |

Carried-over dispositions (from the 2026-07-16 proposal): 20 → A, 12 → B, 4 shared.

**Aggregate bifurcation:** A = 22, B = 15, shared = 5, contested = 0 (total 42). Precision: 37/42 (88%) routed cleanly; 5/42 (12%) shared; 0 contested.

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture (no `## Nick's Annotations` section, no `<!-- PRESERVE -->` regions — verified at Step 0.5 of this regen).

## Routing-table impact

- **Source guide:** proposed deprecation (`stage: deprecated`) post-split.
- **New rows:**
  - `production-agent-execution` — stage: operate, dimension: Orchestration, lifecycle stage = `draft`.
  - `autonomous-scheduled-agent-operation` — stage: operate, dimension: Orchestration, lifecycle stage = `draft`.
- **Dimension → Guide mapping changes:** Orchestration's operate-stage routing splits across both destinations; trigger keywords partition (workflow, execution, cost, degradation, stall detection, observability, tracing, sprint contract, quality-at-source → A; scheduled, headless, cron, trigger shape, routine, loop contract, autonomous, dark factory, unattended, reconciliation queue → B; durable workflow → both). Note: [[lint-test-failures-as-remediation-prompts]] carries `category: Context Engineering` — its inclusion here was a Nick-ruled cross-dimension routing (session 152); on split it stays with A but the dimension-map footnote should record the cross-dimension provenance.

## Codifier recommendation

**Recommendation:** proceed with split as proposed

**Rationale:** Second consecutive firing with a *strengthening* signal — the 5 wave-4 findings split 4:1 toward Q2's unattended/autonomous territory, widening (not blurring) the gap the 2026-07-16 proposal identified. Bifurcation remains clean (88% single-destination, 0 contested, 5 deliberately-shared substrate findings), both destinations are viable guide-sized clusters (22 and 15), and there are no preserved surfaces to dispose. The one soft spot is unchanged: several genuinely-shared findings (durable execution, cost/budget caps, degradation modes, YAML-DAG substrate) serve both regimes and would need deliberate duplication or a cross-reference on split — this is the normal 12% shared tax, not a blocker. If Nick prefers a smaller step, deferral is safe: the guide remains coherent as a single document today (Steps 1-8 + 11 serve Q1, Steps 9-10 serve Q2).

## Notes

- This regen was a Nick-requested wave-4 refresh (queue item 1, session 152), not a split action; the split proposal is the mandatory DD-98 side-channel artifact and changes nothing about the guide, routing table, or changelog.
- The prior proposal (`2026-07-16-...`) remains on disk for audit; both are retained. Nick reads the latest.
