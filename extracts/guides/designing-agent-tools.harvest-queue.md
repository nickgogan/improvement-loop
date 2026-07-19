# Co-occurrence Harvest Queue — Designing Agent Tools

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | extracted | rule | [[static-tool-set-mode-changes-as-callable-tools]] | "tool-surface-session-static-modes-as-tools" | merged into [[never-mutate-cached-prompt-prefix]] |
| 2026-07-16 | extracted | rule | [[monitor-vs-loop-event-driven-vs-time-driven]] | "default-event-driven-watching-over-time-polling" | extracted to [[default-event-driven-watching-over-time-based-polling]] |
| 2026-07-16 | extracted | rule | [[stateful-mcp-subprocess-vs-cli-shell-out]] | "statefulness-boundary-on-cli-first-rule" | merged into [[prefer-cli-over-mcp-when-both-exist-for-the-same-tool]] |
| 2026-07-16 | extracted | rule | [[tiered-capability-registry-engine-behavior-branching]] | "declare-capabilities-as-tiers-not-booleans" | extracted to [[declare-capabilities-as-tiers-not-booleans]] |
| 2026-07-16 | extracted | rule | [[skill-cross-surface-portability-with-constraints]] | "declare-skill-compatibility-design-for-most-restricted-surface" | extracted to [[declare-skill-compatibility-design-for-most-restricted-surface]] |
| 2026-07-16 | extracted | rule | [[code-as-deterministic-tool-inside-skills]] | "reference-bundled-scripts-via-claude-skill-dir" | extracted to [[reference-bundled-scripts-via-claude-skill-dir]] |

## Per-row details

### static-tool-set-mode-changes-as-callable-tools::rule::tool-surface-session-static-modes-as-tools

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[static-tool-set-mode-changes-as-callable-tools]]
- **Source excerpt:**
  > "For us this is a design rule for any mode-bearing agent: represent modes as state the model toggles via tools, not as different tool surfaces. … (1) declare the full tool set once at session start and keep it static; (2) express mode as a callable transition tool plus behavioral instructions, with enforcement in the harness/permission layer rather than by hiding tools … Adopt as a rule in our agent/skill design substrate: 'tool surface is session-static; modes are tools + instructions'"
- **Codifier's reading:** The finding itself proposes adoption "as a rule in our agent/skill design substrate" — an imperative, machine-checkable directive (audit: does any skill/agent design swap toolsets per mode?). Clean rule-form fit per the form rubric.
- **Suggested headline:** tool-surface-session-static-modes-as-tools
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[never-mutate-cached-prompt-prefix]]

Merged 2026-07-19 — Session 152 — designing-agent-tools.harvest-queue — Nick-delegated DD-97 extend-existing ruling (concurring with the Codifier recommendation). Applied by hand per DD-97 v1 (Step 1.7 auto-merge prohibition): a new "Special Case: Mode as Callable Transition Tool" section was added to [[never-mutate-cached-prompt-prefix]] parallel to its byte-stable-catalog special case, and the rule's `applies_to` gained a mode-switching clause; source finding back-annotated (extraction_note + consumed_by). Proposal: [[operations/extension-proposals/2026-07-19-extension-proposals]].

### monitor-vs-loop-event-driven-vs-time-driven::rule::default-event-driven-watching-over-time-polling

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[monitor-vs-loop-event-driven-vs-time-driven]]
- **Source excerpt:**
  > "When choosing between Monitor and /loop for a background watching task, default to Monitor if the watched system emits observable output (logs, stdout, file events). Use /loop only when no event stream exists and you need time-based polling as a fallback."
- **Codifier's reading:** Implementation notes carry a crisp default-with-exception decision rule ("default to X if …; use Y only when …") — imperative and enforceable at design-review time. Rule form per the rubric's directive test.
- **Suggested headline:** default-event-driven-watching-over-time-polling
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[default-event-driven-watching-over-time-based-polling]]

Extracted 2026-07-19 — Session 152 — designing-agent-tools.harvest-queue — to [[default-event-driven-watching-over-time-based-polling]].

### stateful-mcp-subprocess-vs-cli-shell-out::rule::statefulness-boundary-on-cli-first-rule

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[stateful-mcp-subprocess-vs-cli-shell-out]]
- **Source excerpt:**
  > "The decision input is statefulness: stateless tool → CLI-first still holds; stateful local service (open DB, long-lived engine) → local stdio MCP subprocess. Candidate refinement for the extracted rule's applicability clause — flag to the Codifier."
