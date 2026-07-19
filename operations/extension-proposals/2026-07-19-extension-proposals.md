---
type: "extension-proposals-report"
target_system:
  - "improvement-loop"
generated_by: "/extract-artifacts"
date: "2026-07-19"
identification_report: "autonomous-scheduled-agent-operation.harvest-queue"
total_rule_skill_candidates: 8
proposals_emitted: 8
no_match_passthrough: 0
forms_scanned:
  - "rules"
  - "skills"
---

# Extension Proposals — 2026-07-19

Seven rule candidates and one skill candidate scanned across eight separate harvest-queue promotion runs (DD-101, session 152). All eight DD-97 corpus scans (seven over `extracts/rules/`, one over `extracts/skills/`) found a semantic-family match; eight extension proposals are emitted. Source 1: `eval-driven-improvement-loops.harvest-queue.md` (row `garbage-collection-day-persona-review-agents::rule::convert-review-feedback-to-durable-checks`), Status `nick-approved`. Source 2: `autonomous-scheduled-agent-operation.harvest-queue.md` (row `headless-cron-composition-autonomous-scheduled-workflows::rule::headless-output-verifiability-gate`), Status `nick-approved`. Source 3: `agent-architecture-decisions.harvest-queue.md` (row `planner-executor-deterministic-guardrails::rule::deterministic-execution-boundary-rule`), Status `nick-approved`. Source 4: `designing-agent-tools.harvest-queue.md` (row `static-tool-set-mode-changes-as-callable-tools::rule::tool-surface-session-static-modes-as-tools`), Status `nick-approved`. Source 5: `autonomous-scheduled-agent-operation.harvest-queue.md` (row `loop-trigger-taxonomy-poll-then-wake-combo::rule::combo-trigger-cheap-precheck-before-llm-wake`), Status `nick-approved`. Source 6: `agent-architecture-decisions.harvest-queue.md` (row `droid-whispering-per-role-model-assignment::rule::cross-provider-validator-assignment-rule`), Status `nick-approved`. Source 7: `agent-architecture-decisions.harvest-queue.md` (row `four-estimate-agent-routing-test::skill::four-estimate-routing-test-skill`), Status `nick-approved`. Source 8: `designing-agent-tools.harvest-queue.md` (row `stateful-mcp-subprocess-vs-cli-shell-out::rule::statefulness-boundary-on-cli-first-rule`), Status `nick-approved`. Forms scanned: rules, skills. Per DD-97 §Rules #3 this report proposes only — no existing artifact is modified here; Nick rules the merge target per proposal.

## Rulings (session 152, Nick-delegated)

Nick delegated all eight rulings to the orchestrating agent this session ("proceed, I trust your judgement"); every ruling concurs with the Codifier recommendation below, and all eight were executed same-session:

| Proposal | Ruling | Executed as |
|---|---|---|
| droid-whispering-per-role-model-assignment | create new | [[cross-provider-validator-assignment-rule]] |
| four-estimate-agent-routing-test | create new | [[four-estimate-routing-test-skill]] |
| garbage-collection-day-persona-review-agents | extend existing | merged into [[every-recurring-review-comment-triages-to-mechanism-or-judgment]] |
| headless-cron-composition-autonomous-scheduled-workflows | create new | [[headless-output-verifiability-gate]] |
| loop-trigger-taxonomy-poll-then-wake-combo | extend existing | merged into [[deterministic-nodes-for-non-reasoning-steps]] |
| planner-executor-deterministic-guardrails | create new | [[deterministic-execution-boundary-rule]] |
| stateful-mcp-subprocess-vs-cli-shell-out | extend existing | merged into [[prefer-cli-over-mcp-when-both-exist-for-the-same-tool]] |
| static-tool-set-mode-changes-as-callable-tools | extend existing | merged into [[never-mutate-cached-prompt-prefix]] |

## Proposals

### droid-whispering-per-role-model-assignment

**Form:** rule
**Existing artifact (primary match):** [[holdout-validation-pattern-blind-regression]]
**Secondary matches:** (none)

**Codifier recommendation:** create new (false positive)

**Why this match:** Both rules belong to the "keep the validator unbiased" family and both use the word "blind" as their organizing concept, but they attack different bias sources with orthogonal mechanisms: `holdout-validation-pattern-blind-regression` withholds *information* (PR description, git history, branch names) from the validator so it can't be sycophantic about implementation intent it's aware of; the candidate withholds nothing informational — it instead requires the validator to run on a *different model provider* than the implementer, so that shared training-data blind spots don't correlate between builder and checker. The DD-97 loose scan flags the shared "blind/unbiased validator" vocabulary as family overlap worth surfacing rather than silently drafting a second validator-bias rule.

