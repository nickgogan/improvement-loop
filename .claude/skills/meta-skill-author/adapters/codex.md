# OpenAI Codex Adapter

OpenAI Codex CLI uses `AGENTS.md` as its primary auto-loaded context file convention.
`AGENTS.md` is part of the de-facto cross-platform context-file taxonomy (CLAUDE.md,
SOUL.md, AGENTS.md, PROGRESS.md, MEMORY.md, RULES.md) that has emerged across coding
agents. [context-file-taxonomy-claudemd-soulmd-agentsmd] gstack generates SKILL.md files
for Codex alongside Claude Code, Cursor, and 5 other platforms from a single template
source, confirming SKILL.md-based architecture is portable to Codex conventions.
[template-generated-skills-multi-host]

MemPalace demonstrates a three-layer plugin wrapper architecture where a `.codex-plugin/skills/*/SKILL.md`
wrapper delegates to a harness-agnostic instruction source via `mempalace instructions <name>` CLI call.
[shared-instructions-multi-harness-plugin-wrappers]

---

## Native Format

| Attribute | Detail |
|-----------|--------|
| Primary context file | `AGENTS.md` at repository root — Codex CLI auto-loads this file |
| Skill files | `SKILL.md` files in a skills directory (path convention: unknown — verify against current OpenAI Codex docs) |
| Symlink compatibility | `AGENTS.md -> CLAUDE.md` filesystem symlink gives both Codex and Claude Code their expected file with zero content duplication [universal-harness-context-via-symlink] |
| Execution environment | Sandboxed execution — Codex CLI runs in an isolated sandbox; network and filesystem access may be restricted relative to Claude Code [agentic-harness-self-assessment-skill] |
| Distribution | gstack: 38 templates produce skills across 8 platforms including Codex [template-generated-skills-multi-host] |

**Plugin wrapper pattern (MemPalace):**
```
.codex-plugin/
  skills/
    my-skill/
      SKILL.md       # thin wrapper; ≤40 lines; harness-specific metadata only
                     # delegates to: mempalace instructions my-skill
  plugin.json
```
Instruction prose lives in `mempalace/instructions/my-skill.md` (harness-agnostic source).
Wrapper carries only Codex-specific packaging metadata. [shared-instructions-multi-harness-plugin-wrappers]

**Symlink strategy (MemPalace):**
```bash
ln -s CLAUDE.md AGENTS.md    # Claude Code reads CLAUDE.md; Codex reads AGENTS.md
```
Caveats: Windows requires `mklink /D`; tarball/zip distribution may not preserve symlinks.
[universal-harness-context-via-symlink]

---

## Discovery & Activation

| Mode | Behavior |
|------|----------|
| Auto-load on session start | `AGENTS.md` at repo root is loaded automatically by Codex CLI |
| SKILL.md catalog | Whether Codex implements description-based LLM routing (as Claude Code does) is Unknown — verify against current OpenAI Codex docs |
| Explicit invocation | Unknown — verify against current OpenAI Codex docs |
| Sandbox constraints | Codex runs in a sandboxed environment; skill activation may be limited by what the sandbox permits |

**ETH Zurich quality rule applies:** Manually written, concise files outperform auto-generated
ones. Quality over quantity — load only what the agent needs. [context-file-taxonomy-claudemd-soulmd-agentsmd]

**Context-file taxonomy:** `AGENTS.md` is designated as the tool-agnostic conventions file in
the de-facto taxonomy. SOUL.md (values and philosophy) and PROGRESS.md (session bridging)
may complement it. A minimal starting set is `AGENTS.md` + `PROGRESS.md`.
[context-file-taxonomy-claudemd-soulmd-agentsmd]

---

## Frontmatter / Metadata

Whether Codex processes YAML frontmatter in `SKILL.md` files the same way Claude Code does
is partially confirmed by production evidence (gstack ships SKILL.md to Codex via templates)
but the full field support is not documented in findings.

**Open-standard fields (from agentskills.io):**

```yaml
---
name: my-skill               # kebab-case, 1–64 chars; must match directory name
description: |               # 1–1,024 chars; what + when + key capabilities
  [What it does] + [When to use it] + [Key capabilities]
license: MIT
compatibility: "Requires Codex CLI sandbox with filesystem access."
metadata:
  version: "1.0.0"
allowed-tools:               # Experimental; verify Codex support
  - Bash
  - Read
  - Write
---
```

**Open-standard field mapping for Codex:**

| Open-standard field | Codex status | Notes |
|--------------------|-------------|-------|
| `name` | Likely supported (per template evidence) | Use same kebab-case convention |
| `description` | Likely supported | Whether used for LLM routing or just metadata — Unknown |
| `license` | Unknown | Include for standard compliance |
| `compatibility` | Unknown | Include to declare sandbox requirements |
| `metadata` | Unknown | Include for standard compliance |
| `allowed-tools` | Unknown | Verify against current Codex docs |
| `when_to_use` (Claude Code ext.) | Not applicable | Claude Code-specific |
| `disable-model-invocation` (Claude Code ext.) | Not applicable | Claude Code-specific |
| `paths` (Claude Code ext.) | Unknown | May have equivalent — verify |
| `context: fork` / `agent:` (Claude Code ext.) | Not applicable | Claude Code-specific |
| Dynamic shell injection `!`cmd`` | Not applicable | Claude Code-specific |

