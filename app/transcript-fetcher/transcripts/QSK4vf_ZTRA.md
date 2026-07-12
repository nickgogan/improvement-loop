# Transcript: I Was The Only Thing Connecting Claude, ChatGPT, and Codex. So I Built My Replacement.

**URL:** https://www.youtube.com/watch?v=QSK4vf_ZTRA
**Segments:** 619
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 22:04
**Uploaded:** 2026-06-26

---

## Full Text

By the end of this video, you're going to know how to make Claude, Codex, ChatGPT, and Open Claw or Hermes work together without waiting for any of them to start to integrate with each other. And yes, I'm going to show demos, I'm going to show what I built, I'm going to talk to you about why, I'm going to give you real stories, I'm going to tell you I'm using it at home and at work. It's the full shebang. You're going to get the full tour, and by the end, you're going to be able to build it for yourself. I call it Open Engine, and the promise is simple. We need an Open Engine that drives our life because we have too many AIs and they don't talk together well. So, Open Engine gets your agents to stop acting like separate subscriptions or separate products and start acting like a system you can operate. And if you're wondering, is this for teams, too? Yes, I'm using it with my team. It absolutely works for teams. It works for a teams of humans and their agents, and it's a seamless way to get them all to work together. I'm very excited. I'm going to show it off to you in this video. And yes, I've been building and using a working version of this to help me actually get stories out, organize my life, move houses, and I wanted to release it into the world because it's been so useful for me and it's actually lifted the load from my life. Let me make this concrete with a real story of a friend of mine. She has a baby, she runs an agency, she uses Claude Code, she's got loops and automations, she's looked seriously at Open Claw because she wants agents to do real work. She is not trying AI for the first time. She's already using the tools and she's talking to me about them, right? Her challenge is that there are five at least different AI systems she's using that all help with a particular piece of the day, and she becomes the person that carries the work between them. And that's a lot of labor to carry. And anyone who's used these systems knows that that labor is real because you can't trade them out. Claude Code and Codex don't do the same things even though they're aimed at the same segment of the population as a user base. Claude is better at front-end design. It just is. It's intuitive. Open AI is less good at that, but Open AI has a reputation for back-end engineering that's very strong. And a lot of us who understand these things are juggling a lot, and it's painful. And we've had to effectively drive our own harnesses to make up for that by coordinating ourselves across all of these tools. So, she's using five different AI tools, and the question is how work can leave a tool, land with the right person or the right next agent, bring the source material with it, show what happened, and not make anybody read a giant chat transcript. And if that sounds like you, I've got good news for you. I'm putting together an agent tool that solves for that, and that's what Open Agent really is. It is a tool that allows every AI in your system to coordinate seamlessly and carry state or context or detail back and forth without you having to do the work. She is trying to figure out how to balance a client call, a product scoping conversation, and a baby appointment that just came up. She has to figure out how to do all three of those. She typically uses Codex for product scoping. She's using Claude Code to reorganize and move her calendar around, and she's trying to deal with the baby appointment by email, but she would like to find some automation there for that. There is no easy way to tackle all of that in one thing unless you're compromising on models somewhere. And so, the question that she has is can she live without compromises? Can she find a way to get her preferred model against a particular problem and not feel like she has to trade that off in order to keep track of everything. And kind of go in farther than that, can she avoid having to depend on unpredictable memory in order to do that? And one of the challenges with Open Claw, and I've installed it, I've used it, is that it's sometimes not entirely accurate when you're doing multiple different roles in your life over a long enough period of time. And so, in this case, like when you have the the baby appointment pop back up after a couple of months and then at the same time you have an agency team question and your open clock can't talk to the team intuitively unless you give it permissions on Slack and then if you do it doesn't talk to the team's agent and then at the same time you have to get it into the email somehow and then there's a whole memory piece that goes this is the actual conversation here. Are you seeing how many ifs, buts, wins, ifs, and copies and pastes there are? There's so much. It's a lot of extended work that we're carrying for using these AI tools and people who are AI productive are just carrying that load because the AI payoff is so great and what we're seeing in 2026 is that AI is helping with these pieces and post open claw we're getting some of that coordination piece in but the really hard part isn't solved yet. The really hard part is the movement between the pieces seamlessly and carrying full state all the details, right? So on Wednesday I talked about the idea that agents are really loop managers. A useful agent is a remembered workflow that can run again and notice what changed and stop in the right place and bring you in when the decision is really needed and that is absolutely the right basic frame for an agent. But if every loop lives in its own room, the human becomes the hallway. The research loop finishes and the writing loop doesn't know what changed. The support loop sees a pattern but the product loop doesn't get the original messages unless you put them there, right? The coding agent fixes the file but the teammate who owns review only sees a vague summary unless you send them a bunch of chats. The schedule changes but the work loop doesn't know that the afternoon just collapsed. Going back to our story. This is why I built open engine and this is the kind of problem I've been working on solving for a while. So if you recall open brain was about memory. So a few months ago I argued that every AI you use starts from zero unless you give it a true memory system that you control and it lives between your agents. Your context should not be trapped inside one company's chat history. Open engine is the next big piece here. Once the AI can remember, how does your work actually move? And And the basic approach here is very, very simple. And I'm doing this and talking about it as simply as possible because I want this to be easy for you. Open engine is the next missing piece in the story for all of us who are trying to be productive with AI and actually get rid of all of that invisible work. Once the AI can remember, how does our work move so we don't have to spend a lot of time coordinating and doing that invisible labor? The basic move that I'm going to propose here is extremely simple on purpose. I want to make this as easy to use and do as possible. Just put the work in a queue that both people and agents can read. What is a queue? It can be as simple as a Jira system. It can be a a Kanban board that you coded it up. It can be a linear ticket queue, that's what I like. Whatever it is, as long as it is a queue that an agent can write to and you can read to, it's good enough. And if you have a queue like that, then all you need to do is have an issue that says, "This is what needs to happen. This is who owns it. This is the background that matters. This is what the agent can do and where the agent should stop and what it has to show when it's done." And that sounds really, really simple and simple is the point, right? A good queue issue or a good ticket is the difference between asking an AI for help and giving it a job the next person, the next agent can understand so it actually gets off your plate and gets done. Right? If we go back to 2025 when we were talking a lot about prompting, a prompt asks for an answer of some sort. A ticket asks for a result to get done and it can have multiple agents even if the agents don't know with and aren't directly integrated. The ticket becomes the place they talk. And I think that this distinction is really important because as agents get better, we need better state management for our agents. A chat box is a terrible way to manage state. And I'm sorry, but so is Slack. An agent needs to be able to change files and create tasks and move statuses and write drafts and do all of that in a place where you can actually see what happened. When we're picking paint colors for the house, to see what kind of paint we picked out, right? Like otherwise, we're going to get all mixed up and it just lives in somebody's head and then we're doing that mental labor. When my friend is trying to figure out whether she has five or six different companies in pipeline, she actually has to be able to audit that pipeline from any given command line that she has, see what has been done on it by her team, what has been done on it by her team's agents, what has been done on it by her agents, and what the next step is. Again, you can't do that by querying chats. So, this is what I'm trying to build with Open Engine. And And the guide that I put together is very specific. It has five different components that you can point at that all add up together into a complete ecosystem. And if you miss one of them, it doesn't really go together, right? It doesn't hang together. The first is a linear queue, that makes a lot of sense. Linear's got a generous free plan, it works well with with all of the AI systems, that's why I chose it, but you don't have to use Linear. You can use Jira, you can use your own system, it's fine. Then we get into how you tell your AI, "Hey, this is how you use this tool." Because the AI needs to be told, "This is the protocol for using this ticketing system." And so, there are four other pieces that go with that, and I've written basically skills that tell your AI how to use this, right? There's a setup skill, there's a status skill, there's there's a skill to run a a queue through the the AI, and then there's a smoke test so you can start to test this. I want this actually help me. And yes, you can absolutely point your open claw or your Hermes at this as a skill and use that too, right? This is not an anti-open claw sentiment. I love what open claw has done. I love what Peter's done. I love Hermes. You can use those tools as much as you want and you're not limited by only using those tools. Open claw has pointed at a real desire that made a lot of sense. We want agents that can act, right? Agents that aren't a chat window. Hermes and similar projects are aimed at another real desire that goes beyond that. Agents can improve at repeated work and learn instead of starting cold every time. These are real needs, but making an agent autonomous is not enough. A very capable private agent can still become another inbox or a task queue or a text message queue that you have to manage. The bottleneck I care about is the boundary between agents because that's where I feel the pain. Can the work leave Claude and go to Codex? Can a teammate's agent pick up a task created by my agent? Can a support loop escalate to the person with authority without losing any of the message or customer history and the reason for the agent stopping work? All of this stuff is not a model problem. It's not an agent problem. It's a boundary problem. It's a who gets this next and how do we hand hand it off problem? If I go back to my friend, her problem is actually much more painful than a tool problem. It's much more painful than a fluency problem. She's fluent in AI tools. That's not an issue. She's got lots of AI tools. That's not an issue. The problem is a handoff problem. The problem is the information isn't flowing between her, her agents, her team's agents, and her team smoothly, fluently, without someone having to manage it. And it would it is amazing to me how much of AI promise gets bogged down in those handoff points. If you look at AI is essentially a technology change that moves bottlenecks. We are moving a ton of generative energy into this tiny bottleneck around handoffs, and that is what Open Engine is designed to attack and change and blow open so it gets easier. And yes, this works for households and teams at the same time. You think about it, a school pickup change is not the same as a sales pipeline, but the shape of handoff pain underneath is very familiar. Something has changed, several other things now depend on it. Some parts can be handled by agents, some parts need a person, uh and Open Engine doesn't replace the person. All it does is keep the person from being the only one handing all of this stuff off. And that is such a huge load off our shoulders. We found it's a huge load off for the family, and I found working with my team, it's a massive load off of our shoulders, as well, because our agents can now work together seamlessly, and we're not trying to track agent messages in Slack necessarily, although we can invoke our agents through Slack. We actually have a clear system of record, and we can tie each other's agents in, and it becomes a really effective way to collaborate without losing track of any detail of what we're doing. Think about it, if the agent writes a beautiful brief in a private chat, and nobody knows where it came from, it's just a draft in a room by itself. Output is what the AI returns right now. Work is what someone can review, accept, and build on. And Open Engine is about getting from output to work without making human beings the copy-paste path. So, jumping into demo. This is the basic Open Engine loop that you see on the screen. It's a request that becomes a clear linear task, it's assigned to the right operator, Codex wakes up, it checks its assigned queue and finds one eligible agent instructions issue. Before doing the work, it claim locks the issue, it moves it to agent working, and it leaves an agent claim receipt. And then execution starts locally, right? Linear coordinates the team, Codex does the work, a human can create a task for that agent, and an agent create a task for another agent. The task includes the outcome and sources and the definition of done. And when the agent starts, it moves from agent to do to agent working. And when it finishes, it also moves the issue to the right place. The receipt is not decoration here. It actually lets you know what was done. I don't want to ask the agent, "Did you do the thing?" I want to know it got done. And I don't want to have to copy and paste. I don't want to have to coordinate between my my LLMs anymore. I'm so tired of it. So this is how you actually take all of the context, all of the artifacts, and move it into a system where agents can actually tackle that work in a transparent manner so humans don't get confused about what's being worked on, so agents don't get confused. It just becomes very simple. All right, let's take a look at delegation, which is a key part of this pattern. Can you delegate to agents and what does that look like? Let's say Maya asks Codex to route a metrics bolt to Leo's agent. Leo's agent happens to be Claude. Codex checks that Leo's agent is online and then writes a self-contained linear issue with the context needed to act. That's two people's different agents from different LLM providers coordinating in linear. It assigns the issue to Leo's agent, keeps it in agent to do, and labels it as agent instructions. Now Leo's agent can pick it up on its own heartbeat, and the handoff is visible and its scope is not buried in chat. Because the point is not that we made an agent do a trick here, right? The point is you can actually see the work move through the team. And in that context, the smoke test in the skill, right? It's deliberately clean and very, very efficient. All you're doing is saying create an issue called say hello from the queue. You're assigning it to an human or an agent, giving it an instruction label, and making sure that it actually can move to done. So this is not about giving your agent a bunch of work from me. This is just about giving you a clean smoke test so you can see that this agent interaction loop works. The full loop is actually pretty simple. You have to have a request, you have to have an issue, a claim, a piece of work that's done, some proof that it's done, a receipt, and then you want to go on to the next item. Let's say Leo the agent claims the task and moves it into agent working. So everyone knows it's worked on. If it hits ambiguity, the agent doesn't gas. Instead, it moves to needs input and asks the exact blocking question. Maya the human can answer on that issue and the agent can resume and the audit trail stays in one place. And when finished, Leo leaves agent done as a status and moves on to the next task. And we can use that for any piece of work. You can use that for picking paint colors in the house as easily as you can use it for scheduling a pipeline review while you are on the go trying to sort out your kids doctor appointment. The The point is that the queue itself makes it easy to sort out all of the handoff stress so that you're not dealing with it. Because open engine demands that we move from prompt mode to demanding real work and the framework helps us get there. Open engine helps us get there. So prompt mode might be writing a follow-up email. Work mode might be here's the client call transcript, here's the decision we made, here's the promise I don't want to overstate, here's the calendar constraints. You draft the follow-up agent, flag what needs my judgment, and leave notes that I can review later. See? That's a full statement of work right there. And you can actually pass that to another agent to review using open engine, too, if you want a second opinion, which a lot of people do, especially on client-facing communication. You could have a whole agent that just reviews for brand language. I'll give you another couple examples. Prompt mode might be, "Hey, summarize this support ticket." You ask your codex to do that, you ask your cloud to do that. Work mode would be, "Classify this ticket, attach the customer history, identify whether this was a known issue, create a product task only if it meets my escalation rule, and show exactly where you stopped work and why." Or this one, prompt mode would be help me change my schedule. Work mode would be the pickup time for the kids has changed, check what it affects, draft the two messages that might be needed to the school, and wait for approval before anything leaves the system. The model can be the same here, but the assignment is much more clear and the ability to hand off to multiple agents or to a human as you determine is really, really easy. We need to stop assuming that we are the glue between all of the AI systems that we work for. Otherwise, that the AI is prompting us and we're just working for the AI instead of the other way around. We want to be in a place where the work can move across the tools that we're already using and that's the open engine promise. Because our teams don't really live in one AI tool. I don't know anyone who is curious about AI who actually uses only one tool. And especially if you get two people together, it's not one tool. It's like two different tools, three, five. I often see six different tools between two people and you're not going to expect people to actually change that. You actually just want to give people a queue where all of their AIs can talk to each other. So, I'm not going to make you a big promise here. I'm not saying open engine can run your company. I don't want to say that. I don't want to say open engine can run your household. What I want to say is the next useful AI is not another private assistant. It's a queue where your agents can all work together and move stuff forward. And that matters on any team and increasingly we're all managing teams of agents because teams need owners and status and receipts and review. And if you don't tackle that, something gets lost, something drops through the cracks and you have household consequences for that, you have work consequences for that. If we go back to earlier in this video, I talked about the idea that we are the hallway between AI agents. Open engine is what I built to make that hallway into software transparent and smooth and easy so we humans stop carrying all of that load. It It's not up to us to be the invisible laborers for our AIs. It is up to good frameworks and systems to let work move from where it started to where it needs to go. With enough context, the next loop can do something useful. The test for open engine is really simple. Can the work get out of your chat? Can it get out of your chat? Can it carry with it the sources that it has to do the work? Can it respect limits and can it come back and say, "This is what I did and this is what I didn't do and this is the receipt." Because if the answer is yes with open engine, even in a small way, then the entire agent conversation changes for you. You stop asking only what one AI can do in a session. You start asking what kind of work your whole system can carry without you being the messenger. That's the promise of open engine. Not agents replacing our judgment, not one agent to rule them all, but all of the mess of our AI systems just stitched together with a clean framework so agents can carry work to the point where judgment is needed and not bother us for the annoying handoffs along the way. That's the version of autonomy I actually want. That's what I've been living with. That's what I'm sharing with you today. If you want that, I have the full guide up. Uh the Substack community gets it first. We have an active Slack where people are building on this. I encourage you to join that as well. Uh and you can see exactly the the demo that I showed you and also a full guide that you can hand to your AI to get this started today. And remember, so that's open engine. If you have trouble with handoffs as I have had and as so many folks I have had have struggled with, this is for you. Go make your life easier. Go get the headaches out of the way. Go stop copying and pasting and just make make that all go away. Get open engine and get it sorted out so that you save hours. That's actually my personal goal is I want less wasted human hours. I want us to spend less hours on needless agent coordination. That would be my success. So, if you see this and you're like, "Oh my gosh, this is for me." Tell me in the chat, in the comments, what you are going to use this for. Tell me which AI systems you're going to coordinate. Tell me if you're working with agents, with a team, or with your partner. Uh whatever it is and and you want a framework that makes the AI and the human actually work together and you're going to use this to solve it, tell me what it is. One, we'll improve Open Agent and continue to make it better as you give us feedback. But, but two, I want to know how much pain we're going after here because that's what I'm interested in. I'm interested in AI that kills our pain. And this is a pain that has arisen since AI agents got more capable and it's just gotten worse. And so, in the era of Open Claw, in the era of Codex, in the era of Claude, we need something like Open Agent. I hope you've had fun seeing this demo. So, go get yours today.

