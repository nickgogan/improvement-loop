# Transcript: I Built My Own AI Memory by Talking to Claude. It Did 80% Itself.

**URL:** https://www.youtube.com/watch?v=HgAQOkG_v8c
**Segments:** 459
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 16:16
**Uploaded:** 2026-07-01

---

## Full Text

You woke up last week to the two best AI models on the planet getting locked behind a government door and we're all standing on the wrong side of it. Fable's gone. ChatGPT 5.6 shipped to a handful of vetted shops and nobody else. If your work runs on whoever's winning this month, you learn how fast that can change. So, here is the part nobody can lock up. Your memory, your standards, and your skills. I want you to think about how you can own that, rent the intelligence, and swap the models out so the bands don't matter. By the end of this video, you're going to know how to build that system and the agent on your computer is going to be able to carry out all the technical parts for you. I'm going to tell you the story of how an AI agent beat an insurance company and that's not even the real story. The real story is about how the role of memory in agents is evolving and the way we build agentic systems for ourselves. We don't have to wait is evolving too. And not a perfect assistant for your whole life, just a clear agentic loop with an agent that starts from your context, knows what you meant, knows what it can do, what it can't do, and knows where to stop. And by the way, an agent that can prove that it did what it did on purpose. So, Nikita wrote that his open claw quote accidentally started a fight with lemonade insurance because it misinterpreted his response. That is actually a very bad thing even if he won the fight eventually. Lemonade had declined a claim involving his best friend. The agent found the rejection email and offered a draft reply and Nikita didn't want this to happen so he ignored the draft. And then according to Nikita, the agent just sent it for him. And after that email, Lemonade started reinvestigating the case instead of rejecting it immediately. Now, that's an incredible story, but I don't want you to have that kind of incredible story because if an agent will ignore you and send stuff anyway, the agent is out of policy and very, very risky even if in this one particular instance, Nikita was able to roll the dice and it worked out. Now, I get that fighting insurance is kind of the dream version of personal AI. I love it. I think it's a great task. I think it allows you to use an agent in ways that make an agent work well, right? Agents are good at reviewing legal minutia. They're good at digging into detail. They're good at doing tedious work. All of the stuff you would need to file a uh response to a denial that would be listened to. So, that makes sense. The problem is that the agent didn't do it with authority. That the agent misunderstood. That the agent had memory issues, policy issues, all kinds of things that led to problems. What has changed between that moment, which was back in January, and now in June of 2026? Now, agents have got much better at acting. And intent is one of the central problems of the AI agent. We've made huge progress on connecting intent and acting just in the last 6 months. When you're chatting with the model now, you can communicate intent and it will often get it right, right? It will understand that draft response means draft, not send. There are now things like auto review in Codex that make sure that it will not send if you say draft. Now, back in February, when I first started talking about agentic systems, the key problem was kind of what I just described in that story. AI forgets you. It doesn't listen. It doesn't pay attention. So often chats would start cold. You had to explain your preferences again, and your memory didn't belong to you. Now, that world is already changing under our feet. And I'm not the only one who recognized that problem. There are many alternatives to open brain out there, which is great. And agents, critically, are no longer just acting in short form. They're taking much longer actions with much larger consequences. And so, memory has had to evolve, too. I've evolved the open brain system to include uh some of Andre Karpathy's work around wiki-style connections. And you You have that in open brain as part of the framework. I've added other pieces also, open skills and most recently open engine, which connects everything to an agent-to-agent task interaction framework. All of that is designed to get you from a world where agents are a thing out there to a world where agents actually serve you. But, the problem remains the build. And I have had to I have personally troubleshot people who are struggling with building these systems and I have realized that when I say something is easy, it doesn't always feel easy to you. And I want to call out one of the biggest differences between the moment that I just described with the insurance story, with that agent, the moment even that I described open brain back in February and today, June 2026. And that difference is that agents are so good at following intent, they now actually just build it for you. I'm estimating and I've worked with other folks on this, you can build 80% of the open brain stack just by talking to your agent very simply, in a way that you couldn't in February. And I think that that's worth calling out because that's a tremendous jump in just a couple of months. Ultimately, the reason why this stack matters is because agents can act on the wrong version of your intent very quickly and frontier model companies owning the relationship between your intent and intelligence and action is really risky for you long-term. Frankly, we've seen that just in the last few days with GLM 5.2 coming out from an open source perspective while Fable and chat GPT 5.6 are all banned. I mean, long-term, we're in a position where we as consumers have to hedge our bets. We have to have a tool stack that we own. And you may not realize this, but you already have tools like Claude and Codex that can essentially build most of this stack for you. You don't actually even need to get to open Claude, although if you have it, that's great. It will plug right into the open engine format, so will Hermius. You can start wherever you are on one repeated part of your life or work. A client follow-up, a frequent traveler problem that you face, a weekly planning pass, uh or maybe it's the insurance appeal, right? Uh a shared marketing brain. Whatever it is that you get stuck on, where your intent is something you have to repeat all the time, then go there. That's That's where you feel pain. That's where the agent should help you. And then, let your agent, like your Claude, like your Codex, help you build, right? Let it help you build open brain, which carries memories, and open skills, which gives you methods to actually get work done that are suited to you, and transport easily between Claude, between uh OpenAI's agents, between Gemini, etc., etc. Or in the open-source model you choose. And then, agents can build the work layer for you, too. Open engine is just a way to orchestrate work across multiple agents, so that if you want to get big work done across Claude, across Codex, across ChatGPT, you name it, right? Across open claw, you can get it all done in one thing. People have built travel planning memory with this. People have built shared marketing brains in the community. People have built cross-tool context between Claude and ChatGPT and Kimmy. And they've built agents that can read tickets into a tracker and hand work to another agent. I want more intentional agent stories, and fewer accidental ones. The The insurance example, I want people who intended to fight insurance and won. Because the agents are getting good enough to move the world. They are the lever. Archimedes lever that moves the world. The question is whether they're moving from your memory, your standards, and your intent, or from whatever default memory stack the next agent company is giving to you. And the reason this is worth doing now is that the build barrier has dropped. A few months ago, even if you believed in the open brain concept, I get that it was hard, right? The database, the setup, the SQL, the configs, the command line steps. I helped troubleshoot people through that. I've done it myself, and it felt like a technical project. It doesn't feel like a technical project anymore when Claude and Codex and tools like them can walk you through that build almost by themselves. Now, you can still own the human parts. You can say these are the accounts I want to give you access to. These are my permissions. This is the final approval. These are my settings. Uh stuff that involves trust belongs to you. But, the technical middle has gotten so much easier, it is worth naming again. It is worth calling out. Because if a repeated part of your life can get sorted with an agent, and now you don't even have to face the technical build challenge in the same way, that's a big deal. So, I want to make this real with a coffee store. I'm a coffee guy. I used to run a coffee company, and I have colleagues in my Slack, cobuilders with me, who are also coffee people. And both of us stumbled onto the same thing. So, instead of having a generic Google Map search for cafes, both of us figured out that an agent backed by our preferences in Open Brain could go and plan an entire morning for us much more effectively because the agent knew our preferences. By the way, we don't have the same coffee preferences. We live in different parts of the country, etc. But, we both figured this out, and I was able to use it when I was in Japan to do some coffee hunting that I wouldn't have been able to do otherwise, and you can easily input your coffee preferences and get much more customized results as well. That's a tiny tiny little example. You might be like, building an agent for coffee, I would never do that. No, pick the pain that works for you. I don't care if it's coffee. I care that the pain is better because you have an agent that understands the tradeoffs, that understands the the decisions that are right for you because your memory is yours. If you want the world where your agent will fight insurance for you and monitor your email for you, That world runs through your memory, your skills, your ability to orchestrate agents. It should not run through some company that gets stuck in regulation trying to figure out what's good for you. Now, you can use intelligence from whatever source you want, right? You can use it from Open AI or Anthropic or from Kimmy K2 or Quan or whatever. But, your memories are yours, your skills are yours, and they should stay that way. It's going to be more like the agent knows my preferences. The agent knows that I do want to battle every single insurance claim. The agent knows how to go about doing the research to do that well, and I get to approve the drafts, by the way. It doesn't just get sent without me. We need control over our agents. We need agents that belong to us, agents that have memory that we understand, agents that have a scope of action that we approve of. That's why my open engine approach emphasizes that you should be able to see when an agent picks up a task, right? A ticketing system is actually just a good primitive for that cuz you can see, "Oh, it picked up the task. Oh, it wrote something." It's not hidden away in chain of thought, right? It's not like erased in the middle of a chat that I can't find. Have you ever tried to find the chats in ChatGPT or in Claude? I'm just like, "Oh my gosh, I searched for that keyword. It's not there." They need to fix search, but you also need to not depend on that to get agentic work done. You need to have an external scaffolding that lets you be confident that you can get your work done regardless. But, we can control where our memories live, we can control our skills, we can control how work gets done and ensures that it has a a status and an approval layer where relevant, and agent handoffs that we can read and escalations to humans that make sense. So, jump in, the water's warm, and the ability to build is like 1/5 or less technical than it was back in February. I I I reminds you how quickly this is changing, and I hope that reminds you and encourages you that you too can do this. Even though this has technical primitives underneath like a SQL database, you can do it without really digging in and understanding the details of that because the agents are good enough to explain what it means in practice for you. And I think that's one of the things I really struggle with with where we are in the agentic revolution. Because to be honest with you, Claude and Codex are very code-shaped today. And most of the world is not code-shaped. Most of the world is non-technically skilled. And that's just as legitimate a skill set. And so we need to find ways to work with our agents that feel safe if we're non-technical. And a lot of the project that I've been working on with Open Brain over the last 5 months is basically making it easier and easier and easier for you if you are non-technical to use agents to work with that GitHub repo, to work with that code, so it's not scary, so it's not non-transparent, so it doesn't do things you don't want it to do, and so you actually get your work done, and actually do things like weekly planning and family logistics, and the work blocks that you want to protect, and you feed the projects that keep getting started, or whatever it is that you are building this agent for. Giving your agents memory and skills and a clear framework to do stuff in in order to get to that world. And it has never, ever, ever been easier. It's never been easier. So if this is you, if you're like, "Ah, I'm almost there. I want to build." This is your invitation. I am waving the green flag here. I am telling you the agents can get it done. The agents can help you build agents. And that's one of the biggest differences between now and when I made my original Open Brain tutorial, which like 200,000 of you have watched, which is amazing, and I love that. It's easier now. It It's like five times easier now. I know 200,000 of you haven't built this, and I think it's worth building so you own your memory and like these guys who are trying to get approval from Washington for this and that don't own your memory. You should keep your judgment. The agent can carry the technical steps to get this work done for you now, and it could still defer to you about what matters, which things you want to remember, which things are skills that you want to say this is my domain expertise, I want to preserve it. I don't want Claude to own that skill. I don't want OpenAI to own that skill. I want to own that skill. The assistant race is just going to get more seductive from here. The demos will get better. The phone integrations will get smoother. The voices will get warmer. Every one of those improvements is designed to get your attention. It's designed to get us to put our memory and our focus and our work into these apps. The company that holds the memory holds the part that makes the assistant feel personal. I would rather build that part myself. And that is why I keep coming back to this. Intelligence is not a personal thing. Memory is personal. And you know, in February a lot of that was about getting your agents to remember you. And now it it really is about giving your agents a platform to jump from and act from on your behalf cuz there's so much more powerful. Pick a recurring situation you're tired of explaining. Write down the context that would change that answer. Point your agent at the guide, which I will link to, keep control of accounts and secrets and permissions and approval at your level, and then tell it to run and practice, right? And give it feedback. Say, "No, that was wrong. Change this. No, that was wrong. Change this." Agents take a while to break in. Once you start to get into the rhythm of using them, it gets easier and easier and easier and easier. And now even that first step, even getting the shoe so you can wear it, agents can help with that in a way they couldn't back in February. And that is the key. That is the key I want you to take away. And the prize for unlocking that door, the prize is just owning the context every future agent will need but before it even arrives. So, when an agent comes, you can just plug it right in, right? I want you to take advantage of the latest and greatest AI agents that you want to take advantage of. I don't want to pick a favorite, you pick. But you own the memory and you make sure that you rent the intelligence. So the intelligence is something you can apply to your memory, your skills, your orchestration layer, infrastructure that lets the agent work for you. Pick the part of your life that you want to change and let an agent change it for you. I I'm not kidding. You can actually do it. If nothing else, if you know someone who has a really big pain point and maybe it's agent shaped or you know it's agent shaped and you're a builder, go tell them that. Go say, "Hey, this is not that hard. An agent can help you build this." We need positive examples. In fact, if you have positive examples, if you're an open rebuild, if you you built on something else, maybe you built on G brain, I don't care. Put positive examples of why an agent made a difference in your life down here. I would like to see them. I want more people to see positive examples of agents working.

