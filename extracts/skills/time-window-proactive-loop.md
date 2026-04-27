---
title: Time-Window Proactive Loop
type: extracted-artifact
assigned_form: skill
source_finding: time-window-proactive-agent-loop
identification_report: "building-agentic-systems.harvest-queue.md::time-window-proactive-agent-loop::skill::time-window-proactive-loop"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - scheduled-task agents that initiate proactively rather than waiting for user prompts
    - proactive briefing systems that deliver time-aware summaries via channel tools
    - life-engine and work-engine deployments that need recurring decision loops anchored to wall-clock time
    - time-aware notification agents whose payload depends on the time window of invocation
  platform_coupling: agnostic — invokable from any cron, scheduler, or daemon. Channel delivery (Telegram/Discord/etc.) is parameterized.
  autonomy: supervised — the skill executes the full loop autonomously per tick, but the briefing payload is delivered to a human consumer who sets engagement signals (mute, ack, follow-up) that feed back into duplicate-checking and frequency tuning.
  stage: operate
  reversibility: trivial — the skill is invoked per-tick and holds no irreversible state outside the briefings log; disabling the cron tick halts the loop and the log can be read or discarded.
  auditability: high — every delivered briefing is appended to the briefings table with `anchor_date`, time window, and briefing type; the log is the deduplication mechanism and the audit trail simultaneously.
  evidence_strength: Medium (practitioner-documented)
  adoption:
    status: Not Yet Started
    notes: null
contract:
  preconditions: |
    A reliable time source is available (system clock or API response) — the skill establishes its own anchor and does not trust caller-supplied timestamps. A briefings table (or equivalent log store) is readable and writable for the current `anchor_date`. The closed enums for time windows (5 values) and briefing types (7 values) are defined before invocation. At least one delivery channel (Telegram, Discord, or equivalent) is configured. A cron or scheduler is invoking the skill at a cadence finer than the smallest time window.
  invariants: |
    The loop terminates per tick — it is never long-running. `anchor_date` and `anchor_time` are established as the first action of every invocation; no date arithmetic uses vague terms ("recently", "today" without anchor). A briefing is delivered on a given (anchor_date, briefing_type) pair at most once — the duplicate check is mandatory before delivery. External data is fetched before internal enrichment, never after. Silence is a valid output: if the time window has no scheduled briefing or the duplicate check matches, the tick exits without delivery. Every delivery produces a corresponding log entry; no delivery without logging.
  governance: |
    Owner: the human consumer of the briefings, who defines time windows, briefing types, and channel preferences. The skill does not modify its own enums or schedule during execution. The briefings log is the single source of truth for what has been delivered — corruption of the log breaks the deduplication invariant and must be recovered from backups before the loop resumes. Channel tool credentials are caller-owned. If the skill is deployed in a multi-user context, the briefings log must be partitioned per consumer.
  recovery: |
    If the date anchor cannot be established (clock unavailable, API failure): halt the tick; do not deliver; emit a diagnostic. If the briefings table is unreadable: halt the tick; do not deliver (delivering blind risks duplicates). If external data fetch fails: degrade gracefully — deliver an internal-only briefing with an explicit note that external data was unavailable, OR skip the tick if the briefing type is external-data-required (e.g., pre_meeting). If the channel tool fails: log the intended delivery; retry on the next tick if the briefing is still time-window-valid; do not retry indefinitely. If notification fatigue is detected (consumer mutes channel or sets a quiet flag): suppress non-critical briefing types until the flag is cleared.
tags:
  - extracted-artifact
  - skill
  - proactive-agent
  - scheduled-task
---

# Time-Window Proactive Loop

**Source:** [[time-window-proactive-agent-loop]]
**Form:** skill
**Extraction date:** 2026-04-27

## Inputs

