---
title: "opencode -- Structural Analysis"
id: "opencode-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-07-11"
updated: "2026-07-12"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "opencode"
analyzed_version: "dev branch HEAD (2026-07-11)"
analyzed_date: "2026-07-11"
repo_url: "https://github.com/anomalyco/opencode"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# opencode -- Structural Analysis

## Metadata
- **Repo:** https://github.com/anomalyco/opencode
- **Version analyzed:** dev branch HEAD `34e5809` (2026-07-11)
- **Date:** 2026-07-11
- **Spectrum position:** study — primary reference harness for tool/harness-design and loop-engineering dimensions; Claude Code comparison point for the agentic-OS harness layer

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | 6,181 |
| Total directories | 752 |
| Markdown files | 146 `.md` + 627 `.mdx` (docs site) |
| Code files (by language) | ~3,050 — TS 2,463; TSX 579; Astro 8; plus SQL 88 |
| Config/YAML/JSON files | ~362 (JSON 323 + YML 33 + TOML 6) |
| MD-to-code ratio | ~1:21 counting `.md` only; ~1:4 counting the `.mdx` docs site |
| Max directory depth | 9 levels below repo root |

Notable asset mass: 1,251 SVG + 218 PNG + 90 audio files (mp3/aac) — themes, docs-site assets, and product sounds; this is a consumer product repo, not just a CLI.

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Agent definitions / agent guidance | ~10 | root `AGENTS.md` + `.opencode/agent/*`; nested AGENTS.md in packages |
| Commands/skills | ~15 | `.opencode/command/`, `.opencode/skills/` (dogfooding surface) |
| Workflows/orchestration | ~12 | `specs/` (spec-driven development artifacts) |
| Reference docs (shared knowledge) | 2 load-bearing | root `CONTEXT.md` (32k — architecture/context reference), `STATS.md` |
| Human documentation | ~110 | 24 root README translations, CONTRIBUTING, SECURITY, package READMEs; `packages/docs/` carries the 627-file `.mdx` docs site |
| Other | ~10 | `.github/`, glossary (`.opencode/glossary/`) |

Unlike agent-framework repos where markdown is the codebase, opencode's product logic is TypeScript; its markdown surface is (a) the dogfooding context layer (`.opencode/`, AGENTS.md, CONTEXT.md, specs/) and (b) a large human docs site.

### Directory Naming Conventions
Lowercase kebab-case package names under `packages/` (~30 packages: `opencode`, `tui`, `server`, `sdk`, `plugin`, `protocol`, `schema`, `llm`, `codemode`, `session-ui`, `desktop`, `app`, `cli`, `slack`, `enterprise`, `identity`, ...). Dot-config convention for the agent surface (`.opencode/` with role-named subdirs: `agent/`, `command/`, `glossary/`, `plugins/`, `skills/`, `themes/`, `tool/`). Monorepo tooling: Bun + turbo + SST/infra.

### Top-Level Structure
```
packages/            # ~30-package TS monorepo (opencode = brain; tui, server, sdk,
│                    #   plugin, protocol, schema, llm, desktop, app, slack, enterprise...)
.opencode/           # dogfooding agent surface: agent/ command/ glossary/ plugins/
│                    #   skills/ themes/ tool/
specs/               # spec-driven development artifacts
AGENTS.md            # repo agent guidance (8.7k)
CONTEXT.md           # architecture/context reference for agents (32k)
STATS.md             # repo stats doc
infra/ nix/ script/ sdks/ patches/ perf/ artifacts/ github/ .github/
README.{24 locales}.md
```

### Code Surface Outline (optional — ast-grep)
Skipped — ast-grep unavailable on this machine (size gate would have passed: ~3,050 code files ≥ 200; the outline pass would have helped on a repo this size — noted per Rule 11). Find-based inventory above is the baseline.