**Diff sketch:**

If Nick ruled *extend* on the primary match, the appended Evidence row on `holdout-validation-pattern-blind-regression` would cite: "Validation bias also arises independent of context holdout: a validator built on the same model family as the implementer shares training-data blind spots. Run validation on a model from a different provider than implementation — bias decorrelation via different training data, not a cost/capability optimization." Source finding: [[droid-whispering-per-role-model-assignment]].

**However, the honest recommendation is create-new**, because the two constraints are independently necessary and jointly sufficient, not one a special case of the other:

- The existing rule's Invariants are entirely about *information access* (no PR description, no git history, fresh session, full regression suite) — nothing in its Condition, Action, or Enforcement mechanism references model provider or model identity at all. Its `Enforcement` check is a four-part boolean over session context visibility; adding a provider constraint would require a structurally new fifth clause about a completely different axis (which model executes the validator), not a wording tweak to an existing clause.
- The two constraints compose orthogonally: a workflow could satisfy context-holdout with a same-provider model (still vulnerable to shared training-data blind spots) or satisfy cross-provider assignment with full context visibility (still vulnerable to sycophancy from knowing implementation intent). Neither implies the other; a maximally unbiased validator wants both simultaneously.

A merge would conflate "what the validator is allowed to see" with "which model runs the validator" under one rule's invariant set, weakening the existing rule's crisp four-part enforcement check. Two sibling rules in the same "unbiased validation" family, cross-referenced, is the coherent home.

**Notes:** Recommendation **create new (false positive)**. Surfaced per DD-97's loose calibration rather than silently drafting a second validator-bias rule without flagging the family overlap. If Nick concurs, re-invoke `/extract-artifacts --harvest-row droid-whispering-per-role-model-assignment::rule::cross-provider-validator-assignment-rule` to write the new rule. Per DD-97 v1 no artifact is created or modified here.

### four-estimate-agent-routing-test

**Form:** skill
**Existing artifact (primary match):** [[seam-map-delegation-rubric]]
**Secondary matches:** (none)

**Codifier recommendation:** create new (false positive)

**Why this match:** Both are one-minute, human-vs-AI work-allocation rubrics that run *before* any agent is deployed, and both terminate in a distinguished "keep it human / no AI" verdict. The overlap is asserted by the KB itself: this candidate's source finding lists `seam-map-delegation-rubric`'s source (`human-ai-seam-identification-three-question-rubric`) as a `same-problem` related finding, and both artifacts are explicitly destined for the *same* Phase 4 agent-vs-skill design interview (seam-map's Adaptation Notes fold its three questions into "the Phase 4 agent-vs-skill interview script"; this candidate's finding is flagged "a Phase 4 interview / IB-176 design input"). The DD-97 loose scan flags this shared "pre-deployment human/AI allocation rubric feeding the same interview" shape as family overlap worth surfacing rather than silently drafting a second allocation rubric.

**Diff sketch:**

If Nick ruled *parameterize as mode variant* on the primary match, `seam-map-delegation-rubric` would gain a second mode alongside its existing partition mode:

- **Mode flag:** `--mode task-routing` (vs. the existing default `--mode seam-partition`).
- **How the variant differs:** the existing mode takes one candidate *workflow* and returns a three-column human/AI/joint *partition* of its parts. The `task-routing` variant takes one *task* and returns a single categorical *vehicle verdict* — chat / single agent with a goal / team of agents / human (no AI) — from four estimates: size (does it exceed one agent's full-quality context?), independence (can parts run without cross-talk?), separation of concerns (do parts need different minds — e.g. a critic who didn't write the draft?), and checkability (is verifying an answer much cheaper than producing one?).
- **Documentation block to add** to the existing skill's body: a "Task-Routing Mode" section documenting the four estimates, the four-way verdict, the two "money dials" (recurrence, value of a good answer) that sharpen the verdict, and the anti-delegation edge ("no frontier model beats an expert at the thing they are most expert in").
- **ContractSpec invariant additions** covering the new mode: the verdict is one of exactly four classes; a `team` verdict never fires without a named cheap checker satisfying the checkability estimate (verifier-ceiling link); size estimates carry a re-anchoring caveat (what needed a team last quarter may fit one agent now).

