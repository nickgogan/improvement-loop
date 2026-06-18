# Transcript: gmaHRwijOXs

**URL:** https://www.youtube.com/watch?v=gmaHRwijOXs
**Segments:** 446

---

## Full Text

These days, the only AI agents that people seem to care about anymore are AI coding assistants. No one seems to cover anymore building agents with LangChain or n8n or Pydantic AI. If you follow mainstream YouTube or LinkedIn, it just seems like these frameworks don't matter anymore. And honestly, I've kind of fallen into this camp myself. I used to cover all the time building agents with Pydantic AI and n8n and the OpenAI agents SDK, building local AI agents. I was all about this, but then my channel has definitely shifted a lot more towards just using AI coding assistants effectively. That's just what is the most relevant right now. And a lot of these coding agents have released SDKs, so we can build our own agents on top of all the power they give us out of the box. And so there's this big narrative right now that we don't need these frameworks anymore. Let's just build everything on top of the Claude agent SDK. And that is actually kind of true for some use cases. For these, everything you thought about building AI agents needs to be thrown out of the window. But then for other use cases, this isn't true at all. So there's a lot of nuance that we have to cover here. If you look at all of the business use cases out there with the billions of agents that are being built, a lot of them, maybe even a majority, are still being built on top of these more classic use cases. But then some are transitioning. It's making more sense to just build them right on top of these SDKs. So I want to cover this nuance with you. When it makes sense to build on top of the SDKs, when it makes sense to use a framework. There are some other important evolutions we have to talk about as well, like relying a lot more on skills now and different ways of performing rag. I want to cover all this and make the decisions very easy for you. All right, so let's start by talking about the old way of building AI agents. A lot of this still applies, but every agent was built this way in 2024 and 2025. So you'd start by picking your framework. All of these are valid. There's honestly way too many options out there, but you just pick the one that you're the most comfortable with or your organization uses. And then you define the tools for your agent, all the capabilities, like searching through a file system, accessing your inbox, that kind of thing. And then from there, this isn't a hard requirement, but most AI agents, especially back then, had some kind of rag. So you define your chunking embedding and retrieval strategy for your agent to search through a knowledge base. And then finally, you would wire up the agent loop, so state and memory management, things like short-term memory, being able to store all your conversations in a database. And of course, I got some examples here to go with everything that I'm talking about in the diagram. So I'll link to this repo in the description. I want to start here with like the most classic rag agent ever. Not that these ideas have gone away, but this is just how we would see almost every single agent defined in 2024 and 2025. So you'd start with your agent definition using a framework like Pydantic AI. You define your model, your system prompt, the tools, like this is a tool to search our knowledge base with rag, cuz rag was in almost every single agent. So you'd have your chunking strategy and your embedding strategy and your ingestion pipeline. There was a lot of code here. And so within our database, like I love using Neon for my Postgres database. I still do for a lot of my agents. We have our documents here and then we have our chunks, a lot of chunks. We'd manage all of our messages and sessions. Everything what for our agent was managed in our own database. This is the way that it was done before all of the time. Now the point I'm trying to make here is a lot of times that is still necessary, but there is a lot of glue code to create the agent infrastructure ourselves. There is a lot of complexity there. And so a lot of people are shifting over to using the batteries included SDKs. So building non-coding agents on top of a coding agent foundation with something like the Claude agent SDK or the Codex SDK. And the beauty of using this as a starting point is there's a ton of prompting and tools that are built into the solution for us already. And they manage the conversation history for us. So we don't even have to store that part in our database. So it just gives us a launching pad. We have support for skills and MCP servers. Those are the newer ways to build tools into our agents as well. And so it's not that you'll use these all of the time. And I'll cover that in just a second here, but it's so much easier to build agents on top of these SDKs versus doing it the old way, building with one of these frameworks. Take a look at how simple and powerful this is. Now I have my entire AI agent using the Claude agent SDK in a single TypeScript file. And instead of defining my own AI agent, I just call right into Claude code and I define all of my options, like the tools that it's allowed to use, so the ones that I want to leverage that are built right into the SDK. Also, I have sub-agents that I have defined here. So we're adding in a lot more than we didn't even have in the other agent, MCP servers. I can build my own custom tools. So instead of defining the tools directly into our agent, we can create them as MCP servers, so they're a lot more reusable. We can do the same thing with skills. I have skills built into this agent as well, so it can generate PowerPoints for me. There's actually more built into this agent and it's less code overall. We don't even need the rag pipeline and everything because for a lot of these Claude agent SDK agents, you're just going to rely on the file search capabilities built right into the SDK. We can have hooks, we can set the permissions, we can build our own system prompt. We have everything that we had before and more. And if I really wanted to use rag still, and we might, I'll talk about that in a little bit as well, we can just include that through skills and MCP servers. So I hope you can see how powerful it is to use these SDKs. It simplifies things so much for us because we're building on top of these tools that are powerful. There's so much attention going to these coding agents for a reason. And this is exactly what I'm using for my second brain. So I'm using the Claude agent SDK for the whole heartbeat system that I built for my own second brain inspired by Open Claw. It handles all my integrations and everything I wanted it to take care of. It builds memories over time. It does daily reflection to basically learn from its work and my requests over time. This entire thing is using the Claude agent SDK, which by the way, if you're interested in learning how I've built my second brain using the Claude agent SDK and Claude code, I'm hosting a 4-hour workshop in my Dynamis community. Friday, April 3rd at 11:00 a.m. Central Time. So if you want [snorts] to save yourself hours and hours every single week building a second brain on top of Claude code, definitely come be a part of the community and join me for this workshop. And building a second brain with the Claude agent SDK is just one of many very powerful use cases. However, there are some big limitations with these batteries included SDKs. This is what's going to lead us into the importance of still building a lot of our agents with these frameworks. So three key limitations that I want to hone in on with you right now. The first one is that these SDKs are significantly slower than what you can build with these frameworks. And the reason for that is there's a lot of reasoning overhead because there's so much built into these SDKs out of the box for you. So the convenience of having all these tools and support for things like sub-agents and skills and the prompting that's already there for you, like all that makes it very easy to work with these tools, but it means that you're coming into building your agent with something that's already a bit bloated. And that also makes it more token heavy. And so these two very much go hand in hand. And then it's also a bit more non-deterministic because there's a lot of things that are managed for you. So it's non-deterministic in the sense that you don't get to define exactly how your agent operates quite as much. When we're building with a framework, we're more building from the ground up. So any kind of use case where speed or cost or utmost flexibility is extremely important, that's when you want to build on top of a framework like Pydantic AI. I'm still using Pydantic AI all of the time. Building with these frameworks is what's going to allow you to build agents with sub-second response times, the most flexibility possible because you're controlling everything, even the conversation history. For a lot of these production agents where you need a lot of observability and control, like being able to store the message history yourself and manage that yourself, you can't be using something like the Claude agent SDK cuz that's just not an option for you. Now besides the obvious speed difference between the frameworks and the SDKs, there's one other big reason why most of the time when you have an agent deployed to production, it's going to use a framework instead of the SDK. And it is all about cost. Like we talked about earlier, these SDKs are very token heavy. So most of the time when you use them, you're going to be using your subscription, like your Anthropic subscription or your OpenAI subscription. But you're only allowed to use your subscription when it is just you interacting with the agent. Otherwise, it is a violation of the terms of service for any of these SDK platforms. And so if you have multiple people using your agent in production, you have to use your API key. You have to pay an obscene amount for API costs. So that's really another limitation for these SDKs here. So that's why I usually use a framework. It's going to be a lot more cost-effective. You can really use it at scale and not worry about burning millions and millions of tokens. And using these frameworks, you still do have the ability to include all these modern techniques like skills and MCP servers. So it might be a bit more work to set it up, but it's still very realistic. And let me show you this with an example, actually. One of the things you might think is missing out of the box for these agent frameworks is support for skills. And so that's the main way to give capabilities to our coding agents now, and we're just starting to see it added into these agent frameworks. And so, what I did, I'll link to a video right here where I covered this more in-depth, is I created a Pydantic AI agent where I added in my own support for skills. So, you have your skills directory here with all your skill.md files. Everything works the exact same as it would in in Claude Code, but now we have our own custom agent where we have full control. It's going to be a lot faster and more token efficient. And so, this setup looks pretty similar to the very first RAG agent example that I gave. We define the model, the system prompt, the tool set here, but the tools are more about loading the skills now. This is the most modern way to add capabilities into our AI agent. So, we have a dynamic system prompt where I basically describe to the agent, "Here are your available skills." And I load it dynamically from the skills directory, and then the rest of the system prompt is just describing to the agent how to leverage these skills. And so, for example, going into the agent right here, I just have a simple CLI. I can say, "What is the weather in New York?" And just like Claude Code, this agent is able to call a tool to load the skill. So, it brings in the skill.md which gives it instructions for how to make the API calls, and then we get the current weather in New York. But, take a look at how fast that was. That would be take at least 10 seconds to get an answer from the Claude Asian SDK just because of how bloated it is. And so, it's very easy to build any capability you need into your own agents, especially with the help of AI coding assistance now. So, sometimes you just want something out of the box, the Claude Asian SDK is great. Other times you need that speed and scalability, and it's not going to be that difficult to use a coding agent to help you build this all yourself. I use Claude Code to help me build this Pydantic AI agent. So, with all that context setting the stage, I now want to cover the super simple decision framework for you. Should you go with an SDK or a framework? So, we'll talk about this, and then I'll get into RAG because that's really the last component that I haven't hit on too much that I said was a part of the old way. It's still relevant, but then also some strategies with existing tools that replace it. We'll talk about that in a second. But, for the decision framework here, it really just comes down to two questions to ask yourself. Who is going to use your agent, and what is your tolerance for things like speed and scale? If it is just you using the agent and some delay is okay, you don't need to scale, then I would highly recommend going with the Claude Asian SDK or Code X SDK. Something out of the box that gives you a ton of power, and you have to worry about less of the infrastructure. But, if a lot of other people are using your agent, you're deploying it to a production platform, it needs to scale and be fast, then you still should go with, you know, the classic way of using a framework like Pydantic AI or LangGraph. And in the end, you do want to just start with the simplest implementation. So, you won't go the other way, but sometimes you'll start with the Claude Asian SDK just to test some tooling through skills or MCP, and then you would transition to a Pydantic AI agent once you need to scale. So, there is a little bit of like you can try with both, but usually this decision is going to make it very obvious for you right when you're starting with your use case. So, I hope this decision framework is helpful for you. The last thing I want to talk about is what happened to RAG? Why are so many coding agents and other agents not using traditional RAG as the default playbook anymore? A lot of people are saying that RAG is dead. want to clarify this for you right now. So, in 2024, no one really questioned RAG. Pretty much every single agent was using semantic search as a way to access external information. But then in 2025, people started to question this because we were relying a lot more on file search. Coding agents especially stopped using vector databases, they're using tools like grep now. That's why we see all of this built directly into the SDKs. For smaller corpuses of knowledge, it was proven last year that file search actually outperforms RAG or classic semantic search. Llama Index did a study, Claude Code, a lot of these coding agents switching away. A lot of that was pointing towards the direction of RAG is dead. But, there's a lot more nuance to this than people realize because for larger knowledge bases with thousands of documents, semantic search is still more accurate and way, way cheaper. And so, now we've kind of gotten to a middle ground this year with agentic RAG. We give our agent the ability to perform both semantic search and other kinds of searches like grep and keyword search. Graph RAG is really popular as well, especially especially for massive codebases or projects with many different codebases. So, at an enterprise level, RAG is still used for AI coding. And then for most AI agents, we still need RAG to access our knowledge bases. File search is not enough. It's a good starting point, and it works better for smaller knowledge bases, but you still need that for a lot of your agents. For a lot of my AI agents, I'm still spending a good amount of time in my database trying different RAG strategies, building around semantic search. Even with the Claude Asian SDK, building semantic search through skills and MCP servers. And Second Brains are a good demonstration of this. I've built mine on top of the Claude Asian SDK, but I use both of the capabilities built right in, and then also I have my own RAG setup that's actually inspired by OpenClaude, also built in for semantic search. So, to summarize everything here, match your tool for your use case. There are a million use cases that are great for the SDKs, and just as many if not more where you want to use a framework and build it more from the ground up. And I hope this decision framework has made it really easy for you to think about that for your own AI agents. And so, if you found this helpful, and you're looking forward to more things on building AI agents and agentic coding, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.

