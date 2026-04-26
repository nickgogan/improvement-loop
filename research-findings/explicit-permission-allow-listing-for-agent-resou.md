---
notion_id: 32b1e08b-9b34-815d-a41b-f7cd90703571
name: Explicit Permission Allow-Listing for Agent Resource Access
summary: Claude Dispatch surfaces a permission prompt whenever a skill tries to access a new resource the user hasn't pre-authorized, requiring explicit approval before proceeding. This allow-listing model
  is cited as a key security advantage over OpenClaw's permissive-by-default architecture.
implementation_notes: null
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P1
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- claude-codes-leak-changes-everything.md
- anthropic-claude-code-auto-mode.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: mcp-session-scoped-authorization.md
  rel: same-problem
- file: tool-gateway-security-boundary.md
  rel: enables
- file: agent-type-system-six-roles.md
  rel: same-problem
- file: worktree-isolation-for-parallel-agent-sessions.md
  rel: same-problem
- file: claude-code-auto-mode-ai-driven-permission-classif.md
  rel: same-problem
pipeline_status: extracted
consumed_by:
- rules/explicit-permission-allow-listing-for-agent-resource-access.md
---
# Explicit Permission Allow-Listing for Agent Resource Access

## What It Is
When a Dispatch-run skill encounters a resource it needs access to that hasn't been pre-approved (e.g., a specific file path, API endpoint, or system service), a popup appears in the Dispatch interface asking the user to allow or deny. The user must explicitly grant access for the task to proceed. This creates an audit trail of what the agent is accessing and prevents unsanctioned autonomous actions.

## Why It Matters
The author notes that OpenClaw and similar DIY agent stacks have leaked tens of thousands of API keys due to inadequate security design. Real-world incidents included agents deleting all emails, creating dating profiles without being asked, and performing data exfiltration. Explicit allow-listing forces humans to remain in the loop for novel resource access, which is a prerequisite for business and enterprise use.

## Why People Are Using It
Enterprise and business users who cannot afford credential leaks or uncontrolled agent actions need explicit auditability. The design mirrors the security model of mobile OS permission dialogs, which most users already understand.

## Potential Alternatives
Read-only scoped MCP connectors (limiting tools to view-only access by default); role-based agent permission profiles in enterprise systems; OpenAI's Frontier platform permission model.

## Potential Improvements
Persistent allow-lists per skill so frequently-used skills don't trigger repeat approval dialogs. Permission groupings by trust level (read-only, read-write, execute) to reduce cognitive overhead.

## Potential Failure Modes
Permission fatigue — if every skill triggers multiple approval dialogs, users may start blindly approving everything, defeating the purpose. The model requires the user to be present and attentive at approval time.

## Extraction Note — 2026-04-26
Extracted as **rule**: [[explicit-permission-allow-listing-for-agent-resource-access]] in `extracts/rules/`
