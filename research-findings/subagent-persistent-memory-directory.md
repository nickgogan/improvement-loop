---
name: "Subagent Persistent Memory Directory with Auto-Curation"
summary: "A Claude Code subagent can be given a persistent filesystem directory that survives across conversations (~/.claude/agent-memory/{name}/). The subagent's system prompt auto-loads the first 200 lines or 25KB of MEMORY.md from that directory on every invocation and is instructed to curate the file if it exceeds the budget. Plain English: give a specialist subagent a notebook it carries between sessions. The subagent writes what it learns about your codebase, and the next time you invoke it, it remembers."
implementation_notes: "Requires memory: user|project|local in subagent frontmatter. Read/Write/Edit tools are auto-enabled on the memory directory. For MetaSystem: Librarian's encounter log and design-notes already function like a hand-maintained memory; this pattern could automate the read-side of that."
category: "Memory Architecture"
evidence_strength: "Strong (documented, first-party Anthropic canonical spec)"
adoption_status: "Not Yet Started"
priority: P2
applicability:
  - "General"
  - "S3 (Claude Code Build)"
adopted_in: []
sources:
  - "anthropic-claude-code-subagents-docs.md"
related_findings:
  - file: mongodb-single-store-polymorphic-evidence-memory.md
    rel: same-problem
  - file: verbatim-storage-thesis-for-memory.md
    rel: same-problem
  - file: agent-onboarding-via-interview-style-context.md
    rel: same-problem
  - file: claude-code-hooks-for-automatic-session-memory.md
    rel: extends
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-24"
pipeline_status: classified
consumed_by: []
---

## What It Is

A persistent memory mechanism built into Claude Code subagents. Declared by the `memory` field in the subagent's frontmatter with three scope options:

| Scope | Directory | Use |
|---|---|---|
| `user` | `~/.claude/agent-memory/{name}/` | Learnings across all projects |
| `project` | `.claude/agent-memory/{name}/` | Project-specific; shareable via VCS |
| `local` | `.claude/agent-memory-local/{name}/` | Project-specific; NOT checked in |

Mechanics:

1. **Automatic preloading.** The subagent's system prompt on each invocation includes the first 200 lines or 25KB of `MEMORY.md` from its memory directory (whichever comes first).
2. **Curation instruction.** If `MEMORY.md` exceeds the budget, the system prompt instructs the subagent to curate it — compress, prune, restructure.
3. **Auto-enabled tools.** Read, Write, and Edit are automatically enabled on the memory directory so the subagent can manage its memory files.
4. **Extensible.** Memory is a directory, not just a file; the subagent can write supporting files (`{codebase}-patterns.md`, `{team}-conventions.md`, `errors-seen.md`) and reference them from `MEMORY.md`.
5. **Scope-appropriate sharing.** `project` scope makes the memory shareable via Git; `user` scope keeps it personal; `local` scope keeps it personal AND out of version control.

Orchestration pattern Anthropic recommends: ask the subagent to consult memory before starting (*"Review this PR, and check your memory for patterns you've seen before"*) and update memory after completing (*"Now that you're done, save what you learned to your memory."*). Over time this builds a knowledge base specific to the subagent's domain.

## Why It Matters

Classical agent memory is either in-context (ephemeral, per-session) or external (database, search index — query-mediated). This pattern is a third option: filesystem-resident, human-readable, directly accessible by the subagent. No database; no indexing; no retrieval tuning. Just a markdown file the subagent reads at start and writes at end.

For MetaSystem:
- **Matches existing IL patterns.** The Librarian's `operations/system-log/librarian-encounter-log-*.md` files are effectively hand-maintained per-session memory. The pattern-docs in `agents/*/reflections/` are hand-maintained per-agent memory. Moving these from hand-maintained to Claude-Code-native automation is a natural evolution.
- **Scales across subagent types.** Researcher, Codifier, Owner, Librarian each have distinct memory-relevant content (source-triage patterns, classification heuristics, governance patterns, consumer encounters). Each could have its own memory directory.
- **Architectural alternative to the [[verbatim-storage-thesis-for-memory]] / [[mongodb-single-store-polymorphic-evidence-memory]] design-space triangle.** Those are for agent-memory-as-system (infrastructure). Subagent memory is for agent-memory-as-practice (per-subagent knowledge accretion). Different scope, complementary pattern.
- **Graceful degradation with [[claude-code-hooks-for-automatic-session-memory]].** Hooks can auto-capture structured events; memory directory captures free-form subagent reflection. Both work; they measure different things.

