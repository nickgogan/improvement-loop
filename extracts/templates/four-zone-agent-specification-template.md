---
title: "Four-Zone Agent Specification Template"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "four-zone-agent-architecture-framework"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent designers specifying a new agent from first principles"
    - "builders debugging an existing agent by systematically isolating which zone is broken"
    - "any workflow that requires a reproducible, platform-agnostic agent specification"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "trivial — a specification document; revising or discarding it has no migration cost"
  auditability: "high — the four-zone structure is self-documenting; all design choices are recorded in named fields; changes are diffable"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Not Yet Started"
    notes: "Four-zone framework documented by Roman (production course). Widely transferable across agent platforms. No MetaSystem agents currently use this formal template, though the four zones are implicitly present in existing agent definitions."
contract:
  preconditions: "A new agent is being designed, or an existing agent is being rebuilt or debugged. The designer knows the agent's purpose and at minimum has a hypothesis about what its trigger condition and primary tool set should be."
  invariants: "All four zones are specified before implementation begins. Zone 1 (Trigger) names at least one concrete event. Zone 2 (Context) enumerates all injected inputs (system prompt, files, history). Zone 3 (Tools) lists every tool the agent can call, with its binding type. Zone 4 (Output/Memory) specifies at least one persistence location. The debugging checklist is filled in if the template is being used for a broken agent."
  governance: "Owner: the agent designer or architect. The specification exists as a persistent artifact in the agent's directory. Any change to a zone after deployment is a design change — update the specification and log the change. Consumer agents (builders, reviewers) validate that the implemented agent matches its zone specification. This template is the canonical input for agent rebuild-from-spec workflows."
  recovery: "If a zone is left blank at implementation time → halt; a blank zone means an undecided design choice that will become a runtime bug. If the implemented agent diverges from the specification → treat the specification as authoritative; update the implementation or file a design amendment. If debugging reveals a zone failure → complete the zone debugging checklist for that zone before attempting a fix."
tags:
  - "extracted-artifact"
  - "template"
  - "agent-design"
  - "orchestration"
  - "architecture"
---

# Four-Zone Agent Specification Template

**Source:** [[four-zone-agent-architecture-framework]]
**Form:** template
**Extraction date:** 2026-05-25

A reusable specification scaffold for defining any agent using the four-zone decomposition: Trigger, Context, Tools, and Output/Memory. Complete one specification per agent before implementation begins. The template also serves as a debugging checklist when an existing agent is broken.

## Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `{{AGENT_NAME}}` | Identifier for this agent | Yes |
| `{{AGENT_PURPOSE}}` | One-sentence description of what this agent accomplishes | Yes |
| `{{TRIGGER_TYPE}}` | Category: `scheduled`, `event-driven`, `manual`, `api-call`, `message-receive`, `heartbeat` | Yes |
| `{{TRIGGER_SPEC}}` | Concrete trigger definition (e.g., cron expression, event type, API endpoint) | Yes |
| `{{TRIGGER_PRECONDITIONS}}` | Conditions that must be true before the trigger fires a run | No |
| `{{SYSTEM_PROMPT_REF}}` | Path or inline reference to the agent's system prompt | Yes |
| `{{CONTEXT_FILES}}` | Files or documents injected per turn (paths or patterns) | No |
| `{{CONTEXT_HISTORY_SCOPE}}` | How much conversation history is included: `none`, `last-N-turns`, `full-session`, `summary` | Yes |
| `{{CONTEXT_DYNAMIC_INPUTS}}` | Runtime-injected values (e.g., task description, retrieved documents, calling agent output) | No |
| `{{TOOL_N_NAME}}` | Name of tool N | Yes (≥1) |
| `{{TOOL_N_TYPE}}` | One of: `builtin`, `mcp-server`, `api-call`, `bash`, `agent-tool` | Yes |
| `{{TOOL_N_BINDING}}` | How the tool is activated (token sequence, function call, hook) | No |
| `{{TOOL_N_PERMISSIONS}}` | Permission scope required (read-only, write, network, system) | Yes |
| `{{OUTPUT_TYPE_N}}` | Category of output: `file`, `database-row`, `api-response`, `message`, `artifact` | Yes (≥1) |
| `{{OUTPUT_LOCATION_N}}` | Where output is written (path, endpoint, table) | Yes |
| `{{MEMORY_SCOPE}}` | What persists between turns: `none`, `session-state`, `files-on-disk`, `external-store` | Yes |
| `{{MEMORY_SPEC}}` | Concrete persistence mechanism (e.g., file path pattern, database table, session variable) | Conditional |
| `{{STATE_LOSS_RISK}}` | Known risk if Zone 4 fails or is misconfigured | Yes |

## Body

