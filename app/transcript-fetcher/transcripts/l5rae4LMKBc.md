# Transcript: Claude Can Now Build Its Own Harness... For Every Task

**URL:** https://www.youtube.com/watch?v=l5rae4LMKBc
**Segments:** 316
**Channel:** Prompt Engineering
**Duration:** 13:24
**Uploaded:** 2026-06-03

---

## Full Text

Okay, so harness is like Claude code and Codex are designed for coding tasks, but the people are now using them for a lot more than coding including all kind of knowledge work. But the thing is that all of this still gets funneled into one harness that was built for coding. And for these non-coding jobs, this harness is not the optimal one. So, what if instead of forcing your task through it, Claude code could write its own harness custom for your task on the fly right in front of you. This is what exactly dynamic workflows are. I covered how they're different from agents last time. So, today it's all about one idea, a custom harness for every task on the fly. Now, the question is going to be why even bother building custom harness for every task when one Claude works on your task, everything it touches lands in that single context window. Now, when a big messy job, that windows fill up and start hitting a ceiling that impacts the performance of your model or agent. Now, there are usually three failure modes that you will notice. The first one is agentic laziness. This is where it quits early and calls the job done after partial work like a security review where it handles 35 of 50 tasks. The second one is self-preferential bias where it grades its own work too kindly the moment you ask it to check itself. And the third one is gold drift where the original brief slowly leaks out, especially after the context gets compacted. Now, the fix for all of these is that stop running the whole job in one context and split it across separate clean ones. Okay, so a potential solution to this is dynamic workflow. In this video, I want to talk about what exactly they are. For more details, watch my previous video. So, it's just a JavaScript file that runs a small team of Claude's. Now, if you break it down, there is a script and it has a few special function. The main one is agent, which spawns one sub agent within its own clean context window. Then there is parallel, uh which pans a bunch of them out at once and wait for all of them to finish. And a pipeline, which streams a list of items through a chain of stages. Now, on top of all of this, the workflow picks which model each agent is going to run and whether it gets its own work tree or not. Also, if it gets interrupted, it can just resume where it left off. Now, if you are a Claude code user, you might be thinking that you can already do all of these things yourself. So, what's the whole point of this new dynamic workflows? So, think about a question like this. Should we migrate our checkout services to a new provider? The old way was a static workflow. You use the agent SDK or Claude -p to wire it together ahead of time, so it has to stay generic. Now, it turns that question into five web searches and a generic report. A dynamic workflow fits it. With Opus 4.8, Claude is finally good enough to write the harness at runtime, which is going to be custom-built for that specific task. So, for example, for the same question, it's going to read your billing code, pricing at your real volume, even argue the other side, and hands you a specific recommendation, which is going to be custom-built for this specific task at hand. Okay, so Anthropic just published a very interesting blog post exactly on this specific topic. And they looked at specific patterns, which I'm going to show you in the rest of the video. Now, the beauty of these patterns is that you can implement them in any coding agent. Now, according to Anthropic, when Claude is building these harnesses, there are six different patterns that it uses in order to build a custom harness. The first one is classify and act. So, in this case, when a a new task comes in, a classified agent decide what type of task this is. And then it routes it to a different agents from there. So, you can think that a bug is going to go to a fixer, a question is going to go to an answer, right? And we have seen this pattern. There are routing techniques that people use in order to route different queries. But, you can also put the classifier at the very end to shape the final output. Okay, the second is what they're calling fan out and synthesize. So, in this case, you can take a task and split it across many agent all at once. Now, each one runs its own context window, so they do not contaminate each other. And hence, the biases are not spread across all the agents. Then, a synthesize step acts as a barrier. It waits for every agent to finish and merges their results into one. Now, you want to use this whenever each piece of the work needs its own clean context window. Now, this third pattern is what makes it different from agent teams. So, let's say one agent, the worker, produces something. Then, there's going to be a completely separate agent, which we're going to call the critic, is going to attack it against a rubric and the output is going to be only kept if it survives the critique. Now, you can think about this as a direct cure for the self-referential bias from earlier because the critic has no attachment to the answer. You usually have a planner, executor, and then a verifier with it with serial reviews. Okay, so the fourth pattern is generate and filter. Now, in this case, you generate a whole pile of candidates, then you run them through a filter. Say it's a rubric or by actual verification and dedupe the repeats. Now, after this filtering, only the best results are going to come out. So, in this case, you're running multiple different hypothesis, testing them, and then keeping only the best. Now, this pattern is great for naming, for design, or anything where taste matters. Okay, so the fifth pattern is tournament. Instead of dividing the work, the agent competes. Now, this one is very interesting. So, you spawn multiple different agents that attempt to solve the same task in different ways. Then, there's going to be a judge which compares two of them at a time and the winner advances to the next stage. Now, you repeat this pattern until there's only one champion left. Now, here's the beauty. Comparing two things head-to-head is more reliable than asking for an absolute score and it is also how you sort 1,000 items that would never fit in one prompt. So, this is a good pattern to use if you want to use these LLMs as a judge. Okay, so the sixth one is a loop until done. And the idea is when you when you don't know how much work there is, you don't guess a number of passes. So, in this case, an agent runs, and then uh there's a gate or a conditional state- a statement, which asks, "Are there any new findings?" If the answer is yes, it is going to create another uh pass. And if the answer is no, then it's going to be done. So, the loop decides when it finishes, not uh tired contacts window. And that is the cure for agentic laziness. Okay. So, in the last video, I said that this works great for coding tasks, which is true, but I was kind of wrong on uh the premises that it's not going to work well if the task is not well-defined. According to Anthropic, it does work. So, some of the examples that they have presented in the blog post is ranking resumes during a hiring process, and looking for uh uh let's say the top 10 candidate. On the strategy side, it can tear your business plan apart into three different angles. I'm going to put a link to the blog post, where you can actually see some example prompts. Now, you can also use this to improve your own coding agents. So, for example, you can ask it to mine my last 50 session actions and turn the connections into Claude.md rules. Or, some people are using it to analyze messy operation, like dig through 6 months of Slack and find root causes nobody filed a ticket for. Now, these are not coding examples, but seems like you can use dynamic workflows for a task like this. Now, the beauty is that each one of those jobs maps onto one of the patterns we just covered. So, for example, verification is one agent pulling every claim out of a document and another checking each one. If you look at triage plus quarantine, so triage is classifying and deduplication of backlogs with a new to security trick called quarantine where the agent reading untrusted contents are not allowed to act on it. Now, another example would be sorting a thousand support tickets. That basically becomes a pairwise tournament. Similarly, root cause work generates hypothesis from separate piles of evidence with a classifier that can even pick which model to use. Now, the beauty is that dynamic workflows can generate specific harnesses for these tasks on the fly. And also, you can reuse those harnesses again. It's not that once you use them, they are gone. They are artifacts that are going to be within your Claude. Okay, now I coded how exactly you can use this in my last video, but you can simply ask Claude and say like ultra code or workflow and it's going to trigger it for you. There's another thing. You can cap the cost right in the prompt, something like use only 10,000 tokens. And you can also pair this with {slash} loop or {slash} Claude to run it on a schedule with a hard finish line. Okay, but before you go there, this is going to burn through your tokens. And most tasks don't need a panel of five reviewers. So, always ask yourself whether the job really needs more compute or it can be done with a simple agentic pattern. Okay, so let me show you a quick example of this. Uh for more detail uh demonstration, I'll highly recommend you check out my last video. Let's say we want to rank 80 different resumes. Now in the prompt you just need to include the keyword workflow. And it's going to automatically dispatch a workflow for you. The workflow basically is a custom harness for this specific task. And you can try multiple of these and then whenever you get the best one, you can just save that. And that becomes your custom harness for this specific task. Now one problem with this is that if you actually want to use the word workflow in some other context, Claude will usually misunderstands it and will trigger a workflow, which I think is a really bad design pattern. They shouldn't be including these things in the system prompt or at least should have a special tokens for them. The other way you can do it is just go to the effort and set it to ultra code. That also triggers the workflow. Now for the last couple of years we have had one harness specifically designed for coding and we have pushed it through everything else. Dynamic workflows let to Claude build a new one for each task as I showed you in this video. And I think this is a pattern that we're going to see more and more especially when these companies are pushing for building super apps. Now to be honest we don't know all the best uses yet. So try it out on messy non-code work you have been forcing through according to and see what happens. But keep in mind the token cost is going to be pretty dramatic. Anyways, I hope you found this video useful. Thanks for watching and as always see you in the next one.

