---
title: "Designing Agent Tools"
type: "guideline"
category: "Tool Integration"
target_system:
  - "improvement-loop"
stage: "draft"
created: "2026-04-19"
updated: "2026-05-25"
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
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "tools"
contract:
  preconditions: "You are designing, refactoring, or auditing tools that agents will use. You understand the difference between tool definitions (metadata) and tool implementations (code). You have tools that agents invoke via function calling, MCP, CLI, or equivalent."
  invariants: "Tool definitions are data first — metadata exists before implementation. Tool interfaces make common errors structurally impossible. Only tools needed for the current task are loaded into context. Intermediate tool results stay outside the context window when the agent only needs the final output. Tool descriptions are designed for non-deterministic consumers — agents choose whether and how to use them. CLI tools are preferred over protocol-wrapped equivalents when the agent operates in a terminal-native environment. Skills are framework-agnostic — portable across SDKs and agent frameworks without modification."
  governance: "Tool registries are maintained as governed artifacts. Interface changes require review. Tool descriptions are treated as UX copy, not documentation. Tool output formats are designed for the consumer — human-gate outputs use navigable formats (HTML with annotations); agent-consumed outputs use structured data. This guide is owned by Meta-System knowledge layer."
  recovery: "If tool invocations fail frequently: audit the interface for poka-yoke opportunities before debugging the agent's prompting. If context is bloated with tool definitions: implement deferred loading. If multi-tool workflows are slow: evaluate programmatic tool calling or CLI-first integration. If agents choose the wrong tool: improve descriptions and add usage examples before adding instructions. If skills break after infrastructure migration: verify skill portability — skills should be framework-agnostic markdown, not SDK-coupled code."
---

# Designing Agent Tools

How to design tools that agents discover, invoke correctly, and use efficiently. This guide covers twelve concerns: the non-deterministic contract between agents and tools, how to build a metadata-first registry, how to error-proof interfaces, how agents find tools without context bloat, how multi-tool workflows stay efficient, how agents reason between tool calls, how to intercept and control tool execution without modifying tools, how to manage shared skills across projects, how to choose the right integration layer (CLI vs. MCP vs. headless mode), how to compose multi-tool environments across IDE and terminal boundaries, how to design tool output for human review gates, and how to scope skills contextually within workspaces.

## When to Use This Guide

- You are designing new tools for an agent system
- You are connecting an agent to MCP servers, CLI tools, or external APIs
- You are choosing between CLI and MCP integration for a tool that supports both
- Tool definition tokens are consuming a significant fraction of context
- Agents are choosing the wrong tool or making frequent invocation errors
- Multi-tool workflows are slow, producing bloated context, or losing accuracy
- You are wrapping an existing CLI pipeline as an agent-invocable skill
- You are deciding between SDK-native tools, MCP servers, CLI wrappers, or headless mode
- You need to enforce policies or transform arguments without modifying existing tools
- You are distributing shared skills across multiple projects, agents, or frameworks
- You are composing multiple tool environments (IDE + CLI agent) into a single workspace
- Tool output is consumed by human reviewers and needs navigable formatting

## Key Concepts

**1. Tools are a non-deterministic contract.** Unlike function calls in code where the caller must invoke and handle the return, agents decide whether to call a tool at all, which tool to call, what parameters to pass, and how to interpret the response. Tool design is closer to UX design than API design — you must make the right tool the obvious choice. This reframing is the prerequisite for every other principle in this guide.

**2. Tools are data first.** Define capabilities as a metadata registry before implementing them. Agents should reason about available capabilities without executing anything. Two parallel registries serve different consumers: user-facing commands and model-facing tools. The registry enables runtime filtering, dynamic tool pool assembly, and permission management at the metadata level.

**3. Make errors structurally impossible.** Borrowing from manufacturing's poka-yoke philosophy, tool interfaces should prevent errors through structure, not instructions. Requiring absolute filepaths instead of relative ones eliminated an entire class of path errors in SWE-bench. Embedding usage examples in tool definitions improved complex parameter accuracy from 72% to 90%.

**4. Load tools on demand, not upfront.** With dozens of MCP servers, tool definitions alone can consume 134K+ tokens. Two converging approaches — keyword-based Tool Search and filesystem progressive discovery — achieve 47-98.7% token reduction by loading definitions only when needed. Prefer search-style tools over list-style tools: agents have limited context but abundant compute.

