# Transcript: New Skills! v1.1 brings /wayfinder, /research, /implement, /to-spec, /to-tickets

**URL:** https://www.youtube.com/watch?v=A8mokin_YOs
**Segments:** 437
**Channel:** Matt Pocock
**Duration:** 15:11
**Uploaded:** 2026-07-08

---

## Full Text

Hello friends. First video in a while, and that is because I've been working on version 1.1 of my skills repo. It has an astonishing amount of stuff in there. There is an entire new approach to grilling, which probably deserves its own video, but I'll try and squeeze it in here. There is a bunch of new changes to existing skills, including a rename of two main flow skills. There is just really way too much for me to summarize in this intro, so you're just going to have to watch the video to find out. We can see the PR is literally ready to merge now. So, why not? Let's actually freaking merge this thing. And just like that, we have our version 1.1 ready to go. Let's start with the two that are probably going to be most annoying for you, and the most like, why did he do this? And there is a very specific reason that I did it, which is that two skills have been renamed. For instance, two PRD has now been renamed to two spec. And if we go up one level, then we go to two issues has been renamed to two tickets. The reason I've done this is that this has just been bugging me for a long time. The thing that we were creating in two PRD wasn't actually a PRD. It was a spec. A product requirements document kind of describes more things about the actual product itself, whereas we were allowing things to leak into the PRD that weren't necessarily PRDs. So, for a long time I've wanted to rename it to two spec, cuz that's what we were creating. We were just creating a specification. Specification is a much broader term that actually entails what we were building. for a thing we want to build. That can be technical, it can be non-technical, and it can blend the two. It doesn't really matter. When it came to two issues, two issues always felt like it was biased towards GitHub and linear that use issues, but really we want this to be tickets. You have a spec, and then underneath the spec you have the tickets that are the journey that you take to actually enact the spec and create it. This has been annoying me for a long time, and finally it no longer annoys me. It brings me joy. Now, one irritating thing about this rename is that you will need to probably delete those skills and re-add them. This means you'll need to run NPX skills add Map Po  skills. I'm pretty sure that this skills installer won't pick up the rename, so it won't try to update to PRD to turn it into to spec. You get what I mean. And so, running this command is the safest way to grab all of these new skills cuz you get to just pick and choose which ones you want. And once you've done that, you should probably go through a pass through your skills folder and just check that no bad ones are still in there. So, you want to make sure that you're intentionally grabbing all the right skills. The next change is that I've fixed a couple of bugs that people were having with grill me and grill with docs. Both of them rely on this kind of central reference grilling skill that kind of show shows the LLM how to grill a person. I've sharpened up this line here saying asking multiple questions at once is bewildering. Even with this direction to ask questions one at a time, it was still occasionally just going to have multiple questions at once. So, I've told it why we don't want multiple questions at once. We've also added a confirmation gate on the end. Do not enact the plan until I confirm we've reached a shared understanding. Lots of people on different models were reporting that the grilling session would just end and then it would just go straight into implementation. So, this is just an extra little gate there. Finally, on some situations, it would just grill itself, which is very, very odd. Not something I've noticed or seen in my personal thing, but I I can only get a small subset of how these skills are actually used. So, I've basically tried to use a couple of leading words to indicate the difference between facts and decisions. So, sometimes it was using the previous phrasing here by just exploring the code base and grilling itself. This was especially happening with Fable, actually. And so, I've decided to make a distinction between facts, so facts that are things you find yourself by exploring the code base, and decisions. So, decisions are needed to be made by the user. So, just a couple of sentences, added a couple of things changed around, and this has made it a lot more consistent. Definitely getting a lot fewer complaints about those weird issues happening. The next thing to say is that I've added a couple of skills that really just take the process that was primarily a planning process, didn't really hold your hand into implementation, and turn it into a proper software development life cycle. So, many folks ask me, "What is the flow? What is the main flow you're supposed to use with the skills?" And first of all, I mean, this is it. We have number one, you're supposed to instead of using plan mode, you get an agent to grill you. And it uses these couple of docs to add a glossary, to kind of understand you better as you go along, and also add architectural decision records so you can capture the non-obvious stuff. The stuff that goes in the growth for docs then goes into a spec, as we saw before. That spec kind of defines the destination, where you're going. Then, you turn that spec into individual tickets so you can spread the development of it out over multiple agent sessions. That's the purpose of to tickets. You then implement each one of those tickets with a implement skill. And the implement skill is very, very simple. It just looks like this. Implement the work described by the user in the spec or tickets. Use TDD where possible at pre-agreed seams. That's a nice one. And run type checking regularly, single test files regularly, and full test suite once at the end. Once done, use code review to review the work, and then commit your work to the current branch. I almost didn't make a skill for this because it's really simple, right? It's just mostly relying on the agent's priors, on its, you know, on the harness, kind of teaching it what to do. And I didn't honestly think we needed a skill here, but folks kept asking me, "What's the flow? What's the flow here?" And so, I figured just an implement skill, make it nice and simple, right? At each stage of the process, call this skill. So, that means implement earns its place here because you know, okay, once we got two tickets, then we just got to implement each ticket in a separate coding session. Implement then itself calls code review. And code review, I graduated this out of in progress on version one. So, it's been around for a little bit, but I have made some updates to it in this version two. The theory of the code review skill is that it reviews code on two axes. So, it does a sub agent for each one of these. The first one is the standards axis. Does the code conform to this repo's documented coding standards? So, if you've got a coding standards.md file somewhere in your repo, then it will read that and check against those. I generally think that coding standards belong outside of your agents.md file. They're supposed to be somewhere separate, and the code review point is where they're most useful. And then, once you've done the standards, you then go on to the spec. Does the code faithfully implement the originating issue or PR or spec? They both run as parallel sub agents, and it does a process here where it walks through each part. Now, the thing that's cool and new about this skill is that I've been reading Martin Fowler's refactoring again. And what I decided to do is Martin Fowler names a bunch of different smells that the agent can identify in bad code. Refactoring is such an old book, such a well-cited book, that these uh kind of smells are deep in the agent's priors. And so, all you need to do is kind of invoke the idea Okay, mysterious name or duplicated code or feature envy, data clumps, primitive obsession, repeated switches, divergent change, speculative generality, message chains. You see what I mean? Like, these are all deep in the agent's kind of knowledge base, and all we got to do is just really describe them in a sentence. And what I found is that leads the word or leads the agent to repeat that word back to you and say, "Yes, I found some message chains. I need to remove them. I found a middle man situation. I need to uh fix that." So, I tested this for a couple of weeks and it was outrageously useful. It was really, really nice at improving the quality of my code and it's really cheap to add here, just kind of like 10 lines. But, let's go and talk about the one that I'm really, really excited about, which is a whole new change to the way that we kick off and shape specs. So, the pre-spec bit. In other words, it goes here where it may, in some situations, replace Grill with Docs. And it's called Wayfinder. I will make an entire post uh entire video about Wayfinder, but uh suffice to say is that I would love for you, in situations where you're thinking about using Grill with Docs, instead to default to Wayfinder instead. What Wayfinder does is it's designed for situations where you have a ton of stuff that you want to plan, but and too big for one agent session. In other words, you're going to blow out of the smart zone of the agent or you might even blow out of the context window of the agent. You need to split it into multiple parts in order to figure out where you're going. A loose idea has arrived, too big for one agent session and wrapped in fog. The way from here to the destination isn't visible yet. This skill charts the way as a shared map on the repo's issue tracker, then works its tickets one at a time until the route is clear. These maps are saved in GitHub issues. For instance, this is one on the Sandcastle repo where we're doing a spike to think about maybe pulling in the AI SDK as a dependency, a big, big change. And so, you can see there are no decisions that have um been made so far and all of the decisions that need to be made are saved in sub-issues. And these sub-issues have blocking relationships. So, we can see that no decision can be made here before we make this key decision at the start. Each one of these decisions is scoped to be the size of an agent session. And we can see that they're labeled as different types here. So, for instance, this one is labeled as a research task. So, this is really an AFK task for the agent to go off, do some research, and then come back. This one I think is a research as well. This one is a research task, and this one is a grilling task. So, this one needs a grilling session to be done here. I think these are all grillers. We can see these defined in the ticket types down here. So, we have research, we have grilling, we also have prototype as well. So, this is something I've been really advocating for recently is doing more prototyping before you get to a spec. The idea is you raise the fidelity of the discussion by making a cheap, rough, concrete artifact to react to. An outline, rough tech stub, UI logic code via the prototype skill. We'll get to that in a minute. Links to the prototype as an asset. And it says use when how should it look or how should it behave is a key question. And this is essential for almost anything that touches front-end code. So, I would definitely be recommending using Wayfinder for anything that touches the front-end. The final one here is just tasks. So, config that needs to be set up, um provisioning access, you know, moving data into the shape, you know, all the sort of boring stuff that doesn't need a grilling decision and can't really be automated by AI. What you end up with is after all of these tickets are closed, all of that information gets saved onto the map with the original tickets as kind of primary sources for what was captured. And you can then take this map and just turn it into a spec in the regular way. What I found that instead of having the kind of anxiety of managing my session with grill with docs having to hand off, worry about the smart zone. With Wayfinder, it's kind of all managed for me. I just get to close a session, open up the next Wayfinder ticket. It's all saved in GitHub, so it's collaborative. You can share it across your team. And once the map is done, once it's complete, you just go to to spec, and you're good to go. To support the Wayfinder skill, we have a new research skill, which is very small, very handy for when you just need to do a research session, or it kind of influences the model in researching in the right way as well, or at least the way that I like. Spins up a background agent to do the research so you keep working while it reads. Investigate the question against primary sources, write the findings to a simple markdown file, and save it where the repo already keeps such notes match the existing convention. So this is useful too if you need to do any research, you can just invoke the research skill and you're good to go. The next one, of course, is the prototype, which I've kind of shown off a little bit before. I don't think I've done a full video on it. This is now modeling, folks, so that Wayfinder can invoke it itself, and it essentially gives you a choice between logic or state. So it's either a logic prototype or a UI prototype, and they react quite differently. The final change is something that people have been asking for for a while, and I finally decided to pull the trigger on it, which is before in my TDD skill, it would recommend a set of steps for you to follow, and that was a little bit awkward sometimes. The steps were like, it would confirm what tests it wanted to write with you, and then you would, you know, walk it through, walk it through, and it didn't fit with most people's idea of how TDD should work, which is you should be able to pass an AFK agent the TDD skill, and it should just work. And so this TDD skill is now reference material only. So it doesn't specify any particular steps apart from just the order in which you should write tests in, so to do red green refactor. So it's just says red before green, one slice at a time, and it also splits away refactoring as as not part of the loop. So it's no longer a red green refactor loop, it's more just red green. I tend to think that putting the refactoring in the code review part is a lot more productive because then you don't overload the implementation. So that is all of the changes that have come in on the skills. It is a lot of changes, and if you're nervous about missing any of the updates, then I recommend that you clear out all of your skills and do NPX skills update and grab all of the new ones. If you've made updates to your skills in the meantime, then you can just point your clanker at my repo and just say pull down all of the good new stuff, especially pointing at the release notes. The thing I think this release will be remembered for is to spec and to tickets changing because that is just a little bit of friction, but I think good friction cuz it names it properly. And I hope to be the start of you getting obsessed with Wayfinder. I'm using Wayfinder for literally everything, even non-coding stuff. I've actually been planning my next course with Wayfinder and it's really, really good. In fact, why don't I just show you that course now? This is the AI coding crash course. This is going to be different from the cohorts that I usually run. It's going to be much, much cheaper and it's going to be self-paced so you can purchase it anytime. You get help from the Discord kind of in the usual way, but it's not going to be gated like a normal cohort. It is going to be the perfect intro for anyone who's looking to get into AI coding, whether you are a developer or whether you are not a developer. So, for senior engineers, it's going to be a conversion course. For folks who are new to development, it's going to be the way that you can actually get productive using these crazy new tools. I've not announced a price yet. I am going to just be adding sign-ups in here and it'll be available once I finish filming it, maybe in about August time, I think. But folks, thank you so much for watching. It's always a pleasure sharing these skills updates with you. It is really cool to see the usage just absolutely grow and grow. Everyone tells me I shouldn't show the star counts, but it's up to like 160K stars now. Uh 7 million downloads on skills.sh. It is just bonkers. So, thank you so much for enjoying the skills. I hope they are helping you ship more and ship more productively and I'll see you very soon.

