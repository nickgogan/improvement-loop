# Transcript: Google OKF + RAG: The Ultimate AI Agent Architecture

**URL:** https://www.youtube.com/watch?v=_X55fkwdC-Q
**Segments:** 256
**Channel:** Cloud Codes
**Duration:** 9:49
**Uploaded:** 2026-06-28

---

## Full Text

Ask even the smartest AI agent a question about your own business and watch closely. What's our refund window? 30 days, it says. Instant, confident, and completely wrong. It never opened your policy. It just guessed from training data. For the last few years, the fix has been one thing, rag. Take every document you own, chop it into chunks, turn each chunk into a vector, and store it. Ask a question, pull the closest pieces, and hand them to the model. And rag is genuinely powerful until you look at what it did. It shredded your clean, structured policy into fragments, grabbed the three that looked similar, and threw away the order that made them mean anything. The answer is now a guess dressed up as a citation. But, there's a second way now. In June 2026, Google Cloud shipped OKF, the Open Knowledge Format, curated knowledge written as plain markdown files. Ask it the same question, and it answers exactly, 14 days, with a link straight to the source policy. OKF has its own ceiling, though. Someone has to write every word of it. It's precise and trustworthy and auditable. And on its own, it will never cover a million messy, unpredictable documents. So, here's the question every team is asking right now. Rag, with its endless scale and fuzzy search, or OKF, with its precision and structure, which one do you bet your agent on? Wrong question. The answer isn't one or the other, it's both. The architecture that actually wins puts OKF and rag together and takes the best of each. Watch it work. A high-stakes question routes to OKF. Exact, cited, done. An open-ended one routes to rag. Search the entire archive. Two layers of knowledge, one agent on top. OKF carries the canonical 80%. The answers you simply can't get wrong. Rag handles the long tail, the messy 20 you could never sit down and curate by hand. Precision and scale, trust and reach, structure and search. That's the hybrid stack and by the end of this video, you'll know exactly how to wire it together. Let's build rag properly, step by step. A document arrives, it gets split into chunks, usually a few hundred tokens each, and embedding model turns every chunk into a vector, a long list of numbers that captures its meaning. All of those vectors get stored in a vector database. Then someone asks a question. The question becomes a vector, too, and the database returns the chunks sitting nearest to it in that space. That's the real magic. It matches by meaning, not by keyword. Different words, same idea, and rag still finds it. This grew into a whole industry. Pinecone, Weaviate, Qdrant, Chroma, Milvus, Postgres with PG vector, systems storing billions of vectors and searching them in milliseconds. This is the thing OKF can't touch. Raw, open-ended scale across everything you've got, but chunking comes at a price. Cut a table, a step-by-step procedure, or a contract clause down the middle, and the halves stop making sense. The model gets three disconnected fragments and quietly fills the gaps between them, which is exactly how a confident hallucination is born, and retrieval is probabilistic by design. It hands back what's likely relevant, not guaranteed the one correct answer. That's wonderful for a fuzzy exploratory question. It's genuinely dangerous when the exact refund window, the exact price, or the exact dosage is what matters, and it's a black box. Change one policy and you rerun the entire ingestion pipeline. You can't diff it in a pull request. You can't easily audit what the agent actually knows, and outdated chunks sit in the index long after the truth has moved on. OKF takes the exact opposite bet. No pipeline, no embeddings, no vector store, just a folder of markdown files with a little YAML on top. The spec says it best. If you can cat a file, you can read OKF. If you can get clone a repo, you can ship it. Each file is a single concept. The front matter carries a type, and that's the only required field, plus an optional title, description, tags, a timestamp, and a resource, a link pointing at the real asset. Underneath is structured markdown, headings, tables, lists that a model reads cleanly. And concepts link to each other with ordinary markdown links. Follow them, and your knowledge turns into a graph. A table points to its data set. A playbook points to the table it repairs. You get real relationships, not a bag of disconnected chunks. Because a human authored it, retrieval is deterministic. You decide exactly what the model sees, no cosine distance lottery. The structure survives intact, and the whole thing lives in Git, so you can diff it, review it in a pull request, assign an owner, and roll back a bad edit. If this feels familiar, it should. It's the claw.md file. It's the LLM wiki Andrej Karpathy keeps pointing at. Context you engineer deliberately by hand. OKF's contribution is simply writing that pattern down as one shared, open, vendor-neutral spec everyone can target. But here's the honest limit, and it matters. OKF does not scale itself. Every concept is somebody's curation work. It's perfect for the knowledge you can't afford to get wrong, and hopeless as a dumping ground for a decade of raw, unsorted documents. So, you build both, and you put a router in front. A query comes in, is it canonical and high stakes? Send it to OKF for an exact, cited answer. Is it open-ended, exploratory, buried somewhere in the archive? Send it to RAG. Every query goes where it's strongest. The cleanest way to picture it is an 80/20 split. OKF is the spine, the curated, structured, high-trust core of what your agent knows. RAG is the reach, the huge, messy, unbounded long tail you could never realistically handwrite. Make it concrete. A support agent gets two questions. What's our refund window? That's canonical, so it hits OKF and answers 14 days exactly with the policy linked. Has anyone hit this weird billing bug before? That's open-ended, so it hits rag and searches 40,000 old tickets. Same agent, two completely different knowledge paths, and the two make each other better. OKF gives rag ground truth. When a curated concept exists for a question, the agent trusts that over a fuzzy retrieved chunk, and that single rule makes a real measurable dent in hallucinations. OKF also hands the agent a map. Its index files list what knowledge exists before any search runs, progressive disclosure. So, the agent drills into rag only where the curated answer runs out instead of blindly searching from zero every single time. And rag gives OKF reach. Point semantic search at the bundle itself and at everything sprawling beyond it. Curation covers the critical core, retrieval covers the endless rest. Neither one has to pretend it can do the other's job, and the best part, the agent doesn't have to care which is which. Put the OKF bundle in the vector index behind one retrieval interface, even a single MCP server, and the model just asks for knowledge. All the routing and plumbing stays hidden underneath. Now, lay the score card side by side. Precision from OKF, scale from rag, trust and breadth, structure and fuzzy search, get diffable and auto indexed. For the first time, you stop trading one good thing away just to get the other, and the economics line up, too. An OKF bundle is just text in Git. Write it once, edit a line, done. Rag carries real running cost, embedding every document, re-embedding it when it changes, and hosting a vector database that never sleeps. Curate what's worth curating, pay to index the rest. So, practically, when do you reach for OKF on its own? Small curated knowledge bases. High-stakes answers that have to be exact, highly structured tables and procedures, and anything you want versioned in Git and owned by a real accountable human. When is it RAG on its own? A huge unstructured pile of text, open-ended questions you can't predict in advance, contracts, support tickets, transcripts, PDFs, heterogeneous sources where good enough semantic matching is honestly good enough. And when do you run both? Almost every serious agent headed for production. The high-stakes core lives in OKF, the long tail lives in RAG, and a thin router in the middle decides, query by query, who answers. Now, let's kill two myths. First, OKF does not make RAG obsolete. The moment your corpus is too big or too fuzzy to curate by hand, vector search wins, and it isn't close. RAG is not going anywhere. Second, no, you can't just dump everything into one giant context window and call it solved. Irrelevant knowledge actively degrades the answer and quietly burns tokens. Selective routed retrieval still beats brute force, even at a million tokens of context. In the real world, this is a team sport. Data owners curate the OKF bundles, engineers index the archive into a vector store. Frameworks like LangChain and LlamaIndex wire the two together, and an agent, Claude, ChatGPT, or Gemini, quietly consumes both. And it's moving fast. OKF is only weeks old and already thousands of GitHub stars deep, with agents now starting to write OKF bundles themselves. Curated structure and raw retrieval are converging, graph and vector, authored and searched, folding into one stack. So, that's the whole picture in one frame. A router up top, OKF as the curated spine, RAG for the long tail, one grounded agent sitting above both. It was never OKF versus RAG. [music] It's OKF plus RAG. If that finally made the AI knowledge that click, do me a favor and subscribe. Cloud Code takes apart one system exactly like this every single week. Build, solve, deploy. And I'll see you in the next one.

