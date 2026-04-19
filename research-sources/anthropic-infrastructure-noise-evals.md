---
name: "Quantifying infrastructure noise in evals"
source_type: "Blog Post"
status: "Done"
key_takeaways: "Infrastructure configuration alone swings agentic coding benchmark scores by up to 6 percentage points (p < 0.01), exceeding leaderboard gaps between top models. Resource enforcement (guaranteed allocation vs hard kill threshold) is the primary noise source. Infra error rates dropped from 5.8% at 1x to 0.5% uncapped. Leaderboard gaps under 3 points warrant skepticism."
relevance: "High"
added_by: "Agent (Scheduled Scan)"
tags: ["evaluation", "infrastructure"]
url: "https://www.anthropic.com/engineering/infrastructure-noise"
authority: ["anthropic.md"]
findings:
  - "infrastructure-noise-agentic-eval-confounding.md"
  - "benchmark-signal-mismatch-optimization-gap.md"
  - "factorial-design-eval-systematic-context-variati.md"
date_added: "2026-04-09"
date_processed: "2026-04-09"
---
