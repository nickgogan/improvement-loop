# Transcript: Your Claude Limit Burns In 90 Minutes Because Of One ChatGPT Habit.

**URL:** https://www.youtube.com/watch?v=5ztI_dbj6ek
**Segments:** 794
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 26:35
**Uploaded:** 2026-04-02

---

## Full Text

The next generation of models is likely to drop in the next one to two months. I'm talking about Claude Mythos. I'm talking about whatever Chad GPT drops next. I'm talking about the next Gemini model. They will be more expensive, a lot more expensive because they're all trained on much more expensive chips, the GB300 series from Nvidia, and it's just going to get more expensive from there. The intelligence we're going to get, the ambient compute all around us that is essentially free intelligence is going to be the dumber models. That's just how it is. If you want to use cutting edge models, you have got to stop burning tokens and blaming the model. And that is the theme for this video. If you're in a position where you're wondering how much token usage you have or how expensive your AI is or whether you're using too many tokens for your AI or how you can even measure that, how you can get better at it. That is what this is. And that is going to be one of the most valuable skills on the planet. by the way, because you do not want to be in a position where you are putting $250,000 a year. A real number that JSON Huang gave in a real interview for what he expects an actual individual engineer to spend in a year on tokens. You don't want to be the person spending 250 grand on tokens you don't have to be spending on. You want to be smart. And I am going to give you a specific example. This is real life example. A real person I know gave me permission to use this. I recently saw a production AI pipeline that ingests multiple long- form conversations per user, runs an analysis across dozens of dimensions and generates a fully personalized output all on the most expensive models that money can buy. Not because the person wants to use expensive models, but because he tested it and what he found was that the better models produce the results he needs for this business. The cost per user less than a quarter, less than 25 cents per user for that. Most of us are spending more than we need to on AI and this is a video about that. You can be really smart, use really good cutting edge AI and you can be intelligent with your token usage and not spend a ton of money. If you want to know what that's like, keep on watching because we're going to get into specific strategies and I'm going to show you what I built so that we can actually make this easier for everybody so it's not just a guessing game anymore. The takeaway is that Frontier AI can be absurdly cheap when you know what you're doing. Essentially, the models are not expensive. It's your habits that cost a lot. And with cloud usage limits dominating everything in the last week, I think it's worth having that conversation. So, let's get to it. I've made the case we can use our models better. What are the specific habits we can change? I want to name specific habits that I have seen in conversations with others, looking over shoulders, reading GitHub repos, listening to conversations online. These are specific examples that are patterns I see over and over again. And the first one is the rookies. The folks who are new to cutting edge, you know what you bleed out on in tokens? You bleed out on document ingestion. This one drives me crazy because it's so so easy to fix. A brand new Cloud Desktop user might drag in three PDFs into a conversation that might be 1500 words each, which is just 4,500 words of text. It's not that long. And they say, "Summarize these." and Claude processes the raw PDFs with all the formatting overhead that goes with that, the headers, the footers, the embedded fonts, the layout metadata, and the entire binary structure gets encoded as tokens. And so the 4500 words of content can become a 100 plus thousand tokens if you're not careful. All you have to do to avoid that is just think in terms of markdown. If you just ask Claude or frankly go to any of a number of services on the internet that are free and say please convert to markdown. It will just do it right. It will just take 10 seconds and convert to markdown. And then you have a very clean set of content that's between four and 6,000 tokens. And that's like saving you 20x on the memory. And this waste just compounds, right? Because once those 100,000 tokens are in your conversation history, they bounce back and forth and bounce back and forth. And this is how you fill up your token window. and you wonder how other people get so much done. Please, please, please, if you're new to AI or if you've never thought about it, think about the file formats you're throwing because so many of these file formats are designed to be human readable. They're not designed to be AI readable. Think about the token efficiency of these file formats. And if you're wondering, well, how do I convert to markdown? I built something for you because all you have to do is just ingest a file. You you hit transform and it just converts it back into into markdown. That's it. And we have a number of file types. We're adding more from the community all the time. It's part of the open brain ecosystem. It's just a plugin you can put in and it will just convert it to markdown. But that's not the only way. You can tell Claude to do it directly. You can also just directly do it on the internet with any of a number of free web services. Markdown conversion should not be gated. It just it's super easy to do. Tokens are designed to preserve everything in an original text. If you wanted to reason about the style of the PDF, fine, keep it. But 99% of the time, all you care about is the text. You just want it in markdown. Please, please, please think about your file formats. Next big mistake that people make, and this one comes a little bit after people tend to convert to markdown and start to understand how some of these initial documents work. Please do not sprawl your conversations. If you were doing 20, 30, 40 turns on a conversation, no AI was reinforcement learned, trained, or designed to handle that kind of sprawl. All you're doing is compressing the ratio of the conversation where the original instructions happened. And yes, the models are getting better and better and better at anchoring on and remembering those original instructions even when they go through compression. But why make them suffer? Why make yourself suffer by filling up the context window with croft? Why waste tokens? Why not just ask for what you want upfront? And if you're going to have an evolving exchange or evolving conversation, clearly market at the top as our goal here is to evolve and reach a conclusion together. And then you have a light conversation that goes 20 or 30 turns and say, "Thank you. I've got a conclusion. Please summarize this." And then you go and do real work. I see so many people trying to mix together modes, but AI is really designed for single turn do a lot of heavy work more and more and in that context you need to do the thinking in advance and bring that to the table and if you need to think with AI that should be in a separate chat, separate conversation. It might even be a separate model. It might be three separate models and you're bringing all of that in. I do that all the time. I'm like, okay, I want to look through what communities are thinking about AI on X. I'm going to go to Grock for that or I'm going to go through and look at what earnings reports are saying about the state of AI and capital investment. I'm going to go and pipe that through chat GPT thinking mode and get a bunch of reports out on that. Or I'm going to go through perplexity research and get a bunch of reports out on that. Now I'm going to go and have a look at what some major blog posts have to say about a particular AI topic. I'll just go to Claude Opus 4.6. We'll do a targeted web search. We'll go back through. We'll make sure we understand what we're looking at. None of that is intended to be a single answer, right? These are all evolving conversations. Once I get what I want out of each of these individual threads, I can pull them together and say, "Okay, now I have a piece of work to do. Now I have something I actually need done and I have all the context needed." So you should have two modes here. You should have a mode where you are trying to gather information and a mode where you are trying to focus and get work done. Do not mix the two together. That is how you burn tokens. That is how you confuse the AI. Your objective when you want the AI to do real work should be to be so clear that the AI needs to do nothing else and it just goes and gets the work done and comes back. It should be that clear. If you are an intermediate user and you are like, I know this stuff, Nate, well, let me give you another tip you may not know. the people who are adding lots of plugins to their chat GPT or their cloud instances, you are paying a tax every time you start a conversation because in the background, those are going to be loaded in and they're going to start to fill the context window. I know someone who shared with me that they are over 50,000 tokens in on a context window before they type the first word because they actually load that many plugins and connectors. You don't need that much. You know what that's like? That is like walking in to a fully functional tool workshop and the first thing you do instead of leaving the tools on the walls is you go and get all the tools off and you lay them out on the workbench and you say, "Okay, now we're going to do, I don't know, we're going to do something. We're going to make a bench." Do you need all 200 tools in the workshop to make the bench? No. You probably need the right five. Think about that the next time you have an approach to tooling. Because so many people, we we hear about this new plugin, we hear about this new connector, someone hypes it up, we say we need to add it, and we don't realize it's a silent tax for the rest of time. Every time we have a conversation, and it just adds that little bit, it adds a thousand tokens, it adds 2,000 tokens, whatever it does, and it just adds it always. Do you want to pay that for the model? Maybe you should think more strategically about which plugins and connectors are really adding value for you because they can. like they can be tremendously valuable, but make sure you know which ones you really want because if you don't, then you're going to be looking at dozens of plugins that you don't really need that are supposed to add value, but just add a bunch of croft, a bunch of junk into your context window and confuse the model and keep it from doing good work and maybe confuse it as to which tools it's supposed to use. Now, I'm saving the most expensive and the most advanced users for last because this is where the leverage lies. If you are an advanced user, if you are someone who's like, "Send me to the GitHub repo. I can just do this myself. Let me install OpenClaw on my Mac Mini. I'm okay managing the gateway. I can be secure." This is for you. You have the most leverage of anybody out there in terms of how many tokens you use. And typically speaking, your mistakes are the most expensive ones because if you screw up, you're screwing up at a level of hundreds of thousands or millions of tokens, maybe more. And the reason why is simple. You are doing bigger projects with AI. And when you do big projects with AI, your ability to leverage AI effectively becomes one of the most critical things you can do to manage ROI and cost on a particular project. It is a job skill at that level. If you're technical enough to go to a GitHub, you have a job skill to manage tokens efficiently. And you cannot pass that off to somebody else. That is not going to be somebody else's full-time job at an org. All of us are going to have to learn to manage our tokens. Well, if you were sitting there and you are you are the person who is responsible for the system prompt on an agent and you haven't pruned it in the last couple of weeks, what are you doing? If you haven't sat there and gone line by line and said, you know what, a hundred of these lines I don't need anymore because they've been here since 3.5 and like I don't need them now. If you're sitting there and you're like, I don't know why we're loading this entire repo into the context window. We just do it all the time and it seemed to work two generations ago but we never tested it. That's just irresponsible. You need to be in a position where you are actually allowing the gains in model intelligence to lean out your context window. If you want to look at the larger trend that we see in AI today, it is that we needed to frontload and be really specific about a lot of context for dumber models in 2025. And now that it's 2026, as the models get more intelligent, we can lean out the context window initially because we can trust the model to retrieve better. So take that seriously. That is something you can do that is practical to get ready for claude mythos. Don't sleep on it. This is again if you're technical, these are million token decisions we're talking about, especially if you're running this agent over and over again. It adds up. Let me give you a specific example that is based on the original beginner example with PDFs to show you the tangible difference in cost, right? And this is something that should cascade all the way across. If you don't believe me, this is real. Let's say you feed raw PDFs into context. Let's say it's a 100,000 tokens versus 5K like we talked about. Let's say it's a conversation sprawl that takes 30 turns. I've seen these like this is very realistic. And let's say you use Opus 4.6 for everything including formatting, including proof reading, and you're making something over a 5 hour session where you're talking back and forth. You might be spending roughly 800,000 to a million input tokens with maybe 150,000 to 200,000 of output tokens including thinking. $5 in and $25 out per million. you're spending eight to$10 dollars worth of compute which you might say you know what I can tolerate that or I got the unlimited plan or I don't care whatever but I want you to look at the difference because anytime you start to get serious with AI you need to see the difference we talk about not being wasteful with artificial intelligence this is being wasteful you want to save water you want to save energy don't waste your tokens clean session same work convert documents to markdown first start fresh conversations every 10 to 15 turns use opus for reasoning and sonnet for execution ution and haiku for polish and scope the context to what's needed and over the same period of time you get the same result for 100 to 150,000 input tokens a lot less and maybe 50 to 80,000 output tokens you blend that across both models and instead of costing8 to$10 in compute you spend a buck and you got the same amount in other words you got an 8 to10x reduction in cost now scale it right that sloppy user is burning 40 to 50 bucks in compute a week and the clean user is burning five to seven bucks a across a 10 person team on an API. That's 2,000 bucks a month versus 250 bucks a month for the exact same result. For subscription users, it's the difference between hitting your limit daily and then forgetting that limits exist because you just are so productive. Now, if you think this isn't serious, I want you to think about the cost structure for Mythos for a minute. Mythos is rumored to be by far anthropic's most expensive model. I think very strongly by April or May we are going to have a new class of pricing well above $525 range for tokens into maybe 10x that right imagine a world where you are 10x what opus costs now $5 in $25 out for opus what if it's $50 in $250 out for opus well now things start to get serious now that eight or 10x reduction on individual work for a day becomes something that you can actually measure and think about as a business and you imagine how big that gets When you start to work across a dev team, the mistakes you're making today were tolerable because models were priced cheaply when cutting edge intelligence that you want comes out more expensive. And I don't know the exact price, right? I'm not saying it's 50 and 250. I'm giving you a thought exercise. It might be 10 and 50 instead. It's still the same point. The point is the model that you want is going to cost more. And as models cost more, your mistakes scale. Your mistakes scale with the price of intelligence. And make no mistake, the models will keep getting better. Every quarter, every release, the trajectory is unambiguous. People who tell you the models are plateauing are lying. They are lying to you. The models are getting much faster. And I do see that occasionally that people are insisting that the models aren't getting better. It's not true by any measure out there. And the people that I see insisting on it, I think they're insisting on it partly because they don't want to face the world as it will exist when AI is this good and continuing to accelerate this fast. It's scary, right? We but we should face it and we can all work through it together. >> All right. I have built a stupid button. That is my contribution to this discourse. I am building a stupid button so you can check and see if you are using your context incorrectly. I want to save you money. I want to save you hundreds of dollars. Please do not be stupid with your tokens. You know, if if you care about it, don't waste the water. Don't waste the electricity. If you just care about the bottom line, also don't waste your bucks, right? We should probably care about all of those things. If you want to know like what's in Nate's stupid button, it's really simple. There's six questions that I'm helping you answer. Number one, do you feed Claude raw PDFs and images when all you need is text? Is there something you are doing that is grossly inefficient as far as tokens go? By the way, screenshots, terribly inefficient. It would be much, much better just to copy and paste text. Convert to markdown always. Claude can do it really, really fast for you. Why not? Question two. When was the last time you started a fresh conversation? Are you one of those people that keeps a conversation going forever? I swear the number of people who keep their conversations going forever is highly correlated to the number of people who start experiencing symptoms of LLM psychosis. Why? Because models drift over time. They were never intended for that long a conversation. If you're having a longunning conversation, you're just in strange territory. When was the last time you started a fresh conversation? And why is that? Again, every time you take a turn in a conversation, you read it as sending one line back. But Claude or Chad GPT or Gemini reads it as sending the entire conversation back. And if you're wondering, is this something that's just for Claude? Nate's talking about Claude a lot. No, it's for Chad GPT, it's for Gemini, it's for Llama, it's for any LLM you're using. It's for Quen. This is how LLMs work. Don't waste it. Question three, are you using the most expensive model for everything? Are you using Opus? Are you using 5.4 on pro mode? Whatever your choice is, are you picking the most expensive model and just blindly using it regardless when the cheaper model may work better? This is especially important if you have production workloads, but it's also true for all of us. Like, if you're doing something that's a simple formatting task, don't depend on Opus for it. Don't depend on 5.4 for it. Use the models for what they're designed for. Don't bring a Ferrari to the grocery store. Question four, do you know what's loading in context before you even type? You can actually find this out. You can run slashcontext in cla code. By the way, you could look at the number of things that are loading. If you're in cloud code, if you don't know what that means, you can go to your Chad GBT or your cloud. You can see how many connectors you have available. You can see how many you've loaded up. You could be loading tens of thousands of tokens that you're not really aware of and not really using. If you enable Google Drive months ago and you never never ever use Google Drive, you just thought it was cool on the day it launched. Why? just drop it. There are so many examples like that where we see something cool, we add it, and we forget it's there. It's like a barnacle on a ship. It's going to slow you down. It's going to burn tokens. You don't need to have it. Audit. Audit your plugins. It matters. Next question. API builders, are you caching stable context so you don't reuse it? Prompt caching can give you a 90% discount on repeated content. Right. Cash hits on Opus cost 50 cents per million versus $5 per million standard. It makes a difference. Do not sit there and ignore prompt caching. Take it seriously. If your system prompt, your tool definitions, your reference documents aren't cached, what are you doing? This is not advanced stuff in 2026. You should just be doing it. In the last question, the stupid button test for this is a real button. By the way, I really built a stupid button. How are you handling web search? Are you letting Claude do web research the expensive way? People don't realize this, but if you call perplexity for a search, it tends to be much more token cheap than using claude natively. Now, Claude is addressing this. There are lots of ways to do claude search. You can actually use Claude to navigate through a browser. You can also directly search in the terminal and it will spin up something in the background that's a service and you can call something in like an MCP connector for perplexity. All different options you can use. This is broadly true. It's not just true for cloud. It's true for Chad GPT. is true for Gemini, etc. because MCP is magic. But if you are trying to do search, the larger point is that you should be doing search as cheaply as possible. If you just want quick results that are token efficient, it may be worth it to take the time to spin up an MCP and just have a dedicated service that just returns the search results. That's what I have found experimentally with perplexity and claude is that perplexity tends to burn something like 10 to 50,000 less tokens per search which is not a small number if you're doing complex search and it tends to be five times faster and it has structured citations. So this is not meant to be a perplexity plug. It's just a token management plug. Try it for yourself. But I got to say I like faster. I like citations. I like less tokens over a researchheavy session like a plug-in like that can save you a lot on the token side. And that's a larger call out. Like if you have ways to look at your token usage and to diagnose it, you're going to be smarter about it. And that's the whole point of the stupid button is like let's not fly blind here. Let's look at our actual token usage and let's actually make some good choices and let's optimize it. Now what's in this stupid button? Number one, there is a prompt. If you've never done this, if you're like, "What is an MCP server?" We got a prompt for you, right? A prompt you can run against your recent conversations that actually identifies the specific dumb things you specifically are doing. Like it will see which documents you're feeding raw. It will see your conversation spraw. It will look at model misuse. It will look at redundant context loading. It looks at your actual patterns and it will tell you what to fix first. So that's the easy version, right? Anyone can use it. Any plan, no setup required. Number two, a skill. This is an invocable skill that audits your cloud code or your desktop environment or any other environment. It could be it could be chat GPT etc. Skills are also translatable and it measures your per session token overhead. It will flag system prompt load. It will check your plug-in and your skill loading. It will give you a before and after before you make changes. Think of it as like you kind of need a gas tank for your tokens and gee, wouldn't it be nice to have one, right? So, it's like the gas tank skill. Number three, we built some guardrails. So guardrails will sit directly on your knowledge store. So if you're an open brain person, which is something we've been doing as a community, it will sit right on your open brain and you will stop burning tokens on input, which is a nice touch, right? Automatic markdown conversion for documents that are hitting the store. Index first retrieval instead of just dump and search. Uh context scoping that enables a sort of minimum viable context for the query. This is where token management stops just being a personal discipline and it becomes infrastructure that starts to maintain itself. And I think I'm really excited to see how the community continues to build on this because open brain is open source and we'll keep evolving it and improving it. But I wanted to make sure that we had rails that ensured we have responsible token usage for the open brain community. So look, I'm going to close by talking briefly about agents and context because agents burn hundreds of millions of tokens in some cases. We don't want to leave them out. How do we think about context management for agents? And I'm going to give you five commandments. I call it the keep it simple stupid commandments for agents. Number one, index your references. Right? If an agent is getting raw documents instead of relevant trunks, you've already failed. The entire point of retrieval is to scope what the model sees to what it needs. Dumping a full document set into the window on every agent call is wildly irresponsible. You can't do that just to give the agent context. Don't make the agent do work it doesn't need to do. Number two, please prepare your context for consumption. Pre-process, pre-summarized, pre-chunk it. A reference document should arrive in an agent's context, ready to be used, not ready to be read or processed. If the model's first several thousand tokens of reasoning are just spent dealing with the crappy pre-processing you did, you're not being a responsible agent builder. Number three, this is something we've mentioned before. I'm calling it out in the context of agents because it's so important for agent workflows. Please, please, please cash your stable context. System prompts, tool definitions, persona instructions, reference material, anything that is stable, all should be cashed at a 90% discount on cash hits. This is the lowest effort, highest impact optimization that you have on the table. If you're making thousands of agent calls a day and you're not cashing, it's just pouring money down the drain. Number four, scope every agent's contact to the minimum it needs. Right? A planning agent does not need your full codebase. Don't give it the full codebase. An editing agent doesn't need your project roadmap. Don't give it the project roadmap. You get the idea, right? Passing everything to every agent is architectural laziness and it has real costs both in tokens burn and frankly in degraded agent performance. Models perform worse when they're drowning in a relevant context. And by the way, if you're like, I'm not sure what the agent will need. Aren't the smarter agents supposed to find it? The answer is yes. But you will only do that efficiently if you give them a searchable repo that is pre-processed so they can go and get only the relevant slice of context. So take the time to do it right. Number five, measure what you burn. If you don't know your per call token cost, you're just optimizing without any information. Right? Please instrument your agent calls. Track your input tokens. Track your output tokens. Track your overall model mix and your cost ratio. You cannot improve what you do not measure. And most teams building agentic systems are thinking a lot about whether they are semantically correct, not whether they're functionally correct. There's a big difference. And they're thinking a lot about optimizing their system prompt. They're not thinking a ton about their model cost because most of the time the model cost is not what makes the project live or die. And I get that in this age in 2025, early 2026, with the cost we have today and the urgency from executives to build the $12 per run cost or whatever it's going to be is not going to make or break the ship. But plan for a world where the models are more expensive. Plan for a world where you have to scale up. Plan for a world where you have to be responsible and instrument. Now, stepping back, there's a cultural problem we need to acknowledge behind all of this. At some point in the last few months, burning tokens has become a badge of honor. And I get it. There is a degree to which you need to be burning tokens in order to do meaningful work in the age of AI. None of this is to say that I expect token consumption to go down. It won't. You need to be ready to burn those tokens. This is not an ask that you not do that. This is an ask that you do it efficiently. And so when Jensen sits there on stage and says $250,000 in token costs per developer and everyone like is shocked or rolls their eyes or whatever the reaction is, my reaction is I hope it's 250 grand in smart token costs. It's not the individual dollar amount for Jensen because he's got cash in the bank. It's whether the tokens were used well. It's whether it's smart tokens. So begin to think to yourself, yes, I need to be maxing out my cloud. There are people who like go into withdrawal when they don't get to use their cloud. I know people like that who are like, "Ah, I went to a movie and uh I couldn't use my cloud for a few hours. I feel like I missed out on my token limit." Touch some grass. It's going to be okay. But use your tokens well. Be efficient with your token usage. Know what you're spending it on. Don't spend it on silly stuff. Don't spend it on the PDFs that you have to convert. Actually spend it on meaningful work. And that is something that is a human problem. We need to be bold and audacious. These models are really good at stuff. So, let's get more bold, more audacious, and think bigger about what we can aim them at. Because if we can be more efficient, we can do a whole lot more cool and creative stuff with those tokens. That's why I built the internet a stupid bug.

