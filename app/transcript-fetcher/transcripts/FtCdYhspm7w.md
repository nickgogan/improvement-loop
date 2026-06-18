# Transcript: FtCdYhspm7w

**URL:** https://www.youtube.com/watch?v=FtCdYhspm7w
**Segments:** 797

---

## Full Text

It does not get bigger than this. Anthropic accidentally leaked Claude Code. This is a two and a half billion dollar run rate product. This is the secret sauce that describes how Clawed Code works. And what's inside is actually not what most people are focused on. I have read the blogs, the breathless coverage, the hype, and what I see is a ton of focus on, you know, the feature flags that are not toggled on, what Cloud Code is going to release in the next few weeks. That's fine. That's going to last for a few weeks. I wanted to see what is the underlying architecture for cloud code that sustains this $2 and half billion dollar business and specifically what are the baseline infrastructural insights for running agents successfully for businesses that we can learn from and port over how can we take some of claude code secret sauce now that it's leaked now that it's available to everyone and we can say okay what can we learn how can we build this effectively and so I'm going to talk about the things I learned reviewing the repo in detail I am also releasing a special skill to help you to assess your own agentic framework and agentic harness and to recommend changes to your agentic harness based on what we've learned from claude code. I think that's one of the most solid useful actionable takeaways we can get from this. It's not really about the hypiness of we get to take a peek at the next two weeks of Anthropics roadmap. They ship fast. Pretty soon we're going to be right through that window and they're going to be on to shipping other stuff. It's really about how we can learn what Anthropic is building under the surface that sustains an agentic production system that's successful. That's what matters. If you're wondering, is this just all about Claude code? The answer is no. What we can learn from claude code applies to us all. So, I'm also releasing a skill that's tuned to codec specifically that ties in lessons we can learn from cloud code so we can start to cross-pollinate and really understand how agents drive and sustain work over time regardless of the LLM of choice. But before we get there, I want to call a spade a spade. This is the second significant leak from Anthropic in the last few days and it's worth asking ourselves why. Earlier this week, Fortune reported that Enthropic left draft blog materials describing its new model, Claude Mythos, on a server that was open to the public. Now, 5 days later, a build configuration error has ended up leaking Claude code. Now, I want to be clear, these are entirely different mechanisms. They're different systems, but it did all happen to the same company in the same week. I'm not trying to say that Mythos or any other AI model caused this leak. Anthropic says it was human error, and there's certainly no public evidence to the contrary. But the pattern raises a question for me that every team building with AI assisted development should be asking. Is your development velocity outrunning your operational discipline? In light of that, it's telling to me that the developer community's default conjecture for how cloud code got leaked involves an AI model making an error. The theory circulating on X flagged explicitly as conjecture by Alex Vulkov is that someone inside anthropic got switched to adaptive reasoning mode on accident and their clog code session fell back to sonnet and the model committed the map file which was the leak as part of a routine build step. Now, we don't know for sure that that's what happened, but the fact that the AI committed the build artifact that leaked the AI's own code is a part of the discourse is something we can reasonably guess is a chain of events that looks really reasonable from the outside, that tells you everything you need to know about where we are with velocity and build security in 2026. When the AI writes 90% of your code, as Enthropic says it does, and your engineers are shipping multiple releases per engineer per day, maybe up to five, the surface area for configuration drift is really high. And whatever the exact chain of events, it's clear to me that that velocity had some consequences this week. There were two significant leaks for Anthropic, and I'll be curious to see how the team tightens up and goes back to operational discipline. Something tells me they will find a way to do that without significantly adjusting their shipping cadence. the velocity is here to stay and the operational cadence is going to catch up. Ironically, some of the stuff that we're going to talk about when we talk about primitives and AI is exactly the kind of boring stuff that I suspect Anthropic will lean on to tighten up and prevent this happening again. It's stuff like build pipeline configuration, the publish step validation, stuff that you need to do to make sure that you're not accidentally leaking things. And I suspect they're going to revisit those boring basic primitives along the way as they continue to clean up after this mess. Now, what can we learn about the incredible plumbing that makes Claude code possible? You might think, incredible plumbing, Nate, what are you talking about? Well, it's actually true. This is the secret sauce. We've never had a peak behind the curtain at Claude Code. I've done the work to organize this in terms of 12 specific primitives that are organized into multiple tiers. So, I've gone through, this is not an order of presentation. This is not an order in the codebase. This is an order that is rational and makes sense for us to understand how anthropic is building. So I did that codebase analysis for you. And so these are presented in the order you should think about them when building your own agentic system, which I think makes sense. So there are 12 categories, three tiers. And for each primitive, I'm going to name three things, right? The universal pattern, the design principle that applies to any agentic system. Claude codes manifestation, right? One specific production grade implementation of that pattern. and then how this might look in your system beyond that. Right? So, let's jump in. If you're building an agent from scratch, what can claude code tell you about how to do it right? What are some initial non-negotiables? Number one, think about tool registry with metadata first design. This is not super new if you've been following Claude code closely, but boy, do we get a ton of detail about it from the Cloud Code leak. The pattern is really clear. You define your agents capabilities as a data structure before writing any implementation code. The registry should answer what exists and what does it do without executing anything. So how does this look inside cloud code? What I found is that claude code maintains two parallel registries. A command registry with 207 entries for userfacing actions and a parallel tool registry with 184 entries for model facing capabilities. Every single entry there it's like a dictionary. It carries a name, it carries a source hint and it carries a responsibility description. The registries are a source of truth and the implementations from there load on demand. And so this separation is not dependent on the model to infer. This is structural. Now why does this matter? If you don't have a clean tool registry, you can't filter tools by context. You can't introspect your system without triggering side effects. And every new tool is going to require changes in your orchestration code. The registry is a foundation everything else builds on. And so if you're thinking about how to apply this to you, like think about a list tools function that returns metadata for all registered capabilities without necessarily having to invoke them, right? You should be able to support runtime filtering. You should be able to define each tool clearly by a name and a short description. And you should be able to write that function before any kind of ask to the model to think about executing or picking a tool. So that's tool registry. Super basic. Another day one thing I would look at if I were building an agent based on the clog code leak is the permission system. Not all tools carry the same risk. Categorize that risk and apply different approval tiers per category. And so what I found in the code is that Claude segments its capabilities into three different trust tiers. There's built-in always available highest trust tier tools. There are plug-in tools which are medium trust and they can be disabled on command and then there are skills which are userdefined and are lowest trust by default. Yes, a skill is considered a tool in this scheme. Every tier has different loading behavior, different permission requirements and different failure handling. And the shell execution tool alone, which is called bash tool, has an 18 module security architecture. That's not a typo, right? That's 18 separate modules from pre-approved command patterns to destructive command warnings to get specific safety checks to sandbox termination. They're really careful with it because bash tool as a shell execution script could go very wrong very fast. And this is all relevant because this gets at exactly the security concerns we've seen dominating the conversation since the mythos leaks. It's open claw. If your agent bottom line can take actions in the world, if your agent can execute code, if it can call APIs, if it can send messages, if it can modify files and you don't have a permissions layer, you have just a demo, right? You don't have a product. You don't have anything that you can like execute on safely. And so when you think about an 18 module security stack for a single tool, I don't think Anthropic is being paranoid. I think it's what separates a system that works safely at two and a half billion dollar run rate from one that works in a little notebook. And so what does this imply for how you should think about security and permissions? Well, first think about pre-classification. Is this action readon? Is it mutating? Is it potentially a destructive action? Do you have pre-approved patterns that are known safe? Do you have destruction detection where you can flag actions that might delete or overwrite ahead of time? Do you have domain specific safety? Are you looking at targeted checks for specific risk factors you're worried about? Do you have permission logging? Do you record every decision granted or denied with enough context to replay that decision? These are the things you need to be thinking about that are already in the cloud code leak. Number three, not glamorous, but super important. Session persistence that survives crashes. So the pattern we see is really simple. Your agent session is not just the conversation history. It's a recoverable state that includes conversation. It includes usage metrics. It includes permission decisions and it includes configuration. It's the whole ball of wax. If any of those are missing when you resume the session isn't going to work the same as the original. And what I discovered when I got into the code is that clawed code persists those sessions in that way like in in its entirety in the form of JSON files and it captures session ID. It captures messages. It captures the token usage in and out and the query engine essentially can be fully reconstructed from that stored session. You can reinstantiate an entire session after a crash with load, a reconstruct transcript, restore counters, and you can return essentially a fully functional Agentic engine from a crash. Why would you care about this? Well, agents crash. They crash all the time. Connections drop, users close tabs. If your agent can't reliably resume where it left off, including what tools were available, what permissions were granted, how many tokens were consumed, then every single interruption is a restart. And every restart ends up being a degraded experience for the customer. And so you should build your version of this, right? You should look at a session state structure that captures everything needed to resume. You should look at how you can persist after a significant event, not just at shutdown. And you should be able to build a resume session function that reconstructs full agentic state, not just conversation history. Number four, workflow state. This is a really big deal, but it's not getting talked about at all. The pattern is simple. When you resume a conversation, it is not the same thing as resuming a workflow. So a chat transcript answers, what have we said? A workflow state answers, what step are we in? What side effects have happened as a result of that workflow? Is this operation safe to retry? and what should happen after we restart. And this is very tightly connected to session persistence, but it is a different thing. Almost every agentic framework conflates conversation state with task state. And they're different problems with different solutions. And so if you don't have a workflow state, you can reinstantiate the agent to be exactly where it was, but it won't remember where it was in the workflow automatically because the workflow is something that persists beyond the agent. Your agent will not survive a crash mid tool execution without potentially duplicating a write or double sending a message or rerunning which is a very expensive operation and potentially very destructive. You need to have a clear way to retry a workflow and you need to know where you were when the agent crashed. So you should be modeling longunning work as very explicit states. Planned awaiting approval is an example of a state executing as an example of a state. Waiting on an external party is an example of a state. You want to persist those checkpoints all the time. It's like when we were in the 1990s and we saved our game every two seconds because we didn't want to lose the game if the computer crashed. Same idea. Be paranoid. Save your workflow state. Number five, where are you at with your token budget? What I discovered is that Claude Code's query engine configuration defines very hard limits on token usage. It has a maximum number of turns in a conversation. It has a maximum budget for tokens in a conversation. and has a compaction threshold where it will autocompact the conversation. Every turn will calculate projected token usage. If the projection exceeds the budget, the execution is just going to stop with a structured stop reason before an API call is made. And this is confirmed from how we actually use Claude in the wild. This is critical because without budget tracking, you're going to discover you've exceeded your token limits, right? This is just very common sense. You're going to have a runaway loop and spend money you didn't intend to spend. And so Claude is actually putting in checks that are not beneficial to Enthropic, they're beneficial to the long-term health of the customer here because in the short-term interest of Anthropic, you'd love it to burn tokens and spend money with Anthropic. Anthropic being a really responsible citizen here and saying, "We don't want you to have runaway budget spending that you do not clearly intend. It's the same way that Amazon enables returns, which may not be good for Amazon in the short term, but increase customer trust in the long term." Same deal. They are increasing customer trust by making it easy to track tokens. You should also be building if you are building agents token budgeting. You should have input tokens, output tokens, budgets, hard stops. It's a non-negotiable. It's just responsible building in 2026. Number six is a really big one. It's something that is more unique to Claude and is a real trust builder over time. Claude is invested in structured streaming events. This is what we mean when we talk about stream of thought from Claude, right? So the pattern is pretty clear and we see it on the front end all the time. Streaming isn't just about showing text. Every streaming event that you see while the model's running is an opportunity for you to find out what is going on with that model, right? It has to communicate a system state to you. So it needs to be talking about what tools the agent is thinking about using, how many tokens have been consumed, whether the agent is wrapping up. I don't know about you, but I use that streaming state all the time with Claude because it tells me where the model is going and I will sometimes intervene in the model's train of thought and type a message because I have seen what it's thinking about and I know it's going off track. So, it's extremely useful, but it's not automatic. You have to design for it. And so what I discovered is Claude codes query engine emits typed events that are used in the stream like message start command match tool match basically all kinds of typed events that it can call upon as it's constructing this query stream. And what's critical is if there's a crash if there's an issue. Do you see how many times I've talked about crashes and issues? Good engineering assumes a failure path and plans for it. In this case, the clawed team has assumed that sometimes the agent will crash and includes a special typed event with a reason for the crash as the last message that the stream sends if there's an issue. It's like a little black box from a crash. So, when you're thinking about how you send messages back, don't just assume that you can send raw chain of thought or whatever. Take the time to send reasonable streamed events that communicate real information to the user and that allow the user to understand what is going on and make sure you plan for crashes. Okay, number seven is related. It's system event logging. If number six was about streaming events and kind of what the model is thinking, maybe some refined chain of thought there. System event logging is when something goes wrong again the failure cases think about the engineering into failure cases. This is one of the meta. When something goes wrong, the conversational transcript needs to tell the user what the agent did, not just what it said. And so, separate from the conversation, separate from streaming events, claude code maintains a history log of system events. It is a source of truth. What context it loaded? What was its registry initialization like? What routing decisions did Claude make? What execution counts did Claude have? What permission denials or approvals did Claude experience? Every single event has a category and is presented with structured details so you can easily reconstruct an agentic run. This is what you do when you are building a system that you intend for enterprise. When you are building something you intend to run seriously, this is how you prepare. And so if you're trying to build a serious agent, you need to think about event logs. You need to think about how the system maintains a record of not just what was said, but what was done and how you can provably walk that back. Number eight, Clawed Code takes verification seriously and this happens in two levels and I want to talk about each of them because we only see one normally. The one you see is really obvious. I think it's quick to talk about. You see Claude having a separate step to check its work when you go through the stream of events. That's expected and that's something that Claude code explicitly provides for. It's part of the harness. Verify that the work done was correct. Yay. Good job. A+. But we're not done yet. Part two, which I think is really critical that Claude code also thinks about in the leak is you need to recognize that you also need to be able to verify changes that you the human make to the agentic harness. So it's not just did a given agent run complete successfully. That's important and that's good. It is also when I make a change to the harness and I change every subsequent agent run, am I doing so with confidence that I'm not breaking something? And that is where you have special verification tests that should test whether the model still works against common guardrails. So things like do we have destructive tools always requiring approval after we make this change because that's a reasonable guardrail. Or when tokens run out, what happens to the model? Does it gracefully stop as we would expect or is there some sort of hard crash? These are things that you would want to have as guardrails on any agentic experience. You should name them. You should log them. And this is that second level of verification that's in a harness that we don't think about a lot because you have to provide for the harness evolving. Okay, those were day one basics. Those are things that I often see teams consider late or never when they're putting a harnesses together. Now, we're going to move toward operational maturity and think about larger and deeper lessons we can learn. I'm going to give you four of them and if you want more, I've written them up on the substack. Number one here is tool pool assemblies. Say that five times fast. What we're talking about is the idea that if you have 184 tools, Claude isn't going to assemble all of those tools into a usable pool on every agent run. Instead, it is going to assemble a sessionspecific tool pool, a group of tools that will be used to get the run done based on mode flags, based on permission context, based on deny lists, etc. What you need to learn as a designer is that you need to think about the idea that a generalpurpose agent may need to assemble a short list of tools dynamically when preparing for a run. And that's something that we typically see hard-coded in a lot of enterprise workflows where they say these are the tools available. What Claude is suggesting is that if you have a more general purpose problem solving agent, you may want to give it a wider tool subset that it can read efficiently and then let it pick from that tool list what it wants for a given row. Number two has been talked about a lot. Transcript compaction. I want to get into it a little bit more. So conversation history is obviously a token expensive resource and claude code automatically manages that by compacting it after a configurable number of turns and it keeps recent entries when it compacts and it tends to discard the older ones. The transcript store tracks whether it's been persisted to avoid data loss. You want to think about how you build automatic compaction for longer running agents. what your threshold is, what you're compacting, what you're keeping, how you know if what you're keeping is correct. This is a really hot commodity as we think about longer running agents because you have to think about how you initially keep the instruction that gets the agent started, but also how you cut intervening conversational turnpoints or intervening actions that are not relevant to the agent's present state in a way that allows the agent to save significant space. So, compaction is one. We've already talked about it. It's great to see how cloud code does it behind the scenes. There's going to be a lot more effort going into this for everybody in the next few months. Number three, this is a little bit more advanced, but think about your permission audit trail. I talk about permissions as something you need to be ready to sort of talk about and audit all the time, but Claude Code actually makes this easy because they don't make permissions just a boolean gate that is yes or no. Instead, they make permissions state a first class object that is easy to query. And Claude actually builds three separate permission handlers to serve different contexts, right? It has an interactive handler for a human in the loop. It has a coordinator when you have a multi- aent orchestration and the orchestrator agent needs to hand out permissions. And it also has a swarm worker level where you have autonomous execution that's being managed by an orchestrator agent. So that's three different types of agent that all need different permission structures and claude code thinks about all of them in the permission architecture. So should you. And last but not least, claude code has an agent type system that as far as I know was not leaked before now. So, Claude Code defines six built-in agent types. Explore, plan, verify, guide, general purpose, and status line setup. Each of these agent types comes with its own prompt, its own allowed tools, its own behavioral constraints. Like an explore agent, by definition, cannot edit files. A plan agent doesn't execute code. The transferable lesson here is not just spawn agents randomly like you're cloning minions. It's actually to constrain roles really sharply when you split work out and constrain them in a number of observable types so that you can manage those types to control your overall agent population and to manage the efficiency of the work they're able to produce. This is a great way to think about larger multi- aent systems. Okay, that was a lot. Let's hop briefly into what I'm releasing and what I built. I'm releasing an agenta harnesses skill that helps us to operationalize some of this for our own agents that we're running. And yes, if you're wondering if this works on like your open claw agent, if it's something you can use for any agentic setup, you can absolutely run it and it will give you some good tips. So what does this thing do? It has two modes. Design mode is going to enable you to describe the product that you're building like a chat assistant or a workflow orchestrator or a code agent, whatever agent you want to build. And the skill is going to walk you through a structured design process and it's going to recommend a harness shape. It's going to identify the minimum useful set of primitives. It's going to sequence the implementation into phases and it's going to define verification criteria and all of that is going to happen before you write a line of code for the harness. It doesn't just generate boiler plate here, right? It generates an architecture with rationale that is deeply rooted in what we can learn for how the most successful agent in production today runs. It also has a second mode, evaluation mode. If you already have an existing harness, you can point it at your codebase. You can point it at your cloud.mmarkdown, your architecture documents, and it's going to tell you what's missing, what's not there, what could you learn from that you might not know about with this cloud code release. So, it will evaluate every dimension across the codebase in light of the principles I've identified in this video here, architecture, safety, and permissions, state and durability, etc. and it's going to return findings ordered by severity, by a prioritized upgrade path, and specific tests that confirm the fixes work. Now, why is this a skill and not just a document? I'll put it pretty simply. A skill allows you to do something dynamically with the AI. And that's what this is all about. It's about actually implementing and fixing the agentic setups we have today and designing better agentic setups based on what claude code can teach us. I think that's a much more sustainable path to utility to usefulness based on this leak than just trying to hype up the drama. And yes, I built the skill for both claude code as a clouded skill package and also for OpenAI's codecs with codec specific metadata path patterns and agent routing. And the core logic is identical, right? The way it assesses primitives, the way it assesses evaluation dimensions, the way it assesses the design playbook. The reason for that is that I think these primitives scale pretty well. And this was a very deliberate choice on my part to make sure that we are all thinking about the primitives of agentic development as things we can learn from together and use to build more solid systems regardless of our LLM of choice. And I'll be honest here, the skill is opinionated. It biases toward a lean solo maintainable architecture unless you have a good reason not to. It starts with single agent design unless you give it really good reasons that push for a multi-agent design. It biases towards simplicity because simplicity is maintainable. And this is very intentional because the most common failure mode that I've seen in agentic systems, it's not underengineering. It's actually overengineering. Building a really complicated multi-AN coordination layer before you have a working permission system, right? Or implementing a plug-in marketplace before your sessions can survive crashes. So the skill is going to push back on unnecessary complexity because premature complexity is where frankly most projects go to die. If we step back and look at the claw code leak after the dust settles, what is the takeaway here? The larger takeaway is that building agents is 80% non-glamorous plumbing work and 20% AI. So much of what I spent time talking about in this video is stuff that most people will roll their eyes at, but it is the exact boring stuff that makes an agent successful at a multi-billion dollar level. This is what makes it possible to serve to millions and millions of people. You have to think about failure cases. You have to think about security. You have to think about how the agent recovers from from crashes. You have to think about how you have typed events that enable an agent to choose from a limited schema and come back with useful information across a range of scenarios. This is the architecture of scale. And it's amazing to me that so much of this is essentially a function of good back-end engineering. And in the sense that hasn't evolved. We're just applying good back-end engineering to these agentic pipelines and discovering that hey that works pretty well. So the plumbing isn't very glamorous maybe, but I'm talking about it because I believe it's the whole game and I'm launching a skill to make it easy because I don't want it to be hard for people to figure this out. You should not have to go through the cloud code leak yourself to infer these principles. We should be able to just pull them out and have a conversation about them as a community. So, you tell me in the comments, what did you learn from Claude Code that I didn't mention? And what would you like to see included in future agent work that you think we can all pull from Claude Code and make our agents better? I'd love to hear. Cheers.

