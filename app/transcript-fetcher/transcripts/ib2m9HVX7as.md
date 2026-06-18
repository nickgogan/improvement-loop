# Transcript: ib2m9HVX7as

**URL:** https://www.youtube.com/watch?v=ib2m9HVX7as
**Segments:** 776

---

## Full Text

All of the AI app builders like lovable and replet are now pivoting desperately to open claw to maintain relevance. But I don't think that's the real story. I think there's a much more interesting story if you are in the app builder space that we're not covering and it has to do with the future of the web as a whole. Essentially the question is are there any spaces in the web builder landscape? Are there any spaces in between the model makers and the people that are safe to build in right now where the model makers won't just make a better model and take the space? And this is highly relevant because if your name is not Anthropic or OpenAI or Google, you got to find a space somewhere if you want to build something. And this goes not just for the big companies like lovable, but for little guys who are trying to build a software business on the web. How do you build something where you have some degree of confidence you're building in a niche that open claw plus open AI plus anthropic are not going to immediately disrupt and make all of your work worthless. This video is about the five things that AI cannot replace and why they're the future of the web. And I want to think about it strategically with you because if we really understand these five basics, I think we're going to understand the principles around which the future of the web is organized. and we're going to see niches that are buildable that the big players can't grab. And so I've spent the last few weeks digging into the AI app builder landscape, the companies that turn a chat prompt into a deployed application, right? And the picture that's emerging is really much much broader than what those companies say it is. And so let's go there, right? Let's look at what these app builder companies tell us about what the future of the web looks like. Now, they're not setting out to do that, right? They're setting out to compete. They're setting out to put open claw on the table. They're setting out to grow their ARR and justify their valuations as hard as they can. And that's their job. That's what they should be doing. But along the way, we can learn from them. And the first thing I want to tell you about before we get to these five basics for the web is the collapse of the build layer itself. What these guys are all fighting for that felt like it was so big and so open-ended just a few months ago. And so what's happening right now is that there are at least a dozen companies that are racing to build a platform where you describe an app and it magically appears. Lovable just raised $330 million at a $6.6 billion valuation. They're at a $300 million plus recurring revenue run rate and they're growing really fast. They have over a hund,000 new projects created on their platform. Not every month, not every year, every day. That's right, 100,000 every day. Now compared to Lovable, everybody else is tiny. Verscel's V0 has 4 million users. Replet has roughly 25 million developers on the platform at last count. Bolt, shipper, base 44, these are all smaller players in the space. And there's a real longtail that's fighting over essentially the same pitch. You tell your idea to AI and AI will build it for you. Since OpenClaw has come on the scene, that has really evolved into don't just tell us your idea and we'll build your app, but tell us your idea and we will use OpenClaw like capabilities to build your entire business for you. And really, everyone's screaming down the same lane here and most of them end up being functionally very thin rappers with very little differentiation around the same base models, either Claude or Chad GPT or Gemini. or maybe if they want to constrain their token cost they're using something like Kimmy or a Quen architecture on the back end so they have that open- source model foundation they try to differentiate on pitch on UI on pricing and some of them have different flavors right one has an AI advisor one has a visual editor you get the idea right all of them have slightly different twists but I want you to think strategically with me and look underneath and see they're all basically the same and this brings up a really obvious question right if this was considered safe as recently as last year and now it's not what does that mean for the future of the web when Your product is a UI layer on top of someone else's intelligence. Your moat is as deep as the time it takes to replicate the UI, which now that cloud code is around, now that CodeEx is around, takes like a week or less. Like it's not that long. Now, the conventional wisdom is that you escape this trap by training your own model. That is exactly what cursor did on the code side and they're training their own model to compete for time and tokens with developers. And Replet is actually taking this exact approach. They've trained their own code completion models using data bricks. They've released open- source versions on hugging face and they're using them for inline suggestions where cost efficiency matters a lot. Lovable at $300 million ARR certainly has the cash to try that same play. Versel trained a custom autofix model with Fireworks AI that catches code generation errors during streaming and they just updated their terms of service to start using customer code for model training. But training your own model isn't actually what separates the survivors from the casualties. The companies that are going to make it through this middleware trap share a very different trait. They own something structural that the model providers cannot replicate. And that gets me to what is persistent about the web that the AI model builders can't replicate. So replet doesn't escape because they outrain anthropic on models. I don't think you're going to do that. Instead, they escape because Claude can't execute your code. Replet owns the runtime, the actual compute environment where your application lives and breathes. That is a different value proposition than we call an API and show you the output. Bracell doesn't escape because Vzero uses a slightly better system prompt. They escape because nobody else has the deployment infrastructure that already hosts production applications for OpenAI, for Anthropic, for Nike, for PayPal, and a host of others. They're not an AI rapper with hosting. They're actually an infrastructure company that happens to have built an AI front door recently. Notion doesn't often get lumped in with these builders, but arguably it's in a somewhat similar category since you are building on top of an AI model with their AI agent, which they did not train themselves. And Notion doesn't even pretend it wants to train an AI model. They offer a model picker. You can transparently choose Chad GPT or Claude or Gemini. Take your pick. And their bet is completely different. Essentially, they're saying, "We don't care which model wins. We care that a 100 million users have built the largest structured knowledge graph of organizational information on the planet and every model needs to come to us to access that information. There's a pattern across all of these winning builds. The pattern is this. The AI commoditizes production. The companies that survive are the ones that are building on the layers that production can't replace. Which raises that larger question. If building things is essentially going to be free, what is actually worth building a company around? I'm going to suggest to you that I think the web organizes itself around five durable verticals of value that persist that AI structurally cannot provide on its own. These are not product categories, right? These are bigger. They're layers of value that persist regardless of how good the models get. And it's difficult for any one company to completely own a vertical of value like this. The agentic economy that's emerging is going to make each of them more important, not less. And so what are these five verticals of value? Well, number one is trust. The web is about to be flooded. In fact, by most measures, it's already being flooded. We're headed toward a world where there are millions of AI generated apps, services, storefronts, content streams that are created every single day. Most of them will be absolutely indistinguishable from each other. Most of them will be garbage, quite frankly. And some of them may be actively malicious. When anyone can generate a professionallook checkout page in a couple of seconds, just because it looks legitimate doesn't mean it's serious. In fact, it might be trying to steal your information. The companies that become the verification layer, the ones who tell you that this app will not steal your credit card and we will back it up. That this service actually does what it claims and we will back it up. That this content was produced by someone real and who can be held accountable. Those companies capture a tremendous amount of value. This is why Stripe's position keeps getting stronger not weaker in an AI saturated web because powered by Stripe that's not actually a technical because powered by Stripe is not actually a technical feature set trust signal at this point when you process over a trillion dollars in transactions. You become a trusted layer on the web. Same for Shopify. Same for Apple's app store review process. Same for Verscell's deployment infrastructure. In the agentic economy, trust becomes much more critical than it was in the human economy because the proliferation of noise is exponential. When your AI agent is autonomously transacting on your behalf, maybe they're booking their flights, maybe they're going to be signing up for services or making purchases, the trust layer is all that is standing between you and a universe of AI generated scams. The agents themselves are going to need trust signals to be able to operate successfully. Which payments are safe? which services are verified, which APIs are not going to just steal all your data. The trust providers in this world become the routing layer for responsible web traffic. If an agent cannot verify a service in this new world, it's not only not going to transact on it, it likely will not even use it and in many cases won't be allowed to use it. Trust becomes a walled garden for the web as a whole. And it's not going to be one player. I've already mentioned multiple big names that are playing in the trust space. there's going to be a hedge of major players in the trust space that collectively work together to start to secure our agentic future. And that is something an LLM cannot replicate. Okay. Number two after trust is context. The most valuable thing on the internet right now, it's not compute. It's not even your intent and your ability to prompt. It's your specific situation. It's your company's data. It's your customer relationships. Maybe it's your medical records. It's your meeting notes from last Tuesday. Right? The AI is a general application tool. to be useful, it needs that kind of specific data unique to your situation. The companies that become the authoritative store for context and the permissioning layer that governs where that context gets served, they own the choke point on the internet. Every agent, every model, every workflow is going to have to flow through that context layer. Now, Notion understands this at a very deep level. They've built custom agents and they took off immediately. We're into the tens of thousands or hundreds of thousands of custom agents built by users on Notion now. And those run autonomously across each individual person's workspace or context layer. And critically and critically, the context is what makes those agents valuable. In a sense, what notion did is not recognize that AI is powerful. All notion did is recognize that their context is a secret sauce and that they need to bring any old AI into it to make it super powerful for users. And that's what they decided to do. This is exactly the same structural data play that makes Salesforce durable, that makes Epic durable in the health space, that makes Plantier durable in the security space. When AI agents become the primary way work gets done, the way agents get information becomes a source of revenue and a source of dependable competitive advantage. An agent without context is just going to be a chatbot, but an agent that has your context can be a dependable junior employee. And it really is that big a difference. And you can see it for yourself if you prompt correctly. Because correct prompting increasingly is about here's my context. Here's where to go search for more context. Are we good? Right? And then it goes off and does its thing. Now, if you want to look at who's playing in this space, it's interesting to use this angle because you see some players that are not typically put together, but who are all playing in the context space. So, Notion, I mentioned, Salesforce, I mentioned, Epic, I mentioned, Palanteer, also Snowflake and Data Bricks, potentially even Apple and Google if they can nail local AI as well as they want to. You notice that Google recently launched essentially a context layer for maps. They're thinking about this too, and it continues to highlight for me how Google pops up with so many ways to win the AI race. They're not just a model player. They're a foundation player with TPUs. They're a context player. They're an ecosystem player. or they're a devices player, they have got a lot of ways to win on this board. So, we talked about trust, we talked about context. Number three is distribution. You can generate an app in seconds, but who's going to see it? And this is something, by the way, that second time founders know that first- time founders don't. The bottleneck was never about building the thing. It was always about distributing it. Now, in Field of Dreams, the movie, you build it and they will come. That is never ever ever how it works. It is always you build it and then you have to go round people up and get them to come and see if this is what they want and see if they'll pay for it. Distribution has always been king. But what we see in a world where you have a 10x or 100x multiple in the amount of software, the amount of product being generated digitally, you have to have an edge in distribution to be heard or seen or get any signal from customers whatsoever. In other words, when supply is infinite, curation is about to become the scarcest resource in the world. So this is a place where Google plays, Apple's app store plays, Tik Tok plays a role, YouTube plays a role. These are all distribution monopolies in a sense and AI makes them more powerful not less. The gatekeepers get stronger when the flood is bigger because they tell people where to go. So for the agentic economy, this means something very specific. Agent discovery is a massive problem. If every business has AI agents, who is going to help those agents discover where they need to go to do business with one another and with humans? So, there's a new distribution layer that's starting to emerge and it's all about how agents discover what they need to do business on the internet and who they need to do business with. Now, this is actually bullish for content creators because it means that if you are able to establish yourself with a particular niche in AI as an authority, people are going to be able to use you to help get useful information and useful signal on artificial intelligence that they would otherwise not be able to get. But, and this is discussed much less, there is also an opening emerging for an agentic store discovery mechanism. We need something like an agentnative app store that allows agents to start to find and utilize utilities or utilize businesses that are agent-friendly to do business with. And this is a big emerging category. I've spent some previous videos talking about it. I'll be talking about it more in future. I think the question of what makes a business viable for an agent to transact with is one of the most interesting questions of 2026 because it's a whole lot more than putting an MCP server out there. You have to think about how fast the transaction works, how easy it is for the agent to understand the depth of what you offer, how quick it is for the agent to make a selection and operate with your API or whatever you're working with, and how simple it is for the agent to receive the good or service. all of these things and essentially the entire mechanism for commerce has to be rethought with agents at the core and I got to be honest with you almost no businesses are thinking like this if you had to pick big businesses that are trying to play in this space I would guess Google for search and discovery I would guess Apple and Google when you're talking about app stores I would guess Tik Tok YouTube Substack if you're in the content space and I would guess Amazon if you're looking at the commerce side but those are all guesses right I'm not saying all of those have clear agenda IC plays right now. I'm saying all of them have an interesting position to play and they may play those cards. And I am saying if they don't, they are liable to disruption. Okay. So, we've talked about trust, we've talked about context, we've talked about distribution. Now, we're going to talk about taste. It's such an ambiguous word, but we're going to get into why it matters and why it should be considered a separate vertical, not just a personal quality, right? A separate vertical on the web. The bottom line is this. When producing software is free, what you choose to produce becomes the entire game. So this means the way you think about your product decisions, your design sensibility, your editorial judgment about what is worth building and what is not. Your ability to look at what AI generated and know that it's right or know that it's wrong and be accountable for it. This is a human skill that you know AI can assist with, but it's not going to replace it. But because it requires a point of view on how humans do business with humans. Essentially, taste is a conviction about what should exist in the world that is not easily derivable from training data. The best analogy for this, I think, is music production. After Apple's Garage Band went mainstream, the tools got very cheap. Everyone can make a track. The flood of music was enormous. And this is even more the case now that Sunno is going online and people can use a tool to generate an entire AI music track in seconds. The producers and artists who thrive in this world, and there are people who thrive even in the Sunno world, they're not the ones with the most expensive studio anymore because production is essentially free. They're the ones with taste. They have an idea for what is going to work with the audience. They have an ear for how music might play in a variety of settings and they choose to produce something that is going to connect with the audience. The same thing is about to happen to software. So, the vibe coder who ships an app in just a few minutes hasn't done the hard part yet because they haven't figured out how is what I'm building going to deeply connect with my audience. And so, this could be expressed as design or it could be expressed just as absolutely nailing the angle of the value proposition. And in practice, what I see is the best products are both of those. They have a strong design sense and they also have a very clear, accurate, correct value proposition that resonates with a felt need the audience has. Now, if you have to pick one, famously, you stick with the value proposition one. And that's why we see so few designled companies. But both are going to be powerful rocket engines for human-led companies that achieve product market fit in the next few years. I'm going to go further though. We've talked about humanto human transactions, human commerce, and taste. Let's look at the agentic web. What does taste look like on the agentic web? I would argue it looks like orchestration quality. So, the winning agent systems won't necessarily be the ones with the best underlying models. They'll be the ones where a human with deep domain expertise has carefully tuned the prompts and designed the workflows and chosen the right tools and made a thousand small editorial decisions about how the agent should behave so that the agent as a whole is a curated experience that does powerful work. Now, I'm the first person to say that that trend may evolve over time. In particular, as we start to see auto research become something that is applied to agentic harnesses, there may be cases where agents start to self- evvolve. There may be cases where agents start to be intentionally automatically evolved by humans who are supervising the process. But the end responsibility of the human to look at an agentic product in the agentic economy and say this is the direction I want this agent to go in. this is the goal I have. This is what good looks like. That's not changing. It's not changing. And I think that we need to be honest about that. And we need to recognize that regardless of how far above the loop the human sits, the human remains accountable to what the agent is going to be doing and to how the agent participates in this larger economy. And so I don't see us abdicating taste even if we have more powerful tools like auto research that we can put in the toolkit. Number five is the least fun. Liability. Someone is going to have to be on the hook. And it's a place where you can build a powerful business. When an AI generated financial plan loses you money, who's liable? When an AI built medical app gives bad advice, who's liable? When an AI generated contract becomes something that you litigate and lose over, who's liable for that bad clause in the contract? And the AI did it is not going to be an answer that survives court. Regulated industries like healthcare, like finance, like legal, like insurance. Essentially, the niches they build on are liability niches because the professionals in these spaces, even if they're building and using agentic systems, are doing so around the core notion that they are selling accountability. That's part of how lawyers stay in business, right? Lawyers stay in business because they sell accountability before the court for how a particular case is represented. And here's the counterintuitive dynamic. The better AI gets at representing itself and talking about itself and messaging, the more important authentic accountability and liability management becomes because the mistakes that you can make with a plausible sounding AI get much much more serious. In the agentic economy, liability effectively becomes a governance layer you have to manage. You have to look at liability and say, how are we constraining and managing liability? What companies do we need to work with that specialize in agent liability? Because AI agents are going to be autonomously executing complicated workflows for you. They'll be filing documents. They may in the future be moving money for you. They may be making commitments with your name on them. Someone needs to define those boundaries, audit those actions, and ultimately be liable for that choice. The companies and the professionals who position themselves as liability guaranurs or as accountability makers in this space get to own the governance layer for the future web. Now there's an odd collection of companies in this space. I think this one is liable to grow pretty quickly. Right now Deote and McKenzie are starting to reposition themselves a little bit as AI assurance providers. 11 Labs has been in the space offering insurance for voice agents. There are also regulated SAS platforms like Viva and Elation that are in this space and really a lot of AI professionals who focus on providing safety and vetting protocols for agents. They're effectively in this space. And so this is one where you have like a real patchwork. You can have scaled up consulting firms doing billions in revenue and you can also have small mom and pop shops that are focused on this space and they're all in the business of making agents safer to run and handling the liability layer. So what does the web look like when you put all these layers together? If we step back, what is the future of the web? I would argue that the model providers like OpenAI and Anthropic are increasingly positioned to own the bedrock intelligence capability layer for the future of the web. I don't think anyone would disagree there, right? They're enormously valuable and they're increasingly commoditized relative to each other. And if we get to a point where we have open- source models, those open- source models are going to likely be a derivation of the lineages from those core model makers. And so in a sense, the influence of those model makers will live on regardless. The rapper companies like lovable, like Bolt, like Shipper, they don't own anything durable inherent. Some are going to get acquired. To be honest, most of them are going to die. and a few the ones that manage to accumulate enough user information, enough data, enough momentum. I think lovable is a great candidate here. They're going to have a shot at becoming a platform, not just a rapper. And that's absolutely the play lovable making. It wants to be effectively Shopify 2.0. I think the platform where the business of the future is done. Infrastructure players like Verscell and Replet and Stripe and Shopify, those are the ones that own the trust and execution layers of the future web. AI makes them valuable because more things are being built which requires more trust, more verification, more payments etc. So they end up being the picks and shovels of the AI gold rush and their position ends up being very very durable. Meanwhile the context owners like notion, like Salesforce, like Snowflake, like data bricks, they own the data gravity, right? The agents need context to be useful and context ends up getting locked inside those platforms and they become the permissioning layer for the agentic economy if they play their cards right. the distribution gatekeepers like Google, like Amazon, like Apple, they own how you pay attention to things on the internet. And if they play their cards right, they also own how agents pay attention on the internet. And that's going to be something that's very interesting to watch over the next year or two. And finally, us humans, right? The operators, we're founders, we're professionals, we're people, we're householders, we have taste, we have judgment, we have accountability, we provide the connective tissue that makes all of this work. And so AI doesn't necessarily replace the things we bring to the table, but understanding the structure of how the web will work allows us to be above the loop where all these agents are operating, understand what's going on, and provide our perspective and our direction in a way that's useful and strategic. So what does this mean? If you are in the space and you are thinking about building, if you're in the space, maybe you own a business, maybe you run a business, maybe you're building as a side project, whatever it is, ask yourself, what do I own that still matters if AI gets 10 times better? If the answer is nothing, if a better model just makes your product obsolete, you should change your positioning now because you should be assuming that the models will get better. Now, if a better model makes your product more valuable, like if you own a piece of the trust layer or if you own a piece of the liability layer or if you're playing into the agentic economy and you want smarter agents to actually enable that economy to work well, now you're more in business and now you have something you can build on and you don't have to go to sleep at night worrying about how good the next claude model's going to be. Spoiler alert, I think they're not kidding. I think it's going to be really good. And one last word of warning to all of us who are building in this economy. We have put so much work into productionalizing code. We need to keep thinking about distribution. I mentioned it as number three in my list of big pieces for the web. If you build an MVP in a day, that's great. Your job is actually to put it in front of customers, get customer feedback, and validate that you are building something customers want. That is a very human activity. And as much as we can start to scale voice of customer when we have lots of customers to work with, we still need to own and be accountable for whether the product resonated with the customer in a way that's useful. There is no substitute for distribution. And I wish that all of the focus and all of the energy that tools like Lovable and Replet have generated around creation got piped a little bit into the distribution side because what I see right now is a 100,000 a million 10 million apps blooming and most of them are never going to get discovered because no one ever put the thought into whether or not someone really wants this product. And that's not a new lesson. None of that changed. It just matters more now. In fact, that is the larger takeaway. The five things I called out, trust, context, distribution, liability, taste, those are things that have always mattered on the web. And what we're seeing is that AI is essentially a forcing function that makes them matter more now. And AI cannot take their place. And that is why they're durable places to build in the future of the agentic economy. Good luck building.

