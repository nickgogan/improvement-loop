# Transcript: I Analyzed 512,000 Lines of Leaked Code. It Shows What's Coming for Your AI Tools.

**URL:** https://www.youtube.com/watch?v=ro5jpbi5uYc
**Segments:** 703
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 24:34
**Uploaded:** 2026-04-08

---

## Full Text

The most important thing in the Claude code leak isn't the code. I talked last week about how important it is to understand the harness around cloud code. I want to talk today about how Enthropic is building an always on agent called Conway. That was part of the leak. It wasn't announced. It was buried in the Claude code source that Enthropic accidentally published last week when a packaging error pushed half a million lines of code to a public registry. Well, everyone focused on the source code itself, the takedown notices, the security flaws. Some of the bigger pieces of news have taken a while to really dig into. Funway is one of those pieces. It's a standalone agent environment. That means it's separate from the chat. It has its own extension format. It has the ability to be woken up by outside events. It has browser control. It has connections to your tools. This is nowhere on Anthropic's roadmap page. It's an internal project today. And when you line it up against everything else anthropic has shipped in the last 3 months, it reveals a platform strategy that I think a lot of us aren't seeing clearly enough. So, let's dig into what Conway actually looks like. Let me make this concrete because the implications don't really land until you dig into what this really means. According to the leak, Conway operates as a standalone sidebar inside the Claude interface. It's not a chat window. It's actually an entire Aentic environment. It opens a dedicated page tied to a Conway instance with three core areas: search, chat, and system. The system section is where it gets really interesting. There's an extensions area where you can install add-ons, like custom tools, like interface panels, and ways for the agent to understand new kinds of information. Think of it like an app store for agent capabilities. If someone builds an extension and packages it up, Conway can install it, right? There's also a connectors and tools section showing what other services are plugged in, including a toggle that lets Claude and Chrome connect directly to the Conway instance. All of this is from the leak, by the way. And there's a section for automatic triggers, public web addresses that outside services can ping to wake the agent up. You can toggle which services are allowed to do this. And I want you to take all of that in and and now imagine what a Tuesday morning looks like 6 months after you set this up. You wake up, Conway has been running overnight. It notice three emails that match patterns learned over time matter to you. Not because you wrote rules, but because after 6 months of watching you work, it knows which three emails matter. It already drafted responses to the easy ones. But the third one is from your VP, and it flagged that one, but didn't touch it cuz it knows you need to see it. It also checked the Slack channels that it knows it needs to monitor. There's a thread in engineering where someone asked a question about Oth architecture. Conway pulled context from a design doc you reviewed last month, and it already drafted a reply sitting in Q for approval. It noticed a competitor mentioned in competitive intel and cross referenced it against the research you've been running. Your calendar also has a board meeting prep session at 10 because it knows you need to get ready for the board. Conway already pulled the latest numbers from the dashboards it has access to to help you prepare. By the way, you haven't typed a word yet. And about a third of what Conway did overnight might be wrong, right? The email draft might misread tone. The Slack reply might be technically inaccurate. you're going to catch this pretty quickly, but the net is still positive as long as Conway is partly right because it's so fast. And so what I want to get into is the gap between impressive demo because the demos always show this is completely working and actual reality. Both futures are true. The future that's a flashy demo is true in the sense that it unlocks real capabilities and Conway shows that leak. But the reality is also true. These kinds of agents tend to need a lot of babysitting and the way they make value for you in your day is actually a function of their speed and ability to iterate, not just their ability to get everything right the first time. And that's why the story I'm telling you is not just a hype session for Anthropic. It actually digs into why these agents are hard to get right. To make this work, Anthropic has to have a phenomenal ability to understand what you should prioritize in a massive array of undifferiated noise that is your workplace. And that is probably why they haven't launched Conway yet. Nevertheless, I think that's a reasonable guess at what a few months with Conway might look like not too long from now. Let's back up. Conway doesn't make sense in isolation. It makes sense as the capstone of a strategy Anthropic has been executing against all quarter because in the last 90 days, Anthropic has shipped Claude code channels, letting you message Claude code through Discord and Telegram and get notified when it finishes tasks. And this neutralized the core appeal of OpenClaw because it allowed you to essentially do OpenClaw inside Anthropic's own surface. It launched clawed co-work for non-technical users targeting the 95% of enterprise employees who aren't engineers. And co-work's initial adoption reportedly outpaced Claude code at the same stage. It was extremely popular. And then it launched Cloud Marketplace, an enterprise procurement layer where partner apps built on Claude like GitLab or Harvey or Snowflake could be purchased through Anthropic building. Anthropic handles the invoices and purchases count against existing spend commitments. No commission yet. They're just buying market share in the distribution. Meanwhile, Anthropic committed hund00 million dollars to the Claude partner network and Accenture started training 30,000 professionals on Claude while Deoid and Cognizant and Infosys act as anchor partners for the initiative. This is what a complete system integrator lockin looks like at enterprise scale. And Anthropic surprised everybody with what happens next. They're already going for this enterprise lock in with their current strategy. They have now blocked all thirdparty tools from cloud subscriptions as their next move. Open Claw came first with Anthropic confirming the restriction will roll out to everything else in coming weeks. So if you want to use Claude through anything Anthropic didn't build, your pay peruse rates could run 10 to 50 times higher than what the subscription covered. Period. No way to change that. Now add Conway on the top and you're not looking at five separate product decisions. You're looking at a single platform strategy executed across five surfaces in a quarter. You have a developer tool cloud code, an enterprise tool co-work, the always on agent, Conway, the distribution layer, and an enforcement mechanism. That's the harness side. Every one of those pieces pushes in the same direction. If you're old enough to remember the trajectory of Microsoft in the '90s, this feels familiar, right? Microsoft went from selling an operating system, DOSs, to owning the desktop, Windows, to controlling the application layer, Office to locking in the enterprise with Active Directory and Exchange. Every step was an individual product, but together they were a strategy that moved Microsoft from operating system vendor to the company that owns how businesses compute. And that took about 15 years. Anthropic is speedrunning this. They're attempting the same arc, model provider to developer tool to enterprise platform to agent operating system in 15 months. Conway is kind of the active directory play. It's the piece that makes everything else in the stack sticky because the persistent agent knows your organization in a way that nothing else does. The detail in the Conway leak that I keep coming back to is the extension format which is a funny detail to pick on but it exposes the tension at the heart of anthropic strategy. Remember the model context protocol is anthropic's own open standard. They published it and everybody went for it. Open AI adopted it. Google adopted it. The Linux foundation hosts it. It is designed to be the universal connector between AI tools and AI data sources. If you built Open Brain after my piece in March, you are running on an MCP server right now. The whole point is that any AI client can talk to any data source through one open protocol. Well, Conway uses MCP, but not in the same way. Conway's CNW.zip extension format sits on top of MCP and creates a proprietary layer. So, extensions packaged as a CNW.zip include custom interface panels, information handlers, and tools that work specifically inside Conway's environment. They're not portable tools that work everywhere. They're Conway only tools. This is the Google Play services pattern. Android is built on open source software. Sure, it's free for anyone to use. But the Google Play Services layer that makes Android commercially viable like maps, payments, push notifications, the Play Store itself, that's proprietary. So you can technically build an Android phone without Google, but in practice, nobody does because the valuable stuff lives in the proprietary layer. So MCP is the open foundation and Conway's extension ecosystem is the proprietary layer on the top. Enthropic gets the credibility of publishing an open standard and the commercial advantage of building the valuable tooling on a format that runs in their environment. Now think about what this means. If you're a developer building tools for agents, you have two paths. Path one, you can build a standard MCP tool. It's portable. It works with Claude. It works with Chad GBT. It works with Gemini. Any MCP compatible client, that's great. But there's no distribution mechanism. You have to come up with a distribution mechanism. There's no app store, right? There's no featured placement. You're building a website in 2008 and everybody's downloading iPhone apps. It's the same thing. Two, let's say you build a Conway extension. Oh, well, it only works inside Conway, but Conway has a built-in extensions directory. This is the app store. So, when Anthropic launches this to millions of Cloud subscribers, your extension is discoverable inside the environment where people are already working. You don't need to convince anyone to install anything. You're in the store. See that? If that choice sounds familiar, it sure should. It's exactly the same choice Apple gave mobile developers in 2008 and 2009. Build for the open web or build native for the iPhone. And we know how that played out. By and large, the open web might have been the long-term architectural choice, but the app store made all the money. And so, all of the app makers went to the App Store. Now, a decade later, of course, the web still exists. It's still critically important. But the center of gravity in mobile software is native apps distributed through platform controlled stores. The developers who bet on Google Play Services free Android learned this the hard way. And Amazon even tried it with a Firephone and Fire tablets and it totally flopped. Not because the hardware was bad, but because the ecosystem had already organized around Google's proprietary layer. The open kernel didn't matter when the valuable apps needed the proprietary services to function. This is a pattern we've seen before and it's a pattern that has a known outcome. If you're building on MCP because you believed it meant your tools would be portable across all platforms, that's technically true. But you should also understand that Conway's extension model creates a gravitational pull toward anthropic and other model makers are going to follow suit. And so we are going to start to live in a world where Conway becomes the only place tools work in anthropic and you'll have a similar thing in OpenAI and probably a similar thing in Google. I think what happened to OpenClaw over the last couple weeks is too related to be coincidental. Peter Steinberger, OpenClaw's creator, joined OpenAI on February 14th. Sam Alman was excited and said he'd drive the next generation of personal agents. OpenClaw moved to a foundation with OpenAI's backing. And within weeks, Enthropic began enforcing that ban. First quietly blocking thirdparty tools from using subscription login credentials in January, retroactively justified as tightening safeguards, and then a terms of service revision in February explicitly prohibiting that activity, and then the enforcement that cut off open everyone else that came even more recently than that. So Steinberger's read was pretty simple. First, they copy popular features into their closed harness, and then they lock out open source. And that's exactly the pattern I keep an eye on when it comes to Conway. Step one, build the first party version of what the community built. Open Claw became Claude Code channels became Conway. Step two, make the first party version free or subsidized inside the subscription. Step three, make the third party version expensive or impossible. And step four, ship the proprietary format that ensures the ecosystem builds for your surface, not the open one. We are at step one on Conway and steps two through four came out in that claw code leak. Every previous form of tech platform lockin was about stuff. Microsoft locked you in by your files. Salesforce locked you in by your customer records. Slack locked you in by your communication history. And stuff is really painful to migrate. A lot of people will not do it. Technically, it's possible. There are export tools. There are consultants who specialize in that. The switching cost is painful. It's measured in months and sometimes tens of thousands or more dollars. But it's nothing compared to Conway. If Conway launches, it locks in something different. It locks in the accumulated model of how you work. Not your files, but the patterns the agent learned by watching you use them. Not your Slack messages, but the understanding of which messages you respond to in 5 minutes and which ones you ignore for 3 days. Not your calendar, but the knowledge that you always reschedule your 2 p.m. on Thursdays and meetings with your VP always run long. The model doesn't export that. There's no CSV of how this person thinks that you can grab. There's no migration consultant for behavioral contact. So when you switch away from Conway after 6 months, you don't just lose an agent, you lose the 6 months of compounding that made the agent useful. You're back to a brilliant stranger you have to explain everything to. And that's a trade no one wants to make. To be honest, this is lock in at a layer that hasn't existed before. It's not really about data portability. We have laws. We have frameworks for that. It's about intelligence portability. The model of you that the agent built is the product of your data plus their compute plus 6 months of inference. Who owns that? Can you take it with you? If you can take it with you, what format can you take it with you in? These questions don't have legal frameworks yet, let alone regulatory frameworks, let alone even like considered opinions because we haven't had to face it before. Ultimately, I think it's fair to say the accumulated behavioral model, the understanding of how you work, seems like it should be portable. I've suggested a way to make it portable by launching a skill that helps you understand how you work. But it will only truly be portable if we agree as a business community that that's the way things ought to work. Because ultimately to do that, well, we need a practice. We need technical solutions from all the major model makers that say yes your behavior is something that we will not use for lock in. Your behavior is something that should come with you. So the policies around behavioral context portability should ship before Conway does, not after. If we step back a minute, here's the frame that I think is useful for understanding what's actually happening in the industry. The first era of AI competition was all about the models, right? We knew that, right? 2023, 2024, who has the best foundation model, benchmarks, training runs, context windows. We all talked about it a lot, right? GPT versus Claude versus Gemini. That race isn't over, but the margins between Frontier models have compressed to the point where it's no longer the primary axis of competition. And the second era that we're coming to now is about some of these different surfaces and the memory behind them. Right? 2025 and into 2026, who owns the interface where people actually work? Clawed coat, cursor, open claw, wind surf, harness wars. This is the era we just watches climax with the open claw ban and Steinberger's defection to open AI. And we are moving from interfaces into this idea of persistence and memory that drives those experience. Who owns the always on layer is the question for the rest of 2026. The agent that doesn't just respond when prompted, but stays running, accumulates context, wakes on events, and acts autonomously. That agent that knows you not because you're told it something, but because it's been watching, learning, and remembering. That is the persistence question that shapes the next year. That is the question that we have to wrestle with whether we're looking at Google or OpenAI or Anthropic. Who do we want to choose to run that persistence layer for us? All three labs, Gemini, all three labs, Google, Anthropic, and OpenAI have converged on the same insight. They're all building the model as a loss leader and they want to own this persistent agent layer. The thing that holds your memory, your context, your workflows, your integrations. That's the money product. Whoever owns that layer has customer lockin like we have never seen before. Not because the model is better, but because the switching cost is unthinkable. You cannot imagine the cost of switching when this model knows you that well. If you're building agents for yourself, for your team, for your clients, Conway changes your calculus. Now, just the fact that it leaked changes your calculus. If you're an enterprise architecting an agent platform, the question is really clear at this point. Do you want your agent memory to live inside a single provers's infrastructure? Conway and similar products will be convenient. They will be polished. They will ship with an extension ecosystem from day one. But everything your agents learn about your organization, your workflows, your decisions, your institutional knowledge lives inside Anthropic. If you switch providers, you're leaving your brain behind. If you built a solution that is a universal context layer, I've suggested this with open brain. There's lots of other ways to do it. Then the memory is yours and it it's exposed through an open protocol that any model can access. Funway's launch is going to test whether that matters enough to justify the setup cost or whether convenience is going to win. And I need to be honest, I think for a lot of companies, convenience is going to win. Enthropic and Google and OpenAI will make it easy. If you get an agent that just takes care of everything and it pulls you in and it's easy to onboard and you're already a Claude user and now you can use Conway and you wake up and it's just incredible from day one, you're not going to switch, right? Even if it's not perfect, even if it's learning what your VP needs to hear in that third email from the beginning of the video, you're still not going to switch because it's so good at everything else, it can be partially good and still so proactive, so memorable, so nuanced, so thoughtful, you won't move, you won't switch. And I have no illusions about that. I think that one of the things that we are going to see that is the whole game for the rest of 2026 is which companies and to some extent which individuals decide that they would rather own their own persistent memory layer regardless of the convenience of a particular launched agentic system versus which ones want to lean in and pick an agentic system and end up realizing they're locked in there. I think that story is already starting to take shape. I think we're starting to see the broader consumer base pick Chad GPT free or go plans. We're starting to see active professionals pick claude plans and that's starting to leak into enterprise contracts. And we are going to have to see whether concerns around portability and privacy shape enterprise deals and consumer choices or whether people are going to be comfortable with a product like Conway because Conway is just the tip of the iceberg. We are going to see Anthropic, OpenAI, and Google all ship versions of this in the next few months. We're going to have to see if people are comfortable staking the future of their careers on a lock in with a company. And I'm not overexaggerating. If you want to get promoted, increasingly, it will be a function of how well you use the persistent agent layer at your company, which requires your willingness to hop in and use it from day one. If you want to build a team, you're going to need to show that you can build that team from day one across a persistent context layer that the company decides. If you want to start a business, you are going to have to face the decision, which of these agentic interfaces do I choose? And in your own life, you're going to have to decide, do I want these agentic interfaces? Do I want to build my own? And enterprises will make that same choice. And there will be third parties who will claim to stitch together particular models and particular context layers into something that enterprises can choose and that is claimed to be portable. I am concerned that in the middle of all that mess, we are going to miss the larger point. We are going to miss the realization that the behavioral evidence of how we work should belong to us. It should be ours and that companies should be able to learn from it, leverage it while we work there with them and then we should be able to take it with us so that our persistent talent imprint on the context layer is not something they can just copy and continue to leverage after we depart. And so there's a sense in which my ability to handle a Slack message triage, my ability to read email and see what's important, my ability to understand whether a PowerPoint is well structured or not, that is becoming not just my talent, but a company's skill. And so I want us to have an intentional conversation because I understand this is very valuable to companies that when you have talent on your roster that can do this, that's incredibly worthwhile. You want to capture it. I get it. It's going to happen. But in that case, what is the right way to allocate that value back? Do you then say, "We're compensating the employee for using this behavioral evidence as a way to improve our context layer over time." Do you instead go with the approach that the context layer is portable and the employee should be able to take some sort of behavioral fingerprint out and some of the facts and the proprietary information should stay or and I think this is probably the most likely do we not have the conversation at all because it's a difficult conversation with weird power dynamics and instead we say you know what we're going to default to the old assumption whatever you do while you work is the company's property and that includes cludes your behavior at the company and if the company can learn a lot from that they're going to do that and they're going to move on. I think the latter is more likely but I think it poses some real challenges for employees. Ironically this approach as much as it empowers individuals and we've talked so much about how persistent context can give individuals and small team superpowers. The idea of a persistent context memory like this leaked Conway approach actually empowers enterprises in the employee relationship because the enterprise can look at this employee and say, "We know how good you are at this, this, this, and this. We know how to promote you. We know how to give you what you want to stay, but also we know that you're effective because of this agent and you're going to want to stay because when you work with this agent, you're 2x more effective and we can prove it. And we have never had that kind of carrot and stick approach employers to employees and we're all going to figure that out. As you look at the Claude code leaks, as you look at Conway, as you look at other leaks that come out, please start to think through what are the larger implications here? What are the non-obvious implications of extending agents into our lives in ways that are persistent? I hope this video has given you a sense of the different ways that this can unfold. And if you're interested in building a persistent memory layer, you know, I have a way to do that and it can be yours and you can have a behavioral audit that you take with you because I think that's really important. I have no illusions. We are going to be at a point in many cases where that's not an option because employers are going to hold the cards and they're going to encourage employees either through carrots or through sticks to participate in these proprietary contextual platforms in ways that enable the employer to leverage the collective intelligence of teams to make those agents better and stronger and not even necessarily for nefarious purposes. Like the easy narrative is, oh, then they're going to fire everybody. I don't think that's true because you still have to have a lot of smart humans to manage these agents. But it does mean that the lockin effect for employees inside employers is going to get very strong in the second half of 2026. So pick your fighter carefully, right? Choose your employer carefully because increasingly choosing your employer is going to mean who are you choosing to work with as a persistent agent. Are you working with a claude company or a Chad JPT company? It used to be Windows and Mac, right? Well, this is more important than that. Now, it's are you working with an agent that understands you and that you're super familiar with and that you can be two or three more productive with because you've had that time. That's the future that Conway is pointing at. And I want us to understand that because it's easy to get lost in the open claw fiasco. But I want you to understand underneath that why Anthropic is making the moves that they are and where they're going with the persistent agent layer because that's also where OpenAI and Google are going too. Best of luck out there.

