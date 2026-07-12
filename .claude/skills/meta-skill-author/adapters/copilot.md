# GitHub Copilot Adapter

GitHub Copilot's native context-injection mechanism is the `copilot-instructions.md` file
(also accepted at `.github/copilot-instructions.md`). It is workspace-scoped and always-on —
the closest analogue in the portable skill taxonomy to a single, permanently active skill with
no trigger-based filtering. Copilot adopted the Agent Skills open standard within the ~6-month
adoption window after Anthropic's December 2025 publication. [skills-as-open-portable-standard]

---

## Native Format

| Attribute | Detail |
|-----------|--------|
| Primary file | `copilot-instructions.md` in the repo root |
| Alternate path | `.github/copilot-instructions.md` |
| Scope | Workspace (project-local); always injected into every Copilot request in the workspace |
| Activation model | Always-on; no trigger-based or glob-scoped gating |
| Agent Skills format | Copilot also accepts `SKILL.md` files; details of multi-skill support — Unknown, verify against current GitHub Copilot docs |

**Context-file taxonomy:** Among the de-facto standard files (CLAUDE.md, SOUL.md, AGENTS.md,
PROGRESS.md, MEMORY.md, RULES.md), Copilot reads `AGENTS.md` as its preferred auto-loaded
context file when structured agent instructions are intended. The symlink strategy
(`AGENTS.md -> CLAUDE.md`) provides zero-drift dual-harness support for repos targeting both
Copilot and Claude Code. [context-file-taxonomy-claudemd-soulmd-agentsmd]
[universal-harness-context-via-symlink]

**Cross-platform mirroring (Archon pattern):** Archon maintains parallel files in
`.github/agents/` and `.github/prompts/` alongside `.claude/agents/` — maximum per-platform
fidelity with drift risk between copies. The chain-loader indirection strategy (n8n: root
`CLAUDE.md` is a single `@AGENTS.md` pointer) works if Copilot reads `AGENTS.md` directly.
Note: the `@` pointer syntax is Claude Code-specific and Copilot reads the target file
directly rather than following the pointer. [cross-platform-context-file-strategy]

---

## Discovery & Activation

Copilot's model is **always-on** — there is no equivalent to Claude Code's description-matched
lazy-body loading.

| Mode | Behavior |
|------|----------|
| Always-on workspace context | `copilot-instructions.md` injected into every Copilot chat / inline suggestion request |
| Scope filtering | None documented; all instructions apply globally within the workspace |
| Explicit invocation | Unknown — verify against current GitHub Copilot docs |
| Multi-skill catalog routing | Unknown — verify against current GitHub Copilot docs |

**Implication for skill authors:** Because there is no per-skill trigger, the entire instruction
set is always paid. This makes Copilot's cost/benefit profile significantly different from
Claude Code's 1%-budget catalog model. [skill-description-budget-context-overflow]

ETH Zurich confirmed that LLM-generated context files reduce success rates ~3% and increase
inference cost 20%; even human-written files add 14–22% reasoning overhead. This effect is
especially acute under an always-on model. Write the minimum necessary. [context-file-instruction-bloat-eth-zurich]

---

## Frontmatter / Metadata

`copilot-instructions.md` does not require or process YAML frontmatter. The file is treated as
plain markdown prose. When delivering skills via the open Agent Skills format to Copilot, the
standard six-field frontmatter applies.

**Open-standard fields and their Copilot mapping:**

| Open-standard field | Copilot status | Notes |
|--------------------|---------------|-------|
| `name` | No UI consumption documented | Include for open-standard compliance; Copilot may display it |
| `description` | Not used for routing | Copilot has no trigger-based routing; description is metadata only |
| `license` | Not rendered | Include for standard compliance |
| `compatibility` | Not rendered | Use to declare Copilot-specific requirements |
| `metadata` | Not rendered | Include for standard compliance |
| `allowed-tools` | Unknown | Verify against current GitHub Copilot docs |
| `when_to_use` (Claude Code ext.) | Not applicable | No routing engine to consume it |
| `disable-model-invocation` (Claude Code ext.) | Not applicable | Always-on model has no such gate |
| `paths` (Claude Code ext.) | Not applicable | No path-scoped activation |

**Minimal compliant frontmatter for Copilot:**

```yaml
---
name: typescript-conventions
description: |
  TypeScript code quality conventions for this workspace.
  Use when writing, reviewing, or refactoring TypeScript files.
license: MIT
compatibility: "Workspace-scoped; always active. Does not require tool access beyond editor."
---
```

