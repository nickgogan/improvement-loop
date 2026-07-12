# Transcript: Every AI Agent Demo Stops at Email. I Pointed Mine at the Bills That Cost You Money.

**URL:** https://www.youtube.com/watch?v=U4TmrlWEY4M
**Segments:** 447
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 15:44
**Uploaded:** 2026-07-03

---

## Full Text

Every AI agent demo that you've seen this year starts in the same place, email and calendar, or I feel like I've seen a ton of them. You draft the replies, you schedule the meetings, and and I get why, right? So many of us have this problem every single day. It's where we spend a lot of time, bad and Slack, but here's the trap that I see a lot of us fall into. We set up the agent, it kind of works, and we're kind of stuck from there because we don't know how to go from that level of work where you're just getting some of your day-to-day stuff triaged to real work like insurance, like like payments, like health care that takes a lot of delicacy, that takes real trust. So, today, we're going to solve that for you. I'm going to build one agent skeleton live. We're going to learn about it on email and calendar, where mistakes are cheap. And then I'm going to show you how I use the same agent machinery to actually build a real delicate work, highstakes agent that handles insurance and tax stuff. When you tackle agent problems, here's the frame I want you to use. That tax folder you haven't opened, uh maybe the insurance denial that you never appealed, uh those kinds of problems look like different problems to us because we organize them by domain, health versus taxes. But anytime you're dealing with files or paperwork, it's not a different problem. From an agent's perspective, it's the same thing. It requires an understanding of policy. It requires an understanding of category. It requires an understanding of detail. And you don't have good organization to get any of that out. In other words, it's a messtofile organization problem first and then you get structured insights out. That is a common pattern across a lot of our delicate high trust paperwork issues that bedevil our lives and cost us time after time. I see the same thing when I'm booking medical appointments, right? You see the same thing with education forms. Anytime that you have to take a bunch of stuff and turn it into structured context that you can use for a delicate operation, it's the same fundamental agent principle. Now, when we talk about agents, we almost always talk about action, right? the agent will do something. It will send an email or file something. And I get it, right? It looks really good, but when you're doing high trust work, I would encourage you and I would ask you to focus on the part that the agent actually lifts the weight on. Like I'm interested in agents that lift the load off. And and to me, an agent that can sort through bureaucracy with unstructured context with the mess in my folder. Uh that's more useful to me than an agent that can click a button. I can click the button. I need the agent to get everything ready so that clicking that button is really easy. And so the skeleton we're building today does nine things. And you're going to see every one of them on screen. So I'll just say them once. We're building a context pack. We're building injust. We're building chunking. We're building normalizing, storing, retrieving, citing, exporting, and gating. And yes, agents will help with all of it. That last one, the gate, is the rule from the top of this video. If the agent can read and organize and draft and site, that's great. but it's not allowed to submit or pay or sign. And I want to be clear, this is a job that we're giving the agent from the beginning. So, it has good guard rails. We're not giving the agent ever the option to take an unallowed step. And it's up to you as the human to keep that guardrail in place as you build and to ensure that you are actually testing this stuff and you are actually validating before you submit an insurance claim or a tax claim that it's on you as the human to submit it. It's not on the agent. So, here's how we're going to run this. We're going to have three builds all in this video. Same fundamental structure. What I'm trying to teach you is one structure that scales. We're going to start easy. We're going to start with your email and calendar, which is unstructured mess, but very low stakes. Then, I'm going to stop and I'm going to show you the bridge, the actual move that takes you from the calendared email world to the more advanced part. And it's something everybody skips. And then, we're going to get into insurance appeals and then taxes as some of our advanced use cases, our 2011 use cases, if you will. So, let's get started. All right, we're going to get into build one. And let's be honest, your inbox is probably a dumpster fire. Mine certainly was, too. And it's not because we're disorganized. I'm going to keep saying that. It's because email is effort that other people give to us. Everything lands there, not on our agenda. And it's so hard to structure it. Now, let's notice something before we start. This is not just the training wheels example. Your W2 is probably in that inbox somewhere. I know mine was. The denial letter from an insurance company may have arrived as a PDF attachment. You may have notes from your doctor leading to secure messages. The trusted work we're building toward is often email mediated. Here's a thread where someone's trying to schedule a meeting with me. The agent gets a context pack. That's the first skeleton idea that I talked about. And a context pack just defines what the agent is allowed to read. This thread, my calendar constraints, the people involved. And it has one goal. Prepare a reply with a proposed calendar hold. Notice the word prepare. Watch what it does. It ingests the thread. It pulls out the people, the date ranges, the time zone mismatch. Dates become dates. People become people. That's what normalization is called. And I know it sounds boring, but this boring stuff is what makes the agent do useful high trust work. I promise you it's worth it. So the agent checks my constraints. It drafts the reply and it builds the proposed calendar of Now watch this because this is the moment the whole video turns on. The draft is done and the next obvious thing would be to send it and and the agent stops and I want it to. It leaves the draft. It leaves the proposed hold and it leaves a receipt. What sources it used? What it changed? What still needs my approval? And if it's right, I'll just send it. If it's wrong, I can fix it. That receipt to me is critical. It's the difference between AI handled it and I know what happened here and I can trust the AI. It is so important to build for trust from day one. if you ever want your AI to do stuff that involves high value delicate work where real money is on the line where real value is coming back to you because like you we all know like if we appeal insurance and we win if if if we file taxes correctly and we get a refund that's real money on the lens thousands of dollars potentially if you wanted to help with that you got to get this trust piece right now let's pause for a second because this is a move almost everybody misses and it's the reason most people never get past that initial email simple 101 agent demo. You might think that going from a basic agent like an email agent to an insurance appeal means starting over. A new tool, a new setup, a new system that's higher trust. It doesn't if you build it right. Look at what you already own from build one. You own ingestion, turning documents into text the agent can use with anchors back to the source. You own normalization. You own dates becoming dates and people becoming people. You own the receipt. You own the gate. And those are primitives or building blocks. And none of them care whether you're in a scheduling thread or an insurance denial claim. It's the same thing to the agent. And that's why I keep calling this a flywheel. Every build we do, if we're doing it right, adds a skill to our shelf. And that makes the next build cheaper. So now, let's turn around again, and let's tackle a task that actually costs you money. First, I'm going to tell you what's real and what isn't here because I want you to actually know and trust this demo. The policy documents you're about to see are real. Insurers publish their plan documents. So, this system is querying an actual insurers's actual policy language. The patient for privacy is synthetic. The denial letter is built from the kind of denial letter that people post publicly, but every identifying detail has been masked. And this build works exactly the same on your real files and yours stay on your machine. Now, some new words to learn here in the context pack. We have denial letter. We have real policies and claim histories and supporting documents. And we have a new goal. I don't want a vibes-based appeal letter. I want a case file that I can inspect. So, this is more delicate work already than the email. All right, let's get to work. The agent starts by chunking. The denial letter is not one blob, right? It's got a date. It's got a denial reason. It's got a claim number, a deadline, and somewhere in there, there's a paragraph that says, "What evidence would change that decision?" And the policy is not one blob either. It has sections and definitions and exclusions and appeal rules. Everything is getting split into tagged and addressable pieces by the agent. Now we're normalizing. Like before, dates are becoming dates. Amounts are becoming amounts. And this one matters. Missing documents are becoming missing documents. That's especially important if you have a gap in your evidence because it can affect what you can act on and you won't get a surprise a few days before some kind of deadline. All of it is stored locally. You have a little database called SQLite and you have a folder and you can open the sources and the records yourself. Nothing leaves your machine. You never have to ask the model to remember what happened. When an insurer denies you, they're required to site the specific policy language they're relying on. Think about what that means. You're not searching for something you can't find. You already know the address of the thing that's hurting you. So, there's no vector database there, only a similarity search. The system simply has to retrieve by structure the denial reason, the exact policy section, the denial sites, the deadline, and the document checklist. And the first thing that the agent is going to do when it does all this is a sanity check. Does the section they cited actually say what the letter implies that it says? Sometimes it doesn't. And when it doesn't, that's finding number one. Now, look at what this produces. There's a timeline with a service date and claim date and denial date and an appeal deadline. There's actually a denial map. There's the exact policy language that governs all of this. There's an evidence checklist, what I have right now, what isn't there yet. And yes, there's a draft appeal letter, but the letter isn't the main thing. The whole evidence packet is what really matters here because the citation map means you can actually validate that what you're arguing is true. So, here's the reframe against conventional wisdom. The agent is not winning the appeal for you. It is turning the pile of unstructured information into a case file that makes you able to win. you were losing or you didn't win because you were showing up to a structured fight with an unstructured pile. This bill doesn't guarantee that you win. It just means you stopped showing up with bad data. Now, again, watch where the agent stops. The agent has drafted the appeal, the address, the claim number, the deadline, and the viral demo would be to say, "Okay, now we're going to send it." No, it stops. And I want to be very plain about this. You are responsible for what you send. I'm not advocating anybody fire one of these packets at an insurance company unread. The citations make your review faster. They don't make it optional because if an agent sends a bad appeal on its own, now you have two problems. The denial and the mess the agent made. This is the same skeleton as our email build. The nouns may have changed, but the underlying data, the underlying structure of how we solve this problem is exactly the same from the agents point of view. And that's how we build momentum. Okay. Build number three. I'm going to show you taxes. Everybody has to deal with taxes. And I want you to notice how fast this goes now because this is the flywheel doing what I promised at the top of the video. Again, we're going to say synthetic documents here. Tax folders are things nobody should see on YouTube. Uh, and we're going to tackle some new objects, right? So, you're going to see W2s and 1099s and invoices and receipts and bank exports and mileage notes. The works. And notice where half of this stuff was living. It was living in the inbox. That dumpster fire from build one is a source now for build three. Our new goal here is we're not filing. We are preparing a reviewable packet for you or your CPA. And if you're paying somebody hundreds of dollars or thousands of dollars to painfully comb through your pile of tax docs, understand what you're paying for. You're paying for the combing. This is the combing of the docks. It's the same skeleton we already built. It goes through the same order agent-wise. You're just ingesting. You chunk it into forms. You have income, expenses, unknowns. You normalize into a tax year ledger with date and vendor and amount and category and source file. And again, we have guard rails. The citation guard won't let a deduction float through without evidence. If the agent says it's a business expense, it's going to point at the receipt or it's going to flag the line instead of pretending it knows. The export you get is a packet, not a completed 1040 return. You get an income summary, an expense ledger, a deduction evidence map, and missing docs where you have them, plus a list of questions for the CPA. And that last one is underrated. A good agent doesn't just give you answers. A good agent gives you better questions to ask an expert. And look at that. It doesn't submit. It doesn't file. It doesn't email your CPO. It preps the folder. It gives you a summary. It stops. The whole build took a fraction of the setup the insurance one did. Why? Nothing in it was new. Third turn of the wheel, much easier. This is the principle I want you to understand. You put the work into building this system. Now, you can do lots of sensitive stuff relatively easily. This is an expandable agent. We're into Legos here, people. Okay? So, hold these three builds side by side for a second. Email, insurance, and taxes. Sure, the words changed, the stakes changed, but the skeleton of the agent didn't. You still had to have a context pack and ingest and chunk and normalize and store and retrieve and site and export and gate. You've now watched me run that list three times. That is the build. Now, one more thing that all three builds share underneath. Clean normalized data. That's the secret, guys. When dates are dates and every claim has an address, you stop needing the most expensive model for most of the work. I get asked a lot, especially post fable, what's the cheapest model? It's the open- source model. Listen, this is the same play Apple wants to run on your phone. Lightweight models can do advanced things when the data underneath is clean. So, I'm laying the stage for you to think about more model choice by making sure you take care of the data first. Number one, the hard part is not the final click. The hard part is context. Fix that dirty pile of data first. Number two, learn the gate where mistakes are cheap. Where does it become expensive to do something? Number three, understand where humans need to have expertise. If it touches money, if it touches health, this is something where a professional needs to get involved and you need to not pretend that AI can just do the job. Number four, don't build one offs. Please, I'm begging you, build a flywheel like I showed you today. Every build that I'm showing you makes the next one cheaper. And the bridge from your 101 agent to your 2011 to your 301 is shorter than you think. The Substack post has both of the runbooks, the healthcare appeals build and the tax prep organizer, plus the two open skills underneath them. It has a guide for context engineering, and it has runbooks. Now, here's what I'm asking you to do. Put in the comments the folder you'd point this at next, whether it's insurance or taxes or something I haven't thought of. Tell me what it is. I'll pick a few and we're going to build guides around them because this shelf is going to grow over time. Next time we're going to talk about how to put every model in the world at your fingertips, including the cheap ones. Because once your data is as clean as I've shown you in this video, you don't need an expensive model for most of this work. You just need the same agent skeleton and you can apply to different paperwork. You can keep that human yes or no at the end and you can go for it. So, subscribe for more and go open that folder and get to

