# Co-occurrence Harvest Queue — Eval-Driven Improvement Loops

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

Rows transferred from the deprecated source guide `building-agent-evaluation-suites` on the G4→G4a/G4b split (session 152, DD-123); each row routed here because its source finding lands in destination B (G4b). The shared finding `eval-rubric-carve-outs-subjective-and-script-core-skills` appears in both destinations' queues (it is shared substrate).

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | queued | skill | [[skill-description-optimization-loop-held-out-test]] | "skill-description-optimization-loop" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[skill-testing-three-tier-trigger-functional-perf]] | "three-tier-skill-test-plan" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[skill-smells-triage-layer-before-full-audit]] | "skill-smells-triage-table" | extract via /extract-artifacts |
| 2026-07-16 | queued | skill | [[with-without-skill-ab-baseline-measurement]] | "with-without-skill-ab-baseline" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[convergence-loop-optimizer-family-contract]] | "convergence-and-severity-contract" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[skill-popularity-vs-measured-efficacy]] | "no-adoption-without-eval-evidence" | extract via /extract-artifacts |
| 2026-07-19 | queued | rule | [[garbage-collection-day-persona-review-agents]] | "convert-review-feedback-to-durable-checks" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[eval-rubric-carve-outs-subjective-and-script-core-skills]] | "class-aware-eval-rubric-carve-outs" | extract via /extract-artifacts |

## Per-row details

### skill-description-optimization-loop-held-out-test::skill::skill-description-optimization-loop

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[skill-description-optimization-loop-held-out-test]]
- **Source excerpt:**
  > "1. Generate eval queries. 20 total: 8-10 should-trigger, 8-10 should-not-trigger... 3. Split 60/40. Train = 60%, held-out test = 40%. 4. Evaluate current description. Run each train query 3 times... 7. Iterate. Up to 5 iterations. 8. Select best by TEST score — not train score... Implementation: `python -m scripts.run_loop --eval-set <path> --skill-path <path> --model <id> --max-iterations 5`."
- **Codifier's reading:** A complete numbered procedure with defined input (eval set + skill path), invocation contract (the run_loop CLI), step-by-step structure, and termination condition (5 iterations, test-score selection) — skill shape per the form rubric.
- **Suggested headline:** skill-description-optimization-loop
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### skill-testing-three-tier-trigger-functional-perf::template::three-tier-skill-test-plan

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[skill-testing-three-tier-trigger-functional-perf]]
- **Source excerpt:**
  > "Tier 1: Triggering Tests... ✅ Triggers on obvious tasks / ✅ Triggers on paraphrased requests / ❌ Doesn't trigger on unrelated topics... Tier 2: Functional Tests... 'Test: Create project with 5 tasks. Given: ... When: ... Then: ...' Tier 3: Performance Comparison... Baseline (without skill) vs. with-skill comparison."
- **Codifier's reading:** The three-tier structure with named test-case shapes, given/when/then scaffolds, and a baseline-comparison format is a structural scaffold meant for rendering per skill — template form. (The guide's Skill Test Plan template embeds a merged variant; the standalone scaffold is the residual candidate.)
- **Suggested headline:** three-tier-skill-test-plan
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### skill-smells-triage-layer-before-full-audit::template::skill-smells-triage-table

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[skill-smells-triage-layer-before-full-audit]]
- **Source excerpt:**
  > "Each row is *what you notice* → *likely cause* → *go to* (the reference section that diagnoses it in depth). Five smell categories... The quantified verdict rule does the routing: 0 smells → run the deterministic validator and proceed; 1–2 smells in one category → patch that smell...; 3+ smells across categories → ... run the full scored audit...; any Category E smell → block."
- **Codifier's reading:** A fixed table shape (symptom → cause → pointer) with five named categories and a quantified verdict rule is a fillable structural scaffold for any assessor roster — template form. Finding is P1 (Direct Adoption); its implementation_notes name a smells pre-pass for /assess-skill.
- **Suggested headline:** skill-smells-triage-table
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### with-without-skill-ab-baseline-measurement::skill::with-without-skill-ab-baseline

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[with-without-skill-ab-baseline-measurement]]
- **Source excerpt:**
  > "launches a separate background Claude session (headless, no permission stops, reports output back) that executes the target task **twice — once with the skill and once without it**. The comparison isolates the skill's marginal impact... logged as structured lessons in a `learning.md` file living inside the skill."
