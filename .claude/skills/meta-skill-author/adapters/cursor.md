# Cursor Adapter

Cursor is a VS Code-based AI coding editor. Its native context-injection mechanism — `.cursorrules`
at the repo root or rules files in `.cursor/rules/` — maps to the project-context tier of the
portable skill taxonomy. BMAD maintains installer templates targeting Cursor alongside Claude Code
and 5+ other IDEs, confirming that SKILL.md-based architecture is adaptable to Cursor conventions
via a thin wrapper layer. [multi-ide-portability-via-installer-templates]

---

## Native Format

| Attribute | Detail |
|-----------|--------|
| Legacy file | `.cursorrules` at repository root — a single plain-text or markdown file, always loaded |
| Modern location | `.cursor/rules/<name>.mdc` — individual rule files, supports glob-scoped activation |
| File extension | `.mdc` (Cursor-specific markdown with frontmatter) for scoped rules |
| Scope | Workspace (project-local); no user-global or enterprise-managed tier equivalent to Claude Code's four-tier hierarchy |

**Three cross-platform strategies observed in production repos:**
1. **Platform-specific mirroring** (Archon): parallel files for `.claude/agents/`, `.github/agents/`,
   `.github/prompts/` — maximum fidelity, drift risk. [cross-platform-context-file-strategy]
2. **Chain-loader indirection** (n8n): root `CLAUDE.md` has a single `@AGENTS.md` pointer; other
   tools read `AGENTS.md` directly. Note: `@` reference syntax is Claude Code-specific.
   [cross-platform-context-file-strategy]
3. **Symlink** (MemPalace): `AGENTS.md -> CLAUDE.md` filesystem symlink — zero drift, zero
   maintenance. Caveat: Windows compatibility requires `mklink /D`; tarball/zip may lose symlinks.
   [universal-harness-context-via-symlink]

The SKILL.md portable unit maps to `.cursor/rules/<name>.mdc`; the canonical instruction prose
lives in a harness-agnostic source; the Cursor file carries only harness-specific metadata.
[shared-instructions-multi-harness-plugin-wrappers]

---

## Discovery & Activation

Cursor's loading model is **eager** — rules are injected into every request context once
activated, without lazy body deferral. This differs from Claude Code's description-based
routing.

| Activation mode | Mechanism |
|----------------|-----------|
| **Always-on** | `.cursorrules` at repo root; loaded for every request in the workspace |
| **Glob-scoped** | `.cursor/rules/<name>.mdc` with `globs:` frontmatter; rule applies only when active file matches the glob pattern |
| **Manual invocation** | Unknown — verify against current Cursor docs |
| **Description-matched auto-load** | Not available; Cursor does not implement LLM-based description routing as in Claude Code [skill-md-frontmatter-as-discovery-trigger-primitive] |

**Context-file taxonomy:** Among the de-facto standard files (CLAUDE.md, SOUL.md, AGENTS.md,
PROGRESS.md, MEMORY.md, RULES.md), Cursor reads `.cursorrules` rather than CLAUDE.md.
[context-file-taxonomy-claudemd-soulmd-agentsmd] ETH Zurich confirmed that manually written,
concise context files outperform auto-generated ones; quality over quantity applies here as
much as anywhere. [context-file-taxonomy-claudemd-soulmd-agentsmd]

**Eager-load implication:** Because all activated rules enter context on every turn, instruction
bloat is more costly in Cursor than in Claude Code's lazy-body model. ETH Zurich found context
files increase reasoning token usage 14–22%. [context-file-instruction-bloat-eth-zurich] Minimum
viable rules only; no content the AI can discover itself.

---

## Frontmatter / Metadata

Cursor `.mdc` files support a small YAML frontmatter block. The open-standard fields do not
map one-to-one; Cursor has its own metadata schema.

```yaml
---
description: "Code review conventions for TypeScript files"   # shown in Cursor UI
globs:
  - "**/*.ts"
  - "**/*.tsx"
alwaysApply: false    # true = always-on regardless of globs; false = glob-gated
---
```

**Open-standard field mapping for Cursor:**

