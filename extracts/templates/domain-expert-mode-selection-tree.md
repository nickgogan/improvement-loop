---
title: "Domain-Expert Mode-Selection Tree"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "oracle-evaluator-architect-domain-expert-progression"
extraction_date: "2026-07-19"
last_change_session: 152
last_change_report: "agent-design-patterns.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams embedding a subject-matter expert's judgment into an AI product's quality loop and needing to decide how that judgment is captured"
    - "product or engineering leads diagnosing why a hired domain expert isn't producing the expected quality improvement"
    - "teams re-evaluating their current review/improvement setup as usage scale or output variation grows"
  platform_coupling: "agnostic"
  autonomy: "hitl-only"
  stage: "specify"
  reversibility: "trivial — the worksheet is a diagnostic document; filling it out commits to nothing. Acting on its answer (building measurement infrastructure, hiring for a different mode) is a separate, heavier decision with its own reversibility."
  auditability: "high — the two branch questions and the resulting mode are recorded as explicit answers with rationale, so a reviewer can check the diagnosis without re-deriving it"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Framework documented and demonstrated across three named production case studies (a meeting-notes product, a medical scribe product, and a prior-authorization product) by its originator; no adoption in this scaffold's consuming context yet."
contract:
  preconditions: "An AI product or feature exists where a domain expert's judgment (clinical, legal, editorial, or any other trust-bearing call) needs to be captured into a quality loop — assessed and improved over time. Someone can answer, even provisionally, whether the quality dimension in question is objectively measurable."
  invariants: "The two branch questions are asked in order — measurability first, then (only if measurable) whether manual iteration still keeps pace. The mode selected is one of a closed set (Oracle, Decentralized Oracle, Evaluator, Architect); the tree does not skip a mode based on preference or perceived sophistication. A domain expert is named for whichever mode is selected — the tree diagnoses a mode, it does not remove the need for a person."
  governance: "Owner: whoever is accountable for the product's AI-quality decisions (ideally the named principal domain expert, if one exists). Re-run the worksheet when scale, variation, or team size changes materially — the diagnosis is a snapshot, not a permanent classification."
  recovery: "If the selected mode stalls (an Oracle-shaped setup can't keep up, an Evaluator's dashboard isn't closing the loop fast enough) → re-answer the branch questions with current data; the framework treats this as expected progression, not failure. If a hire was made for the wrong mode (e.g., an Oracle-shaped hire dropped into a product that needs an Evaluator) → re-run the tree before changing the hire; the mismatch is usually a mode question, not a competence question. If different parts of the same product diagnose to different modes → complete one worksheet per part rather than forcing a single answer."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-design"
  - "decision-tree"
  - "domain-expertise"
  - "ai-quality"
---

# Domain-Expert Mode-Selection Tree

**Source:** [[oracle-evaluator-architect-domain-expert-progression]]
**Form:** template
**Extraction date:** 2026-07-19

A fillable decision-tree worksheet for diagnosing which of three modes — Oracle, Evaluator, or Architect — a domain expert's judgment should take in a given AI product, and for recording the two testable questions that produce that diagnosis. Complete one worksheet per product, or per feature if different parts of the same product plausibly sit at different modes.

## Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `{{PRODUCT_OR_FEATURE}}` | The product or feature this worksheet diagnoses | Yes |
| `{{DOMAIN_EXPERT}}` | Who currently holds (or would hold) the domain-expert role for this product | Yes |
| `{{QUALITY_MEASURABLE}}` | `yes` or `no` — can output quality here be captured in objective metrics, or is it fundamentally a taste call? | Yes |
| `{{MEASURABILITY_RATIONALE}}` | Why the answer above is true — what would (or wouldn't) count as an objective metric | Yes |
| `{{DECENTRALIZATION_NEEDED}}` | If `{{QUALITY_MEASURABLE}}` is `no`: `yes` or `no` — is one person enough to personally review and improve output at current scale, or does the work need to split across several people each owning a subset? | Conditional |
| `{{MANUAL_ITERATION_FAST_ENOUGH}}` | If `{{QUALITY_MEASURABLE}}` is `yes`: `yes` or `no` — can a domain expert flag issues and an engineer fix them by hand fast enough to keep up with need? | Conditional |
| `{{SELECTED_MODE}}` | The resulting mode: `Oracle`, `Decentralized Oracle`, `Evaluator`, or `Architect` | Yes |
| `{{MEASUREMENT_MECHANISM}}` | For Evaluator/Architect: what captures quality (user signals, hired reviewers, LLM-as-judge, other) | Conditional |
| `{{IMPROVEMENT_MECHANISM}}` | Who or what performs fixes: the domain expert directly (Oracle), engineers driven by the evaluator's findings (Evaluator), or the system itself (Architect) | Yes |
| `{{NEXT_BOTTLENECK}}` | The condition that would force progression to the next mode, per the framework (e.g., "iteration can't keep pace with variation") | Yes |

## Body

```markdown
# Domain-Expert Mode Diagnosis: {{PRODUCT_OR_FEATURE}}

**Domain expert:** {{DOMAIN_EXPERT}}

## Question 1 — Is quality objectively measurable?

{{QUALITY_MEASURABLE}}

**Rationale:** {{MEASURABILITY_RATIONALE}}

*If NO → proceed to Question 1a. If YES → proceed to Question 2.*

## Question 1a — (only if Question 1 = NO) Is one person enough?

{{DECENTRALIZATION_NEEDED}}

*If NO → mode is **Oracle**. If YES → mode is **Decentralized Oracle**.*

## Question 2 — (only if Question 1 = YES) Is manual iteration still fast enough?

{{MANUAL_ITERATION_FAST_ENOUGH}}

*If YES → mode is **Evaluator**. If NO → mode is **Architect**.*

## Diagnosis

**Selected mode:** {{SELECTED_MODE}}
**Measurement mechanism:** {{MEASUREMENT_MECHANISM}}
**Improvement mechanism:** {{IMPROVEMENT_MECHANISM}}
**Next bottleneck (re-run trigger):** {{NEXT_BOTTLENECK}}
```

## Usage

1. **Ask the two questions in order — never skip to a mode.** Measurability comes first; manual-iteration speed only applies once quality is measurable. Skipping straight to "we need an Architect" before quality is even measurable wastes effort on automation with nothing solid to optimize against.
2. **Name a domain expert regardless of mode.** The tree diagnoses which role that person plays — it does not remove the person from the loop, even at Architect.
3. **Treat the diagnosis as a snapshot.** Re-run the worksheet when scale, variation, or team composition changes; progression through the modes is typically necessity-driven, not planned in advance.
4. **One worksheet per part, if parts differ.** A core feature can sit at Architect while a new feature launches at Oracle — do not force a single product-wide answer if the diagnosis genuinely differs by part.
5. **Use the diagnosis to check a hire, not just a system.** An Oracle-shaped hire dropped into a product that needs an Evaluator (or vice versa) is a common failure this worksheet is meant to catch before the hire, not after.

## Variation Axis

What drives different renderings of this scaffold:

- **Measurability granularity.** Some products have partially-measurable quality (some dimensions scorable, others taste); render one worksheet per dimension rather than forcing a single yes/no when this is the case.
- **Scale trajectory.** A young product completes the worksheet once and expects to re-run it as it grows; a mature product at a stable scale may complete it once and treat the mode as settled until a specific trigger event.
- **Regression case.** The framework as documented describes forward progression only; if a product's variation drops (post-consolidation, narrower scope), the worksheet can be re-run and may legitimately produce a lower-complexity mode than the current one — record this as a deliberate re-diagnosis, not an error.

## Contract

### Preconditions
An AI product or feature exists where a domain expert's judgment (clinical, legal, editorial, or any other trust-bearing call) needs to be captured into a quality loop — assessed and improved over time. Someone can answer, even provisionally, whether the quality dimension in question is objectively measurable.

### Invariants
The two branch questions are asked in order — measurability first, then (only if measurable) whether manual iteration still keeps pace. The mode selected is one of a closed set (Oracle, Decentralized Oracle, Evaluator, Architect); the tree does not skip a mode based on preference or perceived sophistication. A domain expert is named for whichever mode is selected — the tree diagnoses a mode, it does not remove the need for a person.

### Governance
Owner: whoever is accountable for the product's AI-quality decisions (ideally the named principal domain expert, if one exists). Re-run the worksheet when scale, variation, or team size changes materially — the diagnosis is a snapshot, not a permanent classification.

### Recovery
If the selected mode stalls (an Oracle-shaped setup can't keep up, an Evaluator's dashboard isn't closing the loop fast enough) → re-answer the branch questions with current data; the framework treats this as expected progression, not failure. If a hire was made for the wrong mode (e.g., an Oracle-shaped hire dropped into a product that needs an Evaluator) → re-run the tree before changing the hire; the mismatch is usually a mode question, not a competence question. If different parts of the same product diagnose to different modes → complete one worksheet per part rather than forcing a single answer.
