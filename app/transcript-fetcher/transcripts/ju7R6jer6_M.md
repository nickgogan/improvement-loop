# Transcript: Stop Building AI Agents the Old Way

**URL:** https://www.youtube.com/watch?v=ju7R6jer6_M
**Segments:** 385
**Channel:** Prompt Engineering
**Duration:** 14:50
**Uploaded:** 2026-07-03

---

## Full Text

Long running agents, that's what we're going to be talking about in this video. Because we're seeing a lot of companies that are claiming that their agents can run for hours or days completely on their own without any supervision. Which is pretty great, but as a developer, you want to know how to design it, what components are needed, and how to keep it in check so it doesn't go off the rails. Now, I think there are seven different components that you need for any long running agent. In this video, we're going to go through them and also talk about how exactly to design each one of those. Okay, so you start with the agent that is basically the executor. Now, this is the core component, but on its own, it will drift, take shortcuts, or just stop. Now, in order to keep this agent running for much longer time horizon, you need to wrap it around seven different things. The first one is going to be a goal. The second one is an evaluator. Third are verifiers. Fourth are loops, which are different than the loop inside the agent. Fifth is going to be the orchestration. Sixth is the observability. And seventh is the memory. Now, we're going to have a deeper dive into each one of them to explain how exactly you should think about it. So, if you're designing a long running agent, the first component that you need to think about is the goal. Now, the key principle here is that the goal is more than a prompt. It's really a contract between you and the agent. So, instead of telling what to do step-by-step, you define the end state. What done actually looks like. You need to define the clear success criteria and the constraints it cannot break. And a budget for how much it can spend. Now, based on this goal, the agent goes and does the work. But the main idea is that now it has something really concrete to measure itself against. And this matters because a vague goal is dangerous. Say, add a settings page is the goal. It will build something, call it done, and move on, even if half of it is broken. But, if you say something like match this design, save every setting, and pass this test, now it has a measurable goal. This is the most important thing that a lot of people avoid. If you cannot clearly define what the success criteria looks like, and it's not measurable, these systems are going to make a lot of assumptions, will implement things that are not what you want, and you're going to be stuck in a loop. Okay, so you set a goal, then you need to have an evaluator or a judge which can actually verify the work. So, on one side, you have got the agent doing the work. Say, it's writing the code, and then a separate evaluator checks it. Now, here's the most important part. The agent that did the work should not be the one that is grading it. And the evaluator should be just looking at the initial specs and the final output and provides a verdict. It shouldn't be sharing the same context with the agent that is implementing the work. Otherwise, you are going to get a biased evaluator. Now, if it passes the tests, great. If not, it goes back for another pass. Okay, so how does it check if the success is clear-cut? You can use deterministic checks like tests, types, linting, et cetera. But, if the outcome is fuzzy, then you need to look at is it well written? Does this look right? So, you will need to use another agent as a judge. Now, the main theory here is that great evaluators setups use both deterministic checks as the baseline and then agent reviews on top of them. Now, let's talk a little more about the verifiers because this is the component that actually keeps your agent in check. Now, an agent can confidently tell you that it has finished some work, but that explanation is not the proof. So, when you designing these checks, you want to do it in two different steps. The first one is going to be cheap and deterministic. Simple verifiers are does it compile? Does it pass the test? Length types etc. And then you can have more expensive ones like a benchmark screenshot comparisons and held out evaluation. And only what clears those checks are actually acceptable as done. Now, think of this as a climbing anchor. The agent can feel sure all it wants, but the anchor either holds or it doesn't. Now, the most important thing to keep in mind is that your verifiers evaluators needs to be really clear cut. They cannot be vague. Treat this as a boundary for the agent to say that it has done the work. Okay, the next component is the outer loop. Uh because agents tends to stop uh when they hit the limit, maybe lose track, or decide a half-finished answer is good enough. You want to have a control mechanism. And to do that, you simply put them inside a loop that wakes them up. The idea is that these loops are going to check the progress and compare them against the goal that you define in the beginning. Then, they ask whether the goal is actually met. If done, you mark it as a complete. If not, it sends the agent back with the failures and runs again. The simplest version of this is the rough loop. Now, a more advanced version of this is an evaluator inside the loop that can re-plan and escalate back to you. So, the key idea here is that we're not looking for a long-running agent that is simply thinking for us. We're looking for one that is taking short attempts supervised by this loop and then refine its approach if needed. If you look at something like /goal and codex or cloud code, they are basically implementing this loop pattern. Now, here's the thing with the long-running loops. Your agent can run for hours completely unattended. But, can you actually see what exactly is happening? Because you can't baby sit it for 6 hours. This is where today's sponsor, Latitude, comes into play. It's an open-source observability for agents. It does three very simple things. It lets you see what your agent is doing, catches what's breaking, and lets you fix things. And it's fully open-source MIT licensed. This gives you complete visibility into your production systems by letting you see what your agent is doing. Every run is fully traced in terms of cost, latency, and whole span tree. And you can search your traces in plain English. It clusters thousands of conversations into one single picture. For example, you can look at what people are asking and why they are dropping off. Now, second, you can catch what is breaking before your users realize. So, for example, here's the issue view. When your agent fails the same way over and over, it collapses that into a single signal. Not only it clusters them, but it can even write an eval for that exact failure automatically. You can also save a search as a monitor, so it's going to run on every new conversation. And the third is that you can fix it without ever leaving your editor. There is an MCB server that wires Latitude straight into your coding agent, whether it's Codex or cloud code or any IDE. So, you pull the real failing traces right into the editor. Turn those production failures into a data set and verify the fix actually worked before you ship it. And like I said, this is fully open source MIT license. Link to the GitHub repo is going to be in the video description. There is even a hosted solution if you don't want to run it on your own premises. So, definitely check out Latitude. Your agent needs observability. Now, back to the video. Okay, next we're going to talk about the orchestration layer. So, once you define the goal, the main idea here is that you should stop thinking about the model, but rather think about the roles. So, you want a strong model for planning, then a fast and cheaper model for execution, and then a capable model that can do evaluation. And you want to repeat this pattern inside a loop. So, instead of one model for everything, you assign the right model to each role. Model choice becomes an architecture decision in this case. This is not only going to keep your execution flow in check, but also it's going to keep the cost low. Now, the main idea here is that planning is the step where your expertise matter the most. You as the human in the loop are going to review the plan and sharpen it before handing it to the loop. If you have a really really good plan with capable models, you'll be able to execute it really effectively. The core idea is that you don't want to outsource your thinking to the model. Okay, so the next component is observability. So, let's say once you have got agents running for hours, maybe several at a time, you can't be really looking at the text output or raw transcript. This is where the idea of orchestration tax comes into play. So, you separate the storage from presentation. The raw logs and data lives somewhere the agent can search and then you want a clean dashboard that it renders just specifically for you. Think about this as a Kanban board or something like a linear dashboard. You can see the tasks, the costs, the errors, screenshots, and the key decisions. And that's what lets you decide when to step in instead of finding out when it's all over. This is where the today's sponsor, Latitutde, also comes into play. Now, this also should give you the mechanism of providing feedback. So, observability is your control surface, not a report you read after the fact. And this is more important than people realize, especially for long-running agents that need human in the loop. Now, the last component we're going to talk about is memory. It's not only for the agent to remember your preferences. Actually, your past agent runs are basically free training data, but most people just throw them away. Now, here is an idea called session mining. And in this, you want to simply go back through recent runs and look for patterns. Now, when you're designing agents, you'll find that the same mistakes keep repeating. You'll probably find similar failed checks and wrong paths. These are kind of patterns that you want to mine because this is really a signal for your agent. So, the idea would be that you turn these into rules. You write them into your project instruction or agent's configuration. Or simply have them as rules in your agent.md or prompt.md. And the idea would be that during the next run, the agent agent should not repeat the same mistakes. This is kind of a naive version of recursive self-improvement plan for one specific agent that a lot of people don't really take advantage of. Now, in practice, here's kind of the workflow that I would put together. So, start small and cheap. Prove it on something you can check in a couple of minutes. Then write a clear measurable goal. Separate your execution from your evaluator. Define your verifiers before you start the loop. In this, you want deterministic checks first and then agent reviews on top. You want to make sure you require proof. These could be logs, screenshots, and actual changes. Make sure to mine your sessions for lessons. And do those and you have gone from just using an agent to actually engineering one. Okay, but here's the most important takeaway. None of this makes the hard problems disappear. Agents still take shortcuts. They will stop early and write weak plans, especially on stuff outside their training data. But each of those failures has a component that catches it. Say, if they're taking shortcuts, the verifiers can help. With early stopping, You can have the loop if the agent is making weak plans. You review if you see over fitting. You probably want to look at held out e walls. If you have a sale contacts, you probably want to look at memory. Now, you want to put them together and you want to create a system that actually has controls. Now, a lot of people have tried to run hundreds of thousands of agents, but the main idea is you don't want to trust them. You want to design systems around them which are going to keep them in check. Basically, this needs to be observable and correctable. And this is going to help you actually achieve your goal. Okay, so here's a quick recap. The seven components are a goal, an evaluator, a verifier, a loop, orchestration, observability, and memory, and the agent itself is just the engine. It's the whole system around it that lets it run on its own and stay reliable. If you're building long running agents, simply starts with these seven different components. Do let me know what you think about what are some other components that I might have missed in this video. Anyways, I hope you found this video useful. Thanks for watching and as always, see you in the next one.

