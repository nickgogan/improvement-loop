---
type: "split-proposal"
target_system:
  - "improvement-loop"
generated_by: "/synthesize-guide"
date: "2026-05-25"
source_guide: "agent-governance-and-trust"
finding_count: 38
practitioner_question_count: 4
session: 98
sl: "session-98-codifier-g9-re-synthesis"
---

# Split Proposal — Agent Governance and Trust

## Source guide identity

- **Guide stem:** `agent-governance-and-trust`
- **Current title:** "Agent Governance and Trust"
- **Finding count:** 38 (post-resolution; >=25)
- **Routing-table row:** [link to row in `operations/references/guide-routing-table.md`]

## Practitioner-question analysis

The source cluster covers 4 distinct practitioner questions:

1. **Q1:** "How do I make governance machine-readable and enforceable at runtime?"
   - Findings clustering against Q1: [[governance-ontology-semantic-foundation]], [[governed-dependency-chain-build-order]], [[policy-as-data-machine-readable-constraints]], [[policy-as-data-runtime-governance-pattern]], [[runtime-governance-gap-buildtime-to-production]], [[runtime-threshold-management-truth-conditions]]

2. **Q2:** "How do I manage permissions across agent delegation chains?"
   - Findings clustering against Q2: [[permission-compounding-across-agent-delegation-chains]], [[cross-system-permission-composition-audit-gap]], [[capability-restricted-agent-spawning-via-allowlist]], [[foreground-vs-background-subagent-permission-models]], [[subagent-scope-priority-ladder]], [[tool-access-as-security-boundary-not-feature-toggle]]

3. **Q3:** "How do I trace and audit agent decisions?"
   - Findings clustering against Q3: [[actor-passport-schema-bound-identity]], [[passport-object-decision-governance-binding]], [[context-warrant-justified-data-package]], [[tool-model-io-contracts-with-preconditions]]

4. **Q4:** "How do I govern agent autonomy with human oversight at scale?"
   - Findings clustering against Q4: [[review-bandwidth-as-organizational-bottleneck]], [[review-obsolescence-as-design-goal]], [[behavioral-context-portability-intelligence-lock-in]], [[governance-memory-append-only-audit-layer]], [[compound-review-debt-from-deferred-inspection]], [[reviewer-skill-elevation-for-agentic-output]], [[tool-gateway-security-boundary]], [[human-on-the-loop-hotl-autonomy-tiering-framework]], [[trust-calibration-progressive-autonomy-ramp]], [[agent-identity-governance-enforcement-layer]], [[dark-code-organizational-capability-problem]], [[distributed-boundary-guides]], [[middleware-as-enforcement-architecture]], [[per-node-tool-restrictions-workflow-governance]], [[specification-as-governance-fourth-enforcement-philosophy]], [[three-enforcement-pipeline-architectures]], [[supervision-debt-anti-pattern]], [[pattern-scale-signals-systemic-not-individual-failure]], [[management-unbundling-routing-sensemaking-accountability]], [[dri-rotation-pattern-time-bounded-sensemaking-ownership]], [[interpretive-boundary-layer-fact-vs-judgment]], [[agent-action-reversibility-as-design-requirement]]

## Proposed bifurcation

Destination guide names (working draft; per-split DD codifies finals):

- **Destination A:** `runtime-governance-machine-readable-policy` — practitioner question: "How do I make governance machine-readable and enforceable at runtime?"
- **Destination B:** `agent-permission-delegation-chains` — practitioner question: "How do I manage permissions across agent delegation chains?"
- **Destination C:** `agent-decision-tracing-auditability` — practitioner question: "How do I trace and audit agent decisions?"
- **Destination D (current guide, narrowed):** `agent-governance-and-trust` — practitioner question: "How do I govern agent autonomy with human oversight at scale?"

