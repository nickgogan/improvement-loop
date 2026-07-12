# Transcript: This Skill Instantly 10x’es Every Claude Output

**URL:** https://www.youtube.com/watch?v=d2XiTDzoizc
**Segments:** 436
**Channel:** Ben AI
**Duration:** 14:19
**Uploaded:** 2026-07-02

---

## Full Text

Most people that use Claude, including me, have a few giant chat sessions we keep coming back to for reviewing copy, writing responses, or other repetitive use cases. And the reason we don't start new chats is because it means re-explaining all of the rules and context for that specific task again. But there's one big problem we're ignoring while doing this, which is context rot. So in this video, I'll explain what context rot is and why actually managing it makes a huge impact on your AI outputs, show you a simple skill that tells you when to continue in a new chat session, and show you the refresh skill that helps you start a new chat session without ever having to re-explain stuff again. Now, you'll be able to download the refresh skill for free in the first link in the description below, but before showing you the skill, it is important to actually understand how a context window works. Each chat session you open in Claude Opus, for example, has a 1 million token context window. And every prompt, every answer, every file, every connector you use, or every skill Claude uses, this all fills up that context window. And the easiest way to understand the limitations of this context window is by thinking of the context window as your own brain on a normal day-to-day. The more information you ingest, the more it fills up, and the closer you come to your daily processing limit. And the more you start forgetting information you learned earlier in the day, the less clearly you remember things, the more fuzzy all of this info becomes, and the less productive you become. And although Claude has a very large 1 million token window with Opus 4.8, the same thing happens with Claude. Even far before hitting that limit, it starts forgetting, becoming fuzzy, and therefore significantly impacting the quality of your AI outputs. Essentially, it becomes dumber the more you use it, which you've probably noticed. But this actually starts happening a lot earlier than most people realize. From 0 to 200,000 tokens is really where you're going to get the best outputs from AI. And from 200 to 350,000, it can still be very useful, but it can already start drifting a bit. By 350,000 tokens, it really starts significantly impacting your outputs. And after reaching 400,000 tokens, it's usually the point where you really start to get frustrated with AI. And therefore, I call the "you're right to push back" zone. Uh because when you hear Claude say that, you're probably in this zone. And it's where you really need to start a fresh chat session. Now, before showing you the refresh skill that helps you continue the conversation in a fresh context window or fresh chat without having to re-explain the rules and the context again, you first need to be able to know how many tokens you actually used in each chat and when you actually should switch to a new chat. Now, if you use Claude code in the terminal, you actually have a setting to show how many the amount of tokens you used inside of one chat, so it becomes really easy to track. But if you're like me and often work in a Claude desktop because you prefer the UI, especially for knowledge work, there's no way to directly see the amount of tokens you've used inside of one chat window. Not in Claude co-work, but also not in Claude code desktop. But there is actually a skill that many people don't know about, which is the {slash} context skill that you can use at any time in any chat in co-work or Claude code to know how many tokens you've spent and what on. So, first of all, I highly recommend starting to use the {slash} context regularly and get in the habit of using it because using it will not only instantly give you the insight in where you are in the chat, so you know when to start fresh, but also a nice benefit of this is that the more you start using this, the more you start understanding what burns tokens and what not. Then you start to develop a better feeling of when you're at the sort of this cut-off limit and should start a new chat. For example, I've learned by using this more and more that doing research and using connectors and MCPs is probably by far one of the biggest token spenders. So, I know I have to switch to a new chat a lot sooner. Now, in order to form that habit of using {slash} context, it's good to look out for a few signals that indicate that you probably should be using {slash} context to know where you're at in the context window. Now, the first one, of course, the obvious one is in really long sessions, you want to start using this. Secondly, if you're anything like me and you keep coming back to similar chats because you already have primed a specific chat for specific tasks. For example, here I have a really long chat where I usually review all of my new newsletter copies and I keep coming back to this one because uh this one already has all my specific rules and instructions on optimizing the copy for my newsletters. I usually have these very long chats too for every YouTube video I create where I go from title ideation to research to outline preparation, everything in one chat because it already has all the context in there. Then thirdly, you especially want to start doing this earlier in chats uh when you use a lot of connectors or do a lot of research because these tend to spend a lot of tokens, much more than you think. And fourthly, of course, the biggest signal to look out for is clearly seeing the outputs getting worse, you having to re-explain things, AI maybe drifting a bit, or you getting frustrated. And this is probably your strongest signal. And instead of screaming at AI, you have to get in the habit of using {slash} context because you'll notice that often it is simply because you're already past that 400K mark. Now, once you have identified a session that is in the dumb zone, you need to start a new chat. But how do we actually carry over the context into the new chat so we don't have to re-prompt and give all of that context again. Now, some of you might already know that Claude has a built-in skill called {slash} compact. And this basically aims to help you do exactly this. It basically makes a summary of everything you've done in that chat, the chat history, the context files, and everything else, and compacts this into summary of around 50 to 60K tokens so you can continue with the same task in a fresh context window while still having relevant context from your previous chat session. And if you use it in Claude, for example, here {slash} compact, you see that starts compacting the conversation and making a summary. And once it's compacted the conversation, you can actually continue in the same chat window. But what happens in the back is it actually starts a fresh context window with that summary. But in my experience, this {slash} compact has some real flaws, and it's why I haven't been using it that much and often preferred to just keep going in a longer session, even with some context rot. So this is exactly why I built the refresh skill to get around some of the flaws of the {slash} compact. So in essence, this refresh skill is very similar to the compact skill. They both summarize the chat and the context. But firstly, the refresh skill actually works in co-work because {slash} compact only works in Claude code. And for many copywriting or YouTube ideation or knowledge work-type task, I just prefer co-work. But the three bigger problems with the {slash} compact that I tried to resolve with the refresh skill is that firstly, in my experience, the {slash} compact, the summary, is just not comprehensive enough. It basically makes a short summary of everything, which in my experience just means uh re-explaining and re-prompting a lot of the same stuff in that new chat session again. So firstly, the refresh skill just makes a far more comprehensive summary to avoid that re-explaining. It does mean it spends more tokens, probably around a 100,000 mark. But again, in my experience, it's just worth the time and the effort you gain by spending a bit more tokens in that fresh context window. It also actually asks you what's the goal of your next session before creating the summary so you can actually put in the relevant context for what you're trying to do in the next chat. Because you don't just want to use this to continue on the same task in a very long session. You also want to do this when you're varying off your original task and trying to do a different task that still needs that same context. For example, I want to write a newsletter based on the context in my YouTube ideation chat, then I'd also want to use the refresh skill to make sure I'm doing the iteration on the newsletter in a fresh chat, so it doesn't pollute the context window of the YouTube ideation chat. Secondly, the reason these recurring chats or long chats are often so valuable and why you keep coming back to them is because you've accumulated a lot of little rules and instructions and do's and don'ts around the specific task while going back and forth with AI. And I noticed that those little rules and and instructions get completely lost with the slash compact. And this is exactly what the refresh skill also does. It looks first of all of the status, where are we in the process in this chat? It looked at what worked, what didn't work, and all the rules. They write They write down the specific rules and instructions and the do's and don'ts that the user gave inside of that chat and takes them into the new chat session. And lastly, which is the biggest one for me, because when I'm using AI, for example, for my YouTube ideation or my copywriting tasks or many other things, I often feed a lot of context docs to my AI to get a full understanding of me, my business, my ICP before giving me outputs. For example, you can see here in one of my YouTube ideation chats, I let it read my strategy, my ICP, my brand, some of my old video transcripts, and some more uh documents because it just improves the outputs and they get far more relevant in my experience. And the problem with the slash compact skill is it basically makes a very tiny summary of each of these files, which means again I have to re-prompt to read all of these files or re-feed this context each time I start a new chat. And this is the next thing that the refresh skill does. It basically lists out all of the context docs that were fed inside of this chat and instructs the next session to first read all of these docs before actually continuing with the task, which for me just creates so much less friction in the process of transferring this into a new chat that I actually start doing it and actually can get far better outputs because I'm not, you know, uh prompting back and forth in a context window that's actually in the dumb zone. So, let me show you some examples of how this skill works in practice. So, here I used it, for example, in one of my uh YouTube preparation chats where I do anything from title ideation to research to outline generation to script reviewing and more. But, because I do that, of course, it reaches that 400k mark pretty quick. So, after a long session here, I used that refresh skill. What the skill always does is it first asks you about what you want to do in your next session. Because depending on what I want to do, it can then actually save the relevant context based on that goal. Now, in this case, I said I want to continue working on the same video. And what the skill then does is it first starts creating a few files and adding them into the folder that I selected at the start of this chat. One around the outline that we confirmed for this video in this chat, one around the intro, one about the research findings, uh one around the decisions and rules. Basically, a very comprehensive summary with all of the relevant context from this chat and the history that we need the next session to know. And then it creates a prompt for the new session in Claude where it first of all states the goal for this task. It then directly gives an instruction of read all of these files first. So, it basically tells Claude in that new session to first read all of these files that it just created. And it also points to all of the other context um we used inside of this chat like my strategy, my ICP, my brand, and some YouTube transcripts. Now, this is of course especially powerful and relevant if you already use a lot of context in your chat or are using a second brain. And then lastly, it adds a few sections on uh where things stand and all of the specific rules and instructions that I've given in this chat, what worked in this chat and what didn't work and what corrections were made. We can then just copy this, go to a new task, make sure that we select the same folder as we worked in in the previous chat. That's why you always want to select a folder when you work in uh co-work or Claude code. It's just a habit you want to get into even if you haven't set up a second brain or use a lot of context yet. And once you paste that in, you see that it starts reading all of the context files before doing anything else. So, you can see by reading all of this relevant context around the last chat and the context it used in our last chat, it is immediately primed to continue on that same task. It knows the status, it knows the specific roles I've given in the last chat. I've also been using this on these chats where I keep coming back to like my newsletter email copy optimization chats cuz as you can see this has just become way too long over time. So, same thing here. Use my refresh skill to get a fresh session while still having all of those specific instructions, the context docs, and examples are still saved. There's a second use case you want to start using this for, which is when you're actually veering off your original task and start using that same chat window for new type of task. I know this is also an issue and a trap many people fall into including myself. For example, if I now in a YouTube ideation chat want to create a newsletter out of the context that I already have inside of this this chat, which is great because of course it already has lots of context around this topic, I shouldn't actually start doing that in that same chat because of course I start polluting the context window. Claude completely drifts off from the original task. So, it's far better to use the refresh skill because you still keep that same context but use it for a new type of task in a fresh window. So, you can see for this YouTube video I used the refresh but in this case I told it to I want to create a newsletter based on the context in this chat. It then did the same again, created some files, created a prompt, pasted that into a new window, it read all the relevant files, and then actually started using my newsletter skill right away. Again, you can download the skill for free in the first link in the description below. It is a little bit of a habit you have to get into but I highly recommend it cuz first of all if you start tracking your context window with {slash} context, if you get in the habit of that, it is really going to improve the way you use AI and the outputs you'll get from AI. And second, once you start doing that highly recommend starting to use this refresh skill more and more and maybe earlier and earlier in your context windows because you'll be surprised how much better your outputs become in general. Also, if you want access to all of the skills that me and my team are building out, including workflow specific ones for sales, marketing, operations, and general business skills, you can check out my AI accelerator in the second link in the description below. We also have unlimited one-on-one live tech help, full cloud courses, and courses on setting up your own AI OS and second brain, and a community of serious professionals and business owners. So, if that's interesting to you, you can check it out in the second link in the description below. Also, credits to Matt Pocock who came up with the handoff skill, which inspired me to actually build this refresh skill. The handoff skill works in a similar way, but is more of an engineering skill. I built the refresh skill more for knowledge type work. So, again, credits to Matt Pocock. Definitely follow him if you don't know him yet. He's a great creator. Thank you so much for watching, and if you want to learn eight more skills that I use almost every day, you can check out the video here above.

