# Improvement Loop — Progress

**Last Updated:** 2026-05-25 (session 105)

## Current Focus

Session 105 completed the post-extraction health check. System verified consistent: 13 active guides confirmed (count corrected from 14), G1 phantom entries removed (11→9), 5 stale G2 cross-refs fixed in G2a/G2b, 32 consumed_by back-annotations repaired, missing changelogs and SL entry created. No guides are critically stale; 19 classified-pending findings remain.

**KB totals:** ~739 findings, ~179 sources, 31 watched libraries, 30 analysis docs, cross-repo comparison updated (29 repos). 13 active guides (G1:9, G2a:35, G2b:30, G3:42, G3b:20, G4:46, G5:23, G6:5, G7:27, G8:20, G9:38, G10:37, G11:30); G2 deprecated. 0 open split proposals (G2 resolved, G3/G9 deferred).

**Next session target:** Owner — build Owner agent skills (logged-for-future item 1). Use Librarian subagent for KB best practices + Perplexity for external research. Check existing coverage first (assess-agent, assess-prompt, assess-skill may overlap).

---

## Nick's Prioritizaton

Ordered queue. Status markers: `[nick-gate]` waits on Nick's ruling; `[deferred]` held by Nick, re-evaluate on trigger; `[trigger]` waits on external evidence or volume; `[don't-do-yet]` do not reintroduce until a specific upstream condition lands.

---

## Logged-for-future

Trigger-gated carryover. Don't action unless trigger fires.

1. Create Owner agent skills: skill-assessment, skill-extraction, agent-assessment, agent-extraction. Check if these exist already.
2. Place IL system on an actual harness, not just rely on the agent to invoke the right skills to take the right actions in the right order every time. 
3. - **`[deferred]` G3 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-architecture-decisions-split-proposal.md`. At 42 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45.
4. **`[deferred]` G9 bifurcation** — Split proposal at `operations/split-proposals/2026-05-25-agent-governance-and-trust-split-proposal.md`. At 38 findings, below DD-102 threshold (45). Codifier rec: defer. Resolution added session 104. Re-evaluate when crossing 45 or enforcement cluster hits 10.
