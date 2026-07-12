# Co-occurrence Harvest Queue — Agent Architecture Decisions

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-05-24 | extracted | template | [[oz-multi-agent-room-model]] | Room Charter Template | extracted to [[room-charter-template]] |
| 2026-05-24 | extracted | template | [[agui-human-control-layer-not-ui]] | AGUI Boundary Control-Points Specification | extracted to [[agui-boundary-control-points-specification]] |
| 2026-05-25 | extracted | rule | [[orchestrated-execution-one-task-per-sub-agent-wit]] | "Verify sub-agent wiring after each wave" | extracted to [[verify-sub-agent-wiring-after-each-wave]] |
| 2026-05-25 | extracted | rule | [[subagent-as-uniform-tool-interface]] | "Sub-agent dispatch as uniform tool entry" | extracted to [[sub-agent-dispatch-as-uniform-tool-entry]] |
| 2026-05-25 | extracted | template | [[four-zone-agent-architecture-framework]] | "Four-zone agent specification template" | extracted to [[four-zone-agent-specification-template]] |
| 2026-05-25 | extracted | skill | [[review-triggered-remediation-dispatch]] | "Review-triggered remediation chain" | extracted to [[review-triggered-remediation-chain]] |

## Per-row details

### oz-multi-agent-room-model::template::room-charter-template

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[oz-multi-agent-room-model]]
- **Source excerpt:**
  > "Agents assigned to rooms communicate via @mentions over SSE, self-manage per-room kanban tasks, and produce typed artifacts (PRs, plans, docs). Human observers see real-time agent work. Room is the coordination boundary."
- **Codifier's reading:** The room model introduces a structured unit of multi-agent coordination with enough recurring components (scope declaration, agent roster, artifact type registry, SSE channel config, human observer access, kanban initialization) to warrant a reusable template. Without a charter, rooms will be defined ad hoc and risk scope creep into Pattern D dynamics. The template would operationalize "room scope defined by task characteristics" — the core invariant added to the guide.
- **Suggested headline:** Room Charter Template — define scope, agents, artifact types, and human observer access for a bounded-context coordination room
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[room-charter-template]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[room-charter-template]].

---

### agui-human-control-layer-not-ui::template::agui-boundary-control-points-specification

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[agui-human-control-layer-not-ui]]
- **Source excerpt:**
  > "Actual function is encoding control points at which a human must observe, approve, edit, or cancel running agent work. Teams without this layer accumulate 'supervision debt.' The design question is 'which steps require human approval?' not 'how do we render the output?'"
- **Codifier's reading:** The `human_control_points` contract field introduced into the guide's boundary contract table needs a filling specification: how to enumerate each agent step, classify it as observe/approve/cancel, and record the rationale. This is mechanical enough and recurring enough (every multi-agent boundary contract should have it) to be a standalone template rather than an inline note. The guide references it but does not draft it — the template would close that gap.
- **Suggested headline:** AGUI Boundary Control-Points Specification — enumerate agent steps as observe / approve-before-proceed / cancellable with rationale
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[agui-boundary-control-points-specification]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[agui-boundary-control-points-specification]].

---

### orchestrated-execution-one-task-per-sub-agent-wit::rule::verify-wiring-after-waves

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[orchestrated-execution-one-task-per-sub-agent-wit]]
- **Source excerpt:**
  > "After each wave of sub-agents completes, the developer verifies that each sub-agent's implementation was actually wired into the main application — a critical step because sub-agents frequently complete their building task but fail to integrate their output with the rest of the codebase, leaving 'islands' of unreachable code."
- **Codifier's reading:** Imperative directive ("verify after each wave") that is machine-enforceable (automated connectivity checks from application entry point). The rule form is appropriate because this is a binary-testable constraint applicable to any wave-based sub-agent workflow, not just the source framework. The pattern form captures the broader orchestration approach; the rule captures the specific enforcement.
- **Suggested headline:** verify-wiring-after-waves
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[verify-sub-agent-wiring-after-each-wave]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[verify-sub-agent-wiring-after-each-wave]].

---

### subagent-as-uniform-tool-interface::rule::sub-agent-dispatch-as-tool

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[subagent-as-uniform-tool-interface]]
- **Source excerpt:**
  > "Sub-agent dispatch is implemented as a standard tool in the tool registry ('agent tool'), called identically to bash, file-read, or web-search. The orchestrator does not have special-case logic for delegation — spawning a sub-agent follows the same call/result/checkpoint path as any other tool."
- **Codifier's reading:** Imperative design constraint ("implement as standard tool entry"; "no special-case logic") that is binary-testable (does the tool registry enumerate sub-agent dispatch alongside other tools, or does delegation use a separate API?). Applies to any system building sub-agent orchestration. The rule would enforce interface homogeneity as a structural invariant.
- **Suggested headline:** sub-agent-dispatch-as-tool
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[sub-agent-dispatch-as-uniform-tool-entry]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[sub-agent-dispatch-as-uniform-tool-entry]].

---

### four-zone-agent-architecture-framework::template::four-zone-spec

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[four-zone-agent-architecture-framework]]
- **Source excerpt:**
  > "A formal spec template that covers all four zones per agent would make the architecture reproducible. Monitoring tools that visualize live state per zone would aid debugging."
  > Four zones: (1) Trigger — the event that initiates the agent. (2) Context — everything injected into the model's context window. (3) Tools — capabilities for reading/writing external systems. (4) Output/Memory — where work persists between turns.
- **Codifier's reading:** The finding explicitly calls for "a formal spec template that covers all four zones per agent." The guide's Architecture Decision Record template includes a Four-Zone Audit table, but a standalone four-zone agent specification template — with per-zone fields, constraints, and debugging checklist — would be a reusable scaffold for specifying individual agents. Template form is appropriate: structural scaffold with placeholder fields.
- **Suggested headline:** four-zone-spec
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[four-zone-agent-specification-template]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[four-zone-agent-specification-template]].

---

### review-triggered-remediation-dispatch::skill::review-remediation-chain

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** skill
- **Source finding:** [[review-triggered-remediation-dispatch]]
- **Source excerpt:**
  > "The chain is: review -> classify severity -> dispatch fix agent per issue -> verify fix. ... The composition primitive is: review as trigger, not terminus. The review output (issue list with severity) becomes the dispatch queue for fix agents."
- **Codifier's reading:** Clear procedural structure with input (code or spec to review), output (fixed code + remediation report), and step-by-step invocation (review → classify → dispatch → verify). Matches skill form: procedure with input/output contract. The existing `/gsd-code-review-fix` skill already implements this pattern — recommend merge rather than standalone extraction.
- **Suggested headline:** review-remediation-chain
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[review-triggered-remediation-chain]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[review-triggered-remediation-chain]].