---

## Timestamped Segments

**[0:00]** Most people that use Claude, including

**[0:02]** me, have a few giant chat sessions we

**[0:04]** keep coming back to for reviewing copy,

**[0:06]** writing responses, or other repetitive

**[0:08]** use cases. And the reason we don't start

**[0:11]** new chats is because it means

**[0:12]** re-explaining all of the rules and

**[0:14]** context for that specific task again.

**[0:17]** But there's one big problem we're

**[0:19]** ignoring while doing this, which is

**[0:20]** context rot. So in this video, I'll

**[0:22]** explain what context rot is and why

**[0:25]** actually managing it makes a huge impact

**[0:27]** on your AI outputs, show you a simple

**[0:29]** skill that tells you when to continue in

**[0:31]** a new chat session, and show you the

**[0:33]** refresh skill that helps you start a new

**[0:36]** chat session without ever having to

**[0:38]** re-explain stuff again. Now, you'll be

**[0:40]** able to download the refresh skill for

**[0:42]** free in the first link in the

**[0:43]** description below, but before showing

**[0:44]** you the skill, it is important to

**[0:46]** actually understand how a context window

**[0:47]** works. Each chat session you open in

**[0:50]** Claude Opus, for example, has a 1

**[0:52]** million token context window. And every

**[0:55]** prompt, every answer, every file, every

