# Transcript: I Built a Deck With AI, Then Made a Second AI Attack It.

**URL:** https://www.youtube.com/watch?v=MFzxIT88zfg
**Segments:** 559
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 19:29
**Uploaded:** 2026-05-27

---

## Full Text

So, finally, this is the Excel spreadsheet conversation. Finally, we get to talk about what all of these agents have made a difference for when it comes to work and office files because everything still lives in Word. It lives in Excel. It lives in PowerPoint. And when I did all of my prompting guides and everything like that last year, they were hugely popular around Excel and PowerPoint. You can still find them. They're still useful for building individual assets, but we have moved past individual asset territory with what models can do now. It just isn't the same thing. I I'm not kidding you. I can now draft eight simultaneous documents at once. I don't think that's the ceiling. That's just what I happened to do this week. And I did it by focusing on the structure of the data around the document so that what I got was high high quality and very powerful. You want to think beyond that. You want to think in terms of how you build an entire infrastructure around agents that drives successful artifact creation, whether that's Excel or PowerPoint or something else. And that mindset parallels a lot of what we're seeing in the rest of the workforce as we wrestle with what it means to have agents in production in 2026. Because the real, you know, n-dimensional move, the big brain move right now is not to think of it as I bolt this onto my workflow, but to think of it as agents are at the heart of the new workflow. I therefore need to torque myself around, change my process, adjust everything inside so that agents are centralized and agents are first. And so a lot of what I'm going to talk about is essentially how you rebuild an office document workflow agentically. And that's the theme. That's what makes this really exciting because if you do that, that's when you get to these massive increases because if you think about it, eight documents, 10 documents, whatever it is, you're talking about an order of magnitude increase in productivity on just knowledge work. That's huge. And I don't see that happening. In fact, I know that's not happening because I have talked to folks at Hyperscalers about what I'm doing and they're like, "Oh, wow. That's actually really cool. We didn't know that these models could do that." Well, they can. And we're going to show you how. Claude can build Excel and PowerPoint files. Chat GPT analyzes any spreadsheet you drop into it. So does Codeex. Microsoft Copilot for Office hit general availability in April. Everybody watching this video has access to AI that can build a PowerPoint deck in minutes. What you don't have is a way to know that the deck is correct, accurate, and complete. A and I know this because I've lived it. Last quarter, I opened an Excel file that looked like a financial model. Assumption inputs at the top, revenue projections, valuation outputs rolling up very cleanly. There was a written guide attached saying the model had been validated. And then I opened the revenue growth row and the formula was incorrect and it was copied across every future year from the same two cells year after year. Excel didn't tell me that. There was no ref error. The valuation output still looked good, but it was a financial model in a costume. It wasn't the real thing. The the layout was right. The labels were right. The cells were incorrect. And that's obviously the only thing that matters. And the same thing is happening in a lot of docs that I see time after time in real production environments. And in this video, I want to fix that for you. I want to get into how we build workflows for agents with agents at the center that help us to build these heavy knowledge work documents in ways that ensure reliability and accuracy. The key fix is a mental shift. A prompt asks for an output. A workflow defines the stages the output has to pass through before it can be trusted. And you need to be in a workflow world, not a prompt world. So for Office files, that workflow has four stages. And we're going to go through all four. One, you have to prepare your sources. You do not ask for the deck or the spreadsheet. You ask for an inventory of what the model has to work with, and you make sure that it's organized. Two, structure. Before any slide or formula gets created, AI needs to produce a file specification. For a deck, that's a narrative spine and a slide list with claim headlines. For a workbook, it should have a tab architecture and a calculation flow. You want to go from producing that spec to then building the artifact. Right now, you build the artifact constrained by the source packet of information, constrained by the spec that you've built. You're not freestyling from whatever the model thinks the answer should be. And then four, verification. The file isn't done when it opens. It's done when it has survived a reviewer that looks at it really aggressively. I use another model for this. I actually use codeex to build office artifacts and then I use claude opus 4.7 to review them aggressively and generate edit loops. And it's like my own Ralph loop, right? Where like it finishes and opus looks at it and says, "Oh, you're not finished. Here's your edit loop to make it better." And I just keep running that until I get a very high quality set of docs. And I can run it at scale if my document source repositories are clear. I I'm increasingly thinking of knowledge work as if it was code. So the capability to generate these files is absolutely everywhere and it's far outpacing our ability to scale quality unless we have these kinds of systems like I'm talking about. I wrote about the upstream piece of this on Substack earlier this month about how to organize your sources before you ever ask AI to write anything. It's critical for this kind of work to actually scale and call that the before, right? This video is the after, how you build with it. Uh, so that link to the previous Substack is in the description. If you're interested, feel free to dive in. I think it's a nice pair with this video. Let's get back to it. The failures I worry about aren't dramatic. They're ordinary enough to survive a quick review. Right? A board deck pulled from a folder containing a Q3 actuals export and a Q4 plan file. The slide headline says, "Revenue is ahead of plan." and the chart looks really clean and then you look at the underlying numbers and they're blending actuals and plan data because nobody labeled the difference and that error travels every time the deck gets shared. It traveled out of the spreadsheet or wherever it came from originally and it's a problem. So you are now in a world where you can have a great PowerPoint with sharp headlines and executive language but there's no way to show that it has a foundation. It may look finished but it has no foundation. And I want to talk to you about how you build documents reliably in a pipeline that are wellounded because that's how you actually start to build momentum with this knowledge work. Otherwise, all of this AI tooling becomes a massive trust breaker. And I want to be clear, I'm not cherrypicking edge cases here. Models are goaloriented. If you tell them to build something on a bad foundation, they'll try to do it. And that's the normal result of asking AI to jump straight from messy sources to a finished file. the model is optimizing for the artifact you asked for. And if you ask for a deck and don't give it choices, it'll try to make a deck. Same thing with a spreadsheet. Unless you explicitly define the evidence structure, the tool treats source discipline as optional. And that's backwards. Source discipline is a big part of the work. And I want to call out this is not because the models are getting worse. In fact, the models have had a lot of work put into them to care about sources. And if you give them the chance to, they will. Part of why we have to have this conversation now is that the models are trained to check claims and look at sources. And if you don't take the same care as the models do, the models will try to take that care, try to look at sources. And that very goalorientedness to build completely will betray you because you have no clean sources for it to rely on. It will just have to work its way through and guess, but it's been trained to try and find it. So, it will try and do that and it will guess and then you'll be in trouble. And so we have to be aware of where the hyperscalers are taking the models. And the hyperscalers are basically saying models need to do better work by checking sources. They're right, but we have to do the work of making sure the sources and the workflow pipelines are there so the models can build these office documents appropriately. And that's what serious knowledge work looks like in 2026. The goal is to make every important claim and calculation something that can be checked and that invites that scrutiny. And so you have two stages here, right? You have source prep. That's stage one. Before you ask AI for the deck or the workbook, you need to ask AI to look at what it can see. What's in the folder? Find out what your work packet has. Does does everything in the work packet have an owner and a date and a file type? And can you create an index of evidence that has all of that? Does it have a status? Has the AI said if it's current data or superseded? If it's an estimate, if it's a transcript, if it's raw data, have you removed sensitive material that would need to be removed before any public-f facing artifact gets generated? That does happen, too. Uh, have you checked your facts and your estimates based on research on the net? This one move changes the process. A messy folder can become a controlled work packet. The AI can't blend a transcript and a deck and a spreadsheet and a half-remembered assumption into a confident answer if you've organized everything and if there's an index of what's in there. Stage two is structure. Before any file gets created, you need to produce a file specification. At least if you're doing serious work. I'm not saying every single time you have a conversation with Jet GPT. Don't don't misunderstand me. I'm saying when you're doing serious knowledge work that has implications. So for PowerPoint, that's the narrative in English in a way that you understand. And do insist on plain English. One of the issues with the current models is they like cute language. They like shortorthhand. Insist on plain English. Who is the audience? What decision do they need to make? What do they need to believe before they can make that decision? And then look at the list of slides. What are the claims? What are the supporting source IDs? Where are charts needed? What are the assumptions? What are the open questions? And for Excel, you need to look at your tab architecture. Where does raw data live in the tab? Where do the assumptions live? Where are calculations performed? Where are checks recorded? Where does the user see the summary and how is it driven? So the file spec is like a blueprint for a serious doc. If the blueprint doesn't explain where the truth lives, the finished file won't do that either. So, if you're wondering how to get started, there is a full source packet template on the Substack, including an ID schema, a status taxonomy, a conflict log format. If you want to copy it for your team for the next big project you do, I've linked it in the description. Let's move on here, though. I want to talk about file creation. This is the part we all want, right? How can we create this stuff? So only now does AI actually build the artifact. After you prep for PowerPoint, I would do it in two passes. First pass is the storyboard. You want slide titles and claims and evidence and notes. Don't design render yet. No charts laid out, just the argument and the evidence trail. Second pass, render the deck. This split keeps visual polish from hiding a weak argument. And you catch unsupported claims before they become beautiful and difficult to edit. Right now I am doing all of the argumentation in codec and I'm moving to claude opus 4.7 for the render of the deck because that front-end polish is just beautiful and claude for Excel do it in three layers. Layer one load the raw data exactly. Layer two build the assumptions in the calculation logic and layer three produce the output views. A workbook should be able to answer a very simple question. If I change an assumption, does the relevant output change for the right reason? And that question matters a lot more than whether the workbook itself looks good. A spreadsheet that cannot recalculate isn't a model. A model whose formulas can't be inspected isn't ready for decisioning. Right now, what I am doing is I am using codeex to build Excel models and then I am having Claude take a pass at making them pretty afterward. But I find that codeex is really really good at completeness in Excel files and that's really important when you're trying to build serious models. One more piece I want to call out here. You need to understand your task risk gradient. Where is AI highest risk or lowest risk? AI is lowest risk for formatting, layout exploration, chart drafts, summary wording and consistency checks. It's medium risk for source attribution and data extraction. And it's highest risk for numerical synthesis, for financial calculations, for any kind of regulatory language or compliance language, and for claims that will travel up to senior leadership for a decision. Make sure you check those. So yes, let the model help her everywhere. No matter what the task risk gradient is, it's faster with the model. Now, don't give every task the same review burden depending on the risk. If you want to understand how to dig into that further, there's more on that in the substack. I broke down the full file specification format. There's a PowerPoint narrative spine template. There's an Excel tab architecture. There's assumption log fields. And there are sort of checks, tab, smoke alarms you can set in Excel that I put together. So, if you want the full version both for PowerPoint and Excel, the link is in the description. We're going to move on though to one of the things I think is most important, and that's verification with a hostile reviewer prompt. So verification asks whether the artifact can be trusted. Sources, dates, formulas, assumptions, charts, and unsupported claims. Every one of these gets inspected. It's a different job from proofreading, and most teams tend to skip it because the file can look done much sooner than it's actually done. The useful pattern is to make the model itself act as a hostile reviewer. You you can use the same model. I use different models for this. I like to play them off against each other. So, I use Opus 4.7 to review what 5.5 does. I think that's super fun. Uh, and I'm going to give you the prompt right here. So, you know, pay attention. So, the prompt is this. Read this Decker workbook as a skeptical reviewer who suspects every claim and every number. For each slider sheet, identify claims without source attribution, numbers without a data source, charts whose underlying data isn't traceable, formulas inconsistent across parallel rows or columns, and assumptions presented as facts. Produce a written list of every issue found. Don't fix anything, just enumerate. That last instruction, don't fix, just enumerate, is what makes it work. The model is just trying to find the problems. It's not trying to solve them. different task, different output, different value. A model can catch a lot of its own mistakes when you flip the task from generation to enumeration. And the human gate can stay on the consequential claims, the numbers that travel, the calls that are going to become an important decision. And and one of the things I want to call out here is my personal workflow is very much a Ralph loop for this. I will take a doc that is created by codeex and I will give it to opus 4.7 and I will ask opus 4.7 to do that hostile review and generate an extremely detailed edit list. I will pipe that back to codeex and I will ask codeex to fix everything in there with a new version in the same folder. Then I will go back to the same thread in open 4.7 and say check the work. Did they do the job? And then I will do it again and I will do it again. And toward the end, I will actually introduce a language check. Opus is actually very very good at checking for LLM isms like you're absolutely right in the doc, right? Something like that. And you can get it into plain English that actually works better for humans to read if you introduce that polish step later. And the overall goal is that you have an autonomous loop between codeex and opus that gets you to Alevel work without having to invest a ton of time along the way so that your time is best focused on reading A-level material and saying, "Okay, this is where I agree. This is where I disagree. This is where I would edit. Here's some final polish." And that's what it looks like to do heavy knowledge work in 2026. If we step back, AI has made it much easier to create Office files, right? And that matters a lot. PowerPoint and Excel are still where an enormous amount of business judgment becomes visible inside companies. And traditionally, they have taken real hours out of everyone's week in millions and millions of cases. If AI helps people build those artifacts faster, the productivity upside is real. It's measured in weeks a year for all of us. The upgrade is that you can now build a repeatable production system around the file. Source prep and structure and constrained creation and verification. The file is just an output of that knowledge works system. It's not the whole thing. Drag in the sources, ask for a deck, hope the output is right, that's the version of the workflow that loses you a meeting. Instead, if you prepare your sources and define your structure and create the file carefully and verify it, you're going to be trusted more and more. So, the next deck you build with AI should not start with a deck. It should start with the moves that I described. Right? Write out a narrative spine before you open the AI tool. Drop in your source materials and ask for a source inventory. Ask for a conflict log before you try and make any slides. Generate the storyboard with claims and notes before any visual rendering. And then run a hostile reviewer prompt before you decide to share it out. The model can help everywhere, but you have to keep owning the truth. This is the your polish stopped meaning trust. The companies that build a truth layer around their AI office files are going to ship a lot faster and be wrong much less. The ones that don't are going to put out a really nice looking deck next quarter with a number that nobody can defend. And by the way, if you think that's not true, I want you to remember that the team at OpenAI did that with a chart that chat GPT presumably helped make in the chat GPT5 launch. And the chart was famously wrong and everyone had a good chuckle and that happens to the best of us. We can do better than that. I want to answer one question to close us off and I think I I I think a number of you will ask this and it's simple. Nate, why is it this hard? I have to build this entire effectively knowledge work harness on my own. Why do I have to do that? Why hasn't someone made this for me so it's easier and it's just push a button simple? I have a really clear answer for you. Knowledge work is profoundly contingent on domain knowledge. That's why it's knowledge work. If you are going to do knowledge work that is specific and memorable and useful and deep, you have to be deep enough in theformational context that you can custom assemble the pieces of information you need to make a useful artifact. It's not something you can generically turn into a workflow. It's not that simple. It's not like you can assume there are five slots for evidence for a PowerPoint deck and good luck if you have more than five. No one who does serious knowledge work thinks like that. And so I think part of the reason we have to build our own, it's sort of like Luke Skywalker making his own lightsaber. You have to understand how the system works to become a master at that system. And I am sure that there are startups out there that are working on making parts of this simpler, parts of gathering the information simpler, parts of communicating that review step simpler, parts of checking the work and checking sort of the calculations on Excel simpler. All of those pieces are problems that we can get better at solving. But I don't want to lose sight of the fact that good deep knowledge work is tremendously detailed. reality has a surprising amount of detail. Good deep knowledge work is extremely detailed and it's difficult to generalize an abstraction like an abstracted knowledge work harness over that level of detail. So that's the honest answer for you. That's why we can't just get a push button answer from Microsoft that makes Excel superpowered for this. There you go. I if wishes were fishes, right? I wish it was that way. But instead, we get to work at this. And by the way, for everyone saying we'll lose our brains when we use AI, this is a great example of why you got to keep your brain turned on when you use AI.

