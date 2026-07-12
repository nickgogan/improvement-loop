---
title: "Artifact Lifecycle Spec — Design Proposal"
type: "design-note"
target_system:
  - "improvement-loop"
created: "2026-04-20"
updated: "2026-04-20"
author: "claude"
stage: "draft"
source_dd:
  - "DD-29"
  - "DD-77"
  - "DD-78"
  - "DD-80"
  - "DD-81"
  - "DD-82"
tags:
  - "design-note"
  - "lifecycle"
  - "governance"
  - "proposal"
aliases:
  - "Artifact lifecycle"
  - "Merge and creation spec"
  - "Change-log proposal"
---

# Artifact Lifecycle Spec — Design Proposal

**Status:** Design proposal. Not a decision. Nick gates any DD that would codify this.

## Context

Nick surfaced at the end of session 45: *"investigate what we do when we have new research findings and existing guides. How do we merge new findings into guides? How do we know when we create new guides? How do we have a change log of the guides that have changed and why? … Same thing for skills and the other artifacts."*

**Why this matters now.** The KB crossed 545 findings and 11 synthesized guides. The pipeline is no longer producing first-drafts — it is producing second-drafts, third-drafts, and increasingly often revisions to revisions. The lifecycle was under-specified in DD-80 because the problem hadn't surfaced yet. It has now:

- G7 is overdue for re-synthesis (+11 findings). Re-running `/synthesize-guide` today would overwrite the current guide with whatever the skill produces. If Nick manually edited the guide between syntheses, those edits are lost without warning. This is a real risk — not hypothetical.
- Session 44's Codifier extracted 26 non-pattern artifacts into `extracts/`. If a source finding updates (new evidence, priority reassessment, dimension rebalance), there is no defined behavior for the downstream artifact. Current implicit behavior: nothing happens — the artifact drifts from its source.
- G2 is at 26 findings and growing. The routing table has a "guide split at 20+ findings" note but no documented procedure.
- The Agentic OS theme is at 3 findings. The graduation trigger is 5. There is no documented path from "theme in unrouted bucket" to "dimension #11" to "candidate guide cluster."
- `extracts/guides/changelog/` exists as an empty directory (created 2026-04-20). Someone intended a per-guide change-log mechanism. It has no content and no documented spec.

**What this spec must cover.** Four questions from Nick, for every artifact class (guide, rule, skill, template, agent):

1. **Merge mechanics** — when new evidence arrives for an existing artifact, what happens?
2. **Creation trigger** — when does a new artifact get created vs. extending an existing one?
3. **Change log** — how do we know what changed and why?
4. **Uniform vs. per-class** — one mechanism, or several?

**What is out of scope.** Deployment mechanics (DD-29 already governs this — Nick manually deploys from `extracts/`). Automated drift detection beyond what's proposed. Retroactive changelog backfill. This spec is about *going forward*, not about reconstructing history.

---

## Current State Inventory

What mechanisms already exist, and what do they capture?