**[0:57]** connector you use, or every skill Claude

**[0:59]** uses, this all fills up that context

**[1:02]** window. And the easiest way to

**[1:03]** understand the limitations of this

**[1:05]** context window is by thinking of the

**[1:07]** context window as your own brain on a

**[1:09]** normal day-to-day. The more information

**[1:11]** you ingest, the more it fills up, and

**[1:14]** the closer you come to your daily

**[1:15]** processing limit. And the more you start

**[1:17]** forgetting information you learned

**[1:19]** earlier in the day, the less clearly you

**[1:20]** remember things, the more fuzzy all of

**[1:23]** this info becomes, and the less

**[1:24]** productive you become. And although

**[1:27]** Claude has a very large 1 million token

**[1:29]** window with Opus 4.8, the same thing

**[1:31]** happens with Claude. Even far before

**[1:33]** hitting that limit, it starts

**[1:35]** forgetting, becoming fuzzy, and

**[1:37]** therefore significantly impacting the

**[1:39]** quality of your AI outputs. Essentially,

**[1:41]** it becomes dumber the more you use it,

**[1:43]** which you've probably noticed. But this

**[1:45]** actually starts happening a lot earlier

**[1:47]** than most people realize. From 0 to

**[1:49]** 200,000 tokens is really where you're

