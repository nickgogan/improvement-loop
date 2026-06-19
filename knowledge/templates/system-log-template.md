---
title: "{Session N — Short descriptive title of what happened}"
type: "system-log"
target_system:
  - "{system-name}"   # improvement-loop (sole live system). Archived (historical rows only): household-os | claude-build
actor: "{Agent: Claude (role disposition) | Nick | Multi-actor: [...]}"
area: null            # optional subsystem/area tag
change_type: "{Design | Implementation | Migration | Governance | Bugfix | Cleanup | ...}"
milestone: null       # optional milestone reference
rationale: "{1-3 sentence summary of why this session happened and what it produced. This line is the SL entry's elevator pitch — it should stand alone as a searchable summary.}"
source_dd: "{DD-XX, DD-YY, ...}"    # comma-separated list of governing DDs
timestamp: "{ISO-8601 timestamp}"
session: {N}          # integer session number
tags:
  - "system-log"
  - "{primary-tag}"
  - "{secondary-tag}"

# === Session telemetry (see _schema.yaml; agent-reflections and drift-detection substrate) ===
telemetry:
  model: "{claude-opus-4-7[1m] | claude-sonnet-4-6 | ...}"
  tokens_consumed: {integer-or-"unknown"}
  context_window_size: {integer}            # e.g., 1000000 for 1M variant
  context_window_pct_peak: {number-or-"unknown"}
  turns: {integer-or-"unknown"}
  tool_calls: {integer-or-"unknown"}
  subagents:
    # - type: "Explore"
    #   count: 2
    #   avg_tokens: 18000-or-"unknown"
    #   total_tokens: 36000-or-"unknown"
  capture_quality: "{measured | estimated}"   # Nick is not a telemetry source — unmeasurable, unestimable fields land as "unknown"
  harness: "{claude-code-cli-cursor-macos | other}"
  capture_note: "{optional free-form note on capture context — e.g., 'tokens estimated at session close; subagent breakdown not exposed by harness'}"
---

# {Session N — Short descriptive title}

## Session Scope

{1 paragraph: what the session set out to do; how that scope evolved (if at all); what was actually delivered.}

---

## What Changed

### {Stream A — name}

- {bullet: specific artifact created, decision made, finding surfaced}
- {bullet: ...}

### {Stream B — name (if applicable)}

- {bullet: ...}

---

## Artifacts Produced

| # | Type | Path |
|---|---|---|
| 1 | {proposal | design-note | skill | agent-constitution-edit | SL-entry | ...} | `{relative path}` |

---

## Key Decisions (by actor)

1. **{Decision 1}.** {Who decided it; quote or paraphrase if a user quote is load-bearing; 1-line rationale.}
2. {...}

---

## Readiness Checklist — downstream work pending

| Item | Gated on | Owner |
|---|---|---|
| {thing to do next} | {DD filing / review / brief} | {who} |

---

## Observations

### What went well
- {bullet}

### What could have gone better
- {bullet}

### Help {actor} could use
- {bullet}

---

## Links

- **Handoff input (if applicable):** `{path}`
- **Precursor session:** `{path to prior SL entry}`
- **Active proposals at session close:**
  - `{path}`
- **Active design notes at session close:**
  - `{path}`
