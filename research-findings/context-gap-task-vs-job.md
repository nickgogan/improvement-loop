---
notion_id: 32b1e08b-9b34-81d5-98eb-e9b68ad3da98
name: 'Context Gap: Task vs. Job'
summary: AI agents excel at tasks (bounded, context-provided) but fail at jobs (open-ended, context must be supplied from organizational memory). The missing context includes unwritten decisions, informal
  agreements, historical constraints, and stakeholder politics — none of which appear in the task brief.
implementation_notes: null
category: Intent Engineering
evidence_strength: Strong (production-tested)
adoption_status: Not Yet Started
proposer_priority: P2
applicability:
- General
adopted_in: []
sources:
- your-ai-agent-fails-975-of-real-work-the-fix-isnt.md
proposals: []
date_discovered: '2026-03-22'
last_updated: '2026-04-19'
related_findings:
- file: sweci-benchmark-ai-fails-at-code-maintenance.md
  rel: same-problem
- file: production-database-wipeout-agent-context.md
  rel: same-problem
pipeline_status: raw
consumed_by: []
---
# Context Gap: Task vs. Job

## What It Is
Nate defines the task-vs-job distinction: a task comes with all necessary context provided (like GDP-val benchmarks); a job requires the worker to bring accumulated context from experience and organizational memory. Examples: a legal agent can parse contract clauses but cannot know about an informal payment arrangement negotiated at dinner three years ago. A marketing agent can build audiences but cannot know the brand had a crisis in that market segment and needs a different tone. A finance agent can build technically correct projections but cannot know which numbers are politically dangerous to the board this quarter. In every case, 'the agent does the task well' but misses what matters because the relevant context exists only in human heads.

## Why It Matters
This is the fundamental architectural insight for AI deployment: the limiting factor is not model intelligence but context transfer from humans to machines. Every agent deployment is implicitly a context engineering problem, and the hardest contexts to transfer are the unwritten, relational, and historical ones.

## Why People Are Using It
This framework helps practitioners prioritize: before investing in model upgrades, invest in context capture (decision documentation, eval writing, knowledge base building). It also explains why senior employees remain valuable even as AI automates task execution.

## Potential Alternatives
Long-context window expansion (more tokens does not equal more organizational wisdom), fine-tuning on company documents (captures documents, not undocumented decisions), RAG over internal wikis (retrieves what was written, not what was never written).

## Potential Improvements
Structured decision-logging systems that capture rationale, constraints, and context alongside outcomes. AI-assisted interviews with domain experts to elicit tacit knowledge into structured form.

## Potential Failure Modes
Even when context is documented, agents may not know when to retrieve it or recognize that a situation requires specific historical context. Documentation quality varies — poorly written context can mislead agents.