### Notable Structural Patterns
- **Dual root context files with divided labor:** `AGENTS.md` (behavioral rules for agents) + `CONTEXT.md` (32k architecture reference) — the repo ships a large curated context document specifically for agents working on it.
- **`.opencode/` as self-hosted agent surface** — the product's own config-dir convention, dogfooded in its own repo with agents, commands, skills, custom tools, plugins, glossary, and themes.
- **`specs/` directory at root** — spec-driven workflow artifacts as first-class repo citizens.
- **24 localized READMEs** at root — community scale signal.
- **88 SQL files** — embedded persistence (sessions/state) is schema-managed, not ad-hoc.

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|---|---|---|---|---|---|
| `AGENTS.md` (root, ~8.7k) | LLM (contributors read too) | Project | Auto-loaded (system context) | Constraints/Rules + Workflow | Repo law: SDK regen commands, package dependency direction, branch/commit conventions, dense TS style guide (inline-over-helpers, no destructuring/aliased imports, early returns, Drizzle snake_case), test/typecheck rules, plus a "V2 Session Core" section of architectural invariants distilled from CONTEXT.md |
| `CONTEXT.md` (root, 32k) | LLM+Human (domain spec) | Project | Referenced only — NOT auto-loaded here (see Loading Strategy) | Memory/State + Constraints | DDD-style ubiquitous-language document for the v2 session runtime: ~30 glossary terms each with explicit `_Avoid_:` anti-terms ("System Context", not "system prompt"; "Context Epoch", "Session Drain"), ~110 relationship invariants, client-contract architecture, example dev/domain-expert dialogue, flagged ambiguities |
| `.opencode/agent/triage.md` | LLM | Task (CI agent) | Auto-loaded as agent prompt | Identity + Tool Usage | Hidden primary agent (`hidden: true`, gpt-5.4-mini), all tools denied except custom `github-triage`; encodes team-routing ownership rules (TUI/Desktop/Core/Inference/Windows) |
| `.opencode/agent/duplicate-pr.md` | LLM | Task (CI agent) | Auto-loaded as agent prompt | Identity + Tool Usage | Hidden agent (haiku), single tool `github-pr-search`, duplicate-PR detection with strict output contract |
| `.opencode/command/commit.md` | LLM | Task | Injected on `/commit` | Workflow | Commit+push workflow; embeds live `` !`git diff` ``/`git status` shell output into the prompt; runs as `subtask: true` on kimi-k2.5 |
| `.opencode/command/learn.md` | LLM | Task | Injected on `/learn` | Workflow + Memory | Session→AGENTS.md memory distillation: extract non-obvious learnings, place at the deepest applicable directory, 1–3 lines each, explicit include/exclude criteria |
| `.opencode/command/rmslop.md` | LLM | Task | Injected | Workflow | De-slop pass: remove AI-typical comments, defensive try/catch, `any` casts, emoji from branch diff |
| `.opencode/command/{ai-deps,changelog,issues,spellcheck,translate}.md` | LLM | Task | Injected | Workflow | Dep-bump report (fan out subagents per dep), changelog generation (pinned model gpt-5.4), issue search (haiku), md spellcheck, parallel docs translation (opus, references glossary) |
| `.opencode/glossary/README.md` + 16 locale files (`ja.md`, `zh-cn.md`, …) | LLM | Task (translation) | Referenced by translate workflow | Constraints | Per-locale do-not-translate terms, preferred terms tables, tone guidance; README defines the template and sourcing rules (backed by community PRs) |
| `.opencode/skills/effect/SKILL.md` | LLM | Tool/Task | Chain-loader (skill tool; name+description advertised in system context) | Tool Usage + Rules | Effect v4 skill: instructs agent to **clone `effect-smol` into `.opencode/references/`** and answer only from source, never memory; testing patterns |
| `.opencode/tool/{github-triage,github-pr-search}.ts` | Code (LLM-facing via tool schema) | Tool | Registered custom tools (disabled by default in `opencode.jsonc`, enabled per-agent) | Tool Usage | TypeScript custom tools backing the two CI agents |
| `.opencode/opencode.jsonc` | Harness | Project | Auto-loaded config | Constraints + Memory | Declares `references` (effect-smol repo, `~/.local/share/opencode` logs dir) injected into system context as `<available_references>`; disables triage tools globally |
| `.opencode/{plugins,themes}/`, `tui.json`, `env.d.ts` | Human/Harness | Project | Config | — | TUI smoke-test plugin + theme; dev tooling, not LLM context |
| `specs/project.md`, `specs/tui-package.md`, `specs/storage/*.md`, `specs/v2/*.md` (10 files, up to 843 lines) | Both | Project (design) | Referenced | Workflow + Constraints | Design-spec workspace for the v2 rebuild: API sketches, port instructions (`specs/v2/instructions.md` = how to port services core-ward with plugin hooks), status tables, and `specs/v2/todo.md` — a launch checklist with human owner names |
| `packages/opencode/AGENTS.md` (131 lines) | LLM | Package | Chain-loaded on file read | Rules + Tool Usage | DB schema locations, tmux recipe for running the TUI dev server non-blockingly, module-shape rule (no `export namespace`, self-reexport pattern) |
| `packages/llm/AGENTS.md` (321 lines) | LLM | Package | Chain-loaded | Rules | Effect/HTTP conventions, constructor placement ("Two ways to construct the same thing is one too many"), test rules |
| `packages/schema/AGENTS.md` (88 lines) | LLM | Package | Chain-loaded | Constraints | Package boundary law: dependency direction, what may/may not live in Schema, V1 naming |
| `packages/opencode/src/session/llm/AGENTS.md` (90 lines) | LLM | Folder | Chain-loaded | Constraints | Adapter-layer boundary notes with embedded file-structure map |
| `packages/core/src/tool/AGENTS.md` (59 lines) | LLM | Folder | Chain-loaded | Constraints | "One canonical tool representation"; forbids second registries/executors |
| 9 more nested `AGENTS.md` (`app`, `app/e2e/performance`, `codemode`, `desktop`, `effect-drizzle-sqlite`, `stats`, `opencode/test`, `opencode/test/server`, `server/routes/instance/httpapi`) | LLM | Package/Folder | Chain-loaded | Rules | Scope-local notes, some one-liners (`stats`: how to start dev server; `app`: "NEVER try to restart the app") |
| `STATS.md` | Human | — | Not loaded | — | Daily download-count table appended by `stats.yml` CI; not LLM-facing |
| Built-in prompts `packages/opencode/src/agent/prompt/*.txt`, `src/session/prompt/*.txt` | LLM | Global (product) | Compiled into binary | Identity + Workflow | Provider-family base prompts (anthropic/gpt/codex/gemini/kimi/beast/trinity/meta), `plan-mode.txt` (5-phase plan workflow), `build-switch.txt`, plan reminders |

### Sampling Notes
Read fully: root AGENTS.md, CONTEXT.md, both `.opencode/agent/` files, 3 of 8 commands (+ heads of remaining 5), effect SKILL.md, glossary README, `opencode.jsonc`, `tui.json`, `specs/project.md`, `specs/v2/instructions.md`, heads of `specs/v2/todo.md`, 6 nested AGENTS.md read in full or head-sampled. Classified by pattern: 16 locale glossary files (uniform per README template), remaining specs (classified from line counts + v2/instructions + todo), remaining nested AGENTS.md (uniform scope-local-rules shape). Code evidence read fully: `packages/opencode/src/session/instruction.ts`, `src/session/system.ts`, `src/session/llm/request.ts` (assembly), `src/agent/agent.ts` (built-in agents), plan tool prompts, `.github/workflows/triage.yml`, `opencode.yml`.

### Context Loading Strategy

