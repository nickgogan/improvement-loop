# Transcript: szaszUEmjfU

**URL:** https://www.youtube.com/watch?v=szaszUEmjfU
**Segments:** 224

---

## Full Text

Look at this graph. It's the fastest repo in GitHub's entire history to hit that milestone. 100,000 stars in just few hours. And this isn't a new framework or a product launch. It's a reconstruction of Anthropic's internal tool that was never supposed to be public. So what's inside that made 150,000 engineer plus to stop and pay attention? And that's what we are breaking down today. How cloud code actually works under the hood and what you as an engineer can learn from it. Let's get started. Anthropic accidentally exposed a large chunk of cloud source code. Not a hack, a deployment mistake. Now, cloud code is Anthropic's own AI coding agent written in TypeScript. And here is roughly what happened. When you deploy a NodeJS application, the source TypeScript gets compiled down to JavaScript and bundled. That bundle gets shipped to wherever it runs. In this case, Anthropic was running cloud codes as a CLI tool that users install on their machines. And at some point, the bundle that ended up on user machines still contain the original TypeScript source maps. Source maps are files that map the compiled JavaScript back to the original source code. And they exist to make debugging easier in development. They should never shift to production, but they did. So, anyone who looked inside their cloud code installation directory found not just the compile JavaScript but the full original TypeScript source CLI. MJS sitting right there. No reverse engineering needed, no decompilation. Just open the folder and within hours someone had gone through it and started rebuilding the core architecture from scratch in Python. not copying it line by line, reading it, understanding the patterns, and reimplementing the same ideas cleanly. That distinction matters legally. A clean room rewrite means you study how something works and rebuild it independently. You don't copy the original code. The Python version came together fast because the architecture is not that complicated once you see it laid out. A loop, a tool registry, a memory system, a few hundred lines of Python gets you a working skeleton. Then that Python version got ported to Rust. Rust for performance, memory safety, and because shipping a single compiled library is much cleaner than distributing a Python script with dependencies. The Rust port is where most of the active development is happening. Now, that whole sequence from exposure to working Rust implementation happened in roughly 24 hours, driven mostly by engineers using EI tools to accelerate the porting work. So, let's look at what they actually found inside. You give the agent a task. The agent receives it and instead of replying once, it starts a loop. At each step of that loop, it calls a tool. Every tool call passes through a checkpoint called hooks. First tools are how it actually does things. Read a file, run a shell command, search the web, the result comes back through hooks again and goes to the agent. Everything gets written to memory. So the agent stays oriented across the long task. And if the task is big enough, the agent spins out sub aents to handle pieces of it in parallel. Before any of this starts, the agent loads context. Your project conventions, your preferences, reusable skill sets, all loaded before the first loop runs. All of that together is cloud code. Your reasoning loop, a tool layer, memory, sub aents, and context loading. Now, let's take each piece apart. Everything starts with the loop. You give it a task. Instead of calling the AI model once and returning an answer, it keeps going. Here is roughly what that tool looks in code. The model decides what to do. A tool runs, the result come back, the model looks at it and decides the next step. This keeps going until the task is finished. It's the same pattern you'd use in any automated workflow. The difference is the model is making the decisions at each step instead of hard coding logic. Now the question is what tools does the model actually have access to? The original TypeScript source has over 20 tools. Reading files, writing files, running shell commands, searching the web, pattern matching across a codebase. Each tool has a simple description so the model knows when to use it. The model reads that description, decides it needs to run a command, and calls a bash tool with the right input. The important design decision here is separation. The model handles the thinking. The tool layer handles the doing. The model never directly touches your file system or runs commands itself. It makes a request. The tool executes it. The results come back. But there is more to the tool layer than just running commands. There's a checkpoint on every single tool call. And that checkpoint is called hooks. Before any tool runs, you can intercept it, inspect what the agent is about to do, modify the input or block it entirely. And same thing after the tool runs, you can inspect the result before it goes back to the model. Think of it like a middleware in a web framework. Every request passes through it. And this is how you build safety and observability into an agent. You want to know every tool call that happens. You want to be able to catch a dangerous command before it executes. Hooks are the mechanism for that. Now once you have tools and hooks, the next challenge is memory because these tasks can run for a long time. The agent needs to remember what it has done during a session. But conversations get long. The model has a limited memory window. You can't keep adding to it forever. So there is compaction step. When the history gets too long, the system summarizes what's already happened and replaces the full history with that summary. The agent keeps a compressed version and keeps working. It's the same idea as compressing old logs. Simple but essential for any agent working on tasks that span hundreds of steps. And beyond session memory, the agent also loads two things before it even starts. The first is cloud MD. Before the agent starts working on your project, it reads a file called cloud MD from your repo. Think of it as the onboarding dog for the agent. your project conventions, your preferences, what folders to avoid, how you like test written, the agent reads that first and uses it throughout the whole session. The second is skills. These are reusable instruction sets for specific task, how to do a code review, how to write documentation, prepackaged behaviors the agent can pull in when needed. The original TypeScript source has a whole registry of these bundled in. The Rust port reads them from your local skill MD files in your project directory. So the agent knows your project from CloudMD, knows how to handle specific tasks through skills and can run any tool it needs through the tool registry. But there is one more capability that changes the picture entirely. The agent can spawn other agents. When a task is too complex to handle in a single thread of work, the main agent breaks it into pieces and delegates each piece to a sub agent. Each sub agent runs its own loop focused on one specific thing. Code review, test generation, security scanning, they do their work and report back when done. What's elegant about this is that spawning a sub agent is just another tool in the registry called agent tool. The orchestrator calls it exactly the same way it calls the bash tool or the file reader. The system stays consistent all the way through. This is just a distributed system. An orchestrator figures out what needs to happen. Workers handle the individual pieces. Coordination happens through a clean interface. Every design decision in here is something you have seen before in other context. The agent loop is a worker processing a task Q. Tools are a service interface layer. Hooks are middleware. Memory compaction is like log rotation. Sub aents are like working nodes in NodeJS. And cloud MD is just configuration. None of this is magic. Understanding how an agent loops work, how tools are wired up, how memory gets managed, how sub agents coordinate. That's the new distributed system literacy. And the engineers who get comfortable with these patterns now are going to be the ones designing what comes next. Do let me know in the comments. Maybe in a future video we build a minimal agent loop from scratch and wire up a basic tool so you can see exactly how this fits together in real code. Do subscribe if you found this video useful.

