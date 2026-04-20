---
name: MCP Elicitation for Mid-Execution User Input
summary: 'MCP servers can pause execution and request user input via two modes: URL-mode for flows requiring external interaction (OAuth, payment, credential entry) and form-mode for structured clarification
  questions rendered in-chat. Enables workflows that cannot be fully automated without human decision-making.'
implementation_notes: Complements our human-gate principle (DD-29). MCP elicitation provides protocol-level support for the approval gates we currently implement manually. When building MCP-exposed workflows,
  elicitation points should map to our existing human gate requirements.
category: Agent Design
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3 (Monitor)
applicability:
- General
adopted_in: []
sources:
- mcp-everything-your-team-needs-to-know-workos.md
related_findings:
- file: human-on-the-loop-hotl-autonomy-tiering-framework.md
  rel: enables
proposals: []
date_discovered: '2026-04-07'
last_updated: '2026-04-08'
pipeline_status: raw
consumed_by: []
---

# MCP Elicitation for Mid-Execution User Input

## What It Is
MCP defines a protocol-level pattern for servers to pause execution and request user input during tool execution. Two modes: (1) URL-mode routes users to trusted external URLs for flows requiring interaction (OAuth consent, payment, credential entry); (2) form-mode renders structured clarification questions directly in the chat interface. The sampling primitive also allows servers to request completions from the AI model during execution for intermediate reasoning.

## Why It Matters
Handles workflows that cannot be fully automated without human decision-making at protocol level rather than as custom implementation. Keeps humans in the loop for accuracy-sensitive workflows without requiring the entire workflow to be synchronous.

## Why People Are Using It
Part of the MCP 2026 spec. Addresses the gap between fully autonomous and fully manual agent workflows. Combined with MCP Apps (sandboxed HTML interfaces in iframes), enables rich interactive experiences within chat.

## Potential Improvements
Form-mode could support conditional fields and multi-step forms. Integration with approval queue systems for asynchronous human review.

## Potential Failure Modes
Adds latency and round trips. Breaks fully offline operation. URL-mode requires trust validation of external URLs to prevent phishing.
