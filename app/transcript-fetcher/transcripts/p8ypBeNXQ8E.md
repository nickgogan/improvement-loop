# Transcript: Make Fable 5 80% Cheaper (& Other Usage Cheat Codes)

**URL:** https://www.youtube.com/watch?v=p8ypBeNXQ8E
**Segments:** 341
**Channel:** Chase AI
**Duration:** 12:01
**Uploaded:** 2026-07-03

---

## Full Text

What if I told you we could reduce Fable 5's cost by 80% while still beating Opus 4.8? Well, that is just one of five tricks I'm going to show you today that are all about reducing Fable 5's usage and token cost without losing what makes this model great. Because we all know the clock is ticking. We just got a few days left until Fable 5 is kicked off the Pro and the Max plan and we are stuck paying API prices. And on top of that, we're also usage capped. So, it is imperative that we figure out quickly how to get the best bang for the buck with this new model. So, that is exactly what we're going to talk about today and let's dive in. So, tip number one, this is the easiest one and arguably the highest leverage. It is changing the effort level. It is reducing the effort level with Claude Fable 5. Now, by default, we are on high and some of you are crazy out there and I see you pushing it to extra high or even max. And the truth is, you probably do not need that. First of all, what are we looking at here? Well, we're looking at a benchmark. This is Deep Sweet. This is one of my favorite benchmarks. It's all about long horizon, long-running agentic tasks and we see Fable 5 here, Opus 4.8 as well as GPT 5.5. Now, I said in the intro, I said you could reduce cost by 80%. When we look at the max effort level, which by the way doesn't give you that much of an upgrade in terms of, you know, pass percentage from extra high, it's costing us $22. Our average cost per task when looking at Deep Sweet. If we compare that to low, it's $3.76. More than an 80% reduction in cost. Yet, at low effort level with Claude Fable 5, we're doing better than max at Opus 4.8. So, we're at 60% at Fable 5 low and we're at 59% with max Opus 4.8. And Opus in this case is $13 versus $3.76. That's crazy. Like you could argue that's crazier than the jump from 59 to 70. Is the fact we're doing this so much more efficiently. And when we pop up to medium, we're going up from 60% to 65% pass rate. And we go up to high, we're at 69%. And on extra high, we're at 70% versus 59%. But at low, again, we're getting really solid outputs that are extremely cheap. Even compared to GPT 5.5, which honestly is such a sleeper model, it's so good. I'm super excited to use 5.6 when it comes out. It's still doing better than medium. Slightly more expensive, but not by a ton. Now, we see this reflected in other benchmarks as well. Here's a look at frontier code accuracy versus cost. And this is coming from Anthropic itself. So, in the orange, we have Fable. In the green, we have Opus 4.8. And then down here at the bottom, we have 5.5. Look at low. All right, just a shade over $5. And the score is about 11%. If we look at Opus 4.8 on max, it's call it $11. And it's the same exact score percentage. So, I'm getting the same pass rate as Opus 4.8 on max at half the cost. And if I go up to medium, I'm blowing Opus 4.8 out of the water while still being less expensive than extra high, which is where a lot of people sit for just default Opus settings. So, with that in mind, does it make sense for us to sit on the default high level with Fable 5? I think when you look at both of these benchmarks, the answer is probably no. And when we look at Deep Sweep, Deep Sweep is rather complicated tasks. Are you doing something very complicated? The less complicated of the task you're doing, if you're doing web design, you probably should be on medium or low. And that right away is going to reduce your costs and reduce your usage substantially. Substantially. So, out of everything you see today, if nothing else, I want you to try doing a task on medium with Fable. Try doing a task on low and see how well it does. I think you would be surprised and you're not going to get to that 50% of your weekly limit nearly as quickly as you would otherwise. And of course, to change the effort level, all you have to do is go into the terminal, do {forward slash} effort, and then set it where you want to. Now, before we jump into tip number two, quick word from today's sponsor, me. So, I just released my Claude Code Masterclass and it is the number one way to go from zero to AI dev, especially if you don't come from a technical background. We focus on real use cases, it's updated every single week, and it also includes a Codex Masterclass and an Agentic OS Masterclass. So, if you're someone who's really trying to level up your AI game, you want to get serious about this, make sure to check it out. It's inside of Chase AI Plus, there's a link to that in the pinned comment. Now, tip number two when it comes to reducing Fable's usage is also pretty straightforward. And that is stop using Fable to both plan everything and execute everything. Instead, make Fable the architect. Have it come up with the plan and then, depending on the complexity of the plan, have it divvy up the work to the appropriate model. Whether that is Opus, whether that's Sonnet, or it's an outside model. It could be GPT 5.5, it could be something local. Fable's also smart enough to know which model is best for the job. And you can have Fable 5 explicitly call out those models in the plan. So, Fable 5 does the plan, and then it says, "Hey, for the first part, I want Opus. For the second part, Sonnet makes sense. And for the third part, let's send that to OpenAI and bring in GPT 5.5." This is a perfect use case for something like the Codex plugin within Claude Code. And if you haven't used that before, I highly suggest you do. You can totally bring in something like the Codex rescue function and have Fable call on that, too. Give features to GPT 5.5, which again, awesome model. But if all that's too complicated and having it call out all these agents, you can do something as simple as simply throwing it in plan mode, you know, having it come up with the plan, having it create some sort of markdown file, set the stage for your code base, and then simply spinning up another session with Opus and having it execute the plan that Fable laid out. You don't need to overcomplicate it, but that stops Fable from burning a bunch of tokens on low-level tasks that are going to be necessary for, you know, whatever you're creating. Now, tip number three is to bring in outside tools and skills like Ponytail that are all about reducing token count. Now, if you don't know what Ponytail is, I did a full video on it, and its thing is like, "Hey, Claude's pretty verbose. What if we gave it a set of guidelines to follow so that we still get the same outputs, still just as effective, it just writes less code to get there." Now, the thing with Ponytail is it gives us a bunch of benchmarks. The thing with the benchmarks are they've only been tested on Haiku 4.5, and Fable 5 is a different beast entirely. In my last video, I tested the numbers using Opus 4.8 and found that using Opus 4.8, these numbers were actually even better. It actually wrote less code, it consumed less tokens, and it was faster. And so, I went ahead and I ran some of the same benchmarks using Fable. So, these numbers on the left right here that are underlined, this is the baseline, and then these over here on the right is what Fable 5 got using Ponytail. And this was on a medium setting. So, across the board, essentially, it put out less tokens, and in terms of cost, which is what we really care about because, you know, the tokens, like we do care if they're input versus output. At the end of the day, it was essentially 22% cheaper, which, funny enough, is actually even better than what they claim for Haiku. Now, there's other skills like Caveman that claim to do the same thing, but the big picture with this tip is this is an expensive model. If there's stuff out there that can give us a 20% boost, it's worth experimenting with. So, even if something like this is sort of like suspect to you, I think we shouldn't dismiss it at a hand because 20% is a lot of money when we're talking about thousands of dollars. Now, on the surface, tip number four is the exact opposite of what I told you in tip number two. Remember tip number two, I said, "Hey, Fable doesn't need a plan and execute. Just have a plan." Well, in this tip, I'm saying, let's not have a plan. Let's actually have Opus plan for Fable. Now, what I mean by this is in every plan should be done by Opus and we have Fable actually create everything. I'm saying for a lot of our plans, they require research. And one of the best ways to research these days is with Ultra Code in dynamic workflows. Specifically, I'm talking about deep research. So, for those of you who don't know, /deep-research is a built-in dynamic workflow you can use. And it's going to spawn a ton of sub-agents. I used deep research in preparation for this video and it spawned 109 sub-agents. First of all, would I want to run deep research with Fable 5 is every one of those sub-agents? Absolutely not. I would blow through my limits. That makes no sense. But, the real point here is I want to use a lower-level model like Opus for deep research because research isn't something that requires like super high intellect reasoning level like Fable. However, Fable 5 doesn't necessarily have all the context of today. It's knowledge cut off wasn't yesterday. We still need something to go out there on the web, gather information, do some baseline adversarial work to make sure that information even makes sense, and then hand that to Fable. And then Fable makes the plan. Right? If we're going to plan something, we need information to start. And so, I don't think it makes a lot of sense to have Fable go out and gather all the information. Let the lower-level peons like Opus and Sonnet gather all that context and then hand it to Fable. And then Fable creates the plan and then they can hand it off. So, Fable doesn't have to do everything in the planning stage. We can kind of give it a leg up, let it do the high-level intellectual architecture work, and let these dumber models do everything else. And in that sense, dynamic workflows, Ultra code deep research is perfect for these low-level models and saves that fable usage for the more important things. Now, tip number five is something that actually came out a few months ago, and that is advisor mode. Advisor mode was originally shown with Opus and Sonnet working together. The idea is, this should sound familiar, is we have a smart model that is the advisor, that is the planner. It is handing off its plan to an executor, a lower-level model, in this case Sonnet. It is executing tools. It is reading. It is writing. But, anytime it gets stuck, what does it do? Well, it shares its context with the advisor. The smarter model says, "Hey, here's what's going on. I'm stuck. What should I do?" And if this sounds like a more sophisticated version of everything we've been talking about up until this point, you would be correct. Now, Anthropic hasn't put out any official numbers of what this looks like with fable as the advisor and having Opus be the executor or Sonnet, but we can make a few assumptions. What you see here is a graph from Opus and Sonnet 4.6. This is one of the all-time graphs from Anthropic. I mean, just look at these axes. But, what you got using advisor mode was a Sonnet that performed better for cheaper. So, it was overall, it was just more effective. And you see that reflected here as well across multiple benchmarks. Now, to actually use advisor in this way, you can't have your model set to fable five because whatever model you have set, that is the model that is the executor. That's the model that's actually writing the code. So, if I want fable five as the advisor, and I want Opus actually doing everything, then I need to make sure my model is set to Opus. Then, I just need to do {forward slash} advisor, and then that's when you set the advisor model. So, I do {forward slash} advisor, fable. Now, fable is the one that's going to be essentially telling Opus what to do. So, if you're someone who really loves the idea of fable purely acting as the architect, the conductor, and letting the lower-level models do everything, this is definitely a you should try out. So, those are five quick tips for reducing your Fable 5 usage while still getting the most you can out of this amazing model. Hopefully, Anthropic is nice to us and they just keep it on the Pro and Max plan. That would be great. And also, by the way, if you give us more than 50% of the weekly limit, that would be awesome, too. But, until then, we're going to work with what we have. So, as always, let me know what you thought. Make sure to check out Chase AI Plus if you want to get your hands on my Claude Code Masterclass. And besides that, I'll see you around.