---

## Timestamped Segments

**[0:00]** All of the AI app builders like lovable

**[0:01]** and replet are now pivoting desperately

**[0:03]** to open claw to maintain relevance. But

**[0:06]** I don't think that's the real story. I

**[0:07]** think there's a much more interesting

**[0:09]** story if you are in the app builder

**[0:11]** space that we're not covering and it has

**[0:13]** to do with the future of the web as a

**[0:14]** whole. Essentially the question is are

**[0:18]** there any spaces in the web builder

**[0:21]** landscape? Are there any spaces in

**[0:24]** between the model makers and the people

**[0:26]** that are safe to build in right now

**[0:28]** where the model makers won't just make a

**[0:30]** better model and take the space? And

**[0:32]** this is highly relevant because if your

**[0:33]** name is not Anthropic or OpenAI or

**[0:35]** Google, you got to find a space

**[0:37]** somewhere if you want to build

**[0:38]** something. And this goes not just for

**[0:40]** the big companies like lovable, but for

**[0:42]** little guys who are trying to build a

**[0:43]** software business on the web. How do you

**[0:45]** build something where you have some

**[0:46]** degree of confidence you're building in

**[0:48]** a niche that open claw plus open AI plus

**[0:52]** anthropic are not going to immediately

**[0:53]** disrupt and make all of your work

