# Transcript: This Meta-Harness Changes How You Run AI Agents

**URL:** https://www.youtube.com/watch?v=141biWM1mlE
**Segments:** 380
**Channel:** Prompt Engineering
**Duration:** 14:09
**Uploaded:** 2026-06-15

---

## Full Text

Most of us don't use a single AI agent. We use multiple of them for different purposes because each one of them have their own capabilities. But none of them can see each other. You are the one connecting them. Copy, paste, and repeat. Now, every agent is trapped in its own box, but what if they were not? Now, an agent today is basically the model plus the harness. A model on its own just predicts text. A harness is everything wrapped around it that gets the work done. It usually includes agent loop, tools, memories, and a UI. Codex, Cloud, Code, Pi, each one is a harness with similar ideas, but very different implementations. And different capabilities. Now, line up the agents that you actually use. The here are four different harnesses side by side. Each one has its own memory, its own UI, its own tools. And no harness can see the other one. No shared session, no shared history. Now, we usually work simultaneously in most of them, but what if you can put everything under a single roof? Now, if you build agents on top of them, the wall hurts from the other side. When a better model ships, say a new SDK or a stronger harness, to adopt it, you replumb everything you built and the cost climbs. You are basically locked to the layer you started on. Now, but if you look closer at any harness, however different they are from the inside, everyone speaks the same language on the outside. There are messages and files in, text and tool calls out. So, it's a great advantage that they have exactly this identical interface. Now, if the interface is identical, you can build one layer over all of them. Take the harness you already use and slide one rail underneath them. Every harness becomes an interchangeable worker. So, a harness sits over a model and this layer sits over the harness. We can call this a meta harness. This is exactly what Databricks just open-sourced. They are calling it Omni. It's a meta harness for all your AI agents. It's Apache 2.0, so you can build on top of it. It's one command, and every agent you have runs under one roof. They use it internally, so it's a battle-tested. Under the hood, it has three different pieces. On the left, you bring your agents. These include proprietary agents like Cloud Code, Codex, or your custom agents, which you can set up in the form of a YAML file. Then, runner wraps any of them in one uniform sandbox session. A server adds search history, policies, MCPs, skills, and artifacts. It's Postgres and deploys everywhere. You can run this on Docker, Railway, Fly, or Cloud Sandbox. And it exposes that one session everywhere, whether you want to access it through terminal, web native app, mobile, or a REST API, which is pretty great, because you can now use the same interface interacting with Codex, Cloud Code, Pi, or any agent of your choice. Now, because the session lives in the layer, not the tool, there is just one session object, which is your agent files and history. Every device is just a window onto it. You can start in your terminal, continue in the browser, or pick it up on your phone, which is pretty awesome, because you have the same agent, same files, just different interfaces, which are in sync, and you can work from anywhere. Okay, now let's talk about the capabilities. This is an open-source meta harness. The beauty is that you can customize it for your own need, if you want. Let's first talk about what exactly does it unlock. The first one is composition. An agent is just a short YAML file which includes a prompt, some tools, and a harness. Switching from Claude to Codex is one-line change. And you can run several at once as a team. Now, agents can even write agents. You can just describe one and it authors the file. Now, they ship with two different ready-made agents. The first one is Polly. Polly does not write any code. It's the tech lead. It plans and splits the work across coding agents in parallel, get work trees, then routes each diff to a reviewer from a different vendor than which wrote the code. So, say Claude codes is reviewed by Codex code is reviewed by Claude. And when you're happy with the results, you just merge it. So, cross-vendor review only works about the harness. Now, this planner, executor, and reviewer or verify by patterns is extremely important. Especially, you don't want the same agent that wrote the code to review its code because it has internal biases. And OmniJade makes it extremely easy. Now, the second built-in agent is called Debbie, which basically is a brainstorm partner with two heads. So, the two are Claude and GPT. You can I think bring your own one as well. Every question goes to both at once. You will get two answers side by side. But here's the fun part. If you type {slash} debate, these are going to critique each other for a few rounds, then converge. A lot of people plan with say Codex and then implement with Claude code or the other way around. You could do that. Or if you have to make an architectural decision, this agent can be extremely helpful. Okay, the second big unlock that this provides is control. Now, in this case every action passes through a gate, allow deny or ask you first. Now, the thing is that this is not just a polite request in a prompt. It is enforced on every tool call. And because it lives in the layer, the rules can depend on history. This is going to be extremely important, especially if you want to impose cost gaps, risk scores, repo and file scopes. Or even things like PPI scans, everything is built in. Now, this is important, especially if you don't want to have YOLO runs and really want to make sure that there are specific follow policies that the agents follow. Okay, so how exactly all of this work? Well, underneath all of this is the OS sandbox. So, every agent runs boxed in. It can only touch the files and network you allow. Now, another most important feature is that it the agents cannot directly read your secret keys. The agent actually never sees this. The layer injects it on the way out through an approval proxy. So, even if you're running the YOLO mode, it is going to be a lot safer than just providing it access to the agent. Now, the third biggest unlock this provides is collaboration. When your session is live and you're driving it, you can share a link and a teammate can watch the work or even chat with it in real time. So, basically this is code driving and collaboration. The beauty is that their messages run on your machine. Or you can simply fork it and take the conversation your own way. Okay, let me show you a quick demo of how exactly this works in practice. Thanks to Databricks for giving me early access in making this video possible through their sponsorship. In the rest of the video, I'll show you how to set it up and use it locally. All you need to do is just run this command to install the meta harness. Now, after installation, the first thing you want to do is to set up this on your local machine. Right now, I'm using my cloud code subscription, code x subscription, and Pi is using Ollama. In each one of this case, you can add your own API keys or use your subscription. Then, you can use coding agent of your choice. So, say you can use the cloud code harness or code x harness. Or you can also use some of the built-in agents. They have Poly, which is basically a multi-agent orchestration setup. Now, keep in mind, Omni harness is not a coding harness. It basically enables you to interact with these multiple harnesses directly. So, Poly doesn't write code itself. It decomposes your goal into subtasks and delegates each one of them into a subagent running on its own harness and get work tree. So, in my case, you can just directly start this orchestrator agent. Now, whenever you start a session, you're going to see that it opens up this web UI along with the actual terminal window. So, either you can work here in the terminal or in the web UI or even there is a desktop app. The beauty is that all of them are going to be sharing the exact same session. To show you a quick example, I'm going to describe a task. Create a single-page web UI that uses the Gemini Nano Banana model for image generation. User provides input in the form of text. The output is going to be an image. Also, add the ability for the user to provide their API key within and UI. Now, we can just send this. Okay, so on my machine, it wasn't actually able to see the Pine and Cloud Code CLI. Uh so, I simply asked it to configure those for me, and it went ahead and configured everything. Which is pretty awesome. But more interestingly, you actually see the same conversation happening exactly in the terminal where I started this. Right? So, these are different interfaces which are interacting with the exact same session. Now, in this case, it's going to use Cloud Code to implement things. Then for review, it's going to use CodeX. And it says that it runs autonomously and will wake me up when it's done. Right? So, it seems like the process is running. If we look back, uh here are basically the agents working under the hood. So, it gives you visibility to what exactly every agent is doing. So, right now it's autonomously testing the app. Okay, so it quickly tested the app. Seems to be working. Now, on the meta harness side, right now the implementation is done by Cloud Code. Then it started the independent verification step. For this, it's using CodeX. Now, the interesting thing is that it's going to be only passing on the diffs cuz there are different work trees where these agents or harnesses are working independently. Now, another feature is that you can just directly interact with a specific agent or harness. Which is pretty neat, right? So, right now CodeX is reviewing the code, but you can go and ask Cloud Code something. Now, here's another browser session that I opened. I see exactly the same processing happening. So, you could just potentially deploy this in the cloud and then share the link from here with your coworker, and they will be able to interact with the exact same session that is running in the cloud. Or if it's via local network, you can have the session running on your machine and your teammates will be able to interact with that. So, it's great for collaboration. Okay, so a couple of other features I think are going to be very important for everybody who's building with this, especially given the cost of these API based models is crazy right now. So, you can actually see the session cost. It gives you a breakdown of what exactly was done, how many tokens was consumed by each one of these models, but then you can set up different policies. [clears throat] And I think this is very important. You can have, let's say, limit tool calls or for the specific session, uh maybe deny PPI and other requests, right? So, these are contextual policies that you can set. Even you can set access to different tools or connectors, but what I would highly recommend is to set the cost. So, you can have a session cost budget or for user daily cost budget. I think this is going to be more and more important for organizations. So, just to give you an example, I would say like $10, right? And then you can define different thresholds based on soft warnings. Okay, so here's the app that is running. It has a link to the Google AI Studio. Now, here here was the initial implementation from Cloud Code. Then there was a independent review from Codex and you can actually see that it specifically found issues. Those were sent back. The implementation was done again, tested again, right? And this is kind of the loop that you want. Now, you can write this orchestration logic yourself, but OmniGen ships this with their polyagent. So, here's the final app that it created. A picture of a starfish wearing sunglasses jumping with happiness. All right, so we're going to see. This is pretty awesome. Okay, there is a lot more to cover, but do check out Omnigen. It's an open source model. I think this meta harness of orchestration layer is going to be very critical, especially when you have these different harnesses designed for custom tasks with different capabilities. It's a very awesome project. Still really early days. There might be some tweaks that you'll need, but since this is open source, I think this is going to grow really fast. Again, thanks to Databricks for giving me early access and making this video possible. Anyways, I hope you found this video useful. Thanks for watching and as always, see you in the next one.

