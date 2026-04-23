---
title: "Session Telemetry — Harness Requirements and SL Schema"
type: "design-note"
target_system:
  - "improvement-loop"
created: "2026-04-21"
updated: "2026-04-21"
author: "owner"
stage: "draft"
source_dd:
  - "DD-52"
  - "DD-59"
  - "DD-82"
  - "DD-86"
related_design_notes:
  - "project-management/design-notes/2026-04-21-agent-reflections-to-proposals-architecture.md"
tags:
  - "design-note"
  - "telemetry"
  - "observability"
  - "harness"
  - "system-log"
  - "session-metrics"
aliases:
  - "Session telemetry spec"
  - "Harness observability requirements"
  - "SL telemetry schema"
---

# Session Telemetry — Harness Requirements and SL Schema

**Status:** Design note. Captures a harness-portable requirement: what session-level telemetry the IL wants an agent runtime to emit, independent of which runtime is hosting it. Nick gates any downstream schema or DD.

**Prompted by:** Nick's session-51 direction (2026-04-21) — *"for the system log frontmatter, I want us to start capturing: tokens consumed, percent of context window consumed, model run, turns, average token consumption per subagent, number of tool calls."* Plus follow-on: *"If these are not available, then tell you what. Let's capture this as some sort of a pattern or design proposal so that if we choose to re-harness the implementation loop using something else that can give us this out of the box, we have that option."*

**Why a design note:** the requirement is durable; the current harness (Claude Code CLI) provides some of it, reliably surfaces only a subset, and doesn't cleanly surface subagent-granular telemetry. A design note separates the requirement from the capture implementation — so the requirement stays true across harness substitutions.

---

## 1. Purpose

Session-level telemetry serves three downstream consumers:

1. **Agent reflections** (see `2026-04-21-agent-reflections-to-proposals-architecture.md`). The reflection scaffold includes *"on efficiency — where am I burning tokens, time, or attention unnecessarily?"* Without telemetry in SL entries, that section is vibes-based. With it, reflections are grounded.
2. **Owner drift detection.** Sessions that run 800K+ tokens on a task that used to run 200K tokens are a signal — drift, bloat, poor context hygiene, or tooling regression. Without telemetry, the Owner can't detect these patterns.
3. **Harness evaluation.** If IL is ever re-hosted (custom runtime, different agent framework, bespoke SDK), today's telemetry becomes the benchmark. A candidate harness that exposes richer observability becomes a known upgrade; one that exposes less becomes a known regression.

Each of these gets better the more faithfully telemetry is captured — but the architecture stays valid even when capture is partial.

---

## 2. The two-layer model

| Layer | Purpose | Lifetime | Changes when? |
|---|---|---|---|
| **Requirement layer** | What telemetry IL wants recorded per session, harness-agnostic | Durable | Only when IL's observability needs change |
| **Capture layer** | How today's harness provides each field, with fallback rules | Harness-specific | Every time the harness changes |

This note specifies the requirement layer. The capture layer is described for the current harness (Claude Code CLI) and updated when the harness changes.

---

## 3. Requirement layer — what telemetry IL wants per session

Seven fields. Each has a durable intent independent of harness implementation.

| Field | Intent | Example | Consumer |
|---|---|---|---|
| `model` | Which model(s) drove the session. Multi-value if the session switched. | `claude-opus-4-7[1m]` | Drift detection, cost analysis, reflections §4 |
| `tokens_consumed` | Total tokens used by the session (input + output + cache read + cache write). | `287000` | Reflections §4, cost analysis |
| `context_window_size` | Max context size of the session's primary model. | `1000000` | Denominator for `context_window_pct` |
| `context_window_pct_peak` | Highest context fill reached during the session. | `28.7` | Pressure detection; sessions running >70% flag for compaction or split |
| `turns` | Number of user→assistant exchanges. | `14` | Session-shape detection; high turns + low tokens = frictional |
| `tool_calls` | Total tool invocations. | `87` | Tool-use density; correlates with externalization vs in-context reasoning |
| `subagents[]` | Per-subagent-type: count, avg tokens, total tokens. | `[{type: "Explore", count: 2, avg_tokens: 18000, total_tokens: 36000}]` | Decomposition analysis; reflection §4 for agents-that-spawn-agents |

### Why these seven specifically

- **`model`** is load-bearing because behavior differs across models. A reflection in six months that says *"I was Opus 4.6"* is different from one that says *"I was Haiku 4.5"*.
- **`tokens_consumed` + `context_window_pct_peak`** separates volume from pressure. A 300K-token session at 3% of context is different from a 300K-token session at 97%.
- **`turns` and `tool_calls`** are shape descriptors. Same token count can reflect 4 turns × 75K tokens (deep synthesis) or 40 turns × 7.5K tokens (frictional back-and-forth). Shape matters for reflection.
- **`subagents[]`** captures IL's hierarchical decomposition. When Owner spawns an Explore subagent, the Owner's parent-session token count doesn't include the subagent's spend. Without breakdown, we can't tell whether a session's budget went to the orchestrator or the delegates.

