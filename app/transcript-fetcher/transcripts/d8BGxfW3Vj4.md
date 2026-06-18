# Transcript: d8BGxfW3Vj4

**URL:** https://www.youtube.com/watch?v=d8BGxfW3Vj4
**Segments:** 364

---

## Full Text

What if one file can fix the biggest problems that every cloud code user deals with? Well, Andre Carpathy listed down the top mistakes that every AI agent makes, and this single claw.md file just codified the fixes for those mistakes. And almost 43,000 people installed it just in the past week. In this video, I'll break down what this magical claw.md does, how it improves your AI agent setup so that you too can use Claude as good as how Karpati does it. And if you're new here, my name is Jay. I spent over a decade working with brands you probably know. Have been in AI since my masters in data science and now I run our AI solutions practice in one of the largest AI communities globally. Let's get started. So some time ago, Andre Karpati, who previously headed Tesla AI and also part of the founding team of OpenAI, made this now viral tweet where he provided a good analysis of how to work with agents better. It's actually a pretty detailed one and you can see here at the bottom that it already garnered 7 almost 8 million views at this point. Now a lot of people took note of this tweet once again because over the past week what happened was this repo called Andre Karpati skills just shot up in popularity over at GitHub now at over 43,000 stars and it was made and published by this developer Forest. So credit where it's due. And if you go to this skill, what it is is basically a single claw.md file to improve claude code behavior which is derived from the observations from that tweet. And I think the reason why it became so popular and viral over the past week is simply because of how simple it is. It's one claw.md file that you just drop into your claw code. And also the solution that it provides here are boiled down to four key principles which I'll talk about in a bit. And I think regardless whether you want to use this claw.md file or not, learning about these principles will level up how you use your AI agents in order to make sure that you get the output that you want whenever you work with claude. But if you were looking to install this and try this out yourself, what you can simply do is to provide your Claude code with this GitHub link. But if you're already using clawed code, most likely you already have a claw.md file. In which case, it would be better for you to provide a more detailed prompt like this where you explain to your agent that you're giving it a set of guidelines called karpati skills and more importantly to suggest to you how you can best integrate it to your specific setup. So this more detailed installation prompt, I will link it down below if you need it. But as I mentioned, the core of this claw.md file are these four principles that I think are worth learning no matter what AI agent you use. So the first principle that it instills to your agent is that it allows claude code to think before coding. And just to refer back to what Andre wrote here, you can see he mentioned that the most common category of mistake that these agents make is that the models make wrong assumptions on your behalf and just run along with them without checking. They also don't manage their confusion. They don't see clarifications and they don't surface inconsistencies. And so the core idea for this principle is this. Without this rule, Claude assumes what you want. With it, Claude asks first. And so if you were to boil down one key principle that you should follow in order to upgrade how you should work with agents better, it is basically this. It is almost always better to have your agent ask you questions in order to clarify intent before it starts building and coding things for you. And so just to illustrate this, what I have here are two cloud code sessions. This one doesn't have the karpati claw.md and this one is where I loaded that claw MD we just talked about. And what I'm going to do is just give each of these agents a copy of this rubric application to illustrate the difference between the approaches of these agents with one of the agents not having this Kpati principle baked in and the other agent following the principle that we just talked about. So now just to show the difference between these two. If I send the same task to both of them where I'm simply requesting let's say to add a toggle for light mode to the rubric app. If we send it to both with this one to recap has that Karpati skill and claw.md already installed. And so now that both of those sessions are done, you can see this one without the carpatic claw. MD confirmed to me that there is a light mode toggle. But if I look at the application it's working on, it doesn't actually have it. And if you compare that with this session which was working on this localhost 10,01, this also confirmed to me that the toggle is in the top right bar next to search. And you can see that it is actually here. And it was able to implement that because it actually thought through the problem and even was able to decide what are the right colors across all of the other icons in here. which if you compare that to this one which was coming from the agent without that claw.md file, it thought that it was able to do the task but not really. And if you want to sort of peek under the hood on why the karpati claw.md is more proficient with what it just did. If you ask both to outline the steps that they just took, you can see the vanilla claw code, it did do some detailed steps like finding the right files, reading the CSS variables, and trying to add a light theme CSS. But if you just compare that with the outline of the steps of the Karpati claude code, you can see this is much more detailed versus what the vanilla claw code did. And so the result of that is that with just one prompt, it was able to oneshot this light theme for us without any issues. Now, real quick, we just released the Agentic AI masterass for our members at RoboNuggets, which takes you from zero to mastery when working with agents. There's a link to the community in the pinned comment below. We've got founders in there who landed their first client in weeks, live build sessions where we create this stuff together, and the actual templates behind what I showed in this video. The community is also the reason these lessons get made. So see that below if that's for you. The second principle that it implements is to put simplicity first. And just going back to what Andre wrote here, he mentioned that these AI agents by default will implement an inefficient, bloated, and brittle construction, which is sometimes over a thousand lines of code. And it's up to you to challenge that. And only then will they be able to realize that they can actually cut it down to 100 lines or less. And so without this principle, your AI agent tends to overbuild. But with it, Claude is writing the minimum. And the reason by the way why this is so important is because you have to remember that these AI agents, they are mostly trained on production code bases. And so they default to production patterns, which is mostly large scale in nature. And so when you ask for a simple feature ad, it tends to overthink, it tends to overbuild. But what this claw.md file does is that it allows your agent to put simplicity first. So now for our second test, what I'll be doing is asking both of these agents to add a search bar that filters the tab list. So let's send that over and we'll see what the difference are between these two. And once those two are done again, the vanilla cloud code confirmed to me that the filter search bar is available. But if I refresh this local host 10,000, it wasn't really able to implement that, which in contrast to the Kurpatic claude code, you can see it was able to successfully add this filter which I wanted where if I just type in there, it will be able to find the specific tab that I want. And in fact, I was curious because the vanilla cloud code doesn't seem to be changing anything in the app that it's working on. But you can see here that it does know exactly the application on port 10,000, which is this one. But because it doesn't have the karpati skill, it tends to fall to the same agentic traps that this claw.md is hoping to address. And so for the kpati claw code, I just ask it how it implemented principle 2 in that build. You can see it made deliberate decisions around not having complex logic to track which separators are between visible tabs and also didn't add other items which I didn't ask for. And what's even better is that the amount of lines that it added is only 20 lines which is much more simple and lean versus what the vanilla claw code added which is more than 50% of that. So you can imagine for bigger code bases and bigger builds then having this principle does really help. The third principle is the ability to make surgical changes. And the key observation that you may have also seen these agents do is this piece by Andre where he said that they still sometimes change or remove comments in code that they don't like or don't sufficiently understand even if it is orthogonal or not related to the task at hand. And so without this rule Claude and your other agents tend to improve things that you didn't ask for. But with it Claude changes only what it is that you want. Now, what's interesting about this principle is that it is actually one of the sneakiest failure mode for agents because it does look helpful if when, let's say, your agent writes multiple lines of code, but it's sort of like productivity for productivity's sake. If you can do the job in two lines of code, then that not only simplifies your setup, but it also consumes less tokens for you. So now for this third principle, the test that I'll do is to have them both update the font from outfit to this font called enter. And then let's see what they will actually do. And so looking at those two sessions, you can see this one is still working because even though it confirmed to me that it actually changed the fonts, if you look at the dashboard here, it is still the same font as what we started with. And so this might be a common problem for you where when you're working with AI agents because it doesn't have those best practices in mind. You actually end up spending more tokens because the bills and the changes that you want reflected are not properly being updated. And so right now this session is basically just burning through my tokens in order to just assess why this particular issue is present. Meanwhile, if I go to this Karpati cloud code version, the one with the light mode, you can see that it was able to successfully change the font into this new one called enter. And again, that's just one command. It was able to find every instance of outfit and replace it within the codebase. And here you can see I just asked it how it implemented principal tree in that whole build. And you can see what it did here is to only apply surgical changes and not reformat or restructure any of the font family declarations. Not reorganizing the Google fonts URL and basically just leaving out and not touching anything that it shouldn't touch. Meanwhile, this vanilla cloud code is still working through its errors and is just spending tokens left and right. And the final principle that it implements for your cloud code is the ability to have goal-driven execution. And this now operates within the core concept you need to understand which is defining what done looks like. And just going back to the Karpati tweet, you can see he mentioned here that LLMs are exceptionally good at looping until they meet specific goals. And so instead of telling it what to do, just give it success criteria or a specific goal in mind and just leave it to explore. And that is how you can extract the most value from these AI agents. And he also mentions here that changing your approach from imperative, which is basically commanding agents on how to do things to declarative, which is you declaring what you want out of these agents, then you'll be able to get better results each time. And to illustrate this principle, you can see what I did here is to ask our agent to make a version of this skill trees view, which is a nice visual view here in rubric of each of our agents and what are the specific skills that they have access to would be. But here I just ask a version where the goal is for the user to be able to select an icon for each agent here. And so when it was done, you can see that when I click on each of these agents, you now have the ability to change the icons, which if I select, let's say, this one for the beta agent, it will update that icon cleanly in the UI as well. And you can see what I did for this prompt is to just give it a goal, right? So I just ask it to think of a way for the user to be able to select an icon for each agent. I didn't really specify which part of the user interface here should the icons live in. And I also didn't specify how many icon options it should provide or what are the designs. Now you can obviously be more imperative or prescriptive to your agent on where each icon should live. But I think if you have this claw MD and there is that goal-driven mindset for your agent, then if you provide a clear end in mind and a definition of done, then it'll be able to work through pretty much the best course of action for that build that you're giving it. And there you go. All the principles that Andre Karpati himself uses to improve his cla code setup now publicly available through this repo. I hope that was useful and if it is then consider subscribing because that helps us a lot to put out more educational content like this. And if you want to learn how to automatically build slides with cloud code just like the one I showed in this video then you can watch this video next. I'll see you guys next time. Thank you.

