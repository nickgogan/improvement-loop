# Perplexity Adapter

Perplexity's custom skills system is the **host platform** for this meta-skill itself.
Skills are markdown files with YAML frontmatter, loaded via the `load_skill` tool, and
scoped to `user`, `space`, or `org`. The description field drives discovery: agents match
task context against skill descriptions to decide which to load, directly implementing the
portable `skill-md-frontmatter-as-discovery-trigger-primitive` pattern.
[skill-md-frontmatter-as-discovery-trigger-primitive]

The four-discipline prompt evaluator finding was already adopted in production by Perplexity
Skills, making this the platform with the highest degree of direct research-to-implementation
alignment in the corpus. [four-discipline-prompt-evaluator]

---

## Native Format

| Attribute | Detail |
|-----------|--------|
| File name | `SKILL.md` (all uppercase) inside a named directory |
| Directory convention | `<name>/SKILL.md`; scoped skills copied to `workspace/skills/<scope>/<name>/` |
| Install path (built-in) | `workspace/skills/<name>/` for scope=None (built-in skills) |
| Install path (scoped) | `workspace/skills/<scope>/<name>/` for scope=user/space/org |
| Invocation | `load_skill(name="<name>")` or `load_skill(name="parent/sub-skill")` |
| Preloading | `preload_skills` field in subagent context — skills can be preloaded before the agent's first turn |
| Sub-skills | Parent/child naming: `parent/sub-skill` (e.g., `office/docx`) |

**Scope values:**
- `scope=None` — built-in skills (shipped with Computer)
- `scope="user"` — user-owned skills
- `scope="space"` — space-level shared skills
- `scope="org"` — org-level shared skills

---

## Discovery & Activation

Perplexity's activation model is **description-matched with explicit load_skill invocation** —
not the eager-catalog auto-load that Claude Code uses. The agent reads available skill
descriptions, decides which skill applies, then calls `load_skill` to fetch the full body.
This is a pull-model (lazy dispatch) implementation of the progressive disclosure pattern.
[progressive-tiered-context-loading-convergence]

| Mode | Behavior |
|------|----------|
| **Description-matched load** | Agent infers skill relevance from description and calls `load_skill` — primary activation path [skill-md-frontmatter-as-discovery-trigger-primitive] |
| **Explicit load by caller** | Parent agent or orchestrator calls `load_skill(name="skill-name")` directly |
| **Preload in subagent context** | `preload_skills` in subagent configuration loads skills before the first turn — always-on equivalent |
| **User request** | User can direct the agent to "use the X skill" — direct invocation |

**Description as the sole routing signal:** The frontmatter `description` field is the only
content the agent sees before deciding to call `load_skill`. A SKILL.md body that is never
loaded is dead capability. The description must encode: what it does + when to use it + key
capabilities, with "a little bit pushy" language to combat documented undertriggering bias.
[skill-md-frontmatter-as-discovery-trigger-primitive]

**Description optimization loop (applicable directly):**
Anthropic's held-out eval loop is directly applicable — treat Perplexity skill triggering as
a classification problem. 20 eval queries (8–10 should-trigger, 8–10 should-not-trigger
near-misses), 60/40 train/test split, 3 runs each, ≤5 iterations, select by TEST score.
[skill-description-optimization-loop-held-out-test]

---

## Frontmatter / Metadata

Perplexity skills use the SKILL.md frontmatter format. The open-standard six fields are the
foundation; Perplexity-specific conventions extend where needed.

```yaml
---
name: skill-name             # kebab-case; 1–64 chars; lowercase a-z/0-9/hyphens;
                             # no leading/trailing/consecutive hyphens;
                             # must match parent directory name;
                             # reserved words `anthropic` and `claude` forbidden;
                             # no XML angle brackets
                             # [skill-md-frontmatter-as-discovery-trigger-primitive]
description: |               # 1–1,024 chars; no XML tags; non-empty
  [What it does] + [When to use it] + [Key capabilities]
  # Canonical three-part structure. Target ~800 chars to leave room for when_to_use
  # if porting to Claude Code later. [skill-description-structure-what-when-capabilities]
  # Include trigger phrases: "Use when user asks for...", "Load this skill when..."
  # Pushy language combats undertriggering: "Make sure to use this skill whenever..."
  # [skill-md-frontmatter-as-discovery-trigger-primitive]
license: MIT                 # optional; SPDX expression
compatibility: |             # optional; declare scope and surface requirements
  scope=user|space|org; requires Perplexity Computer with load_skill tool available.
metadata:                    # optional key-value map
  version: "1.0.0"
  tags: ["research", "analysis"]
allowed-tools:               # Experimental open-standard field
  - search_web
  - fetch_url
---
```