---

## Timestamped Segments

**[0:00]** These days, the only AI agents that

**[0:01]** people seem to care about anymore are AI

**[0:04]** coding assistants. No one seems to cover

**[0:06]** anymore building agents with LangChain

**[0:08]** or n8n or Pydantic AI. If you follow

**[0:11]** mainstream YouTube or LinkedIn, it just

**[0:13]** seems like these frameworks don't matter

**[0:15]** anymore. And honestly, I've kind of

**[0:18]** fallen into this camp myself. I used to

**[0:19]** cover all the time building agents with

**[0:22]** Pydantic AI and n8n and the OpenAI

**[0:25]** agents SDK, building local AI agents. I

**[0:28]** was all about this, but then my channel

**[0:30]** has definitely shifted a lot more

**[0:32]** towards just using AI coding assistants

**[0:34]** effectively. That's just what is the

**[0:36]** most relevant right now. And a lot of

**[0:38]** these coding agents have released SDKs,

**[0:40]** so we can build our own agents on top of

**[0:43]** all the power they give us out of the

**[0:44]** box. And so there's this big narrative

**[0:47]** right now that we don't need these

**[0:48]** frameworks anymore. Let's just build

**[0:49]** everything on top of the Claude agent

**[0:52]** SDK. And that is actually kind of true