---

## Timestamped Segments

**[0:00]** Long running agents, that's what we're

**[0:02]** going to be talking about in this video.

**[0:04]** Because we're seeing a lot of companies

**[0:06]** that are claiming that their agents can

**[0:07]** run for hours or days

**[0:09]** completely on their own without any

**[0:11]** supervision.

**[0:13]** Which is pretty great, but as a

**[0:14]** developer, you want to know how to

**[0:16]** design it, what components are needed,

**[0:18]** and how to keep it in check so it

**[0:21]** doesn't go off the rails.

**[0:22]** Now, I think there are seven different

**[0:24]** components that you need for any long

**[0:27]** running agent. In this video, we're

**[0:29]** going to go through them and also talk

**[0:30]** about how exactly to design each one of

**[0:33]** those. Okay, so you start with the agent

**[0:36]** that is basically the executor. Now,

**[0:39]** this is the core component, but on its

**[0:41]** own, it will drift, take shortcuts, or

**[0:44]** just stop. Now, in order to keep this

**[0:46]** agent running for

**[0:48]** much longer time horizon, you need to

**[0:51]** wrap it around seven different things.

**[0:53]** The first one is going to be a goal. The

**[0:56]** second one is an evaluator.

**[0:58]** Third are verifiers. Fourth are loops,

