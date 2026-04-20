---
notion_id: 32b1e08b-9b34-81b5-bc5b-c397d448e42f
name: Context Engineering Supersedes Prompt Engineering
summary: 'The paradigm shift from prompt engineering to context engineering: as agents take over more work, the quality of an agent''s context file (what it knows about the business, role, and preferences)
  determines output quality more than the sophistication of individual prompts.'
implementation_notes: null
category: Prompt Craft
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P3
applicability:
- S3 (Claude Code Build)
adopted_in: []
sources:
- building-ai-agents-that-actually-work-full-course.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: memorymd-cross-session-preference-persistence.md
  rel: enables
- file: global-vs-project-level-skill-and-context.md
  rel: extended-by
- file: model-agnostic-prompting-three-properties.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Context Engineering Supersedes Prompt Engineering

## What It Is
Prompt engineering was the dominant meta-skill when people used LLMs as chat tools: crafting the perfect prompt for each query. In the agent paradigm, prompts are replaced by simple task descriptions ('write me a cold email') while the sophistication lives in the context file (agents.md/CLAUDE.md). A well-loaded agent answers simple prompts with expert-quality outputs; a poorly-loaded agent fails even on carefully crafted prompts. The practitioner frames this as: 'It's about how well you can load up your agent with all the information about your business so that your prompts can be stupidly simple.'

## Why It Matters
This reframing has practical implications for where users should invest their time: not in prompt engineering libraries, but in building and maintaining rich context files. The leverage shifts from per-query effort to upfront setup that pays dividends on every subsequent query.

## Why People Are Using It
Users who have built comprehensive agents.md files report dramatically better outputs from trivial prompts. The more you invest in context, the less you need to invest in individual prompts.

## Potential Alternatives
N/A — this is a conceptual reframing, not a tool. The tools that implement it are context files, memory systems, and skills.

## Potential Improvements
Tooling that helps users audit and improve their context files (identifying gaps, outdated information, conflicting rules) would make context engineering more accessible.

## Potential Failure Modes
Over-investing in context files without validating that the context is actually correct or current. Static context files that become outdated as the business changes can produce worse results than no context at all.

---

## April 2026 Update

**Now confirmed as the dominant framing in March 2026** across practitioner, enterprise, and academic sources:

**Academic validation:** ACE (ICLR 2026, Stanford/SambaNova) validates the principle at a research level. The paper treats the context window as an "evolving playbook" and demonstrates +10.6% benchmark improvement from structured context management vs. default approaches. This is the first peer-reviewed paper to validate context engineering as a distinct discipline.

**Leadership citation:** Shopify CEO Tobi Lutke now cited in multiple March 2026 sources: "The fundamental skill of using AI well is to be able to state a problem with enough context, in such a way that without any additional pieces of information, the task is plausibly solvable." This framing has become a touchstone reference across the practitioner community.

**Next evolution — Intent Engineering:** An emerging meta-layer above context engineering is now visible in multiple March 2026 sources. The progression:
- **Prompt Engineering** (2023-2024): Craft perfect prompts for each query
- **Context Engineering** (2025-2026): Load agent with rich context so prompts can be simple
- **Intent Engineering** (emerging 2026): Encode *why* and *under what conditions* the agent should act, not just what context it has

Intent Engineering addresses the gap: "Context without intent is noise." The Seven-Part Agent Intent Specification (Product Compass, Jan 2026) is the first formal framework for this layer. See new finding: Intent Engineering Framework — Seven-Part Agent Intent Specification.

**Updated evidence strength:** Strong (was Medium — now with ICLR validation and wider adoption signals including Shopify CEO citation)

**Sources:** https://iclr.cc/virtual/2026/poster/10008343 / https://www.productcompass.pm/p/intent-engineering-framework-for-ai-agents
