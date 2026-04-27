---
title: "AI and Human Vaults Must Be Strictly Separated"
type: "extracted-artifact"
assigned_form: "rule"
source_finding: "ai-managed-vault-separate-from-human-vault"
identification_report: "building-agentic-systems.harvest-queue.md::ai-managed-vault-separate-from-human-vault::rule::ai-and-human-vaults-must-be-separate"
extraction_date: "2026-04-27"
last_change_session: 83
last_change_sl: "session-83-codifier-ib164-resume-extract-artifacts"
deployed: false
deployed_to: null
context:
  applies_to:
    - "practitioners maintaining a personal knowledge base alongside an AI agent that produces summaries, entity pages, or meeting notes"
    - "teams running file-based AI memory stores intended to be portable across models or vendors"
    - "anyone whose AI agent has file-write capability into a directory that also contains human-authored notes"
  platform_coupling: "agnostic"
  autonomy: "all"
  stage: "specify"
  reversibility: "medium — splitting an already-mixed vault is expensive but tractable; the earlier the separation is established, the cheaper it stays"
  auditability: "high when each vault has its own git history and writer-class is enforced at the tool/hook layer; medium when relying on author discipline alone"
  evidence_strength: "Medium"
  adoption:
    status: "Not Yet Started"
    notes: "Practitioner-documented (single source) with several years of personal-vault history and a parallel AI vault now operating. No known team-scale deployment at extraction time."
contract:
  preconditions: "AI-generated and human-authored content both exist in markdown form on local disk and are intended to persist over time. A specific AI agent or family of agents has file-write capability. The human uses the AI's outputs as a reference layer rather than treating them as drafts to be edited in place."
  invariants: "Each vault has a single declared writer class (human or AI). All files in a vault are written by that class; no file has mixed-authorship edits. Cross-vault references are read-only — a human note may link to an AI-vault entry, but does not embed or fork its content without going through a defined promotion step that tags provenance."
  governance: "Owner: the practitioner or team operating the vaults. The separation must be encoded in the AI agent's tool configuration (write-path restriction) and in vault-level git hooks or filesystem permissions, not delegated to author discipline. Promotion workflows (AI-vault content elevated into human vault after review) must produce provenance metadata at promotion time."
  recovery: "If a mixed-provenance file is discovered, do not retroactively rewrite history; split the file by authorship, restore the AI-vault copy to its last AI-authored state, and create a paired human-vault note carrying the human edits. If an AI agent is found writing into the human vault, treat the violation as a tool-config bug, fix the configuration, and audit recent writes for damage. If the AI model is being swapped, the AI vault carries over unchanged — that is the entire point of the separation."
tags:
  - "extracted-artifact"
  - "rule"
---

# AI and Human Vaults Must Be Strictly Separated

**Source:** [[ai-managed-vault-separate-from-human-vault]]
**Form:** rule
**Extraction date:** 2026-04-27

## Condition

A practitioner or team is accumulating AI-generated content (content summaries, entity profiles, meeting notes, daily briefs, project documentation) alongside human-authored content (personal notes, hand-written thinking, curated knowledge) in a markdown-based knowledge store such as Obsidian, a git repository of notes, or a comparable file-system vault. The intent is for both bodies of content to persist and be navigable over time.

## Action

**Required:** Maintain two distinct vaults (or distinct, write-isolated roots) — one written exclusively by humans, one written exclusively by the AI. The human uses the AI vault read-only. The AI never writes into the human vault. Every file's provenance is determined by which vault it lives in; no entry has mixed authorship.

**Forbidden:** Allowing the AI to edit human-authored notes in place. Allowing humans to hand-edit AI-generated content inside the AI vault (corrections must go through a defined promotion workflow with explicit provenance tagging, not silent edits). Combining AI-generated and human-authored content in the same vault root without write-access separation.

## Boundary

Enforced at the file-write boundary for both vaults. The check fires on any write operation that would create or modify a file: the writer's identity (human user vs. AI agent) must match the vault's declared owner. Also fires at vault setup — a new vault must declare which class of writer owns it before content accumulates.

## Enforcement

- **Mechanism:** Per-vault write-access controls — the AI agent's tool configuration restricts file writes to the AI vault root; human edits to the AI vault are blocked or require an explicit override flag. A pre-commit hook on each vault rejects commits whose author class does not match the vault's owner.
- **Check (deterministic):** `(write_target_vault.owner == writer.class)`. Any mismatch → block the write, or route it through an explicit cross-vault promotion step that tags provenance.
- **Violation response:**
  - *AI attempts to write to human vault:* block at the tool-config layer; surface as an agent violation, not a silent failure.
  - *Human edits AI vault file:* block via hook, or accept the edit only if it carries an explicit provenance change marker (e.g., the file is moved/copied into the human vault with attribution preserved).
  - *Mixed-provenance file discovered:* split it — extract the human edits into a human-vault note, restore the AI-vault file to its last AI-authored state, and link them.

## Rationale

Most AI memory systems are vendor-locked; switching providers loses accumulated context. Anchoring AI memory in local files is the portability mechanism, but portability collapses if humans hand-edit AI-generated content — the AI can no longer maintain the structure systematically and a future model cannot reliably take over. Strict separation also makes trust auditable: the human can verify what the AI knows by reading the AI vault and inspecting any specific entry, knowing nothing was silently human-corrected. The single largest failure mode of mixed-provenance vaults is that humans naturally start "fixing" AI output, which degrades the AI's ability to maintain it and erases the provenance signal that makes the vault inspectable. Separation is the positive-space invariant; mixed editing is the negative-space failure.

## Contract

### Preconditions
AI-generated and human-authored content both exist in markdown form on local disk and are intended to persist over time. A specific AI agent or family of agents has file-write capability. The human uses the AI's outputs as a reference layer rather than treating them as drafts to be edited in place.

### Invariants
Each vault has a single declared writer class (human or AI). All files in a vault are written by that class; no file has mixed-authorship edits. Cross-vault references are read-only — a human note may link to an AI-vault entry, but does not embed or fork its content without going through a defined promotion step that tags provenance.

### Governance
Owner: the practitioner or team operating the vaults. The separation must be encoded in the AI agent's tool configuration (write-path restriction) and in vault-level git hooks or filesystem permissions, not delegated to author discipline. Promotion workflows (AI-vault content elevated into human vault after review) must produce provenance metadata at promotion time.

### Recovery
If a mixed-provenance file is discovered, do not retroactively rewrite history; split the file by authorship, restore the AI-vault copy to its last AI-authored state, and create a paired human-vault note carrying the human edits. If an AI agent is found writing into the human vault, treat the violation as a tool-config bug, fix the configuration, and audit recent writes for damage. If the AI model is being swapped, the AI vault carries over unchanged — that is the entire point of the separation.