---

## Timestamped Segments

**[0:00]** Ask even the smartest AI agent a

**[0:02]** question about your own business and

**[0:03]** watch closely. What's our refund window?

**[0:06]** 30 days, it says. Instant, confident,

**[0:09]** and completely wrong. It never opened

**[0:11]** your policy. It just guessed from

**[0:12]** training data. For the last few years,

**[0:15]** the fix has been one thing, rag. Take

**[0:18]** every document you own, chop it into

**[0:20]** chunks, turn each chunk into a vector,

**[0:22]** and store it. Ask a question, pull the

**[0:25]** closest pieces, and hand them to the

**[0:27]** model. And rag is genuinely powerful

**[0:30]** until you look at what it did. It

**[0:31]** shredded your clean, structured policy

**[0:33]** into fragments, grabbed the three that

**[0:35]** looked similar, and threw away the order

**[0:37]** that made them mean anything. The answer

**[0:39]** is now a guess dressed up as a citation.

**[0:42]** But, there's a second way now. In June

**[0:44]** 2026, Google Cloud shipped OKF, the Open

**[0:47]** Knowledge Format, curated knowledge

**[0:50]** written as plain markdown files. Ask it

**[0:52]** the same question, and it answers

**[0:54]** exactly, 14 days, with a link straight