---

## Timestamped Segments

**[0:00]** Hello friends. First video in a while,

**[0:01]** and that is because I've been working on

**[0:03]** version 1.1 of my skills repo. It has an

**[0:07]** astonishing amount of stuff in there.

**[0:08]** There is an entire new approach to

**[0:11]** grilling, which probably deserves its

**[0:13]** own video, but I'll try and squeeze it

**[0:14]** in here. There is a bunch of new changes

**[0:17]** to existing skills, including a rename

**[0:20]** of two main flow skills. There is just

**[0:22]** really way too much for me to summarize

**[0:24]** in this intro, so you're just going to

**[0:26]** have to watch the video to find out. We

**[0:27]** can see the PR is literally ready to

**[0:29]** merge now. So, why not? Let's actually

**[0:31]** freaking merge this thing. And just like

**[0:33]** that, we have our version 1.1 ready to

**[0:37]** go. Let's start with the two that are

**[0:38]** probably going to be most annoying for

**[0:40]** you, and the most like, why did he do

**[0:42]** this? And there is a very specific

**[0:44]** reason that I did it, which is that two

**[0:47]** skills have been renamed. For instance,

**[0:49]** two PRD has now been renamed to two

**[0:53]** spec. And if we go up one level, then we

**[0:55]** go to two issues has been renamed to two