**Runtime assembly** (evidence: `packages/opencode/src/session/llm/request.ts:58-66`, `src/session/prompt.ts:1256-1268`, `src/session/instruction.ts`, `src/session/system.ts`). System prompt = join of, in order:
1. **Base persona**: custom agent's `prompt` if set, else a **provider-family prompt selected by model-ID substring match** (`SystemPrompt.provider` — claude→anthropic.txt, gpt-4/o1/o3→beast.txt, codex→codex.txt, gemini→gemini.txt, kimi→kimi.txt, default.txt fallback).
2. **Environment block**: model ID, `<env>` (cwd, worktree, git, platform, date) + `<available_references>` rendered from `opencode.jsonc` `references`.
3. **Instruction files** (`Instruction.system()`), each wrapped `Instructions from: <path>`: (a) *global* — first-existing of `~/.config/opencode/AGENTS.md` then `~/.claude/CLAUDE.md` (Claude-compat, flag-disableable), **break after first hit**; (b) *project* — walk up cwd→worktree for `AGENTS.md`, then `CLAUDE.md`, then `CONTEXT.md` (marked `// deprecated`); **first filename that matches wins and stops the fallback chain** (so in this repo, root CONTEXT.md is *not* auto-loaded — root AGENTS.md shadows it; CONTEXT.md is a referenced spec); (c) `config.instructions` globs (~ expansion) and **remote HTTP URLs fetched with 5s timeout**.
4. **MCP server instructions**, permission-filtered per agent.
5. **Skills index** — names+descriptions only; bodies load via the permission-checked `skill` tool (chain-loading).
6. Per-message `user.system` override. A plugin hook `experimental.chat.system.transform` may mutate; the first element is kept separate to preserve the provider cache prefix.

**Lazy nested context**: `Instruction.resolve` fires when the agent *reads any file* — it walks upward from that file to the project root and attaches every `AGENTS.md`/`CLAUDE.md` found, deduplicated three ways (already in system paths, already loaded earlier in the transcript via tool metadata, already claimed for this message). Directory-scoped rules cost zero tokens until the agent actually touches that subtree.

**Dogfooding surface**: root AGENTS.md (global law) + 14 nested AGENTS.md (subtree law, grown by `/learn`) + CONTEXT.md/specs (deep domain language, referenced on demand) + `references` config pointing at the upstream Effect repo + the `effect` skill mandating source-verified answers. The v2 design itself (CONTEXT.md) formalizes all of this as "Context Sources" in a "System Context Registry" with durable "Context Epochs" for provider-cache stability and "Mid-Conversation System Messages" for in-flight context updates.

---

## 3. Workflow Topology

### Phases/Stages

Two interlocking workflows: the product's plan/build loop, and repo automation.

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|---|---|---|---|
| Build (default agent) | Session start / user accepts build switch | User switches agent; `plan_enter` suggestion accepted | Per-tool permission asks (allow/ask/deny ruleset) |
| Plan-enter suggestion | Model judges task complex; user mentions "plan" | User accepts/declines | **Yes** — tool asks user |
| Plan P1: Understanding | Plan mode active (`plan-mode.txt` system-reminder) | Codebase understood | `question` tool allowed for clarification |
| Plan P2: Design | P1 done | Design agent(s) return | No |
| Plan P3: Review | P2 done | Plan aligns with intent | Optional `question` |
| Plan P4: Write plan file | P3 done | Plan file complete (only editable file) | No |
| Plan P5: `plan_exit` | Plan finalized | User approves → build | **Yes** — approval gate; `build-switch.txt` reminder injected |
| Session drain (v2) | Prompt admitted durably (`session_input` row) | No continuation remains | Steer vs queue: steering prompts promote mid-drain; queued wait for idle |
| Compaction | Context overflow | New Context Epoch baseline rendered | No |
| CI: triage | Issue opened (non-team author) | Owner assigned | No (fully autonomous, single tool) |
| CI: `/oc` comment | Comment on issue/PR | Agent replies | Human invokes; `bash: deny` |

### Flow Diagram (ASCII)

```
                 USER PROMPT
                     |
              [admit durable input]
                     v
   +------------- BUILD (default) -------------+
   |  tool call -> permission ruleset          |
   |    allow ----------------- execute        |
   |    ask   --> USER GATE --> execute/deny   |
   |  complex task? --plan_enter--> USER GATE  |
   +-----------------|-------------------------+
                     v (accepted)
   +--------------- PLAN (edits denied except plan file) ---+
   | P1 Understand: <=3 explore subagents IN PARALLEL       |
   | P2 Design:     general subagent(s)                     |
   | P3 Review:     read critical files, question tool      |
   | P4 Write plan: .opencode/plans/*.md only               |
   | P5 plan_exit ------------------> USER GATE             |
   +--------------------------------------|-----------------+
                                          v approved
                     [build-switch system-reminder] --> BUILD
   ---------------------------------------------------------
   REPO AUTOMATION:
   issue opened --> triage.yml --> opencode run --agent triage
                                     (1 tool: github-triage)
   PR opened  --> duplicate-pr agent (1 tool: github-pr-search)
   "/oc" comment --> opencode GitHub Action (bash denied)
   session end --> /learn --> distill into nested AGENTS.md
```

### Transition Mechanisms
- **Tool-mediated mode switches with user consent**: `plan_enter`/`plan_exit` are tools whose effect is *asking the user* to switch agent; the switch injects a `<system-reminder>` (`build-switch.txt`) stating the new permission reality. Mode = agent = permission ruleset (`agent.ts`: plan agent denies `edit: *` except plan-file globs, denies `task: general` in P1 constraints).
- **Permission rulesets** are the enforcement layer under the prose: prompts describe the workflow, permissions make violations impossible.
- **v2 lifecycle** (CONTEXT.md): durable prompt admission → promotion at Safe Provider-Turn Boundaries → provider turns within a process-local Session Drain; context changes admitted lazily at boundaries as Mid-Conversation System Messages; compaction rolls a new Context Epoch.
- **Spec-driven development**: partial. `specs/` is a live design workspace (v2 rebuild) with port instructions and human-owned TODO lists, but root AGENTS.md encodes no spec-gated pipeline; specs feed agents as reference context, and distilled invariants get promoted into AGENTS.md ("V2 Session Core" section).

### Parallelism
- Plan P1 mandates up to **3 explore subagents launched in parallel** ("single message, multiple tool calls"), with sizing heuristics; P2 launches design subagents.
- Built-in subagents: `general` ("execute multiple units of work in parallel", todowrite denied), `explore` (read-only permission mask, caller specifies thoroughness), `compaction`.
- Commands encode fan-out: `ai-deps.md` ("use subagents for each dep to save your context window"), `translate.md` ("translate all languages in parallel").
- CI agents run concurrently per-event; each is a single-tool, deny-all-else agent.

---

## 4. Governance Model

### Constraint Expression