- **Cron tick / current time:** The skill is invoked by an external scheduler at a cadence finer than the smallest time window (e.g., every 15 minutes). The current time is established internally — caller-supplied timestamps are not trusted.
- **`anchor_date` / `anchor_time`:** Established as step 0 of every invocation via the `date` command or API response. All date arithmetic is calculated from this anchor — never use vague terms like "recently" or "today" without anchor.
- **Briefings table:** Read-write store of prior deliveries, keyed by `(anchor_date, briefing_type)`. Used for the duplicate check (step 2) and log write (step 7). The briefings log is the deduplication mechanism — corruption means repeated messages.
- **Time window enum (closed, 5 values):** `early_morning | pre_meeting | midday | late_afternoon | evening`. Each window has a defined start/end time and a set of permitted briefing types.
- **Briefing type enum (closed, 7 values):** `morning | pre_meeting | checkin | evening | habit_reminder | weekly_review | custom`.
- **External data sources:** Calendar API, weather API, attendee directory — fetched in step 4. External-before-internal is mandatory: cannot enrich what hasn't been seen.
- **Knowledge base:** Internal store searched in step 5 for context on the external data (attendee history, meeting topics, related notes).
- **Channel tools:** Delivery target — Telegram, Discord, or equivalent. Mobile-friendly, concise, bullet-point output.

## Outputs

- **Delivered briefing:** A concise, mobile-friendly message sent via the configured channel tool — OR silence if the duplicate check matched, the time window has no scheduled briefing, or a quiet flag is set. Silence is better than noise.
- **Log entry:** An append-only record in the briefings table containing `anchor_date`, `anchor_time`, time window, briefing type, channel, and delivery status. Written on every successful delivery; absence of a log entry means absence of delivery.

## Steps

The 8-step procedure (steps 0–7) from the source finding. Each step has named state and produces a verifiable side effect or decision.

0. **Date anchor.** Establish exact date/time via `date` command or API response. Store as `anchor_date` and `anchor_time`. All subsequent date arithmetic is calculated from this anchor — never use vague terms like "recently." If the anchor cannot be established, halt the tick.

1. **Time check.** Classify `anchor_time` into one of the 5 time windows: `early_morning`, `pre_meeting`, `midday`, `late_afternoon`, `evening`. The classification is deterministic from `anchor_time` and the configured window boundaries.

2. **Duplicate check.** Query the briefings table for entries with `anchor_date` matching today's anchor. For each candidate briefing type the time window allows, check whether it has already been delivered today. If all candidate types are already delivered, exit the tick silently.

3. **Decide.** Based on the time window and the duplicate-check result, select the briefing type (one of 7: `morning`, `pre_meeting`, `checkin`, `evening`, `habit_reminder`, `weekly_review`, `custom`) to deliver this tick. If no type is appropriate, exit the tick silently.

4. **External pull.** Fetch live data the briefing type requires — calendar events, weather, attendee lists. External data must be fetched before internal enrichment (step 5), never after. If the fetch fails and the briefing is external-data-required (e.g., `pre_meeting`), halt the tick or degrade per the recovery contract.

5. **Internal enrich.** Search the knowledge base for context on what step 4 returned — attendee history, meeting topics, related notes. The enrichment uses the external pull as its query input; the order is fixed (external before internal).

6. **Deliver.** Send the assembled briefing via the configured channel tool (Telegram/Discord). Concise, mobile-friendly, bullet points. Silence is better than noise — if the briefing has no actionable content, prefer no delivery over an empty message.

7. **Log.** Append an entry to the briefings table recording `anchor_date`, `anchor_time`, time window, briefing type, channel, and delivery status. The log is the deduplication mechanism — every delivery must produce a log entry, and no delivery may occur without a corresponding log write.

## Boundary

**In scope:**
- Per-tick decision logic over a closed time-window enum and a closed briefing-type enum
- External-then-internal data assembly for time-aware payloads
- Channel-mediated delivery with deduplication via a persistent log

