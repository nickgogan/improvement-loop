---
title: "Compounding Knowledge Loop"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "compounding-knowledge-loop-internal-data"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Agent sessions produce structured logs; a promotion mechanism exists to move session-level insights into a persistent, queryable knowledge store."
  invariants: "Every session both consumes and produces knowledge; promoted entries pass a quality gate before entering the canonical store."
  governance: "Promotion criteria are explicit; the canonical store has an owner responsible for pruning and conflict resolution."
  recovery: "If the canonical store becomes corrupted or contradictory, a human review pass can freeze promotion, audit entries, and prune conflicting items."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Compounding Knowledge Loop

**Source:** [[compounding-knowledge-loop-internal-data]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent sessions generate valuable insights -- architectural decisions, debugging strategies, domain-specific patterns -- that are lost when the session ends. Subsequent sessions start from zero, repeating mistakes and rediscovering solutions. Manual curation of session knowledge does not scale across many sessions and projects.

## Forces

- **Ephemeral context:** Agent conversations are discarded after each session. Valuable reasoning evaporates.
- **Manual curation cost:** A human reviewing and filing every session's insights is effective but unsustainable at scale.
- **Signal-to-noise ratio:** Most session content is operational noise (tool calls, retries, dead ends). Only a fraction contains genuinely novel insights worth preserving.
- **Contradiction risk:** Later sessions may produce insights that contradict earlier ones. Without conflict detection, the knowledge store drifts into inconsistency.
- **Cold-start problem:** The loop only compounds if sessions actually query the knowledge store. If the store is not wired into the agent's context, it is write-only and useless.

## Solution

Build a self-reinforcing cycle where each agent session both reads from and writes to a persistent knowledge store:

1. **Consume:** At session start, the agent queries the knowledge store for entries relevant to the current task (project, domain, tool, pattern).
2. **Produce:** At session end (or via hooks during the session), the agent summarizes novel insights from the conversation into a structured session log.
3. **Promote:** A periodic process (daily flush, manual review, or automated quality gate) evaluates session log entries and promotes high-quality items into the canonical knowledge store (wiki, findings database, memory file).
4. **Compound:** Future sessions query the now-richer store, producing better work, which generates better insights, which further enriches the store.

**Key mechanisms:**
- Session logs are structured (not raw conversation dumps) so they can be filtered and deduplicated.
- Promotion has a quality gate -- not everything gets promoted. This prevents garbage accumulation.
- The canonical store is queryable by topic, project, or pattern -- not a flat append-only log.
- Conflict detection flags when new entries contradict existing ones, requiring human resolution.

## Consequences

**Positive:**
- Knowledge compounds automatically. Each session is incrementally better than the last without manual effort.
- Institutional memory survives across sessions, agents, and team members.
- The pattern is self-reinforcing: better knowledge leads to better sessions, which produce better knowledge.

**Negative:**
- Garbage-in-garbage-out: if session quality is low, the store accumulates noise rather than signal.
- Knowledge drift: contradictory information can accumulate if conflict detection is absent or weak.
- Store bloat: without periodic pruning, the canonical store grows unboundedly, eventually degrading retrieval quality.
- The compounding effect assumes sessions produce genuinely novel insights -- repetitive sessions add volume without value.

## Known Uses

- **Cole Medin's self-evolving memory system** -- Working implementation where agent conversations are summarized, promoted to a structured wiki via hooks and daily flush, and queried by future sessions. Measurable improvement in session quality over time.
- **MetaSystem research-loop** -- Implements this pattern for external research data: sources are extracted into findings, findings are promoted into patterns, patterns are deployed into agent context. The internal-data variant (applying this to session decisions and lessons) is the natural next step.
- **Karpathy's external-data KB architecture** -- The foundational pattern of structured extraction from unstructured sources into a queryable knowledge base, applied here to internal session data rather than external documents.

## Contract

### Preconditions
- Agent sessions produce structured logs (not raw conversation dumps).
- A promotion mechanism exists to move session-level insights into a persistent, queryable knowledge store.
- The knowledge store is wired into the agent's context at session start so it is actually consumed.

### Invariants
- Every session both consumes from and produces to the knowledge pipeline. The loop is bidirectional.
- Promoted entries pass a quality gate before entering the canonical store. No automatic promotion without filtering.
- The canonical store remains queryable and navigable as it grows. Retrieval quality does not degrade with volume.

### Governance
- Promotion criteria are explicit and documented.
- The canonical store has a designated owner responsible for periodic pruning, conflict resolution, and quality audits.
- Metrics on knowledge utilization rate (how often entries are actually queried and used) are tracked to detect write-only stores.

### Recovery
- If the canonical store becomes contradictory, a human review pass can freeze promotion, audit conflicting entries, and prune or reconcile them.
- If store bloat degrades retrieval quality, a pruning pass removes low-utilization entries.
- If the promotion pipeline breaks (hooks fail, flush stalls), session logs accumulate but are not lost -- they can be batch-promoted once the pipeline is restored.
