# Transcript: The Real Problem With AI Agents Nobody's Talking About

**URL:** https://www.youtube.com/watch?v=2PWJu6uAaoU
**Segments:** 748
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 37:38
**Uploaded:** 2026-04-15

---

## Full Text

Agents by themselves don't make you productive. I'm just going to say it straight out. So many people right now are running to OpenClaw with 250,000 GitHub stars or they're they're VCs and their builders and all they can do is they can build copycats of OpenClaw. And everyone assumes that as soon as you get the agent, you'll know what to do with it. And there's a massive gap between I can install an agent, which everyone has now solved for. You can install an agent in 10 seconds. By the time I have finished saying this sentence, you can have an agent up and going. that's how fast these things are going now. That's not the point. Whether you can use it productively is actually the question that matters. And yes, all of those people who are out there who are making lots of clickbait who are saying, "I used my agent to do lots and lots of stuff. I have 10 agents that do this and that. I have two agents that do this and that. I manage my whole $5 billion company with agents." Those are all true stories, but they're only true stories because someone figured out how to clarify enough of what they were looking to do to give it to an agent. And that turns out to be a very, very hard problem. And it's funnily enough, not a problem that most companies out there are interested in solving. And I know because I went through and I looked at all the products. And so in this video, we are going to go through and talk about the real gap that's upstream of all of these open claw agent metos. We're going to go through and survey the different approaches to building your agents, the different ways these products are handling open claw like implementations. And then we're going to talk about how you actually solve this problem. And yes, I built something to solve it. I want you to have an easier time using your agent. Right? Let's assume you have an agent because now it's very easy to get one. how do you use it? And so I built something to make that jump into using the agent much much easier. And we'll get to that. The most common message I've been able to find in most open claw community forums is this. Now what? It's really simple. Like I I did it. Now what's next? How do I go from here? Variants of that, right? Like I have installed the open claw. Now what do I do next? It's not really how do I fix this error. It's not which model do I use? Although there's a few of those. It's just I got it to run, which is great, and I don't know what to tell it, right? Give me a recipe. Give me something to do. And I think there's a structural reason this keeps happening. And I don't think the correct fix is just to hand out recipe cards for openclaw use cases because that's not really what you want an agent to do. The whole reason we have an agent is because it does many things well. It doesn't just do one thing. Well, if you start telling your agent, hey, here's my, you know, expensive Mac Mini. Here's my expensive cloud subscription. Now you triage my email. Is that really a good use for your dollars? Yet a lot of people, the most common use of OpenClaw is triaging your email. We need to understand why agent implementations are not delivering the 10x ROI that have been promised for so many people. And we need to be honest about it or there's going to be a lot of people who are a little bit frustrated. There are going to be people who are lining up to undo OpenClaw if we're not careful. And I say that because there actually have been cases of lines in China where people who had previously installed OpenClaw are going back and standing in line to uninstall it because they didn't want it. I don't want that to happen. So here's what I'm going to dig into. I'm going to dig into the common patterns across agent implementations that really work. I'm going to dig into the meto landscape and why every open clawike product is kind of aiming at the same target and kind of hitting the same wall when it comes to success. And I'm going to dig into the structural reasons why it's really really difficult for us to actually explain what we need to do with these agents in a way that they can understand. I'm going to explain a little bit about why I think this is the larger problem. It goes beyond agents and then we're going to get into what to do about it. How do we solve it? So let's jump in. All right. We're gonna start with a story of Brad Mills. This is a real story. Brad spent 40 hours building a delegation framework for his OpenClaw agent. Not 40 hours installing. I want to be very clear. The install took 10 minutes. He spent 40 hours writing standards, accountability rules, a definition of done for every single project. He transcribed 200 hours of videos into a searchable knowledge base. 40 hours of trying to describe what he wanted, right? I'm not making that up. That's like a week of work and it still did not work. And he wrote about it publicly, right? Constant failure. He wrote fail after fail after fail. Two steps forward, one step back. and he ended up micromanaging the agent harder than he'd ever had to micromanage a human. And the autonomy that so many other stories share felt in practice like the second job of supervising something that confidently reports tasks complete when it's not really done. Brad is not an outlier here. I would say Brad is closer to the median experience than a lot of the folks who are promising 10x results. One prominent OpenClaw guide creator reports getting flooded with DMs all the time right after setup. The stuck point is not installation anymore. We figured that out. It's actually figuring out what to do with the agent and how to make it understand your specific context. Right? Another user asked his agent to write five cold email variants. The agent sent done and wrote nothing. And his solution was to build a second adversarial auditor agent whose only job was to verify the first agent completed the task. He needed a management layer because the worker couldn't be trusted to self-report. And this became like a nesting turtles problem. like you just have issues managing the agents because you don't understand how agent architecture works if you've just spent 10 minutes on an open claw installation and you've just heard about it on the internet a day ago. Another user tried rolling out agents to a team and he gave everyone access and just called it done. It technically worked, he pointed out, but it was completely useless because nobody had mapped their workflows, their decisions, their data needs in advance and no one knew what to give the agent as a task that would be successful. Without all that upstream work, the agent stayed so generic it was useless. And a generic agent with right access to your email is actually worse than no agent at all. It's a liability with a chat interface. Right? There are whole business models emerging on places like X to fix this. Right? That is how bad an issue it is. There's a guy on X I saw selling a $49 pack of pre-written config files. A soul.markdown file, a heartbeat.mmarkdown file, a user.mmarkdown file. is core files for OpenClaw. The whole stack specifically marketed to quote skip 40 hours of OpenClaw setup. You can build a small business around the gap between installed and useful. And that tells you something about where the agent market is. But before we talk too much more about what's broken, let's talk about what does work. Because there's a pattern across hundreds of thousands of Open Claw installations. The deployments that stick, the ones where people are still getting daily value weeks and months later, they share a particular architecture and it has almost nothing to do with which model you end up picking. The successful setups all have a set of markdown files that function as the agent's operating system. If you open theopenclaw directory on anyone running a working agent, you'll find the same structure. There's a soul. Markdown file that defines the agent's role, its job, its tone, its boundaries, basically a job description. There's an identity.mmarkdown which has its name. It has its personality constraints. There's a user.mmarkdown with a detailed profile of the human including preferences, schedule patterns, communication style. And there's a heartbeat markdown with a checklist that the agent reviews every half hour to decide if there's work to do. And then there's a very simple cron job that maps that human's actual operating rhythm. None of this is particularly technically difficult. And I want to underline this three times. None of what I just described is artificial intelligence. It's just plain text. But the quality of those files determines whether your artificial intelligence agent is actually any good at anything at all. So the people who run multiple specialized agents, the not the one do everything bot, right? But a team with clear roles and scoped access, you know how you've seen the clickbait, right? Well, I have a marketing manager for this and then I have my scheduler for this and I have my CEO for this and I have my chief of staff for this. Okay, fine. The only way that works is if each agent has truly its own identity, its own markdown files, its own tool sets, its own workspace so it can get jobs done and it doesn't share context with other agents. They have clear jurisdictions. We would say they have clear separation of concerns in engineering speak. And that same clarity shows up everywhere you see a multi- aent system working. So, people running specialist bots in Slack that delegate to each other like co-workers, which you've also seen demos of, I'm sure, where someone asks a question and the orchestrator agent decides that the specialist should handle it. There's a whole flow, right? These are not toy demos. They're running daily. Those are real orchestration patterns. They really work and they and they only work because there's a clear separation of concerns and a clear identity that's separate for each of the agents involved. Now you can absolutely in more sophisticated implementations use your open claw as a general planner and have it spin up executor agents on the fly to help you get tasks done. That is one of the ways a general purpose agent solves problems. But it only does that successfully to the extent it has the tools, the identity, all of the context to know how you want the problem solved and to do so successfully. And so it still comes back to context in the end even if you're doing a more sophisticated implementation. There's another pattern worth naming. The people who have open claw configured correctly have invested a lot in the memory side of things. They either have a memory.mmarkdown file that accumulates insights over time which is closer to the original vanilla openclaw approach or they've got closer to something like the open brain approach that a lot of folks in my community are building where they have a database that the open claw can search from and get back insights on and that ends up being sort of a richer more multi-dimensional repository over time. You can have a hybrid, you can kind of work with both. The point is you have intent around memory. you know that your agent needs to learn and get better over time. And if it doesn't learn and get better over time, it's not a very smart agent and it's not going to help you for very long. And the common thread through the context piece, the separation of concerns, the ability to set up memory correctly, the ability to write all those markdown files right, the ability to maybe configure a database so your agent can query for memory. All of that means having clarity of intent around what you want the agent to do and the ability to articulate at a pretty high degree of detail what you expect the agent to do in a series of steps. Right? The human has to sit down and describe in triggerable verifiable language what you do all day to get an agent to do it. Right? Not I handle marketing, but these are the different websites I check. These are the metrics I look at. This is the spend that I'm willing to budget for. This is how I know that spend is correct. These are the equations I run. And then finally, these are the optimization and leverage opportunities I see. Now, people will say, "It's the agent's job to get better at marketing. Why are we giving it that detail?" And I will answer, you got to orient the agent toward the current context if you want to ask the agent to improve over time. You cannot just magically say, "Here's marketing. You do it agent." and it's just going to magically know all of the nuances of your context for your product and just randomly do it. That's just not how it works. And yet that underlying assumption is lying behind so many of the meto products that we see in the landscape. If we look across the landscape, and I'm going to profile them here, and we look at how agents are being built and sold right now, so many of them are being built and sold as essentially magic boxes with arms and legs. Like, here's the magic box. Type anything you want and the magic box will fix it. And it turns out if you're selling magic boxes, they'll sell like hotcakes. But the problem is once you have a magic box and it's not magical anymore, it's a disappointing experience. Let's go through each of them in turn. Obviously, Open Claw is the original. It's 250,000 or whatever number of thousand GitHub stars it is now. It runs locally on your hardware. It connects to any LLM. You talk through it through any channel, right? Telegram, WhatsApp, iMessage, Slack. Now you can phone call it like whatever you want. It's free. It's infinitely configurable and the cold start problem is entirely up to you which is appropriate because the original audience was developers. Peter Steinberger built this for developers and developers quite reasonably could be expected to write markdown files and configure their own tool set and for so many of them that was not an obstacle and so so much of this conversation is basically OpenClaw is out in the wild now. Openclaw is on the loose. Open Claw is the most copied product of 2026. What does it mean when everybody wants an agent and they're not just developers and they're like, "What is a markdown file and why should I care?" Developers, to be fair, have a little bit of an advantage at writing specifics. If you've ever sat in the product chair like I have, and you've had conversations with engineers, you know the engineers tend to be the ones and should be the ones asking you for specifics. Okay, fine. You say you want the image to appear in that way on the web page. Tell me why. Tell me what is the file size. Tell me how quickly you expect it to load. Tell me how it goes with and overlays the rest of the web experience. And that's just a very simple presentation, right? Love to get specific. And I think that mental habit has helped open claw take off for so many in the engineering community because it's actually very clear to them that you need to describe a lot of what you do in high specifics to the agent to make it useful. That's not that unusual. For the rest of us, it's a new step. Now, a bunch of folks have come into the space since OpenClaw, and the thesis for most of them has been correctly. OpenClaw was hard to install originally. Peter designed it that way on purpose. He did not want non-developers using it because you can easily configure your OpenClaw to be a security risk. And that was the dominant headline for the first month or so of OpenClaw's popularity. And so, so many players are in the space now basically saying, "We took care of security. We took care of ease of install. You don't have to worry about it." And I'm here saying that's not the real problem. That's just the first problem, right? Manis, now owned by Meta, is doing exactly that. You can either have a desktop app which has local access or you have a cloud virtual app. But either way, it's more secure. It's got a little bit of structure. You type in your query. It automatically decomposes all of that work into its own sub agents. And the idea is it's easier to use. It's more secure. It can be locally if you feel comfortable with that or in the cloud. And it's something that you can get up and running on in 10 or 15 minutes. The problem is the manness agent is really going to be limited by the lack of initial context you give it. So it's optimizing for the cold start problem in the sense that it makes it easy to type the first word, but without the ability to really deeply configure what the agent knows about you and why it cares about you and the workflows you're doing and what you're trying to accomplish and what you're trying to delegate, it's going to be somewhat limited in its ability to work with you. Now, I do know Manis users who have deliberately put intent into that platform and swear by it. They're like, "This is incredible. The more intent I put in, the better it gets." And that is kind of a universal law of AI. If you put more passion, heart, intent, clarity, and communication into the tool because these tools have memory systems, they start to learn over time and they're more useful for you. But that is not the experience of the majority of Manis users. And that brings me to the next tool, which is Perplexity's personal computer. Perplexity personal computer is in a sense the most audacious of these open claw plays. We know that we cannot get a hold of Mac minis because Apple has sold out of them because so many people want to put open claws on them. Perplexity saw that said we're a corporate account. We can get lots of Mac minis and they literally offer you a dedicated Mac Mini. It's a real Mac Mini connected to Perplexity's cloud, merging local file access with their computer orchestrator and they give you a project manager AI that routes tasks across 20 Frontier models for that Mac Mini. So, it takes away all of the pain of having a local Mac Mini. You actually have a real Mac Mini that's yours. It has an orchestrator. It has 20 models. It's a very bold vision. CEO Aravven Sinas framed it at the developer conference like this. He said a traditional operating system takes instructions and an AI operating system takes objectives. I think he is right that openclaw is popular because it is fundamentally an operating system. That is a correct insight. I think he's also correct in saying that it is about optimizing for objectives. But the piece that is challenging for most people is when you have that firepower delivered for you, all of that agentic power at your fingertips, what do you do with it? Then how do you communicate your intent in a way that actually gets across? The fundamental bet is the same as all these other ones. You state the objective for openclaw and openclaw will figure out the rest. In this case, you state the objective for perplexity personal computer and you bet the personal computer will figure out the rest. And that works well right until the objective requires knowledge about your life, your judgment patterns, your operating rhythm that no system actually has because you never wrote it down. And you may not be aware you have it, but it's in your bar for powerpoints. It's in your bar for financial products. It's in your bar for everything, and you just never realize it was written down. Let's have a look at Neimoclaw next. Nemoclaw is Nvidia's enterprise security wrapper for OpenClaw. It was launched at GTC by Jensen Hang itself. It runs agents in sandbox environments using Open Shell for privacy guardrails and Neotron for advanced model output. Basically, it's a it's a buttoned up corporatefriendly open claw with lots of security guard rails and it solves the security problem really thoroughly. The real and serious risk of an agent with full access to your machine deleting stuff like they've taken care of that. It does not solve the problem of what to put in the agents operating instructions and it effectively punts that to the enterprise. And the problem is most enterprises also don't know how to solve that problem. I know because I talk with them. They do not know out of the gate how to solve the problem of what to do with a Nemo Claw. If you roll it out to 10,000 people and only five of them have used OpenClaw in a way that's productive, those five are going to be perfectly happy and be able to use that. The other 9,995, they're not going to know what to do. They're not going to know what to do because no one trained them. And that is absolutely a larger issue with AI, but it's especially bad with agents. And the reason it's especially bad with agents and with the open claw phenomenon is that the open claw phenomenon gives you so much power. It is really a story of transformation. It does really give you that 10x potential on your work and they just do not tell you how much work you have to put in at the top to get that result and how much training you have to do if you are rolling this out to a workforce. It is not a plug it in and go solution and it never is going to be because it takes context from you. Right? I just want to be honest with you. All the people who are promising and all of these ones that I'm covering are promising this. All of them who are promising 10 minutes to open claw are right technically and wrong functionally. They're correct. Technically, you can get very very quickly up and running with your open claw. They are wrong in that you cannot get utility out of the open claw unless you put a lot more work than that into getting it ready. Claude dispatch is part of anthropic's answer and Anthropic has been investing heavily in essentially pivoting their claw product. So it is open claw like over the last month there's probably been 15 ships around this. Dispatch is the most obvious because it makes it so easy to pair your phone with your Mac and it makes it easy to send messages through whatever version of your messaging app that you want and you can now control your claude from your phone which is one of the key benefits people called out from OpenClaw in the first place because you can use your openclaw wherever you are. You can be dropping the kids off to school. You could be out looking at the beach. You can be working in the kitchen and you can be messaging your computer and getting work done. People like the mobile friendliness. It's one of the oldest bets in software. We've had this bet since 2007. Really earlier than that when we had the mobile phone revolution in 2007 with the iPhone. People like to be on the go with computing. And this is just taking your agents on the go. It's one of the oldest and most reliable bets in software. It turns out it works for agents, too. But you can't send, and I've tried this, by the way, with popular agents, you can't send a threeline or four-line text message to an agent and expect it to work well if the agent doesn't know you. And it turns out that a lot of these text message first apps do not work well if you are just introducing yourself by text. Because guess what? I have done a 15 paragraph introduction by text message to a popular open claw like application and it has completely failed because it still wasn't enough. 15 paragraphs of text that's a whole wall of text and it's still not enough to get the agent to actually get it. And so as much as it's really cool that Claude is pivoting to make it easier to message, there are a lot of developers that find it super useful, it does not by itself solve this problem. The issue here is that we need to be able to say or speak what we really mean in a way that's clear enough that an agent can run with it and we can truly delegate that task. And that is the problem none of these solutions are really solving. And that goes not just for these purpose-built solutions I profiled like perplexity personal computer or like Nemo Claw, but it also goes for the hosted rappers start claw, myclaw, simpleclaw, uniclaw, you name it, claw and and there's like dozens a week launching. They're all trying to make open clause setup easier, right? One-click deploy, preconfigured personas, managed infrastructure. They're solving all of that installation friction very successfully, which is a real UX problem. But the guy selling the $49 pack of pre-written sold out markdown files or the guy repackaging and calling it start.claw and having the exact same markdown files as a quote persona, they're not really solving that issue, right? They're giving you their generic version of what it is, not the thing that's going to be useful for you. Because the thing that makes agents useful is that they are particular, is that they are personal and you can't take that away. The people who are having transformative impact have realized they need to put the work in to make their agent personal. There is no substitute. So every product in this landscape is fighting over installation, over UI, over model selection, over security, over pricing, over cloud versus local. And they're competing on this implementation layer. And they're trying to get us to care. Do I care about the fact that I want a Mac Mini in the cloud from Perplexity? Is that better? I don't even know how to assess that in most cases, right? Most people don't. And every product in this landscape breaks against that same wall, right? The human on the other end has to understand what they need to do and produce a usable spec for the agent to do that task. And that is actually much more important to the long-term value of the agent than just a particular kind of installation, which is just a one-time problem. And so that wall, there's a reason why products are not going after that. It's a structural property of how expertise works. And it's actually a really hard problem. It's not easy. You can't solve it with UX. And here's where it would be easy for me to hop off and say, "Well, it's really hard. We're done." But I want to go deeper. What it makes it difficult for people to describe what they do. Because that observation, while true, doesn't explain why this is happening and why we find it hard. And there's a larger story there. If you don't understand the mechanism, you're going to waste time on solutions that don't address the root cause. Knowledge work has a structural property that makes it uniquely resistant to delegation, whether that's delegation to humans or delegation to machines. And that property is this. The more senior and valuable you become, the more your work migrates from explicit processes to tacit judgment, and the less visible your own operating system becomes to you, the person using it. And this is not a failure of good intentions. This is not a failure of self-awareness. It's the intended outcome of how expertise actually develops. When you're a beginner, everything is very conscious. It's very deliberate. When I started to play basketball, when I was in middle school, I was focusing on dribbling so hard and eventually you start to get good at dribbling the ball. You don't think about it as much. So, you follow the checklist and knowledge work to begin as an intern. You think through every step. As you gain expertise, all of those steps compress into automatic patterns. Just as when you drive a car today, you don't think about turning right after 20 years of driving a car. It just happens. You stop thinking about your knowledge work. You stop thinking about what to check. You just check it. You stop reasoning through decisions and you just make them. But the reasoning still happens. The thing that makes you fast and effective is the same thing that makes your knowledge very inaccessible. It's been compiled from source code into machine code. metaphorically speaking and you no longer have the source code. Let's take an example of a really senior product manager. They don't think I should cross reference the revenue dashboard with the churn data before forming an opinion. Instead, they'll open three tabs. They'll glance at the numbers and they just know. And if you ask what was checked and can you reconstruct and explain what happened, they'll narrate backwards from the conclusion, but they're not they're not really going to describe the actual process in most cases because it's so low level. The real decision often involved a hundred micro evaluations that re reflect thousands of hours of patterns that that product manager has seen over multiple startups. But but that doesn't get articulated, right? The magical pattern matching that allowed the deep insight that they had about churn is something that is a function of all of those thousands of hours. It's not something you can substitute for with just an explicit intern checklist. It it doesn't work that way. Now, you might stop here and say, "Well, then there's no point in agents." And I will come back and I'll say, "No, the stories of agents making you insanely productive are all true." And our goal is to make more of those stories. And I am telling you what it takes. And the first thing we have to acknowledge is that knowledge work is really hard. A strong salesperson doesn't consciously decide to mirror their prospect's phrasing and slow their cadence where they when they detect defense. a strong salesperson, they don't consciously decide to mirror the prospect's phrasing and slow down their cadence when they detect that that they're just a little defensive. They just do that. A senior engineer doesn't think, well, this code has a concurrency issue that'll service under load on Tuesdays because we have a lot of email traffic on Tuesdays and when the batch job overlaps with the peak traffic, we're going to have issues. They they may be able to get to that point and tell you later, but initially they just feel it. They say, "Oh, that's bad." and then they go look and then they're right and then everyone calls it experience. This is worth digging into because it's the root cause of a product failure happening at an absolutely massive scale across the industry. The entire agent ecosystem is built on a model where the human provides instructions and the machine executes them. That model works when the instructions are really clear like summarize the document, right? Super easy. Reformat the spreadsheet. But it breaks when the instructions require expertise that the human genuinely has but struggles to articulate. And almost all of the most valuable knowledge work that agents can tackle lies in that second category. In other words, 2026, the year of these long-running agents that do impactful knowledge work, only really delivers on that promise if we can get into the very hard problem of explaining to these agents this tacit knowledge, work, and judgment that makes us good at what we do. We have to think through what does it mean to have deep insights about churn and actually articulate enough of our personal experience to give the agent something to work against. Not because the agent has to mimic us like a parrot, but because the agent needs to orient enough in our local context that it can then go beyond that and continue to optimize and deliver insights. Because the best agents do that, right? the best agents know enough about your context and what you're trying to do that they can then go beyond that and deliver really interesting novel insights you wouldn't have expected. That's fantastic. That's the dream. It does really happen. But you got to give them enough out of your tacid experience to actually make that possible. Think about what a good sold out markdown file contains. It's not just a personality description. It's it's a decision framework. when to escalate versus how you handle things autonomously, what what tone to use with different audiences, which data sources are are you going to trust versus which ones are you skeptical of, what is good enough at various task types. That's the same thing a strong vice president would put in an operating memo for the team when he or she joins the team for the first time. And most VPs, honestly, they haven't written that down either. I' I've been under a number who have moved in new, and most of them don't send an operating memo like that, even though they should. This is also the same reason why senior engineers notoriously are pretty bad at writing onboarding docs. It's not laziness. It's that the knowledge that would make the doc useful has been sort of compressed into a form of automatic behavior for them and the doc is going to list steps but miss so much nuance that they have in their heads because it just makes sense for them. It's like the person who's describing the way to uh a friend's house down the road and they're giving you all of these landmarks that are local to them that make sense. It's like there's the big tree and then you stop by the the the store that has the broken down sign and then you go over it. This is no like as a stranger in these parts, you don't understand it, but they understand all of the nuances that help them get to their friend's house. And the structural trap is this. The people with the most to gain from agent delegation are exactly the people whose work is hardest to delegate. The most senior, most overloaded knowledge workers carry the highest ratio of tacet to explicit knowledge. Their work is the most compressed. It's the most invisible to themselves. They need the leverage most and the cold start problem hits them the hardest. Ironically, beginners just getting started in their careers. Folks who are you're one year, two years out of college and all of this is stuff that you are still doing intentionally, explicitly in your head, you haven't compressed it yet. You may have a much easier time with agents and delegating to OpenClaw than the seniors. And the reason I say that is because you have not gone through that automation process in your head yet. And that's actually fantastic and it's one of the reasons why firms like Shopify intentionally hire juniors because there are things that you can go much faster at than seniors. And ironically, this inability to sort of get our operational knowledge, our tacet knowledge out of our heads is at the root of at least three big chronic people problems that plague most organizations. Delegation fails. That's that's one of them, right? Managers will cite that as a key challenge. And the standard explanation is that they're control freaks. But the real explanation is that they don't know how to delegate because they don't know how to express what they've got in their heads. It's it's a real challenge for new managers. Another related one, people not getting promoted. The most common reason strong IC's plateau is that they cannot be replaced. Their knowledge work is locked in their head. And so even if they are qualified for the next level, no one wants to risk losing their expertise on their current job and that becomes a trap for them. And then of course the third one is obvious. People leave. Institutional knowledge evaporates. it walks out the door in someone's head and and it's just gone. So, I would argue agents did not create these problems, but agents create the first universal selfish incentive for every single one of us in knowledge work to actually fix these problems. Not because HR launched a knowledge management initiative, right? It's not because a consultant ran a workshop. It's because you personally want a robot to stop asking you to confirm calendar entries that you already freaking approved. and the robot needs you to describe your calendar rules first. That's new. Look, we've had decades of top- down pressure to externalize our knowledge. It never worked at scale because there was no direct personal upside for any of us. The benefit occurred entirely to the organization when you wrote the wiki, right? A and traditionally, the person who documents their expertise is the person who loses. In this case, agents flip that incentive structure on its head. The person who documents their expertise is the person who gets the leverage in the world of agents. The organization might benefit secondarily. It's actually a bottoms up knowledge management revolution disguised as a consumer AI product. And I don't think that anyone, including the people building these products, really appreciates that because if they did appreciate it, I feel like they would put more into onboarding. I have been through the onboarding flows for like half a dozen of these and they all feel really, really light. Really light for what you're expecting this agent to do, for what you're hoping it will do for you. If you want it to really lift up, leverage two, three, or more X your work. And that and that leads us to a very uncomfortable correlary that's worth naming explicitly. If the value of agents depends on your ability to articulate your work, agents are about to create an extremely visible divide in the workforce. Right now, tacet knowledge is invisible, right? Nobody knows that you can't describe your own process because nobody's ever asked you. Performance reviews tend to measure your outputs, not your self-nowledge. You might be a phenomenal operator with zero ability to explain how you operate and the system just never penalizes you and agents are about to change that. In a world where everyone has access to the same tooling, the differentiator is not which model you use or how many Mac minis you can put your open claws on. It's whether you can feed the thing well enough to actually get leverage. The people who invest that time, who can decompose their expertise into explicit delegatable components will get compounding returns. That's where the value is. Their agents improve because their specs improve. The second agent deploys faster than the first. The 10th deploys in a few minutes and they actually build on all of that knowledge. So, it doesn't even take them a ton of time to provision it because they understand the memory system so well. The people who skip all of that will install, play for a weekend, hit the wall, and conclude agents are all hype. And they will be wrong. The agent worked fine. The problem was never the agent. So, I want to propose a solution. I've gone through the problem. You understand the problem. The solution I have is this. The first agent you run should not be your open claw assistant. The first agent you run should be a tool to prepare you to run agents the way you want. And no one seems to be thinking this way, so I'm just going to say it out loud. The first agent worth deploying, it's not your personal assistant. It's not your chief of staff. It's not your scheduler. It's not your email uh guy. It's not your briefing bot. It's just an interviewer. It is one designed to do what expertise elicitation researchers do. Yes, that's a real job. Ask you the right questions in the right order with the right follow-ups to extract the operational knowledge you carry but cannot access on your own. And no, this is not the same as asking you three questions on install. I know that OpenClaw asks you who am I, who are you, and what is my job? I get that. This is a lot deeper than that. And of course, I've been building this. I've been digging in because I want to build a demo that actually allows you to immediately use this so that if you have trouble actually using your agent and making it valuable, you have a tool now to get your agent going. It's a structured elicitation workflow. I know it's a $10 word, but it basically means getting that information out of your head. Uh, it's a structured elicitation workflow that walks you through five specific layers. Your operating rhythms, what are your days, your weeks, and your months actually like in detail, not the calendar version, the real one. Your actual recurring decisions, what judgment calls you make, what are the easy calls, the hard calls, what inputs that you actually need, your dependency, who do you need things from, and when. Nobody's asking that, right? They've been through these flows. Your friction, the recurring annoyances that eat your time. Most of them don't ask that either. It takes time. I'm not going to pretend this doesn't take time, right? Like I've gone through it at best. It takes 45 minutes. It might take you longer. And and I think that time is worth it if you're going to actually save time on your agent, right? The output is structured data and you can plug it right into your open brain if you've built that. That's just a simple personal knowledge store uh that's quick to set up and runs for like 10 cents a month. Uh and then it becomes durable, right? it becomes searchable knowledge and it's available to any agent that interacts with an MCP which all of these openclaw agents do by the way and from that output I built a configuration file generator that will automatically produce soul.markdown heartbeat.mmarkdown user.mmarkdown files that you can use to provision an openclaw and that solves the gap that solves the gap that manis isn't building for perplexity isn't building for nemo claw isn't building for dispatch skips over this and to be honest with you the configuration files that I can output. And to be honest with you, the configuration files you get at the end of this process are in some ways the least interesting output. The more valuable output is the conversation itself and the way it creates a structured database, a structured map of how you work, what you know, where your leverage points are. And that makes you so much better at delegating to agents. Yes. But also talking about it means you're better at delegating to people. It makes you easier to promote. It makes your expertise survivable. All of this stuff that was locked in your head, you had an AI agent help you get it out. And that's what I focused on building. The AI agent that helps you get it out. And yes, it does help you make your agents work, which is kind of the whole reason you'd have agents. I know that every agent product in the market today is competing on the implementation layer. How easy is it to set up from scratch with your open claw? Fine. The question I have is once you have it set up, can you actually use it to do interesting stuff? Can you actually use it in ways that help your workflow? And the only way it will ever do that is if it gets into your brain and gets the stuff out that you don't think about every day. And that's why I built an open brain interview agent to help you get that knowledge out so that you can provision whatever open claw you choose in whatever way you choose confident that it actually knows the details, the nuance, the depth of your work in a way that will make it effective because that depth is where you get the disproportionate returns. That's how the people who are getting these three, four, 5x returns are doing it. So don't make your first agent the agent that is your personal assistant. Instead, make your first agent the one that prepares you to have a personal assistant agent. The extra work is worth it. I promise. Cheers. Agents by themselves don't make you productive. I'm just going to say it straight out. So many people right now are running to OpenClaw with 250,000 GitHub stars or they're they're VCs and their builders and all they can do is they can build copycats of OpenClaw. And everyone assumes that as soon as you get the agent, you'll know what to do with it. And there's a massive gap between I can install an agent, which everyone has now solved for. You can install an agent in 10 seconds. By the time I have finished saying this sentence, you can have an agent up and going. that's how fast these things are going now. That's not the point. Whether you can use it productively is actually the question that matters. And yes, all of those people who are out there who are making lots of clickbait who are saying, "I used my agent to do lots and lots of stuff. I have 10 agents that do this and that. I have two agents that do this and that. I manage my whole $5 billion company with agents." Those are all true stories, but they're only true stories because someone figured out how to clarify enough of what they were looking to do to give it to an agent. And that turns out to be a very, very hard problem. And it's funnily enough, not a problem that most companies out there are interested in solving. And I know because I went through and I looked at all the products. And so in this video, we are going to go through and talk about the real gap that's upstream of all of these open claw agent metos. We're going to go through and survey the different approaches to building your agents, the different ways these products are handling open claw like implementations. And then we're going to talk about how you actually solve this problem. And yes, I built something to solve it. I want you to have an easier time using your agent. Right? Let's assume you have an agent because now it's very easy to get one. how do you use it? And so I built something to make that jump into using the agent much much easier. And we'll get to that. The most common message I've been able to find in most open claw community forums is this. Now what? It's really simple. Like I I did it. Now what's next? How do I go from here? Variants of that, right? Like I have installed the open claw. Now what do I do next? It's not really how do I fix this error. It's not which model do I use? Although there's a few of those. It's just I got it to run, which is great, and I don't know what to tell it, right? Give me a recipe. Give me something to do. And I think there's a structural reason this keeps happening. And I don't think the correct fix is just to hand out recipe cards for openclaw use cases because that's not really what you want an agent to do. The whole reason we have an agent is because it does many things well. It doesn't just do one thing. Well, if you start telling your agent, hey, here's my, you know, expensive Mac Mini. Here's my expensive cloud subscription. Now you triage my email. Is that really a good use for your dollars? Yet a lot of people, the most common use of OpenClaw is triaging your email. We need to understand why agent implementations are not delivering the 10x ROI that have been promised for so many people. And we need to be honest about it or there's going to be a lot of people who are a little bit frustrated. There are going to be people who are lining up to undo OpenClaw if we're not careful. And I say that because there actually have been cases of lines in China where people who had previously installed OpenClaw are going back and standing in line to uninstall it because they didn't want it. I don't want that to happen. So here's what I'm going to dig into. I'm going to dig into the common patterns across agent implementations that really work. I'm going to dig into the meto landscape and why every open clawike product is kind of aiming at the same target and kind of hitting the same wall when it comes to success. And I'm going to dig into the structural reasons why it's really really difficult for us to actually explain what we need to do with these agents in a way that they can understand. I'm going to explain a little bit about why I think this is the larger problem. It goes beyond agents and then we're going to get into what to do about it. How do we solve it? So let's jump in. All right. We're gonna start with a story of Brad Mills. This is a real story. Brad spent 40 hours building a delegation framework for his OpenClaw agent. Not 40 hours installing. I want to be very clear. The install took 10 minutes. He spent 40 hours writing standards, accountability rules, a definition of done for every single project. He transcribed 200 hours of videos into a searchable knowledge base. 40 hours of trying to describe what he wanted, right? I'm not making that up. That's like a week of work and it still did not work. And he wrote about it publicly, right? Constant failure. He wrote fail after fail after fail. Two steps forward, one step back. and he ended up micromanaging the agent harder than he'd ever had to micromanage a human. And the autonomy that so many other stories share felt in practice like the second job of supervising something that confidently reports tasks complete when it's not really done. Brad is not an outlier here. I would say Brad is closer to the median experience than a lot of the folks who are promising 10x results. One prominent OpenClaw guide creator reports getting flooded with DMs all the time right after setup. The stuck point is not installation anymore. We figured that out. It's actually figuring out what to do with the agent and how to make it understand your specific context. Right? Another user asked his agent to write five cold email variants. The agent sent done and wrote nothing. And his solution was to build a second adversarial auditor agent whose only job was to verify the first agent completed the task. He needed a management layer because the worker couldn't be trusted to self-report. And this became like a nesting turtles problem. like you just have issues managing the agents because you don't understand how agent architecture works if you've just spent 10 minutes on an open claw installation and you've just heard about it on the internet a day ago. Another user tried rolling out agents to a team and he gave everyone access and just called it done. It technically worked, he pointed out, but it was completely useless because nobody had mapped their workflows, their decisions, their data needs in advance and no one knew what to give the agent as a task that would be successful. Without all that upstream work, the agent stayed so generic it was useless. And a generic agent with right access to your email is actually worse than no agent at all. It's a liability with a chat interface. Right? There are whole business models emerging on places like X to fix this. Right? That is how bad an issue it is. There's a guy on X I saw selling a $49 pack of pre-written config files. A soul.markdown file, a heartbeat.mmarkdown file, a user.mmarkdown file. is core files for OpenClaw. The whole stack specifically marketed to quote skip 40 hours of OpenClaw setup. You can build a small business around the gap between installed and useful. And that tells you something about where the agent market is. But before we talk too much more about what's broken, let's talk about what does work. Because there's a pattern across hundreds of thousands of Open Claw installations. The deployments that stick, the ones where people are still getting daily value weeks and months later, they share a particular architecture and it has almost nothing to do with which model you end up picking. The successful setups all have a set of markdown files that function as the agent's operating system. If you open theopenclaw directory on anyone running a working agent, you'll find the same structure. There's a soul. Markdown file that defines the agent's role, its job, its tone, its boundaries, basically a job description. There's an identity.mmarkdown which has its name. It has its personality constraints. There's a user.mmarkdown with a detailed profile of the human including preferences, schedule patterns, communication style. And there's a heartbeat markdown with a checklist that the agent reviews every half hour to decide if there's work to do. And then there's a very simple cron job that maps that human's actual operating rhythm. None of this is particularly technically difficult. And I want to underline this three times. None of what I just described is artificial intelligence. It's just plain text. But the quality of those files determines whether your artificial intelligence agent is actually any good at anything at all. So the people who run multiple specialized agents, the not the one do everything bot, right? But a team with clear roles and scoped access, you know how you've seen the clickbait, right? Well, I have a marketing manager for this and then I have my scheduler for this and I have my CEO for this and I have my chief of staff for this. Okay, fine. The only way that works is if each agent has truly its own identity, its own markdown files, its own tool sets, its own workspace so it can get jobs done and it doesn't share context with other agents. They have clear jurisdictions. We would say they have clear separation of concerns in engineering speak. And that same clarity shows up everywhere you see a multi- aent system working. So, people running specialist bots in Slack that delegate to each other like co-workers, which you've also seen demos of, I'm sure, where someone asks a question and the orchestrator agent decides that the specialist should handle it. There's a whole flow, right? These are not toy demos. They're running daily. Those are real orchestration patterns. They really work and they and they only work because there's a clear separation of concerns and a clear identity that's separate for each of the agents involved. Now you can absolutely in more sophisticated implementations use your open claw as a general planner and have it spin up executor agents on the fly to help you get tasks done. That is one of the ways a general purpose agent solves problems. But it only does that successfully to the extent it has the tools, the identity, all of the context to know how you want the problem solved and to do so successfully. And so it still comes back to context in the end even if you're doing a more sophisticated implementation. There's another pattern worth naming. The people who have open claw configured correctly have invested a lot in the memory side of things. They either have a memory.mmarkdown file that accumulates insights over time which is closer to the original vanilla openclaw approach or they've got closer to something like the open brain approach that a lot of folks in my community are building where they have a database that the open claw can search from and get back insights on and that ends up being sort of a richer more multi-dimensional repository over time. You can have a hybrid, you can kind of work with both. The point is you have intent around memory. you know that your agent needs to learn and get better over time. And if it doesn't learn and get better over time, it's not a very smart agent and it's not going to help you for very long. And the common thread through the context piece, the separation of concerns, the ability to set up memory correctly, the ability to write all those markdown files right, the ability to maybe configure a database so your agent can query for memory. All of that means having clarity of intent around what you want the agent to do and the ability to articulate at a pretty high degree of detail what you expect the agent to do in a series of steps. Right? The human has to sit down and describe in triggerable verifiable language what you do all day to get an agent to do it. Right? Not I handle marketing, but these are the different websites I check. These are the metrics I look at. This is the spend that I'm willing to budget for. This is how I know that spend is correct. These are the equations I run. And then finally, these are the optimization and leverage opportunities I see. Now, people will say, "It's the agent's job to get better at marketing. Why are we giving it that detail?" And I will answer, you got to orient the agent toward the current context if you want to ask the agent to improve over time. You cannot just magically say, "Here's marketing. You do it agent." and it's just going to magically know all of the nuances of your context for your product and just randomly do it. That's just not how it works. And yet that underlying assumption is lying behind so many of the meto products that we see in the landscape. If we look across the landscape, and I'm going to profile them here, and we look at how agents are being built and sold right now, so many of them are being built and sold as essentially magic boxes with arms and legs. Like, here's the magic box. Type anything you want and the magic box will fix it. And it turns out if you're selling magic boxes, they'll sell like hotcakes. But the problem is once you have a magic box and it's not magical anymore, it's a disappointing experience. Let's go through each of them in turn. Obviously, Open Claw is the original. It's 250,000 or whatever number of thousand GitHub stars it is now. It runs locally on your hardware. It connects to any LLM. You talk through it through any channel, right? Telegram, WhatsApp, iMessage, Slack. Now you can phone call it like whatever you want. It's free. It's infinitely configurable and the cold start problem is entirely up to you which is appropriate because the original audience was developers. Peter Steinberger built this for developers and developers quite reasonably could be expected to write markdown files and configure their own tool set and for so many of them that was not an obstacle and so so much of this conversation is basically OpenClaw is out in the wild now. Openclaw is on the loose. Open Claw is the most copied product of 2026. What does it mean when everybody wants an agent and they're not just developers and they're like, "What is a markdown file and why should I care?" Developers, to be fair, have a little bit of an advantage at writing specifics. If you've ever sat in the product chair like I have, and you've had conversations with engineers, you know the engineers tend to be the ones and should be the ones asking you for specifics. Okay, fine. You say you want the image to appear in that way on the web page. Tell me why. Tell me what is the file size. Tell me how quickly you expect it to load. Tell me how it goes with and overlays the rest of the web experience. And that's just a very simple presentation, right? Love to get specific. And I think that mental habit has helped open claw take off for so many in the engineering community because it's actually very clear to them that you need to describe a lot of what you do in high specifics to the agent to make it useful. That's not that unusual. For the rest of us, it's a new step. Now, a bunch of folks have come into the space since OpenClaw, and the thesis for most of them has been correctly. OpenClaw was hard to install originally. Peter designed it that way on purpose. He did not want non-developers using it because you can easily configure your OpenClaw to be a security risk. And that was the dominant headline for the first month or so of OpenClaw's popularity. And so, so many players are in the space now basically saying, "We took care of security. We took care of ease of install. You don't have to worry about it." And I'm here saying that's not the real problem. That's just the first problem, right? Manis, now owned by Meta, is doing exactly that. You can either have a desktop app which has local access or you have a cloud virtual app. But either way, it's more secure. It's got a little bit of structure. You type in your query. It automatically decomposes all of that work into its own sub agents. And the idea is it's easier to use. It's more secure. It can be locally if you feel comfortable with that or in the cloud. And it's something that you can get up and running on in 10 or 15 minutes. The problem is the manness agent is really going to be limited by the lack of initial context you give it. So it's optimizing for the cold start problem in the sense that it makes it easy to type the first word, but without the ability to really deeply configure what the agent knows about you and why it cares about you and the workflows you're doing and what you're trying to accomplish and what you're trying to delegate, it's going to be somewhat limited in its ability to work with you. Now, I do know Manis users who have deliberately put intent into that platform and swear by it. They're like, "This is incredible. The more intent I put in, the better it gets." And that is kind of a universal law of AI. If you put more passion, heart, intent, clarity, and communication into the tool because these tools have memory systems, they start to learn over time and they're more useful for you. But that is not the experience of the majority of Manis users. And that brings me to the next tool, which is Perplexity's personal computer. Perplexity personal computer is in a sense the most audacious of these open claw plays. We know that we cannot get a hold of Mac minis because Apple has sold out of them because so many people want to put open claws on them. Perplexity saw that said we're a corporate account. We can get lots of Mac minis and they literally offer you a dedicated Mac Mini. It's a real Mac Mini connected to Perplexity's cloud, merging local file access with their computer orchestrator and they give you a project manager AI that routes tasks across 20 Frontier models for that Mac Mini. So, it takes away all of the pain of having a local Mac Mini. You actually have a real Mac Mini that's yours. It has an orchestrator. It has 20 models. It's a very bold vision. CEO Aravven Sinas framed it at the developer conference like this. He said a traditional operating system takes instructions and an AI operating system takes objectives. I think he is right that openclaw is popular because it is fundamentally an operating system. That is a correct insight. I think he's also correct in saying that it is about optimizing for objectives. But the piece that is challenging for most people is when you have that firepower delivered for you, all of that agentic power at your fingertips, what do you do with it? Then how do you communicate your intent in a way that actually gets across? The fundamental bet is the same as all these other ones. You state the objective for openclaw and openclaw will figure out the rest. In this case, you state the objective for perplexity personal computer and you bet the personal computer will figure out the rest. And that works well right until the objective requires knowledge about your life, your judgment patterns, your operating rhythm that no system actually has because you never wrote it down. And you may not be aware you have it, but it's in your bar for powerpoints. It's in your bar for financial products. It's in your bar for everything, and you just never realize it was written down. Let's have a look at Neimoclaw next. Nemoclaw is Nvidia's enterprise security wrapper for OpenClaw. It was launched at GTC by Jensen Hang itself. It runs agents in sandbox environments using Open Shell for privacy guardrails and Neotron for advanced model output. Basically, it's a it's a buttoned up corporatefriendly open claw with lots of security guard rails and it solves the security problem really thoroughly. The real and serious risk of an agent with full access to your machine deleting stuff like they've taken care of that. It does not solve the problem of what to put in the agents operating instructions and it effectively punts that to the enterprise. And the problem is most enterprises also don't know how to solve that problem. I know because I talk with them. They do not know out of the gate how to solve the problem of what to do with a Nemo Claw. If you roll it out to 10,000 people and only five of them have used OpenClaw in a way that's productive, those five are going to be perfectly happy and be able to use that. The other 9,995, they're not going to know what to do. They're not going to know what to do because no one trained them. And that is absolutely a larger issue with AI, but it's especially bad with agents. And the reason it's especially bad with agents and with the open claw phenomenon is that the open claw phenomenon gives you so much power. It is really a story of transformation. It does really give you that 10x potential on your work and they just do not tell you how much work you have to put in at the top to get that result and how much training you have to do if you are rolling this out to a workforce. It is not a plug it in and go solution and it never is going to be because it takes context from you. Right? I just want to be honest with you. All the people who are promising and all of these ones that I'm covering are promising this. All of them who are promising 10 minutes to open claw are right technically and wrong functionally. They're correct. Technically, you can get very very quickly up and running with your open claw. They are wrong in that you cannot get utility out of the open claw unless you put a lot more work than that into getting it ready. Claude dispatch is part of anthropic's answer and Anthropic has been investing heavily in essentially pivoting their claw product. So it is open claw like over the last month there's probably been 15 ships around this. Dispatch is the most obvious because it makes it so easy to pair your phone with your Mac and it makes it easy to send messages through whatever version of your messaging app that you want and you can now control your claude from your phone which is one of the key benefits people called out from OpenClaw in the first place because you can use your openclaw wherever you are. You can be dropping the kids off to school. You could be out looking at the beach. You can be working in the kitchen and you can be messaging your computer and getting work done. People like the mobile friendliness. It's one of the oldest bets in software. We've had this bet since 2007. Really earlier than that when we had the mobile phone revolution in 2007 with the iPhone. People like to be on the go with computing. And this is just taking your agents on the go. It's one of the oldest and most reliable bets in software. It turns out it works for agents, too. But you can't send, and I've tried this, by the way, with popular agents, you can't send a threeline or four-line text message to an agent and expect it to work well if the agent doesn't know you. And it turns out that a lot of these text message first apps do not work well if you are just introducing yourself by text. Because guess what? I have done a 15 paragraph introduction by text message to a popular open claw like application and it has completely failed because it still wasn't enough. 15 paragraphs of text that's a whole wall of text and it's still not enough to get the agent to actually get it. And so as much as it's really cool that Claude is pivoting to make it easier to message, there are a lot of developers that find it super useful, it does not by itself solve this problem. The issue here is that we need to be able to say or speak what we really mean in a way that's clear enough that an agent can run with it and we can truly delegate that task. And that is the problem none of these solutions are really solving. And that goes not just for these purpose-built solutions I profiled like perplexity personal computer or like Nemo Claw, but it also goes for the hosted rappers start claw, myclaw, simpleclaw, uniclaw, you name it, claw and and there's like dozens a week launching. They're all trying to make open clause setup easier, right? One-click deploy, preconfigured personas, managed infrastructure. They're solving all of that installation friction very successfully, which is a real UX problem. But the guy selling the $49 pack of pre-written sold out markdown files or the guy repackaging and calling it start.claw and having the exact same markdown files as a quote persona, they're not really solving that issue, right? They're giving you their generic version of what it is, not the thing that's going to be useful for you. Because the thing that makes agents useful is that they are particular, is that they are personal and you can't take that away. The people who are having transformative impact have realized they need to put the work in to make their agent personal. There is no substitute. So every product in this landscape is fighting over installation, over UI, over model selection, over security, over pricing, over cloud versus local. And they're competing on this implementation layer. And they're trying to get us to care. Do I care about the fact that I want a Mac Mini in the cloud from Perplexity? Is that better? I don't even know how to assess that in most cases, right? Most people don't. And every product in this landscape breaks against that same wall, right? The human on the other end has to understand what they need to do and produce a usable spec for the agent to do that task. And that is actually much more important to the long-term value of the agent than just a particular kind of installation, which is just a one-time problem. And so that wall, there's a reason why products are not going after that. It's a structural property of how expertise works. And it's actually a really hard problem. It's not easy. You can't solve it with UX. And here's where it would be easy for me to hop off and say, "Well, it's really hard. We're done." But I want to go deeper. What it makes it difficult for people to describe what they do. Because that observation, while true, doesn't explain why this is happening and why we find it hard. And there's a larger story there. If you don't understand the mechanism, you're going to waste time on solutions that don't address the root cause. Knowledge work has a structural property that makes it uniquely resistant to delegation, whether that's delegation to humans or delegation to machines. And that property is this. The more senior and valuable you become, the more your work migrates from explicit processes to tacit judgment, and the less visible your own operating system becomes to you, the person using it. And this is not a failure of good intentions. This is not a failure of self-awareness. It's the intended outcome of how expertise actually develops. When you're a beginner, everything is very conscious. It's very deliberate. When I started to play basketball, when I was in middle school, I was focusing on dribbling so hard and eventually you start to get good at dribbling the ball. You don't think about it as much. So, you follow the checklist and knowledge work to begin as an intern. You think through every step. As you gain expertise, all of those steps compress into automatic patterns. Just as when you drive a car today, you don't think about turning right after 20 years of driving a car. It just happens. You stop thinking about your knowledge work. You stop thinking about what to check. You just check it. You stop reasoning through decisions and you just make them. But the reasoning still happens. The thing that makes you fast and effective is the same thing that makes your knowledge very inaccessible. It's been compiled from source code into machine code. metaphorically speaking and you no longer have the source code. Let's take an example of a really senior product manager. They don't think I should cross reference the revenue dashboard with the churn data before forming an opinion. Instead, they'll open three tabs. They'll glance at the numbers and they just know. And if you ask what was checked and can you reconstruct and explain what happened, they'll narrate backwards from the conclusion, but they're not they're not really going to describe the actual process in most cases because it's so low level. The real decision often involved a hundred micro evaluations that re reflect thousands of hours of patterns that that product manager has seen over multiple startups. But but that doesn't get articulated, right? The magical pattern matching that allowed the deep insight that they had about churn is something that is a function of all of those thousands of hours. It's not something you can substitute for with just an explicit intern checklist. It it doesn't work that way. Now, you might stop here and say, "Well, then there's no point in agents." And I will come back and I'll say, "No, the stories of agents making you insanely productive are all true." And our goal is to make more of those stories. And I am telling you what it takes. And the first thing we have to acknowledge is that knowledge work is really hard. A strong salesperson doesn't consciously decide to mirror their prospect's phrasing and slow their cadence where they when they detect defense. a strong salesperson, they don't consciously decide to mirror the prospect's phrasing and slow down their cadence when they detect that that they're just a little defensive. They just do that. A senior engineer doesn't think, well, this code has a concurrency issue that'll service under load on Tuesdays because we have a lot of email traffic on Tuesdays and when the batch job overlaps with the peak traffic, we're going to have issues. They they may be able to get to that point and tell you later, but initially they just feel it. They say, "Oh, that's bad." and then they go look and then they're right and then everyone calls it experience. This is worth digging into because it's the root cause of a product failure happening at an absolutely massive scale across the industry. The entire agent ecosystem is built on a model where the human provides instructions and the machine executes them. That model works when the instructions are really clear like summarize the document, right? Super easy. Reformat the spreadsheet. But it breaks when the instructions require expertise that the human genuinely has but struggles to articulate. And almost all of the most valuable knowledge work that agents can tackle lies in that second category. In other words, 2026, the year of these long-running agents that do impactful knowledge work, only really delivers on that promise if we can get into the very hard problem of explaining to these agents this tacit knowledge, work, and judgment that makes us good at what we do. We have to think through what does it mean to have deep insights about churn and actually articulate enough of our personal experience to give the agent something to work against. Not because the agent has to mimic us like a parrot, but because the agent needs to orient enough in our local context that it can then go beyond that and continue to optimize and deliver insights. Because the best agents do that, right? the best agents know enough about your context and what you're trying to do that they can then go beyond that and deliver really interesting novel insights you wouldn't have expected. That's fantastic. That's the dream. It does really happen. But you got to give them enough out of your tacid experience to actually make that possible. Think about what a good sold out markdown file contains. It's not just a personality description. It's it's a decision framework. when to escalate versus how you handle things autonomously, what what tone to use with different audiences, which data sources are are you going to trust versus which ones are you skeptical of, what is good enough at various task types. That's the same thing a strong vice president would put in an operating memo for the team when he or she joins the team for the first time. And most VPs, honestly, they haven't written that down either. I' I've been under a number who have moved in new, and most of them don't send an operating memo like that, even though they should. This is also the same reason why senior engineers notoriously are pretty bad at writing onboarding docs. It's not laziness. It's that the knowledge that would make the doc useful has been sort of compressed into a form of automatic behavior for them and the doc is going to list steps but miss so much nuance that they have in their heads because it just makes sense for them. It's like the person who's describing the way to uh a friend's house down the road and they're giving you all of these landmarks that are local to them that make sense. It's like there's the big tree and then you stop by the the the store that has the broken down sign and then you go over it. This is no like as a stranger in these parts, you don't understand it, but they understand all of the nuances that help them get to their friend's house. And the structural trap is this. The people with the most to gain from agent delegation are exactly the people whose work is hardest to delegate. The most senior, most overloaded knowledge workers carry the highest ratio of tacet to explicit knowledge. Their work is the most compressed. It's the most invisible to themselves. They need the leverage most and the cold start problem hits them the hardest. Ironically, beginners just getting started in their careers. Folks who are you're one year, two years out of college and all of this is stuff that you are still doing intentionally, explicitly in your head, you haven't compressed it yet. You may have a much easier time with agents and delegating to OpenClaw than the seniors. And the reason I say that is because you have not gone through that automation process in your head yet. And that's actually fantastic and it's one of the reasons why firms like Shopify intentionally hire juniors because there are things that you can go much faster at than seniors. And ironically, this inability to sort of get our operational knowledge, our tacet knowledge out of our heads is at the root of at least three big chronic people problems that plague most organizations. Delegation fails. That's that's one of them, right? Managers will cite that as a key challenge. And the standard explanation is that they're control freaks. But the real explanation is that they don't know how to delegate because they don't know how to express what they've got in their heads. It's it's a real challenge for new managers. Another related one, people not getting promoted. The most common reason strong IC's plateau is that they cannot be replaced. Their knowledge work is locked in their head. And so even if they are qualified for the next level, no one wants to risk losing their expertise on their current job and that becomes a trap for them. And then of course the third one is obvious. People leave. Institutional knowledge evaporates. it walks out the door in someone's head and and it's just gone. So, I would argue agents did not create these problems, but agents create the first universal selfish incentive for every single one of us in knowledge work to actually fix these problems. Not because HR launched a knowledge management initiative, right? It's not because a consultant ran a workshop. It's because you personally want a robot to stop asking you to confirm calendar entries that you already freaking approved. and the robot needs you to describe your calendar rules first. That's new. Look, we've had decades of top- down pressure to externalize our knowledge. It never worked at scale because there was no direct personal upside for any of us. The benefit occurred entirely to the organization when you wrote the wiki, right? A and traditionally, the person who documents their expertise is the person who loses. In this case, agents flip that incentive structure on its head. The person who documents their expertise is the person who gets the leverage in the world of agents. The organization might benefit secondarily. It's actually a bottoms up knowledge management revolution disguised as a consumer AI product. And I don't think that anyone, including the people building these products, really appreciates that because if they did appreciate it, I feel like they would put more into onboarding. I have been through the onboarding flows for like half a dozen of these and they all feel really, really light. Really light for what you're expecting this agent to do, for what you're hoping it will do for you. If you want it to really lift up, leverage two, three, or more X your work. And that and that leads us to a very uncomfortable correlary that's worth naming explicitly. If the value of agents depends on your ability to articulate your work, agents are about to create an extremely visible divide in the workforce. Right now, tacet knowledge is invisible, right? Nobody knows that you can't describe your own process because nobody's ever asked you. Performance reviews tend to measure your outputs, not your self-nowledge. You might be a phenomenal operator with zero ability to explain how you operate and the system just never penalizes you and agents are about to change that. In a world where everyone has access to the same tooling, the differentiator is not which model you use or how many Mac minis you can put your open claws on. It's whether you can feed the thing well enough to actually get leverage. The people who invest that time, who can decompose their expertise into explicit delegatable components will get compounding returns. That's where the value is. Their agents improve because their specs improve. The second agent deploys faster than the first. The 10th deploys in a few minutes and they actually build on all of that knowledge. So, it doesn't even take them a ton of time to provision it because they understand the memory system so well. The people who skip all of that will install, play for a weekend, hit the wall, and conclude agents are all hype. And they will be wrong. The agent worked fine. The problem was never the agent. So, I want to propose a solution. I've gone through the problem. You understand the problem. The solution I have is this. The first agent you run should not be your open claw assistant. The first agent you run should be a tool to prepare you to run agents the way you want. And no one seems to be thinking this way, so I'm just going to say it out loud. The first agent worth deploying, it's not your personal assistant. It's not your chief of staff. It's not your scheduler. It's not your email uh guy. It's not your briefing bot. It's just an interviewer. It is one designed to do what expertise elicitation researchers do. Yes, that's a real job. Ask you the right questions in the right order with the right follow-ups to extract the operational knowledge you carry but cannot access on your own. And no, this is not the same as asking you three questions on install. I know that OpenClaw asks you who am I, who are you, and what is my job? I get that. This is a lot deeper than that. And of course, I've been building this. I've been digging in because I want to build a demo that actually allows you to immediately use this so that if you have trouble actually using your agent and making it valuable, you have a tool now to get your agent going. It's a structured elicitation workflow. I know it's a $10 word, but it basically means getting that information out of your head. Uh, it's a structured elicitation workflow that walks you through five specific layers. Your operating rhythms, what are your days, your weeks, and your months actually like in detail, not the calendar version, the real one. Your actual recurring decisions, what judgment calls you make, what are the easy calls, the hard calls, what inputs that you actually need, your dependency, who do you need things from, and when. Nobody's asking that, right? They've been through these flows. Your friction, the recurring annoyances that eat your time. Most of them don't ask that either. It takes time. I'm not going to pretend this doesn't take time, right? Like I've gone through it at best. It takes 45 minutes. It might take you longer. And and I think that time is worth it if you're going to actually save time on your agent, right? The output is structured data and you can plug it right into your open brain if you've built that. That's just a simple personal knowledge store uh that's quick to set up and runs for like 10 cents a month. Uh and then it becomes durable, right? it becomes searchable knowledge and it's available to any agent that interacts with an MCP which all of these openclaw agents do by the way and from that output I built a configuration file generator that will automatically produce soul.markdown heartbeat.mmarkdown user.mmarkdown files that you can use to provision an openclaw and that solves the gap that solves the gap that manis isn't building for perplexity isn't building for nemo claw isn't building for dispatch skips over this and to be honest with you the configuration files that I can output. And to be honest with you, the configuration files you get at the end of this process are in some ways the least interesting output. The more valuable output is the conversation itself and the way it creates a structured database, a structured map of how you work, what you know, where your leverage points are. And that makes you so much better at delegating to agents. Yes. But also talking about it means you're better at delegating to people. It makes you easier to promote. It makes your expertise survivable. All of this stuff that was locked in your head, you had an AI agent help you get it out. And that's what I focused on building. The AI agent that helps you get it out. And yes, it does help you make your agents work, which is kind of the whole reason you'd have agents. I know that every agent product in the market today is competing on the implementation layer. How easy is it to set up from scratch with your open claw? Fine. The question I have is once you have it set up, can you actually use it to do interesting stuff? Can you actually use it in ways that help your workflow? And the only way it will ever do that is if it gets into your brain and gets the stuff out that you don't think about every day. And that's why I built an open brain interview agent to help you get that knowledge out so that you can provision whatever open claw you choose in whatever way you choose confident that it actually knows the details, the nuance, the depth of your work in a way that will make it effective because that depth is where you get the disproportionate returns. That's how the people who are getting these three, four, 5x returns are doing it. So don't make your first agent the agent that is your personal assistant. Instead, make your first agent the one that prepares you to have a personal assistant agent. The extra work is worth it. I promise. Cheers.

