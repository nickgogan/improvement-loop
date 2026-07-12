---
name: How to Distill Claude Fable 5
source_type: Video
status: Done
key_takeaways: 'Quantified counter-evidence on trace distillation: naive off-policy imitation of Fable 5

  traces made a Qwen3-4B student WORSE than its own base (tool-calling 99 -> 96; bug-fix

  19/30 -> 11/30) — "style transfers, genius does not." On-policy distillation (student

  attempts the task, teacher grades every token; Thinking Machines paper) reached 70% on a

  hard math benchmark at 1/10 the cost of full RL, up to 30x cheaper than naive imitation

  and 7-10x faster to train. Six-step recipe: capture, clean, format (ChatML), train

  (LoRA), quantize (4-bit GGUF), run (Ollama). Evidence-only for the Model dimension — the

  engine has no fine-tuning surface. Primary-paper verification pending.'
relevance: Medium
added_by: Nick
tags:
- evaluation
- claude-code
url: https://www.youtube.com/watch?v=qWhSFjDS3LA
authority:
- cloud-codes.md
findings:
- on-policy-vs-naive-trace-distillation.md
date_added: '2026-07-12'
date_processed: '2026-07-12'
date_published: '2026-07-05'
---

# How to Distill Claude Fable 5 (Cloud Codes)

Pass 2 extraction completed 2026-07-12 (session 136) from the full transcript
(`app/transcript-fetcher/transcripts/qWhSFjDS3LA.md`). Channel: Cloud Codes — no
authority entry yet (flagged for Researcher follow-up). Narrative framing (government
shutdown story) treated as unverified color; only the distillation mechanics and
benchmark numbers were extracted, with primary-paper verification flagged.
