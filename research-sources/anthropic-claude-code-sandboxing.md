---
name: "Beyond permission prompts: Claude Code sandboxing"
source_type: "Blog Post"
status: "Done"
key_takeaways: "OS-level sandboxing using Linux bubblewrap and macOS seatbelt for filesystem and network isolation. Reduces permission prompts by 84%. Network isolation via Unix domain socket proxy with domain allowlisting. Credential proxy for cloud-based Claude Code keeps secrets outside sandbox. Open-sourced sandboxing runtime."
relevance: "High"
added_by: "Agent (Scheduled Scan)"
tags: ["sandboxing", "security", "permissions", "open-source"]
url: "https://www.anthropic.com/engineering/claude-code-sandboxing"
authority: ["anthropic.md"]
findings:
  - "os-level-agent-sandboxing-filesystem-network-isolation.md"
  - "tiered-permission-system-bash-safety.md"
  - "tool-gateway-security-boundary.md"
  - "claude-code-auto-mode-ai-driven-permission-classif.md"
date_added: "2026-04-09"
date_processed: "2026-04-09"
---