- **Codifier's reading:** The finding explicitly flags itself as a refinement to the existing extracted rule's applicability clause. Rule-shaped boundary condition; the right disposition is amending the existing rule artifact, not creating a twin.
- **Suggested headline:** statefulness-boundary-on-cli-first-rule
- **Recommendation:** merge into existing [[prefer-cli-over-mcp-when-both-exist-for-the-same-tool]]
- **Resolution:** merged into [[prefer-cli-over-mcp-when-both-exist-for-the-same-tool]]

Merged 2026-07-19 — Session 152 — designing-agent-tools.harvest-queue — Nick-delegated DD-97 extend-existing ruling (concurring with the Codifier recommendation). Applied by hand per DD-97 v1 (Step 1.7 auto-merge prohibition): Scope/applies_to gained the statefulness qualifier + a third scope clause, and a new "Special Case: Stateful Local Services (the statefulness discriminator)" section was added to [[prefer-cli-over-mcp-when-both-exist-for-the-same-tool]]; source finding back-annotated (extraction_note + consumed_by). Proposal: [[operations/extension-proposals/2026-07-19-extension-proposals]].

### tiered-capability-registry-engine-behavior-branching::rule::declare-capabilities-as-tiers-not-booleans

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[tiered-capability-registry-engine-behavior-branching]]
- **Source excerpt:**
  > "capability claims should be tiered discriminated values with per-tier consumer behavior spelled out (enforce / verify-and-retry / refuse-or-degrade), not booleans."
- **Codifier's reading:** Implementation notes state an imperative constraint on registry design ("should be X, not Y") directly applicable to the engine's model-capability registry — checkable against any capability declaration. Rule form; a companion template (tiered declaration schema) now lives in the guide's Templates section.
- **Suggested headline:** declare-capabilities-as-tiers-not-booleans
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[declare-capabilities-as-tiers-not-booleans]]

Extracted 2026-07-19 — Session 152 — designing-agent-tools.harvest-queue — to [[declare-capabilities-as-tiers-not-booleans]].

### skill-cross-surface-portability-with-constraints::rule::declare-skill-compatibility-design-for-most-restricted-surface

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[skill-cross-surface-portability-with-constraints]]
- **Source excerpt:**
  > "the practical implication is to design for the most restricted target surface (typically the Claude API) and use the `compatibility` field to declare when a skill expects more. … Skills targeting one surface's capabilities may not work elsewhere — authors should test on target surfaces or use the compatibility frontmatter field to declare requirements."
- **Codifier's reading:** Two paired imperatives (design for most-restricted surface; declare extra requirements in `compatibility`) that are lintable against SKILL.md frontmatter — fits rule form's machine-enforceability criterion.
- **Suggested headline:** declare-skill-compatibility-design-for-most-restricted-surface
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[declare-skill-compatibility-design-for-most-restricted-surface]]

Extracted 2026-07-19 — Session 152 — designing-agent-tools.harvest-queue — to [[declare-skill-compatibility-design-for-most-restricted-surface]].

### code-as-deterministic-tool-inside-skills::rule::reference-bundled-scripts-via-claude-skill-dir

- **Date queued:** 2026-07-16
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[code-as-deterministic-tool-inside-skills]]
- **Source excerpt:**
  > "Use ${CLAUDE_SKILL_DIR} in Claude Code skills to reference bundled scripts portably regardless of CWD. … Without `${CLAUDE_SKILL_DIR}` (Claude Code) or equivalent, bundled script paths can be wrong when the skill runs from a project subdirectory. Hard-coding `scripts/foo.py` breaks across surfaces."
- **Codifier's reading:** Narrow imperative directive embedded in a pattern finding — grep-checkable across every SKILL.md that bundles scripts (flag hard-coded `scripts/` relative paths). Rule form; the broader script-bundling pattern stays in the guide body.
- **Suggested headline:** reference-bundled-scripts-via-claude-skill-dir
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[reference-bundled-scripts-via-claude-skill-dir]]

Extracted 2026-07-19 — Session 152 — designing-agent-tools.harvest-queue — to [[reference-bundled-scripts-via-claude-skill-dir]].