---

## Timestamped Segments

**[0:00]** Agents by themselves don't make you productive. I'm just going to say it straight out. So many people right now

**[0:06]** are running to OpenClaw with 250,000 GitHub stars or they're they're VCs and their builders and all they can do is

**[0:12]** they can build copycats of OpenClaw. And everyone assumes that as soon as you get

**[0:17]** the agent, you'll know what to do with it. And there's a massive gap between I can install an agent, which everyone has

**[0:23]** now solved for. You can install an agent in 10 seconds. By the time I have finished saying this sentence, you can have an agent up and going. that's how

**[0:29]** fast these things are going now. That's not the point. Whether you can use it productively is actually the question

**[0:35]** that matters. And yes, all of those people who are out there who are making lots of clickbait who are saying, "I

**[0:40]** used my agent to do lots and lots of stuff. I have 10 agents that do this and that. I have two agents that do this and that. I manage my whole $5 billion

**[0:47]** company with agents." Those are all true stories, but they're only true stories

**[0:53]** because someone figured out how to clarify enough of what they were looking to do to give it to an agent. And that

**[0:59]** turns out to be a very, very hard problem. And it's funnily enough, not a

**[1:04]** problem that most companies out there are interested in solving. And I know because I went through and I looked at

**[1:10]** all the products. And so in this video, we are going to go through and talk about the real gap that's upstream of

