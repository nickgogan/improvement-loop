---
title: "Tiered Memory File Architecture (Hot/Warm/Cold)"
type: "extracted-artifact"
assigned_form: "template"
source_finding: "bounded-tiered-memory-inference-driven-curation"
extraction_date: "2026-05-25"
last_change_session: 146
last_change_report: "2026-07-13-source-drift"
identification_report: null
deployed: false
deployed_to: null
context:
  applies_to:
    - "agent systems that persist user or environment state across sessions and need to prevent unbounded memory growth"
    - "operators who want a portable, file-based memory architecture that transfers across agent runtimes"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "build"
  reversibility: "medium — schema migration is needed if hot-tier file structure changes; adding warm/cold tiers is additive and reversible; the portable-markdown variant reverses trivially"
  auditability: "high — hot-tier files are plain markdown; warm-tier retrieval queries are logged; cold-tier is append-only JSONL; promotion rules in an operator-editable policy file are themselves auditable"
  evidence_strength: "Strong (production-tested)"
  adoption:
    status: "Not Yet Started"
    notes: "Production pattern from the Hermes agent (Nous Research); independently rebuilt inside Claude Code as portable local markdown (2026-07: ~2,500-char capped snapshot, post-turn-hook writes, user-editable promotion rules), confirming the architecture transfers across runtimes."
contract:
  preconditions: "The agent has access to persistent file storage across sessions. If the warm tier is used, a SQLite database (or equivalent full-text search store) is available; the portable-markdown variant omits it. The agent can make write decisions based on conversation content without explicit user commands (via write-time inference or a post-turn hook)."
  invariants: "Hot-tier files never exceed their declared character ceilings. The Curator step runs whenever a ceiling is reached — never deferred. Cold-tier storage is append-only; no deletion. Inference-driven writes use explicit criteria, not 'record everything'. Promotion/curation criteria are declared in a readable, operator-editable location — never implicit in the loop. Operator-designated standing instructions live outside ceiling-governed files."
  governance: "Ceilings are declared in the agent's system prompt or configuration and enforced by the agent loop or a hook. The Curator step procedure is a named, documented operation — not ad-hoc summarization. Promotion rules are owned by the operator and editable without modifying the loop. Changes to tier boundaries (ceiling sizes, FTS5 schema, hook triggers) are configuration changes requiring explicit decision."
  recovery: "If a hot-tier file exceeds its ceiling before the Curator runs → run Curator immediately; do not write further until ceiling is restored. If the FTS5 database is corrupt or unavailable → degrade to hot-tier-only; log the warm-tier gap; restore the DB before the next session. If Curator evicts or overwrites an entry that later proves important → the cold tier (append-only) is the audit log; restore from there. If curation compresses away standing instructions → restore them and relocate to an uncapped identity/instruction file before resuming."
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
| `{{SOUL_FILE}}` | Path to the agent identity file (always-injected, no ceiling; standing instructions live here, out of Curator reach) | `SOUL.md` |
| `{{MEMORY_FILE}}` | Path to environment facts memory file | `MEMORY.md` |
| `{{MEMORY_CEILING}}` | Hard character ceiling for MEMORY_FILE | `2200` (original) / `2500` (portable rebuild) |
| `{{USER_FILE}}` | Path to user preference memory file | `USER.md` |
| `{{USER_CEILING}}` | Hard character ceiling for USER_FILE | `1375` |
| `{{STATE_DB}}` | Path to SQLite database for warm-tier FTS5 (omit in portable-markdown variant) | `state.db` |
| `{{SESSIONS_DIR}}` | Directory for cold-tier append-only transcripts | `sessions/` |
| `{{CURATOR_PROMPT}}` | Prompt used by the Curator step to consolidate/evict | see Curator Step below |
| `{{WRITE_TRIGGER_CRITERIA}}` | Conditions under which the agent writes to memory | see Inference-Driven Write section below |
| `{{PROMOTION_RULES_FILE}}` | Operator-editable, human-readable policy file defining what qualifies for promotion to hot-tier memory and what is evicted first | `memory-policy.md` |

---

## Body

### Tier Definitions

#### Hot Tier — Always Injected

| File | Purpose | Ceiling |
|------|---------|---------|
| `{{SOUL_FILE}}` | Agent identity, values, behavioral invariants, standing instructions | None — stable, rarely changes; never curated |
| `{{MEMORY_FILE}}` | Environment facts: tool versions, project paths, integration states | `{{MEMORY_CEILING}}` chars |
| `{{USER_FILE}}` | User preferences, working style, priorities, recurring corrections | `{{USER_CEILING}}` chars |

All three files are loaded verbatim into the system prompt at session start. Timestamps are embedded in each entry. Standing instructions belong in `{{SOUL_FILE}}` (uncapped, uncurated) — production evidence shows that placing them in ceiling-governed files leads to curation progressively compressing them away.

#### Warm Tier — FTS5 Retrieved (optional)

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

The **portable-markdown variant** (2026-07 practitioner rebuild) omits this tier entirely: the hot tier is a capped curated snapshot plus a profile file and a "today's memories" file, all plain local markdown. This keeps the whole architecture runtime-independent at the cost of losing full-text recall of older sessions.

#### Cold Tier — Archival Append-Only

Append-only raw transcripts in `{{SESSIONS_DIR}}`. One JSONL file per session. Never deleted. Used for:
- Audit and recovery (restore evicted or curation-damaged hot-tier entries)
- Offline analysis and manual review
- Training data if applicable

---

### Inference-Driven Write Triggers