**[0:59]** tickets. The reason I've done this is

**[1:01]** that this has just been bugging me for a

**[1:03]** long time. The thing that we were

**[1:04]** creating in two PRD wasn't actually a

**[1:07]** PRD. It was a spec. A product

**[1:10]** requirements document kind of describes

**[1:13]** more things about the actual product

**[1:15]** itself, whereas we were allowing things

**[1:17]** to leak into the PRD that weren't

**[1:20]** necessarily PRDs. So, for a long time

**[1:22]** I've wanted to rename it to two spec,

**[1:25]** cuz that's what we were creating. We

**[1:26]** were just creating a specification.

**[1:27]** Specification is a much broader term

**[1:30]** that actually entails what we were

**[1:32]** building.

**[1:33]** for a thing we want to build. That can

**[1:35]** be technical, it can be non-technical,

**[1:37]** and it can blend the two. It doesn't

**[1:39]** really matter. When it came to two

**[1:40]** issues, two issues always felt like it

**[1:42]** was biased towards GitHub and linear

**[1:44]** that use issues, but really we want this

**[1:47]** to be tickets. You have a spec, and then

**[1:49]** underneath the spec you have the tickets

**[1:51]** that are the journey that you

**[1:53]** take to actually enact the spec and

**[1:55]** create it. This has been annoying me for