**[1:51]** going to get the best outputs from AI.

**[1:53]** And from 200 to 350,000,

**[1:56]** it can still be very useful, but it can

**[1:58]** already start drifting a bit. By 350,000

**[2:01]** tokens, it really starts significantly

**[2:03]** impacting your outputs. And after

**[2:06]** reaching 400,000 tokens, it's usually

**[2:08]** the point where you really start to get

**[2:09]** frustrated with AI. And therefore, I

**[2:11]** call the "you're right to push back"

**[2:13]** zone. Uh because when you hear Claude

**[2:15]** say that, you're probably in this zone.

**[2:17]** And it's where you really need to start

**[2:18]** a fresh chat session. Now, before

**[2:20]** showing you the refresh skill that helps

**[2:22]** you continue the conversation in a fresh

**[2:24]** context window or fresh chat without

**[2:27]** having to re-explain the rules and the

**[2:28]** context again, you first need to be able

**[2:30]** to know how many tokens you actually

**[2:32]** used in each chat and when you actually

**[2:34]** should switch to a new chat. Now, if you

**[2:36]** use Claude code in the terminal, you

**[2:38]** actually have a setting to show how many

**[2:40]** the amount of tokens you used inside of

**[2:42]** one chat, so it becomes really easy to

**[2:44]** track. But if you're like me and often

**[2:45]** work in a Claude desktop because you

**[2:47]** prefer the UI, especially for knowledge

**[2:49]** work, there's no way to directly see the

**[2:51]** amount of tokens you've used inside of

**[2:53]** one chat window. Not in Claude co-work,

