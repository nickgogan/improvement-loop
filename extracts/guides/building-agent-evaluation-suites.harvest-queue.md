# Co-occurrence Harvest Queue — Building Agent Evaluation Suites

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | queued | skill | [[skill-description-optimization-loop-held-out-test]] | "skill-description-optimization-loop" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[skill-testing-three-tier-trigger-functional-perf]] | "three-tier-skill-test-plan" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[skill-smells-triage-layer-before-full-audit]] | "skill-smells-triage-table" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[eval-rubric-carve-outs-subjective-and-script-core-skills]] | "class-aware-eval-rubric-carve-outs" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[enumerate-dont-fix-hostile-reviewer-prompt]] | "enumerate-dont-fix-verifier-contract-line" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[deterministic-store-checker-runtime-threshold-flags]] | "runtime-computed-counts-never-stored" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[five-point-agent-health-checklist]] | "five-question-agent-health-review" | extract via /extract-artifacts |
| 2026-07-16 | queued | skill | [[with-without-skill-ab-baseline-measurement]] | "with-without-skill-ab-baseline" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[convergence-loop-optimizer-family-contract]] | "convergence-and-severity-contract" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[task-risk-gradient-for-verification-depth]] | "task-risk-gradient-rubric" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[harness-cost-readout-unreliability-independent-log-accounting]] | "log-based-cost-accounting-over-harness-readouts" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[skill-popularity-vs-measured-efficacy]] | "no-adoption-without-eval-evidence" | extract via /extract-artifacts |
| 2026-07-16 | queued | skill | [[no-mistakes-post-implementation-validation-pipeline]] | "post-implementation-validation-pipeline" | extract via /extract-artifacts |

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
- **Codifier's reading:** The three-tier structure with named test-case shapes, given/when/then scaffolds, and a baseline-comparison format is a structural scaffold meant for rendering per skill — template form. (The guide's new Skill Test Plan template embeds a merged variant; the standalone scaffold is the residual candidate.)
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

### eval-rubric-carve-outs-subjective-and-script-core-skills::rule::class-aware-eval-rubric-carve-outs

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[eval-rubric-carve-outs-subjective-and-script-core-skills]]
- **Source excerpt:**
  > "Subjective-skill carve-out. Skills whose primary output is inherently judgment-based ... must NOT be scored down for lacking a functional assertion suite... Script-core carve-out. Skills whose core is a deterministic program ... get their functional guarantee from the script's own tests... description/trigger optimization is objective and required of *every* skill regardless of output type."
- **Codifier's reading:** Imperative, machine-checkable directives ("must not be scored down", "required of every skill") that re-anchor an audit dimension — rule form. Directly patches a known /assess-skill misdiagnosis shape; finding is P1 (Direct Adoption).
- **Suggested headline:** class-aware-eval-rubric-carve-outs
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### enumerate-dont-fix-hostile-reviewer-prompt::rule::enumerate-dont-fix-verifier-contract-line

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[enumerate-dont-fix-hostile-reviewer-prompt]]
- **Source excerpt:**
  > "the reviewer's only permitted output is a written enumeration of issues. 'That last instruction — don't fix, just enumerate — is what makes it work. The model is just trying to find the problems, not solve them.'"
- **Codifier's reading:** A single enforceable contract line for every verifier prompt ("don't fix anything, just enumerate") plus a five-category enumeration checklist — imperative directive, rule form. The finding's implementation_notes flag it as a prompt-craft delta for /assess-* and verifier subagents.
- **Suggested headline:** enumerate-dont-fix-verifier-contract-line
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### deterministic-store-checker-runtime-threshold-flags::rule::runtime-computed-counts-never-stored

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[deterministic-store-checker-runtime-threshold-flags]]
- **Source excerpt:**
  > "Counts are runtime-only. The readiness count is computed per run and reported in the flag output; the store files never carry counters... 'reports them separately at runtime — never store counts in this file.' Exit codes: `0` = schema valid..., `1` = violations, `2` = store not initialized."
- **Codifier's reading:** Machine-enforceable imperatives (never store counts; regex-validate every entry; distinct exit codes) — rule form. This is Nick's standing no-hardcoded-counts rule made executable; the engine's pre-commit hook is the same species.
- **Suggested headline:** runtime-computed-counts-never-stored
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### five-point-agent-health-checklist::template::five-question-agent-health-review

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[five-point-agent-health-checklist]]
- **Source excerpt:**
  > "1. What's it eating? Are the sources current?... 2. Test its reach. What can it touch...? 3. Check its job. ... 'Do not let the job change silently.' 4. Check the proof. ... a linkable trail a human can inspect, not the agent saying so. 5. Check the value. Does anyone read the output?"
- **Codifier's reading:** A fixed five-question review instrument with per-question triggers (time cadence vs. model upgrade) is a fillable checklist scaffold — template form. Implementation_notes flag it as a future ENHANCE delta for /system-health.
- **Suggested headline:** five-question-agent-health-review
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

### task-risk-gradient-for-verification-depth::template::task-risk-gradient-rubric

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[task-risk-gradient-for-verification-depth]]
- **Source excerpt:**
  > "low risk (formatting, layout exploration, chart drafts, summary wording, consistency checks — wrongness is cheap and visible), medium risk (source attribution, data extraction — wrongness propagates but is traceable), high risk (numerical synthesis, financial calculations, regulatory/compliance language, claims that travel to leadership)."
- **Codifier's reading:** A three-tier classification rubric meant to be re-instantiated per domain (the finding's improvements section names per-domain gradients) — template form. Implementation_notes flag it as an /assess-* calibration input composing with DD-108.
- **Suggested headline:** task-risk-gradient-rubric
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### harness-cost-readout-unreliability-independent-log-accounting::rule::log-based-cost-accounting-over-harness-readouts

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[harness-cost-readout-unreliability-independent-log-accounting]]
- **Source excerpt:**
  > "Any cost claim should come from independent log-based accounting (e.g. `npx ccusage@latest session` for Claude Code, or pure API metering via a gateway), not from the harness's own display... treat divergence between the two surfaces as the signal to distrust both."
- **Codifier's reading:** An imperative, checkable directive on measurement provenance (log-derived numbers only; harness readouts marked suspect) — rule form. Directly applicable to the engine's session telemetry per the finding's implementation_notes.
- **Suggested headline:** log-based-cost-accounting-over-harness-readouts
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

### no-mistakes-post-implementation-validation-pipeline::skill::post-implementation-validation-pipeline

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[no-mistakes-post-implementation-validation-pipeline]]
- **Source excerpt:**
  > "Stages, in order: 1. Worktree isolation... 2. Intent extraction — the pipeline analyzes the agent session that produced the change to recover the real intent... 4. Adversarial fresh-context review... 5. End-to-end test against intent, with evidence... 6. Documentation pass, lint, PR, babysitting... also invocable as a skill so any implementing agent can hand itself off to validation."
- **Codifier's reading:** A fixed six-stage orchestrated procedure with defined input (a first-pass change), output (a clean PR with evidence + risk assessment), and explicit invocation contract ("invocable as a skill") — skill shape. Two stages the engine lacks entirely per implementation_notes: intent extraction and evidence artifacts.
- **Suggested headline:** post-implementation-validation-pipeline
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**