---

## Timestamped Segments

**[0:00]** By the end of this video, you're going

**[0:01]** to know how to make Claude, Codex,

**[0:03]** ChatGPT, and Open Claw or Hermes work

**[0:05]** together without waiting for any of them

**[0:07]** to start to integrate with each other.

**[0:09]** And yes, I'm going to show demos, I'm

**[0:10]** going to show what I built, I'm going to

**[0:11]** talk to you about why, I'm going to give

**[0:13]** you real stories, I'm going to tell you

**[0:14]** I'm using it at home and at work. It's

**[0:17]** the full shebang. You're going to get

**[0:19]** the full tour, and by the end, you're

**[0:21]** going to be able to build it for

**[0:21]** yourself. I call it Open Engine, and the

**[0:24]** promise is simple. We need an Open

**[0:27]** Engine that drives our life because we

**[0:29]** have too many AIs and they don't talk

**[0:31]** together well. So, Open Engine gets your

**[0:34]** agents to stop acting like separate

**[0:36]** subscriptions or separate products and

**[0:38]** start acting like a system you can

**[0:40]** operate. And if you're wondering, is

**[0:41]** this for teams, too? Yes, I'm using it

**[0:44]** with my team. It absolutely works for

**[0:46]** teams. It works for a teams of humans

**[0:48]** and their agents, and it's a seamless

