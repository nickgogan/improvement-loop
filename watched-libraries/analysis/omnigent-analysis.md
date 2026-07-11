---
title: "Omnigent -- Structural Analysis"
id: "omnigent-analysis"
type: "analysis"
category: "upstream-tracking"
target_system:
  - "cross-system"
stage: "active"
created: "2026-07-11"
updated: "2026-07-11"
author: "improvement-loop"
source_dd:
  - "DD-45"
  - "DD-46"
tags:
  - "repo-analysis"
  - "watched-library"
  - "omnigent"
analyzed_version: "alpha (2026-07-11 HEAD)"
analyzed_date: "2026-07-11"
repo_url: "https://github.com/omnigent-ai/omnigent"
dimensions_analyzed:
  - "structural-inventory"
  - "context-file-map"
  - "workflow-topology"
  - "governance-model"
  - "cross-agent-protocol"
---

# Omnigent -- Structural Analysis

## Metadata
- **Repo:** https://github.com/omnigent-ai/omnigent
- **Version analyzed:** alpha, v0.6.0.dev0 (HEAD `6e3c778`, 2026-07-10)
- **Date:** 2026-07-11
- **Spectrum position:** study — shipped instance of the harness-layer + governance-first architecture the agentic-OS direction note formalizes

---

## 1. Structural Inventory

### File Tree Statistics
| Metric | Value |
|--------|-------|
| Total files | 2,980 |
| Total directories | 433 |
| Markdown files | 125 (incl. `CLAUDE.md` → `AGENTS.md` symlink) |
| Code files (by language) | 2,435 total — Python 1,783; TSX 287; TS 272; JS 41; Swift 19; Rust 19; Kotlin 14 |
| Config/YAML/JSON files | ~272 (YAML 141 + YML 67 + JSON 53 + TOML 11) |
| MD-to-code ratio | ~1:19 — markdown is supplementary, not the codebase |
| Max directory depth | 9 levels below repo root |

### Markdown Composition
| Purpose | Count | Directory |
|---------|-------|-----------|
| Agent definitions (AGENTS.md guidance) | 4 | root, `tests/e2e/`, `tests/integration/`, `omnigent/onboarding/agent/` |
| Commands/skills (SKILL.md) | ~34 | `.claude/skills/` (8 dev skills), `omnigent/onboarding/agent/skills/` (3 shipped), `examples/*/skills/` (8), `deploy/docker/` (1), test fixtures (~14) |
| Workflows/orchestration | 0 dedicated | workflow lives in code (`omnigent/runner/`, `server/`), not markdown |
| Reference docs (shared knowledge) | ~28 | `docs/` (15, incl. `POLICIES.md`, `AGENT_YAML_SPEC.md`, harness design docs), `designs/` (13 design proposals) |
| Templates (artifact schemas) | 1 | `.github/pull_request_template.md` |
| Human documentation | ~55 | root (README, CONTRIBUTING, RELEASING, SECURITY, CHANGELOG), `deploy/*` (19 backend READMEs), `web/`, `sdks/`, `editors/` |
| Other | ~3 | `.github/` misc |

Markdown is *supplementary* here: the product is a Python server/CLI + TS web client. The exceptions — where markdown IS behavior — are the SKILL.md surfaces (dev skills, shipped onboarding-agent skills, example-agent skills) and the four AGENTS.md guidance files.

### Directory Naming Conventions
Lowercase throughout; kebab-case for skill directories (`harness-integration-guide`), snake_case for Python modules (`native_policy_hook.py`), role-based top-level naming (`policies/`, `sandbox/`, `runner/`, `server/`, `entities/`). Per-harness code follows a strict `{harness}_native[_role].py` flat-file convention at package root rather than per-harness subdirectories.

### Top-Level Structure
```
omnigent/                  # Python package — the meta-harness
├── policies/              #   policy layer (builtins/, framework)
├── sandbox/               #   OS sandbox (bwrap/seatbelt) + backends
├── runner/ runtime/ host/ inner/  # execution stack
├── server/ db/ stores/    #   multi-user session server + persistence
├── entities/ spec/        #   agent/session domain model, YAML agent spec
├── llms/ tools/ client_tools/ terminals/ repl/ onboarding/ ...
├── {claude,codex,cursor,opencode,goose,hermes,kimi,kiro,pi,qwen,antigravity}_native*.py
web/                       # TS/React client (+ electron, ios, android)
sdks/                      # python-client, ui
examples/                  # 5 YAML example agents (debby, polly, remy, scribe, sentinel)
deploy/                    # 16 sandbox/hosting backends (modal, daytona, e2b, k8s, databricks, ...)
docs/ designs/             # reference docs + design proposals
.claude/skills/            # 8 dev-facing skills for working ON omnigent
tests/ dev/ scripts/ editors/
```

### Code Surface Outline (optional — ast-grep)
Skipped — ast-grep unavailable on this machine (size gate would have passed: 2,435 code files ≥ 200; the outline pass would have helped on a repo this size — noted per Rule 11). Find-based inventory above is the baseline.

### Notable Structural Patterns
- **Per-harness flat-file families.** Each supported harness gets a family of root-level modules split by role: `_native` (integration core), `_native_bridge`, `_native_forwarder`, plus optional `_permissions`, `_hook`, `_state`, `_status`, `_credentials`, `_app_server`. Eleven harness families visible at package root — the abstraction seams are literally readable from the file listing.
- **`CLAUDE.md` is a symlink to `AGENTS.md`** — single-source agent guidance served under both harness conventions.
- **Deploy matrix as directories.** 16 `deploy/<backend>/` directories, each self-contained with its own README — the sandbox-backend abstraction mirrored in repo layout.
- **Examples as YAML agents.** Each example (`debby`, `polly`, `remy`, `scribe`, `sentinel`) is a YAML agent definition + `skills/` folder — the data-driven actors model shipped as fixtures.
- Version singleton (`omnigent/version.py`) synced from `pyproject.toml` by a pre-commit hook.

---

## 2. Context File Map

