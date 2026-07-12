# Transcript: Here we go again...

**URL:** https://www.youtube.com/watch?v=J2ZE6XGCYb0
**Segments:** 135
**Channel:** Maximilian Schwarzmüller
**Duration:** 8:11
**Uploaded:** 2026-06-09

---

## Full Text

I came across this post by Peter
Steinberger, the creator of OpenClaw, of course, yesterday on X, where he wrote, "Here's your monthly reminder
that you shouldn't be prompting coding agents anymore.
You should be designing loops that prompt your agents." And, oh boy,
I have some thoughts here. So loop engineering it is now, right? I don't think it's an official term yet.
But we'll see if it will be. And of course,
we're coming from a past where we had then parts of the industry decided
that this should be rephrased or relabeled as context
engineering, which was always stupid because it's the same thing
in the end because it always was about ensuring that the model has the right
context. That was the entire idea behind prompt
engineering too, because yeah, obviously, the right context matters, did matter,
still matters, will matter because if you wanna have better chances
of getting good results out of LLMs,
you need to give them the right context. You have a better chance then.
No guarantee. Even with the right context, mistakes
are possible or just not getting what you were looking for.
That's all possible because it's still, non-deterministic system,
a non-deterministic tool. But if you wanna have a shot at getting
good results, and you definitely can get good results,
then providing the right context Now, around the change from 2025 to 2026, and of course throughout this year,
we then saw the rise of agentic coding since tools like
Claude Code and Codex, combined with the models that
are used inside them, fine-tuned and optimized for instruction
following and coding tasks, those tools with the models showed us
that, yeah, you can really use these AI models, LLMs, for coding tasks and get stuff done with
them as assistants. At least that
is still my take and my experience.
And I've been using these models a lot, tools, playing around with them pretty much every
day, using them every day. And not just playing around with them,
also using them for serious projects. And of course, that
is why I built courses, uh, Codex, where I dive a bit deeper
and share my learnings And these tools are useful assistants, but they just aren't those replacements of developers yet, and, um, as I've shared in many other episodes,
probably also not in the near future. Nonetheless, of course, Anthropic
and OpenAI, they added extra commands to these, uh, tools, like the slash goal command in Codex
or the slash loop command in Claude Code, where the idea is that you can specify a specific goal, a maybe more complex task, with
that command added in front of it, and the tool, Codex, Claude Code with the model, will keep on going
and will keep on re-prompting itself until that task is completed.
And it's kind of only the Ralph Loop again.
Remember the Ralph Loop at the beginning of 2026? We had that hype around the Ralph Loop where some people just sold you
that you just need a detailed step-by-step list, uh,
of tasks that need to be completed to achieve a certain
goal, build a certain feature, and then you could use an extension, uh,
to keep Claude Code, and Codex then at some point, going and,
and work its way through that list. And even though we had the Ralph Loop back
in January already and some people sold it to you as the solution
for building software autonomously, wh- where is all that software? Where
is all that software, that error-free, amazing software? Why
is Claude Code still flickering? Uh, yeah, anyway.
(laughs) So we had the Ralph Loop back back here officially integrated into
Claude Code and Codex and now we're talking about loop engineering
or designing your loops that prompt your agents. And of course that
is something that's easy to say for who works for OpenAI in the end because of unlimited tokens,
because it turns out this, these loops, these commands,
they can burn through a lot of tokens. The, the problem just
is you have the same probabilistic nature of the entire system, and I think one thing that's often
overlooked is that indeed my experience has been
that these AI models that were, and/or these tools
and the models combined, it's, are indeed pretty good at just keeping on
going until a certain goal is achieved. I mean, o- one tiny example I had a, a few weeks or months ago now,
is I had a couple of PDF documents which I needed to combine into one,
which combined must not be bigger than megabytes,
but each individual document contain scans.
So I just threw my coding agent, I think Codex, at the task and it kept on going,
kept on writing some little programs and stuff and, until it really achieved that. And obviously that might not be a super
complex task. The point just is, indeed these models,
if they can verify an outcome,
they are quite decent at achieving a goal, at achieving a, a certain task. They just keep on going
and try different ways of getting there. The problem just is, that
is not necessarily how good software is being built.
It's one thing to just get something done,
to just find a way of doing something. That may be enough for certain use cases. If we're talking about software,
software that should be distributed, that should be evolved and maintained, it's not a good strategy to just find a
way of getting there, because
that one way may get one thing done.... at this point in time.
It may break in the future. It may break for slightly different input. It may contain a lot of bugs
or security issues. It may fail for so many reasons,
for so many other situations.
It may have poor performance and all that, again, may not matter
if you're just trying to get one thing now. But that is, again,
not what software in general, if we're talking about software as a product at
least, is about. So there are reasons why we learned as developers that certain patterns and practices
and approaches make sense because they're easier to adapt,
easier to understand, easier to adjust. Simply cleaner,
not just for the cleanliness sake, but for the extensibility,
maintainability, performance, security and understandability sake. And even if you don't care about
understanding the code anymore because you'd say
that the AI just needs to understand it, not a human, which is also really,
really a bad take, um,
because obviously AI models have limited But even then,
if that's your take on the the other parts still matter. And, yeah. I don't think there
is more to say about that. I,
I really hate the current (laughs) point time where we have all these annoying stupid terms coming up all the time
and then we got people trying to sell you products and, and,
and courses and stuff off that. And I sell cor- courses myself.
I just don't sell and won't sell you a course on loop engineering or any-
anything like that. But yeah, here we are. Um, I'm sure at some point we'll be past that
and we can use these coding agents for what they are,
helpful assistants. But right now, we're still stuck here
and I'm excited to see what will be next after loop engineering.

