---
title: "Designing Agent Tools"
type: "guideline"
category: "Tool Integration"
target_system:
  - "cross-system"
stage: "draft"
created: "2026-04-19"
updated: "2026-04-19"
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
source_dd:
  - "DD-81"
tags:
  - "guide"
  - "tools"
contract:
  preconditions: "You are designing, refactoring, or auditing tools that agents will use. You understand the difference between tool definitions (metadata) and tool implementations (code). You have tools that agents invoke via function calling, MCP, or equivalent."
  invariants: "Tool definitions are data first — metadata exists before implementation. Tool interfaces make common errors structurally impossible. Only tools needed for the current task are loaded into context. Intermediate tool results stay outside the context window when the agent only needs the final output. Tool descriptions are designed for non-deterministic consumers — agents choose whether and how to use them."
  governance: "Tool registries are maintained as governed artifacts. Interface changes require review. Tool descriptions are treated as UX copy, not documentation. This guide is owned by Meta-System knowledge layer."
  recovery: "If tool invocations fail frequently: audit the interface for poka-yoke opportunities before debugging the agent's prompting. If context is bloated with tool definitions: implement deferred loading. If multi-tool workflows are slow: evaluate programmatic tool calling. If agents choose the wrong tool: improve descriptions and add usage examples before adding instructions."
---

# Designing Agent Tools

How to design tools that agents discover, invoke correctly, and use efficiently. This guide covers six concerns: the non-deterministic contract between agents and tools, how to build a metadata-first registry, how to error-proof interfaces, how agents find tools without context bloat, how multi-tool workflows stay efficient, and how agents reason between tool calls.

## When to Use This Guide

- You are designing new tools for an agent system
- You are connecting an agent to MCP servers or external APIs
- Tool definition tokens are consuming a significant fraction of context
- Agents are choosing the wrong tool or making frequent invocation errors
- Multi-tool workflows are slow, producing bloated context, or losing accuracy
- You are wrapping an existing CLI pipeline as an agent-invocable skill
- You are deciding between SDK-native tools, MCP servers, or script wrappers

## Key Concepts

**1. Tools are a non-deterministic contract.** Unlike function calls in code where the caller must invoke and handle the return, agents decide whether to call a tool at all, which tool to call, what parameters to pass, and how to interpret the response. Tool design is closer to UX design than API design — you must make the right tool the obvious choice. This reframing is the prerequisite for every other principle in this guide.

**2. Tools are data first.** Define capabilities as a metadata registry before implementing them. Agents should reason about available capabilities without executing anything. Two parallel registries serve different consumers: user-facing commands and model-facing tools. The registry enables runtime filtering, dynamic tool pool assembly, and permission management at the metadata level.

**3. Make errors structurally impossible.** Borrowing from manufacturing's poka-yoke philosophy, tool interfaces should prevent errors through structure, not instructions. Requiring absolute filepaths instead of relative ones eliminated an entire class of path errors in SWE-bench. Embedding usage examples in tool definitions improved complex parameter accuracy from 72% to 90%.

**4. Load tools on demand, not upfront.** With dozens of MCP servers, tool definitions alone can consume 134K+ tokens. Two converging approaches — keyword-based Tool Search and filesystem progressive discovery — achieve 47-98.7% token reduction by loading definitions only when needed. Prefer search-style tools over list-style tools: agents have limited context but abundant compute.

**5. Keep intermediates out of context.** When an agent orchestrates multi-tool workflows, intermediate results should stay in the execution environment. Only the final filtered output enters the model context — achieving up to 98.7% token reduction and accuracy gains of 5-10 percentage points on benchmarks.

**6. Give agents a scratchpad.** A "think" tool with no side effects lets agents reason between tool calls without executing anything. Domain-specific prompting of when to use the scratchpad improves policy compliance by up to 76%.

