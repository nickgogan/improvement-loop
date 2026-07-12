# Transcript: 12 Open Source AI Tools That Feel ILLEGAL To Know About

**URL:** https://www.youtube.com/watch?v=dk1Y3VtC3F8
**Segments:** 365
**Channel:** Cloud Codes
**Duration:** 14:30
**Uploaded:** 2026-07-08

---

## Full Text

Right now, somewhere, a startup is raising millions of dollars to sell you a feature you could get for free. I am going to show you exactly where it is hiding. These are 12 open-source AI tools so powerful and so completely free that knowing about them almost feels illegal. Learn these and you can stop paying for half the AI services on your monthly bill. No catch, no trial, no credit card, no per token meter running in the background. A document parser here, a vector database there, model hosting, an observability suite, a scraping API, stack up the paid versions, and it is easily a few thousand dollars a month. Every one of them has a free open-source twin that is often just plain better. Because together, these are not random downloads. They are the entire modern AI stack. Reading documents and web pages, chunking and storing them, running the models, structuring the output, and watching the whole thing in production. Every single layer open-source. And here is what changed. Open models finally caught up. So, the same toolkit the big labs and funded startups quietly built on is now sitting on GitHub waiting for anyone who knows the names. Let us count them down from number 10. Number 10, Chunky. Before any AI can answer questions about your own documents, it first has to break them into small bite-size pieces. That step is called chunking, and almost nobody thinks about it until their AI starts giving confidently wrong answers. Chunky is a tiny library that does this one boring job perfectly. You install it in about a second, hand it a wall of text, and it splits that text intelligently. Not by blindly counting characters, but by sentences, by paragraphs, by actual meaning, and even by the structure of source code. You get token, sentence, recursive, and semantic chunkers, plus late chunking that embeds the whole document first, so every piece keeps its surrounding context. One import, a single line, and your messy document becomes clean. Slightly overlapping chunks that are ready to embed. It is faster than the heavyweight frameworks that try to do the same thing, and it stays out of your way. 4,400 stars, a permissive MIT license, and it quietly fixes the number one reason retrieval systems give you garbage. This is the piece every tutorial skips right past. Number nine, Marker. Roughly 65% of the useful information is trapped inside PDFs. Contracts, research papers, financial filings, scanned manuals. Copy and paste turns them into scrambled garbage. Marker turns them into clean, usable text. Point it at a PDF, a Word file, a slide deck, or even a photo of a page, and it hands you back tidy markdown. And it keeps what actually matters. The tables stay tables, the math equations stay math, the headings and the reading order all survive the trip intact. It even pulls equations out as clean LaTeX, and turns form fields and checkboxes into structured data you can actually query. It runs entirely on your own machine. It handles dozens of languages, and in blind comparisons, people rank its output above the paid cloud parsers. 37,000 stars, built by the team at Data Lab. Something like 2/3 of enterprise data is locked in documents like these. This is the tool that finally hands all of it to an AI for nothing. Number eight, LangFuse. The moment your AI app hits real users, one question starts to haunt you. What is it actually doing in there? Why was that answer weird? Why did the bill suddenly triple overnight? LangFuse gives you eyes inside the black box. It records every call your app makes to a model. The exact prompt, the response, how long it took, how many tokens it burned, and precisely what it cost. You get a full trace of every step, so you can replay a bad answer and see exactly where it went off the rails. You can tag traces by user and session, so you can find the one conversation that broke out of a hundred thousand of them. On top of that, it manages your prompts, runs evaluations, and scores quality over time. The exact stuff that paid monitoring platforms charge you per seat for every month. 30,000 stars, and it is fully self-hostable, so all of that sensitive prompt and user data never has to leave your own servers. Number seven, Qdrant. Once your text is chunked and turned into vectors, long lists of numbers that capture meaning, you need somewhere to keep them and a way to search them by similarity in milliseconds. That is a vector database, and Qdrant is one of the very best. Ask it for the 10 pieces of text closest in meaning to a question, and it finds them almost instantly, even across millions of vectors. It filters by metadata, it shrinks memory with quantization, and it does hybrid keyword plus vector search right out of the box. Because every vector carries a payload, you filter and search in one request. The closest matches, but only from this user in this date range. It is written in Rust, so it stays blisteringly fast and rock solid under heavy load, and you can run the entire thing in a single Docker container on your laptop. 33,000 stars, and it is the quiet engine sitting behind a huge amount of the AI search you already use every day. Number six, Ollama. This is the one that made running a full large language model on your own computer feel completely normal. No API keys, no cloud, no meter ticking in the background. You type three words, Ollama run, and the name of a model, and seconds later you are chatting with a serious AI running entirely offline on your own hardware. Llama, Mistral, Qwen, Gemma, Deepseek, a whole library of them, one command each. It quietly handles all the hard parts, downloading the weights, fitting them onto your GPU or CPU, and exposing a clean local API that speaks the exact same language as OpenAI. So, most apps can point at a Llama instead and just work. It runs the newest open models the day they drop and pulls them from a simple registry, exactly like Docker images. That means total privacy, zero usage fees, and no rate limit forever. 176,000 stars make it one of the most loved projects in all of open source, and it is the front door to local AI number five, DSPy out of Stanford. Right now, everyone is hand-tweaking magic prompt words, "Please, I will tip you. Take a deep breath." hoping the model behaves. DSPy calls that a dead end and replaces it with actual programming. Instead of writing a fragile paragraph of instructions, you just declare what goes in and what should come out. Then, DSPy optimizers automatically write and tune the prompt for you, testing variation after variation against real examples until the scores climb. You compose your app out of modules, a retriever, a chain of thought, a validator, and DSPy tunes the whole pipeline as one system. Swap the underlying model and you do not rewrite a thing. You simply recompile and the system reoptimizes itself for the new one. It is prompt engineering done by the machine instead of by you guessing in the dark. 36,000 stars, and it is how serious teams build AI that actually survives contact with the real world. Number four, crawl for AI. The entire internet is the largest data set on Earth, and this is the tool that hands it to your AI for free. It was the single most trending repository on all of GitHub, and it is really not hard to see why. Give it a URL and it loads the page in a real browser, JavaScript, dynamic content and all, then strips away the ads, the menus, and the clutter, and returns clean markdown that a language model can actually read. You can even feed those pages straight into a model in the same call. So, crawling and extraction happen in one clean step. It runs fully asynchronous, so it can crawl hundreds of pages at once. It handles logins, scrolling, and clicks, and it can pull out exactly the structured fields you ask for. No more fragile, handwritten scrapers breaking every week. Commercial scraping APIs bill you by the thousand pages. Crawl 4 AI does the same job on your own machine for nothing. 71,000 stars and climbing fast. Number three, outlines. Language models love to ramble, but your code needs clean, structured data, a specific JSON shape every single time with no apologies and no stray commentary bolted on the end. Outlines guarantees it. You hand it a schema, say a Pydantic model, or even a regular expression, and it constrains the model as it generates token by token, so the output physically cannot break the shape you asked for. Valid JSON is not likely, it is guaranteed. It handles JSON schema, regular expressions, multiple choice, and full grammars, anywhere the output has to obey strict rules. This is not a hopeful retry loop. It steers the decoding itself, and it runs right on top of your local models through a llama or vLLM. 14,000 stars, and it turns an unpredictable chatbot into a reliable API you can build on. Number two, Light LLM. Every AI provider has its own slightly different API. OpenAI, Anthropic, Google, your local Alama. Wire your app to one of them, and you are quietly locked in. LiteLLM smashes that lock wide open. It gives you one single format, the OpenAI one, to call over 100 different models. Want to swap GPT for Claude, or fall back to a cheap local model the second the bill gets scary? You change one string. The rest of your code never even notices. It smooths over the messy differences, too. Streaming, tool calls, vision, embeddings, so they behave identically no matter who is serving the model. Run it as a gateway in front of your whole team, and it gets even better. One place for every API, key, live cost tracking, hard spending limits, automatic fallbacks, and load balancing across every provider at once. It is a universal adapter for the entire AI industry. 53,000 stars, and it means you are never ever locked to a single vendor again. And number one, Instructor. If I could keep only a single tool from this entire list, it would be this one, because it fixes the exact problem that makes AI so painful to actually build real software with. You define the shape of the data you want as a plain Python class. You ask the model, and Instructor hands you back a fully typed, validated object, not a blob of text you then have to pray parses correctly at 2:00 in the morning. And here is the magic. When the model gets it slightly wrong, Instructor catches the validation error, feeds it right back with the specific mistake, and asks the model to fix itself, automatically retrying until the data comes out clean and correct. Pull the name, the amount, and the due date off an invoice, and you get back a typed object with the right fields, or a precise error, never a silent mess. It is built on Pydantic. It works with basically every model, and it now runs in Python, TypeScript, Go, and more. 13,000 stars, and it turns flaky AI output into software you can genuinely trust. That is the list that started all of this, but I promised you two more. These are the two professional-grade tools I added myself, and they slot straight into the exact same stack. Bonus number one, vLLM. Ollama is perfect for running a model just for yourself, but what happens when you need to serve that model to thousands of users at once, at full speed, without melting your GPU? That is vLLM, born at Berkeley, now the industry default serving engine. Its secret is a trick called paged attention. It manages the model memory the way an operating system manages RAM, wasting almost none of it. The result is up to 24 times the throughput of a naive setup from the very same graphics card. It also does continuous batching, slotting new requests in between others mid-flight, so the GPU is never left sitting there waiting. It serves an OpenAI-compatible API. It batches incoming requests automatically, and it powers a huge share of the world's self-hosted AI. 85,000 stars. When a company tells you they run their own models in production at scale, this is very often exactly how they are doing it. Bonus number two, RagAs. So, you have built your AI, and it gives you an answer. Here is the genuinely terrifying question. Is that answer correct, or is it just confidently making things up? RagAs replaces gut feeling with real numbers. It scores your system on the things you simply cannot eyeball at scale. Is the answer faithful to the source? Is it actually relevant? And did retrieval even pull back the right context? And it does it using models as the judges, so you barely need any hand-labeled data. It can even generate a synthetic test set straight from your own documents, so you have something to measure against on day one. That turns a vague it seems fine into a dashboard of hard metrics you can track on every change and catch the moment an innocent update quietly makes everything worse. 15,000 stars. So, there is the whole stack in one picture. Marker and crawl for AI together. Chunky to chunk, Qdrant to store, a llama and vLLM to run, DSPy, outlines, instructor, and LiteLLM to build and control it. And LangFuse and RagAs to actually trust it. 12 tools, every layer, all free. Companies stitch these exact projects together and charge you thousands of dollars a month for the result. Now, you know they are just sitting on GitHub waiting. And once you have seen them, you honestly cannot unsee them. The barrier was never money. It was only ever knowing which names to type into that search bar. If this saved you from a subscription or two, do the free thing and subscribe. I go deep on open source AI like this every week here on Cloud Code. I will see you in the next