---

## Timestamped Segments

**[0:00]** What if one file can fix the biggest

**[0:01]** problems that every cloud code user

**[0:03]** deals with? Well, Andre Carpathy listed

**[0:05]** down the top mistakes that every AI

**[0:07]** agent makes, and this single claw.md

**[0:10]** file just codified the fixes for those

**[0:12]** mistakes. And almost 43,000 people

**[0:14]** installed it just in the past week. In

**[0:17]** this video, I'll break down what this

**[0:18]** magical claw.md does, how it improves

**[0:21]** your AI agent setup so that you too can

**[0:23]** use Claude as good as how Karpati does

**[0:25]** it. And if you're new here, my name is

**[0:26]** Jay. I spent over a decade working with

**[0:27]** brands you probably know. Have been in

**[0:29]** AI since my masters in data science and

**[0:31]** now I run our AI solutions practice in

**[0:33]** one of the largest AI communities

**[0:34]** globally. Let's get started.

**[0:39]** So some time ago, Andre Karpati, who

**[0:41]** previously headed Tesla AI and also part

**[0:43]** of the founding team of OpenAI, made

**[0:45]** this now viral tweet where he provided a

**[0:47]** good analysis of how to work with agents

**[0:50]** better. It's actually a pretty detailed

**[0:51]** one and you can see here at the bottom