### Deliberately excluded

- **Wall-clock duration.** Easy to capture but a weak proxy for anything interesting — depends heavily on hardware and network. Not meaningful for reflection or drift detection. If ever added, as a weak signal field.
- **Cost in dollars.** Derivable from tokens × model rate. Don't duplicate.
- **Per-tool breakdown.** Useful but would dominate the frontmatter. If needed, emit as a separate `.telemetry.json` file alongside the SL entry rather than inline frontmatter.

---

## 4. Capture layer — today's harness (Claude Code CLI)

Reality check on what today's harness (Claude Code running via Cursor on macOS) reliably provides:

| Field | Availability | Source | Reliability |
|---|---|---|---|
| `model` | ✓ | Visible to Claude at session boot; Nick can confirm | High |
| `tokens_consumed` | Partial | Visible via `/status` in Claude Code UI to Nick; estimatable by Claude at close; `/gsd-session-report` skill estimates | Medium — mostly Nick-provided |
| `context_window_size` | ✓ | Fixed per model | High |
| `context_window_pct_peak` | Partial | Nick observes via Claude Code UI; Claude cannot introspect its own peak reliably | Medium — Nick-provided |
| `turns` | Partial | Countable in principle; no direct API surface in-session | Medium — Owner estimates at close, or user provides |
| `tool_calls` | Partial | Countable from transcript; `/gsd-session-report` estimates | Medium |
| `subagents[]` | Weak | Claude sees that subagents ran (tool results); does not see subagent token spend | Low — typically best-effort with explicit "unknown" |

**Population protocol for the current harness:**

1. At session close, the Owner (or the session-closing skill) drafts SL entry frontmatter with telemetry fields.
2. For fields marked *High*: populate autonomously.
3. For fields marked *Medium*: estimate + flag ("estimated" vs "reported by Nick"); ask Nick to confirm at SL entry review if he chooses.
4. For fields marked *Low* (subagent tokens): populate count and type; mark `avg_tokens: "unknown"` and `total_tokens: "unknown"` when not available.

Unknowns are a first-class value. An SL entry with `subagents[].avg_tokens: "unknown"` is valid. This preserves the schema and communicates what the harness can and can't surface.

---

## 5. SL frontmatter schema addition

Proposed additive field on all SL entries (no existing field changes):

```yaml
telemetry:
  model: "claude-opus-4-7[1m]"
  tokens_consumed: 287000
  context_window_size: 1000000
  context_window_pct_peak: 28.7
  turns: 14
  tool_calls: 87
  subagents:
    - type: "Explore"
      count: 2
      avg_tokens: 18000
      total_tokens: 36000
    - type: "general-purpose"
      count: 1
      avg_tokens: "unknown"
      total_tokens: "unknown"
  capture_quality: "estimated" | "reported" | "measured"
  harness: "claude-code-cli-cursor-macos"
```

Two meta-fields:
- `capture_quality` — self-disclosed fidelity. `measured` = directly observed from harness; `reported` = Nick or another authoritative actor provided; `estimated` = Claude's best-guess at session close.
- `harness` — the runtime that hosted the session. Future-proofing: when IL is re-harnessed, the harness identifier lets post-hoc analysis distinguish "this field was unknown under Claude Code CLI" from "this field was reliably captured under the new harness".

**All fields are optional** on the schema level. An SL entry without `telemetry:` is not invalid; it simply doesn't carry the telemetry (useful for historical SL entries written before this schema landed). Going forward, populate what's available and mark the rest `unknown`.

---

## 6. Harness requirements, made explicit

When IL is re-harnessed, the new harness is evaluated against this requirement list. Minimum viable harness exposes:

**Required (measurable, not estimated):**
- Current model identifier, reliably retrievable at session start and mid-session (model switches).
- Running token total (cumulative across input, output, cache read, cache write).
- Context window percent fill, with access to peak value across the session.

**Strong preference:**
- Turn count, tool-call count — derivable from transcript but ideally surfaced as counters.
- Per-subagent token spend — critical for hierarchical architectures. Any harness that doesn't surface this is a regression against IL's agent model, even if it's otherwise richer.

**Nice to have:**
- Per-tool-call token breakdown.
- Cache-hit-rate telemetry.
- Inter-turn latency.

**A candidate harness that exposes all of the above as API-level values is the upgrade target.** A candidate that exposes less than today's Claude Code CLI is a regression and should be evaluated against what IL loses.

---

## 7. Cross-system applicability

Every system in MetaSystem (IL, Meta-System, Household OS, Claude Build) has a system-log folder per DD-59. Every one of those folders produces SL entries. If the telemetry schema is useful for IL, it is likely useful everywhere.