---

## Timestamped Segments

**[0:00]** Right now, somewhere, a startup is

**[0:02]** raising millions of dollars to sell you

**[0:04]** a feature you could get for free.

**[0:06]** I am going to show you exactly where it

**[0:08]** is hiding. These are 12 open-source AI

**[0:10]** tools so powerful and so completely free

**[0:14]** that knowing about them almost feels

**[0:15]** illegal. Learn these and you can stop

**[0:18]** paying for half the AI services on your

**[0:20]** monthly bill. No catch, no trial, no

**[0:23]** credit card, no per token meter running

**[0:26]** in the background. A document parser

**[0:28]** here, a vector database there, model

**[0:31]** hosting, an observability suite, a

**[0:33]** scraping API, stack up the paid

**[0:36]** versions, and it is easily a few

**[0:38]** thousand dollars a month. Every one of

**[0:40]** them has a free open-source twin that is

**[0:42]** often just plain better. Because

**[0:44]** together, these are not random

**[0:46]** downloads. They are the entire modern AI

**[0:48]** stack. Reading documents and web pages,

**[0:52]** chunking and storing them, running the

**[0:54]** models, structuring the output, and

**[0:56]** watching the whole thing in production.

**[0:58]** Every single layer open-source. And here

**[1:01]** is what changed. Open models finally