**[0:55]** worthless. This video is about the five

**[0:58]** things that AI cannot replace and why

**[1:01]** they're the future of the web. And I

**[1:03]** want to think about it strategically

**[1:04]** with you because if we really understand

**[1:06]** these five basics, I think we're going

**[1:08]** to understand the principles around

**[1:10]** which the future of the web is

**[1:11]** organized. and we're going to see niches

**[1:14]** that are buildable that the big players

**[1:17]** can't grab. And so I've spent the last

**[1:19]** few weeks digging into the AI app

**[1:21]** builder landscape, the companies that

**[1:22]** turn a chat prompt into a deployed

**[1:24]** application, right? And the picture

**[1:26]** that's emerging is really much much

**[1:28]** broader than what those companies say it

**[1:30]** is. And so let's go there, right? Let's

**[1:32]** look at what these app builder companies

**[1:35]** tell us about what the future of the web

**[1:37]** looks like. Now, they're not setting out

**[1:38]** to do that, right? They're setting out

**[1:39]** to compete. They're setting out to put

**[1:41]** open claw on the table. They're setting

**[1:42]** out to grow their ARR and justify their

**[1:44]** valuations as hard as they can. And

**[1:46]** that's their job. That's what they

**[1:47]** should be doing. But along the way, we

**[1:49]** can learn from them. And the first thing