---

## Timestamped Segments

**[0:00]** Every AI agent demo that you've seen

**[0:02]** this year starts in the same place,

**[0:04]** email and calendar, or I feel like I've

**[0:06]** seen a ton of them. You draft the

**[0:08]** replies, you schedule the meetings, and

**[0:10]** and I get why, right? So many of us have

**[0:12]** this problem every single day. It's

**[0:14]** where we spend a lot of time, bad and

**[0:16]** Slack, but here's the trap that I see a

**[0:18]** lot of us fall into. We set up the

**[0:20]** agent, it kind of works, and we're kind

**[0:22]** of stuck from there because we don't

**[0:23]** know how to go from that level of work

**[0:27]** where you're just getting some of your

**[0:28]** day-to-day stuff triaged to real work

**[0:30]** like insurance, like like payments, like

**[0:33]** health care that takes a lot of

**[0:36]** delicacy, that takes real trust. So,

**[0:39]** today, we're going to solve that for

**[0:40]** you. I'm going to build one agent

**[0:42]** skeleton live. We're going to learn

**[0:44]** about it on email and calendar, where

**[0:46]** mistakes are cheap. And then I'm going

**[0:48]** to show you how I use the same agent

**[0:50]** machinery to actually build a real

**[0:54]** delicate work, highstakes agent that

