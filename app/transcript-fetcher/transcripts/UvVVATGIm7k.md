# Transcript: Claude Code Cuts Token Usage by 94% | Here's Why

**URL:** https://www.youtube.com/watch?v=UvVVATGIm7k
**Segments:** 548
**Channel:** Eric Tech
**Duration:** 17:14
**Uploaded:** 2026-06-23

---

## Full Text

If you're using Claude code, then you've got to check out the skill called ponytail because this skill can help you to writing less code, help you to consume less token, and also help you to refactor code base and make it much more reusable. And honestly, this is going to be a game-changer because if you were to compare this to the previous skills like caveman, you can see that this is how much it reduced. So, this is the reduction for line of code, token, cost, time. You can see it has reduced so much. And it's actually doing this by following these seven steps on how we can be able to writing code that's reusable and also help you to consume less tokens in terms of reusability for code base. And honestly, this skill is really important if you're building a SaaS product or production application and you actually want to make your application here scalable, reusable, and whenever you're adding a new feature, it doesn't just creating a stuff from scratch, but it's actually reusing things that are already created existingly, then this skill here is a perfect fit for you. So, that's why in this video, I'm showing you a full tutorial on how you can install it. And I'm also going to show you a practical demo on how I refactor my entire production applications, bookzero.ai, using the skill to go minimal here for my project. And most importantly, I'm also going to show you my take on how I would use a skill combined with other skills that we talked about on this channel. So, with that being said, if that sounds interesting, let's get into the video. Now, before we continue, I recently launched our school community where I help you to master AI agents, automations, and so much more. And that's all coming from someone who used to work as a senior AI software engineer at companies like Amazon and Microsoft. And in this community, you're going to get over 100 plus video materials like templates and workflows that I personally built and sold over 100 plus times. On top of that, you're also going to get access to our weekly live calls. And just to give you an idea, this week we're actually running a Claude code masterclass where we're going to dive into how to improve Claude code's accuracy and we're going to use it to building applications. Plus, you're also going to get full community supports where you're going to get a chance to ask questions and get direct answers back. So, if you're ready to level up, make sure you jump right in and I'll see you in a community. All right, so to get started, first thing first, we're going to talk about is how does it actually work behind the scene? So, right here you can see it tells you exactly these are the seven steps that it follows before it writes a single line of code. So, you provide a prompt on this exactly what you want to have a here to build and here is the list of things that it check. First of all, does it actually really even need this, right? Can we skip this and it follows this you on you ain't going to need it principle and try to see if we can be able to go minimal with this. And then second step what it does is check to see if this feature already exists inside of a code base. Can we actually be able to reuse similar components inside of a code base here to basically make this happen, right? So, take a look at my project that I built called bugzero.ai and you can see that I have a receipt page and also transaction page. So, rather than just creating a brand new table from scratch, maybe we can be able to reuse some components that we already have inside our application, right? So, that's basically the sweet part is that we can be able to reuse components rather than just building or reinventing something from from scratch, right? And can we be able to use a standard library? So, based on the prompt, based on the instruction you give, can we actually use a standard library here to to resolve this rather than just creating something new? And if that doesn't work, then we check to see if we have a native platform feature, right? A installed dependencies, right? Is there like a dependency that we can install to make this work? And if that doesn't cut it, then we also going to check to see if we can be able to fix it in just one single line. Maybe calling a function, maybe try to go with minimal here and only then that minimal here is going to start to writing code, right? Apply that to our code writing here to have our AI agent here to write minimal code to satisfy what we need. And that's basically what Ponytail here follows whenever it's writing code behind the scene. All right. So, now you know exactly how this work. Let me show you exactly what are skills that Ponytail offers and how we can be able to install it. Now, to install this, simply all we have to do here is going to start our Clockwork session. So, right here Here can see in my terminal, I'm going to start a new Clockwork right here. And then that's what I'm going to do here is we're going to install this add this plugin here into our marketplace. So, in this case, I'm going to do type in this command right here and simply is going to add this plugins into our marketplace. So, the next thing I'm going to do here is we're going to install it once we added. So, I'm going to copy that command and try to install this plugins into our plugins here. So, in this case, you can see we're now prompted with a couple options. So, either we're going to install it with our user scope or it's going to install it for all the collaborators on this repositories. So, maybe you have a team members on working on this repository. So, you can also choose the second option here to actually install all the collaborators in this repository. So, I'm going to go with that option here. So, once we have this installed, the next thing I'm going to do here is to restart our Clowder session. And simply, if I were to cut this terminal and restart it, now you can see if I were to type in Ponytail, for example, here you can see we have all the skills that we can use for Ponytail. Okay, so once we have the Ponytail installed, the next thing I'm going to do here is see what are the skills that we can use Ponytail for, right? What can we do with this? So, right here you can see I have created a diagram and basically you can see this is how we can use Ponytail. So, we install once and we can literally just apply that for all kinds of app building process. So, there's two path. One is we can be able to turn this always on. So, every time when we have AI here writing code, it's going to follow this seven-step process, seven ladders, which we'll talk about it just now, right? And the other option we can do is the on-demand commands. So, for example, let's say for a specific process, maybe at this part right here, beginning part, we're not using Ponytail at all. Maybe you're using Sue Power, you're using G Stack, or maybe you're using something else. And once you have everything finished, you want to have Ponytail here to review things, or you want to Ponytail here to audit things, or doing like a collection for audit, you can also do that, right? That's basically the on-demand skills, which we will talk about in a second. But you can see that we can be able to have this always on when writing code, or we can have this always be triggered on demand, or after we using like G Stack or other skills, we can go to using those skills like ponytail offers and try to continue forward. All right? So, basically you can see that these are some skills, on demand skills that we can trigger ponytail for. And personally, I think that triggering this skill on demand is probably the best option because, honestly, for a production application that I have right now, I have a lot of skills like superpower, G stack, and skills that I built on my own, real me skills, tons of it. And I don't want to have ponytail to pollute with other skills that I have. So, I prefer the trigger on demand part, and you can see that for trigger on demand, there's actually six skills that we can use for ponytail for. One is ponytail ultra, which codebase here, maybe you have a codebase that's over engineered, and you actually want a ponytail here to simplify things instead of just over engineer, right? And that's going to be the skill that you're going to use. And we also have our ponytail review, which before you committing things, maybe you just working on a project, you have some stuff in your commits, and you want to have ponytail here to review and try to trim things down before you actually commit it, then that's going to be a skill for that. We also have our ponytail audit, so it's going to do a cleanup for the entire repository, try to do audit to see exactly what are the things that we need to simplify down. There's also the ponytail debit, which will basically try to push things down later. Maybe you have a feature that you want to ship quickly, and you want it to defer that later. And that's exactly what it does. Ponytail gain, which will basically prove the impact. So, let's say you want to see the difference between using ponytail without using ponytail, that's going to be a skill to help you to do that. And the last part here is temporary disable the ponytail, and that's going to be the ponytail off. So, pretty much these are all the on demand skills that we have for ponytail, and honestly, in this video, I'm going to show exactly how we can use the ponytail on demand skills to really see the difference what ponytail here offers us, right? For making our application here simple. So, for this project that I built, bug zero AI, this is the whole repository that we have, okay? There's a lot of code, a lot of skills, and what I want to do here is I wanted to actually have it do an audit first and try to see, you know, is there anything that we need to really fix, right? Is there anything that we can do to make a difference and try to simplify things down, okay? So, I'm going to type in ponytail and we're just going to choose the audit skill here and let's try to do an entire audit for the entire code base and try to see what it does. Okay, so first thing's first, you can see here that it has run a repository-wide over-engineer audit and try to scan for anything that are over-engineer currently inside of our repository. And right here you can see it has scanned over 200,000 lines of code across 1,000 source files. And here you can see it has found out multiple sub-agent here to basically have a multiple agent here to look at it. So, here you can see we have different sub-agent here and they're all done. So, it looked things like dead code, flags, configs, over abstract services or types, hand-rolled for the standard libraries or dependencies, and also the single implementation interface and factories, right? So, these are the things that it looked for. And if we were scrolling down here, you can see here is the entire summary of the audit. And honestly, for better viewing experience, I asked it to generate a table to show me exactly what are the features and pages that's going to be affected based on the changes that you propose. So, right here you can see these are the list of features and pages. So, the cloud imports, the exports, the import page, the admin, AI chat. So, you can see that this is what it recommends. And also, does it actually affect the user experience? So, here you can see this is what it listed out. Now, I usually don't trust what AI gave us. Like usually stuff like this, I usually don't trust it. But what my recommendation to you is let's say if it actually does a big refactor into your code base and you are pretty scared if it actually will make a big difference in the production applications, then I highly recommend just creating a staging environment, which is a clone version or duplicate [clears throat] version of your production, but you're not using the same database or same, you know, deployment platforms or same projects as the production, and you're keeping the environment here to be separate, right? This way, you can have a standalone environment that you can test the changes that ponytail has done for the refactoring work. So, once you have that done, you merge it to staging, you test them manually, everything's all working fine, then you can be able to merge it to the production and safely, if it doesn't work, you can actually do a rollback, but that won't be able to affect the changes for your production this is not something that your customer are using. This is what your customer are using, but this is not because this is just a testing environment that you can be able to test the changes that you have done for the refactoring work. So, that's what I recommend, just creating a duplicate version of your production in a staging environment, test it before you actually push it to production. But then back to the summary here, you can see the only removal that it has done is the testing file that it has created for the one-off thing. So, those are only for development only, so they're safe to delete. But the everything else here you can see is just internal refactorings, but the behaviors are identical to what we have right now. And the only thing that might carries some real risk is the cloud import. So, again, test it in a staging environment here to make sure that it actually works before you move on to your production. And the second thing that I did here is I also ask you to generate a spec, right? To create a spec.md file for the requirements on what are things we're going to refactor. Now, the reason why we do this is because we're going to using our own spec driven development here to take over from rest. Because we're only using ponytail here to do the audit, right? To help us to identify what is wrong with our code base. And from now on, we're using our spec driven development skills here to actually have AI here to do the implementation with the highest accuracy. And if you're new to spec driven development here, I actually have a tons of video on this channel which I talk about spec driven developments on this topic. So, the most popular one that I have is called the cloud with superpower. That one is a really lightweight and is really beginner-friendly. So, if you're new to spectrum developments, you can check out this video right here, which I talk about how you can have Clocko here to implement things with highest accuracy when you're building applications or vibe coding in general. And essentially, what I'm going to do here is I'm simply going to use the superpower here to basically try to do a spectrum development plus test-driven development here to basically implement the changes with the highest accuracy. Now, the reason why we say it's highest accuracy is because it follows something called test-driven developments, which means that it will first write a test first before it does the implementation or refactoring. And you can see here that this is really important because whenever we're doing refactoring, we need to know exactly what is the current expected behavior by simply putting that or translating that into an automation test that we can be the one to verify if the actual refactoring here doesn't really change any expected behavior that we currently have. And that's where superpower really shines is in following test-driven development here to make this happen. So, what we do here is we're going to have the spec that the point tool has generated. We pass it to superpower, and superpower here is going to translate that into a plan and to-do list on exactly what Clocko here is going to do, and it's going to follow test-driven development here to make this happen. So now, if I want to come back here inside of Clocko session, and here you can see I started a new session. Simply, I'm just going to run or trigger the using superpower skill. Now, superpower skill here is going to take the prompt that I wrote and try to trigger the right superpower skill to finish this. So, I provide a doc for the spec, and you can see this is the MD file. And I said, "Hey, I want you to take it from here, plan this, tackle this, and try to complete it, okay?" And you can see that it triggers the writing plan skill and try to turn that into a to-do list on exactly how Clocko is going to implement this step by step. So, here you can see it creates a plan. So, let's take a look at this plan right here. Uh you can see that it breaks this entire refactoring work into multiple pull requests. So, pull request one, you can see these are the to-do lists on the things that we're going to do. And the pull request two, you can see here is the to-do list. So, it gives you a checkpoint for each and everything. And while we're doing this, you can see it basically creates a plan, save it into our local files, break it down into different tiers, and it also asked me different questions. So, I also have answered that already. So, for example, do we want to break it down into two tiers or four tiers? I said two tiers. And also, should we create a GitHub issue? yes. So, then once it has gone ahead and do that, I said yes, why don't you go ahead and try to do implementation. But most important part, you can see that for each pull request, it has mentioned that it's going to do a type check and also do NPM test. To making sure that our current test here is actually passing before we actually going to, you know, implement any new changes, right? So, that's the most important part is making sure that we're testing everything before we actually do the implementation or the refactoring work. So, here you can see currently it's actually building right now. So, I'm going to scrolling down right now. You can see currently it's actually creating the changes, creating the pull request as we speak. And already you can see here that we already switched over to a different branch now. Currently we're in tier two. So, I'm just going to have clock here using superpower to take over the rest, try to do the refactoring work, and everything else. >> Before we jump back in, I want to show you something I've been testing recently, especially if you do any product work or UI prototyping. So, I'm in Figma right now using UX Pilot's Nody agent, and what caught my attention is this isn't one of those AI tools where you go to some separate browser tab, generate a mock-up, then drag everything back into Figma and clean it up. Everything happens right here in the canvas. So, I can prompt something like build me a SaaS analytics dashboard, and it starts generating directly inside my Figma file. But what's cool is it's not just making random UI. It can actually pull from your existing components and design system, which is where most AI tools kind of fall apart. Like I imported a component library here, and if I tell it to extend this flow with a settings page, it reuses those same buttons, cards, spacing, all of that, instead of hallucinating some totally different interface. That's a huge difference. And what I like is I can iterate without regenerating everything. Like, I can click just this section here, prompt it to change only this dashboard module, and it updates that part without wrecking the rest of the screen, which honestly feels much closer to how real design work actually happens. And they have this credit model that lets you work through a ton of screens without hitting those annoying AI session limits, which is surprisingly nice when you're iterating a lot. If you do product design, build SaaS, or even just prototype ideas before coding them, it's worth trying. They've got a free tier. I'll leave a link below if you want to check out UX Pilot. All right, let's get back to it. All right, so finally, you can see we have Ponytail here, created a bunch of pull requests, and now we're ready for review. All right, so pretty much that's it for this video on how we can use Ponytail here to install it and showing you exactly a practical demo on how I I would use Ponytail here to do a full audit and try to use it our own scale here to take it from there, okay? Now, this basically my take on how to use Ponytail. I would never use Ponytail here to overwrite a system prompt. And because I have tons of skills, and I just wanted to trigger Ponytail here on demand. And if I were triggered on demand, I would probably just use it for like reviewing code or do a full refactor code and try to simplify things before we make a big commit. That's probably when I would use Ponytail along with like Superpower or like any other things for doing implementations. But pretty much that's how I would use it. Comment down below on how you would use Ponytail. I would love to hear that. So, pretty much that's it for this video. I'll see you in the next video.