**[1:51]** I want to tell you about before we get

**[1:52]** to these five basics for the web is the

**[1:55]** collapse of the build layer itself. What

**[1:57]** these guys are all fighting for that

**[1:59]** felt like it was so big and so

**[2:01]** open-ended just a few months ago. And so

**[2:03]** what's happening right now is that there

**[2:05]** are at least a dozen companies that are

**[2:06]** racing to build a platform where you

**[2:08]** describe an app and it magically

**[2:10]** appears. Lovable just raised $330

**[2:13]** million at a $6.6 billion valuation.

**[2:16]** They're at a $300 million plus recurring

**[2:17]** revenue run rate and they're growing

**[2:19]** really fast. They have over a hund,000

**[2:21]** new projects created on their platform.

**[2:24]** Not every month, not every year, every

**[2:26]** day. That's right, 100,000 every day.

**[2:28]** Now compared to Lovable, everybody else

**[2:30]** is tiny. Verscel's V0 has 4 million

**[2:33]** users. Replet has roughly 25 million

**[2:35]** developers on the platform at last

**[2:37]** count. Bolt, shipper, base 44, these are

**[2:40]** all smaller players in the space. And

**[2:42]** there's a real longtail that's fighting

**[2:44]** over essentially the same pitch. You

**[2:46]** tell your idea to AI and AI will build

**[2:48]** it for you. Since OpenClaw has come on

**[2:51]** the scene, that has really evolved into

**[2:53]** don't just tell us your idea and we'll

**[2:55]** build your app, but tell us your idea

**[2:57]** and we will use OpenClaw like

**[2:59]** capabilities to build your entire

**[3:03]** business for you. And really, everyone's

**[3:05]** screaming down the same lane here and

**[3:07]** most of them end up being functionally

**[3:09]** very thin rappers with very little

**[3:11]** differentiation around the same base

**[3:13]** models, either Claude or Chad GPT or

**[3:16]** Gemini. or maybe if they want to

**[3:17]** constrain their token cost they're using

**[3:19]** something like Kimmy or a Quen

**[3:20]** architecture on the back end so they

**[3:21]** have that open- source model foundation

**[3:23]** they try to differentiate on pitch on UI

**[3:25]** on pricing and some of them have

**[3:26]** different flavors right one has an AI

**[3:28]** advisor one has a visual editor you get

**[3:30]** the idea right all of them have slightly

**[3:32]** different twists but I want you to think

**[3:34]** strategically with me and look

**[3:35]** underneath and see they're all basically

**[3:37]** the same and this brings up a really

**[3:38]** obvious question right if this was

**[3:40]** considered safe as recently as last year

**[3:42]** and now it's not what does that mean for

**[3:44]** the future of the web when Your product

**[3:46]** is a UI layer on top of someone else's

**[3:49]** intelligence. Your moat is as deep as

**[3:52]** the time it takes to replicate the UI,

**[3:55]** which now that cloud code is around, now

**[3:57]** that CodeEx is around, takes like a week

**[3:59]** or less. Like it's not that long. Now,

**[4:01]** the conventional wisdom is that you

**[4:03]** escape this trap by training your own

**[4:05]** model. That is exactly what cursor did

**[4:07]** on the code side and they're training

**[4:08]** their own model to compete for time and

**[4:12]** tokens with developers. And Replet is

**[4:14]** actually taking this exact approach.

**[4:16]** They've trained their own code

**[4:17]** completion models using data bricks.

**[4:19]** They've released open- source versions

**[4:20]** on hugging face and they're using them

**[4:22]** for inline suggestions where cost

**[4:24]** efficiency matters a lot. Lovable at

**[4:26]** $300 million ARR certainly has the cash

**[4:29]** to try that same play. Versel trained a

**[4:32]** custom autofix model with Fireworks AI

**[4:34]** that catches code generation errors

**[4:35]** during streaming and they just updated

**[4:38]** their terms of service to start using

**[4:39]** customer code for model training. But

**[4:42]** training your own model isn't actually

**[4:44]** what separates the survivors from the

**[4:46]** casualties. The companies that are going

**[4:48]** to make it through this middleware trap

**[4:51]** share a very different trait. They own

**[4:53]** something structural that the model

**[4:55]** providers cannot replicate. And that

**[4:57]** gets me to what is persistent about the

**[5:00]** web that the AI model builders can't

**[5:03]** replicate. So replet doesn't escape

**[5:05]** because they outrain anthropic on

**[5:07]** models. I don't think you're going to do

**[5:08]** that. Instead, they escape because

**[5:11]** Claude can't execute your code. Replet

**[5:14]** owns the runtime, the actual compute

**[5:17]** environment where your application lives

**[5:19]** and breathes. That is a different value

**[5:22]** proposition than we call an API and show

**[5:24]** you the output. Bracell doesn't escape

**[5:25]** because Vzero uses a slightly better

**[5:27]** system prompt. They escape because

**[5:29]** nobody else has the deployment

**[5:31]** infrastructure that already hosts

