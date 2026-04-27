---
title: "Compounding Knowledge Loops Must Encode Outcomes"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "compounding-knowledge-loop-internal-data"
identification_report: "building-agentic-systems.harvest-queue.md::compounding-knowledge-loop-internal-data::rule::compounding-loops-must-encode-outcomes"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "teams building a self-improving knowledge layer on top of agent session data"
    - "operators of memory or wiki systems that promote session summaries into a queryable store"
    - "designers of any feedback loop that intends to compound — e.g., personal knowledge bases, team retrospectives, agent memory architectures"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "low — once a loop has been running without outcome encoding, retroactive backfill is expensive and often impractical; the schema decision is effectively irreversible without a clean reset"
  auditability: "high when entries are inspected for the three required fields and outcome verification is tagged; low when the schema is free-form prose without explicit fields"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Cole Medin demonstrated a working compounding-loop implementation; the corroborating world-models source (2026-04-20) names outcome encoding as the gap most implementations skip. No known production deployment as of extraction has the outcome field as a hard schema requirement."
contract:
  preconditions: "A system is implementing or operating a knowledge loop that promotes session-derived content into a queryable store consumed by future sessions. There exists a promotion step (automated or manual) where session data becomes a knowledge-store entry. The loop's stated goal is compounding improvement, not just searchable history."
  invariants: "Every promoted entry carries event, action, and outcome. Entries missing the outcome field are not treated as compounding-loop content — they may be retained as raw history but are not surfaced to future sessions as compiled knowledge. Outcome quality (verified vs. speculative) is preserved as metadata so consumers can weight accordingly."
  governance: "Owner: the team or operator responsible for the knowledge-loop architecture and its ingestion schema. The required-outcome field must be encoded in the schema or template, not delegated to author discipline. Exemption (entries promoted without outcomes) requires an explicit reason and a backfill plan with a deadline."
  recovery: "If outcomes are systematically missing, halt promotion and audit the upstream capture workflow — the problem is upstream, not at the schema. If a deployed loop is found to lack outcome encoding, do not retroactively claim compounding benefits; document the gap, retrofit the schema, and treat the loop's compounding clock as restarting from the schema-fix date. If outcomes are present but low-quality (rumored, unverified), introduce confidence tags and downgrade query weight rather than purging entries."
tags:
  - "extracted-artifact"
  - "rule"
---

# Compounding Knowledge Loops Must Encode Outcomes

