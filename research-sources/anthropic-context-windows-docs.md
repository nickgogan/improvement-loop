---
name: "Context Windows — Claude API Docs"
source_type: "Documentation"
status: "Done"
date_processed: "2026-04-23"
date_published: null
key_takeaways: "Canonical Anthropic docs for context-window behavior. Documents that Claude Sonnet 4.5, Sonnet 4.6, and Haiku 4.5 'feature context awareness that lets these models track their remaining context window (i.e. token budget) throughout a conversation, enabling Claude to execute tasks and manage context more effectively.' This is a model-native capability — distinct from (and complementary to) harness-side pre-turn projection. Opus behavior at 1M context is not explicitly described in the same terms."
relevance: "High"
added_by: "Claude"
tags: ["context-engineering", "canonical-source", "anthropic", "token-budget"]
url: "https://platform.claude.com/docs/en/build-with-claude/context-windows"
authority:
  - "anthropic.md"
findings:
  - "model-native-context-window-awareness.md"
date_added: "2026-04-23"
---
