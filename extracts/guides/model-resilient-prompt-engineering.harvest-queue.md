# Co-occurrence Harvest Queue — Model-Resilient Prompt Engineering

Embedded artifact candidates surfaced during `/synthesize-guide` runs. Per DD-101.
Nothing here is auto-extracted; rows feed `/extract-artifacts` only after Nick rules.

| Date queued | Status | Target form | Source finding | Suggested headline | Recommendation |
|---|---|---|---|---|---|
| 2026-07-16 | queued | rule | [[mandatory-explicit-model-per-dispatch]] | "explicit-model-per-subagent-dispatch" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[no-mid-session-model-switching-subagent-handoff]] | "pin-model-per-session-delegate-instead" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[dev-cost-estimation-bias-correction]] | "discount-dev-cost-in-design-decisions" | extract via /extract-artifacts |
| 2026-07-16 | queued | rule | [[seven-rung-minimal-code-decision-ladder]] | "reuse-before-write-decision-ladder" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[skill-description-structure-what-when-capabilities]] | "skill-description-three-part-template" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[strictness-escalation-skill-architecture]] | "strict-mode-review-skill-overlay" | extract via /extract-artifacts |
| 2026-07-16 | queued | template | [[hands-off-routine-prompt-precision-pattern]] | "unattended-routine-prompt-sop-checklist" | dismiss as inline |

## Per-row details

### mandatory-explicit-model-per-dispatch::rule::explicit-model-per-subagent-dispatch

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[mandatory-explicit-model-per-dispatch]]
- **Source excerpt:**
  > "**The rule.** Every subagent dispatch MUST name a model. The failure it targets is silent inheritance: an unspecified model defaults to the session's model — usually the most expensive — and nothing surfaces the cost until the bill. Observed incident: all 26 reviewers in one run on the top tier."
- **Codifier's reading:** Imperative, machine-enforceable directive ("every dispatch MUST name a model") with a checkable property (model field present + tier distribution auditable). Clean rule-form fit per the form rubric; the finding itself frames it as a dispatch-time governance rule. Directly applicable to the engine's own fan-outs (see the session-146 fan-out model-class ruling).
- **Suggested headline:** explicit-model-per-subagent-dispatch
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### no-mid-session-model-switching-subagent-handoff::rule::pin-model-per-session-delegate-instead

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[no-mid-session-model-switching-subagent-handoff]]
- **Source excerpt:**
  > "The Claude Code team's rule: keep the session on one model and delegate cheap subtasks to a subagent on the cheaper model via an explicit hand-off message. For us this is a hard constraint on skill-to-model coupling — model choice is a session-boundary decision, not a mid-session dial."
- **Codifier's reading:** Never-X-do-Y-instead directive, enforceable at design-review time ("any skill that suggests changing model mid-run gets flagged" — the finding proposes exactly this design-time check). Rule form per the rubric's imperative test; implementation notes already name the target surfaces (skill/agent design templates, /design-agent variant B).
- **Suggested headline:** pin-model-per-session-delegate-instead
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### dev-cost-estimation-bias-correction::rule::discount-dev-cost-in-design-decisions

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[dev-cost-estimation-bias-correction]]
- **Source excerpt:**
  > "His correction is a one-line standing rule in the always-loaded global memory file: 'when making technical decisions, don't give too much weight to development cost.'"
- **Codifier's reading:** Literal one-line standing rule intended for always-loaded context — the artifact IS a rule by the source's own framing. The finding's implementation notes name it "directly adoptable as a candidate standing rule in the engine's CLAUDE.md / agent constitutions," with the Occam's-razor interaction caveat to carry into the artifact's applicability clause.
- **Suggested headline:** discount-dev-cost-in-design-decisions
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### seven-rung-minimal-code-decision-ladder::rule::reuse-before-write-decision-ladder

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** rule
- **Source finding:** [[seven-rung-minimal-code-decision-ladder]]
- **Source excerpt:**
  > "a fixed decision ladder the agent must climb before generating anything new. The Ponytail skill's seven checks, in order: (1) is this needed at all (YAGNI), (2) does it already exist in the codebase / can existing components be reused, (3) does a standard library cover it, (4) does a native platform feature cover it, (5) can an installed/installable dependency cover it, (6) can it be a one-line fix, (7) only then write minimal new code."
- **Codifier's reading:** Ordered pre-generation checklist with a mandatory-sequence directive ("must climb before generating") — rule-shaped and model-independent per the finding's own implementation notes ("a candidate rule for any engine surface that generates code"). The Ponytail plugin wrapper is skill-shaped, but the extractable core is the ladder itself.
- **Suggested headline:** reuse-before-write-decision-ladder
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### skill-description-structure-what-when-capabilities::template::skill-description-three-part-template

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[skill-description-structure-what-when-capabilities]]
- **Source excerpt:**
  > "A three-part structure prescribed by Anthropic's Complete Guide PDF for the skill `description` field: `[What it does] + [When to use it] + [Key capabilities]` … Validation constraints (also from the PDF): name kebab-case only, must match folder name, cannot contain reserved words `claude` or `anthropic`, no XML angle brackets in frontmatter. Description max 1024 chars, no XML, MUST include both what and when."
- **Codifier's reading:** A structural scaffold meant for rendering — fixed slot structure plus validation constraints, exactly template form per the rubric. P1 finding; natural substrate for `/design-skill`'s Template skeleton and `/assess-skill`'s description check. Guide Template 7 embodies it; a standalone template artifact would make it reusable outside the guide.
- **Suggested headline:** skill-description-three-part-template
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### strictness-escalation-skill-architecture::template::strict-mode-review-skill-overlay

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[strictness-escalation-skill-architecture]]
- **Source excerpt:**
  > "Consider folding the eight-layer scaffold into design-skill's Template skeleton as an optional 'strict-mode overlay': (1) core prompt, (2) numbered non-negotiable standards, (3) per-change review questions, (4) aggressive-flag list, (5) preferred remedies, (6) tone calibration with literal example phrases, (7) prioritized output ordering, (8) approval bar with presumptive blockers vs waivable concerns."
- **Codifier's reading:** The finding's own implementation notes propose the artifact: an eight-slot structural scaffold for audit-grade skills — template form (structure meant for rendering into new SKILL.md drafts), not a skill to adopt as-is. Target surface: `/design-skill` Template skeleton as an optional overlay.
- **Suggested headline:** strict-mode-review-skill-overlay
- **Recommendation:** extract via /extract-artifacts
- **Resolution:**

### hands-off-routine-prompt-precision-pattern::template::unattended-routine-prompt-sop-checklist

- **Date queued:** 2026-07-16
- **Status:** queued
- **Target form:** template
- **Source finding:** [[hands-off-routine-prompt-precision-pattern]]
- **Source excerpt:**
  > "A checklist or template for routine prompt authorship: (1) data sources named, (2) steps enumerated, (3) done-signal defined, (4) edge cases handled, (5) output destination specified. MetaSystem's skill templates could add a 'scheduled variant' section for any skill intended to run unattended."
- **Codifier's reading:** The embedded five-point authorship checklist is template-shaped (a scaffold for writing routine prompts), but it is speculative in the source ("could add") and the guide's Step 2 decision tree already carries the full discipline inline. Queued for completeness per DD-101's LLM-loose calibration; recommending dismissal as inline unless scheduled-skill authoring recurs as a demand.
- **Suggested headline:** unattended-routine-prompt-sop-checklist
- **Recommendation:** dismiss as inline
- **Resolution:**
