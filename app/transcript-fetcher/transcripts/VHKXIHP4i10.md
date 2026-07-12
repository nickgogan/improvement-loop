# Transcript: Google OKF vs RAG Confusion, Finally Cleared Up

**URL:** https://www.youtube.com/watch?v=VHKXIHP4i10
**Segments:** 251
**Channel:** Cloud Codes
**Duration:** 9:00
**Uploaded:** 2026-07-08

---

## Full Text

Last week a post blew up on my feed. Four words, OKF just killed rag. It didn't. It couldn't. These two aren't even playing the same sport. So, one line, then we earn it. Rag is a process, OKF is a format. Comparing them is a category error. It's like asking whether NPM beats package.json. One is a tool that does something, the other just sits on disk. Fast catch-up. OKF is Google Cloud's Open Knowledge Format. It shipped in June, a spec on GitHub, markdown files in a folder. If you've ever written a claw.md to give your assistant context, you already get OKF. Same instinct standardized for a whole company. Rag you probably know, retrieval augmented generation. Before the model answers, you fetch relevant text and drop it into the prompt. And there's the trap. Both end the same way. Knowledge lands in the model's context. Same destination, different vehicle, which sounds like nitpicking until you pick the wrong one and spin up a vector database you never needed. So, here's the deal. By the end, you'll never mix these up again. What each one is, where each wins, and why you often want both. Start with the problem both of these are chasing. In any real company, the stuff a model needs is scattered everywhere. A table schema lives in one tool. What a metric actually means lives in someone's head. The incident runbook is buried in a wiki nobody opens. Fragmented knowledge, that's the enemy. Rag was the first big answer, so start there. It frames everything else. Picture the classic pipeline. A question comes in. A retriever sprints off, searches your knowledge, grabs the most relevant scraps, pastes them above the question, and only then does the model get to speak. But your documents don't go in whole. First they get shredded. A 100-page handbook becomes hundreds of little chunks, maybe 500 tokens each, because the whole thing was never going to fit inside one prompt. So, already, before anything smart happens, your knowledge is in pieces. Then every chunk gets turned a vector, a long list of numbers that captures roughly what it means. Similar ideas land as nearby points, unrelated ones drift apart. Your entire corpus becomes a cloud of dots floating in math space, and that cloud gets saved in a vector database. Now the query time magic. Your question becomes a vector, too, and the system grabs its nearest neighbors, the top five or so closest chunks. Those and only those get stuffed into the prompt. The model never saw your database. It only ever saw the handful of pieces that scored well. And when it fits, RAG is genuinely great. I don't want to undersell it. Point it at 10 million support tickets nobody will ever hand organize, and it finds the needle. Messy, gigantic, constantly changing piles of text, that is exactly where retrieval earns its keep. Here's the catch, though, and it matters. RAG retrieves chunks, not concepts. It rederives what your data means on every single query, from fragments with no memory between calls. Grab the wrong five paragraphs, and the model will answer confidently from the wrong context entirely. Now flip to OKF and watch how different the shape is. No database, no embedding model, no retriever. There's a folder. Google calls it a knowledge bundle, and that bundle is the whole unit. Just a directory of markdown files you could open in any editor on Earth. Inside, each file is one concept, one idea per document. Up top sits a small block of YAML, the metadata. Below it, plain markdown, the prose, the schema, the examples. A human might have written it, an agent might have. Either way, there's no decoding step. You just read it. And the spec is almost aggressively minimal, which I love. Of all that metadata, exactly one field is required, type. That is it. Title, description, tags, timestamps, all recommended, all optional. Google deliberately left the rest up to whoever's writing the bundle. Here's the part that actually stands in for retrieval. Every bundle can carry an index.md, a table of contents for the whole thing. So, the agent doesn't grope around in the dark. It reads the index, sees exactly what concepts exist, and walks straight to the one it needs. Navigation, not guessing. And that navigation is quietly efficient. Instead of dumping a dozen fuzzy chunks into the context and hoping, the agent pulls the two files that actually matter. Fewer tokens, less noise, and a much better shot at the model reading the thing you meant. The concepts also link to each other, like a wiki. The orders table points at the customers table, which points at the refunds runbook. Follow those links, and the whole bundle becomes a little knowledge graph. One an agent can walk hop by hop on its own. And it's alive. There's a reserved log.md that records changes over time. Append-only, like a little change log. So, the knowledge stays curated and versioned. And both people and agents can edit it in place, exactly the way you'd tidy up a shared handbook. Because it's just files, it travels anywhere. No SDK, no cloud account, no proprietary database holding it hostage. Google's own pitch was refreshingly blunt. What was missing is a format, not another service. Think USB-C. One connector every tool already speaks. Okay, put them side by side and the difference goes from scary to obvious. Same job, get the right knowledge in front of the model. Completely opposite strategy for getting it there. This is the one sentence to keep, lifted straight from the write-ups. RAG re-derives knowledge at query time from raw chunks. An OKF bundle stores curated, cross-linked concepts the agent reads directly. Re-derive versus read. Honestly, that is the entire ball game right there. And there's a second gap most people miss. RAG is read-only. Retrieval hands you some text and forgets you existed. But an agent can open an OKF concept and rewrite it. Fix a stale schema, add a note, commit the change. The knowledge base can actually improve itself over time. Both of them fight hallucination, but from different angles. RAG grounds the model in whatever it happened to retrieve. OKF grounds it in something a human already decided was correct and worth keeping. One is best effort search, the other is curated truth, which is exactly why the killed RAG take falls apart. They aren't rivals, they compose. You can take an OKF bundle and feed it straight into a RAG pipeline as clean, structured, already labeled source. The format doesn't replace the process, it makes the process better. So, when do you actually reach for RAG? When the pile is huge and nobody curated it. Years of PDFs, support tickets, wiki rot, chat logs, contracts, text at a scale no human will ever sit down and organize by hand. There, search is the only sane answer. And OKF, when the knowledge is worth the care. Your table schemas, what a metric actually means, the runbook for the 3:00 a.m. incident. The high-value stuff you need exactly right, not fuzzily retrieved and probably close enough. That deserves to be written down once, properly. Want to watch a clip? Follow an agent through a bundle. It reads the index, opens the orders concept, follows the join path over to customers, and answers, no vector search anywhere in sight. It just navigated a wiki the same way you would have. And this isn't only a spec on paper, Google shipped real tooling alongside it. There's an enrichment agent that walks a big query data set and draft OKF docs for every table and view. Schemas, citations, and join paths generated automatically, so you're not starting from a blank page. They also shipped a visualizer. Drop in a bundle and it renders the whole knowledge graph as a single, self-contained HTML file. No back end, nothing leaving the page. It's a small thing, but it tells you they want people actually reading these bundles, not just feeding them to robots. And the samples are data sets you might already recognize. The GA4 e-commerce set, the Stack Overflow data dump, the Bitcoin public data set, clone one from the repo, open it in your editor, and you're reading a real working OKF bundle inside about a minute. Now step back because there's a pattern here. lms.danext, agents.md, claude.md, and now OKF. A clear drift is underway. We are quietly learning to write plain structured files whose entire intended audience is a model, not a person. Now the honest part because I'm not here to sell you anything. This is version 0.1, a draft from a single vendor only weeks old. The spec itself is genuinely elegant, but whether the rest of the industry actually adopts it is the real open question. Bookmark it. Don't bet the whole company on it yet. So keep the mental model dead simple. Rag is the librarian. You ask a question and it sprints off to find the right passages. OKF is the handbook, already written, already organized, sitting right there on the shelf. You don't fire the librarian to write a handbook. In a good setup, you keep both. So here's your move this week. Look hard at what your agent keeps getting wrong. Is it drowning in a haystack of documents? That's a rag problem. Is it fumbling your own schemas and definitions over and over? Write a small bundle. And that four-word post, now you know exactly why it's wrong. One is a process, one is a format. Now you'll never confuse them again.