| Mechanism | Location | Enforcement | Example |
|---|---|---|---|
| Permission ruleset (allow/ask/deny per permission-key × wildcard pattern) | `packages/core/src/v1/config/permission.ts` (schema), `packages/opencode/src/permission/index.ts` (engine) | Hard — every tool calls `ctx.ask()` before acting; `deny` raises `PermissionDeniedError` back into the model transcript | `"permission": { "bash": { "git push *": "ask", "*": "allow" } }` |
| Per-agent permission overrides (+ deprecated per-agent `tools` boolean map, normalized into permissions) | `packages/core/src/v1/config/agent.ts` (`normalize()` maps `tools: {edit:false}` → `permission.edit = "deny"`) | Hard — merged into the ruleset per session: `Permission.merge(input.agent.permission, input.session.permission)` in `packages/opencode/src/session/tools.ts:87` | `agent.plan` config with `edit: "deny"` |
| Subagent permission derivation | `packages/opencode/src/agent/subagent-permissions.ts` | Hard — parent's `deny` + `external_directory` rules propagate; `task`/`todowrite` denied by default unless subagent ruleset grants them | `deriveSubagentSessionPermission()` |
| Tool visibility filtering | `packages/opencode/src/permission/index.ts` (`disabled()`, `visibleTools()`) | Hard — tools with a blanket `deny` on pattern `*` are removed from the model's tool list entirely, not just blocked at call time | `disabled(["edit","write","apply_patch"], ruleset)` |
| Bash command-prefix normalization | `packages/opencode/src/permission/arity.ts` + `packages/opencode/src/tool/shell.ts:388-410` | Hard — shell commands are AST-parsed (real bash/PowerShell parser), each node reduced to an LLM-generated arity dictionary prefix (`git checkout main` → `git checkout`), matched against wildcard rules | `ARITY = { git: 2, "npm run": 3, ... }` |
| External-directory guard | `packages/opencode/src/tool/shell.ts:262-277`, `external_directory` permission key | Hard — path arguments in shell commands resolved; anything outside the project triggers a separate `external_directory` ask | `patterns: [dir + "/*"]` |
| Doom-loop breaker | `packages/opencode/src/session/processor.ts:372` | Hard — repeated identical tool calls trigger a `doom_loop` permission ask (configurable to allow/deny) | `permission: "doom_loop", patterns: [toolName]` |
| Env-var / remote policy injection | `OPENCODE_PERMISSION` env (`packages/opencode/src/config/config.ts:545`); `.well-known/opencode` remote config (`config.ts:360`) | Hard — deep-merged over local config, enabling CI and org-level override | enterprise URL serves `remote_config` JSON |
| Experimental policy engine (v2) | `packages/core/src/policy.ts`, `experimental.policies` in `packages/core/src/config/experimental.ts` | Hard — IAM-style `{action, resource, effect}` statements, last-match-wins, currently gating provider access | `Policy.evaluate(action, resource, fallback)` |
| Repo: AGENTS.md style/architecture rules | `AGENTS.md` (root) | Soft (advisory to agents) except where CI mirrors them | "Client runtime code may depend on Schema and Protocol but never Core or Server" |
| Repo: pre-push hook | `.husky/pre-push` | Hard locally — pins Bun version to `packageManager` field, runs `bun typecheck` | |
| Repo: CI gates | `.github/workflows/test.yml`, `typecheck.yml`, `pr-standards.yml`, `compliance-close.yml` | Hard — PR-standards bot labels non-compliant PRs `needs:compliance`; a cron closes them after 2 hours | `compliance-close.yml` runs every 30 min |
| Repo: contribution scope boundary | `CONTRIBUTING.md` | Hard-ish (socially + bot-enforced) — "any UI or core product feature must go through a design review with the core team"; "PRs that ignore these guardrails will likely be closed" | |

### Guardrail Patterns

- **Last-match-wins wildcard evaluation with safe default.** `evaluate()` in `packages/opencode/src/permission/index.ts:28` does `findLast` over merged rulesets and falls back to `{action: "ask"}` when nothing matches — unknown territory always escalates to the human. Config key order is deliberately preserved (`propertyOrder: "original"` comment in `packages/core/src/v1/config/permission.ts`) so users express precedence positionally, like firewall rules.
- **Two-tier bash governance.** Commands are parsed with a real shell parser, then (a) each command's full source becomes the ask pattern, and (b) the arity-dictionary prefix + `" *"` becomes the "always allow" pattern — so "always allow" generalizes to the human-meaningful command family, not the exact string. The arity dictionary itself was LLM-generated (prompt is preserved as a comment in `arity.ts:11-23`).
- **Rejection carries semantics into the loop.** Three distinct error types in `packages/core/src/v1/permission.ts`: `DeniedError` (rule-based; the message quotes the relevant rules to the model), `RejectedError` (human said no), `CorrectedError` (human said no *with feedback text* that is injected back as steering). Rejecting one request cascades: all other pending asks in the same session are auto-rejected; approving with "always" auto-approves matching pending asks.
- **Deny shrinks the surface, not just the gate.** A blanket `deny` removes the tool from the model's advertised toolset (`visibleTools()`), preventing wasted attempts; `Permission.evaluate("task", agentName, ...)` similarly filters which subagents are even listed (`packages/opencode/src/tool/registry.ts:263`).
- **Subagent privilege containment.** Deny rules are inherited downward but allow rules are not — a subagent's capabilities come from its own config; recursion (`task`) and `todowrite` are denied by default.
- **No OS sandboxing.** No bwrap/seatbelt/seccomp/landlock anywhere. "Sandboxes" in `packages/opencode/src/project/project.ts` are just extra directories a project is permitted to touch. Isolation is delegated to the permission layer + the user's environment; worktrees provide workspace isolation, not security isolation.
- **Repo governance is automated and time-boxed.** `pr-standards.yml` (skips team members via `.github/TEAM_MEMBERS`) labels non-compliant PRs; `compliance-close.yml` closes them after a 2-hour grace window — governance-as-cron rather than maintainer attention.

### Permission Model

Config schema (`packages/core/src/v1/config/permission.ts`, abridged):