---

## Timestamped Segments

**[0:00]** The next generation of models is likely

**[0:01]** to drop in the next one to two months.

**[0:03]** I'm talking about Claude Mythos. I'm

**[0:04]** talking about whatever Chad GPT drops

**[0:06]** next. I'm talking about the next Gemini

**[0:07]** model. They will be more expensive, a

**[0:10]** lot more expensive because they're all

**[0:11]** trained on much more expensive chips,

**[0:13]** the GB300 series from Nvidia, and it's

**[0:16]** just going to get more expensive from

**[0:17]** there. The intelligence we're going to

**[0:18]** get, the ambient compute all around us

**[0:21]** that is essentially free intelligence is

**[0:22]** going to be the dumber models. That's

**[0:24]** just how it is. If you want to use

**[0:26]** cutting edge models, you have got to

**[0:27]** stop burning tokens and blaming the

**[0:29]** model. And that is the theme for this

**[0:31]** video. If you're in a position where

**[0:32]** you're wondering how much token usage

**[0:34]** you have or how expensive your AI is or

**[0:37]** whether you're using too many tokens for

**[0:38]** your AI or how you can even measure

**[0:41]** that, how you can get better at it. That

**[0:43]** is what this is. And that is going to be

**[0:44]** one of the most valuable skills on the

