# Co-occurrence Harvest Queue — Agent Workflow and Execution

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | queued | rule | [[headless-cron-composition-autonomous-scheduled-workflows]] | "headless-output-verifiability-gate" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[dark-factory-ai-only-codebase-management]] | "deterministic-nodes-for-non-reasoning-steps" | extract via /extract-artifacts |
| 2026-07-16 | queued | skill | [[ecosystem-monitoring-meta-loop]] | "write-run-log-shared-utility-skill" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[self-improvement-dispatch-table-route-never-reimplement]] | "dispatch-table-schema-template" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[scheduled-skill-chaining-with-file-based-activation]] | "scheduled-job-config-schema-template" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[github-label-as-workflow-state]] | "workflow-state-label-schema-template" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[concept-family-explorer-five-neighborhood-gap-mapping]] | "five-neighborhood-coverage-checklist" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[sprint-contract-negotiation-pattern]] | "sprint-contract-template" | extract via /extract-artifacts |
| 2026-07-19 | queued | template | [[loop-contract-anatomy-and-evolve-session-cadence]] | "loop-contract-file-schema (contract/state/log)" | extract via /extract-artifacts |
| 2026-07-19 | queued | rule | [[loop-trigger-taxonomy-poll-then-wake-combo]] | "combo-trigger: cheap pre-check before LLM wake" | extract via /extract-artifacts |
| 2026-07-19 | queued | rule | [[lint-test-failures-as-remediation-prompts]] | "author lint/test failures as remediation prompts" | extract via /extract-artifacts |

## Per-row details

### headless-cron-composition-autonomous-scheduled-workflows::rule::headless-output-verifiability-gate

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[headless-cron-composition-autonomous-scheduled-workflows]]
- **Source excerpt:**
  > "The decision criterion for going headless is **output verifiability**: only use headless mode for tasks where the output is easy to verify after the fact. Hard-to-undo operations should not run headless."
- **Codifier's reading:** Imperative, machine-enforceable directive ("only use headless mode when...; hard-to-undo operations should not run headless") — a binary gate checkable at workflow-definition time. Fits the rule form: never/only phrasing, enforceable at review of any scheduled-job config.
- **Suggested headline:** headless-output-verifiability-gate
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### dark-factory-ai-only-codebase-management::rule::deterministic-nodes-for-non-reasoning-steps

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[dark-factory-ai-only-codebase-management]]
- **Source excerpt:**
  > "**Deterministic vs agentic nodes:** steps that don't need reasoning (formatting, lint, triggering deploys) should be plain code, not LLM calls — reliability by subtraction."
- **Codifier's reading:** Imperative directive with a clear enforcement test (audit every workflow node: does this step need reasoning? if not, no LLM call). Machine-checkable against a workflow DAG definition. Fits the rule form.
- **Suggested headline:** deterministic-nodes-for-non-reasoning-steps
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### ecosystem-monitoring-meta-loop::skill::write-run-log-shared-utility-skill

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[ecosystem-monitoring-meta-loop]]
- **Source excerpt:**
  > "**Health check via a shared run-log skill.** A `write-run-log` utility skill writes every loop's results to one folder. Updating that one skill updates logging across every loop. Cross-referencing the logs shows what is and isn't running successfully — the practitioner's claim is that most loop operators are silently burning tokens on broken or useless loops, and this makes them visible enough to turn off."
- **Codifier's reading:** A named procedure with a clear input/output contract (loop result in, standardized log row out to one folder) and an invocation contract (called by every loop at run end). Fits the skill form; directly serves the engine's own loop portfolio gap noted in the finding's implementation_notes.
- **Suggested headline:** write-run-log-shared-utility-skill
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### self-improvement-dispatch-table-route-never-reimplement::template::dispatch-table-schema-template

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[self-improvement-dispatch-table-route-never-reimplement]]
- **Source excerpt:**
  > "A reference table in the skill package with one row per finding class. Each row carries three things: **signals** (how to recognize the class), **route** (which skill owns the work), and — the subtle part — **what this skill still does** (its residual duty even when routing)."
- **Codifier's reading:** A structural scaffold meant for rendering — a fixed three-column row schema (signals / route / residual duty) fillable per work class by any intake surface. Fits the template form: placeholder fields, structural form, reusable across dispatchers.
- **Suggested headline:** dispatch-table-schema-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### scheduled-skill-chaining-with-file-based-activation::template::scheduled-job-config-schema-template

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[scheduled-skill-chaining-with-file-based-activation]]
- **Source excerpt:**
  > "The file-based activation pattern would benefit from a standard schema: job name, schedule (cron expression), skill chain (ordered list), activation flag, last-run timestamp, last-run status. This enables the scheduled task dashboard pattern to visualize all jobs."