---

## Body Conventions

**Size guidance:**
- Anthropic's 500-line / 5K-token body budget is the portable ceiling; carry it across
  platforms unless the target platform provides a different limit. [skill-as-directory-progressive-disclosure-three-levels]
- ETH Zurich: context files add 14–22% reasoning overhead even when well-written.
  [context-file-instruction-bloat-eth-zurich]

**Progressive disclosure:**
- L1 equivalent: SKILL.md frontmatter name + description (if Codex implements catalog routing).
- L2 equivalent: full SKILL.md body on activation.
- L3 equivalent: reference files loaded on demand — whether Codex supports bash-based on-demand
  file reading as Claude Code does is Unknown — verify against current docs.

**Instruction style:**
- Explain WHY; avoid ALL-CAPS imperatives. [skill-authoring-explain-the-why-not-musts]
- Declarative (outcome-based) instructions for reasoning-model targets. [declarative-goal-driven-agent-prompting]
- Write as standing instructions (invariants), not one-time setup steps.
  [skill-content-lifecycle-context-budget]

**Sandbox-aware authoring:**
- Codex's sandboxed execution means filesystem and network access is restricted relative to
  Claude Code. Skills that reference external network resources or local absolute paths may
  fail silently. [skill-cross-surface-portability-with-constraints]
- Use relative paths; avoid network calls in skill body instructions unless sandbox permissions
  are confirmed.
- The `compatibility` field should declare sandbox requirements explicitly.
  [skill-cross-surface-portability-with-constraints]

**Body structure (five-element model):**
1. Purpose and scope
2. Triggering conditions and invocation context
3. Instructions with branching logic
4. Internal policies and constraints (including sandbox limitations)
5. Expected output format
[skill-as-new-employee-mental-model]

---

## Tool Permissioning

Codex's sandboxed execution model provides **environment-level** permission constraints
rather than SKILL.md-level constraints.

- The sandbox restricts what tools are available; SKILL.md `allowed-tools` may have no
  effect beyond what the sandbox already permits.
- Whether `allowed-tools` in the open standard is processed by Codex to further restrict
  within the sandbox is Unknown — verify against current OpenAI Codex docs.
- Design skills to operate within the most restricted plausible sandbox: no assumed network,
  no absolute path assumptions, no package install.

---

## HITL Primitives Available

| Primitive | Availability in Codex |
|-----------|----------------------|
| Sandbox isolation | Available; Codex runs in isolated execution environment [agentic-harness-self-assessment-skill] |
| Per-call tool approval | Unknown — verify against current Codex docs |
| Side-effect guard | No `disable-model-invocation` equivalent available |
| Description-based routing guard | Unknown — verify if Codex has routing equivalent |
| Audit log | Unknown — verify against current Codex docs |

**Compensating pattern:** Encode side-effect guards as explicit body instructions:
"Confirm with the user before running any command that creates, modifies, or deletes
files outside the current working directory."

The sandbox itself is the primary HITL primitive — scope skills to operations permitted
within the sandbox, and treat network/filesystem expansion as requiring explicit privilege
declaration.

---

## Reasoning-Model Considerations