**7. Wrap complex pipelines as skills.** Multi-step CLI workflows (scripts, Docker operations, file management) can be encapsulated as natural-language-invocable skills, eliminating cognitive overhead while preserving pipeline reliability.

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
    source: "{{MCP_SERVER_OR_BUILTIN}}"
    description: "{{ACTION_VERB — front-load what it does}}"
    category: "{{read/write/execute/query}}"
    risk_level: "{{safe/mutating/destructive}}"
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
- Metadata is queryable — agents can filter tools by category, risk level, or keyword without loading full definitions
- Implementations load on demand (lazy loading)
- Two registries: one for user-facing commands, one for model-facing tools
- Risk classification (safe/mutating/destructive) maps to the permission system
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

### Step 4: Implement Discovery and Loading

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

### Step 5: Design Multi-Tool Execution

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

### Step 6: Add a Think Tool for Complex Chains

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

### Step 7: Choose Your Infrastructure Layer

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
| Best for | Prototyping, personal tools | Production, scale | Client automations |

**MCP is baseline infrastructure.** With 97M installs, 4,000+ servers, and universal provider support, MCP is no longer an adoption decision. The question is whether you are using MCP deeply enough — audit your tool surface against the available server catalog.

**Queryable intelligence stores.** For tools that provide codebase or domain intelligence, consider persistent structured stores (e.g., `.planning/intel/` with JSON for files, symbols, dependencies) queryable via CLI. This converts repeated O(n) discovery cost into O(1) lookup. Key risk: stale data is worse than no data — build in freshness indicators and incremental update mechanisms.

---

## Templates

### Tool Definition Template

```yaml
# Tool Definition — {{TOOL_NAME}}
name: "{{TOOL_NAME}}"
source: "{{MCP_SERVER_NAME | builtin | skill}}"
description: "{{ACTION_VERB + OBJECT + KEY_CONSTRAINT — max 1 sentence}}"
category: "{{read | write | execute | query}}"
risk_level: "{{safe | mutating | destructive}}"
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
```

**Worked Example:**

```yaml
name: "search_findings"
source: "research-kb-mcp"
description: "Search research findings by keyword, category, or evidence strength"
category: "query"
risk_level: "safe"
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
```

### Tool Design Audit Worksheet

```markdown
## Tool Audit — {{SYSTEM_NAME}}

### Contract Model
- [ ] Tool descriptions front-load the action verb
- [ ] Similar tools have disambiguation guidance in descriptions
- [ ] Response formats are structured and interpretable

### Registry Health
- [ ] All tools have metadata entries (name, description, category, risk_level)
- [ ] Metadata is queryable without loading implementations
- [ ] Risk levels are classified (safe/mutating/destructive)
- [ ] Complex tools have usage examples in definitions

### Interface Quality (per tool)
| Tool | Poka-Yoke Opportunities | Current Interface | Improved Interface |
|------|------------------------|-------------------|-------------------|
| {{TOOL}} | {{ISSUE}} | {{CURRENT}} | {{FIXED}} |

### Discovery Assessment
| Metric | Value |
|--------|-------|
| Total tool definitions | {{COUNT}} tools |
| Estimated definition tokens | ~{{TOKENS}} tokens |
| Loading strategy | {{UPFRONT / DEFERRED / HYBRID}} |
| List-style tools to convert to search | {{LIST}} |

**Decision:** If definitions > 10K tokens or > 10 tools, implement deferred loading.

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
- Intelligence store: {{NONE / PLANNED / ACTIVE}}
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
- [ ] Complex tools have usage examples — some skills have worked examples, most don't

### Interface Quality
| Tool | Poka-Yoke Opportunities | Current | Improved |
|------|------------------------|---------|----------|
| /extract-artifacts | Report path is free-text | Any path accepted | Validate report exists in operations/ |
| /research-loop | URL list is unbounded | Any count accepted | Max 10 URLs per invocation |
| /pdf-to-markdown | File path can be relative | Accepts relative paths | Require absolute path or URL |

### Discovery Assessment
| Metric | Value |
|--------|-------|
| Total tool definitions | ~40 skills + 50+ MCP tools |
| Estimated definition tokens | ~2K per skill listing, MCP loaded upfront |
| Loading strategy | HYBRID — skills deferred (SKILL.md on invoke), MCP upfront |
| List-style tools to convert to search | Notion list-pages, finding enumeration |

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
- Intelligence store: None — codebase re-scanned each session
```

