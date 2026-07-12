---
name: The Folder Structure That Makes AI Build Better Software
source_type: Video
status: Done
key_takeaways: 'Alex Brockway (AI Code That Works) on the project-on-disk skeleton as the real

  infrastructure: a thin root CLAUDE.md that routes rather than contains (a task-to-file

  table, max ~200 lines), a rules layer (.claude/), a knowledge layer (one reference

  file of decided facts), and a documentation layer split by LIFESPAN, not topic —

  active / decisions / reference / archive — because stale plans left in the active pile

  confidently steer agents at already-hit targets ("stale docs are worse than no docs").

  Archive gets stamped "do not follow"; decision records freeze the why in ~90 seconds.

  Two named failure duals: the drowning problem (knowledge-dump root file) and

  over-fragmentation (400 tiny files). Standing rule: the agent asks before editing the

  root CLAUDE.md itself.'
relevance: High
added_by: Nick
tags:
- context-engineering
- claude-code
- vault-architecture
url: https://www.youtube.com/watch?v=RQckIBzOCsA
authority:
- ai-code-that-works.md
findings:
- docs-split-by-lifespan-not-topic.md
- root-context-file-edit-guard.md
- claudemd-as-knowledge-base-traversal-guide.md
- intent-based-meta-routing-skill.md
- skills-as-pointers-to-second-brain-files.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-06-21'
---

# The Folder Structure That Makes AI Build Better Software

Production stance ("real companies run on software that I built"): you don't fix
context failures with a smarter model, you fix them with structure the AI walks
deterministically. Both context failure modes — dumping everything (drowning) and
giving nothing (guessing) — are killed by a thin router plus three pointed-to layers.

Note for the pipeline: the docs-lifecycle deltas to /maintain-docs and engine CLAUDE.md
conventions are future Nick-gated work — captured here as KB findings only.

Pass 2 deep extraction completed from full transcript (360 segments, 14:24).
