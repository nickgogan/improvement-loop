---
name: "Splx.ai — Kimi K2 Safety Red-Team Evaluation"
source_type: "Article"
status: "Done"
key_takeaways: "Raw Kimi K2 (no system prompt): 1.55% security, 4.47% safety, 0.00% business alignment vs Claude Sonnet 4's 34.63%/39.72% raw. Prompt-hardened K2 reaches 59.52%/82.70%/86.39% but still trails hardened Sonnet 4 (83.69%/98.77%/92.97%). Verdict: 'unfit for anything even close to production' without guardrails; not yet fit for secure enterprise deployment even hardened. The quantified half of the Kimi safety-gap claim (the arXiv K2.5 audit is the other half)."
relevance: "High"
added_by: "Agent (Research Query)"
tags:
  - model-selection
  - kimi
  - safety
  - red-team
  - governance
url: "https://splx.ai/blog/kimi-k2-safety-test"
authority: []
findings:
  - kimi-k2-line-near-opus-coding-with-safety-gap.md
date_added: "2026-07-11"
date_processed: "2026-07-11"
date_published: "2025-07-17"
---
