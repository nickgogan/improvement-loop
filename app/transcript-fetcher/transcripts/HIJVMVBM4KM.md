# Transcript: When to Use Claude Agent SDK: the Agent Harness explained

**URL:** https://www.youtube.com/watch?v=HIJVMVBM4KM
**Segments:** 410
**Channel:** Edward Donner
**Duration:** 14:30
**Uploaded:** 2026-06-19

---

## Full Text

Claude Agent SDK is an exciting, but also a perplexing product. When you really understand what it is and how it's positioned, and that takes a second, you're left with this question of, "Okay, but then why would I ever use Claude Agent SDK when I could do all of that with the Claude code CLI?" Well, I'm going to explain how it's positioned, and then I'm going to answer that question. But, I'm going to start by explaining the term harness and what an agent harness is. It's very much in vogue at the moment. Remember that an agent is where you have an LLM with tools in a loop to achieve a goal. That's the definition of an AI agent. Well, there's another way that you can describe an AI agent, too. It's also popular to say that an agent is where you have an LLM in a harness. An LLM plus a harness is an agent. In other words, all those other things, the tools, the loop, the goal, they form the harness. And that's what we mean when we talk about an agent harness. And that is where Claude Agent SDK fits in. So, suppose you want to build your own AI agent. Well, you're going to have to call an LLM and put it in some kind of a harness. And you could do this just by making direct API calls to LLMs, but there are some frameworks, some libraries out there that make it easier for you. They do some of the job for you. And there's in fact a whole spectrum of different frameworks in terms of how much of a helping hand they give you. So, on one end of the spectrum are lightweight agent frameworks. And these are things like OpenAI Agents SDK and Google ADK that make it easier to do things like calling tools. That's on one end. On the other end, there are batteries included agent harnesses that take care of everything for you. A opinionated setup out of the box. They handle tools, they've got built-in tools, they do planning, they have sub-agents, they compact the context, they deal with the sandbox and memory and all of that. And they are sometimes called agent harnesses. And examples of agent harnesses include LangChain's deep agents and of course Claude agent SDK. And it makes sense to think of that when you want to get all the functionality that you might have in Claude code and be able to have that in an agent SDK that you can deliver. And perhaps the only special thing about the Claude agent SDK compared to the others is that you can only use it or at least you're only supposed to use it with Anthropic's models. That's how it's designed to be used where things like LangChain deep agents can be used with any models. The Claude agent SDK itself is wonderfully simple to use as you will see there is just this query function that we will call and you iterate over the results. It's an SDK that lets you programmatically call Claude code. It's as simple as that. Here are some things that Anthropic says about it. They say, "Build AI agents that autonomously read files, run commands, search the web, edit code and more. It gives you the same tools, agent loop and context management that power Claude code, programmable in Python and TS." And then just to make it super clear why you would use this instead of one of the lightweight frameworks, Anthropic puts on the site, "Look, the SDK includes built-in tools for reading files, running commands, editing code so your agent starts working immediately without you having to implement tool execution." All right, got it. We understand why you would pick Claude agent SDK over a lightweight framework. But that kind of begs the question, "Okay, but why would you drive it from Python code when you can drive it from the Claude code CLI really effectively? It's got all of the tooling that you might want to handle permissions and how the loop should run and then you can just run it and ask your questions and interact that way. Why interact through Python code when you can interact effectively through the CLI? And that's what I will show you right now and to do it we're going to go to the lab." And I'm in a repo called tutor and I'll put details in the description below and let me walk you through using the Claude agent SDK. So it's the same engine that powers Claude Code exposed through this one function, query, giving us a way to programmatically drive Claude Code through software rather than the CLI. So, in order to answer the question of why not just use the CLI, we are going to go through and build a language tutor. Something It's again, something to try and teach me español, but you can have it teach you any language you want. Change it to Esperanto, change it to German, whatever you want, you just change this word here from Spanish to a language of your choice, ancient Greek perhaps, and you can learn that language. Let's now press ahead with the first step, the simplest possible agent loop to teach us a language using the Claude agent SDK. It's as simple as this. I have a system prompt. You're speaking with a beginner at Spanish and having a friendly conversation to help them learn. And then query, that is the big function and we iterate over it. For message in query, we pass in the prompt all and then we see what comes next and we print it out. That is running right now and note that it doesn't need to use an API key because I'm logged in to Claude AI. It can use your subscription account. If you make this into a product for other people to use, it would have to use your API key. And back we've got a response. That response came from running a Claude Code agent behind the scenes in a short loop that came up with that answer. And now on to step two, we start to give it capabilities. We're going to point it at a local folder we're going to create called data. And data is going to be where it will store all of its information, its knowledge about me. We're going to give it a prompt. You are a warm, patient Spanish tutor and you're going to speak mostly in Spanish and keep memory of your learner as files in your working directory. The vocab I've learned, my grammar, my mistakes, notes about me, and the phases of my learning journey. And then we set up the Claude agent options with this prompt. We tell it we want it to be low reasoning Sonnet models. We give it access to read, write, and edit, and we say that it can edit these files. We give it the current working directory, this data directory, and we say we don't want any settings from the local Claude code config. And that is all it should take. And then, I can say, "My name's Ed, and guess what I like? I like bananas." Okay, so I've now kicked that off, and you can see it's just this very simple loop, again with query as the keyword. And what's happening now is that basically, Claude code is running behind the scenes. It's been programmatically launched. It's running. It's got access to the tools that it has here, the file tools to read and write and edit. There's this data directory that's been created. It will hopefully write some stuff in there as it thinks about how to respond to the fact that apparently, I like bananas. And there we go, it's replied. It's happy with the way that I did it. Let's look in here, and indeed, it's created a bunch of files, too. And you can check out the files that it left itself, the notes that it recorded, including the fact that I know the word for bananas. And then, I've got some notes here about the fact that it can handle compacting your context as it builds up, something you get in the package that you wouldn't get with a lightweight framework. And then, there's stuff here so that you can stream back if you wish to. It's a little bit more verbose here. There's a bit of code here to to test what kind of thing is coming back and stream it as it needs, show when it's using different tools. So, we can see that, but it just gives you a sense that you can do the kinds of things you might do with a lightweight framework, but you can do it operating all of Claude code. And this is showing, and there you see it wrote the vocab at the end of it. We see it using its tools, running its agent loop, responding to me, editing its notes about me right here. Lots going on as Claude code runs programmatically. Okay, now we're going to kick it up a notch. We're going to create another agent, which is going to be an agent that can look at the overall learning journey and can rewrite, update, tune the learning journey based on mistakes I've made, based on the vocab that I'm learning. It's going to be like a second agent, and it's not as much It's not like a sub agent, like when you have Claude code just delegate something off and then come back again. This is going to be like another agent that's running that we can programmatically decide when it runs. So, this is a interesting different dimension that we have more control over because we're writing it programmatically. Let's see. So, we're saying here, "You're a Spanish curriculum coach working quietly behind the scenes. You read in the learner's files and then you prepare the progressive plan in phases." So, this will be continually refining the learning journey phases, and that's something that our main agent is going to be reading. So, this can be happening in parallel. So, we set up those options. I've got like this function, refine journey, right here, and then we can kick it off. So, I'm going to kick off a task to be having my agent refining the journey. And meanwhile, I'm going to tell the main agent, "Oh, I've got two dogs and they're called Mango and Salsa," which is not true, but it's just something to put out there. And uh we will then let it think about that. And meanwhile, the coach will be running at the same time. So, there's now two different Claude code processes going on in parallel. One of them is answering my question. How lovely. Uh Mango and Salsa, I love those names. Uh that is all running. Uh you see I'm getting better with my Spanish. That's all running. But meanwhile, at the same time, the journey is also running, too. So, this is a bit akin to starting two different terminals and running Claude code twice and having them run on tasks independently and yet operating against the same files. So, that's happening, and you can see that it's all going on right now, and I'll see you in a second when everything completes. So, the conversation finished after 33 seconds and then the coach was done after 55 seconds. They were working in parallel and presumably this learning journey phases by I've got a preview of this. This is something that's now been written by the the learning coach. It's written quite a lot. So, that's been developed and that will now automatically be used by the tutor in the future. So, that's pretty cool and yeah, it's going to show the text right there. So, that is now showing a more sophisticated system that we've put together and we are orchestrating these different agents using code. And now I've taken the code we've gone through and I put it into tutor core.py, a module with just the most recent code and then I've also got an app that organizes it into a Gradio app and there's some styling in tutor style and this will allow me to launch a Gradio app to do much the same thing. I will launch it right now and then we will take a look at it. And here it is. This is the Gradio app. Gradio is so easy to work with. I've also I deleted the data directory so we start fresh. And let me start by saying, "Hola." Let's see what we get back. We're talking to our Claude agent. "Hola." Uh okay. Come chilling with us. All right. So, let's see if I can handle this live. Let's give it a shot. Let it do its thing. Uh it says, "You're so Claude." It did that so it knows who he is and I'll definitely say, "Estoy muy bien." There we go. We'll see how we do. Look on the right. We're at level one. We've got 65 out of 100 to get to level two and we're seeing some of the recent words that we've used. Okay, well, it's asked me what I like and I think I know what I like. We can give it the same answer. We can make sure that it's quite clear on my preferences. And look what just happened. The learning journey just appeared on the right. That's been going in the background. The other agent has been working on the learning journey. And meanwhile, the progress just updated, the recent words just updated. We have a real language tutor here that's on the move with two different agents working on it. And conveniently, the learning journey has when it was updated, and it's got lots of useful stuff in here. It's asking me what else do I like to eat? And I don't think I'm going to tell it what I like to eat. I think I'm going to tell it >> [laughter] >> You knew I was going to say that. Uh let's give it something to think about. See how it does that. Uh okay, there we go. And uh hopefully, this will update with those words, and the learning journey will update. It's set so that the learning journey will update every few times that we chat with it, so that it's not like every time that it's changing the learning journey, but as there's something more to say. But of course, the progress and the words updates frequently as it's running its tools behind the scenes. So, this is really giving you that sense that we have Claude Code running behind the scenes, and we're driving it programmatically. And now, it's time to answer that big question. So, obviously, many reasons why you might choose to have a framework like Claude Agent SDK over a lightweight agent framework. But why would you choose it over just using the Claude Code CLI? Well, it might now be obvious to you, but here are three reasons from my perspective. The first reason is the one that Anthropic really pushes home in their docs, which is that if you've worked interactively with Claude Code on some process, you can then productionize it with Claude Agent SDK. I'm not sure how often I would need to do that myself. I can see maybe with a CICD pipeline, it might be useful. But that's certainly one of their stated reasons. But the second reason is the one that really nails it for me. It's about if you want to build your own product, like maybe a language tutor, and you want to have it powered by the Claude agent, the agent that sits behind Claude Code. You love using Claude Code. You love that harness, and you want the power of that harness as the brains behind your product. That's a reason to use the Claude Agent SDK in your product. And the third example is if you have a sophisticated Claude code setup where you want to be able to have, let's say, multiple agents will have slightly different prompts, and you want those prompts to be programmatically constructed, like having the word language passed in, like Spanish, but something more complicated than that. And you could see how trying to stitch all that together every time in the Claude code CLI might be quite a pain, particularly if you're creating lots of agents in different terminals and so on. Well, of course, this gives you a way to programmatically configure a complex Claude code setup, and that makes total sense. I don't think it's as common, but I can see how it might be very useful. Well, that's my take anyway. If you have a different take or other use cases, please put them in the comments below, and I look forward to reading them. And if you enjoyed this, then please do like and subscribe. That's the way I know you're really there and that you want me to keep making these, and I will. And I hope to see you very soon for another video, by which point I'll hopefully be speaking fluent Spanish.