---

## Timestamped Segments

**[0:00]** If you're using Claude code, then you've

**[0:01]** got to check out the skill called

**[0:02]** ponytail because this skill can help you

**[0:04]** to writing less code, help you to

**[0:06]** consume less token, and also help you to

**[0:08]** refactor code base and make it much more

**[0:10]** reusable. And honestly, this is going to

**[0:11]** be a game-changer because if you were to

**[0:12]** compare this to the previous skills like

**[0:14]** caveman, you can see that this is how

**[0:16]** much it reduced. So, this is the

**[0:18]** reduction for line of code, token, cost,

**[0:21]** time. You can see it has reduced so

**[0:24]** much. And it's actually doing this by

**[0:25]** following these seven steps on how we

**[0:27]** can be able to writing code that's

**[0:29]** reusable and also help you to consume

**[0:31]** less tokens in terms of reusability for

**[0:33]** code base. And honestly, this skill is

**[0:35]** really important if you're building a

**[0:36]** SaaS product or production application

**[0:39]** and you actually want to make your

**[0:40]** application here scalable, reusable, and

**[0:42]** whenever you're adding a new feature, it

**[0:44]** doesn't just creating a stuff from

**[0:45]** scratch, but it's actually reusing

**[0:47]** things that are already created

**[0:48]** existingly, then this skill here is a

