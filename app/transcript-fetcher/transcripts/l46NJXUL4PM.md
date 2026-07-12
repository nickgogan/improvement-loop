# Transcript: Google OKF + Claude : Why We Stopped Using RAG

**URL:** https://www.youtube.com/watch?v=l46NJXUL4PM
**Segments:** 274
**Channel:** Cloud Codes
**Duration:** 9:45
**Uploaded:** 2026-07-04

---

## Full Text

Watch what happens when you give a brilliant AI agent a real task, then close the window and come back tomorrow. It is gone. Every decision, every preference, every hard-won detail wiped. The smartest coder on Earth waking up with amnesia every single morning. So, for years we patched around it the same way everyone did, a vector database. Chop your knowledge into little chunks, turn each chunk into a long list of numbers, and pile them all into a special store you can search by fuzzy similarity. For a long time, that was simply how you gave an agent a memory. And when the agent needs something, it does not read your files, it guesses. It grabs the chunks that look mathematically close to the question, hands back the top few, and hopes the answer is in there somewhere. Sometimes it is. Often it is only half of it. Here's the twist. Claude Code tried exactly this, a local vector database baked right in, and then ripped it out. Plain old search, grep across real files, beat it. No embeddings, no index, just the agent reading what is actually there. Because the best memory an agent can have is not a database at all. It is a file. A plain markdown file the agent reads at the start of every session and writes back to at the end. Memory you can open, read, and fix yourself. And in June, Google made it official. They published the Open Knowledge Format, OKF, a standard that says an agent's memory should be exactly this, a folder of markdown files, no database, no runtime, just files. Every piece of knowledge becomes one file. At the top, a tiny block of structured tags, what type of thing this is, a title, a timestamp. Below it, the actual knowledge in plain markdown. That is the entire format. Then the files link to each other, exactly like a wiki. One concept points to the next with an ordinary markdown link, and the whole folder quietly becomes a graph, a live map of how everything your agent knows connects together. And the agent maintains it itself. It reads the files, adds new ones, updates the old, and links them. The bookkeeping a human would abandon in a week. As Karpathy put it, models do not get bored, and they can touch 15 files in one pass. So, here's the plan for the next 10 minutes. Why agent memory has been quietly broken, how OK F fixes it with nothing but files, and how to wire it into Claude Code today. Plus, the honest truth about what it still cannot do. Let us start with the wound. A language model has no memory of its own. Every request is a blank slate. It only knows what is inside the context window right now. Close the session, and that context is gone for good. The model did not learn anything. It just borrowed your words for a moment. The industry's answer was retrieval. Take all your documents, slice them into little chunks, and run each chunk through an embedding model that turns text into a long list of numbers, a single point in a few thousand dimensions. Store every point in a vector database. Every time a document changes, you re-embed it and rebuild the index. That is rag. And for a while, it was the only game in town. But, look closely at what retrieval actually does. When you ask a question, it embeds your question, too. Then, find the stored chunks whose numbers sit closest to it. Closest is not the same as correct. The one paragraph you needed might be split across two chunks, or drowned out by a chunk that merely shares some words, and the database hands you the wrong neighbors with total confidence. You never see why. You just get a slightly wrong answer, and you cannot see any of it. A vector is not readable. You cannot open one, diff it, or fix a wrong fact by hand. You are running a whole extra service, re-embedding on every edit, paying to store and search millions of numbers just so your agent can approximate what a folder of files would have told it exactly. Which is why Claude Code went the other way. Early on, it shipped with a local vector store for your code base, and the team pulled it out. Boris Cherny, who led Claude Code, said it plainly. Agentic search, letting the model grep, list, and open real files on its own turned out simpler, and cheaper, and more accurate than any embedding index. Think about why. If you want every place a function is called, grep gives you all of them exactly in milliseconds. Cosine similarity gives you the 10 that merely felt close. For precise facts, exact search wins, and the agent already knows how to drive it. So, Claude code's memory is just files you already own. A Claude.md that holds your standing instructions loaded at the top of every session. A memory.md that grows as the agent learns your project. You can read them, you can edit them, and soak in it. And because it is all files, your agent's memory lives in Git. Every change to what it knows becomes a diff you can review line by line. You can see the exact moment it learned something, roll back a bad fact with a single revert, and approve new knowledge in a pull request. Try doing any of that with a blob of floating-point numbers, memory you can actually read, audit, and trust. That is the idea Google set out to standardize. Open knowledge format version 0.1 published by the Google Cloud data team in June 2026. The whole pitch fits on one screen. It is just markdown, just files, just a little YAML on top. If you can read a file, you can read it. If you can clone a repo, you can ship it. The repo crossed 6,000 stars in weeks. A collection of this knowledge is called a bundle, nothing more than a directory tree. Concepts group into folders however you like. Datasets here, tables there, playbooks and metrics beside them. The file's path is its identity. Move it and it is renamed. That is the whole database. Open one concept and you see the two halves. Up top, YAML front matter, the structured card. Exactly one field is required, type, telling the agent what kind of thing this is. Everything under it is free-form markdown, schemas, steps, examples, whatever the knowledge actually needs. The rest of the front matter is optional but recommended, a title, a one-line description, a link to the real resource it describes, tags, and a timestamp. Small, queryable fields an agent can scan without reading a single body. Think of it as the index card in front of the essay. The real magic is the links. A concept references another with a plain markdown link, and those links turn a flat folder into a graph. The orders table points to the customers table, a playbook points to the alert it fixes, a metric points to the query behind it. Follow the edges, and you are literally walking the agent's knowledge, the same shape you would draw on a whiteboard, except the agent can read it. To keep the agent from swallowing everything at once, each folder can carry an index, a short menu of what lives inside. The agent reads the menu, decides what it actually needs, and opens only that. Progressive disclosure, instead of dumping the entire brain into the context window. And every corner of the bundle can keep a log, a dated history of what changed and when. New table added here, playbook deprecated there. Your agent's memory does not just hold facts, it remembers how those facts got there, in plain, readable, chronological order. Three rules hold the whole thing together. Minimally opinionated, the only requirement is that one type field. Producer and consumer are independent. A human can write what an agent reads, and it is a format, not a platform. No account, no SDK, no owner. That is exactly why anyone can speak it. Now, put the two together. You point Claude code at an OKF bundle, a knowledge folder sitting right inside your repo, and mention it in claude.md. From that moment on, the folder is the agent's long-term memory, portable, versioned, and completely under your control. When a task arrives, the agent does not load the whole thing. It opens the top-level index, follows the one link that matters, reads that single concept, and gets to work. You could have 10,000 files of knowledge, and the agent only ever touches the handful it needs. No embeddings, no retrieval step, no context blown on things it will never use. And when it learns something new, it writes a fresh file, links it in, and appends a line to the log. Here's the best part. Because OKF is a standard, that brain travels. Hand the same folder to a different agent, Gemini, a homegrown tool, anything, and it reads the exact same memory. Now the honest part, because this is not a miracle, OKF is version 0.1, a draft barely a month old. The spec is deliberately tiny, the tooling is early, and the conventions will shift. Treat it as a foundation to build on, not a finished product to bet your company on tomorrow. And a format cannot save bad content. OKF standardizes where knowledge lives, not whether it is any good. Dump messy notes into markdown, and your agent gets messy memory. Someone still has to curate the brain, the format just makes that work portable, reviewable, and shared. And no, this does not kill vector search. For a giant pile of unstructured text, millions of documents, fuzzy semantic questions where you do not even know the exact words, embeddings still shine, and often the two work side by side. What changed is the default. Files and search are now the first choice for agent memory, and the vector database is the special case you reach for on purpose. So, three things to carry out of here. Agents forget by default. Memory is something you deliberately give them. The best memory is not a database, it is a folder of readable files, and OKF is the standard that finally makes that folder portable across every agent you touch. Perfect memory for your AI was never going to be a bigger vector database. It was here the whole time. Plain files, in plain sight, that you and your agent can both read, edit, and version. Claude code proved it in practice. Google just wrote it down as a standard. The brain your agent has been missing is a folder you already know how to use. If this rewired how you think about agent memory, subscribe. This is where we make the future of building make sense. I'm Cloud Code, now go give your agent a brain worth keeping.

