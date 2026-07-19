# Co-occurrence Harvest Queue — Agent Architecture Decisions

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | queued | template | [[loop-node-anatomy-schema-enforced-ralph-primitive]] | "loop-anatomy-spec-template" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[work-ticket-contract-prompt-mode-vs-work-mode]] | "work-ticket-contract-template" | extract via /extract-artifacts |
| 2026-07-16 | queued | skill | [[four-estimate-agent-routing-test]] | "four-estimate-routing-test-skill" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[planner-executor-deterministic-guardrails]] | "deterministic-execution-boundary-rule" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[effort-scaling-rules-embedded-in-orchestrator]] | "effort-scaling-resource-allocation-rule" | extract via /extract-artifacts |
| 2026-07-19 | queued | template | [[structured-handoff-schema-self-healing-multi-agent-missions]] | "worker-handoff-schema-template" | extract via /extract-artifacts |
| 2026-07-19 | queued | template | [[pre-code-validation-contracts-dual-blind-validators]] | "pre-code-validation-contract-template" | extract via /extract-artifacts |
| 2026-07-19 | queued | rule | [[droid-whispering-per-role-model-assignment]] | "cross-provider-validator-assignment-rule" | extract via /extract-artifacts |

## Per-row details

### loop-node-anatomy-schema-enforced-ralph-primitive::template::loop-anatomy-spec-template

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[loop-node-anatomy-schema-enforced-ralph-primitive]]
- **Source excerpt:**
  > "| Completion signal | `until:` string matched in AI output (e.g. `<promise>COMPLETE</promise>`) |
  > | Deterministic check | `until_bash:` optional script run after each iteration; exit 0 = complete |
  > | Budget | `max_iterations` (required); exceeding it fails the node; `retry` is explicitly rejected on loop nodes by schema validation |
  > | Context policy | `fresh_context: true` starts a new session per iteration; `$LOOP_PREV_OUTPUT` bridges the previous iteration's cleaned output into the fresh session |
  > | Human-in-loop | `interactive: true` + `gate_message` pauses every iteration ... |"
- **Codifier's reading:** The loop-config element table is a structural scaffold meant for rendering — a complete fill-in spec for any agent loop (signal, check, budget, context policy, gate, observability, resume). It fits the template form: placeholder fields, structural form, reusable across loop implementations. The guide now embeds a Loop Anatomy Spec template derived from it; a standalone template artifact would make it reusable outside the guide.
- **Suggested headline:** loop-anatomy-spec-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### work-ticket-contract-prompt-mode-vs-work-mode::template::work-ticket-contract-template

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[work-ticket-contract-prompt-mode-vs-work-mode]]
- **Source excerpt:**
  > "A conformant work-ticket states:
  > - **Outcome** — what needs to happen, as a result, not a request
  > - **Owner** — who (human or agent) it is assigned to
  > - **Sources** — the background material carried with the work ...
  > - **Scope limits** — what the agent may do and where it must stop
  > - **Definition of done** — the acceptance condition
  > - **Receipt** — what it must show when finished"
- **Codifier's reading:** A fixed field list defining the boundary object for agent-to-agent/human work handoff, plus lifecycle states (claim receipt, done receipt, needs-input). Reads as a fillable structural scaffold — template form per the rubric's "structural form meant for rendering" criterion.
- **Suggested headline:** work-ticket-contract-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### four-estimate-agent-routing-test::skill::four-estimate-routing-test-skill

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** skill
- **Source finding:** [[four-estimate-agent-routing-test]]
- **Source excerpt:**
  > "A one-minute estimation pass over any task ... 1. **Size** — is the task bigger than what one agent can hold at full quality? 2. **Independence** — can the parts be done without knowing what the other parts did? 3. **Separation of concerns** — do any parts need different minds? 4. **Checkability** — is checking an answer much cheaper than producing one? ... Verdicts: small problem → **chat**; fits one context window and checks its own work → **single agent with a goal**; bigger than one perspective or needs separate minds → **team of agents**; judgment call ... → **human, no AI**."
