---
title: "Tiered Memory File Architecture (Hot/Warm/Cold)"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "bounded-tiered-memory-inference-driven-curation"
extraction_date: "2026-05-25"
last_change_session: 102
last_change_sl: "session-102-codifier-identify-and-extract-artifacts"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent systems that persist user or environment state across sessions and need to prevent unbounded memory growth"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — schema migration is needed if hot-tier file structure changes; adding warm/cold tiers is additive and reversible"
  auditability: "high — hot-tier files are plain markdown; warm-tier retrieval queries are logged; cold-tier is append-only JSONL"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Not Yet Started"
    notes: "Pattern from Nous Research Hermes agent. MetaSystem MEMORY.md has no hard ceiling and no curator step at time of extraction."
contract:
  preconditions: "The agent has access to persistent file storage across sessions. A SQLite database (or equivalent full-text search store) is available for the warm tier. The agent can make write decisions based on conversation content without explicit user commands."
  invariants: "Hot-tier files never exceed their declared character ceilings. The Curator step runs whenever a ceiling is reached — never deferred. Cold-tier JSONL is append-only; no deletion. Inference-driven writes use explicit criteria, not 'record everything'."
  governance: "Ceilings are declared in the agent's system prompt and enforced by the agent loop or a hook. The Curator step procedure is a named, documented operation — not ad-hoc summarization. Changes to tier boundaries (ceiling sizes, FTS5 schema) are configuration changes requiring explicit decision."
  recovery: "If a hot-tier file exceeds its ceiling before the Curator runs → run Curator immediately; do not write further until ceiling is restored. If the FTS5 database is corrupt or unavailable → degrade to hot-tier-only; log the warm-tier gap; restore the DB before the next session. If Curator evicts an entry that later proves important → the cold tier (JSONL) is the audit log; restore from there."
tags:
  - "extracted-artifact"
  - "template"
  - "memory"
  - "context-engineering"
  - "agent-design"
---

# Tiered Memory File Architecture (Hot/Warm/Cold)

**Source:** [[bounded-tiered-memory-inference-driven-curation]]
**Form:** template
**Extraction date:** 2026-05-25

## Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{SOUL_FILE}}` | Path to the agent identity file (always-injected, no ceiling) | `SOUL.md` |
| `{{MEMORY_FILE}}` | Path to environment facts memory file | `MEMORY.md` |
| `{{MEMORY_CEILING}}` | Hard character ceiling for MEMORY_FILE | `2200` |
| `{{USER_FILE}}` | Path to user preference memory file | `USER.md` |
| `{{USER_CEILING}}` | Hard character ceiling for USER_FILE | `1375` |
| `{{STATE_DB}}` | Path to SQLite database for warm-tier FTS5 | `state.db` |
| `{{SESSIONS_DIR}}` | Directory for cold-tier JSONL transcripts | `sessions/` |
| `{{CURATOR_PROMPT}}` | Prompt used by the Curator step to consolidate/evict | see Curator Step below |
| `{{WRITE_TRIGGER_CRITERIA}}` | Conditions under which the agent writes to memory | see Inference-Driven Write section below |

---

## Body

### Tier Definitions

#### Hot Tier — Always Injected

| File | Purpose | Ceiling |
|------|---------|---------|
| `{{SOUL_FILE}}` | Agent identity, values, behavioral invariants | None — stable, rarely changes |
| `{{MEMORY_FILE}}` | Environment facts: tool versions, project paths, integration states | `{{MEMORY_CEILING}}` chars |
| `{{USER_FILE}}` | User preferences, working style, priorities, recurring corrections | `{{USER_CEILING}}` chars |

All three files are loaded verbatim into the system prompt at session start. Timestamps are embedded in each entry.

#### Warm Tier — FTS5 Retrieved

Prior-session snippets stored in `{{STATE_DB}}` using SQLite FTS5 full-text search. At session start:
1. The agent generates 2-5 retrieval queries based on the current task or conversation opener.
2. FTS5 returns top-N matching snippets.
3. An LLM summarization step condenses the snippets before injection.

```sql
-- Schema (warm tier)
CREATE VIRTUAL TABLE memory_snippets USING fts5(
  session_id,
  timestamp,
  content,
  tags
);
```

#### Cold Tier — Archival JSONL