**[2:56]** but also not in Claude code desktop. But

**[2:58]** there is actually a skill that many

**[2:59]** people don't know about, which is the

**[3:00]** {slash} context skill that you can use

**[3:03]** at any time in any chat in co-work or

**[3:05]** Claude code to know how many tokens

**[3:07]** you've spent and what on. So, first of

**[3:09]** all, I highly recommend starting to use

**[3:11]** the {slash} context regularly and get in

**[3:14]** the habit of using it because using it

**[3:16]** will not only instantly give you the

**[3:17]** insight in where you are in the chat, so

**[3:20]** you know when to start fresh, but also a

**[3:22]** nice benefit of this is that the more

**[3:24]** you start using this, the more you start

**[3:26]** understanding what burns tokens and what

**[3:28]** not. Then you start to develop a better

**[3:30]** feeling of when you're at the sort of

**[3:32]** this cut-off limit and should start a

**[3:34]** new chat. For example, I've learned by

**[3:36]** using this more and more that doing

**[3:38]** research and using connectors and MCPs

**[3:40]** is probably by far one of the biggest

**[3:43]** token spenders. So, I know I have to

**[3:45]** switch to a new chat a lot sooner. Now,

**[3:47]** in order to form that habit of using

**[3:49]** {slash} context, it's good to look out

**[3:51]** for a few signals that indicate that you

**[3:53]** probably should be using {slash} context

**[3:55]** to know where you're at in the context

**[3:57]** window. Now, the first one, of course,

**[3:58]** the obvious one is in really long

**[4:00]** sessions, you want to start using this.

**[4:01]** Secondly, if you're anything like me and

**[4:04]** you keep coming back to similar chats

**[4:06]** because you already have primed a

**[4:08]** specific chat for specific tasks. For

**[4:10]** example, here I have a really long chat

**[4:12]** where I usually review all of my new

**[4:14]** newsletter copies and I keep coming back

**[4:16]** to this one because uh this one already

**[4:18]** has all my specific rules and

**[4:20]** instructions on optimizing the copy for

**[4:22]** my newsletters. I usually have these

**[4:24]** very long chats too for every YouTube

**[4:26]** video I create where I go from title

**[4:28]** ideation to research to outline

**[4:30]** preparation, everything in one chat

**[4:32]** because it already has all the context

**[4:34]** in there. Then thirdly, you especially

**[4:35]** want to start doing this earlier in

**[4:37]** chats uh when you use a lot of

**[4:39]** connectors or do a lot of research

**[4:41]** because these tend to spend a lot of

**[4:43]** tokens, much more than you think. And

**[4:45]** fourthly, of course, the biggest signal

**[4:47]** to look out for is clearly seeing the

**[4:49]** outputs getting worse, you having to

**[4:51]** re-explain things, AI maybe drifting a

**[4:53]** bit, or you getting frustrated. And this

**[4:56]** is probably your strongest signal. And

**[4:58]** instead of screaming at AI, you have to

**[5:00]** get in the habit of using {slash}

**[5:01]** context because you'll notice that often

**[5:03]** it is simply because you're already past

**[5:06]** that 400K mark. Now, once you have

**[5:08]** identified a session that is in the dumb

**[5:09]** zone, you need to start a new chat. But

**[5:11]** how do we actually carry over the

**[5:13]** context into the new chat so we don't

**[5:15]** have to re-prompt and give all of that

**[5:16]** context again. Now, some of you might

**[5:18]** already know that Claude has a built-in

**[5:20]** skill called {slash} compact. And this

**[5:22]** basically aims to help you do exactly

**[5:24]** this. It basically makes a summary of

**[5:27]** everything you've done in that chat, the

**[5:28]** chat history, the context files, and

**[5:31]** everything else, and compacts this into

**[5:33]** summary of around 50 to 60K tokens so

**[5:36]** you can continue with the same task in a

**[5:38]** fresh context window while still having

**[5:41]** relevant context from your previous chat

**[5:43]** session. And if you use it in Claude,

**[5:45]** for example, here {slash} compact, you

**[5:47]** see that starts compacting the

**[5:48]** conversation and making a summary. And