**[0:46]** planet. by the way, because you do not

**[0:48]** want to be in a position where you are

**[0:49]** putting $250,000 a year. A real number

**[0:52]** that JSON Huang gave in a real interview

**[0:54]** for what he expects an actual individual

**[0:56]** engineer to spend in a year on tokens.

**[0:58]** You don't want to be the person spending

**[1:00]** 250 grand on tokens you don't have to be

**[1:02]** spending on. You want to be smart. And I

**[1:05]** am going to give you a specific example.

**[1:07]** This is real life example. A real person

**[1:09]** I know gave me permission to use this. I

**[1:11]** recently saw a production AI pipeline

**[1:14]** that ingests multiple long- form

**[1:16]** conversations per user, runs an analysis

**[1:19]** across dozens of dimensions and

**[1:21]** generates a fully personalized output

**[1:23]** all on the most expensive models that

**[1:25]** money can buy. Not because the person

**[1:27]** wants to use expensive models, but

**[1:28]** because he tested it and what he found

**[1:30]** was that the better models produce the

**[1:32]** results he needs for this business. The

**[1:34]** cost per user less than a quarter, less

**[1:36]** than 25 cents per user for that. Most of

**[1:39]** us are spending more than we need to on

**[1:43]** AI and this is a video about that. You

**[1:46]** can be really smart, use really good

