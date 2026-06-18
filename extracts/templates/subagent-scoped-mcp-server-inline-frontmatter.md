---
title: "Subagent-Scoped MCP Server Inline Frontmatter Definition"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "inline-scoped-mcp-servers-per-subagent"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "Claude Code subagent definitions that require MCP tools not needed by the parent session"
  platform_coupling: "specific:claude-code"
  autonomy: "all"
  stage: "build"
  reversibility: "trivial — moving a server from inline subagent frontmatter to .mcp.json (or back) is a config file edit with no code changes"
  auditability: "medium — inline MCP scope is visible in the subagent frontmatter file; not visible in the session-wide .mcp.json; requires per-agent inspection for full tool-surface inventory"
  evidence_strength: "Strong (documented, first-party Anthropic canonical spec)"
  adoption:
    status: "Not Yet Started"
    notes: "Documented in Anthropic's Claude Code subagents docs (2026). MetaSystem loads multiple MCP servers session-wide; no subagent-scoped MCP in use at time of extraction."
contract:
  preconditions: "The task requires a subagent with MCP tools that are not needed by the parent session. Claude Code subagent frontmatter syntax is available. The MCP server can be started via stdio command or is already registered session-wide."
  invariants: "Inline MCP servers are defined in the subagent's frontmatter, not in .mcp.json. Reference-mode entries (string names) reuse parent session connections. The parent session's context never receives the inline server's tool descriptions."
  governance: "Subagent files with inline MCP definitions are stored in the agents/ directory alongside other subagent definitions. The tool-surface for any given subagent is fully described by its frontmatter — no hidden session-wide dependencies. When a subagent is deprecated, its inline MCP config is removed with it."
  recovery: "If an inline MCP server fails to connect at subagent startup → subagent surfaces the error; parent session does not inherit the failure. If the same MCP server is needed across many subagents with identical config → promote to .mcp.json reference and switch subagents to reference-mode. If permission model blocks an inline server → the subagent's permission mode still applies; resolve at the permission layer, not by widening session-wide permissions."
tags:
  - "extracted-artifact"
  - "template"
  - "mcp"
  - "subagent"
  - "context-engineering"
  - "claude-code"
---

# Subagent-Scoped MCP Server Inline Frontmatter Definition

**Source:** [[inline-scoped-mcp-servers-per-subagent]]
**Form:** template
**Extraction date:** 2026-05-25

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{SUBAGENT_NAME}}` | Name of the subagent | `browser-tester` |
| `{{SUBAGENT_DESCRIPTION}}` | One-line description of what the subagent does | `Tests features in a real browser using Playwright` |
| `{{SERVER_NAME}}` | Identifier for the inline MCP server | `playwright` |
| `{{COMMAND}}` | Executable to launch the MCP server | `npx` |
| `{{ARGS}}` | Arguments passed to the command | `["-y", "@playwright/mcp@latest"]` |
| `{{ENV}}` | Environment variables for the server process | `{API_KEY: "..."}` or omit if none |
| `{{SESSION_REF_NAME}}` | Name of a session-wide server to reuse by reference | `github` |
| `{{SUBAGENT_PROMPT}}` | The subagent's system prompt or task instructions | see body below |

---

## Body

### Subagent Frontmatter with Inline MCP Server

```yaml
---
name: {{SUBAGENT_NAME}}
description: {{SUBAGENT_DESCRIPTION}}
mcpServers:
  # Inline definition: server connects when this subagent starts,
  # disconnects when it finishes. Tool descriptions never enter the parent context.
  - {{SERVER_NAME}}:
      type: stdio
      command: {{COMMAND}}
      args: {{ARGS}}
      # env:
      #   {{ENV_KEY}}: "{{ENV_VALUE}}"

  # Reference entry: reuses a server already configured in the session's .mcp.json.
  # No new process is started; parent's existing connection is shared.
  - {{SESSION_REF_NAME}}
---
```

### System Prompt (below frontmatter divider)

```markdown
---

{{SUBAGENT_PROMPT}}
```

---

### Lifecycle Behavior

| Event | What happens |
|-------|-------------|
| Parent invokes subagent | Inline server process starts; tools register in subagent context |
| Subagent executes | All `{{SERVER_NAME}}` tools available; parent context unaffected |
| Subagent completes | Server process terminates; tools unregistered |
| Parent continues | No `{{SERVER_NAME}}` tool descriptions in parent's context |

---

### Reference vs. Inline Decision Matrix

| Condition | Use |
|-----------|-----|
| MCP server needed only by this subagent | **Inline** |
| MCP server needed by parent AND subagent | **Reference** (session-wide .mcp.json + reference entry) |
| MCP server needed by multiple subagents with identical config | Promote to **session-wide** + use reference entries |
| MCP server has destructive tools that should not be in parent context | **Inline** (safety isolation) |
| MCP server has 10+ tool descriptions (high token cost) | **Inline** (context economics) |

---

## Usage

1. Create a new subagent file (e.g., `agents/{{SUBAGENT_NAME}}.md`).
2. Fill in the frontmatter variables above.
3. Write the subagent's system prompt below the second `---` divider.
4. Remove the `env:` block if no environment variables are needed.
5. Remove the reference entry if the subagent does not need any session-wide servers.
6. Invoke the subagent from the parent session — the MCP server will be lifecycle-scoped automatically.
7. Validate: inspect parent context after subagent completes; confirm `{{SERVER_NAME}}` tools are absent.

---

## Variation Axis

| Axis | Option A | Option B |
|------|----------|----------|
| **Server type** | `stdio` (subprocess, most common) | `sse` (HTTP server-sent events) |
| **Multiple inline servers** | One server per subagent | Multiple inline servers in one subagent (browser + database) |
| **Config source** | Hardcoded in frontmatter | Environment variable substitution in frontmatter values |
| **Reuse pattern** | Reference by name | Full inline definition (allows per-subagent config overrides) |
| **Safety scope** | Default permission mode | Explicit `permissionMode: restricted` added to frontmatter |

---

## Contract

### Preconditions
The task requires a subagent with MCP tools that are not needed by the parent session. Claude Code subagent frontmatter syntax is available. The MCP server can be started via stdio command or is already registered session-wide.

### Invariants
Inline MCP servers are defined in the subagent's frontmatter, not in .mcp.json. Reference-mode entries (string names) reuse parent session connections. The parent session's context never receives the inline server's tool descriptions.

### Governance
Subagent files with inline MCP definitions are stored in the agents/ directory alongside other subagent definitions. The tool-surface for any given subagent is fully described by its frontmatter — no hidden session-wide dependencies. When a subagent is deprecated, its inline MCP config is removed with it.

### Recovery
If an inline MCP server fails to connect at subagent startup → subagent surfaces the error; parent session does not inherit the failure. If the same MCP server is needed across many subagents with identical config → promote to .mcp.json reference and switch subagents to reference-mode. If permission model blocks an inline server → the subagent's permission mode still applies; resolve at the permission layer, not by widening session-wide permissions.