---

## Timestamped Segments

**[0:00]** You woke up last week to the two best AI

**[0:02]** models on the planet getting locked

**[0:04]** behind a government door and we're all

**[0:06]** standing on the wrong side of it.

**[0:08]** Fable's gone. ChatGPT 5.6 shipped to a

**[0:10]** handful of vetted shops and nobody else.

**[0:13]** If your work runs on whoever's winning

**[0:15]** this month, you learn how fast that can

**[0:17]** change. So, here is the part nobody can

**[0:19]** lock up. Your memory, your standards,

**[0:22]** and your skills. I want you to think

**[0:23]** about how you can own that, rent the

**[0:26]** intelligence, and swap the models out so

**[0:28]** the bands don't matter. By the end of

**[0:30]** this video, you're going to know how to

**[0:31]** build that system and the agent on your

**[0:33]** computer is going to be able to carry

**[0:34]** out all the technical parts for you. I'm

**[0:36]** going to tell you the story of how an AI

**[0:38]** agent beat an insurance company and

**[0:40]** that's not even the real story. The real

**[0:42]** story is about how the role of memory in

**[0:45]** agents is evolving and the way we build

**[0:48]** agentic systems for ourselves. We don't

**[0:50]** have to wait is evolving too. And not a

**[0:53]** perfect assistant for your whole life,

