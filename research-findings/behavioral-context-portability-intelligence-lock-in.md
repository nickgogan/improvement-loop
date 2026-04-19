---
name: Behavioral Context Portability (Intelligence Lock-In)
summary: The next generation of AI platform lock-in will be based on accumulated behavioral models — not data, but the patterns an agent learned by watching you work. Data is portable (CSV, export tools);
  behavioral context is not. There is no 'migration consultant' for how a person thinks. This creates switching costs that exceed anything seen in previous platform eras.
implementation_notes: Build or adopt a behavioral audit skill now. The behavioral fingerprint should be user-owned and portable before persistent agents launch widely.
category: Governance
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- conway-anthropics-always-on-agent.md
related_findings: []
proposals: null
date_discovered: '2026-04-09'
last_updated: '2026-04-09'
pipeline_status: synthesized
consumed_by:
- agent-governance-and-trust.md
---
# Behavioral Context Portability (Intelligence Lock-In)

## What It Is
A new category of platform lock-in identified from the Conway leak analysis. Previous lock-in was about stuff: Microsoft locked in files, Salesforce locked in customer records, Slack locked in communication history. Data lock-in is painful but solvable — export tools exist, migration consultants exist. Behavioral context lock-in is different. After 6 months, a persistent agent has learned: which emails you respond to immediately vs. ignore, how you schedule, which Slack threads matter, how you prepare for meetings. This behavioral model is the product of your data + the provider's compute + 6 months of inference. It doesn't export. There's no CSV of "how this person thinks." When you switch providers, you lose the compounding that made the agent useful — you're back to a "brilliant stranger."

## Why It Matters
This is lock-in at a layer that hasn't existed before. Data portability has legal frameworks (GDPR, etc.). Intelligence portability does not. The question of who owns the behavioral model — the user, the employer, or the provider — has no regulatory answer yet. Employers may leverage accumulated behavioral context as both carrot (you're 2x more productive with this agent) and stick (leaving means starting over). This will reshape employee-employer dynamics in the second half of 2026.

## Why People Are Using It
The concept is emerging from analysis, not yet from practice. Nate B Jones proposed a "behavioral audit skill" as a portable alternative. The broader community has not yet grappled with this.

## Potential Alternatives
- Build a personal behavioral context layer that is provider-agnostic (e.g., Open Brain)
- Portable behavioral audit exports (skill that captures how you work)
- Industry standard for behavioral context export (does not yet exist)

## Potential Improvements
- Legal frameworks for intelligence portability
- Technical standards for behavioral model export
- User-controlled learning boundaries

## Potential Failure Modes
- Convenience will likely win over portability for most users
- Employers may claim ownership of behavioral patterns generated during work
- The conversation about portability may not happen until lock-in is already established
