# Co-occurrence Harvest Queue — Production Agent Execution

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.
Transferred from the G3b `agent-workflow-and-execution` queue on the DD-122 split (session 152); rows whose source finding routed to G3c land here.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | extracted | template | [[self-improvement-dispatch-table-route-never-reimplement]] | "dispatch-table-schema-template" | extracted to [[dispatch-table-schema-template]] |
| 2026-07-16 | extracted | template | [[concept-family-explorer-five-neighborhood-gap-mapping]] | "five-neighborhood-coverage-checklist" | extracted to [[five-neighborhood-coverage-checklist]] |
| 2026-07-16 | extracted | template | [[sprint-contract-negotiation-pattern]] | "sprint-contract-template" | extracted to [[sprint-contract-template]] |
| 2026-07-19 | extracted | rule | [[lint-test-failures-as-remediation-prompts]] | "author lint/test failures as remediation prompts" | extracted to [[author-lint-failures-as-remediation-prompts]] |

## Per-row details

### self-improvement-dispatch-table-route-never-reimplement::template::dispatch-table-schema-template

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[self-improvement-dispatch-table-route-never-reimplement]]
- **Source excerpt:**
  > "A reference table in the skill package with one row per finding class. Each row carries three things: **signals** (how to recognize the class), **route** (which skill owns the work), and — the subtle part — **what this skill still does** (its residual duty even when routing)."
- **Codifier's reading:** A structural scaffold meant for rendering — a fixed three-column row schema (signals / route / residual duty) fillable per work class by any intake surface. Fits the template form: placeholder fields, structural form, reusable across dispatchers.
- **Suggested headline:** dispatch-table-schema-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[dispatch-table-schema-template]]

Extracted 2026-07-19 — Session 152 — [[production-agent-execution.harvest-queue]] — to [[dispatch-table-schema-template]].

### concept-family-explorer-five-neighborhood-gap-mapping::template::five-neighborhood-coverage-checklist

- **Date queued:** 2026-07-16
- **Status:** extracted
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
- **Resolution:** extracted to [[five-neighborhood-coverage-checklist]]

Extracted 2026-07-19 — Session 152 — [[production-agent-execution.harvest-queue]] — to [[five-neighborhood-coverage-checklist]].

### sprint-contract-negotiation-pattern::template::sprint-contract-template

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[sprint-contract-negotiation-pattern]]
- **Source excerpt:**
  > "Before each sprint, the generator proposes implementation scope and success criteria; the evaluator reviews and negotiates until both agree on what \"done\" looks like. These contracts contain granular, testable criteria. The evaluator then scores against these specific criteria rather than subjective quality judgments."
- **Codifier's reading:** The described contract (scope + granular testable criteria + negotiation record) is a fillable document scaffold; the guide embeds a Sprint Contract template derived from it, but no standalone template artifact exists (finding was synthesized in 2026-04, pre-DD-101, and never queue-scanned). Fits the template form.
- **Suggested headline:** sprint-contract-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[sprint-contract-template]]

Extracted 2026-07-19 — Session 152 — [[production-agent-execution.harvest-queue]] — to [[sprint-contract-template]].

### lint-test-failures-as-remediation-prompts::rule::author-lint-failures-as-remediation-prompts

- **Date queued:** 2026-07-19
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[lint-test-failures-as-remediation-prompts]]
- **Source excerpt:**
  > "write every failure message as if it were a prompt ... a failure that states the codebase's convention, the reason for it, and the specific fix ... does [change behavior], because it's legible as an instruction rather than a symptom report."
- **Codifier's reading:** An imperative authoring standard applicable to every custom lint rule and structural test — "state the convention, the why, and the what-instead, not just the no." Machine-checkable at rule-authoring review (does this failure message carry a fix and a rationale?). Fits the rule form. Scope caveat noted in the finding (embedded-agent-in-test extension is a separate, tightly-scoped concern).
- **Suggested headline:** author lint/test failures as remediation prompts
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[author-lint-failures-as-remediation-prompts]]

Extracted 2026-07-19 — Session 152 — [[production-agent-execution.harvest-queue]] — to [[author-lint-failures-as-remediation-prompts]].