**[1:03]** caught up. So, the same toolkit the big

**[1:06]** labs and funded startups quietly built

**[1:08]** on is now sitting on GitHub waiting for

**[1:11]** anyone who knows the names. Let us count

**[1:13]** them down from number 10. Number 10,

**[1:16]** Chunky. Before any AI can answer

**[1:19]** questions about your own documents, it

**[1:21]** first has to break them into small

**[1:23]** bite-size pieces. That step is called

**[1:26]** chunking, and almost nobody thinks about

**[1:28]** it until their AI starts giving

**[1:30]** confidently wrong answers. Chunky is a

**[1:32]** tiny library that does this one boring

**[1:35]** job perfectly.

**[1:36]** You install it in about a second, hand

**[1:38]** it a wall of text, and it splits that

**[1:41]** text intelligently. Not by blindly

**[1:43]** counting characters, but by sentences,

**[1:46]** by paragraphs, by actual meaning, and

**[1:48]** even by the structure of source code.

**[1:51]** You get token, sentence, recursive, and

**[1:53]** semantic chunkers, plus late chunking

**[1:56]** that embeds the whole document first, so

**[1:58]** every piece keeps its surrounding

**[2:00]** context. One import, a single line, and

**[2:03]** your messy document becomes clean.

**[2:05]** Slightly overlapping chunks that are