---

## Timestamped Segments

**[0:00]** Most of us don't use a single AI agent.

**[0:02]** We use multiple of them for different

**[0:05]** purposes because each one of them have

**[0:07]** their own capabilities.

**[0:08]** But none of them can see each other.

**[0:11]** You are the one connecting them. Copy,

**[0:14]** paste, and repeat. Now, every agent is

**[0:17]** trapped in its own box, but what if they

**[0:20]** were not? Now, an agent today is

**[0:22]** basically the model plus the harness. A

**[0:25]** model on its own just predicts text. A

**[0:27]** harness is everything wrapped around it

**[0:30]** that gets the work done. It usually

**[0:32]** includes agent loop, tools, memories,

**[0:35]** and a UI. Codex, Cloud, Code, Pi, each

**[0:38]** one is a harness with similar ideas, but

**[0:41]** very different implementations. And

**[0:43]** different capabilities. Now, line up the

**[0:46]** agents that you actually use. The here

**[0:48]** are four different harnesses side by

**[0:50]** side. Each one has its own memory, its

**[0:52]** own UI, its own tools.

**[0:54]** And no harness can see the other one. No

**[0:57]** shared session, no shared history. Now,

**[0:59]** we usually work simultaneously in most

**[1:02]** of them, but what if you can put