```ts
export const Action = Schema.Literals(["ask", "allow", "deny"])
export const Object = Schema.Record(Schema.String, Action)   // pattern -> action
export const Rule = Schema.Union([Action, Object])
const InputObject = Schema.StructWithRest(
  Schema.Struct({
    read: Rule?, edit: Rule?, glob: Rule?, grep: Rule?, list: Rule?,
    bash: Rule?, task: Rule?, external_directory: Rule?,
    todowrite: Action?, question: Action?, webfetch: Action?, websearch: Action?,
    lsp: Rule?, doom_loop: Action?, skill: Rule?,
  }),
  [Schema.Record(Schema.String, Rule)],   // open-world: MCP tools, plugins
)
// whole field may also be a single Action string, normalized to {"*": action}
```

**Verdict set:** `allow | ask | deny` in config; at ask-time the human replies `once | always | reject` (reply schema surfaced via `Permission.reply`), where `reject` optionally carries a correction message, and `always` appends runtime `allow` rules to session state. So the effective outcomes are: allow, allow-once, allow-always (persisted for session), deny-by-rule, reject, reject-with-feedback.

**Enforcement flow:** config (global → project `opencode.json` → `OPENCODE_PERMISSION` env → remote `.well-known/opencode`) is flattened via `Permission.fromConfig()` into an ordered ruleset → per-agent rulesets merge in agent-level `permission`/legacy `tools` → at tool execution, each tool's `execute()` calls `ctx.ask({permission, patterns, always})` (`packages/opencode/src/session/tools.ts:81-89` wires `ctx.ask` → `Permission.ask` with `ruleset: merge(agent.permission, session.permission)`) → `evaluate()` per pattern: any `deny` → `DeniedError` immediately; all `allow` → proceed silently; otherwise publish `permission.asked` event, park on a `Deferred`, and block the tool until UI/API reply. The check is *inside* each tool, pre-side-effect (e.g. `shell.ts` asks after parsing but before spawning; `edit.ts` after computing the diff but before writing). A plugin hook `"permission.ask"` (`packages/plugin/src/index.ts:261`) can programmatically force `allow/deny/ask`, making the permission layer extensible middleware.

**Per-agent overrides:** any agent in `config.agent.<name>.permission` gets its own ruleset (built-ins: `plan`, `build`, `general`, `explore`, plus arbitrary named agents, `packages/core/src/v1/config/config.ts:93-106`); subagents additionally pass through `deriveSubagentSessionPermission`.

**Other governance-relevant config fields** (`packages/core/src/v1/config/config.ts`): `tools` (global boolean enable/disable per tool), `share: "manual"|"auto"|"disabled"`, `disabled_providers` / `enabled_providers` (model-provider allowlist), `agent.<n>.steps` (max agentic iterations before forced text-only), `experimental.primary_tools` (tools restricted to primary agents), `experimental.continue_loop_on_deny`, `experimental.policies` (IAM-style statements), `enterprise.url` (remote org config source), `mcp` (per-server enable). Enterprise package itself (`packages/enterprise/src/core/share.ts`, `storage.ts`) is structurally thin — self-hosted share/storage, with org policy delivered via the `.well-known/opencode` remote-config channel rather than a dedicated policy service. `packages/identity` is brand assets only.

**Explicit vs implicit:** product-level governance is highly explicit and centralized (one permission engine, one schema). Repo-level governance is split: explicit hard gates in CI (typecheck, tests, PR-standards bot, compliance cron) and an explicit but advisory `AGENTS.md` that is unusually deep — it encodes architectural invariants (dependency direction between packages, V2 session-core semantics at `AGENTS.md:151-161`) as prose rules for agents, effectively a constitution for contributing agents with no automated enforcement of the architectural clauses.

---

## 5. Cross-Agent Protocol

### Agent Roster

| Agent/Role | Defined In | Capabilities | Communicates With |
|---|---|---|---|
| **build** (default primary) | `packages/opencode/src/agent/agent.ts` (native) | All tools per configured permissions; `plan_enter` allowed | User; spawns any subagent via `task` tool |
| **plan** (primary) | same | Read/search only — `edit: deny` except `.opencode/plans/*.md`; `plan_exit` allowed; `task.general` denied | User; explore subagent |
| **general** (subagent) | same | Full toolset minus `todowrite`; multi-step research/execution | Parent session only (task result) |
| **explore** (subagent) | same | Deny-all baseline + grep/glob/list/bash/read/webfetch/websearch; read-only external dirs | Parent session only |
| **compaction** (hidden primary) | same + `agent/prompt/compaction.txt` | No tools; summarizes history | Invoked by loop as in-history task |
| **title** / **summary** (hidden primary) | same + `prompt/title.txt`, `prompt/summary.txt` | No tools; small-model metadata generation | Forked from loop step 1 |
| **triage** (custom, hidden) | `.opencode/agent/triage.md` | Deny-all except custom `github-triage` tool; routes issues to 5 teams | GitHub via custom tool |
| **duplicate-pr** (custom, hidden) | `.opencode/agent/duplicate-pr.md` | Only `github-pr-search`; dup detection on PR open | GitHub via custom tool |
| User-defined agents | `opencode.jsonc` `agent{}` / `.opencode/agent/*.md` frontmatter (`mode`, `model`, `tools`, `steps`, `permission`) | Overlay onto permission defaults; `mode: primary\|subagent\|all` | Per mode |

An agent in opencode is **a named permission ruleset + optional prompt/model override** — build vs plan are pure permission diffs over one loop, not separate code paths. `Agent.generate` (`agent/agent.ts:368`) even LLM-generates new agent configs from a description.

### Handoff Mechanisms

- **`task` tool** (`packages/opencode/src/tool/task.ts`): parent creates a *child session* (`sessions.create({parentID, agent, permission})`) with permissions derived via `deriveSubagentSessionPermission` plus injected denies (`todowrite`, nested `task`). Child gets **fresh context** — only the prompt string (with `@file` references resolved into file parts); no history inheritance. Model inherits from the parent's current assistant message unless the agent pins one. Result = child's last text part, returned wrapped in `<task id state><task_result>...` XML.
- **Task resume**: `task_id` parameter continues a prior child session with its context intact — persistent subagent identity.
- **Background subagents** (flag-gated): child runs as a `BackgroundJob`; completion is **injected into the parent as a synthetic user message**, re-triggering the parent loop.
- **Subtask parts**: a user message can carry `subtask` parts; the loop pops them as tasks (`prompt.ts:1144`) and runs `handleSubtask` before normal processing.
- **Compaction as handoff-to-self**: compaction is queued as a *part in the message history* (`tasks.pop()` → `compaction.process`), i.e., control flow is serialized into the durable transcript.