**[1:01]** which are different than the loop inside

**[1:04]** the agent.

**[1:05]** Fifth is going to be the orchestration.

**[1:08]** Sixth is the observability. And seventh

**[1:10]** is the memory.

**[1:12]** Now, we're going to have a deeper dive

**[1:14]** into each one of them to explain how

**[1:17]** exactly you should think about it. So,

**[1:20]** if you're designing a long running

**[1:21]** agent, the first component that you need

**[1:23]** to think about is the goal. Now, the key

**[1:26]** principle here is that the goal is more

**[1:28]** than a prompt. It's really a contract

**[1:30]** between you and the agent.

**[1:34]** So, instead of telling what to do

**[1:36]** step-by-step, you define the end state.

**[1:39]** What done actually looks like.

**[1:42]** You need to define the clear success

**[1:45]** criteria and the constraints it cannot

**[1:47]** break. And a budget for how much it can

**[1:50]** spend. Now, based on this goal, the

**[1:52]** agent goes and does the work.

**[1:55]** But the main idea is that now it has

**[1:57]** something really concrete to measure

**[2:00]** itself against.

**[2:01]** And this matters because a vague goal is

**[2:04]** dangerous. Say, add a settings page is

**[2:08]** the goal. It will build something, call

**[2:10]** it done, and move on, even if half of it

**[2:13]** is broken.

**[2:15]** But, if you say something like match

**[2:16]** this design,

**[2:18]** save every setting, and pass this test,

**[2:21]** now it has a measurable goal. This is

**[2:24]** the most important thing that a lot of

**[2:25]** people avoid. If you cannot clearly

**[2:28]** define what the success criteria looks

**[2:30]** like, and it's not measurable, these

**[2:34]** systems are going to make a lot of

**[2:35]** assumptions, will implement things that

**[2:39]** are not what you want, and you're going

**[2:41]** to be stuck in a loop. Okay, so you set

**[2:43]** a goal, then you need to have an

**[2:45]** evaluator or a judge which can actually

**[2:48]** verify the work. So, on one side, you

**[2:51]** have got the agent doing the work.

**[2:54]** Say, it's writing the code,

**[2:56]** and then a separate evaluator checks it.

**[2:59]** Now, here's the most important part. The

**[3:02]** agent that did the work should not be

**[3:05]** the one that is grading it. And the

**[3:07]** evaluator should be just looking at the

**[3:09]** initial specs