**[1:16]** all of these open claw agent metos. We're going to go through and survey the different approaches to building your

**[1:22]** agents, the different ways these products are handling open claw like implementations. And then we're going to

**[1:28]** talk about how you actually solve this problem. And yes, I built something to solve it. I want you to have an easier

**[1:34]** time using your agent. Right? Let's assume you have an agent because now it's very easy to get one. how do you

**[1:39]** use it? And so I built something to make that jump into using the agent much much easier. And we'll get to that. The most

**[1:46]** common message I've been able to find in most open claw community forums is this. Now what? It's really simple. Like I I

**[1:54]** did it. Now what's next? How do I go from here? Variants of that, right? Like I have installed the open claw. Now what

**[1:59]** do I do next? It's not really how do I fix this error. It's not which model do I use? Although there's a few of those.

**[2:05]** It's just I got it to run, which is great, and I don't know what to tell it, right? Give me a recipe. Give me

**[2:12]** something to do. And I think there's a structural reason this keeps happening. And I don't think the correct fix is

**[2:17]** just to hand out recipe cards for openclaw use cases because that's not really what you want an agent to do. The

**[2:22]** whole reason we have an agent is because it does many things well. It doesn't just do one thing. Well, if you start telling your agent, hey, here's my, you

**[2:30]** know, expensive Mac Mini. Here's my expensive cloud subscription. Now you triage my email. Is that really a good