**[0:55]** just a clear agentic loop with an agent

**[0:57]** that starts from your context, knows

**[1:00]** what you meant, knows what it can do,

**[1:02]** what it can't do, and knows where to

**[1:04]** stop. And by the way, an agent that can

**[1:06]** prove that it did what it did on

**[1:08]** purpose. So, Nikita wrote that his open

**[1:10]** claw quote accidentally started a fight

**[1:12]** with lemonade insurance because it

**[1:14]** misinterpreted his response. That is

**[1:16]** actually a very bad thing even if he won

**[1:18]** the fight eventually. Lemonade had

**[1:20]** declined a claim involving his best

**[1:22]** friend. The agent found the rejection

**[1:24]** email and offered a draft reply and

**[1:26]** Nikita didn't want this to happen so he

**[1:27]** ignored the draft. And then according to

**[1:29]** Nikita, the agent just sent it for him.

**[1:31]** And after that email, Lemonade started

**[1:33]** reinvestigating the case instead of

**[1:34]** rejecting it immediately. Now, that's an

**[1:36]** incredible story, but I don't want you

**[1:38]** to have that kind of incredible story

**[1:41]** because if an agent will ignore you and

**[1:43]** send stuff anyway, the agent is out of

**[1:45]** policy and very, very risky even if in

