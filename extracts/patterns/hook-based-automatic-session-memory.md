---
title: "Hook-Based Automatic Session Memory"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "claude-code-hooks-for-automatic-session-memory"
confidence: "MED"
tier: "guided"
reason_codes: []
co_occurrence: "skill"
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "The agent harness must support lifecycle hooks (session start, pre-compaction, session end). A writable local filesystem must be available for daily logs. A summarization mechanism (SDK call or local model) must be available at hook execution time."
  invariants: "Every session produces at least one structured log entry. Hook failures are logged and surfaced, never silently swallowed. Promotion from daily logs to the knowledge wiki requires a quality filter -- raw session chatter is never promoted directly."
  governance: "Owned by Meta-System knowledge layer. Hook configuration changes require review. Promotion logic (daily flush) must be auditable -- what was promoted, what was filtered, and why."
  recovery: "If a hook fails to fire, the session log entry is missing but no data is corrupted. Recovery is manual: review conversation history and backfill. If the daily flush promotes low-quality entries, quarantine and review the promotion filter criteria."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Hook-Based Automatic Session Memory

**Source:** [[claude-code-hooks-for-automatic-session-memory]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agentic coding sessions generate valuable knowledge -- decisions made, constraints discovered, approaches tried and abandoned -- but this knowledge is lost when the session ends. Manual session summaries (like PROGRESS.md updates) capture some of it, but they depend on human discipline, are inconsistent in format, and frequently omitted under time pressure. Over weeks of sessions, the accumulated knowledge loss is substantial: the agent re-derives solutions, forgets constraints, and the human repeats context that was already established.

## Forces

- **Capture completeness vs. noise.** Automated capture grabs everything, including low-value session chatter. Manual capture is selective but inconsistent.
- **Zero-effort vs. zero-quality.** Fully automated systems require no discipline but can promote garbage. Manual systems produce high-quality summaries but require effort that competes with actual work.
- **Immediacy vs. curation.** Session-end hooks capture while context is fresh, but raw captures need curation before they are useful as persistent knowledge. Delaying curation risks losing the context needed to curate well.
- **Compounding value vs. compounding noise.** Each session's memory makes subsequent sessions more effective -- but only if the accumulated memory is high-signal. Accumulated noise degrades performance.

## Solution

Use agent harness lifecycle hooks to automatically capture, structure, and promote session knowledge through a three-stage pipeline:

**Stage 1: Context Loading (session_start hook)**
On session start, inject the agent's system description (who it is, how its memory works) and a file index into context. This gives the agent meta-awareness of its own memory architecture, enabling it to reason about what to capture and where to retrieve.

**Stage 2: Structured Capture (pre_compact and session_end hooks)**
Before context compaction and at session end, fire a hook that sends the conversation to a summarization call (e.g., Claude Agent SDK). The output is a structured summary -- not a prose recap -- appended to a daily log file (e.g., `daily-logs/2026-04-19.md`). The summary should separate facts learned, decisions made, and open questions.

**Stage 3: Knowledge Promotion (daily flush)**
Once per day, a batch process reads accumulated daily log entries, extracts two categories -- **concepts** (standalone knowledge units) and **connections** (relationships between concepts) -- and promotes them to a persistent wiki structure (e.g., `wiki/concepts/` and `wiki/connections/`). This is the quality gate: only entries that meet a relevance threshold are promoted.

**Auxiliary benefit:** A post-session hook can auto-commit or auto-push to keep git status clean, which is itself a context optimization (dirty git status injects noise into every subsequent session).

## Consequences

**Positive:**
- Zero manual effort for session capture. Knowledge accumulates from normal work without changing workflows.
- Compounding memory: each session builds on prior sessions' captured knowledge.
- Structured daily logs provide an audit trail of what was learned and decided, session by session.
- Separation of capture (hooks) from curation (daily flush) allows different quality bars at each stage.

**Negative:**
- Hook failures silently lose data. If `session_end` fails to fire (crash, timeout, network issue), that session's knowledge is lost with no indication.
- Daily flush without human supervision can promote low-quality or contradictory entries into the wiki, degrading the knowledge base over time.
- Over-reliance on automated extraction misses nuance that requires human judgment -- implicit decisions, context-dependent reasoning, political or organizational factors.
- The summarization call itself costs tokens and adds latency to session end. For short sessions, the overhead may exceed the value captured.

## Known Uses

- **Cole Medin's claude-memory-compiler.** Open-source implementation (github.com/coleam00/claude-memory-compiler) demonstrating the three-hook pattern with Claude Code. Uses Claude Agent SDK for summarization, daily logs for capture, and wiki promotion for persistence.
- **Karpathy's gist prompt.** A one-shot setup prompt for configuring the hook-based memory system, referenced as a bootstrapping mechanism.
- **MetaSystem's PROGRESS.md.** A manual implementation of the same concept (session bridge document), demonstrating the need but not automating the capture.

## Contract

### Preconditions

- The agent harness must support lifecycle hooks at session start, pre-compaction, and session end.
- A writable local filesystem must be available for daily log files.
- A summarization mechanism (SDK call, local model, or deterministic extractor) must be available at hook execution time.
- The daily flush process must be schedulable (cron, manual trigger, or session-start check).

### Invariants

- Every session that runs to completion produces at least one structured log entry in the daily log.
- Hook failures are logged and surfaced to the user, never silently swallowed.
- Promotion from daily logs to the knowledge wiki requires a quality filter. Raw session chatter is never promoted directly.
- The wiki is append-only during automated promotion. Deletions and consolidations are human-initiated.

### Governance

- Owned by Meta-System knowledge layer.
- Hook configuration changes (what is captured, what triggers capture) require review.
- Promotion logic (daily flush filter criteria) must be auditable: what was promoted, what was filtered, and why.
- Wiki content promoted by automation is tagged as machine-generated until human-reviewed.

### Recovery

- If a hook fails to fire, the session log entry is missing but no data is corrupted. Recovery is manual: review conversation history and backfill the daily log.
- If the daily flush promotes low-quality entries, quarantine the affected wiki entries and review the promotion filter criteria before the next flush.
- If the wiki grows beyond a size budget, apply the Delta Updates pattern (consolidation via human review) rather than automated pruning.