### Shared State

- **SQLite via Drizzle** (`packages/core` `database/`, `session/sql.ts`): sessions, messages, parts are DB rows; the loop re-reads `MessageV2.filterCompactedEffect` each iteration — the transcript *is* the state machine.
- **Snapshots** (`processor.ts:102`, `snapshot.track()`): file-state snapshots captured before stream start and at each `step-start`/`step-finish`, enabling revert (`session/revert.ts`).
- **Permission rulesets stored on session rows** — child sessions carry their derived ruleset.
- **Todo list, background-job registry, run-state** (`session/run-state.ts`) as service-level shared state; events broadcast over the server bus to all clients.

### Coordination Patterns

**Hub-and-Spoke** (primary agent → task-tool subagents, results funneled back as tool output) layered over **Event-Driven** client fan-out (server publishes session/part events; TUI, desktop, web, Slack all subscribe). No peer-to-peer agent communication; subagents cannot spawn subagents by default (nested `task` denied).

### Harness Architecture Deep-Dive

#### Monorepo package map

| Package | Role |
|---|---|
| `packages/opencode` | **The brain**: agent loop, agents, tools, permissions, MCP, LSP, plugin host, server routes |
| `packages/core` | Effect-based kernel: SQLite/Drizzle DB, v1 schemas, models.dev catalog, git/fs/shell utils, event system |
| `packages/llm` | Provider-agnostic LLM layer: `LLMRequest`/`LLMEvent` schema, native wire protocols per provider, cache policy |
| `packages/protocol` / `packages/schema` | HTTP API + base schema definitions (Effect `httpapi`) — the typed seam |
| `packages/server` | Standalone server composition of core + protocol |
| `packages/sdk` / `packages/client` | Generated clients: legacy JS SDK from `openapi.json` (1.1 MB); `client` generated from protocol (`sdk-next` composes them) |
| `packages/plugin` | Public plugin API surface (Hooks, `tool()`, auth/provider hooks) |
| `packages/tui` | TypeScript terminal UI (solid-style components), talks to server via SDK |
| `packages/desktop` / `packages/app` / `packages/web` | Electron shell / shared web app / site+docs |
| `packages/cli` | Secondary CLI (`lildax`) |
| `packages/slack` / `packages/enterprise` | Slack bot via SDK; Teams/cloud offering |
| `packages/codemode` | "Effect-native confined code execution over schema-described tools" — code-as-tool-calls (`tool/code-mode.ts` consumer) |
| `packages/session-ui`, `ui`, `storybook` | Shared session-rendering components |
| `console`, `function`, `identity`, `containers`, `stats`, `http-recorder`, `httpapi-codegen`, `effect-drizzle-sqlite` | Cloud infra (SST), telemetry, codegen support |

Dependency law (root `AGENTS.md`): Schema → Core/Protocol → Server; Client may depend on Schema+Protocol but **never** Core or Server.

#### Agent-loop anatomy

`packages/opencode/src/session/prompt.ts` — `runLoop` (line 1081) is the whole harness:

1. **Init**: set session status busy; reload messages from DB filtered to post-compaction window.
2. **Exit check**: break when last assistant finished with a non-`tool-calls` reason, has no pending tool calls, and postdates the last user message (orphaned interrupted tools explicitly excluded).
3. **In-history tasks**: pop `subtask` → spawn child session; pop `compaction` → summarize (hidden compaction agent) then optionally auto-continue.
4. **Overflow trigger**: if tokens ≥ `usable` (= input limit − reserved buffer, default `min(20_000, maxOutput)`; `session/overflow.ts:8`), queue auto-compaction and loop.
5. **Context assembly**: `SessionReminders.apply`, system = environment + instructions + MCP instructions + skills; `agent.steps` budget — on last step, `MAX_STEPS_PROMPT` is injected *as an assistant message*.
6. **Model call**: `SessionTools.resolve` (agent permissions × registry × MCP × plugins), optional `StructuredOutput` pseudo-tool with `toolChoice: "required"` for JSON-schema output; `processor.handle.process` consumes the `LLMEvent` stream.
7. **Repeat/exit**: process returns `"stop" | "compact" | "continue"`; content-filter finishes surfaced as errors; after exit, `compaction.prune` trims old tool outputs.

```ts
// prompt.ts:1088 (abridged)
while (true) {
  yield* status.set(sessionID, { type: "busy" })
  let msgs = yield* MessageV2.filterCompactedEffect(sessionID)
  const { user: lastUser, assistant: lastAssistant, tasks } = MessageV2.latest(msgs)
  if (lastAssistant?.finish && !["tool-calls"].includes(lastAssistant.finish)
      && !hasToolCalls && lastUser.id < lastAssistant.id) break
  const task = tasks.pop()
  if (task?.type === "subtask") { yield* handleSubtask({...}); continue }
  if (task?.type === "compaction") {
    if ((yield* compaction.process({...})) === "stop") break; continue
  }
  if (lastFinished && (yield* compaction.isOverflow({ tokens, model }))) {
    yield* compaction.create({ sessionID, auto: true }); continue
  }
  // ... assemble system/tools, handle.process(stream), break|continue
}
```

**Streaming processor** (`session/processor.ts`): per-event handling of `tool-call`/`tool-result`/`step-start`/`step-finish`; snapshot per step; usage/cost accrual; **doom-loop breaker** — 3 consecutive identical tool calls (same name + JSON-identical input) escalates to `permission.ask("doom_loop")` (lines 29, 356–380) rather than erroring.

**Retry** (`session/retry.ts`): Effect `Schedule` policy; honors `retry-after(-ms)` headers, else exponential 2s×2ⁿ capped at 30s; 5xx always retryable; `ContextOverflowError` never retried; typed retry reasons drive UI actions (upsell/rate-limit banners).

#### Tool contract