| Mechanism | Captures | Granularity | Where it lives | Used by |
|-----------|----------|-------------|----------------|---------|
| Frontmatter `created` / `updated` | File-creation and last-modification dates | File-level, date-only | Every artifact | All |
| Frontmatter `source_findings[]` | Which findings fed this artifact | Per-artifact | Guides (primarily) | Guides |
| Frontmatter `source_finding` (singular) | The single finding this artifact extracts | Per-artifact | Non-pattern extracts | Rules / skills / templates / agents |
| Frontmatter `consumed_by[]` | Reverse lookup: finding → downstream artifacts | Per-finding | Findings | All consumption paths |
| Frontmatter `pipeline_status` | Stage: raw / classified / extracted / synthesized / deployed | Per-finding | Findings | Pipeline tracking |
| Frontmatter `contract` (DD-78) | preconditions / invariants / governance / recovery | Per-artifact | Every non-finding artifact | All |
| Frontmatter `stage` | draft / active / deprecated | Per-artifact | All | Deployment gate |
| Frontmatter `deployed` + `deployed_to` | Whether artifact has been promoted to live location | Per-artifact | Extracts only | Deployment audit |
| Guide routing table — Synthesis Status row | Last synthesized date, findings at synthesis, output path, status | Per-guide, one row | `operations/references/guide-routing-table.md` | Guides |
| Guide routing table — Guide Clusters row | Finding count, dimensions, practitioner question, stage | Per-guide, one row | Same file | Guides |
| Guide routing table — Unrouted Bucket | Findings that don't map to any active guide | Per-finding | Same file | Guide creation trigger |
| Extraction note (appended to finding body) | Which artifact consumed this finding, with date | Per-finding, append-only | Finding body | Non-pattern path |
| System Log entries | Session-level narrative — what a session did and why | Per-session | `operations/system-log/` | All work |
| Git log | File-level commit diff history | Per-commit | `.git/` | All files |
| `_index.md` catalog (extracts, guides) | Per-artifact row with date, source, deployed status | Per-artifact | `extracts/_index.md` etc. | Cross-form discovery |
| `extracts/guides/changelog/` (empty) | Intended to hold per-guide change logs — mechanism undefined | Planned: per-guide | Empty directory | Signal of intent |

**What this inventory reveals.** The system already has most of the raw ingredients for lifecycle tracking — it just lacks a specification for how they compose. In particular:

1. **State is captured; rationale is not.** `last_updated` tells you a file changed; it does not tell you *why*. Git commits carry some rationale in messages, but not in artifact-semantic form.
2. **Guide-specific state is semi-structured** (routing table rows). Non-pattern artifact state is effectively only frontmatter + git.
3. **There is no documented behavior for source-finding updates.** If a finding's content changes after its downstream artifact is extracted, the artifact drifts silently.
4. **There is no documented behavior for human edits to generated artifacts.** If Nick edits a guide or a rule, re-generation will clobber it without warning.

---

## Q1 — Merge Mechanics

### 1.1 Current behavior per class

| Class | Current behavior when new evidence arrives | Gap |
|-------|--------------------------------------------|-----|
| Guide | `/synthesize-guide` at staleness threshold (+3) → full regenerate. No merge-diff. Updates `source_findings[]`. Overwrites body. | Human edits clobbered. Finding removals handled implicitly. Finding reordering not documented. |
| Rule | `/extract-artifacts` writes once per source finding. Dedup at write time skips existing. | If source finding updates, the rule artifact is untouched. No hash, no drift check. |
| Skill | Same as rule. | Same. |
| Template | Same as rule. | Same; templates may also need versioning (multiple versions coexist). |
| Agent | Same as rule. | Changing an agent's disposition is system-level; single-source 1:1 is probably still right. |

### 1.2 Options for merge semantics

**Option A — Full regenerate (status quo).** Every re-synthesis or re-extraction regenerates from source. Simple. Clobbers human edits.

**Option B — Merge-diff against existing.** Re-run produces a diff; human reviews and applies. Preserves edits. Implementation cost high — markdown merge is not straightforward, and ContractSpec semantics must be preserved.

**Option C — Preserve designated sections.** Regenerate everything except sections marked `<!-- PRESERVE -->`. Human edits go in designated sections. Simpler than B. Gets most of the benefit with 10% of the complexity.

**Option D — Regenerate to a side file + human resolves.** New content lands at `artifact.md.new`; human diffs and adopts. Zero risk of clobbering; resolves workflow friction via explicit gate.

### 1.3 Recommendation (per class, with reasoning)

