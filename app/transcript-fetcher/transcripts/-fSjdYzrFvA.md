# Transcript: Give Your AI Agent a Second Brain (Gbrain + Hermes Agent)

**URL:** https://www.youtube.com/watch?v=-fSjdYzrFvA
**Segments:** 453
**Channel:** Tonbi's AI Garage
**Duration:** 15:20
**Uploaded:** 2026-07-07

---

## Full Text

So, one of the tools I get asked about a lot with Hermes Agent is Gbrain. And Gbrain is this open source repo by Garry Tan, the president of Y Combinator. But, it's been out quite a while. It's very popular. You see over 25,000 stars. And it's used most often with open claw or Hermes Agent as a second brain. So, finally getting around to actually test So, in this video I'm going to kind of describe what it is, how it's different from like Hermes memory or an LM Wiki, and then we're going to install it, and then test it out with our Hermes Agent. Let's get started. And if you like this video, please consider following me on X at tombi.studio. I'll often be posting short videos on the latest AI news and agent features, as well as more in-depth written post and articles. Also, sign up for my free weekly newsletter, which I write by hand and release every Friday. Here, you'll see my honest thoughts about the latest AI news, models, research, and give a sneak peek of new projects I'm working on before they're announced anywhere else. Sign up on onchainaigarage.com. Link is in the description. Okay, so to start off, what is Gbrain and how do we use it? So, take this example, right? You're in Hermes chat. You ask, "What did we decide about the Acme pilot?" Hermes will do a normal session session search for Acme pilot has zero matches. So, it takes the full text of every past conversation and still can't find any reference to this because we never discussed it in Hermes itself. It actually lives in meeting notes that Hermes had never seen. So, Hermes can really only search a memory if you actually talked about a certain topic with it. And that's a boundary, and it's architectural. It's not really a bug. Every layer of Hermes memory, the curated files, the session index, even external providers, they all remember what passed through the agent. The world outside of the chat is invisible to it. So, G brain intends to fix this. Under the hood in G brain, you have a knowledge that lives in markdown files in a Git repo. So, that's the system of record. G brain syncs it to your local Postgres PG light running in process, no server, and no docker. On top of that, you have a hybrid search here. Uh vector plus keyword plus knowledge graph that wires itself. And the whole thing exposes 30 plus tools over MCP. Which is that is which is exactly the door Hermes knows how to walk through. So, it's MIT license. Um like I said, 25,000 stars plus. And it's being actively developed. A very popular uh tool in this ecosystem. So, what are really the the differences between these three things? Hermes memory, an LM wiki or knowledge base, and then G brain. And these are just kind of general explanations. Um I know some some may vary a little bit. So, Hermes memory has a layer system. Uh memory MD and user MD, which are curated and always loaded. Session search, which is FDS 5 over every past conversation. And then there's a lot of pluggable providers. Honcho memory, super memory, many others. And what this whole system is built to do is to remember a collaboration with the agent. What was said, what was decided and inferred inside of the agent. And in the middle here, you can see LM wiki, which if you've watched my videos, you've heard me talk about this concept a lot. And you've seen me build agent wikis, which is built around this concept. Um and these are just curated knowledge bases like the Hermes knowledge base you'll see there. Um so, it's a domain reference. You have concepts, entities, how things work. You know, it's compiled by a pipeline with human gates and published for any agent to read. It can answer questions about that domain. For example, my Hermes knowledge base, you can ask it, you know, how does Hermes memory work? And it will give you an updated and accurate answer. And it's a very useful tool. You can tell I used LM wikis on both Hermes and Gbrain to research this video. But it is specific to one domain. So Gbrain is a little bit different. Cuz it's basically a knowledge base for your world. Typed pages, people, companies, meetings, decisions at whatever scare scale at whatever scale with a graph and cited synthesis. And critically, it ingests things that never touched your chat. So notes folder, Obsidian vaults, meeting write-ups, captures. It's the difference between what the agent picked up along the way and what you deliberately decide to keep. So simply put, memory remembers our conversations, the LM wikis know domains, Gbrain knows our world. So here's the architecture and it's fairly simple. If you're working in Hermes agent or whatever agent harness you're using, you can use a MCP or STTIO subprocess to spawn Gbrain serve. And that's a local MCP subprocess. There's no HTTP server, no tunnel, no token or anything like that. Gbrain reads and writes a PG light database and the database is synced from plain markdown repo under Git. So every layer is inspectable here. The markdown is yours. The database is a local file. The MCP server is just a subprocess that dies with the session. Okay, so let's install it. So you can see in the repo itself, it has instructions for how you want to install it. Um and it's very simple. It has a markdown file that gives instructions for it. So you just paste this and give it to your agent. So let's do that. Okay, so you can see I told it uh I just copy and pasted that message uh for this install for agent markdown file. We see it's fetching it and starting to install it right now. It's using bun, so you will need bun. So if you want to do manually as well, here's the instructions. Uh like I said, you need to install bun and then get this embedding key. And then install use bun to install the G brain and then you can you can check it there. You can see my Hermes agent is doing all of that. There you go. G brain is installed but no embedding API keys are present in this shell. So, you need the embeddings key for the vector search. And you can see these are the different um providers that will allow you to do that. But you do need an API key. You can't just use like I'm using Codex OAuth for Hermes agent. It runs separately from Hermes itself. So, it's not going to work with your OAuth. I mean, the embeddings are very small. So, it's not going to cost you a lot of money, but I'm going to be using open router um cuz it will just it'll cost you not that much for it. But you do need to have it set for the vector search to be working. So, once again, these are the manual commands, but once you have that set up, you do G brain in it and then the PG light. So, this will set the the brain as ready and then G brain doctor, which will verify everything is set up properly. But if you're doing this in Hermes, it'll do it uh all automatically. So, you won't have to put in those those commands. Okay, so it's done. Uh everything is installed. And installed the G brain. Everything verified. Uh using open router embedding provider. There we go. So, you can see G brain's been around for a lot, so there's a lot of these kind of optional skill packs. There's been a lot built around it as well. Um but instructions explicitly said to not install them. So, you can see check out all of these and see if they work for you. So, some of these may be different like um ways of ingesting data. I see voice note ingest here. Um so, you could pick what you really have a use for. Okay, so once it's uh set up, you can kind of seed it with different information. I have some demo info here. Um but then Hermes can fill it out more later or you can use different integrations to try to seed it as well. Uh so I just said, "Please seed the G brain with the data in this directory." Okay, so I seeded with that data. So I can ask here, "What do I need to prepare for the meeting with Alice?" And it'll check the uh the G brain. There you go. For the meeting with Alice, prepare three things. It has all these three things I need to prepare based on the notes that were ingested into the G brain. And you'd see it references sources at the bottom here for Alice under people, Acme Robotics under companies, and then the meetings note. So everything is cited and not just assumed. The next part, um this graph graph query, this is something that G brain does quietly that most retrieval stacks won't. Using graph query here will already show what Alice is connected to. We never had to build a graph. It just every page is written and extracts entity references and creates typed edges. So it has worked at, um attended, mentions. With zero LM calls, it's pure pattern matching on the links and the names that's already in your prose. And it really really makes a difference and it makes a real difference. You can see here it's worth 31 points precision over vector only rag based on G brains based on G brains own benchmark. So you can ask here, "Who works at Acme?" And it will have the information as well as once again the sources here. So we use this graph the graph query um to check works at people Alice. So, everything is properly cited and organized and you don't just have an agent kind of making assumptions. So, next you're going to want to set up the MCP server for Gbrain. And this is going to be using Gbrain serve um in order to give it access. So, Gbrain serve wraps Gbrain's engine operations and there's like 47 of them into an MCP and exposes them as 30-plus type tools. When Hermes spawns it as a sub process, those tools get discovered and registered as, you know, MCP Gbrain search, etc. Um and then the model can call them exactly like Hermes built-in tools with structured inputs and outputs that instead of text it has to parse. So, without a MCP server you would have to have the Hermes shelling out to the Gbrain CLI through the terminal tool for every interaction. Um like if you see here after I asked it this question, it had to go here into the CLI and you do Gbrain search directly. And you can do that, but it's not a it doesn't work. You can do that, but it is worse as a process. The model has to compose CLI flags and scrape uh STD out and every call pays the full process startup and opens and closes the PGL uh PG light database. And each command is another shell approval surface, so the MCP server is just one long-lived process holding the database open with a type tool schema as the model can fumble. So, it's a better smoother process. You could simply just in Hermes say, "Can you add the Gbrain MCP server?" Um or if you want to do it manually in config .yaml, you can do this, but easier just to ask your agent to do it. Okay, you can see it added it. And then actually 102 Gbrain MCP tools. That must have increased a lot. Um so, these are all the different tools you can use. Um and then you just need to reload the MCP server. Okay, so let's try asking it a question now. I ask, "Can you tell me what I need to prepare for the next meeting with Alice?" And you could see it's using the MCP G Brain right here. There you go. It's actually much faster. So, yeah, in addition to not having to shell out to the CLI, um it's much faster just to use the MCP tools. And you get similar type of answer, right? With all the sources cited. So, the real advantage of a G Brain is going to be seen as you develop this kind of habit for using it. So, these are kind of the five rules that they list. First, you tell your Hermes to search G Brain first for people, companies, projects, meetings, decisions. Answer from the pages itself. Uh write decisions back. So, durable calls become brain pages. So, anything you decide inside the Hermes itself goes back and stored in the brain. Uh everything is cited. And then memory is not the brain. So, world facts go into the G Brain, not Hermes memory. So, I think this G Brain is probably most useful for people who are kind of solo entrepreneurs or maybe work in a small team. Having a shared G Brain, if you work for a small business or something, I think would be really helpful. And especially in whatever work you do involves a lot of different people and companies and projects that you're trying to juggle all the same time. It just makes for a cleaner integration than just trying to rely on agent memory. Okay, so then close the loop, right? So, before we were going from Hermes or before we were going from the G Brain inputting information into Hermes. So, now we're going to start from Hermes and input information into the brain. So, this is the prompt, "Write this decision to G Brain for the Acme pilots. We start with local PG light. They want uh zero infra proof of concept before considering hosted Postgres. So, this will also call a MCP skill or MCP tool from G Brain. And you see it's calling it right here. Go to the decision to G Brain, it's verified and searchable. So, it created this page actually based on this decision. And you can see this is kind of the structure of it, brain decisions. And then this uh this pilot program. So, these two are not really opposite, Hermes memory and G Brain, but they really work together. Hermes memory is still doing its job. Um nothing was replaced today. It's still a lean curator layer layer in every prompt. And you could just say, you know, what did we talk about last month? And it uses session search to search for it. Whereas G Brain is more of a world catalog. Um and includes whatever hit a chat. We didn't talk about kind of outside integrations uh too much, but there's easy ways to kind of ingest outside data, whether it's meeting notes, plans, emails, anything like that can be organized and put into the G Brain. So, Hermes memory remembers our conversations. G Brain knows our world. So, there you have it. Um in this video it was just kind of an introduction to G Brain. Uh my own introduction since I'm just learning about this. Uh we installed it, we got it set up, and then we did a couple basic commands with it. And now I'm going to use it. I'll probably do a follow-up in a couple weeks or maybe a month as I use uh G Brain now on a daily basis for different projects. I'll let you know any any issues I run into and any kind of lessons or trip tricks I learn while using it. So, that's going to be it for this video. Uh please leave a comment. Let me know your experience with G Brain. Give me any, you know, tips or tricks that you found with it. And I'll I'll try them out. Um thank you for watching.