**[1:48]** this one particular instance, Nikita was

**[1:50]** able to roll the dice and it worked out.

**[1:52]** Now, I get that fighting insurance is

**[1:54]** kind of the dream version of personal

**[1:56]** AI. I love it. I think it's a great

**[1:58]** task. I think it allows you to use an

**[2:00]** agent in ways that make an agent work

**[2:03]** well, right? Agents are good at

**[2:04]** reviewing legal minutia. They're good at

**[2:06]** digging into detail. They're good at

**[2:08]** doing tedious work. All of the stuff you

**[2:09]** would need to file a

**[2:12]** uh response to a denial that would be

**[2:14]** listened to. So, that makes sense. The

**[2:17]** problem is that the agent didn't do it

**[2:19]** with authority. That the agent

**[2:21]** misunderstood. That the agent had memory

**[2:23]** issues, policy issues, all kinds of

**[2:25]** things that led to problems. What has

**[2:28]** changed between that moment, which was

**[2:31]** back in January, and now in June of

**[2:34]** 2026?

**[2:35]** Now, agents have got much better at

**[2:37]** acting. And intent is one of the central

**[2:40]** problems of the AI agent. We've made

**[2:41]** huge progress on connecting intent and

**[2:44]** acting just in the last 6 months. When

**[2:47]** you're chatting with the model now, you

**[2:49]** can communicate intent and it will often

**[2:52]** get it right, right? It will understand

**[2:54]** that draft response means draft, not

**[2:57]** send. There are now things like auto

**[2:59]** review in Codex that make sure that it

**[3:02]** will not send if you say draft. Now,

**[3:04]** back in February, when I first started

**[3:06]** talking about agentic systems, the key

**[3:09]** problem was kind of what I just

**[3:10]** described in that story. AI forgets you.

**[3:13]** It doesn't listen. It doesn't pay

**[3:14]** attention. So often chats would start

