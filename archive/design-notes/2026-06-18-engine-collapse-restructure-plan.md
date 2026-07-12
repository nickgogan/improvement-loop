# Plan: Collapse MetaSystem into one self-evolving engine

## Context

The workspace was built as a federation: a `meta-system` "governance + knowledge layer" governing three peer systems (Household OS, Claude Build, Improvement Loop). That premise has dissolved:

- **Household OS** is moving to Notion (Notion custom agents over household data) — it leaves the markdown/fractal machinery and becomes a *consumer* the engine helps design, not a peer.
- **Claude Build** (a coding-agent harness) is being retired — the coding-harness market is saturated (GSD, BMAD, OpenSpec, Antigravity, Claude Code itself); reinventing it is low-value. Its opinionated-stack intent (Python / OpenAPI-first / SOA) becomes *knowledge artifacts* the engine can draw on, not a separate system.
- That leaves **Improvement Loop** as the only live system. "Meta-system governing peers" now governs one peer plus itself — overhead that fails IL's own Rule 11 (abstractions must earn their keep).

**Intended outcome:** one engine — research at the bottom, per-artifact assess/design in the middle, whole-system composition at the top, a small charter at the root — that produces and audits agentic systems of any kind, grounded in research and able to self-evolve. Validated against a 2026 agent-taxonomy review (layered model; sparse design space → capture clusters, not grids; evaluation/feedback as load-bearing for self-evolution).

This restructure is large and touches governance DDs, two Owner agents, ~20 CLAUDE.md files, skill path references, and Obsidian links. It is staged so the repo is never left in a broken intermediate state.

---

## End-state architecture

```
MetaSystem/                         (workspace / Obsidian vault — name unchanged)
├── CHARTER.md                      ← NEW: vision, mission, purpose, values, trajectory signals
├── CLAUDE.md  +  .claude/rules/    ← workspace operating law (human gate, spec-before-build, safety) — stays
├── systems/
│   └── improvement-loop/           ← THE ENGINE (folder name unchanged to avoid ~16k-file path churn)
│       ├── governance/             ← engine's own operating rules (agent/boundary/pipeline/knowledge) — stays
│       ├── knowledge/              ← NEW (absorbs meta-system/knowledge): patterns, guides, templates,
│       │   │                          reference  + design-wisdom (fractal-pattern, DBDO, vocabulary)
│       │   └── schematics/         ← NEW artifact form: system-configuration archetypes
│       ├── research-findings/ …    ← bottom altitude (evidence) — unchanged
│       ├── operations/references/librarian/  ← middle altitude (per-axis concept docs) — unchanged
│       ├── .claude/skills/         ← assess-*/design-* (middle) + audit-system, design-harness (top)
│       ├── app/                    ← NEW (fractal completion): transcript-fetcher, pdf-to-markdown tools
│       └── agents/owner/           ← single merged Owner
├── archive/{claude-build, household-os, meta-system}
└── .claude/  (cross-system skills, single Owner subagent)
```

**The three altitudes** (now with concrete top-altitude content):
- **Bottom — research:** findings, indexed by the dimension registry (incl. Dim 7 Evaluation, Dim 9 Governance).
- **Middle — per-artifact:** Librarian concept docs (the *configuration axes*: agent/skill/prompt/harness/memory) + `/assess-*` / `/design-*`. Single-agent schematics live here.
- **Top — whole-system:** the **schematic library** + `/audit-system` and (to-be-built) `/design-harness`. Multi-agent / system-level schematics live here.

**Charter (root):** one short doc — vision, mission, purpose, values, and explicit **trajectory signals** ("how do we know we're on track vs. wandering?"). Not a rulebook. Operating rules already live in `CLAUDE.md` / `.claude` / IL `governance/`; design-wisdom (fractal-pattern, DBDO pipeline, vocabulary) becomes plain knowledge.

