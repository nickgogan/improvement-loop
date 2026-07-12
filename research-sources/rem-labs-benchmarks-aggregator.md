---
name: "REM Labs LongMemEval Aggregated Leaderboard"
source_type: "Leaderboard / Benchmark Aggregation"
status: "Done"
date_processed: "2026-04-23"
date_published: null
key_takeaways: "Most-referenced third-party aggregated LongMemEval table. Published and maintained by REM Labs (vendor of Dream Engine, itself a ranked system on the table — disclosed conflict-of-interest). As of 2026-04-23 the leaderboard ordering is: AgentMemory 96.2%, Chronos 95.6%, Hindsight/TEMPR 94.6%, REM Labs/Dream Engine 94.6%, Supermemory 81.6%, Mem0 66.9%, Zep/Graphiti 63.8%, GPT-4 native 52.9%. MemPalace (96.6% headline claim, previously listed as #1 in session 56's snapshot) is NOT on the current table — meaningful leaderboard volatility in ~3 weeks. All rows scored against 500-question LongMemEval with GPT-4o judge (temperature=0, max_tokens=10, n=1) via official anscheck_prompt. Methodology explicitly reproducible via public containers. Most important governance signal: REM Labs has announced external benchmark hosting at benchlist.ai, ceding scoring authority to an independent party 'because the scoring authority should sit above any single vendor.' That intentional ceding is the primary evidence for the external-benchmark-hosting-as-trust-mechanism finding."
relevance: "High"
added_by: "Claude"
tags: ["benchmarking", "leaderboard", "memory-architecture", "governance", "conflict-of-interest"]
url: "https://remlabs.ai/benchmarks"
authority: ["rem-labs"]
findings:
  - "external-benchmark-hosting-as-trust-mechanism.md"
date_added: "2026-04-23"
---
