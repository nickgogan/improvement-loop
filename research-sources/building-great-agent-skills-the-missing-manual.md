---
name: 'Building Great Agent Skills: The Missing Manual (Matt Pocock @ AI Engineer)'
source_type: Video
status: Done
key_takeaways: 'Pocock''s four-part skill-audit checklist — trigger, structure, steering, pruning — shipped

  as a "writing great skills" meta-skill in his repo. Trigger: user-invoked vs model-invoked

  is a real tradeoff (context load on the agent vs cognitive load on the user); user-invoked

  removes triggering unpredictability and the need for triggering evals. Structure: skills

  decompose into steps + reference; enumerate the skill''s branches and move reference

  material used on only some branches behind context pointers (external references).

  Steering: leading words — high-prior-density phrases repeated consistently, verified by

  watching the phrase echo in the agent''s reasoning traces; plus leg-work amplification by

  splitting multi-phase skills so the agent sees one step at a time (hides the future goal

  that causes eager underinvestment, e.g. plan mode''s shallow clarifying questions).

  Pruning: massive skills are a symptom; failure modes are duplication (single source of

  truth per part), sediment (accreted contributions nobody dares delete), and no-ops

  (paragraphs whose deletion wouldn''t change behavior — the deletion test).'
relevance: High
added_by: Nick
tags:
- skills
- prompt-engineering
- claude-code
url: https://www.youtube.com/watch?v=UNzCG3lw6O0
authority:
- matt-pocock.md
findings:
- leading-words-lexical-steering-reasoning-trace-verification.md
- branch-analysis-externalization-rule-skill-reference.md
- leg-work-amplification-hiding-future-steps.md
- skill-pruning-failure-modes-noop-deletion-test.md
- skill-invocation-control-side-effect-guard.md
- meta-skill-for-skill-authorship.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-06-29'
---

Session-136 Pass-2 extraction (link-intake wave 2). Transcript:
`app/transcript-fetcher/transcripts/UNzCG3lw6O0.md`. Processed as one cluster with
`pocock-skills-v1-1-wayfinder-research-implement.md` — shared patterns extracted once,
multi-sourced; the 07-08 v1.1 video's applied-evidence framing leads where they overlap,
this talk remains lineage. The checklist maps nearly 1:1 onto what the engine's
`/assess-skill` and `/design-skill` check — rubric-relevant findings flagged P2 for the
restructure program's Nick-gated Phase-2 substrate pass.