| Class | Recommended merge behavior | Why |
|-------|----------------------------|-----|
| Guide | **Option C — preserve designated sections.** Regenerate structural body; leave `## Notes` and `## Open Questions` sections untouched. Findings list is authoritative (from routing table). Nick's tuning goes in a reserved `## Nick's Annotations` section that the skill is instructed never to rewrite. | Guides churn most. Clobbering is the biggest real risk. Option C is the cheapest solution that solves it without merge-diff complexity. |
| Rule | **Option A with drift detection.** Re-extraction replaces the artifact body. BUT: compare source finding's `updated` timestamp against artifact's `created`. If source is newer, regenerate and log as `regenerate-on-source-update`. If source is unchanged, skip. | Rules are terse and stable. Human edits are rare (rules are machine-enforced). A drift flag is sufficient. |
| Skill | **Option A with drift detection.** Same as rule, plus: if skill ContractSpec changes, require Nick gate (skills have invocation contracts — silent changes break callers). | Skills may have dependents; changes need review. |
| Template | **Option D — side-file regenerate with version bump.** Templates are like code. On regenerate, write `template-v2.md` alongside `template.md`. Nick chooses which is canonical. Older versions stay for backwards-compat. | Templates are consumed by renderers; silently changing a template breaks every rendered instance. Explicit versioning is industry-standard (think: schema migrations). |
| Agent | **Option D — side-file + manual review.** Changes to an agent's disposition are system-level decisions. Write the new disposition to `agent-v2.md`; Nick promotes. | Agent persona drift is a real risk (identity shouldn't silently shift). Low volume, high stakes — manual is right. |

### 1.4 Handling finding removal

When `/dimension-rebalance` or deduplication reclassifies a finding out of a guide's cluster:

- **Guides:** Re-synthesis sees the updated `source_findings[]` and the finding is silently absent. This is correct behavior *if* the routing table was updated. The risk is the finding's removal changing the guide's argument — Nick needs visibility. **Proposal:** `/synthesize-guide` emits a delta report showing `ADDED: [...], REMOVED: [...]` before writing.
- **Non-pattern extracts:** If a finding is reclassified (pattern → rule or vice versa), the existing artifact should be marked `stage: deprecated` rather than deleted. Deployed artifacts never silently disappear.

### 1.5 Handling finding content updates

When a finding's body changes (Researcher adds evidence, priority gets reassessed):

- **Guides:** Full regenerate at next staleness cycle. The finding's new content flows through naturally.
- **Non-pattern extracts:** Drift detection (compare `updated` on finding vs. `created` on artifact). If drift detected, flag in an operations report — do not regenerate autonomously. Nick chooses when to re-run `/extract-artifacts` on the flagged set.

### 1.6 Tradeoffs to surface

- **Option C requires tooling discipline.** The skill must be instructed not to touch preserved sections. A single slip clobbers the edits we were trying to protect. Mitigation: regression test — after re-synthesis, diff preserved sections; fail if changed.
- **Drift detection for non-pattern artifacts requires a new operations report.** More files. More skills. Balance: without it, artifacts drift silently — visibility beats cleanliness.
- **Versioning templates adds cognitive load.** Nick has to remember which version is current. Mitigation: `extracts/_index.md` already tracks per-artifact; add a `version` column. Same for agents.

---

## Q2 — Creation Trigger

### 2.1 Current behavior per class

| Class | Current creation trigger | Gap |
|-------|--------------------------|-----|
| Guide | 5+ unrouted findings with `same-problem` relationships → candidate cluster → Nick approval | No split trigger documented. No cross-dimension trigger. No "theme below 5" graduation path. |
| Rule | Every non-pattern finding classified as rule → 1 artifact (DD-80, DD-81) | No "fold into existing rule" rubric. A finding that restates an existing rule still creates a new one. |
| Skill | Same as rule | Same — no clustering of related skills. |
| Template | Same as rule | Same. |
| Agent | Same as rule (none created this way yet in practice — all agents are Owner-defined) | Never exercised. DD-82's 4-agent architecture is fixed; new agents would be system-level design decisions, not Codifier output. |

### 2.2 Problems with the current model

1. **Guide splits are manually triggered and subjective.** G2 at 26 findings has no documented path to split.
2. **Cross-dimension themes have no home.** A finding that spans "Context Engineering" and "Memory Architecture" (like `surprisal-novelty`) gets routed to one dimension's guide; the cross-link is lost.
3. **1:1 finding:artifact for non-pattern classes creates duplication.** Two findings describing "require absolute paths" become two rule artifacts instead of one. This is fine at small scale but will not scale past ~50 rules.
4. **Theme graduation is under-specified.** Agentic OS is at 3 findings. The trigger at 5 is documented; the *process* is not (who proposes? what DD gets filed? how does the routing table update?).

### 2.3 Recommendations per class

| Class | Recommended creation trigger |
|-------|------------------------------|
| Guide | (a) **Create new:** 5+ unrouted findings with `same-problem` relationships → Nick approves. (b) **Split existing:** guide reaches 25 findings AND covers ≥2 distinct practitioner questions → Codifier proposes split; Nick approves. (c) **Cross-dimension theme:** 5+ findings share tags/links but span multiple dimensions → Codifier proposes a "meta-guide" or cross-reference section; Nick decides. |
| Rule | (a) **Create new:** every rule-classified finding unless (b) matches. (b) **Extend existing:** before creating, Codifier greps `extracts/rules/` for semantically similar rules; if found, proposes extension to existing rule's "Evidence" section instead of new rule. Nick's review gate catches false negatives. |
| Skill | (a) **Create new:** every skill-classified finding unless (b) matches. (b) **Parameterize existing:** if a skill-classified finding describes a variant of an existing skill (same I/O contract, different mode), extend the existing skill with a mode flag rather than creating a new one. |
| Template | (a) **Create new:** every template-classified finding unless (b) matches. (b) **Version existing:** if a template-classified finding describes an evolution of an existing template, bump the version (see Q1 recommendation). |
| Agent | **Never auto-create.** Agent creation is a system-level decision (DD-82 governs the 4-agent architecture). Codifier flags agent-classified findings for Nick's review. No extraction without explicit Nick approval. |

### 2.4 Theme graduation procedure (surfacing here because it's a gap)

Proposed: when a theme in the unrouted bucket reaches 5 findings with `same-problem` links:

1. `/identify-artifacts` flags the cluster in the next report's "Candidate Cluster" section.
2. Codifier proposes: (a) promote to new guide cluster + dimension, OR (b) absorb into existing dimension as sub-theme.
3. Nick approves one of:
   - **New dimension (e.g., #11 "Agentic OS"):** file DD; update `research-dimensions.md`; add guide cluster to routing table.
   - **Absorb into existing dimension:** update routing table; findings route to existing guide via updated dimension mapping.
4. Codifier runs `/dimension-rebalance` if absorption route chosen.

### 2.5 Tradeoffs to surface

- **Extension rubric for rules/skills creates false positives.** "Semantically similar" is LLM-fuzzy; the Codifier may propose bad extensions. Mitigation: Codifier always surfaces the similar artifact + a diff; Nick gates.
- **Auto-splitting guides at 25 findings is arbitrary.** Some guides may benefit from 40+ findings (e.g., G4 Evaluation at 30 is coherent). Mitigation: the rule is *propose*, not *execute*. Nick always gates.
- **Never-auto-create for agents may be too conservative.** But the blast radius of silently creating an agent is high (DD-82 invariant). Conservative is correct here.

---

## Q3 — Change Log

### 3.1 What we want to capture

Per Nick's prompt: what changed, why, who, when. Applied to artifacts:

| Signal | Example |
|--------|---------|
| What | "Added findings X, Y, Z; removed finding W; rewrote Pitfalls section" |
| Why | "Staleness threshold +5 since last synthesis" / "Nick request: emphasize Memongo evidence" / "Dimension rebalance moved W to G2" |
| Who | "Codifier — session 46" |
| When | ISO timestamp |

### 3.2 Options to evaluate

**Option A — Frontmatter `changelog:` array per artifact.**
```yaml
changelog:
  - date: 2026-04-20
    session: 46
    change: "Re-synthesized from 21 findings (+7 from session 45)"
    trigger: "staleness-threshold"
  - date: 2026-04-19
    ...