---

## Pitfalls

### 1. Designing tools like APIs instead of UX
Traditional API design assumes a deterministic caller that must invoke the endpoint. Agent tool design must assume a non-deterministic consumer that chooses whether to use the tool based on its description. If the description is unclear, the agent will guess or work around it — producing worse results than if the tool did not exist. Treat tool descriptions as UX copy: front-load the verb, disambiguate from similar tools, explain when NOT to use it.

### 2. All tool definitions loaded upfront
With 50+ tools, definitions alone can consume 134K tokens. Agents perform worse when drowning in irrelevant tool specs. Load only what is needed for the current task. Both OpenAI and Anthropic now ship deferred loading as a cross-vendor standard.

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

---

## Related Guides

- **Tool risk classification -> permission tiers:** The risk levels (safe/mutating/destructive) in Step 2 feed directly into the permission architecture in *Agent Safety and Permissions* (G6), Step 1.
- **Deferred loading -> context curation:** Deferred tool loading in Step 4 is an application of the context curation principles in *Managing Agent Context* (G2), Step 2. The search-over-list pattern is a tool-specific instance of the broader "load selectively" principle.
- **Programmatic execution -> context efficiency:** Keeping intermediates out of context in Step 5 follows the selective loading principles in *Managing Agent Context* (G2), Step 3.
- **Think tool prompting -> model-agnostic properties:** Domain-specific think tool prompts in Step 6 should follow the three properties in *Model-Resilient Prompt Engineering* (G8), Step 1.
- **Tool contract model -> spec writing:** The non-deterministic contract in Step 1 shapes how tool behaviors are specified in *Writing Agent Specifications* (G1).
- **Skill wrapping -> agent architecture:** Wrapping CLI pipelines as skills (Step 5) interfaces with the delegation model in *Agent Architecture Decisions* (G3), where the orchestrator must decide whether to invoke a skill directly or decompose it.
- **MCP integration in agentic systems:** *[[building-agentic-systems]]* (G11) Section 5 (Querying) references MCP integration patterns from this guide in the context of vault-native agentic OS toolchains.

---

## Contract

### Preconditions
- You are designing, refactoring, or auditing tools that agents will use.
- You have tools that agents invoke via function calling, MCP, or equivalent.
- You understand the non-deterministic contract: agents choose whether and how to use your tools.

### Invariants
- Tool definitions are data first — metadata exists before implementation.
- Tool interfaces make common errors structurally impossible (poka-yoke).
- Tool descriptions are designed for non-deterministic consumers — they persuade, disambiguate, and explain when not to use the tool.
- Only tools needed for the current task are loaded into context.
- Intermediate tool results stay outside the context window when the agent only needs the final output.
- Complex tools include usage examples that teach correct parameter patterns beyond what schemas convey.

### Governance
- Tool registries are maintained as governed artifacts. Interface changes require review.
- Risk classifications (safe/mutating/destructive) are reviewed when tool capabilities change.
- Tool descriptions are treated as UX copy — reviewed for clarity, disambiguation, and action-verb fronting.
- Usage examples are maintained alongside schema definitions and updated when tool behavior changes.
- This guide is owned by Meta-System knowledge layer.

### Recovery
- If agents choose the wrong tool: improve descriptions and add usage examples before adding prompt instructions.
- If tool invocations fail frequently: audit the interface for poka-yoke opportunities before debugging the agent's prompting.
- If context is bloated with tool definitions: implement deferred loading via Tool Search or filesystem progressive discovery.
- If multi-tool workflows are slow or producing large context: evaluate code-orchestrated execution to move orchestration into code.
- If skill-wrapped pipelines break silently: add health checks between steps and surface which step failed.
- If intelligence stores return stale data: implement incremental updates and staleness indicators before expanding the store.