**[0:50]** perfect fit for you. So, that's why in

**[0:52]** this video, I'm showing you a full

**[0:53]** tutorial on how you can install it. And

**[0:54]** I'm also going to show you a practical

**[0:55]** demo on how I refactor my entire

**[0:57]** production applications, bookzero.ai,

**[1:00]** using the skill to go minimal here for

**[1:02]** my project. And most importantly, I'm

**[1:04]** also going to show you my take on how I

**[1:06]** would use a skill combined with other

**[1:07]** skills that we talked about on this

**[1:08]** channel. So, with that being said, if

**[1:10]** that sounds interesting, let's get into

**[1:11]** the video. Now, before we continue, I

**[1:13]** recently launched our school community

**[1:15]** where I help you to master AI agents,

**[1:17]** automations, and so much more. And

**[1:19]** that's all coming from someone who used

**[1:20]** to work as a senior AI software engineer

**[1:22]** at companies like Amazon and Microsoft.

**[1:25]** And in this community, you're going to

**[1:26]** get over 100 plus video materials like

**[1:28]** templates and workflows that I

**[1:30]** personally built and sold over 100 plus

**[1:32]** times. On top of that, you're also going

**[1:34]** to get access to our weekly live calls.

**[1:36]** And just to give you an idea, this week

**[1:37]** we're actually running a Claude code