---

## Timestamped Segments

**[0:00]** Claude Agent SDK is an exciting, but

**[0:03]** also a perplexing product. When you

**[0:05]** really understand what it is and how

**[0:07]** it's positioned, and that takes a

**[0:08]** second, you're left with this question

**[0:10]** of, "Okay, but then why would I ever use

**[0:12]** Claude Agent SDK when I could do all of

**[0:15]** that with the Claude code CLI?" Well,

**[0:17]** I'm going to explain how it's

**[0:19]** positioned, and then I'm going to answer

**[0:20]** that question. But, I'm going to start

**[0:22]** by explaining the term harness and what

**[0:24]** an agent harness is. It's very much in

**[0:26]** vogue at the moment. Remember that an

**[0:28]** agent is where you have an LLM with

**[0:31]** tools in a loop to achieve a goal.

**[0:33]** That's the definition of an AI agent.

**[0:36]** Well, there's another way that you can

**[0:37]** describe an AI agent, too. It's also

**[0:39]** popular to say that an agent is where

**[0:41]** you have an LLM in a harness. An LLM

**[0:45]** plus a harness is an agent. In other

**[0:47]** words, all those other things, the

**[0:49]** tools, the loop, the goal, they form the

**[0:51]** harness. And that's what we mean when we

**[0:53]** talk about an agent harness. And that is