---

## Timestamped Segments

**[0:00]** Watch what happens when you give a

**[0:01]** brilliant AI agent a real task, then

**[0:03]** close the window and come back tomorrow.

**[0:06]** It is gone. Every decision, every

**[0:08]** preference, every hard-won detail wiped.

**[0:11]** The smartest coder on Earth waking up

**[0:13]** with amnesia every single morning.

**[0:15]** So, for years we patched around it the

**[0:17]** same way everyone did, a vector

**[0:19]** database. Chop your knowledge into

**[0:21]** little chunks, turn each chunk into a

**[0:23]** long list of numbers, and pile them all

**[0:25]** into a special store you can search by

**[0:27]** fuzzy similarity.

**[0:28]** For a long time, that was simply how you

**[0:30]** gave an agent a memory. And when the

**[0:32]** agent needs something, it does not read

**[0:34]** your files, it guesses. It grabs the

**[0:37]** chunks that look mathematically close to

**[0:38]** the question, hands back the top few,

**[0:41]** and hopes the answer is in there

**[0:42]** somewhere. Sometimes it is. Often it is

**[0:45]** only half of it. Here's the twist.

**[0:47]** Claude Code tried exactly this, a local

**[0:50]** vector database baked right in, and then

**[0:52]** ripped it out. Plain old search, grep