---

## Timestamped Segments

**[0:00]** So, finally, this is the Excel

**[0:02]** spreadsheet conversation. Finally, we

**[0:04]** get to talk about what all of these

**[0:06]** agents have made a difference for when

**[0:08]** it comes to work and office files

**[0:10]** because everything still lives in Word.

**[0:12]** It lives in Excel. It lives in

**[0:13]** PowerPoint. And when I did all of my

**[0:16]** prompting guides and everything like

**[0:17]** that last year, they were hugely popular

**[0:19]** around Excel and PowerPoint. You can

**[0:21]** still find them. They're still useful

**[0:22]** for building individual assets, but we

**[0:25]** have moved past individual asset

**[0:27]** territory with what models can do now.

**[0:30]** It just isn't the same thing. I I'm not

**[0:32]** kidding you. I can now draft eight

**[0:34]** simultaneous documents at once. I don't

**[0:36]** think that's the ceiling. That's just

**[0:37]** what I happened to do this week. And I

**[0:39]** did it by focusing on the structure of

**[0:42]** the data around the document so that

**[0:44]** what I got was high high quality and

**[0:46]** very powerful. You want to think beyond

**[0:48]** that. You want to think in terms of how

**[0:50]** you build an entire infrastructure

**[0:53]** around agents that drives successful