---

## Timestamped Segments

**[0:00]** So, one of the tools I get asked about a

**[0:02]** lot with Hermes Agent is Gbrain.

**[0:05]** And Gbrain is this open source repo by

**[0:08]** Garry Tan, the president of Y

**[0:10]** Combinator.

**[0:12]** But, it's been out quite a while. It's

**[0:13]** very popular. You see over 25,000 stars.

**[0:17]** And it's used most often with open claw

**[0:19]** or Hermes Agent as a second brain.

**[0:22]** So,

**[0:24]** finally getting around

**[0:25]** to actually test

**[0:26]** So, in this video I'm going to kind of

**[0:28]** describe what it is, how it's different

**[0:30]** from like Hermes memory or an LM Wiki,

**[0:33]** and then we're going to install it,

**[0:35]** and then test it out with our Hermes

**[0:36]** Agent.

**[0:38]** Let's get started.

**[0:40]** And if you like this video, please

**[0:41]** consider following me on X at

**[0:42]** tombi.studio. I'll often be posting

**[0:45]** short videos on the latest AI news and

**[0:48]** agent features, as well as more in-depth

**[0:50]** written post and articles.

**[0:52]** Also, sign up for my free weekly

**[0:54]** newsletter, which I write by hand and

**[0:56]** release every Friday. Here, you'll see

