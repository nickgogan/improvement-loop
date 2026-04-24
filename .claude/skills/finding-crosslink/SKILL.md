---
name: finding-crosslink
description: >-
  Detect and create cross-links between related research findings in the Improvement Loop KB.
  Uses 4 binary-testable relationship types (enables, contradicts, extends, same-problem) and
  parallel subagent batches for throughput. Run after bulk extraction, backfill, or periodically
  as KB maintenance. Produces a proposal report, then executes approved links after human gate.
user-invocable: true
allowed-tools: Read Grep Glob Edit Agent
argument-hint: "[--dry-run] [--category <name>] [--batch-size <n>]"
---

# Finding Crosslink

Detect meaningful relationships between research findings and write them as `related_findings:` entries in frontmatter.

## When to Use This Skill

- After a bulk extraction or backfill that added many new findings
- After a dimension rebalance that moved findings between categories
- Periodically as KB quality maintenance (e.g., quarterly)
- When you notice findings that should reference each other but don't

## Relationship Types

Exactly 4 types. Each has a two-question binary test — both questions must be answered YES to propose the link.

### 1. `enables`

**Meaning:** Finding A describes a mechanism/technique that is required or strongly useful for Finding B to work.

**Binary test:**
1. Does Finding A describe a concrete mechanism, technique, or infrastructure component?
2. If you removed or disabled A, would Finding B break, degrade significantly, or become impractical?

**Direction:** A enables B (asymmetric — write on both files with correct direction).

**Examples:**
- "Pre-Compression Identity Pinning" **enables** "SOUL.md Agent Constitution Pattern" (without pinning, SOUL.md gets compressed away)
- "Token Budget Pre-Turn Projection" **enables** "Context Bracket Auto-Adaptation" (budget tracking is needed for bracket decisions)

### 2. `contradicts`

**Meaning:** Both findings address the same problem but recommend incompatible approaches.

**Binary test:**
1. Do both findings explicitly address the same problem or design decision?
2. Can you adopt both simultaneously without conflict? (If NO → contradicts)

**Direction:** Bidirectional (write on both files).

**Examples:**
- "Agent Sprawl Anti-Pattern" **contradicts** "AIOS Architecture: Folder-Per-Role Agent Organization" (one warns against many agents, the other prescribes one-per-role)
- "CLI-First Tool Integration" **contradicts** "MCP as universal tool protocol" (if both address the same integration need)

### 3. `extends`

**Meaning:** Finding A covers everything in Finding B and adds substantial new scope.

**Binary test:**
1. Does Finding A cover all the ground that Finding B covers?
2. Does Finding A add at least one substantial new concept, mechanism, or insight beyond B?

**Direction:** A extends B (asymmetric).

**Examples:**
- "Four-Layer Agent Evaluation Architecture" **extends** "Two-Level Verification" (adds more layers beyond the two-level model)
- "ACE Evolving Playbook" **extends** "ACE RAG-Based Playbook" (broader scope, includes the RAG approach plus more)

### 4. `same-problem`

**Meaning:** Both findings address the same need but offer different, compatible approaches.

**Binary test:**
1. Do both findings explicitly address the same problem, need, or design question?
2. Are the approaches different but non-conflicting? (Could you adopt either or both?)

**Direction:** Bidirectional (write on both files).

**Examples:**
- "Index-File Navigation as RAG Replacement" **same-problem** "Karpathy LLM Knowledge Base (Obsidian RAG)" (both solve KB navigation, different mechanisms)
- "Prompt Caching for Stable Agent Context" **same-problem** "Pre-Compression Identity Pinning" (both address context persistence, different mechanisms)

## Frontmatter Schema

```yaml
related_findings:
  - file: "pre-compression-identity-pinning.md"
    rel: "enables"
  - file: "context-file-taxonomy-claudemd-soulmd-agentsmd.md"
    rel: "same-problem"
```

The `related_findings:` array is added to the finding's YAML frontmatter. Each entry has:
- `file:` — the related finding's filename (not path, just filename)
- `rel:` — one of: `enables`, `contradicts`, `extends`, `same-problem`

For asymmetric relationships (`enables`, `extends`), the direction matters:
- On Finding A's file: `rel: "enables"` means "this finding enables the linked finding"
- On Finding B's file: `rel: "enabled-by"` means "this finding is enabled by the linked finding"
- On Finding A's file: `rel: "extends"` means "this finding extends the linked finding"
- On Finding B's file: `rel: "extended-by"` means "this finding is extended by the linked finding"

For symmetric relationships (`contradicts`, `same-problem`), both files use the same `rel` value.