**[1:03]** everything under a single roof? Now, if

**[1:06]** you build agents on top of them, the

**[1:07]** wall hurts from the other side. When a

**[1:10]** better model ships, say a new SDK or a

**[1:12]** stronger harness, to adopt it, you

**[1:15]** replumb everything you built and the

**[1:17]** cost climbs. You are basically locked to

**[1:20]** the layer you started on. Now, but if

**[1:23]** you look closer at any harness, however

**[1:26]** different they are from the inside,

**[1:27]** everyone speaks the same language on the

**[1:30]** outside. There are messages and files

**[1:33]** in, text and tool calls out. So, it's a

**[1:36]** great advantage that they have exactly

**[1:38]** this identical interface. Now, if the

**[1:41]** interface is identical, you can build

**[1:43]** one layer over all of them. Take the

**[1:45]** harness you already use and slide one

**[1:48]** rail underneath them.

**[1:50]** Every harness becomes an interchangeable

**[1:53]** worker. So, a harness sits over a model

**[1:55]** and this layer sits over the harness.

**[1:58]** We can call this a meta harness. This is

**[2:01]** exactly what Databricks just

**[2:03]** open-sourced. They are calling it Omni.

**[2:06]** It's a meta harness for all your AI

**[2:08]** agents.

**[2:09]** It's Apache 2.0, so you can build on top

**[2:12]** of it.

**[2:13]** It's one command, and every agent you

**[2:15]** have runs under one roof.

**[2:18]** They use it internally, so it's a

**[2:20]** battle-tested.

**[2:22]** Under the hood, it has three different

**[2:23]** pieces.

**[2:24]** On the left, you bring your agents.

**[2:26]** These include proprietary agents like

**[2:28]** Cloud Code,

**[2:29]** Codex, or your custom agents,

**[2:33]** which you can set up in the form of a

**[2:35]** YAML file.

**[2:36]** Then, runner wraps any of them in one

**[2:39]** uniform sandbox session.

**[2:42]** A server adds search history, policies,

**[2:44]** MCPs, skills, and artifacts.

**[2:47]** It's Postgres and deploys everywhere.

**[2:50]** You can run this on Docker, Railway,

**[2:52]** Fly, or Cloud Sandbox.

**[2:55]** And it exposes that one session

**[2:58]** everywhere,

**[2:59]** whether you want to access it through

**[3:01]** terminal, web native app, mobile, or a