**[0:55]** where Claude Agent SDK fits in. So,

**[0:57]** suppose you want to build your own AI

**[1:00]** agent. Well, you're going to have to

**[1:01]** call an LLM and put it in some kind of a

**[1:03]** harness. And you could do this just by

**[1:06]** making direct API calls to LLMs, but

**[1:09]** there are some frameworks, some

**[1:10]** libraries out there that make it easier

**[1:12]** for you. They do some of the job for

**[1:14]** you. And there's in fact a whole

**[1:15]** spectrum of different frameworks in

**[1:18]** terms of how much of a helping hand they

**[1:20]** give you. So, on one end of the spectrum

**[1:22]** are lightweight agent frameworks. And

**[1:24]** these are things like OpenAI Agents SDK

**[1:27]** and Google ADK that make it easier to do

**[1:29]** things like calling tools. That's on one

**[1:32]** end. On the other end, there are

**[1:35]** batteries included agent harnesses that

**[1:38]** take care of everything for you. A

**[1:40]** opinionated setup out of the box. They

**[1:42]** handle tools, they've got built-in

**[1:44]** tools, they do planning, they have

**[1:46]** sub-agents, they compact the context,

**[1:49]** they deal with the sandbox and memory

**[1:51]** and all of that. And they are sometimes

**[1:53]** called agent harnesses. And examples of