**Three description failure modes to avoid** [skill-description-structure-what-when-capabilities]:
1. Too vague: "Helps with projects" — no routing signal
2. Missing triggers: "Creates sophisticated multi-page documentation systems" — no when-to-use
3. Too technical: "Implements the Project entity model with hierarchical relationships" — no user triggers

**Good description example:**
> "Analyzes financial data and generates investment research reports. Use when the user uploads
> financial statements, asks for 'investment analysis', 'DCF model', 'comparable company analysis',
> or 'earnings review'. Key capabilities: ratio analysis, valuation modeling, risk identification."

---

## Body Conventions

**Size budget:**
- Keep SKILL.md under 500 lines. [skill-as-directory-progressive-disclosure-three-levels]
- Recommended body: < 5K tokens. [skill-as-directory-progressive-disclosure-three-levels]
- Skill body is loaded into context on activation and stays there for the session.
  Write as standing instructions (invariants), not one-time setup steps.
  [skill-content-lifecycle-context-budget]

**Progressive disclosure (three levels):**
- L1 (~100 tokens): frontmatter name + description — what the agent reads before load decision.
- L2 (< 5K tokens): full SKILL.md body, loaded by `load_skill`.
- L3 (unbounded): files in `references/`, `scripts/`, `assets/` — accessed on demand.
  [skill-as-directory-progressive-disclosure-three-levels]

**Sub-skill pattern:**
```
parent-skill/
  SKILL.md             # parent: routes to sub-skills; ~150 lines
  sub-skill-a/
    SKILL.md           # sub-skill: detailed capability; full body
  sub-skill-b/
    SKILL.md
  references/
    api-reference.md
```
Invoked as `load_skill(name="parent-skill/sub-skill-a")`. The parent/child naming mirrors
the core/specialized inheritance pattern. [core-specialized-skill-inheritance-pattern]

**Instruction style:**
- Explain WHY behind every instruction; avoid ALL-CAPS MUST/ALWAYS/NEVER.
  [skill-authoring-explain-the-why-not-musts]
- Declarative (outcome-based) outperforms imperative step-by-step for reasoning models.
  [declarative-goal-driven-agent-prompting]
- Write negative constraints for behavioral rules; positive guidance weakly biases.
  [negative-constraints-as-probabilistic-output-collapse]
- Front-load critical instructions — content past 5K tokens is at risk after compaction.
  [skill-content-lifecycle-context-budget]

**Reference file pattern:**
```
my-skill/
  SKILL.md             # ≤500 lines; links references by relative path
  references/
    domain-guide.md
    api-reference.md
    examples.md
  assets/
    template.docx
```
SKILL.md stays lean; depth lives in `references/`. [skill-as-package-export-with-references]

---

## Tool Permissioning

Perplexity skills can declare tools in `allowed-tools` (open standard, Experimental).
Tool availability is governed by the agent's connected integrations and the platform's
tool catalog (`list_external_tools`, `search_web`, `fetch_url`, `bash`, etc.).

- Skills should declare their expected tools in `allowed-tools` for documentation
  and potential future enforcement.
- `describe_external_tools` is the runtime mechanism for confirming tool schema before
  invocation — skills that call external tools should include this pattern in their body.
- The `list_external_tools` → `describe_external_tools` → `call_external_tool` flow is
  the standard Perplexity tool-use pattern; skills should reference it rather than
  assuming specific tool availability.

**Side-effect guard pattern for Perplexity:**
Skills that perform irreversible actions (send messages, create posts, make purchases) should
explicitly call `confirm_action` with the complete draft content before execution. This is the
Perplexity-native equivalent of Claude Code's `disable-model-invocation` side-effect guard.
[skill-invocation-control-side-effect-guard]