**[0:58]** my honest thoughts about the latest AI

**[1:00]** news, models, research, and give a sneak

**[1:02]** peek of new projects I'm working on

**[1:04]** before they're announced anywhere else.

**[1:06]** Sign up on onchainaigarage.com.

**[1:09]** Link is in the description.

**[1:12]** Okay, so to start off, what is Gbrain

**[1:14]** and how do we use it?

**[1:16]** So,

**[1:17]** take this example, right? You're in

**[1:18]** Hermes chat. You ask, "What did we

**[1:20]** decide about the Acme pilot?"

**[1:22]** Hermes will do a normal session session

**[1:24]** search

**[1:25]** for Acme pilot has zero matches.

**[1:29]** So, it takes the full text of every past

**[1:32]** conversation and still can't find any

**[1:33]** reference to this because we never

**[1:35]** discussed it in Hermes itself. It

**[1:37]** actually lives in meeting notes that

**[1:39]** Hermes had never seen.

**[1:41]** So, Hermes can really only search a

**[1:42]** memory if you actually talked about a

**[1:44]** certain topic with it.

**[1:47]** And that's a boundary, and it's

**[1:48]** architectural. It's not really a bug.

**[1:50]** Every layer of Hermes memory, the

**[1:52]** curated files, the session index, even