```
- Pros: locality (lives with the artifact); queryable.
- Cons: grows unboundedly inside frontmatter; frontmatter becomes heavy; conflicts with "no duplicated content" feedback principle.

**Option B — Companion `.changelog.md` file per artifact.**
`extracts/guides/managing-agent-context.md` paired with `extracts/guides/managing-agent-context.changelog.md`.
- Pros: locality without frontmatter bloat; scales to large histories; already signaled by the empty `extracts/guides/changelog/` directory.
- Cons: 2x the files; every change requires two writes; drift risk between artifact and changelog.

**Option C — Centralized `operations/artifact-changelog.md`.**
One file, all artifacts, every change.
- Pros: single query surface; easy to diff across artifacts.
- Cons: grows unboundedly in one file; merge conflicts; no per-artifact locality.

**Option D — Leverage System Log entries only.**
Each SL entry already captures what a session did. Point to SL as the authoritative change log.
- Pros: zero new mechanism; reuses existing file.
- Cons: SL is session-scoped, not artifact-scoped — looking up "why did G7 change in April?" requires grepping every SL entry. Queryability is poor.

**Option E — Hybrid.** Frontmatter holds a minimal pointer (latest change date + SL session ref); SL is the narrative source of truth; git log is the file-diff source of truth. No new changelog files created.
- Pros: reuses existing mechanisms; no duplication; artifact-to-SL is a direct lookup via frontmatter.
- Cons: still requires grepping SL for history queries.

### 3.3 Recommendation

**Option E for non-guide classes (rule / skill / template / agent). Option B for guides.**

Rationale: Stability profiles diverge.

- **Rules / skills / templates / agents** change rarely. Option E's overhead (grep SL) is acceptable because the query is rare. Adding `.changelog.md` companions to 26+ low-churn artifacts is net-negative.
- **Guides** change often (staleness cycles, Nick's tuning, dimension rebalances). Option B pays off because queries are frequent and the narrative is richer than what fits in a frontmatter line. The empty `extracts/guides/changelog/` directory already signals this intent.

**Concrete shape:**

For guides (Option B): Add `extracts/guides/changelog/<guide-name>.changelog.md`. Entries are lean — SL-like terseness, not report-shaped. Each entry is ~5–8 lines: one header line, one-line delta summary, compact added/removed lists, one-line structural summary, preservation note, SL link. Narrative lives in SL; the changelog is the per-guide index into it.

```markdown
## 2026-04-XX — Session NN — staleness-threshold

