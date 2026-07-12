---
name: I Built a Deck With AI, Then Made a Second AI Attack It
source_type: Video
status: Done
key_takeaways: 'Third independent corroboration of generator-assessor separation (IL rule 10), applied to

  office-document knowledge work, with three genuine deltas. (1) Enumerate-don''t-fix

  hostile-reviewer prompt: "identify claims without source attribution, numbers without a

  data source, charts whose data isn''t traceable, formulas inconsistent across parallel

  rows, assumptions presented as facts. Produce a written list. Don''t fix anything, just

  enumerate" — flipping the task from generation to enumeration is what makes a model catch

  its own class of mistakes. (2) Cross-vendor adversarial build/attack loop: Codex builds,

  Opus 4.7 hostile-reviews and generates an edit list, Codex fixes, Opus re-checks —

  iterated Ralph-loop style, with a terminal language-polish pass (Opus strips LLM-isms)

  only at the end. (3) Task risk gradient calibrates verification depth: low risk =

  formatting/layout/chart drafts/wording; medium = source attribution, data extraction;

  high = numerical synthesis, financial calculations, regulatory language, claims that

  travel to leadership. Wrapped in a four-stage workflow: source prep (evidence inventory)

  -> file spec -> constrained build -> hostile verification.'
relevance: High
added_by: Nick
tags:
- evaluation
- multi-agent
- prompt-engineering
url: https://www.youtube.com/watch?v=MFzxIT88zfg
authority:
- nate-b-jones.md
findings:
- enumerate-dont-fix-hostile-reviewer-prompt.md
- cross-vendor-adversarial-build-attack-loop.md
- task-risk-gradient-for-verification-depth.md
- generator-assessor-separation-in-skill-iteration.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-05-27'
---

# I Built a Deck With AI, Then Made a Second AI Attack It (Nate B Jones)

Pass 2 extraction completed 2026-07-12 (session 136) from the full transcript
(`app/transcript-fetcher/transcripts/MFzxIT88zfg.md`). Logged as the third external
corroboration on the generator-assessor-separation finding (a /reassess-priorities
evidence-strength candidate); the three deltas are extracted as their own findings.