**[3:03]** REST API,

**[3:05]** which is pretty great, because you can

**[3:06]** now use the same interface interacting

**[3:08]** with Codex, Cloud Code, Pi, or any agent

**[3:12]** of your choice.

**[3:13]** Now, because the session lives in the

**[3:15]** layer, not the tool, there is just one

**[3:17]** session object, which is your agent

**[3:19]** files and history.

**[3:21]** Every device is just a window onto it.

**[3:24]** You can start in your terminal, continue

**[3:26]** in the browser, or pick it up on your

**[3:28]** phone,

**[3:29]** which is pretty awesome, because you

**[3:31]** have the same agent, same files, just

**[3:32]** different interfaces, which are in sync,

**[3:36]** and you can work from anywhere.

**[3:38]** Okay, now let's talk about the

**[3:39]** capabilities. This is an open-source

**[3:41]** meta harness.

**[3:43]** The beauty is that you can customize it

**[3:45]** for your own need, if you want. Let's

**[3:47]** first talk about what exactly does it

**[3:49]** unlock. The first one is composition.

**[3:51]** An agent is just a short YAML file which

**[3:54]** includes a prompt, some tools, and a

**[3:57]** harness.

**[3:58]** Switching from Claude to Codex is

**[4:01]** one-line change.

**[4:03]** And you can run several at once as a

**[4:06]** team.

**[4:07]** Now, agents can even write agents. You

**[4:09]** can just describe one and it authors the

**[4:12]** file.

**[4:13]** Now, they ship with two different

**[4:15]** ready-made agents. The first one is

**[4:16]** Polly.

**[4:18]** Polly does not write any code. It's the

**[4:20]** tech lead. It plans and splits the work

**[4:23]** across coding agents in parallel, get

**[4:26]** work trees, then routes each diff to a

**[4:29]** reviewer from a different vendor than

**[4:32]** which wrote the code.

**[4:33]** So, say Claude codes

**[4:36]** is reviewed by Codex code is reviewed by

**[4:38]** Claude. And when you're happy with the

**[4:40]** results, you just merge it. So,

**[4:42]** cross-vendor

**[4:43]** review only works about the harness.

**[4:46]** Now, this planner, executor, and

**[4:48]** reviewer or verify by patterns is

**[4:51]** extremely important. Especially, you

**[4:53]** don't want the same agent that wrote the

**[4:55]** code to review its code because it has

**[4:58]** internal biases.

**[5:00]** And OmniJade makes it extremely easy.

**[5:03]** Now, the second built-in agent is called

**[5:05]** Debbie,

**[5:06]** which basically is a brainstorm partner

**[5:09]** with two heads.

**[5:11]** So, the two are Claude and GPT. You can

**[5:14]** I think bring your own one as well.

**[5:15]** Every question goes to both at once.

**[5:19]** You will get two answers side by side.

**[5:22]** But here's the fun part. If you type

**[5:24]** {slash} debate, these are going to

**[5:26]** critique each other for a few rounds,

**[5:28]** then converge.

**[5:30]** A lot of people plan with say Codex and

**[5:33]** then implement with Claude code or the

**[5:35]** other way around. You could do that. Or

**[5:38]** if you have to make an architectural

**[5:40]** decision, this agent can be extremely

**[5:43]** helpful.

**[5:44]** Okay, the second big unlock that this

**[5:46]** provides is control. Now, in this case

**[5:49]** every action passes through a gate,

**[5:51]** allow deny or ask you first.

**[5:54]** Now, the thing is that this is not just

**[5:55]** a polite request in a prompt. It is

**[5:58]** enforced on every tool call.

**[6:01]** And because it lives in the layer, the

**[6:03]** rules can depend on history. This is

**[6:06]** going to be extremely important,

**[6:07]** especially if you want to impose cost

**[6:10]** gaps, risk scores, repo and file scopes.

**[6:13]** Or even things like PPI

**[6:16]** scans, everything is built in. Now, this

**[6:20]** is important, especially if you don't

**[6:21]** want to have YOLO runs and really want

**[6:25]** to make sure that

**[6:26]** there are specific follow policies that

**[6:28]** the agents follow. Okay, so how exactly

**[6:32]** all of this work? Well, underneath all

**[6:34]** of this is the OS sandbox.

**[6:38]** So, every agent runs boxed in. It can

**[6:42]** only touch the files and network you

**[6:44]** allow. Now, another most important

**[6:46]** feature is that it the agents cannot

**[6:49]** directly read your secret keys.

