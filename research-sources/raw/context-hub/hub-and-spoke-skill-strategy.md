# The Hub-and-Spoke Skill Strategy

> **Anonymized copy.** The upstream repository is private and its org, product, author,
> tool prefixes, and paths have been replaced with neutral placeholders before this vault
> was shared publicly. Structural content is unchanged.

A technical guide to the skill taxonomy, the build/maintain pipeline, and how the optimizer family, `/dr` (deep-research), `concept-family-explorer`, and `skill-tree-architect` fit together.

**Audience:** engineers and operators who author, optimize, and maintain Claude Code / enterprise skills. This explains *why* the system is shaped the way it is, not just the commands to run.

---

## 1\. The problem this solves

A "skill" is a Markdown file (`SKILL.md`) with YAML frontmatter that the agent's harness can load on demand. The harness does **not** read every skill body up front. At session start it reads only the **frontmatter `description`** of every installed skill and uses those descriptions to decide which skill(s) to pull into context for a given turn.

That single fact drives the entire architecture:

- **The description is the router.** If a skill's description is vague, too broad, or collides with a sibling, the wrong skill fires (or none does).  
- **Descriptions cost context on every turn.** N skills × description length is paid on *every* request, whether or not any skill is used. Left unmanaged, a growing flat list of skills silently inflates the base context cost of every interaction.  
- **Bodies can be arbitrarily large** because they load only when selected — so detail is cheap, but *discoverability* is the scarce resource.

The hub-and-spoke taxonomy is the answer to "how do we keep hundreds of skills' worth of knowledge available without paying for hundreds of descriptions on every turn, and without trigger collisions."

---

## 2\. The two-tier taxonomy

```
                       ┌─────────────────────────────────────┐
   top-level index     │  HUB skill  (e.g. db-platform-expert)    │  ← 1 description in
   (paid every turn)   │  description = domain ROUTER         │     the always-on index
                       │  TRIGGER: broad domain surface       │
                       │  SKIP: → sibling hubs                │
                       └──────────────┬──────────────────────┘
                                      │  loads on demand
                          ┌───────────┴───────────┐
                          ▼                       ▼
              references/spoke-a.md     references/spoke-b.md   ← SPOKES: full detail,
              (deep, specific)          (deep, specific)           zero index cost
```

**Hub** — a single top-level skill whose body is mostly a *routing table*. Its description enumerates the domain surface (broad `TRIGGER:`) and hands off out-of-scope work to sibling hubs (`SKIP: … → <id>`). Examples: `db-platform-expert`, `applied-psychology`, `aws-cloud`, `deep-optimizer`.

**Spoke** — a detailed reference living at `<hub>/references/<spoke>.md`. Spokes carry the real depth. They are **never** indexed individually; the agent reaches them only *after* the hub fires and the hub's routing table points at them.

**Why this works:** a family of \~8–30 related topics costs **one** description in the always-on index instead of 8–30. The hub absorbs the trigger surface; the spokes absorb the detail. The index stays small; depth stays unbounded.

### The ≥8-sibling hub threshold

A family is consolidated into a hub when it has (or is expected to reach) **≥8 sibling skills**. Below that, the skills stay standalone top-level entries — a hub for 3 spokes adds an indirection hop without meaningfully shrinking the index. This threshold is the core rule in `skill-consolidation/HUB-STRATEGY.md`.

---

## 3\. Description caps (the context-budget contract)

Because descriptions are paid on every turn, they are capped on a **two-tier** scale. These caps are enforced by `skill-tree-architect` and checked by `meta-validate.mjs`:

| Tier | Threshold | Severity | Rationale |
| :---- | :---- | :---- | :---- |
| Soft | **\> 1000 chars** | Medium finding | Glean/export cap; description is getting expensive |
| Hard | **\> 1536 chars** | High finding | Harness truncation risk — the router text may be cut |

A description over the hard cap can be silently truncated by the loading harness, which means the `SKIP:` clauses (the part that prevents collisions) may never be read. That is why exceeding 1536 is a High, not a stylistic nit.

### Anatomy of a good description

```
description: >-
  <one-line capability statement>.
  TRIGGER: <comma-separated positive phrasings that SHOULD fire this skill>.
  SKIP: <negative cases> → <sibling-id>; <other case> → <other-sibling-id>.
```