**[0:50]** way to get them all to work together.

**[0:51]** I'm very excited. I'm going to show it

**[0:52]** off to you in this video. And yes, I've

**[0:55]** been building and using a working

**[0:56]** version of this to help me actually get

**[0:58]** stories out, organize my life, move

**[1:00]** houses, and I wanted to release it into

**[1:02]** the world because it's been so useful

**[1:03]** for me and it's actually lifted the load

**[1:05]** from my life. Let me make this concrete

**[1:07]** with a real story of a friend of mine.

**[1:09]** She has a baby, she runs an agency, she

**[1:11]** uses Claude Code, she's got loops and

**[1:13]** automations, she's looked seriously at

**[1:14]** Open Claw because she wants agents to do

**[1:16]** real work. She is not trying AI for the

**[1:18]** first time. She's already using the

**[1:20]** tools and she's talking to me about

**[1:21]** them, right? Her challenge is that there

**[1:23]** are five at least different AI systems

**[1:25]** she's using that all help with a

**[1:27]** particular piece of the day, and she

**[1:29]** becomes the person that carries the work

**[1:31]** between them. And that's a lot of labor

**[1:33]** to carry. And anyone who's used these

**[1:35]** systems knows that that labor is real

**[1:38]** because you can't trade them out. Claude

**[1:40]** Code and Codex don't do the same things