The 200-line / 25KB budget with auto-curation is an interesting design choice: it forces the subagent to compress rather than append. Unbounded append produces stale knowledge bases that no one reads; budgeted curation keeps the knowledge base as living documentation.

## Why People Are Using It

Documented canonically at [Anthropic's Claude Code subagents docs](https://code.claude.com/docs/en/sub-agents) — see [[anthropic-claude-code-subagents-docs]] for the source. The canonical example is a code-reviewer subagent with `memory: user`:

```yaml
---
name: code-reviewer
description: Reviews code for quality and best practices
memory: user
---

You are a code reviewer. As you review code, update your agent memory with
patterns, conventions, and recurring issues you discover.
```

Anthropic's stated design intent: *"the subagent uses this to accumulate insights across conversations, such as codebase patterns and recurring issues."* The feature is new (2026 Claude Code update) so adoption-in-the-wild is early; the pattern's primary evidence is the first-party docs and the design rationale.

## Potential Alternatives

- **In-context memory only.** Subagent gets zero persistent state; must re-derive everything from scratch each run. Baseline; produces generic outputs.
- **Database-backed agent memory** (mem0, Zep, Supermemory). Rich query capabilities; structured; higher ops cost; requires retrieval tuning.
- **CLAUDE.md hand-maintained.** Humans maintain knowledge; agents read only. Reliable content; doesn't compound with agent use.
- **Session-transcript replay.** Load prior session transcripts as context. Faithful reproduction; noisy; exceeds budgets fast.
- **External knowledge-management tool** (Notion, Obsidian, Readwise). General-purpose; not agent-aware; integration overhead.

## Potential Improvements

- **Memory diff summaries.** When the subagent curates `MEMORY.md`, surface a diff so the user sees what was added/removed/restructured. Governance over the memory evolution.
- **Multi-file memory indexing.** `MEMORY.md` as an index pointing to supplementary files; 200-line cap applies to the index, not the full corpus. Enables larger effective memory.
- **Memory export/import.** Move a subagent's memory across scopes (user → project, local → project). Enables promoting personal learnings to shared team artifacts.
- **Memory versioning.** Git-track memory directory; revert bad curations; diff across time. Native to `project` scope; manual at other scopes.
- **Cross-subagent memory sharing.** `security-reviewer` and `code-reviewer` might benefit from shared memory on "patterns-in-this-codebase." Named shared memory directories referenced by multiple subagents.

## Potential Failure Modes

- **Memory drift.** Subagent curates memory per its own understanding; human never inspects; the memory accumulates stale or wrong knowledge. Mitigation: periodic human audit; diff summaries on curation.
- **Budget gaming.** Subagent keeps only shallow summaries to stay under budget; loses nuance. Mitigation: reference supplementary files from index-style `MEMORY.md`.
- **Cross-project contamination.** `user` scope memory pollutes subagent behavior on projects where it doesn't apply. Mitigation: prefer `project` or `local` scope; use `user` only for truly project-agnostic knowledge.
- **Curation deadlock.** Subagent rewrites the same sections on every invocation, chasing the budget without converging. Mitigation: include stable structural sections the subagent is instructed not to touch on curation.
- **Memory-as-prompt-injection surface.** If the subagent accepts instructions via PR comments or issue bodies, those could contaminate `MEMORY.md`. Mitigation: explicit separation of "what the user said" vs "what the subagent decides to remember."
- **Security: secrets in memory.** Subagent accidentally writes an API key or credential into `MEMORY.md`. Mitigation: pre-commit hooks that scan memory files for secrets; memory directory structure that flags security-sensitive sections.