**[2:07]** ready to embed. It is faster than the

**[2:10]** heavyweight frameworks that try to do

**[2:11]** the same thing, and it stays out of your

**[2:13]** way.

**[2:14]** 4,400 stars, a permissive MIT license,

**[2:18]** and it quietly fixes the number one

**[2:20]** reason retrieval systems give you

**[2:21]** garbage. This is the piece every

**[2:23]** tutorial skips right past. Number nine,

**[2:27]** Marker. Roughly 65% of the useful

**[2:30]** information is trapped inside PDFs.

**[2:33]** Contracts, research papers, financial

**[2:35]** filings, scanned manuals. Copy and paste

**[2:38]** turns them into scrambled garbage.

**[2:40]** Marker turns them into clean, usable

**[2:42]** text. Point it at a PDF, a Word file, a

**[2:46]** slide deck, or even a photo of a page,

**[2:49]** and it hands you back tidy markdown. And

**[2:51]** it keeps what actually matters. The

**[2:53]** tables stay tables, the math equations

**[2:55]** stay math, the headings and the reading

**[2:57]** order all survive the trip intact. It

**[3:00]** even pulls equations out as clean LaTeX,

**[3:03]** and turns form fields and checkboxes

**[3:05]** into structured data you can actually

**[3:07]** query.

**[3:08]** It runs entirely on your own machine. It

**[3:10]** handles dozens of languages, and in

**[3:12]** blind comparisons, people rank its

**[3:14]** output above the paid cloud parsers.

**[3:17]** 37,000 stars, built by the team at Data

**[3:20]** Lab. Something like 2/3 of enterprise

**[3:22]** data is locked in documents like these.

**[3:25]** This is the tool that finally hands all

**[3:27]** of it to an AI for nothing. Number

**[3:29]** eight, LangFuse. The moment your AI

**[3:33]** app hits real users, one question starts

**[3:35]** to haunt you. What is it actually doing

**[3:38]** in there? Why was that answer weird? Why

**[3:40]** did the bill suddenly triple overnight?

**[3:43]** LangFuse gives you eyes inside the black

**[3:45]** box. It records every call your app

**[3:48]** makes to a model. The exact prompt, the

**[3:50]** response, how long it took, how many

**[3:53]** tokens it burned, and precisely what it

**[3:55]** cost. You get a full trace of every

**[3:57]** step, so you can replay a bad answer and

**[4:00]** see exactly where it went off the rails.

**[4:02]** You can tag traces by user and session,

**[4:05]** so you can find the one conversation

**[4:06]** that broke out of a hundred thousand of

**[4:08]** them. On top of that, it manages your

**[4:11]** prompts, runs evaluations, and scores

**[4:13]** quality over time. The exact stuff that

**[4:16]** paid monitoring platforms charge you per

**[4:18]** seat for every month. 30,000 stars, and

**[4:21]** it is fully self-hostable, so all of

**[4:24]** that sensitive prompt and user data

