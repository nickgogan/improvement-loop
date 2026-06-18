# Transcript: wRDk9_JoIic

**URL:** https://www.youtube.com/watch?v=wRDk9_JoIic
**Segments:** 349

---

## Full Text

There's basically a hundred different agent products out there that are saying that like this can do anything on the web. Then you try it once and it doesn't really work. If we think of a 10-step, 20-step, or 50-step workflow, even if the accuracy at each step is like 90%, the 10% error rate compounds very quickly. And so the overall success rate of a task of a workflow is like quite low. So that's one of the reasons why the technology is not there yet to do long horizon workflows. It feels like we have started normalizing and developed a tolerance for non-determinism and low reliability in shipping products. The product builder in me is like really annoyed that how is this okay for someone to ship an agentic product where they say that this can do anything, but you try it the first time and like it doesn't work. I push back on that getting normalized, especially with agentic products. If it's not good enough to work on the first try, it's not good enough. The true differentiator is in My name's Abhishek Das. I'm the co-founder and co-CEO of Utori. So with Utori, we're building agents that can take actions and complete tasks on users' behalf on the web so that you can focus on whatever is most meaningful to you. The three co-founders, we're all AI researchers by background. It is a bigger bet than just another agent company. So Fefe Li and Jeff Dean, and they were excited to support us. I come from a family of doctors and medical practitioners. So it was a bit of a an irony that I'm scared of blood. And so like the choice was pretty clear that like yeah, I'm not going to pursue medicine. That's when I ended up deciding to to pursue engineering. Science and the scientific process and method really appeals to me. Like the whole life cycle of coming up with hypotheses, come then designing experiments to validate or invalidate those hypotheses, drawing conclusions, and then coming up with the next set of hypotheses. I think that is a very neat sort of process and method. I found that really inspiring. And then I went to IIT Roorkee for my undergrad. That was a an amazing sort of learning experience, met some of the smartest people I know. And so, first year of college, I was getting good grades, but very quickly I realized that like electrical engineering, especially this was more geared towards like power systems, etc., was not where my interest was. And so, at the end of first year, that was sort of the first major sort of rebellious streak in me where I decided that, "Okay, like I don't see a future in electrical engineering. I'm going to stop paying as much attention to it." So, that was like a fairly sig- significant fork in my in my life in some sense. And instead, I ended up spending a lot of my time learning programming and how to build software. That's when I got into building software and applications very seriously. What also helped was that IIT Roorkee had even at the time this is like almost 13, 14 years back had a really strong programming club and culture. In particular, there was this group called SDSLabs, which was a group of like 10, 15 coders from from every year who were just tinkering and hack- like building a ton of applications for the intranet, for the rest of the campus. Seeing how users use it, building something from scratch and putting it out there, and seeing how users interact with, I think that was like a dopamine hit that kept like sort of fueling this. And I would stay up nights to to build this, to add features, to like improve it, and and so on, right? I especially because I was surrounded by people who were as obsessed with this stuff as I was. And that was like extremely extremely motivating. To be honest, I wanted to start something of my own for as long as I can remember. I had strongly considered it at the end of my undergrad, at the end of my PhD, and for various reasons didn't end up doing it. So, it was just a matter of time. And the main reason for it is that like there's lots of interesting problems in the world to solve, to go after. Like I did want to push on that vision that I care about as opposed to working on somebody else's vision. Over the last two or three decades, web browsers by and large have stayed the same, right? Like we open browser, we open a web page, we click around, scroll, type stuff, etc. There is an opportunity now to reimagine what that experience looks and feels like. We're going to be talking to our AI assistants that take actions and complete tasks on the web, and a lot of it is going to be agents that work in the background in a proactive manner for you. That's what the future looks like, and that is how we approached it. Felt like before physical agents become a reality, um digital agents will become reality. Like the timeline for digital agents is shorter than for physical agents. If you think about interacting with the web, maybe like 5 to 10 years in the future, it is going to be at a slightly higher level of abstraction. Instead of us having to do digital chores ourselves manually, it lets us focus on tasks and stuff that's more meaningful, that's more interesting to us. Like if we can delegate all the mundane stuff to AI assistants, AI agents on our behalf, it lets us focus on stuff that's more more interesting to us. So it's more like humans and agents working together to overall improve productivity, less so that like these agents are going to like replace humans and then humans won't have anything to do. But part of it is also just making it accessible to more people. Like my parents, for example, no longer have to learn every new website and how to operate it, right? Like if they can just tell an assistant that this is what I want to do on this particular website, and it does it for them reliably, then that's awesome, right? So it makes it more accessible for more people. In this day and age, there's basically a hundred different agent products out there that are saying that like this can do anything on the web, and you try it once and it doesn't really work. And there's also this notion of that like if you usually works, right? Like if you try it 10 times, then maybe like three times or like five times, it it does the right thing. I push back on that getting normalized. Agents are basically making a sequence of decisions. Like if we think of a 10-step, 20-step, or 50-step workflow, even if the accuracy at each step is like 90%, the 10% error rate compounds very quickly, and so the overall success rate of a task of a workflow is like quite low, right? And so that's one of the reasons why the technology is not there yet to do long-horizon workflows. Being able to recognize when it makes mistakes and backtrack from that to then go down a different branch is really, really important. We put in a lot of effort into building evals and guardrails. Like every single production query that a user runs goes through a fairly comprehensive set of evals that lets us quickly identify where these agents are doing well versus not, which domains need more work, and so on. That's one aspect of it. And because we're in the space of web agents, right? Like agents that can do actions and tasks on the web, it will never be the case that we will be able to train on every single website that's out there. Like there's new websites coming up all the time. The number of websites that exist in the world is already pretty large. So we will always be training on a finite set of websites and improving these models there. Like people make mistakes on new website, click on the wrong buttons, etc., all the time, right? Like So it is very natural to expect models to also make mistakes. But when it makes a mistake, is it able to recognize and then backtrack and correct itself to do the right thing is a fairly important ingredient in the recipe of like how we train and build and ship these models. But the other part is is more ecosystem-wide where like it feels like we have started normalizing and developed a tolerance for non-determinism and low reliability in shipping products. I don't like the normalization of slop and non-determinism and poor reliability, especially with agentic products. Yeah, if it's not good enough to work on the first try, it's not good enough. We take sort of an 80/20 approach to it. Like there is always the prioritization question of like, okay, there are 100 features that we could be building. What are the top 10 that we need to focus on? Like some of those are informed by users and what what users are are telling us, what they're asking for. But very often there are ways to build product that users may not be asking for, but if you build it and a lot of what intuition goes into identifying what those features might be, then users feel seen and they feel like, oh, this is someone who is listening to us, even though that's not exactly what they asked for initially. I'll give you an example. The feature on iOS or Android that like anytime you get a two-factor authentication SMS, it auto reads your SMS and fills it into whichever app asked for it. It is hard to imagine like a user asking for that feature, but it saves a few seconds multiple times a day for people all across the world. But it's like a tiny thing that makes users feel seen. Like, oh, someone is actually giving thought how to reduce these tiny paper cuts in our in our day-to-day life. That's really important. So like it is a marriage of intuition with what users are actually asking for. In a world where it's very easy to come up with first prototypes using these coding LLMs, the true differentiator is in taste and craft, in how intuitive and well-designed the product is. One thing we do in the team that helps with that, I think, is we take dog fooding our own product very seriously. Like every single week we have an hour hour and a half docked out for dog fooding new features in the product. At any given point of time we're running like tens of experiments internally and maybe like one of them will ship to the production version of the product that external users will see. So like constantly dog fooding our our own product is a way to refine our own taste for like, okay, what is good versus bad, what awesome or magical feels like. Like anything else, a lot of reps to build that muscle is like one way to go about it. The Grad Camp project was led by one of my lab mates. I was sort of a supporting author on that paper. I was 25 when we did that paper. It's been extremely well received. I think 20, 30,000 citations is quite non-trivial. At the time, interpretability in like around deep learning models was like a big area of focus. Still is to this day. And so, it was motivated from that that like, okay, like these models, especially classification models to start with, that go from like images to classifying it in one of 1,000 or 10,000 categories, what part of the image are they looking at to make those predictions, right? There is clearly some signal coming from the image itself and then some signal that may be coming from the label that the classification model is predicting. And how can we combine the two, develop better intuition for what part of the image the model is looking at? To this day, it seems to work quite effectively across a bunch of tasks and models. Like with AI models, it is important for models to be able to convey not just the final prediction or the final answer, but also the proof of work. Like, what are the steps that went into coming up with this final prediction or the final answer. And so, Grad-CAM is like one manifestation of that. But even in how we build the the Scouts product today, like you can set up the Scouts and agents to monitor the web for something and they will generate these reports and notify you when they find something that's of value to you. But there is a button in the UI that lets you inspect the work that went in in behind the scenes. Like, which websites were were visited, what did the agent actually look at to pull out this piece of information. And that gives you a glimpse into the work that went in behind the scenes to put this together. very, very important for trust building, for users to be able to trust that yes, this is a reliable product. A lot of our time and attention in how we are building our product at Unitary goes into thinking about, how should we build the product so that we don't make the same mistake? Whenever we ship something, we have to get it right. It has to really work. It has to be reliable. Users have to trust that it works well. If you put attention to detail into parts of the product that users can see, then the user is more likely to trust the parts of the product that they cannot see. Right? Like everything awesome that we see around us, it's like individuals or groups who put in a lot of hard work and attention to detail to build that. So, I think we should approach everything that we are building with that kind of philosophy. It takes time to build something meaningful, to build something right, to bring a vision of the future to life. And building like delightful and reliable product experiences, it doesn't just appear out of nowhere.