**[0:54]** across real files, beat it. No

**[0:57]** embeddings, no index, just the agent

**[0:59]** reading what is actually there. Because

**[1:01]** the best memory an agent can have is not

**[1:03]** a database at all. It is a file. A plain

**[1:06]** markdown file the agent reads at the

**[1:08]** start of every session and writes back

**[1:10]** to at the end. Memory you can open,

**[1:12]** read, and fix yourself. And in June,

**[1:14]** Google made it official. They published

**[1:16]** the Open Knowledge Format, OKF, a

**[1:19]** standard that says an agent's memory

**[1:20]** should be exactly this, a folder of

**[1:22]** markdown files, no database, no runtime,

**[1:26]** just files. Every piece of knowledge

**[1:27]** becomes one file. At the top, a tiny

**[1:30]** block of structured tags, what type of

**[1:32]** thing this is, a title, a timestamp.

**[1:35]** Below it, the actual knowledge in plain

**[1:37]** markdown. That is the entire format.

**[1:39]** Then the files link to each other,

**[1:41]** exactly like a wiki. One concept points

**[1:43]** to the next with an ordinary markdown

**[1:45]** link, and the whole folder quietly

**[1:47]** becomes a graph, a live map of how

**[1:49]** everything your agent knows connects

**[1:51]** together. And the agent maintains it

**[1:53]** itself. It reads the files, adds new

**[1:55]** ones, updates the old, and links them.

**[1:58]** The bookkeeping a human would abandon in

**[2:00]** a week. As Karpathy put it, models do

**[2:03]** not get bored, and they can touch 15

**[2:05]** files in one pass.

**[2:06]** So, here's the plan for the next 10

**[2:08]** minutes. Why agent memory has been

**[2:10]** quietly broken, how OK F fixes it with

**[2:13]** nothing but files, and how to wire it

**[2:15]** into Claude Code today. Plus, the honest

**[2:17]** truth about what it still cannot do.

**[2:19]** Let us start with the wound. A language

**[2:21]** model has no memory of its own. Every

**[2:23]** request is a blank slate. It only knows

**[2:26]** what is inside the context window right

**[2:27]** now. Close the session, and that context

**[2:30]** is gone for good. The model did not

**[2:32]** learn anything. It just borrowed your

**[2:33]** words for a moment. The industry's

**[2:35]** answer was retrieval.

**[2:37]** Take all your documents, slice them into

**[2:39]** little chunks, and run each chunk

**[2:41]** through an embedding model that turns

**[2:43]** text into a long list of numbers, a

**[2:45]** single point in a few thousand

**[2:46]** dimensions. Store every point in a

**[2:48]** vector database. Every time a document

**[2:51]** changes, you re-embed it and rebuild the

**[2:53]** index. That is rag. And for a while, it

**[2:56]** was the only game in town. But, look

**[2:57]** closely at what retrieval actually does.

**[3:00]** When you ask a question, it embeds your

**[3:02]** question, too. Then, find the stored

**[3:04]** chunks whose numbers sit closest to it.

**[3:06]** Closest is not the same as correct. The

**[3:08]** one paragraph you needed might be split

**[3:10]** across two chunks, or drowned out by a

**[3:12]** chunk that merely shares some words, and

**[3:14]** the database hands you the wrong

**[3:15]** neighbors with total confidence. You

**[3:17]** never see why. You just get a slightly

**[3:19]** wrong answer, and you cannot see any of

