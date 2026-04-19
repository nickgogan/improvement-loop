---
notion_id: 32b1e08b-9b34-8111-b71b-d9575a53a3e3
name: 'Model Tier Routing: Expensive Orchestrator, Cheap Sub-Agents'
summary: Using a premium model for orchestration (user interaction, planning, aggregation) and a cheaper/faster model for narrow sub-agent tasks makes parallel sub-agent architectures economically viable
  at scale without sacrificing orchestration quality.
implementation_notes: null
category: Orchestration
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: null
applicability:
- S3 (Claude Code Build)
adopted_in: null
sources:
- andrej-karpathys-math-proves-agent-skills-will-fai.md
- multi-agent-orchestration-production-playbook-nick.md
- ai-agents-in-production-2026-nick-gupta-linkedin.md
proposals: null
date_discovered: '2026-03-22'
last_updated: '2026-04-09'
related_findings:
- file: agent-cost-blowup-mitigation-strategies.md
  rel: extended-by
pipeline_status: raw
consumed_by: []
---
# Model Tier Routing: Expensive Orchestrator, Cheap Sub-Agents

## What It Is
In the demo harness, the main conversational agent uses Gemini 2.5 Pro (via OpenRouter) as the orchestrator — handling user interaction, planning, and aggregation. The parallel sub-agents (one per contract clause) use Gemini 2.5 Flash, a cheaper and faster model. The rationale: sub-agent tasks are narrow and well-defined ('analyze this specific clause against this specific playbook and return this specific schema') — well within the capability of a smaller model. The orchestrator task requires more nuanced judgment (user interaction, phase sequencing, synthesizing diverse sub-agent outputs) and benefits from a higher-capability model. The video notes this pattern keeps 'costs under control while still burning lots of tokens.'

## Why It Matters
At scale, sub-agent parallelism can consume enormous token volumes (323K total in the demo). Using a premium model for all sub-agent calls would make the workflow cost-prohibitive. Model tier routing makes parallel sub-agent architectures economically viable for high-volume workflows.

## Why People Are Using It
Practitioners building production systems must optimize cost-quality tradeoffs. The insight that sub-task capability requirements differ from orchestration capability requirements enables more efficient model allocation. OpenRouter makes multi-model orchestration straightforward without managing multiple API keys.

## Potential Alternatives
Single model for all tasks (simpler but expensive or underperforming), local models for sub-agents (free but slower and less capable), caching repeated sub-agent calls (reduces repeat costs but adds complexity).

## Potential Improvements
Dynamic model selection: the orchestrator evaluates task complexity at runtime and selects the appropriate model tier rather than using a fixed mapping. Model performance monitoring: track sub-agent success rates by model to empirically validate tier assignments.

## Potential Failure Modes
Smaller models may fail on tasks that appear narrow but have hidden complexity. Model API availability differs across providers — a harness depending on a specific sub-agent model may fail if that model is unavailable. Cost assumptions break if sub-agent task complexity is higher than expected.
