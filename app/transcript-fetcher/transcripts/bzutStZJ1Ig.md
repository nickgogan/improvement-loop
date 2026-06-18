# Transcript: bzutStZJ1Ig

**URL:** https://www.youtube.com/watch?v=bzutStZJ1Ig
**Segments:** 410

---

## Full Text

We all know that CLCO here is able to take any app ideas and is able to generate it no problem. But do we really trust the code that Clo writes? Do we have the right automation testing? Do we have the right framework in place? Is it able to have a consistent output? And most importantly, what about security? And maybe the time that it takes for clawo here to fix the issue that it wrote, it take longer compared to just writing the code ourself. And a solution to this from the community is there are three popular framework that the community built. One is GSD which currently has 40,000 stars on GitHub and I actually made a video on my channel on how to use GSD and then there's also GStack which is built by Gary Tang who is the CEO of Y Combinator and then there's also the plug-in for superpowers which is a gentic skill framework that I made a video on on my channel as well and based on this chart you can see that there are three frameworks and you might be asking well are they trying to solve the same thing well the answer is no and all three frameworks here are trying to solve a particular problem in this process and that's why in this video I'm going to show you exactly what each of those framework does how are they different and most importantly how can be able to use that to improve accuracy for building applications using claw code. Now before we continue I recently launched our school community where I help you to master AI agents automations and so much more and that's all coming from someone who used to work as a senior AI software engineer at companies like Amazon and Microsoft and in this community you're going to get over 100 plus video materials like templates and workflows that I personally built and sold over 100 plus times. On top of that, you're also going to get access to our weekly live calls. And just to give you an idea, this week we're actually running a claw code master class where we're going to dive into how to improve Claw Co's accuracy when we're going to use it to building applications. Plus, you're also going to get full community support where you're going to get a chance to ask questions and get direct answers back. So, if you're ready to level up, make sure you jump right in and I'll see you in a community. Now, first we're going to take a look at it superpowers. Basically what essentially does here is that having clock here to follow a strict framework or a software development methodology here to complete a task step by step. So instead of having clock here to give it instructions maybe have it to you know code it randomly or maybe like not really consistent every single time we're going to have a basically like a framework. So it's going to first asking some clarification questions right try to clarify the intent and then it's going to confirm on exactly is this what you're trying to build right it's going to create a spec then it's going to create a plan on exactly how we're going to do this like the entire implementation plan and furthermore what's really unique about this framework here is that it's also following the test-driven approach which essentially what it does here is that it's going to first try to set the rules on exactly how the software here is going to behave right it's going to first try to create a test before it's going to try to write the code try to do the implement mentation. We're going to guarantee that agent here is going to write code because we already have the automation testing in place and then after the code is written and the test is passed then it's going to do some refactoring until we have nothing to refactor anymore right until the code here is more scalable and also the application here behave as what we expected in the tests and that's basically what superpowers here in a nutshell now if superpowers here is really trying to set up the agendic framework on how AI agent here do things GST here is trying to solve the context rod And basically what context raw means is that if you were to have a conversation with claw code maybe the first 20% is good right by the time when you get to like 40 60 80% and then the accuracy here start to drop dramatically and this is the same for any other large language models and what GSD believe in is that if we were to have the context window always stay below 50% we're going to get the best accuracy from large language model all the time and you can see here that it's going to break different phases here into different stages and for each stage here it's going to trigger different sub agents here to execute it. And the way how different stages here keep it consistent on which stage we're in, it uses the MD file to save in our local disk to keep track of the process. And basically, for example, if session one is complete, it's going to save the state here inside of the MD file in our local machine. And then for the next session after clock is going to spin up, it's going to read through the state that we put in our local disk and it's going to continue the task from there. And like I said, both of superpowers here and GST all uses sub agents for different stage. Like for example, the phase one here, phase one right here is all doing research. Yes, they're going to spin up different sub aents to do this. But the main difference here is that yes, super powers here has it own framework. But the problem here is that they have a mega orchestrator that doing everything. Like for example, this is phase one, this is phase two, this is phase three, phase four. They have different sub agents spinning it up for each phases. But the context for the orchestrator here never changed, right? Is we're using the same orchestrator throughout the entire conversation. But for difference for GSD here, yes, the GSD is using sub agents to do all different phases. But for each phase here, we are actually switching different orchestrators. So for phase one, we have orchestrator one. For phase 2, we have orchestrator 2, right? So after orchestrator 2 is done, it's going to save the states in our local disk. Then it's going to spin up the phase three sub agents here and also the orchestrator to do the task. So fresh starts after every phase memory are saved in a disk. And for superpowers here you can see it's just one conversation always awake. And here you can see this is another illustration here to prove it simply like I said super powers here we have brainstorm plan execution. We are all done using this one orchestrator. And this orchestrator here is going to spin up different sub agents here to complete this. But for GSD, we're going to have one orchestrator for phase one, one orchestrator for phase 2, one orchestrator for phase three. This way, the orchestrator here is always going to be under 50% for the context window. So you can see that both of them are trying to solve different problem. One is try to set the standards on exactly how AI agent here to do things, right? Brainstorm, plan, execute, and the other one is try to make sure that every agent here is staying under 50% for the context window, even including the orchestrator themsel. And lastly, we also have GStack. And what Gstack mission statement here is basically try to break the single agent here into different specialist role. Right? So instead of having one general agent do everything, we're going to break it down into different roles. For example, a CEO role, maybe a engineer role, designer role, or maybe also a release engineer role, right? There could be many roles by the time you watch this video. So for example whenever we come to the stage of planning or maybe we can be able to trigger the co lens here to review the things or whenever we try to do the building it's going to trigger the engineering manager right so it's going to go through this process here by different stages and for each stage here it's going to trigger a specialist agent and you'll be wondering well how is it different compared to the super power stages right super powers also has brainstorming writing plans all those kind of things the key difference here is that super powers is only act as a discipline engineer which basically means that it's like a tech lead following these software development methodologies but it doesn't switch to different lenses on like seeing different roles perspective like QA you know actually be able to open the browser here creating the test plan also it doesn't have the ability here to like plan as a CEO right so these are all different specialist agents that Gstack here is also operating differently compared to superpowers and lastly you may wondering well are they just role prompts that we just basically tell claude hey I want you to behave a certain way well the answer is it's actually not because there's actually five layers you can see here of mechanism on how it actually behave for each rows that we have seen here to making sure that each row here doesn't break characters and starting the first one here is the role focus and basically what it does here is that it's going to put on the blenders so whenever it's going to put on this role like for example QA lead is only going to focus on what QA have to focus on right for example the user flow the bug report testing checklist or what's the result look like right is going to look through that but it doesn't look through any other things that's not part of the responsibility for example the Post style data schema is other specialist agents job and this agent here is only focusing on his job responsibility and then the second layer here is data flow and basically the way how it works for these agents or these specialist agents here you can see is that their work is built on top of the previous stage for example let's say this is the reviewer agents reviewer agent here say okay looks good uh please help me to QA this work help me to test this then the QA lead here is going to take this response which is how the data is actually flowing going and then we also have quality control which is a checklist on exactly what everyone can see for example for CEO yes it has done the review engineer manager has done the review as well right so we have a checklist on exactly what roles has been processed based on a certain project we're currently doing and then the fourth layer here is basically boil the lake what it means here is that trying to finish what you can do perfectly and don't start do anything that you cannot do perfectly for example it's easier to boil a small lake because it's very small right you can be able to do this perfectly fine but if it's like outside of your responsibility if it's something that you cannot be able to do perfectly for example you cannot be able to boil ocean because it's huge right so if you cannot do it then don't do it right so what we want to do here is that we want to do something that you can be able to do 100% and so so you can see here that's exactly what we're trying to set in the layer four and the layer five here is really just trying to keep things simple like instead of having so many things for at you it's going to take it slow down and try to summarize everything like it's going to boil down into these three things like here's what I found why it matters and what to do next. It's going to give you a direct answer to explain to you like a 16 years old. And that's it. And lastly, just to conclude everything for all three frameworks, you can see that for superpowers here is helping you to constrain the process. Making sure that AI agent here is following the testdriven development framework here. Making sure that we set the expectation before we're going to do the execution. GSD here is making sure that we constrain the environment. Making sure that every session that we have here is below 50% for the context window. So that we ensure AI agent here is able to output with you know high accuracy right and the GStack here is basically constrained with perspective means that we're going to focusing on different lenses right having different persona different specialists reviewing different stages of the development process rather than just having one generous agent that does everything. So then you asking well every framework here is trying to solve a particular problem. Is it possible if we can be able to combine them all into a power stack and the answer here is yes we can definitely do that. You can see here we can combine the power of GStack which is really good at you know exact team GSD here is really good at project manager. superpowers here is really good as being a senior engineer right so what we can do here is that for planning for strategy planning like let's say we want to have a big idea or vague idea Gstack here has different persona it's going to help you to like for example these different skills here like CEO engineer manager here is going to help you to craft a overall architecture is this project idea valid right it's going to help you to refine that project idea a bit more and then when it comes to taking that project idea or taking that project plan into a execution solution like how we can be able to break it down into different task or different milestones is really good at using GST because GSD here is really thinking about context protection making sure that AI agent here is going to be stay under 50% for the context window and they're going to do this by calculating the projects and breaking that project into different milestones so that each milestone here can be done under you know 50% for using just one orchestrator agent and then finally when it comes to execution superpower here is going to be really good because it follow the testdriven developments. So what we can do here is that we can trigger those skills and be able to implement those features by forcing AI here to write the test before it does the coding work. And finally we can have GStack here to do the QA polishing work to making sure that it's able to use play right here to actually click using the UI here to test it. So eventually here you can see that's exactly how each room works and what we can do here is that we can be able to piece them together into our overall development workflows. For example, Gstack is really good at planning QA, maybe other frameworks is not really good at that, we can use that for that particular job. If it's like project management, like breaking the entire project into different milestones, then we're going to do it with GSD. And making sure that each milestone here is going to take less than 50% of context when the superpower agent here is going to do it, right? And then when we trigger the superpower agent, we're going to have that agent here is focusing on just writing code, making sure that we follow the strict testing, having parallel sub agents here going to run at the same time. And that's exactly how we can do this. We can be able to take the best of all three frameworks to making sure that everything is accurate and stable and also consistent throughout the entire development process. So with that being said, if you do this video, please make sure to like this video and be sure to check out this playlist right here on all the spectrum development frameworks that I have talked about in this channel. And of course, if you do find out in this video, please make sure to like this video, consider subscribing more content like this. But with that being said, I'll see you in the next video.