**However, the honest recommendation is create-new**, because the two rubrics compose in sequence rather than being two modes of one operation:

- `seam-map-delegation-rubric` **decomposes and partitions** a single workflow into human/AI/joint parts — its output is a map, and it makes no claim about *what shape* the AI-owned side should take.
- The candidate **classifies a whole task to a deployment vehicle** — its output is one of four verdicts, and its defining axis (single agent vs. a *team* of agents, gated by independence + checkability) is entirely absent from seam-map. A `team of agents` verdict is itself the *input* to a subsequent seam/decomposition partition — the two run in series (route the task to a vehicle → if team, partition the work), not as alternate modes of one skill.

A merge would collapse "which parts leave the human" and "what shape of AI deployment this task needs" into one skill's invariant set, blurring seam-map's crisp partition-map output with a categorical routing verdict. Two sibling skills in the same "pre-deployment human/AI allocation" family, cross-referenced and composed in sequence, is the coherent home — mirroring this run's `droid-whispering` and `planner-executor` create-new rulings (orthogonal, composable members of a family, not one subsuming the other).

**Notes:** Recommendation **create new (false positive)**; the `parameterize as mode variant` path is the plausible alternative if Nick prefers a single allocation-rubric skill with two modes, which is why the diff sketch above is written as a mode-variant delta. Surfaced per DD-97's loose calibration — the KB's own `same-problem` link plus the shared Phase 4 interview destination make this exactly the family overlap DD-97 exists to catch. If Nick concurs with create-new, re-invoke `/extract-artifacts --harvest-row four-estimate-agent-routing-test::skill::four-estimate-routing-test-skill` to write the new skill (note: re-invocation will re-trigger this same Step 1.7 scan — the merge decision must be recorded, e.g. by dismissing the match or scoping the write, so the second run drafts rather than re-proposing). Per DD-97 v1 no artifact is created or modified here.

### garbage-collection-day-persona-review-agents

**Form:** rule
**Existing artifact (primary match):** [[every-recurring-review-comment-triages-to-mechanism-or-judgment]]
**Secondary matches:** (none)

**Codifier recommendation:** extend existing

**Why this match:** Both rules answer the same question — what happens to recurring review feedback so it stops being re-given by a human — with the same two-terminal-state shape: convert to an automated mechanism (lint/test/CI check) or convert to a recorded judgment-only artifact a reviewer consults. The existing rule's two terminal states (`mechanism` / `judgment-only`) map directly onto the candidate's two fix vehicles ("a failing test or lint that makes the agent self-heal automatically" / "an addition to a persona's review-agent documentation"). This file is already the established live home for extending this shape — it previously absorbed an "Additional Evidence" addition (from `pattern-scale-signals-systemic-not-individual-failure`) broadening scope beyond code review to governance-scale recurrence, using exactly the same triage-to-mechanism-or-judgment structure.

**Diff sketch:**

Proposed as a new "Additional Evidence" paragraph under the existing rule's Rationale section, parallel in shape to the existing `pattern-scale-signals-systemic-not-individual-failure` addition:

> The garbage-collection-day pattern ([[garbage-collection-day-persona-review-agents]]) supplies a concrete, named cadence implementation of this rule's "stated cadence" governance requirement — a fixed weekly ritual (every Friday) rather than an ad-hoc or purely count-triggered check-in. It also broadens the trigger condition: rather than waiting for a comment class to recur across two or more changes, the ritual triages *every* piece of review friction observed within the week, once, on a fixed schedule — a stricter cadence variant teams may adopt when they want zero-lag conversion rather than a recurrence-count threshold. It corroborates the judgment-only terminal state's implementation as living documentation: bucketing recurring feedback by the reviewing engineer's persona (front-end architect, reliability engineer, scalability engineer) and consulting that persona's accumulated "what good looks like" doc is one concrete shape a judgment-only triage record can take, subsequently machine-enforced by a per-persona review agent that runs on every push.

Body wording elsewhere on the existing rule is unchanged; the Contract (preconditions/invariants/governance/recovery) is unchanged — this is corroborating evidence and a named cadence exemplar, not a new invariant.