**[2:35]** use for your dollars? Yet a lot of people, the most common use of OpenClaw is triaging your email. We need to

**[2:41]** understand why agent implementations are not delivering the 10x ROI that have

**[2:47]** been promised for so many people. And we need to be honest about it or there's going to be a lot of people who are a little bit frustrated. There are going

**[2:53]** to be people who are lining up to undo OpenClaw if we're not careful. And I say that because there actually have been

**[2:59]** cases of lines in China where people who had previously installed OpenClaw are

**[3:04]** going back and standing in line to uninstall it because they didn't want it. I don't want that to happen. So here's what I'm going to dig into. I'm

**[3:09]** going to dig into the common patterns across agent implementations that really work. I'm going to dig into the meto

**[3:14]** landscape and why every open clawike product is kind of aiming at the same target and kind of hitting the same wall

**[3:20]** when it comes to success. And I'm going to dig into the structural reasons why it's really really difficult for us to

**[3:26]** actually explain what we need to do with these agents in a way that they can understand. I'm going to explain a

**[3:33]** little bit about why I think this is the larger problem. It goes beyond agents and then we're going to get into what to do about it. How do we solve it? So

**[3:39]** let's jump in. All right. We're gonna start with a story of Brad Mills. This is a real story. Brad spent 40 hours building a

**[3:46]** delegation framework for his OpenClaw agent. Not 40 hours installing. I want to be very clear. The install took 10

**[3:52]** minutes. He spent 40 hours writing standards, accountability rules, a definition of done for every single

**[3:57]** project. He transcribed 200 hours of videos into a searchable knowledge base. 40 hours of trying to describe what he

**[4:04]** wanted, right? I'm not making that up. That's like a week of work and it still did not work. And he wrote about it

**[4:09]** publicly, right? Constant failure. He wrote fail after fail after fail. Two steps forward, one step back. and he

**[4:16]** ended up micromanaging the agent harder than he'd ever had to micromanage a human. And the autonomy that so many

**[4:22]** other stories share felt in practice like the second job of supervising something that confidently reports tasks

**[4:28]** complete when it's not really done. Brad is not an outlier here. I would say Brad is closer to the median experience than

**[4:36]** a lot of the folks who are promising 10x results. One prominent OpenClaw guide creator reports getting flooded with DMs

**[4:43]** all the time right after setup. The stuck point is not installation anymore. We figured that out. It's actually

**[4:48]** figuring out what to do with the agent and how to make it understand your specific context. Right? Another user

**[4:54]** asked his agent to write five cold email variants. The agent sent done and wrote nothing. And his solution was to build a

**[5:00]** second adversarial auditor agent whose only job was to verify the first agent completed the task. He needed a

**[5:06]** management layer because the worker couldn't be trusted to self-report. And this became like a nesting turtles

**[5:11]** problem. like you just have issues managing the agents because you don't understand how agent architecture works

**[5:17]** if you've just spent 10 minutes on an open claw installation and you've just heard about it on the internet a day ago. Another user tried rolling out

**[5:24]** agents to a team and he gave everyone access and just called it done. It technically worked, he pointed out, but

**[5:29]** it was completely useless because nobody had mapped their workflows, their decisions, their data needs in advance

**[5:35]** and no one knew what to give the agent as a task that would be successful. Without all that upstream work, the agent stayed so generic it was useless.

**[5:43]** And a generic agent with right access to your email is actually worse than no agent at all. It's a liability with a

**[5:48]** chat interface. Right? There are whole business models emerging on places like X to fix this. Right? That is how bad an

**[5:55]** issue it is. There's a guy on X I saw selling a $49 pack of pre-written config files. A soul.markdown file, a

**[6:02]** heartbeat.mmarkdown file, a user.mmarkdown file. is core files for OpenClaw. The whole stack specifically

**[6:07]** marketed to quote skip 40 hours of OpenClaw setup. You can build a small

**[6:12]** business around the gap between installed and useful. And that tells you something about where the agent market

**[6:18]** is. But before we talk too much more about what's broken, let's talk about what does work. Because there's a

**[6:23]** pattern across hundreds of thousands of Open Claw installations. The deployments that stick, the ones where people are

**[6:28]** still getting daily value weeks and months later, they share a particular architecture and it has almost nothing

**[6:34]** to do with which model you end up picking. The successful setups all have a set of markdown files that function as

**[6:41]** the agent's operating system. If you open theopenclaw directory on anyone running a working agent, you'll find the

**[6:47]** same structure. There's a soul. Markdown file that defines the agent's role, its job, its tone, its boundaries, basically

**[6:53]** a job description. There's an identity.mmarkdown which has its name. It has its personality constraints.