**5. Keep intermediates out of context.** When an agent orchestrates multi-tool workflows, intermediate results should stay in the execution environment. Only the final filtered output enters the model context — achieving up to 98.7% token reduction and accuracy gains of 5-10 percentage points on benchmarks.

**6. Give agents a scratchpad.** A "think" tool with no side effects lets agents reason between tool calls without executing anything. Domain-specific prompting of when to use the scratchpad improves policy compliance by up to 76%.

**7. Wrap complex pipelines as skills.** Multi-step CLI workflows (scripts, Docker operations, file management) can be encapsulated as natural-language-invocable skills, eliminating cognitive overhead while preserving pipeline reliability.

**8. Intercept, don't modify.** The tool-call event interception pattern lets extensions enforce policies and transform arguments by subscribing to execution events — without touching tool source code. This is the right approach when you need to apply cross-cutting concerns (logging, argument normalization, permission enforcement) across many tools. The risk is that mutations bypass re-validation and compose in load order; understand both before adopting this pattern.

**9. Treat shared skills as dependencies.** When skills are distributed across projects and agents, they need the same dependency hygiene as software packages: a lock file to pin versions, conflict detection to prevent silent overwrites, and a CLI that manages install targets (project vs. global). Unmanaged skill distribution drifts silently.

**10. Prefer CLI over protocol when the environment is terminal-native.** When a tool exists as both an MCP server and a CLI, and the agent operates in a terminal (e.g., Claude Code), prefer the CLI. Head-to-head benchmarks show CLI integration uses ~90,000 fewer tokens per task and produces more accurate results. MCP adds a process boundary, a protocol layer, and initialization overhead that CLI tools avoid entirely. This maps to a lazy-vs-eager loading distinction: MCP servers load all tool schemas at startup (eager), while CLI tools are invoked only when needed (lazy).

**11. Design tool output for the consumer.** Agent-consumed output should be structured data (JSON, frontmatter). Human-consumed output at review gates benefits from navigable formats — HTML with margin annotations, severity colors, and jump links outperforms flat text for complex multi-file reviews. Match the output format to who reads it and what decision they are making.

**12. Scope skills to context, not globally.** Rather than loading all skills at session start (forcing the agent to disambiguate among 15+ options), map skills to workspaces and task types. The agent receives only contextually relevant skills, eliminating disambiguation overhead and preventing unintended skill triggering. This is the skill-level equivalent of deferred tool loading.

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

**Search over list.** When a tool could return all records or search for specific ones, prefer the search interface. Agents have limited context windows but abundant compute — searching is cheaper than listing. Validate across Anthropic's internal MCP servers (Slack, Asana, Claude Code).

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
| Best for | Tools with existing CLIs | GUI tools without CLI equivalents, cross-platform | Programmatic agent orchestration | Core operations (read, write, search) |

**The CLI-first rule for terminal-native agents:** When a tool has both a CLI and an MCP server, and the agent operates in a terminal environment (e.g., Claude Code), default to the CLI. Head-to-head testing of Playwright's MCP server vs. CLI showed the CLI was faster and used ~90,000 fewer tokens. The principle generalizes: CLI tools and terminal agents share an environment natively — no process boundary, no protocol overhead, no eager schema loading.

**When MCP is still correct:**
- The tool has no CLI equivalent (GUI-native tools, OAuth-gated APIs)
- Cross-platform portability matters more than token efficiency
- The tool requires persistent connection state (WebSocket-based protocols)
- You are operating in a non-terminal environment (IDE extension, web app)

**Headless mode (`claude -p`) for programmatic orchestration:** When you need to invoke an agent itself as a tool — controlling trigger, context, tools, and output from a script — headless mode provides full programmatic control without any framework dependency. Key flags: `--append-system-prompt` (adds to default prompt), `--system-prompt` (replaces it entirely), `--resume` (session persistence), `--tools` (tool subset control). This replaces proprietary agent platforms for single-developer automation: readable, modifiable, auditable bash scripts with no abstraction layers.

**Browser automation as a specific CLI case.** Playwright CLI exemplifies the CLI-first principle for browser automation: headless browser control via the accessibility tree, parallel sessions, deterministic waits, and 76-99% token savings over Chrome extension approaches. For any web UI that lacks an API, Playwright CLI is the preferred tool before considering visual/screenshot-based automation.

