---
name: 'Two-Tree Model — Editable Authoring Tree vs Canonical Generated Pack, with an Allow-List as the Durability Contract'
summary: 'A private enterprise context-hub separates the skill library into two trees: the editable authoring tree (~/.claude/skills, where humans and optimizer tools work) and the canonical generated tree (the hub repo''s local-sources/ plus a generated skills/registry.json, which is committed, shared, and served). A sync pipeline reconciles them, and durability runs through one constant: SELECTED_SKILLS, an allow-list — a skill ships in the generated pack ONLY if listed, and anything unlisted is pruned on the next sync. An idempotent persist script (persist-spoke.mjs) is the only sanctioned writer of the allow-list and registry; the standing rule is "edit upstream, not the generated output" — generated files carry a sync banner and hand-edits are overwritten.'
implementation_notes: 'This is the most direct evidence yet for the engine''s Rule-11 asset-catalog FORM question (directory convention vs frontmatter-indexed registry vs generated view) — and the production answer is ALL THREE, arranged in a generation pipeline rather than chosen between: directory convention for authoring (skills as directories with frontmatter), a generated machine registry (registry.json) for runtime/serving, and generated docs/views for humans, with one-directional generation (author → generate → serve) making them consistent by construction. The engine already has the precedent in FOUNDATIONS.md (generated from DD frontmatter; DDs canonical); this finding says: scale that idiom to the whole asset catalog, and put an explicit allow-list + idempotent persist script at the boundary so durability is a contract, not a convention. The prune-if-unlisted semantics is the sharp edge worth copying — it makes catalog membership auditable and makes drift self-healing (hand-edits and strays get pruned on next sync) at the cost of requiring the script pathway for every legitimate addition.'
category: Governance
evidence_strength: Medium (practitioner-documented, production system at a large enterprise (repo private, author-shared writeup))
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- hub-and-spoke-context-hub.md
proposals: null
date_discovered: '2026-07-12'
last_updated: '2026-07-12'
related_findings:
- file: manifest-hash-drift-detection-for-derived-docs.md
  rel: same-problem
- file: deterministic-doc-audit-battery.md
  rel: same-problem
- file: dr-research-to-skill-gated-pipeline.md
  rel: enabled-by
- file: mcp-hub-skill-pack-serving-telemetry-middleware.md
  rel: enables
pipeline_status: raw
consumed_by: []
tags:
- source-of-truth
- generated-artifacts
- allow-list
- asset-catalog
- sync-pipeline
---

# Two-Tree Model — Editable Authoring Tree vs Canonical Generated Pack

## What It Is

A source-of-truth architecture for a skill/asset library shared beyond one machine:

- **Authoring tree** (`~/.claude/skills/<id>/SKILL.md`) — the working copy the human and
  the optimizer/build tools edit directly. Local, mutable, per-operator.
- **Canonical tree** (hub repo: `local-sources/<id>/{manifest.yaml, context.md}` plus the
  generated `skills/registry.json`) — the git-tracked pack that gets committed, cloned by
  teammates, and served to agents over MCP.

The flow between them:

```
authoring tree ──persist-spoke.mjs──► local-sources pair + SELECTED_SKILLS += <id>
              ──npm run sync:skills──► skills/registry.json + generated contexts
              ──registry loads at server start──► hub_* tools (served to any agent)
```

Two rules make it hold:

1. **`SELECTED_SKILLS` is the durability contract.** A skill is included in the generated
   pack only if its id appears in this allow-list; anything unlisted is *pruned* on the
   next sync. `persist-spoke.mjs` idempotently inserts ids (below an auto-managed marker)
   and writes the backing pair — it is the only sanctioned writer.
2. **Edit upstream, never the generated output.** Generated files carry a sync banner;
   hand-edits to them are overwritten on the next sync. Fix the generator or the source.

## Why It Matters

Plain English: any asset catalog eventually faces the question "which copy is real?" —
the file someone edited, the index that lists it, or the view an agent consumes. This
design answers it structurally: exactly one editable surface, everything downstream
generated, and membership in the catalog controlled by one explicit list with prune-if-
absent semantics. Hand-edits don't drift; they get deleted — which sounds harsh and is
precisely what makes the catalog trustworthy. A teammate who clones the repo gets the
identical pack; an agent that queries the server reads the identical registry.

It also cleanly separates *survival* from *quality*: the persist step is gated on zero
unresolved High findings from the optimizer, so nothing reaches the canonical tree
unaudited, and nothing audited is lost to a laptop wipe.

## How It Works

- **Idempotency as a safety property.** `persist-spoke.mjs` is safe to re-run; repeated
  persists of the same skill are no-ops. That is what allows pipelines (and humans) to
  retry without corrupting the allow-list.
- **Registry double-write for freshness.** Persist also upserts `skills/registry.json`
  directly so the new skill is discoverable immediately, without waiting for the next
  full sync.
- **Batch canonicalization.** When many skills land (a domain saturation run), the pack
  is canonicalized once at the end (`--sync`), not per skill.
- **Two source-of-truth boundaries.** Upstream docs feed the generator (fix the
  generator, not its output); registries feed the service layer (the server reads only
  generated registries at runtime).
- **Reshapes must re-persist.** A taxonomy rebalance in the authoring tree is not durable
  until affected skills re-run persist + sync.

## How It Could Fail

- **The prune is unforgiving.** A skill added by hand to the generated tree — or whose
  allow-list line is lost in a bad merge — silently disappears on the next sync. The
  auto-managed marker and idempotent script reduce, but don't eliminate, merge hazards.
- **Two trees can diverge between syncs.** The model tolerates a stale canonical tree
  (authoring runs ahead); it breaks if someone treats the canonical tree as editable.
- **Single-writer bottleneck.** Everything legitimate flows through one script; if the
  script's schema lags a new asset shape, authors route around it — the exact drift the
  model exists to prevent.
