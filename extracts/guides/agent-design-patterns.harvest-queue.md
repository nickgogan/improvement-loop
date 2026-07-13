# Co-occurrence Harvest Queue — Agent Design Patterns

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

> Ruled 2026-07-13 (session 146) under Nick's delegated-judgment grant; per-row statuses set accordingly.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-13 | extracted | template | [[capability-as-agent-composition-primitive]] | "composition-unit-bundle-scaffold" | extracted to [[composition-unit-bundle-scaffold]] |
| 2026-07-13 | extracted | rule | [[disclosure-granularity-decision-rubric]] | "eager-prompt-whitelist" | extracted to [[eager-prompt-whitelist]] |
| 2026-07-13 | extracted | rule | [[cache-stable-progressive-disclosure-catalog]] | "byte-stable-disclosure-catalog" | merged into [[never-mutate-cached-prompt-prefix]] |

## Per-row details

### capability-as-agent-composition-primitive::template::composition-unit-bundle-scaffold

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[capability-as-agent-composition-primitive]]
- **Source excerpt:**
  > "A framework-level unit that packages everything one responsibility needs:
  > instructions (the system-prompt fragment for this responsibility),
  > tools / toolsets (including MCP servers),
  > lifecycle hooks (e.g., pre-tool-use, for deterministic security/guidance),
  > guardrails (input/output constraints),
  > model settings."
- **Codifier's reading:** The bundle enumeration is a structural scaffold with named slots (instructions / tools / hooks / guardrails / settings) meant for rendering per responsibility — template shape per the form rubric. The 2026-07-13 identification report independently flagged this template co-occurrence.
- **Suggested headline:** composition-unit-bundle-scaffold
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[composition-unit-bundle-scaffold]]

Extracted 2026-07-13 — Session 146 — [[agent-design-patterns.harvest-queue]] — to [[composition-unit-bundle-scaffold]].

### disclosure-granularity-decision-rubric::rule::eager-prompt-whitelist

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[disclosure-granularity-decision-rubric]]
- **Source excerpt:**
  > "Eager-prompt whitelist — the always-loaded prompt is bounded to identity, task
  > boundaries, global safety, and routing. Everything else earns eager status or loads
  > on demand."
- **Codifier's reading:** A closed positive-space boundary ("eager content must be one of four categories") — machine-checkable and lintable; the finding itself proposes lint integration. Rule shape per the form rubric's deterministic-enforceable criterion.
- **Suggested headline:** eager-prompt-whitelist
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[eager-prompt-whitelist]]
### cache-stable-progressive-disclosure-catalog::rule::byte-stable-disclosure-catalog

- **Date queued:** 2026-07-13
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[cache-stable-progressive-disclosure-catalog]]
- **Source excerpt:**
  > "keep that catalog byte-identical every turn — even re-listing items already loaded —
  > so the provider's prompt cache never breaks; it is cheaper to bounce an occasional
  > redundant load than to bust the cache on every load."
- **Codifier's reading:** Imperative directive with a byte-equality check ("catalog rendering must be byte-identical across turns") — deterministic and enforceable on any always-injected catalog surface. Rule shape; the pattern rationale stays in the finding/guide.
- **Suggested headline:** byte-stable-disclosure-catalog
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** merged into [[never-mutate-cached-prompt-prefix]]
Merge applied 2026-07-13 (session 146, delegated-judgment grant): DD-97 extension ruled `extend existing` per the DD's extension-first thesis and the Codifier's primary recommendation; the byte-stable-catalog tactic is now a Special Case section on [[never-mutate-cached-prompt-prefix]]. Nick may override to a standalone catalog-scoped rule if he prefers finer granularity — two-way door.