---

## Timestamped Segments

**[0:00]** What if I told you we could reduce Fable

**[0:01]** 5's cost by 80% while still beating Opus

**[0:04]** 4.8? Well, that is just one of five

**[0:07]** tricks I'm going to show you today that

**[0:09]** are all about reducing Fable 5's usage

**[0:11]** and token cost without losing what makes

**[0:14]** this model great. Because we all know

**[0:16]** the clock is ticking. We just got a few

**[0:18]** days left until Fable 5 is kicked off

**[0:20]** the Pro and the Max plan and we are

**[0:22]** stuck paying API prices. And on top of

**[0:24]** that, we're also usage capped. So, it is

**[0:27]** imperative that we figure out quickly

**[0:30]** how to get the best bang for the buck

**[0:33]** with this new model. So, that is exactly

**[0:35]** what we're going to talk about today and

**[0:37]** let's dive in. So, tip number one, this

**[0:39]** is the easiest one and arguably the

**[0:41]** highest leverage. It is changing the

**[0:44]** effort level. It is reducing the effort

**[0:46]** level with Claude Fable 5. Now, by

**[0:48]** default, we are on high and some of you

**[0:51]** are crazy out there and I see you

**[0:52]** pushing it to extra high or even max.

**[0:55]** And the truth is, you probably do not