---

## Timestamped Segments

**[0:00]** I came across this post by Peter
Steinberger, the creator of OpenClaw,

**[0:04]** of course, yesterday on X, where he wrote,

**[0:07]** "Here's your monthly reminder
that you shouldn't be prompting

**[0:11]** coding agents anymore.
You should be designing loops

**[0:15]** that prompt your agents." And, oh boy,
I have

**[0:18]** some thoughts here.

**[0:21]** So loop engineering it is now, right?

**[0:24]** I don't think it's an official term yet.
But we'll see if it will be.

**[0:27]** And of course,
we're coming from a past where we had

**[0:31]** then parts of the industry decided
that this should be

**[0:35]** rephrased or relabeled as context
engineering, which was

**[0:39]** always stupid because it's the same thing
in the end because it always was about

**[0:42]** ensuring that the model has the right
context.

**[0:45]** That was the entire idea behind prompt
engineering too, because yeah, obviously,

**[0:50]** the right context matters, did matter,
still matters, will matter

**[0:54]** because if you wanna have better chances
of getting good results

**[0:58]** out of LLMs,
you need to give them the right context.

**[1:02]** You have a better chance then.
No guarantee.

**[1:05]** Even with the right context, mistakes
are possible or just not getting

**[1:09]** what you were looking for.
That's all possible because it's still,

**[1:13]** non-deterministic system,
a non-deterministic tool.

**[1:16]** But if you wanna have a shot at getting
good results, and you definitely can get

**[1:20]** good results,
then providing the right context

**[1:24]** Now, around the change from 2025 to

**[1:27]** 2026, and of course throughout this year,
we then saw the

**[1:31]** rise of agentic coding since tools like
Claude Code and Codex,

**[1:34]** combined with the models that
are used inside them,

**[1:38]** fine-tuned and optimized for instruction
following and coding tasks,

**[1:43]** those tools with the models showed us
that, yeah, you

**[1:46]** can really use these AI models, LLMs,

**[1:50]** for coding tasks and get stuff done with
them

**[1:54]** as assistants. At least that
is still my take and

**[1:57]** my experience.
And I've been using these models a lot,

**[2:01]** tools,

**[2:03]** playing around with them pretty much every
day, using them every day.

**[2:06]** And not just playing around with them,
also using them for serious projects.

**[2:10]** And of course, that
is why I built courses, uh,

**[2:13]** Codex, where I dive a bit deeper
and share my learnings

**[2:17]** And these tools are useful assistants,

**[2:21]** but they just aren't those replacements

**[2:25]** of developers yet, and, um, as I've

**[2:29]** shared in many other episodes,
probably also not in the near future.

**[2:33]** Nonetheless, of course, Anthropic
and OpenAI, they added

**[2:37]** extra commands to these, uh, tools, like

**[2:41]** the slash goal command in Codex
or the slash loop command in Claude

**[2:45]** Code, where the idea is that you can

**[2:48]** specify a specific goal,

**[2:51]** a maybe more complex task, with
that command added in front of

**[2:55]** it, and the tool, Codex, Claude Code with

**[2:59]** the model, will keep on going
and will keep on re-prompting itself

**[3:03]** until that task is completed.
And it's kind of only

**[3:07]** the Ralph Loop again.
Remember the Ralph Loop at the beginning

**[3:11]** of 2026? We had that hype around the

**[3:15]** Ralph Loop where some people just sold you
that you just need a

**[3:19]** detailed step-by-step list, uh,
of tasks that

**[3:23]** need to be completed to achieve a certain
goal, build a certain feature,