---

## Timestamped Segments

**[0:00]** Okay, so harness is like Claude code and

**[0:03]** Codex are designed for coding tasks, but

**[0:06]** the people are now using them for a lot

**[0:08]** more than coding including all kind of

**[0:10]** knowledge work. But the thing is that

**[0:12]** all of this still gets funneled into one

**[0:14]** harness that was built for coding.

**[0:17]** And for these non-coding jobs, this

**[0:19]** harness is not the optimal one. So, what

**[0:22]** if

**[0:24]** instead of forcing your task through it,

**[0:26]** Claude code could write its own harness

**[0:28]** custom for your task on the fly

**[0:32]** right in front of you. This is what

**[0:34]** exactly dynamic workflows are. I covered

**[0:37]** how they're different from agents

**[0:39]** last time. So, today

**[0:41]** it's all about one idea, a custom

**[0:44]** harness for every task on the fly. Now,

**[0:47]** the question is going to be why even

**[0:48]** bother building custom harness for every

**[0:51]** task when one Claude works on your task,

**[0:55]** everything it touches lands in that

**[0:57]** single context window. Now, when a big

**[1:00]** messy job, that windows fill up and

**[1:03]** start hitting a ceiling that impacts the

**[1:05]** performance of your model or agent. Now,

**[1:08]** there are usually three failure modes

