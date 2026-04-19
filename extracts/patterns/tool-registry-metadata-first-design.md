---
title: "Tool Registry with Metadata-First Design"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "tool-registry-metadata-first-design"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Agent system has multiple tools or capabilities that need to be discoverable. Tool implementations exist or are planned. A schema for tool metadata (name, source, responsibility, parameters) is defined before any implementations are registered."
  invariants: "Every tool has a registry entry before it has an implementation. The registry is the single source of truth for what tools exist and what they do -- tool discovery never bypasses the registry. Registry metadata and tool implementations are kept in sync through a defined update process. list_tools() returns metadata without executing any tool."
  governance: "Owned by Meta-System knowledge layer. Registry schema changes require a Design Decision. New tool registrations are reviewed for naming consistency, responsibility overlap, and permission classification. Modifications to registry entries require updating both metadata and implementation."
  recovery: "If registry and implementation drift out of sync, run a reconciliation check that flags mismatches (registry entries without implementations, implementations without registry entries). If the registry grows too large for context windows, implement category-based filtering so agents query subsets rather than the full registry. If a tool's metadata misrepresents its behavior, freeze the tool until metadata is corrected and verified."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Tool Registry with Metadata-First Design

**Source:** [[tool-registry-metadata-first-design]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent systems accumulate tools over time -- file operations, search, API integrations, domain-specific actions -- but lack a unified way to discover, filter, and reason about available capabilities without executing them. Tools are defined inline in system prompts, hardcoded in configuration, or discovered ad hoc through trial and error. This makes it impossible for agents to answer "what can I do?" without loading every tool's implementation, wastes context window space on irrelevant tool descriptions, and prevents systematic permission management.

## Forces

- **Discoverability vs. overhead.** Agents need to know what tools exist, but loading full tool definitions (with parameter schemas, examples, and implementation details) for every tool in every session wastes context.
- **Metadata accuracy vs. maintenance burden.** Rich metadata (descriptions, categories, permissions, version info) enables smart tool selection, but keeping metadata synchronized with implementations requires ongoing discipline.
- **Single registry vs. multiple consumers.** User-facing commands and model-facing tools serve different consumers with different needs, but maintaining two separate inventories risks drift. A unified registry with consumer-specific views resolves this.
- **Static definition vs. runtime flexibility.** Hardcoded tool lists are easy to reason about but cannot adapt to context. Dynamic registries support runtime filtering but add complexity.

## Solution

Define all agent tool capabilities as a **data-structure registry** where metadata is the primary artifact and implementations load on demand.

The pattern has four components:

1. **Metadata-first entries.** Each tool is defined as a data record before any implementation exists: name, source hint (where it comes from), responsibility description (what it does, in one sentence), category, permission tier, and parameter schema. The metadata entry is the tool's identity -- it exists in the registry whether or not the implementation is loaded.

2. **Lazy loading.** Implementations are not loaded into memory or context until a tool is actually invoked. The registry serves metadata for discovery and filtering; the runtime loads the implementation only when needed. This keeps context overhead proportional to tools used, not tools available.

3. **Parallel registries for different consumers.** Maintain separate views for different audiences: a command registry for user-facing commands (human-readable names, help text, keyboard shortcuts) and a tool registry for model-facing tools (parameter schemas, semantic descriptions, usage examples). Both views derive from the same underlying data, preventing drift.

4. **Runtime filtering via `list_tools()`.** A queryable interface that returns tool metadata filtered by category, permission tier, capability type, or other dimensions. Agents call `list_tools()` to reason about available capabilities without executing anything. The filter set can change per session, project, or permission level.

For MetaSystem specifically: the existing skills system (discovered via Glob/Grep and CLAUDE.md tables) serves a similar purpose but lacks the metadata-first registry structure. Skills are discovered through filesystem conventions rather than a queryable registry, and there is no lazy-loading separation between skill metadata and skill implementation.

## Consequences

**Positive:**
- Agents can reason about available capabilities without loading or executing any tool, reducing context overhead.
- Runtime filtering enables dynamic tool pool assembly -- different sessions or contexts load different tool subsets.
- Permission management operates at the metadata level (tool tiers, categories) rather than requiring per-invocation checks.
- Foundation for other patterns: tiered permissions, tool gateway security, and orchestrator delegation all build on a queryable registry.
- Proven at scale: Claude Code maintains 207 user-facing commands and 184 model-facing tools through this architecture.

**Negative:**
- Registry/implementation drift is the primary risk -- if metadata says a tool does X but the implementation does Y, the agent makes wrong decisions about which tool to use.
- Over-indexing on metadata without testing actual tool behavior creates a false sense of capability documentation.
- Registry maintenance burden grows linearly with tool count. At scale, automated consistency checks become necessary.
- The lazy-loading boundary adds architectural complexity compared to simply loading all tools eagerly.

## Known Uses

- **Anthropic Claude Code.** Production system maintaining two parallel registries: 207 user-facing commands and 184 model-facing tools. Identified as a "Tier 1 day-one non-negotiable" primitive by Nate B Jones.
- **MCP Server Cards.** The Model Context Protocol's server discovery mechanism uses a similar metadata-first approach -- server capabilities are described in metadata before any tool is invoked.
- **MetaSystem skills table.** The CLAUDE.md skill tables and SKILL.md files are an informal metadata-first pattern -- they describe what each skill does before the skill is loaded. However, they lack queryable filtering and lazy loading.

## Contract

### Preconditions

- Agent system has multiple tools or capabilities that need to be discoverable.
- Tool implementations exist or are planned.
- A schema for tool metadata (name, source, responsibility, parameters, permission tier) is defined before any implementations are registered.

### Invariants

- Every tool has a registry entry before it has an implementation -- metadata-first, not implementation-first.
- The registry is the single source of truth for what tools exist and what they do -- tool discovery never bypasses the registry.
- Registry metadata and tool implementations are kept in sync through a defined update process.
- `list_tools()` returns metadata without executing any tool or loading any implementation.

### Governance

- Owned by Meta-System knowledge layer.
- Registry schema changes require a Design Decision.
- New tool registrations are reviewed for naming consistency, responsibility overlap with existing tools, and correct permission classification.
- Modifications to existing registry entries require updating both metadata and implementation.

### Recovery

- If registry and implementation drift out of sync, run a reconciliation check that flags mismatches: registry entries without implementations (stale metadata), and implementations without registry entries (unregistered tools).
- If the registry grows too large for context windows, implement category-based filtering so agents query subsets rather than the full registry.
- If a tool's metadata misrepresents its actual behavior, freeze the tool (remove from `list_tools()` results) until metadata is corrected and verified against the implementation.
- If lazy loading fails for a registered tool, surface the error with the registry entry's metadata so the agent can select an alternative rather than failing silently.