**[4:25]** never has to leave your own servers.

**[4:28]** Number seven, Qdrant. Once your text is

**[4:31]** chunked and turned into vectors, long

**[4:33]** lists of numbers that capture meaning,

**[4:35]** you need somewhere to keep them and a

**[4:37]** way to search them by similarity in

**[4:39]** milliseconds. That is a vector database,

**[4:42]** and Qdrant is one of the very best. Ask

**[4:45]** it for the 10 pieces of text closest in

**[4:47]** meaning to a question, and it finds them

**[4:49]** almost instantly, even across millions

**[4:51]** of vectors. It filters by metadata, it

**[4:54]** shrinks memory with quantization, and it

**[4:57]** does hybrid keyword plus vector search

**[4:59]** right out of the box. Because every

**[5:01]** vector carries a payload, you filter and

**[5:03]** search in one request. The closest

**[5:06]** matches, but only from this user in this

**[5:08]** date range. It is written in Rust, so it

**[5:11]** stays blisteringly fast and rock solid

**[5:13]** under heavy load, and you can run the

**[5:15]** entire thing in a single Docker

**[5:17]** container on your laptop. 33,000 stars,

**[5:20]** and it is the quiet engine sitting

**[5:22]** behind a huge amount of the AI search

**[5:24]** you already use every day. Number six,

**[5:27]** Ollama. This is the one that made

**[5:29]** running a full large language model on

**[5:31]** your own computer feel completely

**[5:32]** normal. No API keys, no cloud, no meter

**[5:36]** ticking in the background. You type

**[5:38]** three words, Ollama run, and the name of

**[5:41]** a model, and seconds later you are

**[5:43]** chatting with a serious AI running

**[5:45]** entirely offline on your own hardware.

**[5:48]** Llama, Mistral, Qwen, Gemma, Deepseek, a

**[5:52]** whole library of them, one command each.

**[5:55]** It quietly handles all the hard parts,

**[5:57]** downloading the weights, fitting them

**[5:59]** onto your GPU or CPU, and exposing a

**[6:02]** clean local API that speaks the exact

**[6:04]** same language as OpenAI. So, most apps

**[6:07]** can point at a Llama instead and just

**[6:09]** work.

**[6:10]** It runs the newest open models the day

**[6:12]** they drop and pulls them from a simple

**[6:14]** registry, exactly like Docker images.

**[6:17]** That means total privacy, zero usage

**[6:20]** fees, and no rate limit forever.

**[6:23]** 176,000

**[6:25]** stars make it one of the most loved

**[6:26]** projects in all of open source, and it

**[6:29]** is the front door to local AI number

**[6:31]** five, DSPy out of Stanford. Right now,

**[6:35]** everyone is hand-tweaking magic prompt

**[6:37]** words, "Please, I will tip you. Take a

**[6:39]** deep breath." hoping the model behaves.

**[6:42]** DSPy calls that a dead end and replaces

**[6:45]** it with actual programming.

**[6:47]** Instead of writing a fragile paragraph

**[6:49]** of instructions, you just declare what

**[6:51]** goes in and what should come out. Then,

**[6:53]** DSPy optimizers automatically write and

**[6:56]** tune the prompt for you, testing

**[6:58]** variation after variation against real

**[7:00]** examples until the scores climb.

**[7:03]** You compose your app out of modules, a

**[7:05]** retriever, a chain of thought, a

**[7:07]** validator, and DSPy tunes the whole

**[7:10]** pipeline as one system. Swap the

**[7:12]** underlying model and you do not rewrite

**[7:14]** a thing. You simply recompile and the

**[7:16]** system reoptimizes itself for the new

**[7:19]** one. It is prompt engineering done by

**[7:21]** the machine instead of by you guessing

**[7:24]** in the dark. 36,000 stars, and it is how

**[7:27]** serious teams build AI that actually

**[7:29]** survives contact with the real world.

**[7:32]** Number four, crawl for AI. The entire

**[7:35]** internet is the largest data set on

**[7:37]** Earth, and this is the tool that hands

**[7:39]** it to your AI for free.

**[7:42]** It was the single most trending

**[7:43]** repository on all of GitHub, and it is

**[7:46]** really not hard to see why. Give it a