**[3:10]** and the final output and provides a

**[3:13]** verdict. It shouldn't be sharing the

**[3:16]** same context with the agent that is

**[3:18]** implementing the work. Otherwise, you

**[3:21]** are going to get a biased evaluator.

**[3:24]** Now, if it passes the tests, great. If

**[3:28]** not,

**[3:29]** it goes back for another pass.

**[3:31]** Okay, so how does it check if the

**[3:33]** success is clear-cut? You can use

**[3:36]** deterministic checks like tests, types,

**[3:39]** linting, et cetera. But, if the outcome

**[3:43]** is fuzzy, then you need to look at is it

**[3:45]** well written? Does this look right? So,

**[3:48]** you will need to use another agent as a

**[3:51]** judge.

**[3:52]** Now, the main theory here is that great

**[3:56]** evaluators setups use both deterministic

**[3:59]** checks as the baseline and then agent

**[4:02]** reviews on top of them. Now, let's talk

**[4:05]** a little more about the verifiers

**[4:07]** because this is the component that

**[4:09]** actually keeps your

**[4:11]** agent in check. Now, an agent can

**[4:13]** confidently tell you that it has

**[4:15]** finished some work, but that explanation

**[4:17]** is not the proof.

**[4:19]** So, when you designing these checks, you

**[4:22]** want to do it in two different steps.

**[4:24]** The first one is going to be cheap and

**[4:26]** deterministic.

**[4:27]** Simple

**[4:29]** verifiers are does it compile? Does it

**[4:31]** pass the test? Length types etc.

**[4:35]** And then you can have more

**[4:38]** expensive ones like a benchmark

**[4:40]** screenshot comparisons and held out

**[4:43]** evaluation. And only what clears those

**[4:45]** checks are actually acceptable as done.

**[4:49]** Now, think of this as a climbing anchor.

**[4:51]** The agent can feel sure

**[4:53]** all it wants, but the anchor either

**[4:57]** holds or it doesn't. Now, the most

**[4:59]** important thing to keep in mind is that

**[5:01]** your verifiers evaluators needs to be

**[5:04]** really clear cut. They cannot be vague.

**[5:08]** Treat this as a boundary for the agent

**[5:11]** to say that it has done the work. Okay,

**[5:13]** the next component is the outer loop. Uh

**[5:16]** because agents tends to stop uh when

**[5:19]** they hit the limit, maybe lose track, or

**[5:21]** decide a half-finished answer is good

**[5:23]** enough. You want to have a control

**[5:26]** mechanism.

**[5:27]** And to do that, you simply put them

**[5:28]** inside a loop that wakes them up. The

**[5:32]** idea is that these loops are going to

**[5:34]** check the progress and compare them

**[5:36]** against the goal that you define in the

**[5:38]** beginning. Then, they ask whether the

**[5:41]** goal is actually met.

**[5:44]** If done,

**[5:45]** you mark it as a complete.

**[5:48]** If not, it sends the agent back with the

**[5:51]** failures and runs again.

**[5:54]** The simplest version of

**[5:56]** this is the rough loop. Now, a more

**[5:59]** advanced version of this is an evaluator

**[6:01]** inside the loop that can re-plan and

**[6:03]** escalate back to you.

**[6:06]** So, the key idea here is that we're not

**[6:08]** looking for a long-running agent

**[6:10]** that is simply thinking for us.

**[6:13]** We're looking for one that is taking

**[6:15]** short attempts supervised by this loop

**[6:17]** and then refine its approach if needed.

**[6:20]** If you look at something like /goal and

**[6:22]** codex or cloud code, they are basically

**[6:25]** implementing this loop

**[6:28]** pattern.

**[6:29]** Now, here's the thing with the

**[6:30]** long-running loops. Your agent can run

**[6:32]** for hours completely unattended.

**[6:35]** But, can you actually see what exactly

**[6:36]** is happening? Because you can't baby sit

**[6:38]** it for 6 hours.

**[6:40]** This is where today's sponsor, Latitude,

**[6:42]** comes into play. It's an open-source

**[6:44]** observability for agents.

**[6:46]** It does three very simple things. It

**[6:48]** lets you see what your agent is doing,

**[6:50]** catches what's breaking, and lets you

**[6:53]** fix things.

**[6:55]** And it's fully open-source MIT licensed.

**[6:58]** This gives you complete visibility into

**[7:01]** your production systems by letting you

**[7:04]** see what your agent is doing.