**[0:53]** that it already garnered 7 almost 8

**[0:55]** million views at this point. Now a lot

**[0:57]** of people took note of this tweet once

**[0:58]** again because over the past week what

**[1:00]** happened was this repo called Andre

**[1:02]** Karpati skills just shot up in

**[1:04]** popularity over at GitHub now at over

**[1:06]** 43,000 stars and it was made and

**[1:08]** published by this developer Forest. So

**[1:10]** credit where it's due. And if you go to

**[1:12]** this skill, what it is is basically a

**[1:14]** single claw.md file to improve claude

**[1:16]** code behavior which is derived from the

**[1:18]** observations from that tweet. And I

**[1:20]** think the reason why it became so

**[1:21]** popular and viral over the past week is

**[1:23]** simply because of how simple it is. It's

**[1:25]** one claw.md file that you just drop into

**[1:27]** your claw code. And also the solution

**[1:29]** that it provides here are boiled down to

**[1:31]** four key principles which I'll talk

**[1:32]** about in a bit. And I think regardless

**[1:34]** whether you want to use this claw.md

**[1:36]** file or not, learning about these

**[1:37]** principles will level up how you use

**[1:39]** your AI agents in order to make sure

**[1:41]** that you get the output that you want

**[1:42]** whenever you work with claude. But if