**[1:54]** external providers, they all remember

**[1:56]** what passed through the agent. The world

**[1:58]** outside of the chat is invisible to it.

**[2:01]** So, G brain intends to fix this.

**[2:03]** Under the hood in G brain, you have a

**[2:05]** knowledge that lives in markdown files

**[2:07]** in a Git repo. So, that's the system of

**[2:09]** record. G brain syncs it to your local

**[2:12]** Postgres PG light running in process, no

**[2:16]** server, and no docker.

**[2:17]** On top of that, you have a hybrid search

**[2:19]** here. Uh vector plus keyword plus

**[2:21]** knowledge graph that wires itself.

**[2:24]** And the whole thing exposes 30 plus

**[2:25]** tools over MCP. Which is that is which

**[2:28]** is exactly the door Hermes knows how to

**[2:29]** walk through.

**[2:31]** So, it's MIT license. Um like I said,

**[2:33]** 25,000 stars plus. And it's being

**[2:35]** actively developed.

**[2:37]** A very popular uh tool in this

**[2:39]** ecosystem.

**[2:41]** So, what are really the the differences

**[2:42]** between these three things? Hermes

**[2:44]** memory, an LM wiki or knowledge base,

**[2:47]** and then G brain. And these are just

**[2:48]** kind of general explanations. Um I know

**[2:51]** some some may vary a little bit.

**[2:53]** So, Hermes memory has a layer system.

**[2:56]** Uh memory MD and user MD, which are

**[2:59]** curated and always loaded. Session

**[3:01]** search, which is FDS 5 over every past

**[3:04]** conversation. And then there's a lot of

**[3:05]** pluggable providers. Honcho memory,

**[3:07]** super memory,

**[3:08]** many others.

**[3:10]** And what this whole system is built to

