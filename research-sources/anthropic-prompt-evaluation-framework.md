---
notion_id: "32b1e08b-9b34-81aa-b83d-e445fc729543"
name: "Anthropic Prompt Evaluation Framework"
source_type: "Documentation"
status: "Done"
key_takeaways: "Three eval design principles: task-specific, automate when possible, volume over quality. Three-tier grading hierarchy: code-based > LLM-based > human (avoid if possible). Multidimensional SMART success criteria across 8 dimensions. LLM-as-judge best practice: reasoning before scoring then discard reasoning. Use different model for grading than generation. Concrete code examples: exact match, cosine similarity, ROUGE-L, Likert scale, binary classification, ordinal scale."
relevance: "High"
added_by: "Nick"
tags:
  - "evaluation"
url: "https://docs.anthropic.com/en/docs/build-with-claude/develop-tests"
authority: []
findings:
  - "volume-over-quality-eval-principle.md"
  - "three-tier-grading-hierarchy.md"
  - "multidimensional-success-criteria-smart.md"
  - "four-discipline-prompt-evaluator.md"
date_added: "2026-03-16"
date_processed: "2026-04-07"
---

# Anthropic Prompt Evaluation Framework