**Out of scope:**
- Cron / scheduler implementation (the skill is invoked, not the invoker)
- Channel tool authentication (handled by the caller / harness)
- Long-running daemons or event-driven triggers (this is tick-driven; calendar-event triggers are a different pattern — see Alternatives in the source finding)
- Multi-tick state beyond the briefings log (the skill is stateless across ticks except via the log)

## Failure Modes

- **Notification fatigue.** Proactive agents that talk too much get muted. Mitigation: tune briefing-type frequency; respect quiet flags; prefer silence when no actionable content exists; consider priority-based delivery during focus windows.

- **Date anchor drift.** If the system clock is wrong or the anchor is established from an unreliable source, all time-window logic fails — wrong window selected, wrong duplicate-check date, log entries with bogus dates. Mitigation: always establish anchor as step 0; use a redundant time source where possible; halt the tick if anchor establishment fails.

- **Channel tool reliability.** Telegram/Discord API failures break delivery. Mitigation: log the intended delivery on failure; retry on the next tick if the briefing is still time-window-valid; don't retry indefinitely (use the time window as the retry horizon).

- **State table corruption.** The briefings log is the deduplication mechanism — corruption means repeated messages. Mitigation: append-only writes; periodic backup; on detection of corruption, halt the loop and recover from backup before resuming.

- **External-before-internal violation.** Enriching internal context before the external pull is complete produces irrelevant or stale enrichment (you can't enrich what you haven't seen). Mitigation: enforce step ordering structurally — step 5 cannot start until step 4 returns or fails.

- **Window-edge race conditions.** A tick that arrives at a window boundary may classify ambiguously. Mitigation: define windows as half-open intervals `[start, end)`; deterministic classification from `anchor_time`.

- **Duplicate-check skipped under load.** Skipping the duplicate check to "save time" produces repeated messages — the most common fatigue trigger. Mitigation: the duplicate check is mandatory; treat its failure as a halt condition, not a skippable optimization.

## Contract

### Preconditions
A reliable time source is available (system clock or API response) — the skill establishes its own anchor and does not trust caller-supplied timestamps. A briefings table (or equivalent log store) is readable and writable for the current `anchor_date`. The closed enums for time windows (5 values) and briefing types (7 values) are defined before invocation. At least one delivery channel (Telegram, Discord, or equivalent) is configured. A cron or scheduler is invoking the skill at a cadence finer than the smallest time window.

### Invariants
The loop terminates per tick — it is never long-running. `anchor_date` and `anchor_time` are established as the first action of every invocation; no date arithmetic uses vague terms ("recently", "today" without anchor). A briefing is delivered on a given (anchor_date, briefing_type) pair at most once — the duplicate check is mandatory before delivery. External data is fetched before internal enrichment, never after. Silence is a valid output: if the time window has no scheduled briefing or the duplicate check matches, the tick exits without delivery. Every delivery produces a corresponding log entry; no delivery without logging.

### Governance
Owner: the human consumer of the briefings, who defines time windows, briefing types, and channel preferences. The skill does not modify its own enums or schedule during execution. The briefings log is the single source of truth for what has been delivered — corruption of the log breaks the deduplication invariant and must be recovered from backups before the loop resumes. Channel tool credentials are caller-owned. If the skill is deployed in a multi-user context, the briefings log must be partitioned per consumer.

### Recovery
If the date anchor cannot be established (clock unavailable, API failure): halt the tick; do not deliver; emit a diagnostic. If the briefings table is unreadable: halt the tick; do not deliver (delivering blind risks duplicates). If external data fetch fails: degrade gracefully — deliver an internal-only briefing with an explicit note that external data was unavailable, OR skip the tick if the briefing type is external-data-required (e.g., `pre_meeting`). If the channel tool fails: log the intended delivery; retry on the next tick if the briefing is still time-window-valid; do not retry indefinitely. If notification fatigue is detected (consumer mutes channel or sets a quiet flag): suppress non-critical briefing types until the flag is cleared.