The agent writes to hot-tier memory files without explicit user commands when `{{WRITE_TRIGGER_CRITERIA}}` are met. Two proven trigger mechanisms:

- **Write-time inference (original):** the agent decides mid-conversation that a fact is worth persisting and writes it, subject to the ceiling check.
- **Post-turn hook (portable rebuild):** a hook runs after every turn and decides whether anything from the turn is worth promoting as a durable fact (decisions, changed values, preferences). The hook is the single choke point for all memory promotion, which also closes bypass paths.

Default criteria:

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

Declare these criteria in `{{PROMOTION_RULES_FILE}}` — a readable policy file the operator owns and can edit without touching the loop. Baking promotion policy into the loop makes curation errors uncorrectable by the operator.

---

### Curator Step

Run when any hot-tier file reaches its ceiling. Overflow policy: **dedup-then-replace** — merge duplicate facts, then replace older/lower-relevance entries in favor of the most-recent, most-relevant. Procedure:

```
{{CURATOR_PROMPT}}

Default curator prompt:
You are reviewing {{TARGET_FILE}} which has reached its {{CEILING}}-character ceiling.
Current content: [FILE_CONTENT]
Promotion/eviction policy: [{{PROMOTION_RULES_FILE}} CONTENT]

Your task:
1. Identify entries that are redundant, outdated, or low-confidence.
2. Merge entries that describe the same fact with different timestamps (keep most recent).
3. Evict entries that have not been referenced in the last N sessions, respecting the policy file's eviction priorities.
4. If two entries conflict, keep the most recent high-confidence fact; note the conflict resolution.
5. Never evict entries marked evict-proof; never summarize standing instructions.
6. Ensure the resulting file is under {{CEILING}} characters.
7. Output the revised file content only — no commentary.
```

Before running Curator: append the about-to-be-evicted entries to `{{STATE_DB}}` (warm tier, if present) and `{{SESSIONS_DIR}}/curator-evictions.jsonl` (cold tier). This ensures no information is permanently lost — production reports of self-curating agents overwriting good information in their own memory/skill files make this archive step load-bearing, not optional.

---

## Usage

1. Create the three hot-tier files (`{{SOUL_FILE}}`, `{{MEMORY_FILE}}`, `{{USER_FILE}}`) and `{{PROMOTION_RULES_FILE}}`.
2. Initialize `{{STATE_DB}}` with the FTS5 schema above (skip in the portable-markdown variant).
3. Create `{{SESSIONS_DIR}}` directory.
4. Declare the ceilings in the agent's system prompt or configuration: "{{MEMORY_FILE}} must not exceed {{MEMORY_CEILING}} characters. Run the Curator step when the ceiling is reached."
5. Embed `{{WRITE_TRIGGER_CRITERIA}}` in `{{PROMOTION_RULES_FILE}}` and reference it from the agent's system prompt (or wire it into the post-turn hook).
6. Configure the Curator step with `{{CURATOR_PROMPT}}` — or adopt the default prompt above.
7. At session start: load hot tier verbatim → run warm-tier FTS5 queries (if present) → summarize → inject.
8. At session end (or per turn, in the hook variant): append the transcript to `{{SESSIONS_DIR}}/{{SESSION_ID}}.jsonl`.

---

## Variation Axis

| Axis | Option A | Option B |
|------|----------|----------|
| **Write trigger** | Inference-driven (agent decides) | Explicit user command only ("remember this") |
| **Write timing** | Write-time inference (mid-conversation) | Post-turn hook (decides after every turn; single promotion choke point) |
| **Warm tier** | FTS5 full-text search over SQLite | Omitted — portable local markdown only (hot snapshot + profile + today's memories) |
| **Warm tier retrieval** | FTS5 full-text search | Embedding-based semantic search |
| **Curator timing** | On ceiling breach | Periodic (every N sessions) |
| **Curator executor** | LLM (same agent) | Separate curator subagent with tighter scope |
| **Curation policy location** | Embedded in system prompt / loop | Operator-editable policy file (`{{PROMOTION_RULES_FILE}}`) |
| **Cold tier format** | JSONL transcripts | Structured event log with typed fields |
| **Ceiling size** | Fixed values from this template | Dynamically adjusted based on session frequency |

---

## Contract

### Preconditions
The agent has access to persistent file storage across sessions. If the warm tier is used, a SQLite database (or equivalent full-text search store) is available; the portable-markdown variant omits it. The agent can make write decisions based on conversation content without explicit user commands (via write-time inference or a post-turn hook).

### Invariants
Hot-tier files never exceed their declared character ceilings. The Curator step runs whenever a ceiling is reached — never deferred. Cold-tier storage is append-only; no deletion. Inference-driven writes use explicit criteria, not "record everything." Promotion/curation criteria are declared in a readable, operator-editable location — never implicit in the loop. Operator-designated standing instructions live outside ceiling-governed files.

### Governance
Ceilings are declared in the agent's system prompt or configuration and enforced by the agent loop or a hook. The Curator step procedure is a named, documented operation — not ad-hoc summarization. Promotion rules are owned by the operator and editable without modifying the loop. Changes to tier boundaries (ceiling sizes, FTS5 schema, hook triggers) are configuration changes requiring explicit decision.

### Recovery
If a hot-tier file exceeds its ceiling before the Curator runs → run Curator immediately; do not write further until ceiling is restored. If the FTS5 database is corrupt or unavailable → degrade to hot-tier-only; log the warm-tier gap; restore the DB before the next session. If Curator evicts or overwrites an entry that later proves important → the cold tier (append-only) is the audit log; restore from there. If curation compresses away standing instructions → restore them and relocate to an uncapped identity/instruction file before resuming.
