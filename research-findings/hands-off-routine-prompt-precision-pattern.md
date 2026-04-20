---
name: "Hands-Off Routine Prompt Precision Pattern"
summary: "Autonomous routines (unattended, cloud-scheduled agents) require substantially more precise prompts than interactive skills. The session cannot be steered mid-run, so error surface must be minimized upfront: narrow scope, explicit completion criteria, and step-by-step SOP instructions rather than goal-oriented prompts."
implementation_notes: "Applies directly to MetaSystem's watch-upstream, research-loop, and any future scheduled skills. Prompts for scheduled IL skills should be written to this standard: enumerate steps, define done explicitly, handle edge cases inline."
category: "Prompt Craft"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
proposer_priority: "P2 (Design Required)"
applicability:
  - "S3 (Claude Code Build)"
  - "General"
adopted_in: []
sources:
  - "claude-routines-scheduled-automations-webhooks.md"
related_findings:
  - file: claude-routines-webhook-triggered-pipeline-chaining.md
    rel: companion
  - file: anthropic-managed-agents-platform.md
    rel: companion
  - file: morning-routine-skill-active-experiment-check-in.md
    rel: same-problem
  - file: agent-clarification-over-assumption-pattern.md
    rel: contrasts-with
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: raw
consumed_by: []
---

## What It Is

A prompt design discipline for unattended agent execution. The core distinction: interactive skills (run with a human present) can be vague because the human can redirect mid-session. Scheduled routines and cloud automations run entirely without supervision — any ambiguity becomes an error that cannot be corrected.

**Practical rules (from the source):**
1. Write the routine description as a numbered SOP, not a goal statement
2. Be explicit about data sources ("use the provided Gmail connector" not "check my email")
3. Define the completion signal ("once done, send a Slack update" — the agent knows it's done)
4. Narrow scope to minimize the blast radius of mistakes — a routine that checks 10 emails is safer than one that processes your entire inbox
5. Lean toward more context, not less — the video presenter tested for a length limit and found none; verbosity is safe, under-specification is not
6. Encode edge case handling inline: "if no unreads exist, send a Slack message saying 'No unread emails'"

**Contrast with interactive skills:** In an interactive Claude Code session, the user can type "actually stop, skip that step" or "wait, that's not what I meant." A routine cannot be steered once triggered. The prompt is the complete specification.

## Why It Matters

Failure modes in unattended agents are invisible until the user checks output. A misconfigured interactive prompt produces a wrong answer the user sees immediately. A misconfigured routine sends the wrong email, posts incorrect data, or silently produces nothing — discovered hours later.

The precision requirement also defines the design boundary for which tasks are suitable for routines vs. skills: routine-suitable tasks have well-defined inputs, clear outputs, and predictable edge cases. Tasks requiring human judgment mid-flow should remain interactive.

## Why People Are Using It

Practitioners building production routines (email triage, proposal generation, daily briefs) report that the discipline of writing SOP-style prompts reduces failure rates substantially. The format forces explicit enumeration of steps that might otherwise be assumed.

## Potential Improvements

A checklist or template for routine prompt authorship: (1) data sources named, (2) steps enumerated, (3) done-signal defined, (4) edge cases handled, (5) output destination specified. MetaSystem's skill templates could add a "scheduled variant" section for any skill intended to run unattended.

## Potential Failure Modes

- Over-specification can make prompts brittle — an SOP that assumes a specific email format breaks when the format changes
- Comprehensive edge case coverage is impossible; the long tail of unexpected inputs will still produce failures
- Writing SOP-style prompts requires domain knowledge of the task; practitioners who do not understand the workflow well enough to write an SOP should not be automating it unattended
