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