**[0:54]** for some use cases. For these,

**[0:57]** everything you thought about building AI

**[0:58]** agents needs to be thrown out of the

**[1:00]** window. But then for other use cases,

**[1:02]** this isn't true at all. So there's a lot

**[1:05]** of nuance that we have to cover here. If

**[1:07]** you look at all of the business use

**[1:09]** cases out there with the billions of

**[1:10]** agents that are being built, a lot of

**[1:12]** them, maybe even a majority, are still

**[1:14]** being built on top of these more classic

**[1:16]** use cases. But then some are

**[1:19]** transitioning. It's making more sense to

**[1:20]** just build them right on top of these

**[1:22]** SDKs. So I want to cover this nuance

**[1:25]** with you. When it makes sense to build

**[1:26]** on top of the SDKs, when it makes sense

**[1:28]** to use a framework. There are some other

**[1:30]** important evolutions we have to talk

**[1:31]** about as well, like relying a lot more

**[1:34]** on skills now and different ways of

**[1:36]** performing rag. I want to cover all this

**[1:38]** and make the decisions very easy for

**[1:40]** you. All right, so let's start by

**[1:42]** talking about the old way of building AI

**[1:44]** agents. A lot of this still applies, but

**[1:47]** every agent was built this way in 2024

**[1:50]** and 2025. So you'd start by picking your

