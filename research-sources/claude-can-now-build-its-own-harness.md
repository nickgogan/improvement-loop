---
name: Claude Can Now Build Its Own Harness... For Every Task
source_type: Video
status: Done
key_takeaways: 'Digest of an Anthropic first-party blog on dynamic workflows: with Opus 4.8, Claude can

  author a task-custom harness at runtime (a JavaScript file with agent/parallel/pipeline

  primitives, per-agent model choice, optional worktrees, resumability) instead of forcing

  every job through the one coding-shaped harness. Anthropic names six composition

  patterns the model uses: classify-and-act, fan-out+synthesize, worker-critic,

  generate-and-filter, tournament, loop-until-done. Notable specifics: pairwise tournament

  judging beats absolute scoring; loop-until-done cures agentic laziness; harnesses persist

  as reusable saved artifacts; token cost caps can be set in the prompt; the "workflow"

  trigger keyword misfires on ordinary uses of the word. Secondhand evidence — the primary

  Anthropic dynamic-workflows blog fetch is queued as a follow-up.'
relevance: High
added_by: Nick
tags:
- orchestration
- multi-agent
- claude-code
- evaluation
- tools
url: https://www.youtube.com/watch?v=l5rae4LMKBc
authority:
- prompt-engineering-channel.md
findings:
- frontier-model-as-harness-designer.md
- harness-composition-six-pattern-taxonomy.md
- pairwise-tournament-judging-over-absolute-scoring.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-06-03'
---

Session-136 Pass 2 deep extraction from the full transcript
(`app/transcript-fetcher/transcripts/l5rae4LMKBc.md`). KB-ONLY verdict from the
2026-07-12 link-intake triage (harness/infrastructure cluster). The video is a digest of
an Anthropic first-party blog post on dynamic workflows — all Anthropic claims here are
secondhand until the primary blog is ingested (follow-up queued in the triage report).
The channel's claimed non-coding examples (resume ranking, business-plan attack,
Slack root-cause mining, session-history → CLAUDE.md rule mining) are attributed to the
Anthropic post but unverified against it.
