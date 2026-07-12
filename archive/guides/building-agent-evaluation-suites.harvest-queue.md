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
