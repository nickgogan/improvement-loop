---
name: "Hierarchical Container-Tag Multi-Tenancy with Scope-at-Query-Time"
summary: "A single flat-string tag field on each memory record. Consumers adopt a hierarchical naming convention (`org_acme`, `org_acme_team_eng`, `org_acme_team_eng_user_alice`) — no schema enforcement of the hierarchy. Search accepts one container tag at query time; the tag scopes retrieval to that level. User-level retrieval returns user-only memories; team-level returns team + implicitly user-level (via separate queries); org-level returns org-wide. Simpler than typed hierarchies; works today; scales to many tenants."
implementation_notes: null
category: "Agent Design"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: scoped-memory-model.md
    rel: same-problem
  - file: memory-bank-isolation-per-agent-per-project.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-23"
pipeline_status: raw
consumed_by: []
---

## What It Is

A single-field multi-tenancy mechanism with three design points:

1. **Tag is a flat string.** Every memory record has one `containerTag` field. No schema, no type, no hierarchy enforcement at the storage layer.
2. **Hierarchy is a naming convention.** Consumers encode hierarchy in the tag value: `org_acme` for org-wide, `org_acme_team_engineering` for team, `org_acme_team_engineering_user_alice` for individual. The storage layer sees only strings.
3. **Scope is query-time.** Search accepts a `containerTag` parameter; results are scoped to that tag. To see multiple levels (e.g., user's private + team shared), issue multiple queries and merge.

Example usage shape (from `skills/supermemory/references/use-cases.md` §7):

```typescript
const tags = {
  org:    `org_${orgId}`,
  team:   `org_${orgId}_team_${teamId}`,
  user:   `org_${orgId}_team_${teamId}_user_${userId}`,
  shared: `org_${orgId}_shared`,
};

// Save at appropriate level
await memory.add({ content: ..., containerTag: tags.user });   // private
await memory.add({ content: ..., containerTag: tags.shared }); // org-wide

// Search at appropriate level
await memory.search.memories({ q: ..., containerTag: tags.user });   // user only
await memory.search.memories({ q: ..., containerTag: tags.shared }); // org shared only
```

Contrasts with:

- [[scoped-memory-model]] (mem0) — three first-class named dimensions (user_id, agent_id, run_id) that compose. Typed; schema-enforced; different query semantics.
- [[memory-bank-isolation-per-agent-per-project]] — separate storage per scope. Stricter isolation; no shared views.
- Workspace-based isolation (OpenClaw) — directory-level physical separation. Hard boundary; cross-scope impossible by design.

The Supermemory pattern sits between untyped-tags (flexible but unstructured) and typed-dimensions (rigorous but schema-coupled). The tradeoff: less rigor at the storage layer, more flexibility at the application layer. Consumers choose the hierarchy depth that matches their domain.

## Why It Matters

Directly applicable to two MetaSystem contexts:

1. **Household OS** needs multi-member and potentially multi-household scoping. Members share household-wide memories (schedule, shared expenses, family decisions) and have individual memories (their own preferences, personal schedules). The hierarchical-tag pattern fits natively. No schema change to add "multi-household support later."

2. **IL** could scope findings and reflections per system (`il`, `household-os`, `claude-build`) and per agent (`il_agent_researcher`, `il_agent_codifier`). Our current implicit scoping by directory (`systems/improvement-loop/research-findings/`) works at the filesystem level; a tag field would let us lift it into a queryable dimension without restructuring the directory tree.

Also relevant to [[typed-relationship-memory-graph]] (Supermemory's companion pattern — both features ship together). Together: typed evolutionary graph + hierarchical scoping = multi-tenant memory infrastructure with minimal schema.

## Why People Are Using It

Observed in [Supermemory](https://github.com/supermemoryai/supermemory) latest — see [[supermemory-analysis]] for structural details. Documented in `skills/supermemory/references/architecture.md` §"Container Tag Isolation" and `skills/supermemory/references/use-cases.md` §7 ("Multi-Tenant SaaS Application") with full TypeScript implementation. Production-deployed in Supermemory's SaaS backend; MCP server exposes `containerTag` as a tool parameter on `memory` and `recall`. Used by all four plugin repos (`claude-supermemory`, `openclaw-supermemory`, `opencode-supermemory`, `hermes-agent`).

## Potential Alternatives

- [[scoped-memory-model]] (mem0) — three named dimensions (user_id, agent_id, run_id) with typed composition. Better for known-ahead-of-time scoping axes; harder to extend.
- **Typed hierarchy** (parent_id references). Explicit parent-child relationships. Allows "walk upward" queries without multiple lookups; adds schema complexity.
- **ACL-per-record.** Each memory has explicit allowed-readers list. Maximum flexibility; maximum overhead; scales poorly.
- **Directory-based isolation.** File-backed memory in per-scope directories. Works for file-based stores; doesn't apply to database-backed.

## Potential Improvements

- **Hierarchical query in a single call.** "Find memories at user-or-team-or-org level" requires three queries today. A single call that walks up the tag hierarchy and merges results would reduce client-side logic.
- **Schema-enforced hierarchy (optional).** A `parentTag` field, populated from naming convention, would let the storage layer surface hierarchical queries natively while keeping the simple flat-tag behavior as the default.
- **Tag-rename discipline.** When an org changes its slug, every tag using it is stale. A rename utility that walks the store and updates tags would be a standard ops requirement at scale.
- **Cross-level deduplication.** Same content stored at team and user level (e.g., user saved it, then team adopted it) is duplicated. An optional dedup pass at query time or write time would help.

## Potential Failure Modes

- **Naming-convention drift.** Consumers are expected to build tags consistently (`org_X_team_Y_user_Z`). If one service writes `orgX_teamY_userZ` (no underscores) and another writes `org-X-team-Y-user-Z` (hyphens), queries miss records. Enforcement has to live in a shared tagging library.
- **Tag-collision at scale.** Flat strings have no collision detection. Two orgs named "acme" both generate `org_acme` tags — their data mixes. Requires unique org slugs or UUIDs in the tag.
- **Query-time scope-escalation bugs.** A user-scope query that accidentally passes an org-level tag returns someone else's data. Needs defense-in-depth (auth-layer enforcement that the caller's user_id is in the allowed tag path).
- **Multiple-query overhead.** Every time a consumer wants "user + team + org" they issue 3 queries. Latency compounds; cost compounds.
- **No query across orgs.** Works as intended for isolation; breaks when a legitimate cross-org query is needed (e.g., "what's the industry-wide best practice?"). Requires a separate "shared" tag space.
