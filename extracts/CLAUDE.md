# Extracts — Research-Substrate Library (+ staging residue)

`extracts/` is **not** a single drafts-staging bin. Per **DD-111**, it holds two things that share
folder names but play different roles:

## Live substrate (the Librarian composes this — not staging)

| Subtree | Tier | Role |
|---------|------|------|
| `guides/` | **Tier 1** | Live substrate. Slug-referenced by the concept docs, the guide-routing-table, and skills. The Librarian advisory layer (`/assess-*`, `/design-*`, `/ask-kb`, `/audit-artifacts`) composes these directly. |
| `patterns/` | **Tier 2** | Live corpus. Browsed by category/tag/dimension (not by filename); individual files are mostly un-pinned but reachable as Tier-2 substrate. |

This is **product/substrate, consumed pull-style** — distilled external agentic-coding best-practice.
It is one of the **two bodies** (DD-103, DD-111): `extracts/` = research substrate the Librarian
composes; `knowledge/` = the engine's own self-knowledge. They are not the same artifacts at two
pipeline stages.

## Harvest archive (`rules/`, `skills/`, `templates/`, `agents/`)

These four subtrees are a **harvest archive**, not a deployment queue. Each file is a raw
finding-derivative — **distilled external best-practice** (what other teams/tools do) bucketed by
form. They are NOT engine artifacts:

- An `extracts/rules/` file (e.g. `context-degradation-40-percent-threshold.md`) records an *observed*
  practice — it is **not** an engine-enforced rule. Engine rules live in `governance/` and
  `.claude/rules/`.
- Likewise `extracts/skills/`, `extracts/templates/`, `extracts/agents/` are external skill/template/
  agent *patterns*, not the engine's own skills/templates/agents.

**Status & disposition (DD-111, session-126 promote-or-prune pass):**

- **Kept, not deleted.** Each traces to a source finding; the archive is valuable as future
  `/synthesize-guide` input and as low-tier (Tier-3) research substrate reachable by browse.
- **Not composed as substrate today.** The Librarian composes guides + patterns + findings; it does
  **not** compose extracted rules/skills/templates/agents. ~5% are slug-pinned by a live consumer
  (a schematic, the form-rubric, a skill, a concept doc) and serve as substrate **in place** — leave
  them where they are.
- **Promotion is a per-item Nick adopt decision (DD-29), not implied by presence here.** Turning an
  observed external practice into engine law (`.claude/rules/`), an engine skill (`.claude/skills/`),
  or an engine template (`knowledge/templates/`) is a deliberate adoption Nick gates one artifact at a
  time — there is no bulk promotion.

**Do not deploy or promote from here automatically.** Human gate required (DD-29). Each form has its
own deployment target per DD-81 *if and when* Nick adopts it.

---

*Framing set by DD-111 (rename-in-place); spec input:
`archive/design-notes/2026-06-20-extracts-knowledge-reconciliation.md`.*