**[1:56]** agent harnesses include LangChain's deep

**[1:58]** agents and of course Claude agent SDK.

**[2:01]** And it makes sense to think of that when

**[2:03]** you want to get all the functionality

**[2:04]** that you might have in Claude code and

**[2:06]** be able to have that in an agent SDK

**[2:09]** that you can deliver. And perhaps the

**[2:11]** only special thing about the Claude

**[2:13]** agent SDK compared to the others is that

**[2:15]** you can only use it or at least you're

**[2:16]** only supposed to use it with Anthropic's

**[2:19]** models. That's how it's designed to be

**[2:21]** used where things like LangChain deep

**[2:23]** agents can be used with any models. The

**[2:25]** Claude agent SDK itself is wonderfully

**[2:27]** simple to use as you will see there is

**[2:29]** just this query function that we will

**[2:31]** call and you iterate over the results.

**[2:34]** It's an SDK that lets you

**[2:35]** programmatically call Claude code. It's

**[2:38]** as simple as that. Here are some things

**[2:40]** that Anthropic says about it. They say,

**[2:42]** "Build AI agents that autonomously read

**[2:44]** files, run commands, search the web,

**[2:46]** edit code and more. It gives you the

**[2:48]** same tools, agent loop and context

**[2:50]** management that power Claude code,