**[1:44]** you were looking to install this and try

**[1:45]** this out yourself, what you can simply

**[1:47]** do is to provide your Claude code with

**[1:48]** this GitHub link. But if you're already

**[1:50]** using clawed code, most likely you

**[1:51]** already have a claw.md file. In which

**[1:54]** case, it would be better for you to

**[1:55]** provide a more detailed prompt like this

**[1:57]** where you explain to your agent that

**[1:58]** you're giving it a set of guidelines

**[2:00]** called karpati skills and more

**[2:01]** importantly to suggest to you how you

**[2:03]** can best integrate it to your specific

**[2:05]** setup. So this more detailed

**[2:06]** installation prompt, I will link it down

**[2:07]** below if you need it. But as I

**[2:09]** mentioned, the core of this claw.md file

**[2:11]** are these four principles that I think

**[2:13]** are worth learning no matter what AI

**[2:14]** agent you use. So the first principle

**[2:16]** that it instills to your agent is that

**[2:18]** it allows claude code to think before

**[2:20]** coding. And just to refer back to what

**[2:21]** Andre wrote here, you can see he

**[2:22]** mentioned that the most common category

**[2:24]** of mistake that these agents make is

**[2:26]** that the models make wrong assumptions

**[2:28]** on your behalf and just run along with

**[2:29]** them without checking. They also don't

**[2:31]** manage their confusion. They don't see

**[2:32]** clarifications and they don't surface

**[2:35]** inconsistencies. And so the core idea

**[2:37]** for this principle is this. Without this

**[2:39]** rule, Claude assumes what you want. With

**[2:41]** it, Claude asks first. And so if you

**[2:43]** were to boil down one key principle that

**[2:45]** you should follow in order to upgrade

**[2:46]** how you should work with agents better,

**[2:48]** it is basically this. It is almost

**[2:50]** always better to have your agent ask you

**[2:52]** questions in order to clarify intent

**[2:54]** before it starts building and coding

**[2:56]** things for you. And so just to

**[2:57]** illustrate this, what I have here are

**[2:58]** two cloud code sessions. This one

**[3:00]** doesn't have the karpati claw.md and

**[3:02]** this one is where I loaded that claw MD

**[3:04]** we just talked about. And what I'm going

**[3:05]** to do is just give each of these agents

**[3:07]** a copy of this rubric application to

**[3:09]** illustrate the difference between the

**[3:10]** approaches of these agents with one of

**[3:12]** the agents not having this Kpati

**[3:14]** principle baked in and the other agent

**[3:16]** following the principle that we just

**[3:17]** talked about. So now just to show the

**[3:19]** difference between these two. If I send

**[3:20]** the same task to both of them where I'm

**[3:22]** simply requesting let's say to add a

**[3:23]** toggle for light mode to the rubric app.

**[3:25]** If we send it to both with this one to

**[3:27]** recap has that Karpati skill and claw.md