**Schematics (new artifact form):** an evidence-grounded mapping `demand → configuration`.
- *Indexed by demand:* function (coding / research / operations / assistant) × scope/lifespan (personal-persistent ↔ project-bound) × non-functionals (data boundary, reliability, autonomy need, cost).
- *Layered configuration internals* (by volatility): **capability + memory core** → coordination/architecture → **autonomy (5-level: operator→collaborator→consultant→approver→observer)** → deployment/hosting (Notion-embedded / local+local-LLM / provider-API / harness). Cores are reusable across schematics.
- *First-class evaluation & feedback layer* (required): how the agent is evaluated (outcome vs process; independent vs self-report) and its feedback mechanism (internal / external / multi-agent / human). A schematic without this is not self-evolving.
- *Links:* `grounded_in` → findings; `composed_of` → artifacts/templates; light risk annotation.
- *Populated by capturing recurring named clusters* (e.g. "project-scoped coding workcell: Python/OpenAPI/SOA, Claude Code harness"), **not** the full axis cross-product (design space is sparse).
- *Inside the engine's drift loop:* schematics are added to `/detect-drift` scope so new Dim-7/Dim-9 findings flag dependent schematics for re-evaluation.

---

## Phase 1 — Structural collapse

Each step = one atomic commit; co-updates listed must land in the *same* commit to avoid breakage. Use `git mv` throughout (preserves history; carries the 52 tracked transcript files and all DD/governance/knowledge `.md`).

**Step 0 — Spec corrections (verified during planning, no commit):**
- Survivor Owner subagent = workspace-root `/.claude/agents/owner.md` (`name: owner`). IL's `systems/improvement-loop/.claude/agents/` is **empty** — there is no IL-local owner subagent file to keep.
- `/design-harness` does **not** exist (roadmap item only) — nothing to move; it becomes a capability to build later.
- Assign homes for meta-system artifacts not covered elsewhere: `project-management/design-notes/`, `capability-roadmap.md`, `audit-reports/`, `operations/handoffs/`, `agents/`, `app/`, `HUB.md`, `CLAUDE.md`.

**Step 1 — Relocate active tools out of claude-build (before archiving).**
`git mv incubator/claude-build/app/transcript-fetcher → systems/improvement-loop/app/transcript-fetcher` and `…/pdf-to-markdown → systems/improvement-loop/app/pdf-to-markdown` (the root `/pdf-to-markdown` skill depends on the claude-build copy of `convert.py`).
*Co-update same commit:* `transcript-fetcher/SKILL.md` (8 path refs), `research-loop/SKILL.md` (lines 198/200/280/281), `source-triage/SKILL.md`, root `pdf-to-markdown/SKILL.md` (8 refs), `.gitignore:19-20`, and `research-findings/five-durable-verticals-ai-cannot-replace.md:59`.

**Step 2 — Archive dormant systems.**
`git mv incubator/claude-build → archive/claude-build`; `git mv incubator/household-os → archive/household-os`. Before/within the household-os move, lift `knowledge/reference/schemas/*.json` (7 Notion schemas) and `knowledge/reference/architecture/*` into `systems/improvement-loop/knowledge/reference/` as design substrate for the Notion build (see Open Decisions).
*Co-update:* root `CLAUDE.md` Workspace Structure table; `systems/CLAUDE.md` status table; `HUB.md` lines 21–22.

**Step 3 — Move knowledge into the engine.**
`git mv systems/meta-system/knowledge → systems/improvement-loop/knowledge`.
*Co-update same commit:* `bootstrap/SKILL.md` (4 refs), `preflight/SKILL.md` (4 refs), root `CLAUDE.md:67-68`, `.claude/agents/librarian.md:37`, `synthesize-guide/SKILL.md` (5 refs), IL `CLAUDE.md:89,196`, codifier/librarian/researcher `agent.md` deploy refs, `handoff-protocol.md:169`, `pipeline-rules.md:37`, `extracts/guides/CLAUDE.md:5`, the 3 Dataview `FROM "systems/meta-system/knowledge/…"` strings inside the moved `_index.md` files, `.obsidian/graph.json:15`.
*Semantic rewrite (the key landmine):* the invariant "IL never deploys, only stages to meta-system/knowledge" (DD-29/41, `boundary-rules.md:32`, codifier/librarian/researcher `agent.md`) becomes incoherent once knowledge lives inside IL. Rewrite it: **the human gate stays** (Nick still approves what gets codified), but the deploy *target* is now `systems/improvement-loop/knowledge/` — an in-engine promotion, not a cross-system write. Record via DD (see Phase 1 governance).