---

## Timestamped Segments

**[0:00]** There's basically a hundred different

**[0:01]** agent products out there that are saying

**[0:03]** that like this can do anything on the

**[0:04]** web. Then you try it once and it doesn't

**[0:06]** really work. If we think of a 10-step,

**[0:08]** 20-step, or 50-step workflow, even if

**[0:10]** the accuracy at each step is like 90%,

**[0:13]** the 10% error rate compounds very

**[0:14]** quickly. And so the overall success rate

**[0:16]** of a task of a workflow is like quite

**[0:19]** low. So that's one of the reasons why

**[0:20]** the technology is not there yet to do

**[0:23]** long horizon workflows. It feels like we

**[0:26]** have started normalizing and developed a

**[0:28]** tolerance for non-determinism and low

**[0:31]** reliability in shipping products. The

**[0:33]** product builder in me is like really

**[0:35]** annoyed that how is this okay for

**[0:37]** someone to ship an agentic product where

**[0:38]** they say that this can do anything, but

**[0:40]** you try it the first time and like it

**[0:41]** doesn't work. I push back on that

**[0:44]** getting normalized, especially with

**[0:45]** agentic products. If it's not good

**[0:47]** enough to work on the first try, it's

**[0:49]** not good enough. The true differentiator

**[0:51]** is in

