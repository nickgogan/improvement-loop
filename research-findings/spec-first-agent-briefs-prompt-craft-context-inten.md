---
notion_id: 3351e08b-9b34-8118-9357-f35b94f3c769
name: 'Spec-first agent briefs: Prompt Craft -> Context -> Intent -> Specification engineering'
summary: 'For long-running agentic work, the most reliable prompting pattern is to package work as a self-contained spec: objective + success metrics + authoritative inputs + deliverables + acceptance criteria
  + constraints (must/must-not/preferences) + escalation triggers + plan-first checkpoints.'
implementation_notes: 'Adopt a standard spec template for all agentic coding tasks: require plan-first with checkpoints, explicit success metrics, acceptance criteria with runnable commands, and escalation
  triggers (ambiguity, policy conflicts, risky changes). Treat context (docs/repos/tool definitions/memory) and intent (trade-offs: speed vs quality/cost vs correctness) as first-class sections rather than
  implicit prompt text.'
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Partially Adopted
priority: P1 (Implement Now)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- intent-engineering-framework-for-ai-agents-product.md
- prompting-after-feb-2026-prompt-craft-context-inten.md
proposals: []
date_discovered: '2026-04-01'
last_updated: '2026-04-07'
related_findings:
- file: acceptance-criteria-as-verifiable-eval-anchor.md
  rel: extends
pipeline_status: synthesized
consumed_by:
- writing-agent-specifications.md
---
# Spec-first agent briefs: Prompt Craft -> Context -> Intent -> Specification engineering

Key spec primitives highlighted:
- Objective + why
- Success metrics
- Authoritative inputs + definitions
- Deliverables + exact format
- Acceptance criteria (verifiable)
- Constraints: must/must-not/preferences + escalate-if
- Workflow: plan + checkpoints -> confirm -> execute -> verification notes

Source: https://maniak.io/articles/2026-02-27-prompting-post-feb-2026/

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[spec-first-agent-briefs-prompt-craft-context-inten.md]] in `extracts/patterns/`