---

## Timestamped Segments

**[0:00]** The most important thing in the Claude

**[0:01]** code leak isn't the code. I talked last

**[0:04]** week about how important it is to

**[0:06]** understand the harness around cloud

**[0:07]** code. I want to talk today about how

**[0:09]** Enthropic is building an always on agent

**[0:11]** called Conway. That was part of the

**[0:13]** leak. It wasn't announced. It was buried

**[0:15]** in the Claude code source that Enthropic

**[0:18]** accidentally published last week when a

**[0:20]** packaging error pushed half a million

**[0:21]** lines of code to a public registry.

**[0:23]** Well, everyone focused on the source

**[0:24]** code itself, the takedown notices, the

**[0:26]** security flaws. Some of the bigger

**[0:28]** pieces of news have taken a while to

**[0:30]** really dig into. Funway is one of those

**[0:32]** pieces. It's a standalone agent

**[0:34]** environment. That means it's separate

**[0:35]** from the chat. It has its own extension

**[0:37]** format. It has the ability to be woken

**[0:39]** up by outside events. It has browser

**[0:41]** control. It has connections to your

**[0:42]** tools. This is nowhere on Anthropic's

**[0:45]** roadmap page. It's an internal project

**[0:47]** today. And when you line it up against

**[0:49]** everything else anthropic has shipped in