**[1:43]** even though they're aimed at the same

**[1:45]** segment of the population as a user

**[1:47]** base. Claude is better at front-end

**[1:49]** design. It just is. It's intuitive. Open

**[1:52]** AI is less good at that, but Open AI has

**[1:54]** a reputation for back-end engineering

**[1:56]** that's very strong. And a lot of us who

**[1:58]** understand these things are juggling a

**[2:00]** lot, and it's painful. And we've had to

**[2:04]** effectively drive our own harnesses to

**[2:07]** make up for that by coordinating

**[2:09]** ourselves across all of these tools. So,

**[2:11]** she's using five different AI tools, and

**[2:14]** the question is how work can leave a

**[2:16]** tool, land with the right person or the

**[2:18]** right next agent, bring the source

**[2:20]** material with it, show what happened,

**[2:22]** and not make anybody read a giant chat

**[2:25]** transcript. And if that sounds like you,

**[2:26]** I've got good news for you. I'm putting

**[2:28]** together an agent tool that solves for

**[2:29]** that, and that's what Open Agent really

**[2:31]** is. It is a tool that allows every AI in

**[2:36]** your system to coordinate seamlessly and

**[2:39]** carry state or context or detail back

**[2:42]** and forth without you having to do the

**[2:44]** work. She is trying to figure out how to

**[2:47]** balance a client call, a product scoping

**[2:49]** conversation, and a baby appointment

**[2:51]** that just came up. She has to figure out

**[2:54]** how to do all three of those. She

**[2:55]** typically uses Codex for product

**[2:57]** scoping. She's using Claude Code to

**[2:59]** reorganize and move her calendar around,

**[3:01]** and she's trying to deal with the baby

**[3:03]** appointment by email, but she would like

**[3:05]** to find some automation there for that.

**[3:07]** There is no easy way to tackle all of

**[3:10]** that in one thing unless you're

**[3:12]** compromising on models somewhere. And

**[3:14]** so, the question that she has is can she

**[3:17]** live without compromises? Can she find a

**[3:19]** way to get her preferred model against a

**[3:22]** particular problem and not feel like she

**[3:25]** has to trade that off in order to keep

**[3:28]** track of everything. And kind of go in

**[3:30]** farther than that, can she avoid having

**[3:32]** to depend on unpredictable memory in

**[3:36]** order to do that? And one of the

**[3:37]** challenges with Open Claw, and I've

**[3:39]** installed it, I've used it, is that it's

**[3:41]** sometimes not entirely accurate when

**[3:44]** you're doing multiple different roles in

**[3:46]** your life over a long enough period of

**[3:48]** time. And so, in this case, like when

**[3:50]** you have the the baby appointment pop

**[3:52]** back up after a couple of months and

**[3:54]** then at the same time you have an agency

**[3:55]** team question and your open clock can't

**[3:57]** talk to the team intuitively unless you

**[3:59]** give it permissions on Slack and then if

**[4:02]** you do it doesn't talk to the team's

**[4:04]** agent and then at the same time you have

**[4:06]** to get it into the email somehow and

**[4:08]** then there's a whole memory piece that

**[4:09]** goes this is the actual conversation

**[4:11]** here. Are you seeing how many ifs, buts,

**[4:14]** wins, ifs, and copies and pastes there

**[4:16]** are? There's so much. It's a lot of

**[4:19]** extended work that we're carrying for