**[0:53]** My name's Abhishek Das. I'm the

**[0:55]** co-founder and co-CEO of Utori. So with

**[0:58]** Utori, we're building agents that can

**[0:59]** take actions and complete tasks on

**[1:01]** users' behalf on the web so that you can

**[1:03]** focus on whatever is most meaningful to

**[1:05]** you. The three co-founders, we're all AI

**[1:07]** researchers by background. It is a

**[1:09]** bigger bet than just another agent

**[1:11]** company. So Fefe Li and Jeff Dean, and

**[1:13]** they were excited to support us.

**[1:25]** I come from a family of doctors and

**[1:26]** medical practitioners. So it was a bit

**[1:28]** of a an irony that I'm scared of blood.

**[1:30]** And so like the choice was pretty clear

**[1:32]** that like yeah, I'm not going to pursue

**[1:33]** medicine. That's when I ended up

**[1:35]** deciding to to pursue engineering.

**[1:37]** Science and the scientific process and

**[1:39]** method really appeals to me. Like the

**[1:41]** whole life cycle of coming up with

**[1:42]** hypotheses, come then designing

**[1:44]** experiments to validate or invalidate

**[1:46]** those hypotheses, drawing conclusions,

**[1:48]** and then coming up with the next set of

**[1:50]** hypotheses. I think that is a very neat

**[1:52]** sort of process and method. I found that

**[1:54]** really inspiring. And then I went to IIT

**[1:56]** Roorkee for my undergrad. That was a an

**[1:58]** amazing sort of learning experience, met

**[2:00]** some of the smartest people I know. And

**[2:02]** so, first year of college, I was getting

**[2:04]** good grades, but very quickly I realized

**[2:06]** that like electrical engineering,

**[2:07]** especially this was more geared towards

**[2:09]** like power systems, etc., was not where

**[2:12]** my interest was. And so, at the end of

**[2:14]** first year, that was sort of the first

**[2:16]** major sort of rebellious streak in me

**[2:18]** where I decided that, "Okay, like I

**[2:19]** don't see a future in electrical

**[2:21]** engineering. I'm going to stop paying as