**[1:10]** that you will notice. The first one is

**[1:12]** agentic laziness. This is where it quits

**[1:15]** early and calls the job done after

**[1:17]** partial work like a security review

**[1:20]** where it handles 35 of 50 tasks.

**[1:24]** The second one is self-preferential bias

**[1:28]** where it grades its own work too kindly

**[1:31]** the moment you ask it to check itself.

**[1:34]** And the third one is gold drift where

**[1:37]** the original brief slowly leaks out,

**[1:40]** especially after the context gets

**[1:42]** compacted. Now, the fix for all of these

**[1:45]** is that stop running the whole job in

**[1:47]** one context and split it across separate

**[1:50]** clean ones. Okay, so a potential

**[1:52]** solution to this is dynamic workflow. In

**[1:55]** this video, I want to talk about what

**[1:57]** exactly they are.

**[1:58]** For more details, watch my previous

**[2:01]** video. So, it's just a JavaScript file

**[2:03]** that runs a small team of Claude's. Now,

**[2:06]** if you break it down, there is a script

**[2:09]** and it has a few special function.

**[2:12]** The main one is agent, which spawns one

**[2:15]** sub agent within its own clean context

**[2:18]** window. Then there is parallel, uh which

**[2:20]** pans a bunch of them out

**[2:23]** at once and wait for all of them to

**[2:25]** finish. And a pipeline, which streams a

**[2:28]** list of items through a chain of stages.

**[2:31]** Now, on top of all of this, the workflow

**[2:34]** picks which model each agent is going to

**[2:37]** run and whether it gets its own work

**[2:40]** tree or not. Also, if it gets

**[2:42]** interrupted, it can just resume where it