**[1:48]** cutting edge AI and you can be

**[1:50]** intelligent with your token usage and

**[1:52]** not spend a ton of money. If you want to

**[1:54]** know what that's like, keep on watching

**[1:56]** because we're going to get into specific

**[1:57]** strategies and I'm going to show you

**[1:59]** what I built so that we can actually

**[2:01]** make this easier for everybody so it's

**[2:03]** not just a guessing game anymore. The

**[2:05]** takeaway is that Frontier AI can be

**[2:07]** absurdly cheap when you know what you're

**[2:10]** doing. Essentially, the models are not

**[2:12]** expensive. It's your habits that cost a

**[2:14]** lot. And with cloud usage limits

**[2:15]** dominating everything in the last week,

**[2:17]** I think it's worth having that

**[2:19]** conversation. So, let's get to it. I've

**[2:21]** made the case we can use our models

**[2:22]** better. What are the specific habits we

**[2:24]** can change? I want to name specific

**[2:26]** habits that I have seen in conversations

**[2:28]** with others, looking over shoulders,

**[2:31]** reading GitHub repos, listening to

**[2:33]** conversations online. These are specific

**[2:35]** examples that are patterns I see over

**[2:37]** and over again. And the first one is the

**[2:39]** rookies. The folks who are new to

**[2:40]** cutting edge, you know what you bleed

**[2:42]** out on in tokens? You bleed out on

**[2:44]** document ingestion. This one drives me

**[2:46]** crazy because it's so so easy to fix. A

**[2:49]** brand new Cloud Desktop user might drag

**[2:51]** in three PDFs into a conversation that

**[2:54]** might be 1500 words each, which is just

**[2:56]** 4,500 words of text. It's not that long.

**[2:59]** And they say, "Summarize these." and

**[3:01]** Claude processes the raw PDFs with all

**[3:04]** the formatting overhead that goes with

**[3:05]** that, the headers, the footers, the

**[3:07]** embedded fonts, the layout metadata, and

**[3:09]** the entire binary structure gets encoded

**[3:11]** as tokens. And so the 4500 words of

**[3:14]** content can become a 100 plus thousand

**[3:16]** tokens if you're not careful. All you

**[3:18]** have to do to avoid that is just think

**[3:20]** in terms of markdown. If you just ask

**[3:24]** Claude or frankly go to any of a number

**[3:26]** of services on the internet that are

**[3:27]** free and say please convert to markdown.

**[3:29]** It will just do it right. It will just

**[3:32]** take 10 seconds and convert to markdown.

**[3:35]** And then you have a very clean set of

**[3:37]** content that's between four and 6,000

**[3:39]** tokens. And that's like saving you 20x

**[3:42]** on the memory. And this waste just

**[3:43]** compounds, right? Because once those

**[3:45]** 100,000 tokens are in your conversation

**[3:47]** history, they bounce back and forth and

**[3:49]** bounce back and forth. And this is how

**[3:50]** you fill up your token window. and you

**[3:52]** wonder how other people get so much

**[3:53]** done. Please, please, please, if you're

**[3:55]** new to AI or if you've never thought

**[3:58]** about it, think about the file formats

**[4:00]** you're throwing because so many of these

**[4:01]** file formats are designed to be human

**[4:04]** readable. They're not designed to be AI

**[4:05]** readable. Think about the token

**[4:08]** efficiency of these file formats. And if

**[4:11]** you're wondering, well, how do I convert

**[4:13]** to markdown? I built something for you

**[4:15]** because all you have to do is just

**[4:18]** ingest a file. You you hit transform and

**[4:21]** it just converts it back into into

**[4:23]** markdown. That's it. And we have a

**[4:25]** number of file types. We're adding more

**[4:26]** from the community all the time. It's

**[4:27]** part of the open brain ecosystem. It's

**[4:29]** just a plugin you can put in and it will

**[4:31]** just convert it to markdown. But that's

**[4:32]** not the only way. You can tell Claude to

**[4:34]** do it directly. You can also just

**[4:36]** directly do it on the internet with any

**[4:38]** of a number of free web services.

**[4:40]** Markdown conversion should not be gated.

**[4:42]** It just it's super easy to do. Tokens

**[4:45]** are designed to preserve everything in

**[4:47]** an original text. If you wanted to

**[4:49]** reason about the style of the PDF, fine,

**[4:53]** keep it. But 99% of the time, all you

**[4:56]** care about is the text. You just want it

**[4:58]** in markdown. Please, please, please

**[5:00]** think about your file formats. Next big

**[5:03]** mistake that people make, and this one

**[5:04]** comes a little bit after people tend to

**[5:06]** convert to markdown and start to

**[5:08]** understand how some of these initial

**[5:09]** documents work. Please do not sprawl

**[5:12]** your conversations. If you were doing

**[5:14]** 20, 30, 40 turns on a conversation, no

**[5:17]** AI was reinforcement learned, trained,

**[5:19]** or designed to handle that kind of

**[5:22]** sprawl. All you're doing is compressing

**[5:24]** the ratio of the conversation where the

**[5:27]** original instructions happened. And yes,

**[5:29]** the models are getting better and better

**[5:31]** and better at anchoring on and