- **Capability statement** — what the skill *is*, not a workflow summary.  
- **`TRIGGER:`** — the positive surface. Tested by the optimizer's trigger-accuracy eval (target ≥9/10 on positive phrasings).  
- **`SKIP:`** — the **peer-deferral** mechanism. Each `→ <id>` is a routing edge that says "this looks close but belongs to that sibling." This is what keeps two adjacent skills from both firing (a *collision*).

---

## 4\. Peer deferral and the cross-hub map

Skills do not exist in isolation; they form a directed graph of deferral edges.

- **`SKIP: … → <id>`** in the description is a *hard* deferral the harness can act on at routing time.  
- **`related_skills:`** in frontmatter and inline `→ <spoke-id>` "cold-spoke pointers" in bodies are *soft* edges used for cross-pollination and navigation.

When a new spoke is created or folded into a hub, those edges can dangle (point at a name that moved). `referents.mjs --repair` rewrites every `→ <spoke-id>` and `related_skills:` entry to the hub-aware form so the graph stays consistent.

This deferral graph is what lets the system stay *crisp* as it grows: every skill knows what it is **not**, and hands those cases off explicitly.

---

## 5\. The lifecycle: how skills are born and maintained

The four headline tools map onto distinct phases of one pipeline. Read this as the mental model the rest of the doc fills in:

```
   ┌────────────────────────┐
   │ concept-family-explorer │  WHAT should exist? Map the family, find the gaps,
   │   (discovery / gaps)    │  score each gap, decide what's worth building.
   └────────────┬───────────┘
                │  loops over each viable gap
                ▼
   ┌────────────────────────┐
   │   /dr  (deep-research)  │  BUILD it. Research the topic to saturation,
   │   (research → skill)    │  synthesize a cited skill/spoke, route it to a hub.
   └────────────┬───────────┘
                │  Phase 2 calls
                ▼
   ┌────────────────────────┐
   │  skill-optimizer (/sko) │  Is the artifact GOOD? Convergence-loop quality gate:
   │   (per-skill quality)   │  trigger accuracy, collision check, caps, fixes.
   └────────────┬───────────┘
                │  after many skills land
                ▼
   ┌────────────────────────┐
   │  skill-tree-architect   │  Is the TREE balanced? Whole-tree audit: caps, hub
   │   (whole-tree shape)    │  balance, misplaced spokes, when to split/spawn hubs.
   └────────────────────────┘
```

The **optimizer family** (next section) is the *quality engine* that `skill-optimizer` belongs to; the same convergence-loop machinery is reused for prose, code, prompts, SQL, and design.

---

## 6\. The optimizer family

All optimizers share one contract defined in `skill-consolidation/convergence-and-severity.md`:

1. **Multi-pass audit** — each pass is a distinct *lens* (e.g. structure, accuracy, voice, security). Passes run in parallel bundles where independent.  
2. **Severity rating** — every finding is rated `Blocker > High > Medium > Low > Nit`.  
3. **Apply every Medium+ fix in place** — not just report; fix.  
4. **Verify gate** — re-render / build / lint / test / re-eval; back out any change that regresses.  
5. **Convergence loop** — re-run the audit; repeat until **no Medium-or-higher finding remains** or a budget/iteration cap is hit (typically 3, raised to 5 if findings are still dropping ≥50% per iteration).

`deep-optimizer` is the **router** for the family (no logic of its own — it picks the right member):

| Member | Alias | Target artifact | Passes | Verify gate |
| :---- | :---- | :---- | :---- | :---- |
| `code-deep-optimizer` | `/cdo` | source files / repos | \~19 | build \+ lint \+ tests |
| `document-critique` | `/ddo` | prose docs (specs, runbooks, KBs) | 0–14 (+10.5, 11.5) | fact-check \+ anti-AI-ism |
| `prompt-deep-optimizer` | `/pdo` | production prompts in code | 16 (5 bundles) | champion-challenger held-out eval |
| `skill-optimizer` | `/sko` | `SKILL.md` files | 15 | trigger eval \+ collision check \+ sync |
| `deep-query-optimizer` | `/dqo` | SQL queries | — | `EXPLAIN`/`EXPLAIN ANALYZE` plan \+ result parity |
| `design-deep-optimizer` | `/deso` | UI/UX & brand screens | 11 | re-render \+ contrast \+ axe |

### skill-optimizer in depth (the one wired into the pipeline)

Its 15 passes (detailed in `skill-optimizer/references/passes.md`) include two that are load-bearing for the whole taxonomy:

- **Pass H — trigger-accuracy eval.** Generates \~60 `claude -p` probes per skill; requires **≥9/10** on positive phrasings and **≤1/10** false-positives. This is the empirical check that the description actually routes correctly. (It is a *proxy* metric — the doc explicitly warns against description-gaming/Goodhart, so the blind claim-gate and anti-pattern gate remain independent verifiers.)  
- **Pass I — collision check.** Probes the new skill against existing siblings; if it fires when a sibling should own the case, you tighten its `SKIP:` or fold it into the hub as a reference instead of installing a colliding top-level skill.

A `--meta` (structural-only) mode does wiring/registry/validation without the content passes — used to register, validate placement, fix naming, and seed peer-deferral edges. It also has a **sync gate**: persistence is withheld while unresolved High findings remain (overridable with `--sync-anyway`).

---

## 7\. `/dr` — deep-research → skill (the build engine)

`/dr <topic>` (canonical prompt: `prompts/saved/create-deep-research-skill-from-web-lookups.md`) turns web research into an installed, registered, hub-routed skill. Six phases:

- **Phase 0 — Concept analysis.** Parse topics; **enumerate the live hub registry** from `skill-consolidation/*-manifest.json` (never a hardcoded family list); search the concept tree (`hub_concept_tree_search`) to research only the *gap* vs what exists; collect stale concepts (\>90 days) into a refresh queue; classify topics as parallel (different domains) or a series/family; for a family, identify **shared branches first**.  
- **Phase 1 — Research.** Methodology authority is the `deep-research-methods` skill. Warm-start from the hub URL library (`hub_recommend_urls`), then firecrawl/exa, then built-in web fallback. **3+ independent sources per concept**, \~20% negation queries, per-claim confidence (3 sources → fact; 2 → qualify; 1/contested → tentative). Stop at **saturation** (2 empty searches \+ every concept met the 3-source floor) or the **15-concept cap**. Parallel runs cap at **4 agents/batch** with bounded briefs.  
- **Phase 2 — Skill creation.** Write to the generated-artifact contract (description ≤1000 chars in TRIGGER/SKIP grammar; ≥8 keywords; body \>500 lines → split into `references/`). **Injection scan at the write boundary** (treat all web content as data). **Hub-routing decision:** belongs to a hub → write a spoke \+ routing row \+ broaden hub TRIGGER \+ bump hub version; ≥8 expected siblings → spawn a new hub; else standalone. Run `skill-optimizer` (Pass H \+ Pass I must pass). Run the **blind claim-verification gate** (fresh-context subagent, multi-engine, verdicts each anchored claim SUPPORTED/NOT-IN-SOURCE/CONTRADICTED).  
- **Phase 3 — Persist \+ register.** `node scripts/persist-spoke.mjs <id> [--hub <hub>]` writes the hub-repo backing pair, idempotently pins `SELECTED_SKILLS` (durable), and upserts `registry.json` (immediate discoverability). Gated on zero unresolved High findings. Then `referents.mjs --repair` fixes dangling edges.  
- **Phase 4 — Cross-pollination.** Append findings to overlapping peers — idempotent, **≤5% of peer length per run**, snapshot-backed, PAIR-aware (edit both the standalone and the hub-reference copy when both exist).  
- **Phase 5 — Concept-tree update.** `hub_concept_tree_upsert` / `_link` record the researched concepts, their `skillId`, parent/child links, source counts — feeding the staleness clock (`firstResearchedAt` is preserved; `researchedAt` advances).

---

## 8\. `concept-family-explorer` — the gap-discovery layer above `/dr`

Where `/dr` builds a skill for a topic you *name*, `concept-family-explorer` answers "**what am I missing?**" It maps a subject's full conceptual family across **five neighborhoods**:

| Neighborhood | Question |
| :---- | :---- |
| **Parent** | What broader domain contains this? |
| **Sibling** | What peers sit alongside it under the same parent? |
| **Child / sub-concept** | What does this decompose into? |
| **Adjacent / cross-over** | What neighboring fields overlap or feed in? |
| **Frontier** | What's emerging / next at the edge of the field? |

It then **scores** each discovered concept (rubric in `references/scoring-rubric.md` — novelty, usefulness, coverage gap), and **loops `/dr` over every viable gap** with a bounded brief until the concept tree **saturates** (loop control in `references/saturation-and-loop-control.md`). It is resumable (`references/run-state-and-resume.md`) and persists results to the hub (`references/repo-persistence.md`).

Use it to *complete coverage* of a domain; use `/dr` directly when you already know the topic.

---

## 9\. `skill-tree-architect` — the whole-tree shape