---

## Timestamped Segments

**[0:00]** It does not get bigger than this.

**[0:01]** Anthropic accidentally leaked Claude

**[0:04]** Code. This is a two and a half billion

**[0:06]** dollar run rate product. This is the

**[0:08]** secret sauce that describes how Clawed

**[0:10]** Code works. And what's inside is

**[0:13]** actually not what most people are

**[0:14]** focused on. I have read the blogs, the

**[0:17]** breathless coverage, the hype, and what

**[0:19]** I see is a ton of focus on, you know,

**[0:20]** the feature flags that are not toggled

**[0:22]** on, what Cloud Code is going to release

**[0:24]** in the next few weeks. That's fine.

**[0:26]** That's going to last for a few weeks. I

**[0:28]** wanted to see what is the underlying

**[0:30]** architecture for cloud code that

**[0:32]** sustains this $2 and half billion dollar

**[0:33]** business and specifically what are the

**[0:36]** baseline infrastructural insights for

**[0:38]** running agents successfully for

**[0:40]** businesses that we can learn from and

**[0:43]** port over how can we take some of claude

**[0:45]** code secret sauce now that it's leaked

**[0:47]** now that it's available to everyone and

**[0:49]** we can say okay what can we learn how

**[0:50]** can we build this effectively and so I'm

