---
name: "Can AI Agents Answer Your Data Questions? A Benchmark for Data Agents (DAB)"
source_type: "Research Paper"
status: "Done"
key_takeaways: "Data Agent Benchmark (DAB) — first benchmark covering the full pipeline of integrating, transforming, and analyzing data across multiple heterogeneous database systems. 54 queries across 12 datasets, 9 domains, 4 DBMS. Best frontier model (Gemini-3-Pro) scores only 38% pass@1. Grounded in formative study of enterprise data agent workloads across six industries. Five frontier LLMs benchmarked; failure modes analyzed. Code at github.com/ucbepic/DataAgentBench."
relevance: "Medium"
added_by: "Nick"
tags:
  - "evaluation"
  - "benchmark"
  - "data-agents"
  - "multi-database"
url: "https://arxiv.org/abs/2603.20576"
authority:
  - "uc-berkeley-epic-lab.md"
findings:
  - "data-agent-benchmark-dab-cross-dbms-pipeline-eval.md"
date_added: "2026-04-20"
date_processed: "2026-04-20"
date_published: "2026-03-21"
---

# Can AI Agents Answer Your Data Questions? A Benchmark for Data Agents

arXiv:2603.20576 v1, submitted 21 March 2026. Authors: Ruiying Ma, Shreya Shankar, Ruiqi Chen, Yiming Lin, Sepanta Zeighami, Rajoshi Ghosh, Abhinav Gupta, Anushrut Gupta, Tanmai Gopal, Aditya G. Parameswaran. Category: cs.DB.

## Abstract (Verbatim)

"Users across enterprises increasingly rely on AI agents to query their data through natural language. However, building reliable data agents remains difficult because real-world data is often fragmented across multiple heterogeneous database systems, with inconsistent references and information buried in unstructured text. Existing benchmarks only tackle individual pieces of this problem -- e.g., translating natural-language questions into SQL queries, answering questions over small tables provided in context -- but do not evaluate the full pipeline of integrating, transforming, and analyzing data across multiple database systems. To fill this gap, we present the Data Agent Benchmark (DAB), grounded in a formative study of enterprise data agent workloads across six industries. DAB comprises 54 queries across 12 datasets, 9 domains, and 4 database management systems. On DAB, the best frontier model (Gemini-3-Pro) achieves only 38% pass@1 accuracy. We benchmark five frontier LLMs, analyze their failure modes, and distill takeaways for future data agent development."

## Contributions

- DAB benchmark construction grounded in enterprise formative study
- Scale: 54 queries, 12 datasets, 9 domains, 4 DBMS types
- First full-pipeline assessment (integration + transformation + analysis) across heterogeneous systems
- Failure mode analysis across five frontier LLMs

## Resources

- PDF: https://arxiv.org/pdf/2603.20576
- HTML: https://arxiv.org/html/2603.20576v1
- Benchmark code: https://github.com/ucbepic/DataAgentBench
- DOI: https://doi.org/10.48550/arXiv.2603.20576