**[5:32]** remembering those original instructions

**[5:34]** even when they go through compression.

**[5:36]** But why make them suffer? Why make

**[5:38]** yourself suffer by filling up the

**[5:41]** context window with croft? Why waste

**[5:43]** tokens? Why not just ask for what you

**[5:46]** want upfront? And if you're going to

**[5:48]** have an evolving exchange or evolving

**[5:50]** conversation, clearly market at the top

**[5:53]** as our goal here is to evolve and reach

**[5:55]** a conclusion together. And then you have

**[5:58]** a light conversation that goes 20 or 30

**[6:00]** turns and say, "Thank you. I've got a

**[6:02]** conclusion. Please summarize this." And

**[6:03]** then you go and do real work. I see so

**[6:05]** many people trying to mix together

**[6:07]** modes, but AI is really designed for

**[6:09]** single turn do a lot of heavy work more

**[6:11]** and more and in that context you need to

**[6:14]** do the thinking in advance and bring

**[6:15]** that to the table and if you need to

**[6:16]** think with AI that should be in a

**[6:18]** separate chat, separate conversation. It

**[6:20]** might even be a separate model. It might

**[6:22]** be three separate models and you're

**[6:23]** bringing all of that in. I do that all

**[6:25]** the time. I'm like, okay, I want to look

**[6:27]** through what communities are thinking

**[6:28]** about AI on X. I'm going to go to Grock

**[6:30]** for that or I'm going to go through and

**[6:32]** look at what earnings reports are saying

**[6:33]** about the state of AI and capital

**[6:34]** investment. I'm going to go and pipe

**[6:36]** that through chat GPT thinking mode and

**[6:39]** get a bunch of reports out on that. Or

**[6:40]** I'm going to go through perplexity

**[6:41]** research and get a bunch of reports out

**[6:43]** on that. Now I'm going to go and have a

**[6:45]** look at what some major blog posts have

**[6:47]** to say about a particular AI topic. I'll

**[6:49]** just go to Claude Opus 4.6. We'll do a

**[6:51]** targeted web search. We'll go back

**[6:53]** through. We'll make sure we understand

**[6:54]** what we're looking at. None of that is

**[6:56]** intended to be a single answer, right?

**[7:00]** These are all evolving conversations.

**[7:02]** Once I get what I want out of each of

**[7:03]** these individual threads, I can pull

**[7:05]** them together and say, "Okay, now I have

**[7:07]** a piece of work to do. Now I have

**[7:09]** something I actually need done and I

**[7:11]** have all the context needed." So you

**[7:13]** should have two modes here. You should

**[7:15]** have a mode where you are trying to

**[7:17]** gather information and a mode where you

**[7:19]** are trying to focus and get work done.

**[7:21]** Do not mix the two together. That is how

**[7:22]** you burn tokens. That is how you confuse

**[7:25]** the AI. Your objective when you want the

**[7:27]** AI to do real work should be to be so

**[7:30]** clear that the AI needs to do nothing

**[7:33]** else and it just goes and gets the work

**[7:35]** done and comes back. It should be that

**[7:38]** clear. If you are an intermediate user

**[7:39]** and you are like, I know this stuff,

**[7:41]** Nate, well, let me give you another tip

**[7:43]** you may not know. the people who are

**[7:44]** adding lots of plugins to their chat GPT

**[7:46]** or their cloud instances, you are paying

**[7:48]** a tax every time you start a

**[7:50]** conversation because in the background,

**[7:51]** those are going to be loaded in and

**[7:53]** they're going to start to fill the

**[7:54]** context window. I know someone who

**[7:56]** shared with me that they are over 50,000

**[7:59]** tokens in on a context window before

**[8:02]** they type the first word because they

**[8:04]** actually load that many plugins and

**[8:06]** connectors. You don't need that much.

**[8:08]** You know what that's like? That is like

**[8:10]** walking in to a fully functional tool

**[8:14]** workshop and the first thing you do

**[8:15]** instead of leaving the tools on the

**[8:17]** walls is you go and get all the tools

**[8:18]** off and you lay them out on the

**[8:20]** workbench and you say, "Okay, now we're

**[8:21]** going to do, I don't know, we're going

**[8:22]** to do something. We're going to make a

**[8:23]** bench." Do you need all 200 tools in the

**[8:25]** workshop to make the bench? No. You

**[8:27]** probably need the right five. Think

**[8:28]** about that the next time you have an

**[8:31]** approach to tooling. Because so many

**[8:33]** people, we we hear about this new

**[8:36]** plugin, we hear about this new

**[8:37]** connector, someone hypes it up, we say

**[8:39]** we need to add it, and we don't realize

**[8:41]** it's a silent tax for the rest of time.

**[8:44]** Every time we have a conversation, and

**[8:46]** it just adds that little bit, it adds a

**[8:47]** thousand tokens, it adds 2,000 tokens,

**[8:49]** whatever it does, and it just adds it

**[8:50]** always. Do you want to pay that for the

**[8:52]** model? Maybe you should think more

**[8:54]** strategically about which plugins and

**[8:56]** connectors are really adding value for

**[8:57]** you because they can. like they can be

**[8:59]** tremendously valuable, but make sure you

**[9:01]** know which ones you really want because

**[9:03]** if you don't, then you're going to be

**[9:04]** looking at dozens of plugins that you

**[9:06]** don't really need that are supposed to

**[9:08]** add value, but just add a bunch of

**[9:10]** croft, a bunch of junk into your context

**[9:13]** window and confuse the model and keep it

**[9:15]** from doing good work and maybe confuse

**[9:16]** it as to which tools it's supposed to

**[9:18]** use. Now, I'm saving the most expensive

**[9:20]** and the most advanced users for last

**[9:22]** because this is where the leverage lies.

**[9:24]** If you are an advanced user, if you are

**[9:26]** someone who's like, "Send me to the

**[9:27]** GitHub repo. I can just do this myself.

**[9:30]** Let me install OpenClaw on my Mac Mini.

**[9:32]** I'm okay managing the gateway. I can be

**[9:34]** secure." This is for you. You have the

**[9:37]** most leverage of anybody out there in

**[9:39]** terms of how many tokens you use. And

**[9:41]** typically speaking, your mistakes are

**[9:43]** the most expensive ones because if you

**[9:45]** screw up, you're screwing up at a level

**[9:47]** of hundreds of thousands or millions of

**[9:48]** tokens, maybe more. And the reason why

**[9:50]** is simple. You are doing bigger projects

**[9:53]** with AI. And when you do big projects

**[9:54]** with AI, your ability to leverage AI

**[9:57]** effectively becomes one of the most

**[10:00]** critical things you can do to manage ROI

**[10:02]** and cost on a particular project. It is

**[10:04]** a job skill at that level. If you're

**[10:06]** technical enough to go to a GitHub, you

**[10:08]** have a job skill to manage tokens

**[10:10]** efficiently. And you cannot pass that

**[10:12]** off to somebody else. That is not going

**[10:13]** to be somebody else's full-time job at

**[10:15]** an org. All of us are going to have to

**[10:16]** learn to manage our tokens. Well, if you

**[10:18]** were sitting there and you are you are

**[10:20]** the person who is responsible for the

**[10:22]** system prompt on an agent and you

**[10:23]** haven't pruned it in the last couple of

**[10:25]** weeks, what are you doing? If you

**[10:27]** haven't sat there and gone line by line

**[10:28]** and said, you know what, a hundred of

**[10:30]** these lines I don't need anymore because

**[10:32]** they've been here since 3.5 and like I

**[10:34]** don't need them now. If you're sitting

**[10:35]** there and you're like, I don't know why

**[10:37]** we're loading this entire repo into the