## Procedure

### Step 0: Parse Arguments

- `--dry-run`: Produce the proposal report but don't write any links. Default if no flag specified.
- `--category <name>`: Only crosslink findings within the specified category (faster, narrower scope).
- `--batch-size <n>`: Number of findings per subagent batch. Default: 25.

### Pre-step: Script-Based Pair Generation (Recommended)

Run the crosslink pair generator to get candidate pairs as structured JSON:

```bash
# All categories
python3 systems/improvement-loop/operations/kb-maintenance-scripts/crosslink_pair_generator.py

# Single category (faster, use after bulk extraction in one category)
python3 systems/improvement-loop/operations/kb-maintenance-scripts/crosslink_pair_generator.py --category "Orchestration"

# Only pairs involving the newest findings
python3 systems/improvement-loop/operations/kb-maintenance-scripts/crosslink_pair_generator.py --new-only
```

This outputs a JSON array of `{a, a_name, a_cat, a_sum, b, b_name, b_cat, b_sum}` objects ready for subagent dispatch at Step 2. Skip Step 1 below and go directly to Step 2.

For crosslink health stats before deciding scope, run:
```bash
python3 systems/improvement-loop/operations/kb-maintenance-scripts/crosslink_coverage.py
```

If the scripts are unavailable, fall back to the manual procedure below.

### Step 1: Build the Candidate Pair List

Not every pair of findings needs testing. Use these heuristics to reduce the 24K+ pair space to a manageable set:

**Tier 1 — Same-category pairs (highest signal):**
- For each category, generate all pairs of findings within that category.
- These are the most likely to have meaningful relationships.

**Tier 2 — Shared-source pairs (cross-category):**
- For each source file, find all findings that list it in their `sources:` array.
- Generate pairs across those findings, even if they're in different categories.
- Co-occurrence in the same source is a strong signal of relatedness.

**Tier 3 — Keyword overlap (cross-category, filtered):**
- For findings not covered by Tier 1 or 2, compute a quick keyword overlap score using the `name` and `summary` fields.
- Only include pairs where at least 2 non-trivial keywords overlap (exclude stop words: agent, pattern, system, tool, model, AI, LLM, framework, architecture).
- This catches cross-category relationships that don't share a source.

**Skip if `--category` was specified** — only generate Tier 1 pairs for that category.

### Step 2: Batch and Dispatch Subagents

1. Divide the candidate pair list into batches of `--batch-size` pairs (default 25).
2. For each batch, launch a subagent with this prompt template:

```
You are evaluating potential relationships between research findings in a knowledge base.

For each pair below, read both findings' summaries and "What It Is" sections, then test each of the 4 relationship types using the binary questions. Both questions must be YES to propose a link.

## Relationship Types and Tests

### enables (A enables B)
Q1: Does Finding A describe a concrete mechanism, technique, or infrastructure component?
Q2: If you removed A, would Finding B break, degrade significantly, or become impractical?

### contradicts (bidirectional)
Q1: Do both findings explicitly address the same problem or design decision?
Q2: Can you adopt both simultaneously without conflict? (If NO → contradicts)

### extends (A extends B)
Q1: Does Finding A cover all the ground that Finding B covers?
Q2: Does Finding A add at least one substantial new concept beyond B?

### same-problem (bidirectional)
Q1: Do both findings explicitly address the same SPECIFIC problem or need? (Not just the same domain or category.)
Q2: Are the approaches different but non-conflicting?

## Rules
- Read ONLY the frontmatter (name, summary, category) and the "What It Is" section. Do NOT read the full finding body.
- Both binary questions must be answered YES for a relationship to be proposed.
- A pair can have AT MOST ONE relationship type. If multiple could apply, choose the most specific: enables > extends > same-problem > contradicts.
- When in doubt, do NOT propose a link. Precision over recall.

## same-problem Anti-Patterns (Common False Positives)
These patterns look like same-problem but are NOT. Reject them:
- **Category proximity**: Two findings in the same category (e.g., both Context Engineering) that address different sub-problems. Sharing a category is NOT same-problem.
- **Complementary ≠ same-problem**: If A is a principle/framework and B is a technique that benefits from A, that relationship is "enables" (if B depends on A) or no link (if they're just loosely related). It is NOT same-problem.
- **Scope mismatch**: A broad framework (e.g., 26 agents, full SDLC) is NOT same-problem with a narrow technique (e.g., five token efficiency rules) even if they touch the same domain. The SPECIFIC problems they solve must match.
- **Different levels of the stack**: A runtime optimization and a design-time principle may both relate to "performance" but address fundamentally different problems.

## enables Anti-Patterns
- **Helpful ≠ required**: Q2 asks "would B BREAK or degrade SIGNIFICANTLY," not "would B be slightly less effective." If B can function perfectly well without A using alternative mechanisms, the answer is NO.

## enables Positive Pattern
- **Definitional dependency**: Correct enables links share a pattern — B is an explicit sub-component or internal mechanism of A. The dependency is definitional (B literally cannot exist without A's framework/architecture), not just functional. Examples: ACE framework enables ACE-specific mechanisms; a layered memory stack enables cross-layer governance. If you can't articulate what specific mechanism in B *breaks* without A, the answer is NO.

## Output Format
Return a JSON array. For each proposed link:
{"finding_a": "filename-a.md", "finding_b": "filename-b.md", "rel": "enables", "q1": "YES - [brief reason]", "q2": "YES - [brief reason]"}

For pairs with no relationship, do not include them in the output.

## Pairs to Evaluate
[list of {finding_a, finding_b} pairs with their summaries]
```

