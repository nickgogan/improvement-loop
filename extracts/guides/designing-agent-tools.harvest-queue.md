# Co-occurrence Harvest Queue — Designing Agent Tools

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-05-24 | extracted | rule | [[tool-call-event-interception-pattern]] | Mutation interceptors own their output validity | merged into [[hook-based-enforcement-for-agent-outputs]] |
| 2026-05-24 | nick-dismissed | rule | [[skills-lock-portable-agent-skills]] | Verify skill lock before diagnosing agent behavior | dismiss as inline |
| 2026-05-25 | extracted | rule | [[cli-first-tool-integration-less-overhead-than-mcp]] | "Prefer CLI over MCP when both exist for the same tool" | extracted to [[prefer-cli-over-mcp-when-both-exist-for-the-same-tool]] |
| 2026-05-25 | extracted | template | [[html-pr-explainer-with-margin-annotations]] | "HTML PR Explainer with margin annotations and severity colors" | extracted to [[html-pr-explainer-with-margin-annotations]] |
| 2026-05-25 | extracted | template | [[skills-portability-across-sdk-and-framework-boundaries]] | "Framework skill integration pattern (scan-catalog-inject-load)" | extracted to [[framework-skill-integration-pattern]] |
| 2026-05-25 | extracted | rule | [[skills-inside-workspace-contextual-skill]] | "Scope skills to workspace routing tables, never globally load" | extracted to [[scope-skills-to-workspace-routing-tables]] |

## Per-row details

### tool-call-event-interception-pattern::rule::mutation-interceptors-own-output-validity

- **Date queued:** 2026-05-24
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[tool-call-event-interception-pattern]]
- **Source excerpt:**
  > "No re-validation after mutation. Enables policy enforcement, argument transformation, conditional blocking without modifying the tool itself. Risks: no re-validation means extensions can produce invalid arguments."
- **Codifier's reading:** The no-re-validation constraint is a cross-cutting safety invariant that applies to any middleware pattern in any harness — not just the Pi agent implementation. As a standalone rule it could be referenced from tool design, safety, and middleware contexts without duplicating the guide. The failure mode (silent invalid args downstream) is distinct enough from poka-yoke principles to warrant its own rule entry.
- **Suggested headline:** Mutation interceptors own their output validity — schema re-validation does not run after argument mutation
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[hook-based-enforcement-for-agent-outputs]]

Pending merge 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — DD-97 extension proposal emitted at [[operations/extension-proposals/2026-05-25-extension-proposals]]; primary match [[hook-based-enforcement-for-agent-outputs]]. Manual apply per DD-97 v1 (Step 1.7 auto-merge prohibition); after apply, row Status flips to extracted and Resolution to merged into [[hook-based-enforcement-for-agent-outputs]] via manual queue edit (or future skill mode).

Merged 2026-05-25 — Session 103 — [[session-103-codifier-complete-extract-artifacts-write-phase]] — into [[hook-based-enforcement-for-agent-outputs]].

---

### cli-first-tool-integration-less-overhead-than-mcp::rule::prefer-cli-over-mcp

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[cli-first-tool-integration-less-overhead-than-mcp]]
- **Source excerpt:**
  > "Playwright has both an MCP server and a CLI tool. Head-to-head test: the CLI version was faster and used ~90,000 fewer tokens than the MCP version. General principle: Claude Code lives in the terminal, CLIs live in the terminal — they share an environment natively. MCP servers require a separate process, a protocol layer, and additional initialization overhead."
- **Codifier's reading:** Clear imperative for tool integration decisions: when a tool exposes both CLI and MCP server interfaces, prefer CLI (lazy-loading, ~90K fewer tokens, shared environment). Machine-enforceable as a tool-selection audit: check whether registered MCP servers have CLI equivalents. The directive is independent of the broader lazy-vs-eager loading pattern.
- **Suggested headline:** prefer-cli-over-mcp
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[prefer-cli-over-mcp-when-both-exist-for-the-same-tool]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[prefer-cli-over-mcp-when-both-exist-for-the-same-tool]].

### html-pr-explainer-with-margin-annotations::template::html-pr-explainer

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[html-pr-explainer-with-margin-annotations]]
- **Source excerpt:**
  > "The HTML artifact renders the PR diff alongside: margin annotations explaining why specific changes were made, severity colors distinguishing critical changes from cosmetic ones, jump links for navigating between related changes across files."
- **Codifier's reading:** Structural scaffold for a review companion artifact: [diff section] + [margin annotation: why] + [severity color: critical/cosmetic] + [jump links: related changes]. Fill-in structure with clear slots. The template is distinct from the pattern (which is about format-as-governance); the template is the concrete structural form the output takes.
- **Suggested headline:** html-pr-explainer
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[html-pr-explainer-with-margin-annotations]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[html-pr-explainer-with-margin-annotations]].

### skills-portability-across-sdk-and-framework-boundaries::template::framework-skill-integration

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[skills-portability-across-sdk-and-framework-boundaries]]
- **Source excerpt:**
  > "The implementation pattern for frameworks: (1) scan the skills directory at startup to build a skill catalog, (2) inject skill names and descriptions into the system prompt dynamically, (3) provide a 'load skill' tool that reads the full SKILL.md content when the agent needs it, (4) the agent follows the skill's instructions to make API calls or execute workflows."
- **Codifier's reading:** A 4-step implementation scaffold for adding SKILL.md-based capabilities to any agent framework. Structural enough to be a fill-in template: scan directory → build catalog → inject into system prompt → provide load-tool. Independent of the portability argument — any framework implementer needs this scaffold regardless of whether they're migrating.
- **Suggested headline:** framework-skill-integration
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[framework-skill-integration-pattern]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[framework-skill-integration-pattern]].

### skills-inside-workspace-contextual-skill::rule::scope-skills-to-routing-tables

- **Date queued:** 2026-05-25
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[skills-inside-workspace-contextual-skill]]
- **Source excerpt:**
  > "Globally loaded skills create disambiguation problems at scale: with 15+ skills, the agent must reason about which skill applies to the current task, which adds latency and can cause incorrect skill selection. Contextual mapping eliminates this overhead by pre-specifying relevance."
- **Codifier's reading:** Imperative directive: "scope skills to workspace routing tables rather than globally loading all skills." Machine-enforceable: audit whether skills are contextually scoped or globally loaded; flag systems with >15 globally loaded skills. The rule stands independently of the broader workspace-routing pattern — it's a design constraint applicable to any skill system.
- **Suggested headline:** scope-skills-to-routing-tables
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[scope-skills-to-workspace-routing-tables]]

Extracted 2026-05-25 — Session 102 — [[session-102-codifier-identify-and-extract-artifacts]] — to [[scope-skills-to-workspace-routing-tables]].

### skills-lock-portable-agent-skills::rule::verify-skill-lock-before-diagnosing

- **Date queued:** 2026-05-24
- **Status:** nick-dismissed
- **Target form:** rule
- **Source finding:** [[skills-lock-portable-agent-skills]]
- **Source excerpt:**
  > "Lock staleness, project vs global resolution complexity, version conflicts."
- **Codifier's reading:** "Run verify before diagnosing" is an operational discipline rather than a design rule — it's a single sentence that is already fully expressed in the guide's Recovery section and the Audit Worksheet. No additional structure would be created by extracting it as a rule artifact. Low extraction value.
- **Suggested headline:** Verify installed skills against lock file before diagnosing agent behavior failures
- **Recommendation:** dismiss as inline
- **Resolution:** dismissed
