<!-- ARCHIVED 2026-07-19: source guide building-agent-evaluation-suites deprecated on the G4->G4a/G4b split (session 152, DD-123). These 15 rows were transferred to the per-destination harvest queues extracts/guides/verifying-agent-output.harvest-queue.md (A) and extracts/guides/eval-driven-improvement-loops.harvest-queue.md (B). The live rows are those per-destination files; this archived file is read-only history. The May-2026 fully-extracted snapshot from sessions 102-103 is retained below the separator. -->

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
| 2026-07-19 | queued | rule | [[pre-code-validation-contracts-dual-blind-validators]] | "validation-contract-before-code" | extract via /extract-artifacts |
| 2026-07-19 | queued | rule | [[garbage-collection-day-persona-review-agents]] | "convert-review-feedback-to-durable-checks" | extract via /extract-artifacts |

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

### pre-code-validation-contracts-dual-blind-validators::rule::validation-contract-before-code

- **Date queued:** 2026-07-19
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[pre-code-validation-contracts-dual-blind-validators]]
- **Source excerpt:**
  > "a validation contract, written by the orchestrator during planning before any code exists, defines correctness independently of any implementation... Targets a named failure mode directly: 'tests written after implementation don't catch bugs, they confirm decisions.'"
- **Codifier's reading:** A machine-checkable imperative on assertion provenance — author the validation contract before implementation, so tests can't be shaped by the code — rule form per the form rubric. Strong (production-tested) evidence. The finding's implementation_notes propose /identify-artifacts carry a lightweight validation-contract field for /extract-artifacts to draft against; the rule is the general directive under that design.
- **Suggested headline:** validation-contract-before-code
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


---

# Prior archived snapshot (May 2026, sessions 102-103)

The four rows below were extracted/merged in May 2026 (a separate resolved-queue snapshot that predates the July intake above). Retained for audit continuity.

# Co-occurrence Harvest Queue — Building Agent Evaluation Suites

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-05-25 | extracted | rule | [[goal-backward-verification]] | "Never trust agent summaries for verification; verify against actual state" | merged into [[agent-self-reporting-unreliability-independent-eval]] |
| 2026-05-25 | extracted | template | [[tdd-step-ordering-in-plan-tasks]] | "TDD step ordering template for plan task checkboxes" | extracted to [[tdd-step-ordering-in-plan-tasks]] |
| 2026-05-25 | extracted | rule | [[holdout-validation-pattern-blind-regression]] | "Never reveal implementation scope to validation agent" | extracted to [[holdout-validation-pattern-blind-regression]] |
| 2026-05-25 | extracted | rule | [[production-database-wipeout-agent-context]] | "Agents must have explicit production vs non-production environment markers" | extracted to [[production-database-wipeout-agent-context]] |

## Per-row details

### goal-backward-verification::rule::never-trust-agent-summaries

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[goal-backward-verification]]
- **Source excerpt:**
  > "Do NOT trust SUMMARY.md claims. Verify what ACTUALLY exists in the code. Task completion != goal achievement. The verifier starts from the desired outcome and works backwards to check what actually exists."
- **Codifier's reading:** Imperative directive embedded within the goal-backward verification pattern: "never trust agent-generated summaries or completion claims; verify against actual codebase state." Machine-enforceable: a verification step that reads declared goals and checks filesystem state independently of any agent-produced summary. The rule stands independently of the backward-verification procedure — it's a trust invariant applicable to any verification architecture.
- **Suggested headline:** never-trust-agent-summaries
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[agent-self-reporting-unreliability-independent-eval]]

Pending merge 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-05-25-extension-proposals]]; primary match [[agent-self-reporting-unreliability-independent-eval]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to extracted and Resolution to merged into [[agent-self-reporting-unreliability-independent-eval]] via manual queue edit (or future skill mode).

Merged 2026-05-25 — Session 103 — [[session-103-codifier-complete-extract-artifacts-write-phase]] — into [[agent-self-reporting-unreliability-independent-eval]].

### tdd-step-ordering-in-plan-tasks::template::tdd-plan-task-checkboxes

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[tdd-step-ordering-in-plan-tasks]]
- **Source excerpt:**
  > "Each task in the implementation plan contains a fixed sequence: (1) Write test file, (2) Run test to verify it fails, (3) Implement code, (4) Run test to verify it passes, (5) Commit. The plan document is the enforcement mechanism for TDD, not the agent's prompt."
- **Codifier's reading:** Structural scaffold for plan task documents: a 5-step checkboxed template (write test → verify red → implement → verify green → commit) that embeds TDD discipline in the artifact format rather than in agent instructions. Fill-in with {{TASK_NAME}}, {{TEST_FILE}}, {{IMPLEMENTATION_FILE}}. The template is distinct from the pattern (which argues WHY plan-level enforcement works) — the template is the concrete checkbox structure.
- **Suggested headline:** tdd-plan-task-checkboxes
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[tdd-step-ordering-in-plan-tasks]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[tdd-step-ordering-in-plan-tasks]].

### holdout-validation-pattern-blind-regression::rule::never-reveal-scope-to-validator

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[holdout-validation-pattern-blind-regression]]
- **Source excerpt:**
  > "The validation agent is never told what was just implemented, what issue was being addressed, or what the PR contains. Holdout constraint breaks if the validator can read git history, PR descriptions, or branch names — the fresh session must explicitly not have access to these."
- **Codifier's reading:** Hard constraint on validation agent context: "never reveal implementation scope, git history, PR descriptions, or branch names to the validation agent." Machine-enforceable: the validation workflow configuration must exclude these context sources. The rule is independently actionable — any verification architecture can adopt this constraint regardless of whether it uses the full holdout pattern.
- **Suggested headline:** never-reveal-scope-to-validator
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[holdout-validation-pattern-blind-regression]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[holdout-validation-pattern-blind-regression]].

### production-database-wipeout-agent-context::rule::explicit-production-environment-markers

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[production-database-wipeout-agent-context]]
- **Source excerpt:**
  > "A real incident where an AI coding agent destroyed 1.9M rows of production student data because it had no knowledge of which infrastructure was production vs. temporary — knowledge that existed in the team's heads but was never made explicit in context available to the agent."
- **Codifier's reading:** Imperative directive derived from incident: "agents must have explicit, machine-readable production/non-production environment markers before operating on any data infrastructure." Machine-enforceable: a pre-flight check that verifies the agent's context contains environment classification for all data stores it can access. The rule stands independently of the evaluation guide — it's a safety invariant for any agent with write access to external systems.
- **Suggested headline:** explicit-production-environment-markers
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[production-database-wipeout-agent-context]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[production-database-wipeout-agent-context]].