**[0:57]** to the source policy. OKF has its own

**[1:00]** ceiling, though. Someone has to write

**[1:02]** every word of it. It's precise and

**[1:04]** trustworthy and auditable. And on its

**[1:06]** own, it will never cover a million

**[1:08]** messy, unpredictable documents. So,

**[1:10]** here's the question every team is asking

**[1:12]** right now. Rag, with its endless scale

**[1:14]** and fuzzy search, or OKF, with its

**[1:18]** precision and structure, which one do

**[1:20]** you bet your agent on? Wrong question.

**[1:22]** The answer isn't one or the other, it's

**[1:24]** both. The architecture that actually

**[1:26]** wins puts OKF and rag together and takes

**[1:29]** the best of each. Watch it work. A

**[1:32]** high-stakes question routes to OKF.

**[1:34]** Exact, cited, done. An open-ended one

**[1:38]** routes to rag. Search the entire

**[1:40]** archive. Two layers of knowledge, one

**[1:43]** agent on top. OKF carries the canonical

**[1:45]** 80%. The answers you simply can't get

**[1:48]** wrong. Rag handles the long tail, the

**[1:51]** messy 20 you could never sit down and

**[1:52]** curate by hand. Precision and scale,

**[1:55]** trust and reach, structure and search.

**[1:58]** That's the hybrid stack and by the end

**[2:00]** of this video, you'll know exactly how

**[2:01]** to wire it together. Let's build rag

**[2:04]** properly, step by step. A document

**[2:06]** arrives, it gets split into chunks,

**[2:08]** usually a few hundred tokens each, and

**[2:11]** embedding model turns every chunk into a

**[2:13]** vector, a long list of numbers that

**[2:15]** captures its meaning. All of those

**[2:17]** vectors get stored in a vector database.

**[2:19]** Then someone asks a question. The

**[2:21]** question becomes a vector, too, and the

**[2:23]** database returns the chunks sitting

**[2:25]** nearest to it in that space. That's the

**[2:27]** real magic. It matches by meaning, not

**[2:29]** by keyword. Different words, same idea,

**[2:32]** and rag still finds it. This grew into a

**[2:35]** whole industry. Pinecone, Weaviate,

**[2:38]** Qdrant, Chroma, Milvus, Postgres with PG

**[2:41]** vector, systems storing billions of

**[2:43]** vectors and searching them in

**[2:45]** milliseconds. This is the thing OKF

**[2:47]** can't touch. Raw, open-ended scale

**[2:49]** across everything you've got, but

**[2:51]** chunking comes at a price. Cut a table,

**[2:54]** a step-by-step procedure, or a contract

**[2:56]** clause down the middle, and the halves

**[2:58]** stop making sense. The model gets three

**[3:00]** disconnected fragments and quietly fills

**[3:02]** the gaps between them, which is exactly

**[3:04]** how a confident hallucination is born,

**[3:06]** and retrieval is probabilistic by

**[3:08]** design. It hands back what's likely

**[3:11]** relevant, not guaranteed the one correct

**[3:13]** answer. That's wonderful for a fuzzy

**[3:15]** exploratory question. It's genuinely

**[3:17]** dangerous when the exact refund window,

**[3:19]** the exact price, or the exact dosage is

**[3:22]** what matters, and it's a black box.

