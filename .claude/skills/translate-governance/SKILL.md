---
name: translate-governance
description: >-
  Read MetaSystem constitution, values, principles, vocabulary, and fractal pattern,
  then produce or update IL-specific governance rules in governance/. Also refreshes
  the _governance/ snapshot for standalone publishing. Flags drift between source
  governance and existing translations. Use when governance source docs change, when
  bootstrapping a new system's governance, or periodically to detect drift. DD-86
  defines this as an Owner agent responsibility.
user-invocable: true
allowed-tools: Read Grep Glob Write Edit Bash
argument-hint: "[--check-only]"
---

# Translate Governance

Read MetaSystem governance source documents and produce IL-specific operational translations. The Owner agent's primary governance maintenance skill.

## When to Use This Skill

- The `governance/` directory is empty or newly created
- MetaSystem governance docs have been updated (constitution, values, principles, vocabulary)
- A new DD or governance artifact affects IL operations
- Periodic drift check — are IL-specific rules still aligned with the source?
- Before running `/system-audit` to ensure governance baseline is current

## When NOT to Use This Skill

- **Editing MetaSystem governance** — that's cross-system, Human-Required tier
- **Creating Design Decisions** — DD creation is Human-Required (DD-44)
- **Researching governance patterns** — use `/research-query` instead
- **Auditing system consistency** — use `/system-health` or `/system-audit`

## Available Tools

| Tool | Purpose |
|------|---------|
| `Read` | Read MetaSystem governance source docs and existing IL translations |
| `Grep` | Search for specific governance references across files |
| `Glob` | Find governance files by pattern |
| `Write` | Create new governance translation documents |
| `Edit` | Update existing translations with drift corrections |
| `Bash` | Copy files to `_governance/` snapshot directory |

## Cognitive Disposition

You are the **Owner** — the system steward translating governance intent into operational rules.

- **Translate, don't copy.** The constitution says "human gate at every stage boundary." The IL translation says "Researcher writes findings; Codifier writes extracts; Nick deploys. No agent crosses these stage boundaries." Same principle, system-specific language.
- **Flag drift, don't hide it.** If an existing translation contradicts the current source, report the delta explicitly. Don't silently overwrite — the drift itself is diagnostic information.
- **Preserve provenance.** Every translated rule traces back to a source document and section. If the source changes, the translation can be updated.
- **Be opinionated about what matters.** Not every constitution clause needs an IL translation. Translate what constrains IL operations; skip what's irrelevant to this system.

---

## Procedure

### Step 0: Parse Arguments

- **No arguments or `--check-only` absent:** Full translation run — read sources, produce/update translations, refresh snapshot.
- **`--check-only`:** Drift detection only — read sources, compare with existing translations, report drift. No writes.

### Step 1: Read Source Governance

Read all MetaSystem governance documents:

1. `systems/meta-system/governance/constitution.md` — boundary rules, ownership, design philosophy
2. `systems/meta-system/governance/values.md` — core values and design dimensions
3. `systems/meta-system/governance/principles.md` — DBDO pipeline, generalization principle
4. `systems/meta-system/governance/vocabulary.md` — authoritative term definitions
5. `systems/meta-system/governance/fractal-pattern.md` — structural requirements

Also read `.claude/rules/governance.md` for engine-facing governance rules that may need IL-specific translation.

### Step 2: Read Existing Translations

Use `Glob` to find all files in `systems/improvement-loop/governance/` (excluding `_index.md`). Read each one. Note:
- Which source sections each translation covers
- The `source_sections` field in frontmatter (if present)
- Any drift markers or TODO items from previous runs

### Step 3: Extract IL-Relevant Governance

For each source document, identify clauses that constrain IL operations:

**From Constitution:**
- Boundary rules (IL cannot modify other systems)
- Ownership matrix (IL is self-improving, Nick + Agents operate it)
- Design philosophy principles that apply to IL work
- Human gate requirements

**From Values:**
- "Spec before build" — applies to IL proposals and skill creation
- "Consumer feedback to producer" — applies to agent handoff protocol
- "Start lean, refine later" — applies to how IL evolves

**From Principles:**
- DBDO pipeline stages — how IL work flows through design/build/deploy/operate
- Generalization principle — IL should produce portable patterns

**From Vocabulary:**
- Terms IL agents must use consistently
- Definitions that constrain how IL classifies its artifacts

**From Fractal Pattern:**
- Structural requirements for IL's directory layout
- Knowledge vault subdirectory expectations
- Agent-as-directory pattern requirements

### Step 4: Produce Translations

For each governance domain, write a translation document to `systems/improvement-loop/governance/`. Use this template:

```markdown
---
title: "{Domain} — IL Governance"
type: "governance"
category: "governance"
target_system:
  - "improvement-loop"
stage: "active"
created: "{YYYY-MM-DD}"
updated: "{YYYY-MM-DD}"
author: "agent"
source_governance:
  - "{source-file-path}"
source_sections:
  - "{specific section or clause}"
tags:
  - "governance"
  - "improvement-loop"
  - "{domain-tag}"
---

# {Domain} — IL Governance

> Derived from: {source document titles with paths}
> Last reconciled: {date}

## Rules

{Numbered list of IL-specific operational rules. Each rule:}
1. **{Rule name}.** {Rule text — system-specific, not a copy of the source.}
   - *Source:* {Which source doc and section this derives from}

## Applicability Notes

{Where and when these rules apply within IL operations.}
```

**Recommended documents to produce:**

| Document | Source | Covers |
|----------|--------|--------|
| `boundary-rules.md` | Constitution boundary rules | What IL can/cannot modify, cross-system constraints |
| `pipeline-rules.md` | Constitution + Principles | How IL work flows through DBDO, human gates, stage boundaries |
| `agent-rules.md` | Constitution + Fractal Pattern | Agent boundaries, handoff requirements, agent-as-directory |
| `knowledge-rules.md` | Values + Vocabulary | How IL manages its KB, terminology requirements, knowledge lifecycle |

These are starting recommendations. Adjust based on what the source governance actually says — don't force-fit content into predetermined buckets.

### Step 5: Detect Drift (all runs including --check-only)

Compare existing translations against current source governance:

1. For each translation, re-read its `source_governance` and `source_sections`
2. Check if the source content has changed since the translation's `updated` date
3. Check if new source sections have appeared that aren't covered by any translation
4. Check if any translated rules contradict current source text

Produce a drift summary:

```markdown
## Drift Report — {date}

### Aligned
- {translation}: {N} rules, all consistent with source

### Drifted
- {translation}: Rule {N} says "{translated text}" but source now says "{current source text}"

### Uncovered
- {source section}: No IL translation exists for this governance clause

### Obsolete
- {translation}: Source section "{section}" no longer exists
```

If `--check-only`, output this report to conversation and stop. Otherwise, continue to Step 6.

### Step 6: Refresh `_governance/` Snapshot

The `_governance/` directory contains a standalone snapshot for the published `improvement-loop` repo (which doesn't have access to `../meta-system/`).

1. Copy MetaSystem governance source files to `_governance/`:
   - `constitution.md`
   - `values.md` (if exists in `_governance/`)
   - `principles.md` (if exists in `_governance/`)
   - `vocabulary.md` (if exists in `_governance/`)
   - `fractal-pattern.md` (if exists in `_governance/`)

2. Copy the `guides/` subdirectory if it exists in `_governance/guides/`

3. Use `Bash` with `cp` to perform copies (overwrite existing).

4. Report what was refreshed.

### Step 7: Update `_index.md`

Update `systems/improvement-loop/governance/_index.md` to reflect the current contents of the directory.

### Step 8: Report

Output a summary to conversation:

```
## Governance Translation Complete

**Created:** {N} new documents
**Updated:** {N} existing documents
**Drift detected:** {summary or "none"}
**Snapshot refreshed:** _governance/ updated with {N} files
```

---

## Rules

1. **Autonomy tier: Guarded.** Write translations, then report what changed. All writes are git-reversible. Do not wait for approval before writing governance translations — these are operational docs, not DDs.
2. **Never modify source governance.** Read from `meta-system/governance/` only. If a source error is found, flag it for human action.
3. **Never create DDs.** If a governance gap requires a Design Decision, propose it in the report. DD creation is Human-Required.
4. **Preserve existing translations.** Update in place via `Edit`. Don't delete and recreate — this loses git history.
5. **Provenance is mandatory.** Every translated rule must cite its source document and section. If you can't cite a source, the rule doesn't belong here.
6. **Drift reports are always produced.** Even if nothing drifted, say so. The absence of drift is information.
7. **`_governance/` is a copy, not a fork.** The snapshot mirrors source governance verbatim. IL-specific translations live in `governance/`, not `_governance/`.

## Calibration Notes

- The first run on an empty `governance/` directory will create all documents. Subsequent runs will mostly update and drift-check.
- Some constitution clauses are IL-irrelevant (e.g., JR's Notion access). Skip these in translations — don't create stub rules.
- The `_governance/` snapshot exists for the standalone `improvement-loop` repo. If the standalone repo isn't published yet, this step is preparatory but still correct to maintain.
- This skill complements `/system-audit`, which checks whether the IL system actually follows its governance. This skill maintains what governance says; `/system-audit` checks whether reality matches.