---

## Timestamped Segments

**[0:00]** We all know that CLCO here is able to

**[0:01]** take any app ideas and is able to

**[0:03]** generate it no problem. But do we really

**[0:05]** trust the code that Clo writes? Do we

**[0:08]** have the right automation testing? Do we

**[0:10]** have the right framework in place? Is it

**[0:12]** able to have a consistent output? And

**[0:14]** most importantly, what about security?

**[0:16]** And maybe the time that it takes for

**[0:17]** clawo here to fix the issue that it

**[0:19]** wrote, it take longer compared to just

**[0:21]** writing the code ourself. And a solution

**[0:23]** to this from the community is there are

**[0:25]** three popular framework that the

**[0:27]** community built. One is GSD which

**[0:29]** currently has 40,000 stars on GitHub and

**[0:31]** I actually made a video on my channel on

**[0:33]** how to use GSD and then there's also

**[0:35]** GStack which is built by Gary Tang who

**[0:37]** is the CEO of Y Combinator and then

**[0:40]** there's also the plug-in for superpowers

**[0:42]** which is a gentic skill framework that I

**[0:43]** made a video on on my channel as well

**[0:45]** and based on this chart you can see that

**[0:46]** there are three frameworks and you might

**[0:48]** be asking well are they trying to solve

**[0:49]** the same thing well the answer is no and