**[2:46]** left off. Now, if you are a Claude code

**[2:48]** user, you might be thinking that you can

**[2:50]** already do all of these things yourself.

**[2:53]** So, what's the whole point of

**[2:56]** this new dynamic workflows? So,

**[2:59]** think about a question like this. Should

**[3:01]** we migrate our checkout services to a

**[3:04]** new provider? The old way was a static

**[3:08]** workflow. You use the agent SDK or

**[3:10]** Claude -p to wire it together ahead of

**[3:14]** time, so it has to stay generic. Now, it

**[3:19]** turns that question into five web

**[3:21]** searches and a generic report. A dynamic

**[3:24]** workflow fits it. With Opus 4.8, Claude

**[3:27]** is finally good enough to write the

**[3:29]** harness at runtime,

**[3:31]** which is going to be custom-built for

**[3:33]** that specific task. So, for example, for

**[3:36]** the same question,

**[3:38]** it's going to read your billing code,

**[3:40]** pricing at your

**[3:42]** real volume, even argue

**[3:45]** the other side, and hands you a specific

**[3:47]** recommendation, which is going to be

**[3:50]** custom-built for this specific task at

**[3:52]** hand. Okay, so Anthropic just published

**[3:55]** a very interesting blog post exactly on

**[3:58]** this specific topic. And they looked at

**[4:00]** specific patterns, which I'm going to

**[4:03]** show you in the rest of the video. Now,

**[4:05]** the beauty of these patterns is that you

**[4:07]** can implement them in any coding agent.

**[4:10]** Now, according to Anthropic, when Claude

**[4:12]** is building these harnesses, there are

**[4:14]** six different patterns that it uses in

**[4:17]** order to build a custom harness. The

**[4:19]** first one is classify and act. So, in

**[4:23]** this case, when a a new task comes in, a

**[4:25]** classified agent decide what type of

**[4:28]** task this is.

**[4:29]** And then it routes it to a different

**[4:32]** agents from there. So, you can think

**[4:35]** that a bug is going to go to a fixer, a

**[4:38]** question is going to go to an answer,

**[4:40]** right? And we have seen this pattern.

**[4:42]** There are routing techniques that people

**[4:45]** use in order to route different queries.

**[4:48]** But, you can also put the classifier at

**[4:50]** the very end to shape the final output.

**[4:53]** Okay, the second is what they're calling

**[4:54]** fan out and synthesize. So, in this

**[4:58]** case, you can take a task and split it

**[5:00]** across many agent all at once.

**[5:03]** Now, each one runs its own context

**[5:06]** window,

**[5:07]** so they do not contaminate each other.

**[5:10]** And hence, the biases are not spread

**[5:12]** across all the agents.

**[5:14]** Then, a synthesize step acts as a

**[5:17]** barrier. It waits for every agent to

**[5:19]** finish and merges their results into

**[5:21]** one. Now, you want to use this whenever

**[5:25]** each piece of the work needs its own

**[5:27]** clean context window. Now, this third

**[5:29]** pattern is what makes it different from

**[5:33]** agent teams. So, let's say one agent,

**[5:37]** the worker, produces something. Then,

**[5:40]** there's going to be a completely

**[5:41]** separate agent, which we're going to

**[5:44]** call the critic, is going to attack it

**[5:47]** against a rubric and the output is going

**[5:50]** to be only kept if it survives the

**[5:52]** critique. Now, you can think about this

**[5:54]** as a direct cure for the

**[5:56]** self-referential bias from earlier

**[5:58]** because the critic has no attachment to

**[6:01]** the answer.

**[6:02]** You usually have a planner, executor,

**[6:04]** and then a verifier with it with serial

**[6:07]** reviews.

**[6:08]** Okay, so the fourth pattern is generate

**[6:11]** and filter. Now, in this case, you

**[6:14]** generate a whole pile of candidates,

**[6:17]** then you run them through a filter. Say