**[2:52]** programmable in Python and TS." And then

**[2:55]** just to make it super clear why you

**[2:57]** would use this instead of one of the

**[2:58]** lightweight frameworks, Anthropic puts

**[3:00]** on the site, "Look, the SDK includes

**[3:03]** built-in tools for reading files,

**[3:04]** running commands, editing code so your

**[3:07]** agent starts working immediately without

**[3:09]** you having to implement tool execution."

**[3:12]** All right, got it. We understand why you

**[3:14]** would pick Claude agent SDK over a

**[3:16]** lightweight framework. But that kind of

**[3:18]** begs the question, "Okay, but why would

**[3:20]** you drive it from Python code when you

**[3:23]** can drive it from the Claude code CLI

**[3:25]** really effectively? It's got all of the

**[3:27]** tooling that you might want to handle

**[3:28]** permissions and how the loop should run

**[3:30]** and then you can just run it and ask

**[3:32]** your questions and interact that way.

**[3:34]** Why interact through Python code when

**[3:36]** you can interact effectively through the

**[3:38]** CLI? And that's what I will show you

**[3:40]** right now and to do it we're going to go

**[3:42]** to the lab." And I'm in a repo called

**[3:44]** tutor and I'll put details in the

**[3:45]** description below and let me walk you

**[3:47]** through using the Claude agent SDK. So

**[3:50]** it's the same engine that powers Claude

**[3:52]** Code exposed through this one function,

**[3:54]** query, giving us a way to

**[3:56]** programmatically drive Claude Code

**[3:58]** through software rather than the CLI.

**[4:01]** So, in order to answer the question of

**[4:02]** why not just use the CLI, we are going

**[4:04]** to go through and build a language

**[4:07]** tutor. Something It's again, something

**[4:10]** to try and teach me español, but you can

**[4:12]** have it teach you any language you want.

**[4:15]** Change it to Esperanto, change it to

**[4:17]** German, whatever you want, you just

**[4:18]** change this word here from Spanish to a

**[4:21]** language of your choice, ancient Greek

**[4:23]** perhaps, and you can learn that

**[4:25]** language. Let's now press ahead with the

**[4:27]** first step, the simplest possible agent

**[4:31]** loop to teach us a language using the

**[4:33]** Claude agent SDK. It's as simple as

**[4:36]** this. I have a system prompt. You're

**[4:38]** speaking with a beginner at Spanish and

**[4:40]** having a friendly conversation to help

**[4:42]** them learn. And then query, that is the

**[4:45]** big function and we iterate over it. For

**[4:47]** message in query, we pass in the prompt

**[4:49]** all and then we see what comes next and

**[4:52]** we print it out. That is running right

**[4:54]** now and note that it doesn't need to use

**[4:56]** an API key because I'm logged in to

**[4:58]** Claude AI. It can use your subscription

**[5:00]** account. If you make this into a product

**[5:02]** for other people to use, it would have

**[5:04]** to use your API key. And back we've got

**[5:07]** a response. That response came from

**[5:09]** running a Claude Code agent behind the

**[5:12]** scenes in a short loop that came up with

**[5:15]** that answer. And now on to step two, we

**[5:17]** start to give it capabilities. We're

**[5:19]** going to point it at a local folder

**[5:21]** we're going to create called data. And

**[5:23]** data is going to be where it will store

**[5:25]** all of its information, its knowledge

**[5:27]** about me. We're going to give it a

**[5:29]** prompt. You are a warm, patient Spanish

**[5:32]** tutor and you're going to speak mostly

**[5:34]** in Spanish and keep memory of your

**[5:36]** learner as files in your working

**[5:38]** directory. The vocab I've learned, my

**[5:41]** grammar, my mistakes, notes about me,

**[5:43]** and the phases of my learning journey.

**[5:46]** And then we set up the Claude agent

**[5:48]** options with this prompt. We tell it we

**[5:50]** want it to be low reasoning Sonnet