**[7:07]** Every run is fully traced

**[7:09]** in terms of cost, latency, and whole

**[7:12]** span tree.

**[7:13]** And you can search your traces in plain

**[7:16]** English.

**[7:17]** It clusters thousands of conversations

**[7:19]** into one single picture.

**[7:22]** For example, you can look at what people

**[7:23]** are asking and why they are dropping

**[7:26]** off.

**[7:27]** Now, second, you can catch what is

**[7:29]** breaking before your users realize.

**[7:33]** So, for example, here's the issue view.

**[7:35]** When your agent fails the same way over

**[7:37]** and over, it collapses that into a

**[7:40]** single signal. Not only it clusters

**[7:43]** them, but it can even write an eval for

**[7:45]** that exact failure automatically. You

**[7:48]** can also save a search as a monitor, so

**[7:50]** it's going to run on every new

**[7:52]** conversation.

**[7:53]** And the third is that you can fix it

**[7:55]** without ever leaving your editor. There

**[7:58]** is an MCB server that wires Latitude

**[8:00]** straight into your coding agent, whether

**[8:02]** it's Codex or cloud code or any IDE.

**[8:06]** So, you pull the real failing traces

**[8:08]** right into the editor.

**[8:11]** Turn those production failures into a

**[8:13]** data set and verify the fix actually

**[8:16]** worked before you ship it.

**[8:19]** And like I said, this is fully open

**[8:21]** source MIT license. Link to the GitHub

**[8:24]** repo is going to be in the video

**[8:25]** description. There is even a hosted

**[8:28]** solution if you don't want to run it on

**[8:31]** your own premises. So, definitely check

**[8:34]** out Latitude.

**[8:36]** Your agent needs observability. Now,

**[8:39]** back to the video. Okay, next we're

**[8:41]** going to talk about the orchestration

**[8:43]** layer.

**[8:44]** So, once you define the goal,

**[8:47]** the main idea here is that you should

**[8:48]** stop thinking about the model, but

**[8:51]** rather think about the roles.

**[8:53]** So, you want a strong model for

**[8:56]** planning,

**[8:57]** then a fast and cheaper model for

**[9:00]** execution, and then a capable model that

**[9:04]** can do evaluation.

**[9:06]** And you want to repeat this pattern

**[9:08]** inside a loop. So, instead of one model

**[9:11]** for everything, you assign the right

**[9:13]** model to each role.

**[9:16]** Model choice becomes an architecture

**[9:18]** decision in this case.

**[9:19]** This is not only going to keep your

**[9:22]** execution flow in check, but also it's

**[9:24]** going to keep the cost low. Now, the

**[9:27]** main idea here is that planning is the

**[9:29]** step where your expertise matter the

**[9:32]** most.

**[9:33]** You

**[9:34]** as the human in the loop are going to

**[9:37]** review the plan and sharpen it before

**[9:40]** handing it to the loop. If you have a

**[9:42]** really really good plan with capable

**[9:44]** models, you'll be able to execute it

**[9:48]** really effectively.

**[9:49]** The core idea is that you don't want to

**[9:52]** outsource your thinking to the model.

**[9:55]** Okay, so the next component is

**[9:56]** observability.

**[9:58]** So, let's say once you have got agents

**[10:00]** running for hours, maybe several at a

**[10:03]** time,

**[10:04]** you can't be really looking at the text

**[10:06]** output

**[10:08]** or raw transcript. This is where the

**[10:10]** idea of orchestration tax comes into

**[10:13]** play.

**[10:14]** So, you separate the storage from

**[10:16]** presentation. The raw logs and data

**[10:19]** lives somewhere the agent can search

**[10:22]** and then you want a clean dashboard

**[10:25]** that it renders just specifically for

**[10:28]** you.

**[10:29]** Think about this as a Kanban board

**[10:31]** or

**[10:32]** something like a linear dashboard.

**[10:35]** You can see the tasks, the costs, the

**[10:37]** errors, screenshots, and the key

**[10:39]** decisions.

**[10:41]** And that's what lets you decide when to

**[10:44]** step in instead of

**[10:46]** finding out when it's all over.

**[10:49]** This is where the today's sponsor,

**[10:50]** Latitutde, also comes into play.

**[10:53]** Now, this also should give you the

**[10:54]** mechanism of providing feedback. So,

**[10:56]** observability is your control surface,

**[10:59]** not a report you read after the fact.