**[1:39]** masterclass where we're going to dive

**[1:40]** into how to improve Claude code's

**[1:42]** accuracy and we're going to use it to

**[1:43]** building applications. Plus, you're also

**[1:45]** going to get full community supports

**[1:47]** where you're going to get a chance to

**[1:48]** ask questions and get direct answers

**[1:49]** back. So, if you're ready to level up,

**[1:51]** make sure you jump right in and I'll see

**[1:52]** you in a community. All right, so to get

**[1:54]** started, first thing first, we're going

**[1:55]** to talk about is how does it actually

**[1:57]** work behind the scene? So, right here

**[1:59]** you can see it tells you exactly these

**[2:00]** are the seven steps that it follows

**[2:02]** before it writes a single line of code.

**[2:04]** So, you provide a prompt on this exactly

**[2:06]** what you want to have a here to build

**[2:09]** and here is the list of things that it

**[2:10]** check. First of all, does it actually

**[2:12]** really even need this, right? Can we

**[2:14]** skip this and it follows this you on you

**[2:17]** ain't going to need it principle and try

**[2:19]** to see if we can be able to go minimal

**[2:20]** with this. And then second step what it

**[2:22]** does is check to see if this feature

**[2:24]** already exists inside of a code base.

**[2:26]** Can we actually be able to reuse similar

**[2:28]** components inside of a code base here to

**[2:30]** basically make this happen, right? So,

**[2:32]** take a look at my project that I built

**[2:34]** called bugzero.ai and you can see that I

**[2:36]** have a receipt page and also transaction

**[2:38]** page. So, rather than just creating a

**[2:40]** brand new table from scratch, maybe we

**[2:42]** can be able to reuse some components

**[2:44]** that we already have inside our

**[2:46]** application, right? So, that's basically

**[2:48]** the sweet part is that we can be able to

**[2:49]** reuse components rather than just

**[2:51]** building or reinventing something from

**[2:53]** from scratch, right? And can we be able

**[2:55]** to use a standard library? So, based on

**[2:57]** the prompt, based on the instruction you

**[2:59]** give, can we actually use a standard

**[3:01]** library here to to resolve this rather

**[3:03]** than just creating something new? And if

**[3:05]** that doesn't work, then we check to see

**[3:07]** if we have a native platform feature,

**[3:09]** right? A installed dependencies, right?

**[3:12]** Is there like a dependency that we can

**[3:13]** install to make this work? And if that

**[3:16]** doesn't cut it, then we also going to

**[3:17]** check to see if we can be able to fix it

**[3:19]** in just one single line. Maybe calling a

**[3:21]** function, maybe try to go with minimal

**[3:23]** here and only then that minimal here is