**[7:00]** There's a user.mmarkdown with a detailed profile of the human including preferences, schedule patterns,

**[7:05]** communication style. And there's a heartbeat markdown with a checklist that the agent reviews every half hour to

**[7:11]** decide if there's work to do. And then there's a very simple cron job that maps that human's actual operating rhythm.

**[7:18]** None of this is particularly technically difficult. And I want to underline this three times. None of what I just

**[7:23]** described is artificial intelligence. It's just plain text. But the quality of

**[7:28]** those files determines whether your artificial intelligence agent is actually any good at anything at all. So

**[7:34]** the people who run multiple specialized agents, the not the one do everything bot, right? But a team with clear roles

**[7:41]** and scoped access, you know how you've seen the clickbait, right? Well, I have a marketing manager for this and then I have my scheduler for this and I have my

**[7:48]** CEO for this and I have my chief of staff for this. Okay, fine. The only way that works is if each agent has truly

**[7:55]** its own identity, its own markdown files, its own tool sets, its own workspace so it can get jobs done and it

**[8:01]** doesn't share context with other agents. They have clear jurisdictions. We would say they have clear separation of

**[8:06]** concerns in engineering speak. And that same clarity shows up everywhere you see

**[8:12]** a multi- aent system working. So, people running specialist bots in Slack that delegate to each other like co-workers,

**[8:18]** which you've also seen demos of, I'm sure, where someone asks a question and the orchestrator agent decides that the

**[8:24]** specialist should handle it. There's a whole flow, right? These are not toy demos. They're running daily. Those are

**[8:30]** real orchestration patterns. They really work and they and they only work because there's a clear separation of concerns

**[8:36]** and a clear identity that's separate for each of the agents involved. Now you can absolutely in more sophisticated

**[8:43]** implementations use your open claw as a general planner and have it spin up

**[8:49]** executor agents on the fly to help you get tasks done. That is one of the ways a general purpose agent solves problems.

**[8:56]** But it only does that successfully to the extent it has the tools, the identity, all of the context to know how

**[9:04]** you want the problem solved and to do so successfully. And so it still comes back to context in the end even if you're

**[9:09]** doing a more sophisticated implementation. There's another pattern worth naming. The people who have open

**[9:15]** claw configured correctly have invested a lot in the memory side of things. They

**[9:20]** either have a memory.mmarkdown file that accumulates insights over time which is closer to the original vanilla openclaw

**[9:26]** approach or they've got closer to something like the open brain approach that a lot of folks in my community are

**[9:32]** building where they have a database that the open claw can search from and get back insights on and that ends up being

**[9:38]** sort of a richer more multi-dimensional repository over time. You can have a hybrid, you can kind of work with both.

**[9:44]** The point is you have intent around memory. you know that your agent needs

**[9:49]** to learn and get better over time. And if it doesn't learn and get better over time, it's not a very smart agent and it's not going to help you for very

**[9:55]** long. And the common thread through the context piece, the separation of concerns, the ability to set up memory

**[10:00]** correctly, the ability to write all those markdown files right, the ability to maybe configure a database so your agent can query for memory. All of that

**[10:07]** means having clarity of intent around what you want the agent to do and the

**[10:12]** ability to articulate at a pretty high degree of detail what you expect the agent to do in a series of steps. Right?

**[10:19]** The human has to sit down and describe in triggerable verifiable language what you do all day to get an agent to do it.

**[10:26]** Right? Not I handle marketing, but these are the different websites I check. These are the metrics I look at. This is

**[10:32]** the spend that I'm willing to budget for. This is how I know that spend is correct. These are the equations I run.

**[10:39]** And then finally, these are the optimization and leverage opportunities I see. Now, people will say, "It's the

**[10:44]** agent's job to get better at marketing. Why are we giving it that detail?" And I will answer, you got to orient the agent

**[10:50]** toward the current context if you want to ask the agent to improve over time. You cannot just magically say, "Here's

**[10:57]** marketing. You do it agent." and it's just going to magically know all of the nuances of your context for your product

**[11:03]** and just randomly do it. That's just not how it works. And yet

**[11:08]** that underlying assumption is lying behind so many of the meto products that

**[11:14]** we see in the landscape. If we look across the landscape, and I'm going to profile them here, and we look at how

**[11:19]** agents are being built and sold right now, so many of them are being built and sold as essentially magic boxes with

**[11:25]** arms and legs. Like, here's the magic box. Type anything you want and the magic box will fix it. And it turns out

**[11:31]** if you're selling magic boxes, they'll sell like hotcakes. But the problem is once you have a magic box and it's not

**[11:37]** magical anymore, it's a disappointing experience. Let's go through each of them in turn. Obviously, Open Claw is

**[11:43]** the original. It's 250,000 or whatever number of thousand GitHub stars it is now. It runs locally on your hardware.

**[11:48]** It connects to any LLM. You talk through it through any channel, right? Telegram, WhatsApp, iMessage, Slack. Now you can

**[11:54]** phone call it like whatever you want. It's free. It's infinitely configurable and the cold start problem is entirely

**[12:00]** up to you which is appropriate because the original audience was developers. Peter Steinberger built this for

**[12:05]** developers and developers quite reasonably could be expected to write markdown files and configure their own

**[12:11]** tool set and for so many of them that was not an obstacle and so so much of this conversation is basically OpenClaw

**[12:17]** is out in the wild now. Openclaw is on the loose. Open Claw is the most copied product of 2026. What does it mean when

**[12:23]** everybody wants an agent and they're not just developers and they're like, "What is a markdown file and why should I care?" Developers, to be fair, have a

**[12:30]** little bit of an advantage at writing specifics. If you've ever sat in the product chair like I have, and you've had conversations with engineers, you

**[12:37]** know the engineers tend to be the ones and should be the ones asking you for specifics. Okay, fine. You say you want

**[12:44]** the image to appear in that way on the web page. Tell me why. Tell me what is

**[12:49]** the file size. Tell me how quickly you expect it to load. Tell me how it goes with and overlays the rest of the web

**[12:55]** experience. And that's just a very simple presentation, right? Love to get specific. And I think that mental habit

**[13:01]** has helped open claw take off for so many in the engineering community because it's actually very clear to them

**[13:07]** that you need to describe a lot of what you do in high specifics to the agent to make it useful. That's not that unusual.

**[13:12]** For the rest of us, it's a new step. Now, a bunch of folks have come into the space since OpenClaw, and the thesis for

**[13:18]** most of them has been correctly. OpenClaw was hard to install originally. Peter designed it that way on purpose.

**[13:24]** He did not want non-developers using it because you can easily configure your OpenClaw to be a security risk. And that

**[13:30]** was the dominant headline for the first month or so of OpenClaw's popularity. And so, so many players are in the space

**[13:35]** now basically saying, "We took care of security. We took care of ease of install. You don't have to worry about it." And I'm here saying that's not the

**[13:42]** real problem. That's just the first problem, right? Manis, now owned by Meta, is doing exactly that. You can either have a desktop app which has

**[13:49]** local access or you have a cloud virtual app. But either way, it's more secure. It's got a little bit of structure. You

**[13:55]** type in your query. It automatically decomposes all of that work into its own sub agents. And the idea is it's easier

**[14:01]** to use. It's more secure. It can be locally if you feel comfortable with that or in the cloud. And it's something that you can get up and running on in 10

**[14:08]** or 15 minutes. The problem is the manness agent is really going to be limited by the lack of initial context

**[14:15]** you give it. So it's optimizing for the cold start problem in the sense that it makes it easy to type the first word,

**[14:20]** but without the ability to really deeply configure what the agent knows about you

**[14:25]** and why it cares about you and the workflows you're doing and what you're trying to accomplish and what you're trying to delegate, it's going to be

**[14:31]** somewhat limited in its ability to work with you. Now, I do know Manis users who have deliberately put intent into that

**[14:38]** platform and swear by it. They're like, "This is incredible. The more intent I put in, the better it gets." And that is kind of a universal law of AI. If you

**[14:45]** put more passion, heart, intent, clarity, and communication into the tool because these tools have memory systems,

**[14:51]** they start to learn over time and they're more useful for you. But that is not the experience of the majority of

**[14:58]** Manis users. And that brings me to the next tool, which is Perplexity's personal computer. Perplexity personal

**[15:03]** computer is in a sense the most audacious of these open claw plays. We know that we cannot get a hold of Mac

**[15:09]** minis because Apple has sold out of them because so many people want to put open claws on them. Perplexity saw that said

**[15:15]** we're a corporate account. We can get lots of Mac minis and they literally offer you a dedicated Mac Mini. It's a

**[15:22]** real Mac Mini connected to Perplexity's cloud, merging local file access with their computer orchestrator and they

**[15:29]** give you a project manager AI that routes tasks across 20 Frontier models for that Mac Mini. So, it takes away all

**[15:36]** of the pain of having a local Mac Mini. You actually have a real Mac Mini that's yours. It has an orchestrator. It has 20

**[15:42]** models. It's a very bold vision. CEO Aravven Sinas framed it at the developer conference like this. He said a

**[15:47]** traditional operating system takes instructions and an AI operating system takes objectives. I think he is right

**[15:54]** that openclaw is popular because it is fundamentally an operating system. That is a correct insight. I think he's also

**[16:00]** correct in saying that it is about optimizing for objectives. But the piece

**[16:05]** that is challenging for most people is when you have that firepower delivered for you, all of that agentic power at

**[16:12]** your fingertips, what do you do with it? Then how do you communicate your intent in a way that actually gets across? The

**[16:18]** fundamental bet is the same as all these other ones. You state the objective for openclaw and openclaw will figure out

**[16:24]** the rest. In this case, you state the objective for perplexity personal computer and you bet the personal computer will figure out the rest. And

**[16:30]** that works well right until the objective requires knowledge about your life, your judgment patterns, your

**[16:36]** operating rhythm that no system actually has because you never wrote it down. And you may not be aware you have it, but

**[16:43]** it's in your bar for powerpoints. It's in your bar for financial products. It's in your bar for everything, and you just

**[16:48]** never realize it was written down. Let's have a look at Neimoclaw next. Nemoclaw is Nvidia's enterprise security wrapper

**[16:53]** for OpenClaw. It was launched at GTC by Jensen Hang itself. It runs agents in sandbox environments using Open Shell

**[17:00]** for privacy guardrails and Neotron for advanced model output. Basically, it's a it's a buttoned up corporatefriendly

**[17:06]** open claw with lots of security guard rails and it solves the security problem really thoroughly. The real and serious

**[17:13]** risk of an agent with full access to your machine deleting stuff like they've taken care of that. It does not solve

**[17:19]** the problem of what to put in the agents operating instructions and it effectively punts that to the enterprise. And the problem is most

**[17:25]** enterprises also don't know how to solve that problem. I know because I talk with them. They do not know out of the gate

**[17:31]** how to solve the problem of what to do with a Nemo Claw. If you roll it out to 10,000 people and only five of them have

**[17:38]** used OpenClaw in a way that's productive, those five are going to be perfectly happy and be able to use that. The other 9,995,

**[17:46]** they're not going to know what to do. They're not going to know what to do because no one trained them. And that is absolutely a larger issue with AI, but

**[17:52]** it's especially bad with agents. And the reason it's especially bad with agents and with the open claw phenomenon is

**[17:58]** that the open claw phenomenon gives you so much power. It is really a story of

**[18:03]** transformation. It does really give you that 10x potential on your work and they just do not tell you how much work you

**[18:10]** have to put in at the top to get that result and how much training you have to do if you are rolling this out to a

**[18:15]** workforce. It is not a plug it in and go solution and it never is going to be because it takes context from you.

**[18:21]** Right? I just want to be honest with you. All the people who are promising and all of these ones that I'm covering are promising this. All of them who are

**[18:28]** promising 10 minutes to open claw are right technically and wrong functionally. They're correct.

**[18:33]** Technically, you can get very very quickly up and running with your open claw. They are wrong in that you cannot

**[18:40]** get utility out of the open claw unless you put a lot more work than that into getting it ready. Claude dispatch is

**[18:46]** part of anthropic's answer and Anthropic has been investing heavily in essentially pivoting their claw product.

**[18:51]** So it is open claw like over the last month there's probably been 15 ships around this. Dispatch is the most

**[18:57]** obvious because it makes it so easy to pair your phone with your Mac and it makes it easy to send messages through

**[19:02]** whatever version of your messaging app that you want and you can now control your claude from your phone which is one

**[19:07]** of the key benefits people called out from OpenClaw in the first place because you can use your openclaw wherever you

**[19:13]** are. You can be dropping the kids off to school. You could be out looking at the beach. You can be working in the kitchen

**[19:19]** and you can be messaging your computer and getting work done. People like the mobile friendliness. It's one of the

**[19:24]** oldest bets in software. We've had this bet since 2007. Really earlier than that when we had the mobile phone revolution

**[19:29]** in 2007 with the iPhone. People like to be on the go with computing. And this is just taking your agents on the go. It's

**[19:36]** one of the oldest and most reliable bets in software. It turns out it works for agents, too. But you can't send, and

**[19:42]** I've tried this, by the way, with popular agents, you can't send a threeline or four-line text message to

**[19:49]** an agent and expect it to work well if the agent doesn't know you. And it turns out that a lot of these text message

**[19:55]** first apps do not work well if you are just introducing yourself by text.

**[20:02]** Because guess what? I have done a 15 paragraph introduction by text message

**[20:07]** to a popular open claw like application and it has completely failed because it

**[20:13]** still wasn't enough. 15 paragraphs of text that's a whole wall of text and it's still not enough to get the agent

**[20:20]** to actually get it. And so as much as it's really cool that Claude is pivoting to make it easier to message, there are

**[20:25]** a lot of developers that find it super useful, it does not by itself solve this problem. The issue here is that we need

**[20:32]** to be able to say or speak what we really mean in a way that's clear enough that an agent can run with it and we can

**[20:38]** truly delegate that task. And that is the problem none of these solutions are really solving. And that goes not just

**[20:43]** for these purpose-built solutions I profiled like perplexity personal computer or like Nemo Claw, but it also

**[20:50]** goes for the hosted rappers start claw, myclaw, simpleclaw, uniclaw, you name it, claw and and there's like dozens a

**[20:56]** week launching. They're all trying to make open clause setup easier, right? One-click deploy, preconfigured

**[21:02]** personas, managed infrastructure. They're solving all of that installation friction very successfully, which is a

**[21:08]** real UX problem. But the guy selling the $49 pack of pre-written sold out markdown files or the guy repackaging

**[21:14]** and calling it start.claw and having the exact same markdown files as a quote persona, they're not really solving that

**[21:21]** issue, right? They're giving you their generic version of what it is, not the thing that's going to be useful for you.

**[21:27]** Because the thing that makes agents useful is that they are particular, is that they are personal and you can't

**[21:32]** take that away. The people who are having transformative impact have realized they need to put the work in to make their agent personal. There is no

**[21:39]** substitute. So every product in this landscape is fighting over installation, over UI, over model selection, over

**[21:46]** security, over pricing, over cloud versus local. And they're competing on this implementation layer. And they're trying to get us to care. Do I care

**[21:52]** about the fact that I want a Mac Mini in the cloud from Perplexity? Is that better? I don't even know how to assess that in most cases, right? Most people

**[21:58]** don't. And every product in this landscape breaks against that same wall, right? The human on the other end has to

**[22:05]** understand what they need to do and produce a usable spec for the agent to do that task. And that is actually much

**[22:12]** more important to the long-term value of the agent than just a particular kind of installation, which is just a one-time

**[22:18]** problem. And so that wall, there's a reason why products are not going after that. It's a structural property of how

**[22:24]** expertise works. And it's actually a really hard problem. It's not easy. You can't solve it with UX. And here's where

**[22:30]** it would be easy for me to hop off and say, "Well, it's really hard. We're done." But I want to go deeper. What it

**[22:35]** makes it difficult for people to describe what they do. Because that observation, while true, doesn't explain

**[22:41]** why this is happening and why we find it hard. And there's a larger story there. If you don't understand the mechanism,

**[22:46]** you're going to waste time on solutions that don't address the root cause. Knowledge work has a structural property

**[22:52]** that makes it uniquely resistant to delegation, whether that's delegation to humans or delegation to machines. And

**[22:58]** that property is this. The more senior and valuable you become, the more your work migrates from explicit processes to

**[23:05]** tacit judgment, and the less visible your own operating system becomes to you, the person using it. And this is

**[23:12]** not a failure of good intentions. This is not a failure of self-awareness. It's the intended outcome of how expertise

**[23:20]** actually develops. When you're a beginner, everything is very conscious. It's very deliberate. When I started to

**[23:26]** play basketball, when I was in middle school, I was focusing on dribbling so hard and eventually you start to get

**[23:31]** good at dribbling the ball. You don't think about it as much. So, you follow the checklist and knowledge work to begin as an intern. You think through

**[23:37]** every step. As you gain expertise, all of those steps compress into automatic patterns. Just as when you drive a car

**[23:43]** today, you don't think about turning right after 20 years of driving a car. It just happens. You stop thinking about

**[23:51]** your knowledge work. You stop thinking about what to check. You just check it. You stop reasoning through decisions and