**[0:51]** all three frameworks here are trying to

**[0:53]** solve a particular problem in this

**[0:54]** process and that's why in this video I'm

**[0:56]** going to show you exactly what each of

**[0:57]** those framework does how are they

**[0:58]** different and most importantly how can

**[1:00]** be able to use that to improve accuracy

**[1:02]** for building applications using claw

**[1:03]** code. Now before we continue I recently

**[1:05]** launched our school community where I

**[1:07]** help you to master AI agents automations

**[1:09]** and so much more and that's all coming

**[1:11]** from someone who used to work as a

**[1:13]** senior AI software engineer at companies

**[1:15]** like Amazon and Microsoft and in this

**[1:17]** community you're going to get over 100

**[1:19]** plus video materials like templates and

**[1:21]** workflows that I personally built and

**[1:23]** sold over 100 plus times. On top of

**[1:25]** that, you're also going to get access to

**[1:26]** our weekly live calls. And just to give

**[1:28]** you an idea, this week we're actually

**[1:30]** running a claw code master class where

**[1:31]** we're going to dive into how to improve

**[1:33]** Claw Co's accuracy when we're going to

**[1:35]** use it to building applications. Plus,

**[1:37]** you're also going to get full community

**[1:38]** support where you're going to get a

**[1:39]** chance to ask questions and get direct