| Open-standard field | Cursor equivalent | Status |
|--------------------|------------------|--------|
| `name` | Rule filename (without `.mdc`) | Translatable; use same kebab-case name |
| `description` | `description:` in `.mdc` frontmatter | Partial; not used for LLM routing — only UI label |
| `license` | No equivalent | Drop; not rendered |
| `compatibility` | No equivalent | Drop; replace with comment in body |
| `metadata` | No equivalent | Drop or inline as comments |
| `allowed-tools` | No equivalent in rules format | Unknown — verify against current docs |
| `when_to_use` (Claude Code ext.) | `globs:` + `alwaysApply:` | Partial mapping; glob-scoping replaces semantic trigger |
| `disable-model-invocation` (Claude Code ext.) | No equivalent | Unknown — verify against current docs |

**Key difference:** The `description` field in Cursor is a UI label, not a discovery trigger.
There is no equivalent to Claude Code's description-matched auto-load. All routing is either
glob-based (file type) or always-on. [skill-md-frontmatter-as-discovery-trigger-primitive]

---

## Body Conventions

Cursor rule bodies are plain markdown instructions; no Claude Code extensions apply.

**Size guidance:**
- ETH Zurich: even manually written context files add 14–22% reasoning overhead.
  [context-file-instruction-bloat-eth-zurich]
- The eager-loading model means every instruction is paid every turn — keep rules short,
  focused, and non-redundant.
- Anthropic's 500-line / 5K-token body budget is a useful ceiling to carry across platforms
  even though Cursor does not enforce it mechanically. [skill-as-directory-progressive-disclosure-three-levels]

**Instruction style:**
- Explain WHY behind every instruction; avoid ALL-CAPS imperatives. [skill-authoring-explain-the-why-not-musts]
- Declarative (outcome-based) instructions outperform imperative step-by-step for modern
  reasoning models. [declarative-goal-driven-agent-prompting]
- Negative constraints ("never begin with…") are more reliable than positive guidance for
  behavioral rules. [negative-constraints-as-probabilistic-output-collapse]

**Reference files:**
- Cursor rules files can reference other files via `@`-mentions in the rule body (Cursor-
  specific syntax). This provides L3-style on-demand context analogous to Claude Code's
  `references/` directory pattern. [skill-as-package-export-with-references]
- Structure: keep rule body lean; delegate depth to referenced files.

**Progressive disclosure in Cursor:**
- L1 equivalent: `.mdc` frontmatter description (UI label only).
- L2 equivalent: full rule body (always loaded when activated).
- L3 equivalent: `@<file>` references in body (loaded on demand within request).

The three-level progressive disclosure pattern is validated across 6+ independent
implementations; adapt it to Cursor's mechanisms even though the loading model differs.
[progressive-tiered-context-loading-convergence]

---

## Tool Permissioning

Cursor exposes tool approval **per-call**, not session-level bulk pre-approval. This is a
meaningful HITL difference from Claude Code's foreground/background bulk model.

- Each tool invocation (file edits, terminal commands) triggers a separate approval prompt.
- There is no `allowed-tools` frontmatter equivalent that pre-approves tools for a rule.
- Unknown — verify against current Cursor docs whether any rule-level tool permission
  mechanism exists beyond the default per-call prompt.

---

## HITL Primitives Available

| Primitive | Availability in Cursor |
|-----------|----------------------|
| Per-call tool approval | Available; each tool use prompts the user |
| Session-level bulk pre-approval | Not available (per-call model only) |
| Description-based side-effect guard | Not available; no `disable-model-invocation` equivalent |
| Glob-scoped activation | Available via `globs:` frontmatter — limits rule to relevant file types |
| Always-off / demote | Available by removing the rule file or setting `alwaysApply: false` |
| Audit log | Unknown — verify against current Cursor docs |

**Design implication:** Without a `disable-model-invocation` equivalent, side-effect workflows
(deploy, commit) cannot be guarded at the rule level in Cursor. Rely on the per-call tool
approval prompt as the primary gate, and structure instructions to require explicit user
confirmation before irreversible actions.

---

## Reasoning-Model Considerations

Cursor allows users to select from multiple models; the specific reasoning model in use at
any time is user-configured and may change. Rules must be written defensively for all model
tiers, not just reasoning models.

**Anti-patterns that degrade reasoning-model performance** [reasoning-model-anti-pattern-prescribed-reasoning]:

| Pattern | What to do instead |
|---------|-------------------|
| Explicit chain-of-thought prompting in rule body | State goal + constraints; omit CoT scaffolding |
| Few-shot examples embedded in rule | State principles; omit show-then-do examples |
| Decomposition scaffolding | Declare the outcome; let the model decompose |