**[3:27]** and then you could use an extension, uh,
to keep Claude Code,

**[3:31]** and Codex then at some point, going and,
and work its way through that list.

**[3:34]** And even though we had the Ralph Loop back
in January already and

**[3:38]** some people sold it to you as the solution
for building software

**[3:42]** autonomously,

**[3:44]** wh- where is all that software? Where
is all that software, that

**[3:48]** error-free, amazing software? Why
is Claude Code still

**[3:51]** flickering?

**[3:54]** Uh, yeah,

**[3:55]** anyway.
(laughs) So we had the Ralph Loop back

**[3:59]** back here officially integrated into
Claude Code and Codex and

**[4:03]** now we're talking about loop engineering
or designing

**[4:07]** your loops that prompt your agents.

**[4:10]** And of course that
is something that's easy to say for

**[4:14]** who works for OpenAI in the end because

**[4:18]** of unlimited tokens,
because it turns out this, these

**[4:22]** loops, these commands,
they can burn through a lot of

**[4:25]** tokens. The, the problem just
is you have the

**[4:29]** same

**[4:31]** probabilistic nature of the entire system,

**[4:34]** and I think one thing that's often
overlooked is that

**[4:38]** indeed my experience has been
that these AI models that were,

**[4:42]** and/or these tools
and the models combined, it's,

**[4:46]** are indeed pretty good at just keeping on
going

**[4:50]** until a certain goal is achieved. I mean,

**[4:54]** o- one tiny example I had a, a few weeks

**[4:57]** or months ago now,
is I had a couple of PDF documents which I

**[5:02]** needed to combine into one,
which combined must not be bigger than

**[5:05]** megabytes,
but each individual document

**[5:09]** contain scans.
So I just threw my coding agent, I think

**[5:13]** Codex, at the task and it kept on going,
kept on writing some little programs and

**[5:17]** stuff and, until it really achieved that.

**[5:19]** And obviously that might not be a super
complex task.

**[5:22]** The point just is, indeed these models,
if they can verify an

**[5:26]** outcome,
they are quite decent at achieving

**[5:30]** a goal, at achieving a, a certain task.

**[5:33]** They just keep on going
and try different ways of getting there.

**[5:37]** The problem just is, that
is not necessarily how good

**[5:41]** software is being built.
It's one thing to just get something

**[5:45]** done,
to just find a way of doing something.

**[5:49]** That may be enough for certain use cases.

**[5:52]** If we're talking about software,
software that should be distributed, that

**[5:56]** should be evolved and maintained,

**[5:58]** it's not a good strategy to just find a
way of

**[6:02]** getting there, because
that one way may get one thing

**[6:06]** done.... at this point in time.
It may break in the future.

**[6:09]** It may break for slightly different input.

**[6:12]** It may contain a lot of bugs
or security issues.

**[6:15]** It may fail for so many reasons,
for so many other

**[6:19]** situations.
It may have poor performance and all that,

**[6:23]** again, may not matter
if you're just trying to get one thing

**[6:27]** now.

**[6:28]** But that is, again,
not what software in general, if we're

**[6:32]** talking about software as a product at
least, is about.

**[6:36]** So there are reasons why

**[6:38]** we learned as developers that

**[6:42]** certain patterns and practices
and approaches make sense because

**[6:46]** they're easier to adapt,
easier to understand, easier to adjust.

**[6:51]** Simply cleaner,
not just for the cleanliness sake,

**[6:55]** but for the extensibility,
maintainability, performance,

**[6:59]** security and understandability sake.

**[7:02]** And even if you don't care about
understanding the code anymore

**[7:06]** because you'd say
that the AI just needs to understand it,

**[7:10]** not a human, which is also really,
really a bad take,

**[7:14]** um,
because obviously AI models have limited

**[7:17]** But even then,
if that's your take on the

**[7:21]** the other parts still matter. And,

**[7:26]** yeah. I don't think there
is more to say about that.

**[7:29]** I,
I really hate the current (laughs) point

**[7:33]** time where we have all these annoying

**[7:37]** stupid terms coming up all the time
and then we got people trying

**[7:41]** to sell you products and, and,
and courses and stuff off that.

**[7:45]** And I sell cor- courses myself.
I just don't sell and won't sell you

**[7:49]** a course on loop engineering or any-
anything like that.

**[7:52]** But yeah, here we are. Um, I'm sure

**[7:56]** at some point we'll be past that
and we can use these

**[8:00]** coding agents for what they are,
helpful assistants.

**[8:03]** But right now, we're still stuck here
and I'm excited to see

**[8:07]** what will be next after loop engineering.