**[5:52]** models. We give it access to read,

**[5:54]** write, and edit, and we say that it can

**[5:57]** edit these files. We give it the current

**[5:59]** working directory, this data directory,

**[6:02]** and we say we don't want any settings

**[6:04]** from the local Claude code config. And

**[6:06]** that is all it should take. And then, I

**[6:08]** can say, "My name's Ed, and guess what I

**[6:10]** like? I like bananas." Okay, so I've now

**[6:13]** kicked that off, and you can see it's

**[6:15]** just this very simple loop, again with

**[6:17]** query as the keyword. And what's

**[6:19]** happening now is that basically, Claude

**[6:22]** code is running behind the scenes. It's

**[6:24]** been programmatically launched. It's

**[6:26]** running. It's got access to the tools

**[6:28]** that it has here, the file tools to read

**[6:30]** and write and edit. There's this data

**[6:32]** directory that's been created. It will

**[6:34]** hopefully write some stuff in there as

**[6:36]** it thinks about how to respond to the

**[6:38]** fact that apparently, I like bananas.

**[6:40]** And there we go, it's replied. It's

**[6:42]** happy with the way that I did it. Let's

**[6:44]** look in here, and indeed, it's created a

**[6:46]** bunch of files, too. And you can check

**[6:48]** out the files that it left itself, the

**[6:49]** notes that it recorded, including the

**[6:51]** fact that I know the word for bananas.

**[6:54]** And then, I've got some notes here about

**[6:55]** the fact that it can handle compacting

**[6:58]** your context as it builds up, something

**[7:00]** you get in the package that you wouldn't

**[7:02]** get with a lightweight framework. And

**[7:03]** then, there's stuff here so that you can

**[7:05]** stream back if you wish to. It's a

**[7:07]** little bit more verbose here. There's a

**[7:09]** bit of code here to to test what kind of

**[7:11]** thing is coming back and stream it as it

**[7:13]** needs, show when it's using different

**[7:15]** tools. So, we can see that, but it just

**[7:17]** gives you a sense that you can do the

**[7:19]** kinds of things you might do with a

**[7:20]** lightweight framework, but you can do it

**[7:23]** operating all of Claude code. And this

**[7:25]** is showing, and there you see it wrote

**[7:27]** the vocab at the end of it. We see it

**[7:29]** using its tools, running its agent loop,

**[7:32]** responding to me, editing its notes

**[7:34]** about me right here. Lots going on as

**[7:37]** Claude code runs programmatically. Okay,

**[7:39]** now we're going to kick it up a notch.

**[7:40]** We're going to create another agent,

**[7:43]** which is going to be an agent that can

**[7:45]** look at the overall learning journey and

**[7:48]** can rewrite, update, tune the learning

**[7:50]** journey based on mistakes I've made,

**[7:52]** based on the vocab that I'm learning.

**[7:55]** It's going to be like a second agent,

**[7:57]** and it's not as much It's not like a sub

**[7:59]** agent, like when you have Claude code

**[8:01]** just delegate something off and then

**[8:02]** come back again. This is going to be

**[8:04]** like another agent that's running that

**[8:06]** we can programmatically decide when it

**[8:09]** runs. So, this is a interesting

**[8:11]** different dimension that we have more

**[8:13]** control over because we're writing it

**[8:15]** programmatically. Let's see. So, we're

**[8:17]** saying here, "You're a Spanish

**[8:19]** curriculum coach working quietly behind

**[8:21]** the scenes. You read in the learner's

**[8:24]** files and then you prepare the

**[8:25]** progressive plan in phases." So, this

**[8:28]** will be continually refining the

**[8:30]** learning journey phases, and that's

**[8:32]** something that our main agent is going

**[8:34]** to be reading. So, this can be happening

**[8:36]** in parallel. So, we set up those

**[8:39]** options. I've got like this function,

**[8:41]** refine journey, right here, and then we

**[8:43]** can kick it off. So, I'm going to kick

**[8:45]** off a task to be having my agent

