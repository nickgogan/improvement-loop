# Co-occurrence Harvest Queue — Autonomous and Scheduled Agent Operation

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.
Transferred from the G3b `agent-workflow-and-execution` queue on the DD-122 split (session 152); rows whose source finding routed to G3d land here.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | extracted | rule | [[headless-cron-composition-autonomous-scheduled-workflows]] | "headless-output-verifiability-gate" | extracted to [[headless-output-verifiability-gate]] |
| 2026-07-16 | extracted | rule | [[dark-factory-ai-only-codebase-management]] | "deterministic-nodes-for-non-reasoning-steps" | extracted to [[deterministic-nodes-for-non-reasoning-steps]] |
| 2026-07-16 | extracted | skill | [[ecosystem-monitoring-meta-loop]] | "write-run-log-shared-utility-skill" | extracted to [[write-run-log-shared-utility-skill]] |
| 2026-07-16 | extracted | template | [[scheduled-skill-chaining-with-file-based-activation]] | "scheduled-job-config-schema-template" | extracted to [[scheduled-job-config-schema-template]] |
| 2026-07-16 | extracted | template | [[github-label-as-workflow-state]] | "workflow-state-label-schema-template" | extracted to [[workflow-state-label-schema-template]] |
| 2026-07-19 | extracted | template | [[loop-contract-anatomy-and-evolve-session-cadence]] | "loop-contract-file-schema (contract/state/log)" | extracted to [[loop-contract-file-schema]] |
| 2026-07-19 | extracted | rule | [[loop-trigger-taxonomy-poll-then-wake-combo]] | "combo-trigger: cheap pre-check before LLM wake" | merged into [[deterministic-nodes-for-non-reasoning-steps]] |

## Per-row details

### headless-cron-composition-autonomous-scheduled-workflows::rule::headless-output-verifiability-gate

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[headless-cron-composition-autonomous-scheduled-workflows]]
- **Source excerpt:**
  > "The decision criterion for going headless is **output verifiability**: only use headless mode for tasks where the output is easy to verify after the fact. Hard-to-undo operations should not run headless."
- **Codifier's reading:** Imperative, machine-enforceable directive ("only use headless mode when...; hard-to-undo operations should not run headless") — a binary gate checkable at workflow-definition time. Fits the rule form: never/only phrasing, enforceable at review of any scheduled-job config.
- **Suggested headline:** headless-output-verifiability-gate
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[headless-output-verifiability-gate]]

Extracted 2026-07-19 — Session 152 — [[autonomous-scheduled-agent-operation.harvest-queue]] — to [[headless-output-verifiability-gate]]. DD-97 extension proposal (primary match [[scheduled-workflows-require-human-checkpoint]]) ruled **create-new** by Nick (delegated ruling, session 152): the two are complementary siblings — this rule is the design-time headless go/no-go criterion; the checkpoint rule is the runtime publish-boundary gate. The new rule cross-references the sibling in its Governance/Rationale; they compose (a workflow may clear this gate to run headless and still need the publish checkpoint).

### dark-factory-ai-only-codebase-management::rule::deterministic-nodes-for-non-reasoning-steps

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[dark-factory-ai-only-codebase-management]]
- **Source excerpt:**
  > "**Deterministic vs agentic nodes:** steps that don't need reasoning (formatting, lint, triggering deploys) should be plain code, not LLM calls — reliability by subtraction."
- **Codifier's reading:** Imperative directive with a clear enforcement test (audit every workflow node: does this step need reasoning? if not, no LLM call). Machine-checkable against a workflow DAG definition. Fits the rule form.
- **Suggested headline:** deterministic-nodes-for-non-reasoning-steps
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[deterministic-nodes-for-non-reasoning-steps]]

Extracted 2026-07-19 — Session 152 — [[autonomous-scheduled-agent-operation.harvest-queue]] — to [[deterministic-nodes-for-non-reasoning-steps]].

### ecosystem-monitoring-meta-loop::skill::write-run-log-shared-utility-skill

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** skill
- **Source finding:** [[ecosystem-monitoring-meta-loop]]
- **Source excerpt:**
  > "**Health check via a shared run-log skill.** A `write-run-log` utility skill writes every loop's results to one folder. Updating that one skill updates logging across every loop. Cross-referencing the logs shows what is and isn't running successfully — the practitioner's claim is that most loop operators are silently burning tokens on broken or useless loops, and this makes them visible enough to turn off."
- **Codifier's reading:** A named procedure with a clear input/output contract (loop result in, standardized log row out to one folder) and an invocation contract (called by every loop at run end). Fits the skill form; directly serves the engine's own loop portfolio gap noted in the finding's implementation_notes.
- **Suggested headline:** write-run-log-shared-utility-skill
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[write-run-log-shared-utility-skill]]

