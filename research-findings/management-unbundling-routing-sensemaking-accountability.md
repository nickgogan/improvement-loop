---
name: "Management Unbundling: Routing, Sensemaking, Accountability"
summary: "Management bundles three distinct functions: information routing (AI-automatable), sensemaking (partially automatable, human-dominant), and accountability/feedback (human-essential). Flattening that removes management without explicitly reassigning all three functions produces culture strain, drift, and attrition. The correct lever is decomposition before compression."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: "P2 (Design Required)"
applicability:
  - "General"
adopted_in: []
sources:
  - "unbundling-management-ai-age-routing-sensemaking.md"
related_findings:
  - file: five-persistent-human-skills-agent-era-framework.md
    rel: same-problem
  - file: org-redesign-for-agentic-throughput-high-speed-rail.md
    rel: same-problem
  - file: review-bandwidth-as-organizational-bottleneck.md
    rel: same-problem
  - file: dri-rotation-pattern-time-bounded-sensemaking-ownership.md
    rel: extends
  - file: structural-vs-psychological-vs-economic-governance.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-20"
last_updated: "2026-04-20"
pipeline_status: synthesized
consumed_by:
  - "agent-governance-and-trust.md"
---

## What It Is

A practitioner framework (Nate B Jones, 2026) for decomposing the management role into three distinct functions before deciding which to automate, reassign, or eliminate:

**1. Routing (AI-automatable)**
Information logistics: aggregating signal up from teams and distributing directives down from leadership. Synthesizing status updates, cascading policy changes, monitoring competitive signals, generating requirements docs. At Kimi, three agents handle this for a PM in ~2 hours (scan 3K feedback items → sentiment analysis → competitor monitoring → 70% of implementation code). Routing is a solved problem. Intelligence improvements at 10x do not change this verdict.

**2. Sensemaking (partially automatable, human-dominant)**
Distinguishing signal from noise in both directions: translating strategy into team direction, and surfacing meaningful patterns from ground-level data upward. Requires years of domain/company/product context that AI cannot replicate reliably. The problem is not shortage of information — it is shortage of signal. Sensemaking is a human-to-human activity; agents are poor interlocutors for it. At Kimi, five co-founders do this for ~50 reports each (extreme cognitive load). At Block, DRIs own this per problem area with explicit authority and expiration dates. At Meta, it remains bundled in fewer, wider-span managers with AI assist.

**3. Accountability and Feedback (human-essential)**
Human ownership of outcomes over time. Agents can simulate apologies but cannot simulate the multi-year attachment a product manager develops toward a domain. Accountability requires a human who feels the consequences in their bones. Feedback delivery — timed, contextual, developmentally appropriate — is a human talent. AI can assist by gathering and routing performance data, but the judgment and delivery remain human. Removing this function produces "weightlessness": employees don't know what to do or whether they're performing (documented at Kimi).

**Three company experiments (2026):**

| Company | Routing | Sensemaking | Accountability | Model |
|---------|---------|-------------|----------------|-------|
| Kimi/Moonshot AI | Agents | 5 co-founders × 50 reports | Absent (self-reflection only) | Decompose + abdicate accountability |
| Block (Jack Dorsey) | AI world model | DRIs (time-bounded, explicit authority) | Player-coaches (IC-practitioners who also develop people) | Decompose fully |
| Meta | AI-assisted within hierarchy | Human, fewer layers | Intensified (bottom 5% cut) | Compress + intensify |

**The decompose vs. compress choice:** Companies that compress (fewer managers doing more) produce pressure and attrition. Companies that decompose explicitly (name who owns each function) are positioned better long-term because they can specifically imagine what AI handles and what humans handle.

**Span of control reframe:** In the AI era, span of control is less about routing bandwidth and more about the speed of the market-signal → production loop. AI compresses this cycle; hierarchy that requires executive approval for each release becomes the bottleneck.

## Why It Matters

Nearly half of US companies removed management layers in 2024-2025 while assuming AI would handle the gap. Most did not decompose the bundle before cutting. The result: teams that are faster on routing but adrift on direction and accountability. This framework names the three failure modes precisely so that org redesigns can account for all three rather than only the most visible one (routing).

For MetaSystem and Claude Build: agent-heavy workflows handle routing well. The human gate handles accountability. The sensemaking gap — who interprets pattern signals, decides what findings mean for the system, and makes judgment calls about direction — is the function most at risk of becoming an implicit bottleneck or of atrophying.

## Why People Are Using It

Kimi case study is from a journalist-embedded 100-hour observation with 30+ employee interviews (Renw magazine) and represents one of the first rigorous inside accounts of a no-management AI-native company at scale. Block's model is from Jack Dorsey and Rolof Botha's published framework. Meta's data point includes stock performance metrics (3x growth since efficiency push) and anecdotal burnout reports. The triangulation of three large-scale live experiments makes this evidence unusually strong for practitioner-documented work.

## Potential Improvements

- Map the three functions to MetaSystem's existing human gates and agent roles. Routing is handled; accountability is partially handled; sensemaking is implicit and unstructured.
- The Block DRI rotation model (see related finding) could be applied at smaller scale: name a responsible individual per system domain for 90-day terms with explicit authority to interpret signals and make direction calls.
- Player-coach model (IC practitioners who also develop people) maps cleanly to Claude Build's build + governance role for Nick — worth examining whether that model is already implicit and can be made explicit.

## Potential Failure Modes

- Decomposition is cognitively expensive: co-founders/leaders resist explicitly naming who owns sensemaking because it forces acknowledgment of cognitive load.
- DRI rotation (Block) may produce shallow ownership if 90-day cycles are too short for deep context to accumulate.
- Player-coach model collapses under load: when shipping pressure increases, coaching is the first thing dropped.
- Accountability intensification (Meta model) trades short-term throughput for long-term attrition; only works if talent pipeline is stronger than attrition rate.
- Agent-only companies (no sensemaking function) may compete effectively in commoditized markets but fail where trust requires a human face.