**[3:11]** do

**[3:13]** is to remember a collaboration with the

**[3:15]** agent. What was said, what was decided

**[3:17]** and inferred inside of the agent.

**[3:20]** And in the middle here, you can see LM

**[3:22]** wiki, which if you've watched my videos,

**[3:24]** you've heard me talk about this concept

**[3:25]** a lot. And you've seen me build agent

**[3:27]** wikis, which is built around this

**[3:28]** concept. Um and these are just curated

**[3:31]** knowledge bases like the Hermes

**[3:33]** knowledge base you'll see there.

**[3:35]** Um so, it's a domain reference. You have

**[3:37]** concepts, entities, how things work. You

**[3:39]** know, it's compiled by a pipeline with

**[3:41]** human gates and published for any agent

**[3:43]** to read.

**[3:44]** It can answer questions about that

**[3:45]** domain. For example, my Hermes knowledge

**[3:47]** base, you can ask it, you know, how does

**[3:49]** Hermes memory work?

**[3:51]** And it will give you an updated and

**[3:52]** accurate answer.

**[3:54]** And it's a very useful tool. You can

**[3:56]** tell I

**[3:57]** used LM wikis on both Hermes and Gbrain

**[4:00]** to research this video.

**[4:02]** But it is specific to one domain. So

**[4:05]** Gbrain is a little bit different.

**[4:07]** Cuz it's basically a knowledge base for

**[4:09]** your world. Typed pages, people,

**[4:11]** companies, meetings, decisions at

**[4:13]** whatever scare scale

**[4:15]** at whatever scale with a graph and cited

**[4:18]** synthesis.

**[4:20]** And critically, it ingests things that

**[4:21]** never touched your chat. So notes

**[4:23]** folder, Obsidian vaults, meeting

**[4:25]** write-ups, captures.

**[4:27]** It's the difference between what the

**[4:28]** agent picked up along the way and what

**[4:30]** you deliberately decide to keep.

**[4:32]** So simply put, memory remembers our

**[4:34]** conversations, the LM wikis know

**[4:36]** domains, Gbrain knows our world.

**[4:39]** So here's the architecture and it's

**[4:40]** fairly simple.

**[4:43]** If you're working in Hermes agent or

**[4:44]** whatever agent harness you're using, you

**[4:46]** can use a MCP or STTIO subprocess

**[4:51]** to spawn Gbrain serve.

**[4:53]** And that's a local MCP subprocess.

**[4:56]** There's no HTTP server, no tunnel, no

**[4:58]** token or anything like that. Gbrain

**[5:00]** reads and writes a PG light database and

**[5:03]** the database is synced from plain

**[5:05]** markdown repo under Git. So every layer

**[5:07]** is inspectable here.

**[5:10]** The markdown is yours.

**[5:11]** The database is a local file. The MCP

**[5:14]** server is just a subprocess that dies

**[5:16]** with the session.

**[5:18]** Okay, so let's install it.

**[5:19]** So you can see in the repo itself, it

**[5:21]** has instructions for how you want to

**[5:22]** install it.

**[5:23]** Um and it's very simple. It has a

**[5:24]** markdown file that gives instructions

**[5:27]** for it.

**[5:27]** So you just paste this and give it to

**[5:29]** your agent. So let's do that. Okay, so

**[5:31]** you can see I told it uh

**[5:33]** I just copy and pasted that message

**[5:36]** uh for this install for agent markdown

**[5:38]** file.

**[5:39]** We see it's fetching it and starting to

**[5:41]** install it right now.

**[5:42]** It's using bun, so you will need bun.

**[5:46]** So if you want to do manually as well,

**[5:47]** here's the instructions.

**[5:50]** Uh like I said, you need to install bun

**[5:52]** and then get this embedding key.

**[5:55]** And then install use bun to install the

**[5:57]** G brain and then you can you can check

**[5:59]** it there.

**[6:00]** You can see my Hermes agent is doing all

**[6:02]** of that.

**[6:04]** There you go. G brain is installed but

**[6:06]** no embedding