**[23:56]** you just make them. But the reasoning still happens. The thing that makes you fast and effective is the same thing

**[24:01]** that makes your knowledge very inaccessible. It's been compiled from source code into machine code.

**[24:06]** metaphorically speaking and you no longer have the source code. Let's take an example of a really senior product

**[24:12]** manager. They don't think I should cross reference the revenue dashboard with the churn data before forming an opinion.

**[24:18]** Instead, they'll open three tabs. They'll glance at the numbers and they just know. And if you ask what was

**[24:23]** checked and can you reconstruct and explain what happened, they'll narrate backwards from the conclusion, but

**[24:28]** they're not they're not really going to describe the actual process in most cases because it's so low level. The

**[24:34]** real decision often involved a hundred micro evaluations that re reflect thousands of hours of patterns that that

**[24:41]** product manager has seen over multiple startups. But but that doesn't get articulated, right? The magical pattern

**[24:47]** matching that allowed the deep insight that they had about churn is something that is a function of all of those

**[24:52]** thousands of hours. It's not something you can substitute for with just an explicit intern checklist. It it doesn't

**[24:58]** work that way. Now, you might stop here and say, "Well, then there's no point in agents." And I will come back and I'll say, "No, the stories of agents making

**[25:05]** you insanely productive are all true." And our goal is to make more of those

**[25:10]** stories. And I am telling you what it takes. And the first thing we have to acknowledge is that knowledge work is

**[25:15]** really hard. A strong salesperson doesn't consciously decide to mirror their prospect's phrasing and slow their

**[25:21]** cadence where they when they detect defense. a strong salesperson, they don't consciously decide to mirror the

**[25:27]** prospect's phrasing and slow down their cadence when they detect that that they're just a little defensive. They

**[25:32]** just do that. A senior engineer doesn't think, well, this code has a concurrency issue that'll service under load on

**[25:38]** Tuesdays because we have a lot of email traffic on Tuesdays and when the batch job overlaps with the peak traffic,

**[25:44]** we're going to have issues. They they may be able to get to that point and tell you later, but initially they just

**[25:50]** feel it. They say, "Oh, that's bad." and then they go look and then they're right and then everyone calls it experience.

**[25:56]** This is worth digging into because it's the root cause of a product failure happening at an absolutely massive scale

**[26:02]** across the industry. The entire agent ecosystem is built on a model where the human provides instructions and the

**[26:07]** machine executes them. That model works when the instructions are really clear like summarize the document, right?

**[26:13]** Super easy. Reformat the spreadsheet. But it breaks when the instructions require expertise that the human

**[26:18]** genuinely has but struggles to articulate. And almost all of the most

**[26:24]** valuable knowledge work that agents can tackle lies in that second category. In other words, 2026, the year of these

**[26:30]** long-running agents that do impactful knowledge work, only really delivers on

**[26:36]** that promise if we can get into the very hard problem of explaining to these

**[26:41]** agents this tacit knowledge, work, and judgment that makes us good at what we do. We have to think through what does

**[26:50]** it mean to have deep insights about churn and actually articulate enough of

**[26:56]** our personal experience to give the agent something to work against. Not because the agent has to mimic us like a

**[27:01]** parrot, but because the agent needs to orient enough in our local context that

**[27:06]** it can then go beyond that and continue to optimize and deliver insights. Because the best agents do that, right? the best agents know enough about your

**[27:12]** context and what you're trying to do that they can then go beyond that and deliver really interesting novel insights you wouldn't have expected.

**[27:18]** That's fantastic. That's the dream. It does really happen. But you got to give them enough out of your tacid experience

**[27:25]** to actually make that possible. Think about what a good sold out markdown file contains. It's not just a personality

**[27:31]** description. It's it's a decision framework. when to escalate versus how you handle things autonomously, what

**[27:36]** what tone to use with different audiences, which data sources are are you going to trust versus which ones are you skeptical of, what is good enough at

**[27:44]** various task types. That's the same thing a strong vice president would put

**[27:49]** in an operating memo for the team when he or she joins the team for the first time. And most VPs, honestly, they

**[27:55]** haven't written that down either. I' I've been under a number who have moved in new, and most of them don't send an operating memo like that, even though

**[28:00]** they should. This is also the same reason why senior engineers notoriously are pretty bad at writing onboarding

**[28:06]** docs. It's not laziness. It's that the knowledge that would make the doc useful has been sort of compressed into a form

**[28:12]** of automatic behavior for them and the doc is going to list steps but miss so much nuance that they have in their

**[28:18]** heads because it just makes sense for them. It's like the person who's describing the way to uh a friend's

**[28:23]** house down the road and they're giving you all of these landmarks that are local to them that make sense. It's like there's the big tree and then you stop

**[28:29]** by the the the store that has the broken down sign and then you go over it. This is no like as a stranger in these parts,

**[28:36]** you don't understand it, but they understand all of the nuances that help them get to their friend's house. And the structural trap is this. The people

**[28:43]** with the most to gain from agent delegation are exactly the people whose work is hardest to delegate. The most

**[28:49]** senior, most overloaded knowledge workers carry the highest ratio of tacet to explicit knowledge. Their work is the

**[28:56]** most compressed. It's the most invisible to themselves. They need the leverage most and the cold start problem hits

**[29:01]** them the hardest. Ironically, beginners just getting started in their careers. Folks who are you're one year, two years

**[29:07]** out of college and all of this is stuff that you are still doing intentionally, explicitly in your head, you haven't

**[29:12]** compressed it yet. You may have a much easier time with agents and delegating

**[29:18]** to OpenClaw than the seniors. And the reason I say that is because you have not gone through that automation process

**[29:23]** in your head yet. And that's actually fantastic and it's one of the reasons why firms like Shopify intentionally

**[29:29]** hire juniors because there are things that you can go much faster at than seniors. And ironically, this inability

**[29:35]** to sort of get our operational knowledge, our tacet knowledge out of our heads is at the root of at least

**[29:41]** three big chronic people problems that plague most organizations. Delegation

**[29:47]** fails. That's that's one of them, right? Managers will cite that as a key challenge. And the standard explanation is that they're control freaks. But the

**[29:53]** real explanation is that they don't know how to delegate because they don't know how to express what they've got in their heads. It's it's a real challenge for

**[29:59]** new managers. Another related one, people not getting promoted. The most common reason strong IC's plateau is

**[30:05]** that they cannot be replaced. Their knowledge work is locked in their head. And so even if they are qualified for

**[30:11]** the next level, no one wants to risk losing their expertise on their current job and that becomes a trap for them.

**[30:16]** And then of course the third one is obvious. People leave. Institutional knowledge evaporates. it walks out the door in someone's head and and it's just

**[30:22]** gone. So, I would argue agents did not create these problems, but agents create

**[30:29]** the first universal selfish incentive for every single one of us in knowledge

**[30:34]** work to actually fix these problems. Not because HR launched a knowledge management initiative, right? It's not

**[30:40]** because a consultant ran a workshop. It's because you personally want a robot to stop asking you to confirm calendar

**[30:46]** entries that you already freaking approved. and the robot needs you to describe your calendar rules first. That's new. Look, we've had decades of

**[30:53]** top- down pressure to externalize our knowledge. It never worked at scale because there was no direct personal

**[30:58]** upside for any of us. The benefit occurred entirely to the organization when you wrote the wiki, right? A and

**[31:03]** traditionally, the person who documents their expertise is the person who loses. In this case, agents flip that incentive

**[31:09]** structure on its head. The person who documents their expertise is the person who gets the leverage in the world of agents. The organization might benefit

**[31:16]** secondarily. It's actually a bottoms up knowledge management revolution disguised as a consumer AI product. And

**[31:23]** I don't think that anyone, including the people building these products, really appreciates that because if they did

**[31:28]** appreciate it, I feel like they would put more into onboarding. I have been through the onboarding flows for like

**[31:35]** half a dozen of these and they all feel really, really light. Really light for

**[31:40]** what you're expecting this agent to do, for what you're hoping it will do for you. If you want it to really lift up,

**[31:45]** leverage two, three, or more X your work. And that and that leads us to a very uncomfortable correlary that's

**[31:52]** worth naming explicitly. If the value of agents depends on your ability to

**[31:57]** articulate your work, agents are about to create an extremely visible divide in the workforce. Right now, tacet

**[32:03]** knowledge is invisible, right? Nobody knows that you can't describe your own process because nobody's ever asked you.

**[32:09]** Performance reviews tend to measure your outputs, not your self-nowledge. You might be a phenomenal operator with zero

**[32:15]** ability to explain how you operate and the system just never penalizes you and agents are about to change that. In a

**[32:21]** world where everyone has access to the same tooling, the differentiator is not which model you use or how many Mac

**[32:27]** minis you can put your open claws on. It's whether you can feed the thing well enough to actually get leverage. The

**[32:34]** people who invest that time, who can decompose their expertise into explicit

**[32:39]** delegatable components will get compounding returns. That's where the value is. Their agents improve because

**[32:46]** their specs improve. The second agent deploys faster than the first. The 10th deploys in a few minutes and they

**[32:51]** actually build on all of that knowledge. So, it doesn't even take them a ton of time to provision it because they understand the memory system so well.

**[32:58]** The people who skip all of that will install, play for a weekend, hit the wall, and conclude agents are all hype.

**[33:05]** And they will be wrong. The agent worked fine. The problem was never the agent. So, I want to propose a solution. I've

**[33:10]** gone through the problem. You understand the problem. The solution I have is this. The first agent you run should not

**[33:17]** be your open claw assistant. The first agent you run should be a tool to

**[33:22]** prepare you to run agents the way you want. And no one seems to be thinking this way, so I'm just going to say it

**[33:27]** out loud. The first agent worth deploying, it's not your personal assistant. It's not your chief of staff. It's not your scheduler. It's not your

**[33:33]** email uh guy. It's not your briefing bot. It's just an interviewer. It is one

**[33:39]** designed to do what expertise elicitation researchers do. Yes, that's a real job. Ask you the right questions

**[33:46]** in the right order with the right follow-ups to extract the operational knowledge you carry but cannot access on

**[33:51]** your own. And no, this is not the same as asking you three questions on install. I know that OpenClaw asks you

**[33:58]** who am I, who are you, and what is my job? I get that. This is a lot deeper than that. And of course, I've been

**[34:04]** building this. I've been digging in because I want to build a demo that actually allows you to immediately use this so that if you have trouble

**[34:10]** actually using your agent and making it valuable, you have a tool now to get your agent going. It's a structured

**[34:17]** elicitation workflow. I know it's a $10 word, but it basically means getting that information out of your head. Uh,

**[34:23]** it's a structured elicitation workflow that walks you through five specific layers. Your operating rhythms, what are

**[34:29]** your days, your weeks, and your months actually like in detail, not the calendar version, the real one. Your

**[34:35]** actual recurring decisions, what judgment calls you make, what are the easy calls, the hard calls, what inputs

**[34:41]** that you actually need, your dependency, who do you need things from, and when. Nobody's asking that, right? They've

**[34:47]** been through these flows. Your friction, the recurring annoyances that eat your time. Most of them don't ask that either. It takes time. I'm not going to

**[34:54]** pretend this doesn't take time, right? Like I've gone through it at best. It takes 45 minutes. It might take you longer. And and I think that time is

**[35:02]** worth it if you're going to actually save time on your agent, right? The output is structured data and you can

**[35:07]** plug it right into your open brain if you've built that. That's just a simple personal knowledge store uh that's quick to set up and runs for like 10 cents a

**[35:14]** month. Uh and then it becomes durable, right? it becomes searchable knowledge and it's available to any agent that

**[35:21]** interacts with an MCP which all of these openclaw agents do by the way and from that output I built a configuration file

**[35:28]** generator that will automatically produce soul.markdown heartbeat.mmarkdown user.mmarkdown files

**[35:34]** that you can use to provision an openclaw and that solves the gap that solves the gap that manis isn't building for perplexity isn't building for nemo

**[35:41]** claw isn't building for dispatch skips over this and to be honest with you the configuration files that I can output.

**[35:48]** And to be honest with you, the configuration files you get at the end of this process are in some ways the least interesting output. The more

**[35:55]** valuable output is the conversation itself and the way it creates a structured database, a structured map of

**[36:02]** how you work, what you know, where your leverage points are. And that makes you

**[36:07]** so much better at delegating to agents. Yes. But also talking about it means

**[36:13]** you're better at delegating to people. It makes you easier to promote. It makes your expertise survivable. All of this

**[36:20]** stuff that was locked in your head, you had an AI agent help you get it out. And that's what I focused on building. The AI agent that helps you get it out. And

**[36:28]** yes, it does help you make your agents work, which is kind of the whole reason you'd have agents. I know that every

**[36:34]** agent product in the market today is competing on the implementation layer. How easy is it to set up from scratch

**[36:41]** with your open claw? Fine. The question I have is once you have it set up, can

**[36:46]** you actually use it to do interesting stuff? Can you actually use it in ways that help your workflow? And the only

**[36:52]** way it will ever do that is if it gets into your brain and gets the stuff out that you don't think about every day.

**[36:57]** And that's why I built an open brain interview agent to help you get that knowledge out so that you can provision

**[37:03]** whatever open claw you choose in whatever way you choose confident that it actually knows the details, the

**[37:11]** nuance, the depth of your work in a way that will make it effective because that depth is where you get the

**[37:17]** disproportionate returns. That's how the people who are getting these three, four, 5x returns are doing it. So don't

**[37:23]** make your first agent the agent that is your personal assistant. Instead, make your first agent the one that prepares

**[37:30]** you to have a personal assistant agent. The extra work is worth it. I promise.

**[37:36]** Cheers.

**[0:00]** Agents by themselves don't make you productive. I'm just going to say it straight out. So many people right now

**[0:06]** are running to OpenClaw with 250,000 GitHub stars or they're they're VCs and their builders and all they can do is

**[0:12]** they can build copycats of OpenClaw. And everyone assumes that as soon as you get

**[0:17]** the agent, you'll know what to do with it. And there's a massive gap between I can install an agent, which everyone has

**[0:23]** now solved for. You can install an agent in 10 seconds. By the time I have finished saying this sentence, you can have an agent up and going. that's how

**[0:29]** fast these things are going now. That's not the point. Whether you can use it productively is actually the question

**[0:35]** that matters. And yes, all of those people who are out there who are making lots of clickbait who are saying, "I

**[0:40]** used my agent to do lots and lots of stuff. I have 10 agents that do this and that. I have two agents that do this and that. I manage my whole $5 billion

**[0:47]** company with agents." Those are all true stories, but they're only true stories

**[0:53]** because someone figured out how to clarify enough of what they were looking to do to give it to an agent. And that

**[0:59]** turns out to be a very, very hard problem. And it's funnily enough, not a

**[1:04]** problem that most companies out there are interested in solving. And I know because I went through and I looked at

**[1:10]** all the products. And so in this video, we are going to go through and talk about the real gap that's upstream of

**[1:16]** all of these open claw agent metos. We're going to go through and survey the different approaches to building your

**[1:22]** agents, the different ways these products are handling open claw like implementations. And then we're going to

**[1:28]** talk about how you actually solve this problem. And yes, I built something to solve it. I want you to have an easier

**[1:34]** time using your agent. Right? Let's assume you have an agent because now it's very easy to get one. how do you

**[1:39]** use it? And so I built something to make that jump into using the agent much much easier. And we'll get to that. The most

**[1:46]** common message I've been able to find in most open claw community forums is this. Now what? It's really simple. Like I I

**[1:54]** did it. Now what's next? How do I go from here? Variants of that, right? Like I have installed the open claw. Now what

**[1:59]** do I do next? It's not really how do I fix this error. It's not which model do I use? Although there's a few of those.

**[2:05]** It's just I got it to run, which is great, and I don't know what to tell it, right? Give me a recipe. Give me

**[2:12]** something to do. And I think there's a structural reason this keeps happening. And I don't think the correct fix is

**[2:17]** just to hand out recipe cards for openclaw use cases because that's not really what you want an agent to do. The

**[2:22]** whole reason we have an agent is because it does many things well. It doesn't just do one thing. Well, if you start telling your agent, hey, here's my, you

**[2:30]** know, expensive Mac Mini. Here's my expensive cloud subscription. Now you triage my email. Is that really a good

**[2:35]** use for your dollars? Yet a lot of people, the most common use of OpenClaw is triaging your email. We need to

**[2:41]** understand why agent implementations are not delivering the 10x ROI that have

**[2:47]** been promised for so many people. And we need to be honest about it or there's going to be a lot of people who are a little bit frustrated. There are going

**[2:53]** to be people who are lining up to undo OpenClaw if we're not careful. And I say that because there actually have been

**[2:59]** cases of lines in China where people who had previously installed OpenClaw are

**[3:04]** going back and standing in line to uninstall it because they didn't want it. I don't want that to happen. So here's what I'm going to dig into. I'm

**[3:09]** going to dig into the common patterns across agent implementations that really work. I'm going to dig into the meto

**[3:14]** landscape and why every open clawike product is kind of aiming at the same target and kind of hitting the same wall

**[3:20]** when it comes to success. And I'm going to dig into the structural reasons why it's really really difficult for us to