**[3:17]** cold. You had to explain your

**[3:18]** preferences again, and your memory

**[3:20]** didn't belong to you. Now, that world is

**[3:23]** already changing under our feet. And I'm

**[3:25]** not the only one who recognized that

**[3:27]** problem. There are many alternatives to

**[3:29]** open brain out there, which is great.

**[3:31]** And agents, critically, are no longer

**[3:33]** just acting in short form. They're

**[3:36]** taking much longer actions with much

**[3:38]** larger consequences. And so, memory has

**[3:41]** had to evolve, too. I've evolved the

**[3:43]** open brain system to include uh some of

**[3:46]** Andre Karpathy's work around wiki-style

**[3:49]** connections. And you You have that in

**[3:50]** open brain as part of the framework.

**[3:52]** I've added other pieces also, open

**[3:55]** skills and most recently open engine,

**[3:57]** which connects everything to an

**[3:59]** agent-to-agent task interaction

**[4:01]** framework. All of that is designed to

**[4:04]** get you from a world where agents are a

**[4:07]** thing out there to a world where agents

**[4:09]** actually serve you. But, the problem

**[4:13]** remains the build. And I have had to I

**[4:15]** have personally troubleshot people who

**[4:17]** are struggling with building these

**[4:18]** systems and I have realized that when I

**[4:20]** say something is easy, it doesn't always

**[4:22]** feel easy to you. And I want to call out

**[4:25]** one of the biggest differences between

**[4:28]** the moment that I just described with

**[4:30]** the insurance story, with that agent,

**[4:31]** the moment even that I described open

**[4:33]** brain back in February and today, June

**[4:35]** 2026. And that difference is that agents

**[4:38]** are so good at following intent, they

**[4:42]** now actually just build it for you. I'm

**[4:45]** estimating and I've worked with other

**[4:47]** folks on this, you can build 80% of the

**[4:50]** open brain stack just by talking to your

**[4:52]** agent very simply, in a way that you

**[4:54]** couldn't in February. And I think that

**[4:55]** that's worth calling out because that's

**[4:57]** a tremendous jump in just a couple of

**[4:59]** months. Ultimately, the reason why this

**[5:01]** stack matters is because agents can act

**[5:05]** on the wrong version of your intent very

**[5:07]** quickly and frontier model companies

**[5:09]** owning the relationship between your

**[5:12]** intent and intelligence and action is

**[5:14]** really risky for you long-term. Frankly,

**[5:16]** we've seen that just in the last few

**[5:19]** days with GLM 5.2 coming out from an

**[5:22]** open source perspective while Fable and

**[5:24]** chat GPT 5.6 are all banned. I mean,

**[5:27]** long-term, we're in a position where we

**[5:30]** as consumers have to hedge our bets. We

**[5:31]** have to have a tool stack that we own.

**[5:34]** And you may not realize this, but you

**[5:36]** already have tools like Claude and Codex

**[5:38]** that can essentially build most of this

**[5:40]** stack for you. You don't actually even

**[5:42]** need to get to open Claude, although if

**[5:43]** you have it, that's great. It will plug

**[5:45]** right into the open engine format, so

**[5:47]** will Hermius. You can start wherever you

**[5:49]** are on one repeated part of your life or

**[5:51]** work. A client follow-up, a frequent

**[5:53]** traveler problem that you face, a weekly

**[5:55]** planning pass, uh or maybe it's the

**[5:57]** insurance appeal, right? Uh a shared

**[5:59]** marketing brain. Whatever it is that you

**[6:02]** get stuck on, where your intent is

**[6:04]** something you have to repeat all the

**[6:06]** time, then go there. That's That's where

**[6:10]** you feel pain. That's where the agent

**[6:12]** should help you. And then, let your

**[6:15]** agent, like your Claude, like your

**[6:16]** Codex, help you build, right? Let it

**[6:19]** help you build open brain, which carries

**[6:20]** memories, and open skills, which gives

**[6:23]** you methods to actually get work done

**[6:26]** that are suited to you, and transport

**[6:28]** easily between Claude, between uh

**[6:31]** OpenAI's agents, between Gemini, etc.,

**[6:34]** etc. Or in the open-source model you

**[6:35]** choose. And then, agents can build the

**[6:38]** work layer for you, too. Open engine is

**[6:40]** just a way to orchestrate work across

**[6:42]** multiple agents, so that if you want to

