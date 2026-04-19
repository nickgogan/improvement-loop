---
name: "Tool Use Examples -- Sample Calls in Tool Definitions"
summary: "Embedding example invocations directly in tool definitions teaches models correct usage patterns beyond what schemas alone convey. Accuracy on complex parameters improved from 72% to 90% in Anthropic internal testing. Addresses nested objects, optional parameter correlations, and domain-specific conventions."
implementation_notes: null
category: "Tool Integration"
evidence_strength: "Strong (production-tested)"
adoption_status: "Not Yet Started"
proposer_priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "anthropic-advanced-tool-use.md"
related_findings:
  - file: "poka-yoke-error-proof-tool-interfaces.md"
    rel: "extends"
proposals: null
date_discovered: "2026-04-09"
last_updated: "2026-04-09"
pipeline_status: "synthesized"
consumed_by:
  - "designing-agent-tools.md"
---

## What It Is
A beta API feature adding `input_examples` to tool definitions -- sample invocations that teach models correct usage patterns. Schemas define structural validity but not usage conventions: which optional parameters go together, how nested objects should be constructed, what domain-specific formats to use (date formats, ID patterns, label conventions). Examples solve this by showing concrete patterns.

Key patterns examples teach:
- **Formats**: YYYY-MM-DD dates, USR-XXXXX IDs, kebab-case labels
- **Nested object construction**: When to populate `reporter.contact` vs. omit it
- **Parameter correlations**: Critical priority implies full contact info + tight SLA; feature requests need reporter but no escalation; internal tickets need title only
- **Similar tool disambiguation**: Which tool to use when multiple tools have overlapping capabilities

## Why It Matters
Schemas ensure valid JSON but not correct tool usage. A `create_ticket` tool with nested `reporter.contact` and `escalation` objects has many valid JSON combinations, but only a few represent correct usage patterns. Without examples, models guess at correlations and conventions, producing structurally valid but semantically wrong invocations. The 72% to 90% accuracy jump on complex parameters demonstrates the gap.

## Why People Are Using It
Anthropic beta feature with measured accuracy gains. Most beneficial for: complex nested schemas (valid JSON does not equal correct usage), tools with many optional parameters that have correlation patterns, domain-specific conventions Claude cannot infer from schema alone, and similar tools needing disambiguation.

## Potential Improvements
Auto-generation of examples from API usage logs. Example selection based on the current task context (show relevant examples, not all). Integration with Tool Search Tool so examples load only for the tools actually being used.

## Potential Failure Modes
Examples add tokens to tool definitions -- net negative for simple single-parameter tools. Examples can become stale if the API evolves. Over-reliance on examples may reduce model generalization to novel parameter combinations not covered by examples.