**[0:52]** going to talk about the things I learned

**[0:54]** reviewing the repo in detail I am also

**[0:57]** releasing a special skill to help you to

**[1:01]** assess your own agentic framework and

**[1:03]** agentic harness and to recommend changes

**[1:05]** to your agentic harness based on what

**[1:08]** we've learned from claude code. I think

**[1:10]** that's one of the most solid useful

**[1:12]** actionable takeaways we can get from

**[1:14]** this. It's not really about the hypiness

**[1:16]** of we get to take a peek at the next two

**[1:18]** weeks of Anthropics roadmap. They ship

**[1:20]** fast. Pretty soon we're going to be

**[1:22]** right through that window and they're

**[1:24]** going to be on to shipping other stuff.

**[1:25]** It's really about how we can learn what

**[1:29]** Anthropic is building under the surface

**[1:32]** that sustains an agentic production

**[1:34]** system that's successful. That's what

**[1:36]** matters. If you're wondering, is this

**[1:38]** just all about Claude code? The answer

**[1:39]** is no. What we can learn from claude

**[1:41]** code applies to us all. So, I'm also

**[1:43]** releasing a skill that's tuned to codec

**[1:45]** specifically that ties in lessons we can

**[1:47]** learn from cloud code so we can start to

**[1:49]** cross-pollinate and really understand