**[11:02]** And this is more important than people

**[11:04]** realize, especially for long-running

**[11:06]** agents that need human in the loop.

**[11:09]** Now, the last component we're going to

**[11:11]** talk about is memory.

**[11:13]** It's not only for the agent to remember

**[11:16]** your preferences.

**[11:18]** Actually, your

**[11:19]** past agent runs are basically free

**[11:22]** training data, but most people just

**[11:24]** throw them away. Now, here is an idea

**[11:26]** called session mining.

**[11:28]** And in this, you want to simply go back

**[11:30]** through recent runs and look for

**[11:32]** patterns.

**[11:33]** Now, when you're designing agents,

**[11:34]** you'll find that the same mistakes

**[11:38]** keep repeating.

**[11:40]** You'll probably find similar failed

**[11:42]** checks and wrong paths. These are kind

**[11:44]** of patterns that you want to mine

**[11:47]** because this is really a signal for your

**[11:50]** agent.

**[11:51]** So, the idea would be that you turn

**[11:53]** these into rules.

**[11:54]** You write them into your project

**[11:57]** instruction or agent's configuration.

**[12:01]** Or simply have them as rules in your

**[12:04]** agent.md or prompt.md.

**[12:07]** And the idea would be that during the

**[12:09]** next run,

**[12:10]** the agent agent should not repeat the

**[12:12]** same mistakes.

**[12:14]** This is kind of a naive version of

**[12:15]** recursive self-improvement plan for one

**[12:18]** specific agent that a lot of people

**[12:20]** don't really take advantage of.

**[12:23]** Now, in practice, here's kind of the

**[12:24]** workflow

**[12:26]** that I would put together.

**[12:28]** So, start small and cheap. Prove it on

**[12:30]** something you can check in a couple of

**[12:32]** minutes.

**[12:33]** Then write a clear measurable goal.

**[12:37]** Separate your execution from your

**[12:39]** evaluator.

**[12:40]** Define your verifiers before you start

**[12:42]** the loop.

**[12:44]** In this, you want deterministic checks

**[12:46]** first and then agent reviews on top.

**[12:49]** You want to make sure you require proof.

**[12:51]** These could be logs, screenshots, and

**[12:53]** actual changes.

**[12:55]** Make sure to mine your sessions for

**[12:57]** lessons.

**[12:58]** And do those and you have gone from just

**[13:01]** using an agent to actually engineering

**[13:03]** one. Okay, but here's the most important

**[13:05]** takeaway. None of this makes the hard

**[13:07]** problems disappear. Agents still take

**[13:10]** shortcuts. They will stop early and

**[13:13]** write weak plans, especially on stuff

**[13:15]** outside their training data.

**[13:17]** But each of those failures has a

**[13:19]** component that catches it.

**[13:22]** Say, if they're taking shortcuts, the

**[13:24]** verifiers can help. With early stopping,

**[13:27]** You can have the loop if the agent is

**[13:30]** making weak plans. You review if you see

**[13:33]** over fitting.

**[13:35]** You probably want to look at held out e

**[13:37]** walls.

**[13:38]** If you have a sale contacts, you

**[13:40]** probably want to look at memory.

**[13:43]** Now, you want to put them together and

**[13:45]** you want to create a system that

**[13:47]** actually has controls.

**[13:49]** Now, a lot of people have tried to run

**[13:52]** hundreds of thousands of agents, but the

**[13:54]** main idea is you don't want to trust

**[13:56]** them. You want to design systems around

**[13:59]** them which are going to keep them in

**[14:01]** check.

**[14:03]** Basically,

**[14:04]** this needs to be observable and

**[14:06]** correctable.

**[14:07]** And this is going to help you actually

**[14:10]** achieve your goal. Okay, so here's a

**[14:11]** quick recap. The seven components are a

**[14:13]** goal, an evaluator, a verifier, a loop,

**[14:16]** orchestration, observability, and

**[14:18]** memory, and the agent itself is just the

**[14:21]** engine.

**[14:22]** It's the whole system around it that

**[14:24]** lets it run

**[14:25]** on its own and stay reliable. If you're

**[14:29]** building long running agents,

**[14:31]** simply starts with these seven different

**[14:33]** components. Do let me know what you

**[14:35]** think about what are some other

**[14:36]** components that I might have missed in

**[14:38]** this video. Anyways, I hope you found

**[14:40]** this video useful. Thanks for watching

**[14:42]** and as always, see you in the next one.