**[3:30]** already installed. And so now that both

**[3:31]** of those sessions are done, you can see

**[3:33]** this one without the carpatic claw. MD

**[3:35]** confirmed to me that there is a light

**[3:36]** mode toggle. But if I look at the

**[3:38]** application it's working on, it doesn't

**[3:40]** actually have it. And if you compare

**[3:41]** that with this session which was working

**[3:43]** on this localhost 10,01, this also

**[3:46]** confirmed to me that the toggle is in

**[3:47]** the top right bar next to search. And

**[3:49]** you can see that it is actually here.

**[3:51]** And it was able to implement that

**[3:52]** because it actually thought through the

**[3:54]** problem and even was able to decide what

**[3:56]** are the right colors across all of the

**[3:58]** other icons in here. which if you

**[4:00]** compare that to this one which was

**[4:01]** coming from the agent without that

**[4:03]** claw.md file, it thought that it was

**[4:05]** able to do the task but not really. And

**[4:07]** if you want to sort of peek under the

**[4:08]** hood on why the karpati claw.md is more

**[4:11]** proficient with what it just did. If you

**[4:13]** ask both to outline the steps that they

**[4:15]** just took, you can see the vanilla claw

**[4:17]** code, it did do some detailed steps like

**[4:19]** finding the right files, reading the CSS

**[4:21]** variables, and trying to add a light

**[4:23]** theme CSS. But if you just compare that

**[4:25]** with the outline of the steps of the

**[4:26]** Karpati claude code, you can see this is

**[4:29]** much more detailed versus what the

**[4:30]** vanilla claw code did. And so the result

**[4:32]** of that is that with just one prompt, it

**[4:34]** was able to oneshot this light theme for

**[4:36]** us without any issues. Now, real quick,

**[4:38]** we just released the Agentic AI

**[4:39]** masterass for our members at

**[4:41]** RoboNuggets, which takes you from zero

**[4:42]** to mastery when working with agents.

**[4:45]** There's a link to the community in the

**[4:46]** pinned comment below. We've got founders

**[4:47]** in there who landed their first client

**[4:49]** in weeks, live build sessions where we

**[4:50]** create this stuff together, and the

**[4:52]** actual templates behind what I showed in

**[4:53]** this video. The community is also the

**[4:55]** reason these lessons get made. So see

**[4:56]** that below if that's for you. The second

**[4:58]** principle that it implements is to put

**[5:00]** simplicity first. And just going back to

**[5:01]** what Andre wrote here, he mentioned that

**[5:03]** these AI agents by default will

**[5:05]** implement an inefficient, bloated, and

**[5:07]** brittle construction, which is sometimes

**[5:09]** over a thousand lines of code. And it's

**[5:10]** up to you to challenge that. And only

**[5:12]** then will they be able to realize that

**[5:14]** they can actually cut it down to 100

**[5:15]** lines or less. And so without this

**[5:17]** principle, your AI agent tends to

**[5:18]** overbuild. But with it, Claude is

**[5:20]** writing the minimum. And the reason by

**[5:22]** the way why this is so important is

**[5:23]** because you have to remember that these

**[5:25]** AI agents, they are mostly trained on

**[5:27]** production code bases. And so they

**[5:29]** default to production patterns, which is

**[5:31]** mostly large scale in nature. And so

**[5:33]** when you ask for a simple feature ad, it

**[5:35]** tends to overthink, it tends to

**[5:36]** overbuild. But what this claw.md file

**[5:38]** does is that it allows your agent to put

**[5:40]** simplicity first. So now for our second

**[5:42]** test, what I'll be doing is asking both

**[5:44]** of these agents to add a search bar that

**[5:46]** filters the tab list. So let's send that

**[5:48]** over and we'll see what the difference

**[5:50]** are between these two. And once those

**[5:52]** two are done again, the vanilla cloud

**[5:53]** code confirmed to me that the filter