**[0:56]** artifact creation, whether that's Excel

**[0:58]** or PowerPoint or something else. And

**[1:00]** that mindset parallels a lot of what

**[1:03]** we're seeing in the rest of the

**[1:06]** workforce as we wrestle with what it

**[1:08]** means to have agents in production in

**[1:10]** 2026. Because the real, you know,

**[1:13]** n-dimensional move, the big brain move

**[1:15]** right now is not to think of it as I

**[1:17]** bolt this onto my workflow, but to think

**[1:19]** of it as agents are at the heart of the

**[1:22]** new workflow. I therefore need to torque

**[1:24]** myself around, change my process, adjust

**[1:26]** everything inside so that agents are

**[1:28]** centralized and agents are first. And so

**[1:29]** a lot of what I'm going to talk about is

**[1:31]** essentially how you rebuild an office

**[1:34]** document workflow agentically. And

**[1:36]** that's the theme. That's what makes this

**[1:37]** really exciting because if you do that,

**[1:39]** that's when you get to these massive

**[1:41]** increases because if you think about it,

**[1:43]** eight documents, 10 documents, whatever

**[1:44]** it is, you're talking about an order of

**[1:45]** magnitude increase in productivity on

**[1:48]** just knowledge work. That's huge. And I

**[1:50]** don't see that happening. In fact, I

