# Transcript: BlTpG51x94w

**URL:** https://www.youtube.com/watch?v=BlTpG51x94w
**Segments:** 408

---

## Full Text

Spectrum development here helps AI here to plan things before doing implementation. And on this channel we have reviewed tons of spectrum of frameworks. So that's why in this video we're going to take a look at the most popular spectrum development frameworks that we have like superpower, G stack, GSD, and we're going to take a look at how we can piece them all together into a single workflow that we're going to use to building applications with the highest accuracy. And most importantly, we're going to take this one step further. We're going to introducing the route loop here to see how we can be able to build this applications completely autonomous. Or we're going to have Clocko here to using Clocko headless where I can spin up different iterations and each iteration here can be able to call like superpower, G stack, GSD, and all the scales, all the MCP servers that we have and try to having it orchestrator here to loop through until we have the project is fully built. So we can do this completely autonomous using the route loop approach and also achieve the highest accuracy extract by extracting all the best skills from each frameworks and pieces all together into our own workflows. So pretty much that's what we're going to cover in this video and if you're interested, let's get into the video. Now before we continue, I recently launched our school community where I help you to master AI agents, automations, and so much more. And that's all coming from someone who used to work as a senior AI software engineer at companies like Amazon and Microsoft. And in this community, you're going to get over 100 plus video materials like templates and workflows that I personally built and sold over 100 plus times. On top of that, you also going to get access to our weekly live calls. And just give you an idea, this week we're actually running a Clocko masterclass where we're going to dive into how to improve Clocko's accuracy when we're going to use it to building applications. Plus you're also going to get full community supports where you're going to get chance to ask questions and get direct answers back. So if you're ready to level up, make sure you drop right in and I'll see you in the community. All right, so in order to understand how we can be able to piece all those workflows together, let's understand what spectrum development does, right? So for spectrum development here, it basically help you to or help AI here to plan things before doing executions and we all know that. But essentially, this is the workflow that most spectrum development here follows. It doesn't matter if it's spec kit, the B map method, or you know, any other XYZ framework. They always go with something like brainstorming, right? Helping you to clarify what you're trying to build. Then it's going to go down to like planning, right? How exactly we're going to execute this? Maybe a task list, or maybe breaking this task into different phases, and each phase has its own task list. And then eventually it's going to go down to executions, and eventually here has review, has verifications, maybe having using Playwright here to spin up another browser agent here to verify everything, right? So, you can see that this is the entire spectrum of workflows that pretty much most uh frameworks here follows. And essentially, how each framework here different is that for Superpower here, like you can see for each one, what's special about each one is that for Superpower, it's really good at focusing on test-driven developments, which is something that other workflow doesn't have. It's focusing on writing test first before it do the implementation. And then for G-stack, it's a little different. It also follow that framework, but the selling point here for G-stack is that it's focusing on role-based, which has like different CEO, designers, engineer managers, or maybe security manager here, try to integrate with different personalities here, try to help you to decide a best decision for your product, right? Maybe you're still in the planning phase, or maybe brainstorming phase, it's going to help you to dive deep and try to help you to identify that, right? And furthermore, we also have GSD, which it will help us to avoid context rot. And just to give you a quick TLDR what uh the context rot means, if you have ever interact with large language model, usually it will start to become pretty accurate at uh before 50% of the context window, right? Maybe after you surpass like 50% of the context, it will start to become lower for the accuracy, right? That's exactly what context rot means, is that the more you talk to the AI in the same context, the lower the accuracy it start become. And that's exactly what GSD is trying to solve, is that to make sure that each time when you interact with Claude code or any other coding agents, it's going to make sure that you stay under 50% for the context window. And that's exactly what GSD does. And you can see that with all the special power listed from each frameworks, we can now be able to take the best out of each frameworks and try to piece it together into our own spectral framework that will help you to build applications here much more accurate, right? So, that's exactly how I would do it to take the best out of all three and try to place it into the right workflow, right? So, you can see that this is the exact workflow that I use. I use G stack here to do better brainstorming for clarify my intent on exactly what I'm building because that's what G stack is really good for. And I'll basically put this for this uh planning phase. And then once we have our spec down, once we are using G stack here to clarify our intent, create our spec, then we're using G stack, sorry, GSD here to basically taking our spec and break it down into different phases. And the reason why we do this is like I said, the context fraud issue, right? We don't want to put the entire spec into claw code and have it to execute everything. We want to break it down into different phases. And each phase will guarantee claw code here is going to stay under 50% and that's it. And this will give us the highest accuracy when we um delegate each phase to the claw headless or claw session to do the execution, right? And eventually here you can see after we break it down into different phases, we're going to using Superpower here to follow test-driven developments here to doing the execution for each phase. And that's exactly how I would do it if you were to, you know, want to have achieved the highest accuracy when building applications using this approach, right? And that's exactly how I would do it. Now, maybe for some of you guys, this will be like a really overkill because it's a huge, right? You're Let's say if you're going to, you know, building something from scratch is a large application, I would definitely highly highly recommend you go with this approach, especially for a greenfield project, not a brownfield project. If it is a brownfield project, I'll highly recommend go with one or the other, right? For example, using Superpower here to adding additional feature or maybe using G stack plus Superpower here to building a larger or like a semi-large projects. But if you're going from a greenfield project, then I'll highly recommend you to go with this approach. And you can see here that because this is going to break it down into different phases. And let's say if there's like eight or seven phases, then you have to pass the prompts continuously starting a new session to do it all over again, right? That's going to be really time taking. And that's why I built a skill called build loop using the power of Ralph loop here to basically do this autonomously, which means that if I were to, you know, breaking all the phases, like breaking the spec in different phases, and each phase has its own prompt. And we can be able to use that and store all those prompts into a single state or single file. So, for example, we have our build loop here, which will basically triggered and it's going to look look through our states on exactly what are the phases that has completed. Then it's going to complete the one that's not completed and basically by delegating that phase into a hellish session. So, the basically the way how it works here is that we if we were to do claw hyphen p, it's going to do this in a claw hellish way, which for example, if I were to interact with claw code, I usually do something like this, right? And this will start a claw code session and I can be able to start interacting with this approach, right? Interacting with claw with this approach. But if I don't want to do this, I want to have like claw here to run in a terminal, for example, I can do the claw hyphen p. So, if I were to do the hyphen p and I give the exact prompt, I can still use, for example, if I were to do like one what is one plus one, it will basically run in the background and it will basically try to execute that prompt and that's it. And the good thing about this is that I can still run the main claw code session as this is like the orchestrator and the orchestrator here can still run in this command, right? Inside of the orchestration to basically have it to be like this is going to be the one in the phase one. So, if I were to do like claw hyphen p and just the prompt say like, "Hey, execute the phase one." It's going to do that. After it's done, it's going to, you know, respond it just like how we responded to for the answer for one plus one, it's going to give us the answer here. Once they will give us the answer here, it's going to do the next command, which is the claw hyphen p or phase two, right? It's going to do this for iteration after iterations until everything's are all complete. And like I said, the benefits of doing this is that we can have our orchestrator here to basically doing the phase by phase, right? For example, the orchestrator here is going to delegate task to a background job, try to process phase one, and is not going to take any context in the main orchestrator. The only thing that it takes is the headless session. It's going to run in the background. After it has completed the job in the background, it's going to exit, it's going to give you the outputs for the results for the summary, and then it's going to split it back into phase two and try to pass it to a new Clockwork session here in this case in the background session and try to execute, right? So, you can see that this way approach is going to give us the most highest accuracy because the Clockwork orchestrator here doesn't take any context for the exact work. The only thing that it does is to delegate it into sub background job here to do so. And for each background job here or each background Clockwork session here, it's basically going to, you know, using like Superpower or G stack, try to execute those one by one, right? And if you want to take a step deeper on exactly, "Hey, how is each background session is going to work?" You can see that we have our Superpower here, right? So, basically we're using Superpower here for for executions. And usually what it does here is that it may go through like planning, dispatching agents, following test driven development here, and eventually going to do review and verifications, right? And you can see that for Superpower here, if there's any times where there's like decision being made, what we can do here is that usually it will basically try to trigger back to the orchestrator and try to ask those questions. And what we can do is we can be able to actually delegate this task, right? For let's say if there's any design questions, we can we can delegate this to G stack and have G stack here to trigger like different personality here to answer the questions. For example, if they like design patterns, we can trigger the G stack here to basically pass these questions to like different roles like CEO, engineer manager, or designers, and try to have them to vote on exactly what option they want. And at the end of it, it's just going to take the most popular vote and coming back to the main flow and try to continue on going forward, right? So, this way you can see that we're not going to have any manual involvement, we're just going to have each Clockwork headless session here to basically try to do the executions and have it to make its own decisions along the way. And that's basically how it works. So, you can see that for deeper level at the bottom level here, the G stack is there for making decision if there's any questions. Superpower here is the backbone for the execution. And then for the upper level here, you can see we have a work scheduler here that delegated task to each headless session, right? And each headless session here has its own fresh context window. And we're using a route loop here to basically do this iteration after iterations. And the way how we have these phases here is we're using G GSD to breaking them into different from phases. And each phase has its own prompt. It has its own workflow here to basically do executions. And eventually here you can see we're also using G G stack here to basically create a spec. And that's where the these phases here are coming from, which is from the spec, right? That we have using the G stack here to clarify our intent and breaking our requirement here into different phases. So, that's exactly how this works using the most popular spectrum dollar frameworks, taking the best out of all three, and try to piece it all together into our own workflow inside of our app developments with the highest accuracy. And also try to make this completely autonomous using route as well, right? So, pretty much you can see that's exactly how this works. And let me show you some of the results that I have getting using this approach. And finally, just to show you a live demo, here you can see that we have the entire build queue is all completed. So, I basically spun up a clock who session in this terminal and have it to run build loop overnight. And you can see that we have one session, which is, you know, the current session that we're in, which is the orchestrator, and it has completed over 100 sessions in the background. So, it spun up claw headless and try to complete phase by phase over in the background and try to get everything completed. And you can see that the overall project here is 16 phases out of 16 is all completed. And you can see we have the entire uh build queue here is all empty. The entire spec is now codified. And if you were to scroll all the way down, I asked a simple question, you can see. But if you were to scroll all the way down for the context, so for the context window, we only have spent 10% of it. And that's why we delegate all the tasks into different headless sessions to basically complete the job for us. And we're keeping all the things that we have in the current session here clean and simple. And that's exactly how they work. We take the specials from all the frameworks that we have like test-driven developments, different rules for making better decisions, avoiding context lot here from GSD, and eventually piece them all all together into a single workflow that we can follow to have a highest accuracy for building applications following spectrum developments. And eventually we can be able to make this completely autonomous so they can be able to build it by itself overnight and using the power of route loop to do this completely autonomous.