**[0:51]** the last 3 months, it reveals a platform

**[0:53]** strategy that I think a lot of us aren't

**[0:55]** seeing clearly enough. So, let's dig

**[0:57]** into what Conway actually looks like.

**[0:59]** Let me make this concrete because the

**[1:00]** implications don't really land until you

**[1:03]** dig into what this really means.

**[1:05]** According to the leak, Conway operates

**[1:07]** as a standalone sidebar inside the

**[1:10]** Claude interface. It's not a chat

**[1:12]** window. It's actually an entire Aentic

**[1:15]** environment. It opens a dedicated page

**[1:17]** tied to a Conway instance with three

**[1:19]** core areas: search, chat, and system.

**[1:22]** The system section is where it gets

**[1:24]** really interesting. There's an

**[1:25]** extensions area where you can install

**[1:27]** add-ons, like custom tools, like

**[1:29]** interface panels, and ways for the agent

**[1:31]** to understand new kinds of information.

**[1:33]** Think of it like an app store for agent

**[1:35]** capabilities. If someone builds an

**[1:37]** extension and packages it up, Conway can

**[1:39]** install it, right? There's also a

**[1:40]** connectors and tools section showing

**[1:42]** what other services are plugged in,

**[1:44]** including a toggle that lets Claude and

**[1:46]** Chrome connect directly to the Conway