```markdown
# Agent Specification: {{AGENT_NAME}}

**Purpose:** {{AGENT_PURPOSE}}

---

## Zone 1 — Trigger

*What wakes this agent? Without a trigger, the agent never runs.*

| Field | Value |
|-------|-------|
| Trigger type | {{TRIGGER_TYPE}} |
| Trigger specification | {{TRIGGER_SPEC}} |
| Preconditions | {{TRIGGER_PRECONDITIONS}} |

**Debugging Zone 1:**
- [ ] Is the trigger source active and reachable?
- [ ] Are preconditions being evaluated correctly?
- [ ] Is the agent's process running and listening for the trigger?

---

## Zone 2 — Context

*Everything injected into the model's context window on each turn.*

| Input | Value / Reference |
|-------|------------------|
| System prompt | {{SYSTEM_PROMPT_REF}} |
| Injected files | {{CONTEXT_FILES}} |
| Conversation history scope | {{CONTEXT_HISTORY_SCOPE}} |
| Dynamic runtime inputs | {{CONTEXT_DYNAMIC_INPUTS}} |

**Context volume estimate:** _fill in approximate token budget_

**Debugging Zone 2:**
- [ ] Is the system prompt being loaded correctly (right path, right version)?
- [ ] Are injected files accessible and within expected size?
- [ ] Is conversation history being truncated or trimmed as expected?
- [ ] Are dynamic inputs arriving with the correct values?

---

## Zone 3 — Tools

*Capabilities that let the agent read, write, or interact with external systems.*

| Tool Name | Type | Binding | Permissions |
|-----------|------|---------|-------------|
| {{TOOL_1_NAME}} | {{TOOL_1_TYPE}} | {{TOOL_1_BINDING}} | {{TOOL_1_PERMISSIONS}} |
| {{TOOL_2_NAME}} | {{TOOL_2_TYPE}} | {{TOOL_2_BINDING}} | {{TOOL_2_PERMISSIONS}} |

*Add rows for all tools.*

**Debugging Zone 3:**
- [ ] Are all tools listed in the tool registry and reachable?
- [ ] Are permission scopes granted in the runtime environment?
- [ ] Do pre-tool and post-tool hooks fire correctly for each tool?
- [ ] Is there a tool the agent is trying to use that is not in this list?

---

## Zone 4 — Output / Memory

*Where work persists between turns. The model has no persistent memory by default — all statefulness must be explicitly designed here.*

| Output type | Location | Format |
|-------------|----------|--------|
| {{OUTPUT_TYPE_1}} | {{OUTPUT_LOCATION_1}} | — |
| {{OUTPUT_TYPE_2}} | {{OUTPUT_LOCATION_2}} | — |

**Memory scope:** {{MEMORY_SCOPE}}
**Memory specification:** {{MEMORY_SPEC}}
**State loss risk:** {{STATE_LOSS_RISK}}

**Debugging Zone 4:**
- [ ] Is output being written to the correct location with the correct format?
- [ ] Is state from the previous turn being loaded correctly at the start of each turn?
- [ ] If output is missing, does the agent have write permission to the target location?
- [ ] Is state loss from a crash recoverable? What is the recovery path?

---

## Specification Sign-off

| Field | Value |
|-------|-------|
| Author | — |
| Date | YYYY-MM-DD |
| Status | draft / reviewed / approved |
| Reviewed by | — |
```

## Usage

1. Fill in one specification per agent before any implementation begins.
2. All four zones must be complete. A blank zone is a design decision deferred to runtime — which means it will become a bug.
3. For debugging an existing agent: identify which zone the failure is most likely in, then step through that zone's debugging checklist.
4. For rebuilding an agent from scratch: the completed specification is the input — no additional context should be needed to rebuild from this document alone.

## Variation Axis

| Variation | Adaptation |
|-----------|-----------|
| Minimal single-tool agent | Zone 3 has one row; Zone 4 may be `memory-scope: none` if the agent produces only transient output |
| Sub-agent (spawned by orchestrator) | Zone 1 trigger type is `agent-tool`; add a `Spawning agent` row to Zone 2 dynamic inputs |
| Stateful multi-turn agent | Zone 4 memory scope is `files-on-disk` or `external-store`; state loss risk must be explicitly assessed |
| Parallel execution | Add a `Concurrency` section to Zone 1; note whether multiple instances share Zone 4 storage |
| Debugging mode | Prioritize Zone 2 and Zone 4 checklists — these are the two highest-failure zones per the source finding |

## Contract

### Preconditions
A new agent is being designed, or an existing agent is being rebuilt or debugged. The designer knows the agent's purpose and at minimum has a hypothesis about what its trigger condition and primary tool set should be.

### Invariants
All four zones are specified before implementation begins. Zone 1 (Trigger) names at least one concrete event. Zone 2 (Context) enumerates all injected inputs (system prompt, files, history). Zone 3 (Tools) lists every tool the agent can call, with its binding type. Zone 4 (Output/Memory) specifies at least one persistence location. The debugging checklist is filled in if the template is being used for a broken agent.

### Governance
Owner: the agent designer or architect. The specification exists as a persistent artifact in the agent's directory. Any change to a zone after deployment is a design change — update the specification and log the change. Consumer agents (builders, reviewers) validate that the implemented agent matches its zone specification. This template is the canonical input for agent rebuild-from-spec workflows.

### Recovery
If a zone is left blank at implementation time → halt; a blank zone means an undecided design choice that will become a runtime bug. If the implemented agent diverges from the specification → treat the specification as authoritative; update the implementation or file a design amendment. If debugging reveals a zone failure → complete the zone debugging checklist for that zone before attempting a fix.