---

## Timestamped Segments

**[0:00]** Spectrum development here helps AI here

**[0:01]** to plan things before doing

**[0:02]** implementation. And on this channel we

**[0:04]** have reviewed tons of spectrum of

**[0:05]** frameworks. So that's why in this video

**[0:07]** we're going to take a look at the most

**[0:09]** popular spectrum development frameworks

**[0:10]** that we have like superpower, G stack,

**[0:12]** GSD, and we're going to take a look at

**[0:14]** how we can piece them all together into

**[0:16]** a single workflow that we're going to

**[0:17]** use to building applications with the

**[0:18]** highest accuracy. And most importantly,

**[0:20]** we're going to take this one step

**[0:21]** further. We're going to introducing the

**[0:23]** route loop here to see how we can be

**[0:24]** able to build this applications

**[0:26]** completely autonomous. Or we're going to

**[0:27]** have Clocko here to using Clocko

**[0:29]** headless where I can spin up different

**[0:31]** iterations and each iteration here can

**[0:33]** be able to call like superpower, G

**[0:34]** stack, GSD, and all the scales, all the

**[0:37]** MCP servers that we have and try to

**[0:39]** having it orchestrator here to loop

**[0:40]** through until we have the project is

**[0:42]** fully built. So we can do this

**[0:43]** completely autonomous using the route