**[4:22]** using these AI tools and people who are

**[4:25]** AI productive are just carrying that

**[4:27]** load because the AI payoff is so great

**[4:31]** and what we're seeing in 2026 is that AI

**[4:33]** is helping with these pieces and post

**[4:36]** open claw we're getting some of that

**[4:37]** coordination piece in but the really

**[4:40]** hard part isn't solved yet. The really

**[4:42]** hard part is the movement between the

**[4:44]** pieces seamlessly and carrying full

**[4:46]** state all the details, right? So on

**[4:48]** Wednesday I talked about the idea that

**[4:50]** agents are really loop managers. A

**[4:51]** useful agent is a remembered workflow

**[4:54]** that can run again and notice what

**[4:55]** changed and stop in the right place and

**[4:57]** bring you in when the decision is really

**[4:59]** needed and that is absolutely the right

**[5:01]** basic frame for an agent. But if every

**[5:03]** loop lives in its own room, the human

**[5:06]** becomes the hallway. The research loop

**[5:08]** finishes and the writing loop doesn't

**[5:10]** know what changed. The support loop sees

**[5:12]** a pattern but the product loop doesn't

**[5:13]** get the original messages unless you put

**[5:15]** them there, right? The coding agent

**[5:17]** fixes the file but the teammate who owns

**[5:19]** review only sees a vague summary unless

**[5:21]** you send them a bunch of chats. The

**[5:23]** schedule changes but the work loop

**[5:25]** doesn't know that the afternoon just

**[5:26]** collapsed. Going back to our story. This

**[5:28]** is why I built open engine and this is

**[5:30]** the kind of problem I've been working on

**[5:32]** solving for a while. So if you recall

**[5:34]** open brain was about memory. So a few

**[5:36]** months ago I argued that every AI you

**[5:38]** use starts from zero unless you give it

**[5:41]** a true memory system that you control

**[5:44]** and it lives between your agents. Your

**[5:46]** context should not be trapped inside one

**[5:48]** company's chat history. Open engine is

**[5:51]** the next big piece here. Once the AI can

**[5:54]** remember, how does your work actually

**[5:57]** move?

**[5:58]** And And the basic approach here is very,

**[6:01]** very simple. And I'm doing this and

**[6:03]** talking about it as simply as possible

**[6:06]** because I want this to be easy for you.

**[6:08]** Open engine is the next missing piece in

**[6:11]** the story for all of us who are trying

**[6:13]** to be productive with AI and actually

**[6:15]** get rid of all of that invisible work.

**[6:17]** Once the AI can remember, how does our

**[6:20]** work move so we don't have to spend a

**[6:22]** lot of time coordinating and doing that

**[6:24]** invisible labor? The basic move that I'm

**[6:27]** going to propose here is extremely

**[6:29]** simple on purpose. I want to make this

**[6:31]** as easy to use and do as possible. Just

**[6:34]** put the work in a queue that both people

**[6:37]** and agents can read. What is a queue? It

**[6:39]** can be as simple as a Jira system. It

**[6:42]** can be a a Kanban board that you coded

**[6:45]** it up. It can be a linear ticket queue,

**[6:47]** that's what I like. Whatever it is, as

**[6:49]** long as it is a queue that an agent can

**[6:52]** write to and you can read to, it's good

**[6:54]** enough. And if you have a queue like

**[6:56]** that, then all you need to do is have an

**[6:59]** issue that says, "This is what needs to

**[7:01]** happen. This is who owns it. This is the

**[7:03]** background that matters. This is what

**[7:05]** the agent can do and where the agent

**[7:07]** should stop and what it has to show when

**[7:09]** it's done." And that sounds really,

**[7:11]** really simple and simple is the point,

**[7:13]** right? A good queue issue or a good

**[7:15]** ticket is the difference between asking

**[7:18]** an AI for help and giving it a job the

**[7:21]** next person, the next agent can

**[7:23]** understand so it actually gets off your

**[7:24]** plate and gets done. Right? If we go

**[7:26]** back to 2025 when we were talking a lot

**[7:29]** about prompting, a prompt asks for an

**[7:31]** answer of some sort. A ticket asks for a

**[7:34]** result to get done and it can have

**[7:37]** multiple agents even if the agents don't

**[7:39]** know with and aren't directly

**[7:40]** integrated. The ticket becomes the place

**[7:43]** they talk. And I think that this

**[7:45]** distinction is really important because

**[7:47]** as agents get better, we need better

**[7:51]** state management for our agents. A chat

**[7:53]** box is a terrible way to manage state.

**[7:55]** And I'm sorry, but so is Slack. An agent

**[7:58]** needs to be able to change files and

**[8:01]** create tasks and move statuses and write

**[8:03]** drafts and do all of that in a place

**[8:05]** where you can actually see what

**[8:06]** happened. When we're picking paint

**[8:08]** colors for the house, to see what kind

**[8:11]** of paint we picked out, right? Like

**[8:14]** otherwise, we're going to get all mixed

**[8:15]** up and it just lives in somebody's head

**[8:17]** and then we're doing that mental labor.

**[8:18]** When my friend is trying to figure out

**[8:20]** whether she has five or six different

**[8:24]** companies in pipeline, she actually has

**[8:26]** to be able to audit that pipeline from

**[8:29]** any given command line that she has, see

**[8:31]** what has been done on it by her team,

**[8:33]** what has been done on it by her team's

**[8:35]** agents, what has been done on it by her

**[8:37]** agents, and what the next step is.

**[8:38]** Again, you can't do that by querying

**[8:42]** chats. So, this is what I'm trying to

**[8:44]** build with Open Engine. And And the

**[8:46]** guide that I put together is very

**[8:47]** specific. It has five different

**[8:49]** components that you can point at that

**[8:52]** all add up together into a complete

**[8:55]** ecosystem. And if you miss one of them,

**[8:57]** it doesn't really go together, right? It

**[8:58]** doesn't hang together. The first is a