| File Path | Audience | Scope | Mechanism | Content Type | Summary |
|---|---|---|---|---|---|
| `AGENTS.md` (root; `CLAUDE.md` = symlink) | LLM | Project | Auto-loaded (harness convention) | Constraints/Rules | Contribution law for any coding agent working on omnigent: pre-commit before commit, PR-template discipline (Summary/Test Plan/Demo checkboxes), comment style ("scenario, not the PR"). No architecture — pure process rules. |
| `tests/e2e/AGENTS.md` | LLM | Task (directory) | Auto-loaded (dir-scoped) | Tool Usage / Workflow | How to run the real-server, real-LLM e2e suite: credentials (Databricks profile vs OpenAI key), env-var stripping pitfall, and an explicit rule to ALWAYS run suites backgrounded with an `until grep` polling loop inside Claude Code. |
| `tests/integration/AGENTS.md` | LLM | Task (directory) | Auto-loaded (dir-scoped) | Tool Usage | Per-harness journey suite invocation: `--integration` opt-in gate, one harness per run via `--harness`, CI matrix mapping. |
| `.claude/skills/*/SKILL.md` (8 dev skills) | LLM | Task | Chain-loader (Claude Code Skill trigger on description) | Workflow/Process + Tool Usage | E2E dev/verify loops for working ON omnigent. Six are per-harness "spin up live server + exercise harness X" recipes (pi-native, antigravity-native, antigravity-sdk, cursor-sdk, copilot-sdk, polly); `cli-setup-verify` is a PTY-sandboxed before→fix→after verification loop; `harness-integration-guide` is a pure reference (feature matrix + checklist for new harness integrations). Descriptions name the exact source files that trigger them. |
| `omnigent/onboarding/agent/AGENTS.md` | LLM | Global (shipped agent's system prompt) | Injected (spec parser resolves as `instructions`) | Identity/Persona + Workflow + Constraints | Full constitution of the shipped onboarding agent (`omnigent create`): 6-step conversational workflow, dual access-mode detection (shell vs sandbox) with a "never explain which mode you're in" rule, mandatory `validate_agent` gate, prose-over-bullets communication style. |
| `omnigent/onboarding/agent/skills/*/SKILL.md` (3) | LLM | Task | Chain-loader (`load_skill` tool) | Memory/Reference (omnigent-knowledge, 409 lines), Process (detect-framework), Templates (build-omnigent) | The onboarding agent's on-demand knowledge tier: platform reference, framework→executor mapping, agent-directory generation templates. |
| `examples/*/skills/*/SKILL.md` (8: debby/debate; polly/investigate+fanout+cross-review; scribe/api-docs+changelog+migration-guide; sentinel/security-audit) | LLM | Task | Chain-loader (`load_skill` or harness-native Skill tool) | Workflow/Process | Behavioral procedures for shipped example agents. Polly's three are a delegation protocol (see §3 Parallelism); sentinel's is report-only ("never fix"). |
| `omnigent/runtime/prompt.py` | LLM (via code) | Global (per-agent) | Injected (code assembly) | Identity + Tool Usage hint | `build_instructions()`: spec.instructions + per-request instructions + a skill name/description menu — the menu injected ONLY if `load_skill` is among tool schemas. Fallback: "You are a helpful assistant." |
| `web/src/lib/designModePrompt.ts` | LLM (via code) | Task (one message) | Injected (ordinary user message + screenshot attachment) | Tool Usage / context block | Builds a fenced `[Design Mode — …]` element-context block; every DOM-derived field is sanitized (control chars stripped, 200-char clamp) so a hostile page can't forge block lines. |
| `docs/` (15 md) | Human | Project | Referenced | Workflow + design records | User guides (POLICIES.md, AGENT_YAML_SPEC.md, deploy) plus design docs (harness-bench, QWEN_NATIVE_DESIGN, queue-steer). |
| `docs/claude/antigravity-rpc-spike-notes.md` | Both | Task | Referenced | Memory/State | Persisted Claude-session spike notes — an LLM-session findings archive kept in-repo. |
| `deploy/docker/SKILL.md` | LLM | Task | Chain-loader | Tool Usage / Workflow | Docker-compose deploy procedure; documents the two-image split (server "external runner only" vs `omnigent-host` sandbox image). |
| `omnigent/spec/AGENTSPEC.md` | Both | Project | Referenced | Constraints/Rules | Ships inside the package: canonical agent-directory contract (`config.yaml` + optional `AGENTS.md` + `skills/`). |

Excluded: `tests/resources/**/SKILL.md` (13 files) — test fixtures, not real context.

### Sampling Notes
Read in full: root `AGENTS.md`, onboarding `AGENTS.md`, `cli-setup-verify` (~60 lines), `polly/fanout`, `prompt.py`, `designModePrompt.ts`, README, POLICIES.md intro + trust model, `tests/e2e|integration/AGENTS.md` heads, `deploy/docker/SKILL.md` head. Frontmatter-only (classified by uniform pattern): the other 7 dev skills, 3 onboarding skills, 7 example skills. The six `*-e2e-dev` skills are structurally uniform (verified via descriptions + line counts 176–293); their bodies were inferred from the two exemplars.

### Context Loading Strategy
**(a) Developers' agents working on omnigent:** three-tier. Tier 1: root `AGENTS.md` auto-loads (harness-agnostic — `CLAUDE.md` mirrors it, and omnigent's own parser priority shows the same neutrality). Tier 2: directory-scoped `AGENTS.md` in `tests/e2e/` and `tests/integration/` load only when working there. Tier 3: 8 heavyweight verification skills chain-load on demand; their descriptions enumerate exact trigger files (`omnigent/inner/pi_native_executor.py`, …), making activation deterministic. Net effect: the always-on layer is ~40 lines of process rules; everything expensive is pull-based.

**(b) Shipped onboarding agent:** the agent-directory pattern eating its own dogfood — `AGENTS.md` becomes the system prompt via the spec parser, and its three skills are a paged knowledge base loaded via `load_skill` (409-line platform reference never enters context unless needed).

**(c) User YAML agents at runtime:** `omnigent/spec/parser.py:57` resolves missing `instructions:` by scanning `("AGENTS.md", "CLAUDE.md", ".cursorrules")` — first file wins, no merge. `omnigent/runtime/prompt.py:build_instructions()` then concatenates: base instructions → per-request instructions → skill menu, where the menu is injected only when the executor exposes a `load_skill` tool (harnesses with native skill support, e.g. Claude SDK, get no duplicate hint). `LoadSkillTool` (`omnigent/tools/builtins/load_skill.py`) merges bundle skills with host-scope discovery (`.claude/skills/`, `.agents/skills/`, `~/.claude/skills/`, `~/.agents/skills/`, gated by `skills_filter`). **Policies are never in the prompt** — they are enforced out-of-band by the policy engine; path containment in `omnigent/inner/loader.py:_read_contained_file` blocks `instructions: ../../etc/passwd` in uploaded bundles.