**[0:45]** loop approach and also achieve the

**[0:47]** highest accuracy extract by extracting

**[0:49]** all the best skills from each frameworks

**[0:51]** and pieces all together into our own

**[0:52]** workflows. So pretty much that's what

**[0:54]** we're going to cover in this video and

**[0:55]** if you're interested, let's get into the

**[0:56]** video. Now before we continue, I

**[0:58]** recently launched our school community

**[1:00]** where I help you to master AI agents,

**[1:02]** automations, and so much more. And

**[1:04]** that's all coming from someone who used

**[1:05]** to work as a senior AI software engineer

**[1:07]** at companies like Amazon and Microsoft.

**[1:10]** And in this community, you're going to

**[1:11]** get over 100 plus video materials like

**[1:13]** templates and workflows that I

**[1:15]** personally built and sold over 100 plus

**[1:17]** times. On top of that, you also going to

**[1:19]** get access to our weekly live calls. And

**[1:21]** just give you an idea, this week we're

**[1:22]** actually running a Clocko masterclass

**[1:24]** where we're going to dive into how to

**[1:26]** improve Clocko's accuracy when we're

**[1:28]** going to use it to building

**[1:29]** applications. Plus you're also going to

**[1:30]** get full community supports where you're

**[1:32]** going to get chance to ask questions and