**[3:25]** Change one policy and you rerun the

**[3:26]** entire ingestion pipeline. You can't

**[3:29]** diff it in a pull request. You can't

**[3:31]** easily audit what the agent actually

**[3:32]** knows, and outdated chunks sit in the

**[3:35]** index long after the truth has moved on.

**[3:37]** OKF takes the exact opposite bet. No

**[3:40]** pipeline, no embeddings, no vector

**[3:42]** store, just a folder of markdown files

**[3:45]** with a little YAML on top. The spec says

**[3:47]** it best. If you can cat a file, you can

**[3:50]** read OKF. If you can get clone a repo,

**[3:53]** you can ship it. Each file is a single

**[3:55]** concept. The front matter carries a

**[3:57]** type, and that's the only required

**[3:59]** field, plus an optional title,

**[4:01]** description, tags, a timestamp, and a

**[4:04]** resource, a link pointing at the real

**[4:06]** asset. Underneath is structured

**[4:08]** markdown, headings, tables, lists that a

**[4:11]** model reads cleanly. And concepts link

**[4:13]** to each other with ordinary markdown

**[4:15]** links. Follow them, and your knowledge

**[4:17]** turns into a graph. A table points to

**[4:20]** its data set. A playbook points to the

**[4:22]** table it repairs. You get real

**[4:24]** relationships, not a bag of disconnected

**[4:26]** chunks. Because a human authored it,

**[4:28]** retrieval is deterministic. You decide

**[4:31]** exactly what the model sees, no cosine

**[4:33]** distance lottery. The structure survives

**[4:35]** intact, and the whole thing lives in

**[4:37]** Git, so you can diff it, review it in a

**[4:40]** pull request, assign an owner, and roll

**[4:42]** back a bad edit. If this feels familiar,

**[4:45]** it should. It's the claw.md file. It's

**[4:48]** the LLM wiki Andrej Karpathy keeps

**[4:50]** pointing at. Context you engineer

**[4:52]** deliberately by hand. OKF's contribution

**[4:55]** is simply writing that pattern down as

**[4:57]** one shared, open, vendor-neutral spec

**[4:59]** everyone can target.

**[5:01]** But here's the honest limit, and it

**[5:02]** matters. OKF does not scale itself.

**[5:05]** Every concept is somebody's curation

**[5:07]** work. It's perfect for the knowledge you

**[5:09]** can't afford to get wrong, and hopeless

**[5:11]** as a dumping ground for a decade of raw,

**[5:13]** unsorted documents. So, you build both,

**[5:16]** and you put a router in front. A query

**[5:18]** comes in, is it canonical and high

**[5:20]** stakes? Send it to OKF for an exact,

**[5:23]** cited answer. Is it open-ended,

**[5:25]** exploratory, buried somewhere in the

**[5:27]** archive? Send it to RAG. Every query

**[5:29]** goes where it's strongest. The cleanest

**[5:32]** way to picture it is an 80/20 split. OKF

**[5:35]** is the spine, the curated, structured,

**[5:37]** high-trust core of what your agent

**[5:39]** knows. RAG is the reach, the huge,

**[5:42]** messy, unbounded long tail you could

**[5:44]** never realistically handwrite. Make it

**[5:46]** concrete. A support agent gets two

**[5:48]** questions. What's our refund window?

**[5:50]** That's canonical, so it hits OKF and

**[5:53]** answers 14 days exactly with the policy

**[5:56]** linked. Has anyone hit this weird

**[5:58]** billing bug before? That's open-ended,

**[6:00]** so it hits rag and searches 40,000 old

**[6:02]** tickets. Same agent, two completely

**[6:05]** different knowledge paths, and the two

**[6:07]** make each other better. OKF gives rag

**[6:09]** ground truth. When a curated concept

**[6:12]** exists for a question, the agent trusts

**[6:14]** that over a fuzzy retrieved chunk, and

**[6:16]** that single rule makes a real measurable

**[6:18]** dent in hallucinations. OKF also hands

**[6:21]** the agent a map. Its index files list

**[6:24]** what knowledge exists before any search

**[6:25]** runs, progressive disclosure. So, the

**[6:28]** agent drills into rag only where the

**[6:30]** curated answer runs out instead of

**[6:32]** blindly searching from zero every single