**[8:47]** refining the journey. And meanwhile, I'm

**[8:50]** going to tell the main agent, "Oh, I've

**[8:52]** got two dogs and they're called Mango

**[8:54]** and Salsa," which is not true, but it's

**[8:56]** just something to put out there. And uh

**[8:58]** we will then let it think about that.

**[9:00]** And meanwhile, the coach will be running

**[9:02]** at the same time. So, there's now two

**[9:05]** different Claude code processes going on

**[9:07]** in parallel. One of them is answering my

**[9:10]** question. How lovely. Uh Mango and

**[9:12]** Salsa, I love those names. Uh that is

**[9:15]** all running. Uh you see I'm getting

**[9:16]** better with my Spanish. That's all

**[9:18]** running. But meanwhile, at the same

**[9:20]** time, the journey is also running, too.

**[9:23]** So, this is a bit akin to starting two

**[9:25]** different terminals and running Claude

**[9:27]** code twice and having them run on tasks

**[9:29]** independently and yet operating against

**[9:32]** the same files. So, that's happening,

**[9:34]** and you can see that it's all going on

**[9:36]** right now, and I'll see you in a second

**[9:38]** when everything completes. So, the

**[9:39]** conversation finished after 33 seconds

**[9:42]** and then the coach was done after 55

**[9:44]** seconds. They were working in parallel

**[9:47]** and presumably this learning journey

**[9:49]** phases by I've got a preview of this.

**[9:51]** This is something that's now been

**[9:52]** written by the the learning coach. It's

**[9:55]** written quite a lot. So, that's been

**[9:56]** developed and that will now

**[9:57]** automatically be used by the tutor in

**[10:00]** the future. So, that's pretty cool and

**[10:03]** yeah, it's going to show the text right

**[10:04]** there. So, that is now showing a more

**[10:07]** sophisticated system that we've put

**[10:09]** together and we are orchestrating these

**[10:11]** different agents using code. And now

**[10:13]** I've taken the code we've gone through

**[10:14]** and I put it into tutor core.py, a

**[10:17]** module with just the most recent code

**[10:19]** and then I've also got an app that

**[10:21]** organizes it into a Gradio app and

**[10:23]** there's some styling in tutor style and

**[10:26]** this will allow me to launch a Gradio

**[10:29]** app to do much the same thing. I will

**[10:32]** launch it right now and then we will

**[10:33]** take a look at it. And here it is. This

**[10:35]** is the Gradio app. Gradio is so easy to

**[10:37]** work with. I've also I deleted the data

**[10:39]** directory so we start fresh. And let me

**[10:41]** start by saying, "Hola." Let's see what

**[10:43]** we get back. We're talking to our Claude

**[10:46]** agent. "Hola." Uh okay. Come chilling

**[10:50]** with us. All right. So, let's see if I

**[10:52]** can handle this live.

**[10:55]** Let's give it a shot. Let it do its

**[10:58]** thing.

**[11:00]** Uh it says, "You're so Claude." It did

**[11:01]** that so it knows who he is and I'll

**[11:03]** definitely say, "Estoy

**[11:06]** muy bien."

**[11:09]** There we go. We'll see how we do. Look

**[11:11]** on the right. We're at level one. We've

**[11:13]** got 65 out of 100 to get to level two

**[11:16]** and we're seeing some of the recent

**[11:17]** words that we've used. Okay, well, it's

**[11:19]** asked me what I like and I think I know

**[11:21]** what I like. We can give it the same

**[11:24]** answer. We can make sure that it's quite

**[11:26]** clear on my preferences. And look what

**[11:29]** just happened. The learning journey just

**[11:31]** appeared on the right. That's been going

**[11:34]** in the background. The other agent has

**[11:36]** been working on the learning journey.

**[11:38]** And meanwhile, the progress just

**[11:39]** updated, the recent words just updated.

**[11:42]** We have a real language tutor here

**[11:45]** that's on the move with two different

**[11:46]** agents working on it. And conveniently,