**Step 4 — Author the charter; demote design-wisdom to knowledge.**
Create `CHARTER.md` at workspace root (vision/mission/purpose/values/trajectory-signals), drawing the durable content out of `meta-system/governance/{values,principles,constitution}.md`. Move `fractal-pattern.md`, the DBDO pipeline (`principles.md`), and `vocabulary.md` into `systems/improvement-loop/knowledge/reference/` as design-wisdom (consumed, not enforced).
*Co-update same commit:* `.claude/rules/governance.md` (lines 8,15,28 — repoint constitution/vocabulary refs to charter + knowledge), root `CLAUDE.md` (lines 21,31,65-67), `.claude/agents/owner.md:61`, `bootstrap/SKILL.md:180`, **`translate-governance/SKILL.md:65-69,210`** (its entire governance-source input set moves — repoint to charter + IL governance), `system-audit/SKILL.md:115`, the 5 IL governance-rule files' `derived_from:` frontmatter (~16 refs), `governance/proposals/CLAUDE.md:40`, `HUB.md:54-56` (convert to basename wiki-links so they survive), `.obsidian/graph.json:11`.

**Step 5 — Merge PM data into the engine.**
This is a **merge** (IL already has `design-decisions/`, `implementation-backlog/`, `design-notes/`, `operations/system-log/`) — check DD/IB number collisions first. `git mv` the meta-system `design-decisions`, `implementation-backlog`, `operations/system-log`, `design-notes`, and `capability-roadmap.md` into the corresponding IL folders.
*Co-update same commit:* `dd/SKILL.md:25`, `ib/SKILL.md:25`, `sl/SKILL.md:22`, `track/SKILL.md:26,35,222`, `governance-audit/SKILL.md:32,40,48,59`, `session-handoff/SKILL.md:45`, `.claude/settings.local.json:78`. **Decision:** the "Cross-System" routing bucket folds into `improvement-loop` (one engine) — update these skills' system→bucket maps accordingly. DD↔DD cross-cites are by number and survive the merge.

**Step 6 — Merge the two Owners; delete the symlink.**
Fold any unique MetaSystem-Owner responsibilities (charter stewardship, knowledge-vault maintenance) into the narrative `systems/improvement-loop/agents/owner/agent.md` and the root `/.claude/agents/owner.md`. `rm .claude/agents/meta-system-owner.md` (symlink) and `git rm systems/meta-system/.claude/agents/owner.md`. No `settings.json` references exist; only dissolving meta-system CLAUDE.md files mention `meta-system-owner`.

**Step 7 — Dissolve the meta-system shell.**
Archive remaining `systems/meta-system/` content (`CLAUDE.md`, `HUB.md`, `agents/`, `app/`, `audit-reports/`, `operations/handoffs/`) to `archive/meta-system/`, then remove the empty directory.
*Co-update:* root `CLAUDE.md:15` (drop the meta-system row), `HUB.md:19`. Move the `audit-system` skill: `git mv systems/meta-system/.claude/skills/audit-system → systems/improvement-loop/.claude/skills/audit-system` (its IL refs are absolute and survive; refresh its "MetaSystem's composition layer" self-description).

**Step 8 — Governance reset (use DD-44 supersession).**
One consolidating "architecture reset" DD that supersedes DD-32 (multi-system decomposition), DD-45 (meta-system as separate knowledge layer), DD-46 (per-system-architect pipeline); and amends DD-50 (governance home → charter + knowledge), DD-55/56/59 (Cross-System bucket folds into the engine), DD-52 (engine becomes fractal-complete; charter exception noted). Plus targeted new DDs: (a) single-engine + three-altitude architecture; (b) charter concept + trajectory signals; (c) Claude Build retirement + Household-OS-to-Notion direction. (See Open Decisions for DD-surgery weight.)

---

## Phase 2 — Schematics + evaluation/feedback layer

Done after the collapse is stable. Introduce the new top-altitude content.