**[5:55]** search bar is available. But if I

**[5:57]** refresh this local host 10,000, it

**[5:59]** wasn't really able to implement that,

**[6:00]** which in contrast to the Kurpatic claude

**[6:02]** code, you can see it was able to

**[6:04]** successfully add this filter which I

**[6:06]** wanted where if I just type in there, it

**[6:08]** will be able to find the specific tab

**[6:09]** that I want. And in fact, I was curious

**[6:11]** because the vanilla cloud code doesn't

**[6:13]** seem to be changing anything in the app

**[6:14]** that it's working on. But you can see

**[6:16]** here that it does know exactly the

**[6:18]** application on port 10,000, which is

**[6:20]** this one. But because it doesn't have

**[6:21]** the karpati skill, it tends to fall to

**[6:23]** the same agentic traps that this claw.md

**[6:25]** is hoping to address. And so for the

**[6:27]** kpati claw code, I just ask it how it

**[6:29]** implemented principle 2 in that build.

**[6:31]** You can see it made deliberate decisions

**[6:33]** around not having complex logic to track

**[6:35]** which separators are between visible

**[6:37]** tabs and also didn't add other items

**[6:40]** which I didn't ask for. And what's even

**[6:42]** better is that the amount of lines that

**[6:43]** it added is only 20 lines which is much

**[6:45]** more simple and lean versus what the

**[6:47]** vanilla claw code added which is more

**[6:49]** than 50% of that. So you can imagine for

**[6:52]** bigger code bases and bigger builds then

**[6:54]** having this principle does really help.

**[6:56]** The third principle is the ability to

**[6:58]** make surgical changes. And the key

**[7:00]** observation that you may have also seen

**[7:02]** these agents do is this piece by Andre

**[7:04]** where he said that they still sometimes

**[7:06]** change or remove comments in code that

**[7:07]** they don't like or don't sufficiently

**[7:09]** understand even if it is orthogonal or

**[7:12]** not related to the task at hand. And so

**[7:14]** without this rule Claude and your other

**[7:15]** agents tend to improve things that you

**[7:18]** didn't ask for. But with it Claude

**[7:19]** changes only what it is that you want.

**[7:21]** Now, what's interesting about this

**[7:22]** principle is that it is actually one of

**[7:24]** the sneakiest failure mode for agents

**[7:27]** because it does look helpful if when,

**[7:29]** let's say, your agent writes multiple

**[7:30]** lines of code, but it's sort of like

**[7:32]** productivity for productivity's sake. If

**[7:34]** you can do the job in two lines of code,

**[7:36]** then that not only simplifies your

**[7:38]** setup, but it also consumes less tokens

**[7:40]** for you. So now for this third

**[7:42]** principle, the test that I'll do is to

**[7:44]** have them both update the font from

**[7:46]** outfit to this font called enter. And

**[7:48]** then let's see what they will actually

**[7:50]** do. And so looking at those two

**[7:51]** sessions, you can see this one is still

**[7:53]** working because even though it confirmed

**[7:55]** to me that it actually changed the

**[7:56]** fonts, if you look at the dashboard

**[7:58]** here, it is still the same font as what

**[7:59]** we started with. And so this might be a

**[8:01]** common problem for you where when you're

**[8:03]** working with AI agents because it

**[8:05]** doesn't have those best practices in

**[8:06]** mind. You actually end up spending more

**[8:08]** tokens because the bills and the changes

**[8:10]** that you want reflected are not properly

**[8:12]** being updated. And so right now this

**[8:13]** session is basically just burning

**[8:15]** through my tokens in order to just

**[8:17]** assess why this particular issue is

**[8:19]** present. Meanwhile, if I go to this

**[8:20]** Karpati cloud code version, the one with

**[8:22]** the light mode, you can see that it was

**[8:24]** able to successfully change the font

**[8:26]** into this new one called enter. And

**[8:28]** again, that's just one command. It was

