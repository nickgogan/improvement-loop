# Transcript: Google's OKF: The Simple Folder Replacing Vector Databases

**URL:** https://www.youtube.com/watch?v=2kKkb01GxYQ
**Segments:** 151
**Channel:** Cloud Codes
**Duration:** 5:59
**Uploaded:** 2026-06-24

---

## Full Text

Google just did something that sounds almost like a joke. They took a plain folder, text files, nothing fancy, and turned it into an official AI standard. And that quiet little folder does something bold. It makes the expensive vector database you were told you needed optional. On one side, a pile of markdown files. On the other, a vector store with embeddings, indexes, and a monthly bill. Google is betting on the files. It is called OKF, the Open Knowledge Format. Google Cloud shipped version 0.1 in June, and it is beautifully boring. It is just markdown. Ask an agent how your team computes weekly active users, and instead of searching a database, it just opens a file, follows a link, and answers. That is the whole trick. Here is the thing models keep tripping on. It is not intelligence, it is context. A model can write the query, but only if it knows your tables, your metrics, your join paths. And that knowledge is scattered. It lives in metadata catalogs, in wikis, in shared drives, in code comments, and in a few senior engineers' heads. Every agent has to reassemble it from scratch. The standard fix was rag. Upload your documents, chop them into chunks, turn each chunk into a vector, and stash them in a vector database. At query time, you retrieve the closest matches. It works, but the model rediscovers everything on every single question. Nothing accumulates. Ask the same subtle thing twice, and it pieces the answer back together from fragments both times. Andre Carpathy framed the alternative back in April. He called it an LLM wiki, and his line was perfect. Obsidian is the IDE, the LLM is the programmer, and the wiki is the code base. Instead of retrieving raw chunks, the model builds a wiki and keeps it current. Drop in a new source, and it updates a dozen pages, summaries, entities, cross-links, flagging where new facts contradict the old. The knowledge compounds. Three layers make it work. Raw sources you never edit, a wiki the model owns entirely, and a schema file, your claw.md or agents.md, that teaches the model how to keep it all tidy. And honestly, you have seen this pattern everywhere. Obsidian Vault wired to coding agents, agents.md files, metadata as code repos. Great ideas, but every one of them was bespoke, so none of them talk to each other. That is the gap OKF fills. It does not add a runtime or an SDK, it just agrees on a few conventions, so a wiki one team writes, another team's agent can read with no translation. So, what is it exactly? An OKF bundle is a directory of markdown files. Each file is one concept, a table, a metric, a runbook, an API, and the file's path is its identity. Open one up, and it is nothing scary. A little block of YAML at the top, then plain markdown underneath for everything else. That is a concept. The front matter has a handful of reserved fields, type, title, description, tags, a timestamp, but only one of them is actually required, type. Everything else is up to you. Concepts link to each other with ordinary markdown links. And those links quietly turn a flat folder into a graph, one that is richer than any parent and child file tree. Two optional files round it out, an index, so an agent can start at the top and drill down, and a log, so every change keeps a history you can actually read. The design rests on three ideas, be minimally opinionated, keep producers and consumers independent, and stay a format, never a platform you have to log into. Because it is just files, there is nothing to install. It renders on GitHub. It ships as a tarball. It mounts on any file system. Your knowledge stops being trapped inside someone's product. So, how is this different from rag? Rag re-derives knowledge from raw chunks on every query. OKF stores curated, cross-linked concepts that the agent reads and edits directly. Chunks versus concepts. Line it up against the usual suspects. Notion locks you into a database. A vector index gives you fuzzy chunks, not concepts. OKF is portable markdown an agent reads with zero translation and the bill changes. A vector database means hosting, embedding, re-embedding on every edit, and babysitting drift. A folder means get and grep, diffs, pull requests, and basically zero infrastructure. And Google did not just publish a spec. They shipped a BigQuery agent that writes bundles, a static visualizer to browse them, and three sample bundles to copy from. The killer use case is metadata as code. Export your BigQuery tables and metric definitions as a bundle, commit it right next to the SQL, and review every change as a pull request. From there it spreads. On-call agents that read runbooks and follow the links. Vendors shipping a catalog your agent just consumes. A team wiki that finally stays current because the model maintains it. Now the honest part. This is not the death of the vector database. For a huge, messy pile of documents you cannot fit in context, semantic search still wins. OKF shines when the knowledge is curated. So, a folder beats the database when your knowledge is curated, when you need accuracy and version history, when it fits in the agent's context, and when portability actually matters. Step back and the shift is bigger than one format. Context is becoming a portable, version-controlled artifact. Open formats won the data era and they are lining up to win the agent era, too. So, that is OKF, a folder of markdown concepts linked into a graph that an agent reads and keeps current. No embeddings required. Sometimes the boring answer really is the better one. If that clicked, you will like the rest of the channel. Subscribe to Cloud Code, and I will see you in the next one.