**[1:57]** a long time, and finally it no longer

**[1:58]** annoys me. It brings me joy. Now, one

**[2:00]** irritating thing about this rename is

**[2:02]** that you will need to probably delete

**[2:04]** those skills and re-add them. This means

**[2:06]** you'll need to run NPX skills add Map Po

**[2:09]**  skills. I'm pretty sure that this

**[2:11]** skills installer won't pick up the

**[2:13]** rename, so it won't try to update to PRD

**[2:16]** to turn it into to spec. You get what I

**[2:17]** mean. And so, running this command is

**[2:19]** the safest way to grab all of these new

**[2:21]** skills cuz you get to just pick and

**[2:22]** choose which ones you want. And once

**[2:24]** you've done that, you should probably go

**[2:25]** through a pass through your skills

**[2:27]** folder and just check that no bad ones

**[2:30]** are still in there. So, you want to make

**[2:31]** sure that you're intentionally grabbing

**[2:33]** all the right skills. The next change is

**[2:35]** that I've fixed a couple of bugs that

**[2:37]** people were having with grill me and

**[2:39]** grill with docs. Both of them rely on

**[2:41]** this kind of central reference grilling

**[2:43]** skill that kind of show shows the LLM

**[2:46]** how to grill a person. I've sharpened up

**[2:48]** this line here saying asking multiple

**[2:50]** questions at once is bewildering. Even

**[2:53]** with this direction to ask questions one

**[2:55]** at a time, it was still occasionally

**[2:57]** just going

**[2:59]** to have multiple questions at once. So,

**[3:01]** I've told it why we don't want multiple