**[1:41]** answers back. So, if you're ready to

**[1:42]** level up, make sure you jump right in

**[1:44]** and I'll see you in a community. Now,

**[1:46]** first we're going to take a look at it

**[1:47]** superpowers. Basically what essentially

**[1:48]** does here is that having clock here to

**[1:50]** follow a strict framework or a software

**[1:52]** development methodology here to complete

**[1:54]** a task step by step. So instead of

**[1:56]** having clock here to give it

**[1:58]** instructions maybe have it to you know

**[1:59]** code it randomly or maybe like not

**[2:01]** really consistent every single time

**[2:03]** we're going to have a basically like a

**[2:05]** framework. So it's going to first asking

**[2:07]** some clarification questions right try

**[2:09]** to clarify the intent and then it's

**[2:11]** going to confirm on exactly is this what

**[2:13]** you're trying to build right it's going

**[2:14]** to create a spec then it's going to

**[2:16]** create a plan on exactly how we're going

**[2:17]** to do this like the entire

**[2:18]** implementation plan and furthermore

**[2:20]** what's really unique about this

**[2:21]** framework here is that it's also

**[2:23]** following the test-driven approach which

**[2:25]** essentially what it does here is that

**[2:26]** it's going to first try to set the rules

**[2:27]** on exactly how the software here is

**[2:30]** going to behave right it's going to

**[2:31]** first try to create a test before it's

**[2:33]** going to try to write the code try to do

**[2:35]** the implement mentation. We're going to

**[2:36]** guarantee that agent here is going to

**[2:38]** write code because we already have the

**[2:40]** automation testing in place and then

**[2:42]** after the code is written and the test

**[2:44]** is passed then it's going to do some

**[2:45]** refactoring until we have nothing to

**[2:48]** refactor anymore right until the code

**[2:49]** here is more scalable and also the

**[2:51]** application here behave as what we

**[2:53]** expected in the tests and that's

**[2:55]** basically what superpowers here in a

**[2:56]** nutshell now if superpowers here is

**[2:58]** really trying to set up the agendic

**[2:59]** framework on how AI agent here do things

**[3:02]** GST here is trying to solve the context

**[3:04]** rod And basically what context raw means

**[3:06]** is that if you were to have a

**[3:08]** conversation with claw code maybe the

**[3:10]** first 20% is good right by the time when

**[3:12]** you get to like 40 60 80% and then the

**[3:15]** accuracy here start to drop dramatically

**[3:17]** and this is the same for any other large

**[3:18]** language models and what GSD believe in

**[3:20]** is that if we were to have the context

**[3:22]** window always stay below 50% we're going

**[3:25]** to get the best accuracy from large

**[3:27]** language model all the time and you can

**[3:29]** see here that it's going to break

**[3:30]** different phases here into different

**[3:31]** stages and for each stage here it's

**[3:34]** going to trigger different sub agents

**[3:35]** here to execute it. And the way how

**[3:37]** different stages here keep it consistent

**[3:39]** on which stage we're in, it uses the MD

**[3:42]** file to save in our local disk to keep

**[3:44]** track of the process. And basically, for

**[3:46]** example, if session one is complete,

**[3:48]** it's going to save the state here inside

**[3:49]** of the MD file in our local machine. And

**[3:51]** then for the next session after clock is

**[3:53]** going to spin up, it's going to read

**[3:54]** through the state that we put in our

**[3:56]** local disk and it's going to continue

**[3:58]** the task from there. And like I said,

