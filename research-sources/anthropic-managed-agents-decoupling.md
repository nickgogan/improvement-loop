---
name: "Scaling Managed Agents: Decoupling the Brain from the Hands"
source_type: "Blog Post"
status: "Done"
key_takeaways: "Virtualizing agent components (session, harness, sandbox) into stable interfaces. Brain-hands decoupling via execute(name, input) API enables independent scaling, 60-90% TTFT reduction via lazy provisioning. Credential isolation via bundled auth and vault proxy. Session as append-only event log for crash-proof recovery."
relevance: "High"
added_by: "Agent (Scheduled Scan)"
tags:
  - "orchestration"
  - "agent-design"
  - "sandboxing"
  - "governance"
url: "https://www.anthropic.com/engineering/managed-agents"
authority: ["anthropic.md"]
findings:
  - "brain-hands-decoupling-architecture.md"
  - "session-as-append-only-event-log.md"
  - "credential-isolation-bundled-auth-vault-proxy.md"
  - "anthropic-managed-agents-platform.md"
  - "session-persistence-crash-resilient.md"
  - "durable-workflow-engine-for-agent-systems.md"
  - "tool-gateway-security-boundary.md"
date_added: "2026-04-09"
date_processed: "2026-04-09"
---
