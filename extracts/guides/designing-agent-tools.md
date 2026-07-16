---
title: "Designing Agent Tools"
type: "guideline"
category: "Tool Integration"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-04-19"
updated: "2026-07-16"
author: "claude"
source_findings:
  - "gpt-54-tool-search-deferred-tool-loading"
  - "mcp-as-code-api-progressive-tool-discovery"
  - "poka-yoke-error-proof-tool-interfaces"
  - "programmatic-tool-calling-code-orchestrated-tool-use"
  - "tool-registry-metadata-first-design"
  - "think-tool-scratchpad-for-mid-chain-reasoning"
  - "anthropic-managed-agents-platform"
  - "tool-use-examples-sample-calls-in-definitions"
  - "non-deterministic-tool-contract-model"
  - "sdk-vs-framework-decision-for-agent-building"
  - "skill-as-script-wrapper-for-complex-pipelines"
  - "mcp-ecosystem-critical-mass-97m-installs"
  - "gsd-queryable-codebase-intelligence-store"
  - "search-over-list-tool-design-pattern"
  - "tool-call-event-interception-pattern"
  - "skills-lock-portable-agent-skills"
  - "cli-first-tool-integration-less-overhead-than-mcp"
  - "claude-p-headless-mode-as-openclaw-replacement"
  - "cursor-claude-code-ide-composition"
  - "html-pr-explainer-with-margin-annotations"
  - "playwright-cli-for-browser-automation"
  - "skills-inside-workspace-contextual-skill"
  - "skills-portability-across-sdk-and-framework-boundaries"
  - "code-as-deterministic-tool-inside-skills"
  - "ide-first-claude-code-with-deterministic-hooks"
  - "tiered-capability-registry-engine-behavior-branching"
  - "skills-mcp-recipes-kitchen-complementarity"
  - "stateful-mcp-subprocess-vs-cli-shell-out"
  - "monitor-vs-loop-event-driven-vs-time-driven"
  - "claude-code-monitor-tool-event-driven-background"
  - "tool-pruning-as-harness-maintenance"
  - "static-tool-set-mode-changes-as-callable-tools"
  - "skill-cross-surface-portability-with-constraints"
  - "subscription-tos-single-user-boundary-for-agent-sdks"
  - "html-artifact-as-skill-output-design-variations"
  - "bun-hot-reload-interactive-html-artifact-feedback-loop"
  - "mdx-visual-plans-with-reusable-components"
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "tools"
contract:
  preconditions: "You are designing, refactoring, or auditing tools that agents will use. You understand the difference between tool definitions (metadata) and tool implementations (code). You have tools that agents invoke via function calling, MCP, CLI, or equivalent."
  invariants: "Tool definitions are data first — metadata exists before implementation, and capability claims are tiered values, not booleans. Tool interfaces make common errors structurally impossible. Only tools needed for the current task are loaded into context — but the declared tool surface stays static within a session; modes are callable tools, not toolset swaps. Intermediate tool results stay outside the context window when the agent only needs the final output. Tool descriptions are designed for non-deterministic consumers — agents choose whether and how to use them. CLI tools are preferred over protocol-wrapped equivalents when the agent operates in a terminal-native environment and the tool is stateless; stateful local tools get a session-scoped typed server. Background watching defaults to event-driven, not time-driven. Skills are framework-agnostic — portable across SDKs and agent frameworks at the file-shape level, with per-surface runtime constraints declared explicitly. The tool surface is pruned on a recurring cadence — additions are not permanent."
  governance: "Tool registries are maintained as governed artifacts. Interface changes require review. Tool descriptions are treated as UX copy, not documentation. Tool output formats are designed for the consumer — human-gate outputs use navigable formats (HTML with annotations, or reusable component libraries); agent-consumed outputs use structured data. Tool and skill surfaces get scheduled subtractive review, not just additive growth. Multi-user deployment of subscription-backed agents is a ToS boundary checked before launch. This guide is owned by Meta-System knowledge layer."
  recovery: "If tool invocations fail frequently: audit the interface for poka-yoke opportunities before debugging the agent's prompting. If context is bloated with tool definitions: implement deferred loading with name-only stubs — do not remove tools mid-session. If multi-tool workflows are slow: evaluate programmatic tool calling or CLI-first integration; if the tool is stateful, switch to a long-lived local MCP subprocess. If agents choose the wrong tool: improve descriptions and add usage examples before adding instructions. If a background watcher is bleeding tokens: replace time-driven polling with event-driven monitoring. If the agent has grown less trustworthy as capabilities accumulated: run a pruning trial before adding anything else. If skills break after infrastructure migration: verify skill portability — skills should be framework-agnostic markdown, not SDK-coupled code — and check per-surface runtime constraints."
---

# Designing Agent Tools

How to design tools that agents discover, invoke correctly, and use efficiently. This guide covers the full lifecycle of the agent's tool surface: the non-deterministic contract between agents and tools, metadata-first registries with tiered capability declarations, error-proofed interfaces, discovery without context bloat, cache-stable tool surfaces, integration-layer choice (CLI vs. MCP vs. skills vs. headless), efficient multi-tool execution, event-driven background watching, consumer-matched output design, mid-chain reasoning scratchpads, execution middleware and deterministic hooks, skills as a managed and portable capability layer, infrastructure selection — and the maintenance discipline of pruning the surface you built.

## When to Use This Guide

- You are designing new tools for an agent system
- You are connecting an agent to MCP servers, CLI tools, or external APIs
- You are choosing between CLI and MCP integration for a tool that supports both
- Tool definition tokens are consuming a significant fraction of context
- Agents are choosing the wrong tool or making frequent invocation errors
- Multi-tool workflows are slow, producing bloated context, or losing accuracy
- You are designing an agent with modes (plan/execute, read-only/write) and deciding how modes affect the tool surface
- You need the agent to react to a long-running background process without polling
- You are wrapping an existing CLI pipeline as an agent-invocable skill, or bundling scripts inside skills
- You are deciding between SDK-native tools, MCP servers, CLI wrappers, or headless mode
- You need to enforce policies or transform arguments without modifying existing tools
- You are distributing shared skills across multiple projects, agents, frameworks, or Anthropic surfaces
- You are composing multiple tool environments (IDE + CLI agent) into a single workspace
- Tool output is consumed by human reviewers and needs navigable formatting
- Your agent has accumulated tools and skills over months and feels less trustworthy, not more capable

## Key Concepts

**1. Tools are a non-deterministic contract.** Unlike function calls in code where the caller must invoke and handle the return, agents decide whether to call a tool at all, which tool to call, what parameters to pass, and how to interpret the response. Tool design is closer to UX design than API design — you must make the right tool the obvious choice. This reframing is the prerequisite for every other principle in this guide.

**2. Tools are data first — and capabilities are tiers, not booleans.** Define capabilities as a metadata registry before implementing them. Agents should reason about available capabilities without executing anything. When one engine drives multiple backends or tool providers, declare each capability as a graded value (`enforced | best-effort | false`) and branch engine behavior on the grade — enforce where possible, verify-and-retry where plausible, fail closed where impossible. Boolean flags force a lie at the margins.

**3. Make errors structurally impossible.** Borrowing from manufacturing's poka-yoke philosophy, tool interfaces should prevent errors through structure, not instructions. Requiring absolute filepaths instead of relative ones eliminated an entire class of path errors in SWE-bench. Embedding usage examples in tool definitions improved complex parameter accuracy from 72% to 90%.

**4. Load tools on demand — but never mutate the declared surface mid-session.** With dozens of MCP servers, tool definitions alone can consume 134K+ tokens. Keyword-based Tool Search and filesystem progressive discovery achieve 47-98.7% token reduction by loading definitions only when needed. But tool definitions live in the cached prompt prefix: adding or removing tools mid-conversation invalidates the cache. Deferred loading uses name-only stubs that stay present; the declared list never changes. Prefer search-style tools over list-style tools: agents have limited context but abundant compute.

**5. Modes are tools, not toolsets.** An agent with modes (plan vs. execute, read-only vs. write) should not swap tool surfaces per mode. Represent the mode as a pair of always-present transition tools (e.g., `EnterPlanMode`/`ExitPlanMode`) plus injected instructions, with enforcement in the permission layer. This keeps the prompt cache stable and lets the agent enter a mode autonomously. Tool absence was never a security boundary anyway.

**6. Keep intermediates out of context.** When an agent orchestrates multi-tool workflows, intermediate results should stay in the execution environment. Only the final filtered output enters the model context — achieving up to 98.7% token reduction and accuracy gains of 5-10 percentage points on benchmarks.

**7. Give agents a scratchpad.** A "think" tool with no side effects lets agents reason between tool calls without executing anything. Domain-specific prompting of when to use the scratchpad improves policy compliance by up to 76%.

**8. Wrap complex pipelines as skills, and bundle deterministic logic as scripts.** Multi-step CLI workflows can be encapsulated as natural-language-invocable skills. Inside a skill, deterministic operations (sorting, parsing, validation, format conversion) should be bundled scripts the agent executes — the script's code never enters context, only its output does, and the result is bit-exact every run. A tool doesn't have to be an MCP capability or a built-in; it can be a script the skill author bundled for exactly this workflow.

**9. Intercept, don't modify — and make enforcement deterministic.** The tool-call event interception pattern lets extensions enforce policies and transform arguments by subscribing to execution events without touching tool source code. Pre-tool-use hooks are the deterministic end of this spectrum: rules in a context file are probabilistic (the model may ignore them); hooks always fire and cost zero tokens. Convert recurring instructions into hooks. The risk is that mutations bypass re-validation and compose in load order.

**10. Treat shared skills as dependencies.** When skills are distributed across projects and agents, they need the same dependency hygiene as software packages: a lock file to pin versions, conflict detection to prevent silent overwrites, and a CLI that manages install targets. Unmanaged skill distribution drifts silently.

**11. Statefulness picks the transport: CLI-first for stateless tools, session-scoped server for stateful ones.** When a stateless tool exists as both an MCP server and a CLI, and the agent operates in a terminal, prefer the CLI — head-to-head benchmarks show ~90,000 fewer tokens per task. But when the tool holds state (an open database, a warm engine), a long-lived local MCP stdio subprocess beats per-call CLI shell-out: one process holds the state open, exposes typed tools, and dies with the session, while each CLI call would pay full startup plus open/close plus a shell-approval surface. The discriminator is where state lives, not protocol preference.

**12. Skills teach; MCP connects.** MCP provides connectivity — what the agent *can* do (reach your service). Skills provide knowledge — how the agent *should* do it (workflows and best practices). The two are complementary, not competing. An MCP integration shipped without companion skills leaves users connected but not knowing what to do next; the connector gets blamed for a workflow-guidance gap. Service connectivity gap → MCP. Workflow knowledge gap → skill. Both → ship both together.

**13. Watch with events, not timers.** Background watching has two primitives with opposite cost profiles: time-driven polling fires a full inference pass every interval regardless of whether anything changed; event-driven monitoring filters a process stream and costs zero tokens between matching events. Default to event-driven whenever the watched system emits observable output; reserve polling for systems with no event stream.