This is the only tool that reasons about the **entire tree** rather than one skill. It orchestrates (never reimplements) the `skill-consolidation` toolchain:

- **`audit-placement.mjs`** — scans every skill for: description-cap violations (the 1000/1536 tiers), hub balance (hubs that are over-stuffed or too thin), and **cross-hub placement** (a spoke that semantically belongs under a different hub).  
- **`detect-candidates.mjs`** — finds a cluster of ≥8 homeless/standalone siblings that should become a new hub.

It decides **when to split a hub, spawn a new family, or relocate a spoke**, then drives the existing build/fix scripts (`build.mjs`, `fix-crosshub.mjs`, `referents.mjs`) to execute the reshape. `skill-tree-architect` and `concept-family-explorer` are themselves in `exclude-list.mjs` so the tooling never tries to hub *them*.

**Division of labor:** `skill-optimizer` fixes *one* skill's content and seeds *its* deferral edges; `skill-tree-architect` rebalances the *forest* and fixes *cross-hub* placement.

---

## 10\. How they fit together (end-to-end)

```
   "I want to cover domain X well"
                │
                ▼
   concept-family-explorer ──── maps family, scores gaps ───┐
                │                                            │
                │  for each viable gap (bounded brief)       │
                ▼                                            │
            /dr <gap>                                        │
         ├─ Phase 0  hub-aware concept analysis              │
         ├─ Phase 1  research to saturation (deep-research)  │
         ├─ Phase 2  synthesize ──► skill-optimizer (/sko)   │  ← optimizer family
         │                          ├─ Pass H trigger eval   │     (convergence loop)
         │                          ├─ Pass I collision      │
         │                          └─ blind claim gate      │
         ├─ Phase 3  persist-spoke + referents --repair      │
         ├─ Phase 4  cross-pollinate peers (≤5%)             │
         └─ Phase 5  concept-tree upsert ────────────────────┘
                │
                │  after the pack lands (many skills)
                ▼
   skill-tree-architect ── audit caps / hub balance / cross-hub ──► reshape
```

Every artifact that the build engine emits is gated by an optimizer; every batch of artifacts is periodically rebalanced by the architect; the explorer decides what to feed the build engine in the first place.

---

## 11\. Worked examples

**Example A — Add one well-scoped topic.** You need a skill on "queryable encryption (a database-platform topic)." Run `/dr queryable encryption (a database-platform topic)`. Phase 0 matches the `db-operations-expert` hub, so the artifact is written as `db-operations-expert/references/queryable-encryption.md` (a spoke, not a new top-level skill), the hub TRIGGER is broadened, and the hub version is bumped. `skill-optimizer` confirms it doesn't collide with the existing encryption-at-rest spoke. One description cost added to the index: **zero** (it's a spoke).

**Example B — Saturate a new domain.** You want full coverage of "vector databases." Run `concept-family-explorer "vector databases"`. It maps siblings (pgvector, Milvus, Weaviate, Qdrant…), children (HNSW, IVF, quantization), adjacent (RAG retrieval, embeddings), and frontier (disk-based ANN). It scores \~12 gaps, then loops `/dr` over each. Because the family is ≥8 siblings, the first run **spawns a hub**; the rest land as spokes. The whole pack is canonicalized once at the end (`persist-spoke … --sync`), not per skill.

**Example C — The index is bloated.** Routing has gotten mushy and the base context cost is up. Run `skill-tree-architect`. `audit-placement.mjs` flags six descriptions over 1000 chars (two over 1536 — High), a `da-*` hub that's grown to 31 spokes (split candidate), and a "telemetry-pipeline" spoke sitting under the wrong hub. `detect-candidates.mjs` finds nine standalone observability skills that should become an `observability` hub. The architect splits, relocates, spawns the new hub, then runs `referents.mjs --repair` to fix the edges.

**Example D — Improve an existing artifact (any type).** `/sko` a stale skill; `/ddo` a runbook before publishing; `/pdo` a production system prompt that gives inconsistent output; `/cdo` a source file; `/dqo` a slow query; `/deso` a UI screen. Same convergence-loop contract, different lens set.

---

## 12\. Best practices