### Step 5: Implement Discovery and Loading

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

### Step 6: Compose Multi-Tool Environments

When an agent operates across multiple tool environments — IDE, terminal, browser — each layer needs a clear role to prevent tool routing collisions and config drift.

**Decision: Who owns what?**

| Layer | Role | Tool Source | Example |
|-------|------|-------------|---------|
| IDE (Cursor) | Code intelligence, inline completion | `.cursor/mcp.json` as canonical MCP config | Cursor with MCP servers |
| Terminal agent (Claude Code) | Agentic execution, multi-step workflows | CLI tools + skills + deferred MCP | Claude Code in terminal panel |
| Browser automation | Web UI interaction | Playwright CLI | Headless browser via accessibility tree |

**Composition principles:**
- **Single source of truth for MCP config.** When both IDE and terminal agent can register MCP servers, designate one config file as canonical (e.g., `.cursor/mcp.json`). Config drift between environments is a silent failure.
- **Respect tool ceilings.** Claude Code has a 40-tool MCP limit. Audit registrations when adding new servers and prune low-priority tools before hitting the ceiling.
- **Separate concerns by layer.** The IDE handles code intelligence; the terminal agent handles execution. If both try to do the same thing (e.g., both run linting), they collide. Assign each capability to exactly one layer.
- **Version-control tool configs.** Committing `.cursor/mcp.json` and skills directories to the repo makes the tool environment reproducible across machines and team members.

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

### Step 8: Design Tool Output for the Consumer

Tool output format should match the consumer and the decision they are making. Agent-consumed output and human-consumed output have different design constraints.

**Decision: Who consumes this output?**

| Consumer | Format | Design Priority | Example |
|----------|--------|-----------------|---------|
| Agent (next tool call) | Structured data (JSON, YAML) | Parseability, field clarity | API response with typed fields |
| Agent (reasoning) | Concise text with key facts | Information density, relevance | Search result summaries |
| Human (review gate) | Navigable document | Scanability, severity signaling | HTML PR explainer |
| Human (operational) | Dashboard or log | Trends, anomalies | Monitoring output |

**HTML output for human review gates.** When tool output feeds a human decision point — code review, PR approval, audit sign-off — flat text and Markdown lose navigability for complex changes. The HTML PR explainer pattern demonstrates a more effective format:

- **Margin annotations** explaining why specific changes were made
- **Severity colors** distinguishing critical changes from cosmetic ones
- **Jump links** for navigating between related changes across files

This pattern is used habitually by Anthropic engineers on the Claude Code codebase itself. The HTML artifact is a review companion alongside the standard diff, not a replacement for it.

**When to generate navigable output:**
- Multi-file changes where cross-file relationships matter
- Changes touching security-sensitive code or API surfaces
- Reviews where the reviewer is not the author (context gap is large)
- Do NOT generate HTML for single-file, small-diff changes — the overhead exceeds the benefit

**Output format template:**

```yaml
output:
  consumer: "{{agent | human-review | human-operational}}"
  format: "{{json | yaml | markdown | html}}"
  annotations: {{true | false}}  # margin annotations for review output
  severity_signals: {{true | false}}  # color/icon severity classification
  navigation: {{true | false}}  # jump links between related sections
```

### Step 9: Add a Think Tool for Complex Chains

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

### Step 10: Build Tool Execution Middleware

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

**When to use this vs. poka-yoke (Step 3):** Poka-yoke constraints are the right first choice — they enforce correctness at definition time with zero runtime overhead and no composition risk. Interception is the right choice when you cannot modify the tool definition (third-party MCP servers), need runtime context unavailable at definition time (user permissions, session state), or are applying concerns consistently across a large tool surface.

### Step 11: Manage Shared Skills as Dependencies

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

**Worked Example:**