**[6:43]** get big work done across Claude, across

**[6:46]** Codex, across ChatGPT, you name it,

**[6:48]** right? Across open claw, you can get it

**[6:50]** all done in one thing. People have built

**[6:52]** travel planning memory with this. People

**[6:54]** have built shared marketing brains in

**[6:55]** the community. People have built

**[6:56]** cross-tool context between Claude and

**[6:58]** ChatGPT and Kimmy. And they've built

**[7:00]** agents that can read tickets into a

**[7:02]** tracker and hand work to another agent.

**[7:04]** I want more intentional agent stories,

**[7:08]** and fewer accidental ones. The The

**[7:10]** insurance example, I want people who

**[7:12]** intended to fight insurance and won.

**[7:14]** Because the agents are getting good

**[7:15]** enough to move the world. They are the

**[7:16]** lever. Archimedes lever that moves the

**[7:19]** world. The question is whether they're

**[7:20]** moving from your memory, your standards,

**[7:22]** and your intent, or from whatever

**[7:24]** default memory stack the next agent

**[7:27]** company is giving to you. And the reason

**[7:29]** this is worth doing now is that the

**[7:30]** build barrier has dropped. A few months

**[7:33]** ago, even if you believed in the open

**[7:35]** brain concept, I get that it was hard,

**[7:37]** right? The database, the setup, the SQL,

**[7:39]** the configs, the command line steps. I

**[7:41]** helped troubleshoot people through that.

**[7:43]** I've done it myself, and it felt like a

**[7:45]** technical project. It doesn't feel like

**[7:48]** a technical project anymore when Claude

**[7:50]** and Codex and tools like them can walk

**[7:52]** you through that build almost by

**[7:55]** themselves. Now, you can still own the

**[7:56]** human parts. You can say these are the

**[7:58]** accounts I want to give you access to.

**[8:00]** These are my permissions. This is the

**[8:01]** final approval. These are my settings.

**[8:04]** Uh stuff that involves trust belongs to

**[8:05]** you. But, the technical middle has

**[8:07]** gotten so much easier, it is worth

**[8:11]** naming again. It is worth calling out.

**[8:14]** Because if a repeated part of your life

**[8:16]** can get sorted with an agent, and now

**[8:19]** you don't even have to face the

**[8:20]** technical build challenge in the same

**[8:22]** way, that's a big deal. So, I want to

**[8:25]** make this real with a coffee store. I'm

**[8:27]** a coffee guy. I used to run a coffee

**[8:29]** company, and I have colleagues in my

**[8:31]** Slack, cobuilders with me, who are also

**[8:34]** coffee people. And both of us stumbled

**[8:36]** onto the same thing. So, instead of

**[8:38]** having a generic Google Map search for

**[8:40]** cafes, both of us figured out that an

**[8:42]** agent backed by our preferences in Open

**[8:46]** Brain could go and plan an entire

**[8:48]** morning for us much more effectively

**[8:51]** because the agent knew our preferences.

**[8:52]** By the way, we don't have the same

**[8:53]** coffee preferences. We live in different

**[8:54]** parts of the country, etc. But, we both

**[8:56]** figured this out, and I was able to use

**[8:58]** it when I was in Japan to do some coffee

**[9:01]** hunting that I wouldn't have been able

**[9:02]** to do otherwise, and you can easily

**[9:04]** input your coffee preferences and get

**[9:06]** much more customized results as well.

**[9:09]** That's a tiny tiny little example. You

**[9:10]** might be like, building an agent for

**[9:12]** coffee, I would never do that. No, pick

**[9:14]** the pain that works for you. I don't

**[9:16]** care if it's coffee. I care that the

**[9:18]** pain is better because you have an agent

**[9:21]** that understands the tradeoffs, that

**[9:23]** understands the the decisions that are

**[9:25]** right for you because your memory is

**[9:27]** yours. If you want the world where your

**[9:31]** agent will fight insurance for you and

**[9:34]** monitor your email for you, That world

**[9:37]** runs through your memory, your skills,

**[9:40]** your ability to orchestrate agents. It

**[9:43]** should not run through some company that

**[9:45]** gets stuck in regulation trying to

**[9:47]** figure out what's good for you. Now, you

**[9:50]** can use intelligence from whatever

**[9:52]** source you want, right? You can use it

**[9:53]** from Open AI or Anthropic or from Kimmy

**[9:56]** K2 or Quan or whatever. But, your

