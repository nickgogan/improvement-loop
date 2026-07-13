---
name: "I Made GPT 5.6 and Fable 5 Build the Same App (RAW RESULTS)"
source_type: "Video"
status: "Done"
key_takeaways: |-
  One practitioner head-to-head — NOT a benchmark (n=1 per task, self-flagged buggy
  cost readouts). Same one-shot prompt to GPT-5.6 Soul (Codex) and Fable 5 (Claude
  Code) across three deployed builds: a Shots.so pixel-clone, a creative "mischief
  drop" site, and an underspecified NYC learning platform. Soul won on thoroughness,
  design fidelity, and literal staged-gate instruction-following at 3-6x Fable's
  wall-clock (clone: 2h51m/~$100 vs 30min/$12); Fable was fast but shallow on one-shot
  pixel fidelity. Side pattern: harness /cost and /usage readouts were inconsistent on
  subscription plans — he fell back to independent log-based accounting via
  `npx ccusage@latest session`. Registry note: this is the KB grounding for the
  model-capability registry's GPT-5.6 line — the registry should cite this source
  (registry not edited in this pass; claims must be KB-grounded, never invented).
relevance: "High"
added_by: "Nick"
tags:
  - "evaluation"
  - "claude-code"
  - "tools"
url: "https://www.youtube.com/watch?v=1njjOIiA8Kc"
authority:
  - "pat-simmons.md"
findings:
  - "gpt-56-soul-vs-fable-5-one-shot-head-to-head.md"
  - "harness-cost-readout-unreliability-independent-log-accounting.md"
date_added: "2026-07-13"
date_processed: "2026-07-13"
date_published: "2026-07-11"
---

Session-144 Pass 2 deep extraction (link-intake triage 2026-07-13, KB-ONLY verdict,
Nick-accepted). Transcript: `app/transcript-fetcher/transcripts/1njjOIiA8Kc.md`.

Evidence framing per the accepted gate: Anecdotal/Medium — "one practitioner
head-to-head," not a benchmark. Triage estimated 3 novel patterns; extracted as 2
findings — the Soul capability profile and the Fable one-shot pixel-fidelity weakness
are two sides of the same head-to-head and were grouped into one finding; the
cost-observability bug pattern stands alone.

His reusable "clone app pat" staged-gate skill (recon → extraction → design spec →
architecture → build → QA/fix loop → polish → deploy) is corroboration of existing
staged-gate/plan-first findings, not extracted separately.