**[1:52]** how agents drive and sustain work over

**[1:55]** time regardless of the LLM of choice.

**[1:57]** But before we get there, I want to call

**[1:59]** a spade a spade. This is the second

**[2:02]** significant leak from Anthropic in the

**[2:04]** last few days and it's worth asking

**[2:05]** ourselves why. Earlier this week,

**[2:07]** Fortune reported that Enthropic left

**[2:08]** draft blog materials describing its new

**[2:10]** model, Claude Mythos, on a server that

**[2:13]** was open to the public. Now, 5 days

**[2:15]** later, a build configuration error has

**[2:17]** ended up leaking Claude code. Now, I

**[2:19]** want to be clear, these are entirely

**[2:20]** different mechanisms. They're different

**[2:21]** systems, but it did all happen to the

**[2:23]** same company in the same week. I'm not

**[2:25]** trying to say that Mythos or any other

**[2:26]** AI model caused this leak. Anthropic

**[2:28]** says it was human error, and there's

**[2:30]** certainly no public evidence to the

**[2:31]** contrary. But the pattern raises a

**[2:33]** question for me that every team building

**[2:35]** with AI assisted development should be

**[2:37]** asking. Is your development velocity

**[2:39]** outrunning your operational discipline?

**[2:41]** In light of that, it's telling to me

**[2:43]** that the developer community's default

**[2:45]** conjecture for how cloud code got leaked

**[2:47]** involves an AI model making an error.

**[2:49]** The theory circulating on X flagged

**[2:52]** explicitly as conjecture by Alex Vulkov

**[2:54]** is that someone inside anthropic got

**[2:56]** switched to adaptive reasoning mode on

**[2:58]** accident and their clog code session

**[3:00]** fell back to sonnet and the model

**[3:02]** committed the map file which was the

**[3:04]** leak as part of a routine build step.

**[3:07]** Now, we don't know for sure that that's

**[3:09]** what happened, but the fact that the AI

**[3:11]** committed the build artifact that leaked

**[3:13]** the AI's own code is a part of the

**[3:16]** discourse is something we can reasonably

**[3:17]** guess is a chain of events that looks

**[3:20]** really reasonable from the outside, that

**[3:22]** tells you everything you need to know

**[3:23]** about where we are with velocity and

**[3:26]** build security in 2026. When the AI

**[3:28]** writes 90% of your code, as Enthropic

**[3:30]** says it does, and your engineers are

**[3:32]** shipping multiple releases per engineer

**[3:34]** per day, maybe up to five, the surface

**[3:36]** area for configuration drift is really

**[3:38]** high. And whatever the exact chain of

**[3:40]** events, it's clear to me that that

**[3:42]** velocity had some consequences this

**[3:44]** week. There were two significant leaks

**[3:46]** for Anthropic, and I'll be curious to

**[3:48]** see how the team tightens up and goes

**[3:50]** back to operational discipline.

**[3:52]** Something tells me they will find a way

**[3:53]** to do that without significantly

**[3:55]** adjusting their shipping cadence. the

**[3:57]** velocity is here to stay and the

**[3:59]** operational cadence is going to catch

**[4:00]** up. Ironically, some of the stuff that

**[4:02]** we're going to talk about when we talk

**[4:04]** about primitives and AI is exactly the

**[4:06]** kind of boring stuff that I suspect

**[4:08]** Anthropic will lean on to tighten up and

**[4:10]** prevent this happening again. It's stuff

**[4:12]** like build pipeline configuration, the

**[4:15]** publish step validation, stuff that you

**[4:17]** need to do to make sure that you're not

**[4:19]** accidentally leaking things. And I

**[4:22]** suspect they're going to revisit those

**[4:23]** boring basic primitives along the way as

**[4:26]** they continue to clean up after this

**[4:27]** mess. Now, what can we learn about the

**[4:29]** incredible plumbing that makes Claude

**[4:31]** code possible? You might think,

**[4:32]** incredible plumbing, Nate, what are you

**[4:34]** talking about? Well, it's actually true.

**[4:36]** This is the secret sauce. We've never

**[4:39]** had a peak behind the curtain at Claude

**[4:40]** Code. I've done the work to organize

**[4:43]** this in terms of 12 specific primitives

**[4:46]** that are organized into multiple tiers.

**[4:48]** So, I've gone through, this is not an

**[4:49]** order of presentation. This is not an

**[4:50]** order in the codebase. This is an order

**[4:52]** that is rational and makes sense for us

**[4:54]** to understand how anthropic is building.

**[4:56]** So I did that codebase analysis for you.

**[4:58]** And so these are presented in the order

**[5:00]** you should think about them when

**[5:02]** building your own agentic system, which

**[5:03]** I think makes sense. So there are 12

**[5:05]** categories, three tiers. And for each

**[5:07]** primitive, I'm going to name three

**[5:08]** things, right? The universal pattern,

**[5:11]** the design principle that applies to any

**[5:12]** agentic system. Claude codes

**[5:14]** manifestation, right? One specific

**[5:16]** production grade implementation of that

**[5:18]** pattern. and then how this might look in

**[5:20]** your system beyond that. Right? So,

**[5:22]** let's jump in. If you're building an

**[5:23]** agent from scratch, what can claude code