**[1:53]** framework. All of these are valid.

**[1:56]** There's honestly way too many options

**[1:57]** out there, but you just pick the one

**[1:59]** that you're the most comfortable with or

**[2:00]** your organization uses. And then you

**[2:02]** define the tools for your agent, all the

**[2:04]** capabilities, like searching through a

**[2:06]** file system, accessing your inbox, that

**[2:08]** kind of thing. And then from there, this

**[2:10]** isn't a hard requirement, but most AI

**[2:13]** agents, especially back then, had some

**[2:15]** kind of rag. So you define your chunking

**[2:17]** embedding and retrieval strategy for

**[2:19]** your agent to search through a knowledge

**[2:21]** base. And then finally, you would wire

**[2:23]** up the agent loop, so state and memory

**[2:26]** management, things like short-term

**[2:27]** memory, being able to store all your

**[2:28]** conversations in a database. And of

**[2:31]** course, I got some examples here to go

**[2:32]** with everything that I'm talking about

**[2:34]** in the diagram. So I'll link to this

**[2:35]** repo in the description. I want to start

**[2:37]** here with like the most classic rag

**[2:40]** agent ever. Not that these ideas have

**[2:43]** gone away, but this is just how we would

**[2:44]** see almost every single agent defined in

**[2:47]** 2024 and 2025. So you'd start with your

**[2:50]** agent definition using a framework like

**[2:52]** Pydantic AI. You define your model, your

**[2:54]** system prompt, the tools, like this is a

**[2:56]** tool to search our knowledge base with

**[2:58]** rag, cuz rag was in almost every single

**[3:01]** agent. So you'd have your chunking

**[3:03]** strategy and your embedding strategy and

**[3:05]** your ingestion pipeline. There was a lot

**[3:07]** of code here. And so within our