1. **Let the description do the routing.** Spend effort on `TRIGGER:`/`SKIP:`, not the body, when a skill mis-fires. Keep it under 1000 chars; never let it pass 1536\.  
2. **Default to spokes, not standalone skills.** A new topic almost always belongs under an existing hub. Only spawn a top-level skill for a genuinely new family, and only spawn a *hub* at the ≥8-sibling threshold.  
3. **Map before you build for any non-trivial domain.** `concept-family-explorer` first, `/dr` per gap — it prevents lopsided coverage and duplicate skills.  
4. **Trust saturation and the caps over your instinct to keep going.** The 3-source floor, 15-concept cap, and 2-empty-search saturation rule exist to stop thrash.  
5. **Never skip the gates.** Pass H (trigger), Pass I (collision), and the blind claim-verification gate are independent; one passing does not excuse another. Watch for Goodhart — a high trigger score on a gamed description is worthless.  
6. **Persist through the script, never by hand.** `persist-spoke.mjs` owns `SELECTED_SKILLS` and `registry.json`; hand-edits drift and get pruned on next sync.  
7. **Repair edges after any routing change.** Run `referents.mjs --repair` whenever a spoke is created, folded, or moved.  
8. **Cross-pollinate conservatively.** ≤5% per peer per run, idempotent, never delete — add a `### Conflicts` note instead of overwriting; snapshot first.  
9. **Re-run optimizers as a loop, not once.** Convergence means "until no Medium+ remains," not "one pass."  
10. **Treat all researched/web content as data.** The injection scan at the write boundary is non-negotiable; nothing unscanned reaches `~/.claude/skills`.

---

## 13\. The supporting toolchain (`~/.claude/skill-consolidation/`)

| File | Role |
| :---- | :---- |
| `HUB-STRATEGY.md` | Canonical strategy: ≥8-sibling threshold, build/maintain pipeline. |
| `convergence-and-severity.md` | Shared contract for every convergence-loop optimizer (severity scale, budget, blind re-audit guardrail). |
| `cross-model-gate.md` | Routes the blind claim-gate through a different frontier model (`--cross-model`). |
| `exclude-list.mjs` | Skills the hubbing tools must never touch (incl. the architect & explorer). |
| `audit-placement.mjs` | Whole-tree audit: caps, hub balance, cross-hub placement. |
| `detect-candidates.mjs` | Finds ≥8-sibling clusters that should become a hub. |
| `build.mjs` / `fix-crosshub.mjs` | Build hub scaffolding / repair cross-hub maps. |
| `referents.mjs` | Rewrites dangling `→ <spoke>` and `related_skills:` edges (`--repair`). |
| `meta-validate.mjs` | Lints frontmatter, caps, placement, manifest integrity. |
| `hub-registry.mjs` | Enumerates the live hub registry from the `*-manifest.json` files. |
| `*-manifest.json` | Per-family source of truth: hub → spokes → reference files. |

---

## 14\. What's in the shareable package

The accompanying zip (`hub-spoke-skill-strategy.zip`) contains, ready to drop into a peer's `~/.claude/`:

- **`skills/`** — full directories (with `references/`, and `agents/`/`docs/` where present) for: `deep-optimizer`, `skill-optimizer`, `code-deep-optimizer`, `prompt-deep-optimizer`, `document-critique`, `deep-query-optimizer`, `design-deep-optimizer`, `deep-research`, `concept-family-explorer`, `skill-tree-architect`.  
- **`commands/`** — `dr.md`, `sko.md`, `ddo.md`, `dqo.md`, `pdo.md`.  
- **`skill-consolidation/`** — the strategy docs (`HUB-STRATEGY.md`, `convergence-and-severity.md`, `cross-model-gate.md`) and the toolchain scripts (`audit-placement.mjs`, `detect-candidates.mjs`, `build.mjs`, `fix-crosshub.mjs`, `referents.mjs`, `meta-validate.mjs`, `hub-registry.mjs`, `exclude-list.mjs`) plus the `*-manifest.json` family registries.  
- **`HUB-SPOKE-SKILL-STRATEGY.md`** — this document, at the archive root.

**Note on paths:** several scripts assume `~/.claude/...` absolute paths and the `persist-spoke.mjs` durability step lives in the `context-hub` repo (not the `~/.claude` tree), so it is intentionally *not* in this archive — the package is for understanding and running the audit/build tools, not a turnkey clone of the repo.

---

# Part II — The `context-hub` backing store

Part I described the *authoring* side of the system: the `~/.claude/skills` tree, the optimizer family, `/dr`, `concept-family-explorer`, and `skill-tree-architect`. Those tools all read and write a working copy of the skill pack on a single operator's laptop.

**`context-hub` is the durable, shareable backing store and runtime for that pack.** It is the git-tracked source of truth that survives a laptop wipe, the place a teammate clones to get the same skills, and the MCP server that exposes the pack to *any* agent — not just the one editing files locally.