**Multi-model defensive writing:** Because Cursor users may switch between non-reasoning and
reasoning models, rule bodies should work adequately with both. The declarative style
(Goal + Constraints + Context) degrades gracefully on non-reasoning models while maximally
enabling reasoning models. [reasoning-model-anti-pattern-prescribed-reasoning]

---

## Translation From Portable Format

| Portable field | Cursor equivalent | Notes |
|---------------|-----------------|-------|
| `name` | Rule filename (`.cursor/rules/<name>.mdc`) | Use same kebab-case slug |
| `description` | `description:` in `.mdc` frontmatter | UI label only; not a routing trigger |
| `license` | No equivalent | Omit |
| `compatibility` | Inline comment in body | E.g., `<!-- Cursor-specific adapter -->` |
| `metadata` | No equivalent | Omit |
| `allowed-tools` | No equivalent | Omit; rely on per-call approval |
| Body prose | Rule body (markdown) | Direct copy; remove Claude Code shell substitutions |
| `when_to_use` trigger text | `globs:` frontmatter | File-type scoping replaces semantic trigger |
| `paths` (Claude Code ext.) | `globs:` | Same concept; different syntax |
| `disable-model-invocation` | No equivalent | Enforce via instruction wording only |
| `context: fork` / `agent:` | No equivalent | Unknown — verify against current Cursor docs |
| Dynamic shell injection `!`cmd`` | No equivalent | Remove; resolve content statically |

---

## Known Gaps / Verify

- **Manual invocation mechanism:** Whether `.cursor/rules/` files can be invoked explicitly
  by name (like a slash command) is not covered by findings. Verify against current Cursor docs.
- **`allowed-tools` or equivalent:** No finding documents a Cursor rule-level tool
  permission field. Verify whether Cursor's rule format has evolved to include one.
- **`.mdc` frontmatter full schema:** Findings confirm `description`, `globs`, `alwaysApply`.
  Additional fields (e.g., priority, author) are unknown — verify against current Cursor docs.
- **Rule priority / conflict resolution:** When multiple rules match the same file type, the
  precedence order is not covered by findings. Verify.
- **Audit / logging:** Whether Cursor provides any per-rule audit trail is unknown.

---

## Example

Minimal Cursor rule for TypeScript code review (glob-scoped):

```markdown
---
description: "TypeScript code review conventions"
globs:
  - "**/*.ts"
  - "**/*.tsx"
alwaysApply: false
---

## Purpose

Apply these conventions when reviewing or generating TypeScript code, to keep the codebase
consistent and maintainable across team members.

## Conventions

- Prefer explicit return types on exported functions — the reason is that implicit inference
  makes API surface changes invisible to callers.
- Use `const` for all declarations unless reassignment is required — this communicates
  immutability intent to readers.
- Error handling: use `Result<T, E>` pattern (or the project's equivalent) rather than
  throwing bare `Error`; throwing makes control flow invisible at call sites.
- Avoid `any`; use `unknown` with a type guard instead — `any` disables type checking
  for all downstream code that touches the value.

## Output Format

When suggesting changes, show the before/after diff in a fenced block. Explain the
rationale for each change in one sentence.
```

---

## Provides (capability inventory — §4.2 requires × provides)

What this platform supplies against the controlled capability vocabulary
(`../references/capability-vocabulary.md`). **Provisional:** drafted from this staged
profile, which itself carries "Unknown — verify" flags; re-verify rows against current
Cursor docs before a port relies on them (L-10 discipline).

| Capability | Provides | How / note |
|---|---|---|
| `durable-document-store` | **native** | Workspace filesystem — read/write named files across sessions |
| `internal-document-search` | **native** | Workspace search over the repo |
| `workspace-file-inventory` | **native** | Filesystem enumeration over the workspace |
| `connector-source-discovery` | partial | Only via configured MCP servers; nothing built-in |
| `versioned-checkpoints` | **native** | git in the workspace |
| `change-detection` | **native** | git status/diff |
| `script-execution` | **native** | Integrated terminal in agent mode |
| `fresh-context-scoring` | partial | No subagent surface documented in this profile — verify |
| `human-approval-channel` | **native** | Interactive editor chat |
| `reference-bundle-attachment` | partial | Rules load eagerly (.mdc); on-demand reference reading in agent mode — verify |
| `byproduct-store` | partial | Any workspace directory by convention; no platform-defined cleanup lifecycle |