---

## Timestamped Segments

**[0:00]** Look at this graph. It's the fastest

**[0:02]** repo in GitHub's entire history to hit

**[0:04]** that milestone. 100,000 stars in just

**[0:07]** few hours. And this isn't a new

**[0:09]** framework or a product launch. It's a

**[0:11]** reconstruction of Anthropic's internal

**[0:13]** tool that was never supposed to be

**[0:15]** public. So what's inside that made

**[0:17]** 150,000 engineer plus to stop and pay

**[0:20]** attention? And that's what we are

**[0:22]** breaking down today. How cloud code

**[0:24]** actually works under the hood and what

**[0:26]** you as an engineer can learn from it.

**[0:28]** Let's get started.

**[0:35]** Anthropic accidentally exposed a large

**[0:37]** chunk of cloud source code. Not a hack,

**[0:40]** a deployment mistake. Now, cloud code is

**[0:43]** Anthropic's own AI coding agent written

**[0:46]** in TypeScript. And here is roughly what

**[0:48]** happened. When you deploy a NodeJS

**[0:50]** application, the source TypeScript gets

**[0:52]** compiled down to JavaScript and bundled.

**[0:55]** That bundle gets shipped to wherever it

**[0:57]** runs. In this case, Anthropic was

**[1:00]** running cloud codes as a CLI tool that

**[1:02]** users install on their machines. And at

**[1:05]** some point, the bundle that ended up on

**[1:07]** user machines still contain the original

**[1:09]** TypeScript source maps. Source maps are

**[1:12]** files that map the compiled JavaScript

**[1:14]** back to the original source code. And

**[1:17]** they exist to make debugging easier in

**[1:18]** development. They should never shift to

**[1:21]** production, but they did. So, anyone who

**[1:24]** looked inside their cloud code

**[1:25]** installation directory found not just

**[1:27]** the compile JavaScript but the full

**[1:29]** original TypeScript source CLI. MJS

**[1:32]** sitting right there. No reverse

**[1:34]** engineering needed, no decompilation.

**[1:37]** Just open the folder and within hours

**[1:40]** someone had gone through it and started

**[1:42]** rebuilding the core architecture from

