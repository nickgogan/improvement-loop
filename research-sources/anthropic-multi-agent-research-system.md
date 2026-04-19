---
name: "How We Built Our Multi-Agent Research System"
source_type: "Blog Post"
status: "Done"
key_takeaways: "Orchestrator-worker pattern with Opus lead and Sonnet subagents outperforms single agent by 90.2%. Subagent condensed summaries (1-2K tokens) prevent information loss. Embedded effort-scaling rules prevent overinvestment. Self-improving agents diagnose and fix their own prompts and tool descriptions. LLM-as-judge rubric for outcome-focused evaluation."
relevance: "High"
added_by: "Agent (Scheduled Scan)"
tags:
  - "multi-agent"
  - "orchestration"
  - "evaluation"
  - "agent-design"
  - "prompt-engineering"
url: "https://www.anthropic.com/engineering/multi-agent-research-system"
authority: ["anthropic.md"]
findings:
  - "effort-scaling-rules-embedded-in-orchestrator.md"
  - "teach-orchestrator-to-delegate-pattern.md"
  - "self-improving-agent-prompt-tool-diagnosis.md"
  - "progressive-search-wide-then-narrow.md"
  - "sub-agent-context-isolation-for-parallel-complex.md"
  - "orchestrated-execution-one-task-per-sub-agent-wit.md"
  - "llm-as-judge-pattern-for-verification-agents.md"
  - "builder-validator-chain-pattern.md"
date_added: "2026-04-09"
date_processed: "2026-04-09"
---