**[5:50]** once it's compacted the conversation,

**[5:52]** you can actually continue in the same

**[5:54]** chat window. But what happens in the

**[5:56]** back is it actually starts a fresh

**[5:58]** context window with that summary. But in

**[6:00]** my experience, this {slash} compact has

**[6:02]** some real flaws, and it's why I haven't

**[6:05]** been using it that much and often

**[6:06]** preferred to just keep going in a longer

**[6:09]** session, even with some context rot. So

**[6:11]** this is exactly why I built the refresh

**[6:13]** skill to get around some of the flaws of

**[6:16]** the {slash} compact. So in essence, this

**[6:18]** refresh skill is very similar to the

**[6:20]** compact skill. They both summarize the

**[6:22]** chat and the context. But firstly, the

**[6:25]** refresh skill actually works in co-work

**[6:27]** because {slash} compact only works in

**[6:30]** Claude code. And for many copywriting or

**[6:32]** YouTube ideation or knowledge work-type

**[6:34]** task, I just prefer co-work. But the

**[6:36]** three bigger problems with the {slash}

**[6:37]** compact that I tried to resolve with the

**[6:39]** refresh skill is that firstly, in my

**[6:41]** experience, the {slash} compact, the

**[6:43]** summary, is just not comprehensive

**[6:45]** enough. It basically makes a short

**[6:46]** summary of everything, which in my

**[6:48]** experience just means uh re-explaining

**[6:51]** and re-prompting a lot of the same stuff

**[6:53]** in that new chat session again. So

**[6:55]** firstly, the refresh skill just makes a

**[6:57]** far more comprehensive summary to avoid

**[7:00]** that re-explaining. It does mean it

**[7:02]** spends more tokens, probably around a

**[7:04]** 100,000 mark. But again, in my

**[7:06]** experience, it's just worth the time and

**[7:08]** the effort you gain by spending a bit

**[7:10]** more tokens in that fresh context

**[7:11]** window. It also actually asks you what's

**[7:14]** the goal of your next session before

**[7:16]** creating the summary so you can actually

**[7:18]** put in the relevant context for what

**[7:20]** you're trying to do in the next chat.

**[7:22]** Because you don't just want to use this

**[7:24]** to continue on the same task in a very

**[7:26]** long session. You also want to do this

**[7:28]** when you're varying off your original

**[7:30]** task and trying to do a different task

**[7:32]** that still needs that same context. For

**[7:34]** example, I want to write a newsletter

**[7:35]** based on the context in my YouTube

**[7:37]** ideation chat, then I'd also want to use

**[7:39]** the refresh skill to make sure I'm doing

**[7:41]** the iteration on the newsletter in a

**[7:44]** fresh chat, so it doesn't pollute the

**[7:46]** context window of the YouTube ideation

**[7:48]** chat. Secondly, the reason these

**[7:50]** recurring chats or long chats are often

**[7:53]** so valuable and why you keep coming back

**[7:54]** to them is because you've accumulated a

**[7:56]** lot of little rules and instructions and

**[7:59]** do's and don'ts around the specific task

**[8:01]** while going back and forth with AI. And

**[8:03]** I noticed that those little rules and

**[8:05]** and instructions get completely lost

**[8:07]** with the slash compact. And this is

**[8:08]** exactly what the refresh skill also

**[8:10]** does. It looks first of all of the

**[8:11]** status, where are we in the process in

**[8:13]** this chat? It looked at what worked,

**[8:15]** what didn't work, and all the rules.

**[8:17]** They write They write down the specific

**[8:19]** rules and instructions and the do's and

**[8:21]** don'ts that the user gave inside of that

**[8:23]** chat and takes them into the new chat

**[8:25]** session. And lastly, which is the

**[8:27]** biggest one for me, because when I'm

**[8:29]** using AI, for example, for my YouTube

**[8:31]** ideation or my copywriting tasks or many

**[8:33]** other things, I often feed a lot of

**[8:35]** context docs to my AI to get a full

**[8:37]** understanding of me, my business, my ICP

**[8:40]** before giving me outputs. For example,

**[8:41]** you can see here in one of my YouTube