**[7:48]** URL

**[7:49]** and it loads the page in a real browser,

**[7:52]** JavaScript, dynamic content and all,

**[7:54]** then strips away the ads, the menus, and

**[7:57]** the clutter, and returns clean markdown

**[7:59]** that a language model can actually read.

**[8:02]** You can even feed those pages straight

**[8:03]** into a model in the same call. So,

**[8:06]** crawling and extraction happen in one

**[8:08]** clean step. It runs fully asynchronous,

**[8:11]** so it can crawl hundreds of pages at

**[8:12]** once. It handles logins, scrolling, and

**[8:15]** clicks, and it can pull out exactly the

**[8:18]** structured fields you ask for. No more

**[8:20]** fragile, handwritten scrapers breaking

**[8:22]** every week. Commercial scraping APIs

**[8:25]** bill you by the thousand pages. Crawl 4

**[8:28]** AI does the same job on your own machine

**[8:30]** for nothing. 71,000 stars and climbing

**[8:33]** fast. Number three, outlines. Language

**[8:37]** models love to ramble, but your code

**[8:39]** needs clean, structured data, a specific

**[8:42]** JSON shape every single time with no

**[8:45]** apologies and no stray commentary bolted

**[8:47]** on the end.

**[8:48]** Outlines guarantees it. You hand it a

**[8:50]** schema, say a Pydantic model, or even a

**[8:53]** regular expression, and it constrains

**[8:56]** the model as it generates token by

**[8:58]** token, so the output physically cannot

**[9:01]** break the shape you asked for. Valid

**[9:03]** JSON is not likely, it is guaranteed.

**[9:06]** It handles JSON schema, regular

**[9:08]** expressions, multiple choice, and full

**[9:11]** grammars, anywhere the output has to

**[9:13]** obey strict rules. This is not a hopeful

**[9:15]** retry loop. It steers the decoding

**[9:18]** itself, and it runs right on top of your

**[9:20]** local models through a llama or vLLM.

**[9:23]** 14,000 stars, and it turns an

**[9:26]** unpredictable chatbot into a reliable

**[9:28]** API you can build on.

**[9:30]** Number two, Light LLM.

**[9:33]** Every AI provider has its own slightly

**[9:35]** different API. OpenAI, Anthropic,

**[9:39]** Google, your local Alama. Wire your app

**[9:42]** to one of them, and you are quietly

**[9:44]** locked in. LiteLLM smashes that lock

**[9:47]** wide open. It gives you one single

**[9:49]** format, the OpenAI one, to call over 100

**[9:53]** different models. Want to swap GPT for

**[9:55]** Claude, or fall back to a cheap local

**[9:57]** model the second the bill gets scary?

**[10:00]** You change one string. The rest of your

**[10:02]** code never even notices. It smooths over

**[10:05]** the messy differences, too. Streaming,

**[10:07]** tool calls, vision, embeddings, so they

**[10:10]** behave identically no matter who is

**[10:12]** serving the model. Run it as a gateway

**[10:14]** in front of your whole team, and it gets

**[10:16]** even better. One place for every API,

**[10:20]** key, live cost tracking, hard spending

**[10:23]** limits, automatic fallbacks, and load

**[10:25]** balancing across every provider at once.

**[10:28]** It is a universal adapter for the entire

**[10:30]** AI industry. 53,000 stars, and it means

**[10:34]** you are never ever locked to a single

**[10:36]** vendor again. And number one,

**[10:38]** Instructor. If I could keep only a

**[10:40]** single tool from this entire list, it

**[10:43]** would be this one, because it fixes the

**[10:45]** exact problem that makes AI so painful

**[10:47]** to actually build real software with.

**[10:49]** You define the shape of the data you

**[10:51]** want as a plain Python class. You ask

**[10:54]** the model, and Instructor hands you back

**[10:56]** a fully typed, validated object, not a

**[10:58]** blob of text you then have to pray

**[11:00]** parses correctly at 2:00 in the morning.

**[11:02]** And here is the magic. When the model

**[11:04]** gets it slightly wrong, Instructor

**[11:06]** catches the validation error, feeds it

**[11:09]** right back with the specific mistake,

