---
notion_id: "32c1e08b-9b34-8111-bb96-c75482991299"
name: "Standardize Context Enrichment in Subagent Objectives"
proposal: "Every subagent objective across all systems must include four mandatory context fields: (1) Purpose -- what the results will be used for, (2) Audience -- who consumes the output, (3) Workflow Position -- where this task sits in the broader workflow, (4) Success Criteria -- measurable thresholds for quality. Audit existing subagent calls for compliance."
rationale: "Context Enrichment for Task Clarity (Strong evidence): Anthropic and OpenAI best practices document that providing task purpose, audience, workflow position, and success criteria dramatically improves output quality. We do this inconsistently -- subagent objectives in particular often lack this context. Lowest-effort, highest-impact change."
status: "Not started"
target_system: "General / Cross-System"
priority: "P1 (Implement Now)"
risk_level: "Low"
implementation_complexity: "Low"
effort: "Medium (1-4 hours)"
door_type: "Two-Way"
ops_impact: "Reduces Ops Burden"
conflicts: false
conflict_group: null
findings: []
date_proposed: "2026-03-23"
date_resolved: null
---

# Standardize Context Enrichment in Subagent Objectives

## Current State
Subagent objectives across our systems vary widely in context completeness. Some include detailed purpose and success criteria; many do not. The Perplexity system's subagent_usage section provides structural guidance (keep objectives short, save data to files) but doesn't mandate context enrichment fields. S3's subagent delegation similarly lacks a required context template. The result: subagents often optimize for generic "good enough" output because they don't know the broader purpose.

## Proposed Change
Add a mandatory context enrichment template to all subagent delegation points:

**Required fields in every subagent objective:**
1. **Purpose:** What the results will be used for (e.g., "This data feeds into a client-facing report" vs "This is exploratory research")
2. **Audience:** Who consumes the output (e.g., "The parent agent will synthesize this with 3 other subagent outputs" vs "This will be shared directly with the user")
3. **Workflow Position:** Where this task sits (e.g., "Step 2 of 5 in the research loop -- sources have been fetched, findings extraction is next")
4. **Success Criteria:** Measurable quality thresholds (e.g., "Must include source URLs for every claim" or "Accuracy matters more than completeness")

This template should be documented in:
- Perplexity skills subagent guidelines
- S3 CLAUDE.md subagent delegation section
- Any orchestration skill that delegates to subagents

## Rationale
Context enrichment is documented as a high-impact, low-effort improvement in both Anthropic and OpenAI best practices. Without explicit context, models optimize for generic quality. With context, they make informed trade-offs -- prioritizing accuracy over speed for a client report, or breadth over depth for exploratory research. This is especially critical for subagents, which have zero context about the parent workflow unless explicitly told.

## Door Type Assessment
Two-way door. The context template is additive guidance. If it proves too verbose or slows down delegation, fields can be simplified or made optional. No system behavior changes irreversibly.

## Implementation Assessment
Low complexity despite medium effort. The complexity is low (text changes to existing guidelines), but the effort is medium because auditing existing subagent calls across all systems takes time. The template itself is straightforward to add.

## Operational Impact
Reduces ops burden. Better-contextualized subagent objectives produce higher-quality first-pass output, reducing the need for retries, manual correction, and result re-interpretation. No new monitoring needed.

## Implementation Steps
1. Define the four-field context template with examples for each field
2. Add the template to Perplexity skills subagent guidelines (subagent_usage section)
3. Add the template to S3 CLAUDE.md subagent delegation section
4. Audit existing subagent calls in all active skills -- flag any that lack required fields
5. Update flagged calls with appropriate context enrichment
6. Add a reminder in orchestration patterns: "Before spawning, ask: does the objective include Purpose, Audience, Position, and Criteria?"