**[0:56]** handles insurance and tax stuff. When

**[0:59]** you tackle agent problems, here's the

**[1:01]** frame I want you to use. That tax folder

**[1:04]** you haven't opened, uh maybe the

**[1:05]** insurance denial that you never

**[1:06]** appealed, uh those kinds of problems

**[1:10]** look like different problems to us

**[1:12]** because we organize them by domain,

**[1:14]** health versus taxes. But anytime you're

**[1:17]** dealing with files or paperwork, it's

**[1:19]** not a different problem. From an agent's

**[1:22]** perspective, it's the same thing. It

**[1:24]** requires an understanding of policy. It

**[1:28]** requires an understanding of category.

**[1:30]** It requires an understanding of detail.

**[1:32]** And you don't have good organization to

**[1:34]** get any of that out. In other words,

**[1:36]** it's a messtofile organization problem

**[1:39]** first and then you get structured

**[1:41]** insights out. That is a common pattern

**[1:43]** across a lot of our delicate high trust

**[1:46]** paperwork issues that bedevil our lives

**[1:49]** and cost us time after time. I see the

**[1:51]** same thing when I'm booking medical

**[1:52]** appointments, right? You see the same

**[1:54]** thing with education forms. Anytime that

**[1:57]** you have to take a bunch of stuff and