**[1:48]** instance. All of this is from the leak,

**[1:49]** by the way. And there's a section for

**[1:51]** automatic triggers, public web addresses

**[1:53]** that outside services can ping to wake

**[1:56]** the agent up. You can toggle which

**[1:58]** services are allowed to do this. And I

**[2:00]** want you to take all of that in and and

**[2:02]** now imagine what a Tuesday morning looks

**[2:04]** like 6 months after you set this up. You

**[2:07]** wake up, Conway has been running

**[2:08]** overnight. It notice three emails that

**[2:10]** match patterns learned over time matter

**[2:12]** to you. Not because you wrote rules, but

**[2:15]** because after 6 months of watching you

**[2:17]** work, it knows which three emails

**[2:19]** matter. It already drafted responses to

**[2:21]** the easy ones. But the third one is from

**[2:22]** your VP, and it flagged that one, but

**[2:24]** didn't touch it cuz it knows you need to

**[2:26]** see it. It also checked the Slack

**[2:27]** channels that it knows it needs to

**[2:29]** monitor. There's a thread in engineering

**[2:30]** where someone asked a question about Oth

**[2:32]** architecture. Conway pulled context from

**[2:34]** a design doc you reviewed last month,

**[2:36]** and it already drafted a reply sitting

**[2:38]** in Q for approval. It noticed a

**[2:40]** competitor mentioned in competitive

**[2:42]** intel and cross referenced it against

**[2:43]** the research you've been running. Your

**[2:45]** calendar also has a board meeting prep

**[2:47]** session at 10 because it knows you need

**[2:48]** to get ready for the board. Conway

**[2:50]** already pulled the latest numbers from

**[2:52]** the dashboards it has access to to help

**[2:53]** you prepare. By the way, you haven't

**[2:56]** typed a word yet. And about a third of

**[2:58]** what Conway did overnight might be

**[3:00]** wrong, right? The email draft might

**[3:02]** misread tone. The Slack reply might be

**[3:04]** technically inaccurate. you're going to

**[3:06]** catch this pretty quickly, but the net

**[3:08]** is still positive as long as Conway is

**[3:11]** partly right because it's so fast. And

**[3:14]** so what I want to get into is the gap

**[3:17]** between impressive demo because the

**[3:18]** demos always show this is completely

**[3:20]** working and actual reality. Both futures

**[3:23]** are true. The future that's a flashy

**[3:25]** demo is true in the sense that it

**[3:28]** unlocks real capabilities and Conway

**[3:30]** shows that leak. But the reality is also

**[3:33]** true. These kinds of agents tend to need

**[3:36]** a lot of babysitting and the way they

**[3:38]** make value for you in your day is

**[3:40]** actually a function of their speed and

**[3:42]** ability to iterate, not just their

**[3:46]** ability to get everything right the

**[3:48]** first time. And that's why the story I'm

**[3:49]** telling you is not just a hype session

**[3:51]** for Anthropic. It actually digs into why

**[3:54]** these agents are hard to get right. To

**[3:56]** make this work, Anthropic has to have a

**[3:59]** phenomenal ability to understand what

**[4:02]** you should prioritize in a massive array

**[4:06]** of undifferiated noise that is your

**[4:08]** workplace. And that is probably why they

**[4:11]** haven't launched Conway yet.

**[4:12]** Nevertheless, I think that's a

**[4:14]** reasonable guess at what a few months

**[4:17]** with Conway might look like not too long

**[4:20]** from now. Let's back up. Conway doesn't

**[4:22]** make sense in isolation. It makes sense

**[4:24]** as the capstone of a strategy Anthropic

**[4:26]** has been executing against all quarter

**[4:28]** because in the last 90 days, Anthropic

**[4:30]** has shipped Claude code channels,

**[4:32]** letting you message Claude code through

**[4:34]** Discord and Telegram and get notified

**[4:36]** when it finishes tasks. And this

**[4:38]** neutralized the core appeal of OpenClaw

**[4:40]** because it allowed you to essentially do

**[4:42]** OpenClaw inside Anthropic's own surface.

**[4:44]** It launched clawed co-work for

**[4:46]** non-technical users targeting the 95% of

**[4:49]** enterprise employees who aren't

**[4:50]** engineers. And co-work's initial

