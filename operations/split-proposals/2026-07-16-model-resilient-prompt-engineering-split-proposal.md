---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-07-16"
source_guide: "model-resilient-prompt-engineering"
finding_count: 37
practitioner_question_count: 2
session: 147
sl: "session-147 (SL retired as producer per session-138 ruling; git is the session record)"
---

# Split Proposal — Model-Resilient Prompt Engineering

## Source guide identity

- **Guide stem:** `model-resilient-prompt-engineering`
- **Current title:** "Model-Resilient Prompt Engineering"
- **Finding count:** 37 (post-resolution; ≥25)
- **Routing-table row:** G8 in `operations/references/guide-routing-table.md`

## Practitioner-question analysis

The source cluster covers 2 distinct practitioner questions:

1. **Q1:** "How do I write prompts and instructions that survive model upgrades and steer reliably?"
   - Core concern: durability properties, reasoning anti-patterns, declarative vs SOP prompting, constraint engineering, instruction/skill craft (descriptions, leading words, explain-the-why, strictness), spec alignment, layered assembly and caching, output grounding, prompt lifecycle and metaprompting.
   - Findings clustering against Q1: [[model-agnostic-prompting-three-properties]], [[reasoning-model-anti-pattern-prescribed-reasoning]], [[extract-deep-plan-prompt-as-custom-skill]], [[brevity-constraints-reverse-llm-performance]], [[advanced-elicitation-techniques-library]], [[oneshot-infrastructure-setup-prompt-pattern]], [[negative-constraints-as-probabilistic-output-collapse]], [[yaml-template-dual-structure]], [[design-evaluate-dual-phase-prompting-framework]], [[prompt-as-policy-version-control-and-cicd-for-agen]], [[bmad-outcome-based-skill-rewrite-pattern]], [[layered-prompt-assembly-stable-segment-caching]], [[bidirectional-prompting-for-spec-creation]], [[metaprompting-karpathy-autoresearch-for-build]], [[programmatic-snippet-extraction-via-shell-anti-hallucination]], [[star-commands-for-explicit-output-format-override]], [[declarative-goal-driven-agent-prompting]], [[hands-off-routine-prompt-precision-pattern]], [[leading-words-lexical-steering-reasoning-trace-verification]], [[progressive-search-wide-then-narrow]], [[seven-rung-minimal-code-decision-ladder]], [[skill-authoring-explain-the-why-not-musts]], [[skill-description-structure-what-when-capabilities]], [[strictness-escalation-skill-architecture]], [[surgical-change-constraint-agent-scope]], [[thinking-models-mental-framework-commands-for-codi]], [[gstack-office-hours-socratic-discovery-pipeline]], [[dev-cost-estimation-bias-correction]]
2. **Q2:** "Which model, tier, and effort level do I run each task on — and where does that decision bind?"
   - Core concern: task classification (center vs edge of distribution), benchmark-based routing tables, effort-level tuning, dispatch-time model explicitness, session-boundary model pinning, the frontier-prototype-then-downshift lifecycle, advisor-executor pairing, release-cadence review triggers.
   - Findings clustering against Q2: [[advisor-executor-api-pattern]], [[task-specific-model-routing-table-march-2026-bench]], [[frontier-release-compression-march-2026]], [[mandatory-explicit-model-per-dispatch]], [[effort-level-tuning-as-first-order-cost-lever]], [[no-mid-session-model-switching-subagent-handoff]], [[prototype-at-frontier-then-downshift]], [[center-vs-edge-of-distribution-task-classification]]

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `model-resilient-prompt-engineering` (retains stem) — practitioner question: "How do I write prompts and instructions that survive model upgrades and steer reliably?"
- **Destination B:** `selecting-and-routing-models` — practitioner question: "Which model, tier, and effort level do I run each task on — and where does that decision bind?"