---

## Timestamped Segments

**[0:00]** Last week a post blew up on my feed.

**[0:02]** Four words, OKF just killed rag. It

**[0:05]** didn't. It couldn't. These two aren't

**[0:07]** even playing the same sport. So, one

**[0:10]** line, then we earn it. Rag is a process,

**[0:13]** OKF is a format. Comparing them is a

**[0:15]** category error.

**[0:17]** It's like asking whether NPM beats

**[0:18]** package.json. One is a tool that does

**[0:21]** something, the other just sits on disk.

**[0:23]** Fast catch-up. OKF is Google Cloud's

**[0:26]** Open Knowledge Format. It shipped in

**[0:28]** June, a spec on GitHub, markdown files

**[0:30]** in a folder.

**[0:32]** If you've ever written a claw.md to give

**[0:34]** your assistant context, you already get

**[0:36]** OKF. Same instinct standardized for a

**[0:39]** whole company. Rag you probably know,

**[0:42]** retrieval augmented generation. Before

**[0:44]** the model answers, you fetch relevant

**[0:46]** text and drop it into the prompt. And

**[0:48]** there's the trap. Both end the same way.

**[0:50]** Knowledge lands in the model's context.

**[0:53]** Same destination, different vehicle,

**[0:55]** which sounds like nitpicking until you