```json
{
  "version": "1",
  "skills": {
    "research-loop": {
      "version": "2.3.1",
      "source": "registry:improvement-loop/skills",
      "target": "project",
      "checksum": "a1b2c3d4..."
    },
    "pdf-to-markdown": {
      "version": "1.0.4",
      "source": "registry:improvement-loop/skills",
      "target": "global",
      "checksum": "e5f6g7h8..."
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

### Step 12: Scope Skills to Workspaces

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

### Step 13: Design Skills for Portability

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

**What breaks portability:**
- Skills that reference SDK-specific tool names (e.g., `Bash` instead of generic "run a shell command")
- Skills that assume specific built-in tools (file search, grep) without describing the capability needed
- Skills with embedded code that calls framework APIs directly
- Skills that depend on harness-specific features (session persistence, tool interception) without fallback

**The durable investment.** Skills are emerging as the primary capability layer for AI agents — more portable than tools (which have framework-specific APIs), more accessible than MCP servers (which require protocol support), and more maintainable than custom code (which is tightly coupled). Invest in skills first; choose the infrastructure layer second.

### Step 14: Choose Your Infrastructure Layer

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

**MCP is baseline infrastructure.** With 97M installs, 4,000+ servers, and universal provider support, MCP is no longer an adoption decision. The question is whether you are using MCP deeply enough — audit your tool surface against the available server catalog. But remember the CLI-first rule: when a CLI exists for a tool and the agent is terminal-native, CLI beats MCP on every efficiency metric.

**Headless mode as the zero-dependency orchestration layer.** `claude -p` provides the thinnest possible agent infrastructure: a bash script controls trigger (cron, webhook, manual), context (system prompt flags), tools (--tools for subset control), and output (stdout). No framework, no dependency management, no abstraction layers. Every line is readable and modifiable. Use this when the SDK is too heavy and a framework is unnecessary — single-developer automation, scheduled agents, or pipeline glue between systems.

**Queryable intelligence stores.** For tools that provide codebase or domain intelligence, consider persistent structured stores (e.g., `.planning/intel/` with JSON for files, symbols, dependencies) queryable via CLI. This converts repeated O(n) discovery cost into O(1) lookup. Key risk: stale data is worse than no data — build in freshness indicators and incremental update mechanisms.

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
  consumer: "{{agent | human-review | human-operational}}"
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
- [ ] Complex tools have usage examples in definitions

### Interface Quality (per tool)
| Tool | Poka-Yoke Opportunities | Current Interface | Improved Interface |
|------|------------------------|-------------------|-------------------|
| {{TOOL}} | {{ISSUE}} | {{CURRENT}} | {{FIXED}} |

### Integration Layer
| Tool | Has CLI? | Has MCP? | Current Integration | Recommended |
|------|----------|----------|--------------------|--------------------|
| {{TOOL}} | {{YES/NO}} | {{YES/NO}} | {{CURRENT}} | {{CLI if terminal-native, MCP otherwise}} |

**Decision:** For each tool with both CLI and MCP, default to CLI in terminal-native agents.

### Discovery Assessment
| Metric | Value |
|--------|-------|
| Total tool definitions | {{COUNT}} tools |
| Estimated definition tokens | ~{{TOKENS}} tokens |
| Loading strategy | {{UPFRONT / DEFERRED / HYBRID}} |
| List-style tools to convert to search | {{LIST}} |

**Decision:** If definitions > 10K tokens or > 10 tools, implement deferred loading.

### Tool Output
- Human review gate outputs: {{LIST — format used (md/html/text)}}
- Candidates for HTML navigable output: {{LIST — multi-file PRs, security reviews}}
- Agent-consumed outputs using structured format: {{YES/NO}}

### Execution Middleware
- Cross-cutting concerns identified: {{LIST — logging, auth, path normalization, etc.}}
- Interceptors registered: {{COUNT}} (list load order explicitly)
- Tools with mutating interceptors: {{LIST}} (confirm handlers produce valid args)
- Mutation composition reviewed: {{YES/NO}}

### Skill Distribution
- Skills shared across projects: {{LIST}}
- Skills lock file present: {{YES/NO — path}}
- Last verified against lock: {{DATE or NEVER}}
- Project vs global conflicts: {{NONE / LIST}}

### Skill Scoping
- Skills loaded globally: {{LIST}}
- Skills mapped to workspaces: {{LIST with workspace names}}
- Workspace routing table present: {{YES/NO}}
- Cross-framework portability verified: {{YES/NO — which frameworks tested}}

### Execution Efficiency
- Multi-tool workflows identified: {{LIST}}
- Candidates for code orchestration: {{LIST}} (3+ dependent calls, large intermediates)
- Candidates for skill wrapping: {{LIST}} (CLI pipelines with 3+ steps)
- Think tool deployed: {{YES/NO}}
- Think tool domain prompts written: {{YES/NO — list domains}}

### Infrastructure
- Platform: {{SDK / FRAMEWORK / MANAGED / HYBRID}}
- MCP servers connected: {{COUNT}}
- MCP catalog audit done: {{YES/NO — date}}
- CLI tools available: {{LIST}}
- Headless agents deployed: {{COUNT — list triggers}}
- Intelligence store: {{NONE / PLANNED / ACTIVE}}
- IDE composition: {{NONE / Cursor+CC / other — config source documented}}
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
- [ ] Complex tools have usage examples — some skills have worked examples, most don't

### Interface Quality
| Tool | Poka-Yoke Opportunities | Current | Improved |
|------|------------------------|---------|----------|
| /extract-artifacts | Report path is free-text | Any path accepted | Validate report exists in operations/ |
| /research-loop | URL list is unbounded | Any count accepted | Max 10 URLs per invocation |
| /pdf-to-markdown | File path can be relative | Accepts relative paths | Require absolute path or URL |

### Integration Layer
| Tool | Has CLI? | Has MCP? | Current | Recommended |
|------|----------|----------|---------|-------------|
| Playwright | Yes | Yes | Not adopted | CLI (terminal-native) |
| Perplexity | No | Yes | MCP | MCP (no CLI) |
| Notion | No | Yes | MCP | MCP (no CLI) |
| Context7 | No | Yes | MCP | MCP (no CLI) |

### Discovery Assessment
| Metric | Value |
|--------|-------|
| Total tool definitions | ~40 skills + 50+ MCP tools |
| Estimated definition tokens | ~2K per skill listing, MCP loaded upfront |
| Loading strategy | HYBRID — skills deferred (SKILL.md on invoke), MCP upfront |
| List-style tools to convert to search | Notion list-pages, finding enumeration |

### Tool Output
- Human review gate outputs: /code-review (markdown), /ship PR description (markdown)
- Candidates for HTML navigable output: /code-review for multi-file changes, /ship for complex PRs
- Agent-consumed outputs using structured format: Yes (frontmatter-based findings, JSON intel stores)

### Execution Middleware
- Cross-cutting concerns: none currently formalized
- Interceptors: 0 registered
- Mutating interceptors: N/A
- Mutation composition: N/A — would benefit argument normalization for /pdf-to-markdown paths

### Skill Distribution
- Skills shared across projects: /pdf-to-markdown, /session-handoff (workspace root)
- Skills lock file: No — skills tracked in CLAUDE.md skill tables only
- Last verified: Never — manual inspection each session
- Conflicts: None detected (single workspace)

### Skill Scoping
- Skills loaded globally: all IL skills via CLAUDE.md table
- Skills mapped to workspaces: partially — skills are grouped by agent role in CLAUDE.md
- Workspace routing table present: No — would benefit from explicit routing
- Cross-framework portability verified: No — single-framework (Claude Code)

### Execution Efficiency
- Multi-tool workflows: /extract-artifacts (parallel Sonnet subagents), /identify-artifacts
- Candidates for code orchestration: research-loop URL batch processing
- Candidates for skill wrapping: PDF-to-findings pipeline (fetch + convert + extract + write)
- Think tool deployed: No
- Think tool domain prompts: N/A — would benefit /identify-artifacts (form classification)

### Infrastructure
- Platform: SDK (Claude Code CLI)
- MCP servers connected: 4 (Context7, Notion, Perplexity, Gmail)
- MCP catalog audit done: No
- CLI tools available: Playwright (not yet adopted), ripgrep, git, gh
- Headless agents deployed: 0 — candidate for scheduled research scans
- Intelligence store: None — codebase re-scanned each session
- IDE composition: Cursor + Claude Code — .cursor/mcp.json is canonical MCP config
```

