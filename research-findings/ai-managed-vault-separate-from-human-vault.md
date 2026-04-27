---
name: AI-Managed Vault Separate from Human Vault
summary: 'Maintain two distinct Obsidian vaults: one owned and written by humans (personal notes, thinking), and one owned and written exclusively by the AI (summaries, entity pages, project docs, meeting
  notes). The human uses the AI vault read-only. The separation keeps human curation intact, makes the AI vault model-agnostic, and creates an ownable, portable AI memory store.'
implementation_notes: 'The AI vault holds: video/content summaries, entity profiles (people, concepts, tools), meeting notes, project documentation. The human never writes into the AI vault. The AI never
  writes into the human vault. Since all content is markdown files on local disk, swapping the AI model (Claude → future model) requires no data migration — the vault connects to any model that can read
  files. The AI vault is the realization of ''owning your AI memories.'''
category: Agentic Systems
evidence_strength: Medium (practitioner-documented)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- S3 (Claude Code Build)
- General
adopted_in: []
sources:
- claude-code-for-life-daily-briefs-obsidian-memory.md
related_findings:
- file: obsidian-as-transparent-frontend-vs-rag-black-box.md
  rel: extends
- file: file-over-app-philosophy-for-knowledge-permanence.md
  rel: companion
- file: claude-code-as-vault-query-engine-project-assistant.md
  rel: extends
- file: behavioral-context-portability-intelligence-lock-in.md
  rel: same-problem
- file: build-operate-separation-principle.md
  rel: same-problem
- file: karpathy-llm-knowledge-base-obsidian-rag.md
  rel: same-problem
proposals: null
date_discovered: '2026-04-20'
last_updated: '2026-04-20'
pipeline_status: synthesized
consumed_by:
  - "building-agentic-systems.md"
  - artifact: ai-and-human-vaults-must-be-separate
    type: extracted-artifact
    form: rule
    date: 2026-04-27
    session: 83
---
# AI-Managed Vault Separate from Human Vault

## What It Is
A deliberate architectural separation between two Obsidian vaults:

**Human vault** — personal notes, hand-written thinking, curated knowledge. Never touched by the AI.  
**AI vault** — all AI-generated content: content summaries, entity pages, project documentation, meeting notes, daily briefs. The human uses this vault read-only.

The separation enforces clean ownership: anything in the AI vault was written by the AI, and anything in the human vault was written by a human. No mixed provenance. The human navigates the AI vault as a reader-consumer, not as a collaborator who might accidentally pollute AI-generated structure with human edits (or vice versa).

The AI vault accumulates over time: repeated exposure to the same people, concepts, and tools builds up interconnected profiles. The practitioner frames this as "owning your AI memories" — unlike cloud AI memory systems, these are plain markdown files on local disk, fully portable and inspectable.

The model-agnostic property is the key long-term claim: because the vault is just files, disconnecting Claude Code and connecting a future AI model (or a local model) requires no data migration. The vault and its accumulated knowledge persist independently of any AI vendor.

## Why It Matters
Most AI memory systems (ChatGPT memory, Claude Projects, etc.) are vendor-locked. When you switch models or providers, your accumulated context is lost. By anchoring AI memory in local markdown files, the user retains ownership and portability. The separation also prevents the most common failure mode of "AI-assisted" vaults: the human starts editing AI-generated content, which breaks the AI's ability to maintain it systematically.

The separation also makes trust cleaner — the human can verify what the AI knows by reading the AI vault, can see it grow over time, and can inspect any specific entry to check its accuracy. This aligns with and extends the transparent-frontend rationale of the Obsidian-vs-RAG finding.

## Why People Are Using It
Practitioner has used Obsidian for several years (personal vault) and now runs a parallel AI vault for all Claude Code outputs. The pattern has emerged from real usage rather than upfront architectural design — the user noticed problems with mixed-provenance vaults and settled on strict separation as the solution.

## Potential Improvements
- **Selective promotion** — a workflow for promoting AI-generated content into the human vault after human review/editing, with clear provenance tagging
- **Cross-vault linking** — Obsidian supports vault-relative links; a human note about a topic could link to the AI vault's entity page for that topic (read-only reference)
- **Staleness indicators** — AI vault entries older than N days without a recent source reference could be flagged for review

## Potential Failure Modes
- The read-only discipline requires explicit tooling or habit reinforcement — without friction, humans naturally start editing the AI vault, which degrades consistency
- Two vaults create navigation overhead — the human must know which vault to check for a given piece of information
- The model-agnostic portability claim requires that future models also use file I/O as their primary interface; if AI memory systems shift to opaque databases, the portability advantage erodes
- Growing AI vaults without curation accumulate outdated or low-quality content over time; the "it just grows" framing can lead to quality degradation

## Extraction Note — 2026-04-27

Extracted as **rule**: [[ai-and-human-vaults-must-be-separate]] in `extracts/rules/`. Harvested from the G11 (building-agentic-systems) queue per IB-164 / DD-101 promotion path.