**[0:57]** pick the wrong one and spin up a vector

**[0:58]** database you never needed. So, here's

**[1:00]** the deal. By the end, you'll never mix

**[1:03]** these up again. What each one is, where

**[1:05]** each wins, and why you often want both.

**[1:08]** Start with the problem both of these are

**[1:09]** chasing. In any real company, the stuff

**[1:12]** a model needs is scattered everywhere. A

**[1:14]** table schema lives in one tool. What a

**[1:16]** metric actually means lives in someone's

**[1:18]** head. The incident runbook is buried in

**[1:21]** a wiki nobody opens. Fragmented

**[1:23]** knowledge, that's the enemy. Rag was the

**[1:25]** first big answer, so start there. It

**[1:27]** frames everything else. Picture the

**[1:29]** classic pipeline. A question comes in.

**[1:32]** A retriever sprints off, searches your

**[1:34]** knowledge, grabs the most relevant

**[1:36]** scraps, pastes them above the question,

**[1:38]** and only then does the model get to

**[1:39]** speak. But your documents don't go in

**[1:41]** whole. First they get shredded. A

**[1:44]** 100-page handbook becomes hundreds of

**[1:45]** little chunks, maybe 500 tokens each,

**[1:48]** because the whole thing was never going

**[1:50]** to fit inside one prompt. So, already,

**[1:52]** before anything smart happens, your

**[1:54]** knowledge is in pieces. Then every chunk

**[1:57]** gets turned a vector, a long list of

**[1:59]** numbers that captures roughly what it

**[2:00]** means. Similar ideas land as nearby

**[2:03]** points, unrelated ones drift apart. Your

**[2:05]** entire corpus becomes a cloud of dots

**[2:07]** floating in math space, and that cloud

**[2:09]** gets saved in a vector database. Now the

**[2:12]** query time magic. Your question becomes

**[2:14]** a vector, too, and the system grabs its

**[2:16]** nearest neighbors, the top five or so

**[2:18]** closest chunks. Those and only those get

**[2:21]** stuffed into the prompt. The model never

**[2:23]** saw your database. It only ever saw the

**[2:25]** handful of pieces that scored well.

**[2:27]** And when it fits, RAG is genuinely

**[2:29]** great. I don't want to undersell it.

**[2:32]** Point it at 10 million support tickets

**[2:33]** nobody will ever hand organize, and it

**[2:36]** finds the needle. Messy, gigantic,

**[2:38]** constantly changing piles of text, that

**[2:40]** is exactly where retrieval earns its

**[2:42]** keep. Here's the catch, though, and it

**[2:44]** matters. RAG retrieves chunks, not

**[2:46]** concepts. It rederives what your data

**[2:48]** means on every single query, from

**[2:50]** fragments with no memory between calls.

**[2:53]** Grab the wrong five paragraphs, and the

**[2:55]** model will answer confidently from the

**[2:57]** wrong context entirely.

**[2:59]** Now flip to OKF and watch how different

**[3:01]** the shape is. No database, no embedding

**[3:03]** model, no retriever. There's a folder.