---

## Pitfalls

### 1. Designing tools like APIs instead of UX
Traditional API design assumes a deterministic caller that must invoke the endpoint. Agent tool design must assume a non-deterministic consumer that chooses whether to use the tool based on its description. If the description is unclear, the agent will guess or work around it — producing worse results than if the tool did not exist. Treat tool descriptions as UX copy: front-load the verb, disambiguate from similar tools, explain when NOT to use it.

### 2. All tool definitions loaded upfront
With 50+ tools, definitions alone can consume 134K tokens. Agents perform worse when drowning in irrelevant tool specs. Load only what is needed for the current task. Both OpenAI and Anthropic now ship deferred loading as a cross-vendor standard. The same principle applies to skills — scope them to workspaces and task types rather than loading all skills globally.

### 3. Instructions instead of structure
"Always use absolute file paths" is an instruction the agent may forget. Making the parameter accept only absolute paths is a structural constraint that cannot be violated. The same applies to enums, required fields, and length limits. Invest in interface design before prompt engineering.

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
A queryable codebase or domain intelligence store converts O(n) rediscovery into O(1) lookup. But stale data is worse than no data — an agent trusting outdated symbol maps generates incorrect code with high confidence. Build in staleness indicators, incremental updates, and freshness checks.

### 11. Mutation without re-validation
When an event interceptor mutates tool arguments, the tool's schema validation does not re-run. A handler that produces malformed arguments will cause a downstream failure with no validation error surfaced — the bug appears far from the cause. Write mutation handlers defensively: validate the output of your mutation before applying it, document the load order, and test composing multiple mutating handlers before deploying to production.