**[3:04]** questions at once. We've also added a

**[3:05]** confirmation gate on the end. Do not

**[3:07]** enact the plan until I confirm we've

**[3:09]** reached a shared understanding. Lots of

**[3:11]** people on different models were

**[3:12]** reporting that the grilling session

**[3:14]** would just end and then it would just go

**[3:16]** straight into implementation. So, this

**[3:18]** is just an extra little gate there.

**[3:19]** Finally, on some situations, it would

**[3:22]** just grill itself, which is very, very

**[3:25]** odd. Not something I've noticed or seen

**[3:27]** in my personal thing, but I I can only

**[3:29]** get a small subset of how these skills

**[3:31]** are actually used. So, I've basically

**[3:33]** tried to use a couple of leading words

**[3:35]** to indicate the difference between facts

**[3:38]** and decisions. So, sometimes it was

**[3:40]** using the previous phrasing here by just

**[3:42]** exploring the code base and grilling

**[3:44]** itself. This was especially happening

**[3:45]** with Fable, actually. And so, I've

**[3:48]** decided to make a distinction between

**[3:50]** facts, so facts that are things you find

**[3:53]** yourself by exploring the code base, and

**[3:55]** decisions. So, decisions are needed to

**[3:57]** be made by the user. So, just a couple

**[3:59]** of sentences, added a couple of things

**[4:01]** changed around, and this has made it a

**[4:02]** lot more consistent. Definitely getting

**[4:04]** a lot fewer complaints about those weird

**[4:06]** issues happening. The next thing to say

**[4:07]** is that I've added a couple of skills

**[4:09]** that really just take the process that

**[4:12]** was primarily a planning process, didn't

**[4:14]** really hold your hand into

**[4:16]** implementation, and turn it into a

**[4:18]** proper software development life cycle.

**[4:20]** So, many folks ask me, "What is the

**[4:22]** flow? What is the main flow you're

**[4:23]** supposed to use with the skills?" And

**[4:26]** first of all, I mean, this is it. We

**[4:28]** have number one, you're supposed to

**[4:29]** instead of using plan mode, you get an

**[4:32]** agent to grill you. And it uses these

**[4:34]** couple of docs to add a glossary, to

**[4:37]** kind of understand you better as you go

**[4:39]** along, and also add architectural

**[4:40]** decision records so you can capture the

**[4:42]** non-obvious stuff. The stuff that goes

**[4:44]** in the growth for docs then goes into a

**[4:47]** spec, as we saw before. That spec kind

**[4:49]** of defines the destination, where you're

**[4:52]** going. Then, you turn that spec into

**[4:55]** individual tickets so you can spread the

**[4:57]** development of it out over multiple

**[4:59]** agent sessions. That's the purpose of to

**[5:01]** tickets. You then implement each one of

**[5:03]** those tickets with a implement skill.

**[5:06]** And the implement skill is very, very

**[5:08]** simple. It just looks like this.

**[5:09]** Implement the work described by the user

**[5:11]** in the spec or tickets. Use TDD where

**[5:14]** possible at pre-agreed seams. That's a

**[5:16]** nice one. And run type checking

**[5:18]** regularly, single test files regularly,

**[5:20]** and full test suite once at the end.

**[5:22]** Once done, use code review to review the

**[5:24]** work, and then commit your work to the

**[5:25]** current branch. I almost didn't make a

**[5:27]** skill for this because it's really

**[5:29]** simple, right? It's just mostly relying

**[5:31]** on the agent's priors, on its, you know,

**[5:34]** on the harness, kind of teaching it what

**[5:35]** to do. And I didn't honestly think we

**[5:38]** needed a skill here, but folks kept

**[5:40]** asking me, "What's the flow? What's the

**[5:41]** flow here?" And so, I figured just an

**[5:43]** implement skill, make it nice and

**[5:45]** simple, right? At each stage of the

**[5:46]** process, call this skill. So, that means

**[5:48]** implement earns its place here because

**[5:50]** you know, okay, once we got two tickets,

**[5:53]** then we just got to implement each

**[5:54]** ticket in a separate coding session.

**[5:56]** Implement then itself calls code review.

**[5:59]** And code review, I graduated this out of

**[6:01]** in progress on version one. So, it's

**[6:04]** been around for a little bit, but I have