**[1:34]** get direct answers back. So if you're

**[1:35]** ready to level up, make sure you drop

**[1:37]** right in and I'll see you in the

**[1:38]** community. All right, so in order to

**[1:39]** understand how we can be able to piece

**[1:41]** all those workflows together, let's

**[1:42]** understand what spectrum development

**[1:43]** does, right? So for spectrum development

**[1:45]** here, it basically help you to or help

**[1:47]** AI here to plan things before doing

**[1:48]** executions and we all know that. But

**[1:51]** essentially, this is the workflow that

**[1:52]** most spectrum development here follows.

**[1:54]** It doesn't matter if it's spec kit, the

**[1:56]** B map method, or you know, any other XYZ

**[1:58]** framework. They always go with something

**[2:00]** like brainstorming, right? Helping you

**[2:02]** to clarify what you're trying to build.

**[2:03]** Then it's going to go down to like

**[2:04]** planning, right? How exactly we're going

**[2:06]** to execute this? Maybe a task list, or

**[2:08]** maybe breaking this task into different

**[2:10]** phases, and each phase has its own task

**[2:12]** list. And then eventually it's going to

**[2:14]** go down to executions, and eventually

**[2:15]** here has review, has verifications,

**[2:18]** maybe having using Playwright here to

**[2:19]** spin up another browser agent here to

**[2:21]** verify everything, right? So, you can

**[2:23]** see that this is the entire spectrum of

**[2:24]** workflows that pretty much most uh

**[2:27]** frameworks here follows. And

**[2:28]** essentially, how each framework here

**[2:30]** different is that for Superpower here,

**[2:32]** like you can see for each one, what's

**[2:34]** special about each one is that for

**[2:35]** Superpower, it's really good at focusing

**[2:37]** on test-driven developments, which is

**[2:39]** something that other workflow doesn't

**[2:40]** have. It's focusing on writing test

**[2:42]** first before it do the implementation.

**[2:45]** And then for G-stack, it's a little

**[2:46]** different. It also follow that

**[2:47]** framework, but the selling point here

**[2:49]** for G-stack is that it's focusing on

**[2:51]** role-based, which has like different

**[2:53]** CEO, designers, engineer managers,

**[2:55]** or maybe security manager here, try to

**[2:57]** integrate with different personalities

**[2:59]** here, try to help you to decide a best

**[3:01]** decision for your product, right? Maybe

**[3:03]** you're still in the planning phase, or

**[3:04]** maybe brainstorming phase, it's going to

**[3:06]** help you to dive deep and try to help

**[3:08]** you to identify that, right? And

**[3:09]** furthermore, we also have GSD, which it

**[3:11]** will help us to avoid context rot. And

**[3:13]** just to give you a quick TLDR what uh

**[3:16]** the context rot means, if you have ever

**[3:18]** interact with large language model,

**[3:19]** usually it will start to become pretty

**[3:21]** accurate at uh before 50% of the context

**[3:24]** window, right? Maybe after you surpass

**[3:26]** like 50% of the context, it will start

**[3:28]** to become lower for the accuracy, right?

**[3:30]** That's exactly what context rot means,

**[3:32]** is that the more you talk to the AI in

**[3:35]** the same context, the lower the accuracy

**[3:37]** it start become. And that's exactly what

**[3:39]** GSD is trying to solve, is that to make

**[3:41]** sure that each time when you interact

**[3:42]** with Claude code or any other coding

**[3:44]** agents, it's going to make sure that you

**[3:45]** stay under 50% for the context window.

**[3:48]** And that's exactly what GSD does. And