**[2:00]** turn it into structured context that you

**[2:02]** can use for a delicate operation, it's

**[2:04]** the same fundamental agent principle.

**[2:06]** Now, when we talk about agents, we

**[2:09]** almost always talk about action, right?

**[2:10]** the agent will do something. It will

**[2:12]** send an email or file something. And I

**[2:15]** get it, right? It looks really good, but

**[2:17]** when you're doing high trust work, I

**[2:20]** would encourage you and I would ask you

**[2:22]** to focus on the part that the agent

**[2:24]** actually lifts the weight on. Like I'm

**[2:26]** interested in agents that lift the load

**[2:28]** off. And and to me, an agent that can

**[2:30]** sort through bureaucracy with

**[2:32]** unstructured context with the mess in my

**[2:35]** folder. Uh that's more useful to me than

**[2:38]** an agent that can click a button. I can

**[2:40]** click the button. I need the agent to

**[2:42]** get everything ready so that clicking

**[2:44]** that button is really easy. And so the

**[2:45]** skeleton we're building today does nine

**[2:47]** things. And you're going to see every

**[2:49]** one of them on screen. So I'll just say

**[2:50]** them once. We're building a context

**[2:52]** pack. We're building injust. We're

**[2:54]** building chunking. We're building

**[2:56]** normalizing, storing, retrieving,

**[2:58]** citing, exporting, and gating. And yes,

**[3:00]** agents will help with all of it. That

**[3:02]** last one, the gate, is the rule from the

**[3:04]** top of this video. If the agent can read

**[3:06]** and organize and draft and site, that's

**[3:08]** great. but it's not allowed to submit or

**[3:10]** pay or sign. And I want to be clear,

**[3:13]** this is a job that we're giving the