**[1:52]** know that's not happening because I have

**[1:53]** talked to folks at Hyperscalers about

**[1:55]** what I'm doing and they're like, "Oh,

**[1:56]** wow. That's actually really cool. We

**[1:57]** didn't know that these models could do

**[1:59]** that." Well, they can. And we're going

**[2:01]** to show you how. Claude can build Excel

**[2:03]** and PowerPoint files. Chat GPT analyzes

**[2:06]** any spreadsheet you drop into it. So

**[2:07]** does Codeex. Microsoft Copilot for

**[2:09]** Office hit general availability in

**[2:11]** April. Everybody watching this video has

**[2:13]** access to AI that can build a PowerPoint

**[2:16]** deck in minutes. What you don't have is

**[2:19]** a way to know that the deck is correct,

**[2:21]** accurate, and complete. A and I know

**[2:23]** this because I've lived it. Last

**[2:25]** quarter, I opened an Excel file that

**[2:26]** looked like a financial model.

**[2:28]** Assumption inputs at the top, revenue

**[2:29]** projections, valuation outputs rolling

**[2:31]** up very cleanly. There was a written

**[2:33]** guide attached saying the model had been

**[2:35]** validated. And then I opened the revenue

**[2:37]** growth row and the formula was incorrect

**[2:39]** and it was copied across every future

**[2:41]** year from the same two cells year after

**[2:43]** year. Excel didn't tell me that. There

**[2:45]** was no ref error. The valuation output

**[2:47]** still looked good, but it was a

**[2:49]** financial model in a costume. It wasn't

**[2:52]** the real thing. The the layout was

**[2:54]** right. The labels were right. The cells

**[2:55]** were incorrect. And that's obviously the

**[2:57]** only thing that matters. And the same

**[2:59]** thing is happening in a lot of docs that

**[3:01]** I see time after time in real production

**[3:05]** environments. And in this video, I want

**[3:08]** to fix that for you. I want to get into

**[3:10]** how we build workflows for agents with

**[3:12]** agents at the center that help us to

**[3:15]** build these heavy knowledge work

**[3:17]** documents in ways that ensure

**[3:18]** reliability and accuracy. The key fix is

**[3:21]** a mental shift. A prompt asks for an

**[3:24]** output. A workflow defines the stages

**[3:26]** the output has to pass through before it

**[3:28]** can be trusted. And you need to be in a

**[3:30]** workflow world, not a prompt world. So

**[3:32]** for Office files, that workflow has four

**[3:35]** stages. And we're going to go through

**[3:37]** all four. One, you have to prepare your

**[3:39]** sources. You do not ask for the deck or

**[3:42]** the spreadsheet. You ask for an

**[3:43]** inventory of what the model has to work

**[3:46]** with, and you make sure that it's

**[3:47]** organized. Two, structure. Before any

**[3:51]** slide or formula gets created, AI needs

**[3:53]** to produce a file specification. For a