**[6:52]** The agent actually never sees this. The

**[6:54]** layer injects it on the way out through

**[6:58]** an approval proxy. So, even if you're

**[7:00]** running the YOLO mode, it is going to be

**[7:02]** a lot safer than just providing it

**[7:04]** access to the agent. Now, the third

**[7:07]** biggest unlock this provides is

**[7:09]** collaboration. When your session is live

**[7:12]** and you're driving it, you can share a

**[7:14]** link and a teammate can watch the work

**[7:16]** or even chat with it in real time. So,

**[7:19]** basically this is

**[7:21]** code driving and collaboration. The

**[7:24]** beauty is that their messages run on

**[7:26]** your machine.

**[7:27]** Or you can simply fork it and take the

**[7:29]** conversation your own way. Okay, let me

**[7:32]** show you a quick demo of how exactly

**[7:34]** this works in practice. Thanks to

**[7:36]** Databricks for giving me early access in

**[7:38]** making this video possible through their

**[7:40]** sponsorship. In the rest of the video,

**[7:42]** I'll show you how to set it up

**[7:44]** and use it locally. All you need to do

**[7:47]** is just run this command to install the

**[7:50]** meta harness.

**[7:51]** Now, after installation, the first thing

**[7:53]** you want to do is to set up

**[7:56]** this on your local machine.

**[7:57]** Right now,

**[7:58]** I'm using my cloud code subscription,

**[8:00]** code x subscription, and Pi is using

**[8:03]** Ollama.

**[8:04]** In each one of this case, you can

**[8:07]** add your own API keys or use your

**[8:10]** subscription.

**[8:11]** Then, you can use coding agent of your

**[8:13]** choice. So, say you can use

**[8:16]** the cloud code harness or code x

**[8:19]** harness.

**[8:20]** Or you can also use some of the built-in

**[8:22]** agents. They have Poly, which is

**[8:24]** basically a multi-agent orchestration

**[8:27]** setup. Now, keep in mind, Omni harness

**[8:29]** is not

**[8:30]** a coding harness. It basically enables

**[8:33]** you to interact with these multiple

**[8:35]** harnesses directly.

**[8:37]** So, Poly doesn't write code itself. It

**[8:41]** decomposes your goal into subtasks and

**[8:43]** delegates each one of them into a

**[8:45]** subagent running on its own harness and

**[8:48]** get work tree.

**[8:49]** So, in my case, you can just directly

**[8:51]** start this orchestrator agent. Now,

**[8:55]** whenever you start a session, you're

**[8:56]** going to see that it opens up this web

**[8:58]** UI

**[8:59]** along with the actual terminal window.

**[9:02]** So, either you can work here in the

**[9:03]** terminal or in the web UI or even there

**[9:06]** is a desktop app.

**[9:08]** The beauty is that all of them are going

**[9:09]** to be sharing the exact same session.

**[9:12]** To show you a quick example, I'm going

**[9:14]** to describe a task. Create a single-page

**[9:18]** web UI

**[9:19]** that uses the Gemini Nano Banana model

**[9:23]** for image generation. User provides

**[9:25]** input

**[9:26]** in the form of text. The output is going

**[9:28]** to be an image. Also, add the ability

**[9:31]** for the user to provide their API key

**[9:34]** within and UI.

**[9:38]** Now, we can just send this.

**[9:40]** Okay, so on my machine, it wasn't

**[9:42]** actually able to see the Pine and Cloud

**[9:45]** Code CLI.

**[9:46]** Uh so, I simply asked it to configure

**[9:47]** those for me, and it went ahead and

**[9:49]** configured everything. Which is pretty

**[9:52]** awesome.

**[9:53]** But more interestingly, you actually see

**[9:54]** the same conversation happening exactly

**[9:59]** in the terminal where I started this.

**[10:01]** Right? So, these are different

**[10:03]** interfaces which are interacting with

**[10:04]** the exact same session.

**[10:06]** Now, in this case, it's going to use

**[10:08]** Cloud Code to implement things. Then

**[10:10]** for review, it's going to use CodeX.

**[10:13]** And it says that it runs autonomously

**[10:15]** and will wake me up when it's done.

**[10:17]** Right? So, it seems like the process is

**[10:19]** running. If we look back, uh here are

**[10:23]** basically the agents working under the

**[10:25]** hood. So, it gives you visibility to

**[10:28]** what exactly every agent is doing.

**[10:30]** So, right now it's autonomously testing