**[2:22]** much attention to it." So, that was like

**[2:24]** a fairly sig- significant fork in my in

**[2:26]** my life in some sense. And instead, I

**[2:28]** ended up spending a lot of my time

**[2:30]** learning programming and how to build

**[2:32]** software. That's when I got into

**[2:34]** building software and applications very

**[2:36]** seriously. What also helped was that IIT

**[2:39]** Roorkee had even at the time this is

**[2:40]** like almost 13, 14 years back had a

**[2:43]** really strong programming club and

**[2:45]** culture. In particular, there was this

**[2:47]** group called SDSLabs, which was a group

**[2:49]** of like 10, 15 coders from from every

**[2:51]** year who were just tinkering and hack-

**[2:54]** like building a ton of applications for

**[2:56]** the intranet, for the rest of the

**[2:58]** campus. Seeing how users use it,

**[3:00]** building something from scratch and

**[3:02]** putting it out there, and seeing how

**[3:03]** users interact with, I think that was

**[3:06]** like a dopamine hit that kept like sort

**[3:08]** of fueling this. And I would stay up

**[3:10]** nights to to build this, to add

**[3:11]** features, to like improve it, and and so

**[3:13]** on, right? I especially because I was

**[3:16]** surrounded by people who were as

**[3:17]** obsessed with this stuff as I was. And

**[3:20]** that was like extremely extremely

**[3:22]** motivating.

**[3:26]** To be honest, I wanted to start

**[3:28]** something of my own for as long as I can

**[3:30]** remember. I had strongly considered it

**[3:32]** at the end of my undergrad, at the end

**[3:33]** of my PhD, and for various reasons

**[3:35]** didn't end up doing it. So, it was just

**[3:37]** a matter of time. And the main reason

**[3:39]** for it is that like there's lots of

**[3:41]** interesting problems in the world to

**[3:43]** solve, to go after. Like I did want to

**[3:45]** push on that vision that I care about as

**[3:48]** opposed to working on somebody else's

**[3:50]** vision. Over the last two or three

**[3:51]** decades, web browsers by and large have

**[3:53]** stayed the same, right? Like we open

**[3:55]** browser, we open a web page, we click

**[3:56]** around, scroll, type stuff, etc. There

**[3:58]** is an opportunity now to reimagine what

**[4:01]** that experience looks and feels like.

**[4:02]** We're going to be talking to our AI

**[4:04]** assistants that take actions and

**[4:05]** complete tasks on the web, and a lot of

**[4:08]** it is going to be agents that work in

**[4:11]** the background in a proactive manner for

**[4:13]** you. That's what the future looks like,

**[4:15]** and that is how we approached it. Felt

**[4:16]** like before physical agents become a

**[4:19]** reality, um digital agents will become

**[4:22]** reality. Like the timeline for digital

**[4:24]** agents is shorter than for physical

**[4:26]** agents. If you think about interacting

**[4:28]** with the web, maybe like 5 to 10 years

**[4:31]** in the future, it is going to be at a

**[4:32]** slightly higher level of abstraction.

**[4:34]** Instead of us having to do digital

**[4:37]** chores ourselves manually, it lets us

**[4:40]** focus on tasks and stuff that's more

**[4:42]** meaningful, that's more interesting to

**[4:44]** us. Like if we can delegate all the

**[4:46]** mundane stuff to AI assistants, AI

**[4:47]** agents on our behalf, it lets us focus

**[4:49]** on stuff that's more more interesting to

**[4:51]** us. So it's more like humans and agents

**[4:53]** working together to overall improve

**[4:56]** productivity, less so that like these

**[4:58]** agents are going to like replace humans

**[4:59]** and then humans won't have anything to

**[5:01]** do. But part of it is also just making

**[5:03]** it accessible to more people. Like my

**[5:05]** parents, for example, no longer have to

**[5:07]** learn every new website and how to

**[5:09]** operate it, right? Like if they can just

**[5:11]** tell an assistant that this is what I

**[5:12]** want to do on this particular website,

**[5:14]** and it does it for them reliably, then

**[5:16]** that's awesome, right? So it makes it

**[5:18]** more accessible for more people.

**[5:23]** In this day and age, there's basically a

**[5:24]** hundred different agent products out

**[5:26]** there that are saying that like this can

**[5:27]** do anything on the web, and you try it

**[5:29]** once and it doesn't really work. And

**[5:30]** there's also this notion of that like if

