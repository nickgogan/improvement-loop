---
type: "extension-proposals-report"
target_system:
  - "improvement-loop"
generated_by: "/extract-artifacts"
date: "2026-07-13"
identification_report: "agent-design-patterns.harvest-queue"
total_rule_skill_candidates: 1
proposals_emitted: 1
no_match_passthrough: 0
forms_scanned:
  - "rules"
---

# Extension Proposals — 2026-07-13

One rule candidate scanned (harvest-queue promotion mode, DD-101, single row). The DD-97 corpus scan over `extracts/rules/` found a strong semantic match against the existing cache-stability rule family; one extension proposal is emitted and zero findings pass through to drafting. Source: `agent-design-patterns.harvest-queue.md` row `cache-stable-progressive-disclosure-catalog::rule::byte-stable-disclosure-catalog` (Status `nick-approved`). Forms scanned: rules. Per DD-97 §Rules #3 this report proposes only — no existing artifact is modified here; Nick rules the merge target.

## Proposals

### cache-stable-progressive-disclosure-catalog

**Form:** rule
**Existing artifact (primary match):** [[never-mutate-cached-prompt-prefix]]
**Secondary matches:** [[never-inline-ephemeral-into-cached-layers]]

**Codifier recommendation:** extend existing

**Why this match:** `never-mutate-cached-prompt-prefix` already declares itself the parent rule of the cache mechanics — "all are special cases of 'never touch the prefix'" — and explicitly names *static tool sets* as one such special case. The candidate is another special case of exactly that family: an always-injected progressive-disclosure catalog (skill table, tool index, deferred-capability list) must render byte-identical every turn so the prefix cache stays warm. Both rules share the same invariant (prefix byte-identity across turns), the same enforcement check (byte-equality of the rendered surface across consecutive requests), and the same observable signal (provider cache hit-rate). The secondary match, `never-inline-ephemeral-into-cached-layers`, is the sibling assembly-time rule (keep dynamic content out of cache-marked blocks); the candidate's catalog surface is a concrete instance of a segment that naively becomes ephemeral-on-load and must be held stable instead.

**Diff sketch:**

Proposed appended Evidence row on `never-mutate-cached-prompt-prefix` (citing the new source finding alongside the original `append-only-context-updates-system-reminder-injection`):

> Pydantic AI v2.9.0's deferred-capability loader (`_deferred_capability_loader.py`) renders its `load_capability` catalog as a dynamic instruction that deliberately lists *every* deferred capability every turn — including already-loaded ones — so the rendered prefix stays byte-identical and the prompt cache stays warm; redundant loads are bounced with a cheap `ModelRetry` rather than mutating the catalog. In-code rationale: "one occasional wasted retry is far cheaper than busting the prefix cache on every load." Source finding: [[cache-stable-progressive-disclosure-catalog]] (Medium / practitioner-documented). This is a production instance of the parent rule's "static tool sets" special case, extended to a *growing-knowledge* catalog surface.

Proposed body delta (a named special case under §Rationale, or a short §Special Cases addition): a catalog surface that accumulates loaded state must NOT shrink as items load (the naive disclosure move that removes loaded entries rewrites the prefix and busts the cache every time the agent learns something). The catalog-stable tactic: (a) re-list every catalog entry every turn regardless of load state; (b) reject redundant re-loads with a cheap retry rather than mutating the catalog; (c) persist loaded state in message history so resumed runs recover it without catalog mutation. This is a genuinely distinct sub-claim from the original finding's system-reminder-injection mechanism — it addresses the dynamic-catalog case the parent rule's tool-set clause does not spell out.

**Notes:** The candidate is a true special case of the primary match's stated family, so *extend* is the honest recommendation; however, the catalog-specific tactic (re-list-don't-shrink + bounce-redundant-load) is a distinct enforceable sub-claim, so Nick may reasonably rule *create new* (a dedicated `byte-stable-disclosure-catalog` rule scoped to catalog/index surfaces) instead. Both are coherent; the choice is a granularity call for Nick. Per DD-97 v1 the merge/creation is a manual act — this skill does not auto-apply.
