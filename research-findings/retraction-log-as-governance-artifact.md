---
name: "Retraction Log as First-Class Governance Artifact"
summary: "A dated, append-only `HISTORY.md` (distinct from `CHANGELOG.md`) captures public claims the team retracted, audit responses, and impostor-domain notices. Each entry names the retracted claim, root cause, and every file/surface where the claim was removed — correction-as-product rather than silent edits in git history."
implementation_notes: null
category: "Governance"
evidence_strength: "Medium (practitioner-documented)"
adoption_status: "Not Yet Started"
priority: null
applicability:
  - "General"
adopted_in: []
sources: []
related_findings:
  - file: external-benchmark-hosting-as-trust-mechanism.md
    rel: same-problem
  - file: benchmark-dataset-deprecation-lifecycle.md
    rel: extended-by
  - file: experimental-sandbox-labeling-discipline.md
    rel: same-problem
  - file: production-configuration-baseline-discipline.md
    rel: same-problem
proposals: null
date_discovered: "2026-04-23"
last_updated: "2026-04-23"
pipeline_status: raw
consumed_by: []
---

## What It Is

A governance artifact that records, in chronological order, every public claim the project has retracted — separate from the version-by-version CHANGELOG. The file is append-only, newest entries first. Each entry contains:

- The retracted claim verbatim.
- Who identified it (often a community audit with cross-linked issue).
- The root cause (what was wrong with the original claim).
- Every file or surface where the claim was removed (full audit trail).
- Explicit self-disclosure when the original claim would have been a methodological problem in peer-reviewed work.

MemPalace's `docs/HISTORY.md` has three types of entries in its first two weeks post-launch: benchmark-table rewrites (2026-04-14, issue-linked), impostor-domain notices with community-reported issues cross-linked (2026-04-11), and founder retraction notes addressing community criticism itemizing "what we got wrong" vs "what's still true" (2026-04-07).

## Why It Matters

When a claim in a project's public surface turns out to be wrong, teams face a choice: edit quietly, or publish the correction. Silent edits destroy provenance for readers who saw the original claim and broke trust if discovered. Public corrections carry reputation cost but establish a pattern of epistemic honesty that compounds. A dedicated retraction log makes correction-as-product the path of least resistance — there's a canonical home for it, separate from changelog noise.

For MetaSystem: the IL publishes findings, the Owner publishes governance, and all three systems publish claims in their docs. When any of those turns out to be wrong — a benchmark misinterpreted, a DD reasoning flawed, an audit misattributed — a retraction log gives a non-git-archaeology way to surface the correction. Directly transferable to the KB, to DD governance (when supersession rationale needs explicit retraction framing), and to any public-facing claim surface.

## Why People Are Using It

Observed in [MemPalace](https://github.com/MemPalace/mempalace) 3.3.2 — see [[mempalace-analysis]] for structural details. The project launched at 48 hours post-public-release with several factually wrong benchmark claims; the community caught them within hours. Rather than quiet-editing, the team created `docs/HISTORY.md` and restructured every affected surface. The 2026-04-14 entry documents a full-surface retraction of a "+34% palace boost" claim across README, landing pages, multiple website files, and benchmark reproduction commands — with links back to the community-reported issue that triggered the audit. The founder note on 2026-04-07 explicitly states: "Brutal honest criticism is exactly what makes open source work, and it's what we asked for... we'd rather be right than impressive."

## Potential Alternatives

- **Silent git history** — commits quietly update text; no canonical retraction home. Loses the correction signal.
- **CHANGELOG entries** — version-scoped; retractions get buried between feature entries.
- **Blog posts or Twitter threads** — ephemeral; no source-of-truth alignment with the codebase.
- **GitHub Issues with `retraction` label** — fragmented; requires issue hunting rather than linear reading.

## Potential Improvements

- Cross-link retracted claims from the *locations that used to hold them*: when a claim is removed from a README, leave a commit comment or footnote pointing to the HISTORY.md entry so future readers of the git history see the correction path.
- Structure entries with a standard shape (`claim`, `root_cause`, `removed_from`, `triggered_by`, `disclosed_as`) so the log is machine-parseable.
- Require a retraction-log entry as part of the PR checklist when a previously-public claim is being removed.

## Potential Failure Modes

- **Retraction fatigue** — if every minor rephrasing lands in the log, the high-signal entries get diluted. The log should only hold retractions of public claims, not internal renames or stylistic changes.
- **Incomplete audit trails** — entries that don't enumerate every affected file let the claim survive in one unupdated surface. The MemPalace 2026-04-14 entry explicitly lists every location — this discipline has to be enforced.
- **Performative transparency** — the log itself can become a branding asset rather than a governance artifact. The test is whether retractions land *before* the community complains vs after.