---

## HITL Primitives Available

| Primitive | Availability in Perplexity |
|-----------|--------------------------|
| `confirm_action` call | Available; skills requiring user approval before irreversible actions should call this |
| Explicit `load_skill` invocation | Available; parent agents control when each sub-skill is loaded |
| `preload_skills` gating | Available; subagent configuration controls which skills are pre-loaded |
| Description-based routing guard | Available via undertriggering (description not pushy enough); also by not including skill in preload_skills |
| Autonomy-gradient annotation | Available as body-level design pattern; declare per-action HITL tier in body [autonomy-gradient-not-binary-delegation] |
| `update_todo_list` / `update_todo_status` | Available; skills can use these to checkpoint long workflows for user visibility |

**Autonomy gradient in skill body (recommended pattern):**
Annotate each action class with its HITL tier, derived from the 2×2 blast-radius × reversibility
matrix: [autonomy-gradient-not-binary-delegation]

```markdown
## Action Tiers

| Action | Tier | Rationale |
|--------|------|-----------|
| Read/search | Full Autonomy | Reversible; zero blast radius |
| Draft content | Guarded | Show draft before sending |
| Send message | Proposal-first | Confirm before any send action |
| Delete/overwrite | Human-required | Irreversible; explicit approval required |
```

---

## Reasoning-Model Considerations

Perplexity supports multiple models; the specific reasoning model in use is user/session
configurable. Skills must be written defensively for the full model range.

**Anti-patterns that degrade reasoning-model performance** [reasoning-model-anti-pattern-prescribed-reasoning]:

| Pattern | What to do instead |
|---------|-------------------|
| Explicit chain-of-thought ("Think step by step") | State goal + constraints; omit CoT framing |
| Few-shot examples embedded in skill body | State principles; trust the model to generalize |
| Self-consistency loops | Trust single-pass output |
| Least-to-most decomposition scaffolding | Declare the full problem; the model decomposes |
| Skeleton-of-thought structure | Let the model choose its output structure |

These five anti-patterns were validated across GPT-5.4, Claude 4.6, and Gemini 3.1 — the
full frontier model range, any of which may be active in a Perplexity session.
[reasoning-model-anti-pattern-prescribed-reasoning]

**Replacement pattern:** Goal + Constraints + Context. Declarative outcome-based instructions
outperform imperative step-by-step for reasoning models.
[declarative-goal-driven-agent-prompting]

**Exception (unattended routines):** Skills configured to run as scheduled/background tasks
without interactive reasoning may need numbered SOP steps and explicit completion signals
to function reliably without a reasoning budget. Ask: "interactive or scheduled?"
[hands-off-routine-prompt-precision-pattern]

---

## Translation From Portable Format

| Portable field | Perplexity equivalent | Notes |
|---------------|----------------------|-------|
| `name` | `name` in SKILL.md frontmatter | Same; must match directory name |
| `description` | `description` in SKILL.md frontmatter | Same; 1,024-char cap; primary routing signal |
| `license` | `license` | Same |
| `compatibility` | `compatibility` | Declare `scope=user|space|org` requirement |
| `metadata` | `metadata` | Same |
| `allowed-tools` | `allowed-tools` | Same; Experimental |
| `when_to_use` (Claude Code ext.) | Embed in `description` | Merge trigger text into description; no separate field |
| `argument-hint` (Claude Code ext.) | Not applicable | No slash-command UI |
| `disable-model-invocation` (Claude Code ext.) | Use `confirm_action` in body | Encode as body instruction + `confirm_action` call |
| `user-invocable: false` | Omit field; use `preload_skills` | Control visibility via preload config |
| `paths` (Claude Code ext.) | Not applicable | No path-scoped activation |
| `context: fork` (Claude Code ext.) | Subagent delegation via `call_external_tool` | Different mechanism; encode as body instruction pattern |
| Dynamic shell injection `!`cmd`` | Not applicable | Remove; resolve content statically or use `bash` tool in body |
| `hooks` (Claude Code ext.) | Not applicable | No hook system |

---

## Known Gaps / Verify