**[3:27]** going to start to writing code, right?

**[3:28]** Apply that to our code writing here to

**[3:30]** have our AI agent here to write minimal

**[3:32]** code to satisfy what we need. And that's

**[3:34]** basically what Ponytail here follows

**[3:36]** whenever it's writing code behind the

**[3:38]** scene. All right. So, now you know

**[3:40]** exactly how this work. Let me show you

**[3:41]** exactly what are skills that Ponytail

**[3:43]** offers and how we can be able to install

**[3:45]** it. Now, to install this, simply all we

**[3:47]** have to do here is going to start our

**[3:48]** Clockwork session. So, right here Here

**[3:50]** can see in my terminal, I'm going to

**[3:51]** start a new Clockwork right here. And

**[3:53]** then that's what I'm going to do here is

**[3:54]** we're going to install this add this

**[3:56]** plugin here into our marketplace. So, in

**[3:58]** this case, I'm going to do type in this

**[4:00]** command right here and simply is going

**[4:01]** to add this plugins into our

**[4:03]** marketplace. So, the next thing I'm

**[4:04]** going to do here is we're going to

**[4:05]** install it once we added. So, I'm going

**[4:07]** to copy that command and try to install

**[4:09]** this plugins into our plugins here. So,

**[4:12]** in this case, you can see we're now

**[4:14]** prompted with a couple options. So,

**[4:15]** either we're going to install it with

**[4:16]** our user scope or it's going to install

**[4:18]** it for all the collaborators on this

**[4:20]** repositories. So, maybe you have a team

**[4:22]** members on working on this repository.

**[4:24]** So, you can also choose the second

**[4:25]** option here to actually install all the

**[4:26]** collaborators in this repository. So,

**[4:28]** I'm going to go with that option here.

**[4:30]** So, once we have this installed, the

**[4:32]** next thing I'm going to do here is to

**[4:33]** restart our Clowder session. And simply,

**[4:35]** if I were to cut this terminal and

**[4:37]** restart it, now you can see if I were to

**[4:39]** type in Ponytail, for example, here you

**[4:41]** can see we have all the skills that we

**[4:42]** can use for Ponytail.

**[4:44]** Okay, so once we have the Ponytail

**[4:46]** installed, the next thing I'm going to

**[4:47]** do here is see what are the skills that

**[4:49]** we can use Ponytail for, right? What can

**[4:51]** we do with this? So, right here you can

**[4:53]** see I have created a diagram and

**[4:55]** basically you can see this is how we can

**[4:56]** use Ponytail. So, we install once and we

**[4:59]** can literally just apply that for all

**[5:00]** kinds of app building process. So,

**[5:02]** there's two path. One is we can be able

**[5:04]** to turn this always on. So, every time

**[5:06]** when we have AI here writing code, it's

**[5:08]** going to follow this seven-step process,

**[5:10]** seven ladders, which we'll talk about it

**[5:12]** just now, right? And the other option we

**[5:14]** can do is the on-demand commands. So,

**[5:16]** for example, let's say for a specific

**[5:18]** process, maybe at this part right here,

**[5:19]** beginning part, we're not using Ponytail

**[5:21]** at all. Maybe you're using Sue Power,

**[5:23]** you're using G Stack, or maybe you're

**[5:25]** using something else. And once you have

**[5:27]** everything finished, you want to have

**[5:29]** Ponytail here to review things, or you

**[5:31]** want to Ponytail here to audit things,

**[5:32]** or doing like a collection for audit,

**[5:35]** you can also do that, right? That's

**[5:36]** basically the on-demand skills, which we

**[5:38]** will talk about in a second. But you can

**[5:40]** see that we can be able to have this

**[5:41]** always on when writing code, or we can

**[5:43]** have this always be triggered on demand,

**[5:45]** or after we using like G Stack or other

**[5:47]** skills, we can go to using those skills

**[5:50]** like ponytail offers and try to continue

**[5:52]** forward. All right? So, basically you

**[5:54]** can see that these are some skills, on

**[5:56]** demand skills that we can trigger

**[5:57]** ponytail for. And personally, I think

**[5:59]** that triggering this skill on demand is

**[6:01]** probably the best option because,

**[6:03]** honestly, for a production application

**[6:05]** that I have right now, I have a lot of

**[6:07]** skills like superpower, G stack, and

**[6:09]** skills that I built on my own, real me

**[6:11]** skills, tons of it. And I don't want to

**[6:13]** have ponytail to pollute with other

**[6:16]** skills that I have. So, I prefer the

**[6:18]** trigger on demand part, and you can see

**[6:20]** that for trigger on demand, there's

**[6:21]** actually six skills that we can use for

**[6:23]** ponytail for. One is ponytail ultra,

**[6:26]** which codebase here, maybe you have a

**[6:28]** codebase that's over engineered, and you

**[6:30]** actually want a ponytail here to

**[6:31]** simplify things instead of just over

**[6:34]** engineer, right? And that's going to be

**[6:35]** the skill that you're going to use. And

**[6:37]** we also have our ponytail review, which

**[6:39]** before you committing things, maybe you

**[6:41]** just working on a project, you have some