**[5:25]** tell you about how to do it right? What

**[5:27]** are some initial non-negotiables? Number

**[5:30]** one, think about tool registry with

**[5:32]** metadata first design. This is not super

**[5:34]** new if you've been following Claude code

**[5:36]** closely, but boy, do we get a ton of

**[5:37]** detail about it from the Cloud Code

**[5:39]** leak. The pattern is really clear. You

**[5:41]** define your agents capabilities as a

**[5:43]** data structure before writing any

**[5:45]** implementation code. The registry should

**[5:47]** answer what exists and what does it do

**[5:51]** without executing anything. So how does

**[5:53]** this look inside cloud code? What I

**[5:55]** found is that claude code maintains two

**[5:58]** parallel registries. A command registry

**[6:00]** with 207 entries for userfacing actions

**[6:03]** and a parallel tool registry with 184

**[6:06]** entries for model facing capabilities.

**[6:09]** Every single entry there it's like a

**[6:10]** dictionary. It carries a name, it

**[6:12]** carries a source hint and it carries a

**[6:14]** responsibility description. The

**[6:16]** registries are a source of truth and the

**[6:18]** implementations from there load on

**[6:20]** demand. And so this separation is not

**[6:22]** dependent on the model to infer. This is

**[6:24]** structural. Now why does this matter? If

**[6:26]** you don't have a clean tool registry,

**[6:28]** you can't filter tools by context. You

**[6:30]** can't introspect your system without

**[6:32]** triggering side effects. And every new

**[6:34]** tool is going to require changes in your

**[6:36]** orchestration code. The registry is a

**[6:38]** foundation everything else builds on.

**[6:40]** And so if you're thinking about how to

**[6:41]** apply this to you, like think about a

**[6:43]** list tools function that returns

**[6:45]** metadata for all registered capabilities

**[6:47]** without necessarily having to invoke

**[6:49]** them, right? You should be able to

**[6:51]** support runtime filtering. You should be

**[6:52]** able to define each tool clearly by a

**[6:54]** name and a short description. And you

**[6:56]** should be able to write that function

**[6:58]** before any kind of ask to the model to

**[7:01]** think about executing or picking a tool.

**[7:02]** So that's tool registry. Super basic.

**[7:04]** Another day one thing I would look at if

**[7:06]** I were building an agent based on the

**[7:08]** clog code leak is the permission system.

**[7:11]** Not all tools carry the same risk.

**[7:13]** Categorize that risk and apply different

**[7:14]** approval tiers per category. And so what

**[7:17]** I found in the code is that Claude

**[7:19]** segments its capabilities into three

**[7:20]** different trust tiers. There's built-in

**[7:22]** always available highest trust tier

**[7:24]** tools. There are plug-in tools which are

**[7:27]** medium trust and they can be disabled on

**[7:29]** command and then there are skills which

**[7:31]** are userdefined and are lowest trust by

**[7:33]** default. Yes, a skill is considered a

**[7:35]** tool in this scheme. Every tier has

**[7:38]** different loading behavior, different

**[7:39]** permission requirements and different

**[7:41]** failure handling. And the shell

**[7:43]** execution tool alone, which is called

**[7:45]** bash tool, has an 18 module security

**[7:48]** architecture. That's not a typo, right?

**[7:50]** That's 18 separate modules from

**[7:53]** pre-approved command patterns to

**[7:55]** destructive command warnings to get

**[7:57]** specific safety checks to sandbox

**[7:58]** termination. They're really careful with

**[8:00]** it because bash tool as a shell

**[8:02]** execution script could go very wrong

**[8:05]** very fast. And this is all relevant

**[8:07]** because this gets at exactly the

**[8:09]** security concerns we've seen dominating

**[8:10]** the conversation since the mythos leaks.

**[8:12]** It's open claw. If your agent bottom

**[8:14]** line can take actions in the world, if

**[8:16]** your agent can execute code, if it can

**[8:18]** call APIs, if it can send messages, if

**[8:20]** it can modify files and you don't have a

**[8:22]** permissions layer, you have just a demo,

**[8:25]** right? You don't have a product. You

**[8:26]** don't have anything that you can like

**[8:27]** execute on safely. And so when you think

**[8:29]** about an 18 module security stack for a

**[8:31]** single tool, I don't think Anthropic is

**[8:34]** being paranoid. I think it's what

**[8:35]** separates a system that works safely at

**[8:37]** two and a half billion dollar run rate

**[8:39]** from one that works in a little

**[8:40]** notebook. And so what does this imply

**[8:42]** for how you should think about security

**[8:43]** and permissions? Well, first think about

**[8:45]** pre-classification. Is this action

**[8:47]** readon? Is it mutating? Is it

**[8:49]** potentially a destructive action? Do you

**[8:51]** have pre-approved patterns that are

**[8:53]** known safe? Do you have destruction

**[8:54]** detection where you can flag actions

**[8:56]** that might delete or overwrite ahead of

**[8:58]** time? Do you have domain specific

**[8:59]** safety? Are you looking at targeted

**[9:01]** checks for specific risk factors you're

**[9:03]** worried about? Do you have permission

**[9:04]** logging? Do you record every decision

**[9:06]** granted or denied with enough context to

**[9:08]** replay that decision? These are the

**[9:10]** things you need to be thinking about

**[9:12]** that are already in the cloud code leak.

**[9:14]** Number three, not glamorous, but super

**[9:16]** important. Session persistence that

**[9:19]** survives crashes. So the pattern we see

**[9:22]** is really simple. Your agent session is

**[9:25]** not just the conversation history. It's

**[9:28]** a recoverable state that includes

**[9:30]** conversation. It includes usage metrics.

**[9:32]** It includes permission decisions and it

**[9:35]** includes configuration. It's the whole

**[9:36]** ball of wax. If any of those are missing

**[9:39]** when you resume the session isn't going

**[9:41]** to work the same as the original. And

**[9:42]** what I discovered when I got into the

**[9:44]** code is that clawed code persists those

**[9:47]** sessions in that way like in in its

**[9:49]** entirety in the form of JSON files and

**[9:52]** it captures session ID. It captures

**[9:54]** messages. It captures the token usage in

**[9:57]** and out and the query engine essentially

**[9:59]** can be fully reconstructed from that

**[10:01]** stored session. You can reinstantiate an

**[10:03]** entire session after a crash with load,

**[10:06]** a reconstruct transcript, restore

**[10:08]** counters, and you can return essentially

**[10:09]** a fully functional Agentic engine from a

**[10:12]** crash. Why would you care about this?

**[10:14]** Well, agents crash. They crash all the

**[10:16]** time. Connections drop, users close

**[10:18]** tabs. If your agent can't reliably

**[10:20]** resume where it left off, including what

**[10:23]** tools were available, what permissions

**[10:25]** were granted, how many tokens were

**[10:26]** consumed, then every single interruption

**[10:29]** is a restart. And every restart ends up

**[10:31]** being a degraded experience for the

**[10:32]** customer. And so you should build your

**[10:34]** version of this, right? You should look

**[10:36]** at a session state structure that

**[10:38]** captures everything needed to resume.

**[10:40]** You should look at how you can persist

**[10:41]** after a significant event, not just at

**[10:43]** shutdown. And you should be able to

**[10:45]** build a resume session function that

**[10:47]** reconstructs full agentic state, not

**[10:50]** just conversation history. Number four,

**[10:52]** workflow state. This is a really big