**Pathway to cross-system adoption:**
1. IL adopts the schema first (this note).
2. After 5–10 sessions of IL telemetry data, the Owner evaluates — does the telemetry change behavior? Help reflections? Surface drift?
3. If yes: the Owner proposes a MetaSystem-level DD generalizing the schema to all systems' SL entries. Updates `_schema.yaml` accordingly.
4. If no: retain IL-only, document why, consider retiring or simplifying.

IL as the test-bed is consistent with DD-80's stance on pipeline simplification — evaluate before generalizing.

**This note does not propose cross-system adoption yet.** The pattern earns generalization after it proves itself in IL.

---

## 8. Relationship to existing mechanisms

| Mechanism | Relationship |
|---|---|
| **Reflections architecture** (`2026-04-21-agent-reflections-to-proposals-architecture.md`) | Primary consumer. Reflection §4 efficiency discussion is grounded on this telemetry. |
| **`/gsd-session-report`** (cross-system skill) | Adjacent tool. Generates session reports with token estimates; overlaps with `capture_quality: "estimated"` path. Can be used as input to populate the `telemetry:` block. |
| **`_schema.yaml`** (workspace root) | Target for schema amendment if IL adoption succeeds. This note does not propose the amendment directly. |
| **SL template** (if one exists under `systems/meta-system/knowledge/templates/`) | Target for template refresh so new SL entries carry the `telemetry:` block by default. |
| **`/session-handoff` skill** | Possible capture touchpoint. When the handoff skill runs, it could collect telemetry as part of its state-dumping step and emit it into the SL frontmatter. |
| **OpenTelemetry / Claude Code observability** | If Claude Code is configured with OTel export (per MetaSystem preflight manifest), that's the measured-path for several fields. Check whether `.claude/settings.json` exposes the relevant env vars. |

---

## 9. What this design note does not do

- **Does not file a DD.** The schema amendment is a later DD proposal if Nick chooses.
- **Does not amend `_schema.yaml`.** Schema amendment is a workspace-root edit (cross-system); out of session-51 scope.
- **Does not build a capture skill.** A `/capture-session-telemetry` skill may be worth building; not this note's scope.
- **Does not retroactively populate existing SL entries.** Historical entries don't carry telemetry; new ones do. Backfill is explicitly not required.
- **Does not generalize to non-IL systems.** §7 flags the pathway; doesn't commit to it.

---

## 10. Open questions for Nick

1. **Unknowns handling.** Proposed: `"unknown"` as a first-class value. Acceptable, or prefer `null` / omission / explicit comment?
2. **Capture responsibility.** Who populates the `telemetry:` block — the `/session-handoff` skill, a new `/capture-session-telemetry` skill, or the Owner at session close by convention?
3. **`capture_quality` granularity.** Currently one field for the whole block. Worth making per-field? (e.g., `model` is measured, `subagents[].avg_tokens` is unknown). Simpler: one overall quality indicator, with field-level `"unknown"` doing the finer-grain work. Keep simple?
4. **`harness` identifier format.** Proposed: free-form string (`"claude-code-cli-cursor-macos"`). Controlled vocabulary instead? Per-system or MetaSystem-level? If we ever re-harness, a controlled set makes cross-harness analysis cleaner.
5. **IL-scoped vs MetaSystem-scoped adoption.** §7 defers. Comfortable with IL-first adoption, or want cross-system from day one?
6. **Schema location.** Should the schema land in `_schema.yaml` (workspace root, cross-system) or IL-local first? Per §7, IL-local first; defer `_schema.yaml` amendment.

---

## 11. Next steps

If Nick accepts the shape:

1. **Add `telemetry:` block to session 51 SL entry** as the first telemetry-bearing SL entry. Populate what's available; mark unknowns. Serves as the worked example.
2. **Update SL template** (wherever it lives) to include the block by default.
3. **Evaluate after 5–10 sessions.** Does the data change reflection quality? Owner decision quality? If yes → DD proposal + cross-system generalization. If no → simplify or retire.
4. **Surface in a future DD** if the pattern lands — codifying the requirement layer as governance, not just practice.

---

## 12. Cross-references

- **Precipitating direction:** Nick's session-51 direction (2026-04-21), captured in §Purpose.
- **Primary consumer:** `project-management/design-notes/2026-04-21-agent-reflections-to-proposals-architecture.md` §4 (efficiency reflection grounded on telemetry).
- **Related in-flight artifacts:** session 51 Codifier edit proposal (`governance/proposals/2026-04-21-codifier-agent-constitution-design-notes-edit.md`); four-zone DD proposal (`governance/proposals/2026-04-22-dd-proposal-owner-design-artifact-placement.md`).
- **Adjacent tool:** `/gsd-session-report` (cross-system skill).
- **Schema target:** `_schema.yaml` (workspace root).
- **Governing DDs:** DD-52 (fractal pattern), DD-59 (system-log scoping), DD-82 (4-agent architecture), DD-86 (Owner responsibility).