**[3:26]** actually explain what we need to do with these agents in a way that they can understand. I'm going to explain a

**[3:33]** little bit about why I think this is the larger problem. It goes beyond agents and then we're going to get into what to do about it. How do we solve it? So

**[3:39]** let's jump in. All right. We're gonna start with a story of Brad Mills. This is a real story. Brad spent 40 hours building a

**[3:46]** delegation framework for his OpenClaw agent. Not 40 hours installing. I want to be very clear. The install took 10

**[3:52]** minutes. He spent 40 hours writing standards, accountability rules, a definition of done for every single

**[3:57]** project. He transcribed 200 hours of videos into a searchable knowledge base. 40 hours of trying to describe what he

**[4:04]** wanted, right? I'm not making that up. That's like a week of work and it still did not work. And he wrote about it

**[4:09]** publicly, right? Constant failure. He wrote fail after fail after fail. Two steps forward, one step back. and he

**[4:16]** ended up micromanaging the agent harder than he'd ever had to micromanage a human. And the autonomy that so many

**[4:22]** other stories share felt in practice like the second job of supervising something that confidently reports tasks

**[4:28]** complete when it's not really done. Brad is not an outlier here. I would say Brad is closer to the median experience than

**[4:36]** a lot of the folks who are promising 10x results. One prominent OpenClaw guide creator reports getting flooded with DMs

**[4:43]** all the time right after setup. The stuck point is not installation anymore. We figured that out. It's actually

**[4:48]** figuring out what to do with the agent and how to make it understand your specific context. Right? Another user

**[4:54]** asked his agent to write five cold email variants. The agent sent done and wrote nothing. And his solution was to build a

**[5:00]** second adversarial auditor agent whose only job was to verify the first agent completed the task. He needed a

**[5:06]** management layer because the worker couldn't be trusted to self-report. And this became like a nesting turtles

**[5:11]** problem. like you just have issues managing the agents because you don't understand how agent architecture works

**[5:17]** if you've just spent 10 minutes on an open claw installation and you've just heard about it on the internet a day ago. Another user tried rolling out

**[5:24]** agents to a team and he gave everyone access and just called it done. It technically worked, he pointed out, but

**[5:29]** it was completely useless because nobody had mapped their workflows, their decisions, their data needs in advance

**[5:35]** and no one knew what to give the agent as a task that would be successful. Without all that upstream work, the agent stayed so generic it was useless.

**[5:43]** And a generic agent with right access to your email is actually worse than no agent at all. It's a liability with a

**[5:48]** chat interface. Right? There are whole business models emerging on places like X to fix this. Right? That is how bad an

**[5:55]** issue it is. There's a guy on X I saw selling a $49 pack of pre-written config files. A soul.markdown file, a

**[6:02]** heartbeat.mmarkdown file, a user.mmarkdown file. is core files for OpenClaw. The whole stack specifically

**[6:07]** marketed to quote skip 40 hours of OpenClaw setup. You can build a small

**[6:12]** business around the gap between installed and useful. And that tells you something about where the agent market

**[6:18]** is. But before we talk too much more about what's broken, let's talk about what does work. Because there's a

**[6:23]** pattern across hundreds of thousands of Open Claw installations. The deployments that stick, the ones where people are

**[6:28]** still getting daily value weeks and months later, they share a particular architecture and it has almost nothing

**[6:34]** to do with which model you end up picking. The successful setups all have a set of markdown files that function as

**[6:41]** the agent's operating system. If you open theopenclaw directory on anyone running a working agent, you'll find the

**[6:47]** same structure. There's a soul. Markdown file that defines the agent's role, its job, its tone, its boundaries, basically

**[6:53]** a job description. There's an identity.mmarkdown which has its name. It has its personality constraints.

**[7:00]** There's a user.mmarkdown with a detailed profile of the human including preferences, schedule patterns,

**[7:05]** communication style. And there's a heartbeat markdown with a checklist that the agent reviews every half hour to

**[7:11]** decide if there's work to do. And then there's a very simple cron job that maps that human's actual operating rhythm.

**[7:18]** None of this is particularly technically difficult. And I want to underline this three times. None of what I just

**[7:23]** described is artificial intelligence. It's just plain text. But the quality of

**[7:28]** those files determines whether your artificial intelligence agent is actually any good at anything at all. So

**[7:34]** the people who run multiple specialized agents, the not the one do everything bot, right? But a team with clear roles

**[7:41]** and scoped access, you know how you've seen the clickbait, right? Well, I have a marketing manager for this and then I have my scheduler for this and I have my

**[7:48]** CEO for this and I have my chief of staff for this. Okay, fine. The only way that works is if each agent has truly

**[7:55]** its own identity, its own markdown files, its own tool sets, its own workspace so it can get jobs done and it

**[8:01]** doesn't share context with other agents. They have clear jurisdictions. We would say they have clear separation of

**[8:06]** concerns in engineering speak. And that same clarity shows up everywhere you see

**[8:12]** a multi- aent system working. So, people running specialist bots in Slack that delegate to each other like co-workers,

**[8:18]** which you've also seen demos of, I'm sure, where someone asks a question and the orchestrator agent decides that the

**[8:24]** specialist should handle it. There's a whole flow, right? These are not toy demos. They're running daily. Those are

**[8:30]** real orchestration patterns. They really work and they and they only work because there's a clear separation of concerns

**[8:36]** and a clear identity that's separate for each of the agents involved. Now you can absolutely in more sophisticated

**[8:43]** implementations use your open claw as a general planner and have it spin up

**[8:49]** executor agents on the fly to help you get tasks done. That is one of the ways a general purpose agent solves problems.

**[8:56]** But it only does that successfully to the extent it has the tools, the identity, all of the context to know how

**[9:04]** you want the problem solved and to do so successfully. And so it still comes back to context in the end even if you're

**[9:09]** doing a more sophisticated implementation. There's another pattern worth naming. The people who have open

**[9:15]** claw configured correctly have invested a lot in the memory side of things. They

**[9:20]** either have a memory.mmarkdown file that accumulates insights over time which is closer to the original vanilla openclaw

**[9:26]** approach or they've got closer to something like the open brain approach that a lot of folks in my community are

**[9:32]** building where they have a database that the open claw can search from and get back insights on and that ends up being

**[9:38]** sort of a richer more multi-dimensional repository over time. You can have a hybrid, you can kind of work with both.

**[9:44]** The point is you have intent around memory. you know that your agent needs

**[9:49]** to learn and get better over time. And if it doesn't learn and get better over time, it's not a very smart agent and it's not going to help you for very

**[9:55]** long. And the common thread through the context piece, the separation of concerns, the ability to set up memory

**[10:00]** correctly, the ability to write all those markdown files right, the ability to maybe configure a database so your agent can query for memory. All of that

**[10:07]** means having clarity of intent around what you want the agent to do and the

**[10:12]** ability to articulate at a pretty high degree of detail what you expect the agent to do in a series of steps. Right?

**[10:19]** The human has to sit down and describe in triggerable verifiable language what you do all day to get an agent to do it.

**[10:26]** Right? Not I handle marketing, but these are the different websites I check. These are the metrics I look at. This is

**[10:32]** the spend that I'm willing to budget for. This is how I know that spend is correct. These are the equations I run.

**[10:39]** And then finally, these are the optimization and leverage opportunities I see. Now, people will say, "It's the

**[10:44]** agent's job to get better at marketing. Why are we giving it that detail?" And I will answer, you got to orient the agent

**[10:50]** toward the current context if you want to ask the agent to improve over time. You cannot just magically say, "Here's

**[10:57]** marketing. You do it agent." and it's just going to magically know all of the nuances of your context for your product

**[11:03]** and just randomly do it. That's just not how it works. And yet

**[11:08]** that underlying assumption is lying behind so many of the meto products that

**[11:14]** we see in the landscape. If we look across the landscape, and I'm going to profile them here, and we look at how

**[11:19]** agents are being built and sold right now, so many of them are being built and sold as essentially magic boxes with

**[11:25]** arms and legs. Like, here's the magic box. Type anything you want and the magic box will fix it. And it turns out

**[11:31]** if you're selling magic boxes, they'll sell like hotcakes. But the problem is once you have a magic box and it's not

**[11:37]** magical anymore, it's a disappointing experience. Let's go through each of them in turn. Obviously, Open Claw is

**[11:43]** the original. It's 250,000 or whatever number of thousand GitHub stars it is now. It runs locally on your hardware.

**[11:48]** It connects to any LLM. You talk through it through any channel, right? Telegram, WhatsApp, iMessage, Slack. Now you can

**[11:54]** phone call it like whatever you want. It's free. It's infinitely configurable and the cold start problem is entirely

**[12:00]** up to you which is appropriate because the original audience was developers. Peter Steinberger built this for

**[12:05]** developers and developers quite reasonably could be expected to write markdown files and configure their own

**[12:11]** tool set and for so many of them that was not an obstacle and so so much of this conversation is basically OpenClaw

**[12:17]** is out in the wild now. Openclaw is on the loose. Open Claw is the most copied product of 2026. What does it mean when

**[12:23]** everybody wants an agent and they're not just developers and they're like, "What is a markdown file and why should I care?" Developers, to be fair, have a

**[12:30]** little bit of an advantage at writing specifics. If you've ever sat in the product chair like I have, and you've had conversations with engineers, you

**[12:37]** know the engineers tend to be the ones and should be the ones asking you for specifics. Okay, fine. You say you want

**[12:44]** the image to appear in that way on the web page. Tell me why. Tell me what is

**[12:49]** the file size. Tell me how quickly you expect it to load. Tell me how it goes with and overlays the rest of the web

**[12:55]** experience. And that's just a very simple presentation, right? Love to get specific. And I think that mental habit

**[13:01]** has helped open claw take off for so many in the engineering community because it's actually very clear to them

**[13:07]** that you need to describe a lot of what you do in high specifics to the agent to make it useful. That's not that unusual.

**[13:12]** For the rest of us, it's a new step. Now, a bunch of folks have come into the space since OpenClaw, and the thesis for

**[13:18]** most of them has been correctly. OpenClaw was hard to install originally. Peter designed it that way on purpose.

**[13:24]** He did not want non-developers using it because you can easily configure your OpenClaw to be a security risk. And that

**[13:30]** was the dominant headline for the first month or so of OpenClaw's popularity. And so, so many players are in the space

**[13:35]** now basically saying, "We took care of security. We took care of ease of install. You don't have to worry about it." And I'm here saying that's not the

**[13:42]** real problem. That's just the first problem, right? Manis, now owned by Meta, is doing exactly that. You can either have a desktop app which has

**[13:49]** local access or you have a cloud virtual app. But either way, it's more secure. It's got a little bit of structure. You

**[13:55]** type in your query. It automatically decomposes all of that work into its own sub agents. And the idea is it's easier

**[14:01]** to use. It's more secure. It can be locally if you feel comfortable with that or in the cloud. And it's something that you can get up and running on in 10

**[14:08]** or 15 minutes. The problem is the manness agent is really going to be limited by the lack of initial context

**[14:15]** you give it. So it's optimizing for the cold start problem in the sense that it makes it easy to type the first word,

**[14:20]** but without the ability to really deeply configure what the agent knows about you

**[14:25]** and why it cares about you and the workflows you're doing and what you're trying to accomplish and what you're trying to delegate, it's going to be

**[14:31]** somewhat limited in its ability to work with you. Now, I do know Manis users who have deliberately put intent into that

**[14:38]** platform and swear by it. They're like, "This is incredible. The more intent I put in, the better it gets." And that is kind of a universal law of AI. If you

**[14:45]** put more passion, heart, intent, clarity, and communication into the tool because these tools have memory systems,

**[14:51]** they start to learn over time and they're more useful for you. But that is not the experience of the majority of

**[14:58]** Manis users. And that brings me to the next tool, which is Perplexity's personal computer. Perplexity personal

**[15:03]** computer is in a sense the most audacious of these open claw plays. We know that we cannot get a hold of Mac

**[15:09]** minis because Apple has sold out of them because so many people want to put open claws on them. Perplexity saw that said

**[15:15]** we're a corporate account. We can get lots of Mac minis and they literally offer you a dedicated Mac Mini. It's a

**[15:22]** real Mac Mini connected to Perplexity's cloud, merging local file access with their computer orchestrator and they

**[15:29]** give you a project manager AI that routes tasks across 20 Frontier models for that Mac Mini. So, it takes away all

**[15:36]** of the pain of having a local Mac Mini. You actually have a real Mac Mini that's yours. It has an orchestrator. It has 20

**[15:42]** models. It's a very bold vision. CEO Aravven Sinas framed it at the developer conference like this. He said a

**[15:47]** traditional operating system takes instructions and an AI operating system takes objectives. I think he is right

**[15:54]** that openclaw is popular because it is fundamentally an operating system. That is a correct insight. I think he's also

**[16:00]** correct in saying that it is about optimizing for objectives. But the piece

**[16:05]** that is challenging for most people is when you have that firepower delivered for you, all of that agentic power at

**[16:12]** your fingertips, what do you do with it? Then how do you communicate your intent in a way that actually gets across? The

**[16:18]** fundamental bet is the same as all these other ones. You state the objective for openclaw and openclaw will figure out

**[16:24]** the rest. In this case, you state the objective for perplexity personal computer and you bet the personal computer will figure out the rest. And

**[16:30]** that works well right until the objective requires knowledge about your life, your judgment patterns, your

**[16:36]** operating rhythm that no system actually has because you never wrote it down. And you may not be aware you have it, but

**[16:43]** it's in your bar for powerpoints. It's in your bar for financial products. It's in your bar for everything, and you just

**[16:48]** never realize it was written down. Let's have a look at Neimoclaw next. Nemoclaw is Nvidia's enterprise security wrapper

**[16:53]** for OpenClaw. It was launched at GTC by Jensen Hang itself. It runs agents in sandbox environments using Open Shell

**[17:00]** for privacy guardrails and Neotron for advanced model output. Basically, it's a it's a buttoned up corporatefriendly

**[17:06]** open claw with lots of security guard rails and it solves the security problem really thoroughly. The real and serious

**[17:13]** risk of an agent with full access to your machine deleting stuff like they've taken care of that. It does not solve

**[17:19]** the problem of what to put in the agents operating instructions and it effectively punts that to the enterprise. And the problem is most

**[17:25]** enterprises also don't know how to solve that problem. I know because I talk with them. They do not know out of the gate

**[17:31]** how to solve the problem of what to do with a Nemo Claw. If you roll it out to 10,000 people and only five of them have

**[17:38]** used OpenClaw in a way that's productive, those five are going to be perfectly happy and be able to use that. The other 9,995,

**[17:46]** they're not going to know what to do. They're not going to know what to do because no one trained them. And that is absolutely a larger issue with AI, but

**[17:52]** it's especially bad with agents. And the reason it's especially bad with agents and with the open claw phenomenon is

**[17:58]** that the open claw phenomenon gives you so much power. It is really a story of

**[18:03]** transformation. It does really give you that 10x potential on your work and they just do not tell you how much work you

**[18:10]** have to put in at the top to get that result and how much training you have to do if you are rolling this out to a

**[18:15]** workforce. It is not a plug it in and go solution and it never is going to be because it takes context from you.

**[18:21]** Right? I just want to be honest with you. All the people who are promising and all of these ones that I'm covering are promising this. All of them who are

**[18:28]** promising 10 minutes to open claw are right technically and wrong functionally. They're correct.

**[18:33]** Technically, you can get very very quickly up and running with your open claw. They are wrong in that you cannot

**[18:40]** get utility out of the open claw unless you put a lot more work than that into getting it ready. Claude dispatch is

**[18:46]** part of anthropic's answer and Anthropic has been investing heavily in essentially pivoting their claw product.

**[18:51]** So it is open claw like over the last month there's probably been 15 ships around this. Dispatch is the most

**[18:57]** obvious because it makes it so easy to pair your phone with your Mac and it makes it easy to send messages through

**[19:02]** whatever version of your messaging app that you want and you can now control your claude from your phone which is one

**[19:07]** of the key benefits people called out from OpenClaw in the first place because you can use your openclaw wherever you

**[19:13]** are. You can be dropping the kids off to school. You could be out looking at the beach. You can be working in the kitchen

**[19:19]** and you can be messaging your computer and getting work done. People like the mobile friendliness. It's one of the

**[19:24]** oldest bets in software. We've had this bet since 2007. Really earlier than that when we had the mobile phone revolution

**[19:29]** in 2007 with the iPhone. People like to be on the go with computing. And this is just taking your agents on the go. It's

**[19:36]** one of the oldest and most reliable bets in software. It turns out it works for agents, too. But you can't send, and

**[19:42]** I've tried this, by the way, with popular agents, you can't send a threeline or four-line text message to

**[19:49]** an agent and expect it to work well if the agent doesn't know you. And it turns out that a lot of these text message

**[19:55]** first apps do not work well if you are just introducing yourself by text.

**[20:02]** Because guess what? I have done a 15 paragraph introduction by text message

**[20:07]** to a popular open claw like application and it has completely failed because it

**[20:13]** still wasn't enough. 15 paragraphs of text that's a whole wall of text and it's still not enough to get the agent

**[20:20]** to actually get it. And so as much as it's really cool that Claude is pivoting to make it easier to message, there are