**[9:00]** linear queue, that makes a lot of sense.

**[9:02]** Linear's got a generous free plan, it

**[9:03]** works well with with all of the AI

**[9:05]** systems, that's why I chose it, but you

**[9:07]** don't have to use Linear. You can use

**[9:08]** Jira, you can use your own system, it's

**[9:10]** fine. Then we get into how you tell your

**[9:13]** AI, "Hey, this is how you use this

**[9:15]** tool." Because the AI needs to be told,

**[9:17]** "This is the protocol for using this

**[9:19]** ticketing system." And so, there are

**[9:22]** four other pieces that go with that, and

**[9:24]** I've written basically skills that tell

**[9:25]** your AI how to use this, right? There's

**[9:27]** a setup skill, there's a status skill,

**[9:29]** there's there's a skill to run a a queue

**[9:32]** through the the AI, and then there's a

**[9:34]** smoke test so you can start to test

**[9:36]** this. I want this actually help me. And

**[9:38]** yes, you can absolutely point your open

**[9:40]** claw or your Hermes at this as a skill

**[9:43]** and use that too, right? This is not an

**[9:46]** anti-open claw sentiment. I love what

**[9:48]** open claw has done. I love what Peter's

**[9:50]** done. I love Hermes. You can use those

**[9:53]** tools as much as you want and you're not

**[9:55]** limited by only using those tools. Open

**[9:57]** claw has pointed at a real desire that

**[9:59]** made a lot of sense. We want agents that

**[10:01]** can act, right? Agents that aren't a

**[10:03]** chat window. Hermes and similar projects

**[10:05]** are aimed at another real desire that

**[10:06]** goes beyond that. Agents can improve at

**[10:08]** repeated work and learn instead of

**[10:10]** starting cold every time. These are real

**[10:12]** needs, but making an agent autonomous is

**[10:14]** not enough. A very capable private agent

**[10:17]** can still become another inbox or a task

**[10:20]** queue or a text message queue that you

**[10:22]** have to manage. The bottleneck I care

**[10:24]** about is the boundary between agents

**[10:26]** because that's where I feel the pain.

**[10:28]** Can the work leave Claude and go to

**[10:30]** Codex? Can a teammate's agent pick up a

**[10:33]** task created by my agent? Can a support

**[10:35]** loop escalate to the person with

**[10:37]** authority without losing any of the

**[10:39]** message or customer history and the

**[10:40]** reason for the agent stopping work? All

**[10:44]** of this stuff is not a model problem.

**[10:46]** It's not an agent problem. It's a

**[10:48]** boundary problem. It's a who gets this

**[10:50]** next and how do we hand hand it off

**[10:52]** problem? If I go back to my friend, her

**[10:53]** problem is actually much more painful

**[10:56]** than a tool problem. It's much more

**[10:58]** painful than a fluency problem. She's

**[11:01]** fluent in AI tools. That's not an issue.

**[11:03]** She's got lots of AI tools. That's not

**[11:05]** an issue. The problem is a handoff

**[11:08]** problem. The problem is the information

**[11:10]** isn't flowing between her, her agents,

**[11:13]** her team's agents, and her team

**[11:15]** smoothly, fluently, without someone

**[11:18]** having to manage it.

**[11:20]** And it would it is amazing to me how

**[11:23]** much of AI promise gets bogged down in

**[11:26]** those handoff points. If you look at AI

**[11:29]** is essentially a technology change that

**[11:31]** moves bottlenecks. We are moving a ton

**[11:35]** of generative energy into this tiny

**[11:37]** bottleneck around handoffs, and that is

**[11:39]** what Open Engine is designed to attack

**[11:41]** and change and blow open so it gets

**[11:42]** easier. And yes, this works for

**[11:44]** households and teams at the same time.

**[11:46]** You think about it, a school pickup

**[11:47]** change is not the same as a sales

**[11:49]** pipeline, but the shape of handoff pain

**[11:52]** underneath is very familiar. Something

**[11:54]** has changed, several other things now

**[11:56]** depend on it. Some parts can be handled

**[11:58]** by agents, some parts need a person, uh

**[12:00]** and Open Engine doesn't replace the

**[12:02]** person. All it does is keep the person

**[12:05]** from being the only one handing all of

**[12:07]** this stuff off.

**[12:09]** And that is such a huge load off our

**[12:11]** shoulders. We found it's a huge load off

**[12:13]** for the family, and I found working with

**[12:15]** my team, it's a massive load off of our

**[12:18]** shoulders, as well, because our agents

**[12:20]** can now work together seamlessly, and

**[12:22]** we're not trying to track agent messages

**[12:24]** in Slack necessarily, although we can

**[12:25]** invoke our agents through Slack. We

**[12:27]** actually have a clear system of record,

**[12:29]** and we can tie each other's agents in,

**[12:31]** and it becomes a really effective way to

**[12:33]** collaborate without losing track of any

**[12:35]** detail of what we're doing. Think about

**[12:37]** it, if the agent writes a beautiful

**[12:38]** brief in a private chat, and nobody

**[12:40]** knows where it came from, it's just a

**[12:41]** draft in a room by itself. Output is

**[12:44]** what the AI returns right now. Work is

**[12:47]** what someone can review, accept, and

**[12:49]** build on. And Open Engine is about

**[12:51]** getting from output to work without

**[12:54]** making human beings the copy-paste path.

**[12:58]** So, jumping into demo. This is the basic

**[13:01]** Open Engine loop that you see on the

**[13:02]** screen. It's a request that becomes a

**[13:04]** clear linear task, it's assigned to the

**[13:06]** right operator, Codex wakes up, it

**[13:08]** checks its assigned queue and finds one

**[13:10]** eligible agent instructions issue.

**[13:12]** Before doing the work, it claim locks

**[13:14]** the issue, it moves it to agent working,

**[13:17]** and it leaves an agent claim receipt.

**[13:19]** And then execution starts locally,

**[13:20]** right? Linear coordinates the team,