**[1:44]** scratch in Python. not copying it line

**[1:47]** by line, reading it, understanding the

**[1:50]** patterns, and reimplementing the same

**[1:52]** ideas cleanly. That distinction matters

**[1:54]** legally. A clean room rewrite means you

**[1:57]** study how something works and rebuild it

**[1:59]** independently. You don't copy the

**[2:01]** original code. The Python version came

**[2:03]** together fast because the architecture

**[2:05]** is not that complicated once you see it

**[2:07]** laid out. A loop, a tool registry, a

**[2:10]** memory system, a few hundred lines of

**[2:12]** Python gets you a working skeleton. Then

**[2:14]** that Python version got ported to Rust.

**[2:17]** Rust for performance, memory safety, and

**[2:20]** because shipping a single compiled

**[2:21]** library is much cleaner than

**[2:23]** distributing a Python script with

**[2:24]** dependencies. The Rust port is where

**[2:27]** most of the active development is

**[2:29]** happening. Now, that whole sequence from

**[2:31]** exposure to working Rust implementation

**[2:34]** happened in roughly 24 hours, driven

**[2:36]** mostly by engineers using EI tools to

**[2:39]** accelerate the porting work. So, let's

**[2:41]** look at what they actually found inside.

**[2:43]** You give the agent a task. The agent

**[2:46]** receives it and instead of replying

**[2:48]** once, it starts a loop. At each step of

**[2:51]** that loop, it calls a tool. Every tool

**[2:53]** call passes through a checkpoint called

**[2:55]** hooks. First tools are how it actually

**[2:58]** does things. Read a file, run a shell

**[3:00]** command, search the web, the result

**[3:02]** comes back through hooks again and goes

**[3:04]** to the agent. Everything gets written to

**[3:06]** memory. So the agent stays oriented

**[3:08]** across the long task. And if the task is

**[3:11]** big enough, the agent spins out sub

**[3:13]** aents to handle pieces of it in

**[3:15]** parallel. Before any of this starts, the

**[3:17]** agent loads context. Your project

**[3:20]** conventions, your preferences, reusable

**[3:22]** skill sets, all loaded before the first

**[3:24]** loop runs. All of that together is cloud

**[3:27]** code. Your reasoning loop, a tool layer,

**[3:30]** memory, sub aents, and context loading.

**[3:33]** Now, let's take each piece apart.

**[3:35]** Everything starts with the loop. You

**[3:37]** give it a task. Instead of calling the

**[3:39]** AI model once and returning an answer,

**[3:42]** it keeps going. Here is roughly what

**[3:44]** that tool looks in code. The model

**[3:46]** decides what to do. A tool runs, the

**[3:49]** result come back, the model looks at it

**[3:51]** and decides the next step. This keeps

**[3:54]** going until the task is finished. It's

**[3:56]** the same pattern you'd use in any

**[3:58]** automated workflow. The difference is

**[4:00]** the model is making the decisions at

**[4:02]** each step instead of hard coding logic.

**[4:05]** Now the question is what tools does the

**[4:07]** model actually have access to? The

**[4:09]** original TypeScript source has over 20

**[4:11]** tools. Reading files, writing files,

**[4:14]** running shell commands, searching the

**[4:16]** web, pattern matching across a codebase.

**[4:19]** Each tool has a simple description so

**[4:21]** the model knows when to use it. The

**[4:24]** model reads that description, decides it

**[4:26]** needs to run a command, and calls a bash

**[4:28]** tool with the right input. The important

**[4:31]** design decision here is separation. The

**[4:33]** model handles the thinking. The tool

**[4:35]** layer handles the doing. The model never

**[4:38]** directly touches your file system or

**[4:39]** runs commands itself. It makes a

**[4:42]** request. The tool executes it. The

**[4:44]** results come back. But there is more to

**[4:47]** the tool layer than just running

**[4:48]** commands. There's a checkpoint on every

**[4:51]** single tool call. And that checkpoint is

**[4:53]** called hooks. Before any tool runs, you

**[4:56]** can intercept it, inspect what the agent

**[4:59]** is about to do, modify the input or

**[5:02]** block it entirely. And same thing after

**[5:04]** the tool runs, you can inspect the

**[5:06]** result before it goes back to the model.

**[5:08]** Think of it like a middleware in a web

**[5:10]** framework. Every request passes through