**[3:22]** it. A vector is not readable. You cannot

**[3:24]** open one, diff it, or fix a wrong fact

**[3:27]** by hand. You are running a whole extra

**[3:29]** service, re-embedding on every edit,

**[3:31]** paying to store and search millions of

**[3:33]** numbers just so your agent can

**[3:35]** approximate what a folder of files would

**[3:37]** have told it exactly. Which is why

**[3:39]** Claude Code went the other way. Early

**[3:41]** on, it shipped with a local vector store

**[3:43]** for your code base, and the team pulled

**[3:44]** it out. Boris Cherny, who led Claude

**[3:47]** Code, said it plainly. Agentic search,

**[3:50]** letting the model grep, list, and open

**[3:52]** real files on its own turned out

**[3:54]** simpler, and cheaper, and more accurate

**[3:56]** than any embedding index. Think about

**[3:58]** why.

**[3:59]** If you want every place a function is

**[4:00]** called, grep gives you all of them

**[4:02]** exactly in milliseconds. Cosine

**[4:04]** similarity gives you the 10 that merely

**[4:06]** felt close. For precise facts, exact

**[4:09]** search wins, and the agent already knows

**[4:11]** how to drive it. So, Claude code's

**[4:13]** memory is just files you already own. A

**[4:15]** Claude.md that holds your standing

**[4:17]** instructions loaded at the top of every

**[4:19]** session. A memory.md that grows as the

**[4:22]** agent learns your project. You can read

**[4:24]** them, you can edit them, and soak in it.

**[4:26]** And because it is all files, your

**[4:28]** agent's memory lives in Git. Every

**[4:30]** change to what it knows becomes a diff

**[4:32]** you can review line by line. You can see

**[4:34]** the exact moment it learned something,

**[4:36]** roll back a bad fact with a single

**[4:38]** revert, and approve new knowledge in a

**[4:40]** pull request. Try doing any of that with

**[4:42]** a blob of floating-point numbers, memory

**[4:44]** you can actually read, audit, and trust.

**[4:47]** That is the idea Google set out to

**[4:49]** standardize. Open knowledge format

**[4:51]** version 0.1 published by the Google

**[4:54]** Cloud data team in June 2026. The whole

**[4:57]** pitch fits on one screen. It is just

**[4:59]** markdown, just files, just a little YAML

**[5:02]** on top. If you can read a file, you can

**[5:04]** read it. If you can clone a repo, you

**[5:06]** can ship it. The repo crossed 6,000

**[5:08]** stars in weeks. A collection of this

**[5:10]** knowledge is called a bundle, nothing

**[5:12]** more than a directory tree. Concepts

**[5:15]** group into folders however you like.

**[5:17]** Datasets here, tables there, playbooks

**[5:19]** and metrics beside them. The file's path

**[5:22]** is its identity. Move it and it is

**[5:24]** renamed. That is the whole database.

**[5:26]** Open one concept and you see the two

**[5:28]** halves. Up top, YAML front matter, the

**[5:31]** structured card. Exactly one field is

**[5:33]** required, type, telling the agent what

**[5:35]** kind of thing this is. Everything under

**[5:37]** it is free-form markdown, schemas,

**[5:40]** steps, examples, whatever the knowledge

**[5:42]** actually needs.

**[5:43]** The rest of the front matter is optional

**[5:45]** but recommended, a title, a one-line

**[5:48]** description, a link to the real resource

**[5:50]** it describes, tags, and a timestamp.

**[5:53]** Small, queryable fields an agent can

**[5:54]** scan without reading a single body.

**[5:57]** Think of it as the index card in front

**[5:58]** of the essay.

**[6:00]** The real magic is the links. A concept

**[6:02]** references another with a plain markdown

**[6:04]** link, and those links turn a flat folder

**[6:06]** into a graph. The orders table points to

**[6:08]** the customers table, a playbook points

**[6:10]** to the alert it fixes, a metric points

**[6:13]** to the query behind it. Follow the

**[6:14]** edges, and you are literally walking the

**[6:16]** agent's knowledge, the same shape you

**[6:18]** would draw on a whiteboard, except the

**[6:20]** agent can read it. To keep the agent

**[6:22]** from swallowing everything at once, each

**[6:24]** folder can carry an index, a short menu

**[6:27]** of what lives inside. The agent reads

**[6:29]** the menu, decides what it actually