- **Codifier's reading:** Defined input (skill + task corpus), procedure (fresh headless sessions, paired runs, diff), and output (marginal-impact delta + lessons log) — skill shape. Rule 10 note in the finding: the skill's author must not be its scorer.
- **Suggested headline:** with-without-skill-ab-baseline
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### convergence-loop-optimizer-family-contract::template::convergence-and-severity-contract

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[convergence-loop-optimizer-family-contract]]
- **Source excerpt:**
  > "A single quality-engine contract (defined once, in `convergence-and-severity.md`) that six different artifact optimizers implement: 1. Multi-pass audit... 2. Severity rating — every finding is rated `Blocker > High > Medium > Low > Nit`. 3. Fix in place... 4. Verify gate... 5. Convergence loop — re-audit and repeat until no Medium-or-higher finding remains."
- **Codifier's reading:** A shared contract document with a five-part fixed structure and a per-member verify-gate column is a structural scaffold stamped out per artifact type — template form. Implementation_notes call the per-artifact verify-gate column "a ready-made template."
- **Suggested headline:** convergence-and-severity-contract
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### skill-popularity-vs-measured-efficacy::rule::no-adoption-without-eval-evidence

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[skill-popularity-vs-measured-efficacy]]
- **Source excerpt:**
  > "do not install any skill from the internet that claims to make your agent perform better but has published no rigorous evaluation of the claim... 'Their GitHub stars only tell you how popular they are, not whether they are actually helpful.'"
- **Codifier's reading:** A clean adoption imperative with a decidable check (published eval evidence OR local with/without baseline before install) — rule form. Implementation_notes name it a criteria-delta candidate for /assess-skill third-party intake and watched-libraries triage.
- **Suggested headline:** no-adoption-without-eval-evidence
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### garbage-collection-day-persona-review-agents::rule::convert-review-feedback-to-durable-checks

- **Date queued:** 2026-07-19
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[garbage-collection-day-persona-review-agents]]
- **Source excerpt:**
  > "take every piece of 'slop' observed that week in PR review and durably eliminate the underlying cause — not with more review comments, but with documentation, tests, or lints that make the failure structurally impossible to repeat."
- **Codifier's reading:** An imperative, decidable directive — every recurring review-feedback item is converted into a durable check (test/lint/doc) on a protected cadence rather than re-given — rule form. NOTE: the finding's *persona review agent* facet (one agent per reviewer persona) is agent-shaped and is SUPPRESSED from this queue per DD-82 (logged inline in the run report, never queued). Only the durable-conversion rule is queued. Overlaps the engine's own /self-improve capture-and-promote loop (implementation_notes); Nick may prefer to merge rather than extract standalone.
- **Suggested headline:** convert-review-feedback-to-durable-checks
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### eval-rubric-carve-outs-subjective-and-script-core-skills::rule::class-aware-eval-rubric-carve-outs

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[eval-rubric-carve-outs-subjective-and-script-core-skills]]
- **Source excerpt:**
  > "Subjective-skill carve-out. Skills whose primary output is inherently judgment-based ... must NOT be scored down for lacking a functional assertion suite... Script-core carve-out. Skills whose core is a deterministic program ... get their functional guarantee from the script's own tests... description/trigger optimization is objective and required of *every* skill regardless of output type."
- **Codifier's reading:** Imperative, machine-checkable directives ("must not be scored down", "required of every skill") that re-anchor an audit dimension — rule form. Directly patches a known /assess-skill misdiagnosis shape; finding is P1 (Direct Adoption). Shared finding — same row also appears in the G4a (verifying-agent-output) harvest queue.
- **Suggested headline:** class-aware-eval-rubric-carve-outs
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**