**[3:09]** database, like I love using Neon for my

**[3:12]** Postgres database. I still do for a lot

**[3:14]** of my agents. We have our documents here

**[3:16]** and then we have our chunks, a lot of

**[3:19]** chunks. We'd manage all of our messages

**[3:21]** and sessions. Everything what for our

**[3:23]** agent was managed in our own database.

**[3:26]** This is the way that it was done before

**[3:27]** all of the time. Now the point I'm

**[3:29]** trying to make here is a lot of times

**[3:31]** that is still necessary, but there is a

**[3:33]** lot of glue code to create the agent

**[3:36]** infrastructure ourselves. There is a lot

**[3:39]** of complexity there. And so a lot of

**[3:40]** people are shifting over to using the

**[3:43]** batteries included SDKs. So building

**[3:45]** non-coding agents on top of a coding

**[3:48]** agent foundation with something like the

**[3:50]** Claude agent SDK or the Codex SDK. And

**[3:54]** the beauty of using this as a starting

**[3:56]** point is there's a ton of prompting and

**[3:59]** tools that are built into the solution

**[4:01]** for us already. And they manage the

**[4:04]** conversation history for us. So we don't

**[4:06]** even have to store that part in our

**[4:08]** database. So it just gives us a

**[4:09]** launching pad. We have support for

**[4:11]** skills and MCP servers. Those are the

**[4:14]** newer ways to build tools into our

**[4:15]** agents as well. And so it's not that

**[4:18]** you'll use these all of the time. And

**[4:21]** I'll cover that in just a second here,

**[4:22]** but it's so much easier to build agents

**[4:25]** on top of these SDKs versus doing it the

**[4:28]** old way, building with one of these

**[4:30]** frameworks. Take a look at how simple

**[4:32]** and powerful this is. Now I have my

**[4:34]** entire AI agent using the Claude agent

**[4:36]** SDK in a single TypeScript file. And

**[4:39]** instead of defining my own AI agent, I

**[4:41]** just call right into Claude code and I

**[4:44]** define all of my options, like the tools

**[4:46]** that it's allowed to use, so the ones

**[4:48]** that I want to leverage that are built

**[4:49]** right into the SDK. Also, I have

**[4:51]** sub-agents that I have defined here. So

**[4:54]** we're adding in a lot more than we

**[4:55]** didn't even have in the other agent, MCP

**[4:58]** servers. I can build my own custom

**[5:00]** tools. So instead of defining the tools

**[5:02]** directly into our agent, we can create

**[5:04]** them as MCP servers, so they're a lot

**[5:05]** more reusable. We can do the same thing

**[5:07]** with skills. I have skills built into

**[5:10]** this agent as well, so it can generate

**[5:11]** PowerPoints for me. There's actually

**[5:13]** more built into this agent and it's less

**[5:16]** code overall. We don't even need the rag

**[5:19]** pipeline and everything because for a

**[5:20]** lot of these Claude agent SDK agents,

**[5:23]** you're just going to rely on the file

**[5:25]** search capabilities built right into the

**[5:27]** SDK. We can have hooks, we can set the

**[5:30]** permissions, we can build our own system

**[5:32]** prompt. We have everything that we had

**[5:34]** before and more. And if I really wanted

**[5:37]** to use rag still, and we might, I'll

**[5:39]** talk about that in a little bit as well,

**[5:41]** we can just include that through skills

**[5:43]** and MCP servers. So I hope you can see

**[5:46]** how powerful it is to use these SDKs. It

**[5:49]** simplifies things so much for us because

**[5:51]** we're building on top of these tools

**[5:53]** that are powerful. There's so much

**[5:55]** attention going to these coding agents

**[5:57]** for a reason. And this is exactly what

**[5:59]** I'm using for my second brain. So I'm

**[6:01]** using the Claude agent SDK for the whole

**[6:04]** heartbeat system that I built for my own

**[6:06]** second brain inspired by Open Claw. It

**[6:08]** handles all my integrations and

**[6:10]** everything I wanted it to take care of.

**[6:11]** It builds memories over time. It does

**[6:13]** daily reflection to basically learn from

**[6:16]** its work and my requests over time. This

**[6:19]** entire thing is using the Claude agent

**[6:22]** SDK, which by the way, if you're

**[6:23]** interested in learning how I've built my