**[3:56]** deck, that's a narrative spine and a

**[3:58]** slide list with claim headlines. For a

**[4:00]** workbook, it should have a tab

**[4:02]** architecture and a calculation flow. You

**[4:04]** want to go from producing that spec to

**[4:06]** then building the artifact. Right now,

**[4:08]** you build the artifact constrained by

**[4:10]** the source packet of information,

**[4:12]** constrained by the spec that you've

**[4:14]** built. You're not freestyling from

**[4:16]** whatever the model thinks the answer

**[4:18]** should be. And then four, verification.

**[4:21]** The file isn't done when it opens. It's

**[4:24]** done when it has survived a reviewer

**[4:26]** that looks at it really aggressively. I

**[4:28]** use another model for this. I actually

**[4:29]** use codeex to build office artifacts and

**[4:32]** then I use claude opus 4.7 to review

**[4:35]** them aggressively and generate edit

**[4:36]** loops. And it's like my own Ralph loop,

**[4:38]** right? Where like it finishes and opus

**[4:40]** looks at it and says, "Oh, you're not

**[4:41]** finished. Here's your edit loop to make

**[4:43]** it better." And I just keep running that

**[4:45]** until I get a very high quality set of

**[4:47]** docs. And I can run it at scale if my

**[4:50]** document source repositories are clear.

**[4:52]** I I'm increasingly thinking of knowledge

**[4:54]** work as if it was code. So the

**[4:56]** capability to generate these files is

**[4:58]** absolutely everywhere and it's far

**[5:00]** outpacing our ability to scale quality

**[5:02]** unless we have these kinds of systems

**[5:04]** like I'm talking about. I wrote about

**[5:05]** the upstream piece of this on Substack

**[5:07]** earlier this month about how to organize

**[5:09]** your sources before you ever ask AI to

**[5:11]** write anything. It's critical for this

**[5:12]** kind of work to actually scale and call

**[5:14]** that the before, right? This video is

**[5:17]** the after, how you build with it. Uh, so

**[5:19]** that link to the previous Substack is in

**[5:21]** the description. If you're interested,

**[5:22]** feel free to dive in. I think it's a

**[5:24]** nice pair with this video. Let's get

**[5:26]** back to it. The failures I worry about

**[5:28]** aren't dramatic. They're ordinary enough

**[5:30]** to survive a quick review. Right? A

**[5:32]** board deck pulled from a folder

**[5:34]** containing a Q3 actuals export and a Q4

**[5:36]** plan file. The slide headline says,

**[5:38]** "Revenue is ahead of plan." and the

**[5:41]** chart looks really clean and then you

**[5:43]** look at the underlying numbers and

**[5:45]** they're blending actuals and plan data

**[5:47]** because nobody labeled the difference

**[5:49]** and that error travels every time the

**[5:51]** deck gets shared. It traveled out of the

**[5:52]** spreadsheet or wherever it came from

**[5:54]** originally and it's a problem. So you

**[5:56]** are now in a world where you can have a

**[5:58]** great PowerPoint with sharp headlines

**[6:00]** and executive language but there's no

**[6:02]** way to show that it has a foundation. It

**[6:05]** may look finished but it has no

**[6:07]** foundation. And I want to talk to you

**[6:09]** about how you build documents reliably

**[6:12]** in a pipeline that are wellounded

**[6:13]** because that's how you actually start to

**[6:15]** build momentum with this knowledge work.

**[6:17]** Otherwise, all of this AI tooling

**[6:19]** becomes a massive trust breaker. And I

**[6:22]** want to be clear, I'm not cherrypicking

**[6:23]** edge cases here. Models are

**[6:25]** goaloriented. If you tell them to build

**[6:27]** something on a bad foundation, they'll

**[6:30]** try to do it. And that's the normal

**[6:32]** result of asking AI to jump straight

**[6:34]** from messy sources to a finished file.

**[6:36]** the model is optimizing for the artifact

**[6:39]** you asked for. And if you ask for a deck

**[6:41]** and don't give it choices, it'll try to

**[6:42]** make a deck. Same thing with a

**[6:44]** spreadsheet. Unless you explicitly

**[6:46]** define the evidence structure, the tool

**[6:48]** treats source discipline as optional.

**[6:50]** And that's backwards. Source discipline

**[6:52]** is a big part of the work. And I want to

**[6:54]** call out this is not because the models

**[6:57]** are getting worse. In fact, the models

**[6:59]** have had a lot of work put into them to

**[7:01]** care about sources. And if you give them

**[7:03]** the chance to, they will. Part of why we

**[7:06]** have to have this conversation now is

**[7:08]** that the models are trained to check

**[7:10]** claims and look at sources. And if you

**[7:11]** don't take the same care as the models

**[7:13]** do, the models will try to take that

**[7:15]** care, try to look at sources. And that

**[7:18]** very goalorientedness to build

**[7:21]** completely will betray you because you

**[7:24]** have no clean sources for it to rely on.

**[7:26]** It will just have to work its way

**[7:27]** through and guess, but it's been trained

**[7:29]** to try and find it. So, it will try and

**[7:31]** do that and it will guess and then

**[7:33]** you'll be in trouble. And so we have to

**[7:35]** be aware of where the hyperscalers are

**[7:38]** taking the models. And the hyperscalers

**[7:40]** are basically saying models need to do

**[7:42]** better work by checking sources. They're