**[5:33]** production applications for OpenAI, for

**[5:35]** Anthropic, for Nike, for PayPal, and a

**[5:37]** host of others. They're not an AI rapper

**[5:39]** with hosting. They're actually an

**[5:40]** infrastructure company that happens to

**[5:42]** have built an AI front door recently.

**[5:44]** Notion doesn't often get lumped in with

**[5:45]** these builders, but arguably it's in a

**[5:47]** somewhat similar category since you are

**[5:49]** building on top of an AI model with

**[5:51]** their AI agent, which they did not train

**[5:53]** themselves. And Notion doesn't even

**[5:54]** pretend it wants to train an AI model.

**[5:56]** They offer a model picker. You can

**[5:58]** transparently choose Chad GPT or Claude

**[6:00]** or Gemini. Take your pick. And their bet

**[6:02]** is completely different. Essentially,

**[6:04]** they're saying, "We don't care which

**[6:06]** model wins. We care that a 100 million

**[6:08]** users have built the largest structured

**[6:10]** knowledge graph of organizational

**[6:12]** information on the planet and every

**[6:14]** model needs to come to us to access that

**[6:16]** information. There's a pattern across

**[6:18]** all of these winning builds. The pattern

**[6:20]** is this. The AI commoditizes production.

**[6:24]** The companies that survive are the ones

**[6:26]** that are building on the layers that

**[6:27]** production can't replace. Which raises

**[6:29]** that larger question. If building things

**[6:31]** is essentially going to be free, what is

**[6:34]** actually worth building a company

**[6:35]** around? I'm going to suggest to you that

**[6:37]** I think the web organizes itself around

**[6:40]** five durable verticals of value that

**[6:43]** persist that AI structurally cannot

**[6:46]** provide on its own. These are not

**[6:48]** product categories, right? These are

**[6:49]** bigger. They're layers of value that

**[6:51]** persist regardless of how good the

**[6:53]** models get. And it's difficult for any

**[6:56]** one company to completely own a vertical

**[6:59]** of value like this. The agentic economy

**[7:01]** that's emerging is going to make each of

**[7:03]** them more important, not less. And so

**[7:05]** what are these five verticals of value?

**[7:07]** Well, number one is trust. The web is

**[7:10]** about to be flooded. In fact, by most

**[7:12]** measures, it's already being flooded.

**[7:14]** We're headed toward a world where there

**[7:15]** are millions of AI generated apps,

**[7:18]** services, storefronts, content streams

**[7:20]** that are created every single day. Most

**[7:22]** of them will be absolutely

**[7:24]** indistinguishable from each other. Most

**[7:26]** of them will be garbage, quite frankly.

**[7:28]** And some of them may be actively

**[7:29]** malicious. When anyone can generate a

**[7:31]** professionallook checkout page in a

**[7:33]** couple of seconds, just because it looks

**[7:34]** legitimate doesn't mean it's serious. In

**[7:36]** fact, it might be trying to steal your

**[7:38]** information. The companies that become

**[7:39]** the verification layer, the ones who

**[7:42]** tell you that this app will not steal

**[7:43]** your credit card and we will back it up.

**[7:45]** That this service actually does what it

**[7:47]** claims and we will back it up. That this

**[7:48]** content was produced by someone real and

**[7:50]** who can be held accountable. Those

**[7:52]** companies capture a tremendous amount of

**[7:54]** value. This is why Stripe's position

**[7:56]** keeps getting stronger not weaker in an

**[7:58]** AI saturated web because powered by

**[8:00]** Stripe that's not actually a technical

**[8:02]** because powered by Stripe is not

**[8:03]** actually a technical feature set trust

**[8:05]** signal at this point when you process

**[8:07]** over a trillion dollars in transactions.

**[8:09]** You become a trusted layer on the web.

**[8:12]** Same for Shopify. Same for Apple's app

**[8:14]** store review process. Same for

**[8:16]** Verscell's deployment infrastructure. In

**[8:18]** the agentic economy, trust becomes much

**[8:21]** more critical than it was in the human

**[8:23]** economy because the proliferation of

**[8:25]** noise is exponential. When your AI agent

**[8:28]** is autonomously transacting on your

**[8:30]** behalf, maybe they're booking their

**[8:31]** flights, maybe they're going to be

**[8:32]** signing up for services or making

**[8:34]** purchases, the trust layer is all that

**[8:37]** is standing between you and a universe

**[8:39]** of AI generated scams. The agents

**[8:41]** themselves are going to need trust

**[8:43]** signals to be able to operate

**[8:44]** successfully. Which payments are safe?

**[8:46]** which services are verified, which APIs

**[8:49]** are not going to just steal all your

**[8:50]** data. The trust providers in this world

**[8:52]** become the routing layer for responsible

**[8:55]** web traffic. If an agent cannot verify a

**[8:57]** service in this new world, it's not only

**[8:58]** not going to transact on it, it likely

**[9:00]** will not even use it and in many cases

**[9:02]** won't be allowed to use it. Trust

**[9:05]** becomes a walled garden for the web as a

**[9:08]** whole. And it's not going to be one

**[9:10]** player. I've already mentioned multiple

**[9:11]** big names that are playing in the trust

**[9:13]** space. there's going to be a hedge of

**[9:15]** major players in the trust space that

**[9:16]** collectively work together to start to

**[9:18]** secure our agentic future. And that is

**[9:20]** something an LLM cannot replicate. Okay.

**[9:23]** Number two after trust is context. The

**[9:26]** most valuable thing on the internet

**[9:28]** right now, it's not compute. It's not

**[9:29]** even your intent and your ability to

**[9:31]** prompt. It's your specific situation.

**[9:32]** It's your company's data. It's your

**[9:34]** customer relationships. Maybe it's your

**[9:35]** medical records. It's your meeting notes

**[9:37]** from last Tuesday. Right? The AI is a

**[9:40]** general application tool. to be useful,

**[9:43]** it needs that kind of specific data

**[9:45]** unique to your situation. The companies

**[9:48]** that become the authoritative store for

**[9:50]** context and the permissioning layer that

**[9:52]** governs where that context gets served,

**[9:55]** they own the choke point on the

**[9:57]** internet. Every agent, every model,

**[9:58]** every workflow is going to have to flow

**[10:00]** through that context layer. Now, Notion

**[10:02]** understands this at a very deep level.

**[10:03]** They've built custom agents and they

**[10:05]** took off immediately. We're into the

**[10:06]** tens of thousands or hundreds of

**[10:08]** thousands of custom agents built by

**[10:10]** users on Notion now. And those run

**[10:12]** autonomously across each individual

**[10:15]** person's workspace or context layer. And

**[10:17]** critically and critically, the context

**[10:19]** is what makes those agents valuable. In

**[10:20]** a sense, what notion did is not

**[10:22]** recognize that AI is powerful. All

**[10:24]** notion did is recognize that their

**[10:26]** context is a secret sauce and that they

**[10:28]** need to bring any old AI into it to make

**[10:31]** it super powerful for users. And that's

**[10:33]** what they decided to do. This is exactly

**[10:35]** the same structural data play that makes

**[10:38]** Salesforce durable, that makes Epic