---

## Timestamped Segments

**[0:00]** Google just did something that sounds

**[0:01]** almost like a joke. They took a plain

**[0:03]** folder, text files, nothing fancy, and

**[0:06]** turned it into an official AI standard.

**[0:09]** And that quiet little folder does

**[0:10]** something bold. It makes the expensive

**[0:12]** vector database you were told you needed

**[0:15]** optional. On one side, a pile of

**[0:17]** markdown files. On the other, a vector

**[0:20]** store with embeddings, indexes, and a

**[0:22]** monthly bill.

**[0:24]** Google is betting on the files. It is

**[0:26]** called OKF, the Open Knowledge Format.

**[0:29]** Google Cloud shipped version 0.1 in

**[0:32]** June, and it is beautifully boring. It

**[0:34]** is just markdown. Ask an agent how your

**[0:37]** team computes weekly active users, and

**[0:39]** instead of searching a database, it just

**[0:41]** opens a file, follows a link, and

**[0:44]** answers. That is the whole trick. Here

**[0:46]** is the thing models keep tripping on. It

**[0:48]** is not intelligence, it is context. A

**[0:51]** model can write the query, but only if

**[0:53]** it knows your tables, your metrics, your

**[0:56]** join paths. And that knowledge is

**[0:57]** scattered. It lives in metadata

**[0:59]** catalogs, in wikis, in shared drives, in

**[1:02]** code comments, and in a few senior

**[1:04]** engineers' heads. Every agent has to

**[1:07]** reassemble it from scratch.

**[1:09]** The standard fix was rag. Upload your

**[1:11]** documents, chop them into chunks, turn

**[1:14]** each chunk into a vector, and stash them

**[1:16]** in a vector database. At query time, you

**[1:18]** retrieve the closest matches. It works,

**[1:21]** but the model rediscovers everything on

**[1:23]** every single question. Nothing

**[1:25]** accumulates. Ask the same subtle thing

**[1:28]** twice, and it pieces the answer back

**[1:30]** together from fragments both times.

**[1:32]** Andre Carpathy framed the alternative

**[1:34]** back in April. He called it an LLM wiki,

**[1:37]** and his line was perfect. Obsidian is

**[1:40]** the IDE, the LLM is the programmer, and

**[1:43]** the wiki is the code base. Instead of

**[1:45]** retrieving raw chunks, the model builds

**[1:47]** a wiki and keeps it current. Drop in a

**[1:50]** new source, and it updates a dozen

**[1:51]** pages, summaries, entities, cross-links,

**[1:55]** flagging where new facts contradict the

**[1:57]** old. The knowledge compounds. Three

**[1:59]** layers make it work. Raw sources you

**[2:01]** never edit, a wiki the model owns

**[2:04]** entirely, and a schema file, your

**[2:06]** claw.md or agents.md, that teaches the

**[2:10]** model how to keep it all tidy. And

**[2:12]** honestly, you have seen this pattern

**[2:14]** everywhere. Obsidian Vault wired to

**[2:16]** coding agents, agents.md files, metadata

**[2:20]** as code repos. Great ideas, but every

**[2:23]** one of them was bespoke, so none of them

**[2:25]** talk to each other. That is the gap OKF

**[2:27]** fills. It does not add a runtime or an

**[2:29]** SDK, it just agrees on a few

**[2:32]** conventions, so a wiki one team writes,

**[2:34]** another team's agent can read with no

**[2:36]** translation. So, what is it exactly?