**[8:30]** able to find every instance of outfit

**[8:32]** and replace it within the codebase. And

**[8:34]** here you can see I just asked it how it

**[8:35]** implemented principal tree in that whole

**[8:37]** build. And you can see what it did here

**[8:38]** is to only apply surgical changes and

**[8:41]** not reformat or restructure any of the

**[8:43]** font family declarations. Not

**[8:45]** reorganizing the Google fonts URL and

**[8:47]** basically just leaving out and not

**[8:49]** touching anything that it shouldn't

**[8:50]** touch. Meanwhile, this vanilla cloud

**[8:52]** code is still working through its errors

**[8:54]** and is just spending tokens left and

**[8:56]** right. And the final principle that it

**[8:57]** implements for your cloud code is the

**[8:59]** ability to have goal-driven execution.

**[9:01]** And this now operates within the core

**[9:03]** concept you need to understand which is

**[9:04]** defining what done looks like. And just

**[9:06]** going back to the Karpati tweet, you can

**[9:08]** see he mentioned here that LLMs are

**[9:10]** exceptionally good at looping until they

**[9:12]** meet specific goals. And so instead of

**[9:14]** telling it what to do, just give it

**[9:15]** success criteria or a specific goal in

**[9:18]** mind and just leave it to explore. And

**[9:20]** that is how you can extract the most

**[9:21]** value from these AI agents. And he also

**[9:23]** mentions here that changing your

**[9:25]** approach from imperative, which is

**[9:26]** basically commanding agents on how to do

**[9:28]** things to declarative, which is you

**[9:30]** declaring what you want out of these

**[9:32]** agents, then you'll be able to get

**[9:34]** better results each time. And to

**[9:35]** illustrate this principle, you can see

**[9:37]** what I did here is to ask our agent to

**[9:39]** make a version of this skill trees view,

**[9:41]** which is a nice visual view here in

**[9:43]** rubric of each of our agents and what

**[9:45]** are the specific skills that they have

**[9:47]** access to would be. But here I just ask

**[9:48]** a version where the goal is for the user

**[9:51]** to be able to select an icon for each

**[9:53]** agent here. And so when it was done, you

**[9:56]** can see that when I click on each of

**[9:58]** these agents, you now have the ability

**[10:00]** to change the icons, which if I select,

**[10:02]** let's say, this one for the beta agent,

**[10:04]** it will update that icon cleanly in the

**[10:06]** UI as well. And you can see what I did

**[10:08]** for this prompt is to just give it a

**[10:10]** goal, right? So I just ask it to think

**[10:11]** of a way for the user to be able to

**[10:13]** select an icon for each agent. I didn't

**[10:15]** really specify which part of the user

**[10:17]** interface here should the icons live in.

**[10:19]** And I also didn't specify how many icon

**[10:22]** options it should provide or what are

**[10:23]** the designs. Now you can obviously be

**[10:25]** more imperative or prescriptive to your

**[10:27]** agent on where each icon should live.

**[10:29]** But I think if you have this claw MD and

**[10:31]** there is that goal-driven mindset for

**[10:33]** your agent, then if you provide a clear

**[10:36]** end in mind and a definition of done,

**[10:38]** then it'll be able to work through

**[10:39]** pretty much the best course of action

**[10:41]** for that build that you're giving it.

**[10:43]** And there you go. All the principles

**[10:44]** that Andre Karpati himself uses to

**[10:46]** improve his cla code setup now publicly

**[10:48]** available through this repo. I hope that

**[10:50]** was useful and if it is then consider

**[10:52]** subscribing because that helps us a lot

**[10:53]** to put out more educational content like

**[10:55]** this. And if you want to learn how to

**[10:56]** automatically build slides with cloud

**[10:58]** code just like the one I showed in this

**[10:59]** video then you can watch this video

**[11:01]** next. I'll see you guys next time. Thank

**[11:02]** you.