**[6:42]** stuff in your commits, and you want to

**[6:45]** have ponytail here to review and try to

**[6:46]** trim things down before you actually

**[6:48]** commit it, then that's going to be a

**[6:49]** skill for that.

**[6:51]** We also have our ponytail audit, so it's

**[6:52]** going to do a cleanup for the entire

**[6:54]** repository, try to do audit to see

**[6:56]** exactly what are the things that we need

**[6:58]** to simplify down.

**[7:00]** There's also the ponytail debit, which

**[7:02]** will basically try to push things down

**[7:04]** later. Maybe you have a feature that you

**[7:05]** want to ship quickly, and you want it to

**[7:07]** defer that later. And that's exactly

**[7:09]** what it does.

**[7:10]** Ponytail gain, which will basically

**[7:12]** prove the impact. So, let's say you want

**[7:14]** to see the difference between using

**[7:16]** ponytail without using ponytail, that's

**[7:18]** going to be a skill to help you to do

**[7:19]** that. And the last part here is

**[7:21]** temporary disable the ponytail, and

**[7:23]** that's going to be the ponytail off. So,

**[7:25]** pretty much these are all the on demand

**[7:26]** skills that we have for ponytail, and

**[7:27]** honestly, in this video, I'm going to

**[7:29]** show exactly how we can use the ponytail

**[7:31]** on demand skills to really see the

**[7:33]** difference

**[7:34]** what ponytail here offers us, right? For

**[7:37]** making our application here simple. So,

**[7:40]** for this project that I built, bug zero

**[7:41]** AI, this is the whole repository that we

**[7:44]** have, okay? There's a lot of code, a lot

**[7:45]** of skills, and what I want to do here is

**[7:47]** I wanted to actually have it do an audit

**[7:49]** first and try to see, you know, is there

**[7:51]** anything that we need to really fix,

**[7:52]** right? Is there anything that we can do

**[7:53]** to make a difference and try to simplify

**[7:55]** things down, okay? So, I'm going to type

**[7:57]** in ponytail and we're just going to

**[8:00]** choose the audit skill here and let's

**[8:02]** try to do an entire audit for the entire

**[8:04]** code base and try to see what it does.

**[8:06]** Okay, so first thing's first, you can

**[8:07]** see here that it has run a

**[8:09]** repository-wide

**[8:10]** over-engineer audit and try to scan for

**[8:13]** anything that are over-engineer

**[8:15]** currently inside of our repository. And

**[8:17]** right here you can see it has scanned

**[8:18]** over 200,000 lines of code across 1,000

**[8:21]** source files. And here you can see it

**[8:23]** has found out multiple sub-agent here to

**[8:25]** basically have a multiple agent here to

**[8:26]** look at it. So, here you can see we have

**[8:28]** different sub-agent here and they're all

**[8:30]** done. So, it looked things like dead

**[8:32]** code, flags, configs, over abstract

**[8:34]** services or types,

**[8:36]** hand-rolled for the standard libraries

**[8:38]** or dependencies, and also the single

**[8:41]** implementation interface and factories,

**[8:43]** right? So, these are the things that it

**[8:45]** looked for. And if we were scrolling

**[8:46]** down here, you can see here is the

**[8:48]** entire summary of the audit. And

**[8:51]** honestly, for better viewing experience,

**[8:52]** I asked it to generate a table to show

**[8:54]** me exactly what are the features and

**[8:56]** pages that's going to be affected based

**[8:58]** on the changes that you propose. So,

**[8:59]** right here you can see these are the

**[9:00]** list of features and pages. So, the

**[9:02]** cloud imports, the exports, the import

**[9:05]** page, the admin, AI chat. So, you can

**[9:08]** see that this is what it recommends. And

**[9:10]** also, does it actually affect the user

**[9:12]** experience? So, here you can see this is

**[9:14]** what it listed out. Now, I usually don't

**[9:16]** trust what AI gave us. Like usually

**[9:18]** stuff like this, I usually don't trust

**[9:20]** it. But what my recommendation to you is

**[9:22]** let's say if it actually does a big

**[9:24]** refactor into your code base and you are

**[9:26]** pretty scared if it actually will make a

**[9:27]** big difference in the production

**[9:29]** applications, then I highly recommend

**[9:31]** just creating a staging environment,

**[9:33]** which is a clone version or duplicate

**[9:35]** [clears throat] version of your

**[9:35]** production, but you're not using the

**[9:37]** same database or same, you know,

**[9:39]** deployment platforms or same projects as

**[9:42]** the production, and you're keeping the

**[9:44]** environment here to be separate, right?

**[9:46]** This way, you can have a standalone

**[9:48]** environment that you can test the

**[9:49]** changes that ponytail has done for the

**[9:51]** refactoring work. So, once you have that

**[9:53]** done, you merge it to staging, you test

**[9:55]** them manually, everything's all working

**[9:57]** fine, then you can be able to merge it

**[9:59]** to the production and safely, if it

**[10:01]** doesn't work, you can actually do a

**[10:02]** rollback, but that won't be able to

**[10:04]** affect the changes for your production

**[10:06]** this is not something that your customer

**[10:08]** are using. This is what your customer