**[0:58]** need that. First of all, what are we

**[0:59]** looking at here? Well, we're looking at

**[1:01]** a benchmark. This is Deep Sweet. This is

**[1:03]** one of my favorite benchmarks. It's all

**[1:04]** about long horizon, long-running agentic

**[1:07]** tasks and we see Fable 5 here, Opus 4.8

**[1:11]** as well as GPT 5.5. Now, I said in the

**[1:14]** intro, I said you could reduce cost by

**[1:16]** 80%. When we look at the max effort

**[1:19]** level, which by the way doesn't give you

**[1:21]** that much of an upgrade in terms of, you

**[1:23]** know, pass percentage from extra high,

**[1:25]** it's costing us $22. Our average cost

**[1:28]** per task when looking at Deep Sweet. If

**[1:31]** we compare that to low, it's $3.76.

**[1:35]** More than an 80% reduction in cost. Yet,

**[1:39]** at low effort level with Claude Fable 5,

**[1:42]** we're doing better than max at Opus 4.8.

**[1:45]** So, we're at 60% at Fable 5 low

**[1:49]** and we're at 59% with max Opus 4.8. And

**[1:53]** Opus in this case is $13 versus $3.76.

**[1:58]** That's crazy.

**[2:00]** Like you could argue that's crazier than