**[4:00]** both of superpowers here and GST all

**[4:02]** uses sub agents for different stage.

**[4:04]** Like for example, the phase one here,

**[4:06]** phase one right here is all doing

**[4:08]** research. Yes, they're going to spin up

**[4:10]** different sub aents to do this. But the

**[4:12]** main difference here is that yes, super

**[4:14]** powers here has it own framework. But

**[4:15]** the problem here is that they have a

**[4:17]** mega orchestrator that doing everything.

**[4:19]** Like for example, this is phase one,

**[4:21]** this is phase two, this is phase three,

**[4:23]** phase four. They have different sub

**[4:25]** agents spinning it up for each phases.

**[4:27]** But the context for the orchestrator

**[4:29]** here never changed, right? Is we're

**[4:31]** using the same orchestrator throughout

**[4:33]** the entire conversation. But for

**[4:35]** difference for GSD here, yes, the GSD is

**[4:38]** using sub agents to do all different

**[4:40]** phases. But for each phase here, we are

**[4:42]** actually switching different

**[4:43]** orchestrators. So for phase one, we have

**[4:45]** orchestrator one. For phase 2, we have

**[4:47]** orchestrator 2, right? So after

**[4:49]** orchestrator 2 is done, it's going to

**[4:51]** save the states in our local disk. Then

**[4:53]** it's going to spin up the phase three

**[4:55]** sub agents here and also the

**[4:56]** orchestrator to do the task. So fresh

**[4:58]** starts after every phase memory are

**[5:01]** saved in a disk. And for superpowers

**[5:03]** here you can see it's just one

**[5:04]** conversation always awake. And here you

**[5:06]** can see this is another illustration

**[5:08]** here to prove it simply like I said

**[5:10]** super powers here we have brainstorm

**[5:11]** plan execution. We are all done using

**[5:14]** this one orchestrator. And this

**[5:16]** orchestrator here is going to spin up

**[5:17]** different sub agents here to complete

**[5:18]** this. But for GSD, we're going to have

**[5:21]** one orchestrator for phase one, one

**[5:23]** orchestrator for phase 2, one

**[5:24]** orchestrator for phase three. This way,

**[5:26]** the orchestrator here is always going to

**[5:28]** be under 50% for the context window. So

**[5:31]** you can see that both of them are trying

**[5:32]** to solve different problem. One is try

**[5:34]** to set the standards on exactly how AI

**[5:36]** agent here to do things, right?

**[5:37]** Brainstorm, plan, execute, and the other

**[5:40]** one is try to make sure that every agent

**[5:42]** here is staying under 50% for the

**[5:44]** context window, even including the

**[5:46]** orchestrator themsel. And lastly, we

**[5:48]** also have GStack. And what Gstack

**[5:50]** mission statement here is basically try

**[5:51]** to break the single agent here into

**[5:53]** different specialist role. Right? So

**[5:55]** instead of having one general agent do

**[5:57]** everything, we're going to break it down

**[5:58]** into different roles. For example, a CEO

**[6:00]** role, maybe a engineer role, designer

**[6:03]** role, or maybe also a release engineer

**[6:05]** role, right? There could be many roles

**[6:06]** by the time you watch this video. So for

**[6:08]** example whenever we come to the stage of

**[6:10]** planning or maybe we can be able to

**[6:11]** trigger the co lens here to review the

**[6:13]** things or whenever we try to do the

**[6:15]** building it's going to trigger the

**[6:16]** engineering manager right so it's going

**[6:18]** to go through this process here by

**[6:20]** different stages and for each stage here

**[6:21]** it's going to trigger a specialist agent

**[6:24]** and you'll be wondering well how is it

**[6:25]** different compared to the super power

**[6:26]** stages right super powers also has

**[6:28]** brainstorming writing plans all those

**[6:30]** kind of things the key difference here

**[6:32]** is that super powers is only act as a

**[6:34]** discipline engineer which basically

**[6:36]** means that it's like a tech lead

**[6:37]** following these software development

**[6:39]** methodologies but it doesn't switch to

**[6:40]** different lenses on like seeing

**[6:42]** different roles perspective like QA you

**[6:44]** know actually be able to open the

**[6:46]** browser here creating the test plan also