**[5:33]** you usually works, right? Like if you

**[5:35]** try it 10 times, then maybe like three

**[5:37]** times or like five times, it it does the

**[5:39]** right thing. I push back on that getting

**[5:41]** normalized. Agents are basically making

**[5:44]** a sequence of decisions. Like if we

**[5:46]** think of a 10-step, 20-step, or 50-step

**[5:48]** workflow, even if the accuracy at each

**[5:50]** step is like 90%, the 10% error rate

**[5:53]** compounds very quickly, and so the

**[5:54]** overall success rate of a task of a

**[5:56]** workflow is like quite low, right? And

**[5:59]** so that's one of the reasons why the

**[6:00]** technology is not there yet to do

**[6:02]** long-horizon workflows. Being able to

**[6:04]** recognize when it makes mistakes and

**[6:06]** backtrack from that to then go down a

**[6:09]** different branch is really, really

**[6:11]** important. We put in a lot of effort

**[6:14]** into building evals and guardrails. Like

**[6:16]** every single production query that a

**[6:18]** user runs goes through a fairly

**[6:20]** comprehensive set of evals that lets us

**[6:22]** quickly identify where these agents are

**[6:24]** doing well versus not, which domains

**[6:27]** need more work, and so on. That's one

**[6:29]** aspect of it. And because we're in the

**[6:31]** space of web agents, right? Like agents

**[6:32]** that can do actions and tasks on the

**[6:34]** web, it will never be the case that we

**[6:36]** will be able to train on every single

**[6:38]** website that's out there. Like there's

**[6:40]** new websites coming up all the time. The

**[6:42]** number of websites that exist in the

**[6:43]** world is already pretty large. So we

**[6:45]** will always be training on a finite set

**[6:47]** of websites and improving these models

**[6:49]** there. Like people make mistakes on new

**[6:50]** website, click on the wrong buttons,

**[6:52]** etc., all the time, right? Like So it is

**[6:53]** very natural to expect models to also

**[6:55]** make mistakes. But when it makes a

**[6:57]** mistake, is it able to recognize and

**[6:59]** then backtrack and correct itself to do

**[7:01]** the right thing is a fairly important

**[7:03]** ingredient in the recipe of like how we

**[7:06]** train and build and ship these models.

**[7:08]** But the other part is is more

**[7:10]** ecosystem-wide where like it feels like

**[7:13]** we have started normalizing and

**[7:15]** developed a tolerance for

**[7:17]** non-determinism and low reliability in

**[7:19]** shipping products. I don't like the

**[7:21]** normalization of slop and

**[7:23]** non-determinism and poor reliability,

**[7:25]** especially with agentic products. Yeah,

**[7:27]** if it's not good enough to work on the

**[7:29]** first try, it's not good enough. We take

**[7:31]** sort of an 80/20 approach to it. Like

**[7:33]** there is always the prioritization

**[7:34]** question of like, okay, there are 100

**[7:37]** features that we could be building. What

**[7:39]** are the top 10 that we need to focus on?

**[7:41]** Like some of those are informed by users

**[7:43]** and what what users are are telling us,

**[7:45]** what they're asking for. But very often

**[7:47]** there are ways to build product that

**[7:49]** users may not be asking for, but if you

**[7:52]** build it and a lot of what intuition

**[7:54]** goes into identifying what those

**[7:55]** features might be, then users feel seen

**[7:58]** and they feel like, oh, this is someone

**[8:00]** who is listening to us, even though

**[8:02]** that's not exactly what they asked for

**[8:03]** initially. I'll give you an example. The

**[8:05]** feature on iOS or Android that like

**[8:08]** anytime you get a two-factor

**[8:10]** authentication SMS, it auto reads your

**[8:12]** SMS and fills it into whichever app

**[8:14]** asked for it. It is hard to imagine like

**[8:16]** a user asking for that feature, but it

**[8:19]** saves a few seconds multiple times a day

**[8:23]** for people all across the world. But

**[8:24]** it's like a tiny thing that makes users

**[8:26]** feel seen. Like, oh, someone is actually

**[8:28]** giving thought how to reduce these tiny

**[8:30]** paper cuts in our in our day-to-day

**[8:31]** life. That's really important. So like

**[8:33]** it is a marriage of intuition with what

**[8:35]** users are actually asking for.

**[8:37]** In a world where it's very easy to come

**[8:40]** up with first prototypes using these

**[8:42]** coding LLMs, the true differentiator is

