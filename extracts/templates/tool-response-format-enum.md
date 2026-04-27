---
title: "Tool Response-Format Enum (detailed / concise)"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "response-format-enum-for-adaptive-verbosity"
identification_report: "managing-agent-context.harvest-queue.md::response-format-enum-for-adaptive-verbosity::template::tool-response-format-enum"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
version: 1
deployed: false
deployed_to: null
context:
  applies_to:
    - "MCP tools that return variable-length results (document fetchers, search tools, list operations)"
    - "agent-facing tool surfaces where a single tool call may serve scan-mode and chain-mode use cases"
    - "tool definitions in agentic systems where context budget is a first-order constraint"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "low — once tools ship with the parameter, callers depend on the enum values; renaming or removing modes requires coordinated migration of every call site"
  auditability: "high — tool invocations carry the response_format value as a structured argument; per-mode token consumption can be measured directly from invocation logs"
  evidence_strength: "Strong"
  adoption:
    status: "Not Yet Started"
    notes: "Production-tested at Anthropic with measured ~65% token reduction (206 → 72 tokens) when concise mode is selected appropriately. No adoption within this system at time of extraction."
contract:
  preconditions: "Tool returns variable-length output where a high-signal subset is meaningfully smaller than the full payload. The agent is the caller (not a fixed downstream consumer that always needs full data). Tool description can document when each mode is appropriate."
  invariants: "response_format is a closed enum (not free-form). Default mode is documented and chosen for the dominant call pattern. Detailed mode preserves all fields needed for chaining (IDs, references, full metadata). Concise mode strips chaining-required fields only when scan/triage is the named use case."
  governance: "Owner: tool author. Adding new enum values requires updating the tool description and verifying agent-side selection heuristics still hold. Removing or renaming a value is a breaking change."
  recovery: "Agent selects concise but downstream chaining fails on missing IDs: agent retries with detailed; tool description is updated to clarify when concise is unsafe. Token measurements drift from documented values: re-measure and update tool description."
tags:
  - "extracted-artifact"
  - "template"
  - "tool-design"
  - "context-engineering"
---

# Tool Response-Format Enum (detailed / concise)

**Source:** [[response-format-enum-for-adaptive-verbosity]]
**Form:** template
**Extraction date:** 2026-04-27

A tool-design recipe that adds a `response_format` enum parameter to tools returning variable-length output. The agent picks the verbosity mode based on whether it is scanning (concise) or chaining (detailed). Production-tested with ~65% token reduction in the concise path.

## Variables

| Variable | Type | Required | Description |
|----------|------|----------|-------------|
| `{{TOOL_NAME}}` | string | Yes | Snake_case tool identifier (e.g., `fetch_document`, `search_kb`). |
| `{{TOOL_PURPOSE}}` | string | Yes | One-sentence description of what the tool returns. |
| `{{DEFAULT_MODE}}` | enum | Yes | Default value of `response_format` — `"detailed"` or `"concise"`. Pick based on dominant call pattern. |
| `{{DETAILED_FIELDS}}` | YAML / JSON schema fragment | Yes | Fields included in detailed mode. Must include all chaining-required fields (IDs, references, full metadata). |
| `{{CONCISE_FIELDS}}` | YAML / JSON schema fragment | Yes | Fields included in concise mode. Strip everything not needed for scan/triage. |
| `{{DETAILED_TOKEN_BUDGET}}` | integer | No | Approximate token count of a typical detailed response (for tool description). |
| `{{CONCISE_TOKEN_BUDGET}}` | integer | No | Approximate token count of a typical concise response (for tool description). |
| `{{DETAILED_USE_CASES}}` | bullet list | Yes | When the agent should select detailed (e.g., "chaining to another tool that consumes IDs", "presenting full content to user"). |
| `{{CONCISE_USE_CASES}}` | bullet list | Yes | When the agent should select concise (e.g., "scanning for relevance", "summarizing many results", "triage decisions"). |

## Body

### JSON Schema fragment for tool definition

```json
{
  "name": "{{TOOL_NAME}}",
  "description": "{{TOOL_PURPOSE}}\n\nresponse_format selects output verbosity:\n- \"detailed\" (~{{DETAILED_TOKEN_BUDGET}} tokens): full metadata and IDs. Use when: {{DETAILED_USE_CASES}}.\n- \"concise\" (~{{CONCISE_TOKEN_BUDGET}} tokens): high-signal summary only. Use when: {{CONCISE_USE_CASES}}.\nDefault: {{DEFAULT_MODE}}.",
  "input_schema": {
    "type": "object",
    "properties": {
      "response_format": {
        "type": "string",
        "enum": ["detailed", "concise"],
        "default": "{{DEFAULT_MODE}}",
        "description": "Output verbosity. Pick concise for scan/triage, detailed for chaining or full-content delivery."
      }
    }
  }
}
```