---

## 3. Workflow Topology

### Phases/Stages

| Phase | Entry Trigger | Exit Condition | Human Gate? |
|---|---|---|---|
| Install | `curl \| sh` / uv / brew | CLI on PATH, deps verified | No |
| Credential setup | First run / `omnigent setup` | Provider default set (ambient keys auto-detected and offered) | Yes — pick/confirm credential |
| Agent definition | `omnigent create` (onboarding agent) or hand-written YAML | `config.yaml` passes `validate_agent` | Yes — approve plan before file writes; iterate until satisfied |
| Session run | `omnigent` / `omnigent <harness>` / `omnigent run agent.yaml` | Session ends / turn budget | Per-policy |
| Policy gate (inside run loop) | Any of 6 enforcement phases (REQUEST/RESPONSE per turn; tool_call/tool_result etc. per invocation) | ALLOW / DENY / ASK→user verdict | Yes on ASK — turn parks as an elicitation until approved/refused |
| Server + host deploy | `omnigent server start` + `omnigent host` / Docker compose | Server reachable; machine registered as host | Admin sign-in |
| Collaboration | Share link / `omnigent attach` / `omnigent run --fork` | Teammate co-drives or forks | Invite-only signup gate |
| Upgrade | `omni upgrade` | Drains in-flight sessions, then restarts on new version | `--force` overrides drain |

**Onboarding agent sub-workflow** (`omnigent/onboarding/agent/AGENTS.md`): understand goal → (optional) `detect-framework` skill → plan structure + approval → generate via `build-omnigent` templates → `validate_agent` (mandatory, server-side, same parser as production) → iterate → export + print run commands. Gates: plan approval ("ask before writing"), validation loop-until-clean, user satisfaction.

### Flow Diagram (ASCII)

```
install --> setup creds --> [define agent]------------------------+
                             |  omnigent create                   | hand YAML
                             |  goal->detect->plan*->build        |
                             |  ->validate(loop)->export          |
                             +----------------+-------------------+
                                              v
   +-------------------- SESSION RUN LOOP ------------------------+
   | user msg -> [REQUEST policies] -> LLM turn -> tool call?     |
   |                |ASK                 |        [tool_call      |
   |                v                    |         policies]      |
   |         park elicitation            |   ALLOW|DENY|ASK*      |
   |         (server-owned) <------------+        |               |
   |         user verdict -> resume/deny          v               |
   |              [RESPONSE policies] <-- tool_result             |
   +--------------------------------------------------------------+
        | session policies > agent policies > server policies
        v
 server/host deploy --> share / co-drive / attach / fork
                                            (* = human gate)
```

### Transition Mechanisms
- **CLI verbs** move between lifecycle phases (`setup`, `create`, `run`, `server start`, `host`, `attach`, `login`, `upgrade`).
- **Policy verdicts** are the intra-loop transition: three-verdict lattice (ALLOW/DENY/ASK), declaration-order evaluation, DENY short-circuits; three stacking levels evaluated session→agent→server (stricter session rules first) — `docs/POLICIES.md`, `omnigent/spec/types.py:1074` (Phase enum, "six points in the agent loop").
- **Dual-evaluation ASK escalation**: the runner-side gate (`omnigent/runner/policy.py`) fast-paths ALLOW/DENY locally, but ASK is escalated by re-POSTing to the server (`evaluate_policy=True`), which owns the elicitation channel; the runner awaits via `runner.pending_approvals`. DENY feeds refusal text back as the tool output so the LLM "sees the refusal cleanly."
- **Validation gate as tool**: `validate_agent` runs server-side with the production parser — passing it *is* the load guarantee.
- **File-mediated state** in polly: `.polly/registry.json` records worktrees, conversation_ids, PR URLs across turns.
- **Message-passing**: `sys_session_send` dispatches sub-agents; results return asynchronously via `sys_read_inbox`; `sys_cancel_task` for runaway workers.

