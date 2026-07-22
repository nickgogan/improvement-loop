# Claude Code Adapter

Claude Code is the **reference implementation** for the portable skill format. The six-field open
standard (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`) was
published by Anthropic at agentskills.io on December 18, 2025, making Claude Code the authoritative
target when no other platform is specified. [skills-as-open-portable-standard]

---

## Native Format

| Attribute | Detail |
|-----------|--------|
| File name | `SKILL.md` — all uppercase; lowercase `skill.md` fails upload [skill-md-format-yaml-front-matter-requirements] |
| Directory | `SKILL.md` must live inside a named folder: `<name>/SKILL.md` |
| Install paths | Enterprise (managed settings) › Personal (`~/.claude/skills/<name>/`) › Project (`.claude/skills/<name>/`) › Plugin (`plugin-name:skill-name` namespace) [skill-hierarchy-enterprise-personal-project-plugin] |
| Plugin bundle | Multiple skills + agents + hooks + MCP configs shipped as one namespaced unit via GitHub marketplace [skill-plugin-marketplace-distribution] |
| Slash commands | `.claude/commands/<name>.md` is a superset-compatible legacy form; skills win on name collision [slash-commands-merged-into-skills] |

**Upload to claude.ai:** folder must be zipped; drag into Claude → Customize → Skills → +.
Folder+zip requirement is commonly missed. [skill-md-format-yaml-front-matter-requirements]

---

## Discovery & Activation

Claude Code loads **all** skill descriptions at session start (eager catalog) and defers the full
body until task-match (lazy body). [agent-description-auto-dispatch-routing] This means:

1. **Description-matched auto-load** — Claude reads the skill catalog, decides when the task fits,
   pulls the full SKILL.md body. Undertriggering bias is documented; include "Make sure to use this
   skill whenever…" language. [skill-md-frontmatter-as-discovery-trigger-primitive]
2. **Path-scoped auto-load** — `paths` frontmatter field gates auto-load to specific file-glob
   patterns; skill silently skips on non-matching files. [claude-code-skill-frontmatter-extensions]
3. **User-invocable only** — `user-invocable: false` keeps skill in context as background knowledge;
   Claude can use it but users cannot type the slash command. [skill-invocation-control-side-effect-guard]
4. **Side-effect guard (slash-only)** — `disable-model-invocation: true` removes description from
   context entirely; user must type the explicit slash command. Canonical use: `/commit`, `/deploy`,
   `/send-slack-message`. [skill-invocation-control-side-effect-guard]

**Hot reload:** SKILL.md text edits in watched directories take effect immediately without session
restart. New top-level skill directories require restart. [skill-live-change-detection-hot-reload]

**Hierarchy and override precedence:** Enterprise > Personal > Project > Plugin.
Project skills walk up to repo root (monorepo support). Skill wins on skill/command name collision.
[skill-hierarchy-enterprise-personal-project-plugin]

**Budget management:** `skillListingBudgetFraction` = 0.01 (1% of context window for all
descriptions). `maxSkillDescriptionChars` = 1,536 per entry (description + when_to_use combined).
Use `/doctor` to diagnose overflow; `skillOverrides` demotes skills to name-only to free budget.
[skill-description-budget-context-overflow]

---

## Frontmatter / Metadata

### Open-standard fields (portable across platforms)

```yaml
---
name: my-skill            # 1–64 chars; lowercase a-z/0-9/hyphens; no leading/trailing/consecutive
                          # hyphens; must match parent directory name; reserved words `anthropic`
                          # and `claude` forbidden; no XML angle brackets
                          # [skill-md-frontmatter-as-discovery-trigger-primitive]
description: |            # 1–1,024 chars; no XML tags; non-empty
  [What it does] + [When to use it] + [Key capabilities]
  # Canonical three-part structure [skill-description-structure-what-when-capabilities]
  # Good: "Analyzes Figma design files and generates developer handoff documentation.
  #        Use when user uploads .fig files, asks for 'design specs' or 'design-to-code handoff'."
  # Bad failure modes: too vague ("Helps with projects"), missing triggers, too technical
  # [skill-description-structure-what-when-capabilities]
license: MIT              # optional; SPDX expression
compatibility: |          # optional; ≤500 chars; declares surface requirements for non-portable
                          # skills (e.g., "requires Claude Code; full filesystem access needed")
                          # [skill-cross-surface-portability-with-constraints]
metadata:                 # optional key-value map
  version: "1.0.0"
  tags: ["code-review", "quality"]
allowed-tools:            # Experimental; open-standard field; pre-approves tools without
  - Bash(*)               # per-invocation prompting [claude-code-skill-frontmatter-extensions]
  - Read
  - Write
---
```

### Claude Code extension fields (non-portable — Claude Code only)

These ~13 fields are NOT in the open standard; skills using them are silently Claude Code-only.
[claude-code-skill-frontmatter-extensions]

```yaml
when_to_use: |            # Additional triggering guidance shown alongside description.
                          # Combined description + when_to_use budget: 1,536 chars per entry.
                          # [skill-description-budget-context-overflow]
argument-hint: "<file>"   # Tab-completion hint shown in / menu
arguments:                # Typed argument declarations for $ARGUMENTS substitution
  - name: target
    description: "File to analyze"
    required: true
disable-model-invocation: true   # Removes description from context; user-invocable only.
                                 # Use for side-effect workflows (commit, deploy, send-slack).
user-invocable: false            # Hides from / menu; Claude can still auto-trigger.
disallowed-tools:                # Explicitly block specific tools for this skill
  - WebSearch
model: claude-opus-4-6           # Override model for this skill invocation
effort: high                     # Reasoning effort hint ("ultrathink" in body also works)
context: fork                    # Spawn isolated subagent; skill body becomes task prompt
agent: Explore                   # Named subagent type for fork context
paths:                   # Gate auto-load to matching file-glob patterns
  - "**/*.ts"
  - "src/**"
shell: true              # Enable !`cmd` dynamic context injection
hooks:                   # Event hooks (pre/post invocation)
  pre_invoke: ./hooks/pre.sh
```

**Key semantic rules:**
- `disable-model-invocation: true` + `user-invocable: false` together = skill is unreachable from
  any actor. Avoid this combination. [claude-code-skill-frontmatter-extensions]
- `allowed-tools` grants authority silently after workspace trust dialog. Accepting a trust dialog
  for a skill with broad `allowed-tools: Bash(*)` grants that authority silently.
  [skill-security-audit-obligation]
- `context: fork` requires explicit task instructions in body — if the body contains only
  guidelines without a task prompt, the subagent returns without meaningful output.
  [skill-forked-subagent-execution]

---

## Body Conventions

**Size budget:**
- Keep SKILL.md under 500 lines (Anthropic explicit guidance). [skill-as-directory-progressive-disclosure-three-levels]
- Recommended body: < 5K tokens. [skill-as-directory-progressive-disclosure-three-levels]
- Post-compaction: 5K tokens preserved per skill, 25K combined budget, LRU drop for oldest.
  Critical guidance past 5K tokens is at risk; front-load important content. [skill-content-lifecycle-context-budget]

**Progressive disclosure (three levels):**
- L1 (~100 tokens): frontmatter name + description always in system prompt.
- L2 (< 5K tokens): full SKILL.md body on activation.
- L3 (unbounded): bundled files in `references/`, `scripts/`, `assets/` loaded on demand via
  `bash` tool — code in scripts/ executes without entering context. [skill-as-directory-progressive-disclosure-three-levels]

**Required sections (five-element model):**
1. Purpose and scope
2. Triggering conditions and invocation context
3. Step-by-step instructions with branching logic
4. Internal policies and constraints
5. Expected output format [skill-as-new-employee-mental-model]

**Authoring style:**
- Explain the WHY behind every instruction; avoid ALL-CAPS MUST/ALWAYS/NEVER as yellow flags.
  [skill-authoring-explain-the-why-not-musts]
- Write as standing instructions (invariants), not one-time setup steps — the body is re-read
  from context on every turn, not re-fetched from disk. [skill-content-lifecycle-context-budget]
- Negative constraints ("never begin with…") collapse output probability; positive guidance
  weakly biases. Prefer negative-constraint form for behavioral rules. [negative-constraints-as-probabilistic-output-collapse]

**Dynamic context injection (Claude Code-specific):**
- `` !`<command>` `` at line start runs shell at activation time, inserts stdout into rendered SKILL.md.
- Command runs ONCE; output is not re-scanned for nested placeholders.
- `${CLAUDE_SKILL_DIR}` resolves bundled-script paths regardless of CWD.
- `disableSkillShellExecution: true` in settings replaces each command with a placeholder (enterprise policy). [skill-dynamic-context-injection-shell-prerender]

**Reference file pattern:**
```
my-skill/
  SKILL.md           # ≤500 lines; links to references/ by relative path
  references/
    api-reference.md
    architecture.md
    quickstart.md
  scripts/
    analyze.py
  assets/
```
[skill-as-package-export-with-references]

---

## Tool Permissioning

- `allowed-tools` (open standard, Experimental): pre-approves listed tools without per-invocation
  prompting. Accepting workspace trust dialog grants this authority silently. Broad grants
  (`Bash(*)`) are a named security risk. [skill-security-audit-obligation]
- `disallowed-tools` (Claude Code extension): explicitly blocks tools even if otherwise available.
- `Skill(name)` deny rules live in user permissions *outside* the skill, as a separate control
  layer. [skill-invocation-control-side-effect-guard]
- Enterprise-managed settings can override all skill-level tool permissions.
  [skill-hierarchy-enterprise-personal-project-plugin]

---

## HITL Primitives Available

Claude Code exposes the richest HITL surface of any supported platform:

| Primitive | How it works |
|-----------|-------------|
| Side-effect guard | `disable-model-invocation: true` forces explicit human slash-command to trigger [skill-invocation-control-side-effect-guard] |
| Path-scoped auto-load | `paths` prevents auto-loading in unintended file contexts [claude-code-skill-frontmatter-extensions] |
| Tool-level approval | Per-tool permission prompts at session start via workspace trust dialog |
| Foreground pass-through | Interactive gate per action in foreground sessions [foreground-vs-background-subagent-permission-models] |
| Background pre-approval | Bulk pre-approval at launch; silent deny on unapproved actions in background [foreground-vs-background-subagent-permission-models] |
| Deny-and-continue | Blocked actions return as tool results with instructions to find safer paths; after 3 consecutive or 20 total denials, escalate [claude-code-auto-mode-ai-driven-permission-classif] |
| `skillOverrides` | Demotes skills to name-only or off; operator-level budget and scope control [skill-description-budget-context-overflow] |
| Audit log | JSONL per-skill scan decisions when security scanner is active [skill-security-scanner-fail-closed] |

**Design rule for side-effect skills:** if a skill can commit code, send messages, or deploy, set
`disable-model-invocation: true` by default. "You don't want Claude deciding to deploy because your
code looks ready." [skill-invocation-control-side-effect-guard]

---

## Reasoning-Model Considerations

**Available model:** Claude 4.6 / Opus (selectable via `model:` frontmatter field or at session level).
`ultrathink` anywhere in skill body content requests deeper reasoning budget. [claude-code-skill-frontmatter-extensions]

**Anti-patterns that degrade reasoning-model performance** [reasoning-model-anti-pattern-prescribed-reasoning]:

| Pattern | What to do instead |
|---------|-------------------|
| Explicit chain-of-thought ("First, think step by step…") | Omit; the model reasons internally |
| Few-shot examples (show-then-do) | State goal + constraints only |
| Self-consistency prompting | Trust single-pass output |
| Least-to-most decomposition scaffolding | State the full problem; let the model decompose |
| Skeleton-of-thought | Let the model choose its structure |

**Replacement pattern:** Goal + Constraints + Context. Declarative (outcome-based) instructions
outperform imperative (step-by-step) for reasoning models. [declarative-goal-driven-agent-prompting]

**Exception:** Skills intended for unattended/scheduled execution (no interactive reasoning budget)
may need numbered SOP steps. Ask: "interactive or scheduled?" before choosing instruction style.
[hands-off-routine-prompt-precision-pattern]

---

## Translation From Portable Format

| Portable field | Claude Code equivalent | Notes |
|---------------|----------------------|-------|
| `name` | `name` | Same; must match directory name |
| `description` | `description` | Same; 1,024-char open-standard cap; combine with `when_to_use` up to 1,536 chars total |
| `license` | `license` | Unchanged |
| `compatibility` | `compatibility` | Use to declare Claude Code-specific requirements |
| `metadata` | `metadata` | Unchanged |
| `allowed-tools` | `allowed-tools` | Unchanged; Experimental |
| Trigger phrases | Add to `when_to_use` | Claude Code-only extension; combats undertriggering |
| Tool restrictions | `disallowed-tools` | Claude Code extension; no portable equivalent |
| Execution mode | `context: fork` + `agent:` | Claude Code-only; fork subagent pattern |
| File-type scoping | `paths` | Claude Code-only; glob patterns |
| Side-effect guard | `disable-model-invocation: true` | Claude Code-only; no portable equivalent |

---

## Known Gaps / Verify

- **Exact `model:` field values for Claude 4.6 / Opus:** The findings document "Claude 4.6/Opus"
  as the reasoning model; verify current model identifier strings against
  https://docs.anthropic.com/en/docs/about-claude/models before using `model:` in frontmatter.
- **`allowed-tools` experimental status:** Marked Experimental in the open standard; verify
  whether it has graduated to stable. [skill-frontmatter-validation-rules]
- **`hooks` field schema:** Findings confirm the field exists; exact schema (events, allowed
  scripts, path resolution) is not covered. Verify against current Claude Code docs.
- **`effort:` field values:** Findings confirm the field exists alongside `ultrathink` body
  keyword; full enumeration of accepted values is not covered.
- **claude.ai upload surface details:** Folder+zip requirement confirmed for claude.ai upload;
  verify whether the Claude Code filesystem path and the claude.ai upload path now share a sync
  mechanism (no finding confirms automatic sync). [skill-cross-surface-portability-with-constraints]

---

## Example

Minimal Claude Code skill with side-effect guard and dynamic context injection:

```markdown
---
name: commit-staged
description: |
  Commits staged git changes with a conventional-commit message derived from the diff.
  Use this skill when the user asks to "commit", "save changes", or "write a commit message".
  Do NOT use for deploys or pushes — this skill only creates the local commit.
when_to_use: |
  Invoke when staged changes are confirmed ready. Never auto-invoke; require explicit
  user request to commit — deployment is out of scope.
disable-model-invocation: true
allowed-tools:
  - Bash(git commit*)
  - Bash(git status)
  - Bash(git diff --cached)
---

## Purpose

Produce a conventional-commit message for staged changes and create the local commit.
This skill runs only on explicit user request — you should never trigger it autonomously —
because a premature commit cannot easily be undone without rewriting history.

## Context at Invocation

!`git diff --cached --stat`

## Procedure

1. Review the staged diff above.
2. Identify the primary change type: feat / fix / docs / refactor / test / chore.
3. Write a message: `<type>(<scope>): <imperative summary ≤72 chars>`.
4. If the diff spans multiple concerns, write a multi-line body.
5. Run: `git commit -m "<message>"`.
6. Report the commit hash and one-line summary to the user.

## Constraints

- Scope is the nearest package or module path; omit if ambiguous.
- Breaking changes append `!` after type: `feat!`.
- Never include generated files (lock files, dist/) in the message scope.

## Output Format

```
✓ Committed <hash>: <type>(<scope>): <summary>
```
```

---

## Provides (capability inventory — §4.2 requires × provides)

What this platform supplies against the controlled capability vocabulary
(`../references/capability-vocabulary.md`). Stage-2 ports map every row of the source
skill's `capability-contract.yaml` here: unmet **required** ⇒ the port states "do not
install without it"; unmet **optional** ⇒ the port carries the contract's degradation note.

| Capability | Provides | How / note |
|---|---|---|
| `durable-document-store` | **native** | Workspace filesystem — read/write named files across sessions |
| `internal-document-search` | **native** | Workspace file search (grep/glob over the repo) |
| `workspace-file-inventory` | **native** | Filesystem enumeration over the project tree |
| `connector-source-discovery` | partial | Only via configured MCP servers; nothing built-in |
| `versioned-checkpoints` | **native** | git in the workspace |
| `change-detection` | **native** | git status/diff |
| `script-execution` | **native** | Bash tool, scoped via `allowed-tools` |
| `fresh-context-scoring` | **native** | Subagents (`context: fork` / `agent:` extensions) |
| `human-approval-channel` | **native** | Interactive chat + permission prompts; `disable-model-invocation` gates side-effect skills |
| `reference-bundle-attachment` | **native** | Skill-directory `references/` read on demand (L3 progressive disclosure) |
| `byproduct-store` | partial | Any workspace directory by convention; no platform-defined cleanup lifecycle |
| `live-web-retrieval` | **native** | WebSearch/WebFetch tools; MCP servers extend to connected data sources |