**[13:22]** Codex does the work, a human can create

**[13:24]** a task for that agent, and an agent

**[13:25]** create a task for another agent. The

**[13:28]** task includes the outcome and sources

**[13:30]** and the definition of done. And when the

**[13:31]** agent starts, it moves from agent to do

**[13:34]** to agent working. And when it finishes,

**[13:36]** it also moves the issue to the right

**[13:37]** place. The receipt is not decoration

**[13:39]** here. It actually lets you know what was

**[13:42]** done. I don't want to ask the agent,

**[13:43]** "Did you do the thing?" I want to know

**[13:45]** it got done. And I don't want to have to

**[13:47]** copy and paste. I don't want to have to

**[13:49]** coordinate between my my LLMs anymore.

**[13:51]** I'm so tired of it.

**[13:53]** So this is how you actually take all of

**[13:57]** the context, all of the artifacts, and

**[13:59]** move it into a system where agents can

**[14:02]** actually

**[14:04]** tackle that work in a transparent manner

**[14:07]** so humans don't get confused about

**[14:09]** what's being worked on, so agents don't

**[14:10]** get confused. It just becomes very

**[14:13]** simple. All right, let's take a look at

**[14:14]** delegation, which is a key part of this

**[14:16]** pattern. Can you delegate to agents and

**[14:18]** what does that look like? Let's say Maya

**[14:20]** asks Codex to route a metrics bolt to

**[14:23]** Leo's agent. Leo's agent happens to be

**[14:25]** Claude. Codex checks that Leo's agent is

**[14:27]** online and then writes a self-contained

**[14:29]** linear issue with the context needed to

**[14:31]** act. That's two people's different

**[14:33]** agents from different LLM providers

**[14:35]** coordinating in linear. It assigns the

**[14:37]** issue to Leo's agent, keeps it in agent

**[14:39]** to do, and labels it as agent

**[14:41]** instructions. Now Leo's agent can pick

**[14:43]** it up on its own heartbeat, and the

**[14:45]** handoff is visible and its scope is not

**[14:47]** buried in chat. Because the point is not

**[14:49]** that we made an agent do a trick here,

**[14:52]** right? The point is you can actually see

**[14:53]** the work move through the team. And in

**[14:55]** that context, the smoke test in the

**[14:57]** skill, right? It's deliberately clean

**[15:00]** and very, very efficient. All you're

**[15:02]** doing is saying create an issue called

**[15:03]** say hello from the queue. You're

**[15:05]** assigning it to an human or an agent,

**[15:08]** giving it an instruction label, and

**[15:11]** making sure that it actually can move to

**[15:12]** done. So this is not about giving your

**[15:15]** agent a bunch of work from me. This is

**[15:17]** just about giving you a clean smoke test

**[15:20]** so you can see that this agent

**[15:21]** interaction loop works. The full loop is

**[15:23]** actually pretty simple. You have to have

**[15:24]** a request, you have to have an issue, a

**[15:27]** claim, a piece of work that's done, some

**[15:30]** proof that it's done, a receipt, and

**[15:31]** then you want to go on to the next item.

**[15:33]** Let's say Leo the agent claims the task

**[15:36]** and moves it into agent working. So

**[15:38]** everyone knows it's worked on. If it

**[15:39]** hits ambiguity, the agent doesn't gas.

**[15:42]** Instead, it moves to needs input and

**[15:44]** asks the exact blocking question. Maya

**[15:47]** the human can answer on that issue and

**[15:49]** the agent can resume and the audit trail

**[15:50]** stays in one place. And when finished,

**[15:52]** Leo leaves agent done as a status and

**[15:55]** moves on to the next task.

**[15:57]** And we can use that for any piece of

**[16:00]** work. You can use that for picking paint

**[16:01]** colors in the house as easily as you can

**[16:03]** use it for scheduling a pipeline review

**[16:07]** while you are on the go trying to sort

**[16:10]** out your kids doctor appointment. The

**[16:11]** The point is that the queue itself makes

**[16:14]** it easy to sort out all of the handoff

**[16:17]** stress so that you're not dealing with

**[16:19]** it. Because open engine demands that we

**[16:22]** move from prompt mode to demanding real

**[16:24]** work and the framework helps us get

**[16:26]** there. Open engine helps us get there.

**[16:28]** So prompt mode might be writing a

**[16:29]** follow-up email. Work mode might be

**[16:31]** here's the client call transcript,

**[16:33]** here's the decision we made, here's the

**[16:34]** promise I don't want to overstate,

**[16:37]** here's the calendar constraints. You

**[16:39]** draft the follow-up agent, flag what

**[16:41]** needs my judgment, and leave notes that

**[16:43]** I can review later.

**[16:45]** See? That's a full statement of work

**[16:47]** right there. And you can actually pass

**[16:48]** that to another agent to review using

**[16:50]** open engine, too, if you want a second

**[16:51]** opinion, which a lot of people do,

**[16:53]** especially on client-facing

**[16:54]** communication. You could have a whole

**[16:56]** agent that just reviews for brand

**[16:57]** language. I'll give you another couple

**[16:59]** examples. Prompt mode might be, "Hey,

**[17:01]** summarize this support ticket." You ask

**[17:03]** your codex to do that, you ask your

**[17:04]** cloud to do that. Work mode would be,

**[17:06]** "Classify this ticket, attach the

**[17:08]** customer history, identify whether this

**[17:10]** was a known issue, create a product task

**[17:12]** only if it meets my escalation rule, and

**[17:14]** show exactly where you stopped work and

**[17:17]** why." Or this one, prompt mode would be

**[17:19]** help me change my schedule. Work mode

**[17:21]** would be the pickup time for the kids

**[17:22]** has changed, check what it affects,

**[17:24]** draft the two messages that might be

**[17:26]** needed to the school, and wait for

**[17:28]** approval before anything leaves the

**[17:29]** system. The model can be the same here,

**[17:32]** but the assignment is much more clear