**[7:43]** right, but we have to do the work of

**[7:45]** making sure the sources and the workflow

**[7:47]** pipelines are there so the models can

**[7:49]** build these office documents

**[7:50]** appropriately. And that's what serious

**[7:52]** knowledge work looks like in 2026. The

**[7:54]** goal is to make every important claim

**[7:57]** and calculation something that can be

**[7:59]** checked and that invites that scrutiny.

**[8:01]** And so you have two stages here, right?

**[8:03]** You have source prep. That's stage one.

**[8:06]** Before you ask AI for the deck or the

**[8:08]** workbook, you need to ask AI to look at

**[8:10]** what it can see. What's in the folder?

**[8:12]** Find out what your work packet has. Does

**[8:14]** does everything in the work packet have

**[8:16]** an owner and a date and a file type? And

**[8:19]** can you create an index of evidence that

**[8:21]** has all of that? Does it have a status?

**[8:23]** Has the AI said if it's current data or

**[8:25]** superseded? If it's an estimate, if it's

**[8:27]** a transcript, if it's raw data, have you

**[8:30]** removed sensitive material that would

**[8:31]** need to be removed before any public-f

**[8:33]** facing artifact gets generated? That

**[8:35]** does happen, too. Uh, have you checked

**[8:37]** your facts and your estimates based on

**[8:39]** research on the net? This one move

**[8:42]** changes the process. A messy folder can

**[8:44]** become a controlled work packet. The AI

**[8:46]** can't blend a transcript and a deck and

**[8:48]** a spreadsheet and a half-remembered

**[8:49]** assumption into a confident answer if

**[8:51]** you've organized everything and if

**[8:53]** there's an index of what's in there.

**[8:55]** Stage two is structure. Before any file

**[8:57]** gets created, you need to produce a file

**[9:00]** specification. At least if you're doing

**[9:02]** serious work. I'm not saying every

**[9:03]** single time you have a conversation with

**[9:04]** Jet GPT. Don't don't misunderstand me.

**[9:06]** I'm saying when you're doing serious

**[9:07]** knowledge work that has implications. So

**[9:09]** for PowerPoint, that's the narrative in

**[9:11]** English in a way that you understand.

**[9:13]** And do insist on plain English. One of

**[9:15]** the issues with the current models is

**[9:16]** they like cute language. They like

**[9:18]** shortorthhand. Insist on plain English.

**[9:20]** Who is the audience? What decision do

**[9:21]** they need to make? What do they need to

**[9:23]** believe before they can make that

**[9:24]** decision? And then look at the list of

**[9:27]** slides. What are the claims? What are

**[9:29]** the supporting source IDs? Where are

**[9:30]** charts needed? What are the assumptions?

**[9:32]** What are the open questions? And for

**[9:34]** Excel, you need to look at your tab

**[9:35]** architecture. Where does raw data live

**[9:37]** in the tab? Where do the assumptions

**[9:38]** live? Where are calculations performed?

**[9:41]** Where are checks recorded? Where does

**[9:42]** the user see the summary and how is it

**[9:44]** driven? So the file spec is like a

**[9:46]** blueprint for a serious doc. If the

**[9:48]** blueprint doesn't explain where the

**[9:51]** truth lives, the finished file won't do

**[9:53]** that either. So, if you're wondering how

**[9:55]** to get started, there is a full source

**[9:56]** packet template on the Substack,

**[9:59]** including an ID schema, a status

**[10:00]** taxonomy, a conflict log format. If you

**[10:03]** want to copy it for your team for the

**[10:04]** next big project you do, I've linked it

**[10:07]** in the description. Let's move on here,

**[10:09]** though. I want to talk about file

**[10:10]** creation. This is the part we all want,

**[10:12]** right? How can we create this stuff? So

**[10:15]** only now does AI actually build the

**[10:17]** artifact. After you prep for PowerPoint,

**[10:20]** I would do it in two passes. First pass

**[10:22]** is the storyboard. You want slide titles

**[10:24]** and claims and evidence and notes. Don't

**[10:27]** design render yet. No charts laid out,

**[10:29]** just the argument and the evidence

**[10:31]** trail. Second pass, render the deck.

**[10:34]** This split keeps visual polish from

**[10:36]** hiding a weak argument. And you catch

**[10:38]** unsupported claims before they become

**[10:40]** beautiful and difficult to edit. Right

**[10:42]** now I am doing all of the argumentation

**[10:45]** in codec and I'm moving to claude opus

**[10:47]** 4.7 for the render of the deck because

**[10:49]** that front-end polish is just beautiful

**[10:51]** and claude for Excel do it in three

**[10:53]** layers. Layer one load the raw data

**[10:56]** exactly. Layer two build the assumptions

**[10:58]** in the calculation logic and layer three

**[11:01]** produce the output views. A workbook

**[11:03]** should be able to answer a very simple

**[11:05]** question. If I change an assumption,

**[11:07]** does the relevant output change for the

**[11:09]** right reason? And that question matters

**[11:11]** a lot more than whether the workbook

**[11:12]** itself looks good. A spreadsheet that

**[11:14]** cannot recalculate isn't a model. A

**[11:17]** model whose formulas can't be inspected

**[11:19]** isn't ready for decisioning. Right now,

**[11:21]** what I am doing is I am using codeex to

**[11:24]** build Excel models and then I am having

**[11:27]** Claude take a pass at making them pretty

**[11:29]** afterward. But I find that codeex is

