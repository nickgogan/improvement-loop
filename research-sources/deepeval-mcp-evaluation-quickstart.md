---
notion_id: "3351e08b-9b34-81a7-b89f-dc2d347f8e35"
name: "DeepEval: MCP Evaluation Quickstart"
source_type: "Documentation"
status: "Done"
key_takeaways: "Concrete MCP evaluation primitives for agentic apps: track MCP server/tool calls at runtime, then score tool selection and argument correctness."
relevance: "High"
added_by: "Agent (Scheduled Scan)"
tags:
  - "mcp"
  - "evaluation"
  - "tools"
url: "https://deepeval.com/docs/getting-started-mcp"
authority: []
findings:
  - "mcp-evaluation-primitives-deepeval-metrics.md"
date_added: "2026-04-01"
date_processed: "2026-04-07"
date_published: "2025-08-11"
---

# DeepEval: MCP Evaluation Quickstart

Key patterns: Create test cases that include mcp_servers plus the list of tools/resources/prompts called. Metrics: MCPUseMetric, MultiTurnMCPUseMetric, MCPTaskCompletionMetric.