**[4:52]** adoption reportedly outpaced Claude code

**[4:54]** at the same stage. It was extremely

**[4:55]** popular. And then it launched Cloud

**[4:57]** Marketplace, an enterprise procurement

**[4:59]** layer where partner apps built on Claude

**[5:00]** like GitLab or Harvey or Snowflake could

**[5:02]** be purchased through Anthropic building.

**[5:04]** Anthropic handles the invoices and

**[5:06]** purchases count against existing spend

**[5:08]** commitments. No commission yet. They're

**[5:10]** just buying market share in the

**[5:11]** distribution. Meanwhile, Anthropic

**[5:13]** committed hund00 million dollars to the

**[5:15]** Claude partner network and Accenture

**[5:17]** started training 30,000 professionals on

**[5:19]** Claude while Deoid and Cognizant and

**[5:21]** Infosys act as anchor partners for the

**[5:23]** initiative. This is what a complete

**[5:26]** system integrator lockin looks like at

**[5:28]** enterprise scale. And Anthropic

**[5:30]** surprised everybody with what happens

**[5:32]** next. They're already going for this

**[5:34]** enterprise lock in with their current

**[5:36]** strategy. They have now blocked all

**[5:38]** thirdparty tools from cloud

**[5:39]** subscriptions as their next move. Open

**[5:41]** Claw came first with Anthropic

**[5:43]** confirming the restriction will roll out

**[5:44]** to everything else in coming weeks. So

**[5:46]** if you want to use Claude through

**[5:48]** anything Anthropic didn't build, your

**[5:50]** pay peruse rates could run 10 to 50

**[5:52]** times higher than what the subscription

**[5:54]** covered. Period. No way to change that.

**[5:57]** Now add Conway on the top and you're not

**[6:00]** looking at five separate product

**[6:01]** decisions. You're looking at a single

**[6:03]** platform strategy executed across five

**[6:05]** surfaces in a quarter. You have a

**[6:07]** developer tool cloud code, an enterprise

**[6:08]** tool co-work, the always on agent,

**[6:10]** Conway, the distribution layer, and an

**[6:12]** enforcement mechanism. That's the

**[6:14]** harness side. Every one of those pieces

**[6:16]** pushes in the same direction. If you're

**[6:18]** old enough to remember the trajectory of

**[6:19]** Microsoft in the '90s, this feels

**[6:21]** familiar, right? Microsoft went from

**[6:23]** selling an operating system, DOSs, to

**[6:24]** owning the desktop, Windows, to

**[6:26]** controlling the application layer,

**[6:27]** Office to locking in the enterprise with

**[6:29]** Active Directory and Exchange. Every

**[6:31]** step was an individual product, but

**[6:33]** together they were a strategy that moved

**[6:35]** Microsoft from operating system vendor

**[6:37]** to the company that owns how businesses

**[6:39]** compute. And that took about 15 years.

**[6:42]** Anthropic is speedrunning this. They're

**[6:44]** attempting the same arc, model provider

**[6:46]** to developer tool to enterprise platform

**[6:48]** to agent operating system in 15 months.

**[6:50]** Conway is kind of the active directory

**[6:52]** play. It's the piece that makes

**[6:53]** everything else in the stack sticky

**[6:55]** because the persistent agent knows your

**[6:56]** organization in a way that nothing else

**[6:59]** does. The detail in the Conway leak that

**[7:01]** I keep coming back to is the extension

**[7:03]** format which is a funny detail to pick

**[7:05]** on but it exposes the tension at the

**[7:07]** heart of anthropic strategy. Remember

**[7:09]** the model context protocol is

**[7:10]** anthropic's own open standard. They

**[7:12]** published it and everybody went for it.

**[7:14]** Open AI adopted it. Google adopted it.

**[7:16]** The Linux foundation hosts it. It is

**[7:18]** designed to be the universal connector

**[7:21]** between AI tools and AI data sources. If

**[7:24]** you built Open Brain after my piece in

**[7:26]** March, you are running on an MCP server

**[7:28]** right now. The whole point is that any

**[7:30]** AI client can talk to any data source

**[7:32]** through one open protocol. Well, Conway

**[7:35]** uses MCP, but not in the same way.

**[7:37]** Conway's CNW.zip extension format sits

**[7:40]** on top of MCP and creates a proprietary

**[7:43]** layer. So, extensions packaged as a

**[7:46]** CNW.zip include custom interface panels,

**[7:49]** information handlers, and tools that

**[7:51]** work specifically inside Conway's

**[7:53]** environment. They're not portable tools

**[7:54]** that work everywhere. They're Conway

**[7:56]** only tools. This is the Google Play

**[7:58]** services pattern. Android is built on

**[8:00]** open source software. Sure, it's free

**[8:02]** for anyone to use. But the Google Play

**[8:04]** Services layer that makes Android

**[8:06]** commercially viable like maps, payments,

**[8:08]** push notifications, the Play Store

**[8:10]** itself, that's proprietary. So you can

**[8:13]** technically build an Android phone

**[8:14]** without Google, but in practice, nobody

**[8:16]** does because the valuable stuff lives in

**[8:18]** the proprietary layer. So MCP is the

**[8:21]** open foundation and Conway's extension

**[8:24]** ecosystem is the proprietary layer on

**[8:27]** the top. Enthropic gets the credibility

**[8:29]** of publishing an open standard and the

**[8:30]** commercial advantage of building the

**[8:32]** valuable tooling on a format that runs

**[8:34]** in their environment. Now think about

**[8:36]** what this means. If you're a developer

**[8:37]** building tools for agents, you have two

**[8:39]** paths. Path one, you can build a

**[8:41]** standard MCP tool. It's portable. It

**[8:43]** works with Claude. It works with Chad

**[8:45]** GBT. It works with Gemini. Any MCP

**[8:47]** compatible client, that's great. But

**[8:49]** there's no distribution mechanism. You

**[8:50]** have to come up with a distribution

**[8:51]** mechanism. There's no app store, right?

**[8:53]** There's no featured placement. You're

**[8:55]** building a website in 2008 and

**[8:57]** everybody's downloading iPhone apps.

**[8:58]** It's the same thing. Two, let's say you

**[9:00]** build a Conway extension. Oh, well, it

**[9:03]** only works inside Conway, but Conway has

**[9:06]** a built-in extensions directory. This is

**[9:08]** the app store. So, when Anthropic

**[9:11]** launches this to millions of Cloud

**[9:12]** subscribers, your extension is

**[9:14]** discoverable inside the environment

**[9:16]** where people are already working. You

**[9:17]** don't need to convince anyone to install

**[9:19]** anything. You're in the store. See that?

**[9:22]** If that choice sounds familiar, it sure

