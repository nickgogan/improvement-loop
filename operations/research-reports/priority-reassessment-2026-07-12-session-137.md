---
title: "Priority Reassessment Report — 2026-07-12 (session 137)"
type: "research-report"
category: "priority-reassessment"
created: "2026-07-12"
author: "improvement-loop"
findings_scanned: 9
candidates_flagged: 3
---

# Priority Reassessment Report — 2026-07-12 (session 137)

Scoped pass over the five corroboration sets annotated in-file by the session-136
extraction sweep (delta report §Updated Findings). Not a full-KB scan. Companion to
`priority-reassessment-2026-07-12.md` (session 132 scoped run — its verbatim-storage
null→P3 proposal is still ungated and rides the same checkpoint).

## Summary

- Findings scanned: 9
- Reassessment candidates: 3 (2 priority bumps, 1 evidence-strength flag)
- Proposed priority bumps: 2
- Proposed evidence upgrades: 1 (flagged for judgment — no defined Medium→Strong criterion)
- Proposed adoption status changes: 0

## Candidates

### Scale Threshold Heuristic: Obsidian Wiki vs True RAG
- **Current priority:** P3 (Monitor)
- **Proposed priority:** P2 (Design Required)
- **Criteria triggered:** 1 (evidence accumulation), 4 (convergent implementation), 5 (related-findings cluster)
- **Evidence summary:** 3–4 independent channels — Chase AI (original + agentic-OS re-statement = one channel), Cole Medin/LlamaIndex (file search beats RAG below corpus threshold), Nate Herk (production business brain, pain-driven level selection), plus Karpathy's own documented practice. 4 sources in frontmatter; related-findings cluster has 3 extends/enables-class links (2 extended-by + 1 enables).
- **Rationale:** Crossed the 3-independent-source bar while sitting at P3, with convergence from different starting points (KB design, retrieval benchmarking, production second-brain ops). Also `adoption_status: Partially Adopted` — the engine itself is an instance. P2 (Design Required) is honest: the open design question is the per-folder refinement (`per-folder-heterogeneous-retrieval-levels`), not whether the heuristic holds.

### Frontier Model as Harness Designer
- **Current priority:** P3
- **Proposed priority:** P2 (Design Required)
- **Criteria triggered:** 1 (evidence accumulation), 4 (convergent implementation); hub-finding signal from the triage
- **Evidence summary:** First-party Anthropic post (Strong — production Bun Zig→Rust case study, shipped /deep-research skill) + Nate B Jones independent design-time framing + 3 extending sources in adjacent session-136 lanes (war-game plan format, prototype-at-frontier economics). The Prompt Engineering digest is a secondhand read of the Anthropic post, so it does not count independently. Evidence_strength already Strong.
- **Rationale:** The file itself deliberately held priority "pending /reassess-priorities" after the first-party upgrade lifted the secondhand-evidence cap. A Strong, first-party, production-cased hub finding at P3 understates it. P2 fits its actual consumer surfaces (feeds `/design-harness` and the model-capability registry Fable 5 row — both design work, not immediate implementation). Not proposing P1: independent-of-vendor replication is still thin, and the 5+-source P1 bar is not met.

### Trust Calibration via Progressive Autonomy Ramp — evidence-strength flag
- **Current evidence_strength:** Medium (practitioner-documented)
- **Flagged for judgment:** Medium → Strong (production-tested)
- **Criteria triggered:** none automatic — criterion 2 only defines Weak→Medium; Medium→Strong has no defined threshold (same situation as the loop-detection case in the session-132 report)
- **Evidence summary:** Anthropic "Trustworthy agents in practice" (Tier 1, production across Claude.ai/Desktop/Code — trained-in check-in calibration) + Cole Medin (production dark-factory experiment arriving at the supervised tier) + the original 100x/3x asymmetry report. 3 distinct source sets, two with production weight.
- **Rationale:** Presented as a flag, not a proposal — consistent with the skill's conservatism where no criterion defines the transition. Priority stays P2 either way (3 < 5-source P1 bar).

## No Change (Confirmed)

| Finding | Priority | Evidence movement (session 136) | Why no change |
|---|---|---|---|
| intent-based-meta-routing-skill | P2 (Design Required) | Thin-router corroborated at root-file altitude: 4 independent channels (Archon/Medin, Van Clief, AI Code That Works, Herk) | Already P2; 4 channels < 5-source P1 bar and production evidence is one OSS repo |
| skills-as-pointers-to-second-brain-files | P2 (Design Required) | 4 independent channels (Beni, Agentic Academy, AI Code That Works, Chase AI); loop-state application added | Already P2; P1 bar not met; extends-class links at 2 of 3 needed for criterion 5 |
| generator-assessor-separation-in-skill-iteration | P2 (Design Required) | Third independent origin (Nate B Jones cross-vendor build/attack loop) alongside Anthropic skill-creator and engine rule 10 | Already P2 + Strong + Already Adopted; 3 origins < 5-source P1 bar. Note: P1 "Implement Now" would be moot — rule 10 already operationalizes it |
| trust-calibration-progressive-autonomy-ramp | P2 (Design Required) | 3 distinct source sets (see evidence flag above) | Priority threshold not crossed; only the evidence-strength question is live |
| autonomy-gradient-not-binary-delegation | P1 (Implement Now) | Medin/Shapiro maturity-ladder axis added (when a class moves down a gate) | Already at ceiling |
| human-on-the-loop-hotl-autonomy-tiering-framework | P2 (Design Required) | 4th independent source (Medin: level-4 reliability tanks when tiering up early) | 4 < 5-source P1 bar. Watch item: one more independent production source crosses it |
| three-bucket-change-approval-tiering | P2 (Design Required) | Born at P2 with 3 sources (Marchese ×2 = one channel + cross-lane HOTL convergence) | Independent count is effectively 2 channels; P2 already reflects it. Adoption is the governance-gated DD-29 question, not a priority question |

## Gate

Proposals await Nick's approval (skill Rule 1 — no auto-changes). On approval, the
edits are frontmatter-only, block-scalar-safe, `last_updated` bumped:

1. `scale-threshold-heuristic-obsidian-vs-rag.md`: `priority: P3 (Monitor)` → `"P2 (Design Required)"`
2. `frontier-model-as-harness-designer.md`: `priority: "P3"` → `"P2 (Design Required)"`
3. (if the flag is accepted) `trust-calibration-progressive-autonomy-ramp.md`: `evidence_strength` → `"Strong (production-tested)"`