**[6:06]** made some updates to it in this version

**[6:08]** two. The theory of the code review skill

**[6:09]** is that it reviews code on two axes. So,

**[6:12]** it does a sub agent for each one of

**[6:14]** these. The first one is the standards

**[6:16]** axis. Does the code conform to this

**[6:19]** repo's documented coding standards? So,

**[6:21]** if you've got a coding standards.md file

**[6:24]** somewhere in your repo, then it will

**[6:26]** read that and check against those. I

**[6:28]** generally think that coding standards

**[6:30]** belong outside of your agents.md file.

**[6:33]** They're supposed to be somewhere

**[6:34]** separate, and the code review point is

**[6:36]** where they're most useful. And then,

**[6:39]** once you've done the standards, you then

**[6:40]** go on to the spec. Does the code

**[6:42]** faithfully implement the originating

**[6:44]** issue or PR or spec? They both run as

**[6:46]** parallel sub agents, and it does a

**[6:48]** process here where it walks through each

**[6:51]** part. Now, the thing that's cool and new

**[6:53]** about this skill is that I've been

**[6:54]** reading Martin Fowler's refactoring

**[6:56]** again. And what I decided to do is

**[6:59]** Martin Fowler names a bunch of different

**[7:01]** smells that the agent can identify in

**[7:04]** bad code. Refactoring is such an old

**[7:06]** book, such a well-cited book, that these

**[7:09]** uh kind of smells are deep in the

**[7:11]** agent's priors. And so, all you need to

**[7:13]** do is kind of invoke the idea Okay,

**[7:15]** mysterious name or duplicated code or

**[7:17]** feature envy, data clumps, primitive

**[7:18]** obsession, repeated switches, divergent

**[7:20]** change, speculative generality, message

**[7:22]** chains. You see what I mean? Like, these

**[7:24]** are all deep in the agent's kind of

**[7:26]** knowledge base, and all we got to do is

**[7:28]** just really describe them in a sentence.

**[7:30]** And what I found is that leads the word

**[7:33]** or leads the agent to repeat that word

**[7:35]** back to you and say, "Yes, I found some

**[7:37]** message chains. I need to remove them. I

**[7:40]** found a middle man situation. I need to

**[7:42]** uh fix that." So, I tested this for a

**[7:43]** couple of weeks and it was outrageously

**[7:45]** useful. It was really, really nice at

**[7:47]** improving the quality of my code and

**[7:49]** it's really cheap to add here, just kind

**[7:51]** of like 10 lines. But, let's go and talk

**[7:53]** about the one that I'm really, really

**[7:55]** excited about, which is a whole new

**[7:58]** change to the way that we kick off and

**[8:01]** shape specs. So, the pre-spec bit. In

**[8:04]** other words, it goes here where it may,

**[8:07]** in some situations, replace Grill with

**[8:09]** Docs. And it's called Wayfinder. I will

**[8:11]** make an entire post uh entire video

**[8:14]** about Wayfinder, but uh suffice to say

**[8:16]** is that I would love for you, in

**[8:18]** situations where you're thinking about

**[8:20]** using Grill with Docs, instead to

**[8:22]** default to Wayfinder instead. What

**[8:24]** Wayfinder does is it's designed for

**[8:26]** situations where you have a ton of stuff

**[8:29]** that you want to plan, but and too big

**[8:32]** for one agent session. In other words,

**[8:33]** you're going to blow out of the smart

**[8:35]** zone of the agent or you might even blow

**[8:37]** out of the context window of the agent.

**[8:39]** You need to split it into multiple parts

**[8:41]** in order to figure out where you're

**[8:42]** going. A loose idea has arrived, too big

**[8:44]** for one agent session and wrapped in

**[8:46]** fog. The way from here to the

**[8:47]** destination isn't visible yet. This

**[8:49]** skill charts the way as a shared map on

**[8:52]** the repo's issue tracker, then works its

**[8:54]** tickets one at a time until the route is

**[8:56]** clear. These maps are saved in GitHub

**[8:58]** issues. For instance, this is one on the

**[9:00]** Sandcastle repo where we're doing a

**[9:02]** spike to think about maybe pulling in

**[9:04]** the AI SDK as a dependency, a big, big