---

## Body Conventions

**Size guidance:**
- Anthropic's 500-line / 5K-token body budget is a useful portable ceiling. [skill-as-directory-progressive-disclosure-three-levels]
- Always-on loading means every line costs context on every request — be more aggressive
  about brevity than you would be for trigger-scoped Claude Code skills.
- ETH Zurich: agents "are surprisingly good at discovering file structures on their own" —
  do not include directory listings or file inventories. [pointers-over-copies-in-context-files]

**Instruction style:**
- Explain the WHY behind every instruction; avoid ALL-CAPS MUST/ALWAYS/NEVER.
  [skill-authoring-explain-the-why-not-musts]
- Declarative (outcome-based) instructions outperform imperative step-by-step for reasoning
  models. [declarative-goal-driven-agent-prompting]
- Negative constraints are more reliable than positive guidance for behavioral rules.
  [negative-constraints-as-probabilistic-output-collapse]

**Progressive disclosure in Copilot:**
- L1/L2 equivalent: the entire `copilot-instructions.md` is always loaded — there is no deferred
  body tier.
- L3 equivalent: unknown whether Copilot supports `@<file>` reference syntax or equivalent
  on-demand file injection — verify against current GitHub Copilot docs.

The inability to defer body content makes the "pointers over copies" principle especially
important: reference external files by path rather than embedding their content.
[skills-as-pointers-to-second-brain-files]

**Section structure (recommended):**
1. Scope statement — what this instruction set covers
2. Core conventions with WHY rationale per rule
3. Coding patterns and anti-patterns
4. Output format expectations

---

## Tool Permissioning

Compared to Claude Code, Copilot has **limited HITL primitives** at the skill/rule level.

- No `allowed-tools` enforcement at the file level (unknown whether Agent Skills format changes this).
- No `disable-model-invocation` equivalent to guard side-effect workflows.
- Tool invocations in Copilot Chat (e.g., terminal commands, file writes) may prompt
  individually — Unknown, verify against current GitHub Copilot docs.

**Design implication:** Authors cannot rely on file-level permissioning to restrict tool access.
Structure instructions conservatively: state explicitly which actions are in-scope and which
require explicit human initiation.

---

## HITL Primitives Available

| Primitive | Availability in Copilot |
|-----------|------------------------|
| Always-on scope limitation | Available — `copilot-instructions.md` applies only within the workspace |
| Per-call tool approval | Unknown — verify against current GitHub Copilot docs |
| Side-effect guard (`disable-model-invocation`) | Not available |
| Glob-scoped activation | Not available |
| Session-level bulk pre-approval | Unknown — verify against current GitHub Copilot docs |
| Audit log | Unknown — verify against current GitHub Copilot docs |
| `skillOverrides` / demotion | Not available |

**Compensating design pattern:** Encode side-effect guards in the instruction body itself:
"Never commit, push, or deploy autonomously. Always confirm with the user before running
any terminal command that modifies state outside the current file." This is a weaker guarantee
than `disable-model-invocation: true` but is the available primitive. [skill-invocation-control-side-effect-guard]

---

## Reasoning-Model Considerations

GitHub Copilot exposes multiple models; the specific model used is user/org-configured and
may include reasoning models (GPT-4o, Claude Sonnet/Opus, Gemini). Write instructions
defensively for the full model range.

**Anti-patterns that degrade reasoning-model performance** [reasoning-model-anti-pattern-prescribed-reasoning]:

| Pattern | What to do instead |
|---------|-------------------|
| Explicit step-by-step CoT scaffolding | State goal + constraints |
| Few-shot worked examples in instructions | State principles; trust the model to generalize |
| Decomposition templates | Declare the outcome; omit the skeleton |

**Why this matters for always-on instructions:** Prescriptive reasoning scaffolding in an
always-on file costs tokens on every request and actively degrades reasoning-model performance.
The ETH Zurich 14–22% reasoning overhead finding compounds with reasoning-model anti-patterns
when both are present. [context-file-instruction-bloat-eth-zurich]
[reasoning-model-anti-pattern-prescribed-reasoning]

---

## Translation From Portable Format