**[6:07]** API keys are present in this shell.

**[6:11]** So, you need the embeddings key for the

**[6:13]** vector search. And you can see these are

**[6:15]** the different

**[6:17]** um providers that will allow you to do

**[6:19]** that. But you do need an API key. You

**[6:21]** can't just use like I'm using Codex

**[6:23]** OAuth for Hermes agent. It runs

**[6:25]** separately from

**[6:27]** Hermes itself. So, it's not going to

**[6:29]** work with your OAuth.

**[6:31]** I mean, the embeddings are very small.

**[6:33]** So, it's not going to cost you a lot of

**[6:34]** money, but I'm going to be using open

**[6:36]** router

**[6:37]** um cuz it will just it'll cost you not

**[6:39]** that much for it. But you do need to

**[6:41]** have it set for the vector search to be

**[6:43]** working.

**[6:45]** So, once again, these are the manual

**[6:46]** commands, but once you have that set up,

**[6:48]** you do G brain in it and then the PG

**[6:51]** light. So, this will set the the brain

**[6:53]** as ready and then G brain doctor, which

**[6:55]** will verify everything is set up

**[6:57]** properly.

**[6:58]** But if you're doing this in Hermes,

**[6:59]** it'll do it uh all automatically. So,

**[7:02]** you won't have to put in those those

**[7:03]** commands.

**[7:05]** Okay, so it's done.

**[7:07]** Uh everything is installed.

**[7:09]** And installed the G brain.

**[7:12]** Everything verified.

**[7:15]** Uh

**[7:15]** using open router embedding provider.

**[7:19]** There we go.

**[7:21]** So, you can see G brain's been around

**[7:23]** for a lot, so there's a lot of these

**[7:24]** kind of optional skill packs. There's

**[7:25]** been a lot built around it as well.

**[7:28]** Um but instructions explicitly said to

**[7:30]** not install them. So, you can see check

**[7:33]** out all of these and see if they work

**[7:34]** for you.

**[7:36]** So, some of these may be different like

**[7:38]** um

**[7:38]** ways of ingesting data. I see voice note

**[7:41]** ingest here.

**[7:42]** Um so, you could pick what you really

**[7:44]** have a use for.

**[7:46]** Okay, so once it's

**[7:48]** uh set up,

**[7:50]** you can kind of seed it with different

**[7:51]** information. I have some demo

**[7:53]** info here.

**[7:55]** Um but then Hermes can fill it out more

**[7:57]** later or you can

**[7:59]** use different integrations to try to

**[8:00]** seed it as well.

**[8:02]** Uh so I just said, "Please seed the G

**[8:03]** brain with the data in this directory."

**[8:07]** Okay, so I seeded with that data. So I

**[8:09]** can ask here, "What do I need to prepare

**[8:11]** for the meeting with Alice?"

**[8:13]** And it'll check the uh the G brain.

**[8:16]** There you go. For the meeting with

**[8:17]** Alice, prepare three things. It has all

**[8:20]** these three things I need to prepare

**[8:21]** based on the notes

**[8:23]** that were ingested into the G brain.

**[8:25]** And you'd see it references sources at

**[8:27]** the bottom here

**[8:28]** for Alice under people, Acme Robotics

**[8:31]** under companies, and then the meetings

**[8:33]** note. So everything is cited and not

**[8:36]** just assumed.

**[8:37]** The next part, um this graph graph

**[8:40]** query,

**[8:41]** this is something that G brain does

**[8:42]** quietly that most retrieval stacks

**[8:44]** won't.

**[8:45]** Using graph query here will already show

**[8:49]** what Alice is connected to.

**[8:51]** We never had to build a graph. It just

**[8:53]** every page is written and extracts

**[8:55]** entity references and creates typed

**[8:57]** edges. So it has worked at, um attended,

**[9:00]** mentions.

**[9:02]** With zero LM calls, it's pure pattern

**[9:05]** matching on the links and the names

**[9:06]** that's already in your prose.

**[9:09]** And it really really makes a difference

**[9:11]** and it makes a real difference. You can