**[10:39]** context window. We just do it all the

**[10:40]** time and it seemed to work two

**[10:41]** generations ago but we never tested it.

**[10:43]** That's just irresponsible. You need to

**[10:45]** be in a position where you are actually

**[10:47]** allowing the gains in model intelligence

**[10:50]** to lean out your context window. If you

**[10:52]** want to look at the larger trend that we

**[10:55]** see in AI today, it is that we needed to

**[10:58]** frontload and be really specific about a

**[11:00]** lot of context for dumber models in

**[11:03]** 2025. And now that it's 2026, as the

**[11:05]** models get more intelligent, we can lean

**[11:08]** out the context window initially because

**[11:09]** we can trust the model to retrieve

**[11:12]** better. So take that seriously. That is

**[11:15]** something you can do that is practical

**[11:16]** to get ready for claude mythos. Don't

**[11:19]** sleep on it. This is again if you're

**[11:21]** technical, these are million token

**[11:22]** decisions we're talking about,

**[11:24]** especially if you're running this agent

**[11:25]** over and over again. It adds up. Let me

**[11:27]** give you a specific example that is

**[11:28]** based on the original beginner example

**[11:30]** with PDFs to show you the tangible

**[11:32]** difference in cost, right? And this is

**[11:34]** something that should cascade all the

**[11:35]** way across. If you don't believe me,

**[11:37]** this is real. Let's say you feed raw

**[11:39]** PDFs into context. Let's say it's a

**[11:41]** 100,000 tokens versus 5K like we talked

**[11:43]** about. Let's say it's a conversation

**[11:45]** sprawl that takes 30 turns. I've seen

**[11:47]** these like this is very realistic. And

**[11:49]** let's say you use Opus 4.6 for

**[11:51]** everything including formatting,

**[11:53]** including proof reading, and you're

**[11:54]** making something over a 5 hour session

**[11:56]** where you're talking back and forth. You

**[11:57]** might be spending roughly 800,000 to a

**[11:59]** million input tokens with maybe 150,000

**[12:02]** to 200,000 of output tokens including

**[12:05]** thinking. $5 in and $25 out per million.

**[12:08]** you're spending eight to$10 dollars

**[12:10]** worth of compute which you might say you

**[12:12]** know what I can tolerate that or I got

**[12:14]** the unlimited plan or I don't care

**[12:15]** whatever but I want you to look at the

**[12:17]** difference because anytime you start to

**[12:19]** get serious with AI you need to see the

**[12:21]** difference we talk about not being

**[12:22]** wasteful with artificial intelligence

**[12:24]** this is being wasteful you want to save

**[12:26]** water you want to save energy don't

**[12:28]** waste your tokens clean session same

**[12:30]** work convert documents to markdown first

**[12:33]** start fresh conversations every 10 to 15

**[12:35]** turns use opus for reasoning and sonnet

**[12:38]** for execution ution and haiku for polish

**[12:40]** and scope the context to what's needed

**[12:42]** and over the same period of time you get

**[12:45]** the same result for 100 to 150,000 input

**[12:48]** tokens a lot less and maybe 50 to 80,000

**[12:51]** output tokens you blend that across both

**[12:53]** models and instead of costing8 to$10 in

**[12:55]** compute you spend a buck and you got the

**[12:57]** same amount in other words you got an 8

**[12:59]** to10x reduction in cost now scale it

**[13:01]** right that sloppy user is burning 40 to

**[13:03]** 50 bucks in compute a week and the clean

**[13:05]** user is burning five to seven bucks a

**[13:08]** across a 10 person team on an API.

**[13:10]** That's 2,000 bucks a month versus 250

**[13:12]** bucks a month for the exact same result.

**[13:14]** For subscription users, it's the

**[13:15]** difference between hitting your limit

**[13:17]** daily and then forgetting that limits

**[13:18]** exist because you just are so

**[13:20]** productive. Now, if you think this isn't

**[13:21]** serious, I want you to think about the

**[13:23]** cost structure for Mythos for a minute.

**[13:24]** Mythos is rumored to be by far

**[13:26]** anthropic's most expensive model. I

**[13:28]** think very strongly by April or May we

**[13:30]** are going to have a new class of pricing

**[13:32]** well above $525 range for tokens into

**[13:37]** maybe 10x that right imagine a world

**[13:39]** where you are 10x what opus costs now $5

**[13:42]** in $25 out for opus what if it's $50 in

**[13:45]** $250 out for opus well now things start

**[13:47]** to get serious now that eight or 10x

**[13:50]** reduction on individual work for a day

**[13:53]** becomes something that you can actually

**[13:54]** measure and think about as a business

**[13:56]** and you imagine how big that gets When

**[13:58]** you start to work across a dev team, the

**[14:00]** mistakes you're making today were

**[14:01]** tolerable because models were priced

**[14:03]** cheaply when cutting edge intelligence

**[14:06]** that you want comes out more expensive.

**[14:08]** And I don't know the exact price, right?

**[14:10]** I'm not saying it's 50 and 250. I'm

**[14:12]** giving you a thought exercise. It might

**[14:14]** be 10 and 50 instead. It's still the

**[14:16]** same point. The point is the model that

**[14:19]** you want is going to cost more. And as

**[14:21]** models cost more, your mistakes scale.

**[14:24]** Your mistakes scale with the price of

**[14:26]** intelligence. And make no mistake, the

**[14:27]** models will keep getting better. Every

**[14:29]** quarter, every release, the trajectory

**[14:31]** is unambiguous. People who tell you the

**[14:33]** models are plateauing are lying. They

**[14:35]** are lying to you. The models are getting

**[14:37]** much faster. And I do see that

**[14:39]** occasionally that people are insisting

**[14:40]** that the models aren't getting better.

**[14:42]** It's not true by any measure out there.

**[14:43]** And the people that I see insisting on

**[14:45]** it, I think they're insisting on it

**[14:46]** partly because they don't want to face

**[14:49]** the world as it will exist when AI is

**[14:52]** this good and continuing to accelerate

**[14:54]** this fast. It's scary, right? We but we

**[14:56]** should face it and we can all work

**[14:57]** through it together.

**[14:58]** >> All right. I have built a stupid button.

**[15:00]** That is my contribution to this

**[15:02]** discourse. I am building a stupid button

**[15:04]** so you can check and see if you are

**[15:07]** using your context incorrectly. I want

**[15:09]** to save you money. I want to save you

**[15:10]** hundreds of dollars. Please do not be

**[15:12]** stupid with your tokens. You know, if if

**[15:14]** you care about it, don't waste the

**[15:16]** water. Don't waste the electricity. If

**[15:18]** you just care about the bottom line,

**[15:19]** also don't waste your bucks, right? We

**[15:21]** should probably care about all of those

**[15:22]** things. If you want to know like what's

**[15:24]** in Nate's stupid button, it's really

**[15:25]** simple. There's six questions that I'm

**[15:27]** helping you answer. Number one, do you

**[15:29]** feed Claude raw PDFs and images when all

**[15:32]** you need is text? Is there something you

**[15:34]** are doing that is grossly inefficient as

**[15:36]** far as tokens go? By the way,

**[15:38]** screenshots, terribly inefficient. It

**[15:40]** would be much, much better just to copy

**[15:41]** and paste text. Convert to markdown

**[15:44]** always. Claude can do it really, really

**[15:46]** fast for you. Why not? Question two.

**[15:49]** When was the last time you started a

**[15:51]** fresh conversation? Are you one of those

**[15:52]** people that keeps a conversation going

**[15:54]** forever? I swear the number of people

**[15:57]** who keep their conversations going

**[15:58]** forever is highly correlated to the

