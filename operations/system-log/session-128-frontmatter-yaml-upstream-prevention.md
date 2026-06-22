---
notion_id: null
log_entry: |-
  Session 128: upstream frontmatter/YAML prevention — block-scalar authoring convention in 7 producers + pre-commit linter (DD-114)
actor: "Agent: Claude"
area: null
change_type: "Data Integrity"
milestone: null
rationale: |-
  Session 127 fixed 40 frontmatter parse failures downstream with a one-off patcher (removed, Rule 11) but left the upstream cause unaddressed: every active intake/governance skill hand-writes frontmatter using inline quoted prose scalars, which break on a colon, an embedded quote, or a soft-wrap. Traced the producers (research-loop, research-query, promote-findings, watch-blogs author findings/sources; /sl, /dd, /ib author governance entries; identify-artifacts/source-triage are report-only; kb_parser.write_frontmatter is the yaml.dump-safe path but has no caller). Nick authorized prevention layer (a) authoring convention + (c) pre-commit linter, and asked to verify the claim that kb_parser is "useless" before any cleanup. Verified it is NOT: the module is imported by linkage_analyzer/crosslink_pair_generator/crosslink_coverage, and write_frontmatter is the intentionally-retained reusable safe-writer per its origin SL — no cleanup performed. DD-114 records the policy and the mechanism.
source_dd: "DD-114"
target_system: "improvement-loop"
timestamp: "2026-06-22T00:00:00.000Z"
---

## What Changed

- **`_schema.yaml`**: added the canonical "Frontmatter authoring rules (YAML safety)" contract — prose fields as literal block scalars (`|-`), lists with uniform 2-space indent and no duplicates.
- **7 producer skills** updated to model the safe block-scalar form and point to the contract: `research-loop` (sources/findings/authorities templates + Conventions note), `research-query`, `promote-findings`, `watch-blogs`, `/sl`, `/dd`, `/ib`.
- **New linter** `operations/kb-maintenance-scripts/validate_frontmatter.py` — validates named files, `--all` (git-tracked corpus), or stdin paths; binary YAML-parse check; reuses `kb_parser.ROOT`.
- **Pre-commit hook** — tracked master at `operations/kb-maintenance-scripts/hooks/pre-commit`, installed as `.git/hooks/pre-commit` (symlink). Blocks commits introducing unparseable frontmatter; `git commit --no-verify` bypasses one commit.
- **DD-114** filed (Binding) — the prevention policy + mechanism.

## Verification

- Linter: `--all` over the git-tracked corpus → 0 failures (exit 0). Deliberate bad file (prose colon + mixed-indent list) → caught (exit 1). Valid block-scalar file → passes (exit 0).
- `--all` initially flagged 18 files under `watched-libraries/_tmp/repo-cache/` (third-party clones); confirmed gitignored and scoped `--all` to `git ls-files` so it matches the committed corpus only.

## Affected Items

- Closes the upstream gap from SL `session-127-frontmatter-yaml-hygiene-sweep.md`.
- `kb_parser` verified load-bearing; `write_frontmatter` retained (origin SL `kb-parser-write-frontmatter-added.md`).