- **`allowed-tools` enforcement:** Whether Perplexity mechanically enforces the `allowed-tools`
  field to restrict tool invocations is not confirmed — currently likely documentation-only.
- **Frontmatter validation CLI:** The open-standard `skills-ref validate ./my-skill` CLI is
  documented for the standard; whether it is available in Perplexity's tooling environment
  is not confirmed. [skill-frontmatter-validation-rules]
- **`preload_skills` exact schema:** The preload mechanism is referenced in the platform
  context but the exact configuration syntax and scope rules are not documented in findings —
  verify against current Perplexity Skills documentation.
- **Sub-skill discovery depth:** Whether `load_skill(name="parent/sub-skill")` supports
  arbitrary nesting depth (more than one level) is not confirmed.
- **Hot reload:** Whether SKILL.md text edits take effect immediately mid-session (as in Claude
  Code's watched-directory model) or require session restart is not confirmed.

---

## Example

Minimal Perplexity skill with sub-skill pattern and autonomy tier annotation:

```markdown
---
name: market-research
description: |
  Conducts structured market research: competitor analysis, market sizing, trend identification,
  and synthesis into research briefs. Use when the user asks for market research, competitive
  analysis, industry overview, or market sizing for a product or sector.
  Load this skill whenever research involves multiple companies, data sources, or a formal output.
  Key capabilities: parallel web research, structured comparison tables, executive brief generation.
license: MIT
compatibility: "scope=user|space|org; requires search_web and fetch_url tools."
metadata:
  version: "1.0.0"
  tags: ["research", "competitive-analysis", "market-sizing"]
allowed-tools:
  - search_web
  - fetch_url
  - write
---

## Purpose

Produce structured market research from publicly available sources. This skill exists because
ad-hoc research produces inconsistent depth and format — a structured approach ensures
comparable coverage across all research requests.

## Action Tiers

| Action | Tier | Rationale |
|--------|------|-----------|
| Web search / URL fetch | Full Autonomy | Read-only; reversible |
| Draft report sections | Full Autonomy | Internal; user reviews final |
| Save report to file | Guarded | Show path + summary before writing |
| Send / share externally | Human-required | Out of scope for this skill |

## Research Procedure

Given a topic or company:

1. Identify the key research questions (market size, key players, trends, risks).
2. Search for data on each question in parallel where possible.
3. Fetch primary sources (company pages, analyst summaries, industry reports).
4. Synthesize into a structured brief (see Output Format).

Do not fabricate data. If a source does not exist for a claim, note the gap explicitly.

## Constraints

- Cite every factual claim with its source URL inline.
- Do not include data older than 24 months without flagging the date.
- If the research topic is ambiguous, ask one clarifying question before proceeding — not five.

## Output Format

```markdown
## Market Research: <Topic>

### Market Size
...

### Key Players
| Company | Position | Notable |
|---------|----------|---------|

### Trends
...

### Risks / Gaps
...

### Sources
All citations are inline above.
```
```

---

## Provides (capability inventory — §4.2 requires × provides)

What this platform supplies against the controlled capability vocabulary
(`../references/capability-vocabulary.md`). **Provisional:** drafted from this staged
profile; re-verify rows against current Perplexity Computer docs before a port relies
on them (L-10 discipline).

| Capability | Provides | How / note |
|---|---|---|
| `durable-document-store` | partial | Workspace filesystem for skill dirs; durable cross-session document persistence — verify |
| `internal-document-search` | partial | Web search tools documented (`search_web`); org/workspace document search not documented |
| `workspace-file-inventory` | partial | Workspace file access within Computer; scope — verify |
| `connector-source-discovery` | absent | No connector-source surface documented in this profile |
| `versioned-checkpoints` | absent | No version-history surface documented |
| `change-detection` | absent | No diff/status surface documented |
| `script-execution` | partial | `scripts/` are L3 package content; execution surface — verify |
| `fresh-context-scoring` | **native** | Subagents with `preload_skills`; separate context per subagent |
| `human-approval-channel` | **native** | Interactive chat |
| `reference-bundle-attachment` | **native** | `references/`/`assets/` read on demand (L3 progressive disclosure) |
| `byproduct-store` | absent | No designated ephemeral store documented |
