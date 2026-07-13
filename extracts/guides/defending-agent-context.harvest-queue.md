# Co-occurrence Harvest Queue — Defending Against Context Degradation

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

> Ruled 2026-07-13 (session 146) under Nick's delegated-judgment grant; per-row statuses set accordingly.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-13 | extracted | skill | [[file-mediated-subagent-handoff-workspace]] | "sdd-handoff-workspace-scripts" | extracted to [[sdd-handoff-workspace-scripts]] |
| 2026-07-13 | extracted | rule | [[append-only-context-updates-system-reminder-injection]] | "never-mutate-cached-prompt-prefix" | extracted to [[never-mutate-cached-prompt-prefix]] |
| 2026-07-13 | nick-approved | template | [[append-only-context-updates-system-reminder-injection]] | "static-first-prompt-layering-stack" | extract via /extract-artifacts |
| 2026-07-13 | extracted | rule | [[derive-dont-edit-artifacts-as-log-renders]] | "derived-artifacts-single-writer-rule" | extracted to [[derived-artifacts-single-writer-rule]] |
| 2026-07-13 | extracted | skill | [[memory-file-to-skill-migration]] | "memory-file-to-skill-migration-pass" | extracted to [[memory-file-to-skill-migration-pass]] |
| 2026-07-13 | extracted | rule | [[skill-pruning-failure-modes-noop-deletion-test]] | "deletion-test-for-no-op-instructions" | extracted to [[deletion-test-for-no-op-instructions]] |

## Per-row details

### file-mediated-subagent-handoff-workspace::skill::sdd-handoff-workspace-scripts

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** skill
- **Source finding:** [[file-mediated-subagent-handoff-workspace]]
- **Source excerpt:**
  > "Scripts write the files, dispatches carry paths. `task-brief PLAN N` extracts
  > task N into `task-N-brief.md` (no subagent ever reads the whole plan);
  > `review-package BASE HEAD` emits commit list + stat + `-U10` diff readable in one
  > call. A dispatch prompt is one line of scene-setting, the brief path ... and the
  > report-file path + contract."
- **Codifier's reading:** Procedures with defined inputs/outputs and an invocation contract (task-brief PLAN N; review-package BASE HEAD) — ordered, callable, stateless steps instantiating the pattern; matches the form rubric's skill criteria. Flagged as skill co-occurrence in the 2026-07-13 identification report.
- **Suggested headline:** sdd-handoff-workspace-scripts
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[sdd-handoff-workspace-scripts]]
### append-only-context-updates-system-reminder-injection::rule::never-mutate-cached-prompt-prefix

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[append-only-context-updates-system-reminder-injection]]
- **Source excerpt:**
  > "the prompt prefix — system prompt, tool definitions, CLAUDE.md, session context —
  > is append-only. When information in it goes stale ... the harness does not rewrite
  > the prefix; it injects a `<system-reminder>` block into a subsequent user message
  > or tool result carrying the updated fact."
- **Codifier's reading:** Imperative directive ("never mutate the prefix; append instead") with a machine-checkable boundary — prefix byte-identity across turns is lintable. Rule-shaped per the form rubric's deterministic-enforceability criterion.
- **Suggested headline:** never-mutate-cached-prompt-prefix
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[never-mutate-cached-prompt-prefix]]
### append-only-context-updates-system-reminder-injection::template::static-first-prompt-layering-stack

- **Date queued:** 2026-07-13
- **Status:** nick-approved
- **Target form:** template
- **Source finding:** [[append-only-context-updates-system-reminder-injection]]
- **Source excerpt:**
  > "1. Static system prompt & tool definitions — cached globally, across sessions
  > 2. CLAUDE.md — cached per project
  > 3. Session context — cached per session
  > 4. Conversation messages — grows turn by turn"
- **Codifier's reading:** A structural scaffold meant for rendering — a fixed four-layer ordering with named slots for harness/subagent prompt assembly. The finding itself proposes codifying it as a template ("Codify the four-layer static-first stack as a template for our subagent prompt assembly").
- **Suggested headline:** static-first-prompt-layering-stack
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**
- Pending version-bump 2026-07-13 — Session 146 — [[defending-agent-context.harvest-queue]] — DD-100 version-bump proposal emitted at [[operations/version-bump-proposals/2026-07-13-version-bump-proposals]]; primary match [[seven-layer-prompt-assembly-with-cache-control]] (current version v1); proposed filename `seven-layer-prompt-assembly-with-cache-control-v2.md`. On Nick ruling: re-invoke `/extract-artifacts --harvest-row append-only-context-updates-system-reminder-injection::template::static-first-prompt-layering-stack` AFTER updating the existing template (or with the proposal applied as instruction) — Step 1.8 Branch A match-disambiguation then routes to the version-bump write path; row Status flips to `extracted` and Resolution to `version-bumped to [[seven-layer-prompt-assembly-with-cache-control-v2]]` post-write.