**[3:50]** you can see that with all the special

**[3:51]** power listed from each frameworks, we

**[3:53]** can now be able to take the best out of

**[3:55]** each frameworks and try to piece it

**[3:56]** together into our own spectral framework

**[3:59]** that will help you to build applications

**[4:01]** here much more accurate, right? So,

**[4:03]** that's exactly how I would do it to take

**[4:05]** the best out of all three and try to

**[4:07]** place it into the right workflow, right?

**[4:10]** So, you can see that this is the exact

**[4:11]** workflow that I use. I use G stack here

**[4:13]** to do better brainstorming for clarify

**[4:15]** my intent on exactly what I'm building

**[4:17]** because that's what G stack is really

**[4:18]** good for. And I'll basically put this

**[4:19]** for this uh planning phase. And then

**[4:21]** once we have our spec down, once we are

**[4:23]** using G stack here to clarify our

**[4:25]** intent, create our spec, then we're

**[4:26]** using G stack, sorry, GSD here to

**[4:28]** basically taking our spec and break it

**[4:30]** down into different phases. And the

**[4:32]** reason why we do this is like I said,

**[4:33]** the context fraud issue, right? We don't

**[4:35]** want to put the entire spec into claw

**[4:37]** code and have it to execute everything.

**[4:39]** We want to break it down into different

**[4:40]** phases. And each phase will guarantee

**[4:42]** claw code here is going to stay under

**[4:44]** 50% and that's it. And this will give us

**[4:46]** the highest accuracy when we

**[4:48]** um delegate each phase to the claw

**[4:51]** headless or claw session to do the

**[4:53]** execution, right? And eventually here

**[4:55]** you can see after we break it down into

**[4:56]** different phases, we're going to using

**[4:57]** Superpower here to follow test-driven

**[4:59]** developments here to doing the execution

**[5:01]** for each phase. And that's exactly how I

**[5:03]** would do it if you were to, you know,

**[5:05]** want to have achieved the highest

**[5:06]** accuracy when building applications

**[5:08]** using this approach, right? And that's

**[5:10]** exactly how I would do it. Now, maybe

**[5:12]** for some of you guys, this will be like

**[5:14]** a really overkill because it's a huge,

**[5:15]** right? You're Let's say if you're going

**[5:17]** to, you know, building something from

**[5:18]** scratch is a large application, I would

**[5:20]** definitely highly highly recommend you

**[5:22]** go with this approach, especially for a

**[5:24]** greenfield project, not a brownfield

**[5:25]** project. If it is a brownfield project,

**[5:27]** I'll highly recommend go with one or the

**[5:29]** other, right? For example, using

**[5:30]** Superpower here to adding additional

**[5:31]** feature or maybe using G stack plus

**[5:33]** Superpower here to building a larger or

**[5:35]** like a semi-large projects. But if

**[5:37]** you're going from a greenfield project,

**[5:39]** then I'll highly recommend you to go

**[5:40]** with this approach. And you can see here

**[5:42]** that because this is going to break it

**[5:44]** down into different phases. And let's

**[5:45]** say if there's like eight or seven

**[5:47]** phases, then you have to pass the

**[5:48]** prompts continuously starting a new

**[5:50]** session to do it all over again, right?

**[5:52]** That's going to be really time taking.

**[5:54]** And that's why I built a skill called

**[5:55]** build loop using the power of Ralph loop

**[5:57]** here to basically do this autonomously,

**[5:59]** which means that if I were to, you know,

**[6:01]** breaking all the phases, like breaking

**[6:03]** the spec in different phases, and each

**[6:05]** phase has its own prompt. And we can be

**[6:06]** able to use that and store all those

**[6:07]** prompts into a single state or single

**[6:09]** file. So, for example, we have our build

**[6:11]** loop here, which will basically

**[6:12]** triggered and it's going to look look

**[6:14]** through our states on exactly what are

**[6:16]** the phases that has completed. Then it's

**[6:17]** going to complete the one that's not

**[6:18]** completed and basically by delegating

**[6:20]** that phase into a hellish session. So,

**[6:23]** the basically the way how it works here

**[6:25]** is that we if we were to do claw hyphen

**[6:27]** p, it's going to do this in a claw

**[6:29]** hellish way, which for example, if I

**[6:31]** were to interact with claw code, I