**[11:11]** and asks the model to fix itself,

**[11:13]** automatically retrying until the data

**[11:15]** comes out clean and correct. Pull the

**[11:17]** name, the amount, and the due date off

**[11:20]** an invoice, and you get back a typed

**[11:22]** object with the right fields, or a

**[11:24]** precise error, never a silent mess. It

**[11:27]** is built on Pydantic. It works with

**[11:29]** basically every model, and it now runs

**[11:31]** in Python, TypeScript, Go, and more.

**[11:34]** 13,000 stars, and it turns flaky AI

**[11:37]** output into software you can genuinely

**[11:39]** trust. That is the list that started all

**[11:41]** of this, but I promised you two more.

**[11:44]** These are the two professional-grade

**[11:45]** tools I added myself, and they slot

**[11:48]** straight into the exact same stack.

**[11:50]** Bonus number one, vLLM. Ollama is

**[11:54]** perfect for running a model just for

**[11:55]** yourself, but what happens when you need

**[11:57]** to serve that model to thousands of

**[11:59]** users at once, at full speed, without

**[12:02]** melting your GPU? That is vLLM, born at

**[12:05]** Berkeley, now the industry default

**[12:07]** serving engine. Its secret is a trick

**[12:10]** called paged attention. It manages the

**[12:12]** model memory the way an operating system

**[12:14]** manages RAM, wasting almost none of it.

**[12:17]** The result is up to 24 times the

**[12:19]** throughput of a naive setup from the

**[12:21]** very same graphics card.

**[12:23]** It also does continuous batching,

**[12:25]** slotting new requests in between others

**[12:27]** mid-flight, so the GPU is never left

**[12:30]** sitting there waiting. It serves an

**[12:32]** OpenAI-compatible API. It batches

**[12:35]** incoming requests automatically, and it

**[12:37]** powers a huge share of the world's

**[12:39]** self-hosted AI. 85,000 stars.

**[12:42]** When a company tells you they run their

**[12:44]** own models in production at scale, this

**[12:47]** is very often exactly how they are doing

**[12:49]** it. Bonus number two, RagAs. So, you

**[12:52]** have built your AI, and it gives you an

**[12:54]** answer. Here is the genuinely terrifying

**[12:57]** question. Is that answer correct, or is

**[13:00]** it just confidently making things up?

**[13:02]** RagAs replaces gut feeling with real

**[13:04]** numbers.

**[13:05]** It scores your system on the things you

**[13:07]** simply cannot eyeball at scale. Is the

**[13:10]** answer faithful to the source? Is it

**[13:12]** actually relevant? And did retrieval

**[13:14]** even pull back the right context? And it

**[13:17]** does it using models as the judges, so

**[13:19]** you barely need any hand-labeled data.

**[13:22]** It can even generate a synthetic test

**[13:23]** set straight from your own documents, so

**[13:26]** you have something to measure against on

**[13:27]** day one. That turns a vague it seems

**[13:30]** fine into a dashboard of hard metrics

**[13:32]** you can track on every change and catch

**[13:34]** the moment an innocent update quietly

**[13:36]** makes everything worse. 15,000 stars.

**[13:40]** So, there is the whole stack in one

**[13:42]** picture. Marker and crawl for AI

**[13:44]** together. Chunky to chunk, Qdrant to

**[13:47]** store, a llama and vLLM to run, DSPy,

**[13:52]** outlines, instructor, and LiteLLM to

**[13:55]** build and control it. And LangFuse and

**[13:57]** RagAs to actually trust it. 12 tools,

**[14:00]** every layer, all free. Companies stitch

**[14:03]** these exact projects together and charge

**[14:05]** you thousands of dollars a month for the

**[14:07]** result. Now, you know they are just

**[14:08]** sitting on GitHub waiting. And once you

**[14:11]** have seen them, you honestly cannot

**[14:13]** unsee them. The barrier was never money.

**[14:16]** It was only ever knowing which names to

**[14:18]** type into that search bar.

**[14:20]** If this saved you from a subscription or

**[14:21]** two, do the free thing and subscribe. I

**[14:24]** go deep on open source AI like this

**[14:26]** every week here on Cloud Code. I will

**[14:28]** see you in the next