**[3:15]** agent from the beginning. So, it has

**[3:17]** good guard rails. We're not giving the

**[3:19]** agent ever the option to take an

**[3:22]** unallowed step. And it's up to you as

**[3:25]** the human to keep that guardrail in

**[3:28]** place as you build and to ensure that

**[3:29]** you are actually testing this stuff and

**[3:32]** you are actually validating before you

**[3:33]** submit an insurance claim or a tax claim

**[3:35]** that it's on you as the human to submit

**[3:38]** it. It's not on the agent. So, here's

**[3:39]** how we're going to run this. We're going

**[3:40]** to have three builds all in this video.

**[3:43]** Same fundamental structure. What I'm

**[3:44]** trying to teach you is one structure

**[3:46]** that scales. We're going to start easy.

**[3:48]** We're going to start with your email and

**[3:49]** calendar, which is unstructured mess,

**[3:50]** but very low stakes. Then, I'm going to

**[3:52]** stop and I'm going to show you the

**[3:54]** bridge, the actual move that takes you

**[3:56]** from the calendared email world to the

**[3:58]** more advanced part. And it's something

**[3:59]** everybody skips. And then, we're going

**[4:01]** to get into insurance appeals and then

**[4:03]** taxes as some of our advanced use cases,

**[4:05]** our 2011 use cases, if you will. So,

**[4:08]** let's get started. All right, we're

**[4:09]** going to get into build one. And let's

**[4:11]** be honest, your inbox is probably a

**[4:13]** dumpster fire. Mine certainly was, too.

**[4:15]** And it's not because we're disorganized.

**[4:17]** I'm going to keep saying that. It's

**[4:18]** because email is effort that other

**[4:20]** people give to us. Everything lands

**[4:22]** there, not on our agenda. And it's so

**[4:25]** hard to structure it. Now, let's notice

**[4:27]** something before we start. This is not

**[4:29]** just the training wheels example. Your

**[4:31]** W2 is probably in that inbox somewhere.

**[4:33]** I know mine was. The denial letter from

**[4:35]** an insurance company may have arrived as

**[4:37]** a PDF attachment. You may have notes

**[4:39]** from your doctor leading to secure

**[4:40]** messages. The trusted work we're

**[4:42]** building toward is often email mediated.

**[4:45]** Here's a thread where someone's trying

**[4:46]** to schedule a meeting with me. The agent

**[4:48]** gets a context pack. That's the first

**[4:50]** skeleton idea that I talked about. And a

**[4:52]** context pack just defines what the agent

**[4:55]** is allowed to read. This thread, my

**[4:57]** calendar constraints, the people

**[4:58]** involved. And it has one goal. Prepare a

**[5:01]** reply with a proposed calendar hold.

**[5:03]** Notice the word prepare. Watch what it

**[5:05]** does. It ingests the thread. It pulls

**[5:08]** out the people, the date ranges, the

**[5:10]** time zone mismatch. Dates become dates.

**[5:13]** People become people. That's what

**[5:14]** normalization is called. And I know it

**[5:16]** sounds boring, but this boring stuff is

**[5:19]** what makes the agent do useful high

**[5:21]** trust work. I promise you it's worth it.

**[5:23]** So the agent checks my constraints. It

**[5:25]** drafts the reply and it builds the

**[5:26]** proposed calendar of Now watch this

**[5:29]** because this is the moment the whole

**[5:30]** video turns on. The draft is done and

**[5:32]** the next obvious thing would be to send

**[5:34]** it and and the agent stops and I want it

**[5:37]** to. It leaves the draft. It leaves the

**[5:38]** proposed hold and it leaves a receipt.

**[5:40]** What sources it used? What it changed?

**[5:42]** What still needs my approval? And if

**[5:44]** it's right, I'll just send it. If it's

**[5:46]** wrong, I can fix it. That receipt to me

**[5:50]** is critical. It's the difference between

**[5:52]** AI handled it and I know what happened

**[5:55]** here and I can trust the AI. It is so

**[5:57]** important to build for trust from day

**[5:59]** one. if you ever want your AI to do

**[6:01]** stuff that involves high value delicate

**[6:04]** work where real money is on the line

**[6:06]** where real value is coming back to you

**[6:09]** because like you we all know like if we

**[6:10]** appeal insurance and we win if if if we

**[6:12]** file taxes correctly and we get a refund

**[6:15]** that's real money on the lens thousands