**[11:31]** really really good at completeness in

**[11:33]** Excel files and that's really important

**[11:35]** when you're trying to build serious

**[11:36]** models. One more piece I want to call

**[11:38]** out here. You need to understand your

**[11:40]** task risk gradient. Where is AI highest

**[11:43]** risk or lowest risk? AI is lowest risk

**[11:45]** for formatting, layout exploration,

**[11:47]** chart drafts, summary wording and

**[11:49]** consistency checks. It's medium risk for

**[11:51]** source attribution and data extraction.

**[11:54]** And it's highest risk for numerical

**[11:56]** synthesis, for financial calculations,

**[11:58]** for any kind of regulatory language or

**[12:00]** compliance language, and for claims that

**[12:02]** will travel up to senior leadership for

**[12:04]** a decision. Make sure you check those.

**[12:07]** So yes, let the model help her

**[12:09]** everywhere. No matter what the task risk

**[12:10]** gradient is, it's faster with the model.

**[12:12]** Now, don't give every task the same

**[12:14]** review burden depending on the risk. If

**[12:16]** you want to understand how to dig into

**[12:18]** that further, there's more on that in

**[12:19]** the substack. I broke down the full file

**[12:21]** specification format. There's a

**[12:23]** PowerPoint narrative spine template.

**[12:25]** There's an Excel tab architecture.

**[12:27]** There's assumption log fields. And there

**[12:29]** are sort of checks, tab, smoke alarms

**[12:31]** you can set in Excel that I put

**[12:32]** together. So, if you want the full

**[12:34]** version both for PowerPoint and Excel,

**[12:36]** the link is in the description. We're

**[12:38]** going to move on though to one of the

**[12:39]** things I think is most important, and

**[12:41]** that's verification with a hostile

**[12:43]** reviewer prompt. So verification asks

**[12:46]** whether the artifact can be trusted.

**[12:48]** Sources, dates, formulas, assumptions,

**[12:50]** charts, and unsupported claims. Every

**[12:53]** one of these gets inspected. It's a

**[12:54]** different job from proofreading, and

**[12:56]** most teams tend to skip it because the

**[12:58]** file can look done much sooner than it's

**[13:00]** actually done. The useful pattern is to

**[13:03]** make the model itself act as a hostile

**[13:05]** reviewer. You you can use the same

**[13:08]** model. I use different models for this.

**[13:09]** I like to play them off against each

**[13:11]** other. So, I use Opus 4.7 to review what

**[13:14]** 5.5 does. I think that's super fun. Uh,

**[13:16]** and I'm going to give you the prompt

**[13:18]** right here. So, you know, pay attention.

**[13:19]** So, the prompt is this. Read this Decker

**[13:22]** workbook as a skeptical reviewer who

**[13:24]** suspects every claim and every number.

**[13:26]** For each slider sheet, identify claims

**[13:29]** without source attribution, numbers

**[13:31]** without a data source, charts whose

**[13:33]** underlying data isn't traceable,

**[13:35]** formulas inconsistent across parallel

**[13:38]** rows or columns, and assumptions

**[13:40]** presented as facts. Produce a written

**[13:42]** list of every issue found. Don't fix

**[13:44]** anything, just enumerate. That last

**[13:47]** instruction, don't fix, just enumerate,

**[13:49]** is what makes it work. The model is just

**[13:51]** trying to find the problems. It's not

**[13:52]** trying to solve them. different task,

**[13:54]** different output, different value. A

**[13:56]** model can catch a lot of its own

**[13:58]** mistakes when you flip the task from

**[14:00]** generation to enumeration. And the human

**[14:02]** gate can stay on the consequential

**[14:04]** claims, the numbers that travel, the

**[14:06]** calls that are going to become an

**[14:07]** important decision. And and one of the

**[14:09]** things I want to call out here is my

**[14:10]** personal workflow is very much a Ralph

**[14:13]** loop for this. I will take a doc that is

**[14:16]** created by codeex and I will give it to

**[14:19]** opus 4.7 and I will ask opus 4.7 to do

**[14:22]** that hostile review and generate an

**[14:23]** extremely detailed edit list. I will

**[14:26]** pipe that back to codeex and I will ask

**[14:28]** codeex to fix everything in there with a

**[14:31]** new version in the same folder. Then I

**[14:34]** will go back to the same thread in open

**[14:36]** 4.7 and say check the work. Did they do

**[14:38]** the job? And then I will do it again and

**[14:40]** I will do it again. And toward the end,

**[14:42]** I will actually introduce a language

**[14:44]** check. Opus is actually very very good

**[14:46]** at checking for LLM isms like you're

**[14:49]** absolutely right in the doc, right?

**[14:51]** Something like that. And you can get it

**[14:53]** into plain English that actually works

**[14:55]** better for humans to read if you

**[14:56]** introduce that polish step later. And

**[14:58]** the overall goal is that you have an

**[15:00]** autonomous loop between codeex and opus

**[15:03]** that gets you to Alevel work without

**[15:06]** having to invest a ton of time along the

**[15:09]** way so that your time is best focused on

**[15:11]** reading A-level material and saying,

**[15:13]** "Okay, this is where I agree. This is

**[15:15]** where I disagree. This is where I would

**[15:17]** edit. Here's some final polish." And

**[15:19]** that's what it looks like to do heavy

**[15:21]** knowledge work in 2026. If we step back,