### 12. Unmanaged skill distribution
Copying skill files across projects without a lock file creates version drift: one project gets a buggy fix, another doesn't. Silent overwrites occur when a global install clobbers a project-scoped version. Without conflict detection, the first sign of a problem is often incorrect agent behavior rather than an install error. Adopt lock file management before you have more than two projects sharing a skill.

### 13. MCP when CLI would suffice
Defaulting to MCP integration because it is the "standard" when the agent is terminal-native and a CLI exists wastes ~90,000 tokens per task and adds latency from process boundaries and protocol overhead. Check whether a CLI exists before setting up an MCP server. MCP is correct when there is no CLI, when cross-platform portability is required, or when the agent operates outside a terminal.

### 14. One output format for all consumers
Returning the same format (typically JSON or Markdown) regardless of whether an agent or a human consumes the output forces one consumer to do extra work. Agent-consumed output should be structured and parseable; human-consumed output at review gates should be navigable (HTML with annotations, severity colors, jump links). Match the format to the decision being made.

### 15. SDK-coupled skills
Skills that reference SDK-specific tool names, assume specific built-in capabilities, or embed framework API calls lose portability when the infrastructure changes. Skills should describe capabilities in natural language ("run a shell command") rather than referencing specific tool implementations ("use the Bash tool"). The skill should survive an infrastructure migration without modification.

### 16. Global skill loading at scale
Loading 15+ skills globally forces the agent to disambiguate among all of them for every task — adding latency and increasing the risk of wrong-skill invocation. Map skills to workspaces and task types. The agent receives only what is contextually relevant, and skills that could cause harm in the wrong context (production deployment tools during a writing task) are structurally excluded.

---

## Related Guides

- **Tool risk classification -> permission tiers:** The risk levels (safe/mutating/destructive) in Step 2 feed directly into the permission architecture in *Agent Safety and Permissions* (G6), Step 1.
- **Deferred loading -> context curation:** Deferred tool loading in Step 5 is an application of the context curation principles in *Managing Agent Context* (G2), Step 2. The search-over-list pattern is a tool-specific instance of the broader "load selectively" principle. Contextual skill scoping (Step 12) is the skill-level analog.
- **Programmatic execution -> context efficiency:** Keeping intermediates out of context in Step 7 follows the selective loading principles in *Managing Agent Context* (G2), Step 3.
- **Think tool prompting -> model-agnostic properties:** Domain-specific think tool prompts in Step 9 should follow the three properties in *Model-Resilient Prompt Engineering* (G8), Step 1.
- **Tool contract model -> spec writing:** The non-deterministic contract in Step 1 shapes how tool behaviors are specified in *Writing Agent Specifications* (G1).
- **Skill wrapping -> agent architecture:** Wrapping CLI pipelines as skills (Step 7) interfaces with the delegation model in *Agent Architecture Decisions* (G3), where the orchestrator must decide whether to invoke a skill directly or decompose it.
- **MCP integration in agentic systems:** *[[building-agentic-systems]]* (G11) Section 5 (Querying) references MCP integration patterns from this guide in the context of vault-native agentic OS toolchains.
- **Interceptor middleware -> safety architecture:** The blocking capability of event interceptors in Step 10 complements the permission tier model in *Agent Safety and Permissions* (G6) — interceptors enforce runtime policy; permission tiers enforce capability grants.
- **CLI-first integration -> agent design patterns:** The CLI-first rule (Step 4) aligns with the environment-native principle in *Agent Design Patterns* (G4) — tools should match the agent's native execution environment.
- **Skills portability -> SDK vs. framework decision:** The portability of SKILL.md files across boundaries (Step 13) reinforces the SDK vs. framework analysis in *Agent Architecture Decisions* (G3) — skills are the durable capability layer regardless of infrastructure choice.