`packages/opencode/src/tool/tool.ts`: `Tool.define(id, { description, parameters: EffectSchema, execute(args, ctx) → { title, metadata, output, attachments? } })`. `ctx` carries `sessionID`, `messageID`, `agent`, `abort`, `ask()` (permission request), `metadata()` (live progress). Schema-validation failures become `InvalidArgumentsError` whose `message` getter *is the model-facing correction prompt*. A wrapper auto-truncates output (spilled to a file, `metadata.outputPath`). Descriptions live in sibling `.txt` files. Registry (`tool/registry.ts`): shell, edit, apply_patch, write, read, glob, grep, task, todo, webfetch, websearch, lsp, skill, question, plan_enter/plan_exit, code-mode, invalid. Custom tools: `.opencode/tool/*.ts` export `tool({ description, args: zodShape, execute })` from `@opencode-ai/plugin/tool` — a deliberately simpler Promise/zod contract than the internal Effect one.

#### Plugin API surface

`packages/plugin/src/index.ts`: a plugin is `(input) => Promise<Hooks>` where **input includes an SDK client to the local server** (`client`, `serverUrl`, `$` BunShell, project/worktree). Hooks: `event`, `config`, `tool{}`, `auth` (full custom OAuth/API-key flows per provider), `provider.models` injection, `chat.message` / `chat.params` / `chat.headers`, `permission.ask` (override allow/deny), `tool.execute.before/after`, `tool.definition` (rewrite descriptions/params sent to the LLM), `shell.env`, `command.execute.before`, plus experimental transforms for messages, system prompt, compaction prompt, compaction auto-continue, and completed text.

#### Provider abstraction

Two layers mid-migration: `packages/opencode/src/provider/provider.ts` (76 KB) loads the **models.dev catalog** (`@opencode-ai/core/models-dev`) for model metadata/limits/costs, with `transform.ts` (56 KB) holding per-provider quirks, still bridging Vercel AI SDK types; `packages/llm` is the newer native layer — hand-rolled wire protocols per provider (`providers/anthropic.ts`, `openai.ts`, `amazon-bedrock.ts`, `google.ts`, `azure.ts`, `github-copilot.ts`, `openrouter.ts`, `xai.ts`, `openai-compatible.ts`) over a canonical `LLMRequest`/`LLMEvent` schema. Auth: `provider/auth.ts` + plugin `auth` hooks (OAuth device/code flows, e.g., GitHub Copilot, OpenAI OAuth special-cased in `agent/agent.ts:386`).

#### Client/server protocol seam