- Findings: 21 (+7, -0 since last synthesis)
- Added: [[f1]], [[f2]], [[f3]], [[f4]], [[f5]], [[f6]], [[f7]]
- Structural: emphasized Memongo single-store stance in Key Concepts; split Pitfalls into write-path / retrieval-path
- Preserved: `## Nick's Annotations` untouched
- SL: [[session-NN-codifier-guide-resynthesis-g7]]
```

Constraints on entry shape:
- One-line header: date, session, trigger tag.
- **Trigger tags** (controlled vocab): `staleness-threshold` | `nick-request` | `dimension-rebalance` | `finding-removed` | `structural-edit`.
- Added/removed lines: bracket-link lists only; no rationale per finding (rationale lives in SL or the dimension-rebalance report).
- Structural line: 1–2 lines of what-changed-at-guide-level; no section-by-section recap.
- Preserved line: name the section(s); confirm untouched.
- SL link: the narrative lookup target.
- If an entry naturally exceeds ~10 lines, the verbose content belongs in the SL entry, not here.

For non-guide classes (Option E): Add two frontmatter fields:
```yaml
last_change_session: 46
last_change_sl: "session-46-codifier-session-45-identification"
```
(No change-log file. SL is the narrative.)

### 3.4 Tradeoffs to surface

- **Option B creates 11+ new files for guides.** This is the "hardcoded counts / duplicated content" risk Nick has flagged before. Mitigation: changelog files are append-only narrative — not structured counts that need per-session maintenance. They are exactly the sort of content that SHOULD persist, not the sort that creates token tax.
- **Option E's `last_change_*` frontmatter fields add two more controlled-vocab entries.** Frontmatter schema change (DD-level, since `_schema.yaml` defines the contract). Acceptable overhead for the visibility gain.
- **Git log remains the fallback.** Neither option replaces git; both complement it with artifact-semantic narrative. That's correct separation.

### 3.5 The `extracts/guides/changelog/` directory

It exists and is empty. Two interpretations:

1. Nick (or an earlier session) already decided on Option B for guides but didn't implement it. **Proposal: honor the existing signal and populate it.**
2. The directory was created exploratorily and is now a loose end. **Proposal: still populate it — the interpretation that leaves code working is preferred.**

Either way: populating the directory with a README-ish file and the first changelog entries is cheap and aligned. Recommend doing it on the next G7 / G2 / G9 re-synthesis.

---

## Q4 — Uniform vs. Per-Class

### 4.1 Stability profile per class (proposed)

| Class | Stability | Primary update driver | Revision frequency |
|-------|-----------|----------------------|---------------------|
| Guide | Low (high churn) | New findings, Nick's tuning | Weekly-to-monthly |
| Rule | High (stable) | Occasional rubric clarification | Quarterly or less |
| Skill | Medium | Practice evolution, model changes | Monthly |
| Template | High but versioned | Schema or vocabulary changes | Versioned when it changes |
| Agent | Very high (stable) | System-level decisions only | Rare, always human-gated |

### 4.2 Options

**Option U (uniform):** One lifecycle spec applied to every class — merge-diff, 1:1 create, frontmatter changelog.
- Pros: simplest mental model; one skill implements everything.
- Cons: over-engineers stable classes; under-serves high-churn classes.

**Option D (per-class):** Each class has its own lifecycle.
- Pros: right-sized per stability profile.
- Cons: 5 specs to maintain; cognitive overhead.

**Option H (hybrid: core + class-specific).** One core shape (pipeline_status, contract, source tracking) applies to all; class-specific fields (changelog mechanism, creation trigger, merge semantics) diverge.
- Pros: preserves consistency where it matters; allows divergence where stability profiles differ.
- Cons: requires explicit per-class documentation to prevent drift.

### 4.3 Recommendation

**Option H — hybrid core-plus-class-extensions.**

The core (shared across all classes):
- ContractSpec (DD-78) — unchanged.
- `pipeline_status` on source findings — unchanged.
- `consumed_by[]` on source findings — unchanged.
- `source_finding` / `source_findings[]` on artifacts — unchanged.
- Staging in `extracts/` before deployment — unchanged.
- Human gate at deployment — unchanged (DD-29).

The class-specific extensions:
| Class | Merge | Creation | Change log |
|-------|-------|----------|-----------|
| Guide | Preserve designated sections | 5+ cluster / 25-finding split proposal / cross-dim flag | Companion `.changelog.md` file |
| Rule | Drift detection + regenerate | Extend existing if match; else new | Frontmatter `last_change_*` + SL |
| Skill | Drift detection + regenerate (Nick gate on ContractSpec change) | Parameterize existing if mode-variant; else new | Frontmatter `last_change_*` + SL |
| Template | Side-file with version bump | Version existing if evolution; else new | Frontmatter `version` + `last_change_*` + SL |
| Agent | Side-file + manual review | Never auto-create; flag for Nick | Frontmatter `last_change_*` + SL |

### 4.4 Why not uniform

Because the stability profiles differ by ~10x across classes. A uniform spec means either:
- Over-engineer rules/templates/agents (low-churn) by forcing changelog files and merge-diff machinery they never exercise.
- Under-serve guides (high-churn) by giving them only frontmatter changelog entries that grow unboundedly.

Option H preserves consistency on the part that matters (contract, pipeline status, staging, human gate) and allows divergence on the part that doesn't (merge semantics, changelog mechanism).

---

## Per-Artifact-Class Summary Table

| Class | Merge behavior | Creation trigger | Change-log mechanism | Stability profile | Approval path |
|-------|----------------|------------------|----------------------|-------------------|---------------|
| **Guide** | Regenerate body; preserve `## Nick's Annotations` section | 5+ unrouted findings (new), 25-finding split, cross-dim flag | Companion `.changelog.md` file | Low (high churn) | DD-level for split/merge; Nick-gate for routine staleness regen |
| **Rule** | Regenerate on source drift (timestamp check); else skip | 1:1 with finding, unless extension match → extend existing | Frontmatter `last_change_*` + SL entry | High (stable) | Nick-gate at extract time; operational convention for drift re-runs |
| **Skill** | Regenerate on source drift; ContractSpec change → Nick gate | Parameterize existing if mode-variant; else new | Frontmatter `last_change_*` + SL entry | Medium | Nick-gate on ContractSpec; operational convention otherwise |
| **Template** | Side-file with version bump (`template-v2.md`); never clobber | Version existing if evolution; else new | Frontmatter `version` + `last_change_*` + SL entry | Versioned like code | Nick-gate at version promotion |
| **Agent** | Side-file with manual review; never auto-regenerate | Never auto-create; flag classifications for Nick | Frontmatter `last_change_*` + SL entry | Very high (stable) | System-level DD for any change |