**[6:16]** of dollars potentially if you wanted to

**[6:18]** help with that you got to get this trust

**[6:20]** piece right now let's pause for a second

**[6:22]** because this is a move almost everybody

**[6:24]** misses and it's the reason most people

**[6:27]** never get past that initial email simple

**[6:30]** 101 agent demo. You might think that

**[6:33]** going from a basic agent like an email

**[6:35]** agent to an insurance appeal means

**[6:37]** starting over. A new tool, a new setup,

**[6:39]** a new system that's higher trust. It

**[6:41]** doesn't if you build it right. Look at

**[6:43]** what you already own from build one. You

**[6:46]** own ingestion, turning documents into

**[6:48]** text the agent can use with anchors back

**[6:50]** to the source. You own normalization.

**[6:52]** You own dates becoming dates and people

**[6:54]** becoming people. You own the receipt.

**[6:56]** You own the gate. And those are

**[6:57]** primitives or building blocks. And none

**[7:00]** of them care whether you're in a

**[7:01]** scheduling thread or an insurance denial

**[7:04]** claim. It's the same thing to the agent.

**[7:06]** And that's why I keep calling this a

**[7:08]** flywheel. Every build we do, if we're

**[7:10]** doing it right, adds a skill to our

**[7:12]** shelf. And that makes the next build

**[7:15]** cheaper. So now, let's turn around

**[7:17]** again, and let's tackle a task that

**[7:19]** actually costs you money. First, I'm

**[7:22]** going to tell you what's real and what

**[7:23]** isn't here because I want you to

**[7:24]** actually know and trust this demo. The

**[7:26]** policy documents you're about to see are

**[7:28]** real. Insurers publish their plan

**[7:30]** documents. So, this system is querying

**[7:31]** an actual insurers's actual policy

**[7:33]** language. The patient for privacy is

**[7:36]** synthetic. The denial letter is built

**[7:38]** from the kind of denial letter that

**[7:39]** people post publicly, but every

**[7:41]** identifying detail has been masked. And

**[7:43]** this build works exactly the same on

**[7:45]** your real files and yours stay on your

**[7:48]** machine. Now, some new words to learn

**[7:50]** here in the context pack. We have denial

**[7:51]** letter. We have real policies and claim

**[7:53]** histories and supporting documents. And

**[7:55]** we have a new goal. I don't want a

**[7:57]** vibes-based appeal letter. I want a case

**[7:59]** file that I can inspect. So, this is

**[8:01]** more delicate work already than the

**[8:03]** email. All right, let's get to work. The

**[8:05]** agent starts by chunking. The denial

**[8:07]** letter is not one blob, right? It's got

**[8:09]** a date. It's got a denial reason. It's

**[8:10]** got a claim number, a deadline, and

**[8:12]** somewhere in there, there's a paragraph

**[8:14]** that says, "What evidence would change

**[8:16]** that decision?" And the policy is not

**[8:18]** one blob either. It has sections and

**[8:19]** definitions and exclusions and appeal

**[8:21]** rules. Everything is getting split into

**[8:23]** tagged and addressable pieces by the

**[8:25]** agent. Now we're normalizing. Like

**[8:28]** before, dates are becoming dates.

**[8:30]** Amounts are becoming amounts. And this

**[8:31]** one matters. Missing documents are

**[8:33]** becoming missing documents. That's

**[8:35]** especially important if you have a gap

**[8:37]** in your evidence because it can affect

**[8:38]** what you can act on and you won't get a

**[8:40]** surprise a few days before some kind of

**[8:42]** deadline. All of it is stored locally.

**[8:45]** You have a little database called SQLite

**[8:47]** and you have a folder and you can open

**[8:48]** the sources and the records yourself.

**[8:50]** Nothing leaves your machine. You never

**[8:52]** have to ask the model to remember what

**[8:53]** happened. When an insurer denies you,

**[8:55]** they're required to site the specific

**[8:57]** policy language they're relying on.

**[8:59]** Think about what that means. You're not

**[9:01]** searching for something you can't find.

**[9:02]** You already know the address of the

**[9:04]** thing that's hurting you. So, there's no

**[9:05]** vector database there, only a similarity

**[9:08]** search. The system simply has to

**[9:10]** retrieve by structure the denial reason,

**[9:13]** the exact policy section, the denial

**[9:15]** sites, the deadline, and the document