**[5:12]** it. And this is how you build safety and

**[5:15]** observability into an agent. You want to

**[5:18]** know every tool call that happens. You

**[5:20]** want to be able to catch a dangerous

**[5:21]** command before it executes. Hooks are

**[5:24]** the mechanism for that. Now once you

**[5:27]** have tools and hooks, the next challenge

**[5:29]** is memory because these tasks can run

**[5:31]** for a long time. The agent needs to

**[5:34]** remember what it has done during a

**[5:35]** session. But conversations get long. The

**[5:38]** model has a limited memory window. You

**[5:40]** can't keep adding to it forever. So

**[5:42]** there is compaction step. When the

**[5:44]** history gets too long, the system

**[5:46]** summarizes what's already happened and

**[5:48]** replaces the full history with that

**[5:50]** summary. The agent keeps a compressed

**[5:53]** version and keeps working. It's the same

**[5:55]** idea as compressing old logs. Simple but

**[5:58]** essential for any agent working on tasks

**[6:00]** that span hundreds of steps. And beyond

**[6:03]** session memory, the agent also loads two

**[6:06]** things before it even starts. The first

**[6:08]** is cloud MD. Before the agent starts

**[6:11]** working on your project, it reads a file

**[6:13]** called cloud MD from your repo. Think of

**[6:15]** it as the onboarding dog for the agent.

**[6:18]** your project conventions, your

**[6:19]** preferences, what folders to avoid, how

**[6:21]** you like test written, the agent reads

**[6:24]** that first and uses it throughout the

**[6:26]** whole session.

**[6:28]** The second is skills. These are reusable

**[6:30]** instruction sets for specific task, how

**[6:33]** to do a code review, how to write

**[6:35]** documentation,

**[6:37]** prepackaged behaviors the agent can pull

**[6:39]** in when needed. The original TypeScript

**[6:41]** source has a whole registry of these

**[6:43]** bundled in. The Rust port reads them

**[6:45]** from your local skill MD files in your

**[6:47]** project directory. So the agent knows

**[6:49]** your project from CloudMD, knows how to

**[6:52]** handle specific tasks through skills and

**[6:54]** can run any tool it needs through the

**[6:56]** tool registry. But there is one more

**[6:58]** capability that changes the picture

**[7:00]** entirely. The agent can spawn other

**[7:03]** agents. When a task is too complex to

**[7:05]** handle in a single thread of work, the

**[7:08]** main agent breaks it into pieces and

**[7:10]** delegates each piece to a sub agent.

**[7:13]** Each sub agent runs its own loop focused

**[7:15]** on one specific thing. Code review, test

**[7:18]** generation, security scanning, they do

**[7:21]** their work and report back when done.

**[7:23]** What's elegant about this is that

**[7:25]** spawning a sub agent is just another

**[7:27]** tool in the registry called agent tool.

**[7:30]** The orchestrator calls it exactly the

**[7:31]** same way it calls the bash tool or the

**[7:33]** file reader. The system stays consistent

**[7:36]** all the way through. This is just a

**[7:39]** distributed system. An orchestrator

**[7:40]** figures out what needs to happen.

**[7:42]** Workers handle the individual pieces.

**[7:45]** Coordination happens through a clean

**[7:46]** interface. Every design decision in here

**[7:49]** is something you have seen before in

**[7:50]** other context. The agent loop is a

**[7:52]** worker processing a task Q. Tools are a

**[7:55]** service interface layer. Hooks are

**[7:58]** middleware. Memory compaction is like

**[8:00]** log rotation. Sub aents are like working

**[8:03]** nodes in NodeJS. And cloud MD is just

**[8:06]** configuration. None of this is magic.

**[8:09]** Understanding how an agent loops work,

**[8:11]** how tools are wired up, how memory gets

**[8:13]** managed, how sub agents coordinate.

**[8:16]** That's the new distributed system

**[8:17]** literacy. And the engineers who get

**[8:19]** comfortable with these patterns now are

**[8:21]** going to be the ones designing what

**[8:23]** comes next. Do let me know in the

**[8:24]** comments. Maybe in a future video we

**[8:26]** build a minimal agent loop from scratch

**[8:28]** and wire up a basic tool so you can see

**[8:30]** exactly how this fits together in real

**[8:32]** code. Do subscribe if you found this

**[8:34]** video useful.
