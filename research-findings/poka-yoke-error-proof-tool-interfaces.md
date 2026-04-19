---
name: "Poka-Yoke Error-Proof Tool Interface Design"
summary: "Apply manufacturing error-proofing to tool design: restructure arguments to make errors structurally impossible. Requiring absolute filepaths instead of relative ones eliminated path errors completely in SWE-bench."
implementation_notes: "Audit MetaSystem tool/skill parameters for poka-yoke opportunities. The file edit tool's absolute path requirement is an example already in use."
category: "Tool Integration"
evidence_strength: "Strong (production-tested)"
adoption_status: "Partially Adopted"
proposer_priority: "P1 (Implement Now)"
applicability:
  - "S3 (Claude Code Build)"
  - "General / Cross-System"
adopted_in:
  - "S3 (Claude Code Build)"
sources:
  - "anthropic-building-effective-agents.md"
related_findings: []
proposals: null
date_discovered: "2026-04-09"
last_updated: "2026-04-09"
pipeline_status: "synthesized"
consumed_by:
  - "designing-agent-tools.md"
---

## What It Is
Borrowing from manufacturing's poka-yoke philosophy, tool interfaces should make errors structurally impossible rather than relying on instructions to prevent them. The SWE-bench example: models made errors with relative filepaths after directory changes; switching to mandatory absolute filepaths eliminated path errors entirely. The SWE-bench team spent more time on tool refinement than on prompt engineering.

## Why It Matters
Instructions can be forgotten or misapplied; structural constraints cannot. Tool interface quality is at least as important as prompt quality for agent performance. The investment priority — more time on tool design than prompt engineering — signals a paradigm shift.

## Why People Are Using It
Anthropic's SWE-bench agent used this approach to achieve state-of-the-art results. The absolute filepath requirement eliminated an entire class of errors.

## Potential Improvements
Systematic audit methodology for identifying poka-yoke opportunities across existing tool sets. Type systems for tool parameters that enforce valid states.

## Potential Failure Modes
Over-constraining tools reduces flexibility. Some tasks genuinely need relative paths or flexible inputs. Need to distinguish "prevent common errors" from "prevent all non-standard usage."

## Extraction Note — 2026-04-19
Extracted as **pattern**: [[poka-yoke-error-proof-tool-interfaces.md]] in `extracts/patterns/`