**[6:25]** second brain using the Claude agent SDK

**[6:28]** and Claude code, I'm hosting a 4-hour

**[6:30]** workshop in my Dynamis community.

**[6:32]** Friday, April 3rd at 11:00 a.m. Central

**[6:35]** Time. So if you want [snorts] to save

**[6:37]** yourself hours and hours every single

**[6:39]** week building a second brain on top of

**[6:41]** Claude code, definitely come be a part

**[6:43]** of the community and join me for this

**[6:45]** workshop. And building a second brain

**[6:47]** with the Claude agent SDK is just one of

**[6:49]** many very powerful use cases. However,

**[6:53]** there are some big limitations with

**[6:55]** these batteries included SDKs. This is

**[6:58]** what's going to lead us into the

**[6:59]** importance of still building a lot of

**[7:01]** our agents with these frameworks. So

**[7:03]** three key limitations that I want to

**[7:05]** hone in on with you right now. The first

**[7:08]** one is that these SDKs are significantly

**[7:12]** slower than what you can build with

**[7:14]** these frameworks. And the reason for

**[7:16]** that is there's a lot of reasoning

**[7:18]** overhead because there's so much built

**[7:20]** into these SDKs out of the box for you.

**[7:22]** So the convenience of having all these

**[7:24]** tools and support for things like

**[7:25]** sub-agents and skills and the prompting

**[7:28]** that's already there for you, like all

**[7:29]** that makes it very easy to work with

**[7:31]** these tools, but it means that you're

**[7:33]** coming into building your agent with

**[7:35]** something that's already a bit bloated.

**[7:37]** And that also makes it more token heavy.

**[7:39]** And so these two very much go hand in

**[7:42]** hand. And then it's also a bit more

**[7:44]** non-deterministic because there's a lot

**[7:46]** of things that are managed for you. So

**[7:48]** it's non-deterministic in the sense that

**[7:50]** you don't get to define exactly how your

**[7:52]** agent operates quite as much. When we're

**[7:54]** building with a framework, we're more

**[7:56]** building from the ground up. So any kind

**[7:59]** of use case where speed or cost or

**[8:01]** utmost flexibility is extremely

**[8:03]** important, that's when you want to build

**[8:05]** on top of a framework like Pydantic AI.

**[8:07]** I'm still using Pydantic AI all of the

**[8:09]** time. Building with these frameworks is

**[8:11]** what's going to allow you to build

**[8:13]** agents with sub-second response times,

**[8:15]** the most flexibility possible because

**[8:17]** you're controlling everything, even the

**[8:19]** conversation history. For a lot of these

**[8:21]** production agents where you need a lot

**[8:23]** of observability and control, like being

**[8:25]** able to store the message history

**[8:27]** yourself and manage that yourself, you

**[8:29]** can't be using something like the Claude

**[8:31]** agent SDK cuz that's just not an option

**[8:33]** for you. Now besides the obvious speed

**[8:36]** difference between the frameworks and

**[8:37]** the SDKs, there's one other big reason

**[8:40]** why most of the time when you have an

**[8:42]** agent deployed to production, it's going

**[8:44]** to use a framework instead of the SDK.

**[8:46]** And it is all about cost. Like we talked

**[8:49]** about earlier, these SDKs are very token

**[8:51]** heavy. So most of the time when you use

**[8:53]** them, you're going to be using your

**[8:55]** subscription, like your Anthropic

**[8:57]** subscription or your OpenAI

**[8:59]** subscription. But you're only allowed to

**[9:01]** use your subscription when it is just

**[9:03]** you interacting with the agent.

**[9:05]** Otherwise, it is a violation of the

**[9:07]** terms of service for any of these SDK

**[9:10]** platforms. And so if you have multiple

**[9:13]** people using your agent in production,

**[9:15]** you have to use your API key. You have

**[9:17]** to pay an obscene amount for API costs.

**[9:20]** So that's really another limitation for

**[9:23]** these SDKs here. So that's why I usually

**[9:25]** use a framework. It's going to be a lot

**[9:26]** more cost-effective. You can really use

**[9:29]** it at scale and not worry about burning

**[9:31]** millions and millions of tokens. And

**[9:34]** using these frameworks, you still do

**[9:36]** have the ability to include all these

**[9:38]** modern techniques like skills and MCP