### Tool implementation skeleton (pseudocode)

```python
def {{TOOL_NAME}}(args):
    raw = fetch_underlying_data(args)
    mode = args.get("response_format", "{{DEFAULT_MODE}}")

    if mode == "detailed":
        return {
            # {{DETAILED_FIELDS}} — preserve all chaining-required fields
        }
    elif mode == "concise":
        return {
            # {{CONCISE_FIELDS}} — strip to high-signal summary
        }
    else:
        raise ValueError(f"unknown response_format: {mode}")
```

### Agent-side selection heuristic (for tool description or system prompt)

> When calling `{{TOOL_NAME}}`, choose `response_format` as follows:
> - `"detailed"` if you will pass IDs/references from the response into another tool call, or if you need to deliver the full content to the user.
> - `"concise"` if you are scanning multiple results, deciding which to investigate further, or producing a summary.
> - When uncertain and context budget is tight: start with `"concise"`, escalate to `"detailed"` only if the concise response is insufficient.

## Usage

Render this template when authoring or revising a tool whose output is variable-length and where a high-signal subset is meaningfully smaller than the full payload. Common candidates:
- Document/page fetchers
- Search and listing tools
- Database query wrappers
- File readers (return summary vs. full content)

Use this template when:
- The same tool serves both scan-mode and chain-mode use cases
- Token reduction in the dominant call pattern is worth the small ergonomic cost of an extra parameter
- The tool's caller is an agent that can read tool descriptions and make selection decisions

Do not use when:
- The tool's output is fixed-size and small (parameter is overhead with no benefit)
- The tool is consumed by a fixed pipeline that always needs full data (no agent selection happening)
- All callers always need detailed output (the enum becomes dead weight)

## Variation Axis

1. **Number of modes** — Two modes (detailed/concise) is the minimum-viable form. Some tools benefit from three or four levels (`minimal | concise | standard | detailed`). Cost: each additional mode is another set of fields to spec, document, and maintain.
2. **Default selection** — Pick the default by dominant call pattern. If 80% of calls scan, default to concise; if 80% chain, default to detailed. Wrong default silently inflates token usage in the common path.
3. **Adaptive default** — Advanced variant: tool inspects remaining context budget and defaults to concise when budget is tight. Adds runtime complexity; only worth it for tools called frequently in long sessions.
4. **Schema discipline in concise mode** — Concise must remain useful: high-signal does not mean truncated. Drop low-signal fields entirely rather than truncating high-signal ones.

## Failure Modes

- **Agent defaults to concise when chaining** — Downstream tool call fails on missing ID. Mitigation: tool description explicitly names "chaining" as a detailed-mode trigger; recovery via retry with detailed.
- **Concise mode degrades into "detailed minus a few fields"** — Token savings disappear. Mitigation: design concise around the scan/triage use case first, not as a subset of detailed.
- **Enum value drift** — Renaming `concise` to `summary` mid-life breaks every caller. Mitigation: treat enum values as part of the tool's public contract; deprecate before remove.
- **Token budget claims drift from reality** — Documented "~72 tokens" no longer matches output. Mitigation: re-measure periodically and update tool description.

## Contract

### Preconditions
- Tool returns variable-length output where a high-signal subset is meaningfully smaller than the full payload.
- The caller is an agent (not a fixed downstream consumer that always needs full data).
- The tool description can document selection heuristics for the agent.

### Invariants
- `response_format` is a closed enum (not free-form string).
- The default mode is documented and chosen for the dominant call pattern.
- Detailed mode preserves all fields needed for chaining (IDs, references, full metadata).
- Concise mode strips chaining-required fields only when scan/triage is the named use case.
- Per-mode token budgets in the tool description are measured, not guessed.

### Governance
- **Owner:** Tool author.
- **Modification gate:** Adding new enum values requires updating the tool description and verifying agent-side selection heuristics still hold. Removing or renaming a value is a breaking change to the tool's public contract.
- **Scope:** Per-tool. Each tool has its own enum spec; enum values are not standardized across tools (a tool may have `minimal | summary | full` if those names fit better than `detailed | concise`).

### Recovery
- **Agent picks concise, chaining fails on missing IDs:** Agent retries with detailed; update tool description to clarify when concise is unsafe.
- **Token measurements drift from documented values:** Re-measure and update tool description.
- **Enum value needs to change:** Treat as a breaking change — add new value, deprecate old, migrate callers, then remove old.