**[9:58]** memories are yours, your skills are

**[10:00]** yours, and they should stay that way.

**[10:03]** It's going to be more like the agent

**[10:04]** knows my preferences. The agent knows

**[10:06]** that I do want to battle every single

**[10:07]** insurance claim. The agent knows how to

**[10:10]** go about doing the research to do that

**[10:11]** well, and I get to approve the drafts,

**[10:13]** by the way. It doesn't just get sent

**[10:14]** without me. We need control

**[10:18]** over our agents. We need agents that

**[10:20]** belong to us, agents that have memory

**[10:22]** that we understand, agents that have a

**[10:26]** scope of action that we approve of.

**[10:28]** That's why my open engine approach

**[10:30]** emphasizes that you should be able to

**[10:32]** see when an agent picks up a task,

**[10:34]** right? A ticketing system is actually

**[10:35]** just a good primitive for that cuz you

**[10:37]** can see, "Oh, it picked up the task. Oh,

**[10:39]** it wrote something." It's not hidden

**[10:40]** away in chain of thought, right? It's

**[10:42]** not like erased in the middle of a chat

**[10:44]** that I can't find. Have you ever tried

**[10:45]** to find the chats in ChatGPT or in

**[10:47]** Claude? I'm just like, "Oh my gosh, I

**[10:48]** searched for that keyword. It's not

**[10:50]** there." They need to fix search, but you

**[10:52]** also need to not depend on that to get

**[10:54]** agentic work done. You need to have an

**[10:58]** external scaffolding that lets you be

**[11:00]** confident that you can get your work

**[11:02]** done regardless. But, we can control

**[11:05]** where our memories live, we can control

**[11:06]** our skills, we can control how work gets

**[11:09]** done and ensures that it has a a status

**[11:11]** and an approval layer where relevant,

**[11:14]** and agent handoffs that we can read and

**[11:16]** escalations to humans that make sense.

**[11:18]** So, jump in, the water's warm, and the

**[11:21]** ability to build is like 1/5 or less

**[11:26]** technical than it was back in February.

**[11:29]** I I I reminds you how quickly this is

**[11:31]** changing, and I hope that reminds you

**[11:33]** and encourages you that you too can do

**[11:35]** this. Even though this has technical

**[11:38]** primitives underneath like a SQL

**[11:39]** database, you can do it without really

**[11:42]** digging in and understanding the details

**[11:44]** of that because the agents are good

**[11:46]** enough to explain what it means in

**[11:48]** practice for you. And I think that's one

**[11:51]** of the things I really struggle with

**[11:53]** with where we are in the agentic

**[11:54]** revolution. Because to be honest with

**[11:56]** you, Claude and Codex are very

**[11:59]** code-shaped today. And most of the world

**[12:02]** is not code-shaped. Most of the world is

**[12:04]** non-technically skilled.

**[12:07]** And that's just as legitimate a skill

**[12:08]** set.

**[12:09]** And so we need to find

**[12:12]** ways to work with our agents that feel

**[12:15]** safe if we're non-technical. And a lot

**[12:17]** of the project that I've been working on

**[12:19]** with Open Brain over the last 5 months

**[12:21]** is basically making it easier and easier

**[12:23]** and easier for you if you are

**[12:24]** non-technical to use agents to work with

**[12:27]** that GitHub repo, to work with that

**[12:30]** code, so it's not scary, so it's not

**[12:32]** non-transparent, so it doesn't do things

**[12:34]** you don't want it to do, and so you

**[12:35]** actually get your work done, and

**[12:37]** actually do things like weekly planning

**[12:38]** and family logistics, and the work

**[12:40]** blocks that you want to protect, and you

**[12:41]** feed the projects that keep getting

**[12:43]** started, or whatever it is that you are

**[12:45]** building this agent for. Giving your

**[12:46]** agents memory and skills and a clear

**[12:49]** framework to do stuff in in order to get

**[12:52]** to that world. And it has never, ever,

**[12:54]** ever been easier.

**[12:56]** It's never been easier. So if this is

**[12:57]** you, if you're like, "Ah,

**[12:59]** I'm almost there. I want to build." This

**[13:02]** is your invitation. I am waving the

**[13:04]** green flag here. I am telling you the

**[13:06]** agents can get it done. The agents can

**[13:09]** help you build agents. And that's one of

**[13:12]** the biggest differences between now and

**[13:14]** when I made my original Open Brain