**[10:54]** deal, but it's not getting talked about

**[10:55]** at all. The pattern is simple. When you

**[10:57]** resume a conversation, it is not the

**[10:59]** same thing as resuming a workflow. So a

**[11:01]** chat transcript answers, what have we

**[11:03]** said? A workflow state answers, what

**[11:06]** step are we in? What side effects have

**[11:08]** happened as a result of that workflow?

**[11:10]** Is this operation safe to retry? and

**[11:13]** what should happen after we restart. And

**[11:15]** this is very tightly connected to

**[11:16]** session persistence, but it is a

**[11:18]** different thing. Almost every agentic

**[11:21]** framework conflates conversation state

**[11:23]** with task state. And they're different

**[11:25]** problems with different solutions. And

**[11:27]** so if you don't have a workflow state,

**[11:29]** you can reinstantiate the agent to be

**[11:31]** exactly where it was, but it won't

**[11:32]** remember where it was in the workflow

**[11:34]** automatically because the workflow is

**[11:35]** something that persists beyond the

**[11:37]** agent. Your agent will not survive a

**[11:39]** crash mid tool execution without

**[11:41]** potentially duplicating a write or

**[11:43]** double sending a message or rerunning

**[11:45]** which is a very expensive operation and

**[11:47]** potentially very destructive. You need

**[11:48]** to have a clear way to retry a workflow

**[11:53]** and you need to know where you were when

**[11:55]** the agent crashed. So you should be

**[11:57]** modeling longunning work as very

**[11:59]** explicit states. Planned awaiting

**[12:02]** approval is an example of a state

**[12:03]** executing as an example of a state.

**[12:05]** Waiting on an external party is an

**[12:07]** example of a state. You want to persist

**[12:09]** those checkpoints all the time. It's

**[12:11]** like when we were in the 1990s and we

**[12:13]** saved our game every two seconds because

**[12:14]** we didn't want to lose the game if the

**[12:16]** computer crashed. Same idea. Be

**[12:18]** paranoid. Save your workflow state.

**[12:21]** Number five, where are you at with your

**[12:23]** token budget? What I discovered is that

**[12:25]** Claude Code's query engine configuration

**[12:27]** defines very hard limits on token usage.

**[12:30]** It has a maximum number of turns in a

**[12:32]** conversation. It has a maximum budget

**[12:34]** for tokens in a conversation. and has a

**[12:35]** compaction threshold where it will

**[12:37]** autocompact the conversation. Every turn

**[12:40]** will calculate projected token usage. If

**[12:43]** the projection exceeds the budget, the

**[12:45]** execution is just going to stop with a

**[12:48]** structured stop reason before an API

**[12:51]** call is made. And this is confirmed from

**[12:53]** how we actually use Claude in the wild.

**[12:54]** This is critical because without budget

**[12:56]** tracking, you're going to discover

**[12:58]** you've exceeded your token limits,

**[12:59]** right? This is just very common sense.

**[13:00]** You're going to have a runaway loop and

**[13:02]** spend money you didn't intend to spend.

**[13:04]** And so Claude is actually putting in

**[13:06]** checks that are not beneficial to

**[13:08]** Enthropic, they're beneficial to the

**[13:10]** long-term health of the customer here

**[13:11]** because in the short-term interest of

**[13:13]** Anthropic, you'd love it to burn tokens

**[13:15]** and spend money with Anthropic.

**[13:17]** Anthropic being a really responsible

**[13:18]** citizen here and saying, "We don't want

**[13:20]** you to have runaway budget spending that

**[13:23]** you do not clearly intend. It's the same

**[13:25]** way that Amazon enables returns, which

**[13:28]** may not be good for Amazon in the short

**[13:29]** term, but increase customer trust in the

**[13:31]** long term." Same deal. They are

**[13:33]** increasing customer trust by making it

**[13:36]** easy to track tokens. You should also be

**[13:38]** building if you are building agents

**[13:40]** token budgeting. You should have input

**[13:42]** tokens, output tokens, budgets, hard

**[13:45]** stops. It's a non-negotiable. It's just

**[13:47]** responsible building in 2026. Number six

**[13:50]** is a really big one. It's something that

**[13:51]** is more unique to Claude and is a real

**[13:53]** trust builder over time. Claude is

**[13:55]** invested in structured streaming events.

**[13:58]** This is what we mean when we talk about

**[13:59]** stream of thought from Claude, right? So

**[14:01]** the pattern is pretty clear and we see

**[14:03]** it on the front end all the time.

**[14:04]** Streaming isn't just about showing text.

**[14:06]** Every streaming event that you see while

**[14:08]** the model's running is an opportunity

**[14:10]** for you to find out what is going on

**[14:13]** with that model, right? It has to

**[14:14]** communicate a system state to you. So it

**[14:16]** needs to be talking about what tools the

**[14:18]** agent is thinking about using, how many

**[14:20]** tokens have been consumed, whether the

**[14:21]** agent is wrapping up. I don't know about

**[14:23]** you, but I use that streaming state all

**[14:26]** the time with Claude because it tells me

**[14:28]** where the model is going and I will

**[14:29]** sometimes intervene in the model's train

**[14:32]** of thought and type a message because I

**[14:35]** have seen what it's thinking about and I

**[14:36]** know it's going off track. So, it's

**[14:38]** extremely useful, but it's not

**[14:39]** automatic. You have to design for it.

**[14:40]** And so what I discovered is Claude codes

**[14:43]** query engine emits typed events that are

**[14:46]** used in the stream like message start

**[14:49]** command match tool match basically all

**[14:51]** kinds of typed events that it can call

**[14:53]** upon as it's constructing this query

**[14:55]** stream. And what's critical is if

**[14:57]** there's a crash if there's an issue. Do

**[14:58]** you see how many times I've talked about

**[15:00]** crashes and issues? Good engineering

**[15:02]** assumes a failure path and plans for it.

**[15:05]** In this case, the clawed team has

**[15:07]** assumed that sometimes the agent will

**[15:09]** crash and includes a special typed event

**[15:12]** with a reason for the crash as the last

**[15:14]** message that the stream sends if there's

**[15:16]** an issue. It's like a little black box

**[15:18]** from a crash. So, when you're thinking

**[15:20]** about how you send messages back, don't

**[15:22]** just assume that you can send raw chain

**[15:24]** of thought or whatever. Take the time to

**[15:26]** send reasonable streamed events that

**[15:29]** communicate real information to the user

**[15:32]** and that allow the user to understand

**[15:34]** what is going on and make sure you plan

**[15:36]** for crashes. Okay, number seven is

**[15:38]** related. It's system event logging. If

**[15:40]** number six was about streaming events

**[15:41]** and kind of what the model is thinking,

**[15:43]** maybe some refined chain of thought

**[15:45]** there. System event logging is when

**[15:47]** something goes wrong again the failure

**[15:49]** cases think about the engineering into

**[15:50]** failure cases. This is one of the meta.

**[15:52]** When something goes wrong, the

**[15:54]** conversational transcript needs to tell

**[15:56]** the user what the agent did, not just

**[15:59]** what it said. And so, separate from the

**[16:01]** conversation, separate from streaming

**[16:02]** events, claude code maintains a history

**[16:05]** log of system events. It is a source of

**[16:07]** truth. What context it loaded? What was

**[16:09]** its registry initialization like? What

**[16:11]** routing decisions did Claude make? What

