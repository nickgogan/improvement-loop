# Co-occurrence Harvest Queue — Verifying Agent Output

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

Rows transferred from the deprecated source guide `building-agent-evaluation-suites` on the G4→G4a/G4b split (session 152, DD-123); each row routed here because its source finding lands in destination A (G4a). The shared finding `eval-rubric-carve-outs-subjective-and-script-core-skills` appears in both destinations' queues (it is shared substrate).

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | queued | rule | [[enumerate-dont-fix-hostile-reviewer-prompt]] | "enumerate-dont-fix-verifier-contract-line" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[deterministic-store-checker-runtime-threshold-flags]] | "runtime-computed-counts-never-stored" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[five-point-agent-health-checklist]] | "five-question-agent-health-review" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[task-risk-gradient-for-verification-depth]] | "task-risk-gradient-rubric" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[harness-cost-readout-unreliability-independent-log-accounting]] | "log-based-cost-accounting-over-harness-readouts" | extract via /extract-artifacts |
| 2026-07-16 | queued | skill | [[no-mistakes-post-implementation-validation-pipeline]] | "post-implementation-validation-pipeline" | extract via /extract-artifacts |
| 2026-07-19 | queued | rule | [[pre-code-validation-contracts-dual-blind-validators]] | "validation-contract-before-code" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[eval-rubric-carve-outs-subjective-and-script-core-skills]] | "class-aware-eval-rubric-carve-outs" | extract via /extract-artifacts |

## Per-row details

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

### eval-rubric-carve-outs-subjective-and-script-core-skills::rule::class-aware-eval-rubric-carve-outs

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[eval-rubric-carve-outs-subjective-and-script-core-skills]]
- **Source excerpt:**
  > "Subjective-skill carve-out. Skills whose primary output is inherently judgment-based ... must NOT be scored down for lacking a functional assertion suite... Script-core carve-out. Skills whose core is a deterministic program ... get their functional guarantee from the script's own tests... description/trigger optimization is objective and required of *every* skill regardless of output type."
- **Codifier's reading:** Imperative, machine-checkable directives ("must not be scored down", "required of every skill") that re-anchor an audit dimension — rule form. Directly patches a known /assess-skill misdiagnosis shape; finding is P1 (Direct Adoption). Shared finding — same row also appears in the G4b (eval-driven-improvement-loops) harvest queue.
- **Suggested headline:** class-aware-eval-rubric-carve-outs
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**
