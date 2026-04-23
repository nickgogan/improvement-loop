---
name: "Token-Budget-Aware LLM Reasoning — arXiv 2412.18547 / ACL 2025 Findings"
source_type: "Paper"
status: "Done"
date_processed: "2026-04-23"
key_takeaways: "Academic paper showing that surfacing an explicit token budget into the prompt dynamically compresses reasoning traces without degrading answer quality. The framework estimates per-problem budgets based on reasoning complexity. Complements (doesn't replace) harness-side pre-turn projection — this is the *model-facing* equivalent: tell the model its budget and it will self-pace. Provides academic grounding for the model-native-context-window-awareness finding (which documents Anthropic's own productized version of the same idea on Claude 4.5+)."
relevance: "Medium"
added_by: "Claude"
tags: ["context-engineering", "token-budget", "reasoning", "academic", "arxiv"]
url: "https://arxiv.org/html/2412.18547v1"
authority: []
findings:
  - "model-native-context-window-awareness.md"
date_added: "2026-04-23"
---