**[6:34]** time. And rag gives OKF reach. Point

**[6:37]** semantic search at the bundle itself and

**[6:39]** at everything sprawling beyond it.

**[6:41]** Curation covers the critical core,

**[6:43]** retrieval covers the endless rest.

**[6:45]** Neither one has to pretend it can do the

**[6:47]** other's job, and the best part, the

**[6:50]** agent doesn't have to care which is

**[6:51]** which.

**[6:52]** Put the OKF bundle in the vector index

**[6:54]** behind one retrieval interface, even a

**[6:56]** single MCP server, and the model just

**[6:59]** asks for knowledge. All the routing and

**[7:01]** plumbing stays hidden underneath.

**[7:03]** Now, lay the score card side by side.

**[7:05]** Precision from OKF, scale from rag,

**[7:08]** trust and breadth, structure and fuzzy

**[7:10]** search, get diffable and auto indexed.

**[7:13]** For the first time, you stop trading one

**[7:16]** good thing away just to get the other,

**[7:17]** and the economics line up, too. An OKF

**[7:20]** bundle is just text in Git. Write it

**[7:22]** once, edit a line, done. Rag carries

**[7:25]** real running cost, embedding every

**[7:28]** document, re-embedding it when it

**[7:29]** changes, and hosting a vector database

**[7:32]** that never sleeps. Curate what's worth

**[7:34]** curating, pay to index the rest. So,

**[7:37]** practically, when do you reach for OKF

**[7:39]** on its own? Small curated knowledge

**[7:42]** bases. High-stakes answers that have to

**[7:44]** be exact, highly structured tables and

**[7:46]** procedures, and anything you want

**[7:48]** versioned in Git and owned by a real

**[7:50]** accountable human. When is it RAG on its

**[7:53]** own? A huge unstructured pile of text,

**[7:55]** open-ended questions you can't predict

**[7:57]** in advance,

**[7:58]** contracts, support tickets, transcripts,

**[8:01]** PDFs, heterogeneous sources where good

**[8:04]** enough semantic matching is honestly

**[8:06]** good enough. And when do you run both?

**[8:08]** Almost every serious agent headed for

**[8:10]** production. The high-stakes core lives

**[8:12]** in OKF, the long tail lives in RAG, and

**[8:15]** a thin router in the middle decides,

**[8:17]** query by query, who answers. Now, let's

**[8:20]** kill two myths. First, OKF does not make

**[8:23]** RAG obsolete.

**[8:25]** The moment your corpus is too big or too

**[8:27]** fuzzy to curate by hand, vector search

**[8:29]** wins, and it isn't close. RAG is not

**[8:32]** going anywhere. Second, no, you can't

**[8:35]** just dump everything into one giant

**[8:37]** context window and call it solved.

**[8:39]** Irrelevant knowledge actively degrades

**[8:41]** the answer and quietly burns tokens.

**[8:43]** Selective routed retrieval still beats

**[8:45]** brute force, even at a million tokens of

**[8:47]** context. In the real world, this is a

**[8:50]** team sport. Data owners curate the OKF

**[8:53]** bundles, engineers index the archive

**[8:55]** into a vector store. Frameworks like

**[8:57]** LangChain and LlamaIndex wire the two

**[8:59]** together, and an agent, Claude, ChatGPT,

**[9:03]** or Gemini, quietly consumes both. And

**[9:05]** it's moving fast. OKF is only weeks old

**[9:08]** and already thousands of GitHub stars

**[9:10]** deep, with agents now starting to write

**[9:12]** OKF bundles themselves. Curated

**[9:14]** structure and raw retrieval are

**[9:16]** converging, graph and vector, authored

**[9:19]** and searched, folding into one stack.

**[9:22]** So, that's the whole picture in one

**[9:23]** frame. A router up top, OKF as the

**[9:26]** curated spine, RAG for the long tail,

**[9:29]** one grounded agent sitting above both.

**[9:32]** It was never OKF versus RAG. [music]

**[9:34]** It's OKF plus RAG. If that finally made

**[9:37]** the AI knowledge that click, do me a

**[9:39]** favor and subscribe. Cloud Code takes

**[9:42]** apart one system exactly like this every

**[9:44]** single week. Build, solve, deploy. And

**[9:47]** I'll see you in the next one.