**[16:13]** execution counts did Claude have? What

**[16:15]** permission denials or approvals did

**[16:17]** Claude experience? Every single event

**[16:19]** has a category and is presented with

**[16:21]** structured details so you can easily

**[16:23]** reconstruct an agentic run. This is what

**[16:25]** you do when you are building a system

**[16:27]** that you intend for enterprise. When you

**[16:29]** are building something you intend to run

**[16:31]** seriously, this is how you prepare. And

**[16:33]** so if you're trying to build a serious

**[16:34]** agent, you need to think about event

**[16:37]** logs. You need to think about how the

**[16:39]** system maintains a record of not just

**[16:42]** what was said, but what was done and how

**[16:45]** you can provably walk that back. Number

**[16:47]** eight, Clawed Code takes verification

**[16:50]** seriously and this happens in two levels

**[16:52]** and I want to talk about each of them

**[16:54]** because we only see one normally. The

**[16:56]** one you see is really obvious. I think

**[16:58]** it's quick to talk about. You see Claude

**[17:00]** having a separate step to check its work

**[17:03]** when you go through the stream of

**[17:05]** events. That's expected and that's

**[17:07]** something that Claude code explicitly

**[17:09]** provides for. It's part of the harness.

**[17:11]** Verify that the work done was correct.

**[17:13]** Yay. Good job. A+. But we're not done

**[17:15]** yet. Part two, which I think is really

**[17:17]** critical that Claude code also thinks

**[17:19]** about in the leak is you need to

**[17:20]** recognize that you also need to be able

**[17:24]** to verify changes that you the human

**[17:27]** make to the agentic harness. So it's not

**[17:29]** just did a given agent run complete

**[17:31]** successfully. That's important and

**[17:33]** that's good. It is also when I make a

**[17:35]** change to the harness and I change every

**[17:37]** subsequent agent run, am I doing so with

**[17:40]** confidence that I'm not breaking

**[17:41]** something? And that is where you have

**[17:43]** special verification tests that should

**[17:46]** test whether the model still works

**[17:47]** against common guardrails. So things

**[17:49]** like do we have destructive tools always

**[17:52]** requiring approval after we make this

**[17:54]** change because that's a reasonable

**[17:55]** guardrail. Or when tokens run out, what

**[17:57]** happens to the model? Does it gracefully

**[17:59]** stop as we would expect or is there some

**[18:00]** sort of hard crash? These are things

**[18:02]** that you would want to have as

**[18:04]** guardrails on any agentic experience.

**[18:07]** You should name them. You should log

**[18:08]** them. And this is that second level of

**[18:10]** verification that's in a harness that we

**[18:12]** don't think about a lot because you have

**[18:14]** to provide for the harness evolving.

**[18:15]** Okay, those were day one basics. Those

**[18:17]** are things that I often see teams

**[18:19]** consider late or never when they're

**[18:20]** putting a harnesses together. Now, we're

**[18:23]** going to move toward operational

**[18:24]** maturity and think about larger and

**[18:26]** deeper lessons we can learn. I'm going

**[18:27]** to give you four of them and if you want

**[18:29]** more, I've written them up on the

**[18:30]** substack. Number one here is tool pool

**[18:32]** assemblies. Say that five times fast.

**[18:34]** What we're talking about is the idea

**[18:36]** that if you have 184 tools, Claude isn't

**[18:39]** going to assemble all of those tools

**[18:41]** into a usable pool on every agent run.

**[18:44]** Instead, it is going to assemble a

**[18:46]** sessionspecific tool pool, a group of

**[18:49]** tools that will be used to get the run

**[18:51]** done based on mode flags, based on

**[18:53]** permission context, based on deny lists,

**[18:56]** etc. What you need to learn as a

**[18:58]** designer is that you need to think about

**[19:01]** the idea that a generalpurpose agent may

**[19:04]** need to assemble a short list of tools

**[19:07]** dynamically when preparing for a run.

**[19:09]** And that's something that we typically

**[19:11]** see hard-coded in a lot of enterprise

**[19:13]** workflows where they say these are the

**[19:14]** tools available. What Claude is

**[19:16]** suggesting is that if you have a more

**[19:18]** general purpose problem solving agent,

**[19:20]** you may want to give it a wider tool

**[19:22]** subset that it can read efficiently and

**[19:24]** then let it pick from that tool list

**[19:27]** what it wants for a given row. Number

**[19:29]** two has been talked about a lot.

**[19:30]** Transcript compaction. I want to get

**[19:32]** into it a little bit more. So

**[19:33]** conversation history is obviously a

**[19:35]** token expensive resource and claude code

**[19:38]** automatically manages that by compacting

**[19:41]** it after a configurable number of turns

**[19:43]** and it keeps recent entries when it

**[19:45]** compacts and it tends to discard the

**[19:47]** older ones. The transcript store tracks

**[19:49]** whether it's been persisted to avoid

**[19:52]** data loss. You want to think about how

**[19:54]** you build automatic compaction for

**[19:56]** longer running agents. what your

**[19:58]** threshold is, what you're compacting,

**[20:00]** what you're keeping, how you know if

**[20:02]** what you're keeping is correct. This is

**[20:04]** a really hot commodity as we think about

**[20:06]** longer running agents because you have

**[20:07]** to think about how you initially keep

**[20:09]** the instruction that gets the agent

**[20:11]** started, but also how you cut

**[20:12]** intervening conversational turnpoints or

**[20:15]** intervening actions that are not

**[20:16]** relevant to the agent's present state in

**[20:18]** a way that allows the agent to save

**[20:19]** significant space. So, compaction is

**[20:22]** one. We've already talked about it. It's

**[20:24]** great to see how cloud code does it

**[20:25]** behind the scenes. There's going to be a

**[20:27]** lot more effort going into this for

**[20:28]** everybody in the next few months. Number

**[20:30]** three, this is a little bit more

**[20:32]** advanced, but think about your

**[20:33]** permission audit trail. I talk about

**[20:35]** permissions as something you need to be

**[20:36]** ready to sort of talk about and audit

**[20:38]** all the time, but Claude Code actually

**[20:39]** makes this easy because they don't make

**[20:42]** permissions just a boolean gate that is

**[20:44]** yes or no. Instead, they make

**[20:47]** permissions state a first class object

**[20:49]** that is easy to query. And Claude

**[20:51]** actually builds three separate

**[20:53]** permission handlers to serve different

**[20:55]** contexts, right? It has an interactive

**[20:57]** handler for a human in the loop. It has

**[20:58]** a coordinator when you have a multi-

**[21:00]** aent orchestration and the orchestrator

**[21:02]** agent needs to hand out permissions. And

**[21:04]** it also has a swarm worker level where

**[21:06]** you have autonomous execution that's

**[21:08]** being managed by an orchestrator agent.

**[21:09]** So that's three different types of agent

**[21:12]** that all need different permission

**[21:13]** structures and claude code thinks about

**[21:15]** all of them in the permission

**[21:17]** architecture. So should you. And last

**[21:19]** but not least, claude code has an agent

**[21:21]** type system that as far as I know was

**[21:23]** not leaked before now. So, Claude Code

**[21:25]** defines six built-in agent types.

**[21:27]** Explore, plan, verify, guide, general

**[21:31]** purpose, and status line setup. Each of

**[21:33]** these agent types comes with its own

**[21:36]** prompt, its own allowed tools, its own

**[21:38]** behavioral constraints. Like an explore

