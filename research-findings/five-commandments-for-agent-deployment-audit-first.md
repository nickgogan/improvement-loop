---
name: Five Commandments for Agent Deployment (Audit-First Framework)
summary: 'Sequential prerequisite checklist before deploying agents: (1) map actual process with edge cases, (2) fix data schemas, (3) redesign org for throughput, (4) build observability from day one,
  (5) scope authority deliberately. Emphasizes ''audit before automate'' as the governing principle.'
implementation_notes: MetaSystem already practices several of these (schema-first, scope boundaries). Observability (commandment 4) and org redesign (commandment 3) are the gaps. Consider formalizing as
  a pre-deployment checklist for new skills/agents.
category: Intent Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- agent-produces-100x-org-reviews-3x.md
date_discovered: '2026-04-07'
last_updated: '2026-04-07'
related_findings:
- file: org-redesign-for-agentic-throughput-high-speed-rail.md
  rel: same-problem
pipeline_status: extracted
consumed_by:
- skills/five-commandments-agent-deployment.md
---
## What It Is

A five-step prerequisite framework from Nate B Jones for responsible agent deployment, derived from production OpenClaw/agent case studies. The five commandments in sequence:

1. **Audit before you automate.** Map the actual process -- not the idealized one. Include edge cases, tribal knowledge, undocumented exception handling. "All the things that are in your head."
2. **Fix the data before giving agent access.** Establish source of truth, define schemas, build validation, decide conflict resolution for competing sources. (Overlaps with existing "Fix Data Schema Before Automating" finding.)
3. **Redesign your org for throughput.** If the agent 10x's production capacity, plan the whole org around that. Job roles, tool access, IT provisioning -- do not assume the org will "magically adjust."
4. **Build observability from day one.** Independent evaluation of agent outputs, not agent self-reporting. Audit trails, stack traces, automated verification of task completion. "Do not rely on agent self-reporting."
5. **Scope authority deliberately.** Define what the agent can and cannot do. Guardrail it explicitly. "Do not give the agent free access to everything." The dangerously-skip-permissions pattern is explicitly called out as irresponsible beyond day one testing.

## Why It Matters

The pattern addresses the "celebration on day one, crisis on day 30" failure mode. Jones cites multiple real cases: a $14K voice agent that couldn't track data, CRMs that encoded generic workflows instead of business-specific logic, ad creative scaling from 20 to 2,000 without review capacity. The common thread: skipping foundational work because the agent's generative output looked impressive initially.

## Why People Are Using It

Post-hype realism. Early adopters who deployed agents quickly are now encountering the second- and third-month problems: data quality degradation, process gaps, review bottlenecks, security incidents. The commandment pattern provides a sequential checklist that catches these issues before deployment rather than after.

## Potential Improvements

Could be formalized as a pre-flight check for MetaSystem skill/agent creation. The existing preflight skill validates environment setup; a similar pattern could validate deployment readiness against these five commandments. Score each commandment 0-5 to produce a deployment readiness score.

## Potential Failure Modes

The framework is sequential and thorough, which means it is slow. Teams under pressure to ship may skip commandments 1-3 and jump to deployment. The framework also assumes a level of process maturity that many early-stage teams lack -- you cannot "map the actual process" if the process has never been documented.

## Extraction Note — 2026-04-19
Extracted as **skill**: [[five-commandments-agent-deployment]] in `extracts/skills/`