**[20:25]** a lot of developers that find it super useful, it does not by itself solve this problem. The issue here is that we need

**[20:32]** to be able to say or speak what we really mean in a way that's clear enough that an agent can run with it and we can

**[20:38]** truly delegate that task. And that is the problem none of these solutions are really solving. And that goes not just

**[20:43]** for these purpose-built solutions I profiled like perplexity personal computer or like Nemo Claw, but it also

**[20:50]** goes for the hosted rappers start claw, myclaw, simpleclaw, uniclaw, you name it, claw and and there's like dozens a

**[20:56]** week launching. They're all trying to make open clause setup easier, right? One-click deploy, preconfigured

**[21:02]** personas, managed infrastructure. They're solving all of that installation friction very successfully, which is a

**[21:08]** real UX problem. But the guy selling the $49 pack of pre-written sold out markdown files or the guy repackaging

**[21:14]** and calling it start.claw and having the exact same markdown files as a quote persona, they're not really solving that

**[21:21]** issue, right? They're giving you their generic version of what it is, not the thing that's going to be useful for you.

**[21:27]** Because the thing that makes agents useful is that they are particular, is that they are personal and you can't

**[21:32]** take that away. The people who are having transformative impact have realized they need to put the work in to make their agent personal. There is no

**[21:39]** substitute. So every product in this landscape is fighting over installation, over UI, over model selection, over

**[21:46]** security, over pricing, over cloud versus local. And they're competing on this implementation layer. And they're trying to get us to care. Do I care

**[21:52]** about the fact that I want a Mac Mini in the cloud from Perplexity? Is that better? I don't even know how to assess that in most cases, right? Most people

**[21:58]** don't. And every product in this landscape breaks against that same wall, right? The human on the other end has to

**[22:05]** understand what they need to do and produce a usable spec for the agent to do that task. And that is actually much

**[22:12]** more important to the long-term value of the agent than just a particular kind of installation, which is just a one-time

**[22:18]** problem. And so that wall, there's a reason why products are not going after that. It's a structural property of how

**[22:24]** expertise works. And it's actually a really hard problem. It's not easy. You can't solve it with UX. And here's where

**[22:30]** it would be easy for me to hop off and say, "Well, it's really hard. We're done." But I want to go deeper. What it

**[22:35]** makes it difficult for people to describe what they do. Because that observation, while true, doesn't explain

**[22:41]** why this is happening and why we find it hard. And there's a larger story there. If you don't understand the mechanism,

**[22:46]** you're going to waste time on solutions that don't address the root cause. Knowledge work has a structural property

**[22:52]** that makes it uniquely resistant to delegation, whether that's delegation to humans or delegation to machines. And

**[22:58]** that property is this. The more senior and valuable you become, the more your work migrates from explicit processes to

**[23:05]** tacit judgment, and the less visible your own operating system becomes to you, the person using it. And this is

**[23:12]** not a failure of good intentions. This is not a failure of self-awareness. It's the intended outcome of how expertise

**[23:20]** actually develops. When you're a beginner, everything is very conscious. It's very deliberate. When I started to

**[23:26]** play basketball, when I was in middle school, I was focusing on dribbling so hard and eventually you start to get

**[23:31]** good at dribbling the ball. You don't think about it as much. So, you follow the checklist and knowledge work to begin as an intern. You think through

**[23:37]** every step. As you gain expertise, all of those steps compress into automatic patterns. Just as when you drive a car

**[23:43]** today, you don't think about turning right after 20 years of driving a car. It just happens. You stop thinking about

**[23:51]** your knowledge work. You stop thinking about what to check. You just check it. You stop reasoning through decisions and

**[23:56]** you just make them. But the reasoning still happens. The thing that makes you fast and effective is the same thing

**[24:01]** that makes your knowledge very inaccessible. It's been compiled from source code into machine code.

**[24:06]** metaphorically speaking and you no longer have the source code. Let's take an example of a really senior product

**[24:12]** manager. They don't think I should cross reference the revenue dashboard with the churn data before forming an opinion.

**[24:18]** Instead, they'll open three tabs. They'll glance at the numbers and they just know. And if you ask what was

**[24:23]** checked and can you reconstruct and explain what happened, they'll narrate backwards from the conclusion, but

**[24:28]** they're not they're not really going to describe the actual process in most cases because it's so low level. The

**[24:34]** real decision often involved a hundred micro evaluations that re reflect thousands of hours of patterns that that

**[24:41]** product manager has seen over multiple startups. But but that doesn't get articulated, right? The magical pattern

**[24:47]** matching that allowed the deep insight that they had about churn is something that is a function of all of those

**[24:52]** thousands of hours. It's not something you can substitute for with just an explicit intern checklist. It it doesn't

**[24:58]** work that way. Now, you might stop here and say, "Well, then there's no point in agents." And I will come back and I'll say, "No, the stories of agents making

**[25:05]** you insanely productive are all true." And our goal is to make more of those

**[25:10]** stories. And I am telling you what it takes. And the first thing we have to acknowledge is that knowledge work is

**[25:15]** really hard. A strong salesperson doesn't consciously decide to mirror their prospect's phrasing and slow their

**[25:21]** cadence where they when they detect defense. a strong salesperson, they don't consciously decide to mirror the

**[25:27]** prospect's phrasing and slow down their cadence when they detect that that they're just a little defensive. They

**[25:32]** just do that. A senior engineer doesn't think, well, this code has a concurrency issue that'll service under load on

**[25:38]** Tuesdays because we have a lot of email traffic on Tuesdays and when the batch job overlaps with the peak traffic,

**[25:44]** we're going to have issues. They they may be able to get to that point and tell you later, but initially they just

**[25:50]** feel it. They say, "Oh, that's bad." and then they go look and then they're right and then everyone calls it experience.

**[25:56]** This is worth digging into because it's the root cause of a product failure happening at an absolutely massive scale

**[26:02]** across the industry. The entire agent ecosystem is built on a model where the human provides instructions and the

**[26:07]** machine executes them. That model works when the instructions are really clear like summarize the document, right?

**[26:13]** Super easy. Reformat the spreadsheet. But it breaks when the instructions require expertise that the human

**[26:18]** genuinely has but struggles to articulate. And almost all of the most

**[26:24]** valuable knowledge work that agents can tackle lies in that second category. In other words, 2026, the year of these

**[26:30]** long-running agents that do impactful knowledge work, only really delivers on

**[26:36]** that promise if we can get into the very hard problem of explaining to these

**[26:41]** agents this tacit knowledge, work, and judgment that makes us good at what we do. We have to think through what does

**[26:50]** it mean to have deep insights about churn and actually articulate enough of

**[26:56]** our personal experience to give the agent something to work against. Not because the agent has to mimic us like a

**[27:01]** parrot, but because the agent needs to orient enough in our local context that

**[27:06]** it can then go beyond that and continue to optimize and deliver insights. Because the best agents do that, right? the best agents know enough about your

**[27:12]** context and what you're trying to do that they can then go beyond that and deliver really interesting novel insights you wouldn't have expected.

**[27:18]** That's fantastic. That's the dream. It does really happen. But you got to give them enough out of your tacid experience

**[27:25]** to actually make that possible. Think about what a good sold out markdown file contains. It's not just a personality

**[27:31]** description. It's it's a decision framework. when to escalate versus how you handle things autonomously, what

**[27:36]** what tone to use with different audiences, which data sources are are you going to trust versus which ones are you skeptical of, what is good enough at

**[27:44]** various task types. That's the same thing a strong vice president would put

**[27:49]** in an operating memo for the team when he or she joins the team for the first time. And most VPs, honestly, they

**[27:55]** haven't written that down either. I' I've been under a number who have moved in new, and most of them don't send an operating memo like that, even though

**[28:00]** they should. This is also the same reason why senior engineers notoriously are pretty bad at writing onboarding

**[28:06]** docs. It's not laziness. It's that the knowledge that would make the doc useful has been sort of compressed into a form

**[28:12]** of automatic behavior for them and the doc is going to list steps but miss so much nuance that they have in their

**[28:18]** heads because it just makes sense for them. It's like the person who's describing the way to uh a friend's

**[28:23]** house down the road and they're giving you all of these landmarks that are local to them that make sense. It's like there's the big tree and then you stop

**[28:29]** by the the the store that has the broken down sign and then you go over it. This is no like as a stranger in these parts,

**[28:36]** you don't understand it, but they understand all of the nuances that help them get to their friend's house. And the structural trap is this. The people

**[28:43]** with the most to gain from agent delegation are exactly the people whose work is hardest to delegate. The most

**[28:49]** senior, most overloaded knowledge workers carry the highest ratio of tacet to explicit knowledge. Their work is the

**[28:56]** most compressed. It's the most invisible to themselves. They need the leverage most and the cold start problem hits

**[29:01]** them the hardest. Ironically, beginners just getting started in their careers. Folks who are you're one year, two years

**[29:07]** out of college and all of this is stuff that you are still doing intentionally, explicitly in your head, you haven't

**[29:12]** compressed it yet. You may have a much easier time with agents and delegating

**[29:18]** to OpenClaw than the seniors. And the reason I say that is because you have not gone through that automation process

**[29:23]** in your head yet. And that's actually fantastic and it's one of the reasons why firms like Shopify intentionally

**[29:29]** hire juniors because there are things that you can go much faster at than seniors. And ironically, this inability

**[29:35]** to sort of get our operational knowledge, our tacet knowledge out of our heads is at the root of at least

**[29:41]** three big chronic people problems that plague most organizations. Delegation

**[29:47]** fails. That's that's one of them, right? Managers will cite that as a key challenge. And the standard explanation is that they're control freaks. But the

**[29:53]** real explanation is that they don't know how to delegate because they don't know how to express what they've got in their heads. It's it's a real challenge for

**[29:59]** new managers. Another related one, people not getting promoted. The most common reason strong IC's plateau is

**[30:05]** that they cannot be replaced. Their knowledge work is locked in their head. And so even if they are qualified for

**[30:11]** the next level, no one wants to risk losing their expertise on their current job and that becomes a trap for them.

**[30:16]** And then of course the third one is obvious. People leave. Institutional knowledge evaporates. it walks out the door in someone's head and and it's just

**[30:22]** gone. So, I would argue agents did not create these problems, but agents create

**[30:29]** the first universal selfish incentive for every single one of us in knowledge

**[30:34]** work to actually fix these problems. Not because HR launched a knowledge management initiative, right? It's not

**[30:40]** because a consultant ran a workshop. It's because you personally want a robot to stop asking you to confirm calendar

**[30:46]** entries that you already freaking approved. and the robot needs you to describe your calendar rules first. That's new. Look, we've had decades of

**[30:53]** top- down pressure to externalize our knowledge. It never worked at scale because there was no direct personal

**[30:58]** upside for any of us. The benefit occurred entirely to the organization when you wrote the wiki, right? A and

**[31:03]** traditionally, the person who documents their expertise is the person who loses. In this case, agents flip that incentive

**[31:09]** structure on its head. The person who documents their expertise is the person who gets the leverage in the world of agents. The organization might benefit

**[31:16]** secondarily. It's actually a bottoms up knowledge management revolution disguised as a consumer AI product. And

**[31:23]** I don't think that anyone, including the people building these products, really appreciates that because if they did

**[31:28]** appreciate it, I feel like they would put more into onboarding. I have been through the onboarding flows for like

**[31:35]** half a dozen of these and they all feel really, really light. Really light for

**[31:40]** what you're expecting this agent to do, for what you're hoping it will do for you. If you want it to really lift up,

**[31:45]** leverage two, three, or more X your work. And that and that leads us to a very uncomfortable correlary that's

**[31:52]** worth naming explicitly. If the value of agents depends on your ability to

**[31:57]** articulate your work, agents are about to create an extremely visible divide in the workforce. Right now, tacet

**[32:03]** knowledge is invisible, right? Nobody knows that you can't describe your own process because nobody's ever asked you.

**[32:09]** Performance reviews tend to measure your outputs, not your self-nowledge. You might be a phenomenal operator with zero

**[32:15]** ability to explain how you operate and the system just never penalizes you and agents are about to change that. In a

**[32:21]** world where everyone has access to the same tooling, the differentiator is not which model you use or how many Mac

**[32:27]** minis you can put your open claws on. It's whether you can feed the thing well enough to actually get leverage. The

**[32:34]** people who invest that time, who can decompose their expertise into explicit

**[32:39]** delegatable components will get compounding returns. That's where the value is. Their agents improve because

**[32:46]** their specs improve. The second agent deploys faster than the first. The 10th deploys in a few minutes and they

**[32:51]** actually build on all of that knowledge. So, it doesn't even take them a ton of time to provision it because they understand the memory system so well.

**[32:58]** The people who skip all of that will install, play for a weekend, hit the wall, and conclude agents are all hype.

**[33:05]** And they will be wrong. The agent worked fine. The problem was never the agent. So, I want to propose a solution. I've

**[33:10]** gone through the problem. You understand the problem. The solution I have is this. The first agent you run should not

**[33:17]** be your open claw assistant. The first agent you run should be a tool to

**[33:22]** prepare you to run agents the way you want. And no one seems to be thinking this way, so I'm just going to say it

**[33:27]** out loud. The first agent worth deploying, it's not your personal assistant. It's not your chief of staff. It's not your scheduler. It's not your

**[33:33]** email uh guy. It's not your briefing bot. It's just an interviewer. It is one

**[33:39]** designed to do what expertise elicitation researchers do. Yes, that's a real job. Ask you the right questions

**[33:46]** in the right order with the right follow-ups to extract the operational knowledge you carry but cannot access on

**[33:51]** your own. And no, this is not the same as asking you three questions on install. I know that OpenClaw asks you

**[33:58]** who am I, who are you, and what is my job? I get that. This is a lot deeper than that. And of course, I've been

**[34:04]** building this. I've been digging in because I want to build a demo that actually allows you to immediately use this so that if you have trouble

**[34:10]** actually using your agent and making it valuable, you have a tool now to get your agent going. It's a structured

**[34:17]** elicitation workflow. I know it's a $10 word, but it basically means getting that information out of your head. Uh,

**[34:23]** it's a structured elicitation workflow that walks you through five specific layers. Your operating rhythms, what are

**[34:29]** your days, your weeks, and your months actually like in detail, not the calendar version, the real one. Your

**[34:35]** actual recurring decisions, what judgment calls you make, what are the easy calls, the hard calls, what inputs

**[34:41]** that you actually need, your dependency, who do you need things from, and when. Nobody's asking that, right? They've

**[34:47]** been through these flows. Your friction, the recurring annoyances that eat your time. Most of them don't ask that either. It takes time. I'm not going to

**[34:54]** pretend this doesn't take time, right? Like I've gone through it at best. It takes 45 minutes. It might take you longer. And and I think that time is

**[35:02]** worth it if you're going to actually save time on your agent, right? The output is structured data and you can

**[35:07]** plug it right into your open brain if you've built that. That's just a simple personal knowledge store uh that's quick to set up and runs for like 10 cents a

**[35:14]** month. Uh and then it becomes durable, right? it becomes searchable knowledge and it's available to any agent that

**[35:21]** interacts with an MCP which all of these openclaw agents do by the way and from that output I built a configuration file

**[35:28]** generator that will automatically produce soul.markdown heartbeat.mmarkdown user.mmarkdown files

**[35:34]** that you can use to provision an openclaw and that solves the gap that solves the gap that manis isn't building for perplexity isn't building for nemo

**[35:41]** claw isn't building for dispatch skips over this and to be honest with you the configuration files that I can output.

**[35:48]** And to be honest with you, the configuration files you get at the end of this process are in some ways the least interesting output. The more

**[35:55]** valuable output is the conversation itself and the way it creates a structured database, a structured map of

**[36:02]** how you work, what you know, where your leverage points are. And that makes you

**[36:07]** so much better at delegating to agents. Yes. But also talking about it means

**[36:13]** you're better at delegating to people. It makes you easier to promote. It makes your expertise survivable. All of this

**[36:20]** stuff that was locked in your head, you had an AI agent help you get it out. And that's what I focused on building. The AI agent that helps you get it out. And

**[36:28]** yes, it does help you make your agents work, which is kind of the whole reason you'd have agents. I know that every

**[36:34]** agent product in the market today is competing on the implementation layer. How easy is it to set up from scratch

**[36:41]** with your open claw? Fine. The question I have is once you have it set up, can

**[36:46]** you actually use it to do interesting stuff? Can you actually use it in ways that help your workflow? And the only

**[36:52]** way it will ever do that is if it gets into your brain and gets the stuff out that you don't think about every day.

**[36:57]** And that's why I built an open brain interview agent to help you get that knowledge out so that you can provision

**[37:03]** whatever open claw you choose in whatever way you choose confident that it actually knows the details, the

**[37:11]** nuance, the depth of your work in a way that will make it effective because that depth is where you get the

**[37:17]** disproportionate returns. That's how the people who are getting these three, four, 5x returns are doing it. So don't

**[37:23]** make your first agent the agent that is your personal assistant. Instead, make your first agent the one that prepares

**[37:30]** you to have a personal assistant agent. The extra work is worth it. I promise.

**[37:36]** Cheers.