---

## Contract

### Preconditions
- You are designing, refactoring, or auditing tools that agents will use.
- You have tools that agents invoke via function calling, MCP, CLI, or equivalent.
- You understand the non-deterministic contract: agents choose whether and how to use your tools.

### Invariants
- Tool definitions are data first — metadata exists before implementation.
- Tool interfaces make common errors structurally impossible (poka-yoke).
- Tool descriptions are designed for non-deterministic consumers — they persuade, disambiguate, and explain when not to use the tool.
- Only tools needed for the current task are loaded into context.
- Intermediate tool results stay outside the context window when the agent only needs the final output.
- Complex tools include usage examples that teach correct parameter patterns beyond what schemas convey.
- Interceptors that mutate arguments are responsible for producing valid output — no re-validation runs after mutation.
- Shared skills are versioned and locked; silent overwrites and version drift are treated as distribution failures.
- CLI tools are preferred over protocol-wrapped equivalents (MCP) when the agent operates in a terminal-native environment and a CLI exists.
- Tool output format matches the consumer — structured data for agents, navigable documents for human review gates.
- Skills are framework-agnostic markdown files — portable across SDKs and agent frameworks without modification.
- Skills are scoped to workspaces and task types, not loaded globally, when the skill surface exceeds five capabilities.

### Governance
- Tool registries are maintained as governed artifacts. Interface changes require review.
- Risk classifications (safe/mutating/destructive) are reviewed when tool capabilities change.
- Integration type (mcp/cli/builtin/headless) is recorded in the registry and reviewed when new integration options emerge for existing tools.
- Tool descriptions are treated as UX copy — reviewed for clarity, disambiguation, and action-verb fronting.
- Usage examples are maintained alongside schema definitions and updated when tool behavior changes.
- Interceptor load order is documented alongside handler registration; changes to load order require review.
- Skills lock files are committed to version control and updated whenever a shared skill version changes.
- Workspace skill routing tables are reviewed when new skills are added or task types change.
- Tool output formats are reviewed when the consumer changes (agent-only to human-gated, or vice versa).
- This guide is owned by Meta-System knowledge layer.

### Recovery
- If agents choose the wrong tool: improve descriptions and add usage examples before adding prompt instructions.
- If tool invocations fail frequently: audit the interface for poka-yoke opportunities before debugging the agent's prompting.
- If context is bloated with tool definitions: implement deferred loading via Tool Search or filesystem progressive discovery.
- If multi-tool workflows are slow or producing large context: evaluate code-orchestrated execution to move orchestration into code, or switch from MCP to CLI integration.
- If skill-wrapped pipelines break silently: add health checks between steps and surface which step failed.
- If intelligence stores return stale data: implement incremental updates and staleness indicators before expanding the store.
- If a mutating interceptor produces downstream failures: add output validation inside the handler and check load order against other interceptors.
- If installed skills diverge from expected versions: run `npx skills verify` against the lock file before diagnosing agent behavior issues.
- If MCP tool integration is consuming excessive tokens: check whether a CLI exists for the same tool; switch to CLI for terminal-native agents.
- If tool output at human review gates is being skimmed or missed: upgrade to HTML with annotations, severity colors, and jump links.
- If skills break after infrastructure migration: audit for SDK-specific references; skills should be plain markdown with no framework coupling.
- If agents invoke the wrong skill in a multi-skill environment: implement workspace-scoped skill routing to reduce the disambiguation surface.