**[8:45]** in taste and craft, in how intuitive and

**[8:48]** well-designed the product is. One thing

**[8:50]** we do in the team that helps with that,

**[8:52]** I think, is we take dog fooding our own

**[8:55]** product very seriously. Like every

**[8:57]** single week we have an hour hour and a

**[8:59]** half docked out for dog fooding new

**[9:01]** features in the product. At any given

**[9:03]** point of time we're running like tens of

**[9:05]** experiments internally and maybe like

**[9:07]** one of them will ship to the production

**[9:10]** version of the product that external

**[9:12]** users will see. So like constantly dog

**[9:14]** fooding our our own product is a way to

**[9:16]** refine our own taste for like, okay,

**[9:18]** what is good versus bad, what awesome or

**[9:21]** magical feels like. Like anything else,

**[9:23]** a lot of reps to build that muscle is

**[9:26]** like one way to go about it.

**[9:30]** The Grad Camp project was led by one of

**[9:32]** my lab mates. I was sort of a supporting

**[9:34]** author on that paper. I was 25 when we

**[9:36]** did that paper. It's been extremely well

**[9:38]** received. I think 20, 30,000 citations

**[9:41]** is quite non-trivial. At the time,

**[9:43]** interpretability in like around deep

**[9:45]** learning models was like a big area of

**[9:46]** focus. Still is to this day. And so, it

**[9:49]** was motivated from that that like, okay,

**[9:51]** like these models, especially

**[9:53]** classification models to start with,

**[9:55]** that go from like images to classifying

**[9:57]** it in one of 1,000 or 10,000 categories,

**[9:59]** what part of the image are they looking

**[10:01]** at to make those predictions, right?

**[10:03]** There is clearly some signal coming from

**[10:06]** the image itself and then some signal

**[10:07]** that may be coming from the label that

**[10:09]** the classification model is predicting.

**[10:12]** And how can we combine the two, develop

**[10:14]** better intuition for what part of the

**[10:15]** image the model is looking at? To this

**[10:17]** day, it seems to work quite effectively

**[10:20]** across a bunch of tasks and models. Like

**[10:22]** with AI models, it is important for

**[10:25]** models to be able to convey not just the

**[10:27]** final prediction or the final answer,

**[10:29]** but also the proof of work. Like, what

**[10:31]** are the steps that went into coming up

**[10:33]** with this final prediction or the final

**[10:35]** answer. And so, Grad-CAM is like one

**[10:37]** manifestation of that. But even in how

**[10:40]** we build the the Scouts product today,

**[10:42]** like you can set up the Scouts and

**[10:44]** agents to monitor the web for something

**[10:45]** and they will generate these reports and

**[10:47]** notify you when they find something

**[10:49]** that's of value to you. But there is a

**[10:51]** button in the UI that lets you inspect

**[10:53]** the work that went in in behind the

**[10:55]** scenes. Like, which websites were were

**[10:57]** visited, what did the agent actually

**[10:59]** look at to pull out this piece of

**[11:01]** information. And that gives you a

**[11:02]** glimpse into the work that went in

**[11:05]** behind the scenes to put this together.

**[11:06]** very, very important for trust building,

**[11:09]** for users to be able to trust that yes,

**[11:11]** this is a reliable product.

**[11:14]** A lot of our time and attention in how

**[11:16]** we are building our product at Unitary

**[11:18]** goes into thinking about, how should we

**[11:21]** build the product so that we don't make

**[11:22]** the same mistake? Whenever we ship

**[11:24]** something, we have to get it right. It

**[11:25]** has to really work. It has to be

**[11:27]** reliable. Users have to trust that it

**[11:29]** works well. If you put attention to

**[11:31]** detail into parts of the product that

**[11:34]** users can see, then the user is more

**[11:36]** likely to trust the parts of the product

**[11:38]** that they cannot see. Right? Like

**[11:39]** everything awesome that we see around

**[11:41]** us, it's like individuals or groups who

**[11:45]** put in a lot of hard work and attention

**[11:48]** to detail to build that. So, I think we

**[11:50]** should approach everything that we are

**[11:52]** building with that kind of philosophy.

**[11:54]** It takes time to build something

**[11:56]** meaningful, to build something right, to

**[11:57]** bring a vision of the future to life.

**[12:00]** And building like delightful and

**[12:01]** reliable product experiences, it doesn't

**[12:03]** just appear out of nowhere.