**[9:12]** see here it's worth 31 points precision

**[9:14]** over vector only rag based on G brains

**[9:17]** based on G brains own benchmark.

**[9:21]** So you can ask here, "Who works at

**[9:23]** Acme?"

**[9:27]** And it will have the information as well

**[9:29]** as once again the sources here. So we

**[9:31]** use this graph

**[9:32]** the graph query

**[9:33]** um to check works at people Alice. So,

**[9:36]** everything is

**[9:38]** properly cited and organized and you

**[9:41]** don't just have an agent kind of making

**[9:42]** assumptions.

**[9:43]** So, next you're going to want to set up

**[9:44]** the MCP server for Gbrain.

**[9:47]** And this is going to be using Gbrain

**[9:49]** serve

**[9:50]** um in order to give it access.

**[9:53]** So, Gbrain serve wraps Gbrain's engine

**[9:55]** operations and there's like 47 of them

**[9:58]** into an MCP and exposes them as 30-plus

**[10:00]** type tools.

**[10:02]** When Hermes spawns it as a sub process,

**[10:04]** those tools get discovered and

**[10:05]** registered as, you know, MCP Gbrain

**[10:07]** search, etc.

**[10:09]** Um and then the model can call them

**[10:10]** exactly like Hermes built-in tools with

**[10:13]** structured inputs and outputs that

**[10:14]** instead of text it has to parse. So,

**[10:16]** without a MCP server

**[10:19]** you would have to have the Hermes

**[10:20]** shelling out to the Gbrain CLI through

**[10:22]** the terminal tool for every interaction.

**[10:25]** Um like if you see here

**[10:28]** after I asked it this question, it had

**[10:29]** to go here into the CLI and you do

**[10:32]** Gbrain search directly.

**[10:35]** And you can do that, but it's not a

**[10:38]** it doesn't work.

**[10:39]** You can do that, but it is worse as a

**[10:42]** process.

**[10:43]** The model has to compose CLI flags and

**[10:45]** scrape uh STD out and every call pays

**[10:48]** the full process startup and opens and

**[10:50]** closes the PGL

**[10:52]** uh PG light database.

**[10:54]** And each command is another shell

**[10:55]** approval surface, so the MCP server is

**[10:58]** just one long-lived process holding the

**[11:00]** database open with a type tool schema as

**[11:02]** the model can fumble. So, it's a better

**[11:04]** smoother process.

**[11:06]** You could simply just in Hermes say,

**[11:07]** "Can you add the Gbrain MCP server?"

**[11:11]** Um or if you want to do it manually in

**[11:13]** config .yaml, you can do this, but

**[11:16]** easier just to ask your agent to do it.

**[11:18]** Okay, you can see it added it.

**[11:21]** And then actually 102 Gbrain MCP tools.

**[11:25]** That must have increased a lot. Um

**[11:28]** so, these are all the different tools

**[11:29]** you can use.

**[11:31]** Um

**[11:32]** and then you just need to reload the MCP

**[11:34]** server.

**[11:35]** Okay, so let's try asking it a question

**[11:37]** now. I ask, "Can you tell me what I need

**[11:40]** to prepare for the next meeting with

**[11:41]** Alice?"

**[11:43]** And you could see it's using the MCP G

**[11:45]** Brain right here.

**[11:49]** There you go. It's actually much faster.

**[11:51]** So, yeah, in addition to not having to

**[11:53]** shell out to the CLI,

**[11:55]** um it's much faster just to use the MCP

**[11:57]** tools.

**[11:59]** And you get similar type of answer,

**[12:00]** right? With all the sources cited.

**[12:04]** So, the real advantage of a G Brain is

**[12:06]** going to be seen as you develop this

**[12:09]** kind of habit for using it.

**[12:11]** So, these are kind of the five rules

**[12:12]** that they list.

**[12:14]** First, you tell your Hermes to search G

**[12:16]** Brain first for people, companies,

**[12:17]** projects, meetings, decisions. Answer

**[12:20]** from the pages itself. Uh write

**[12:22]** decisions back.