### Governance summary

| Action | Who gates | Codification level |
|--------|-----------|---------------------|
| Regenerate a guide under staleness trigger | Codifier (after this spec approved) | Operational convention |
| Preserve-section discipline on guide regen | Skill enforcement | DD (adds frontmatter schema + skill rule) |
| Drift detection for rule/skill/template | Codifier emits report; Nick reviews | Operational convention |
| Version bump on template | Nick | DD (adds `version` field to frontmatter) |
| Side-file for agent changes | Nick | System-level DD |
| Companion `.changelog.md` for guides | Auto on every re-synthesis | Operational convention |
| Frontmatter `last_change_*` on non-guide | Auto on every re-generation | DD (frontmatter schema change) |
| Guide split proposal at 25 findings | Codifier proposes; Nick approves | DD (split procedure + trigger) |
| Theme graduation to new dimension | Codifier proposes; Nick approves + DD | DD per theme |

---

## Proposed DDs to Codify This Spec

Titles only; one-line rationales. **Not filing this session** — Nick gates.

1. **DD-X1: Guide regeneration preserves designated sections.** `/synthesize-guide` must preserve `## Nick's Annotations` (and any section marked `<!-- PRESERVE -->`) across re-syntheses. Enforced by skill rule + post-regen regression test.
2. **DD-X2: Source drift detection for non-pattern artifacts.** When a finding's `updated` post-dates an extracted artifact's `created`, Codifier emits a drift report. Nick gates re-extraction.
3. **DD-X3: Companion changelog files for guides.** Each guide in `extracts/guides/` has a paired `extracts/guides/changelog/<guide>.changelog.md` that `/synthesize-guide` appends on every re-synthesis.
4. **DD-X4: Frontmatter schema — `last_change_*` fields.** Add `last_change_session` and `last_change_sl` to non-guide extract frontmatter. Not added to guides (they use the companion changelog).
5. **DD-X5: Guide split procedure.** At 25 findings AND ≥2 distinct practitioner questions, Codifier proposes a split; Nick approves via DD.
6. **DD-X6: Theme graduation procedure.** At 5+ unrouted findings with same-problem links, Codifier proposes either new-dimension promotion or absorption into existing dimension.
7. **DD-X7: Extension rubric for rules / skills.** Before creating new rule/skill artifact, Codifier checks `extracts/{form}/` for semantically similar artifacts; proposes extension if match; Nick gates.
8. **DD-X8: Template and agent versioning.** Template regeneration writes to `<name>-v<N>.md` alongside existing. Agents similarly. Nick promotes.
9. **DD-X9: Co-occurrence harvesting during guide synthesis.** When `/synthesize-guide` absorbs pattern findings carrying non-pattern co-occurrences (template / skill / rule), it emits a Co-occurrence Harvest Queue alongside the guide draft — one row per embedded artifact with a sketch and a recommended extraction path. Nothing auto-extracted; Nick gates per-row. Makes DD-77's "resolved at read time" operational rather than implicit, and prevents embedded artifacts from disappearing into guide bodies.

