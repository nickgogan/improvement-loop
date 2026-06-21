---
name: Claude Code Skill Frontmatter Extensions (Beyond the Open Standard)
summary: |-
  Claude Code extends the Agent Skills open standard (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`) with a large set of Claude Code-specific frontmatter fields: `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `disallowed-tools`, `model`, `effort`, `context`, `agent`, `hooks`, `paths`, `shell`. Skills authored against these extensions don't run elsewhere; skills authored against the open standard run everywhere. The trade-off is portability vs. harness-level expressiveness.
implementation_notes: "Important fields by function: triggering (when_to_use, paths), invocation control (disable-model-invocation, user-invocable), argument shape (argument-hint, arguments), tool access (allowed-tools, disallowed-tools), runtime (model, effort, context, agent, hooks, shell). String substitutions available in body: $ARGUMENTS, $ARGUMENTS[N], $N, $name (via arguments: list), ${CLAUDE_SESSION_ID}, ${CLAUDE_EFFORT}, ${CLAUDE_SKILL_DIR}. Indexed args use shell-style quoting (multi-word values need quotes). Including 'ultrathink' anywhere in skill content requests deeper reasoning."
category: Agent Design
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-claude-code-skills-docs.md"
related_findings:
  - file: "skill-md-frontmatter-as-discovery-trigger-primitive.md"
    rel: "extends"
  - file: "skill-frontmatter-validation-rules.md"
    rel: "contradicts"
  - file: "skill-invocation-control-side-effect-guard.md"
    rel: "extends"
  - file: "skill-forked-subagent-execution.md"
    rel: "extends"
  - file: "skill-dynamic-context-injection-shell-prerender.md"
    rel: "extends"
  - file: "skill-cross-surface-portability-with-constraints.md"
    rel: "same-problem"
proposals: null
date_discovered: '2026-06-11'
last_updated: '2026-06-11'
pipeline_status: raw
consumed_by: []
---

# Claude Code Skill Frontmatter Extensions

## What It Is

The Agent Skills open standard at agentskills.io defines six frontmatter fields (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`). Claude Code adds a substantial set of harness-specific extensions:

| Field | Function | Notes |
|---|---|---|
| `name` | Display name in skill listings | Defaults to directory name |
| `description` | What the skill does + when to use it | Recommended; uses first paragraph if omitted |
| `when_to_use` | Additional trigger context (phrases, examples) | Appended to description; counts toward 1,536-char cap |
| `argument-hint` | Autocomplete hint shown when typing the command | e.g., `[issue-number]` |
| `arguments` | Named positional args for `$name` substitution | Space-separated string or YAML list |
| `disable-model-invocation` | Block Claude auto-loading | Use for side-effect skills |
| `user-invocable` | Toggle visibility in `/` menu | Default true |
| `allowed-tools` | Pre-approved tools | Doesn't restrict availability, just skips approval |
| `disallowed-tools` | Remove tools from pool while skill active | Cleared on next message |
| `model` | Override session model for skill | Resumes session model on next prompt |
| `effort` | Override effort level | `low`/`medium`/`high`/`xhigh`/`max` |
| `context` | Set to `fork` for subagent execution | Pairs with `agent:` |
| `agent` | Subagent type when `context: fork` | Built-in `Explore`/`Plan`/`general-purpose`, or custom |
| `hooks` | Skill-lifecycle hooks | Per-skill scope |
| `paths` | Glob patterns gating activation | Skill only loads when working with matching files |
| `shell` | `bash` (default) or `powershell` | PowerShell on Windows + env var |

Body-level substitutions: `$ARGUMENTS`, `$ARGUMENTS[N]`, `$N` shorthand, `$name` (when declared in `arguments`), `${CLAUDE_SESSION_ID}`, `${CLAUDE_EFFORT}`, `${CLAUDE_SKILL_DIR}`.

## Why It Matters

The extensions encode a sophisticated harness-level skill runtime. Each field corresponds to an operational property that the open standard intentionally doesn't specify, leaving it to vendor implementations. For builders inside Claude Code, the extensions are the difference between a basic skill (description-triggered, runs in main conversation) and a fully-shaped operational primitive (path-gated, model-overridden, side-effect-guarded, subagent-forked, hooks-instrumented).

The trade-off is explicit and named in the agentskills.io spec via the `compatibility` field: "Designed for Claude Code (or similar products)" can be declared, but the spec doesn't enforce which extensions a target supports. A skill that uses `context: fork + agent: Explore` is silently a Claude Code-only skill.

The Claude Code frontmatter surface is itself the §Construction substrate for building skills tightly coupled to Claude Code's harness — separate from the portable open-standard substrate.

## Why People Are Using It

Built into Claude Code. The bundled skills (`/run`, `/verify`, `/code-review`, `/debug`, `/loop`, `/claude-api`, etc.) use the extensions extensively. Every example in the canonical Claude Code skills docs leverages at least one Claude Code-specific field. Plugin authors targeting Claude Code can use all extensions; plugin authors targeting the open standard for cross-vendor portability must restrict to the six standard fields.

## Potential Alternatives

Open-standard-only skills (portable but lacking expressiveness). External configuration files (heavier — skill behavior split across multiple files). Tool-call-based composition (the skill could call Claude Code's APIs at runtime — fragile). Per-skill helper subagents that wrap the skill with the extra behavior (more files, more drift).

## Potential Improvements

A formal "portability tier" annotation in the open standard ("this skill requires extensions X, Y, Z"). Progressive enhancement so a skill works degraded on surfaces without all fields. Spec-level convergence — bringing high-utility extensions like `paths` and `disable-model-invocation` into the open standard. Better authoring guidance on when to use which extension (currently the docs list them but don't sequence them).

## Potential Failure Modes

**Portability surprise.** A skill that "just worked" in Claude Code fails silently on Claude.ai because `context: fork` isn't recognized — the skill loads as a regular content blob.

**Extension overlap.** `disable-model-invocation` overlaps with permission deny rules (`Skill(name)`) and with `skillOverrides`. The same effect can be achieved three ways with subtly different semantics; debugging which one is in force requires checking multiple surfaces.

**Field interaction surprises.** `disable-model-invocation: true` removes the description from Claude's context — `when_to_use` is effectively dead text. `user-invocable: false` plus `disable-model-invocation: true` makes the skill unreachable from any actor.

**Substitution escape rules.** `\$1.00` escapes `$1`; `\\$1` doesn't (leaves both backslashes, still expands). Footgun in prose.

**Tool field permissivity.** `allowed-tools` pre-approves tools without prompting — for a skill with broad `allowed-tools` checked into a repo, accepting the workspace trust dialog grants the skill that authority.

**`paths` over-restriction.** A skill gated to specific file patterns silently won't auto-load when working on adjacent files; users see "the skill isn't triggering" and may not realize it's the path gate.