**[2:02]** the jump from 59 to 70. Is the fact

**[2:05]** we're doing this so much more

**[2:07]** efficiently. And when we pop up to

**[2:09]** medium, we're going up from 60% to 65%

**[2:12]** pass rate. And we go up to high, we're

**[2:14]** at 69%. And on extra high, we're at 70%

**[2:18]** versus 59%. But at low, again, we're

**[2:21]** getting

**[2:22]** really solid outputs that are extremely

**[2:24]** cheap. Even compared to GPT 5.5, which

**[2:26]** honestly is such a sleeper model, it's

**[2:28]** so good. I'm super excited to use 5.6

**[2:30]** when it comes out. It's still doing

**[2:31]** better than medium. Slightly more

**[2:34]** expensive, but not by a ton. Now, we see

**[2:36]** this reflected in other benchmarks as

**[2:38]** well. Here's a look at frontier code

**[2:39]** accuracy versus cost. And this is coming

**[2:41]** from Anthropic itself. So, in the

**[2:43]** orange, we have Fable. In the green, we

**[2:44]** have Opus 4.8. And then down here at the

**[2:46]** bottom, we have 5.5. Look at low.

**[2:50]** All right, just a shade over $5. And the

**[2:53]** score is about 11%. If we look at Opus

**[2:56]** 4.8 on max, it's call it $11. And it's

**[2:59]** the same exact score percentage. So, I'm

**[3:01]** getting the same

**[3:03]** pass rate

**[3:04]** as Opus 4.8 on max at half the cost. And

**[3:07]** if I go up to medium, I'm blowing Opus

**[3:09]** 4.8 out of the water while still being

**[3:11]** less expensive than extra high, which is

**[3:13]** where a lot of people sit for just

**[3:14]** default Opus settings. So, with that in

**[3:16]** mind, does it make sense for us to sit

**[3:18]** on the default high level with Fable 5?

**[3:21]** I think when you look at both of these

**[3:22]** benchmarks, the answer is probably no.

**[3:24]** And when we look at Deep Sweep, Deep

**[3:26]** Sweep is rather complicated tasks. Are

**[3:28]** you doing something very complicated?

**[3:30]** The less complicated of the task you're

**[3:32]** doing, if you're doing web design,

**[3:34]** you probably should be on medium or low.

**[3:36]** And that right away is going to reduce

**[3:39]** your costs and reduce your usage

**[3:41]** substantially.

**[3:43]** Substantially. So,

**[3:45]** out of everything you see today, if

**[3:46]** nothing else, I want you to try doing a

**[3:48]** task on medium with Fable. Try doing a

**[3:50]** task on low and see how well it does. I