Each DD is roughly one page. Total codification cost: ~9 DDs. A reasonable bundle to file against this spec's approval.

---

## Open Questions for Nick

1. **Was the empty `extracts/guides/changelog/` directory an explicit decision?** If yes, Option B for guides is pre-aligned and I'll proceed on that track. If no, the question is whether the per-guide changelog file is worth the file proliferation.
2. **Is the "preserve `## Nick's Annotations` section" convention acceptable?** Or should preservation be invisible (HTML comments marking regions)?
3. **On guide splits:** is 25 findings the right number? G4 is at 30 and seems coherent. Maybe the real trigger is "covers ≥2 distinct practitioner questions," not finding count.
4. **On theme graduation:** does Agentic OS (currently 3 findings) graduate as a new dimension, or absorb into an existing dimension like "Context Engineering" or "Agent Design"?
5. **On the rule/skill extension rubric:** how fuzzy is too fuzzy? An LLM saying "semantically similar" will have false positives. Do you want a stricter trigger (e.g., overlapping ContractSpec invariants)?
6. **On template/agent versioning:** is there an upper bound on how many versions coexist before we archive old ones?
7. **Does this spec need Research-KB lifecycle coverage too?** Findings themselves update (Researcher edits, reassessment, dimension rebalance). The current spec treats findings as sources-of-truth; drift flows downstream to artifacts. But finding lifecycle per se (how a finding evolves) is under-specified. Separate spec, or fold in?