Per-finding routing (every finding routed; no implicit handling per DD-98 §Rules #4):

| Finding | Disposition |
|---------|-------------|
| [[model-agnostic-prompting-three-properties]] | A |
| [[reasoning-model-anti-pattern-prescribed-reasoning]] | A |
| [[extract-deep-plan-prompt-as-custom-skill]] | A |
| [[brevity-constraints-reverse-llm-performance]] | A |
| [[advanced-elicitation-techniques-library]] | A |
| [[oneshot-infrastructure-setup-prompt-pattern]] | A |
| [[negative-constraints-as-probabilistic-output-collapse]] | A |
| [[yaml-template-dual-structure]] | A |
| [[design-evaluate-dual-phase-prompting-framework]] | A |
| [[prompt-as-policy-version-control-and-cicd-for-agen]] | A |
| [[bmad-outcome-based-skill-rewrite-pattern]] | A |
| [[layered-prompt-assembly-stable-segment-caching]] | A |
| [[bidirectional-prompting-for-spec-creation]] | A |
| [[metaprompting-karpathy-autoresearch-for-build]] | A |
| [[programmatic-snippet-extraction-via-shell-anti-hallucination]] | A |
| [[star-commands-for-explicit-output-format-override]] | A |
| [[declarative-goal-driven-agent-prompting]] | A |
| [[hands-off-routine-prompt-precision-pattern]] | A |
| [[leading-words-lexical-steering-reasoning-trace-verification]] | A |
| [[progressive-search-wide-then-narrow]] | A |
| [[seven-rung-minimal-code-decision-ladder]] | A |
| [[skill-authoring-explain-the-why-not-musts]] | A |
| [[skill-description-structure-what-when-capabilities]] | A |
| [[strictness-escalation-skill-architecture]] | A |
| [[surgical-change-constraint-agent-scope]] | A |
| [[thinking-models-mental-framework-commands-for-codi]] | A |
| [[gstack-office-hours-socratic-discovery-pipeline]] | A |
| [[dev-cost-estimation-bias-correction]] | A |
| [[advisor-executor-api-pattern]] | B |
| [[task-specific-model-routing-table-march-2026-bench]] | B |
| [[frontier-release-compression-march-2026]] | B |
| [[mandatory-explicit-model-per-dispatch]] | B |
| [[effort-level-tuning-as-first-order-cost-lever]] | B |
| [[no-mid-session-model-switching-subagent-handoff]] | B |
| [[prototype-at-frontier-then-downshift]] | B |
| [[center-vs-edge-of-distribution-task-classification]] | B |
| [[cot-fails-without-inductive-generalization]] | shared (route to both — durability ceiling for A; route-to-human hard ceiling for B) |

Bifurcation precision: 36/37 route cleanly (97%); 1 shared; 0 contested.

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture (no `## Nick's Annotations` section, no `<!-- PRESERVE -->` regions).

## Routing-table impact

- **Source guide:** G8 row retitled/kept as Destination A (prompt craft only); not deprecated — the stem and the majority cluster stay in place.
- **New rows:**
  - `selecting-and-routing-models` — practitioner question Q2, dimension: Model Selection, stage: build, lifecycle stage = `draft`.
- **Dimension → Guide mapping changes:** `Model` row primary guide becomes `selecting-and-routing-models` (currently "Model-Resilient Prompt Engineering"); its note "Model routing → Architecture; model prompting → Prompt Engineering" gains a third clause: model/tier/effort *selection* → Destination B. `Prompt` row unchanged (the pre-declared "split when mass justifies it" condition is what this proposal exercises). G3 keeps model-routing *topology* (orchestrator/subagent tiering architecture); Destination B holds selection/binding discipline — boundary note needed in Disambiguation Notes.

## Codifier recommendation

**Recommendation:** proceed with split as proposed

**Rationale:** Bifurcation is clean (97% routed, 1 shared, 0 contested) and the routing table pre-declared this exact split ("Shares guide with Model; split when mass justifies it"). Destination B starts at 9 findings — above the 5-finding graduation threshold — and Model Selection is accreting fast (5 new P2 findings in the past 5 weeks). Caveat for Nick's gate: Destination A remains >25 findings but single-question (monitor per DD-98 dispatch), and B's boundary with G3 (routing topology vs selection discipline) needs the disambiguation note above.

## Notes

This regen proceeds against the existing unified structure regardless of the ruling (DD-98: proposal is a side-channel artifact). If Nick rules `proceed`, the per-split DD should also dispose of the harvest-queue rows written this session: the three Model Selection rule rows (`mandatory-explicit-model-per-dispatch`, `no-mid-session-model-switching-subagent-handoff` — both B-cluster sources) would migrate to Destination B's queue.