Append-only raw transcripts in `{{SESSIONS_DIR}}`. One JSONL file per session. Never deleted. Used for:
- Audit and recovery (restore evicted hot-tier entries)
- Offline analysis and manual review
- Training data if applicable

---

### Inference-Driven Write Triggers

The agent writes to hot-tier memory files without explicit user commands when `{{WRITE_TRIGGER_CRITERIA}}` are met. Default criteria:

```
Write to {{MEMORY_FILE}} when:
- A new tool, integration, or environment fact is confirmed working
- A project path, credential name, or config value is established
- A previous MEMORY_FILE entry is corrected by new information

Write to {{USER_FILE}} when:
- The user expresses a preference not already recorded
- The user corrects a previous preference entry
- A recurring pattern in user requests emerges (3+ instances)

Do NOT write when:
- The information is task-specific and not session-persistent
- The user explicitly says "don't remember this"
- The information is likely to be stale within one session
```

---

### Curator Step

Run when any hot-tier file reaches its ceiling. Procedure:

```
{{CURATOR_PROMPT}}

Default curator prompt:
You are reviewing {{TARGET_FILE}} which has reached its {{CEILING}}-character ceiling.
Current content: [FILE_CONTENT]

Your task:
1. Identify entries that are redundant, outdated, or low-confidence.
2. Merge entries that describe the same fact with different timestamps (keep most recent).
3. Evict entries that have not been referenced in the last N sessions.
4. If two entries conflict, keep the most recent high-confidence fact; note the conflict resolution.
5. Ensure the resulting file is under {{CEILING}} characters.
6. Output the revised file content only — no commentary.
```

Before running Curator: append the about-to-be-evicted entries to `{{STATE_DB}}` (warm tier) and `{{SESSIONS_DIR}}/curator-evictions.jsonl` (cold tier). This ensures no information is permanently lost.

---

## Usage

1. Create the three hot-tier files (`{{SOUL_FILE}}`, `{{MEMORY_FILE}}`, `{{USER_FILE}}`).
2. Initialize `{{STATE_DB}}` with the FTS5 schema above.
3. Create `{{SESSIONS_DIR}}` directory.
4. Declare the ceilings in the agent's system prompt: "{{MEMORY_FILE}} must not exceed {{MEMORY_CEILING}} characters. Run the Curator step when the ceiling is reached."
5. Embed `{{WRITE_TRIGGER_CRITERIA}}` in the agent's system prompt.
6. Configure the Curator step with `{{CURATOR_PROMPT}}` — or adopt the default prompt above.
7. At session start: load hot tier verbatim → run warm-tier FTS5 queries → summarize → inject.
8. At session end: append session transcript to `{{SESSIONS_DIR}}/{{SESSION_ID}}.jsonl`.

---

## Variation Axis

| Axis | Option A | Option B |
|------|----------|----------|
| **Write trigger** | Inference-driven (agent decides) | Explicit user command only ("remember this") |
| **Warm tier retrieval** | FTS5 full-text search | Embedding-based semantic search |
| **Curator timing** | On ceiling breach | Periodic (every N sessions) |
| **Curator executor** | LLM (same agent) | Separate curator subagent with tighter scope |
| **Cold tier format** | JSONL transcripts | Structured event log with typed fields |
| **Ceiling size** | Fixed values from this template | Dynamically adjusted based on session frequency |

---

## Contract

### Preconditions
The agent has access to persistent file storage across sessions. A SQLite database (or equivalent full-text search store) is available for the warm tier. The agent can make write decisions based on conversation content without explicit user commands.

### Invariants
Hot-tier files never exceed their declared character ceilings. The Curator step runs whenever a ceiling is reached — never deferred. Cold-tier JSONL is append-only; no deletion. Inference-driven writes use explicit criteria, not "record everything."

### Governance
Ceilings are declared in the agent's system prompt and enforced by the agent loop or a hook. The Curator step procedure is a named, documented operation — not ad-hoc summarization. Changes to tier boundaries (ceiling sizes, FTS5 schema) are configuration changes requiring explicit decision.

### Recovery
If a hot-tier file exceeds its ceiling before the Curator runs → run Curator immediately; do not write further until ceiling is restored. If the FTS5 database is corrupt or unavailable → degrade to hot-tier-only; log the warm-tier gap; restore the DB before the next session. If Curator evicts an entry that later proves important → the cold tier (JSONL) is the audit log; restore from there.