---

## Recommendation Shape

If Nick approves this spec in broad strokes:

1. **Phase 1 (lightest weight, highest value):** Populate `extracts/guides/changelog/` on next G7 re-synthesis. Add `last_change_*` frontmatter fields. Add preserved-section convention to `/synthesize-guide`. File DD-X1, DD-X3, DD-X4.
2. **Phase 2 (operational additions):** Add drift-detection report to `/extract-artifacts`. Add extension rubric. File DD-X2, DD-X7.
3. **Phase 3 (procedural):** Formalize guide split and theme graduation procedures. File DD-X5, DD-X6, DD-X8.

Phase 1 is enough to unblock G7 / G2 / G9 re-synthesis. Phases 2 and 3 can be sequenced over subsequent sessions.

---

## What This Spec Does NOT Resolve

- **Deployment lifecycle.** Nick's manual deploy from `extracts/` to `meta-system/knowledge/` is governed by DD-29. Once deployed, the live-location artifact drifts independently of the stage-location artifact. This spec does not address live-location lifecycle — that's a separate question.
- **Retroactive changelog backfill.** The 11 existing guides were all synthesized on 2026-04-19. Their implicit changelogs are lost. This spec is forward-looking only.
- **Finding-level lifecycle.** When a finding's content changes, this spec's downstream-drift detection covers *artifacts*, not the finding itself. Whether findings themselves need a changelog is a separate (open) question.
- **Cross-artifact contract conflicts.** DD-78 ContractSpec is per-artifact. Two artifacts sharing sources could develop contradictory invariants. Form-classification rubric's open-question #6 notes this; still unresolved. Adjacent to this spec.

---

## Cross-References

- Identification report for session 45: `operations/pattern-identification-reports/2026-04-20-session-45-identification-report.md`
- Handoff prompt (session 46): `operations/handoffs/handoff-prompt-session-46-codifier-session-45-identification.md`
- Guide routing table: `operations/references/guide-routing-table.md`
- Form classification rubric: `operations/references/form-classification-rubric.md`
- Frontmatter schema: `_schema.yaml`
- Codifier agent: `agents/codifier/agent.md`
- Governing DDs:
  - DD-29 (human gate at stage boundaries)
  - DD-77 (single-form classification)
  - DD-78 (ContractSpec universal layer)
  - DD-80 (pipeline simplification)
  - DD-81 (pattern filter — patterns route to guides)
  - DD-82 (IL 4-agent architecture)