**[6:47]** it doesn't have the ability here to like

**[6:49]** plan as a CEO right so these are all

**[6:51]** different specialist agents that Gstack

**[6:53]** here is also operating differently

**[6:54]** compared to superpowers and lastly you

**[6:56]** may wondering well are they just role

**[6:58]** prompts that we just basically tell

**[6:59]** claude hey I want you to behave a

**[7:01]** certain way well the answer is it's

**[7:02]** actually not because there's actually

**[7:04]** five layers you can see here of

**[7:07]** mechanism on how it actually behave for

**[7:09]** each rows that we have seen here to

**[7:10]** making sure that each row here doesn't

**[7:12]** break characters and starting the first

**[7:14]** one here is the role focus and basically

**[7:16]** what it does here is that it's going to

**[7:17]** put on the blenders so whenever it's

**[7:19]** going to put on this role like for

**[7:20]** example QA lead is only going to focus

**[7:23]** on what QA have to focus on right for

**[7:25]** example the user flow the bug report

**[7:28]** testing checklist or what's the result

**[7:29]** look like right is going to look through

**[7:31]** that but it doesn't look through any

**[7:33]** other things that's not part of the

**[7:35]** responsibility for example the Post

**[7:37]** style data schema is other specialist

**[7:39]** agents job and this agent here is only

**[7:41]** focusing on his job responsibility and

**[7:44]** then the second layer here is data flow

**[7:46]** and basically the way how it works for

**[7:48]** these agents or these specialist agents

**[7:50]** here you can see is that their work is

**[7:52]** built on top of the previous stage for

**[7:54]** example let's say this is the reviewer

**[7:56]** agents reviewer agent here say okay

**[7:58]** looks good uh please help me to QA this

**[8:01]** work help me to test this then the QA

**[8:03]** lead here is going to take this response

**[8:05]** which is how the data is actually

**[8:06]** flowing going and then we also have

**[8:08]** quality control which is a checklist on

**[8:10]** exactly what everyone can see for

**[8:11]** example for CEO yes it has done the

**[8:14]** review engineer manager has done the

**[8:16]** review as well right so we have a

**[8:17]** checklist on exactly what roles has been

**[8:20]** processed based on a certain project

**[8:22]** we're currently doing and then the

**[8:23]** fourth layer here is basically boil the

**[8:25]** lake what it means here is that trying

**[8:27]** to finish what you can do perfectly and

**[8:29]** don't start do anything that you cannot

**[8:31]** do perfectly for example it's easier to

**[8:33]** boil a small lake because it's very

**[8:35]** small right you can be able to do this

**[8:36]** perfectly fine but if it's like outside

**[8:38]** of your responsibility if it's something

**[8:40]** that you cannot be able to do perfectly

**[8:41]** for example you cannot be able to boil

**[8:42]** ocean because it's huge right so if you

**[8:44]** cannot do it then don't do it right so

**[8:46]** what we want to do here is that we want

**[8:47]** to do something that you can be able to

**[8:48]** do 100% and so so you can see here

**[8:50]** that's exactly what we're trying to set

**[8:52]** in the layer four and the layer five

**[8:53]** here is really just trying to keep

**[8:55]** things simple like instead of having so

**[8:57]** many things for at you it's going to

**[8:59]** take it slow down and try to summarize

**[9:01]** everything like it's going to boil down

**[9:02]** into these three things like here's what

**[9:04]** I found why it matters and what to do

**[9:06]** next. It's going to give you a direct

**[9:08]** answer to explain to you like a 16 years

**[9:10]** old. And that's it. And lastly, just to

**[9:12]** conclude everything for all three

**[9:14]** frameworks, you can see that for

**[9:15]** superpowers here is helping you to

**[9:17]** constrain the process. Making sure that

**[9:19]** AI agent here is following the

**[9:20]** testdriven development framework here.

**[9:22]** Making sure that we set the expectation

**[9:23]** before we're going to do the execution.

**[9:25]** GSD here is making sure that we

**[9:26]** constrain the environment. Making sure

**[9:28]** that every session that we have here is

**[9:29]** below 50% for the context window. So

**[9:31]** that we ensure AI agent here is able to

**[9:34]** output with you know high accuracy right