**[10:10]** are using, but this is not because this

**[10:12]** is just a testing environment that you

**[10:14]** can be able to test the changes that you

**[10:15]** have done for the refactoring work. So,

**[10:17]** that's what I recommend, just creating a

**[10:19]** duplicate version of your production in

**[10:20]** a staging environment, test it before

**[10:22]** you actually push it to production. But

**[10:24]** then back to the summary here, you can

**[10:25]** see the only removal that it has done is

**[10:27]** the testing file that it has created for

**[10:29]** the one-off thing. So, those are only

**[10:31]** for development only, so they're safe to

**[10:33]** delete. But the everything else here you

**[10:35]** can see is just internal refactorings,

**[10:37]** but the behaviors are identical to what

**[10:40]** we have right now. And the only thing

**[10:42]** that might carries some real risk is the

**[10:44]** cloud import. So, again, test it in a

**[10:47]** staging environment here to make sure

**[10:48]** that it actually works before you move

**[10:50]** on to your production. And the second

**[10:52]** thing that I did here is I also ask you

**[10:54]** to generate a spec, right? To create a

**[10:56]** spec.md file for the requirements on

**[10:58]** what are things we're going to refactor.

**[11:00]** Now, the reason why we do this is

**[11:01]** because we're going to using our own

**[11:03]** spec driven development here to take

**[11:05]** over from rest. Because we're only using

**[11:07]** ponytail here to do the audit, right? To

**[11:10]** help us to identify what is wrong with

**[11:11]** our code base. And from now on, we're

**[11:13]** using our spec driven development skills

**[11:15]** here to actually have AI here to do the

**[11:17]** implementation with the highest

**[11:18]** accuracy. And if you're new to spec

**[11:20]** driven development here, I actually have

**[11:21]** a tons of video on this channel which I

**[11:23]** talk about spec driven developments on

**[11:24]** this topic. So, the most popular one

**[11:27]** that I have is called the cloud with

**[11:29]** superpower. That one is a really

**[11:30]** lightweight and is really

**[11:31]** beginner-friendly. So, if you're new to

**[11:33]** spectrum developments, you can check out

**[11:34]** this video right here, which I talk

**[11:36]** about how you can have Clocko here to

**[11:38]** implement things with highest accuracy

**[11:39]** when you're building applications or

**[11:41]** vibe coding in general. And essentially,

**[11:43]** what I'm going to do here is I'm simply

**[11:44]** going to use the superpower here to

**[11:46]** basically try to do a spectrum

**[11:47]** development plus test-driven development

**[11:49]** here to basically implement the changes

**[11:51]** with the highest accuracy. Now, the

**[11:53]** reason why we say it's highest accuracy

**[11:54]** is because it follows something called

**[11:56]** test-driven developments, which means

**[11:58]** that it will first write a test first

**[12:00]** before it does the implementation or

**[12:02]** refactoring. And you can see here that

**[12:04]** this is really important because

**[12:05]** whenever we're doing refactoring, we

**[12:07]** need to know exactly what is the current

**[12:09]** expected behavior by simply putting that

**[12:11]** or translating that into an automation

**[12:13]** test that we can be the one to verify if

**[12:15]** the actual refactoring here doesn't

**[12:17]** really change any expected behavior that

**[12:20]** we currently have. And that's where

**[12:21]** superpower really shines is in following

**[12:23]** test-driven development here to make

**[12:25]** this happen. So, what we do here is

**[12:27]** we're going to have the spec that the

**[12:29]** point tool has generated. We pass it to

**[12:31]** superpower, and superpower here is going

**[12:33]** to translate that into a plan and to-do

**[12:35]** list on exactly what Clocko here is

**[12:37]** going to do, and it's going to follow

**[12:39]** test-driven development here to make

**[12:40]** this happen. So now, if I want to come

**[12:41]** back here inside of Clocko session, and

**[12:44]** here you can see I started a new

**[12:45]** session. Simply, I'm just going to run

**[12:48]** or trigger the using superpower skill.

**[12:50]** Now, superpower skill here is going to

**[12:52]** take the prompt that I wrote and try to

**[12:54]** trigger the right superpower skill to

**[12:56]** finish this. So, I provide a doc for the

**[12:59]** spec, and you can see this is the MD

**[13:00]** file. And I said, "Hey, I want you to

**[13:02]** take it from here, plan this, tackle

**[13:04]** this, and try to complete it, okay?" And

**[13:07]** you can see that it triggers the writing

**[13:08]** plan skill and try to turn that into a

**[13:11]** to-do list on exactly how Clocko is

**[13:13]** going to implement this step by step.

**[13:15]** So, here you can see it creates a plan.

**[13:17]** So, let's take a look at this plan right

**[13:18]** here. Uh you can see that it breaks this

**[13:21]** entire refactoring work into multiple

**[13:23]** pull requests. So, pull request one, you

**[13:25]** can see these are the to-do lists on the

**[13:27]** things that we're going to do. And the

**[13:29]** pull request two, you can see here is

**[13:31]** the to-do list. So, it gives you a

**[13:33]** checkpoint for each and everything. And