| Portable field | Copilot equivalent | Notes |
|---------------|-------------------|-------|
| `name` | Frontmatter `name:` (for compliance) | No routing function; metadata only |
| `description` | Frontmatter `description:` | No routing function; metadata only |
| `license` | Frontmatter `license:` | Compliance only |
| `compatibility` | Frontmatter `compatibility:` | Declare workspace-scope requirement |
| `metadata` | Frontmatter `metadata:` | Compliance only |
| `allowed-tools` | Unknown | Verify |
| Body prose | `copilot-instructions.md` body | Direct port; remove Claude Code extensions |
| `when_to_use` trigger text | N/A | No routing engine; embed context in body scope statement |
| `paths` (Claude Code ext.) | N/A | No path-scoped activation available |
| `disable-model-invocation` | N/A | Encode as body instruction instead |
| Dynamic shell injection `!`cmd`` | N/A | Resolve content statically before copying |
| `context: fork` / `agent:` | N/A | No fork execution model |

---

## Known Gaps / Verify

- **Multi-skill support:** Whether Copilot supports multiple `SKILL.md` files in a catalog
  (as opposed to the single `copilot-instructions.md` file) is not covered by findings.
- **`allowed-tools` in Copilot Agent Skills:** Whether Copilot's implementation of the Agent
  Skills standard processes the `allowed-tools` field is unknown.
- **`@<file>` reference syntax:** Whether Copilot supports on-demand file injection via
  `@filename` mentions in instruction bodies is unknown — this affects whether L3-style
  progressive disclosure is achievable.
- **Per-call vs. session tool approval:** The granularity of Copilot's tool approval
  prompting model is not covered by findings.
- **Copilot Workspace vs. Copilot Chat context file loading:** Whether `copilot-instructions.md`
  applies equally in both Copilot Chat and Copilot Workspace modes is not confirmed.

---

## Example

Minimal `copilot-instructions.md` for a TypeScript workspace (always-on, no frontmatter required
for the plain file; frontmatter added for Agent Skills compliance):

```markdown
---
name: workspace-typescript
description: |
  TypeScript coding conventions and quality standards for this workspace.
  Apply when writing, reviewing, or refactoring any TypeScript or JavaScript file.
license: MIT
compatibility: "GitHub Copilot workspace-scoped; always active."
---

## Scope

These conventions apply to all TypeScript and JavaScript files in this workspace. They
exist because the codebase is shared across multiple teams, and consistency reduces the
cognitive overhead of reading unfamiliar code.

## Type Safety

Prefer explicit return types on all exported functions. The reason: implicit return type
inference hides API surface changes from callers until runtime failures occur.

Use `unknown` over `any` and narrow with type guards. `any` propagates unsafety to every
consumer of the value, defeating TypeScript's purpose.

## Error Handling

Return `Result<T, E>` (or the project's equivalent type) instead of throwing. Thrown
errors make control flow invisible at call sites and break async error propagation.

## Immutability

Declare all values `const` unless reassignment is required. This signals immutability
intent — readers do not need to scan downstream code to check whether a value changes.

## Constraints

Never commit, push, or deploy without explicit user confirmation. These actions affect
state outside the current session and cannot be automatically reversed.

## Output Format

When suggesting changes, provide a before/after diff in a fenced block with a one-sentence
rationale for each change.
```

---

## Provides (capability inventory — §4.2 requires × provides)

What this platform supplies against the controlled capability vocabulary
(`../references/capability-vocabulary.md`). Rows reflect VS Code Copilot agent mode
(the always-on instructions model above constrains *discovery*, not tooling).

| Capability | Provides | How / note |
|---|---|---|
| `durable-document-store` | **native** | Workspace filesystem — read/write named files across sessions |
| `internal-document-search` | **native** | Workspace search tools (grep/glob/semantic) |
| `workspace-file-inventory` | **native** | Filesystem enumeration over the workspace |
| `connector-source-discovery` | partial | Only via configured MCP servers; nothing built-in |
| `versioned-checkpoints` | **native** | git in the workspace |
| `change-detection` | **native** | git status/diff |
| `script-execution` | **native** | Integrated terminal; no per-skill tool gate — the side-effect guard lives in prose (SKILL.md §5.2 operating note) |
| `fresh-context-scoring` | **native** | Subagent runs in agent mode |
| `human-approval-channel` | **native** | Interactive chat approval; weaker per-skill permissioning than Claude Code — gate side effects in prose |
| `reference-bundle-attachment` | **native** | Skill-folder files readable on demand |
| `byproduct-store` | partial | Any workspace directory by convention; no platform-defined cleanup lifecycle |