Per-finding routing (every finding routed; no implicit handling per DD-98 Rules #4):

| Finding | Disposition |
|---------|-------------|
| [[governance-ontology-semantic-foundation]] | A |
| [[governed-dependency-chain-build-order]] | A |
| [[policy-as-data-machine-readable-constraints]] | A |
| [[policy-as-data-runtime-governance-pattern]] | A |
| [[runtime-governance-gap-buildtime-to-production]] | A |
| [[runtime-threshold-management-truth-conditions]] | A |
| [[permission-compounding-across-agent-delegation-chains]] | B |
| [[cross-system-permission-composition-audit-gap]] | B |
| [[capability-restricted-agent-spawning-via-allowlist]] | B |
| [[foreground-vs-background-subagent-permission-models]] | B |
| [[subagent-scope-priority-ladder]] | B |
| [[tool-access-as-security-boundary-not-feature-toggle]] | B |
| [[actor-passport-schema-bound-identity]] | C |
| [[passport-object-decision-governance-binding]] | C |
| [[context-warrant-justified-data-package]] | C |
| [[tool-model-io-contracts-with-preconditions]] | C |
| [[review-bandwidth-as-organizational-bottleneck]] | D |
| [[review-obsolescence-as-design-goal]] | D |
| [[behavioral-context-portability-intelligence-lock-in]] | D |
| [[governance-memory-append-only-audit-layer]] | shared (D + C) |
| [[compound-review-debt-from-deferred-inspection]] | D |
| [[reviewer-skill-elevation-for-agentic-output]] | D |
| [[tool-gateway-security-boundary]] | shared (B + D) |
| [[human-on-the-loop-hotl-autonomy-tiering-framework]] | D |
| [[trust-calibration-progressive-autonomy-ramp]] | D |
| [[agent-identity-governance-enforcement-layer]] | shared (B + C) |
| [[dark-code-organizational-capability-problem]] | D |
| [[distributed-boundary-guides]] | D |
| [[middleware-as-enforcement-architecture]] | shared (A + D) |
| [[per-node-tool-restrictions-workflow-governance]] | shared (B + D) |
| [[specification-as-governance-fourth-enforcement-philosophy]] | shared (A + D) |
| [[three-enforcement-pipeline-architectures]] | shared (A + D) |
| [[supervision-debt-anti-pattern]] | D |
| [[pattern-scale-signals-systemic-not-individual-failure]] | D |
| [[management-unbundling-routing-sensemaking-accountability]] | D |
| [[dri-rotation-pattern-time-bounded-sensemaking-ownership]] | D |
| [[interpretive-boundary-layer-fact-vs-judgment]] | D |
| [[agent-action-reversibility-as-design-requirement]] | D |

## Preserved-section disposition (DD-93)

Source guide has no preserved sections per DD-93 capture. No `## Nick's Annotations` section and no `<!-- PRESERVE -->` markers are present in the current guide.

## Routing-table impact

- **Source guide:** proposed narrowing to Q4 scope (`stage: draft`, narrower title possible: "Agent Autonomy and Human Oversight").
- **New rows:**
  - `runtime-governance-machine-readable-policy` — Q1, dimensions: Governance, lifecycle stage = `draft`.
  - `agent-permission-delegation-chains` — Q2, dimensions: Governance, lifecycle stage = `draft`.
  - `agent-decision-tracing-auditability` — Q3, dimensions: Governance, lifecycle stage = `draft`.
- **Dimension -> Guide mapping changes:** Governance dimension currently routes to G9 only; would add three new guide rows for A, B, C.

## Codifier recommendation

**Recommendation:** defer pending more findings

**Rationale:** While the four practitioner questions are clearly distinct, 7 of 38 findings (18%) route as `shared` across multiple destinations, indicating meaningful conceptual overlap between clusters. The current 38-finding guide remains coherent because Clusters A, B, and C are all downstream of the trust/autonomy framework in Cluster D — they are enforcement mechanisms for the governance decisions made in D. Splitting now would require extensive cross-referencing between four guides. Additionally, Clusters A and C (6 and 4 findings respectively) are below the mass that justifies standalone guides. Recommend monitoring: if next intake pushes any cluster past 10 findings independently, revisit with a 2-way split (D remains; A+B+C form a "Runtime Governance Enforcement" companion guide) rather than the 4-way split.

## Notes

- The governed-dependency-chain-build-order finding is an umbrella pattern that touches all four questions; routed to A because its primary actionable content is the build-order procedure itself.
- Cluster D at 22 findings is itself large and could be further split (autonomy tiers vs. review scaling vs. enforcement architecture), but those are sub-sections of the same practitioner question, not separate questions.
- If a 2-way split is preferred in future, the natural seam is: "how to decide what governance to apply" (D, the decision layer) vs. "how to enforce governance at runtime" (A+B+C merged, the enforcement layer).

## Resolution

**Decision:** deferred — session 104 (2026-05-25)
**Rationale:** At 38 findings, below DD-102 threshold (45). Codifier recommended deferral citing 18% shared routing, thin clusters (A=6, C=4 findings), and conceptual entanglement between enforcement mechanisms and the trust/autonomy framework they serve. Nick concurred. Re-evaluate if finding count crosses 45 or any enforcement cluster independently reaches 10 findings.