**[10:40]** durable in the health space, that makes

**[10:42]** Plantier durable in the security space.

**[10:44]** When AI agents become the primary way

**[10:47]** work gets done, the way agents get

**[10:50]** information becomes a source of revenue

**[10:53]** and a source of dependable competitive

**[10:56]** advantage. An agent without context is

**[10:58]** just going to be a chatbot, but an agent

**[10:59]** that has your context can be a

**[11:01]** dependable junior employee. And it

**[11:04]** really is that big a difference. And you

**[11:05]** can see it for yourself if you prompt

**[11:08]** correctly. Because correct prompting

**[11:09]** increasingly is about here's my context.

**[11:12]** Here's where to go search for more

**[11:13]** context. Are we good? Right? And then it

**[11:15]** goes off and does its thing. Now, if you

**[11:17]** want to look at who's playing in this

**[11:18]** space, it's interesting to use this

**[11:20]** angle because you see some players that

**[11:22]** are not typically put together, but who

**[11:24]** are all playing in the context space.

**[11:25]** So, Notion, I mentioned, Salesforce, I

**[11:27]** mentioned, Epic, I mentioned, Palanteer,

**[11:29]** also Snowflake and Data Bricks,

**[11:31]** potentially even Apple and Google if

**[11:34]** they can nail local AI as well as they

**[11:36]** want to. You notice that Google recently

**[11:38]** launched essentially a context layer for

**[11:40]** maps. They're thinking about this too,

**[11:42]** and it continues to highlight for me how

**[11:45]** Google pops up with so many ways to win

**[11:47]** the AI race. They're not just a model

**[11:49]** player. They're a foundation player with

**[11:51]** TPUs. They're a context player. They're

**[11:53]** an ecosystem player. or they're a

**[11:54]** devices player, they have got a lot of

**[11:56]** ways to win on this board. So, we talked

**[11:58]** about trust, we talked about context.

**[12:00]** Number three is distribution. You can

**[12:03]** generate an app in seconds, but who's

**[12:04]** going to see it? And this is something,

**[12:06]** by the way, that second time founders

**[12:07]** know that first- time founders don't.

**[12:08]** The bottleneck was never about building

**[12:10]** the thing. It was always about

**[12:11]** distributing it. Now, in Field of

**[12:13]** Dreams, the movie, you build it and they

**[12:15]** will come. That is never ever ever how

**[12:17]** it works. It is always you build it and

**[12:19]** then you have to go round people up and

**[12:20]** get them to come and see if this is what

**[12:22]** they want and see if they'll pay for it.

**[12:23]** Distribution has always been king. But

**[12:25]** what we see in a world where you have a

**[12:26]** 10x or 100x multiple in the amount of

**[12:29]** software, the amount of product being

**[12:31]** generated digitally, you have to have an

**[12:34]** edge in distribution to be heard or seen

**[12:36]** or get any signal from customers

**[12:38]** whatsoever. In other words, when supply

**[12:40]** is infinite, curation is about to become

**[12:42]** the scarcest resource in the world. So

**[12:44]** this is a place where Google plays,

**[12:46]** Apple's app store plays, Tik Tok plays a

**[12:48]** role, YouTube plays a role. These are

**[12:50]** all distribution monopolies in a sense

**[12:52]** and AI makes them more powerful not

**[12:54]** less. The gatekeepers get stronger when

**[12:57]** the flood is bigger because they tell

**[12:59]** people where to go. So for the agentic

**[13:01]** economy, this means something very

**[13:03]** specific. Agent discovery is a massive

**[13:06]** problem. If every business has AI

**[13:08]** agents, who is going to help those

**[13:10]** agents discover where they need to go to

**[13:13]** do business with one another and with

**[13:14]** humans? So, there's a new distribution

**[13:16]** layer that's starting to emerge and it's

**[13:18]** all about how agents discover what they

**[13:21]** need to do business on the internet and

**[13:23]** who they need to do business with. Now,

**[13:25]** this is actually bullish for content

**[13:26]** creators because it means that if you

**[13:28]** are able to establish yourself with a

**[13:30]** particular niche in AI as an authority,

**[13:33]** people are going to be able to use you

**[13:35]** to help get useful information and

**[13:37]** useful signal on artificial intelligence

**[13:38]** that they would otherwise not be able to

**[13:40]** get. But, and this is discussed much

**[13:42]** less, there is also an opening emerging

**[13:45]** for an agentic store discovery

**[13:49]** mechanism. We need something like an

**[13:52]** agentnative app store that allows agents

**[13:55]** to start to find and utilize utilities

**[13:58]** or utilize businesses that are

**[14:00]** agent-friendly to do business with. And

**[14:02]** this is a big emerging category. I've

**[14:04]** spent some previous videos talking about

**[14:06]** it. I'll be talking about it more in

**[14:07]** future. I think the question of what

**[14:09]** makes a business viable for an agent to

**[14:13]** transact with is one of the most

**[14:15]** interesting questions of 2026 because

**[14:17]** it's a whole lot more than putting an

**[14:19]** MCP server out there. You have to think

**[14:20]** about how fast the transaction works,

**[14:22]** how easy it is for the agent to

**[14:24]** understand the depth of what you offer,

**[14:27]** how quick it is for the agent to make a

**[14:29]** selection and operate with your API or

**[14:31]** whatever you're working with, and how

**[14:33]** simple it is for the agent to receive

**[14:34]** the good or service. all of these things

**[14:36]** and essentially the entire mechanism for

**[14:39]** commerce has to be rethought with agents

**[14:42]** at the core and I got to be honest with

**[14:44]** you almost no businesses are thinking

**[14:46]** like this if you had to pick big

**[14:47]** businesses that are trying to play in

**[14:49]** this space I would guess Google for

**[14:51]** search and discovery I would guess Apple

**[14:53]** and Google when you're talking about app

**[14:55]** stores I would guess Tik Tok YouTube

**[14:58]** Substack if you're in the content space

**[14:59]** and I would guess Amazon if you're

**[15:01]** looking at the commerce side but those

**[15:02]** are all guesses right I'm not saying all

**[15:04]** of those have clear agenda IC plays

**[15:06]** right now. I'm saying all of them have

**[15:08]** an interesting position to play and they

**[15:11]** may play those cards. And I am saying if

**[15:13]** they don't, they are liable to

**[15:15]** disruption. Okay. So, we've talked about

**[15:17]** trust, we've talked about context, we've

**[15:19]** talked about distribution. Now, we're

**[15:20]** going to talk about taste. It's such an

**[15:23]** ambiguous word, but we're going to get

**[15:24]** into why it matters and why it should be

**[15:26]** considered a separate vertical, not just

**[15:28]** a personal quality, right? A separate

**[15:30]** vertical on the web. The bottom line is

**[15:31]** this. When producing software is free,

**[15:34]** what you choose to produce becomes the

**[15:36]** entire game. So this means the way you

**[15:38]** think about your product decisions, your

**[15:40]** design sensibility, your editorial

**[15:42]** judgment about what is worth building

**[15:44]** and what is not. Your ability to look at

**[15:46]** what AI generated and know that it's

**[15:48]** right or know that it's wrong and be