**[3:51]** think you would be surprised and you're

**[3:53]** not going to get to that 50% of your

**[3:55]** weekly limit nearly as quickly as you

**[3:57]** would otherwise. And of course, to

**[3:59]** change the effort level, all you have to

**[4:00]** do is go into the terminal, do {forward

**[4:02]** slash} effort, and then

**[4:04]** set it where you want to. Now, before we

**[4:06]** jump into tip number two, quick word

**[4:07]** from today's sponsor, me. So, I just

**[4:10]** released my Claude Code Masterclass and

**[4:11]** it is the number one way to go from zero

**[4:13]** to AI dev, especially if you don't come

**[4:15]** from a technical background. We focus on

**[4:17]** real use cases, it's updated every

**[4:18]** single week, and it also includes a

**[4:20]** Codex Masterclass and an Agentic OS

**[4:23]** Masterclass. So, if you're someone who's

**[4:25]** really trying to level up your AI game,

**[4:27]** you want to get serious about this, make

**[4:29]** sure to check it out. It's inside of

**[4:30]** Chase AI Plus, there's a link to that in

**[4:32]** the pinned comment. Now, tip number two

**[4:34]** when it comes to reducing Fable's usage

**[4:35]** is also pretty straightforward. And that

**[4:38]** is stop using Fable to both plan

**[4:40]** everything and execute everything.

**[4:42]** Instead, make Fable the architect. Have

**[4:46]** it come up with the plan and then,

**[4:48]** depending on the complexity of the plan,

**[4:50]** have it divvy up the work to the

**[4:51]** appropriate model. Whether that is Opus,

**[4:53]** whether that's Sonnet, or it's an

**[4:55]** outside model. It could be GPT 5.5, it

**[4:57]** could be something local.

**[5:00]** Fable's also smart enough to know which

**[5:02]** model is best for the job. And you can

**[5:04]** have Fable 5 explicitly call out those

**[5:06]** models in the plan. So,

**[5:08]** Fable 5 does the plan,

**[5:10]** and then it says, "Hey, for the first

**[5:12]** part, I want Opus. For the second part,

**[5:14]** Sonnet makes sense. And for the third

**[5:15]** part, let's send that to OpenAI and

**[5:18]** bring in GPT 5.5." This is a perfect use

**[5:20]** case for something like the Codex plugin

**[5:22]** within Claude Code. And if you haven't

**[5:24]** used that before, I highly suggest you

**[5:26]** do. You can totally bring in something

**[5:27]** like the Codex rescue function and have

**[5:30]** Fable call on that, too.

**[5:32]** Give features to GPT 5.5, which again,

**[5:35]** awesome model. But if all that's too

**[5:36]** complicated and having it call out all

**[5:38]** these agents, you can do something as

**[5:39]** simple as simply throwing it in plan

**[5:41]** mode,

**[5:42]** you know, having it come up with the

**[5:43]** plan, having it create some sort of

**[5:45]** markdown file, set the stage for your

**[5:46]** code base, and then simply spinning up

**[5:48]** another session with Opus and having it

**[5:50]** execute the plan that Fable laid out.

**[5:52]** You don't need to overcomplicate it, but

**[5:54]** that stops Fable from burning a bunch of

**[5:56]** tokens on low-level tasks that are going

**[5:58]** to be necessary for, you know, whatever

**[6:00]** you're creating. Now, tip number three

**[6:02]** is to bring in outside tools and skills

**[6:03]** like Ponytail that are all about

**[6:05]** reducing token count. Now, if you don't

**[6:07]** know what Ponytail is, I did a full

**[6:09]** video on it, and its thing is like,

**[6:11]** "Hey, Claude's pretty verbose. What if

**[6:13]** we gave it a set of guidelines to follow

**[6:15]** so that we still get the same outputs,

**[6:17]** still just as effective, it just writes

**[6:19]** less code to get there." Now, the thing

**[6:21]** with Ponytail is it gives us a bunch of

**[6:23]** benchmarks. The thing with the

**[6:24]** benchmarks are they've only been tested

