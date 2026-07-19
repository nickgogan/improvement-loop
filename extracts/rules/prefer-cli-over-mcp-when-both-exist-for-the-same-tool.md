---
title: "Prefer CLI Over MCP When Both Exist for the Same Tool"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "cli-first-tool-integration-less-overhead-than-mcp"
extraction_date: "2026-05-25"
last_change_session: 152
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
last_change_report: "designing-agent-tools.harvest-queue"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "any agent operating in a terminal-native environment (e.g., a coding agent) that must integrate with a tool offering both a CLI and an MCP server interface — for stateless tools; stateful local services with a session-scoped serve mode are the documented exception"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — tool-selection preference is a prompt-layer or skill-layer instruction; switching from CLI to MCP or back requires no migration work"
  auditability: "high when tool-selection decisions are logged per task; measurable via token-count comparison between CLI and MCP invocations of the same operation"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Not Yet Started"
    notes: "Playwright CLI vs. MCP head-to-head showed ~90,000 fewer tokens per interaction via CLI. Google Trends data shows CLI adoption increasing relative to MCP. No formal MetaSystem tool-selection audit conducted yet."
contract:
  preconditions: "The agent is selecting between a CLI tool and an MCP server that expose equivalent functionality for the same underlying tool. The agent is operating in a terminal-native environment where the CLI is directly accessible without additional process setup."
  invariants: "When a tool exposes both a CLI and an MCP server, the CLI is the default selection. MCP is used only when the CLI is absent or cannot accomplish the required task. The selection criterion is capability coverage, not familiarity or habit. The preference is applied at tool-selection time, before the first invocation — not retroactively after a slow or expensive run."
  governance: "Owner: the skill, CLAUDE.md rule, or agent specification that governs tool selection for the relevant workflow. The preference must be stated explicitly — do not rely on implicit model behavior. A tool-selection audit (comparing CLI vs. MCP availability for currently used MCP servers) is the enforcement mechanism. Exceptions (tool has no CLI equivalent; CLI lacks a required capability) are documented when the MCP server is retained."
  recovery: "If a CLI invocation fails or produces incorrect output → investigate whether the CLI's built-in knowledge in the model is outdated (breaking API change); if so, provide updated CLI flags via context; do not default to MCP without documenting the CLI failure reason. If the CLI cannot accomplish the required task → document the gap, use MCP for that task only, and file a finding for future CLI adoption when the CLI adds the capability."
tags:
  - "extracted-artifact"
  - "rule"
  - "tool-integration"
  - "token-economy"
  - "cli-mcp"
---

# Prefer CLI Over MCP When Both Exist for the Same Tool

**Source:** [[cli-first-tool-integration-less-overhead-than-mcp]]
**Form:** rule
**Extraction date:** 2026-05-25

## Condition

An agent is selecting between a CLI tool and an MCP server that expose equivalent functionality for the same underlying tool (e.g., Playwright CLI vs. Playwright MCP server). The agent is operating in a terminal-native environment where both interfaces are accessible.

Scope: applies when both interfaces exist and the CLI can accomplish the required task — for *stateless* tools; stateful local services with a session-scoped serve mode are the documented exception. Does not apply when the tool has no CLI equivalent, when the CLI lacks a capability required for the specific task, or when the tool holds session state worth keeping open (open DB, warm engine), where a long-lived local MCP subprocess is preferred.

## Action

**Required:** Select the CLI interface. Treat CLI as the default; treat MCP as the fallback for capability gaps only.

**Forbidden:** Selecting MCP when a CLI interface exists and can accomplish the same task. Selecting MCP as default because it was the first option tried or because it is listed first in a tool configuration. Switching to MCP retroactively after a CLI run without first investigating whether the CLI failure is fixable.

## Boundary

The preference is applied at tool-selection time — before the first invocation — not after discovering that MCP is slower or more expensive. The rule does not prohibit MCP use for tools that lack CLI equivalents; it scopes to the case where both exist.

The lazy-vs-eager mental model explains the boundary: MCP (eager loading) injects all tool schemas and configuration into context at startup, bloating context before the first task. CLI (lazy loading) loads tool information only when a relevant task requires it. The context-window cost difference is structural, not incidental.

## Enforcement

- **Mechanism:** A periodic tool-selection audit cross-references currently configured MCP servers against CLI alternatives. For each MCP server, the audit answers: does a CLI equivalent exist? If yes and the CLI is capable, the MCP server is flagged for replacement.
- **Check (deterministic):** For each active MCP server: `(cli_equivalent_exists == true) AND (cli_capability_sufficient == true) AND (mcp_retained_for_capability_gap == false)` → violation; replace with CLI.
- **Violation response:**
  - *MCP in use when CLI is available and capable:* migrate the integration to CLI; document the ~token savings as evidence.
  - *MCP retained without documented capability gap:* treat as incomplete justification; require the gap to be documented before the next audit cycle.