**[9:24]** should. It's exactly the same choice

**[9:26]** Apple gave mobile developers in 2008 and

**[9:29]** 2009. Build for the open web or build

**[9:32]** native for the iPhone. And we know how

**[9:34]** that played out. By and large, the open

**[9:36]** web might have been the long-term

**[9:38]** architectural choice, but the app store

**[9:40]** made all the money. And so, all of the

**[9:42]** app makers went to the App Store. Now, a

**[9:44]** decade later, of course, the web still

**[9:46]** exists. It's still critically important.

**[9:48]** But the center of gravity in mobile

**[9:49]** software is native apps distributed

**[9:51]** through platform controlled stores. The

**[9:53]** developers who bet on Google Play

**[9:54]** Services free Android learned this the

**[9:56]** hard way. And Amazon even tried it with

**[9:58]** a Firephone and Fire tablets and it

**[10:00]** totally flopped. Not because the

**[10:02]** hardware was bad, but because the

**[10:04]** ecosystem had already organized around

**[10:06]** Google's proprietary layer. The open

**[10:08]** kernel didn't matter when the valuable

**[10:10]** apps needed the proprietary services to

**[10:12]** function. This is a pattern we've seen

**[10:15]** before and it's a pattern that has a

**[10:16]** known outcome. If you're building on MCP

**[10:19]** because you believed it meant your tools

**[10:21]** would be portable across all platforms,

**[10:23]** that's technically true. But you should

**[10:25]** also understand that Conway's extension

**[10:27]** model creates a gravitational pull

**[10:29]** toward anthropic and other model makers

**[10:31]** are going to follow suit. And so we are

**[10:33]** going to start to live in a world where

**[10:35]** Conway becomes the only place tools work

**[10:37]** in anthropic and you'll have a similar

**[10:39]** thing in OpenAI and probably a similar

**[10:41]** thing in Google. I think what happened

**[10:42]** to OpenClaw over the last couple weeks

**[10:44]** is too related to be coincidental. Peter

**[10:47]** Steinberger, OpenClaw's creator, joined

**[10:49]** OpenAI on February 14th. Sam Alman was

**[10:52]** excited and said he'd drive the next

**[10:53]** generation of personal agents. OpenClaw

**[10:56]** moved to a foundation with OpenAI's

**[10:57]** backing. And within weeks, Enthropic

**[10:59]** began enforcing that ban. First quietly

**[11:01]** blocking thirdparty tools from using

**[11:03]** subscription login credentials in

**[11:05]** January, retroactively justified as

**[11:07]** tightening safeguards, and then a terms

**[11:09]** of service revision in February

**[11:11]** explicitly prohibiting that activity,

**[11:12]** and then the enforcement that cut off

**[11:15]** open everyone else that came even more

**[11:17]** recently than that. So Steinberger's

**[11:18]** read was pretty simple. First, they copy

**[11:21]** popular features into their closed

**[11:22]** harness, and then they lock out open

**[11:23]** source. And that's exactly the pattern I

**[11:26]** keep an eye on when it comes to Conway.

**[11:28]** Step one, build the first party version

**[11:30]** of what the community built. Open Claw

**[11:31]** became Claude Code channels became

**[11:33]** Conway. Step two, make the first party

**[11:35]** version free or subsidized inside the

**[11:37]** subscription. Step three, make the third

**[11:38]** party version expensive or impossible.

**[11:41]** And step four, ship the proprietary

**[11:43]** format that ensures the ecosystem builds

**[11:46]** for your surface, not the open one. We

**[11:48]** are at step one on Conway and steps two

**[11:50]** through four came out in that claw code

**[11:52]** leak. Every previous form of tech

**[11:55]** platform lockin was about stuff.

**[11:56]** Microsoft locked you in by your files.

**[11:59]** Salesforce locked you in by your

**[12:00]** customer records. Slack locked you in by

**[12:03]** your communication history. And stuff is

**[12:05]** really painful to migrate. A lot of

**[12:07]** people will not do it. Technically, it's

**[12:09]** possible. There are export tools. There

**[12:12]** are consultants who specialize in that.

**[12:15]** The switching cost is painful. It's

**[12:17]** measured in months and sometimes tens of

**[12:19]** thousands or more dollars. But it's

**[12:20]** nothing compared to Conway. If Conway

**[12:22]** launches, it locks in something

**[12:24]** different. It locks in the accumulated

**[12:26]** model of how you work. Not your files,

**[12:28]** but the patterns the agent learned by

**[12:31]** watching you use them. Not your Slack

**[12:33]** messages, but the understanding of which

**[12:35]** messages you respond to in 5 minutes and

**[12:37]** which ones you ignore for 3 days. Not

**[12:39]** your calendar, but the knowledge that

**[12:41]** you always reschedule your 2 p.m. on

**[12:43]** Thursdays and meetings with your VP

**[12:44]** always run long. The model doesn't

**[12:46]** export that. There's no CSV of how this

**[12:49]** person thinks that you can grab. There's

**[12:51]** no migration consultant for behavioral

**[12:53]** contact. So when you switch away from

**[12:55]** Conway after 6 months, you don't just

**[12:57]** lose an agent, you lose the 6 months of

**[12:59]** compounding that made the agent useful.

**[13:02]** You're back to a brilliant stranger you

**[13:04]** have to explain everything to. And

**[13:06]** that's a trade no one wants to make. To

**[13:08]** be honest, this is lock in at a layer

**[13:10]** that hasn't existed before. It's not

**[13:12]** really about data portability. We have

**[13:14]** laws. We have frameworks for that. It's

**[13:16]** about intelligence portability. The

**[13:19]** model of you that the agent built is the

**[13:22]** product of your data plus their compute

**[13:24]** plus 6 months of inference. Who owns

**[13:27]** that? Can you take it with you? If you

**[13:29]** can take it with you, what format can

**[13:32]** you take it with you in? These questions

**[13:34]** don't have legal frameworks yet, let

**[13:36]** alone regulatory frameworks, let alone

**[13:37]** even like considered opinions because we

**[13:39]** haven't had to face it before.

**[13:41]** Ultimately, I think it's fair to say the

**[13:43]** accumulated behavioral model, the

**[13:45]** understanding of how you work, seems

**[13:47]** like it should be portable. I've

**[13:48]** suggested a way to make it portable by

**[13:51]** launching a skill that helps you

**[13:52]** understand how you work. But it will

**[13:54]** only truly be portable if we agree as a

**[13:57]** business community that that's the way

**[13:59]** things ought to work. Because ultimately

**[14:00]** to do that, well, we need a practice. We

**[14:03]** need technical solutions from all the

**[14:05]** major model makers that say yes your

**[14:08]** behavior is something that we will not