**[15:50]** accountable for it. This is a human

**[15:52]** skill that you know AI can assist with,

**[15:54]** but it's not going to replace it. But

**[15:56]** because it requires a point of view on

**[15:58]** how humans do business with humans.

**[16:00]** Essentially, taste is a conviction about

**[16:02]** what should exist in the world that is

**[16:04]** not easily derivable from training data.

**[16:06]** The best analogy for this, I think, is

**[16:08]** music production. After Apple's Garage

**[16:10]** Band went mainstream, the tools got very

**[16:13]** cheap. Everyone can make a track. The

**[16:15]** flood of music was enormous. And this is

**[16:17]** even more the case now that Sunno is

**[16:19]** going online and people can use a tool

**[16:20]** to generate an entire AI music track in

**[16:23]** seconds. The producers and artists who

**[16:25]** thrive in this world, and there are

**[16:27]** people who thrive even in the Sunno

**[16:29]** world, they're not the ones with the

**[16:30]** most expensive studio anymore because

**[16:32]** production is essentially free. They're

**[16:34]** the ones with taste. They have an idea

**[16:36]** for what is going to work with the

**[16:37]** audience. They have an ear for how music

**[16:39]** might play in a variety of settings and

**[16:40]** they choose to produce something that is

**[16:42]** going to connect with the audience. The

**[16:44]** same thing is about to happen to

**[16:46]** software. So, the vibe coder who ships

**[16:48]** an app in just a few minutes hasn't done

**[16:51]** the hard part yet because they haven't

**[16:53]** figured out how is what I'm building

**[16:55]** going to deeply connect with my

**[16:57]** audience. And so, this could be

**[16:59]** expressed as design or it could be

**[17:01]** expressed just as absolutely nailing the

**[17:04]** angle of the value proposition. And in

**[17:06]** practice, what I see is the best

**[17:07]** products are both of those. They have a

**[17:09]** strong design sense and they also have a

**[17:11]** very clear, accurate, correct value

**[17:13]** proposition that resonates with a felt

**[17:15]** need the audience has. Now, if you have

**[17:18]** to pick one, famously, you stick with

**[17:20]** the value proposition one. And that's

**[17:21]** why we see so few designled companies.

**[17:23]** But both are going to be powerful rocket

**[17:26]** engines for human-led companies that

**[17:30]** achieve product market fit in the next

**[17:31]** few years. I'm going to go further

**[17:32]** though. We've talked about humanto human

**[17:34]** transactions, human commerce, and taste.

**[17:36]** Let's look at the agentic web. What does

**[17:38]** taste look like on the agentic web? I

**[17:41]** would argue it looks like orchestration

**[17:43]** quality. So, the winning agent systems

**[17:45]** won't necessarily be the ones with the

**[17:47]** best underlying models. They'll be the

**[17:49]** ones where a human with deep domain

**[17:51]** expertise has carefully tuned the

**[17:54]** prompts and designed the workflows and

**[17:56]** chosen the right tools and made a

**[17:58]** thousand small editorial decisions about

**[18:00]** how the agent should behave so that the

**[18:02]** agent as a whole is a curated experience

**[18:05]** that does powerful work. Now, I'm the

**[18:07]** first person to say that that trend may

**[18:09]** evolve over time. In particular, as we

**[18:12]** start to see auto research become

**[18:14]** something that is applied to agentic

**[18:16]** harnesses, there may be cases where

**[18:19]** agents start to self- evvolve. There may

**[18:21]** be cases where agents start to be

**[18:23]** intentionally automatically evolved by

**[18:26]** humans who are supervising the process.

**[18:28]** But the end responsibility of the human

**[18:31]** to look at an agentic product in the

**[18:33]** agentic economy and say this is the

**[18:34]** direction I want this agent to go in.

**[18:36]** this is the goal I have. This is what

**[18:38]** good looks like. That's not changing.

**[18:40]** It's not changing. And I think that we

**[18:42]** need to be honest about that. And we

**[18:44]** need to recognize that regardless of how

**[18:46]** far above the loop the human sits, the

**[18:49]** human remains accountable to what the

**[18:52]** agent is going to be doing and to how

**[18:54]** the agent participates in this larger

**[18:56]** economy. And so I don't see us

**[18:57]** abdicating taste even if we have more

**[19:00]** powerful tools like auto research that

**[19:02]** we can put in the toolkit. Number five

**[19:04]** is the least fun. Liability. Someone is

**[19:07]** going to have to be on the hook. And

**[19:08]** it's a place where you can build a

**[19:10]** powerful business. When an AI generated

**[19:12]** financial plan loses you money, who's

**[19:14]** liable? When an AI built medical app

**[19:15]** gives bad advice, who's liable? When an

**[19:17]** AI generated contract becomes something

**[19:20]** that you litigate and lose over, who's

**[19:22]** liable for that bad clause in the

**[19:24]** contract? And the AI did it is not going

**[19:26]** to be an answer that survives court.

**[19:28]** Regulated industries like healthcare,

**[19:30]** like finance, like legal, like

**[19:31]** insurance. Essentially, the niches they

**[19:33]** build on are liability niches because

**[19:36]** the professionals in these spaces, even

**[19:38]** if they're building and using agentic

**[19:40]** systems, are doing so around the core

**[19:42]** notion that they are selling

**[19:44]** accountability. That's part of how

**[19:45]** lawyers stay in business, right? Lawyers

**[19:47]** stay in business because they sell

**[19:49]** accountability before the court for how

**[19:52]** a particular case is represented. And

**[19:54]** here's the counterintuitive dynamic. The

**[19:56]** better AI gets at representing itself

**[19:59]** and talking about itself and messaging,

**[20:02]** the more important authentic

**[20:04]** accountability and liability management

**[20:06]** becomes because the mistakes that you

**[20:09]** can make with a plausible sounding AI

**[20:11]** get much much more serious. In the

**[20:13]** agentic economy, liability effectively

**[20:16]** becomes a governance layer you have to

**[20:18]** manage. You have to look at liability

**[20:20]** and say, how are we constraining and

**[20:22]** managing liability? What companies do we

**[20:24]** need to work with that specialize in

**[20:26]** agent liability? Because AI agents are

**[20:28]** going to be autonomously executing

**[20:30]** complicated workflows for you. They'll

**[20:32]** be filing documents. They may in the

**[20:34]** future be moving money for you. They may

**[20:36]** be making commitments with your name on

**[20:37]** them. Someone needs to define those

**[20:39]** boundaries, audit those actions, and

**[20:41]** ultimately be liable for that choice.

**[20:43]** The companies and the professionals who

**[20:45]** position themselves as liability

**[20:47]** guaranurs or as accountability makers in

**[20:50]** this space get to own the governance

**[20:52]** layer for the future web. Now there's an

**[20:54]** odd collection of companies in this

**[20:56]** space. I think this one is liable to

**[20:58]** grow pretty quickly. Right now Deote and

**[21:00]** McKenzie are starting to reposition

**[21:01]** themselves a little bit as AI assurance

**[21:03]** providers. 11 Labs has been in the space

**[21:05]** offering insurance for voice agents.

**[21:07]** There are also regulated SAS platforms

