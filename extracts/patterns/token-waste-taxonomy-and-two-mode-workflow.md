---
title: "Token Waste Taxonomy and Two-Mode Workflow"
type: "extracted-artifact"
assigned_form: "pattern"
source_finding: "token-waste-taxonomy-and-two-mode-workflow"
confidence: "HIGH"
tier: "auto"
reason_codes: []
co_occurrence: null
extraction_date: "2026-04-19"
identification_report: "2026-04-19-identification-report-3.md"
deployed: false
deployed_to: null
contract:
  preconditions: "Agent workflows involve multi-turn conversations with tool access. Token consumption is measurable or estimable per session. The workflow involves both information-gathering and execution phases, even if not currently separated."
  invariants: "Gather-mode threads are short (10-15 turns maximum) and disposable -- they are never carried forward into focus mode as raw context. Focus-mode sessions start fresh with pre-processed, synthesized context only. Raw PDFs are never ingested directly into agent context -- they are pre-processed into compressed markdown first. Unused plugins/tools are periodically audited and removed."
  governance: "Owned by Meta-System knowledge layer. Waste taxonomy categories and mode separation heuristics are reviewed when new tool types or context sources are added. Modifications require a Design Decision."
  recovery: "If gather/focus separation loses cross-thread insights, create an explicit synthesis step between modes that captures key findings in structured format. If PDF pre-processing strips needed formatting or tables, retain the original alongside the compressed version for targeted re-reads. If context budget is exceeded mid-session, start a new focus-mode session with a tighter context selection rather than continuing in a bloated session."
tags:
  - "extracted-artifact"
  - "pattern"
---

# Token Waste Taxonomy and Two-Mode Workflow

**Source:** [[token-waste-taxonomy-and-two-mode-workflow]]
**Form:** pattern
**Extraction date:** 2026-04-19

## Problem

Agent sessions routinely consume 5-10x the tokens necessary for their task. Waste compounds silently: raw PDF ingestion (100K tokens vs. 5K pre-processed), conversation sprawl past 30 turns, unused plugin overhead (66K tokens per session), and accumulated context junk all inflate token budgets without improving output quality. Users on subscription models burn daily limits in 90 minutes; usage-based users accumulate unnecessary cost. The waste patterns originate from habits formed with simpler chat interfaces and persist because token consumption is invisible during interaction.

## Forces

- **Convenience vs. efficiency.** Dumping a raw PDF into context is easy; pre-processing it into compressed markdown requires an extra step but saves 20x the tokens.
- **Continuity vs. freshness.** Long conversations maintain shared context, but past turn 15-20 the accumulated context degrades performance and inflates cost. Starting fresh loses context but resets the token budget.
- **Tool availability vs. tool overhead.** Having many plugins/tools available feels productive, but each unused tool still consumes tokens in every system prompt. Periodic auditing is boring but necessary.
- **Gathering vs. executing.** Research and execution are cognitively distinct modes that benefit from different context strategies, but separating them requires discipline and an explicit synthesis step.

## Solution

Apply a **five-category waste taxonomy** to identify token waste, then adopt a **two-mode workflow** (Gather/Focus) to structurally prevent waste from accumulating.

**Waste Taxonomy:**

1. **Raw document ingestion.** PDFs, large files, and unprocessed documents dumped directly into context. Fix: pre-process into compressed markdown summaries before ingestion (20x token reduction).

2. **Conversation sprawl.** Sessions that extend past 30 turns accumulate stale context, off-topic tangents, and abandoned reasoning paths. Fix: start new conversations every 10-15 turns.

3. **Plugin/tool overhead.** Enabled tools that are never invoked still consume token budget in every system prompt message. Fix: periodic plugin audits -- disable tools enabled months ago but never used.

4. **Model mixing waste.** Unnecessary switching between models mid-task, re-establishing context each time. Fix: choose the right model for the task upfront; do not escalate mid-conversation.

5. **Accumulated context junk.** Prior turns that are no longer relevant but remain in the context window. Fix: fresh sessions with curated context rather than continuing in polluted sessions.

**Two-Mode Workflow:**

- **Gather mode.** Short, disposable threads (5-10 turns each) focused on information collection. Multiple gather threads may run in parallel on different aspects of a question. Output: concise, structured notes -- not raw conversation.

- **Focus mode.** A fresh session that starts with pre-processed, synthesized context from gather mode. No raw PDFs, no prior conversation history, no unused tools. This is the execution session where the actual work happens.

The transition between modes is an explicit **synthesis step**: the user (or an automated process) distills gather-mode outputs into a compact context package before starting the focus-mode session.

**Diagnostic:** The "Stupid Button" -- a 6-question self-audit: (1) Am I past 15 turns? (2) Did I dump a raw PDF? (3) Are unused plugins loaded? (4) Did I switch models mid-task? (5) Is my context full of stale turns? (6) Could I restart with a 5-bullet summary? If any answer is yes, waste is present.

## Consequences

**Positive:**
- 10x cost reduction reported by practitioners applying the full pattern ($8-10 per sloppy session vs. ~$1 per clean session).
- Subscription users who apply the pattern "forget limits exist" -- daily limits are no longer a constraint.
- Gather/focus separation aligns with natural cognitive modes (research vs. execution), improving both phases.
- Periodic plugin audits surface dead tool integrations that were consuming budget invisibly.

**Negative:**
- Gather/focus separation can lose cross-thread insights when the synthesis step is sloppy or skipped.
- PDF pre-processing may strip formatting, tables, or layout information needed for accurate analysis.
- The 10-15 turn heuristic is approximate -- some tasks legitimately require longer conversations, and premature session breaks interrupt flow.
- The pattern requires discipline to maintain. Without periodic self-audits, waste patterns silently return.

## Known Uses

- **Nate B Jones workflow optimization.** Documents 10x cost reduction from applying these patterns across Claude usage. The waste taxonomy and two-mode workflow are derived from his published methodology.
- **MetaSystem session boundaries.** MetaSystem already uses session boundaries and handoff prompts, which are a partial implementation of the gather/focus separation. The explicit waste taxonomy and self-audit diagnostic are not yet adopted.
- **Claude Code `/context` command.** Built-in command that audits loaded context and identifies waste -- a tool-level implementation of the diagnostic concept.

## Contract

### Preconditions

- Agent workflows involve multi-turn conversations with tool access.
- Token consumption is measurable or estimable per session.
- The workflow involves both information-gathering and execution phases, even if not currently separated.

### Invariants

- Gather-mode threads are short (10-15 turns maximum) and disposable -- they are never carried forward into focus mode as raw context.
- Focus-mode sessions start fresh with pre-processed, synthesized context only.
- Raw PDFs are never ingested directly into agent context -- they are pre-processed into compressed markdown first.
- Unused plugins/tools are periodically audited and removed from active sessions.

### Governance

- Owned by Meta-System knowledge layer.
- Waste taxonomy categories and mode separation heuristics are reviewed when new tool types or context sources are added.
- Modifications require a Design Decision.

### Recovery

- If gather/focus separation loses cross-thread insights, create an explicit synthesis step between modes that captures key findings in structured format before discarding gather threads.
- If PDF pre-processing strips needed formatting or tables, retain the original alongside the compressed version for targeted re-reads of specific sections.
- If context budget is exceeded mid-session, start a new focus-mode session with a tighter context selection rather than continuing in a bloated session.
- If the self-audit diagnostic is skipped repeatedly, automate it as a session-start check that surfaces waste indicators before work begins.
