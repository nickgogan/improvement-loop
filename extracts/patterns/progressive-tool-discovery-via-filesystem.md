---
title: "Progressive Tool Discovery via Filesystem Hierarchy"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "mcp-as-code-api-progressive-tool-discovery"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Tools are structured as callable files in a navigable directory hierarchy. A code execution sandbox with resource limits and monitoring is available. Tool files include self-describing metadata (signature, description, parameter schema) readable without execution."
  invariants: "Tool definitions are never loaded into context upfront — all discovery is on-demand via filesystem navigation. Intermediate results stay in the execution environment by default and are only returned to the model when explicitly requested. Code execution is sandboxed with resource limits."
  governance: "Owned by Meta-System knowledge layer. Changes to the filesystem layout convention or tool file schema require a Design Decision. Sandbox security configuration is reviewed when new tool servers are added."
  recovery: "If filesystem exploration fails to locate a needed tool, fall back to a search index (Tool Search Tool) rather than loading all definitions. If code execution produces an error, surface the error message to the model for correction rather than retrying blindly. If sandbox limits are hit, report the constraint rather than escalating privileges."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Progressive Tool Discovery via Filesystem Hierarchy

**Source:** [[mcp-as-code-api-progressive-tool-discovery]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent systems connected to multiple MCP servers suffer from token bloat: all tool definitions are loaded into context upfront, consuming tens of thousands of tokens before any work begins. In Anthropic's experience, tool definitions alone consumed up to 134,000 tokens, with 50,000+ tokens used before a single request in some MCP code execution setups. This creates a destructive tradeoff — connecting to more tool servers (expanding capability) directly reduces available context for the actual task (reducing quality). Additionally, raw tool results are returned in full to the model even when only a fraction is relevant, further wasting context on data filtering that could happen programmatically.

## Forces

- **Capability breadth vs. context budget.** Each additional MCP server adds tool definitions to the upfront context load. More tools means more capability but less room for task context. At scale, the tool definitions crowd out the work.
- **Eager loading vs. discovery latency.** Loading all definitions upfront ensures zero-latency tool invocation but wastes tokens on tools never used. On-demand discovery saves tokens but adds navigation steps before first use.
- **Inference-driven vs. code-driven orchestration.** Chaining tool calls through inference (model decides each step) is flexible but expensive and slow. Code-driven orchestration (loops, conditionals, error handling in code) is efficient but requires the agent to write orchestration code.
- **Data visibility vs. privacy.** Returning full tool results to the model gives maximum flexibility for reasoning but exposes potentially sensitive data (PII, credentials, internal records). Filtering in the execution environment preserves privacy but limits the model's view.

## Solution

Restructure MCP tool servers as **filesystem hierarchies of callable files** that agents discover by navigation, not by upfront definition loading. Combine with code execution to keep intermediate results in the execution environment.

The pattern has five components:

1. **Filesystem-as-registry.** Each MCP server is exposed as a directory (e.g., `./servers/google-drive/`) containing tool files (e.g., `list-files.ts`, `read-sheet.ts`). Each file is self-describing — it contains its signature, parameter schema, and description as readable metadata. Agents discover tools by listing directories and reading file headers, loading only the tools relevant to the current task.

2. **Progressive disclosure.** The agent starts with a directory listing (cheap — just filenames), reads the description of promising tools (moderate — one file header), and loads the full definition only when ready to invoke (expensive — but only for the tool actually needed). This three-tier disclosure reduces token consumption from O(all tools) to O(used tools).

3. **Code-based orchestration.** Instead of chaining individual inference-driven tool calls, the agent writes code that invokes tools programmatically with loops, conditionals, and error handling. This moves control flow from expensive inference to cheap code execution.

4. **Execution-environment filtering.** Intermediate results (e.g., 10,000 spreadsheet rows) stay in the execution environment. The agent writes filtering code to extract the relevant subset (e.g., 5 matching rows) before returning results to the model. This prevents context flooding with irrelevant data.

5. **Privacy-by-default.** Because intermediate data stays in the execution environment, sensitive information (PII, credentials) can be automatically tokenized or redacted before any data is returned to the model. Privacy preservation becomes a structural property rather than a policy overlay.

Demonstrated result: a Google Drive to Salesforce workflow reduced from 150,000 tokens to 2,000 tokens — a 98.7% reduction.

## Consequences

**Positive:**
- 98.7% token reduction demonstrated in production workflows, transforming the economics of multi-server agent systems.
- Decouples capability breadth from context budget — agents can connect to many tool servers without proportional context cost.
- Privacy preservation becomes structural (data stays in sandbox by default) rather than requiring explicit PII detection and redaction.
- Code-based orchestration eliminates inference latency for control flow (loops, conditionals, retries), reducing both cost and wall-clock time.
- Skill persistence — agents can save reusable code functions for future tasks, amortizing the discovery cost.

**Negative:**
- Requires secure sandboxing, resource limits, and monitoring infrastructure — adds operational overhead that simple tool-call patterns do not incur.
- Filesystem exploration adds latency compared to pre-loaded tools for simple, predictable workflows where the same 3-4 tools are always used.
- Code execution introduces a new failure mode: bugs in agent-generated orchestration code. Debugging generated code is harder than debugging tool-call sequences.
- Not all MCP servers can be easily restructured as filesystem hierarchies — servers with dynamic tool sets or authentication-gated discovery need adaptation.
- The agent must be capable of writing correct orchestration code, which is a higher skill bar than sequential tool calling.

## Known Uses

- **Anthropic engineering blog (production metrics).** Google Drive to Salesforce workflow: 150K to 2K tokens. Published with the filesystem-as-registry pattern and code execution integration.
- **Claude Code's Tool Search Tool.** Implements progressive disclosure for deferred tools — tool schemas are not loaded until explicitly fetched via search query, matching the on-demand discovery principle.
- **GPT-5's 54-tool search with deferred loading (related finding).** Same pattern applied independently — tools loaded on-demand via search rather than upfront context injection.
- **Dynamic tool pool assembly (related finding).** Transcript compaction selects relevant tool subsets per task rather than loading all available tools.

## Contract

### Preconditions

- Tools are structured as callable files in a navigable directory hierarchy with self-describing metadata (signature, description, parameter schema) readable without execution.
- A code execution sandbox with resource limits (CPU, memory, disk, network) and monitoring is available.
- The agent is capable of writing orchestration code (loops, conditionals, error handling) in the sandbox language.
- A fallback discovery mechanism (search index, Tool Search Tool) exists for cases where filesystem navigation is insufficient.

### Invariants

- Tool definitions are never loaded into context upfront — all discovery is on-demand via filesystem navigation or search.
- Intermediate results stay in the execution environment by default. Data is returned to the model only after programmatic filtering.
- Code execution is sandboxed with enforced resource limits. No tool execution escapes the sandbox.
- Privacy-sensitive data is tokenized or redacted in the execution environment before any return to the model.

### Governance

- Owned by Meta-System knowledge layer.
- Changes to the filesystem layout convention (directory structure, file naming, metadata format) require a Design Decision.
- Sandbox security configuration (resource limits, network access, filesystem permissions) is reviewed when new tool servers are added.
- The fallback discovery mechanism is maintained alongside the filesystem hierarchy — neither is deprecated in favor of the other.

### Recovery

- If filesystem exploration fails to locate a needed tool (missing file, corrupted metadata), fall back to the search index rather than loading all definitions.
- If agent-generated orchestration code produces an error, surface the full error message to the model for correction rather than retrying the same code.
- If sandbox resource limits are hit during tool execution, report the constraint to the model and suggest a more efficient approach rather than escalating privileges.
- If a tool server cannot be restructured as a filesystem hierarchy, maintain it as a traditional MCP server with explicit definition loading — do not force the pattern where it does not fit.