**[8:42]** ideation chats, I let it read my

**[8:44]** strategy, my ICP, my brand, some of my

**[8:46]** old video transcripts, and some more uh

**[8:49]** documents because it just improves the

**[8:50]** outputs and they get far more relevant

**[8:52]** in my experience. And the problem with

**[8:54]** the slash compact skill is it basically

**[8:56]** makes a very tiny summary of each of

**[8:58]** these files, which means again I have to

**[8:59]** re-prompt to read all of these files or

**[9:02]** re-feed this context each time I start a

**[9:04]** new chat. And this is the next thing

**[9:06]** that the refresh skill does. It

**[9:08]** basically lists out all of the context

**[9:09]** docs that were fed inside of this chat

**[9:12]** and instructs the next session to first

**[9:14]** read all of these docs before actually

**[9:16]** continuing with the task, which for me

**[9:18]** just creates so much less friction in

**[9:20]** the process of transferring this into a

**[9:22]** new chat that I actually start doing it

**[9:25]** and actually can get far better outputs

**[9:26]** because I'm not, you know, uh prompting

**[9:28]** back and forth in a context window

**[9:30]** that's actually in the dumb zone. So,

**[9:32]** let me show you some examples of how

**[9:33]** this skill works in practice. So, here I

**[9:35]** used it, for example, in one of my uh

**[9:37]** YouTube preparation chats where I do

**[9:39]** anything from title ideation to research

**[9:41]** to outline generation to script

**[9:42]** reviewing and more. But, because I do

**[9:44]** that, of course, it reaches that 400k

**[9:46]** mark pretty quick. So, after a long

**[9:48]** session here, I used that refresh skill.

**[9:50]** What the skill always does is it first

**[9:52]** asks you about what you want to do in

**[9:54]** your next session. Because depending on

**[9:56]** what I want to do, it can then actually

**[9:57]** save the relevant context based on that

**[9:59]** goal. Now, in this case, I said I want

**[10:01]** to continue working on the same video.

**[10:02]** And what the skill then does is it first

**[10:05]** starts creating a few files and adding

**[10:07]** them into the folder that I selected at

**[10:09]** the start of this chat. One around the

**[10:11]** outline that we confirmed for this video

**[10:13]** in this chat, one around the intro, one

**[10:15]** about the research findings, uh one

**[10:17]** around the decisions and rules.

**[10:19]** Basically, a very comprehensive summary

**[10:21]** with all of the relevant context from

**[10:22]** this chat and the history that we need

**[10:24]** the next session to know. And then it

**[10:26]** creates a prompt for the new session in

**[10:29]** Claude where it first of all states the

**[10:30]** goal for this task. It then directly

**[10:33]** gives an instruction of read all of

**[10:35]** these files first. So, it basically

**[10:36]** tells Claude in that new session to

**[10:38]** first read all of these files that it

**[10:40]** just created. And it also points to all

**[10:42]** of the other context um we used inside

**[10:45]** of this chat like my strategy, my ICP,

**[10:47]** my brand, and some YouTube transcripts.

**[10:49]** Now, this is of course especially

**[10:51]** powerful and relevant if you already use

**[10:53]** a lot of context in your chat or are

**[10:55]** using a second brain. And then lastly,

**[10:57]** it adds a few sections on uh where

**[11:00]** things stand and all of the specific

**[11:02]** rules and instructions that I've given

**[11:03]** in this chat, what worked in this chat

**[11:06]** and what didn't work and what

**[11:07]** corrections were made. We can then just

**[11:08]** copy this, go to a new task, make sure

**[11:11]** that we select the same folder as we

**[11:13]** worked in in the previous chat. That's

**[11:15]** why you always want to select a folder

**[11:17]** when you work in uh co-work or Claude

**[11:18]** code. It's just a habit you want to get

**[11:20]** into even if you haven't set up a second

**[11:22]** brain or use a lot of context yet. And

**[11:24]** once you paste that in, you see that it

**[11:26]** starts reading all of the context files

**[11:28]** before doing anything else. So, you can

**[11:29]** see by reading all of this relevant