**[6:27]** on Haiku 4.5, and Fable 5 is a different

**[6:29]** beast entirely. In my last video, I

**[6:32]** tested the numbers using Opus 4.8 and

**[6:35]** found that using Opus 4.8, these numbers

**[6:38]** were actually even better. It actually

**[6:39]** wrote less code, it consumed less

**[6:41]** tokens, and it was faster. And so, I

**[6:43]** went ahead and I ran some of the same

**[6:45]** benchmarks using Fable. So, these

**[6:47]** numbers on the left right here that are

**[6:49]** underlined, this is the baseline, and

**[6:52]** then these over here on the right is

**[6:55]** what Fable 5 got using Ponytail. And

**[6:58]** this was on a medium setting. So, across

**[7:00]** the board, essentially, it put out less

**[7:03]** tokens, and in terms of cost, which is

**[7:05]** what we really care about because, you

**[7:07]** know, the tokens, like we do care if

**[7:09]** they're input versus output. At the end

**[7:10]** of the day, it was essentially

**[7:12]** 22% cheaper, which, funny enough, is

**[7:16]** actually even better than what they

**[7:17]** claim for Haiku. Now, there's other

**[7:19]** skills like Caveman that claim to do the

**[7:21]** same thing, but the big picture with

**[7:22]** this tip is

**[7:24]** this is an expensive model. If there's

**[7:26]** stuff out there that can give us a 20%

**[7:27]** boost, it's worth experimenting with.

**[7:29]** So, even if something like this is sort

**[7:31]** of like suspect to you, I think we

**[7:33]** shouldn't dismiss it at a hand because

**[7:35]** 20% is a lot of money when we're talking

**[7:37]** about thousands of dollars. Now, on the

**[7:40]** surface, tip number four is the exact

**[7:42]** opposite of what I told you in tip

**[7:44]** number two. Remember tip number two, I

**[7:45]** said, "Hey, Fable doesn't need a plan

**[7:47]** and execute. Just have a plan." Well, in

**[7:49]** this tip, I'm saying,

**[7:51]** let's not have a plan. Let's actually

**[7:52]** have Opus plan for Fable. Now, what I

**[7:56]** mean by this is in every plan should be

**[7:58]** done by Opus and we have Fable actually

**[8:00]** create everything. I'm saying for a lot

**[8:03]** of our plans, they require research. And

**[8:05]** one of the best ways to research these

**[8:06]** days is with Ultra Code in dynamic

**[8:09]** workflows. Specifically, I'm talking

**[8:11]** about deep research. So, for those of

**[8:13]** you who don't know, /deep-research

**[8:16]** is a built-in dynamic workflow you can

**[8:18]** use. And it's going to spawn a ton of

**[8:21]** sub-agents. I used deep research in

**[8:22]** preparation for this video and it

**[8:24]** spawned 109 sub-agents. First of all,

**[8:27]** would I want to run deep research with

**[8:29]** Fable 5 is every one of those

**[8:31]** sub-agents? Absolutely not. I would blow

**[8:33]** through my limits. That makes no sense.

**[8:35]** But, the real point here is I want to

**[8:37]** use a lower-level model like Opus for

**[8:39]** deep research because research isn't

**[8:42]** something that requires like super high

**[8:44]** intellect reasoning level like Fable.

**[8:47]** However, Fable 5 doesn't necessarily

**[8:49]** have all the context of today. It's

**[8:51]** knowledge cut off wasn't yesterday. We

**[8:52]** still need something to go out there on

**[8:54]** the web, gather information, do some

**[8:57]** baseline adversarial work to make sure

**[8:59]** that information even makes sense, and

**[9:01]** then

**[9:02]** hand that to Fable. And then Fable makes

**[9:04]** the plan. Right? If we're going to plan

**[9:06]** something, we need information to start.

**[9:09]** And so, I don't think it makes a lot of

**[9:11]** sense to have Fable go out and gather

**[9:13]** all the information. Let the lower-level

**[9:15]** peons like Opus and Sonnet gather all

