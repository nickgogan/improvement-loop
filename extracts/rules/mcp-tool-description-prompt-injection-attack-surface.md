---
title: "MCP Tool Descriptions as Prompt-Injection Attack Surface"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "mcp-tool-description-prompt-injection-attack"
extraction_date: "2026-05-24"
last_change_session: 92
last_change_sl: "session-92-codifier-identify-extract"
identification_report: "2026-05-24-identification-report.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "Developers or teams building agent harnesses that consume MCP tool servers, particularly servers operated by third parties"
    - "Agent systems where tool discovery is automated and tool descriptions are loaded into model context without prior human inspection"
    - "Any workflow that grants agents access to write, delete, or communication tools via MCP, where a maliciously redirected agent could cause real harm"
    - "Security reviewers auditing the tool access configuration of an existing agent deployment"
  platform_coupling: "specific:MCP-protocol"
  autonomy: "all"
  stage: "secure"
  reversibility: "low — disconnecting an MCP server and removing its tools from context is immediate; recovering from an agent action already taken under injected instructions may be irreversible depending on what the tool did"
  auditability: "High when all tool calls are logged with parameters and a tool description review record exists for each connected server; low if tool loading is implicit and no call log is maintained."
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: null
contract:
  preconditions: "An agent harness is configured to use one or more MCP servers. The MCP servers are external or third-party (i.e., the operator does not fully control their content). Tool descriptions from those servers are automatically loaded into agent context. A mechanism exists to inspect tool description strings before they reach the model."
  invariants: "Every MCP server connected to the agent harness has had its tool descriptions reviewed before first use. The set of tools loaded into agent context is scoped to the current task — not the full catalog. Every MCP tool call is logged with tool name, parameters, and timestamp. Sensitive operations require explicit human approval before execution. The review record for each connected server is stored alongside the harness configuration."
  governance: "Owner: whoever maintains the agent harness configuration (the file listing which MCP servers are connected and which tools are permitted per task context). Tool description review must be performed and documented by a human before the server is activated. Changes to an MCP server's tool descriptions after initial review trigger a re-review. Approval flow configuration is human-set and cannot be modified by the agent itself."
  recovery: "If injected instructions are found in a tool description after the server was already connected: (1) disconnect the server immediately, (2) audit the call log for any tool invocations that may have been redirected by the injected instructions, (3) treat downstream outputs from affected sessions as potentially unreliable, (4) report to the MCP server operator and wait for remediation before reconnecting. If a sensitive tool was called without triggering an approval flow: audit the call, assess the impact, and harden the approval-flow configuration before the next session."
tags:
  - "extracted-artifact"
  - "rule"
  - "security"
  - "mcp"
  - "prompt-injection"
---

# MCP Tool Descriptions as Prompt-Injection Attack Surface

**Source:** [[mcp-tool-description-prompt-injection-attack]]
**Form:** rule
**Extraction date:** 2026-05-24

## Condition

An agent harness connects to one or more MCP servers. MCP tool descriptions — model-readable metadata strings attached to each tool — are loaded into agent context automatically as part of tool discovery. The agent has no mechanism to validate whether those description strings contain instructions (not just descriptions), and the model cannot reliably distinguish between legitimate tool metadata and injected directives.

## Action

**Required:** Before connecting an agent to an MCP server, audit the tool descriptions that server exposes. Verify that each description contains only factual metadata (tool name, parameter names, what the tool does) and no imperative instructions, role-assignment clauses, or directives that could alter agent behavior.

**Required:** Implement context-sensitive tool visibility: expose only the tools relevant to the current task or phase, not the full catalog of all connected MCP tools. An agent performing a read-only research task must not have write-capable tools in context.

**Required:** For sensitive MCP operations (writes, deletions, external communications), require explicit human approval before execution. The approval prompt must show the tool name, parameters, and a plain-English description of what will happen.

**Required:** Maintain an audit trail: log every MCP tool call with tool name, parameters, invocation timestamp, and which agent or session invoked it.

**Forbidden:** Loading tool descriptions from MCP servers into agent context without prior inspection of those description strings. Exposing all connected MCP tools to an agent regardless of task scope. Treating MCP server trust as binary — MCP protocol trust (the server is reachable) is not the same as content trust (the tool descriptions are safe).

## Boundary

Enforced at **MCP server onboarding** — before a new MCP server is added to the agent's configuration. Also enforced at **task initialization** — the set of tools loaded into context must be scoped to the current task, not defaulted to all available tools.

## Enforcement

- **Mechanism:** A tool description review step is required before any new MCP server is connected. For each tool, the description string is read by a human and checked for imperative language, role-assignment, or behavioral directives.
- **Check:** `(tool_descriptions_reviewed_before_server_connected == true) AND (tools_in_context_scoped_to_task == true) AND (sensitive_operations_require_approval == true) AND (all_tool_calls_logged == true)`.
- **Violation response:** If a tool description containing injected instructions is discovered: disconnect the MCP server immediately, treat any agent actions taken since that server was connected as potentially compromised, review the audit trail for unexpected tool calls, and re-evaluate whether to reconnect after the server operator addresses the description content.

## Rationale

MCP was designed for high-trust environments and does not enforce access control at the protocol level. Tool descriptions are injected into agent context by the protocol itself — the agent has no native defense against description-level injection. Invariant Labs documented "tool poisoning attacks" demonstrating that malicious instructions in tool descriptions successfully redirect agent behavior. The attack surface scales with the number of MCP servers: each additional server adds a new injection surface. Context-sensitive tool visibility reduces the attack surface per task; approval flows add a human checkpoint before harm can be done; audit trails enable post-incident forensics.

## Contract

### Preconditions
An agent harness is configured to use one or more MCP servers. Tool descriptions from those servers are automatically loaded into agent context. A mechanism exists to inspect tool description strings before they reach the model.

### Invariants
Every MCP server connected to the agent harness has had its tool descriptions reviewed before first use. The set of tools loaded into agent context is scoped to the current task. Every MCP tool call is logged. Sensitive operations require explicit human approval.

### Governance
Owner: whoever maintains the agent harness configuration. Tool description review must be performed by a human before server activation. Changes to descriptions after initial review trigger a re-review. Approval flow configuration cannot be modified by the agent itself.

### Recovery
If injected instructions are found post-connection: (1) disconnect the server, (2) audit the call log, (3) treat downstream outputs as potentially unreliable, (4) report to the server operator and wait for remediation before reconnecting.