**[13:15]** tutorial, which like 200,000 of you have

**[13:17]** watched, which is amazing, and I love

**[13:19]** that. It's easier now. It It's like five

**[13:21]** times easier now. I know 200,000 of you

**[13:24]** haven't built this, and I think it's

**[13:25]** worth building so you own your memory

**[13:27]** and like these guys who are trying to

**[13:29]** get approval from Washington for this

**[13:31]** and that don't own your memory. You

**[13:32]** should keep your judgment. The agent can

**[13:35]** carry the technical steps to get this

**[13:36]** work done for you now, and it could

**[13:38]** still defer to you about what matters,

**[13:40]** which things you want to remember, which

**[13:42]** things are skills that you want to say

**[13:43]** this is my domain expertise, I want to

**[13:45]** preserve it. I don't want Claude to own

**[13:46]** that skill. I don't want OpenAI to own

**[13:47]** that skill. I want to own that skill.

**[13:49]** The assistant race is just going to get

**[13:51]** more seductive from here. The demos will

**[13:53]** get better. The phone integrations will

**[13:55]** get smoother. The voices will get

**[13:57]** warmer. Every one of those improvements

**[14:00]** is designed to get your attention. It's

**[14:02]** designed to get us to put our memory and

**[14:05]** our focus and our work into these apps.

**[14:10]** The company that holds the memory holds

**[14:12]** the part that makes the assistant feel

**[14:13]** personal. I would rather build that part

**[14:15]** myself. And that is why I keep coming

**[14:19]** back to this. Intelligence is not a

**[14:20]** personal thing. Memory is personal. And

**[14:24]** you know, in February a lot of that was

**[14:25]** about getting your agents to remember

**[14:27]** you. And now it it really is about

**[14:29]** giving your agents a platform to jump

**[14:30]** from and act from on your behalf cuz

**[14:32]** there's so much more powerful. Pick a

**[14:34]** recurring situation you're tired of

**[14:35]** explaining. Write down the context that

**[14:38]** would change that answer. Point your

**[14:40]** agent at the guide, which I will link

**[14:42]** to, keep control of accounts and secrets

**[14:45]** and permissions and approval at your

**[14:47]** level, and then tell it to run and

**[14:50]** practice, right? And give it feedback.

**[14:51]** Say, "No, that was wrong. Change this.

**[14:52]** No, that was wrong. Change this." Agents

**[14:55]** take a while to break in.

**[14:56]** Once you start to get into the rhythm of

**[14:58]** using them, it gets easier and easier

**[15:00]** and easier and easier. And now even that

**[15:02]** first step, even getting the shoe so you

**[15:04]** can wear it, agents can help with that

**[15:06]** in a way they couldn't back in February.

**[15:08]** And that is the key. That is the key I

**[15:10]** want you to take away. And the prize for

**[15:12]** unlocking that door, the prize is just

**[15:14]** owning the context every future agent

**[15:17]** will need but before it even arrives.

**[15:19]** So, when an agent comes, you can just

**[15:21]** plug it right in, right? I want you to

**[15:22]** take advantage of the latest and

**[15:23]** greatest AI agents that you want to take

**[15:25]** advantage of. I don't want to pick a

**[15:26]** favorite, you pick.

**[15:28]** But you own the memory and you make sure

**[15:30]** that you rent the intelligence. So the

**[15:32]** intelligence is something you can apply

**[15:34]** to your memory, your skills, your

**[15:36]** orchestration layer, infrastructure that

**[15:39]** lets the agent work for you. Pick the

**[15:41]** part of your life that you want to

**[15:43]** change and let an agent change it for

**[15:45]** you. I I'm not kidding. You can actually

**[15:47]** do it. If nothing else, if you know

**[15:50]** someone who has a really big pain point

**[15:52]** and maybe it's agent shaped or you know

**[15:53]** it's agent shaped and you're a builder,

**[15:55]** go tell them that. Go say, "Hey, this is

**[15:58]** not that hard. An agent can help you

**[15:59]** build this." We need positive examples.

**[16:02]** In fact, if you have positive examples,

**[16:04]** if you're an open rebuild, if you you

**[16:05]** built on something else, maybe you built

**[16:06]** on G brain, I don't care. Put positive

**[16:09]** examples of why an agent made a

**[16:10]** difference in your life down here. I

**[16:12]** would like to see them. I want more

**[16:13]** people to see positive examples of

**[16:15]** agents working.