**[14:10]** use for lock in. Your behavior is

**[14:12]** something that should come with you. So

**[14:13]** the policies around behavioral context

**[14:16]** portability should ship before Conway

**[14:18]** does, not after. If we step back a

**[14:20]** minute, here's the frame that I think is

**[14:22]** useful for understanding what's actually

**[14:24]** happening in the industry. The first era

**[14:26]** of AI competition was all about the

**[14:28]** models, right? We knew that, right?

**[14:30]** 2023, 2024, who has the best foundation

**[14:32]** model, benchmarks, training runs,

**[14:34]** context windows. We all talked about it

**[14:36]** a lot, right? GPT versus Claude versus

**[14:38]** Gemini. That race isn't over, but the

**[14:40]** margins between Frontier models have

**[14:42]** compressed to the point where it's no

**[14:44]** longer the primary axis of competition.

**[14:46]** And the second era that we're coming to

**[14:48]** now is about some of these different

**[14:50]** surfaces and the memory behind them.

**[14:51]** Right? 2025 and into 2026, who owns the

**[14:55]** interface where people actually work?

**[14:57]** Clawed coat, cursor, open claw, wind

**[15:00]** surf, harness wars. This is the era we

**[15:03]** just watches climax with the open claw

**[15:06]** ban and Steinberger's defection to open

**[15:08]** AI. And we are moving from interfaces

**[15:10]** into this idea of persistence and memory

**[15:13]** that drives those experience. Who owns

**[15:16]** the always on layer is the question for

**[15:18]** the rest of 2026. The agent that doesn't

**[15:20]** just respond when prompted, but stays

**[15:22]** running, accumulates context, wakes on

**[15:24]** events, and acts autonomously. That

**[15:27]** agent that knows you not because you're

**[15:29]** told it something, but because it's been

**[15:30]** watching, learning, and remembering.

**[15:32]** That is the persistence question that

**[15:35]** shapes the next year. That is the

**[15:38]** question that we have to wrestle with

**[15:40]** whether we're looking at Google or

**[15:42]** OpenAI or Anthropic. Who do we want to

**[15:45]** choose to run that persistence layer for

**[15:48]** us? All three labs, Gemini, all three

**[15:51]** labs, Google, Anthropic, and OpenAI have

**[15:53]** converged on the same insight. They're

**[15:54]** all building the model as a loss leader

**[15:56]** and they want to own this persistent

**[15:59]** agent layer. The thing that holds your

**[16:01]** memory, your context, your workflows,

**[16:03]** your integrations. That's the money

**[16:05]** product. Whoever owns that layer has

**[16:08]** customer lockin like we have never seen

**[16:10]** before. Not because the model is better,

**[16:13]** but because the switching cost is

**[16:15]** unthinkable. You cannot imagine the cost

**[16:17]** of switching when this model knows you

**[16:20]** that well. If you're building agents for

**[16:22]** yourself, for your team, for your

**[16:24]** clients, Conway changes your calculus.

**[16:26]** Now, just the fact that it leaked

**[16:28]** changes your calculus. If you're an

**[16:30]** enterprise architecting an agent

**[16:31]** platform, the question is really clear

**[16:33]** at this point. Do you want your agent

**[16:34]** memory to live inside a single provers's

**[16:37]** infrastructure? Conway and similar

**[16:39]** products will be convenient. They will

**[16:41]** be polished. They will ship with an

**[16:43]** extension ecosystem from day one. But

**[16:45]** everything your agents learn about your

**[16:47]** organization, your workflows, your

**[16:48]** decisions, your institutional knowledge

**[16:50]** lives inside Anthropic. If you switch

**[16:52]** providers, you're leaving your brain

**[16:54]** behind. If you built a solution that is

**[16:56]** a universal context layer, I've

**[16:58]** suggested this with open brain. There's

**[17:00]** lots of other ways to do it. Then the

**[17:02]** memory is yours and it it's exposed

**[17:04]** through an open protocol that any model

**[17:06]** can access. Funway's launch is going to

**[17:08]** test whether that matters enough to

**[17:10]** justify the setup cost or whether

**[17:12]** convenience is going to win. And I need

**[17:14]** to be honest, I think for a lot of

**[17:16]** companies, convenience is going to win.

**[17:17]** Enthropic and Google and OpenAI will

**[17:19]** make it easy. If you get an agent that

**[17:22]** just takes care of everything and it

**[17:24]** pulls you in and it's easy to onboard

**[17:26]** and you're already a Claude user and now

**[17:27]** you can use Conway and you wake up and

**[17:29]** it's just incredible from day one,

**[17:30]** you're not going to switch, right? Even

**[17:32]** if it's not perfect, even if it's

**[17:34]** learning what your VP needs to hear in

**[17:37]** that third email from the beginning of

**[17:38]** the video, you're still not going to

**[17:40]** switch because it's so good at

**[17:41]** everything else, it can be partially

**[17:44]** good and still so proactive, so

**[17:47]** memorable, so nuanced, so thoughtful,

**[17:50]** you won't move, you won't switch. And I

**[17:52]** have no illusions about that. I think

**[17:54]** that one of the things that we are going

**[17:56]** to see that is the whole game for the

**[17:58]** rest of 2026 is which companies and to

**[18:02]** some extent which individuals decide

**[18:04]** that they would rather own their own

**[18:06]** persistent memory layer regardless of

**[18:09]** the convenience of a particular launched

**[18:11]** agentic system versus which ones want to

**[18:14]** lean in and pick an agentic system and

**[18:17]** end up realizing they're locked in

**[18:19]** there. I think that story is already

**[18:21]** starting to take shape. I think we're

**[18:22]** starting to see the broader consumer

**[18:24]** base pick Chad GPT free or go plans.

**[18:26]** We're starting to see active

**[18:28]** professionals pick claude plans and

**[18:31]** that's starting to leak into enterprise

**[18:33]** contracts. And we are going to have to

**[18:35]** see whether concerns around portability

**[18:39]** and privacy shape enterprise deals and

**[18:42]** consumer choices or whether people are

**[18:44]** going to be comfortable with a product

**[18:46]** like Conway because Conway is just the

**[18:48]** tip of the iceberg. We are going to see

**[18:50]** Anthropic, OpenAI, and Google all ship

**[18:52]** versions of this in the next few months.

**[18:54]** We're going to have to see if people are

**[18:56]** comfortable staking the future of their

**[19:00]** careers on a lock in with a company. And

**[19:03]** I'm not overexaggerating. If you want to

**[19:05]** get promoted, increasingly, it will be a

**[19:07]** function of how well you use the

**[19:09]** persistent agent layer at your company,

**[19:11]** which requires your willingness to hop