**[16:00]** number of people who start experiencing

**[16:02]** symptoms of LLM psychosis. Why? Because

**[16:04]** models drift over time. They were never

**[16:05]** intended for that long a conversation.

**[16:07]** If you're having a longunning

**[16:08]** conversation, you're just in strange

**[16:10]** territory. When was the last time you

**[16:12]** started a fresh conversation? And why is

**[16:14]** that? Again, every time you take a turn

**[16:17]** in a conversation, you read it as

**[16:18]** sending one line back. But Claude or

**[16:21]** Chad GPT or Gemini reads it as sending

**[16:24]** the entire conversation back. And if

**[16:26]** you're wondering, is this something

**[16:27]** that's just for Claude? Nate's talking

**[16:28]** about Claude a lot. No, it's for Chad

**[16:30]** GPT, it's for Gemini, it's for Llama,

**[16:32]** it's for any LLM you're using. It's for

**[16:34]** Quen. This is how LLMs work. Don't waste

**[16:36]** it. Question three, are you using the

**[16:39]** most expensive model for everything? Are

**[16:41]** you using Opus? Are you using 5.4 on pro

**[16:43]** mode? Whatever your choice is, are you

**[16:46]** picking the most expensive model and

**[16:49]** just blindly using it regardless when

**[16:51]** the cheaper model may work better? This

**[16:53]** is especially important if you have

**[16:55]** production workloads, but it's also true

**[16:57]** for all of us. Like, if you're doing

**[16:59]** something that's a simple formatting

**[17:00]** task, don't depend on Opus for it. Don't

**[17:03]** depend on 5.4 for it. Use the models for

**[17:05]** what they're designed for. Don't bring a

**[17:07]** Ferrari to the grocery store. Question

**[17:09]** four, do you know what's loading in

**[17:11]** context before you even type? You can

**[17:13]** actually find this out. You can run

**[17:14]** slashcontext in cla code. By the way,

**[17:17]** you could look at the number of things

**[17:18]** that are loading. If you're in cloud

**[17:20]** code, if you don't know what that means,

**[17:22]** you can go to your Chad GBT or your

**[17:24]** cloud. You can see how many connectors

**[17:25]** you have available. You can see how many

**[17:27]** you've loaded up. You could be loading

**[17:30]** tens of thousands of tokens that you're

**[17:32]** not really aware of and not really

**[17:33]** using. If you enable Google Drive months

**[17:36]** ago and you never never ever use Google

**[17:38]** Drive, you just thought it was cool on

**[17:39]** the day it launched. Why? just drop it.

**[17:42]** There are so many examples like that

**[17:44]** where we see something cool, we add it,

**[17:45]** and we forget it's there. It's like a

**[17:47]** barnacle on a ship. It's going to slow

**[17:48]** you down. It's going to burn tokens. You

**[17:50]** don't need to have it. Audit. Audit your

**[17:53]** plugins. It matters. Next question. API

**[17:56]** builders, are you caching stable context

**[17:59]** so you don't reuse it? Prompt caching

**[18:01]** can give you a 90% discount on repeated

**[18:03]** content. Right. Cash hits on Opus cost

**[18:06]** 50 cents per million versus $5 per

**[18:08]** million standard. It makes a difference.

**[18:11]** Do not sit there and ignore prompt

**[18:13]** caching. Take it seriously. If your

**[18:15]** system prompt, your tool definitions,

**[18:16]** your reference documents aren't cached,

**[18:18]** what are you doing? This is not advanced

**[18:20]** stuff in 2026. You should just be doing

**[18:22]** it. In the last question, the stupid

**[18:24]** button test for this is a real button.

**[18:26]** By the way, I really built a stupid

**[18:28]** button. How are you handling web search?

**[18:29]** Are you letting Claude do web research

**[18:31]** the expensive way? People don't realize

**[18:33]** this, but if you call perplexity for a

**[18:36]** search, it tends to be much more token

**[18:39]** cheap than using claude natively. Now,

**[18:41]** Claude is addressing this. There are

**[18:42]** lots of ways to do claude search. You

**[18:44]** can actually use Claude to navigate

**[18:47]** through a browser. You can also directly

**[18:50]** search in the terminal and it will spin

**[18:51]** up something in the background that's a

**[18:53]** service and you can call something in

**[18:54]** like an MCP connector for perplexity.

**[18:56]** All different options you can use. This

**[18:58]** is broadly true. It's not just true for

**[19:00]** cloud. It's true for Chad GPT. is true

**[19:01]** for Gemini, etc. because MCP is magic.

**[19:04]** But if you are trying to do search, the

**[19:07]** larger point is that you should be doing

**[19:09]** search as cheaply as possible. If you

**[19:11]** just want quick results that are token

**[19:13]** efficient, it may be worth it to take

**[19:16]** the time to spin up an MCP and just have

**[19:18]** a dedicated service that just returns

**[19:20]** the search results. That's what I have

**[19:22]** found experimentally with perplexity and

**[19:23]** claude is that perplexity tends to burn

**[19:26]** something like 10 to 50,000 less tokens

**[19:30]** per search which is not a small number

**[19:32]** if you're doing complex search and it

**[19:34]** tends to be five times faster and it has

**[19:37]** structured citations. So this is not

**[19:39]** meant to be a perplexity plug. It's just

**[19:40]** a token management plug. Try it for

**[19:42]** yourself. But I got to say I like

**[19:45]** faster. I like citations. I like less

**[19:47]** tokens over a researchheavy session like

**[19:50]** a plug-in like that can save you a lot

**[19:51]** on the token side. And that's a larger

**[19:53]** call out. Like if you have ways to look

**[19:57]** at your token usage and to diagnose it,

**[19:59]** you're going to be smarter about it. And

**[20:01]** that's the whole point of the stupid

**[20:02]** button is like let's not fly blind here.

**[20:05]** Let's look at our actual token usage and

**[20:07]** let's actually make some good choices

**[20:08]** and let's optimize it. Now what's in

**[20:11]** this stupid button? Number one, there is

**[20:13]** a prompt. If you've never done this, if

**[20:15]** you're like, "What is an MCP server?" We

**[20:17]** got a prompt for you, right? A prompt

**[20:18]** you can run against your recent

**[20:20]** conversations that actually identifies

**[20:21]** the specific dumb things you

**[20:23]** specifically are doing. Like it will see

**[20:25]** which documents you're feeding raw. It

**[20:26]** will see your conversation spraw. It

**[20:28]** will look at model misuse. It will look

**[20:29]** at redundant context loading. It looks

**[20:32]** at your actual patterns and it will tell

**[20:34]** you what to fix first. So that's the

**[20:35]** easy version, right? Anyone can use it.

**[20:37]** Any plan, no setup required. Number two,

**[20:40]** a skill. This is an invocable skill that

**[20:43]** audits your cloud code or your desktop

**[20:45]** environment or any other environment. It

**[20:47]** could be it could be chat GPT etc.

**[20:49]** Skills are also translatable and it

**[20:51]** measures your per session token

**[20:53]** overhead. It will flag system prompt

**[20:55]** load. It will check your plug-in and

**[20:56]** your skill loading. It will give you a

**[20:58]** before and after before you make

**[21:00]** changes. Think of it as like you kind of

**[21:02]** need a gas tank for your tokens and gee,

**[21:04]** wouldn't it be nice to have one, right?

**[21:05]** So, it's like the gas tank skill. Number

**[21:07]** three, we built some guardrails. So

**[21:10]** guardrails will sit directly on your

**[21:12]** knowledge store. So if you're an open

**[21:13]** brain person, which is something we've

**[21:14]** been doing as a community, it will sit

**[21:16]** right on your open brain and you will