**[21:40]** agent, by definition, cannot edit files.

**[21:42]** A plan agent doesn't execute code. The

**[21:44]** transferable lesson here is not just

**[21:46]** spawn agents randomly like you're

**[21:48]** cloning minions. It's actually to

**[21:50]** constrain roles really sharply when you

**[21:52]** split work out and constrain them in a

**[21:55]** number of observable types so that you

**[21:57]** can manage those types to control your

**[21:59]** overall agent population and to manage

**[22:02]** the efficiency of the work they're able

**[22:03]** to produce. This is a great way to think

**[22:06]** about larger multi- aent systems. Okay,

**[22:08]** that was a lot. Let's hop briefly into

**[22:10]** what I'm releasing and what I built. I'm

**[22:12]** releasing an agenta harnesses skill that

**[22:14]** helps us to operationalize some of this

**[22:16]** for our own agents that we're running.

**[22:18]** And yes, if you're wondering if this

**[22:20]** works on like your open claw agent, if

**[22:22]** it's something you can use for any

**[22:23]** agentic setup, you can absolutely run it

**[22:25]** and it will give you some good tips. So

**[22:27]** what does this thing do? It has two

**[22:29]** modes. Design mode is going to enable

**[22:32]** you to describe the product that you're

**[22:33]** building like a chat assistant or a

**[22:35]** workflow orchestrator or a code agent,

**[22:36]** whatever agent you want to build. And

**[22:38]** the skill is going to walk you through a

**[22:39]** structured design process and it's going

**[22:41]** to recommend a harness shape. It's going

**[22:43]** to identify the minimum useful set of

**[22:45]** primitives. It's going to sequence the

**[22:46]** implementation into phases and it's

**[22:48]** going to define verification criteria

**[22:50]** and all of that is going to happen

**[22:52]** before you write a line of code for the

**[22:53]** harness. It doesn't just generate boiler

**[22:55]** plate here, right? It generates an

**[22:56]** architecture with rationale that is

**[22:58]** deeply rooted in what we can learn for

**[23:01]** how the most successful agent in

**[23:02]** production today runs. It also has a

**[23:04]** second mode, evaluation mode. If you

**[23:06]** already have an existing harness, you

**[23:08]** can point it at your codebase. You can

**[23:10]** point it at your cloud.mmarkdown, your

**[23:12]** architecture documents, and it's going

**[23:13]** to tell you what's missing, what's not

**[23:15]** there, what could you learn from that

**[23:18]** you might not know about with this cloud

**[23:20]** code release. So, it will evaluate every

**[23:22]** dimension across the codebase in light

**[23:25]** of the principles I've identified in

**[23:26]** this video here, architecture, safety,

**[23:28]** and permissions, state and durability,

**[23:30]** etc. and it's going to return findings

**[23:32]** ordered by severity, by a prioritized

**[23:34]** upgrade path, and specific tests that

**[23:37]** confirm the fixes work. Now, why is this

**[23:39]** a skill and not just a document? I'll

**[23:41]** put it pretty simply. A skill allows you

**[23:43]** to do something dynamically with the AI.

**[23:45]** And that's what this is all about. It's

**[23:47]** about actually implementing and fixing

**[23:49]** the agentic setups we have today and

**[23:52]** designing better agentic setups based on

**[23:54]** what claude code can teach us. I think

**[23:56]** that's a much more sustainable path to

**[23:58]** utility to usefulness based on this leak

**[24:01]** than just trying to hype up the drama.

**[24:04]** And yes, I built the skill for both

**[24:06]** claude code as a clouded skill package

**[24:08]** and also for OpenAI's codecs with codec

**[24:10]** specific metadata path patterns and

**[24:12]** agent routing. And the core logic is

**[24:15]** identical, right? The way it assesses

**[24:16]** primitives, the way it assesses

**[24:18]** evaluation dimensions, the way it

**[24:19]** assesses the design playbook. The reason

**[24:21]** for that is that I think these

**[24:23]** primitives scale pretty well. And this

**[24:24]** was a very deliberate choice on my part

**[24:27]** to make sure that we are all thinking

**[24:28]** about the primitives of agentic

**[24:30]** development as things we can learn from

**[24:32]** together and use to build more solid

**[24:34]** systems regardless of our LLM of choice.

**[24:37]** And I'll be honest here, the skill is

**[24:39]** opinionated. It biases toward a lean

**[24:42]** solo maintainable architecture unless

**[24:44]** you have a good reason not to. It starts

**[24:46]** with single agent design unless you give

**[24:48]** it really good reasons that push for a

**[24:50]** multi-agent design. It biases towards

**[24:52]** simplicity because simplicity is

**[24:54]** maintainable. And this is very

**[24:56]** intentional because the most common

**[24:57]** failure mode that I've seen in agentic

**[24:59]** systems, it's not underengineering. It's

**[25:02]** actually overengineering. Building a

**[25:03]** really complicated multi-AN coordination

**[25:06]** layer before you have a working

**[25:07]** permission system, right? Or

**[25:08]** implementing a plug-in marketplace

**[25:10]** before your sessions can survive

**[25:12]** crashes. So the skill is going to push

**[25:14]** back on unnecessary complexity because

**[25:17]** premature complexity is where frankly

**[25:19]** most projects go to die. If we step back

**[25:21]** and look at the claw code leak after the

**[25:23]** dust settles, what is the takeaway here?

**[25:25]** The larger takeaway is that building

**[25:26]** agents is 80% non-glamorous plumbing

**[25:30]** work and 20% AI. So much of what I spent

**[25:33]** time talking about in this video is

**[25:35]** stuff that most people will roll their

**[25:37]** eyes at, but it is the exact boring

**[25:40]** stuff that makes an agent successful at

**[25:43]** a multi-billion dollar level. This is

**[25:45]** what makes it possible to serve to

**[25:47]** millions and millions of people. You

**[25:49]** have to think about failure cases. You

**[25:51]** have to think about security. You have

**[25:53]** to think about how the agent recovers

**[25:55]** from from crashes. You have to think

**[25:56]** about how you have typed events that

**[25:59]** enable an agent to choose from a limited

**[26:02]** schema and come back with useful

**[26:04]** information across a range of scenarios.

**[26:06]** This is the architecture of scale. And

**[26:08]** it's amazing to me that so much of this

**[26:10]** is essentially a function of good

**[26:12]** back-end engineering. And in the sense

**[26:14]** that hasn't evolved. We're just applying

**[26:16]** good back-end engineering to these

**[26:17]** agentic pipelines and discovering that

**[26:19]** hey that works pretty well. So the

**[26:21]** plumbing isn't very glamorous maybe, but

**[26:24]** I'm talking about it because I believe

**[26:25]** it's the whole game and I'm launching a

**[26:27]** skill to make it easy because I don't

**[26:28]** want it to be hard for people to figure

**[26:30]** this out. You should not have to go

**[26:31]** through the cloud code leak yourself to

**[26:33]** infer these principles. We should be

**[26:35]** able to just pull them out and have a

**[26:36]** conversation about them as a community.

**[26:38]** So, you tell me in the comments, what

**[26:39]** did you learn from Claude Code that I

**[26:41]** didn't mention? And what would you like

**[26:43]** to see included in future agent work

**[26:46]** that you think we can all pull from

**[26:48]** Claude Code and make our agents better?

**[26:50]** I'd love to hear. Cheers.