**[19:13]** in and use it from day one. If you want

**[19:16]** to build a team, you're going to need to

**[19:17]** show that you can build that team from

**[19:20]** day one across a persistent context

**[19:24]** layer that the company decides. If you

**[19:26]** want to start a business, you are going

**[19:27]** to have to face the decision, which of

**[19:30]** these agentic interfaces do I choose?

**[19:32]** And in your own life, you're going to

**[19:34]** have to decide, do I want these agentic

**[19:35]** interfaces? Do I want to build my own?

**[19:37]** And enterprises will make that same

**[19:39]** choice. And there will be third parties

**[19:41]** who will claim to stitch together

**[19:43]** particular models and particular context

**[19:46]** layers into something that enterprises

**[19:47]** can choose and that is claimed to be

**[19:49]** portable. I am concerned that in the

**[19:52]** middle of all that mess, we are going to

**[19:54]** miss the larger point. We are going to

**[19:57]** miss the realization that the behavioral

**[19:59]** evidence of how we work should belong to

**[20:01]** us. It should be ours and that companies

**[20:05]** should be able to learn from it,

**[20:08]** leverage it while we work there with

**[20:10]** them and then we should be able to take

**[20:12]** it with us so that our persistent talent

**[20:17]** imprint on the context layer is not

**[20:19]** something they can just copy and

**[20:22]** continue to leverage after we depart.

**[20:24]** And so there's a sense in which my

**[20:26]** ability to handle a Slack message

**[20:28]** triage, my ability to read email and see

**[20:30]** what's important, my ability to

**[20:32]** understand whether a PowerPoint is well

**[20:35]** structured or not, that is becoming not

**[20:38]** just my talent, but a company's skill.

**[20:41]** And so I want us to have an intentional

**[20:43]** conversation because I understand this

**[20:45]** is very valuable to companies that when

**[20:47]** you have talent on your roster that can

**[20:49]** do this, that's incredibly worthwhile.

**[20:51]** You want to capture it. I get it. It's

**[20:53]** going to happen. But in that case, what

**[20:54]** is the right way to allocate that value

**[20:58]** back? Do you then say, "We're

**[20:59]** compensating the employee for using this

**[21:02]** behavioral evidence as a way to improve

**[21:06]** our context layer over time." Do you

**[21:09]** instead go with the approach that the

**[21:12]** context layer is portable and the

**[21:14]** employee should be able to take some

**[21:15]** sort of behavioral fingerprint out and

**[21:17]** some of the facts and the proprietary

**[21:19]** information should stay or and I think

**[21:22]** this is probably the most likely do we

**[21:24]** not have the conversation at all because

**[21:27]** it's a difficult conversation with weird

**[21:29]** power dynamics and instead we say you

**[21:31]** know what we're going to default to the

**[21:32]** old assumption whatever you do while you

**[21:35]** work is the company's property and that

**[21:37]** includes cludes your behavior at the

**[21:38]** company and if the company can learn a

**[21:40]** lot from that they're going to do that

**[21:42]** and they're going to move on. I think

**[21:43]** the latter is more likely but I think it

**[21:46]** poses some real challenges for

**[21:48]** employees. Ironically this approach as

**[21:51]** much as it empowers individuals and

**[21:53]** we've talked so much about how

**[21:55]** persistent context can give individuals

**[21:57]** and small team superpowers. The idea of

**[22:00]** a persistent context memory like this

**[22:02]** leaked Conway approach actually empowers

**[22:07]** enterprises in the employee relationship

**[22:09]** because the enterprise can look at this

**[22:12]** employee and say, "We know how good you

**[22:14]** are at this, this, this, and this. We

**[22:15]** know how to promote you. We know how to

**[22:17]** give you what you want to stay, but also

**[22:20]** we know that you're effective because of

**[22:22]** this agent and you're going to want to

**[22:24]** stay because when you work with this

**[22:27]** agent, you're 2x more effective and we

**[22:28]** can prove it. And we have never had that

**[22:30]** kind of carrot and stick approach

**[22:32]** employers to employees and we're all

**[22:34]** going to figure that out. As you look at

**[22:36]** the Claude code leaks, as you look at

**[22:38]** Conway, as you look at other leaks that

**[22:40]** come out, please start to think through

**[22:43]** what are the larger implications here?

**[22:45]** What are the non-obvious implications of

**[22:47]** extending agents into our lives in ways

**[22:50]** that are persistent? I hope this video

**[22:52]** has given you a sense of the different

**[22:55]** ways that this can unfold. And if you're

**[22:59]** interested in building a persistent

**[23:01]** memory layer, you know, I have a way to

**[23:03]** do that and it can be yours and you can

**[23:05]** have a behavioral audit that you take

**[23:07]** with you because I think that's really

**[23:08]** important. I have no illusions. We are

**[23:11]** going to be at a point in many cases

**[23:12]** where that's not an option because

**[23:14]** employers are going to hold the cards

**[23:16]** and they're going to encourage employees

**[23:18]** either through carrots or through sticks

**[23:20]** to participate in these proprietary

**[23:22]** contextual platforms in ways that enable

**[23:26]** the employer to leverage the collective

**[23:30]** intelligence of teams to make those

**[23:32]** agents better and stronger and not even

**[23:34]** necessarily for nefarious purposes. Like

**[23:36]** the easy narrative is, oh, then they're

**[23:37]** going to fire everybody. I don't think

**[23:38]** that's true because you still have to

**[23:40]** have a lot of smart humans to manage

**[23:41]** these agents. But it does mean that the

**[23:44]** lockin effect for employees inside

**[23:46]** employers is going to get very strong in

**[23:48]** the second half of 2026. So pick your

**[23:50]** fighter carefully, right? Choose your

**[23:51]** employer carefully because increasingly

**[23:54]** choosing your employer is going to mean

**[23:56]** who are you choosing to work with as a

**[23:59]** persistent agent. Are you working with a

**[24:00]** claude company or a Chad JPT company? It

**[24:03]** used to be Windows and Mac, right? Well,

**[24:04]** this is more important than that. Now,

**[24:06]** it's are you working with an agent that

**[24:09]** understands you and that you're super

**[24:11]** familiar with and that you can be two or

**[24:13]** three more productive with because

**[24:15]** you've had that time. That's the future

**[24:16]** that Conway is pointing at. And I want

**[24:18]** us to understand that because it's easy

**[24:20]** to get lost in the open claw fiasco. But

**[24:22]** I want you to understand underneath that

**[24:24]** why Anthropic is making the moves that

**[24:26]** they are and where they're going with

**[24:28]** the persistent agent layer because

**[24:30]** that's also where OpenAI and Google are

**[24:32]** going too. Best of luck out there.