**[9:07]** change. And so, you can see there are no

**[9:09]** decisions that have um been made so far

**[9:12]** and all of the decisions that need to be

**[9:14]** made are saved in sub-issues. And these

**[9:16]** sub-issues have blocking relationships.

**[9:19]** So, we can see that no decision can be

**[9:21]** made here before we make this key

**[9:24]** decision at the start. Each one of these

**[9:25]** decisions is scoped to be the size of an

**[9:28]** agent session. And we can see that

**[9:30]** they're labeled as different types here.

**[9:32]** So, for instance, this one is labeled as

**[9:34]** a research task. So, this is really an

**[9:36]** AFK task for the agent to go off, do

**[9:39]** some research, and then come back. This

**[9:41]** one I think is a research as well. This

**[9:43]** one is a research task, and this one is

**[9:45]** a grilling task. So, this one needs a

**[9:48]** grilling session to be done here. I

**[9:50]** think these are all grillers. We can see

**[9:52]** these defined in the ticket types down

**[9:54]** here. So, we have research, we have

**[9:55]** grilling, we also have prototype as

**[9:58]** well. So, this is something I've been

**[10:00]** really advocating for recently is doing

**[10:03]** more prototyping before you get to a

**[10:05]** spec. The idea is you raise the fidelity

**[10:07]** of the discussion by making a cheap,

**[10:08]** rough, concrete artifact to react to. An

**[10:11]** outline, rough tech stub, UI logic code

**[10:13]** via the prototype skill. We'll get to

**[10:15]** that in a minute. Links to the prototype

**[10:17]** as an asset. And it says use when how

**[10:19]** should it look or how should it behave

**[10:21]** is a key question. And this is essential

**[10:24]** for almost anything that touches

**[10:25]** front-end code. So, I would definitely

**[10:27]** be recommending using Wayfinder for

**[10:29]** anything that touches the front-end. The

**[10:31]** final one here is just tasks. So, config

**[10:34]** that needs to be set up, um provisioning

**[10:36]** access, you know, moving data into the

**[10:38]** shape, you know, all the sort of boring

**[10:40]** stuff that doesn't need a grilling

**[10:42]** decision and can't really be automated

**[10:44]** by AI. What you end up with is after all

**[10:46]** of these tickets are closed, all of that

**[10:48]** information gets saved onto the map with

**[10:51]** the original tickets as kind of primary

**[10:53]** sources for what was captured. And you

**[10:55]** can then take this map and just turn it

**[10:58]** into a spec in the regular way. What I

**[11:00]** found that instead of having the kind of

**[11:01]** anxiety of managing my session with

**[11:04]** grill with docs having to hand off,

**[11:06]** worry about the smart zone. With

**[11:07]** Wayfinder, it's kind of all managed for

**[11:09]** me. I just get to close a session, open

**[11:12]** up the next Wayfinder ticket. It's all

**[11:14]** saved in GitHub, so it's collaborative.

**[11:16]** You can share it across your team. And

**[11:17]** once the map is done, once it's

**[11:19]** complete, you just go to to spec, and

**[11:21]** you're good to go. To support the

**[11:22]** Wayfinder skill, we have a new research

**[11:24]** skill, which is very small, very handy

**[11:27]** for when you just need to do a research

**[11:29]** session, or it kind of influences the

**[11:31]** model in researching in the right way as

**[11:33]** well, or at least the way that I like.

**[11:35]** Spins up a background agent to do the

**[11:36]** research so you keep working while it

**[11:38]** reads. Investigate the question against

**[11:40]** primary sources, write the findings to a

**[11:41]** simple markdown file, and save it where

**[11:43]** the repo already keeps such notes match

**[11:45]** the existing convention. So this is

**[11:47]** useful too if you need to do any

**[11:48]** research, you can just invoke the

**[11:50]** research skill and you're good to go.

**[11:51]** The next one, of course, is the

**[11:53]** prototype, which I've kind of shown off

**[11:55]** a little bit before. I don't think I've

**[11:56]** done a full video on it. This is now

**[11:58]** modeling, folks, so that Wayfinder can

**[12:01]** invoke it itself, and it essentially

**[12:03]** gives you a choice between logic or

**[12:05]** state. So it's either a logic prototype

**[12:08]** or a UI prototype, and they react quite