**14. Design tool output for the consumer.** Agent-consumed output should be structured data (JSON, frontmatter). Human-consumed output at review gates benefits from navigable formats — HTML with margin annotations, severity colors, and jump links outperforms flat text. For recurring review artifacts, a bounded library of reusable interactive components beats one-off generated HTML: consistent across runs and models, repo-friendly, and forkable. For subjective decisions, render multiple variations side-by-side — humans select by recognition faster than they specify upfront.

**15. Scope skills to context, not globally.** Rather than loading all skills at session start, map skills to workspaces and task types. The agent receives only contextually relevant skills, eliminating disambiguation overhead and preventing unintended skill triggering. This is the skill-level equivalent of deferred tool loading.

**16. Prune the harness — agents don't monotonically improve with more tools.** Vercel improved its production sales agent by deleting 80% of its tools. The beginner instinct is to add (a tool, an integration, another exception) until the agent looks powerful but can't be trusted; the maintenance instinct asks what should be removed. Pruning is a recurring discipline across the whole harness surface — tools and accumulated skills alike — not a one-time cleanup.

---

## Procedure

### Step 1: Understand the Tool Contract

Before designing any tool, internalize the non-deterministic contract: the agent is the consumer, and it will decide whether your tool gets used. This means:

- **Descriptions are persuasion, not documentation.** Front-load the key action verb. "Search contacts by name, email, or phone number" beats "This tool provides access to the contact database."
- **Disambiguation is your responsibility.** When multiple tools have overlapping capabilities, the descriptions must make the correct choice obvious. If `search_files` and `grep_content` both exist, explain when each is appropriate.
- **Response interpretability matters.** The agent must understand what your tool returned. Structured output with clear field names outperforms raw dumps.
- **The agent may not use your tool.** If it is hard to discover, poorly described, or returns confusing output, the agent will work around it — often badly.

### Step 2: Design the Tool Registry

Define every tool as metadata before implementing it:

```yaml
tools:
  - name: "{{TOOL_NAME}}"
    source: "{{MCP_SERVER_OR_BUILTIN_OR_CLI}}"
    description: "{{ACTION_VERB — front-load what it does}}"
    category: "{{read/write/execute/query}}"
    risk_level: "{{safe/mutating/destructive}}"
    integration: "{{mcp/cli/builtin/headless}}"
    parameters:
      - name: "{{PARAM}}"
        type: "{{string/number/boolean/object}}"
        required: true
        constraints: "{{VALIDATION_RULES}}"
    examples:  # optional but high-value for complex tools
      - description: "{{SCENARIO}}"
        input: { "{{PARAM}}": "{{VALUE}}" }
```

**Registry principles:**
- Metadata is queryable — agents can filter tools by category, risk level, integration type, or keyword without loading full definitions
- Implementations load on demand (lazy loading)
- Two registries: one for user-facing commands, one for model-facing tools
- Risk classification (safe/mutating/destructive) maps to the permission system
- Integration type (mcp/cli/builtin/headless) determines invocation path and overhead characteristics
- Registry is a derived artifact — regenerated from source definitions, never hand-maintained independently

**Declare capabilities as tiers, not booleans.** When the registry describes backends or providers with varying fidelity (multiple models, multiple tool servers, multiple runtimes), a boolean capability flag forces a lie at the margins — a provider that *mostly* supports structured output is neither `true` nor `false`. Declare the capability as a discriminated value and spell out the consumer behavior per grade:

```yaml
capabilities:
  structured_output: "{{enforced | best-effort | false}}"
  # enforced   → engine uses grammar-constrained output
  # best-effort → engine wraps in validate-and-reask loop (bounded attempts)
  # false      → engine refuses the feature rather than silently degrading
  native_tools: {{true | false}}
  # true  → deliver capability as an in-process native tool
  # false → deliver as a generated prompt section teaching the CLI path
  session_resume: {{true | false}}
```

Engine and workflow code branch on the capability grade, never on provider identity. This encodes a graceful-degradation ladder as data — every backend gets the same feature at the best fidelity it supports, with no scattered per-provider conditionals. Two cautions: declared tiers drift from actual behavior unless verified (bench-test the claims), and a validate-and-reask ladder can multiply token cost on best-effort providers before failing anyway.

**When to add usage examples to a definition:**
- Complex nested parameter schemas (valid JSON does not equal correct usage)
- Tools with many optional parameters that have correlation patterns (e.g., critical priority implies full contact info + tight SLA)
- Domain-specific conventions the model cannot infer from schema alone (date formats, ID patterns)
- Similar tools needing disambiguation
- Do NOT add examples to simple single-parameter tools — the token cost outweighs the benefit

### Step 3: Apply Poka-Yoke to Interfaces

Audit each tool parameter for error-proofing opportunities:

| Anti-Pattern | Poka-Yoke Fix | Example |
|-------------|--------------|---------|
| Relative file paths | Require absolute paths | `/Users/nick/project/src/main.ts` not `src/main.ts` |
| Free-text enum values | Constrained enum types | `risk_level: "safe" | "mutating" | "destructive"` |
| Implicit defaults | Explicit required fields | Make `output_format` required, not defaulted |
| Unbounded strings | Length constraints | `description: max 250 chars` |
| Ambiguous booleans | Named actions | `mode: "append" | "overwrite"` not `overwrite: true` |
| List-all endpoints | Search/filter endpoints | `search_contacts(query)` not `list_contacts()` |
| Positional arguments | Named parameters | `{file: ..., line: ...}` not `[file, line]` |

**The investment priority:** More time on tool interface design than prompt engineering. The SWE-bench team spent more time refining tool interfaces than writing prompts — and the tool improvements had a larger effect on accuracy.

**Search over list.** When a tool could return all records or search for specific ones, prefer the search interface. Agents have limited context windows but abundant compute — searching is cheaper than listing. Validated across Anthropic's internal MCP servers (Slack, Asana, Claude Code).

### Step 4: Choose the Integration Layer

Before implementing discovery (Step 5), decide how each tool connects to the agent. The choice between CLI, MCP, headless mode, and built-in tools determines token overhead, latency, and composability.

**Decision: CLI vs. MCP vs. headless mode?**

| Factor | CLI | MCP Server | Headless (`claude -p`) | Built-in |
|--------|-----|------------|----------------------|----------|
| Agent environment | Terminal-native | Any | Terminal/script | SDK-specific |
| Schema loading | None (lazy) | Eager — all schemas at startup | None | Eager |
| Token overhead | Lowest | Highest (+90K per task in benchmarks) | Low | Variable |
| Setup effort | Minimal if CLI exists | Server process + protocol layer | Bash script | Zero |
| Parallelization | Shell-native (`&`, `xargs`) | Protocol-managed | Session flags | Framework-managed |
| Best for | Stateless tools with existing CLIs | Stateful local services; GUI tools without CLI equivalents; cross-platform | Programmatic agent orchestration | Core operations (read, write, search) |

**The CLI-first rule for terminal-native agents — with a statefulness boundary.** When a *stateless* tool has both a CLI and an MCP server, and the agent operates in a terminal environment (e.g., Claude Code), default to the CLI. Head-to-head testing of Playwright's MCP server vs. CLI showed the CLI was faster and used ~90,000 fewer tokens. CLI tools and terminal agents share an environment natively — no process boundary, no protocol overhead, no eager schema loading.

**The boundary condition: stateful tools invert the rule.** When the tool holds session state — an open database, a warm engine, a loaded index — per-call CLI shell-out pays full process startup plus state open/close on every invocation, forces the model to compose flags and scrape stdout instead of using typed schemas, and adds one shell-approval surface per command. A long-lived local MCP stdio subprocess wins here: the agent spawns it once (no HTTP server, no tunnel, no token), it holds the state open for the session, exposes typed tools, and dies with the session. Demonstrated with a local knowledge engine: the CLI path "works, but is worse as a process"; the MCP subprocess path was visibly faster with no per-command approval friction.

**Decision: is the tool stateful?**

| Question | If yes |
|----------|--------|
| Does the tool open a connection/database/index per call? | Stateful — prefer session-scoped stdio MCP subprocess |
| Does the tool offer a session-scoped `serve` mode? | Stateful path exists — use it |
| Does the CLI path add a shell-approval surface per command? | Count it as per-call overhead against CLI |
| Is each call independent with nothing to amortize? | Stateless — CLI-first holds |

Two cautions on the stateful path: a long-lived subprocess can hold stale state after the underlying data changes externally (verify it has reload semantics), and stateful servers can register very large tool inventories — which is its own context tax (see Step 5 and Step 16).

**When MCP is still correct (stateless cases):**
- The tool has no CLI equivalent (GUI-native tools, OAuth-gated APIs)
- Cross-platform portability matters more than token efficiency
- The tool requires persistent connection state (WebSocket-based protocols)
- You are operating in a non-terminal environment (IDE extension, web app)

**Skills complement MCP — connectivity vs. knowledge.** MCP and skills solve orthogonal problems: MCP connects the agent to a service (what it *can* do); skills teach the agent how to use the service for specific workflows (how it *should* do it). The kitchen analogy: MCP is the professional kitchen; skills are the recipes. Three skill use-case categories map onto this: (1) document/asset creation — built-in capabilities, no MCP needed; (2) workflow automation — multi-step methodology, may coordinate MCP servers; (3) MCP enhancement — workflow guidance on top of a specific server's tools. If you ship an MCP integration, ship companion skills with it: MCP-only integrations leave users connected but not knowing what to do next, and the connector gets blamed for a workflow-guidance gap. Beware skill drift against the MCP server's tool surface across versions — a skill encoding v1 workflows misbehaves on v2's renamed tools.

**Headless mode (`claude -p`) for programmatic orchestration:** When you need to invoke an agent itself as a tool — controlling trigger, context, tools, and output from a script — headless mode provides full programmatic control without any framework dependency. Key flags: `--append-system-prompt` (adds to default prompt), `--system-prompt` (replaces it entirely), `--resume` (session persistence), `--tools` (tool subset control). This replaces proprietary agent platforms for single-developer automation: readable, modifiable, auditable bash scripts with no abstraction layers.

**Browser automation as a specific CLI case.** Playwright CLI exemplifies the CLI-first principle for browser automation: headless browser control via the accessibility tree, parallel sessions, deterministic waits, and 76-99% token savings over Chrome extension approaches. For any web UI that lacks an API, Playwright CLI is the preferred tool before considering visual/screenshot-based automation.

### Step 5: Implement Discovery and Loading — on a Static Tool Surface

Choose a discovery strategy based on your tool surface:

**Decision: How should agents find tools?**

| Condition | Strategy | Token Impact |
|-----------|----------|-------------|
| < 10 tools, < 10K tokens | Load all upfront | Negligible |
| 10-50 tools | Tool Search (keyword query) | ~47% reduction |
| 50+ tools or multi-server | Progressive filesystem discovery | Up to 98.7% reduction |
| Mixed: some always-used, some rare | Hybrid: pre-load frequent + search rare | Variable |

**Tool Search approach (cross-vendor standard):**

```
Agent receives:
+-------------------------------+
| Lightweight tool index        |
| - tool_name: description (1 line) |
| - tool_name: description (1 line) |
| ... (50 tools, ~2K tokens)    |
+-------------------------------+

Agent needs a specific tool:
+-------------------------------+
| Tool Search: "github"         |
| -> loads: github.createPullRequest |
| -> loads: github.listIssues   |
| (full definitions, ~500 tokens) |
+-------------------------------+
```

