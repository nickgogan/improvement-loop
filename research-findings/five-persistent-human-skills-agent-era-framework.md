---
notion_id: 32b1e08b-9b34-819b-b8b7-e83d80aa9c13
name: Five Persistent Human Skills (Agent-Era Framework)
summary: 'Five skills humans must actively retain as agents expand: boundary sensing, seam design, failure model maintenance, capability forecasting, and leverage calibration. A framework for directing
  human attention in an agent-heavy system.'
implementation_notes: null
category: Intent Engineering
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
proposer_priority: P3
applicability:
- General
adopted_in: []
sources:
- nate-b-jones-videos-feb-mar-2026.md
proposals: []
date_discovered: '2026-03-09'
last_updated: '2026-04-19'
pipeline_status: raw
consumed_by: []
---
# Five Persistent Human Skills (Agent-Era Framework)

## What It Is
A practitioner framework identifying five skills that humans must deliberately maintain as AI agents take over more execution work: (1) Boundary sensing — knowing where agent authority should stop; (2) Seam design — architecting the handoffs between human and agent; (3) Failure model maintenance — keeping mental models of how the system fails; (4) Capability forecasting — tracking what agents will be able to do soon; (5) Leverage calibration — deciding where human effort compounds most.

**Updated 2026-03-22:** Anthropic's official skill-creation guide ("Most People Build Claude Skills Wrong") maps directly onto this taxonomy via a Five-Pattern Skill Taxonomy: (1) Sequential — steps must execute in order; (2) Multi-MCP Coordination — parallel/sequential calls across multiple external services; (3) Iterative Refinement — loop with quality gate until score threshold met; (4) Context-Aware Routing — initial classifier routes to specialized sub-skills; (5) Domain-Specific Intelligence — knowledge retrieval where uploaded domain documents are the core value. Each pattern uses a reusable outer template (name, trigger phrase, rules/constraints, expected output). Most real use cases fall into Pattern 1 (sequential); Pattern 4 (routing) is particularly powerful for customer support triage.

## Why It Matters
As agents automate execution, humans risk atrophying the meta-skills needed to govern them well. This framework names what not to delegate, which is as important as knowing what to automate.

**Updated 2026-03-22:** Without a pattern framework, practitioners either build overly generic skills ('solve my customer support tickets') or cram all logic into one monolithic prompt. The pattern taxonomy forces explicit design of the central logic — the only part that changes across patterns — reinforcing why skill categorization is a persistent human responsibility that cannot be safely delegated to agents themselves.

## Why People Are Using It
Documented by Nate B. Jones and maps directly onto the existing system: the Playbook covers skill 3 (failure model maintenance). Skills 1 and 2 lack dedicated tooling — a Frontier Ops Dashboard was proposed as IB-96 but never built.

## Potential Improvements
Could be encoded as a periodic self-assessment checklist tied to the Improvement Loop cadence — one item per skill, with concrete evidence required rather than self-report.

**Updated 2026-03-22:** Combining patterns (e.g., a routing skill that dispatches to iterative refinement sub-skills) is briefly mentioned in Anthropic's guide but not fully elaborated. Explicit error-handling paths within each pattern template would improve robustness. Iterative refinement loops without a max-iteration cap will consume all tokens — a concrete failure mode to encode in the checklist.

## Potential Failure Modes
Without concrete metrics for each skill, the framework stays theoretical. It becomes easy to believe you are maintaining all five skills while actually letting several atrophy silently.