**[11:31]** context around the last chat and the

**[11:33]** context it used in our last chat, it is

**[11:35]** immediately primed to continue on that

**[11:37]** same task. It knows the status, it knows

**[11:40]** the specific roles I've given in the

**[11:41]** last chat. I've also been using this on

**[11:44]** these chats where I keep coming back to

**[11:45]** like my newsletter email copy

**[11:48]** optimization chats cuz as you can see

**[11:49]** this has just become way too long over

**[11:51]** time. So, same thing here. Use my

**[11:53]** refresh skill to get a fresh session

**[11:55]** while still having all of those specific

**[11:56]** instructions, the context docs, and

**[11:59]** examples are still saved. There's a

**[12:01]** second use case you want to start using

**[12:02]** this for, which is when you're actually

**[12:04]** veering off your original task and start

**[12:06]** using that same chat window for new type

**[12:09]** of task. I know this is also an issue

**[12:11]** and a trap many people fall into

**[12:13]** including myself. For example, if I now

**[12:15]** in a YouTube ideation chat want to

**[12:18]** create a newsletter out of the context

**[12:20]** that I already have inside of this this

**[12:22]** chat, which is great because of course

**[12:24]** it already has lots of context around

**[12:25]** this topic, I shouldn't actually start

**[12:28]** doing that in that same chat because of

**[12:30]** course I start polluting the context

**[12:31]** window. Claude completely drifts off

**[12:33]** from the original task. So, it's far

**[12:35]** better to use the refresh skill because

**[12:37]** you still keep that same context but

**[12:41]** use it for a new type of task in a fresh

**[12:42]** window. So, you can see for this YouTube

**[12:44]** video I used the refresh but in this

**[12:46]** case I told it to I want to create a

**[12:48]** newsletter based on the context in this

**[12:49]** chat. It then did the same again,

**[12:52]** created some files, created a prompt,

**[12:54]** pasted that into a new window, it read

**[12:56]** all the relevant files, and then

**[12:58]** actually started using my newsletter

**[12:59]** skill right away. Again, you can

**[13:01]** download the skill for free in the first

**[13:02]** link in the description below. It is a

**[13:04]** little bit of a habit you have to get

**[13:05]** into but I highly recommend it cuz first

**[13:08]** of all if you start tracking your

**[13:09]** context window with {slash} context, if

**[13:11]** you get in the habit of that, it is

**[13:13]** really going to improve the way you use

**[13:15]** AI and the outputs you'll get from AI.

**[13:17]** And second, once you start doing that

**[13:19]** highly recommend starting to use this

**[13:21]** refresh skill more and more and maybe

**[13:23]** earlier and earlier in your context

**[13:24]** windows because you'll be surprised how

**[13:26]** much better your outputs become in

**[13:28]** general. Also, if you want access to all

**[13:30]** of the skills that me and my team are

**[13:31]** building out, including workflow

**[13:33]** specific ones for sales, marketing,

**[13:35]** operations,

**[13:36]** and general business skills, you can

**[13:38]** check out my AI accelerator in the

**[13:39]** second link in the description below. We

**[13:40]** also have unlimited one-on-one live tech

**[13:42]** help, full cloud courses, and courses on

**[13:45]** setting up your own AI OS and second

**[13:47]** brain, and a community of serious

**[13:48]** professionals and business owners. So,

**[13:50]** if that's interesting to you, you can

**[13:52]** check it out in the second link in the

**[13:53]** description below. Also, credits to Matt

**[13:55]** Pocock who came up with the handoff

**[13:56]** skill,

**[13:57]** which inspired me to actually build this

**[13:59]** refresh skill. The handoff skill works

**[14:01]** in a similar way, but is more of an

**[14:02]** engineering skill. I

**[14:03]** built the refresh skill more for

**[14:05]** knowledge type work. So, again, credits

**[14:08]** to Matt Pocock. Definitely follow him if

**[14:10]** you don't know him yet. He's a great

**[14:12]** creator. Thank you so much for watching,

**[14:13]** and if you want to learn eight more

**[14:15]** skills that I use almost every day, you

**[14:17]** can check out the video here above.