**[3:06]** Google calls it a knowledge bundle, and

**[3:08]** that bundle is the whole unit. Just a

**[3:10]** directory of markdown files you could

**[3:12]** open in any editor on Earth. Inside,

**[3:14]** each file is one concept, one idea per

**[3:17]** document. Up top sits a small block of

**[3:19]** YAML, the metadata. Below it, plain

**[3:22]** markdown, the prose, the schema, the

**[3:24]** examples. A human might have written it,

**[3:26]** an agent might have. Either way, there's

**[3:29]** no decoding step. You just read it. And

**[3:31]** the spec is almost aggressively minimal,

**[3:33]** which I love. Of all that metadata,

**[3:35]** exactly one field is required, type.

**[3:38]** That is it. Title, description, tags,

**[3:41]** timestamps, all recommended, all

**[3:43]** optional. Google deliberately left the

**[3:45]** rest up to whoever's writing the bundle.

**[3:47]** Here's the part that actually stands in

**[3:49]** for retrieval. Every bundle can carry an

**[3:51]** index.md,

**[3:53]** a table of contents for the whole thing.

**[3:55]** So, the agent doesn't grope around in

**[3:57]** the dark. It reads the index, sees

**[3:59]** exactly what concepts exist, and walks

**[4:01]** straight to the one it needs.

**[4:03]** Navigation, not guessing. And that

**[4:05]** navigation is quietly efficient. Instead

**[4:07]** of dumping a dozen fuzzy chunks into the

**[4:09]** context and hoping, the agent pulls the

**[4:11]** two files that actually matter. Fewer

**[4:14]** tokens, less noise, and a much better

**[4:16]** shot at the model reading the thing you

**[4:18]** meant. The concepts also link to each

**[4:20]** other, like a wiki. The orders table

**[4:22]** points at the customers table, which

**[4:24]** points at the refunds runbook. Follow

**[4:26]** those links, and the whole bundle

**[4:28]** becomes a little knowledge graph. One an

**[4:30]** agent can walk hop by hop on its own.

**[4:33]** And it's alive.

**[4:34]** There's a reserved log.md that records

**[4:36]** changes over time. Append-only, like a

**[4:39]** little change log. So, the knowledge

**[4:41]** stays curated and versioned. And both

**[4:43]** people and agents can edit it in place,

**[4:45]** exactly the way you'd tidy up a shared

**[4:47]** handbook. Because it's just files, it

**[4:50]** travels anywhere. No SDK, no cloud

**[4:52]** account, no proprietary database holding

**[4:55]** it hostage. Google's own pitch was

**[4:57]** refreshingly blunt. What was missing is

**[4:59]** a format, not another service. Think

**[5:01]** USB-C. One connector every tool already

**[5:04]** speaks. Okay, put them side by side and

**[5:07]** the difference goes from scary to

**[5:08]** obvious. Same job, get the right

**[5:10]** knowledge in front of the model.

**[5:12]** Completely opposite strategy for getting

**[5:13]** it there. This is the one sentence to

**[5:15]** keep, lifted straight from the

**[5:17]** write-ups. RAG re-derives knowledge at

**[5:19]** query time from raw chunks. An OKF

**[5:22]** bundle stores curated, cross-linked

**[5:24]** concepts the agent reads directly.

**[5:26]** Re-derive versus read. Honestly, that is

**[5:29]** the entire ball game right there. And

**[5:31]** there's a second gap most people miss.

**[5:33]** RAG is read-only. Retrieval hands you

**[5:35]** some text and forgets you existed. But

**[5:38]** an agent can open an OKF concept and

**[5:40]** rewrite it. Fix a stale schema, add a

**[5:42]** note, commit the change. The knowledge

**[5:44]** base can actually improve itself over

**[5:46]** time. Both of them fight hallucination,

**[5:48]** but from different angles.

**[5:50]** RAG grounds the model in whatever it

**[5:51]** happened to retrieve. OKF grounds it in

**[5:54]** something a human already decided was

**[5:56]** correct and worth keeping. One is best

**[5:58]** effort search, the other is curated

**[6:00]** truth, which is exactly why the killed

**[6:02]** RAG take falls apart. They aren't