**[9:16]** checklist. And the first thing that the

**[9:19]** agent is going to do when it does all

**[9:20]** this is a sanity check. Does the section

**[9:23]** they cited actually say what the letter

**[9:25]** implies that it says? Sometimes it

**[9:27]** doesn't. And when it doesn't, that's

**[9:28]** finding number one. Now, look at what

**[9:30]** this produces. There's a timeline with a

**[9:33]** service date and claim date and denial

**[9:35]** date and an appeal deadline. There's

**[9:36]** actually a denial map. There's the exact

**[9:39]** policy language that governs all of

**[9:41]** this. There's an evidence checklist,

**[9:43]** what I have right now, what isn't there

**[9:44]** yet. And yes, there's a draft appeal

**[9:46]** letter, but the letter isn't the main

**[9:48]** thing. The whole evidence packet is what

**[9:51]** really matters here because the citation

**[9:54]** map means you can actually validate that

**[9:56]** what you're arguing is true. So, here's

**[9:59]** the reframe against conventional wisdom.

**[10:02]** The agent is not winning the appeal for

**[10:05]** you. It is turning the pile of

**[10:07]** unstructured information into a case

**[10:09]** file that makes you able to win. you

**[10:12]** were losing or you didn't win because

**[10:14]** you were showing up to a structured

**[10:16]** fight with an unstructured pile. This

**[10:18]** bill doesn't guarantee that you win. It

**[10:20]** just means you stopped showing up with

**[10:22]** bad data. Now, again, watch where the

**[10:24]** agent stops. The agent has drafted the

**[10:26]** appeal, the address, the claim number,

**[10:28]** the deadline, and the viral demo would

**[10:31]** be to say, "Okay, now we're going to

**[10:32]** send it." No, it stops. And I want to be

**[10:35]** very plain about this. You are

**[10:37]** responsible for what you send. I'm not

**[10:39]** advocating anybody fire one of these

**[10:41]** packets at an insurance company unread.

**[10:44]** The citations make your review faster.

**[10:46]** They don't make it optional because if

**[10:48]** an agent sends a bad appeal on its own,

**[10:50]** now you have two problems. The denial

**[10:52]** and the mess the agent made. This is the

**[10:54]** same skeleton as our email build. The

**[10:57]** nouns may have changed, but the

**[10:59]** underlying data, the underlying

**[11:01]** structure of how we solve this problem

**[11:03]** is exactly the same from the agents

**[11:05]** point of view. And that's how we build

**[11:06]** momentum. Okay. Build number three. I'm

**[11:09]** going to show you taxes. Everybody has

**[11:11]** to deal with taxes. And I want you to

**[11:13]** notice how fast this goes now because

**[11:15]** this is the flywheel doing what I

**[11:17]** promised at the top of the video. Again,

**[11:19]** we're going to say synthetic documents

**[11:20]** here. Tax folders are things nobody

**[11:22]** should see on YouTube. Uh, and we're

**[11:24]** going to tackle some new objects, right?

**[11:26]** So, you're going to see W2s and 1099s

**[11:28]** and invoices and receipts and bank

**[11:30]** exports and mileage notes. The works.

**[11:32]** And notice where half of this stuff was

**[11:34]** living. It was living in the inbox. That

**[11:37]** dumpster fire from build one is a source

**[11:39]** now for build three. Our new goal here

**[11:42]** is we're not filing. We are preparing a

**[11:45]** reviewable packet for you or your CPA.

**[11:47]** And if you're paying somebody hundreds

**[11:49]** of dollars or thousands of dollars to

**[11:51]** painfully comb through your pile of tax

**[11:53]** docs, understand what you're paying for.

**[11:56]** You're paying for the combing. This is

**[11:58]** the combing of the docks. It's the same

**[12:00]** skeleton we already built. It goes

**[12:02]** through the same order agent-wise.

**[12:04]** You're just ingesting. You chunk it into

**[12:06]** forms. You have income, expenses,

**[12:08]** unknowns. You normalize into a tax year

**[12:10]** ledger with date and vendor and amount

**[12:12]** and category and source file. And again,

**[12:14]** we have guard rails. The citation guard

**[12:16]** won't let a deduction float through

**[12:18]** without evidence. If the agent says it's

**[12:20]** a business expense, it's going to point

**[12:22]** at the receipt or it's going to flag the

**[12:24]** line instead of pretending it knows. The