**[9:40]** servers. So it might be a bit more work

**[9:42]** to set it up, but it's still very

**[9:44]** realistic. And let me show you this with

**[9:46]** an example, actually. One of the things

**[9:48]** you might think is missing out of the

**[9:49]** box for these agent frameworks is

**[9:51]** support for skills. And so that's the

**[9:54]** main way to give capabilities to our

**[9:56]** coding agents now, and we're just

**[9:58]** starting to see it added into these

**[10:00]** agent frameworks. And so, what I did,

**[10:02]** I'll link to a video right here where I

**[10:03]** covered this more in-depth, is I created

**[10:05]** a Pydantic AI agent where I added in my

**[10:08]** own support for skills. So, you have

**[10:10]** your skills directory here with all your

**[10:12]** skill.md files. Everything works the

**[10:14]** exact same as it would in in Claude

**[10:16]** Code, but now we have our own custom

**[10:18]** agent where we have full control. It's

**[10:20]** going to be a lot faster and more token

**[10:22]** efficient. And so, this setup looks

**[10:24]** pretty similar to the very first RAG

**[10:26]** agent example that I gave. We define the

**[10:28]** model, the system prompt, the tool set

**[10:30]** here, but the tools are more about

**[10:32]** loading the skills now. This is the most

**[10:34]** modern way to add capabilities into our

**[10:37]** AI agent. So, we have a dynamic system

**[10:39]** prompt where I basically describe to the

**[10:41]** agent, "Here are your available skills."

**[10:43]** And I load it dynamically from the

**[10:45]** skills directory, and then the rest of

**[10:47]** the system prompt is just describing to

**[10:48]** the agent how to leverage these skills.

**[10:50]** And so, for example, going into the

**[10:52]** agent right here, I just have a simple

**[10:53]** CLI. I can say, "What is the weather in

**[10:56]** New York?"

**[10:57]** And just like Claude Code, this agent is

**[11:00]** able to call a tool to load the skill.

**[11:03]** So, it brings in the skill.md which

**[11:04]** gives it instructions for how to make

**[11:06]** the API calls, and then we get the

**[11:08]** current weather in New York. But, take a

**[11:10]** look at how fast that was. That would be

**[11:12]** take at least 10 seconds to get an

**[11:14]** answer from the Claude Asian SDK just

**[11:16]** because of how bloated it is. And so,

**[11:18]** it's very easy to build any capability

**[11:21]** you need into your own agents,

**[11:23]** especially with the help of AI coding

**[11:25]** assistance now. So, sometimes you just

**[11:27]** want something out of the box, the

**[11:28]** Claude Asian SDK is great. Other times

**[11:30]** you need that speed and scalability, and

**[11:32]** it's not going to be that difficult to

**[11:34]** use a coding agent to help you build

**[11:36]** this all yourself. I use Claude Code to

**[11:38]** help me build this Pydantic AI agent.

**[11:41]** So, with all that context setting the

**[11:42]** stage, I now want to cover the super

**[11:44]** simple decision framework for you.

**[11:46]** Should you go with an SDK or a

**[11:48]** framework? So, we'll talk about this,

**[11:50]** and then I'll get into RAG because

**[11:51]** that's really the last component that I

**[11:53]** haven't hit on too much that I said was

**[11:55]** a part of the old way. It's still

**[11:56]** relevant, but then also some strategies

**[11:59]** with existing tools that replace it.

**[12:00]** We'll talk about that in a second. But,

**[12:02]** for the decision framework here, it

**[12:04]** really just comes down to two questions

**[12:06]** to ask yourself. Who is going to use

**[12:08]** your agent, and what is your tolerance

**[12:10]** for things like speed and scale? If it

**[12:13]** is just you using the agent and some

**[12:15]** delay is okay, you don't need to scale,

**[12:18]** then I would highly recommend going with

**[12:20]** the Claude Asian SDK or Code X SDK.

**[12:23]** Something out of the box that gives you

**[12:24]** a ton of power, and you have to worry

**[12:26]** about less of the infrastructure. But,

**[12:29]** if a lot of other people are using your

**[12:31]** agent, you're deploying it to a

**[12:32]** production platform, it needs to scale

**[12:34]** and be fast, then you still should go

**[12:36]** with, you know, the classic way of using