**[2:40]** An OKF bundle is a directory of markdown

**[2:42]** files. Each file is one concept, a

**[2:45]** table, a metric, a runbook, an API, and

**[2:49]** the file's path is its identity. Open

**[2:51]** one up, and it is nothing scary. A

**[2:53]** little block of YAML at the top, then

**[2:55]** plain markdown underneath for everything

**[2:58]** else. That is a concept. The front

**[3:01]** matter has a handful of reserved fields,

**[3:03]** type, title, description, tags, a

**[3:06]** timestamp, but only one of them is

**[3:08]** actually required, type. Everything else

**[3:11]** is up to you. Concepts link to each

**[3:13]** other with ordinary markdown links. And

**[3:15]** those links quietly turn a flat folder

**[3:18]** into a graph, one that is richer than

**[3:20]** any parent and child file tree. Two

**[3:22]** optional files round it out, an index,

**[3:25]** so an agent can start at the top and

**[3:27]** drill down, and a log, so every change

**[3:30]** keeps a history you can actually read.

**[3:32]** The design rests on three ideas, be

**[3:34]** minimally opinionated, keep producers

**[3:37]** and consumers independent, and stay a

**[3:39]** format, never a platform you have to log

**[3:41]** into. Because it is just files, there is

**[3:44]** nothing to install. It renders on

**[3:46]** GitHub. It ships as a tarball. It mounts

**[3:48]** on any file system. Your knowledge stops

**[3:51]** being trapped inside someone's product.

**[3:53]** So, how is this different from rag? Rag

**[3:56]** re-derives knowledge from raw chunks on

**[3:58]** every query. OKF stores curated,

**[4:01]** cross-linked concepts that the agent

**[4:03]** reads and edits directly. Chunks versus

**[4:06]** concepts. Line it up against the usual

**[4:09]** suspects. Notion locks you into a

**[4:11]** database. A vector index gives you fuzzy

**[4:13]** chunks, not concepts. OKF is portable

**[4:17]** markdown an agent reads with zero

**[4:19]** translation and the bill changes. A

**[4:22]** vector database means hosting,

**[4:24]** embedding, re-embedding on every edit,

**[4:26]** and babysitting drift. A folder means

**[4:29]** get and grep, diffs, pull requests, and

**[4:31]** basically zero infrastructure. And

**[4:34]** Google did not just publish a spec. They

**[4:36]** shipped a BigQuery agent that writes

**[4:38]** bundles, a static visualizer to browse

**[4:41]** them, and three sample bundles to copy

**[4:43]** from. The killer use case is metadata as

**[4:46]** code. Export your BigQuery tables and

**[4:49]** metric definitions as a bundle, commit

**[4:51]** it right next to the SQL, and review

**[4:53]** every change as a pull request. From

**[4:55]** there it spreads. On-call agents that

**[4:57]** read runbooks and follow the links.

**[4:59]** Vendors shipping a catalog your agent

**[5:01]** just consumes. A team wiki that finally

**[5:04]** stays current because the model

**[5:05]** maintains it.

**[5:07]** Now the honest part. This is not the

**[5:09]** death of the vector database. For a

**[5:11]** huge, messy pile of documents you cannot

**[5:13]** fit in context, semantic search still

**[5:16]** wins. OKF shines when the knowledge is

**[5:18]** curated. So, a folder beats the database

**[5:21]** when your knowledge is curated, when you

**[5:23]** need accuracy and version history, when

**[5:25]** it fits in the agent's context, and when

**[5:27]** portability actually matters. Step back

**[5:30]** and the shift is bigger than one format.

**[5:33]** Context is becoming a portable,

**[5:35]** version-controlled artifact. Open

**[5:37]** formats won the data era and they are

**[5:39]** lining up to win the agent era, too. So,

**[5:41]** that is OKF, a folder of markdown

**[5:44]** concepts linked into a graph that an

**[5:47]** agent reads and keeps current. No

**[5:49]** embeddings required. Sometimes the

**[5:51]** boring answer really is the better one.

**[5:53]** If that clicked, you will like the rest

**[5:55]** of the channel. Subscribe to Cloud Code,

**[5:57]** and I will see you in the next one.