**[21:18]** stop burning tokens on input, which is a

**[21:22]** nice touch, right? Automatic markdown

**[21:23]** conversion for documents that are

**[21:25]** hitting the store. Index first retrieval

**[21:27]** instead of just dump and search. Uh

**[21:30]** context scoping that enables a sort of

**[21:32]** minimum viable context for the query.

**[21:34]** This is where token management stops

**[21:36]** just being a personal discipline and it

**[21:38]** becomes infrastructure that starts to

**[21:39]** maintain itself. And I think I'm really

**[21:41]** excited to see how the community

**[21:43]** continues to build on this because open

**[21:44]** brain is open source and we'll keep

**[21:46]** evolving it and improving it. But I

**[21:47]** wanted to make sure that we had rails

**[21:49]** that ensured we have responsible token

**[21:50]** usage for the open brain community. So

**[21:52]** look, I'm going to close by talking

**[21:54]** briefly about agents and context because

**[21:56]** agents burn hundreds of millions of

**[21:57]** tokens in some cases. We don't want to

**[21:59]** leave them out. How do we think about

**[22:01]** context management for agents? And I'm

**[22:03]** going to give you five commandments. I

**[22:05]** call it the keep it simple stupid

**[22:06]** commandments for agents. Number one,

**[22:09]** index your references. Right? If an

**[22:11]** agent is getting raw documents instead

**[22:13]** of relevant trunks, you've already

**[22:14]** failed. The entire point of retrieval is

**[22:17]** to scope what the model sees to what it

**[22:20]** needs. Dumping a full document set into

**[22:22]** the window on every agent call is wildly

**[22:26]** irresponsible. You can't do that just to

**[22:27]** give the agent context. Don't make the

**[22:29]** agent do work it doesn't need to do.

**[22:31]** Number two, please prepare your context

**[22:33]** for consumption. Pre-process,

**[22:35]** pre-summarized, pre-chunk it. A

**[22:37]** reference document should arrive in an

**[22:40]** agent's context, ready to be used, not

**[22:42]** ready to be read or processed. If the

**[22:46]** model's first several thousand tokens of

**[22:48]** reasoning are just spent dealing with

**[22:49]** the crappy pre-processing you did,

**[22:52]** you're not being a responsible agent

**[22:54]** builder. Number three, this is something

**[22:55]** we've mentioned before. I'm calling it

**[22:56]** out in the context of agents because

**[22:58]** it's so important for agent workflows.

**[23:00]** Please, please, please cash your stable

**[23:03]** context. System prompts, tool

**[23:04]** definitions, persona instructions,

**[23:06]** reference material, anything that is

**[23:08]** stable, all should be cashed at a 90%

**[23:11]** discount on cash hits. This is the

**[23:13]** lowest effort, highest impact

**[23:15]** optimization that you have on the table.

**[23:17]** If you're making thousands of agent

**[23:18]** calls a day and you're not cashing, it's

**[23:20]** just pouring money down the drain.

**[23:21]** Number four, scope every agent's contact

**[23:25]** to the minimum it needs. Right? A

**[23:27]** planning agent does not need your full

**[23:29]** codebase. Don't give it the full

**[23:30]** codebase. An editing agent doesn't need

**[23:32]** your project roadmap. Don't give it the

**[23:34]** project roadmap. You get the idea,

**[23:35]** right? Passing everything to every agent

**[23:37]** is architectural laziness and it has

**[23:40]** real costs both in tokens burn and

**[23:42]** frankly in degraded agent performance.

**[23:45]** Models perform worse when they're

**[23:46]** drowning in a relevant context. And by

**[23:48]** the way, if you're like, I'm not sure

**[23:49]** what the agent will need. Aren't the

**[23:51]** smarter agents supposed to find it? The

**[23:53]** answer is yes. But you will only do that

**[23:55]** efficiently if you give them a

**[23:57]** searchable repo that is pre-processed so

**[24:00]** they can go and get only the relevant

**[24:02]** slice of context. So take the time to do

**[24:04]** it right. Number five, measure what you

**[24:06]** burn. If you don't know your per call

**[24:09]** token cost, you're just optimizing

**[24:11]** without any information. Right? Please

**[24:14]** instrument your agent calls. Track your

**[24:16]** input tokens. Track your output tokens.

**[24:18]** Track your overall model mix and your

**[24:20]** cost ratio. You cannot improve what you

**[24:22]** do not measure. And most teams building

**[24:25]** agentic systems are thinking a lot about

**[24:28]** whether they are semantically correct,

**[24:30]** not whether they're functionally

**[24:31]** correct. There's a big difference. And

**[24:32]** they're thinking a lot about optimizing

**[24:34]** their system prompt. They're not

**[24:36]** thinking a ton about their model cost

**[24:39]** because most of the time the model cost

**[24:41]** is not what makes the project live or

**[24:43]** die. And I get that in this age in 2025,

**[24:45]** early 2026, with the cost we have today

**[24:48]** and the urgency from executives to build

**[24:50]** the $12 per run cost or whatever it's

**[24:53]** going to be is not going to make or

**[24:54]** break the ship. But plan for a world

**[24:56]** where the models are more expensive.

**[24:58]** Plan for a world where you have to scale

**[25:00]** up. Plan for a world where you have to

**[25:02]** be responsible and instrument. Now,

**[25:04]** stepping back, there's a cultural

**[25:06]** problem we need to acknowledge behind

**[25:07]** all of this. At some point in the last

**[25:10]** few months, burning tokens has become a

**[25:12]** badge of honor. And I get it. There is a

**[25:15]** degree to which you need to be burning

**[25:17]** tokens in order to do meaningful work in

**[25:20]** the age of AI. None of this is to say

**[25:21]** that I expect token consumption to go

**[25:24]** down. It won't. You need to be ready to

**[25:27]** burn those tokens. This is not an ask

**[25:29]** that you not do that. This is an ask

**[25:30]** that you do it efficiently. And so when

**[25:32]** Jensen sits there on stage and says

**[25:34]** $250,000 in token costs per developer

**[25:36]** and everyone like is shocked or rolls

**[25:38]** their eyes or whatever the reaction is,

**[25:40]** my reaction is I hope it's 250 grand in

**[25:42]** smart token costs. It's not the

**[25:44]** individual dollar amount for Jensen

**[25:46]** because he's got cash in the bank. It's

**[25:48]** whether the tokens were used well. It's

**[25:49]** whether it's smart tokens. So begin to

**[25:52]** think to yourself, yes, I need to be

**[25:54]** maxing out my cloud. There are people

**[25:56]** who like go into withdrawal when they

**[25:57]** don't get to use their cloud. I know

**[25:58]** people like that who are like, "Ah, I

**[26:00]** went to a movie and uh I couldn't use my

**[26:02]** cloud for a few hours. I feel like I

**[26:03]** missed out on my token limit." Touch

**[26:05]** some grass. It's going to be okay. But

**[26:07]** use your tokens well. Be efficient with

**[26:09]** your token usage. Know what you're

**[26:10]** spending it on. Don't spend it on silly

**[26:12]** stuff. Don't spend it on the PDFs that

**[26:14]** you have to convert. Actually spend it

**[26:16]** on meaningful work. And that is

**[26:17]** something that is a human problem. We

**[26:19]** need to be bold and audacious. These

**[26:21]** models are really good at stuff. So,

**[26:23]** let's get more bold, more audacious, and

**[26:25]** think bigger about what we can aim them

**[26:26]** at. Because if we can be more efficient,

**[26:28]** we can do a whole lot more cool and

**[26:30]** creative stuff with those tokens. That's

**[26:32]** why I built the internet a stupid bug.
