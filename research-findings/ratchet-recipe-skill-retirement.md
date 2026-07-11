---
name: Ratchet Recipe — Outcome-Driven Skill Retirement with Evidence Floor and Capacity Cap
summary: 'A minimal three-mechanism governance recipe that keeps a self-evolving skill library healthy: retire a skill only when it has enough trials AND a measurably negative contribution (evidence floor
  Nmin=100, threshold 0.10), hard-cap the active bank (C=50, evicting the lowest contributor), and constrain skill authoring with a meta-skill prior. Verified: pass@1 0.258 to 0.584 on MBPP+ hard-100 (Claude
  Opus 4.7, 3 seeds, 100 rounds), at 43% more LLM calls. This is a candidate blueprint for lifecycle rules over our own roster and extracts: outcome-linked retirement plus a bounded active set, with a deliberately
  conservative evidence bar.'
implementation_notes: 'Flagged P2 as the concrete design input for any engine skill/extract lifecycle rule. Components:

  (1) outcome-driven retirement — retire skill s only when trials n(s) >= Nmin AND empirical

  contribution c(s) <= -tau; defaults Nmin=100, tau=0.10, calibrated so useful skills survive

  stochastic noise (Hoeffding epsilon ~0.20) but harmful ones eventually go; (2) bounded active-skill

  cap C=50 with lowest-contribution eviction, which yields a non-divergence guarantee (drift below

  the no-skill floor bounded by tau + epsilon + C*delta); (3) meta-skill authoring prior (see the

  separate finding — it alone carries 57% of the gain). Costs: 43% more LLM calls, 2.8x wall time.

  Doubling the cap to 100 kept the mean but blew up variance (+/-0.110 vs +/-0.018) — the cap buys

  stability, not just ceiling. For the engine, trials-based scoring needs a usage-outcome signal we

  do not currently log; see the contribution-scoring telemetry finding.'
category: Governance
evidence_strength: Medium (empirical benchmarks)
adoption_status: Not Yet Started
priority: P2 (Design Required)
applicability:
- General
adopted_in: []
sources:
- arxiv-skill-library-drift-ratchet-recipe.md
related_findings:
- file: skill-library-drift-failure-mode.md
  rel: same-problem
- file: per-skill-contribution-scoring-telemetry.md
  rel: enabled-by
- file: meta-skill-authoring-prior-dominance.md
  rel: extended-by
proposals: null
date_discovered: '2026-07-11'
last_updated: '2026-07-11'
---

# Ratchet Recipe — Outcome-Driven Skill Retirement with Evidence Floor and Capacity Cap

## What It Is

The governance fix for skill-library drift proposed and verified in arXiv 2605.19576. Three load-bearing mechanisms:

1. **Outcome-driven retirement.** Each skill accumulates a contribution score from an append-only evidence log. A skill is retired only when it has at least Nmin=100 recorded trials **and** its empirical contribution is at or below −τ (τ=0.10). The floor is deliberately conservative: tight enough that harmful skills eventually leave, loose enough that useful skills survive stochastic noise.
2. **Bounded active-skill cap.** A hard cap of C=50 active skills; when synthesis would exceed it, the lowest-contribution skill is evicted. This bounds retrieval degradation and yields a formal non-divergence guarantee (expected pass@1 cannot drift below the no-skill floor by more than τ + ε + Cδ).
3. **Meta-skill authoring prior.** A document constraining the skill synthesizer to produce stylistically consistent skills, reducing harmful/redundant skill birth at the source (covered in a separate finding — it alone accounts for 57% of the gain).

**Results:** pass@1 0.258 → 0.584 late-window mean (peak 0.658) on MBPP+ hard-100, Claude Opus 4.7, 3 seeds over 100 rounds; healthy router engagement at ~73%. **Cost:** ~14.5k LLM calls per 100 rounds vs 10k baseline (43% more), wall time 6.5h vs 2.3h.

## Why It Matters

This is the first verified end-to-end recipe for the lifecycle problem every accumulating agent system eventually hits, and its parameter choices carry the design lesson: the ablation with a harsh floor (Nmin=20, τ=0.0) went *below* the no-skill baseline, and doubling the cap kept the mean but multiplied variance six-fold. For the engine's roster and extracts pipeline, the transferable shape is: retirement must be outcome-linked and evidence-floored, and a bounded active set is a stability mechanism, not just a size limit.

## Why People Are Using It

Published with reproducible ablations at ICML 2026's agentic-failure-modes workshop; it directly answers the SkillsBench finding that ungoverned LLM-authored skills add nothing. The recipe is minimal (three mechanisms) and comes with a non-divergence guarantee, making it attractive as a default governance layer for self-evolving libraries.

## Potential Alternatives

Human curation at intake (the +16.2pp SkillsBench arm — works, but does not scale and does not retire); explicit dedup/canonicalization machinery (the paper's ablations show it is unnecessary and slightly harmful once the authoring prior exists); periodic wholesale library resets (loses accumulated value, no evidence basis).

## Potential Improvements

- Principled (rather than empirical) calibration of Nmin/τ/C per domain — flagged by the authors as future work.
- Adapting "trials" for low-frequency libraries: an engine skill may see 100 invocations over months, so the evidence floor may need time-decay or proxy signals instead of raw counts.

## Potential Failure Modes

- **Insufficient evidence floor**: the A4 ablation is the canonical warning — harsh retirement drove performance below no-skill baseline.
- **Score attribution noise**: contribution scores depend on a critic's helped/hurt verdicts; a miscalibrated critic silently retires good skills.
- **Cap-eviction thrash**: near the cap, newly synthesized skills can evict skills whose scores have not converged, churning the bank.