- **Codifier's reading:** An explicit field-list schema for a config artifact — structural form with named fillable fields. The guide's new Scheduled Workflow Definition template is derived from it; a standalone template artifact would make it reusable outside the guide. Fits the template form.
- **Suggested headline:** scheduled-job-config-schema-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### github-label-as-workflow-state::template::workflow-state-label-schema-template

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[github-label-as-workflow-state]]
- **Source excerpt:**
  > "| `factory-accepted` | Triage workflow classified as in-scope |
  > | `in-progress` | Implementation workflow is currently running |
  > | `needs-fixed` | Implementation failed; awaiting retry or human |
  > | `needs-human` | Failed 2+ times or classifier flagged as ambiguous; requires human review |
  > | `factory-rate-limit` | Daily token/API spend limit reached; pause until next day |"
- **Codifier's reading:** A complete, production-validated label-set scaffold (state name → meaning → orchestrator dispatch rule) directly reusable by any pipeline whose work items live in an issue tracker. Structural form meant for rendering/adaptation. Fits the template form.
- **Suggested headline:** workflow-state-label-schema-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### concept-family-explorer-five-neighborhood-gap-mapping::template::five-neighborhood-coverage-checklist

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[concept-family-explorer-five-neighborhood-gap-mapping]]
- **Source excerpt:**
  > "| **Parent** | What broader domain contains this? |
  > | **Sibling** | What peers sit alongside it under the same parent? |
  > | **Child / sub-concept** | What does this decompose into? |
  > | **Adjacent / cross-over** | What neighboring fields overlap or feed in? |
  > | **Frontier** | What is emerging / next at the edge of the field? |"
- **Codifier's reading:** A five-row question scaffold fillable for any subject — the finding's own implementation_notes call it "directly adoptable as a checklist inside /research-query or a future gap-analysis skill even without the full loop." Structural form for rendering. Fits the template form.
- **Suggested headline:** five-neighborhood-coverage-checklist
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### sprint-contract-negotiation-pattern::template::sprint-contract-template

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[sprint-contract-negotiation-pattern]]
- **Source excerpt:**
  > "Before each sprint, the generator proposes implementation scope and success criteria; the evaluator reviews and negotiates until both agree on what \"done\" looks like. These contracts contain granular, testable criteria. The evaluator then scores against these specific criteria rather than subjective quality judgments."
- **Codifier's reading:** The described contract (scope + granular testable criteria + negotiation record) is a fillable document scaffold; the guide embeds a Sprint Contract template derived from it, but no standalone template artifact exists (finding was synthesized in 2026-04, pre-DD-101, and never queue-scanned). Fits the template form.
- **Suggested headline:** sprint-contract-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### loop-contract-anatomy-and-evolve-session-cadence::template::loop-contract-file-schema

- **Date queued:** 2026-07-19
- **Status:** queued
- **Target form:** template
- **Source finding:** [[loop-contract-anatomy-and-evolve-session-cadence]]
- **Source excerpt:**
  > "every autonomous loop/automation gets ONE living markdown file that is simultaneously its constitution and its memory — a 'contract' section (goal, boundaries on what it can do unsupervised vs. what needs human escalation, and an SOP), a deliberately small 'state' section (current hypothesis, open backlog, items shipped but needing follow-up), and an append-only 'log' of what happened each run."
- **Codifier's reading:** A fixed three-section markdown scaffold (contract / state / log) fillable per automation — placeholder structural form meant for rendering, reusable across any recurring loop. Fits the template form. The guide embeds a prose description of it in Step 9 but no standalone fillable artifact exists.
- **Suggested headline:** loop-contract-file-schema (contract/state/log)
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### loop-trigger-taxonomy-poll-then-wake-combo::rule::combo-trigger-cheap-precheck-before-llm-wake

- **Date queued:** 2026-07-19
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[loop-trigger-taxonomy-poll-then-wake-combo]]
- **Source excerpt:**
  > "a cron-interval ticker runs a cheap deterministic script first to check programmatically whether there is real new work; only if so does it wake the expensive LLM agent."
- **Codifier's reading:** An imperative, machine-checkable directive for scheduled jobs — gate the expensive LLM wake behind a cheap deterministic pre-check; skip the run entirely on no-op. Enforceable at review of any cron-shaped job config. Fits the rule form (a "wake the model only if" gate).
- **Suggested headline:** combo-trigger: cheap pre-check before LLM wake
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### lint-test-failures-as-remediation-prompts::rule::author-lint-failures-as-remediation-prompts

- **Date queued:** 2026-07-19
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[lint-test-failures-as-remediation-prompts]]
- **Source excerpt:**
  > "write every failure message as if it were a prompt ... a failure that states the codebase's convention, the reason for it, and the specific fix ... does [change behavior], because it's legible as an instruction rather than a symptom report."
- **Codifier's reading:** An imperative authoring standard applicable to every custom lint rule and structural test — "state the convention, the why, and the what-instead, not just the no." Machine-checkable at rule-authoring review (does this failure message carry a fix and a rationale?). Fits the rule form. Scope caveat noted in the finding (embedded-agent-in-test extension is a separate, tightly-scoped concern).
- **Suggested headline:** author lint/test failures as remediation prompts
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**