**Note on scope suppression:** the source finding's persona-keyed review-agent architecture (one agent per reviewing-engineer persona) is agent-shaped and was already suppressed from the harvest queue per DD-82 before this scan ran — only the durable-conversion-rule facet reached this corpus scan. That facet is what is proposed for merge here; the persona-agent facet is out of scope for this proposal entirely (not a candidate for either extend or create-new).

**Notes:** Recommendation **extend existing**. If Nick concurs, apply the diff sketch above by hand (or via a future skill mode) to `every-recurring-review-comment-triages-to-mechanism-or-judgment.md`, then flip the harvest-queue row's Status to `extracted` and Resolution to `merged into [[every-recurring-review-comment-triages-to-mechanism-or-judgment]]`. The queue row also separately notes overlap with the engine's own `/self-improve` capture-and-promote loop — that is a distinct, engine-internal comparison for Nick to weigh independently of this KB-corpus merge recommendation. Per DD-97 v1 no artifact is created or modified here.

### headless-cron-composition-autonomous-scheduled-workflows

**Form:** rule
**Existing artifact (primary match):** [[scheduled-workflows-require-human-checkpoint]]
**Secondary matches:** (none)

**Codifier recommendation:** create new (false positive)

**Why this match:** Both rules govern how much unattended autonomy a scheduled/headless agent workflow may exercise, and both key the answer off a risk property of the output (reversibility / verifiability). The DD-97 loose scan flags the family overlap: "unattended agent execution + risk-gated autonomy limit" is the shared shape.

**Diff sketch:**

If Nick ruled *extend* on the primary match, the appended Evidence row on `scheduled-workflows-require-human-checkpoint` would cite: "The decision criterion for going headless is output verifiability: only use headless mode for tasks where the output is easy to verify after the fact. Hard-to-undo operations should not run headless." Source finding: [[headless-cron-composition-autonomous-scheduled-workflows]] (Medium / practitioner-documented).

**However, the honest recommendation is create-new**, because the candidate answers a different question with a different mechanism than the primary match, and covers ground the primary match explicitly excludes:

- `scheduled-workflows-require-human-checkpoint` is a **runtime mechanism** requirement: any scheduled workflow with an externally-visible side effect (publish, send, broadcast) MUST have a blocking human-approval gate before that action, full stop — regardless of how verifiable the output is. Its scope explicitly **excludes** closed-loop workflows with no externally-visible side effect ("reindexing a private knowledge base, generating a draft that lands in a private review folder with no notification").
- The candidate is a **design-time selection criterion**: whether a task is suitable for headless/unattended execution AT ALL, judged by post-hoc verifiability and reversibility of its output — not whether a live blocking gate exists. Its primary cited use cases (morning summary reports written to file, transcript-to-social-post pipelines saved to file) are exactly the closed-loop, non-externally-visible workflows the primary match carves out of its own scope.

So a dedicated rule (`headless-output-verifiability-gate`) is the coherent home for the candidate: a sibling in the "bounded autonomy for unattended agent work" family, not an extension of the publish-boundary checkpoint rule. The two rules are complementary and would compose cleanly (a workflow could satisfy the go/no-go criterion for running headless at all, and separately still need the publish checkpoint if its terminal step is externally visible).

**Notes:** Recommendation **create new (false positive)**. Surfaced per DD-97's loose calibration rather than silently drafting a second unattended-autonomy rule without flagging the family. If Nick concurs, re-invoke `/extract-artifacts --harvest-row headless-cron-composition-autonomous-scheduled-workflows::rule::headless-output-verifiability-gate` to write the new rule. Per DD-97 v1 no artifact is created or modified here.

### loop-trigger-taxonomy-poll-then-wake-combo

**Form:** rule
**Existing artifact (primary match):** [[deterministic-nodes-for-non-reasoning-steps]]
**Secondary matches:** (none)

**Codifier recommendation:** extend existing

**Why this match:** This is the closest overlap surfaced in this run — the primary match was drafted *earlier in the same harvest-queue processing session* from a sibling finding in the same guide cluster (`autonomous-scheduled-agent-operation`). Both rules assert the identical claim — a workflow step that doesn't need reasoning must be deterministic code, not an LLM call — and both cite the same underlying source concept ("reliability/cost by subtraction"). The candidate's "combo trigger" is a concrete instance of the general rule applied specifically to the wake/entry-point node of a scheduled loop: "a cron-interval ticker runs a cheap deterministic script first to check programmatically whether there is real new work; only if so does it wake the expensive LLM agent." The general rule's own Condition already scopes to "any multi-step automated or agentic workflow... per workflow node, not once per workflow" — the trigger/wake-check is itself a node under that Condition, and "is there new work?" is exactly the kind of boolean, fully-input-determined check the general rule's Action already names as deterministic-eligible.