**[12:24]** So, durable calls become brain pages.

**[12:26]** So, anything you decide inside the

**[12:27]** Hermes itself goes back and stored in

**[12:29]** the brain.

**[12:30]** Uh everything is cited.

**[12:32]** And then memory is not the brain. So,

**[12:35]** world facts go into the G Brain, not

**[12:37]** Hermes memory. So, I think this G Brain

**[12:40]** is probably most useful for people who

**[12:43]** are kind of solo entrepreneurs or maybe

**[12:45]** work in a small team.

**[12:48]** Having a shared G Brain, if you work for

**[12:50]** a small business or something, I think

**[12:51]** would be really helpful.

**[12:53]** And especially in whatever work you do

**[12:55]** involves a lot of different people and

**[12:56]** companies and projects that you're

**[12:58]** trying to juggle all the same time.

**[13:01]** It just makes for a cleaner integration

**[13:03]** than just trying to rely on agent

**[13:04]** memory.

**[13:05]** Okay, so then close the loop, right?

**[13:08]** So, before we were going from Hermes or

**[13:10]** before we were going from the G Brain

**[13:12]** inputting information into Hermes. So,

**[13:14]** now we're going to start from Hermes and

**[13:16]** input information into the brain.

**[13:19]** So, this is the prompt, "Write this

**[13:21]** decision to G Brain for the Acme pilots.

**[13:23]** We start with local PG light. They want

**[13:26]** uh zero infra proof of concept before

**[13:28]** considering hosted Postgres.

**[13:30]** So, this will also call a MCP skill

**[13:33]** or MCP tool

**[13:35]** from G Brain.

**[13:37]** And you see it's calling it right here.

**[13:41]** Go to the decision to G Brain, it's

**[13:43]** verified and searchable.

**[13:45]** So, it created this page actually based

**[13:46]** on this decision.

**[13:48]** And you can see this is kind of the

**[13:49]** structure of it, brain decisions.

**[13:52]** And then this uh this pilot program.

**[13:56]** So, these two are not really opposite,

**[13:58]** Hermes memory and G Brain, but they

**[14:00]** really work together. Hermes memory is

**[14:02]** still doing its job. Um nothing was

**[14:04]** replaced today. It's still a lean

**[14:06]** curator layer layer in every prompt. And

**[14:08]** you could just say, you know, what did

**[14:09]** we talk about last month? And it uses

**[14:12]** session search to search for it.

**[14:14]** Whereas G Brain is more of a world

**[14:15]** catalog. Um and includes whatever hit a

**[14:18]** chat. We didn't talk about kind of

**[14:19]** outside integrations uh too much, but

**[14:22]** there's easy ways to kind of ingest

**[14:24]** outside data, whether it's meeting

**[14:26]** notes, plans,

**[14:28]** emails, anything like that can be

**[14:30]** organized and put into the G Brain.

**[14:34]** So, Hermes memory remembers our

**[14:35]** conversations. G Brain knows our world.

**[14:38]** So, there you have it. Um in this video

**[14:40]** it was just kind of an introduction to G

**[14:42]** Brain. Uh my own introduction since I'm

**[14:44]** just learning about this.

**[14:46]** Uh we installed it, we got it set up,

**[14:48]** and then we did a couple basic commands

**[14:50]** with it.

**[14:51]** And now I'm going to use it. I'll

**[14:52]** probably do a follow-up in a couple

**[14:54]** weeks or maybe a month as I use uh G

**[14:57]** Brain now on a daily basis for different

**[14:59]** projects.

**[15:00]** I'll let you know any any issues I run

**[15:02]** into

**[15:03]** and any kind of lessons or trip tricks I

**[15:05]** learn while using it.

**[15:07]** So, that's going to be it for this

**[15:08]** video.

**[15:09]** Uh please leave a comment. Let me know

**[15:10]** your experience with G Brain.

**[15:12]** Give me any, you know, tips or tricks

**[15:14]** that you found with it.

**[15:16]** And I'll I'll try them out. Um thank you

**[15:18]** for watching.