1. **Define the schematic form** in `systems/improvement-loop/knowledge/schematics/` — a finding-like markdown shape with frontmatter for: demand index (function × scope × non-functionals), the layered configuration (capability+memory core → coordination → 5-level autonomy → deployment), the **required evaluation+feedback layer**, `grounded_in` / `composed_of` links, risk + maturity. Add an `_index.md`. Add the new **execution-surface axis** (Claude Code / local+local-LLM / provider-API / Notion-embedded) to the Librarian concept-doc set; let the rest of the axis vocabulary stay emergent from existing concept docs (`agent.md`, `harness.md`, `memory.md`).
2. **Bring schematics into the self-evolution loop:** extend `/detect-drift` scope to schematics (re-flag when `grounded_in` findings move); confirm Dimension 7 (Evaluation) and Dimension 9 (Governance) queries feed schematic re-evaluation; note schematics as input to `/solicit-proposals` reflection rounds.
3. **Seed 2–3 cluster archetypes** as the first real schematics (e.g. "project-scoped coding workcell: Python/OpenAPI/SOA · Claude Code harness · supervised"; "personal household assistant: Notion-embedded · provider model · workspace memory · scheduled · approver-level"). Single-agent ones tagged middle-altitude; compositions tagged top-altitude.
4. **Wire the Librarian Builder mode** to match a demand profile to a schematic (or compose one from axes + findings when none fits) — extend `/ask-kb` Builder path.

---

## Critical files

- `systems/improvement-loop/.claude/skills/translate-governance/SKILL.md` — entire governance-source input set moves (Step 4).
- `systems/improvement-loop/.claude/skills/transcript-fetcher/SKILL.md` + `research-loop/SKILL.md` — 12 hardcoded tool paths (Step 1).
- `systems/improvement-loop/governance/boundary-rules.md` — encodes the IL-never-deploys invariant that must be rewritten (Step 3).
- `.claude/skills/{dd,ib,sl,track,governance-audit}/SKILL.md` — Cross-System routing → engine (Step 5).
- `CLAUDE.md` + `.claude/rules/governance.md` — workspace operating law + constitution/charter path refs (Step 4).
- `systems/improvement-loop/CLAUDE.md` — identity rewrite: from "primary downstream consumer = MetaSystem" to "the engine"; drop the meta-system consumer framing; update Pipeline deploy target and Fractal Compliance table (gains `app/`, `knowledge/`).

## Reuse (don't rebuild)

- `/detect-drift`, `/process-feedback`, `/solicit-proposals`, `/reassess-priorities` — the existing self-evolution machinery; extend scope to schematics rather than build new.
- Librarian concept docs (`operations/references/librarian/{agent,harness,memory,skill,prompt}.md`) — already the per-axis vocabulary; add only the execution-surface axis.
- `research-dimensions.md` Dimension 7 (Evaluation) + Dimension 9 (Governance) — already harvest eval/feedback knowledge; no new dimension needed.
- `git mv` for every relocation; `git rm` the symlink (never leave it dangling).

---

## Locked decisions (confirmed 2026-06-18)

1. **Household OS content:** **archive + extract refs** — archive `household-os/`, but lift its 7 Notion schemas + architecture docs into `knowledge/reference/` as Notion-design substrate.
2. **DD-surgery weight:** **one consolidating "architecture reset" DD + a few targeted new DDs** (Step 8).
3. **Engine folder name:** **keep `systems/improvement-loop/`** (renaming or dissolving `systems/` is a ~16k-file path migration; deferred as optional cosmetic cleanup).
4. **Execution mode:** **step-by-step with gates** — execute Phase 1 one numbered step at a time, pausing for review/commit approval between steps. Do not start Phase 2 (schematics) until Phase 1 is verified and reported.

---

## Verification

This is a docs/structure repo — verification is reference-integrity, not code tests.

1. **No dangling paths:** `git grep -n "systems/meta-system"` returns only intended archive/historical references (no live skill/rule/CLAUDE.md hits); `git grep -n "incubator/"` returns none in live config.
2. **Tool skills work:** dry-run `/transcript-fetcher` and `/pdf-to-markdown` resolve their `app/` tool paths.
3. **Governance skills route correctly:** `/dd list`, `/ib list`, `/track` resolve to engine folders; no "Cross-System → meta-system" routing remains.
4. **Owner discovery:** the harness lists exactly one Owner subagent (`name: owner`); no dangling `meta-system-owner` symlink.
5. **Obsidian:** open the vault — the 7 former full-path links in `HUB.md` resolve; spot-check graph filters in `.obsidian/graph.json`.
6. **Engine self-check:** run `/system-health` then `/system-audit` — expect clean fractal compliance (now incl. `app/`, `knowledge/`), no broken cross-references, charter referenced where the constitution used to be. Run `/preflight` for environment integrity.
7. **Phase 2:** `/detect-drift` includes schematics; the 2–3 seed schematics validate against the form; Librarian Builder mode returns a schematic for a sample demand query.