**[9:36]** and the GStack here is basically

**[9:37]** constrained with perspective means that

**[9:39]** we're going to focusing on different

**[9:41]** lenses right having different persona

**[9:44]** different specialists reviewing

**[9:46]** different stages of the development

**[9:47]** process rather than just having one

**[9:49]** generous agent that does everything. So

**[9:51]** then you asking well every framework

**[9:53]** here is trying to solve a particular

**[9:54]** problem. Is it possible if we can be

**[9:56]** able to combine them all into a power

**[9:58]** stack and the answer here is yes we can

**[10:00]** definitely do that. You can see here we

**[10:02]** can combine the power of GStack which is

**[10:04]** really good at you know exact team GSD

**[10:07]** here is really good at project manager.

**[10:09]** superpowers here is really good as being

**[10:11]** a senior engineer right so what we can

**[10:13]** do here is that for planning for

**[10:14]** strategy planning like let's say we want

**[10:16]** to have a big idea or vague idea Gstack

**[10:19]** here has different persona it's going to

**[10:21]** help you to like for example these

**[10:23]** different skills here like CEO engineer

**[10:25]** manager here is going to help you to

**[10:27]** craft a overall architecture is this

**[10:29]** project idea valid right it's going to

**[10:31]** help you to refine that project idea a

**[10:33]** bit more and then when it comes to

**[10:34]** taking that project idea or taking that

**[10:36]** project plan into a execution solution

**[10:39]** like how we can be able to break it down

**[10:40]** into different task or different

**[10:42]** milestones is really good at using GST

**[10:45]** because GSD here is really thinking

**[10:46]** about context protection making sure

**[10:48]** that AI agent here is going to be stay

**[10:50]** under 50% for the context window and

**[10:52]** they're going to do this by calculating

**[10:54]** the projects and breaking that project

**[10:57]** into different milestones so that each

**[10:59]** milestone here can be done under you

**[11:01]** know 50% for using just one orchestrator

**[11:04]** agent and then finally when it comes to

**[11:06]** execution superpower here is going to be

**[11:08]** really good because it follow the

**[11:10]** testdriven developments. So what we can

**[11:11]** do here is that we can trigger those

**[11:12]** skills and be able to implement those

**[11:14]** features by forcing AI here to write the

**[11:16]** test before it does the coding work. And

**[11:19]** finally we can have GStack here to do

**[11:20]** the QA polishing work to making sure

**[11:22]** that it's able to use play right here to

**[11:24]** actually click using the UI here to test

**[11:27]** it. So eventually here you can see

**[11:28]** that's exactly how each room works and

**[11:30]** what we can do here is that we can be

**[11:31]** able to piece them together into our

**[11:33]** overall development workflows. For

**[11:34]** example, Gstack is really good at

**[11:36]** planning QA, maybe other frameworks is

**[11:38]** not really good at that, we can use that

**[11:40]** for that particular job. If it's like

**[11:42]** project management, like breaking the

**[11:44]** entire project into different

**[11:45]** milestones, then we're going to do it

**[11:46]** with GSD. And making sure that each

**[11:48]** milestone here is going to take less

**[11:50]** than 50% of context when the superpower

**[11:52]** agent here is going to do it, right? And

**[11:54]** then when we trigger the superpower

**[11:55]** agent, we're going to have that agent

**[11:57]** here is focusing on just writing code,

**[11:59]** making sure that we follow the strict

**[12:01]** testing, having parallel sub agents here

**[12:03]** going to run at the same time. And

**[12:04]** that's exactly how we can do this. We

**[12:06]** can be able to take the best of all

**[12:07]** three frameworks to making sure that

**[12:09]** everything is accurate and stable and

**[12:11]** also consistent throughout the entire

**[12:13]** development process. So with that being

**[12:14]** said, if you do this video, please make

**[12:16]** sure to like this video and be sure to

**[12:18]** check out this playlist right here on

**[12:19]** all the spectrum development frameworks

**[12:21]** that I have talked about in this

**[12:22]** channel. And of course, if you do find

**[12:24]** out in this video, please make sure to

**[12:25]** like this video, consider subscribing

**[12:27]** more content like this. But with that

**[12:28]** being said, I'll see you in the next

**[12:30]** video.
