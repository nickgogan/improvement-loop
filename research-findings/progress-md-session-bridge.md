---
notion_id: 32b1e08b-9b34-812a-a24f-dc7a20c41c0c
name: PROGRESS.md Session Bridge
summary: A markdown file Claude Code reads at session start and writes at session end, maintaining what was done, what's in progress, what's blocked, and what's next across sessions.
implementation_notes: null
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Partially Adopted
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in:
- S3 (Claude Code Build)
sources:
- claude-code-works-better-when-you-do-this.md
- anthropic-long-running-claude-scientific-computing.md
- anthropic-effective-harnesses-long-running-agents.md
- anthropic-building-c-compiler.md
related_findings:
- file: gsd-global-learnings-store-cross-session-persistence.md
  rel: extended-by
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: extended-by
proposals: null
date_discovered: '2026-03-15'
last_updated: 2026-04-09
pipeline_status: raw
consumed_by: []
---
# PROGRESS.md Session Bridge

## What It Is
PROGRESS.md is a structured markdown file that serves as persistent working memory between Claude Code sessions. At session start, the agent reads it to orient itself; at session end, it writes an updated summary covering what was completed, what is in progress, what is blocked, and what comes next. The file acts as a handoff note from one session to the next.

## Why It Matters
Claude Code has no native memory across sessions. Without a bridge file, each session starts cold — the agent must rediscover context from code state alone, which is slow and error-prone. PROGRESS.md collapses that ramp-up time and preserves decision rationale that isn't visible in the file system.

## Why People Are Using It
Identified as an essential pattern in 12 of 14 practitioner videos reviewed. The pattern is already designed into the vault architecture with a template created, though not yet deployed to GitHub. Its prevalence across independent practitioners signals strong convergent discovery.

## Potential Improvements
The format could be enriched with structured sections (e.g., decisions made, assumptions in play, known risks) to make the handoff more queryable. Integration with a task management system or automated verification against actual file state would reduce drift.

## Potential Failure Modes
Session summaries can diverge from reality if the agent writes optimistic or incomplete updates. If PROGRESS.md is not verified against actual file state, stale entries accumulate and mislead future sessions. The pattern also breaks down if the agent is interrupted mid-session before writing the closing update.

---

## April 2026 Update

**Claude Code now has official memory infrastructure** (March 2026) that directly relates to this pattern:
- **Custom auto-memory directory**: Configurable location for memory files; PROGRESS.md can now be placed in the designated auto-memory directory for automatic ingestion at session start
- **Timestamps on memory files**: Claude Code now attaches timestamps to memory file reads/writes, enabling temporal ordering of session summaries and drift detection
- **Memory leak fixes**: Prior issues where old memory files were never pruned have been addressed

**The `/loop` command creates a new session continuity challenge:** Recurring tasks created with `/loop` pick up context from prior runs, but the mechanism for this context inheritance is different from the PROGRESS.md handoff pattern. The loop's context is implicit (prior tool call history); PROGRESS.md provides explicit structured summary.

**Cloud Scheduled Tasks create the most significant evolution problem:** When a task runs while the machine is off (cloud-scheduled), it cannot read a local PROGRESS.md. This means PROGRESS.md-style continuity for cloud tasks requires the bridge file to live in a cloud-accessible location (e.g., the repo itself, or a Notion page). This is the PROGRESS.md pattern's next evolution problem — cloud-native session memory.

**Recommendation:** Extend PROGRESS.md template to include explicit "Cloud Task Context" section for tasks that will run as Cloud Scheduled Tasks. Consider hosting the file in the git repo root so cloud tasks can access it.

**Source:** https://www.builder.io/blog/claude-code-updates

## CHANGELOG.md as Lab Notes (April 2026 — Anthropic Tier 1)
Anthropic's long-running Claude for scientific computing workflow uses CHANGELOG.md as long-term memory, acting as "lab notes" that log: current status, completed tasks, failed approaches (e.g., "Tried Tsit5 for perturbation ODE; too stiff, switched to Kvaerno5"), accuracy tables at checkpoints, and known limitations. This prevents re-attempting dead ends across sessions. The pattern is functionally equivalent to PROGRESS.md but oriented toward scientific/engineering work rather than project management. The dual-file pattern (CLAUDE.md for plan + CHANGELOG.md for history) provides a richer session bridge than PROGRESS.md alone — separating intent from narrative. Claude both reads and edits these files iteratively, refined through human-Claude consultation.
