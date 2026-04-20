---
name: MCP as Code API -- Progressive Tool Discovery via Filesystem
summary: Reimagining MCP servers as code APIs rather than direct tool calls. Agents discover tools by navigating filesystem hierarchies (progressive disclosure) and execute them programmatically. 98.7%
  token reduction demonstrated (150K to 2K tokens). Intermediate results stay in execution environment, enabling privacy preservation via automatic PII tokenization.
implementation_notes: null
category: Tool Integration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- anthropic-code-execution-with-mcp.md
- tastematter-concept-graph-mcp-ai-signal.md
related_findings:
- file: dynamic-tool-pool-assembly-transcript-compaction.md
  rel: extends
- file: gpt-54-tool-search-deferred-tool-loading.md
  rel: same-problem
- file: cli-first-tool-integration-less-overhead-than-mcp.md
  rel: same-problem
- file: programmatic-tool-calling-code-orchestrated-tool-use.md
  rel: enabled-by
- file: mcp-ecosystem-critical-mass-97m-installs.md
  rel: extends
- file: non-deterministic-tool-contract-model.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-20'
pipeline_status: synthesized
consumed_by:
- designing-agent-tools.md
---

## What It Is
A pattern where MCP servers are exposed as callable files in a filesystem hierarchy rather than as upfront tool definitions. Each tool becomes a TypeScript file that agents discover by exploring directories (e.g., `./servers/google-drive/`). Agents read only the specific tool files needed for the current task. Combined with code execution, this achieves:

1. **Progressive disclosure**: Models navigate filesystems to load tool definitions on-demand rather than stuffing all definitions into context upfront
2. **Context-efficient results**: Agents filter and transform data in the execution environment before returning it to the model (e.g., filtering 10,000 spreadsheet rows to 5 relevant ones)
3. **Code-based control flow**: Loops, conditionals, and error handling execute in code rather than chaining individual inference-driven tool calls
4. **Privacy preservation**: Intermediate results stay in the execution environment by default; sensitive data can be tokenized automatically so PII never reaches the model
5. **State persistence and skills**: Agents save intermediate results to files and persist reusable code functions as skills for future tasks

Demonstrated on a Google Drive to Salesforce workflow: reduced from 150,000 tokens to 2,000 tokens (98.7% savings).

## Why It Matters
The core problem with MCP at scale is token inefficiency -- tool definitions alone consumed up to 134K tokens in Anthropic's experience, with 50,000+ tokens used before a single request in some MCP code execution setups. This pattern resolves the fundamental tension between MCP's rich tool ecosystem and context window constraints. It also addresses the CLI-vs-MCP debate by making MCP tools behave more like CLI tools (lazy-loaded, programmatically invoked).

## Why People Are Using It
Anthropic engineering blog with production metrics. The 98.7% token reduction is transformative for agents connected to multiple MCP servers. The privacy preservation angle (PII tokenization in execution environment) addresses enterprise compliance requirements that block agent adoption.

## Potential Improvements
Standardized filesystem layout for MCP-as-code-API servers. Caching of frequently-used tool definitions. Skill persistence across sessions for common workflows. Integration with Tool Search Tool for hybrid discovery (search when filesystem exploration is too slow).

## Potential Failure Modes
Requires secure sandboxing, resource limits, and monitoring infrastructure -- adds operational overhead. Filesystem exploration adds latency vs. pre-loaded tools for simple, predictable workflows. Code execution introduces a new failure mode (bugs in generated orchestration code). Not all MCP servers may be easily restructured as filesystem hierarchies.

## Corroborating Evidence — 2026-04-20
TasteMatter MCP server applies the code-mode variant of this pattern to a knowledge graph: the MCP server exposes two tools (search + execute), the agent writes SQL-like code against the graph schema rather than enumerating query parameters, and intermediate graph data stays in the execution environment. The builder attributes the pattern to Cloudflare and reports ~90% content consumption reduction. This confirms the pattern generalizes beyond filesystem/tool-discovery contexts to any structured data store accessible via MCP.

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[progressive-tool-discovery-via-filesystem.md]] in `extracts/patterns/`