**[12:11]** differently. The final change is

**[12:13]** something that people have been asking

**[12:14]** for for a while, and I finally decided

**[12:16]** to pull the trigger on it, which is

**[12:18]** before in my TDD skill, it would

**[12:20]** recommend a set of steps for you to

**[12:22]** follow, and that was a little bit

**[12:24]** awkward sometimes. The steps were like,

**[12:26]** it would confirm what tests it wanted to

**[12:28]** write with you, and then you would, you

**[12:31]** know, walk it through, walk it through,

**[12:33]** and it didn't fit with most people's

**[12:36]** idea of how TDD should work, which is

**[12:38]** you should be able to pass an AFK agent

**[12:41]** the TDD skill, and it should just work.

**[12:43]** And so this TDD skill is now reference

**[12:46]** material only. So it doesn't specify any

**[12:48]** particular steps apart from just the

**[12:51]** order in which you should write tests

**[12:52]** in, so to do red green refactor. So it's

**[12:55]** just says red before green, one slice at

**[12:56]** a time, and it also splits away

**[12:59]** refactoring as as not part of the loop.

**[13:02]** So it's no longer a red green refactor

**[13:04]** loop, it's more just red green. I tend

**[13:07]** to think that putting the refactoring in

**[13:10]** the code review part is a lot more

**[13:12]** productive because then you don't

**[13:14]** overload the implementation. So that is

**[13:17]** all of the changes that have come in on

**[13:19]** the skills. It is a lot of changes, and

**[13:22]** if you're nervous about missing any of

**[13:24]** the updates, then I recommend that you

**[13:25]** clear out all of your skills and do NPX

**[13:28]** skills update and grab all of the new

**[13:30]** ones. If you've made updates to your

**[13:31]** skills in the meantime, then you can

**[13:33]** just point your clanker at my repo and

**[13:35]** just say pull down all of the good new

**[13:36]** stuff, especially pointing at the

**[13:38]** release notes. The thing I think this

**[13:40]** release will be remembered for is to

**[13:42]** spec and to tickets changing because

**[13:43]** that is just a little bit of friction,

**[13:45]** but I think good friction cuz it names

**[13:47]** it properly. And I hope to be the start

**[13:50]** of you getting obsessed with Wayfinder.

**[13:51]** I'm using Wayfinder for literally

**[13:53]** everything, even non-coding stuff. I've

**[13:55]** actually been planning my next course

**[13:57]** with Wayfinder and it's really, really

**[13:59]** good. In fact, why don't I just show you

**[14:01]** that course now? This is the AI coding

**[14:03]** crash course. This is going to be

**[14:05]** different from the cohorts that I

**[14:07]** usually run. It's going to be much, much

**[14:09]** cheaper and it's going to be self-paced

**[14:11]** so you can purchase it anytime. You get

**[14:13]** help from the Discord kind of in the

**[14:14]** usual way, but it's not going to be

**[14:16]** gated like a normal cohort. It is going

**[14:18]** to be the perfect intro for anyone who's

**[14:21]** looking to get into AI coding, whether

**[14:23]** you are a developer or whether you are

**[14:26]** not a developer. So, for senior

**[14:27]** engineers, it's going to be a conversion

**[14:29]** course. For folks who are new to

**[14:31]** development, it's going to be the way

**[14:33]** that you can actually get productive

**[14:34]** using these crazy new tools. I've not

**[14:36]** announced a price yet. I am going to

**[14:38]** just be adding sign-ups in here and

**[14:40]** it'll be available once I finish filming

**[14:42]** it, maybe in about

**[14:44]** August time, I think. But folks, thank

**[14:46]** you so much for watching. It's always a

**[14:47]** pleasure sharing these skills updates

**[14:49]** with you. It is really cool to see the

**[14:51]** usage just absolutely grow and grow.

**[14:54]** Everyone tells me I shouldn't show the

**[14:55]** star counts, but it's up to like 160K

**[14:57]** stars now. Uh 7 million downloads on

**[15:00]** skills.sh. It is just bonkers. So, thank

**[15:03]** you so much for enjoying the skills. I

**[15:04]** hope they are helping you ship more and

**[15:07]** ship more productively and I'll see you

**[15:09]** very soon.