**[10:32]** the app. Okay, so it quickly tested the

**[10:34]** app. Seems to be working.

**[10:35]** Now, on the meta harness side, right now

**[10:38]** the implementation is done by Cloud

**[10:40]** Code. Then it started the independent

**[10:43]** verification step. For this, it's using

**[10:46]** CodeX. Now, the

**[10:48]** interesting thing is that it's going to

**[10:50]** be only passing on the diffs cuz there

**[10:53]** are different work trees where these

**[10:55]** agents or harnesses are working

**[10:57]** independently.

**[10:58]** Now, another feature is that you can

**[10:59]** just directly interact with a specific

**[11:02]** agent or harness. Which is pretty neat,

**[11:05]** right? So, right now CodeX is reviewing

**[11:07]** the code, but you can go and ask Cloud

**[11:10]** Code something.

**[11:11]** Now, here's another browser session that

**[11:13]** I opened. I see exactly the same

**[11:15]** processing happening. So, you could just

**[11:17]** potentially deploy this in the cloud and

**[11:20]** then share the link from here with your

**[11:24]** coworker, and they will be able to

**[11:25]** interact with the exact same session

**[11:27]** that is running in the cloud. Or if it's

**[11:30]** via local network, you can have the

**[11:32]** session running on your machine and your

**[11:35]** teammates will be able to interact with

**[11:37]** that.

**[11:38]** So, it's great for collaboration.

**[11:40]** Okay, so a couple of other features I

**[11:41]** think

**[11:42]** are going to be very important for

**[11:43]** everybody who's building with this,

**[11:45]** especially given the cost of these API

**[11:49]** based models is crazy right now. So, you

**[11:52]** can actually see the session cost.

**[11:54]** It gives you a breakdown of what exactly

**[11:57]** was done, how many tokens was consumed

**[11:59]** by each one of these models, but then

**[12:02]** you can set up different policies.

**[12:03]** [clears throat]

**[12:04]** And I think this is very important. You

**[12:06]** can have, let's say,

**[12:08]** limit tool calls or for the specific

**[12:10]** session,

**[12:12]** uh maybe deny PPI and other requests,

**[12:14]** right? So, these are contextual policies

**[12:16]** that you can set. Even you can set

**[12:18]** access to different tools or connectors,

**[12:22]** but what I would highly recommend is to

**[12:25]** set the cost. So, you can have a

**[12:27]** session cost budget

**[12:29]** or for user daily cost budget. I think

**[12:31]** this is going to be more and more

**[12:32]** important for organizations.

**[12:35]** So,

**[12:36]** just to give you an example, I would say

**[12:38]** like $10, right?

**[12:40]** And then you can define different

**[12:42]** thresholds based on

**[12:43]** soft

**[12:45]** warnings.

**[12:46]** Okay, so here's the app that is running.

**[12:48]** It has a link to the Google AI Studio.

**[12:50]** Now, here here was the initial

**[12:52]** implementation from Cloud Code. Then

**[12:55]** there was a

**[12:56]** independent review from Codex and you

**[12:58]** can actually see that it specifically

**[13:00]** found issues.

**[13:02]** Those were sent back. The implementation

**[13:05]** was done again, tested again, right? And

**[13:08]** this is kind of the loop that you want.

**[13:10]** Now, you can write this orchestration

**[13:12]** logic yourself, but

**[13:15]** OmniGen ships this with their polyagent.

**[13:19]** So, here's the final app that it

**[13:20]** created.

**[13:22]** A picture of a starfish wearing

**[13:25]** sunglasses

**[13:26]** jumping

**[13:28]** with happiness. All right, so we're

**[13:30]** going to see. This is pretty awesome.

**[13:32]** Okay, there is a lot more to cover, but

**[13:34]** do check out Omnigen. It's an open

**[13:36]** source model. I think this meta harness

**[13:39]** of orchestration layer is going to be

**[13:42]** very critical, especially when you have

**[13:44]** these different harnesses designed for

**[13:46]** custom tasks with different

**[13:47]** capabilities.

**[13:49]** It's a very awesome project. Still

**[13:51]** really early days. There might be

**[13:53]** some tweaks that you'll need, but since

**[13:56]** this is open source, I think this is

**[13:57]** going to grow really fast. Again, thanks

**[14:00]** to Databricks for giving me early access

**[14:02]** and making this video possible.

**[14:04]** Anyways, I hope you found this video

**[14:05]** useful. Thanks for watching and as

**[14:06]** always, see you in the next one.