- **Codifier's reading:** A bounded procedure with a clear input (task description), step-by-step estimation sequence, and a closed-enum output (chat/agent/team/human) — skill shape per the rubric's invocation-contract and input/output criteria. The finding itself suggests folding the money dials into "engine skill triggers."
- **Suggested headline:** four-estimate-routing-test-skill
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### planner-executor-deterministic-guardrails::rule::deterministic-execution-boundary-rule

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[planner-executor-deterministic-guardrails]]
- **Source excerpt:**
  > "Hard rule: planning can be probabilistic; execution must be deterministic. ... The executor runs steps deterministically -- no LLM reasoning during execution, only schema validation and tool invocation. ... Compliance controls and retry logic should be deterministic, not probabilistic."
- **Codifier's reading:** An imperative, machine-checkable directive ("execution must be deterministic"; "no LLM reasoning during execution") embedded in a pattern finding. The finding was extracted as a pattern (2026-04-19); the embedded hard rule is a distinct non-pattern form candidate.
- **Suggested headline:** deterministic-execution-boundary-rule
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### effort-scaling-rules-embedded-in-orchestrator::rule::effort-scaling-resource-allocation-rule

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[effort-scaling-rules-embedded-in-orchestrator]]
- **Source excerpt:**
  > "Explicit rules embedded in the lead agent's prompt that govern resource allocation based on query complexity. ... (1) Simple factual queries: 1 subagent, 3-10 tool calls. (2) Comparison queries: 2-4 subagents, 10-15 tool calls. (3) Complex multi-source research: 10+ subagents with explicitly divided roles."
- **Codifier's reading:** Tiered numeric allocation directives suitable for verbatim embedding in an orchestrator prompt — imperative and enforceable, rule shape. The finding was extracted as a pattern (2026-04-19); the embedded allocation table is a distinct rule-form candidate.
- **Suggested headline:** effort-scaling-resource-allocation-rule
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### structured-handoff-schema-self-healing-multi-agent-missions::template::worker-handoff-schema-template

- **Date queued:** 2026-07-19
- **Status:** queued
- **Target form:** template
- **Source finding:** [[structured-handoff-schema-self-healing-multi-agent-missions]]
- **Source excerpt:**
  > "each worker fills out a fixed schema at the end of its feature: (1) what was completed; (2) what was explicitly left undone; (3) every command run paired with its exit code; (4) issues discovered; (5) whether the worker's actual behavior abided by the orchestrator's defined procedures."
- **Codifier's reading:** A fixed five-field schema a worker renders at each boundary — a structural scaffold with placeholder fields meant for rendering, template form per the rubric. The guide now embeds a Worker Handoff Schema template derived from it; a standalone template artifact would make it reusable outside this guide (P1 finding, so high extraction value).
- **Suggested headline:** worker-handoff-schema-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### pre-code-validation-contracts-dual-blind-validators::template::pre-code-validation-contract-template

- **Date queued:** 2026-07-19
- **Status:** queued
- **Target form:** template
- **Source finding:** [[pre-code-validation-contracts-dual-blind-validators]]
- **Source excerpt:**
  > "a validation contract written by the orchestrator during planning, before any code exists ... hundreds of individual assertions; every feature assigned one or more assertions such that the sum of all features' assertions covers the full contract ... two blind adversarial validators run after each milestone, neither of which has seen the implementation: a scrutiny validator ... and a user-testing validator."
- **Codifier's reading:** The contract structure (assertion set + feature-assignment coverage rule + two named blind validators) is a fillable structural scaffold — template form. The guide embeds a Pre-Code Validation Contract template derived from it; a standalone artifact would make the before-code assertion pattern reusable.
- **Suggested headline:** pre-code-validation-contract-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### droid-whispering-per-role-model-assignment::rule::cross-provider-validator-assignment-rule

- **Date queued:** 2026-07-19
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[droid-whispering-per-role-model-assignment]]
- **Source excerpt:**
  > "validation should run on a model from a different provider than implementation — bias decorrelation (different training data, not just a different context window), not cost/capability optimization."
- **Codifier's reading:** An imperative, checkable directive ("run validation on a different provider than the implementer") embedded in a Model-Selection pattern finding — rule shape per the rubric's imperative/machine-enforceable criterion. Distinct from the finding's broader per-role-assignment discussion; the cross-provider validator constraint is the enforceable kernel.
- **Suggested headline:** cross-provider-validator-assignment-rule
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**