3. Launch subagents in parallel (up to 4-6 concurrent, depending on batch count).

### Step 3: Collect and Deduplicate Results

1. Gather all subagent outputs.
2. Parse JSON arrays from each.
3. Deduplicate: if the same pair appears from multiple batches (shouldn't happen with proper batching, but handle it), keep the one with the most specific relationship type.
4. Validate: ensure both findings actually exist in the KB.

### Step 4: Produce Proposal Report

```markdown
## Finding Crosslink Report — [Date]

### Summary
| Metric | Count |
|--------|-------|
| Candidate pairs evaluated | X |
| Proposed links | X |
| enables | X |
| contradicts | X |
| extends | X |
| same-problem | X |

### Proposed Links
| Finding A | Rel | Finding B | Rationale |
|-----------|-----|-----------|-----------|

### Category Cluster Map
[For each category, show which findings link to findings in other categories — reveals cross-dimensional patterns]
```

**Stop here if `--dry-run` was specified.**

### Step 5: Human Gate

Present the report. Wait for approval. The user may:
- Approve all
- Approve selectively (specify which links to write)
- Reject all
- Modify relationship types

### Step 6: Write Approved Links

**YAML Safety:** Use `kb_parser.py` for all reads and writes:
```python
from kb_parser import parse_frontmatter, write_frontmatter, FINDINGS_DIR
fm, body = parse_frontmatter(FINDINGS_DIR / filename)
fm['related_findings'].append({'file': target, 'rel': rel_type})
fm['last_updated'] = TODAY
write_frontmatter(FINDINGS_DIR / filename, fm, body)  # validates round-trip automatically
```
Never use regex replacement on `related_findings:` blocks — they contain nested `file:` + `rel:` entries that span multiple lines and regex will leave orphaned lines that break YAML parsing.

For each approved link:

1. **Read Finding A's frontmatter.**
2. **Check if `related_findings:` exists.** If not, add it as an empty array after `proposals:` (or the last frontmatter field before `date_discovered:`).
3. **Add the link entry** to Finding A's `related_findings:` array.
4. **Read Finding B's frontmatter.**
5. **Add the reverse link** to Finding B's `related_findings:` array:
   - `enables` → write `enabled-by` on the other file
   - `extends` → write `extended-by` on the other file
   - `contradicts` → write `contradicts` on both
   - `same-problem` → write `same-problem` on both
6. **Update `last_updated`** on both files to today.
7. **Validate** that every modified file still parses with `yaml.safe_load`. If any fail, stop and fix before continuing.

### Step 7: Post-Write Validation (Required)

After writing links, run a deep validation pass on a stratified sample by reading full finding files (not just summaries). This catches false positives that summary-only evaluation misses.

1. **Sample selection** — Pick at minimum:
   - All `contradicts` links (highest consequence if wrong)
   - All `enables` links (dependency claims must be verified)
   - All `extends` links
   - 10-15% of `same-problem` links, biased toward cross-category pairs and pairs where the two findings have low keyword overlap (these are most likely to be false positives)

2. **Validation method** — For each sampled pair, launch a validation subagent that:
   - Reads the full "What It Is" section (not just summary) of both findings
   - Re-applies the binary tests strictly
   - Returns a verdict: CORRECT, WRONG (with recommended fix), or BORDERLINE

3. **Known error patterns to watch for:**
   - **Category proximity false positives**: Two findings in the same category (e.g., both Context Engineering) linked as same-problem when they actually address different sub-problems. "Complementary" ≠ "same-problem."
   - **Enables over-reach**: Finding A is *helpful* to Finding B but not *required*. Q2 asks "would B break or degrade significantly," not "would B be slightly less effective."
   - **Scope mismatch**: A broad framework linked as same-problem with a narrow technique that addresses only one sub-problem of the framework.

4. **Fix misclassified links** — For any WRONG verdict:
   - If the correct relationship is a different type, update both files (remove old entry, add new one with correct `rel`)
   - If there should be no link at all, remove the entry from both files
   - Update `last_updated` on modified files

5. **Report validation results** alongside the main crosslink report: pairs tested, verdicts, error rate by type, fixes applied.

### Step 8: Summary

Report:
- Total links written
- Distribution by relationship type
- Findings with the most connections (potential "hub" patterns)
- Categories with the most cross-category links
- Validation sample size, error rate, and fixes applied

## Calibration Notes

- **Precision over recall.** A false link is worse than a missing link. The binary tests are deliberately strict. If a subagent is unsure, it should NOT propose the link.
- **One relationship per pair.** If a pair could be both `enables` and `same-problem`, choose the more specific one (`enables`). The priority order is: enables > extends > same-problem > contradicts.
- **Don't link everything.** Most pairs will have no relationship. A well-linked KB targets 2-4 links per finding on average. Apply a soft cap of ~15 links per finding — beyond that, raise the threshold for additional links to that finding to prevent hub distortion.
- **Summaries are sufficient for initial evaluation** — but summaries produce ~30% false positives on `same-problem` (the loosest test). This is expected; the mandatory Step 7 validation pass catches these using full file reads. Do NOT skip validation.
- **same-problem is the error-prone type.** Contradicts, enables, and extends have tight binary tests that produce high-precision results from summaries alone. Same-problem's Q1 ("same problem?") is subjective enough that subagents default to YES when they see topical overlap. The anti-patterns in the prompt template exist to counter this — make sure they are included.
- **Cross-category links are the highest value.** Same-category relationships are useful but less surprising. The real KB quality win is discovering that a Context Engineering finding `enables` an Orchestration finding — these are the insights that help the Codifier during classification and extraction.
- **Run incrementally.** After a backfill of 20 new findings, run with `--category` for the affected categories rather than re-evaluating the entire KB.
- **Existing links are preserved.** If a finding already has `related_findings:` entries, don't remove them — only add new ones. Dedup against existing links before proposing.

## Lessons from Full KB Pass (2026-04-08)

Reference data from the first full-KB crosslink pass (323 findings, 800 pairs evaluated):

- **Hit rate:** 27% (218 links from 800 pairs). If your hit rate is much higher (>40%), the subagents are likely being too loose on same-problem.
- **Type distribution:** 89% same-problem, 5% contradicts, 4% enables, 1% extends. Same-problem dominates because it's the loosest test. If contradicts or enables are >10% of total, double-check — those are the high-precision types.
- **Validation error rates by type:** contradicts 0% errors, enables ~40% errors (over-reach on Q2), same-problem ~30-60% errors (category proximity false positives). Budget validation time accordingly.
- **Hub cap matters:** Without a cap, one finding (KISS Commandments) accumulated 40 links. This distorts the graph and makes that finding appear in every Codifier cross-finding query. The soft cap of ~15 prevents this.
- **YAML writing:** Regex-based frontmatter editing broke 84/161 files on first attempt due to multi-line `related_findings` entries. Always use `kb_parser.write_frontmatter()` — it validates round-trip parsing before writing.
- **Enables error rate in bulk operations:** Dedicated crosslink evaluation produces ~40% enables errors. Bulk migration/classification produces ~85% enables errors. The difference is scrutiny level. When classifying legacy untyped links, default to same-problem unless the dependency is definitional (B is an explicit sub-component of A).

## Isolate De-Isolation Procedure

When targeting isolated findings specifically, subagent-only evaluation is insufficient — agents over-index on precision and reject borderline-valid connections that would reduce isolation. Use a two-pass approach:

1. **Pass 1 (subagent screen):** Run the standard evaluation procedure. Accept any links the subagent approves.
2. **Pass 2 (manual review):** For any isolate that remains unlinked after Pass 1, manually review the top 3-5 candidate pairs that the subagent rejected. Read full "What It Is" sections yourself and re-apply the binary tests. Subagents evaluating isolates rejected 100% of candidates in the 2026-04-08 session; manual review recovered 2 valid links from the same candidates.

This two-pass approach is only needed for isolate-targeting passes, not for general crosslink evaluation where subagent precision is appropriate.