**Source:** [[compounding-knowledge-loop-internal-data]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A system is implementing a compounding knowledge loop: agent session data (conversations, decisions, work logs) is captured, summarized, promoted into a structured knowledge store, and queried by future sessions with the intent that knowledge accumulates and session quality improves over time. The loop is intended to compound — to make month six measurably better than month one.

## Action

**Required:** Each entry promoted into the knowledge store must encode three elements: (1) **event** — what happened, (2) **action** — what was done about it, and (3) **outcome** — what resulted. The third element is mandatory, not optional. The schema or template used by the loop must require an outcome field, and entries missing an outcome are either not promoted or flagged for outcome backfill.

**Forbidden:** Promoting entries that record only events, or only events plus actions, into the knowledge store and calling that loop a compounding loop. Treating session logs that capture "what we discussed" without "what resulted" as sufficient for the loop. Relying on implicit outcome inference ("presumably it worked, since no follow-up issue was filed").

## Boundary

Enforced at the promotion boundary — wherever session-level data is converted into knowledge-store entries (daily flush, end-of-session summarizer, hook-driven ingestion). Applies to every entry the loop emits. Does not apply to raw session transcripts retained for audit-only purposes; those may lack outcomes if they are not consumed by future sessions.

## Enforcement

- **Mechanism:** The knowledge-store entry schema includes a required `outcome` field (or equivalent — `result`, `effect`, `what-happened-after`). Promotion logic rejects or defers entries with missing/empty outcomes.
- **Check (deterministic):** `(entry.event != null) AND (entry.action != null) AND (entry.outcome != null AND entry.outcome != "")` — any branch false → entry is not promoted, or is promoted into a quarantine for outcome backfill.
- **Violation response:**
  - *Outcome unknown at promotion time:* park the entry in a backfill queue with a deadline; if the deadline passes without an outcome, downgrade the entry's queryable status.
  - *Systemic outcome absence (many entries missing outcomes):* treat the loop as broken, not just incomplete; the upstream capture workflow does not produce outcome data and must be redesigned before further promotion.
  - *Outcomes that are speculative or unverified:* mark the outcome field with a confidence/provenance tag so downstream queries can filter.

## Rationale

A knowledge base records what happened. A world model — and a compounding loop is functionally a world model — must record what happened, what was done, and what resulted. Without the third element, the loop replays past events without learning from their consequences, and month six looks like month one. The outcome element is also where most implementations fail: outcomes do not encode themselves; someone or some workflow must close the loop between action and result. This requires both a schema that demands the field and an organizational willingness to record results honestly, including failures. The corroborating finding (world-models-orgs-three-architectures, 2026-04-20) names this gap as the primary reason compounding fails to materialize in practice.

This rule is the positive-space reformulation of a known anti-pattern (event-only logging that masquerades as a learning system). One invariant — three required elements — bounds enforcement without enumerating an open set of failure modes.

## Failure Modes

- **Outcome field becomes intent restatement.** Writer fills the outcome slot with "implemented as planned" — restating the action rather than measuring its consequence. Mitigation: audit sampling distinguishes intent-restatement from genuine outcome; templates explicitly warn against this pattern; reviewers trained to push back on intent-shaped outcomes.
- **Outcome unknown at promotion time.** Many actions produce results only after the writer has moved on (deployment effects, downstream behavior changes). Mitigation: defer-with-deadline pattern — entry is parked with `outcome: pending [date]`; if the deadline passes without backfill, the entry is downgraded out of the compounding query path.
- **Honest failure-recording erodes over time.** Early entries record failures honestly; later entries omit them as the team becomes invested in the loop's success narrative. Mitigation: monitor recorded failure rates as a health metric; a sudden drop is a warning sign, not a success signal.
- **Free-text outcome permits infinite vagueness.** "Worked well" is not an outcome. Mitigation: schema includes structured sub-fields where applicable (success/failure/partial, measurable signal, time-to-effect, confidence tag).
- **Observational exemption gets over-applied.** Operators mark entries as observational to bypass the outcome requirement. Mitigation: observational exemption requires explicit "no action was taken" justification; entries that record an action cannot claim observational status.
- **Speculative outcomes treated as verified.** "Presumably it worked, since no follow-up issue was filed" is not an outcome — it's an absence of contradicting signal. Mitigation: confidence/provenance tags mandatory on outcome entries; queries can filter by confidence so speculative outcomes don't compound as fact.
- **Wiki bloat without pruning.** Outcome encoding makes entries longer; combined with no pruning, the store becomes unsearchable. Mitigation: outcome encoding does not exempt the loop from periodic pruning of stale or contradicted entries.

## Contract

### Preconditions
A system is implementing or operating a knowledge loop that promotes session-derived content into a queryable store consumed by future sessions. There exists a promotion step (automated or manual) where session data becomes a knowledge-store entry. The loop's stated goal is compounding improvement, not just searchable history.

### Invariants
Every promoted entry carries event, action, and outcome. Entries missing the outcome field are not treated as compounding-loop content — they may be retained as raw history but are not surfaced to future sessions as compiled knowledge. Outcome quality (verified vs. speculative) is preserved as metadata so consumers can weight accordingly.

### Governance
Owner: the team or operator responsible for the knowledge-loop architecture and its ingestion schema. The required-outcome field must be encoded in the schema or template, not delegated to author discipline. Exemption (entries promoted without outcomes) requires an explicit reason and a backfill plan with a deadline.

### Recovery
If outcomes are systematically missing, halt promotion and audit the upstream capture workflow — the problem is upstream, not at the schema. If a deployed loop is found to lack outcome encoding, do not retroactively claim compounding benefits; document the gap, retrofit the schema, and treat the loop's compounding clock as restarting from the schema-fix date. If outcomes are present but low-quality (rumored, unverified), introduce confidence tags and downgrade query weight rather than purging entries.