**Filesystem progressive discovery approach:**

```
Agent explores:
+-------------------------------+
| ls ./servers/                 |
| -> google-drive/              |
| -> salesforce/                |
| -> slack/                     |
| (directory listing, ~100 tokens) |
+-------------------------------+

Agent drills into relevant server:
+-------------------------------+
| ls ./servers/google-drive/    |
| -> list-files.ts              |
| -> read-sheet.ts              |
| -> share-file.ts              |
| (read file header for schema) |
+-------------------------------+
```

Both achieve the same goal: full definitions load only when the agent determines it needs them. Use Tool Search for keyword-based discovery; use filesystem navigation when tools are organized into logical hierarchies (per-server, per-domain).

**Keep the declared tool surface static within a session.** Tool definitions live in the cached prompt prefix. Adding, removing, or editing a tool mid-conversation invalidates the cache — every subsequent turn repays the full prefix cost. Deferred loading is compatible with this constraint because the deferred tools stay *present* as name-only stubs whose full schemas load on demand; the declared list never mutates. Do not implement cost control by dynamically swapping tool subsets in and out.

**Modes are callable tools, not restricted toolsets.** The same cache constraint dictates how to implement agent modes (plan vs. execute, read-only vs. write, teacher vs. builder). The naive implementation — a different tool list per mode — silently destroys caching on every mode toggle. The production pattern (Claude Code's Plan Mode, independently corroborated in opencode):

1. Declare the full tool set once at session start and keep it static.
2. Express the mode as a pair of always-present transition tools (`EnterPlanMode`/`ExitPlanMode`) plus injected instructions stating the mode's constraints.
3. Enforce restrictions in the harness/permission layer — reject out-of-mode tool calls — rather than by hiding tools. Tool absence was never a security boundary.

Second-order benefit: because the transition is a tool, the model can enter a mode autonomously rather than waiting for a user toggle. Watch two failure modes: instruction-only enforcement (if the harness doesn't actually reject out-of-mode calls, discipline rests on model compliance alone) and mode-state drift after compaction (the model's belief about the current mode can desynchronize from reality).

### Step 6: Compose Multi-Tool Environments

When an agent operates across multiple tool environments — IDE, terminal, browser — each layer needs a clear role to prevent tool routing collisions and config drift.

**Decision: Who owns what?**

| Layer | Role | Tool Source | Example |
|-------|------|-------------|---------|
| IDE (Cursor) | Code intelligence, inline completion, config visibility | `.cursor/mcp.json` as canonical MCP config | Cursor with MCP servers |
| Terminal agent (Claude Code) | Agentic execution, multi-step workflows | CLI tools + skills + deferred MCP | Claude Code in terminal panel |
| Browser automation | Web UI interaction | Playwright CLI | Headless browser via accessibility tree |

**Composition principles:**
- **Single source of truth for MCP config.** When both IDE and terminal agent can register MCP servers, designate one config file as canonical (e.g., `.cursor/mcp.json`). Config drift between environments is a silent failure.
- **Respect tool ceilings.** Claude Code has a 40-tool MCP limit. Audit registrations when adding new servers and prune low-priority tools before hitting the ceiling.
- **Separate concerns by layer.** The IDE handles code intelligence; the terminal agent handles execution. If both try to do the same thing (e.g., both run linting), they collide. Assign each capability to exactly one layer.
- **Version-control tool configs.** Committing `.cursor/mcp.json` and skills directories to the repo makes the tool environment reproducible across machines and team members.
- **IDE-first for visibility.** Running the terminal agent inside the IDE (rather than a bare terminal) adds Markdown preview, `.claude/` folder visibility, and sidebar navigation — the terminal alone is a black box for config-heavy agent work.

### Step 7: Design Multi-Tool Execution

When workflows involve 3+ dependent tool calls, large datasets, or filtering/aggregation, decide between inference-driven and code-driven orchestration:

**Decision: Inference-driven vs. code-driven?**

| Factor | Inference-Driven | Code-Driven |
|--------|-------------------|-------------|
| Tool calls | 1-2 simple calls | 3+ dependent calls |
| Intermediate data | Small, needed for reasoning | Large, only final output needed |
| Control flow | Linear, no loops | Loops, conditionals, filtering |
| Data volume | < 100 records | 100+ records, multi-KB payloads |
| Accuracy need | Agent must reason per step | Aggregate/filter is sufficient |

**Code-driven orchestration pattern:**

```
Traditional (each call = full inference pass):
[Agent] -> tool_1() -> result_1 -> [Agent] -> tool_2(result_1) -> ...
         ^ context grows with each result

Programmatic (orchestration in code):
[Agent writes Python]:
  results = []
  for member in get_team_members():
      expenses = get_expenses(member.id)
      budget = get_budget(member.level)
      if expenses > budget:
          results.append(member)
  print(results)  # only this enters context
```

Mark tools as code-callable explicitly via `allowed_callers` or equivalent. Not all tools should be code-callable — tools requiring per-call reasoning stay inference-bound.

**Skill wrapping for CLI pipelines.** When a multi-step workflow involves shell commands, Python scripts, Docker operations, and file management, wrap the entire pipeline as a skill:

```
BEFORE (manual multi-step):
  1. cp document.pdf ./rag-data/
  2. python process.py --input document.pdf --format pdf
  3. docker restart rag-container
  4. curl localhost:8080/health

AFTER (skill-wrapped):
  "ingest this document into the knowledge base"
```

Skills encode not just commands but also error handling, health checks between steps, and verification. The risk: skill wrappers can mask underlying complexity, making failures harder to diagnose.

**Bundle deterministic logic as scripts inside skills.** A skill can carry executable scripts in a `scripts/` subdirectory that the agent runs via shell. The crucial property: **only the script's output enters the context window** — the script's code never loads. This decouples behavior selection (a line of SKILL.md guidance), behavior execution (the script runs deterministically, zero context cost for its body), and result integration (only stdout/stderr enters context). Use bundled scripts for operations LLMs are bad at or that must be bit-exact: sorting, parsing, validation, hashing, format conversion, schema enforcement. "Sorting a list via token generation is far more expensive than simply running a sorting algorithm." Anthropic's production document skills (docx, pdf, pptx, xlsx) all ship bundled Python scripts for the deterministic parts of their workflows.

Bundled-script hygiene:
- Reference scripts portably (`${CLAUDE_SKILL_DIR}/scripts/foo.py` in Claude Code) — hard-coded relative paths break when the skill runs from a different CWD
- Declare system dependencies (Python version, packages, OS tools) — undeclared dependencies fail at runtime with no clean recovery
- Mark whether each script is an *executable* or *reference documentation* — the distinction is ambiguous without explicit SKILL.md guidance
- Prefer structured output (JSON envelopes, error codes) so the agent can robustly interpret results
- Remember the security surface: a bundled script can do anything the environment permits, and its body isn't visible in the system prompt — audit before trusting

### Step 8: Watch Background Processes with Events, Not Timers

Long-running processes (dev servers, test suites, deploys, file drops) need selective awareness without blocking or polling. Two primitives exist with opposite triggering models:

| Dimension | Time-driven (`/loop` every N min) | Event-driven (Monitor) |
|-----------|----------------------------------|------------------------|
| Trigger | Fixed time interval | Filter match in process output |
| Cost per check | Full API call each iteration, changed or not | Zero tokens between events |
| Latency to detect | Up to N minutes | Near-real-time (stdout lag only) |
| Overhead at idle | Continuous | Zero |
| Best for | Systems with no observable event stream | Any process that emits logs/stdout |

**The decision rule:** default to event-driven monitoring whenever the watched system emits observable output (logs, stdout, file events). Use time-driven polling only as a fallback when no event stream exists (e.g., an external API that must be queried). The difference compounds: a 2-minute poll watching a dev server costs a full API call every 2 minutes for a 4-hour session regardless of whether any error occurred; an event-driven monitor on the same server costs nothing until an error line appears.

The event-driven shape (Claude Code's Monitor tool): run a filtered background process; each filter-matching output line becomes one discrete event delivered to the main session; no match, no tokens. This closes the gap between foreground execution (blocks input) and plain background execution (single notification on exit only) — the agent can start diagnosing a failing test before the suite finishes.

**Design cautions:**
- Filters are the interface: over-matching floods the session with noisy events; under-matching silently misses failures. Validate model-generated filter patterns — a wrong grep pattern produces no events and no warning.
- Event-driven watching of a system with no reliable event stream produces silent false-negatives (no events ≠ no problems).
- Bound persistent monitors with timeouts — unbounded monitors accumulate across a session.
- Monitors can stack for multi-signal workflows (errors + warnings + deploy status simultaneously).

### Step 9: Design Tool Output for the Consumer

Tool output format should match the consumer and the decision they are making. Agent-consumed output and human-consumed output have different design constraints.

**Decision: Who consumes this output?**

| Consumer | Format | Design Priority | Example |
|----------|--------|-----------------|---------|
| Agent (next tool call) | Structured data (JSON, YAML) | Parseability, field clarity | API response with typed fields |
| Agent (reasoning) | Concise text with key facts | Information density, relevance | Search result summaries |
| Human (review gate) | Navigable document | Scanability, severity signaling | HTML PR explainer |
| Human (subjective choice) | Side-by-side variations | Recognition over specification | Design-variations grid |
| Human (operational) | Dashboard or log | Trends, anomalies | Monitoring output |

**HTML output for human review gates.** When tool output feeds a human decision point — code review, PR approval, audit sign-off — flat text and Markdown lose navigability for complex changes. The HTML PR explainer pattern demonstrates a more effective format:

- **Margin annotations** explaining why specific changes were made
- **Severity colors** distinguishing critical changes from cosmetic ones
- **Jump links** for navigating between related changes across files

This pattern is used habitually by Anthropic engineers on the Claude Code codebase itself. The HTML artifact is a review companion alongside the standard diff, not a replacement for it.

**Variations grids for subjective decisions.** When the human knows the right answer on sight but cannot describe it upfront (visual design, content tone, layout), have the skill render N distinct alternatives side-by-side in a single self-contained HTML file. The feedback loop becomes generate → scan → recognize → select → integrate, instead of describe → generate → evaluate → redescribe. Keep N modest (a 20+ grid exhausts visual scanning) and explicitly request distinctness — near-duplicate variations defeat the purpose. Any skill whose output a human evaluates subjectively benefits from this over raw text.

**Interactive annotation loops.** A static review artifact still forces the human to describe changes in text. Serving the artifact through a lightweight local server (e.g., Bun) with hot-reload and a click-to-comment overlay collapses the iteration loop: the human pins comments directly on the rendered elements ("make this 10 avatars", "add flags here"), exports them as structured JSON, and the agent actions spatially-grounded changes — more precise than prose references like "the second card in the third row." File saves hot-reload the browser, eliminating refresh-and-re-scroll overhead per iteration.

**Reusable component libraries for recurring review artifacts.** One-off generated HTML has three failure modes at scale: slow and verbose to generate, ugly checked into a repo, and structurally different every run — "HTML slop every time." For artifacts you generate repeatedly (plans, review reports, spec documents), compose them from a bounded library of reusable interactive components (pan/zoomable wireframes, commentable API specs, schema-change views, annotated code blocks — the MDX visual-plan pattern). Reusable components bound generation variance: consistent across runs, models, and agents; repo-friendly as raw files; customizable and forkable. Costs to weigh: the component library needs maintenance (a stale vocabulary pushes the agent back to freeform generation), a renderer toolchain is a real dependency for markdown-native corpora, and a polished wireframe can over-signal certainty about behavior the plan hasn't actually specified.

**When to generate navigable output:**
- Multi-file changes where cross-file relationships matter
- Changes touching security-sensitive code or API surfaces
- Reviews where the reviewer is not the author (context gap is large)
- Do NOT generate HTML for single-file, small-diff changes — the overhead exceeds the benefit

**Output format template:**

```yaml
output:
  consumer: "{{agent | human-review | human-choice | human-operational}}"
  format: "{{json | yaml | markdown | html | component-composed}}"
  annotations: {{true | false}}  # margin annotations for review output
  severity_signals: {{true | false}}  # color/icon severity classification
  navigation: {{true | false}}  # jump links between related sections
  variations: {{N | none}}  # side-by-side alternatives for subjective choices
  interactive: {{static | hot-reload-annotate}}  # click-to-comment feedback loop
```

### Step 10: Add a Think Tool for Complex Chains

For policy-heavy environments or long tool chains, add a zero-side-effect scratchpad:

```yaml
- name: "think"
  description: "Reason about tool outputs without side effects"
  parameters:
    - name: "thought"
      type: "string"
      description: "Your reasoning about what you've learned and what to do next"
```

**Domain-specific prompting is essential.** Generic "use this to think" yields modest gains (+22%). Domain-specific instructions yield +76%:

| Domain | Think Tool Prompt |
|--------|-------------------|
| Code debugging | "Before choosing a fix, use the think tool to brainstorm several unique ways of fixing the bug. Consider edge cases." |
| Policy compliance | "Before acting on search results, use the think tool to check: does this match the user's constraints? Am I following the correct policy?" |
| File operations | "Before executing a file modification, use the think tool to verify: is the file path absolute? Does this change match the acceptance criteria?" |
| Multi-source research | "After receiving search results, use the think tool to assess: what have I learned? What gaps remain? Is this source reliable?" |

**Checkpoint placement:** The think tool is most valuable after receiving tool output that requires interpretation, before taking a mutating action, when multiple valid paths exist, and when policy rules constrain the action space.

### Step 11: Build Tool Execution Middleware

When you need to enforce policies, transform arguments, or log tool calls across many tools without modifying each tool, the tool-call event interception pattern provides a composable middleware layer. Extensions subscribe to a `tool_call` event fired before execution; handlers can block the call (returning a structured reason) or mutate arguments in-place. Later handlers see earlier mutations — the pipeline is ordered by extension load sequence.

**Decision: Should you use event interception or modify the tool directly?**

| Factor | Intercept via Event | Modify the Tool |
|--------|---------------------|-----------------|
| Concern is cross-cutting (logging, auth, normalization) | Yes | No |
| You own the tool source | Either | Yes |
| Multiple tools share the same concern | Yes | No — would require touching each |
| You need bidirectional control (block + mutate) | Yes | Partial |
| Mutations must be re-validated by the schema | No — re-validation does not run | Yes |
| Load order of handlers matters | Yes — be explicit | N/A |

**Interception handler pattern:**

```typescript
// Register an interceptor that enforces an argument policy
harness.on('tool_call', (event) => {
  // Block: return a reason to prevent execution
  if (event.tool === 'delete_file' && !event.args.confirmed) {
    return { blocked: true, reason: 'delete_file requires confirmed: true' };
  }

  // Mutate: transform arguments in-place (later handlers see this)
  if (event.tool === 'read_file' && !path.isAbsolute(event.args.path)) {
    event.args.path = path.resolve(process.cwd(), event.args.path);
  }
});
```

**Critical constraint:** After a handler mutates arguments, the tool's schema validation does not re-run. An extension that produces malformed arguments will cause downstream failure, not a validation error. This means:
- Mutation handlers are responsible for producing valid arguments
- The extension author must understand the target tool's schema
- Composing multiple mutating handlers requires reasoning about their interaction

**Handler composition order matters.** If extension A normalizes a path and extension B checks path existence, they must load in that order. Load order is typically determined by the order extensions are registered — document it if your system supports multiple interceptors.

**Deterministic hooks: convert instructions into enforcement.** Pre-tool-use hooks are the harness-native form of this middleware, and they carry a rule-migration principle: instructions in a context file (CLAUDE.md and equivalents) are *probabilistic* — they consume tokens every turn and the model may still ignore them. A hook is *deterministic* — it always fires, costs zero context tokens, and cannot be ignored. Any rule of the form "never use X, always use Y" (block `npm`, force `pnpm`; block relative paths; forbid a dangerous flag) is a candidate for conversion from instruction to hook. Audit your context files periodically for rules that could become hooks. The counter-pressure: over-hooking creates rigid workflows that can't adapt to edge cases — rules that need context-dependent judgment stay as instructions; rules that are mechanical invariants become hooks.

**When to use middleware vs. poka-yoke (Step 3):** Poka-yoke constraints are the right first choice — they enforce correctness at definition time with zero runtime overhead and no composition risk. Interception is the right choice when you cannot modify the tool definition (third-party MCP servers), need runtime context unavailable at definition time (user permissions, session state), or are applying concerns consistently across a large tool surface.

### Step 12: Manage Shared Skills as Dependencies

When skills are reused across multiple agents or projects, treat them as managed dependencies rather than copied files. The lock file pattern (e.g., `skills-lock.json`) captures the authoritative version and install target for each skill, enabling the same dependency hygiene that package managers provide for code.

**Decision: project-scoped vs. global install?**

| Factor | Project-scoped | Global |
|--------|---------------|--------|
| Skill is specific to one project | Yes | No |
| Skill is used by all agents on the machine | No | Yes |
| Version must track with project codebase | Yes | No |
| Conflicts with another project's version | Isolate with project scope | N/A |

**Lock file structure:**

```json
// skills-lock.json
{
  "version": "1",
  "skills": {
    "{{SKILL_NAME}}": {
      "version": "{{VERSION_TAG}}",
      "source": "{{REGISTRY_OR_PATH}}",
      "target": "{{project | global}}",
      "checksum": "{{SHA256}}"
    }
  }
}
```

**CLI workflow (npx skills or equivalent):**

```
# Install from lock file (detects conflicts, prevents silent overwrites)
npx skills install

# Add a new skill at project scope (updates lock)
npx skills add research-loop --target project

# Verify installed skills match lock file checksums
npx skills verify

# Detect conflicts between project and global installs
npx skills check
```

**Staleness risk.** Lock files can drift from the actual installed state if skills are updated manually or if the registry changes the default version. Run `verify` before any session that depends on skills being current. The conflict detection step is especially important when a skill exists at both project and global scope — the resolution rule (project wins, or error) should be explicit and documented.

**When you don't need this.** Single-project setups with no shared skills, or systems where all skills are maintained in-repo and never distributed, don't benefit from lock management. The overhead is only worth it when skills cross project or agent boundaries.

### Step 13: Scope Skills to Workspaces

Rather than loading all skills globally, map skills to specific workspaces and task types so the agent receives only contextually relevant capabilities.

**Decision: Global vs. contextual skill loading?**

| Factor | Global Loading | Contextual (Workspace-Scoped) |
|--------|---------------|-------------------------------|
| Skill count | < 5 | 5+ |
| Task types are uniform | Yes | No — different tasks need different skills |
| Risk of wrong-skill invocation | Low | High if globally loaded |
| Disambiguation overhead | Acceptable | Unacceptable — agent wastes tokens choosing |

**Workspace skill routing pattern:**

```yaml
# workspace routing table
workspaces:
  - name: "{{WORKSPACE_NAME}}"
    task_types:
      - "{{TASK_TYPE}}"
    skills:
      - "{{SKILL_NAME}}"  # only these skills are available in this context
    suggested_skills:
      - "{{SKILL_NAME}}"  # agent may use if needed, but not pre-loaded
```

**Contextual scoping principles:**
- **Map skills to task types, not sessions.** A writing workspace gets the humanizer skill; a production workspace gets the deployment skill. Skills follow the task, not the user.
- **Suggested vs. required skills.** Required skills are always available in the workspace. Suggested skills are referenced in context files as "you might need this" — the agent considers but does not automatically trigger them.
- **Principle of least privilege for capabilities.** The agent should only have access to skills that make sense for the current context. A writing task should not be able to accidentally trigger a production deployment skill.

### Step 14: Design Skills for Portability

Skills defined as SKILL.md files are portable across SDK and framework boundaries. The same skills directory works in Claude Code SDK agents and custom framework agents (e.g., Pydantic AI) without modification. Design skills to preserve this portability.

**Portability requirements:**
- Skills are plain markdown files — no SDK-specific imports, no framework-coupled code
- Skill discovery follows a standard pattern: scan directory at startup, inject names into system prompt, load full content on demand via a "load skill" tool
- Skills describe procedures in natural language — the agent interprets and executes, rather than the framework compiling to native tool calls
- Skill metadata (name, description, trigger conditions) lives in the SKILL.md frontmatter or header, not in framework config files

**Framework integration pattern:**

```
SDK agent (Claude Code):
  1. Skills directory scanned by harness
  2. Skill names + descriptions injected into system reminder
  3. Agent invokes /skill-name → harness loads SKILL.md
  4. Agent follows SKILL.md instructions using available tools

Framework agent (Pydantic AI, LangGraph, etc.):
  1. Startup script scans skills directory
  2. Skill catalog injected into dynamic system prompt
  3. "load_skill" tool reads SKILL.md content on demand
  4. Agent follows SKILL.md instructions using available tools
```

**The format is portable; the runtime is not.** Across Anthropic surfaces, the same skill folder deploys everywhere but behaves differently per surface:

| Surface | Network | Package Install | Sharing Model |
|---------|---------|-----------------|---------------|
| Claude.ai | Varies with admin policy | Managed | Per-user upload |
| Claude API | None | Pre-installed packages only | Workspace-shared (beta headers required) |
| Claude Code | Full (user's machine) | Local installs | Filesystem: plugins or `.claude/skills/` commit |

Consequences for skill authors:
- A skill whose bundled script makes HTTP calls works on Claude Code, may work on Claude.ai, and fails on the API
- Custom skills do NOT sync across surfaces — each deployment is independent, and drift accumulates between uploads
- **Design for the most restricted target surface** (typically the API) and use the `compatibility` frontmatter field to declare when a skill expects more (e.g., `compatibility: Requires network access and git`)
- Test on the actual target surface — a skill that works in dev on Claude Code and fails in production on the API is the canonical mismatch, and runtime constraints are invisible at install time

**What breaks portability:**
- Skills that reference SDK-specific tool names (e.g., `Bash` instead of generic "run a shell command")
- Skills that assume specific built-in tools (file search, grep) without describing the capability needed
- Skills with embedded code that calls framework APIs directly
- Skills that depend on harness-specific features (session persistence, tool interception) without fallback
- Undeclared surface requirements (network, package installs, filesystem permissions)

**The durable investment.** Skills are emerging as the primary capability layer for AI agents — more portable than tools (which have framework-specific APIs), more accessible than MCP servers (which require protocol support), and more maintainable than custom code (which is tightly coupled). Invest in skills first; choose the infrastructure layer second.

### Step 15: Choose Your Infrastructure Layer

Select the right infrastructure for your tool deployment:

**Decision: SDK vs. Framework vs. Managed Platform?**

| Factor | SDK (Claude Agent SDK, Codex) | Framework (Pydantic AI, LangGraph) | Managed (platform.claude.com) |
|--------|-------------------------------|-------------------------------------|-------------------------------|
| Users | Just you | Multiple people / team | Business automation |
| Speed need | Delay OK | Sub-second required | Variable |
| Token cost | Higher (reasoning overhead) | Lower (full control) | Platform pricing |
| Setup effort | Minimal (single file possible) | More setup, more control | Near-zero |
| Tool integration | Built-in MCP + registry | Manual or plugin-based | OAuth vault + MCP |
| Determinism | Lower | Higher | Lower |
| Skills portability | Native (SKILL.md) | Implementable (same pattern) | Limited |
| Best for | Prototyping, personal tools | Production, scale | Client automations |

**The subscription ToS boundary is the hidden forcing function.** SDK subscription plans (Anthropic Max, OpenAI Plus/Pro) restrict usage to the individual subscriber. Deploying a subscription-backed agent to your team, company, or clients violates terms of service, and account bans for violations are documented. The workaround — API keys — changes the economics by 10-50x (a $200/month Max plan carries an estimated $2,500-$5,000 in API-equivalent usage). This makes "who uses this agent?" the *first* question in the infrastructure decision, not an afterthought: single-user agents can leverage subscription economics; multi-user agents must be designed for API-key economics from day one, which typically means a token-efficient framework rather than a batteries-included SDK. Do not conflate technical capability with legal permission — "the SDK works when my colleague uses it" is not evidence that it's permitted. Skill portability (Step 14) is the hedge: framework-agnostic skills survive the SDK-to-framework graduation this boundary forces.

**MCP is baseline infrastructure.** With 97M installs, 4,000+ servers, and universal provider support, MCP is no longer an adoption decision. The question is whether you are using MCP deeply enough — audit your tool surface against the available server catalog. But remember the CLI-first rule and its statefulness boundary (Step 4): when a CLI exists for a stateless tool and the agent is terminal-native, CLI beats MCP on every efficiency metric.

**Headless mode as the zero-dependency orchestration layer.** `claude -p` provides the thinnest possible agent infrastructure: a bash script controls trigger (cron, webhook, manual), context (system prompt flags), tools (--tools for subset control), and output (stdout). No framework, no dependency management, no abstraction layers. Every line is readable and modifiable. Use this when the SDK is too heavy and a framework is unnecessary — single-developer automation, scheduled agents, or pipeline glue between systems.

**Queryable intelligence stores.** For tools that provide codebase or domain intelligence, consider persistent structured stores (e.g., `.planning/intel/` with JSON for files, symbols, dependencies) queryable via CLI. This converts repeated O(n) discovery cost into O(1) lookup. Key risk: stale data is worse than no data — build in freshness indicators and incremental update mechanisms.

### Step 16: Prune the Tool Surface

Everything the preceding steps add — tools, MCP servers, skills, hooks, monitors — is subject to a maintenance discipline the build phase never teaches: **agents do not monotonically improve as you give them more.** Vercel's production SDR agent got better when the team deleted 80% of its tools. The mechanism is not only context-window cost (though tool schemas tax the prefix): each addition widens the behavior space, making the agent look more capable while becoming harder to predict and trust.

**The discipline:**
- **Ask the subtraction question on a cadence.** The beginner instinct is to add; the maintenance instinct asks what should be removed. Schedule subtractive review of the whole harness surface — tool registrations, MCP servers, skill rosters, accumulated rules — rather than only auditing for consistency and drift.
- **Run pruning trials, not blind deletions.** Remove a tool, run the eval set (see the evaluation guide), keep the deletion if quality holds. This is the no-op deletion test generalized to tools.
- **Select candidates from data.** Track per-tool invocation rates so pruning candidates are chosen by observed usage, not intuition. Watch for the long-tail trap: a tool invoked rarely but critically fails invisibly until the rare case — this is exactly why pruning without evals is dangerous.
- **Ask the deletion question at build time.** The mature design question when adding any capability: "what part of this harness will I need to delete later?" Simplicity is a key to maintainability.
- **Don't cargo-cult the ratio.** The right amount of deletion is workload-specific; the discipline is the recurring review, not the 80% number.
- **Treat it as recurring, not one-time.** A pruned surface regrows. Put the review on the same cadence as dependency updates.

**Pruning worksheet:**

```markdown
## Harness Pruning Review — {{DATE}}

| Surface item | Type | Invocations (period) | Last used | Eval-verified removable? | Action |
|--------------|------|---------------------|-----------|--------------------------|--------|
| {{TOOL_OR_SKILL}} | {{tool/skill/MCP server/hook/rule}} | {{COUNT}} | {{DATE}} | {{YES/NO/UNTESTED}} | {{keep / prune-trial / delete}} |
```

---

## Templates

### Tool Definition Template

```yaml
# Tool Definition — {{TOOL_NAME}}
name: "{{TOOL_NAME}}"
source: "{{MCP_SERVER_NAME | builtin | skill | cli}}"
description: "{{ACTION_VERB + OBJECT + KEY_CONSTRAINT — max 1 sentence}}"
category: "{{read | write | execute | query}}"
risk_level: "{{safe | mutating | destructive}}"
integration: "{{mcp | cli | builtin | headless}}"
parameters:
  - name: "{{PARAM_NAME}}"
    type: "{{string | number | boolean | enum | object}}"
    required: {{true | false}}
    constraints: "{{VALIDATION — absolute path, max length, enum values, format pattern}}"
    description: "{{WHAT_THIS_PARAM_CONTROLS}}"
# Include examples when: nested objects, correlated optional params, domain conventions
examples:
  - description: "{{SCENARIO_NAME}}"
    input:
      {{PARAM_NAME}}: "{{EXAMPLE_VALUE}}"
    expected_behavior: "{{WHAT_HAPPENS}}"
output:
  consumer: "{{agent | human-review | human-choice | human-operational}}"
  format: "{{json | yaml | markdown | html}}"
```

**Worked Example:**

```yaml
name: "search_findings"
source: "research-kb-mcp"
description: "Search research findings by keyword, category, or evidence strength"
category: "query"
risk_level: "safe"
integration: "mcp"
parameters:
  - name: "query"
    type: "string"
    required: true
    constraints: "min 2 chars, max 200 chars"
    description: "Search terms matched against finding names and summaries"
  - name: "category"
    type: "enum"
    required: false
    constraints: "Tool Integration | Context Engineering | Prompt Craft | Agent Architecture | Safety"
    description: "Filter results to a single research dimension"
  - name: "evidence_strength"
    type: "enum"
    required: false
    constraints: "Strong | Medium | Weak"
    description: "Minimum evidence threshold for returned findings"
examples:
  - description: "Find all strong-evidence tool integration findings"
    input:
      query: "tool"
      category: "Tool Integration"
      evidence_strength: "Strong"
    expected_behavior: "Returns findings about tool design, MCP, registries with production evidence"
  - description: "Broad search across all categories"
    input:
      query: "context window optimization"
    expected_behavior: "Returns findings mentioning context window optimization regardless of category or strength"
output:
  consumer: "agent"
  format: "json"
```

### Capability Declaration Template (Tiered)

For registries that describe multiple backends, providers, or runtimes with varying fidelity.

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `PROVIDER_NAME` | string | Backend/provider identifier | yes |
| `CAPABILITY` | string | The capability being declared | yes |
| `GRADE` | enum | Discriminated fidelity value — never a bare boolean for graded capabilities | yes |
| `PER_GRADE_BEHAVIOR` | string | What the consuming engine does at each grade | yes |

```yaml
# Capability Declaration — {{PROVIDER_NAME}}
provider: "{{PROVIDER_NAME}}"
capabilities:
  {{CAPABILITY}}: "{{GRADE — e.g. enforced | best-effort | false}}"
consumer_behavior:
  enforced: "{{PER_GRADE_BEHAVIOR — e.g. grammar-constrained output}}"
  best-effort: "{{PER_GRADE_BEHAVIOR — e.g. validate-and-reask loop, max {{N}} attempts}}"
  false: "{{PER_GRADE_BEHAVIOR — e.g. refuse feature rather than silently degrade}}"
verification: "{{HOW_THE_CLAIM_IS_TESTED — bench suite, manual, unverified}}"
```

**Worked Example:**

```yaml
provider: "codex-cli"
capabilities:
  structured_output: "best-effort"
  native_tools: false
  session_resume: true
consumer_behavior:
  enforced: "n/a for this provider"
  best-effort: "wrap output in schema validation; re-ask on failure, max 3 attempts; fail closed after"
  false: "run management delivered as generated prompt section teaching CLI-over-bash (no native manage_run tool)"
verification: "manual spot-check against v0.5 — flag for bench verification; declared tiers drift without it"
```

### Tool Interceptor Template

```typescript
// Tool Call Interceptor — {{INTERCEPTOR_NAME}}
// Purpose: {{WHAT_THIS_ENFORCES_OR_TRANSFORMS}}
// Load order: {{POSITION_RELATIVE_TO_OTHER_INTERCEPTORS}}
// Re-validation: NONE — handler is responsible for producing valid args

harness.on('tool_call', (event: ToolCallEvent): BlockResult | void => {
  // Guard: only apply to relevant tools
  if (!{{TOOL_SCOPE_PREDICATE}}) return;

  // Block pattern: prevent execution with a structured reason
  if ({{BLOCK_CONDITION}}) {
    return {
      blocked: true,
      reason: '{{HUMAN_READABLE_BLOCK_REASON}}'
    };
  }

  // Mutate pattern: transform args in-place (later handlers see this)
  event.args.{{PARAM}} = {{TRANSFORMED_VALUE}};
});
```

**Worked Example — Path Absolutizer:**

```typescript
// Normalizes relative file paths to absolute before any tool executes
// Load order: FIRST — path normalization must precede existence checks
// Re-validation: handler validates path format before mutating

harness.on('tool_call', (event: ToolCallEvent): void => {
  const fileTools = ['read_file', 'write_file', 'delete_file'];
  if (!fileTools.includes(event.tool)) return;

  const p = event.args.path;
  if (typeof p === 'string' && !path.isAbsolute(p)) {
    // Validate the normalized path won't escape the workspace
    const resolved = path.resolve(process.cwd(), p);
    if (!resolved.startsWith(process.cwd())) {
      return { blocked: true, reason: `Path escapes workspace: ${p}` };
    }
    event.args.path = resolved;
  }
});
```

**Worked Example — Permission Gate:**

```typescript
// Blocks destructive tool calls unless the session has elevated permissions
// Load order: AFTER path normalization, BEFORE any other write interceptors

harness.on('tool_call', (event: ToolCallEvent): BlockResult | void => {
  const destructiveTools = ['delete_file', 'drop_table', 'truncate_store'];
  if (!destructiveTools.includes(event.tool)) return;

  if (!session.hasPermission('destructive')) {
    return {
      blocked: true,
      reason: `${event.tool} requires destructive permission; current session: ${session.role}`
    };
  }
});
```

**Worked Example — Deterministic Command Steering (pre-tool-use hook):**

```typescript
// Converts a CLAUDE.md instruction ("always use pnpm, never npm") into
// deterministic enforcement. Zero context tokens; cannot be ignored.
// Load order: FIRST among shell interceptors.

harness.on('tool_call', (event: ToolCallEvent): BlockResult | void => {
  if (event.tool !== 'bash') return;

  if (/^npm\s/.test(event.args.command)) {
    return {
      blocked: true,
      reason: 'npm is blocked in this workspace — use pnpm (rule enforced by hook, not instruction)'
    };
  }
});
```

### Mode Transition Tools Template

For mode-bearing agents (plan/execute, read-only/write). The tool surface stays static; the mode is a callable transition plus injected instructions.

| Variable | Type | Description | Required |
|----------|------|-------------|----------|
| `MODE_NAME` | string | The mode being entered/exited | yes |
| `MODE_CONSTRAINTS` | string | What the model may/may not do in this mode | yes |
| `ENFORCEMENT` | string | How out-of-mode calls are rejected (permission layer, not tool hiding) | yes |

```yaml
# Mode transition tools — always present in the declared tool set
tools:
  - name: "Enter{{MODE_NAME}}"
    description: "{{WHEN_THE_AGENT_SHOULD_ENTER — the model may call this autonomously}}"
    on_call:
      inject_instructions: "{{MODE_CONSTRAINTS — system message stating the new behavioral reality}}"
      permission_profile: "{{ENFORCEMENT — e.g. deny all write tools except {{ALLOWED_GLOBS}}}}"
  - name: "Exit{{MODE_NAME}}"
    description: "{{EXIT_CONDITION — e.g. plan approved by user}}"
    on_call:
      inject_instructions: "{{POST_MODE_REALITY — what is now permitted}}"
      permission_profile: "default"
# Invariant: the declared tool list never changes across mode transitions —
# tool definitions live in the cached prompt prefix; swaps invalidate the cache.
```

**Worked Example:**

```yaml
tools:
  - name: "EnterReviewMode"
    description: "Enter read-only review mode before auditing staged artifacts. Call this before any audit task."
    on_call:
      inject_instructions: "You are in review mode: read and report only. Do not edit, write, or delete any file. Produce findings as a report."
      permission_profile: "deny Edit, Write, NotebookEdit; deny bash mutations (rm, mv, git commit)"
  - name: "ExitReviewMode"
    description: "Exit review mode after the findings report is delivered and the user approves fixes."
    on_call:
      inject_instructions: "Review mode ended. Write operations are permitted again per your standard profile."
      permission_profile: "default"
```

### Tool Output Template (Human Review Gate)

```html
<!-- PR Explainer — {{PR_TITLE}} -->
<!-- Generated: {{TIMESTAMP}} -->
<html>
<head>
  <style>
    .severity-critical { border-left: 4px solid #e74c3c; }
    .severity-important { border-left: 4px solid #f39c12; }
    .severity-info { border-left: 4px solid #3498db; }
    .annotation { margin-left: 1em; font-style: italic; color: #666; }
    .jump-link { font-size: 0.85em; color: #2980b9; }
  </style>
</head>
<body>
  <h1>{{PR_TITLE}}</h1>
  <nav><!-- jump links to each file section --></nav>

  <section class="severity-{{SEVERITY}}">
    <h2>{{FILE_PATH}}</h2>
    <pre>{{DIFF_CONTENT}}</pre>
    <div class="annotation">{{WHY_THIS_CHANGED}}</div>
    <a class="jump-link" href="#{{RELATED_SECTION}}">Related: {{RELATED_FILE}}</a>
  </section>
</body>
</html>
```

### Skills Lock File Template

```json
{
  "version": "1",
  "skills": {
    "{{SKILL_NAME}}": {
      "version": "{{VERSION_TAG}}",
      "source": "{{REGISTRY_PATH_OR_LOCAL_PATH}}",
      "target": "{{project | global}}",
      "checksum": "{{SHA256_OF_SKILL_BUNDLE}}"
    }
  }
}
```

**Worked Example:**

```json
{
  "version": "1",
  "skills": {
    "research-loop": {
      "version": "2.3.1",
      "source": "registry:improvement-loop/skills",
      "target": "project",
      "checksum": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
    },
    "extract-artifacts": {
      "version": "1.4.0",
      "source": "registry:improvement-loop/skills",
      "target": "project",
      "checksum": "b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7"
    },
    "pdf-to-markdown": {
      "version": "1.0.4",
      "source": "registry:cross-system/skills",
      "target": "global",
      "checksum": "c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8"
    }
  }
}
```

### Workspace Skill Routing Template

```yaml
# Workspace Skill Routing — {{SYSTEM_NAME}}
workspaces:
  - name: "{{WORKSPACE_NAME}}"
    task_types:
      - "{{TASK_TYPE_1}}"
      - "{{TASK_TYPE_2}}"
    skills:
      - "{{REQUIRED_SKILL_1}}"
      - "{{REQUIRED_SKILL_2}}"
    suggested_skills:
      - "{{OPTIONAL_SKILL}}"
```

**Worked Example:**

```yaml
workspaces:
  - name: "improvement-loop"
    task_types:
      - "research"
      - "extraction"
      - "synthesis"
    skills:
      - "research-loop"
      - "identify-artifacts"
      - "extract-artifacts"
    suggested_skills:
      - "perplexity-research"
      - "transcript-fetcher"
  - name: "claude-build"
    task_types:
      - "schema-modification"
      - "build-spec-execution"
    skills:
      - "notion-schema-tools"
      - "playwright-automation"
    suggested_skills:
      - "pdf-to-markdown"
```

### Tool Design Audit Worksheet

```markdown
## Tool Audit — {{SYSTEM_NAME}}

### Contract Model
- [ ] Tool descriptions front-load the action verb
- [ ] Similar tools have disambiguation guidance in descriptions
- [ ] Response formats are structured and interpretable

### Registry Health
- [ ] All tools have metadata entries (name, description, category, risk_level, integration)
- [ ] Metadata is queryable without loading implementations
- [ ] Risk levels are classified (safe/mutating/destructive)
- [ ] Integration types are recorded (mcp/cli/builtin/headless)
- [ ] Graded capabilities are declared as tiers (enforced/best-effort/false), not booleans
- [ ] Complex tools have usage examples in definitions

### Interface Quality (per tool)
| Tool | Poka-Yoke Opportunities | Current Interface | Improved Interface |
|------|------------------------|-------------------|-------------------|
| {{TOOL}} | {{ISSUE}} | {{CURRENT}} | {{FIXED}} |

### Integration Layer
| Tool | Has CLI? | Has MCP? | Stateful? | Current Integration | Recommended |
|------|----------|----------|-----------|--------------------|--------------------|
| {{TOOL}} | {{YES/NO}} | {{YES/NO}} | {{YES/NO}} | {{CURRENT}} | {{CLI if stateless+terminal-native; session-scoped MCP subprocess if stateful; MCP otherwise}} |

**Decision:** For each stateless tool with both CLI and MCP, default to CLI in terminal-native agents. For stateful local tools, prefer a long-lived stdio MCP subprocess.

### Discovery Assessment
| Metric | Value |
|--------|-------|
| Total tool definitions | {{COUNT}} tools |
| Estimated definition tokens | ~{{TOKENS}} tokens |
| Loading strategy | {{UPFRONT / DEFERRED / HYBRID}} |
| List-style tools to convert to search | {{LIST}} |
| Tool surface static within sessions? | {{YES / NO — list mid-session mutations}} |
| Modes implemented as callable tools? | {{YES / NO / N/A}} |

**Decision:** If definitions > 10K tokens or > 10 tools, implement deferred loading with name-only stubs — never mid-session toolset swaps.

### Background Watching
- Long-running processes watched: {{LIST}}
- Watch mechanism per process: {{event-driven monitor / time-driven poll}}
- Time-driven polls with an available event stream: {{LIST — convert to monitors}}
- Monitor filters validated against real output: {{YES/NO}}

### Tool Output
- Human review gate outputs: {{LIST — format used (md/html/text)}}
- Candidates for HTML navigable output: {{LIST — multi-file PRs, security reviews}}
- Recurring review artifacts using a reusable component library: {{YES/NO — or one-off HTML each time}}
- Subjective-decision outputs rendered as variations grids: {{YES/NO/N/A}}
- Agent-consumed outputs using structured format: {{YES/NO}}

### Execution Middleware
- Cross-cutting concerns identified: {{LIST — logging, auth, path normalization, etc.}}
- Interceptors registered: {{COUNT}} (list load order explicitly)
- Tools with mutating interceptors: {{LIST}} (confirm handlers produce valid args)
- Mutation composition reviewed: {{YES/NO}}
- Context-file rules convertible to deterministic hooks: {{LIST}}

### Skill Distribution
- Skills shared across projects: {{LIST}}
- Skills lock file present: {{YES/NO — path}}
- Last verified against lock: {{DATE or NEVER}}
- Project vs global conflicts: {{NONE / LIST}}

### Skill Scoping and Portability
- Skills loaded globally: {{LIST}}
- Skills mapped to workspaces: {{LIST with workspace names}}
- Workspace routing table present: {{YES/NO}}
- Cross-framework portability verified: {{YES/NO — which frameworks tested}}
- Target surfaces per skill declared (`compatibility` field): {{YES/NO}}
- Skills tested on their most restricted target surface: {{YES/NO}}
- Bundled scripts use portable path references: {{YES/NO/N/A}}

### Execution Efficiency
- Multi-tool workflows identified: {{LIST}}
- Candidates for code orchestration: {{LIST}} (3+ dependent calls, large intermediates)
- Candidates for skill wrapping: {{LIST}} (CLI pipelines with 3+ steps)
- Deterministic operations bundled as scripts: {{LIST / NONE — candidates: sorting, parsing, validation}}
- Think tool deployed: {{YES/NO}}
- Think tool domain prompts written: {{YES/NO — list domains}}

### Infrastructure
- Platform: {{SDK / FRAMEWORK / MANAGED / HYBRID}}
- Who uses the agent: {{single subscriber / multiple users}} — ToS boundary checked: {{YES/NO}}
- MCP servers connected: {{COUNT}}
- MCP catalog audit done: {{YES/NO — date}}
- CLI tools available: {{LIST}}
- Headless agents deployed: {{COUNT — list triggers}}
- Intelligence store: {{NONE / PLANNED / ACTIVE}}
- IDE composition: {{NONE / Cursor+CC / other — config source documented}}

### Harness Pruning
- Last subtractive review: {{DATE or NEVER}}
- Per-tool invocation tracking: {{YES/NO}}
- Pruning trials run with eval verification: {{COUNT}}
- Surface items added since last review: {{COUNT}}
```

**Worked Example:**

```markdown
## Tool Audit — MetaSystem Skills

### Contract Model
- [x] Tool descriptions front-load the action verb (SKILL.md pattern)
- [ ] Similar tools have disambiguation guidance — /research-loop vs /perplexity-research overlap
- [x] Response formats are structured (markdown with frontmatter)

### Registry Health
- [x] All tools have metadata entries (CLAUDE.md skill tables + SKILL.md)
- [ ] Metadata is queryable without loading implementations — currently Glob/Grep, not a registry API
- [ ] Risk levels are classified — not formalized; skills are implicitly safe/mutating
- [ ] Integration types are recorded — not formalized; implicitly CLI/builtin
- [ ] Graded capabilities as tiers — model-capability registry uses prose claims; tier enums are the upgrade path
- [ ] Complex tools have usage examples — some skills have worked examples, most don't

### Interface Quality
| Tool | Poka-Yoke Opportunities | Current | Improved |
|------|------------------------|---------|----------|
| /extract-artifacts | Report path is free-text | Any path accepted | Validate report exists in operations/ |
| /research-loop | URL list is unbounded | Any count accepted | Max 10 URLs per invocation |
| /pdf-to-markdown | File path can be relative | Accepts relative paths | Require absolute path or URL |

### Integration Layer
| Tool | Has CLI? | Has MCP? | Stateful? | Current | Recommended |
|------|----------|----------|-----------|---------|-------------|
| Playwright | Yes | Yes | No | Adopted (CLI) | CLI (terminal-native, stateless) |
| Perplexity | No | Yes | No | MCP | MCP (no CLI) |
| Notion | No | Yes | No | MCP | MCP (no CLI) |
| Context7 | No | Yes | No | MCP | MCP (no CLI) |
| Future local KB engine | Maybe | Maybe | Yes (open index) | — | Session-scoped stdio MCP subprocess, not per-call CLI |

### Discovery Assessment
| Metric | Value |
|--------|-------|
| Total tool definitions | ~40 skills + 50+ MCP tools |
| Estimated definition tokens | ~2K per skill listing, MCP deferred via ToolSearch |
| Loading strategy | HYBRID — skills deferred (SKILL.md on invoke), MCP deferred (name stubs + ToolSearch) |
| List-style tools to convert to search | Notion list-pages, finding enumeration |
| Tool surface static within sessions? | Yes — deferred tools are stubs, list never mutates |
| Modes implemented as callable tools? | Yes — plan mode via EnterPlanMode/ExitPlanMode |

### Background Watching
- Long-running processes watched: transcript-fetcher batch runs, research-loop URL batches
- Watch mechanism per process: background bash with exit notification; no monitors yet
- Time-driven polls with an available event stream: /loop candidates should check Monitor first
- Monitor filters validated: N/A — adopt validation step with first monitor

### Tool Output
- Human review gate outputs: /code-review (markdown), /ship PR description (markdown)
- Candidates for HTML navigable output: /code-review for multi-file changes, /ship for complex PRs
- Recurring review artifacts using reusable components: No — identification reports and DDs are one-off markdown; component library is the IB-175 visualization path
- Subjective-decision outputs as variations grids: N/A today — candidate for guide/report layout choices
- Agent-consumed outputs using structured format: Yes (frontmatter-based findings, JSON intel stores)

### Execution Middleware
- Cross-cutting concerns: none currently formalized
- Interceptors: 0 registered
- Mutating interceptors: N/A
- Mutation composition: N/A — would benefit argument normalization for /pdf-to-markdown paths
- Context-file rules convertible to hooks: destructive-command approval, absolute-path requirement

### Skill Distribution
- Skills shared across projects: /pdf-to-markdown, /session-handoff (workspace root)
- Skills lock file: No — skills tracked in CLAUDE.md skill tables only
- Last verified: Never — manual inspection each session
- Conflicts: None detected (single workspace)

### Skill Scoping and Portability
- Skills loaded globally: all IL skills via CLAUDE.md table
- Skills mapped to workspaces: partially — skills are grouped by agent role in CLAUDE.md
- Workspace routing table present: No — would benefit from explicit routing
- Cross-framework portability verified: No — single-framework (Claude Code)
- Target surfaces declared: No — all skills implicitly Claude Code-only (full network, local installs)
- Tested on most restricted surface: No — acceptable while Claude Code is the only target
- Bundled scripts portable paths: Partial — transcript-fetcher wraps a Python tool; audit for ${CLAUDE_SKILL_DIR}

### Execution Efficiency
- Multi-tool workflows: /extract-artifacts (parallel Sonnet subagents), /identify-artifacts
- Candidates for code orchestration: research-loop URL batch processing
- Candidates for skill wrapping: PDF-to-findings pipeline (fetch + convert + extract + write)
- Deterministic operations bundled as scripts: kb_parser.py (frontmatter read/write); candidates: link validation, count checks
- Think tool deployed: No
- Think tool domain prompts: N/A — would benefit /identify-artifacts (form classification)

### Infrastructure
- Platform: SDK (Claude Code CLI)
- Who uses the agent: single subscriber (Nick) — ToS boundary checked: Yes; multi-user scenarios would force API-key economics
- MCP servers connected: 4 (Context7, Notion, Perplexity, Gmail)
- MCP catalog audit done: No
- CLI tools available: Playwright, ripgrep, git, gh
- Headless agents deployed: 0 — candidate for scheduled research scans
- Intelligence store: None — codebase re-scanned each session
- IDE composition: Cursor + Claude Code — .cursor/mcp.json is canonical MCP config

### Harness Pruning
- Last subtractive review: Never — audits check consistency and drift, not removal
- Per-tool invocation tracking: No
- Pruning trials with eval verification: 0
- Surface items added since last review: growing skill roster — schedule subtractive review in /system-health
```

---

## Pitfalls

### 1. Designing tools like APIs instead of UX
Traditional API design assumes a deterministic caller that must invoke the endpoint. Agent tool design must assume a non-deterministic consumer that chooses whether to use the tool based on its description. If the description is unclear, the agent will guess or work around it — producing worse results than if the tool did not exist. Treat tool descriptions as UX copy: front-load the verb, disambiguate from similar tools, explain when NOT to use it.

### 2. All tool definitions loaded upfront
With 50+ tools, definitions alone can consume 134K tokens. Agents perform worse when drowning in irrelevant tool specs. Load only what is needed for the current task. Both OpenAI and Anthropic now ship deferred loading as a cross-vendor standard. The same principle applies to skills — scope them to workspaces and task types rather than loading all skills globally.

### 3. Instructions instead of structure
"Always use absolute file paths" is an instruction the agent may forget. Making the parameter accept only absolute paths is a structural constraint that cannot be violated. The same applies to enums, required fields, and length limits — and, at the execution layer, to hooks: a recurring "never X, always Y" instruction in a context file is probabilistic and costs tokens every turn; a pre-tool-use hook is deterministic and free. Invest in interface design and structural enforcement before prompt engineering.

### 4. List tools returning unbounded results
A `list_contacts` tool that returns all 10,000 records floods the context window. Replace with `search_contacts(query)` — agents have limited context but abundant compute. Provide a "browse top N" fallback for exploration tasks where the agent does not know what to search for.

### 5. Intermediate results in context
A multi-tool workflow that dumps every API response into the context window wastes tokens and degrades attention. Keep intermediates in the execution environment; return only the final output. Measured impact: 200KB raw data reduced to 1KB, with accuracy improvements.

### 6. Generic think tool prompting
"Use this tool to think" yields modest improvement (+22%). Domain-specific instructions yield +76%. Write think-tool prompts that name the specific checks, policies, or constraints the agent should verify at each checkpoint.

### 7. Tools without metadata
If agents cannot reason about available tools without executing them, they will either guess (hallucinated tool calls) or trial-and-error (wasted tokens). Metadata-first registries solve both problems.

### 8. Schema without examples
A `create_ticket` tool with nested `reporter.contact` and `escalation` objects has many valid JSON combinations, but only a few represent correct usage. Schema ensures valid JSON; examples teach correct usage. Without examples on complex tools, accuracy drops from 90% to 72%.

### 9. Skill wrappers that mask failures
Wrapping a multi-step CLI pipeline as a skill makes it easy to invoke but hard to debug. If the underlying tools change their interface, the skill silently breaks. Include health checks between steps, surface which step failed, and log intermediate outputs for diagnosis.

### 10. Stale intelligence stores
A queryable codebase or domain intelligence store converts O(n) rediscovery into O(1) lookup. But stale data is worse than no data — an agent trusting outdated symbol maps generates incorrect code with high confidence. Build in staleness indicators, incremental updates, and freshness checks. The same applies to long-lived stateful MCP subprocesses: state held open can go stale when the underlying data changes externally — verify reload semantics.

### 11. Mutation without re-validation
When an event interceptor mutates tool arguments, the tool's schema validation does not re-run. A handler that produces malformed arguments will cause a downstream failure with no validation error surfaced — the bug appears far from the cause. Write mutation handlers defensively: validate the output of your mutation before applying it, document the load order, and test composing multiple mutating handlers before deploying to production.

### 12. Unmanaged skill distribution
Copying skill files across projects without a lock file creates version drift: one project gets a buggy fix, another doesn't. Silent overwrites occur when a global install clobbers a project-scoped version. Without conflict detection, the first sign of a problem is often incorrect agent behavior rather than an install error. Adopt lock file management before you have more than two projects sharing a skill.

### 13. MCP when CLI would suffice — and CLI when the tool is stateful
Defaulting to MCP integration because it is the "standard" when the agent is terminal-native and a CLI exists wastes ~90,000 tokens per task and adds latency from process boundaries and protocol overhead. But the inverse error is applying CLI-first blindly to a stateful tool: per-call shell-out to an engine that opens a database on every invocation pays startup + open/close + a shell-approval surface per command, and is demonstrably worse than a session-scoped stdio MCP subprocess. Check statefulness before choosing the transport.

### 14. One output format for all consumers
Returning the same format (typically JSON or Markdown) regardless of whether an agent or a human consumes the output forces one consumer to do extra work. Agent-consumed output should be structured and parseable; human-consumed output at review gates should be navigable (HTML with annotations, severity colors, jump links); subjective choices should see side-by-side variations. Match the format to the decision being made.

### 15. SDK-coupled skills
Skills that reference SDK-specific tool names, assume specific built-in capabilities, or embed framework API calls lose portability when the infrastructure changes. Skills should describe capabilities in natural language ("run a shell command") rather than referencing specific tool implementations ("use the Bash tool"). The skill should survive an infrastructure migration without modification.

### 16. Global skill loading at scale
Loading 15+ skills globally forces the agent to disambiguate among all of them for every task — adding latency and increasing the risk of wrong-skill invocation. Map skills to workspaces and task types. The agent receives only what is contextually relevant, and skills that could cause harm in the wrong context (production deployment tools during a writing task) are structurally excluded.

### 17. Swapping toolsets to implement modes
Implementing plan mode (or any restricted mode) by removing tools from the declared list invalidates the prompt cache on every mode toggle — tool definitions live in the cached prefix. Represent modes as always-present transition tools plus injected instructions, with enforcement in the permission layer. And do not mistake instruction-only modes for enforced modes: if the harness never rejects out-of-mode calls, mode discipline rests entirely on model compliance.

### 18. Time-driven polling where an event stream exists
A `/loop 2m` watching a dev server pays a full API call every 2 minutes whether or not anything happened — over a long session this is a substantial silent tax. If the watched process emits logs or stdout, use an event-driven monitor that costs zero tokens between matching events. Reserve polling for systems with no observable event stream — and when you do use a monitor, validate the filter pattern: a wrong filter silently produces no events.

### 19. Shipping MCP without workflow knowledge
An MCP integration without companion skills leaves users connected to a service they don't know how to use for real workflows: support tickets, inconsistent results, and blame directed at the connector when the gap is workflow guidance. Ship MCP + skills together, and version the skills against the MCP server's tool surface so a server upgrade doesn't orphan the workflow layer.

### 20. Testing a skill on one surface, shipping to another
The SKILL.md format is portable; the runtime is not. A skill that fetches a URL works on Claude Code (full network), may work on Claude.ai (admin policy), and fails on the Claude API (no network, pre-installed packages only). Test on the actual target surface, declare requirements in the `compatibility` field, and design shared skill libraries for the most restricted target. Runtime constraints are invisible at install time — the failure appears in production.

### 21. Bundled scripts with hidden dependencies
A script inside a skill can require a Python version, packages, or OS tools that nothing declares. It works on the author's machine and fails at runtime elsewhere with no clean recovery path. Declare dependencies, use portable path references (`${CLAUDE_SKILL_DIR}`), mark scripts as executable vs. documentation, and remember the security surface: the script's body is not visible in the system prompt, so audit before trusting.

### 22. Additive-only harness growth
Every tool, skill, integration, and exception added makes the agent look more capable while widening the behavior space it must navigate — and past the build phase, additions degrade trust faster than they add capability. Vercel's sales agent improved when 80% of its tools were deleted. Schedule subtractive review; run pruning trials against your eval set; track per-tool invocation rates. The discipline is the recurring review, not any particular deletion ratio — and pruning without evals risks deleting the rarely-but-critically-needed tool.

### 23. Deploying a subscription-backed agent to multiple users
SDK subscription plans are licensed to the individual subscriber; multi-user deployment violates ToS and account bans are documented. The API-key alternative costs 10-50x more, which changes the architecture calculus entirely. Ask "who uses this agent?" before building, not at launch — a full product built on subscription economics may need an expensive rewrite when the boundary surfaces.

---

## Related Guides

- **Tool risk classification -> permission tiers:** The risk levels (safe/mutating/destructive) in Step 2 feed directly into the permission architecture in *Agent Safety and Permissions* (G6), Step 1. Mode enforcement via the permission layer (Step 5) is the same machinery.
- **Deferred loading -> context curation:** Deferred tool loading in Step 5 is an application of the context curation principles in *Managing Agent Context* (G2a), and the static-tool-surface constraint is a prompt-cache-stability instance of the degradation defenses in *Defending Against Context Degradation* (G2b). The search-over-list pattern is a tool-specific instance of the broader "load selectively" principle. Contextual skill scoping (Step 13) is the skill-level analog.
- **Programmatic execution -> context efficiency:** Keeping intermediates out of context in Step 7 — including bundled scripts whose code never loads — follows the selective loading principles in *Structuring and Loading Agent Context* (G2a).
- **Harness pruning -> context rot defense:** The subtractive-review discipline in Step 16 is the tool-surface analog of the rule-accumulation rot defenses in *Defending Against Context Degradation* (G2b), and pruning trials depend on the eval suites in *Building Agent Evaluation Suites* (G4).
- **Event-driven watching -> production operations:** Step 8's monitor-vs-poll decision feeds the cost-control and observability practices in *Agent Workflow and Execution* (G3b).
- **Think tool prompting -> model-agnostic properties:** Domain-specific think tool prompts in Step 10 should follow the three properties in *Model-Resilient Prompt Engineering* (G8), Step 1.
- **Tool contract model -> spec writing:** The non-deterministic contract in Step 1 shapes how tool behaviors are specified in *Writing Agent Specifications* (G1).
- **Skill wrapping -> agent architecture:** Wrapping CLI pipelines as skills (Step 7) interfaces with the delegation model in *Agent Architecture Decisions* (G3), where the orchestrator must decide whether to invoke a skill directly or decompose it. The SDK-vs-framework economics in Step 15 (including the subscription ToS boundary) extend G3's infrastructure analysis.
- **MCP integration in agentic systems:** *[[building-agentic-systems]]* (G11) Section 5 (Querying) references MCP integration patterns from this guide in the context of vault-native agentic OS toolchains.
- **Interceptor middleware -> safety architecture:** The blocking capability of event interceptors and deterministic hooks in Step 11 complements the permission tier model in *Agent Safety and Permissions* (G6) — interceptors enforce runtime policy; permission tiers enforce capability grants.
- **CLI-first integration -> agent design patterns:** The CLI-first rule and its statefulness boundary (Step 4) align with the environment-native principle in *Agent Design Patterns* (G4/G10) — tools should match the agent's native execution environment.
- **Skills portability -> SDK vs. framework decision:** The portability of SKILL.md files across boundaries (Step 14) reinforces the SDK vs. framework analysis in *Agent Architecture Decisions* (G3) — skills are the durable capability layer regardless of infrastructure choice.
- **Visual review output -> human gating:** The reusable-component and variations-grid patterns in Step 9 serve the human-oversight gates in *Agent Governance and Trust* (G9) — review artifacts the human can actually engage with keep the gate meaningful.

---

## Contract

### Preconditions
- You are designing, refactoring, or auditing tools that agents will use.
- You have tools that agents invoke via function calling, MCP, CLI, or equivalent.
- You understand the non-deterministic contract: agents choose whether and how to use your tools.

### Invariants
- Tool definitions are data first — metadata exists before implementation.
- Graded capabilities are declared as tiered discriminated values with per-tier consumer behavior, not booleans.
- Tool interfaces make common errors structurally impossible (poka-yoke); mechanical "never X, always Y" rules are enforced by deterministic hooks, not instructions.
- Tool descriptions are designed for non-deterministic consumers — they persuade, disambiguate, and explain when not to use the tool.
- Only tools needed for the current task are loaded into context — via name-only stubs and on-demand schemas, never by mutating the declared tool list mid-session.
- Modes are represented as always-present transition tools plus injected instructions, with enforcement in the permission layer; the tool surface is session-static.
- Intermediate tool results stay outside the context window when the agent only needs the final output; deterministic logic runs as bundled scripts whose code never enters context.
- Complex tools include usage examples that teach correct parameter patterns beyond what schemas convey.
- Interceptors that mutate arguments are responsible for producing valid output — no re-validation runs after mutation.
- Shared skills are versioned and locked; silent overwrites and version drift are treated as distribution failures.
- CLI tools are preferred over protocol-wrapped equivalents (MCP) when the agent operates in a terminal-native environment, a CLI exists, and the tool is stateless; stateful local tools use a session-scoped typed server (stdio MCP subprocess).
- Background watching is event-driven by default; time-driven polling is a fallback for systems with no observable event stream.
- Tool output format matches the consumer — structured data for agents, navigable documents for human review gates, side-by-side variations for subjective choices, reusable component libraries for recurring review artifacts.
- Skills are framework-agnostic markdown files — portable across SDKs and agent frameworks at the file-shape level, with per-surface runtime requirements declared in the `compatibility` field.
- Skills are scoped to workspaces and task types, not loaded globally, when the skill surface exceeds five capabilities.
- The harness surface (tools, skills, servers, hooks, rules) receives recurring subtractive review; additions are not permanent.

### Governance
- Tool registries are maintained as governed artifacts. Interface changes require review.
- Risk classifications (safe/mutating/destructive) are reviewed when tool capabilities change.
- Capability tier declarations are verified against actual provider behavior on a cadence — unverified tiers are flagged.
- Integration type (mcp/cli/builtin/headless) is recorded in the registry and reviewed when new integration options emerge for existing tools; statefulness is recorded as a transport-decision input.
- Tool descriptions are treated as UX copy — reviewed for clarity, disambiguation, and action-verb fronting.
- Usage examples are maintained alongside schema definitions and updated when tool behavior changes.
- Interceptor and hook load order is documented alongside handler registration; changes to load order require review. Context-file rules are periodically audited for conversion to deterministic hooks.
- Skills lock files are committed to version control and updated whenever a shared skill version changes.
- Workspace skill routing tables are reviewed when new skills are added or task types change.
- Tool output formats are reviewed when the consumer changes (agent-only to human-gated, or vice versa); recurring review artifacts maintain their component library as a governed asset.
- Harness pruning reviews are scheduled recurring events with eval-verified deletions, not ad-hoc cleanups.
- The subscription ToS single-user boundary is checked before any multi-user deployment decision.
- This guide is owned by Meta-System knowledge layer.

### Recovery
- If agents choose the wrong tool: improve descriptions and add usage examples before adding prompt instructions.
- If tool invocations fail frequently: audit the interface for poka-yoke opportunities before debugging the agent's prompting.
- If context is bloated with tool definitions: implement deferred loading via Tool Search or filesystem progressive discovery — keeping the declared list static.
- If prompt cache hit rates collapse: check for mid-session tool list mutations (including mode implementations that swap toolsets); convert modes to transition tools.
- If multi-tool workflows are slow or producing large context: evaluate code-orchestrated execution, bundled scripts for deterministic steps, or switch from MCP to CLI integration for stateless tools.
- If a per-call CLI integration to a stateful tool is slow or approval-heavy: switch to a long-lived local stdio MCP subprocess; verify it has reload semantics for externally-changed state.
- If a background watcher is consuming tokens at idle: replace time-driven polling with an event-driven monitor; validate the filter against real output.
- If skill-wrapped pipelines break silently: add health checks between steps and surface which step failed.
- If bundled scripts fail on a new surface: check declared dependencies, path portability (`${CLAUDE_SKILL_DIR}`), and the target surface's network/package constraints.
- If intelligence stores return stale data: implement incremental updates and staleness indicators before expanding the store.
- If a mutating interceptor produces downstream failures: add output validation inside the handler and check load order against other interceptors.
- If the model keeps violating a mechanical rule: convert the instruction into a pre-tool-use hook.
- If installed skills diverge from expected versions: run `npx skills verify` against the lock file before diagnosing agent behavior issues.
- If MCP tool integration is consuming excessive tokens: check whether a CLI exists for the same (stateless) tool; switch to CLI for terminal-native agents.
- If tool output at human review gates is being skimmed or missed: upgrade to HTML with annotations, severity colors, and jump links; for recurring artifacts, adopt a reusable component library.
- If humans cannot articulate what they want from generative output: render N distinct variations side-by-side and let them select by recognition.
- If skills break after infrastructure migration: audit for SDK-specific references; skills should be plain markdown with no framework coupling.
- If agents invoke the wrong skill in a multi-skill environment: implement workspace-scoped skill routing to reduce the disambiguation surface.
- If the agent has grown less trustworthy as capabilities accumulated: run an eval-verified pruning trial across the harness surface before adding anything else.
- If a multi-user deployment is planned on subscription infrastructure: stop; redesign for API-key economics (typically framework-based) before launch.
