---
notion_id: 32b1e08b-9b34-816e-b025-e823496ee186
name: Five Context Management Techniques in Claude Code
summary: 'Five distinct techniques manage context in Claude Code, with different cost/quality tradeoffs: sub-agent (fresh window), /re context trimming (selective cut), compaction (lossy compression), /handoff
  + /clear (structured summary), and /clear (destructive reset at break points).'
implementation_notes: null
category: Context Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- your-ai-coding-is-bad-heres-how-to-fix-it.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: context-curation-over-context-stuffing.md
  rel: same-problem
- file: ace-delta-updates-over-monolithic-rewrites.md
  rel: same-problem
- file: agent-context-kiss-commandments-minimum-viable.md
  rel: same-problem
- file: ace-agentic-context-engineering-evolving-playbook.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Five Context Management Techniques in Claude Code

## What It Is
Roman documents five context management techniques in Claude Code: (1) Sub-agent spawn: creates a fresh context window for an isolated task — the cleanest option with no information loss. (2) /re (context trimming): selectively removes completed, irrelevant context without resetting the full conversation — requires careful manual selection. (3) Compaction: Claude Code's automatic context compression — the most common but least effective, causes significant information loss. (4) /handoff + /clear: user requests a structured handoff document containing specified information, then clears context — the most time-intensive but highest quality option, produces a precisely controlled summary. (5) /clear: complete context wipe — most destructive but often best if timed at good break points; can be combined with agents.md or CLAUDE.md to immediately re-orient the model. Preference order (best to worst): sub-agent > /handoff+/clear > context trimming > /clear > compaction.

## Why It Matters
Choosing the wrong context management technique at the wrong time is one of the most common sources of quality degradation in long agentic sessions. Most users rely on compaction by default and accept the resulting quality drop without knowing better options exist.

## Why People Are Using It
Each technique has a different time cost vs. quality tradeoff, making them suited to different points in a session. Sub-agents are fast but change the execution model; /handoff is slow but preserves quality.

## Potential Alternatives
External memory systems (episodic logs, vector DBs) as alternatives to in-context state. Persistent project state files updated incrementally.

## Potential Improvements
Automated context budget monitoring that recommends the appropriate technique based on current token usage and task type. Tooling to make /handoff structured and fast.

## Potential Failure Modes
Compaction at the wrong moment (mid-implementation rather than at a clean break point) causes irreversible information loss. /clear without a handoff document loses all implementation context. Sub-agents without clear scopes cause fragmented, unwired code.
