# Co-occurrence Harvest Queue — Agent Design Patterns

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

> Ruled 2026-07-13 (session 146) under Nick's delegated-judgment grant; per-row statuses set accordingly.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-13 | extracted | template | [[capability-as-agent-composition-primitive]] | "composition-unit-bundle-scaffold" | extracted to [[composition-unit-bundle-scaffold]] |
| 2026-07-13 | extracted | rule | [[disclosure-granularity-decision-rubric]] | "eager-prompt-whitelist" | extracted to [[eager-prompt-whitelist]] |
| 2026-07-13 | extracted | rule | [[cache-stable-progressive-disclosure-catalog]] | "byte-stable-disclosure-catalog" | merged into [[never-mutate-cached-prompt-prefix]] |
| 2026-07-19 | extracted | template | [[agent-as-folder-compiled-to-manifest]] | "agent-folder-skeleton" | extracted to [[agent-folder-skeleton]] |
| 2026-07-19 | extracted | template | [[oracle-evaluator-architect-domain-expert-progression]] | "domain-expert-mode-selection-tree" | extracted to [[domain-expert-mode-selection-tree]] |
| 2026-07-19 | extracted | rule | [[principal-domain-expert-single-ownership]] | "name-single-principal-domain-expert" | extracted to [[name-single-principal-domain-expert]] |

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

### agent-as-folder-compiled-to-manifest::template::agent-folder-skeleton

- **Date queued:** 2026-07-19
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[agent-as-folder-compiled-to-manifest]]
- **Source excerpt:**
  > "structures an entire AI agent as one parent folder containing a fixed set of named
  > subfolders, each holding one primitive: instructions ... skills ... tools ... sandbox
  > ... channels ... connections ... sub-agents ... schedules. The minimum viable agent is
  > just agent.ts specifying a model ...; every other folder is optional and additive."
- **Codifier's reading:** A fixed named-subfolder taxonomy with a required-vs-optional slot structure is a structural scaffold meant for rendering per agent — template shape per the form rubric. The guide already embeds an "Agent Folder Skeleton" template synthesized from this; a standalone extract would carry the safeguard checklist (manifest-inspect + drift check) with it.
- **Suggested headline:** agent-folder-skeleton
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[agent-folder-skeleton]]

Extracted 2026-07-19 — Session 152 — [[agent-design-patterns.harvest-queue]] — to [[agent-folder-skeleton]].

### oracle-evaluator-architect-domain-expert-progression::template::domain-expert-mode-selection-tree

- **Date queued:** 2026-07-19
- **Status:** extracted
- **Target form:** template
- **Source finding:** [[oracle-evaluator-architect-domain-expert-progression]]
- **Source excerpt:**
  > "The decision tree, asked in order: Can AI quality here be measured in objective
  > metrics, or is it fundamentally a taste call? If not measurable → Oracle. ... If
  > measurable: is manual iteration still fast enough? If yes → Evaluator ... If ... can't
  > keep up → progress to Architect."
- **Codifier's reading:** An ordered decision tree with fixed branch labels and mode outputs is a fillable decision-rubric scaffold — template shape per the form rubric. Embedded in the guide as the Mode-Selection Worksheet; separable as a standalone mode-selection decision template.
- **Suggested headline:** domain-expert-mode-selection-tree
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[domain-expert-mode-selection-tree]]

Extracted 2026-07-19 — Session 152 — [[agent-design-patterns.harvest-queue]] — to [[domain-expert-mode-selection-tree]].

### principal-domain-expert-single-ownership::rule::name-single-principal-domain-expert

- **Date queued:** 2026-07-19
- **Status:** extracted
- **Target form:** rule
- **Source finding:** [[principal-domain-expert-single-ownership]]
- **Source excerpt:**
  > "Name a principal domain expert. A single individual is ultimately accountable for
  > AI-quality decisions and empowered to make the call. This explicitly avoids consensus
  > by committee ... Give them ownership, not an advisory seat."
- **Codifier's reading:** Imperative directives ("name a single owner", "not an advisory seat") read as rule shape. Enforceability is organizational/checklist-grade, not machine-lintable — Nick may prefer this stays inline as guide guidance (Step 20); queued for his ruling per DD-101 loose calibration.
- **Suggested headline:** name-single-principal-domain-expert
- **Recommendation:** extract via /extract-artifacts
- **Resolution:** extracted to [[name-single-principal-domain-expert]]

Extracted 2026-07-19 — Session 152 — [[agent-design-patterns.harvest-queue]] — to [[name-single-principal-domain-expert]].
