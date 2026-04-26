---
title: "Stupid Button: Six-Question Token Waste Self-Audit Diagnostic"
type: "extracted-artifact"
assigned_form: "skill"
source_finding: "stupid-button-six-question-token-audit-diagnostic"
extraction_date: "2026-04-19"
last_change_session: 44
last_change_sl: "session-44-codifier-extraction-run"
identification_report: "2026-04-19-identification-report-4.md"
deployed: false
deployed_to: null
context:
  applies_to:
    - "agentic coding systems where token efficiency is operationally significant"
    - "teams or individuals running high-volume Claude sessions who need concrete waste diagnosis, not generic advice"
    - "context engineering audits at session boundaries or during system setup"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "operate"
  reversibility: "trivial — diagnostic only; produces a report but does not modify any configuration or files unless the user acts on recommendations"
  auditability: "high — invariants require all six questions answered with specific named instances and measured token counts; outputs are concrete, not generic"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Documented by a practitioner (Nate B Jones) with quantified cost comparisons ($8-10 sloppy vs ~$1 clean per session); no production deployments known within this system at time of extraction."
contract:
  preconditions: "User has declared the target scope and selected an implementation tier. For Tier 2: session metadata is accessible. For Tier 3: integration infrastructure exists."
  invariants: "All six questions are answered for the declared scope. Outputs are specific (named instances, measured token counts) not generic advice. Tier escalation is a recommendation, not automatic."
  governance: "Owner: MetaSystem improvement-loop system. Applicable across all three systems. Modifications to the six questions or tier definitions require a DD."
  recovery: "If scope not declared: halt and prompt. If Tier 2 cannot access metadata: fall back to Tier 1. If Tier 3 infrastructure absent: document requirements and return."
tags:
  - "extracted-artifact"
  - "skill"
---

# Stupid Button: Six-Question Token Waste Self-Audit Diagnostic

**Source:** [[stupid-button-six-question-token-audit-diagnostic]]
**Form:** skill
**Extraction date:** 2026-04-19

## Purpose

Identify and eliminate the most common token waste patterns in Claude sessions. Three progressive implementation tiers.

## Inputs

- Target scope: recent conversation history, Claude Code session, or desktop environment
- Implementation tier selection: Prompt (1), Skill (2), or Guardrails (3)
- For Tier 2: access to Claude Code session metadata or desktop environment configuration
- For Tier 3: integration infrastructure (CI hook, preprocessing pipeline, or tool harness)

## Outputs

- Answers to all six diagnostic questions for the declared scope
- Waste pattern inventory: specific instances identified
- Recommended remediation actions ranked by estimated token savings
- Tier escalation recommendation if current tier cannot address identified patterns

## The Six Questions

1. Do you feed Claude raw PDFs and images when all you need is text?
2. When was the last time you started a fresh conversation?
3. Are you using the most expensive model for everything?
4. Do you know what's loading in context before you type?
5. Are you caching stable context?
6. How are you handling web search?

## Steps

### Tier 1 — Prompt Diagnostic
1. Run the six questions against the declared scope.
2. For each question, produce a specific answer: not "possibly" but a concrete yes/no with evidence.
3. Map each yes-answer to a waste pattern and estimated cost.
4. Produce a ranked remediation list.

### Tier 2 — Skill Audit
1. Invoke against Claude Code or desktop environment.
2. Measure per-session token overhead: system prompt size, auto-loaded context, persistent memory bloat.
3. Flag system prompt sections that are large, rarely relevant, or duplicated.
4. Report: overhead breakdown by source, flagged sections, estimated savings from pruning each.

### Tier 3 — Guardrails Infrastructure
1. Implement automatic markdown conversion for PDFs and images at ingestion.
2. Implement index-first retrieval: agent reads index before deciding whether to read full file.
3. Scope context to minimum viable context per query.
4. Automate cache warming for stable context.
5. Instrument and log token overhead per session; alert when overhead exceeds threshold.

## Failure Modes

- **Anxiety spiral.** Creates over-optimization focus leading to under-specification. Apply only at session boundaries.
- **Tier 3 integration cost.** May exceed savings for low-volume users. Complete Tiers 1-2 first.
- **API/power-user bias.** Six questions calibrated for high-volume users. Declare scope and volume before invoking.

## Contract

### Preconditions
User has declared the target scope and selected an implementation tier. For Tier 2: session metadata is accessible. For Tier 3: integration infrastructure exists.

### Invariants
All six questions are answered for the declared scope. Outputs are specific (named instances, measured token counts) not generic advice. Tier escalation is a recommendation, not automatic.

### Governance
Owner: MetaSystem improvement-loop system. Applicable across all three systems. Modifications to the six questions or tier definitions require a DD.

### Recovery
If scope not declared: halt and prompt. If Tier 2 cannot access metadata: fall back to Tier 1. If Tier 3 infrastructure absent: document requirements and return.