### derive-dont-edit-artifacts-as-log-renders::rule::derived-artifacts-single-writer-rule

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[derive-dont-edit-artifacts-as-log-renders]]
- **Source excerpt:**
  > "A write-discipline rule pair over shared artifacts: 1. Artifacts are derived, not
  > edited. ... 'SPEC.md … DERIVED from .memlog.md, never hand-edited.' A hand-edit is
  > not merged — it is overwritten on the next derive. 2. One writer per artifact."
- **Codifier's reading:** The finding's own body names it "a write-discipline rule pair" — imperative, binary-testable (was the artifact written by its single writer? was it hand-edited?), enforceable structurally via overwrite-on-derive.
- **Suggested headline:** derived-artifacts-single-writer-rule
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[derived-artifacts-single-writer-rule]]
- Extracted 2026-07-13 — Session 146 — [[defending-agent-context.harvest-queue]] — to [[derived-artifacts-single-writer-rule]]. DD-97 corpus scan of `extracts/rules/` found no match (the `append-only-no-edit-delete-log-invariant` rule governs the log's own immutability; this rule governs derived-artifact write discipline + single-writer — distinct, complementary claims), so drafted as a new rule. Canonical extraction of a cross-guide duplicate: the twin `one-writer-per-artifact-derive-dont-edit` (session-persistence-and-memory.harvest-queue) is to be merged into this artifact by a later agent per DD-97; both directives (derive-don't-edit AND one-writer-per-artifact) are already captured here.

### memory-file-to-skill-migration::skill::memory-file-to-skill-migration-pass

- **Date queued:** 2026-07-13
- **Status:** nick-approved
- **Target form:** skill
- **Source finding:** [[memory-file-to-skill-migration]]
- **Source excerpt:**
  > "periodically migrate conditionally-useful sections (e.g., end-to-end testing
  > instructions, only needed when the agent changes code) out of the memory file into
  > skills ... The agent performs the migration itself ('extract the E2E testing
  > instructions from AGENTS.md into a project-level skill')."
- **Codifier's reading:** An ordered, delegable procedure with input (memory-file section failing the always-loaded test), output (new skill + slimmed memory file), and a review step — skill-shaped per the rubric. Complements the engine's /simplify-context, per the finding's implementation notes.
- **Suggested headline:** memory-file-to-skill-migration-pass
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[memory-file-to-skill-migration-pass]]
- Extracted 2026-07-13 — Session 146 — [[defending-agent-context.harvest-queue]] — to [[memory-file-to-skill-migration-pass]]. DD-97 corpus scan of `extracts/skills/` found no match.

### skill-pruning-failure-modes-noop-deletion-test::rule::deletion-test-for-no-op-instructions

- **Date queued:** 2026-07-13
- **Status:** nick-approved
- **Target form:** rule
- **Source finding:** [[skill-pruning-failure-modes-noop-deletion-test]]
- **Source excerpt:**
  > "Detection is the deletion test: delete the paragraph mentally (or actually) and
  > ask whether behavior would change. 'Write a long detailed commit message' fails
  > the test — the agent does that anyway from priors."
- **Codifier's reading:** A binary-testable audit check ("would behavior change if deleted? if not, remove") applicable per-paragraph to any context artifact — rule-shaped; the finding's implementation notes already flag it as an /assess-skill pruning axis. Caveat for the gate: safety text can false-positive as a no-op.
- **Suggested headline:** deletion-test-for-no-op-instructions
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[deletion-test-for-no-op-instructions]]
- Extracted 2026-07-13 — Session 146 — [[defending-agent-context.harvest-queue]] — to [[deletion-test-for-no-op-instructions]]. DD-97 corpus scan of `extracts/rules/` found no match (the `claudemd-minimum-viable-rule` is an authorship-side global-truth gate on additions; the deletion test is a distinct audit-side no-op-detection primitive).
