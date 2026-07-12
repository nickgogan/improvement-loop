---
name: Nate B Jones — GLM 5.2 Is Free And Beats Claude On Most Work. So Why Can't Companies Switch?
source_type: Video
status: Done
key_takeaways: 'Model switching is not swapping a model call — it''s replacing a whole work system.

  Lindy (Flo Crivello) publicly rewrote their harness from scratch to move from Claude to

  a DeepSeek architecture: prompts, memory handling, tool calls — no lift-and-shift. The

  model-strategy question companies fail to ask: is your task load center-of-distribution

  (open/cheap models at parity or better — GLM 5.2 framed as best-in-class there, ~98%

  cheaper than Claude, free self-hosted) or edge-of-distribution (frontier models still

  separate)? Vendor harness dynamics: GLM 5.2 shipped its own Codex-clone harness; Codex

  markets itself as a model-independent harness; Claude Tag is a team-level harness that

  creates context lock-in ("renting your company brain back").'
relevance: High
added_by: Nick
tags:
- model-capability
- harness-design
- model-routing
- open-source-models
url: https://www.youtube.com/watch?v=Zp8lr6IzUnQ
authority:
- nate-b-jones.md
findings:
- center-vs-edge-of-distribution-task-classification.md
- harness-non-portability-across-model-families.md
- no-mid-session-model-switching-subagent-handoff.md
- model-specific-context-file-sensitivity.md
- provider-adaptive-prompt-rendering.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-06-28'
---

Session-136 Pass 2 deep extraction (link-intake wave 2, Models/economics cluster).
Transcript: `app/transcript-fetcher/transcripts/Zp8lr6IzUnQ.md`. First half of the
Nate-Jones econ pair (with `you-cant-compete-on-cheap-models-anymore.md`) — one
model-strategy framework across two videos: center/edge task classification as the
routing input, harness non-portability as the switching cost. The Lindy harness-rewrite
evidence is the strongest practitioner corroboration yet for the KB's skill↔model
coupling findings and was annotated onto them. Registry-relevant GLM 5.2 datapoints
captured in the linked findings (registry writes are Nick-gated).