**[11:49]** the learning journey has when it was

**[11:50]** updated, and it's got lots of useful

**[11:52]** stuff in here. It's asking me what else

**[11:55]** do I like to eat? And I don't think I'm

**[11:56]** going to tell it what I like to eat. I

**[11:57]** think I'm going to tell it

**[11:59]** >> [laughter]

**[11:59]** >> You knew I was going to say that.

**[12:01]** Uh let's give it something to think

**[12:02]** about. See how it does that.

**[12:04]** Uh okay, there we go. And uh hopefully,

**[12:07]** this will update with those words, and

**[12:09]** the learning journey will update. It's

**[12:11]** set so that the learning journey will

**[12:12]** update every few times that we chat with

**[12:14]** it, so that it's not like every time

**[12:17]** that it's changing the learning journey,

**[12:18]** but as there's something more to say.

**[12:19]** But of course, the progress and the

**[12:21]** words updates frequently as it's running

**[12:23]** its tools behind the scenes. So, this is

**[12:26]** really giving you that sense that we

**[12:28]** have Claude Code running behind the

**[12:30]** scenes, and we're driving it

**[12:31]** programmatically. And now, it's time to

**[12:34]** answer that big question. So, obviously,

**[12:36]** many reasons why you might choose to

**[12:38]** have a framework like Claude Agent SDK

**[12:40]** over a lightweight agent framework. But

**[12:42]** why would you choose it over just using

**[12:44]** the Claude Code CLI? Well, it might now

**[12:47]** be obvious to you, but here are three

**[12:48]** reasons from my perspective. The first

**[12:50]** reason is the one that Anthropic really

**[12:52]** pushes home in their docs, which is that

**[12:54]** if you've worked interactively with

**[12:55]** Claude Code on some process, you can

**[12:58]** then productionize it with Claude Agent

**[13:00]** SDK. I'm not sure how often I would need

**[13:03]** to do that myself. I can see maybe with

**[13:05]** a CICD pipeline, it might be useful. But

**[13:07]** that's certainly one of their stated

**[13:09]** reasons. But the second reason is the

**[13:11]** one that really nails it for me. It's

**[13:13]** about if you want to build your own

**[13:15]** product, like maybe a language tutor,

**[13:17]** and you want to have it powered by the

**[13:20]** Claude agent, the agent that sits behind

**[13:22]** Claude Code. You love using Claude Code.

**[13:24]** You love that harness, and you want the

**[13:26]** power of that harness as the brains

**[13:28]** behind your product. That's a reason to

**[13:31]** use the Claude Agent SDK in your

**[13:34]** product. And the third example is if you

**[13:36]** have a sophisticated Claude code setup

**[13:39]** where you want to be able to have, let's

**[13:40]** say, multiple agents will have slightly

**[13:42]** different prompts, and you want those

**[13:43]** prompts to be programmatically

**[13:45]** constructed, like having the word

**[13:46]** language passed in, like Spanish, but

**[13:48]** something more complicated than that.

**[13:50]** And you could see how trying to stitch

**[13:52]** all that together every time in the

**[13:54]** Claude code CLI might be quite a pain,

**[13:56]** particularly if you're creating lots of

**[13:58]** agents in different terminals and so on.

**[14:00]** Well, of course, this gives you a way to

**[14:02]** programmatically configure a complex

**[14:05]** Claude code setup, and that makes total

**[14:07]** sense. I don't think it's as common, but

**[14:09]** I can see how it might be very useful.

**[14:11]** Well, that's my take anyway. If you have

**[14:13]** a different take or other use cases,

**[14:15]** please put them in the comments below,

**[14:16]** and I look forward to reading them. And

**[14:18]** if you enjoyed this, then please do like

**[14:20]** and subscribe. That's the way I know

**[14:21]** you're really there and that you want me

**[14:22]** to keep making these, and I will. And I

**[14:25]** hope to see you very soon for another

**[14:26]** video, by which point I'll hopefully be

**[14:28]** speaking fluent Spanish.