**[6:32]** usually do something like this, right?

**[6:33]** And this will start a claw code session

**[6:35]** and I can be able to start interacting

**[6:37]** with this approach, right? Interacting

**[6:39]** with claw with this approach. But if I

**[6:41]** don't want to do this, I want to have

**[6:42]** like claw here to run in a terminal, for

**[6:44]** example, I can do the claw hyphen p. So,

**[6:47]** if I were to do the hyphen p and I give

**[6:50]** the exact prompt, I can still use, for

**[6:52]** example, if I were to do like one what

**[6:54]** is one plus one, it will basically run

**[6:55]** in the background and it will basically

**[6:58]** try to execute that prompt and that's

**[6:59]** it. And the good thing about this is

**[7:01]** that I can still run the main claw code

**[7:03]** session as this is like the orchestrator

**[7:05]** and the orchestrator here can still run

**[7:07]** in this command, right? Inside of the

**[7:09]** orchestration to basically have it to be

**[7:11]** like this is going to be the one in the

**[7:12]** phase one. So, if I were to do like claw

**[7:14]** hyphen p and just the prompt say like,

**[7:16]** "Hey, execute the phase one." It's going

**[7:18]** to do that. After it's done, it's going

**[7:19]** to, you know, respond it just like how

**[7:21]** we responded to for the answer for one

**[7:23]** plus one, it's going to give us the

**[7:24]** answer here. Once they will give us the

**[7:26]** answer here, it's going to do the next

**[7:28]** command, which is the claw hyphen p or

**[7:30]** phase two, right? It's going to do this

**[7:32]** for iteration after iterations until

**[7:34]** everything's are all complete. And like

**[7:35]** I said, the benefits of doing this is

**[7:37]** that we can have our orchestrator here

**[7:39]** to basically doing the phase by phase,

**[7:40]** right? For example, the orchestrator

**[7:42]** here is going to delegate task to a

**[7:44]** background job, try to process phase

**[7:45]** one, and is not going to take any

**[7:47]** context in the main orchestrator. The

**[7:49]** only thing that it takes is the

**[7:51]** headless session. It's going to run in

**[7:53]** the background. After it has completed

**[7:55]** the job in the background, it's going to

**[7:57]** exit, it's going to give you the outputs

**[7:59]** for the results for the summary, and

**[8:01]** then it's going to split it back into

**[8:02]** phase two and try to pass it to a new

**[8:05]** Clockwork session here in this case in

**[8:06]** the background session and try to

**[8:08]** execute, right? So, you can see that

**[8:09]** this way approach is going to give us

**[8:11]** the most highest accuracy because the

**[8:14]** Clockwork orchestrator here doesn't take

**[8:16]** any context for the exact work. The only

**[8:19]** thing that it does is to delegate it

**[8:20]** into sub background job here to do so.

**[8:22]** And for each background job here or each

**[8:24]** background Clockwork session here, it's

**[8:25]** basically going to, you know, using like

**[8:27]** Superpower or G stack, try to execute

**[8:29]** those one by one, right? And if you want

**[8:31]** to take a step deeper on exactly, "Hey,

**[8:33]** how is each background session is going

**[8:35]** to work?" You can see that we have our

**[8:36]** Superpower here, right? So, basically

**[8:38]** we're using Superpower here for for

**[8:40]** executions. And usually what it does

**[8:41]** here is that it may go through like

**[8:43]** planning, dispatching agents, following

**[8:45]** test driven development here, and

**[8:46]** eventually going to do review and

**[8:47]** verifications, right? And you can see

**[8:49]** that for Superpower here, if there's any

**[8:51]** times where there's like decision being

**[8:53]** made, what we can do here is that

**[8:54]** usually it will basically try to trigger

**[8:55]** back to the orchestrator and try to ask

**[8:57]** those questions. And what we can do is

**[8:59]** we can be able to actually delegate this

**[9:00]** task, right? For let's say if there's

**[9:02]** any design questions, we can we can

**[9:04]** delegate this to G stack and have G

**[9:06]** stack here to trigger like different

**[9:07]** personality here to answer the

**[9:09]** questions. For example, if they like

**[9:10]** design patterns, we can trigger the G

**[9:12]** stack here to basically pass these

**[9:14]** questions to like different roles like

**[9:15]** CEO, engineer manager, or designers, and