**[9:18]** that context and then hand it to Fable.

**[9:21]** And then Fable creates the plan and then

**[9:23]** they can hand it off. So, Fable doesn't

**[9:25]** have to do everything in the planning

**[9:27]** stage. We can kind of give it a leg up,

**[9:29]** let it do the high-level intellectual

**[9:32]** architecture work,

**[9:33]** and let these dumber models do

**[9:34]** everything else. And in that sense,

**[9:36]** dynamic workflows, Ultra code deep

**[9:38]** research is perfect for these low-level

**[9:39]** models and saves that fable usage for

**[9:42]** the more important things. Now, tip

**[9:43]** number five is something that actually

**[9:45]** came out a few months ago, and that is

**[9:46]** advisor mode. Advisor mode was

**[9:48]** originally shown with Opus and Sonnet

**[9:51]** working together. The idea is, this

**[9:53]** should sound familiar, is we have a

**[9:55]** smart model that is the advisor, that is

**[9:58]** the planner. It is handing off its plan

**[10:01]** to an executor, a lower-level model, in

**[10:04]** this case Sonnet. It is executing tools.

**[10:07]** It is reading. It is writing. But,

**[10:10]** anytime it gets stuck, what does it do?

**[10:12]** Well, it shares its context with the

**[10:15]** advisor. The smarter model says, "Hey,

**[10:17]** here's what's going on. I'm stuck. What

**[10:19]** should I do?" And if this sounds like a

**[10:21]** more sophisticated version of everything

**[10:23]** we've been talking about up until this

**[10:24]** point, you would be correct. Now,

**[10:26]** Anthropic hasn't put out any official

**[10:27]** numbers of what this looks like with

**[10:29]** fable as the advisor and having Opus be

**[10:31]** the executor or Sonnet, but we can make

**[10:34]** a few assumptions. What you see here is

**[10:36]** a graph from Opus and Sonnet 4.6. This

**[10:40]** is one of the all-time graphs from

**[10:41]** Anthropic. I mean, just look at these

**[10:42]** axes. But, what you got using advisor

**[10:45]** mode was a Sonnet that performed better

**[10:47]** for cheaper. So, it was overall, it was

**[10:49]** just more effective. And you see that

**[10:51]** reflected here as well across multiple

**[10:53]** benchmarks. Now, to actually use advisor

**[10:55]** in this way, you can't have your model

**[10:57]** set to fable five because whatever model

**[10:59]** you have set, that is the model that is

**[11:02]** the executor. That's the model that's

**[11:03]** actually writing the code. So, if I want

**[11:06]** fable five as the advisor, and I want

**[11:08]** Opus actually doing everything, then I

**[11:09]** need to make sure my model is set to

**[11:11]** Opus. Then, I just need to do {forward

**[11:13]** slash} advisor, and then that's when you

**[11:16]** set the advisor model. So, I do {forward

**[11:17]** slash} advisor, fable. Now, fable is the

**[11:21]** one that's going to be essentially

**[11:22]** telling Opus what to do. So, if you're

**[11:24]** someone who really loves the idea of

**[11:26]** fable purely acting as the architect,

**[11:27]** the conductor, and letting the

**[11:29]** lower-level models do everything, this

**[11:31]** is definitely a you should try out. So,

**[11:33]** those are five quick tips for reducing

**[11:35]** your Fable 5 usage while still getting

**[11:37]** the most you can out of this amazing

**[11:39]** model. Hopefully, Anthropic is nice to

**[11:41]** us and they just keep it on the Pro and

**[11:43]** Max plan. That would be great. And also,

**[11:44]** by the way, if you give us more than 50%

**[11:46]** of the weekly limit, that would be

**[11:48]** awesome, too. But, until then, we're

**[11:50]** going to work with what we have. So, as

**[11:53]** always, let me know what you thought.

**[11:54]** Make sure to check out Chase AI Plus if

**[11:56]** you want to get your hands on my Claude

**[11:57]** Code Masterclass. And besides that, I'll

**[11:59]** see you around.