### Parallelism
- **Polly fanout** (`examples/polly/skills/fanout/SKILL.md`): one git worktree + one sub-agent per parallel-safe task, each from a possibly different vendor, each opening its own PR. Protocol: dispatch the entire batch in one turn, then END TURN — no polling; workers notify via inbox. A per-turn dispatch cap is *enforced by policy* (not prompt honor); excess tasks go in waves. Cross-review routes each diff to a different-vendor reviewer; polly never merges — the human does.
- **Debby**: static two-head parallelism — every question fans to Claude + GPT simultaneously; `/debate` adds adversarial rounds before synthesis.
- **Multi-user sessions**: share (watch+chat), co-drive (teammate's messages execute on your machine), fork (`omnigent run --fork <id>`) — divergent parallel continuation from a common prefix.
- **Dev-side**: `cli-setup-verify` explicitly supports "several agents concurrently on separate worktrees"; e2e suite runs `-n 8` backgrounded per its AGENTS.md.

---

## 4. Governance Model

### Constraint Expression

| Mechanism | Location | Enforcement | Example |
|---|---|---|---|
| Declarative policy attachment (YAML `guardrails.policies` / top-level `policies:`) | `omnigent/spec/types.py` (`GuardrailsSpec`, `PolicySpec`, `PhaseSelector`), parsed by `omnigent/spec/parser.py` | Hard — engine composes ALLOW/ASK/DENY per phase | `examples/polly/agents/claude_code/config.yaml` attaches `blast_radius` with `gate_pushes: false` |
| Python callable policies (`type: function`) | `omnigent/policies/function.py`, contract in `omnigent/policies/schema.py` | Hard — DENY short-circuits, ASK parks for approval | `omnigent.policies.builtins.safety.ask_on_os_tools` |
| LLM prompt-classifier policies | `omnigent/policies/builtins/prompt.py` (`prompt_policy` factory) | Hard, fail-closed — classifier error → DENY | `tests/_fixtures/agents/prompt-policy-demo/prompt-policy-demo.yaml` ("Deny if the user mentions Canada") |
| CEL expression policies | `omnigent/policies/builtins/cel.py` (`cel_policy` factory) | Hard | `expression: event.type == "tool_call" && event.data.name == "sys_os_shell"` |
| Guardrails labels + label-gate `condition:` | `omnigent/spec/types.py` (`LabelDef`, `PolicySpec.condition`) | Gating — non-matching policies skipped before dispatch | `tests/_fixtures/agents/e2e-label-ask-gate/e2e-label-ask-gate.yaml` (`condition: {tainted: "1"}`) |
| Cost budgets (session / per-user daily / subagent subtree) | `omnigent/policies/builtins/cost.py`; label namespace in `omnigent/cost_plan.py` | Hard DENY at hard cap (on "expensive models"), soft ASK at checkpoints | `cost_budget` with `max_cost_usd` + `ask_thresholds_usd` |
| Sandbox declaration + sandbox-forcing policy | YAML `os_env.sandbox` (`omnigent/spec/types.py`), `omnigent/cli_sandbox.py`, `safety.enforce_sandbox` in `omnigent/policies/builtins/safety.py` | Hard — `enforce_sandbox` intercepts the synthetic `__agent_start` tool call and overrides the agent's sandbox config | `examples/sentinel/config.yaml` (`sandbox: {type: none}` with a comment flagging "best-effort guardrails only") |
| Native-harness hook bridge | `omnigent/native_policy_hook.py` + `omnigent/claude_native_hook.py`, `codex_native_hook` | Hard on `PreToolUse` / `UserPromptSubmit`; observational on `PostToolUse` | `PreToolUse` → `hookSpecificOutput.permissionDecision`; `UserPromptSubmit` → `decision: "block"` |
| Handler allowlist (anti-injection) | `omnigent/policies/registry.py` (`is_registered_handler`) | Hard — unregistered dotted paths rejected at the policy write APIs and bundle upload | Blocks registering `subprocess.Popen` as a "policy" |

### Guardrail Patterns

- **Six-phase interception.** `Phase` enum (`omnigent/spec/types.py:1074`): `request`, `tool_call`, `tool_result`, `response`, `llm_request`, `llm_response`. Policies declare `on:` selectors, optionally tool-narrowed (`tool_call:code_sandbox`); function policies may omit `on:` and self-select by returning `None` (abstain).
- **Fail-closed asymmetry.** `FAIL_CLOSED_PHASES = ("PHASE_TOOL_CALL", "PHASE_REQUEST")` in `omnigent/policies/types.py:61` — pre-execution gates DENY when the policy server is unreachable; `tool_result` and the advisory LLM phases fail open (the side effect already happened). Enforced identically at `omnigent/runner/app.py:6442` and `omnigent/runtime/harnesses/_scaffold.py:651` from the one shared constant.
- **Label state machine.** Conversations carry schema'd labels (`LabelDef`: `initial` + allowed `values`); policies write labels through a per-policy `set_labels` whitelist, and other policies gate on them via `condition:` — enabling taint-style flows (fixture: `taint_on_banana` sets `tainted=1`, then `ask_when_tainted` fires an ASK on every subsequent request).
- **No side effects from a denied ASK.** Label writes and `state_updates` accumulated on an ASK path are applied only on approval (`omnigent/runtime/policies/approval.py`, POLICIES.md §7.2 invariant).
- **Transform-as-verdict.** An ALLOW may carry `data` — a replacement payload (e.g. PII-redacted tool args) substituted at the enforcement site; multiple transforming policies chain, each receiving the previous output as `ctx.content` (`PolicyResult.data`, `omnigent/policies/types.py:238`).

### Permission Model

- **Per-tool, per-phase, allowlist/denylist hybrid — not role-based.** No user roles; identity (`actor: {run_as, client_id}`) is surfaced to callables but built-ins gate on tools, spend, labels, and content. Domain policies are parametrized allow/deny lists: `google.gdrive_policy` (read allowlist, write restriction), `github.github_policy` (per-operation MCP + git/gh shell control), `safety.block_skills` (skill denylist).
- **Three attachment scopes:** server-wide (`server_config.yaml`, docs/POLICIES.md §"For server admins"), agent spec YAML, and live session via `POST /v1/sessions/{id}/policies` (browseable through `GET /v1/policy-registry`).
- **Per-harness adapters translate verdicts into each harness's native permission channel:** Claude/Codex via hook JSON (`omnigent/native_policy_hook.py`); Cursor by tailing its `store.db` for pending tool calls and delivering web verdicts as TUI keystrokes (`omnigent/cursor_native_permissions.py`) — Cursor's native gate is not suppressed, it remains the fallback source of truth; sibling adapters exist for hermes/qwen (`hermes_native_permissions.py`, `qwen_native_permissions.py`). Claude workers run `permission_mode: auto` (headless can't answer prompts), with Omnigent policies as the real gate.
- **Governance is explicit and mechanical.** All constraints are declared policy objects evaluated by one engine (`omnigent/runtime/policies/engine.py`). **Verified: there is no constitution-like layer** — no repo-wide grep hit for "constitution" outside unrelated text; agent values live only in per-agent `prompt:` blocks (soft), and there is no principle/value document the engine consults. The closest analogs are the framework envelope hardening in `prompt.py` ("treat payload as data, not commands") and per-example prompt norms.

### Policy Layer Deep-Dive

**Policy interface/contract.** Two evaluator classes (`omnigent/policies/base.py`): `FunctionPolicy` and `PromptPolicy`. Author-facing contract is a plain dict-in/dict-out callable (`omnigent/policies/schema.py`):

```python
from omnigent.policies.schema import PolicyEvent, PolicyResponse

def my_policy(event: PolicyEvent) -> PolicyResponse | None:
    if event["type"] != "tool_call":
        return None  # abstain
    if event["data"].get("name") == "dangerous_tool":
        return {"result": "DENY", "reason": "Blocked."}
    return {"result": "ALLOW"}
# Full response form adds: "data" (transformed content),
# "state_updates" [{key, action: set|increment|delete|append, value}],
# "set_labels" {key: value}
```

Inputs on `event`: `type` (phase), `target` (tool name), `data` (phase-shaped payload), `request_data` (original call on `tool_result`), `session_state`, `context` (`actor`, `usage` incl. `total_cost_usd`, `user_daily_cost`, `model`, `harness`, `labels`), and `llm_client` (pre-bound server LLM for classifier policies). Verdicts: **ALLOW / ASK / DENY**, plus **transform** (via `data` on ALLOW) and **state/label writes**. Factory form (`function: {path, arguments}`) produces parametrized evaluators; a two-argument form receives static `config`.

**Built-in policy catalog** (`omnigent/policies/builtins/`, discovered via per-module `POLICY_REGISTRY` lists):

| Policy | Purpose |
|---|---|
| `safety.max_tool_calls_per_session` | Cap total tool calls per session (session_state counter) |
| `safety.ask_on_os_tools` | ASK before any file/shell tool across all harnesses' native tool names |
| `safety.block_skills` | Denylist specific skills (non-native loaders + native Skill tool) |
| `safety.enforce_sandbox` | Force a sandbox config (e.g. `linux_bwrap`) at agent start |
| `safety.deny_pii_in_llm_request` | Regex-scan prompts/LLM requests for SSN/CC/email/phone |
| `cost.cost_budget` | Session spend cap: hard DENY on expensive models + soft ASK checkpoints |
| `cost.user_daily_cost_budget` | Per-owner UTC-day spend cap across all their sessions |
| `cost.subagent_cost_budget` | Subtree spend cap attached to child sessions (internal-only) |
| `github.github_policy` | Per-operation GitHub control (MCP + git/gh shell) |
| `google.gdrive_policy` / `gmail_policy` / `gcalendar_policy` | Workspace access control (read allowlists; Gmail default blocks send; Calendar default read-only) |
| `working_dir.block_working_dir_changes` | Gate `cd`/`pushd`/`git -C`/worktree escapes in shell commands |
| `risk_score.risk_score_policy` | Accrue per-session risk from risky calls + sensitivity labels; escalate |
| `routing.deny_trivial_to_expensive_model` | LLM-classify task triviality; deny expensive models for trivial work |
| `routing.intent_based_authorization` | Record first message as session intent; gate every tool call against it |
| `cel.cel_policy` | CEL-expression predicate policy |
| `prompt.prompt_policy` | LLM classifier from author's natural-language intent (fail-closed) |
| `context.detect_task_switch` | LLM-classify user messages for task switches |
| `orchestration.blast_radius` | Classify shell commands safe / risky (ASK) / catastrophic (DENY) |
| `orchestration.spawn_bounds` | Cap sub-agent dispatches per turn |
| `orchestration.headless_subagent_purpose_guard` | Require declared purpose (implement/review/explore/search) on every spawn |
| `orchestration.worktree_guard` | Block writes outside the worker's git worktree |
| `orchestration.read_only_os` | Deny all file-mutating tools (report-only agents) |

**Enforcement flow.** Two symmetric paths converge on one engine. (a) Omnigent-executed tools: the workflow's four enforcement sites (input, tool_call, tool_result, output) call `_enforce_policy` (`omnigent/runtime/policies/enforcement.py`) → `PolicyEngine.evaluate(ctx)` (`omnigent/runtime/policies/engine.py`): filter by `on:` selector → gate by `condition:` labels → dispatch each policy in YAML order → compose (DENY short-circuits with the deciding policy named; ASKs accumulate and merge into one elicitation; ALLOW chains transforms). (b) Native harnesses (Claude Code, Codex, Kimi): the executor bakes hook wrappers into the harness config; `PreToolUse`/`UserPromptSubmit` hooks POST to `POST /v1/sessions/{id}/policies/evaluate` (`omnigent/native_policy_hook.py`, with a 30 s retry budget then fail-closed DENY) and translate the verdict into the harness's own permission-decision output. ASK verdicts become MCP-style elicitations (`ElicitationRequest`, `omnigent/runtime/policies/approval.py`) surfaced in the web UI or terminal popup (`omnigent/native_cost_popup.py` renders cost ASKs into tmux panes); only `action: "accept"` maps to ALLOW — decline/cancel/timeout → DENY. `PostToolUse` is observational only.

**YAML attachment schema.** `guardrails:` (or legacy top-level `policies:`/`labels:`) with named policies keyed by name; fields: `type`, `on:` (phase selectors, optionally `phase:tool`), `condition:` (label gate), `function: {path, arguments}` (factory) or bare path, `set_labels:` whitelist, `ask_timeout:`. Real excerpt (`examples/polly/agents/claude_code/config.yaml`):

```yaml
guardrails:
  policies:
    blast_radius:
      type: function
      on: [tool_call]
      function:
        path: omnigent.inner.nessie.policies.blast_radius
        arguments:
          gate_pushes: false
```

Label-gated composition (`tests/_fixtures/agents/e2e-label-ask-gate/e2e-label-ask-gate.yaml`): `labels: {tainted: "0"}` + `label_schema` + a policy with `condition: {tainted: "1"}` producing `action: ask`.

---

## 5. Cross-Agent Protocol

### Agent Roster

| Agent/Role | Defined In | Capabilities | Communicates With |
|---|---|---|---|
| **Onboarding assistant** (built-in) | `omnigent/onboarding/agent/` (config.yaml, AGENTS.md, skills/, tools/) | Interviews user, detects existing frameworks, generates + validates agent images (`validate_agent`, `list_builtin_tools`) | User only |
| **Native-UI wrappers** (built-in, one per harness) | `omnigent/harness_plugins.py` (`NativeCodingAgent` records, e.g. `claude-native-ui`) | Terminal-first session binding a vendor TUI; internal wrapper name hidden from users (`native_coding_agents.py::public_agent_name`) | Web UI + local TTY |
| **polly** — coding orchestrator | `examples/polly/config.yaml` | claude-sdk brain; writes no code; plans, delegates, `spawn: true` for ad-hoc child sessions | 6 harness sub-agents |
| polly workers: `claude_code`, `codex`, `opencode`, `cursor`, `hermes`, `pi` | `examples/polly/agents/*/config.yaml` | Each binds one vendor harness (`claude-native`, `codex-native`, …, `pi` headless); implement/review/explore in own git worktree, opens own PR | polly (via inbox) |
| **debby** — debate moderator | `examples/debby/config.yaml` | claude-sdk brain, no substantive thinking; fan-out + cross-critique + synthesis | `claude` (claude-sdk), `gpt` (codex) responders |
| **scribe** — docs orchestrator | `examples/scribe/config.yaml` | Authors prose itself; delegates read-only investigation | `researcher` (claude-sdk), `reviewer` (codex) |
| **sentinel** — security reviewer | `examples/sentinel/config.yaml` | Report-only, never edits code | `scanner` (claude-sdk), `reviewer` (codex) |
| **remy** — memory assistant | `examples/remy/config.yaml` | Long-term memory, single agent | User only |

### Handoff Mechanisms

- **`sys_session_send`** — the core dispatch tool (`omnigent/runner/tool_dispatch.py`): creates or continues a sub-agent session keyed by (`agent`, `title`); repeated sends to the same title continue that thread (debby's debate loop relies on this). Payload = free-text task + optional `args` (purpose, model override, harness override, file_ids).
- **`sys_session_create`** — gated by `spawn: true` in the parent's config; lets an orchestrator launch an existing agent by id or author a brand-new agent config and launch it via `config_path` (polly).
- **Inbox, not polling** — sub-agents run autonomously and signal completion; the parent ends its turn after dispatching and is woken, then drains results with **`sys_read_inbox`** (`omnigent/tools/builtins/async_inbox.py`, "inbox-vs-poll flip", contract §Async work; gated by top-level `async:` flag, default true). `sys_session_get_history` is the debug fallback.
- **Human takeover** — native-harness workers run in real terminals; the human can open any worker in the UI Subagents panel and take over the TUI mid-task.

### Shared State

- **Server-side SQL stores** (`omnigent/stores/`: conversation, agent, artifact, file, permission, policy, comment stores over SQLAlchemy; `omnigent/db/db_models.py`, Postgres or SQLite lite tier) — the durable coordination point. Deploying the server (`deploy/README.md`) buys cross-device continuity ("sessions reachable from any device, including your phone") and teammate access; code and model keys stay on registered hosts.
- **Multi-user presence** — `omnigent/server/presence.py`: Google-Docs-style viewer circles scoped to the session *tree* root, so two users on different sub-agents of the same session see each other.
- **Filesystem rendezvous per harness** — bridge dirs (`/tmp/omnigent-<uid>/claude-native/`, `~/.omnigent/opencode-native/<hash>/state.json` + `auth.secret` + per-session XDG dirs) shared between runner, forwarder, hooks, and executor.
- **Orchestrator-level registries** — polly's `.polly/registry.json` (worktree, branch, conversation_id, PR URL per task); explicitly file-based, since sub-agents "have no shared memory of each other" (debate skill passes answers as text).

### Coordination Patterns

- **Hub-and-Spoke (dominant)** — polly/debby/scribe/sentinel are all a single "brain" dispatching to isolated workers; workers never talk to each other. Even debby's debate is hub-relayed cross-critique, not peer-to-peer.
- **Event-Driven** — completion flows through the async inbox (`async_work_complete` signal wakes the parent's drain); forwarders translate vendor SSE/hook events into a uniform session-event stream (`external_conversation_item` / `external_session_status` / `external_output_text_delta`).
- **Sequential Pipeline (embedded)** — polly's implement → deterministic gates → cross-review → fix-task loop per task (`examples/polly/skills/cross-review/SKILL.md`), with the hard rule that the reviewer must be a *different vendor* than the implementer and only surfaces issues, never fixes.
- Peer-to-Peer: absent by design (sub-agents isolated; allowlist-only `tools.agents`).

### Harness Abstraction Deep-Dive

**Per-harness file pattern and role split.** Each harness X at package root splits into:

- `X_native.py` — the CLI wrapper / agent-spec materializer: creates-or-binds an Omnigent session, launches the vendor CLI through the runner terminal-resource API, attaches the local TTY to the terminal WebSocket protocol (`claude_native.py` docstring).
- `X_native_bridge.py` — the rendezvous layer between the two live processes (resident vendor TUI/server ↔ Omnigent harness turn). Claude: filesystem bridge dir + an MCP stdio server Claude launches as a child (advertises `sys_*` tools) + **tmux send-keys** — web messages are literally typed into the user's pane (Channels MCP was blocked by org policy). OpenCode: bridge state file carrying loopback URL, auth secret, and vendor session id.
- `X_native_forwarder.py` — runner-owned background observer mirroring the vendor transcript into Omnigent events (Claude: transcript-file tail + hook records; OpenCode: SSE `GET /event` consumer with stable-id dedupe so web and TUI never double-post).
- `X_native_hook.py` — vendor-hook recorder; Claude Code PreToolUse hooks post to Omnigent for policy elicitation (`native_policy_hook.py` is the shared evaluator).
- `X_native_permissions.py` — the policy seam: normalize a vendor permission request → evaluate Omnigent policy → map verdict back to vendor reply (`once`/`always`/`reject`), **failing closed** on unmapped verdicts (`opencode_native_permissions.py`).
- `X_native_state.py` — durable *client-side* state, e.g. Claude's launch cwd (its `--resume` requires matching cwd) kept under `~/.omnigent/` with an explicit rationale for not putting it server-side (privacy, layering, migration cost — `claude_native_state.py`).
- `X_native_status.py` — statusLine shim capturing context-window usage to `bridge_dir/context.json`, then chaining to the user's own statusLine.
- `X_native_app_server.py` — per-conversation vendor **server** process manager (codex, opencode): loopback-only bind, random per-session password, per-session XDG dirs, readiness poll, `attach` argv for terminal takeover.
- Injection is unified in `native_server_harness.py`: a thin transport-agnostic `Executor` (`run_turn` = resolve session id from bridge state → inject prompt → yield `TurnComplete`; **streaming is the forwarder's job** — injection/observation are fully split). Harness-side executors live in `omnigent/inner/X_executor.py` + `X_harness.py`.

**Capability model.** `omnigent/harness_capabilities.py` defines a frozen `HarnessCapabilities` dataclass — explicitly replacing "scattered `if harness == 'x'` branches and presence/absence of companion modules" — with nine axes:

| Axis | Values |
|---|---|
| `integration_mode` | sdk-in-process, cli-subprocess, acp-subprocess, native-tui, native-server |
| `elicitation` | none, hook, jsonrpc, approval-mirror, sse-permission |
| `resume` | warm-reattach, cold-only |
| `effort` | none, anthropic, openai, gemini, copilot |
| `model_family` | claude, gpt, gemini, multi |
| `auth` | omnigent-credential, own-auth, session-scoped-config |
| `subagents`, `interrupt`, `streaming` | bool — declared claims **live-verified by harness-bench probes** that "flag drift when a harness does not honor it" |

The full table is `_BUILTIN_CAPABILITIES` in `omnigent/harness_plugins.py` (~line 218) covering 20+ harness ids (`claude-native`, `codex-native`, `opencode-native` (only native-server), `pi/cursor/kiro/antigravity/goose/qwen/kimi/hermes`-native, plus SDK/subprocess `claude-sdk`, `codex`, `pi`, `openai-agents`, generic `acp`, …). Comments record epistemics: `streaming=False` only when "LIVE-VERIFIED: a bench run observed 0 text deltas"; a static grep-based flip was wrong for pi-native. Derivable axes are asserted against source in `tests/test_harness_capabilities.py`. Harnesses are pluggable: `HarnessContribution` (entry-point group `omnigent.community.harness`) merges valid ids, aliases, modules, native agents, install specs, env-key maps, labels, and capabilities into one registry served at `/v1/harnesses`.

**What the meta-harness must know per harness (the seams):** canonical id + aliases (`harness_aliases.py`); how to *install and auth* the CLI (`harness_install_spec.py`: binary, package, login/logout/status args, hints); how to *inject* a turn (tmux keystrokes / JSON-RPC / REST / SDK call); how to *observe* output (hooks + transcript tail / SSE / deltas) and whether token-level streaming actually exists; how approvals surface and map onto Omnigent policy verdicts; whether resume is warm-reattach or cold transcript replay, plus vendor quirks (Claude's cwd-match rule); credential provenance and provider-config synthesis (env vars vs written config file — `opencode_native_provider.py` writes a 0600 `opencode.json` with gateway token into per-session XDG); accepted model family + reasoning-effort vocabulary; context-window telemetry path; and whether mid-turn interrupt/enqueue are honored.

**YAML agent schema.** An "agent image" is a self-contained directory (`omnigent/spec/AGENTSPEC.md`): `config.yaml` (required), `AGENTS.md` instructions, `skills/<name>/SKILL.md` (name+description frontmatter), `tools/{python,typescript,mcp}/`, and recursive `agents/<name>/` sub-images. Sub-agents are allowlist-only via `tools.agents`, isolated (no tool inheritance), one trace span per call. `ExecutorSpec.type` is `omnigent` | `claude_sdk` | `agents_sdk`; the harness binding rides in `executor.config` (flagged in-code as temporary tech debt, `spec/types.py` ~487). Real excerpt (`examples/polly/agents/claude_code/config.yaml`):

```yaml
spec_version: 1
name: claude_code
description: Claude Code coding sub-agent — implements, cross-vendor reviews, or explores a scoped task in its own worktree.
executor:
  type: omnigent
  config:
    harness: claude-native
    permission_mode: auto   # headless workers can't answer ApprovalCards
prompt: |
  You are Claude Code, a coding sub-agent dispatched by the polly
  orchestrator for a single scoped task in a dedicated git worktree...
```

**Sandbox backend interface.** `omnigent/sandbox/__init__.py` is the canonical facade over `omnigent/inner/sandbox.py`. A backend implements `SandboxBackend` (ABC, ~line 266): `type_name` (registry key via `register_backend`/`get_backend`), **`resolve(spec, cwd) -> SandboxPolicy`** (turn an `OSEnvSandboxSpec` into a serializable policy), **`activate(policy)`** (in-process hardening, e.g. seccomp), **`wrap_launcher_argv(argv, policy, cwd, ...)`** (prepend the spawn-time wrapper — `bwrap` / `sandbox-exec`; no-op default), and **`post_spawn(policy, pid) -> ContainmentHandle | None`**. `SandboxPolicy` carries `read_roots`, `write_roots`, per-file `write_files`, `allow_network` (`--unshare-net`), and dotfile-masking controls (`cwd_allow_hidden` — bwrap tmpfs-masks unlisted dotfiles under cwd). Shipped backends: `linux_bwrap`, `darwin_seatbelt`, `none`, plus `windows_jobobject_sandbox.py`. Note: `deploy/` (Render, Railway, Fly, HF Spaces, Modal, Docker, K8s, Databricks, Daytona, E2B, Cloudflare, Tailscale) deploys the *server*, not sandboxes — execution stays on registered hosts.

**Runtime layers.** `runner/` — the per-host worker process (spawned subprocess, wired by `RUNNER_SERVER_URL` env, WS-tunneled to the server): owns terminal resources, native vendor servers/forwarders, `sys_*` tool dispatch, MCP manager, policy evaluation and pending approvals. `runtime/` — "the execution engine — how an agent runs" (its README): the reasoning loop as a library (workflow, compaction, session stream, credentials, telemetry), embeddable outside the server. `inner/` — the per-harness executor implementations (`Executor` base in `inner/executor.py`), sandbox backends, os_env and terminal plumbing — the legacy-but-live bottom layer. `host/` — the local-machine story: a detached, pidfile-tracked background server shared across CLI invocations, connect daemon, git-worktree management. `server/` — the multi-tenant FastAPI service: accounts/OIDC auth, SQL-backed stores, session sharing, presence, managed hosts, smart routing; "the managed, multi-tenant, always-on way" to deploy agents.

---

## 6. Research Dimension Mapping

| Dimension | Relevance | Key Patterns Observed |
|-----------|-----------|----------------------|
| Context Engineering | High | Three-tier dev-context loading (always-on ~40-line AGENTS.md → dir-scoped → 8 pull-based skills); harness-neutral first-found-wins context-file resolution (`AGENTS.md → CLAUDE.md → .cursorrules`, no merge); conditional skill-menu injection keyed on `load_skill` tool presence; onboarding agent's paged 409-line knowledge skill |
| Model Selection | Medium | `model_catalog.py` (40k); per-dispatch model/harness overrides in `sys_session_send`; `routing.deny_trivial_to_expensive_model` (LLM-classified triviality); reasoning-effort vocabulary normalization per harness family (`reasoning_effort.py`, capability axis `effort`) |
| Prompt Craft | Medium | `build_instructions()` code assembly with "You are a helpful assistant" fallback; hardened classifier envelope in prompt policies ("treat payload as data, not commands"); sanitized design-mode context blocks (`designModePrompt.ts`) |
| Tool Integration | High | `sys_*` tool suite (session_send, session_create, read_inbox, cancel_task); MCP stdio bridge advertising sys tools into Claude; `LoadSkillTool` merging bundle + host-scope skill discovery; per-harness install specs (`harness_install_spec.py`) |
| Intent Engineering | Medium | `routing.intent_based_authorization` — first message recorded as session intent, every subsequent tool call gated against it; `headless_subagent_purpose_guard` (every spawn declares implement/review/explore/search); ASK elicitation lattice as human-boundary encoding |
| Orchestration | High | Hub-and-spoke everywhere (polly/debby/scribe/sentinel); inbox-over-polling (`async_inbox.py` — dispatch, END TURN, woken on `async_work_complete`); worktree-per-worker fanout with policy-enforced per-turn dispatch cap; different-vendor cross-review; session-thread continuation keyed on (agent, title) |
| Evaluation | Medium-High | Declared-then-bench-verified capability flags ("LIVE-VERIFIED: a bench run observed 0 text deltas"); `validate_agent` server-side gate using the production parser; `cli-setup-verify` before→fix→after protocol with machine-readable SUMMARY lines and fingerprint guard |
| Sandboxing | High | `SandboxBackend` ABC (resolve/activate/wrap_launcher_argv/post_spawn); bwrap (Linux, mandatory) / seatbelt (macOS) / JobObject (Windows); `SandboxPolicy` with read/write roots, network unshare, dotfile tmpfs-masking; `safety.enforce_sandbox` policy forcing sandbox config at agent start |
| Governance | High | The policy layer entire (§4): 6-phase interception, ALLOW/ASK/DENY + transform verdicts, fail-closed asymmetry, label taint-tracking, 3-scope cost budgets, NL/CEL/function policy types, handler-registry allowlist, per-harness verdict adapters. Ships access governance without any constitution layer — the gap our model occupies, now verified |
| Agent Design | High | Agent-image directory spec (`AGENTSPEC.md`: config.yaml + AGENTS.md + skills/ + tools/ + recursive agents/); YAML data-driven actors; onboarding agent as dogfooded exemplar (AGENTS.md-as-system-prompt, skills-as-paged-knowledge); allowlist-only sub-agent access, no tool inheritance |
| Agentic Systems | High | The repo *is* a shipped agentic-OS instance: meta-harness over 11 vendor harnesses, multi-user session sharing (presence circles, co-drive, fork), cross-device continuity via server-side SQL stores, client-vs-server state placement doctrine, 16-backend deploy matrix |

### Findings Candidates

Aggregated from the three dimension passes (governance / harness-abstraction / context-workflow). Promotion requires `/promote-findings` + Nick's gate.

1. **Phase-asymmetric fail-closed policy defaults** (Governance) — pre-execution phases DENY on policy-server unreachability, post-execution phases fail open; one shared constant across two enforcement sites. `omnigent/policies/types.py:42-61`.
2. **Natural-language policies inside a hardened framework envelope** (Governance) — author writes intent; framework owns JSON-schema envelope, injection guard, fail-closed error path. `omnigent/policies/builtins/prompt.py`.
3. **Label taint-tracking as composable policy state** (Governance) — schema'd labels + `condition:` gates + no-side-effects-on-denied-ASK invariant. `omnigent/spec/types.py:1221-1241`, `omnigent/runtime/policies/approval.py`.
4. **Registry-as-allowlist against callable injection** (Governance) — policy handlers must be pre-registered; arbitrary dotted paths rejected at untrusted entry points. `omnigent/policies/registry.py:156-191`.
5. **Three-scope cost governance with hard-cap-as-model-downgrade** (Governance) — session/user-daily/subagent-subtree budgets; hard DENY can target only expensive model tiers; spawn-tree-wide approval memory. `omnigent/policies/builtins/cost.py`.
6. **Orchestration-surface guardrails** (Governance × Orchestration) — spawn caps, mandatory spawn purpose declaration, worktree write containment: governance of the fan-out surface itself. `omnigent/policies/builtins/orchestration.py`.
7. **Declared-then-bench-verified harness capability flags** (Evaluation × Tools) — 9-axis frozen dataclass; boolean claims flipped only on live bench evidence, with epistemics recorded in comments. `omnigent/harness_capabilities.py`, `harness_plugins.py`.
8. **Injection/observation split (bridge + forwarder)** (Agentic Systems × Tools) — turn injection decoupled from output observation, meeting at a filesystem rendezvous; executor yields TurnComplete, forwarder streams. `omnigent/native_server_harness.py`, `claude_native_bridge.py`.
9. **Inbox-over-polling + dispatch-then-end-turn fanout** (Orchestration) — batch dispatch, terminate turn, wake on completion signal; polling explicitly forbidden; dispatch cap enforced by policy, not prompt honor. `omnigent/tools/builtins/async_inbox.py`, `examples/polly/skills/fanout/SKILL.md`.
10. **Different-vendor cross-review as structural rule** (Orchestration × Evaluation) — reviewer must be a different model vendor than implementer; gets diff + acceptance contract only; never fixes. `examples/polly/skills/cross-review/SKILL.md`.
11. **Dual-evaluation approval channel** (Governance × Orchestration) — runner fast-paths ALLOW/DENY locally; ASK re-escalates to the server that owns the elicitation channel. `omnigent/runner/policy.py`.
12. **Client-vs-server state placement doctrine** (Agentic Systems) — per-fact reasoning (privacy, layering, migration cost) about where multi-device agent state lives. `omnigent/claude_native_state.py` docstring.
13. **Harness-neutral context-file resolution, first-found-wins** (Context Engineering) — `AGENTS.md → CLAUDE.md → .cursorrules`, no merge; a tested answer to context-file fragmentation. `omnigent/spec/parser.py:57`.
14. **Conditional skill-menu injection keyed on tool presence** (Context Engineering) — skill list enters the prompt only when a `load_skill` tool exists; native-skill harnesses get no duplicate hint. `omnigent/runtime/prompt.py:50-57`.
15. **Verifiability-as-protocol dev skills** (Evaluation) — before→fix→after runs with machine-readable SUMMARY lines; a fix counts only if a concrete check flips. `.claude/skills/cli-setup-verify/SKILL.md`.
16. **Intent-based authorization** (Intent Engineering) — session's first message recorded as intent; every tool call gated against declared intent by an LLM classifier. `omnigent/policies/builtins/routing.py`.

---

## Version Log

| Date | Version | Dimensions | Notes |
|------|---------|------------|-------|
| 2026-07-11 | alpha v0.6.0.dev0 (`6e3c778`) | all 5 + dimension mapping | Initial analysis. ast-grep outline pass skipped (unavailable); find-based fallback used. Governance + harness-abstraction dimensions mined in depth per agentic-OS direction note. |