Extracted 2026-07-19 — Session 152 — [[autonomous-scheduled-agent-operation.harvest-queue]] — to [[write-run-log-shared-utility-skill]].

### scheduled-skill-chaining-with-file-based-activation::template::scheduled-job-config-schema-template

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[scheduled-skill-chaining-with-file-based-activation]]
- **Source excerpt:**
  > "The file-based activation pattern would benefit from a standard schema: job name, schedule (cron expression), skill chain (ordered list), activation flag, last-run timestamp, last-run status. This enables the scheduled task dashboard pattern to visualize all jobs."
- **Codifier's reading:** An explicit field-list schema for a config artifact — structural form with named fillable fields. The guide's Scheduled Workflow Definition template is derived from it; a standalone template artifact would make it reusable outside the guide. Fits the template form.
- **Suggested headline:** scheduled-job-config-schema-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[scheduled-job-config-schema-template]]

Extracted 2026-07-19 — Session 152 — [[autonomous-scheduled-agent-operation.harvest-queue]] — to [[scheduled-job-config-schema-template]].

### github-label-as-workflow-state::template::workflow-state-label-schema-template

- **Date queued:** 2026-07-16
- **Status:** extracted
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
- **Resolution:** extracted to [[workflow-state-label-schema-template]]

Extracted 2026-07-19 — Session 152 — [[autonomous-scheduled-agent-operation.harvest-queue]] — to [[workflow-state-label-schema-template]].

### loop-contract-anatomy-and-evolve-session-cadence::template::loop-contract-file-schema

- **Date queued:** 2026-07-19
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[loop-contract-anatomy-and-evolve-session-cadence]]
- **Source excerpt:**
  > "every autonomous loop/automation gets ONE living markdown file that is simultaneously its constitution and its memory — a 'contract' section (goal, boundaries on what it can do unsupervised vs. what needs human escalation, and an SOP), a deliberately small 'state' section (current hypothesis, open backlog, items shipped but needing follow-up), and an append-only 'log' of what happened each run."
- **Codifier's reading:** A fixed three-section markdown scaffold (contract / state / log) fillable per automation — placeholder structural form meant for rendering, reusable across any recurring loop. Fits the template form. The guide embeds a fillable Loop Contract File template derived from it (G3d Templates).
- **Suggested headline:** loop-contract-file-schema (contract/state/log)
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[loop-contract-file-schema]]

Extracted 2026-07-19 — Session 152 — [[autonomous-scheduled-agent-operation.harvest-queue]] — to [[loop-contract-file-schema]]. DD-100 version-bump proposal (primary match [[loop-anatomy-spec-template]] v1) ruled **create-new** by Nick (delegated ruling, session 152): written as a new baseline template at the unsuffixed stem `loop-contract-file-schema` (not a `-v2`), since it addresses a different object (ongoing lifecycle governance: contract/state/log) at a different altitude than the build-time mechanical iteration anatomy of [[loop-anatomy-spec-template]]. The new template's Composition Note cross-references the sibling — a single automation may carry both (anatomy spec at build time, contract file across its lifetime).

### loop-trigger-taxonomy-poll-then-wake-combo::rule::combo-trigger-cheap-precheck-before-llm-wake

- **Date queued:** 2026-07-19
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[loop-trigger-taxonomy-poll-then-wake-combo]]
- **Source excerpt:**
  > "a cron-interval ticker runs a cheap deterministic script first to check programmatically whether there is real new work; only if so does it wake the expensive LLM agent."
- **Codifier's reading:** An imperative, machine-checkable directive for scheduled jobs — gate the expensive LLM wake behind a cheap deterministic pre-check; skip the run entirely on no-op. Enforceable at review of any cron-shaped job config. Fits the rule form (a "wake the model only if" gate).
- **Suggested headline:** combo-trigger: cheap pre-check before LLM wake
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[deterministic-nodes-for-non-reasoning-steps]]

Extracted 2026-07-19 — Session 152 — [[autonomous-scheduled-agent-operation.harvest-queue]] — merged into [[deterministic-nodes-for-non-reasoning-steps]]. DD-97 extension proposal (primary match [[deterministic-nodes-for-non-reasoning-steps]]) ruled **extend-existing** by Nick (delegated ruling, session 152): the "Special Case: The Trigger/Wake Node" section was appended to that rule by hand (blockquote content rendered as normal section prose in house style), with [[loop-trigger-taxonomy-poll-then-wake-combo]] cited as the section's source; the source finding was back-annotated (extraction note + consumed_by) with pipeline_status held at synthesized. No new artifact created — same claim and mechanism applied to the trigger/wake node specifically.