**[12:27]** export you get is a packet, not a

**[12:29]** completed 1040 return. You get an income

**[12:32]** summary, an expense ledger, a deduction

**[12:34]** evidence map, and missing docs where you

**[12:36]** have them, plus a list of questions for

**[12:37]** the CPA. And that last one is

**[12:39]** underrated. A good agent doesn't just

**[12:41]** give you answers. A good agent gives you

**[12:43]** better questions to ask an expert. And

**[12:46]** look at that. It doesn't submit. It

**[12:48]** doesn't file. It doesn't email your CPO.

**[12:50]** It preps the folder. It gives you a

**[12:52]** summary. It stops. The whole build took

**[12:55]** a fraction of the setup the insurance

**[12:58]** one did. Why? Nothing in it was new.

**[13:00]** Third turn of the wheel, much easier.

**[13:02]** This is the principle I want you to

**[13:04]** understand. You put the work into

**[13:06]** building this system. Now, you can do

**[13:09]** lots of sensitive stuff relatively

**[13:11]** easily. This is an expandable agent.

**[13:14]** We're into Legos here, people. Okay? So,

**[13:16]** hold these three builds side by side for

**[13:18]** a second. Email, insurance, and taxes.

**[13:22]** Sure, the words changed, the stakes

**[13:24]** changed, but the skeleton of the agent

**[13:26]** didn't. You still had to have a context

**[13:28]** pack and ingest and chunk and normalize

**[13:31]** and store and retrieve and site and

**[13:33]** export and gate. You've now watched me

**[13:35]** run that list three times. That is the

**[13:38]** build. Now, one more thing that all

**[13:40]** three builds share underneath. Clean

**[13:42]** normalized data. That's the secret,

**[13:45]** guys. When dates are dates and every

**[13:48]** claim has an address, you stop needing

**[13:50]** the most expensive model for most of the

**[13:52]** work. I get asked a lot, especially post

**[13:54]** fable, what's the cheapest model? It's

**[13:56]** the open- source model. Listen, this is

**[13:58]** the same play Apple wants to run on your

**[14:00]** phone. Lightweight models can do

**[14:02]** advanced things when the data underneath

**[14:04]** is clean. So, I'm laying the stage for

**[14:06]** you to think about more model choice by

**[14:09]** making sure you take care of the data

**[14:11]** first. Number one, the hard part is not

**[14:14]** the final click. The hard part is

**[14:16]** context. Fix that dirty pile of data

**[14:18]** first. Number two, learn the gate where

**[14:21]** mistakes are cheap. Where does it become

**[14:24]** expensive to do something? Number three,

**[14:26]** understand where humans need to have

**[14:29]** expertise. If it touches money, if it

**[14:32]** touches health, this is something where

**[14:34]** a professional needs to get involved and

**[14:36]** you need to not pretend that AI can just

**[14:38]** do the job. Number four, don't build one

**[14:41]** offs. Please, I'm begging you, build a

**[14:44]** flywheel like I showed you today. Every

**[14:46]** build that I'm showing you makes the

**[14:47]** next one cheaper. And the bridge from

**[14:50]** your 101 agent to your 2011 to your 301

**[14:53]** is shorter than you think. The Substack

**[14:55]** post has both of the runbooks, the

**[14:57]** healthcare appeals build and the tax

**[14:59]** prep organizer, plus the two open skills

**[15:02]** underneath them. It has a guide for

**[15:03]** context engineering, and it has

**[15:05]** runbooks. Now, here's what I'm asking

**[15:07]** you to do. Put in the comments the

**[15:09]** folder you'd point this at next, whether

**[15:11]** it's insurance or taxes or something I

**[15:13]** haven't thought of. Tell me what it is.

**[15:15]** I'll pick a few and we're going to build

**[15:16]** guides around them because this shelf is

**[15:18]** going to grow over time. Next time we're

**[15:20]** going to talk about how to put every

**[15:22]** model in the world at your fingertips,

**[15:24]** including the cheap ones. Because once

**[15:26]** your data is as clean as I've shown you

**[15:28]** in this video, you don't need an

**[15:30]** expensive model for most of this work.

**[15:32]** You just need the same agent skeleton

**[15:34]** and you can apply to different

**[15:36]** paperwork. You can keep that human yes

**[15:38]** or no at the end and you can go for it.

**[15:41]** So, subscribe for more and go open that

**[15:43]** folder and get to