**[6:20]** it's a rubric

**[6:21]** or by actual verification and dedupe the

**[6:25]** repeats. Now, after this filtering, only

**[6:28]** the best results are going to come out.

**[6:31]** So, in this case, you're running

**[6:32]** multiple different hypothesis, testing

**[6:34]** them, and then keeping only the best.

**[6:38]** Now, this pattern is great for naming,

**[6:40]** for design, or anything where taste

**[6:43]** matters.

**[6:44]** Okay, so the fifth pattern is

**[6:46]** tournament. Instead of dividing the

**[6:48]** work, the agent

**[6:50]** competes. Now, this one is very

**[6:53]** interesting.

**[6:54]** So, you spawn multiple different agents

**[6:58]** that attempt to solve

**[7:00]** the same task

**[7:02]** in different ways. Then, there's going

**[7:04]** to be a judge

**[7:06]** which compares two of them at a time

**[7:10]** and the winner advances to the next

**[7:12]** stage.

**[7:13]** Now, you repeat this pattern until

**[7:15]** there's only one champion left. Now,

**[7:17]** here's the beauty. Comparing two things

**[7:19]** head-to-head is more reliable than

**[7:22]** asking for an absolute score

**[7:24]** and it is also how you sort 1,000 items

**[7:28]** that would never fit in one prompt. So,

**[7:31]** this is a good pattern to use if you

**[7:33]** want to use these LLMs as a judge. Okay,

**[7:36]** so the sixth one

**[7:38]** is a loop until done.

**[7:41]** And the idea is when you when you don't

**[7:43]** know how much work there is, you don't

**[7:46]** guess a number of passes.

**[7:48]** So, in this case, an agent runs, and

**[7:50]** then uh there's a gate or a conditional

**[7:53]** state- a statement, which asks, "Are

**[7:55]** there any new findings?"

**[7:57]** If the answer is yes, it is going to

**[8:00]** create another uh pass. And if the

**[8:03]** answer is no, then it's going to be

**[8:05]** done. So, the loop decides when it

**[8:08]** finishes, not uh

**[8:10]** tired contacts window.

**[8:12]** And that is the cure for agentic

**[8:14]** laziness. Okay. So, in the last video, I

**[8:17]** said that this works great for coding

**[8:19]** tasks, which is true,

**[8:22]** but I was kind of wrong on uh the

**[8:24]** premises that it's not going to work

**[8:26]** well

**[8:27]** if the task is not well-defined.

**[8:29]** According to Anthropic, it does

**[8:32]** work. So, some of the examples that they

**[8:35]** have presented in the blog post is

**[8:37]** ranking resumes during a hiring process,

**[8:41]** and looking for uh uh let's say the top

**[8:43]** 10 candidate.

**[8:44]** On the strategy side, it can tear your

**[8:47]** business plan apart into three different

**[8:50]** angles.

**[8:51]** I'm going to put a link to the blog

**[8:53]** post, where you can actually see some

**[8:55]** example prompts. Now, you can also use

**[8:58]** this to improve your own coding agents.

**[9:00]** So, for example, you can ask it to mine

**[9:02]** my last 50 session actions and turn the

**[9:06]** connections into Claude.md rules. Or,

**[9:09]** some people are using it to analyze

**[9:12]** messy operation, like dig through 6

**[9:14]** months of Slack and find root causes

**[9:16]** nobody filed a ticket for.

**[9:19]** Now, these are not coding examples, but

**[9:22]** seems like you can use dynamic workflows

**[9:25]** for a task like this. Now, the beauty is

**[9:27]** that each one of those jobs maps

**[9:30]** onto one of the patterns we just

**[9:32]** covered.

**[9:33]** So, for example, verification is one

**[9:35]** agent pulling every

**[9:37]** claim out of a document and another

**[9:40]** checking each one. If you look at triage

**[9:44]** plus quarantine, so triage is