**Repository:** (private enterprise repo — anonymized)

---

## 15\. What the hub is (and is not)

The hub is a **single-package Node.js repository** that combines two things behind one version number:

1. **A generated skill pack** — normalized skill manifests, migrated context docs, prompt templates, and a set of JSON catalogs (skills, prompts, MCP/repo/shared/URL libraries, roles, concepts, and coding patterns), all regenerated by a sync pipeline.  
2. **A TypeScript MCP server** — transports, a registry loader, a service layer, and telemetry that expose the pack to MCP clients over stdio or loopback HTTP.

| It is | It is not |
| :---- | :---- |
| The durable git home of the skill pack (clone-to-share) | The place you hand-edit skill bodies (that's `~/.claude/skills`) |
| An MCP server that serves skills/prompts/catalogs to agents | A second copy of the harness's own skill loader |
| The persistence target of `/dr` Phase 3 (`persist-spoke.mjs`) | A turnkey mirror of `~/.claude` — `persist-spoke.mjs` lives here, not in the `~/.claude` tree |
| A telemetry \+ dashboard surface for every tool call | A general-purpose monorepo (it is intentionally local-first today) |

The relationship to Part I is a **two-tree** model. `~/.claude/skills` is the *editable working tree* the authoring tools touch directly; `context-hub/local-sources` plus the generated `skills/registry.json` is the *canonical tree* that gets committed, shared, and served. The sync pipeline reconciles the two.

---

## 16\. Repository shape

```
context-hub/
├── mcp-server/        TypeScript MCP transports, registry loader, service, tools, telemetry
├── scripts/           sync pipeline + persist-spoke + import/validate helpers
├── skills/            normalized manifests, migrated contexts, skills/registry.json
├── local-sources/     repo-local custom skill sources folded into the pack
├── prompts/           generated prompt templates/bundles + prompts/saved/ registry
├── mcp-library/       catalog of known MCP servers
├── repo-library/      catalog of org-backed repos/tools
├── shared-library/    catalog of reusable code modules
├── url-library/       catalog of reference URLs (warm-start for /dr Phase 1)
├── roles/             persona registry (auto-load skill sets per role)
├── concept-tree/      researched-concept graph + staleness clock
├── coding-patterns/   reusable code-pattern entries
├── reports-library/   generated report registry
├── file-analysis/     per-file analysis store + telemetry.jsonl
├── agents/  hooks/     repo-local subagents and hooks
├── tests/             Vitest suites for the generator and the service layer
└── docs/              generated inventories + handwritten operational docs
```

Two source-of-truth boundaries matter:

- **Upstream docs feed the generator** (`scripts/` → `skills/`, `prompts/`, generated `docs/`). Anything carrying the sync banner is generated — fix the generator, not the output.  
- **Registries feed the service layer.** `skills/registry.json`, the `prompts/` registries, and the six library `registry.json` files are what the MCP server actually reads at runtime.

---

## 17\. The sync pipeline (`npm run sync:skills`)

`node scripts/sync-skill-pack.mjs` is the generator. It imports the upstream skill sources (absolute paths declared in `scripts/skill-pack.config.mjs`) and regenerates the local manifests, context docs, prompt templates, and the generated docs under `docs/`.

The contract that ties Part I to Part II runs through one constant in that config:

```
SELECTED_SKILLS   ← the allow-list of skills the pack ships
```

A skill is included in the generated pack **only if it appears in `SELECTED_SKILLS`**. Anything not on the list is *pruned* on the next sync. This is the durability guarantee behind `/dr` Phase 3: `persist-spoke.mjs` idempotently inserts the new skill's id into `SELECTED_SKILLS` (below an auto-managed marker) so the sync will never drop it, and writes the `local-sources/<id>/{manifest.yaml, context.md}` backing pair that the generator consumes.

```
~/.claude/skills/<id>/SKILL.md          (authoring tree — edited by the optimizers/dr)
            │   persist-spoke.mjs
            ▼
local-sources/<id>/{manifest.yaml,context.md}   +   SELECTED_SKILLS += <id>
            │   npm run sync:skills
            ▼
skills/registry.json  +  skills/<id> context        (canonical tree — committed & served)
            │   registry.ts loads at server start
            ▼
hub_* MCP tools                                      (served to any agent)
```

---

## 18\. Runtime architecture

The server has **two transports over one service implementation**:

```
        npm run sync:skills
upstream docs ──────────────► generated registries (skills/prompts/libraries/roles)
                                        │
                                        ▼
   registry.ts ─► service.ts ─► server.ts ─► index.ts   (stdio transport)
       (load)      (logic)      (register)  └► http.ts   (loopback HTTP /mcp + /healthz)
                                        ▲
                                  telemetry.ts (wraps every tool)
```

- **`registry.ts`** loads the skill/prompt/saved-prompt registries and their text assets into an in-memory cache at start.  
- **`service.ts`** implements search, recommendation, provenance lookup, prompt optimization, and the file-backed save operations for the prompt/MCP/URL libraries.  
- **`server.ts`** registers the MCP tools, plus a dynamic *resource* per skill/prompt asset and a *prompt* entry per saved prompt. Every tool is wrapped by `instrumentedRegisterTool` from `telemetry.ts` — `server.registerTool` is never called directly.  
- **`telemetry.ts`** is the middleware: it captures per-call status, duration, redacted args, console output, and suggested fixes; persists to `file-analysis/telemetry.jsonl`; and exposes the in-memory history through `hub_get_call_history`, `hub_resync_call`, and `hub_get_call_card`.  
- **`http.ts`** wraps the server in a Streamable HTTP transport on `127.0.0.1:3939` and is treated as a **trusted loopback** surface. `.mcp.json` registers exactly this endpoint as the `context_hub` server.

Any change to a tool must land in three places together — `service.ts`, `server.ts`, and `tests/mcp-server.test.ts` — and also appear in `docs/tool-inventory.json`. The `package.json` and `mcp-server/src/constants.ts` versions stay aligned on every change.

---

## 19\. The `hub_*` MCP tool surface

The server exposes the pack as a family of `hub_*` tools. They fall into groups that mirror the catalogs:

| Group | Representative tools | What it serves |
| :---- | :---- | :---- |
| **Skills** | `hub_list_skills`, `hub_get_skill`, `hub_search_skills`, `hub_recommend_skills`, `hub_build_skill_bundle` | The skill pack — list/fetch/rank/bundle skills and their contexts |
| **Prompts** | `hub_list_prompts`, `hub_get_prompt`, `hub_recommend_prompts`, `hub_optimize_prompt`, `hub_save_prompt`, prompt-variant tools | Saved prompts, templates, the optimizer entry point, and A/B variants |
| **Libraries** | `hub_*_mcp_servers`, `hub_*_repo_libraries`, `hub_*_shared_libraries`, `hub_*_urls` | The MCP / repo / shared-code / URL catalogs (search \+ recommend) |
| **Roles** | `hub_role_list`, `hub_role_recommend`, `hub_role_resolve_skills` | Personas → the auto-load skill set for that persona |
| **Concept tree** | `hub_concept_tree_list/get/upsert/link/search` | The researched-concept graph \+ staleness clock that `/dr` and CFE read/write |
| **Coding patterns** | `hub_coding_pattern_search/recommend/save` | Reusable code patterns extracted from repos |
| **File analysis** | `hub_save_file_analysis`, `hub_list_file_analyses`, `hub_get_file_analysis_state` | Per-file summaries \+ change-hash state for repo audits |
| **Dependency / staleness** | `hub_dependency_graph`, `hub_impact_analysis`, `hub_staleness_scan` | Cross-catalog edges, blast-radius, and staleness reports |
| **Telemetry / ops** | `hub_get_call_history`, `hub_resync_call`, `hub_get_call_card`, `hub_ops_*` | The operational dashboard for every instrumented call |

Two distinctions matter when choosing a tool: **`search_*` is substring/metadata matching** ("find a known item"), while **`recommend_*` is relevance ranking** ("rank for a described task"). Use search when you know the id/term; use recommend when you are describing a need.

---

## 20\. How the optimizers, research, and family skills bind to the hub

The Part I tools and the Part II hub are two halves of one loop. The authoring tools produce and refine artifacts; the hub makes them durable, shareable, and queryable.

- **The optimizer family** edits skills in the authoring tree. `skill-optimizer` (`/sko`), after its convergence loop passes, calls `persist-spoke.mjs` to write the canonical backing pair and pin `SELECTED_SKILLS` — that is the moment a `~/.claude` edit becomes a committed hub artifact. Its **sync gate** withholds persistence while unresolved High findings remain.  
- **`/dr` (deep-research)** is the hub's primary writer. Phase 0 enumerates the *live* hub registry (never a hardcoded list) and searches the **concept tree** (`hub_concept_tree_search`) so it only researches the gap versus what the hub already holds. Phase 1 warm-starts from the hub's **URL library** (`hub_recommend_urls`). Phase 3 persists via `persist-spoke.mjs` and upserts `skills/registry.json` for immediate discoverability. Phase 5 records the researched concepts back into the concept tree, advancing the staleness clock.  
- **`concept-family-explorer`** reads the concept tree to know what is already covered and loops `/dr` over the gaps — so the hub's concept graph is both an input (what exists) and an output (what was just researched) of every run.  
- **`skill-tree-architect`** operates on the authoring tree's shape, but the result is only *durable* once the affected skills are re-persisted and `npm run sync:skills` regenerates the canonical pack. A tree reshape that is never synced exists only on one laptop.

The through-line: **the concept tree and `SELECTED_SKILLS` are the two shared-state artifacts** that let the stateless authoring tools coordinate across runs and across operators. The hub owns both.

---

## 21\. Examples and use cases

**Example E — A teammate onboards.** A new engineer clones `(private enterprise repo — anonymized)`, runs `npm install`, `npm run build`, and `npm run mcp:server:http`, then points their agent's `.mcp.json` at `http://127.0.0.1:3939/mcp`. They now have the same skill pack, prompt library, and catalogs the author has — without copying anyone's `~/.claude` tree.

**Example F — An agent asks the hub instead of guessing.** Mid-task, an agent needs to know whether a skill exists for "cloud private endpoints." It calls `hub_recommend_skills "cloud private-endpoint networking"` and gets `db-cloud-expert` ranked first, with the routing context — no local file access required. This is the hub acting as a *remote* skill index for agents that do not run on the author's laptop.

**Example G — `/dr` closes a gap durably.** Running `/dr "vector quantization"` researches the topic, writes `db-cloud-expert/references/vector-quantization.md` in the authoring tree, then Phase 3 runs `node scripts/persist-spoke.mjs vector-quantization --hub db-cloud-expert`. That pins `SELECTED_SKILLS`, writes the `local-sources` pair, and the next `npm run sync:skills` bakes it into `skills/registry.json`. A teammate who pulls `main` now has the spoke.

**Example H — Debugging a flaky tool.** A `hub_*` call returns odd output. The operator runs `hub_get_call_card` for that tool to see the last call's status, duration, redacted args, and console output, then `hub_resync_call` to replay it with the original in-memory args — all from the telemetry the middleware captured, with no code changes.

---

## 22\. Best practices for the hub

1. **Edit upstream, not the generated output.** If a file carries the sync banner, change the generator or the `local-sources` source — your edit to the generated copy is overwritten on the next `npm run sync:skills`.  
2. **Let `persist-spoke.mjs` own `SELECTED_SKILLS` and `registry.json`.** Hand-edits drift and get pruned. The script is idempotent and safe to re-run.  
3. **Keep the three tool-touch-points in sync.** A new or changed tool lands in `service.ts`, `server.ts`, and `tests/mcp-server.test.ts` together, and is reflected in `docs/tool-inventory.json`.  
4. **Never bypass telemetry.** Register tools through `instrumentedRegisterTool`, never `server.registerTool` directly, so every call stays logged and dashboard-visible.  
5. **Treat the HTTP daemon as loopback-only.** Document any security-impacting transport change before merging; the server assumes a trusted local client.  
6. **Bump the version in lockstep.** `package.json`, `package-lock.json`, and `mcp-server/src/constants.ts` move together on every committed change.  
7. **Prefer `recommend_*` for described needs, `search_*` for known ids.** Picking the wrong one is the most common reason a hub query returns nothing useful.  
8. **Run the focused test after a surface change.** `npx vitest run tests/mcp-server.test.ts` after MCP changes; `npx vitest run tests/skill-pack.test.ts` after sync-pipeline changes.  
9. **Re-sync after any authoring-tree reshape.** A `skill-tree-architect` rebalance is not durable until the affected skills are re-persisted and the pack is regenerated.  
10. **Follow the workflow log rule.** Append the request to `prompts.md`, update `memory.md`, and bump the patch version on every repository change.

---

## 23\. Repository

The full source — MCP server, sync pipeline, skill pack, and its catalogs — lives at:

(private enterprise repo — anonymized)

Clone it, run `npm install && npm run build`, start the loopback server with `npm run mcp:server:http`, and point an MCP client at `http://127.0.0.1:3939/mcp` (or check health at `http://127.0.0.1:3939/healthz`).  