**[6:31]** needs, and opens only that. Progressive

**[6:33]** disclosure, instead of dumping the

**[6:35]** entire brain into the context window.

**[6:37]** And every corner of the bundle can keep

**[6:39]** a log, a dated history of what changed

**[6:42]** and when. New table added here, playbook

**[6:44]** deprecated there.

**[6:46]** Your agent's memory does not just hold

**[6:48]** facts, it remembers how those facts got

**[6:50]** there, in plain, readable, chronological

**[6:52]** order. Three rules hold the whole thing

**[6:54]** together. Minimally opinionated, the

**[6:57]** only requirement is that one type field.

**[7:00]** Producer and consumer are independent. A

**[7:02]** human can write what an agent reads, and

**[7:04]** it is a format, not a platform. No

**[7:06]** account, no SDK, no owner. That is

**[7:09]** exactly why anyone can speak it. Now,

**[7:12]** put the two together. You point Claude

**[7:14]** code at an OKF bundle, a knowledge

**[7:16]** folder sitting right inside your repo,

**[7:18]** and mention it in claude.md.

**[7:21]** From that moment on, the folder is the

**[7:23]** agent's long-term memory, portable,

**[7:25]** versioned, and completely under your

**[7:27]** control. When a task arrives, the agent

**[7:30]** does not load the whole thing. It opens

**[7:32]** the top-level index, follows the one

**[7:34]** link that matters, reads that single

**[7:36]** concept, and gets to work. You could

**[7:38]** have 10,000 files of knowledge, and the

**[7:41]** agent only ever touches the handful it

**[7:42]** needs. No embeddings, no retrieval step,

**[7:46]** no context blown on things it will never

**[7:48]** use. And when it learns something new,

**[7:50]** it writes a fresh file, links it in, and

**[7:52]** appends a line to the log. Here's the

**[7:54]** best part. Because OKF is a standard,

**[7:57]** that brain travels. Hand the same folder

**[7:59]** to a different agent, Gemini, a

**[8:01]** homegrown tool, anything, and it reads

**[8:04]** the exact same memory. Now the honest

**[8:06]** part, because this is not a miracle, OKF

**[8:09]** is version 0.1, a draft barely a month

**[8:12]** old. The spec is deliberately tiny, the

**[8:14]** tooling is early, and the conventions

**[8:16]** will shift. Treat it as a foundation to

**[8:18]** build on, not a finished product to bet

**[8:21]** your company on tomorrow. And a format

**[8:23]** cannot save bad content. OKF

**[8:25]** standardizes where knowledge lives, not

**[8:27]** whether it is any good. Dump messy notes

**[8:30]** into markdown, and your agent gets messy

**[8:31]** memory. Someone still has to curate the

**[8:34]** brain, the format just makes that work

**[8:36]** portable, reviewable, and shared. And

**[8:38]** no, this does not kill vector search.

**[8:41]** For a giant pile of unstructured text,

**[8:43]** millions of documents, fuzzy semantic

**[8:45]** questions where you do not even know the

**[8:47]** exact words, embeddings still shine, and

**[8:50]** often the two work side by side.

**[8:52]** What changed is the default. Files and

**[8:54]** search are now the first choice for

**[8:56]** agent memory, and the vector database is

**[8:58]** the special case you reach for on

**[9:00]** purpose. So, three things to carry out

**[9:02]** of here. Agents forget by default.

**[9:04]** Memory is something you deliberately

**[9:06]** give them.

**[9:07]** The best memory is not a database, it is

**[9:09]** a folder of readable files, and OKF is

**[9:12]** the standard that finally makes that

**[9:13]** folder portable across every agent you

**[9:15]** touch. Perfect memory for your AI was

**[9:18]** never going to be a bigger vector

**[9:19]** database. It was here the whole time.

**[9:22]** Plain files, in plain sight, that you

**[9:24]** and your agent can both read, edit, and

**[9:26]** version. Claude code proved it in

**[9:28]** practice. Google just wrote it down as a

**[9:30]** standard. The brain your agent has been

**[9:32]** missing is a folder you already know how

**[9:34]** to use.

**[9:35]** If this rewired how you think about

**[9:36]** agent memory, subscribe. This is where

**[9:39]** we make the future of building make

**[9:40]** sense. I'm Cloud Code, now go give your

**[9:43]** agent a brain worth keeping.