**Available model:** GPT-5.x series (verify current model identifiers against
https://platform.openai.com/docs/models before using a model identifier in code).

The `reasoning-model-anti-pattern-prescribed-reasoning` finding was validated against
GPT-5.4, Claude 4.6, and Gemini 3.1 — all three frontier model families are affected.
[reasoning-model-anti-pattern-prescribed-reasoning]

**Anti-patterns that degrade GPT-5.x reasoning performance** [reasoning-model-anti-pattern-prescribed-reasoning]:

| Pattern | What to do instead |
|---------|-------------------|
| Explicit chain-of-thought: "First, think step by step…" | State goal + constraints; let the model reason |
| Few-shot worked examples | State the principle; trust GPT-5.x to generalize |
| Self-consistency prompting | Trust single-pass output |
| Least-to-most decomposition scaffolding | State the full problem; the model decomposes internally |
| Skeleton-of-thought | Let the model choose its output structure |

**Replacement pattern:** Goal + Constraints + Context. This is the cross-model-family portable
instruction style. [reasoning-model-anti-pattern-prescribed-reasoning]

**Declarative vs. procedural:** For interactive skills, declarative (outcome-based) outperforms
imperative step-by-step. Exception: unattended/scheduled routines in the sandbox benefit from
numbered SOP steps and explicit completion signals. [hands-off-routine-prompt-precision-pattern]

---

## Translation From Portable Format

| Portable field | Codex equivalent | Notes |
|---------------|----------------|-------|
| `name` | `name` in SKILL.md frontmatter | Same; use in directory naming |
| `description` | `description` in SKILL.md frontmatter | Same; routing behavior — Unknown |
| `license` | `license` | Include for standard compliance |
| `compatibility` | `compatibility` | Declare sandbox requirements here |
| `metadata` | `metadata` | Include for standard compliance |
| `allowed-tools` | `allowed-tools` | Unknown Codex support; include anyway |
| Body prose | SKILL.md body | Direct port; sandbox-proof the instructions |
| `when_to_use` (Claude Code ext.) | N/A | Remove; no routing extension |
| `paths` (Claude Code ext.) | Unknown equivalent | Verify |
| `disable-model-invocation` | N/A | Remove; encode as body instruction |
| Dynamic shell injection `!`cmd`` | N/A | Remove; resolve content statically |
| `context: fork` / `agent:` | N/A | Remove; no fork execution model |
| `hooks` | N/A | Remove |

**AGENTS.md translation:**
For project-level context (equivalent to CLAUDE.md), write to `AGENTS.md` instead.
Use the symlink strategy to serve both Claude Code and Codex from the same source:
`AGENTS.md -> CLAUDE.md`. [universal-harness-context-via-symlink]

---

## Known Gaps / Verify

- **SKILL.md catalog routing:** Whether Codex implements description-based LLM catalog routing
  (analogous to Claude Code's eager-description / lazy-body model) is not confirmed by findings.
- **`allowed-tools` support:** Whether Codex processes `allowed-tools` frontmatter to constrain
  tool invocations is not covered.
- **SKILL.md install path:** The exact directory path Codex expects for skill files is not
  covered; verify against current OpenAI Codex docs.
- **Sandbox permission levels:** The precise capabilities available in Codex's sandboxed
  environment (filesystem read/write scope, network access, package installs) are not detailed
  in findings.
- **Hot reload / live change detection:** Whether Codex watches skill directories for changes
  mid-session (as Claude Code does) is unknown.
- **GPT-5.x exact model IDs:** Verify current model identifier strings at
  https://platform.openai.com/docs/models before referencing them in any configuration.

---

## Example

Minimal SKILL.md for Codex (sandbox-safe; declarative style; no Claude Code extensions):

```markdown
---
name: code-quality-review
description: |
  Reviews code for quality issues: correctness, maintainability, security, and test coverage.
  Use when asked to review a file, PR, or function for quality, correctness, or best practices.
  Key capabilities: static analysis interpretation, security anti-pattern detection, test gap identification.
license: MIT
compatibility: "Codex CLI sandboxed environment; filesystem read access required; no network needed."
---

## Purpose

Provide a structured quality review for the submitted code. This skill exists to catch
issues early — before review fatigue or deadline pressure leads to shallow checks.

## Review Dimensions

Assess the code across four dimensions, in this order:

1. **Correctness** — Does the logic handle edge cases (empty inputs, type coercions, error paths)?
2. **Security** — Are there injection risks, unvalidated inputs, or leaked secrets?
3. **Maintainability** — Is the code readable, is complexity locally bounded, are concerns separated?
4. **Test coverage** — Are the critical paths covered? Are error branches tested?

Work through all four dimensions before synthesizing; do not stop at the first issue found,
because coverage gaps and security issues are often more important than style issues.

## Constraints

- Report findings, do not auto-apply fixes. The user decides which fixes to accept.
- Rank findings by severity: Critical / High / Medium / Low.
- Do not flag style issues as High unless the style causes correctness risk.

## Output Format

```
## Code Quality Review: <filename>

### Critical
- <finding> — <one-sentence rationale>

### High
- ...

### Summary
<2–3 sentence synthesis of the most important action items>
```
```

---

## Provides (capability inventory — §4.2 requires × provides)

What this platform supplies against the controlled capability vocabulary
(`../references/capability-vocabulary.md`). **Provisional:** drafted from this staged
profile, which itself carries "Unknown — verify" flags; re-verify rows against current
OpenAI Codex docs before a port relies on them (L-10 discipline).

| Capability | Provides | How / note |
|---|---|---|
| `durable-document-store` | **native** | Repo filesystem inside the sandbox |
| `internal-document-search` | **native** | Filesystem search within the sandboxed repo |
| `workspace-file-inventory` | **native** | Repo tree enumeration |
| `connector-source-discovery` | absent | Sandboxed execution; no connector surface documented |
| `versioned-checkpoints` | partial | git where the sandbox permits — verify permissions |
| `change-detection` | partial | git status/diff where the sandbox permits |
| `script-execution` | partial | Sandboxed; filesystem/network access restricted relative to Claude Code — verify |
| `fresh-context-scoring` | absent | No documented subagent surface — verify against current docs |
| `human-approval-channel` | **native** | Interactive CLI chat |
| `reference-bundle-attachment` | partial | Whether on-demand L3 file reading is supported is unverified |
| `byproduct-store` | partial | Workspace directory by convention; no platform-defined lifecycle |
