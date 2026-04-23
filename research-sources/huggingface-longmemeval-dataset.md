---
name: "LongMemEval Dataset on HuggingFace (xiaowu0162/longmemeval)"
source_type: "Dataset"
status: "Done"
date_processed: "2026-04-23"
key_takeaways: "Primary distribution channel for the LongMemEval benchmark dataset. 3.04 GB, MIT licensed, maintained by xiaowu0162 (one of the paper's authors). ~1,220 monthly downloads. IMPORTANT STATUS: the original dataset is DEPRECATED (2026) in favor of xiaowu0162/longmemeval-cleaned — the original contains 'noisy history sessions that interfere with answer correctness.' This is itself a meta-governance pattern: the benchmark maintainers retracted-via-deprecation when they discovered dataset noise was inflating or deflating scores in ways that made cross-system comparisons unreliable. Every published LongMemEval number should be audited for which dataset revision it targets."
relevance: "High"
added_by: "Claude"
tags: ["dataset", "benchmarking", "memory-architecture", "deprecation", "governance"]
url: "https://huggingface.co/datasets/xiaowu0162/longmemeval"
authority: ["uc-santa-barbara-longmemeval-team"]
findings:
  - "benchmark-dataset-deprecation-lifecycle.md"
date_added: "2026-04-23"
---