**Diff sketch:**

Proposed as a new "Special Case: The Trigger/Wake Node" section on `deterministic-nodes-for-non-reasoning-steps.md`, naming the loop-trigger context explicitly since the general rule's body doesn't currently call out the entry-point node as a special case (it only gives internal-step examples — formatting, lint, deploy, diff, file move):

> **Special Case: The Trigger/Wake Node**
>
> The first node of any scheduled or event-driven loop — the check that decides whether to invoke the reasoning agent at all this cycle — is itself covered by this rule. A cron-interval ticker should run a cheap deterministic pre-check (compare a feed's last-modified/etag, query an API's "updates since" endpoint, diff a known state) and skip the run entirely — no agent invocation, no token spend — when the check finds no new work. Only a positive pre-check result should wake the expensive LLM-driven step. This is the "combo trigger" pattern: cron/schedule (trigger type 2) composed with a cheap deterministic gate before the actual agentic work fires.
>
> **Source:** [[loop-trigger-taxonomy-poll-then-wake-combo]] (Strong / production-tested — a support-inbox triage loop polling Intercom every 30 minutes, arrived at via a self-proposed evolve-session optimization after running for a while, not the loop's original design).

Body wording elsewhere on the existing rule is unchanged; the Contract (preconditions/invariants/governance/recovery) is unchanged — the new content is a named special case of the existing invariant ("every non-reasoning node is deterministic code"), applied to the specific node that starts the workflow, not a new invariant.

**Notes:** Recommendation **extend existing** — unlike several of this run's other proposals, this candidate does not answer a different question or use a different mechanism; it is the same claim, same mechanism, applied to one specific node type (the wake/trigger check) that the general rule's body doesn't yet call out by name, drawn from a different source finding in the same guide. If Nick concurs, apply the diff sketch above by hand (or via a future skill mode) to `deterministic-nodes-for-non-reasoning-steps.md`, then flip the harvest-queue row's Status to `extracted` and Resolution to `merged into [[deterministic-nodes-for-non-reasoning-steps]]`. Per DD-97 v1 no artifact is created or modified here.

### planner-executor-deterministic-guardrails

**Form:** rule
**Existing artifact (primary match):** [[deterministic-nodes-for-non-reasoning-workflow-steps]]
**Secondary matches:** (none)

**Codifier recommendation:** create new (false positive)

**Why this match:** Both rules share the same core normative move — forbid LLM/agent reasoning on steps that don't need it, replace with deterministic execution. The DD-97 loose scan flags the family overlap: "deterministic execution over probabilistic LLM steps" is the shared shape, and both rules' Rationale sections cite the same underlying risk (stochastic failure surface / irreversible side effects from ungoverned LLM calls).

**Diff sketch:**

If Nick ruled *extend* on the primary match, the appended Evidence row on `deterministic-nodes-for-non-reasoning-workflow-steps` would cite: "In a planner-executor architecture, the plan/execute boundary is itself a categorical instance of the reasoning-audit: everything downstream of a finalized plan is by construction non-reasoning (the judgment already happened during planning), so the entire executor phase is deterministic — schema validation and tool invocation only, no LLM calls." Source finding: [[planner-executor-deterministic-guardrails]] (Strong / production-tested).

**However, the honest recommendation is create-new**, because the candidate answers a different question with a different mechanism than the primary match:

- `deterministic-nodes-for-non-reasoning-workflow-steps` is a **per-node audit heuristic**: for each node in ANY workflow graph, ask "does this step need reasoning?" — if no, deterministic code; if yes, an LLM call is explicitly retained ("Nodes that genuinely require synthesis, classification of ambiguous input, or open-ended judgment retain an LLM/agent call"). It makes no architectural claim about where planning happens.
- The candidate is an **architectural phase-boundary claim** specific to a planner-executor-verifier split: the planner (LLM) resolves all judgment up front into an explicit step plan; the executor then runs with zero exceptions — no LLM reasoning during execution at all, "only schema validation and tool invocation." It doesn't audit nodes one at a time; it asserts a categorical boundary between two named roles (planner vs. executor), and the source pattern already extracted (`extracts/patterns/planner-executor-deterministic-guardrails.md`) treats this three-phase pattern (plan → execute → verify) as a named architecture, not a generic per-step heuristic.

A merge would blur an architecture-scoped rule (planner-executor separation) into a general per-node audit rule that deliberately preserves exceptions for reasoning-needed nodes — the candidate has no such exception at the executor phase. The two rules are complementary siblings in the same family (a team could apply the general node-audit heuristic when NOT using a planner-executor split, and apply this stricter phase-boundary rule when they ARE), not one subsuming the other.

**Notes:** Recommendation **create new (false positive)**. Surfaced per DD-97's loose calibration rather than silently drafting a second deterministic-execution rule without flagging the family. If Nick concurs, re-invoke `/extract-artifacts --harvest-row planner-executor-deterministic-guardrails::rule::deterministic-execution-boundary-rule` to write the new rule. Per DD-97 v1 no artifact is created or modified here.

### stateful-mcp-subprocess-vs-cli-shell-out

**Form:** rule
**Existing artifact (primary match):** [[prefer-cli-over-mcp-when-both-exist-for-the-same-tool]]
**Secondary matches:** (none)

**Codifier recommendation:** extend existing

**Why this match:** The candidate is a self-declared boundary condition on this exact rule. Its source finding's `implementation_notes` name `prefer-cli-over-mcp-when-both-exist` explicitly and flag "Candidate refinement for the extracted rule's applicability clause — flag to the Codifier," and its `related_findings` records an `extends` edge to the rule's own source finding (`cli-first-tool-integration-less-overhead-than-mcp`). Both artifacts govern the identical decision — CLI vs. MCP for a tool exposing both — and the candidate supplies the discriminator the existing rule currently leaves implicit. The existing rule's Strong evidence came entirely from *stateless* tools (Playwright), where the CLI shares the terminal environment natively and amortizes nothing across calls; the candidate demonstrates the same trade with the opposite winner when the tool holds *session state* (an open database, a warm engine): there a long-lived local stdio MCP subprocess amortizes process startup + connection open/close + typed schemas across the session and wins. Same trade, opposite winner, one discriminator (statefulness) — a textbook applicability-clause refinement, not a disjoint rule.

**Diff sketch:**

Proposed as (a) a scoping amendment to the existing rule's **Boundary**/**Condition** section adding statefulness as an explicit applicability discriminator, plus (b) a new "Special Case: Stateful Local Services" section parallel to the rule's existing failure-mode/exception structure — rather than a bare Evidence-row append, since the candidate introduces a genuine carve-out (a class of tools where the default *flips*), not just corroborating evidence for the existing claim:

> **Special Case: Stateful Local Services (the statefulness discriminator)**
>
> The CLI-first default is scoped to *stateless* tools — where each invocation shares the terminal environment natively and amortizes nothing across calls, so the CLI's zero protocol overhead wins (Playwright is the canonical case). When the tool holds session state worth keeping open — an open database, a warm index, a long-lived engine — the winner flips: a long-lived local stdio MCP subprocess (spawned once, tokenless, session-scoped, dying with the session) beats per-call CLI shell-out, because it amortizes process startup + connection open/close + typed tool schemas across the whole session and removes one shell-approval surface per command. Discriminator checklist for a tool-integration review: does the tool open a connection/database/index per call? Is there a session-scoped `serve` mode? If yes, prefer the local MCP subprocess for that tool; the CLI-first default does not apply. (Two documented costs to watch: a long-lived subprocess can hold stale state after the underlying store changes externally — it needs reload semantics — and session-scoped servers can register tool-count bloat that taxes the context window.)
>
> **Source:** [[stateful-mcp-subprocess-vs-cli-shell-out]] (Medium / practitioner-documented — Gbrain's ~47 engine operations exposed both ways; CLI shell-out "works, but is worse as a process," the local MCP path visibly faster in Hermes Agent).

The existing rule's core invariant (CLI is the default when both interfaces exist) is not overturned — it is *scoped*: its Condition/`applies_to` gains a statefulness qualifier ("...for stateless tools; stateful local services with a session-scoped serve mode are the documented exception"), and the Scope line "Does not apply when the tool has no CLI equivalent, or when the CLI lacks a capability required for the specific task" gains a third clause: "...or when the tool holds session state worth keeping open (open DB, warm engine), where a long-lived local MCP subprocess is preferred."

**Notes:** Recommendation **extend existing** — the candidate does not answer a different question or use a different mechanism; it refines the applicability clause of the very rule it cites, adding the statefulness discriminator the existing (stateless-derived) evidence base left implicit. The Codifier's harvest-queue reading concurs ("amending the existing rule artifact, not creating a twin"). If Nick concurs, apply the diff sketch above by hand (or via a future skill mode) to `prefer-cli-over-mcp-when-both-exist-for-the-same-tool.md`, then flip the harvest-queue row's Status to `extracted` and Resolution to `merged into [[prefer-cli-over-mcp-when-both-exist-for-the-same-tool]]`. Per DD-97 v1 no artifact is created or modified here.

### static-tool-set-mode-changes-as-callable-tools

**Form:** rule
**Existing artifact (primary match):** [[never-mutate-cached-prompt-prefix]]
**Secondary matches:** (none)

**Codifier recommendation:** extend existing

**Why this match:** Both rules govern the same prefix-caching mechanic and, read together, share an invariant almost word-for-word: `never-mutate-cached-prompt-prefix`'s existing invariant states "Tool definitions and their ordering are stable within a session" and its Action forbids "Reordering or redefining tools within a session" — that rule's Rationale explicitly names "static tool sets" as one of the "special cases of 'never touch the prefix'" it is the parent rule for. The candidate's first implementation point ("declare the full tool set once at session start and keep it static") is the same claim, not merely adjacent to it. The candidate's added content — points (2) and (3): express mode as a callable transition tool plus behavioral instructions with enforcement in the harness/permission layer, and let the model call the transition tool itself — is genuinely new and not covered by the existing rule's body, but it is a specific *mechanism* for satisfying the existing rule's static-toolset invariant during a mode change, not a competing or disjoint concern. The existing rule already carries exactly this kind of addition once before: its "Special Case: Byte-Stable Disclosure Catalogs" section was itself merged in via a prior DD-97 extension (session 146, from `cache-stable-progressive-disclosure-catalog`), establishing this file as the live home for prefix-stability special cases.

**Diff sketch:**

Proposed as a new "Special Case: Mode as Callable Transition Tool" section on `never-mutate-cached-prompt-prefix.md`, parallel in shape to the existing "Special Case: Byte-Stable Disclosure Catalogs" section, rather than a bare Evidence-row append (the candidate's mode-as-tool mechanism needs a few lines of "how," not just a citation):

> **Special Case: Mode as Callable Transition Tool**
>
> A mode-bearing agent (plan vs. execute, read-only vs. write, teacher vs. builder) is a second concrete instance of the "tool defs are stable within a session" invariant, with its own tempting violation: swapping in a restricted toolset when the mode changes. Don't. Model the mode itself as two always-present, callable tools (e.g., `EnterPlanMode` / `ExitPlanMode`) plus a system message describing the mode's constraints; the tool surface never changes, and enforcement of what the mode does/doesn't allow lives in the harness or permission layer — never in tool absence. This also lets the model enter a mode autonomously, since the transition is just another tool call.
>
> **Source:** [[static-tool-set-mode-changes-as-callable-tools]] (Strong / production-tested, first-party — Claude Code's Plan Mode; independently cross-harness-corroborated by opencode's `plan_enter`/`plan_exit` tools, though opencode diverges by shrinking the visible toolset per mode rather than keeping it static).

Body wording elsewhere on the existing rule is unchanged; the Contract (preconditions/invariants/governance/recovery) is unchanged — the new content elaborates the existing "tool definitions... stable within a session" invariant rather than adding a new one. `applies_to` in the existing rule's `context` could optionally gain "agent or skill designs that implement mode switching (plan/execute, read-only/write) via tool-surface changes" — a call for whoever applies the merge, not prescribed here.

**Notes:** Recommendation **extend existing**, not create-new — unlike the sibling proposal above, this candidate does not answer a different question with a different mechanism; it answers the *same* question (keep the tool surface static) with an implementation detail (mode-as-callable-tool) the existing rule's body doesn't yet spell out, for a use case (mode toggles) the existing rule's Condition already lists as an example of state that must travel via the append channel. If Nick concurs, apply the diff sketch above by hand (or via a future skill mode) to `never-mutate-cached-prompt-prefix.md`, then flip the harvest-queue row's Status to `extracted` and Resolution to `merged into [[never-mutate-cached-prompt-prefix]]`. Per DD-97 v1 no artifact is created or modified here.