- **Benchmark instrument:** For any task migrated from MCP to CLI, measure and record the token count difference. This produces a per-tool evidence record and validates the selection.

## Rationale

Playwright's head-to-head benchmark is the canonical evidence: the CLI version used approximately 90,000 fewer tokens per interaction than the MCP server version, with no loss of task capability. The structural explanation is the lazy/eager loading asymmetry: MCP servers load all schemas and configuration eagerly at startup, consuming context that is not used for the current task. CLIs load only what the current command requires.

For terminal-native coding agents, the CLI preference compounds across the session: every MCP server loaded adds a fixed context overhead that persists for the session's duration. Multiple MCP servers can collectively consume a significant fraction of the context window before any task-relevant content is loaded. Switching to CLI for tools that have CLI equivalents recovers that context for task content.

The Google Trends signal — CLI adoption increasing relative to MCP — suggests that practitioners are discovering this asymmetry independently. The rule codifies what production experience is demonstrating.

## Special Case: Stateful Local Services (the statefulness discriminator)

The CLI-first default is scoped to *stateless* tools — where each invocation shares the terminal environment natively and amortizes nothing across calls, so the CLI's zero protocol overhead wins (Playwright is the canonical case). When the tool holds session state worth keeping open — an open database, a warm index, a long-lived engine — the winner flips: a long-lived local stdio MCP subprocess (spawned once, tokenless, session-scoped, dying with the session) beats per-call CLI shell-out, because it amortizes process startup + connection open/close + typed tool schemas across the whole session and removes one shell-approval surface per command.

Discriminator checklist for a tool-integration review: does the tool open a connection/database/index per call? Is there a session-scoped `serve` mode? If yes, prefer the local MCP subprocess for that tool; the CLI-first default does not apply.

Two documented costs to watch: a long-lived subprocess can hold stale state after the underlying store changes externally — it needs reload semantics — and session-scoped servers can register tool-count bloat that taxes the context window.

**Source:** [[stateful-mcp-subprocess-vs-cli-shell-out]] (Medium / practitioner-documented — Gbrain's ~47 engine operations exposed both ways; CLI shell-out "works, but is worse as a process," the local MCP path visibly faster in Hermes Agent). Merged here via DD-97 extension (session 152, Nick-delegated extend-existing ruling) rather than drafted as a standalone rule.

## Failure Modes

- **CLI built-in knowledge is outdated.** The model's internal knowledge of a CLI tool's flags and syntax does not reflect the current version. The CLI invocation uses deprecated flags and fails or produces wrong output. Mitigation: when a CLI invocation fails, check whether the failure matches an API change; provide updated syntax via context rather than falling back to MCP.
- **Tool has no adequate CLI.** The tool is GUI-native or the CLI wraps only a subset of its functionality. The CLI preference leads to selecting an inferior interface for the task. Mitigation: the capability-sufficiency check gates the preference; MCP is retained for tools where the CLI is inadequate.
- **Audit not performed.** MCP servers accumulate without review because no tool-selection audit is scheduled. The token overhead compounds across servers without a forcing function. Mitigation: schedule the audit at system setup and at each new MCP server addition.
- **False equivalence.** The CLI and MCP server do not expose identical functionality; a task requires a capability present only in the MCP server. The CLI preference causes task failure. Mitigation: the capability-sufficiency check is required before selecting CLI; exceptions are documented.

## Contract

### Preconditions
The agent is selecting between a CLI tool and an MCP server that expose equivalent functionality for the same underlying tool. The agent is operating in a terminal-native environment where the CLI is directly accessible without additional process setup.

### Invariants
When a tool exposes both a CLI and an MCP server, the CLI is the default selection. MCP is used only when the CLI is absent or cannot accomplish the required task. The selection criterion is capability coverage, not familiarity or habit. The preference is applied at tool-selection time, before the first invocation — not retroactively after a slow or expensive run.

### Governance
Owner: the skill, CLAUDE.md rule, or agent specification that governs tool selection for the relevant workflow. The preference must be stated explicitly — do not rely on implicit model behavior. A tool-selection audit (comparing CLI vs. MCP availability for currently used MCP servers) is the enforcement mechanism. Exceptions (tool has no CLI equivalent; CLI lacks a required capability) are documented when the MCP server is retained.

### Recovery
If a CLI invocation fails or produces incorrect output → investigate whether the CLI's built-in knowledge in the model is outdated (breaking API change); if so, provide updated CLI flags via context; do not default to MCP without documenting the CLI failure reason. If the CLI cannot accomplish the required task → document the gap, use MCP for that task only, and file a finding for future CLI adoption when the CLI adds the capability.
