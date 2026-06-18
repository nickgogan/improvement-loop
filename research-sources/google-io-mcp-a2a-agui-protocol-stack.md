---
name: "Google Spent a Year Stitching MCP, A2A, AG-UI Together. I/O Today."
source_type: "Video"
status: "Done"
key_takeaways: "MCP tool descriptions are a prompt-injection attack surface (Invariant Labs research). AGUI is a human control layer, not a UI layer — it encodes approval/observe/cancel control points. Teams that skip this accumulate supervision debt. Six agent protocols mapped."
relevance: "High"
added_by: "Nick"
tags:
  - "governance"
  - "tools"
  - "orchestration"
url: "https://www.youtube.com/watch?v=zP6TnEiueEc"
authority: []
findings:
  - "agui-human-control-layer-not-ui.md"
  - "coordination-cost-vs-flexibility-tradeoff-agent-delegation.md"
  - "google-a2a-protocol-agent-to-agent-interoperabilit.md"
  - "mcp-high-trust-design-assumption.md"
  - "mcp-tool-description-prompt-injection-attack.md"
  - "operating-surface-underspecification-anti-pattern.md"
  - "protocol-substrate-shapes-customer-experience.md"
  - "supervision-debt-anti-pattern.md"
  - "three-layer-core-agent-protocol-stack.md"
  - "three-question-protocol-selection-framework.md"
  - "tool-access-as-security-boundary-not-feature-toggle.md"
date_added: "2026-05-24"
date_processed: "2026-05-24"
---

# Google Spent a Year Stitching MCP, A2A, AG-UI Together. I/O Today.

Practitioner analysis of six agent protocols (MCP, A2A, AGUI and others) and how they compose. Key security insight: MCP tool descriptions are a prompt-injection vector. Key architectural insight: AGUI is about encoding human control points, not rendering UI.