**[21:09]** like Viva and Elation that are in this

**[21:11]** space and really a lot of AI

**[21:14]** professionals who focus on providing

**[21:17]** safety and vetting protocols for agents.

**[21:20]** They're effectively in this space. And

**[21:22]** so this is one where you have like a

**[21:23]** real patchwork. You can have scaled up

**[21:25]** consulting firms doing billions in

**[21:27]** revenue and you can also have small mom

**[21:28]** and pop shops that are focused on this

**[21:30]** space and they're all in the business of

**[21:32]** making agents safer to run and handling

**[21:34]** the liability layer. So what does the

**[21:36]** web look like when you put all these

**[21:37]** layers together? If we step back, what

**[21:39]** is the future of the web? I would argue

**[21:41]** that the model providers like OpenAI and

**[21:43]** Anthropic are increasingly positioned to

**[21:45]** own the bedrock intelligence capability

**[21:48]** layer for the future of the web. I don't

**[21:49]** think anyone would disagree there,

**[21:50]** right? They're enormously valuable and

**[21:53]** they're increasingly commoditized

**[21:54]** relative to each other. And if we get to

**[21:56]** a point where we have open- source

**[21:58]** models, those open- source models are

**[22:00]** going to likely be a derivation of the

**[22:03]** lineages from those core model makers.

**[22:06]** And so in a sense, the influence of

**[22:08]** those model makers will live on

**[22:09]** regardless. The rapper companies like

**[22:11]** lovable, like Bolt, like Shipper, they

**[22:13]** don't own anything durable inherent.

**[22:15]** Some are going to get acquired. To be

**[22:17]** honest, most of them are going to die.

**[22:19]** and a few the ones that manage to

**[22:20]** accumulate enough user information,

**[22:22]** enough data, enough momentum. I think

**[22:24]** lovable is a great candidate here.

**[22:26]** They're going to have a shot at becoming

**[22:28]** a platform, not just a rapper. And

**[22:30]** that's absolutely the play lovable

**[22:32]** making. It wants to be effectively

**[22:34]** Shopify 2.0. I think the platform where

**[22:37]** the business of the future is done.

**[22:39]** Infrastructure players like Verscell and

**[22:41]** Replet and Stripe and Shopify, those are

**[22:44]** the ones that own the trust and

**[22:45]** execution layers of the future web. AI

**[22:48]** makes them valuable because more things

**[22:50]** are being built which requires more

**[22:51]** trust, more verification, more payments

**[22:53]** etc. So they end up being the picks and

**[22:56]** shovels of the AI gold rush and their

**[22:57]** position ends up being very very

**[22:59]** durable. Meanwhile the context owners

**[23:01]** like notion, like Salesforce, like

**[23:02]** Snowflake, like data bricks, they own

**[23:04]** the data gravity, right? The agents need

**[23:07]** context to be useful and context ends up

**[23:09]** getting locked inside those platforms

**[23:11]** and they become the permissioning layer

**[23:12]** for the agentic economy if they play

**[23:14]** their cards right. the distribution

**[23:16]** gatekeepers like Google, like Amazon,

**[23:18]** like Apple, they own how you pay

**[23:21]** attention to things on the internet. And

**[23:22]** if they play their cards right, they

**[23:24]** also own how agents pay attention on the

**[23:26]** internet. And that's going to be

**[23:27]** something that's very interesting to

**[23:28]** watch over the next year or two. And

**[23:30]** finally, us humans, right? The

**[23:31]** operators, we're founders, we're

**[23:33]** professionals, we're people, we're

**[23:34]** householders, we have taste, we have

**[23:36]** judgment, we have accountability, we

**[23:38]** provide the connective tissue that makes

**[23:40]** all of this work. And so AI doesn't

**[23:42]** necessarily replace the things we bring

**[23:44]** to the table, but understanding the

**[23:46]** structure of how the web will work

**[23:48]** allows us to be above the loop where all

**[23:50]** these agents are operating, understand

**[23:52]** what's going on, and provide our

**[23:54]** perspective and our direction in a way

**[23:56]** that's useful and strategic. So what

**[23:58]** does this mean? If you are in the space

**[24:00]** and you are thinking about building, if

**[24:01]** you're in the space, maybe you own a

**[24:03]** business, maybe you run a business,

**[24:04]** maybe you're building as a side project,

**[24:06]** whatever it is, ask yourself, what do I

**[24:10]** own that still matters if AI gets 10

**[24:12]** times better? If the answer is nothing,

**[24:14]** if a better model just makes your

**[24:16]** product obsolete, you should change your

**[24:19]** positioning now because you should be

**[24:20]** assuming that the models will get

**[24:22]** better. Now, if a better model makes

**[24:24]** your product more valuable, like if you

**[24:25]** own a piece of the trust layer or if you

**[24:27]** own a piece of the liability layer or if

**[24:29]** you're playing into the agentic economy

**[24:31]** and you want smarter agents to actually

**[24:33]** enable that economy to work well, now

**[24:34]** you're more in business and now you have

**[24:36]** something you can build on and you don't

**[24:37]** have to go to sleep at night worrying

**[24:39]** about how good the next claude model's

**[24:41]** going to be. Spoiler alert, I think

**[24:43]** they're not kidding. I think it's going

**[24:44]** to be really good. And one last word of

**[24:46]** warning to all of us who are building in

**[24:48]** this economy. We have put so much work

**[24:50]** into productionalizing code. We need to

**[24:53]** keep thinking about distribution. I

**[24:54]** mentioned it as number three in my list

**[24:56]** of big pieces for the web. If you build

**[24:59]** an MVP in a day, that's great. Your job

**[25:01]** is actually to put it in front of

**[25:03]** customers, get customer feedback, and

**[25:05]** validate that you are building something

**[25:07]** customers want. That is a very human

**[25:09]** activity. And as much as we can start to

**[25:11]** scale voice of customer when we have

**[25:13]** lots of customers to work with, we still

**[25:15]** need to own and be accountable for

**[25:17]** whether the product resonated with the

**[25:19]** customer in a way that's useful. There

**[25:21]** is no substitute for distribution. And I

**[25:23]** wish that all of the focus and all of

**[25:26]** the energy that tools like Lovable and

**[25:28]** Replet have generated around creation

**[25:30]** got piped a little bit into the

**[25:32]** distribution side because what I see

**[25:34]** right now is a 100,000 a million 10

**[25:36]** million apps blooming and most of them

**[25:38]** are never going to get discovered

**[25:40]** because no one ever put the thought into

**[25:42]** whether or not someone really wants this

**[25:45]** product. And that's not a new lesson.

**[25:47]** None of that changed. It just matters

**[25:49]** more now. In fact, that is the larger

**[25:51]** takeaway. The five things I called out,

**[25:53]** trust, context, distribution, liability,

**[25:56]** taste, those are things that have always

**[25:57]** mattered on the web. And what we're

**[25:59]** seeing is that AI is essentially a

**[26:00]** forcing function that makes them matter

**[26:02]** more now. And AI cannot take their

**[26:05]** place. And that is why they're durable

**[26:06]** places to build in the future of the

**[26:08]** agentic economy. Good luck building.