**[13:36]** while we're doing this, you can see it

**[13:38]** basically creates a plan, save it into

**[13:40]** our local files, break it down into

**[13:42]** different tiers, and it also asked me

**[13:44]** different questions. So, I also have

**[13:46]** answered that already. So, for example,

**[13:48]** do we want to break it down into two

**[13:50]** tiers or four tiers? I said two tiers.

**[13:53]** And also, should we create a GitHub

**[13:54]** issue? yes. So, then once it has gone

**[13:57]** ahead and do that, I said yes, why don't

**[13:59]** you go ahead and try to do

**[14:00]** implementation. But most important part,

**[14:02]** you can see that for each pull request,

**[14:03]** it has mentioned that it's going to do a

**[14:04]** type check and also do NPM test. To

**[14:07]** making sure that our current test here

**[14:09]** is actually passing before we actually

**[14:11]** going to, you know, implement any new

**[14:13]** changes, right? So, that's the most

**[14:14]** important part is making sure that we're

**[14:16]** testing everything before we actually do

**[14:18]** the implementation or the refactoring

**[14:20]** work. So,

**[14:22]** here you can see currently it's actually

**[14:23]** building right now. So, I'm going to

**[14:25]** scrolling down right now. You can see

**[14:26]** currently it's actually creating the

**[14:28]** changes, creating the pull request as we

**[14:30]** speak. And already you can see here that

**[14:32]** we already switched over to a different

**[14:34]** branch now. Currently we're in tier two.

**[14:36]** So, I'm just going to have clock here

**[14:38]** using superpower to take over the rest,

**[14:40]** try to do the refactoring work, and

**[14:42]** everything else.

**[14:42]** >> Before we jump back in, I want to show

**[14:44]** you something I've been testing

**[14:45]** recently, especially if you do any

**[14:47]** product work or UI prototyping. So, I'm

**[14:50]** in Figma right now using UX Pilot's Nody

**[14:52]** agent, and what caught my attention is

**[14:54]** this isn't one of those AI tools where

**[14:56]** you go to some separate browser tab,

**[14:58]** generate a mock-up, then drag everything

**[15:00]** back into Figma and clean it up.

**[15:02]** Everything happens right here in the

**[15:04]** canvas. So, I can prompt something like

**[15:06]** build me a SaaS analytics dashboard, and

**[15:09]** it starts generating directly inside my

**[15:11]** Figma file. But what's cool is it's not

**[15:13]** just making random UI. It can actually

**[15:15]** pull from your existing components and

**[15:17]** design system, which is where most AI

**[15:19]** tools kind of fall apart. Like I

**[15:21]** imported a component library here, and

**[15:23]** if I tell it to extend this flow with a

**[15:25]** settings page, it reuses those same

**[15:27]** buttons, cards, spacing, all of that,

**[15:30]** instead of hallucinating some totally

**[15:32]** different interface. That's a huge

**[15:34]** difference. And what I like is I can

**[15:36]** iterate without regenerating everything.

**[15:38]** Like, I can click just this section

**[15:40]** here, prompt it to change only this

**[15:42]** dashboard module, and it updates that

**[15:44]** part without wrecking the rest of the

**[15:46]** screen, which honestly feels much closer

**[15:48]** to how real design work actually

**[15:50]** happens. And they have this credit model

**[15:52]** that lets you work through a ton of

**[15:53]** screens without hitting those annoying

**[15:55]** AI session limits, which is surprisingly

**[15:57]** nice when you're iterating a lot. If you

**[15:59]** do product design, build SaaS, or even

**[16:01]** just prototype ideas before coding them,

**[16:04]** it's worth trying. They've got a free

**[16:05]** tier. I'll leave a link below if you

**[16:07]** want to check out UX Pilot. All right,

**[16:09]** let's get back to it. All right, so

**[16:11]** finally, you can see we have Ponytail

**[16:12]** here, created a bunch of pull requests,

**[16:14]** and now we're ready for review. All

**[16:15]** right, so pretty much that's it for this

**[16:16]** video on how we can use Ponytail here to

**[16:19]** install it and showing you exactly a

**[16:20]** practical demo on how I I would use

**[16:22]** Ponytail here to do a full audit and try

**[16:24]** to use it our own scale here to take it

**[16:25]** from there, okay? Now, this basically my

**[16:27]** take on how to use Ponytail. I would

**[16:29]** never use Ponytail here to overwrite a

**[16:31]** system prompt. And because I have tons

**[16:33]** of skills, and I just wanted to trigger

**[16:35]** Ponytail here on demand. And if I were

**[16:37]** triggered on demand, I would probably

**[16:38]** just use it for like reviewing code or

**[16:41]** do a full refactor code and try to

**[16:43]** simplify things before we make a big

**[16:44]** commit. That's probably when I would use

**[16:46]** Ponytail along with like Superpower or

**[16:49]** like any other things for doing

**[16:50]** implementations. But pretty much that's

**[16:52]** how I would use it. Comment down below

**[16:54]** on how you would use Ponytail. I would

**[16:56]** love to hear that. So, pretty much

**[16:57]** that's it for this video. I'll see you

**[16:59]** in the next video.