**[6:04]** rivals, they compose. You can take an

**[6:06]** OKF bundle and feed it straight into a

**[6:08]** RAG pipeline as clean, structured,

**[6:11]** already labeled source. The format

**[6:13]** doesn't replace the process, it makes

**[6:15]** the process better. So, when do you

**[6:17]** actually reach for RAG? When the pile is

**[6:19]** huge and nobody curated it. Years of

**[6:21]** PDFs, support tickets, wiki rot, chat

**[6:24]** logs, contracts, text at a scale no

**[6:27]** human will ever sit down and organize by

**[6:29]** hand. There, search is the only sane

**[6:31]** answer. And OKF, when the knowledge is

**[6:34]** worth the care. Your table schemas, what

**[6:36]** a metric actually means, the runbook for

**[6:38]** the 3:00 a.m.

**[6:40]** incident. The high-value stuff you need

**[6:42]** exactly right, not fuzzily retrieved and

**[6:44]** probably close enough. That deserves to

**[6:46]** be written down once, properly. Want to

**[6:48]** watch a clip? Follow an agent through a

**[6:50]** bundle.

**[6:51]** It reads the index, opens the orders

**[6:53]** concept, follows the join path over to

**[6:55]** customers, and answers, no vector search

**[6:58]** anywhere in sight. It just navigated a

**[7:00]** wiki the same way you would have. And

**[7:02]** this isn't only a spec on paper, Google

**[7:04]** shipped real tooling alongside it.

**[7:06]** There's an enrichment agent that walks a

**[7:08]** big query data set and draft OKF docs

**[7:11]** for every table and view. Schemas,

**[7:13]** citations, and join paths generated

**[7:15]** automatically, so you're not starting

**[7:17]** from a blank page. They also shipped a

**[7:19]** visualizer.

**[7:21]** Drop in a bundle and it renders the

**[7:22]** whole knowledge graph as a single,

**[7:24]** self-contained HTML file. No back end,

**[7:27]** nothing leaving the page. It's a small

**[7:29]** thing, but it tells you they want people

**[7:31]** actually reading these bundles, not just

**[7:33]** feeding them to robots. And the samples

**[7:35]** are data sets you might already

**[7:37]** recognize. The GA4 e-commerce set, the

**[7:40]** Stack Overflow data dump, the Bitcoin

**[7:42]** public data set, clone one from the

**[7:44]** repo, open it in your editor, and you're

**[7:46]** reading a real working OKF bundle inside

**[7:49]** about a minute. Now step back because

**[7:51]** there's a pattern here. lms.danext,

**[7:54]** agents.md,

**[7:56]** claude.md,

**[7:57]** and now OKF. A clear drift is underway.

**[8:00]** We are quietly learning to write plain

**[8:02]** structured files whose entire intended

**[8:04]** audience is a model, not a person. Now

**[8:07]** the honest part because I'm not here to

**[8:09]** sell you anything. This is version 0.1,

**[8:11]** a draft from a single vendor only weeks

**[8:14]** old. The spec itself is genuinely

**[8:16]** elegant, but whether the rest of the

**[8:17]** industry actually adopts it is the real

**[8:19]** open question. Bookmark it. Don't bet

**[8:22]** the whole company on it yet. So keep the

**[8:24]** mental model dead simple. Rag is the

**[8:26]** librarian. You ask a question and it

**[8:28]** sprints off to find the right passages.

**[8:30]** OKF is the handbook, already written,

**[8:33]** already organized, sitting right there

**[8:35]** on the shelf. You don't fire the

**[8:36]** librarian to write a handbook. In a good

**[8:39]** setup, you keep both. So here's your

**[8:41]** move this week. Look hard at what your

**[8:42]** agent keeps getting wrong. Is it

**[8:44]** drowning in a haystack of documents?

**[8:46]** That's a rag problem. Is it fumbling

**[8:48]** your own schemas and definitions over

**[8:50]** and over? Write a small bundle. And that

**[8:52]** four-word post, now you know exactly why

**[8:55]** it's wrong. One is a process, one is a

**[8:57]** format. Now you'll never confuse them

**[8:59]** again.