**[17:34]** and the ability to hand off to multiple

**[17:36]** agents or to a human as you determine is

**[17:39]** really, really easy. We need to stop

**[17:42]** assuming that we are the glue between

**[17:45]** all of the AI systems that we work for.

**[17:48]** Otherwise, that the AI is prompting us

**[17:51]** and we're just working for the AI

**[17:52]** instead of the other way around. We want

**[17:54]** to be in a place where the work can move

**[17:56]** across the tools that we're already

**[17:58]** using and that's the open engine

**[18:00]** promise. Because our teams don't really

**[18:02]** live in one AI tool. I don't know anyone

**[18:05]** who is curious about AI who actually

**[18:08]** uses only one tool. And especially if

**[18:11]** you get two people together, it's not

**[18:12]** one tool. It's like two different tools,

**[18:14]** three, five. I often see six different

**[18:16]** tools between two people and you're not

**[18:18]** going to expect people to actually

**[18:19]** change that. You actually just want to

**[18:21]** give people a queue where all of their

**[18:23]** AIs can talk to each other. So, I'm not

**[18:25]** going to make you a big promise here.

**[18:26]** I'm not saying open engine can run your

**[18:28]** company. I don't want to say that. I

**[18:30]** don't want to say open engine can run

**[18:31]** your household. What I want to say is

**[18:34]** the next useful AI is not another

**[18:37]** private assistant. It's a queue where

**[18:39]** your agents can all work together and

**[18:41]** move stuff forward. And that matters on

**[18:43]** any team and increasingly we're all

**[18:45]** managing teams of agents because teams

**[18:47]** need owners and status and receipts and

**[18:49]** review. And if you don't tackle that,

**[18:51]** something gets lost, something drops

**[18:52]** through the cracks and you have

**[18:53]** household consequences for that, you

**[18:55]** have work consequences for that. If we

**[18:57]** go back to earlier in this video, I

**[18:59]** talked about the idea that we are the

**[19:00]** hallway between AI agents. Open engine

**[19:04]** is what I built to make that hallway

**[19:06]** into software transparent and smooth and

**[19:10]** easy so we humans stop carrying all of

**[19:13]** that load. It It's not up to us to be

**[19:16]** the invisible laborers for our AIs. It

**[19:20]** is up to good frameworks and systems to

**[19:23]** let work move from where it started to

**[19:26]** where it needs to go. With enough

**[19:27]** context, the next loop can do something

**[19:29]** useful. The test for open engine is

**[19:31]** really simple. Can the work get out of

**[19:34]** your chat? Can it get out of your chat?

**[19:36]** Can it carry with it the sources that it

**[19:38]** has to do the work? Can it respect

**[19:41]** limits and can it come back and say,

**[19:43]** "This is what I did and this is what I

**[19:45]** didn't do and this is the receipt."

**[19:47]** Because if the answer is yes with open

**[19:50]** engine, even in a small way, then the

**[19:52]** entire agent conversation changes for

**[19:54]** you. You stop asking only what one AI

**[19:57]** can do in a session. You start asking

**[19:59]** what kind of work your whole system can

**[20:00]** carry without you being the messenger.

**[20:03]** That's the promise of open engine. Not

**[20:05]** agents replacing our judgment, not one

**[20:08]** agent to rule them all, but all of the

**[20:10]** mess of our AI systems just stitched

**[20:14]** together with a clean framework so

**[20:17]** agents can carry work to the point where

**[20:20]** judgment is needed and not bother us for

**[20:22]** the annoying handoffs along the way.

**[20:25]** That's the version of autonomy I

**[20:26]** actually want. That's what I've been

**[20:28]** living with. That's what I'm sharing

**[20:29]** with you today. If you want that, I have

**[20:31]** the full guide up. Uh the Substack

**[20:33]** community gets it first. We have an

**[20:35]** active Slack where people are building

**[20:37]** on this. I encourage you to join that as

**[20:39]** well. Uh and you can see exactly the the

**[20:41]** demo that I showed you and also a full

**[20:43]** guide that you can hand to your AI to

**[20:45]** get this started today. And remember, so

**[20:47]** that's open engine. If you have trouble

**[20:49]** with handoffs as I have had and as so

**[20:51]** many folks I have had have struggled

**[20:53]** with, this is for you. Go make your life

**[20:57]** easier. Go get the headaches out of the

**[20:58]** way. Go stop copying and pasting and

**[21:01]** just make make that all go away.

**[21:04]** Get open engine and get it sorted out so

**[21:06]** that you save hours. That's actually my

**[21:09]** personal goal is I want less wasted

**[21:11]** human hours. I want us to spend less

**[21:13]** hours on needless agent coordination.

**[21:15]** That would be my success. So, if you see

**[21:17]** this and you're like, "Oh my gosh, this

**[21:19]** is for me." Tell me in the chat, in the

**[21:22]** comments, what you are going to use this

**[21:24]** for. Tell me which AI systems you're

**[21:26]** going to coordinate. Tell me if you're

**[21:27]** working with agents, with a team, or

**[21:28]** with your partner.

**[21:29]** Uh whatever it is and and you want a

**[21:31]** framework that makes the AI and the

**[21:33]** human actually work together and you're

**[21:34]** going to use this to solve it, tell me

**[21:36]** what it is. One, we'll improve Open

**[21:37]** Agent and continue to make it better as

**[21:39]** you give us feedback. But, but two, I

**[21:42]** want to know how much pain we're going

**[21:45]** after here because that's what I'm

**[21:46]** interested in. I'm interested in AI that

**[21:48]** kills our pain. And this is a pain that

**[21:50]** has arisen since AI agents got more

**[21:52]** capable and it's just gotten worse. And

**[21:54]** so, in the era of Open Claw, in the era

**[21:57]** of Codex, in the era of Claude, we need

**[21:59]** something like Open Agent. I hope you've

**[22:00]** had fun seeing this demo. So, go get

**[22:02]** yours today.