**[9:18]** try to have them to vote on exactly what

**[9:20]** option they want. And at the end of it,

**[9:22]** it's just going to take the most popular

**[9:23]** vote and coming back to the main flow

**[9:24]** and try to continue on going forward,

**[9:26]** right? So, this way you can see that

**[9:28]** we're not going to have any manual

**[9:29]** involvement, we're just going to have

**[9:31]** each Clockwork headless session here to

**[9:33]** basically try to do the executions and

**[9:35]** have it to make its own decisions along

**[9:36]** the way. And that's basically how it

**[9:38]** works. So, you can see that for deeper

**[9:40]** level at the bottom level here, the G

**[9:41]** stack is there for making decision if

**[9:43]** there's any questions. Superpower here

**[9:45]** is the backbone for the execution. And

**[9:47]** then for the upper level here, you can

**[9:49]** see we have a work scheduler here that

**[9:50]** delegated task to each headless session,

**[9:53]** right? And each headless session here

**[9:54]** has its own fresh context window. And

**[9:56]** we're using a route loop here to

**[9:57]** basically do this iteration after

**[9:59]** iterations. And the way how we have

**[10:01]** these phases here is we're using G GSD

**[10:04]** to breaking them into different from

**[10:05]** phases. And each phase has its own

**[10:06]** prompt. It has its own workflow here to

**[10:08]** basically do executions. And eventually

**[10:10]** here you can see we're also using G G

**[10:12]** stack here to basically create a spec.

**[10:14]** And that's where the these phases here

**[10:16]** are coming from, which is from the spec,

**[10:17]** right? That we have using the G stack

**[10:19]** here to clarify our intent and breaking

**[10:22]** our requirement here into different

**[10:23]** phases. So, that's exactly how this

**[10:24]** works using the most popular spectrum

**[10:26]** dollar frameworks, taking the best out

**[10:28]** of all three, and try to piece it all

**[10:29]** together into our own workflow inside of

**[10:31]** our app developments with the highest

**[10:33]** accuracy. And also try to make this

**[10:35]** completely autonomous using route as

**[10:38]** well, right? So, pretty much you can see

**[10:39]** that's exactly how this works. And let

**[10:41]** me show you some of the results that I

**[10:42]** have getting using this approach. And

**[10:44]** finally, just to show you a live demo,

**[10:46]** here you can see that we have the entire

**[10:48]** build queue is all completed. So, I

**[10:49]** basically spun up a clock who session in

**[10:51]** this terminal and have it to run build

**[10:53]** loop overnight. And you can see that we

**[10:55]** have one session, which is, you know,

**[10:57]** the current session that we're in, which

**[10:58]** is the orchestrator, and it has

**[10:59]** completed over 100 sessions in the

**[11:01]** background. So, it spun up claw headless

**[11:03]** and try to complete phase by phase over

**[11:06]** in the background and try to get

**[11:07]** everything completed. And you can see

**[11:08]** that the overall project here is 16

**[11:10]** phases out of 16 is all completed. And

**[11:13]** you can see we have the entire uh build

**[11:15]** queue here is all empty. The entire spec

**[11:18]** is now codified. And if you were to

**[11:20]** scroll all the way down, I asked a

**[11:21]** simple question, you can see. But if you

**[11:23]** were to scroll all the way down for the

**[11:24]** context, so for the context window, we

**[11:26]** only have spent 10% of it. And that's

**[11:28]** why we delegate all the tasks into

**[11:29]** different headless sessions to basically

**[11:31]** complete the job for us. And we're

**[11:33]** keeping all the things that we have in

**[11:34]** the current session here clean and

**[11:36]** simple. And that's exactly how they

**[11:37]** work. We take the specials from all the

**[11:39]** frameworks that we have like test-driven

**[11:41]** developments, different rules for making

**[11:42]** better decisions, avoiding context lot

**[11:44]** here from GSD, and eventually piece them

**[11:46]** all all together into a single workflow

**[11:48]** that we can follow to have a highest

**[11:50]** accuracy for building applications

**[11:52]** following spectrum developments. And

**[11:54]** eventually we can be able to make this

**[11:55]** completely autonomous so they can be

**[11:57]** able to build it by itself overnight and

**[12:00]** using the power of route loop to do this

**[12:02]** completely autonomous.