**[9:45]** classifying and deduplication

**[9:49]** of backlogs

**[9:51]** with a new to security trick called

**[9:52]** quarantine where the agent reading

**[9:55]** untrusted contents are not allowed to

**[9:58]** act on it. Now, another example would be

**[10:00]** sorting a thousand support tickets. That

**[10:03]** basically becomes a pairwise tournament.

**[10:06]** Similarly, root cause work generates

**[10:08]** hypothesis from separate piles of

**[10:11]** evidence with a classifier that can even

**[10:15]** pick which model to use.

**[10:17]** Now, the beauty is that dynamic

**[10:20]** workflows can generate specific

**[10:23]** harnesses for these tasks on the fly.

**[10:26]** And also, you can reuse those harnesses

**[10:29]** again. It's not that

**[10:31]** once you use them, they are gone. They

**[10:33]** are artifacts that are going to be

**[10:35]** within your Claude. Okay, now I coded

**[10:37]** how exactly you can use this in my last

**[10:40]** video, but you can simply ask Claude and

**[10:44]** say like ultra code or workflow and it's

**[10:46]** going to trigger it for you.

**[10:49]** There's another thing. You can cap the

**[10:51]** cost right in the prompt, something like

**[10:54]** use only

**[10:55]** 10,000 tokens.

**[10:57]** And you can also pair this with {slash}

**[11:00]** loop or {slash} Claude to run it on a

**[11:02]** schedule with a hard finish line.

**[11:06]** Okay, but before you go there, this is

**[11:08]** going to burn through your tokens.

**[11:11]** And most tasks don't need a panel of

**[11:13]** five reviewers.

**[11:15]** So, always ask yourself whether the job

**[11:17]** really needs more compute or it can be

**[11:20]** done with a simple agentic pattern.

**[11:24]** Okay, so let me show you a quick example

**[11:26]** of this. Uh for more detail

**[11:29]** uh demonstration, I'll highly recommend

**[11:31]** you check out my last video.

**[11:33]** Let's say we want to rank 80 different

**[11:36]** resumes. Now in the prompt you just need

**[11:38]** to include the keyword workflow.

**[11:42]** And it's going to automatically dispatch

**[11:45]** a workflow for you. The workflow

**[11:48]** basically is a custom harness for this

**[11:50]** specific task. And you can try multiple

**[11:53]** of these and then whenever you get the

**[11:55]** best one, you can just save that. And

**[11:58]** that becomes your custom harness for

**[12:01]** this specific task. Now one problem with

**[12:04]** this is that if you actually want to use

**[12:07]** the word workflow in some other context,

**[12:10]** Claude will usually misunderstands it

**[12:14]** and will trigger a workflow, which I

**[12:17]** think is a really bad design pattern.

**[12:19]** They shouldn't be including these things

**[12:21]** in the system prompt or at least should

**[12:24]** have a special tokens for them. The

**[12:27]** other way you can do it is just go to

**[12:29]** the effort and set it to ultra code.

**[12:33]** That also

**[12:34]** triggers the workflow. Now for the last

**[12:36]** couple of years we have had one harness

**[12:39]** specifically designed for coding and we

**[12:42]** have pushed it through everything else.

**[12:44]** Dynamic workflows let to Claude build

**[12:47]** a new one for each task as I showed you

**[12:50]** in this video.

**[12:51]** And I think this is a pattern that we're

**[12:54]** going to see more and more especially

**[12:57]** when these companies are pushing for

**[13:00]** building super apps. Now to be honest we

**[13:03]** don't know all the best uses yet.

**[13:07]** So try it out on messy non-code work you

**[13:10]** have been forcing through according to

**[13:13]** and see what happens. But keep in mind

**[13:16]** the token cost is going to be pretty

**[13:18]** dramatic. Anyways, I hope you found this

**[13:20]** video useful. Thanks for watching and as

**[13:22]** always see you in the next one.