**[15:24]** AI has made it much easier to create

**[15:26]** Office files, right? And that matters a

**[15:28]** lot. PowerPoint and Excel are still

**[15:30]** where an enormous amount of business

**[15:31]** judgment becomes visible inside

**[15:33]** companies. And traditionally, they have

**[15:34]** taken real hours out of everyone's week

**[15:38]** in millions and millions of cases. If AI

**[15:40]** helps people build those artifacts

**[15:42]** faster, the productivity upside is real.

**[15:45]** It's measured in weeks a year for all of

**[15:47]** us. The upgrade is that you can now

**[15:49]** build a repeatable production system

**[15:51]** around the file. Source prep and

**[15:53]** structure and constrained creation and

**[15:55]** verification. The file is just an output

**[15:58]** of that knowledge works system. It's not

**[16:00]** the whole thing. Drag in the sources,

**[16:02]** ask for a deck, hope the output is

**[16:04]** right, that's the version of the

**[16:05]** workflow that loses you a meeting.

**[16:07]** Instead, if you prepare your sources and

**[16:09]** define your structure and create the

**[16:11]** file carefully and verify it, you're

**[16:12]** going to be trusted more and more. So,

**[16:15]** the next deck you build with AI should

**[16:16]** not start with a deck. It should start

**[16:18]** with the moves that I described. Right?

**[16:20]** Write out a narrative spine before you

**[16:22]** open the AI tool. Drop in your source

**[16:24]** materials and ask for a source

**[16:26]** inventory. Ask for a conflict log before

**[16:28]** you try and make any slides. Generate

**[16:30]** the storyboard with claims and notes

**[16:32]** before any visual rendering. And then

**[16:34]** run a hostile reviewer prompt before you

**[16:37]** decide to share it out. The model can

**[16:39]** help everywhere, but you have to keep

**[16:41]** owning the truth. This is the your

**[16:43]** polish stopped meaning trust. The

**[16:45]** companies that build a truth layer

**[16:46]** around their AI office files are going

**[16:48]** to ship a lot faster and be wrong much

**[16:51]** less. The ones that don't are going to

**[16:53]** put out a really nice looking deck next

**[16:55]** quarter with a number that nobody can

**[16:57]** defend. And by the way, if you think

**[16:58]** that's not true, I want you to remember

**[17:00]** that the team at OpenAI did that with a

**[17:04]** chart that chat GPT presumably helped

**[17:07]** make in the chat GPT5 launch. And the

**[17:11]** chart was famously wrong and everyone

**[17:12]** had a good chuckle and that happens to

**[17:15]** the best of us. We can do better than

**[17:17]** that. I want to answer one question to

**[17:20]** close us off and I think I I I think a

**[17:22]** number of you will ask this and it's

**[17:24]** simple. Nate, why is it this hard? I

**[17:28]** have to build this entire effectively

**[17:29]** knowledge work harness on my own. Why do

**[17:32]** I have to do that? Why hasn't someone

**[17:34]** made this for me so it's easier and it's

**[17:36]** just push a button simple? I have a

**[17:38]** really clear answer for you. Knowledge

**[17:40]** work is profoundly contingent on domain

**[17:44]** knowledge. That's why it's knowledge

**[17:45]** work. If you are going to do knowledge

**[17:48]** work that is specific and memorable and

**[17:51]** useful and deep, you have to be deep

**[17:54]** enough in theformational

**[17:56]** context that you can custom assemble the

**[17:59]** pieces of information you need to make a

**[18:02]** useful artifact. It's not something you

**[18:05]** can generically turn into a workflow.

**[18:08]** It's not that simple. It's not like you

**[18:10]** can assume there are five slots for

**[18:11]** evidence for a PowerPoint deck and good

**[18:13]** luck if you have more than five. No one

**[18:15]** who does serious knowledge work thinks

**[18:16]** like that. And so I think part of the

**[18:19]** reason we have to build our own, it's

**[18:21]** sort of like Luke Skywalker making his

**[18:23]** own lightsaber. You have to understand

**[18:25]** how the system works to become a master

**[18:27]** at that system. And I am sure that there

**[18:30]** are startups out there that are working

**[18:32]** on making parts of this simpler, parts

**[18:35]** of gathering the information simpler,

**[18:37]** parts of communicating that review step

**[18:40]** simpler, parts of checking the work and

**[18:42]** checking sort of the calculations on

**[18:44]** Excel simpler. All of those pieces are

**[18:47]** problems that we can get better at

**[18:49]** solving. But I don't want to lose sight

**[18:51]** of the fact that good deep knowledge

**[18:53]** work is tremendously detailed. reality

**[18:56]** has a surprising amount of detail. Good

**[18:58]** deep knowledge work is extremely

**[19:00]** detailed and it's difficult to

**[19:02]** generalize an abstraction like an

**[19:04]** abstracted knowledge work harness over

**[19:06]** that level of detail. So that's the

**[19:07]** honest answer for you. That's why we

**[19:10]** can't just get a push button answer from

**[19:12]** Microsoft that makes Excel superpowered

**[19:14]** for this. There you go. I if wishes were

**[19:17]** fishes, right? I wish it was that way.

**[19:18]** But instead, we get to work at this. And

**[19:21]** by the way, for everyone saying we'll

**[19:22]** lose our brains when we use AI, this is

**[19:24]** a great example of why you got to keep

**[19:25]** your brain turned on when you use AI.