**[12:38]** a framework like Pydantic AI or

**[12:41]** LangGraph. And in the end, you do want

**[12:42]** to just start with the simplest

**[12:44]** implementation. So, you won't go the

**[12:45]** other way, but sometimes you'll start

**[12:47]** with the Claude Asian SDK just to test

**[12:49]** some tooling through skills or MCP, and

**[12:52]** then you would transition to a Pydantic

**[12:54]** AI agent once you need to scale. So,

**[12:56]** there is a little bit of like you can

**[12:58]** try with both, but usually this decision

**[13:01]** is going to make it very obvious for you

**[13:03]** right when you're starting with your use

**[13:05]** case. So, I hope this decision framework

**[13:07]** is helpful for you. The last thing I

**[13:09]** want to talk about is what happened to

**[13:11]** RAG? Why are so many coding agents and

**[13:14]** other agents not using traditional RAG

**[13:16]** as the default playbook anymore? A lot

**[13:19]** of people are saying that RAG is dead.

**[13:21]** want to clarify this for you right now.

**[13:23]** So, in 2024, no one really questioned

**[13:26]** RAG. Pretty much every single agent was

**[13:28]** using semantic search as a way to access

**[13:31]** external information. But then in 2025,

**[13:34]** people started to question this because

**[13:36]** we were relying a lot more on file

**[13:38]** search. Coding agents especially stopped

**[13:41]** using vector databases, they're using

**[13:43]** tools like grep now. That's why we see

**[13:45]** all of this built directly into the

**[13:47]** SDKs. For smaller corpuses of knowledge,

**[13:51]** it was proven last year that file search

**[13:54]** actually outperforms RAG or classic

**[13:56]** semantic search. Llama Index did a

**[13:58]** study, Claude Code, a lot of these

**[13:59]** coding agents switching away. A lot of

**[14:01]** that was pointing towards the direction

**[14:03]** of RAG is dead. But, there's a lot more

**[14:05]** nuance to this than people realize

**[14:07]** because for larger knowledge bases with

**[14:10]** thousands of documents, semantic search

**[14:12]** is still more accurate and way, way

**[14:15]** cheaper. And so, now we've kind of

**[14:17]** gotten to a middle ground this year with

**[14:19]** agentic RAG. We give our agent the

**[14:20]** ability to perform both semantic search

**[14:23]** and other kinds of searches like grep

**[14:25]** and keyword search. Graph RAG is really

**[14:28]** popular as well, especially especially

**[14:30]** for massive codebases or projects with

**[14:32]** many different codebases. So, at an

**[14:34]** enterprise level,

**[14:35]** RAG is still used for AI coding. And

**[14:37]** then for most AI agents, we still need

**[14:40]** RAG to access our knowledge bases. File

**[14:42]** search is not enough. It's a good

**[14:44]** starting point, and it works better for

**[14:47]** smaller knowledge bases, but you still

**[14:49]** need that for a lot of your agents. For

**[14:52]** a lot of my AI agents, I'm still

**[14:54]** spending a good amount of time in my

**[14:55]** database trying different RAG

**[14:57]** strategies, building around semantic

**[14:59]** search. Even with the Claude Asian SDK,

**[15:02]** building semantic search through skills

**[15:03]** and MCP servers. And Second Brains are a

**[15:06]** good demonstration of this. I've built

**[15:08]** mine on top of the Claude Asian SDK, but

**[15:11]** I use both of the capabilities built

**[15:13]** right in, and then also I have my own

**[15:16]** RAG setup that's actually inspired by

**[15:18]** OpenClaude, also built in for semantic

**[15:20]** search. So, to summarize everything

**[15:22]** here, match your tool for your use case.

**[15:25]** There are a million use cases that are

**[15:27]** great for the SDKs, and just as many if

**[15:30]** not more where you want to use a

**[15:32]** framework and build it more from the

**[15:33]** ground up. And I hope this decision

**[15:35]** framework has made it really easy for

**[15:37]** you to think about that for your own AI

**[15:39]** agents. And so, if you found this

**[15:41]** helpful, and you're looking forward to

**[15:43]** more things on building AI agents and

**[15:45]** agentic coding, I would really

**[15:47]** appreciate a like and a subscribe. And

**[15:49]** with that, I will see you in the next

**[15:50]** video.