Everything is client/server: `packages/opencode/src/server/` exposes an Effect `HttpApi` (route groups: `session`, `event`, `permission`, `question`, `pty`, `tui`, `provider`, `config`, `mcp`, `project`, `workspace`, `global`, `sync`, `control-plane`, `experimental` — `server/routes/instance/httpapi/groups/`), with websocket event streaming (`websocket-tracker.ts`) and mDNS discovery. `packages/protocol` defines the API; `bun run generate` in `packages/client` regenerates typed clients; `packages/sdk/openapi.json` feeds the legacy SDK. TUI, desktop, web app, Slack bot, enterprise, *and plugins* are all peers on this one seam.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | High | Read-triggered lazy chain-loading of 14 nested AGENTS.md (zero-token until subtree touched, triple-deduped); `/learn` as the memory write-path; first-filename-wins shadowing (AGENTS.md shadows CONTEXT.md); `references` config → `<available_references>` block; Context Epoch / Mid-Conversation System Message model for cache-safe dynamic context; skills index as names+descriptions with permission-checked body loading |
| Model Selection | Medium | models.dev catalog for metadata/limits/costs; provider-family base-prompt selection by model-ID substring; per-command pinned models (haiku for issue search, opus for translation, kimi for commits); default-on cache policy with documented 1.25×/0.1× breakpoint math |
| Prompt Craft | Medium | Provider-family prompt variants (anthropic/beast/codex/gemini/kimi); `rmslop` de-slop command; schema-validation errors whose message *is* the model-facing repair prompt; MAX_STEPS budget injected as assistant message |
| Tool Integration | High | Two-tier tool contracts (internal Effect Schema vs plugin zod/Promise); plugin hooks spanning the whole loop (permission.ask, tool.execute.before/after, tool.definition rewrite, system-prompt transform); plugins receive the same SDK client as the TUI; auto-truncation with file spill; codemode (code-as-tool-calls) |
| Intent Engineering | Medium | `CorrectedError` — rejection-with-feedback as steering; plan_enter/plan_exit user-consent gates; `question` tool; doom-loop escalation to human |
| Orchestration | Medium-High | task-tool child sessions with fresh context + task_id resume (persistent subagent identity); background subagents completing as synthetic user messages; plan P1 mandates ≤3 parallel explore subagents; nested task denied by default; hub-and-spoke only |
| Evaluation | Medium | Doom-loop breaker (3 identical calls → permission ask); per-step file snapshots enabling revert; CI agents (triage, duplicate-pr) as single-tool deny-all-else evaluators; typed retry reasons driving UI actions |
| Sandboxing | Low | **Explicitly none** — no bwrap/seatbelt/seccomp anywhere; "sandboxes" are just extra permitted directories; isolation delegated to the permission layer and user environment. High-signal contrast with omnigent |
| Governance | High | Central permission engine (allow/ask/deny × wildcard patterns, last-match-wins, ask-on-no-match); LLM-generated arity dictionary for bash generalization; deny-shrinks-toolset; asymmetric subagent inheritance (denies flow down, allows don't); env/remote org config injection; experimental IAM-style policy engine; automated time-boxed PR compliance |
| Agent Design | High | Agent = named permission ruleset + optional prompt/model override (mode-as-policy); hidden single-tool CI agents; `Agent.generate` LLM-authors agent configs; frontmatter-defined custom agents in `.opencode/agent/` |
| Agentic Systems | Medium-High | One protocol seam serving TUI/desktop/web/phone/Slack/plugins; transcript-as-state-machine (SQLite; control flow serialized as message parts — crash-safe by construction); session sharing; `.opencode/` as self-hosted dogfooding surface |

### Findings Candidates

Aggregated from the three dimension passes (context-workflow / harness-loop / governance). Promotion requires `/promote-findings` + Nick's gate.

1. **Read-triggered chain-loading of nested AGENTS.md** (Context Engineering) — instruction files attach lazily when the agent reads a file in their subtree, triple-deduped; scope-local rules cost nothing until relevant. `packages/opencode/src/session/instruction.ts:179-221`.
   → Skipped: single-source; partial existing coverage ([[monorepo-context-distribution-three-strategies]]) on 2026-07-12
2. **`/learn` as the memory write-path** (Context Engineering) — session learnings distilled into the *deepest applicable* AGENTS.md, 1–3 lines, hard include/exclude criteria; paired with (1), a complete file-based memory loop with zero new infrastructure. `.opencode/command/learn.md`.
   → Skipped: single-source; partial existing coverage ([[gsd-global-learnings-store-cross-session-persistence]]) on 2026-07-12
3. **Ubiquitous-language glossary with explicit anti-terms** (Context Engineering × Prompt) — ~30 domain terms each with `_Avoid_:` alternatives + ~110 relationship invariants keeping agent/human vocabulary converged during a rewrite. `CONTEXT.md`.
   → Promoted to [[ubiquitous-language-glossary-with-anti-terms]] on 2026-07-12
4. **Mode = agent = permission ruleset, with tool-mediated user-gated transitions** (Agent Design × Governance) — plan mode is an agent whose ruleset denies all edits except plan-file globs; `plan_enter`/`plan_exit` are tools that ask the user; enforcement backs the prose. `packages/opencode/src/agent/agent.ts:140-265`.
   → Folded into [[static-tool-set-mode-changes-as-callable-tools]] as independent cross-harness corroboration on 2026-07-12
5. **Context Epoch / Mid-Conversation System Message model** (Context Engineering) — immutable baseline system context for provider-cache stability; context changes admitted only at safe boundaries as chronological system messages. `CONTEXT.md` §Relationships.
   → Folded into [[append-only-context-updates-system-reminder-injection]] as named independent implementation on 2026-07-12
6. **Transcript-as-state-machine** (Agentic Systems × Orchestration) — compaction and subtask directives stored as message parts and popped as tasks each loop iteration; the durable DB transcript is the loop's control flow, resumable by construction. `packages/opencode/src/session/prompt.ts:1142-1168`.
   → Skipped: single-source; partial existing coverage ([[session-as-append-only-event-log]]); O9↔C6 cross-repo same-problem link added to [[monitor-vs-loop-event-driven-vs-time-driven]] on 2026-07-12
7. **Doom-loop breaker as a permission, not an error** (Governance × Evaluation) — 3 identical consecutive tool calls escalate to `permission.ask("doom_loop")`; pathological loops become a human gate. `packages/opencode/src/session/processor.ts:356-380`.
   → Folded into [[loop-detection-hash-based-sliding-window]] as third response-strategy variant; also synthesized into [[permission-channel-as-escalation-steering-bus]] on 2026-07-12
8. **Default-on prompt-cache policy with documented breakpoint math** (Model Selection × Context) — cache hints auto-placed at last tool def / last system part / latest user message; cost math cited in comments. `packages/llm/src/cache-policy.ts`.
   → Folded into [[layered-prompt-assembly-stable-segment-caching]] (breakpoint heuristic + cost math; cross-linked to the 2026-07-11 caching cluster) on 2026-07-12
9. **Plugins are SDK clients** (Tool Integration) — plugins receive the same generated HTTP client as the TUI; every extension surface shares one wire-protocol seam. `packages/plugin/src/index.ts:56-75`.
   → Promoted to [[plugins-as-sdk-clients]] on 2026-07-12
10. **Two-tier tool contracts as complexity firewall** (Tool Integration) — internal Effect-Schema contract with typed repair-prompt errors vs deliberately minimal zod/Promise contract for user tools. `packages/opencode/src/tool/tool.ts` vs `packages/plugin/src/tool.ts`.
   → Promoted to [[two-tier-tool-contracts-complexity-firewall]] on 2026-07-12
11. **LLM-generated arity dictionary for bash permission generalization** (Governance) — "always allow" generalizes to the human-meaningful command family (`git checkout`, not `git checkout main`); generating prompt checked in as provenance. `packages/opencode/src/permission/arity.ts`.
   → Skipped: single-source; partial existing coverage ([[tiered-permission-system-bash-safety]]) on 2026-07-12
12. **Rejection-with-feedback as a first-class permission verdict** (Governance × Intent) — `CorrectedError` delivers the human's rejection message to the model as course-correction, unifying the permission gate and the steering channel. `packages/core/src/v1/permission.ts:13-19`.
   → Promoted (synthesized with O11+C7 per the convergence note) into [[permission-channel-as-escalation-steering-bus]] on 2026-07-12
13. **Deny-shrinks-toolset** (Governance) — blanket-denied tools removed from the advertised tool list; denied subagents filtered from task options; governance shapes the perceived capability surface. `packages/opencode/src/permission/index.ts:204-219`.
   → Promoted to [[deny-shrinks-toolset]] with `contradicts` link to [[static-tool-set-mode-changes-as-callable-tools]] (the batch's key tension) and O14↔C13 same-problem link to [[progressive-skill-loading]] on 2026-07-12
14. **Asymmetric subagent permission inheritance** (Governance × Orchestration) — denies and external-directory rules flow parent→child, allows do not; recursion denied by default. `packages/opencode/src/agent/subagent-permissions.ts`.
   → Skipped: single-source; partial existing coverage ([[permission-compounding-across-agent-delegation-chains]]) on 2026-07-12
15. **Time-boxed automated PR compliance** (Governance, repo-level) — bot labels non-compliant PRs; a 30-min cron closes them after a 2-hour window; team exemption via checked-in file. `.github/workflows/pr-standards.yml`, `compliance-close.yml`.
   → Promoted to [[time-boxed-automated-pr-compliance]] on 2026-07-12

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-07-11 | dev HEAD `34e5809` | all 5 + dimension mapping | Initial analysis. ast-grep outline pass skipped (unavailable); find-based fallback used. Mined as Claude Code comparison point per agentic-OS direction note. |
