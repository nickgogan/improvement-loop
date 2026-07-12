# Transcript: I Love the Karpathy LLM Wiki but it Doesn't Scale. Here's What Does.

**URL:** https://www.youtube.com/watch?v=R-5_2nsF_ZM
**Segments:** 565
**Channel:** Cole Medin
**Duration:** 18:57
**Uploaded:** 2026-07-09

---

## Full Text

There are two very different kinds of AI agents in the world and right now it feels like everyone is hyper fixated on one of them, personal agents, like the one you're looking at right here. You're generally have a coding agent like Claude Code or Hermes or Open Claw running on your machine, helping you manage a bunch of interconnected markdown documents that make up your knowledge base. And so typically you'll have something like a Karpathy LLM Wiki for your organization. You have your index documents with your tagging and categorization and all of your entities. You're building this up over time with your agent. And don't get me wrong, personal agents are extremely powerful. This is mine you're looking at right here. I use it every single day. But also there is a line that has to be drawn where personal agents they don't scale. And really it's when you want to ship an agent to other people, you no longer can use the LLM Wiki locally running agent setup. It has to look totally different. And that's what I want to focus on in this video because I myself been doing of content on personal agents. And I feel like I haven't covered the other side of the coin enough recently. And so we'll talk about what this really looks like, why we have to fundamentally change our approach to building agents when we're shipping for other people. So let's first start by talking about why everyone is building personal agents or second brains in the way that they are. Then we'll get into how the architecture has to ship for production agents and how we can accomplish that. And so everything for a personal agent is markdown driven. It really doesn't matter what you build for yourself or what you use off the shelf like Hermes. It is always markdown. And the reason for that is for a personal agent, it's just the simplest and most flexible. It is so easy to build up your knowledge base over time as you're having conversations with your second brain and pulling in other information. The power here is keeping everything on your own system so it can be as accessible and fast as possible. And at this point we don't really care about governance or access control or a lot of the traceability and auditability that you need in production systems. And so, just keeping it as simple as possible. But, as soon as other people are using your agent, so many users at once, you have live data, you need to care about things like access control and retrieval at scale, that is when this just it doesn't cut it anymore. I mean, first of all, there's a reason we have databases in the first place. If you're managing everything with just markdown documents, your organization and search, even just creating all the files and managing all that is never going to scale. And also, second brains are actually quite expensive. Generally, you're using a coding agent SDK like Claude or Codex, and you're using it with your subscription. And so, when you go to production, you can't use that subscription anymore cuz it's only for personal use. And all of the system prompts and tooling and everything that you're dumping into your second brain and having it read through entire markdown documents, like it doesn't really matter how much you optimize it. It's really never going to cut it for how much you have to scale the retrieval and the cost optimizations in production. And so, that's where we get to our architecture here. What does it look like to ship an agent for others? We still want to have all the same benefits of a second brain where we can have user memories and we're able to organize information for the agent to retrieve well, but everything has to look different. And I also want to go into this by saying that this setup right here is way more common than personal agents. I think the reason people are so hyper-fixated on these right now, it's for good reason. It's that it's just so applicable to everybody. No matter what you do in your life, you can use a second brain to help you manage your job or your personal life. But, the thing is, almost anything that's really providing real business value is an agent that is shipped as a part of a platform to a production environment with other people logging in and talking to the agent. And that is the architecture that we're we're about right here. So, here we're using a database to scale. Markdown doesn't cut it anymore. We can't just have a Hermes or Claude code wiki for production agents. And there are two things that our database needs to store and handle for us and give our agent access to. We have the context retriever and agent memory. These are the two things that I'm going to focus on for the rest of the video here. And I'm going to be using Redis as a platform to drive all of this in this video, but really these ideas apply to any system you're going to create for a production agent. Because essentially what we have here is a wrapper over our database. It's the context layer for our agent. So, we have the context retriever. This is giving our agent access to our business data and telling it the format, helping it understand what it can query. And then the agent memory is the short-term and long-term memory for our customers. We want to build up intelligence of our users for the agent over time. So, for the demonstration that I have for you today, I'm going to be using Redis. This is the best platform that I could use for a demonstration of both the business context and the user memory all in one place because they recently put out Redis Iris. This is in preview right now, but it is extremely powerful. It really is the entire wrapper over Redis as the database to give your agents better access. So, we have the context retriever. This is how we allow our agent to understand and search through our data through an MCP server. Very, very neat. And then we have agent memory. This is for the short-term and long-term memory of our users and actually storing their memories in Redis as well. So, we'll talk about all this. I'll cover how it all works, but first I want to just give you the high-level overview here. And I will say that I am working with Redis on this video. They reached out to me and I've been looking for a database platform to use as an example for this exact video for a while now. And I've been seriously impressed by what they've released here with context retriever and agent memory. That's what we're going to be focusing on here. And again, you can take these ideas and apply them to any production system. This is just what gives the best explanation right now. So, going back to our database, this is our key-value store that houses a bunch of mock data for an e-commerce store. I picked this as the example because every single e-commerce store should have an agent to help you with analytics and a customer-facing one for support. And so, we have all of our information for our customers. This is just key-value pairs, nice and flexible and unstructured in Redis. This is obviously fake for each one of our users here. And then we have orders, and then we have products and shipments. So, this is all of the data that we want our agent to be able to search through to help users understand where their orders are, to perform analytics for the internal team, that kind of thing. And so, to build an agent on top of this, I've created a Pydantic AI agent. I'll link to this GitHub repo in the description as well. I still love using Pydantic AI for all of my production agents because coding agent SDKs, like the Claude agent SDK or Codex SDK, I know they're very popular now, but they're slow because they're made for longer agentic coding tasks, and they're also more token heavy. So, for anything that you're shipping to production, Pydantic AI is still my recommendation. So, this is a Pydantic AI agent that has access to the context retriever MCP that we'll cover more in a bit, and then also the tools to access the agent memory, all happening in the same Redis database using Redis Iris to access the database with both of these capabilities. And so, I already have this agent up and running. I'm not going to get into the code for it today cuz that's not the point of this video, but I'll show you how the context retriever and agent memory can work in tandem. This is the big payoff, and then we'll get more into how each of the individual components work. And so, I know this is a little bit of a silly demonstration. We don't have any user interface. There's also no authentication, so I have to say explicitly who I am, but obviously when you take this agent, like if you build with Pydantic AI and Redis Iris, you're going to build it into a front end and you're going to have authentication, so the agent knows who you are without you having to say so. But here for the demo, I'm saying it's Jordan Rivera, customer 1004. Why is my order late and can you handle it the way I asked last time? This is actually a pretty loaded request because it has to take advantage of memory to know what we mean by this and it needs to search through business data, specifically the orders for this specific customer. And there we go, we got the answer from the agent. Hi Jordan, here's the full picture of what's going on. And take a look at this, for the CLI tool I built here, I'm also listing out all the individual tools that the agent called in order to leverage the memory and the context layer for it. So everything going into Redis under the hood. So first, it searched through memories to find my preferences for order handling and then it got information on the customer and then also found the orders and used that to get the shipment. So we can watch the agent go through the different relationships that we have in Redis, which by the way, without context retriever, it'd be very hard for the agent to do this because there's no schema. Everything is just key-value pairs. And so that's one of the big things that context retriever does on top of Redis is it provides that structure. It's kind of like the metadata in a Karpathy LLM wiki. We're telling the agent the different ways that it can search and filter so it can access things more efficiently. And so we have information on the delayed orders and then you can see right here that your customer notes say you prefer reshipments over refunds. And so that specifically is a memory that it extracted in a prior interaction with this fictitious Jordan Rivera. So very, very powerful. It's really cool to see how quickly he was able to capture all of this information. Like a lot of context it had to load in order to give us this complete answer and it did it without having to spend tens of thousands of tokens. In fact, I don't even think it spent a thousand tokens to get this information. So, in order to break down all of this for you nice and simple, of course, like usual, I have an Excalidraw diagram. So, we'll use this to talk about the business data and the context retriever right now, and then we'll get into the agent memory in a little bit. But, I want to show you everything that happens under the hood just to get that one response that we saw in our CLI. And so, again, the context retriever is for the business data, things like the customers or orders. And so, the way that it works, when we start with our Redis database, everything is unstructured. The agent doesn't have a way to really know, what is the information that I can even search through, much less how do I search through it efficiently. And so, context retriever is helping us do both of those things. And so, when we set up a retriever service, it is going to essentially help us document and establish the structure for our agent. And it even takes it as far as creating an MCP server. I'll show you this in the Redis dashboard in a little bit, but it auto generates the tools. So, it builds the intelligence of our data, and then formulates that into these are the tools to filter through things and to search by text, all the operations that our agent needs to search through our database at scale. It does not matter how many records we have in our Redis database, it's going to be able to sift through everything cuz the tools allow it to search by user, filter by the status of an order, whatever it might need to do. And so, now going into the Redis dashboard, we have the context retriever service. And so, setting up a brand new service is very, very straightforward. So, I already have mine built right here for North Peak Support. So, this is my context retriever service. And you can see that it exposes an MCP endpoint. More on that in a second. But, when you first set it up, you have to define your entities. And this is really cool because this is another tie-back to the Karpathy LLM wiki. We provide structure to the agent by telling it the different core entities that it's going to be operating on when it is sifting through our data. And this maps pretty much one-to-one to the different tables that we have in our underlying Redis database. And so, going back here to the retriever, we have the customer entity, we have the product entity, but you can see we're starting to specify a schema here. We're building the structure as the context layer on top of the database, like the different types that we have, how things are related, so it can go through that kind of like you would do in a knowledge graph in a personal agent. There are a lot of ties that we can make here. And so, now that we have the entities defined, this is the intelligence part that I was talking about. After you work through the setup process to create those entities, it is automatically going to generate all of the MCP tools based on the different ways you're going to have to access the data, like filtering a customer by city, filtering by email, basically just tool for each one of the attributes, and then for other types, like the text type, we also have a full search capability. So, being able to find keywords within the customer or the product description, that kind of thing. And this is my favorite part of the entire platform, just having these tools auto-generated. And I'll show you, if we go back into our CLI here, I will do {slash} tools, and we can see that these are all the tools that are automatically loaded into the MCP server attached to my Pydantic AI agent. And by the way, getting the MCP server attached very, very straightforward. It's just like any other MCP server. You can, of course, if you want to read the documentation right here. I'll have that linked in the description as well. I literally just gave the documentation to my Claude code and told it to connect and authenticate the context retriever MCP, and it just one-shot the whole thing. So, very easy to get this incorporated, giving it immediate intelligent access to all of the underlying data. And so, for example, going back to the CLI here, I can ask it, "Show me every delayed order with its product and total. So, more of a back-end analytics question. You wouldn't want every user to search over other users, but you can imagine this being an agent for people on your team for the e-commerce platform. And so, there we go. Here are the five delayed orders across the system, and the powerful thing here is instead of having to read an index document and then search through other markdown documents or figure out the schema of the database and then query that, it just had to make a single tool call, one MCP tool to filter the order by status, and that gave it all the information that it needed, and we got our final answer. And then, another example here, do we have any support tickets mentioning a refund? So, one where we're going to have to do a text search because we're going to have to see, does the ticket include the word refund? And there we go. Search ticket by text, a single MCP call again, query with refund. Here are the five support tickets mentioning a refund. Super fast, super efficient. And so, in the end, what it comes down to is no matter what your agent needs access to in the database, there's an MCP tool for that. And if you find that for some reason there isn't a tool available to the agent that you find it needing, then you just work with the entities and the types to make it so that tool is surfaced to the agent. And so, with that, that's really everything for the context retriever. That's the middleman to give the agent business data access. Now, let's talk about the agent memory, which again is both the short-term and long-term memory for all interactions with our agent. So, I'll show you in just a second what this looks like in the database, but my favorite part about this entire system is the fact that we're storing the short-term memory for every single conversation. But then, Redis Iris, with their agent memory, automatically is running a background process that is extracting the key information from the short-term memory to promote it to long-term memory. This is also a very common technique in personal agents and second brains. You're working with your second brain to do things over time like creating plans and doing research, and you're extracting key findings and things you tell it to remember into that promoted memory like that memory.md file that's always given to the agent. So, there's a very similar idea here where we're just trying to extract the golden nuggets out of conversations so that we can store it in Redis and then have the agent recall that later. And so, we are using vectors here. So, it's more traditional rag with semantic search. That way we're able to scale and each individual user can have millions of memories and we're still going to be able to pull out the most important ones for that next conversation they have. So, back in our dashboard, our agent memory works just like context retriever where we create a service. This time though, it's not an MCP server, it's just an API endpoint. So, we have the endpoint, we have the API key, and I just use Claude code to build the tools into my Pydantic AI agent to access and build up the memories here. And so, everything is managed in our database just like our business data. So, we have the memory folder here, all the key-value pairs for memory. So, we have the session memory, this is our short-term memory, and then the background process is automatically promoting the important things to write here. These are our long-term memory. So, we have the vector, this is what our agent uses to search. It's not supposed to be human readable for us, but then we also have the text. And so, look at this, "User prefers reshipments over refunds for delayed orders." This is the demo I showed you earlier where I had that conversation, I said that this is how I want you to handle any of the delayed orders and now it's going to remember that going forward. So, any conversation in the future where I say, "Help me handle my order like last time" or something like that, it's going to find this memory and use that so that the agent operates better on my behalf. And so, going back into the CLI, I'll just do a new session here. So, it's {slash} new session and then, "Hi, I'm Jordan and whenever an order of mine is delayed, always reship it expedited instead of refunding me." So, usually a user is not going to be this explicit in asking it to remember a fact, but this is just for the sake of demo. The agent Redis Iverson is still going to be able to extract key memories even if you're not being that explicit. And so, going into a brand new conversation here to prove that there's no short-term memory guiding this, we're going to ask it about our preferences, and it's going to quickly pull the memories and tell us everything we need to know. Like right here, summary of everything I know from our prior conversations. We have the identity, which of course could come from authentication as well, and it should in production. Past orders, support tickets, and preferences. You strongly prefer reshipments over refunds. That's the golden nugget right there. And the best part about all this with Redis Iris is if you don't use that as a platform, like of course the ideas still apply to whatever you might build in your own infrastructure, but you have to maintain the process that extract these memories. You have to build the tooling for the search. We can also delete memories here as well. The entire layer of memory management is just handled for you, but you have full control and visibility at the same time. Because everything is just in your Redis database. And so, there you go. That's everything you need to know on what it takes to build the architecture for production agents. And Redis Iris is a phenomenal platform. I'll link to them in the description. They just give the best idea of how you build that layer on top of your database to give your agent access and structure while still keeping your underlying data flexible. And remember, you don't need this for personal agents. LLM Wiki, if using Hermes or Claude code or whatever with Obsidian, like that's actually ideal to keep things simple and flexible. But as soon as you go into production, this is what you need. As soon as you have other people using your agent. And I'm going to keep making content on both of these lanes here. They're both super important. And so, if you appreciate this video and you're looking forward to more things on AI coding and building and shipping agents, I'd really appreciate a like and a subscribe. And with that, I will see you in the next video.

---

## Timestamped Segments

**[0:00]** There are two very different kinds of AI

**[0:02]** agents in the world and right now it

**[0:04]** feels like everyone is hyper fixated on

**[0:06]** one of them, personal agents, like the

**[0:08]** one you're looking at right here. You're

**[0:10]** generally have a coding agent like

**[0:11]** Claude Code or Hermes or Open Claw

**[0:14]** running on your machine, helping you

**[0:15]** manage a bunch of interconnected

**[0:17]** markdown documents that make up your

**[0:19]** knowledge base. And so typically you'll

**[0:21]** have something like a Karpathy LLM Wiki

**[0:23]** for your organization. You have your

**[0:25]** index documents with your tagging and

**[0:27]** categorization and all of your entities.

**[0:30]** You're building this up over time with

**[0:31]** your agent. And don't get me wrong,

**[0:33]** personal agents are extremely powerful.

**[0:36]** This is mine you're looking at right

**[0:37]** here. I use it every single day. But

**[0:39]** also there is a line that has to be

**[0:42]** drawn where personal agents they don't

**[0:44]** scale. And really it's when you want to

**[0:47]** ship an agent to other people, you no

**[0:49]** longer can use the LLM Wiki locally

**[0:52]** running agent setup. It has to look

**[0:54]** totally different. And that's what I

**[0:56]** want to focus on in this video because I

**[0:58]** myself been doing of content on personal

**[1:01]** agents. And I feel like I haven't

**[1:03]** covered the other side of the coin

**[1:05]** enough recently. And so we'll talk about

**[1:07]** what this really looks like, why we have

**[1:09]** to fundamentally change our approach to

**[1:11]** building agents when we're shipping for

**[1:13]** other people. So let's first start by

**[1:15]** talking about why everyone is building

**[1:17]** personal agents or second brains in the

**[1:19]** way that they are. Then we'll get into

**[1:21]** how the architecture has to ship for

**[1:23]** production agents and how we can

**[1:25]** accomplish that. And so everything for a

**[1:28]** personal agent is markdown driven. It

**[1:30]** really doesn't matter what you build for

**[1:32]** yourself or what you use off the shelf

**[1:34]** like Hermes. It is always markdown. And

**[1:36]** the reason for that is for a personal

**[1:38]** agent, it's just the simplest and most

**[1:41]** flexible. It is so easy to build up your

**[1:43]** knowledge base over time as you're

**[1:45]** having conversations with your second

**[1:47]** brain and pulling in other information.

**[1:49]** The power here is keeping everything on

**[1:51]** your own system so it can be as

**[1:53]** accessible and fast as possible. And at

**[1:55]** this point we don't really care about

**[1:57]** governance or access control or a lot of

**[2:00]** the traceability and auditability that

**[2:01]** you need in production systems. And so,

**[2:03]** just keeping it as simple as possible.

**[2:06]** But, as soon as other people are using

**[2:08]** your agent, so many users at once, you

**[2:10]** have live data, you need to care about

**[2:12]** things like access control and retrieval

**[2:14]** at scale, that is when this just it

**[2:16]** doesn't cut it anymore. I mean, first of

**[2:18]** all, there's a reason we have databases

**[2:20]** in the first place. If you're managing

**[2:21]** everything with just markdown documents,

**[2:24]** your organization and search, even just

**[2:26]** creating all the files and managing all

**[2:28]** that is never going to scale. And also,

**[2:30]** second brains are actually quite

**[2:31]** expensive. Generally, you're using a

**[2:34]** coding agent SDK like Claude or Codex,

**[2:36]** and you're using it with your

**[2:38]** subscription. And so, when you go to

**[2:40]** production, you can't use that

**[2:42]** subscription anymore cuz it's only for

**[2:44]** personal use. And all of the system

**[2:46]** prompts and tooling and everything that

**[2:47]** you're dumping into your second brain

**[2:49]** and having it read through entire

**[2:51]** markdown documents, like it doesn't

**[2:52]** really matter how much you optimize it.

**[2:54]** It's really never going to cut it for

**[2:56]** how much you have to scale the retrieval

**[2:58]** and the cost optimizations in

**[3:00]** production. And so, that's where we get

**[3:03]** to our architecture here. What does it

**[3:04]** look like to ship an agent for others?

**[3:07]** We still want to have all the same

**[3:08]** benefits of a second brain where we can

**[3:10]** have user memories and we're able to

**[3:12]** organize information for the agent to

**[3:14]** retrieve well, but everything has to

**[3:16]** look different. And I also want to go

**[3:18]** into this by saying that this setup

**[3:20]** right here is way more common than

**[3:22]** personal agents. I think the reason

**[3:24]** people are so hyper-fixated on these

**[3:25]** right now, it's for good reason. It's

**[3:28]** that it's just so applicable to

**[3:29]** everybody. No matter what you do in your

**[3:31]** life, you can use a second brain to help

**[3:33]** you manage your job or your personal

**[3:35]** life. But, the thing is, almost anything

**[3:38]** that's really providing real business

**[3:40]** value is an agent that is shipped as a

**[3:42]** part of a platform to a production

**[3:44]** environment with other people logging in

**[3:46]** and talking to the agent. And that is

**[3:48]** the architecture that we're we're about

**[3:50]** right here. So, here we're using a

**[3:52]** database to scale. Markdown doesn't cut

**[3:55]** it anymore. We can't just have a Hermes

**[3:57]** or Claude code wiki for production

**[3:59]** agents. And there are two things that

**[4:01]** our database needs to store and handle

**[4:03]** for us and give our agent access to. We

**[4:06]** have the context retriever and agent

**[4:08]** memory. These are the two things that

**[4:09]** I'm going to focus on for the rest of

**[4:11]** the video here. And I'm going to be

**[4:12]** using Redis as a platform to drive all

**[4:16]** of this in this video, but really these

**[4:18]** ideas apply to any system you're going

**[4:20]** to create for a production agent.

**[4:21]** Because essentially what we have here is

**[4:24]** a wrapper over our database. It's the

**[4:26]** context layer for our agent. So, we have

**[4:29]** the context retriever. This is giving

**[4:32]** our agent access to our business data

**[4:35]** and telling it the format, helping it

**[4:36]** understand what it can query. And then

**[4:38]** the agent memory is the short-term and

**[4:41]** long-term memory for our customers. We

**[4:43]** want to build up intelligence of our

**[4:45]** users for the agent over time. So, for

**[4:48]** the demonstration that I have for you

**[4:49]** today, I'm going to be using Redis. This

**[4:51]** is the best platform that I could use

**[4:53]** for a demonstration of both the business

**[4:56]** context and the user memory all in one

**[4:59]** place because they recently put out

**[5:01]** Redis Iris. This is in preview right

**[5:03]** now, but it is extremely powerful. It

**[5:05]** really is the entire wrapper over Redis

**[5:08]** as the database to give your agents

**[5:10]** better access. So, we have the context

**[5:12]** retriever. This is how we allow our

**[5:14]** agent to understand and search through

**[5:16]** our data through an MCP server. Very,

**[5:18]** very neat. And then we have agent

**[5:20]** memory. This is for the short-term and

**[5:21]** long-term memory of our users and

**[5:24]** actually storing their memories in Redis

**[5:26]** as well. So, we'll talk about all this.

**[5:27]** I'll cover how it all works, but first I

**[5:30]** want to just give you the high-level

**[5:32]** overview here. And I will say that I am

**[5:34]** working with Redis on this video. They

**[5:36]** reached out to me and I've been looking

**[5:38]** for a database platform to use as an

**[5:40]** example for this exact video for a while

**[5:43]** now. And I've been seriously impressed

**[5:46]** by what they've released here with

**[5:47]** context retriever and agent memory.

**[5:49]** That's what we're going to be focusing

**[5:50]** on here. And again, you can take these

**[5:52]** ideas and apply them to any production

**[5:54]** system. This is just what gives the best

**[5:57]** explanation right now. So, going back to

**[5:59]** our database, this is our key-value

**[6:01]** store that houses a bunch of mock data

**[6:03]** for an e-commerce store. I picked this

**[6:05]** as the example because every single

**[6:07]** e-commerce store should have an agent to

**[6:09]** help you with analytics and a

**[6:10]** customer-facing one for support. And so,

**[6:13]** we have all of our information for our

**[6:15]** customers. This is just key-value pairs,

**[6:17]** nice and flexible and unstructured in

**[6:18]** Redis. This is obviously fake for each

**[6:20]** one of our users here. And then we have

**[6:22]** orders, and then we have products and

**[6:25]** shipments. So, this is all of the data

**[6:27]** that we want our agent to be able to

**[6:28]** search through to help users understand

**[6:31]** where their orders are, to perform

**[6:32]** analytics for the internal team, that

**[6:35]** kind of thing. And so, to build an agent

**[6:37]** on top of this, I've created a Pydantic

**[6:40]** AI agent. I'll link to this GitHub repo

**[6:43]** in the description as well. I still love

**[6:46]** using Pydantic AI for all of my

**[6:48]** production agents because coding agent

**[6:50]** SDKs, like the Claude agent SDK or Codex

**[6:52]** SDK, I know they're very popular now,

**[6:54]** but they're slow because they're made

**[6:56]** for longer agentic coding tasks, and

**[6:58]** they're also more token heavy. So, for

**[7:00]** anything that you're shipping to

**[7:01]** production, Pydantic AI is still my

**[7:03]** recommendation. So, this is a Pydantic

**[7:05]** AI agent that has access to the context

**[7:08]** retriever MCP that we'll cover more in a

**[7:10]** bit, and then also the tools to access

**[7:12]** the agent memory, all happening in the

**[7:15]** same Redis database using Redis Iris to

**[7:18]** access the database with both of these

**[7:20]** capabilities. And so, I already have

**[7:22]** this agent up and running. I'm not going

**[7:23]** to get into the code for it today cuz

**[7:25]** that's not the point of this video, but

**[7:26]** I'll show you how the context retriever

**[7:28]** and agent memory can work in tandem.

**[7:30]** This is the big payoff, and then we'll

**[7:32]** get more into how each of the individual

**[7:34]** components work. And so, I know this is

**[7:36]** a little bit of a silly demonstration.

**[7:38]** We don't have any user interface.

**[7:40]** There's also no authentication, so I

**[7:42]** have to say explicitly who I am, but

**[7:44]** obviously when you take this agent, like

**[7:46]** if you build with Pydantic AI and Redis

**[7:48]** Iris, you're going to build it into a

**[7:50]** front end and you're going to have

**[7:51]** authentication, so the agent knows who

**[7:53]** you are without you having to say so.

**[7:55]** But here for the demo, I'm saying it's

**[7:57]** Jordan Rivera, customer 1004. Why is my

**[8:00]** order late and can you handle it the way

**[8:02]** I asked last time? This is actually a

**[8:04]** pretty loaded request because it has to

**[8:06]** take advantage of memory to know what we

**[8:08]** mean by this and it needs to search

**[8:11]** through business data, specifically the

**[8:13]** orders for this specific customer. And

**[8:15]** there we go, we got the answer from the

**[8:17]** agent. Hi Jordan, here's the full

**[8:18]** picture of what's going on. And take a

**[8:20]** look at this, for the CLI tool I built

**[8:21]** here, I'm also listing out all the

**[8:23]** individual tools that the agent called

**[8:25]** in order to leverage the memory and the

**[8:27]** context layer for it. So everything

**[8:29]** going into Redis under the hood. So

**[8:31]** first, it searched through memories to

**[8:33]** find my preferences for order handling

**[8:35]** and then it got information on the

**[8:36]** customer and then also found the orders

**[8:38]** and used that to get the shipment. So we

**[8:40]** can watch the agent go through the

**[8:42]** different relationships that we have in

**[8:44]** Redis, which by the way, without context

**[8:46]** retriever, it'd be very hard for the

**[8:48]** agent to do this because there's no

**[8:50]** schema. Everything is just key-value

**[8:52]** pairs. And so that's one of the big

**[8:54]** things that context retriever does on

**[8:56]** top of Redis is it provides that

**[8:57]** structure. It's kind of like the

**[8:59]** metadata in a Karpathy LLM wiki. We're

**[9:02]** telling the agent the different ways

**[9:04]** that it can search and filter so it can

**[9:05]** access things more efficiently. And so

**[9:07]** we have information on the delayed

**[9:09]** orders and then you can see right here

**[9:10]** that your customer notes say you prefer

**[9:12]** reshipments over refunds. And so that

**[9:15]** specifically is a memory that it

**[9:17]** extracted in a prior interaction with

**[9:20]** this fictitious Jordan Rivera. So very,

**[9:22]** very powerful. It's really cool to see

**[9:24]** how quickly he was able to capture all

**[9:26]** of this information. Like a lot of

**[9:28]** context it had to load in order to give

**[9:30]** us this complete answer and it did it

**[9:32]** without having to spend tens of

**[9:34]** thousands of tokens. In fact, I don't

**[9:36]** even think it spent a thousand tokens to

**[9:38]** get this information. So, in order to

**[9:40]** break down all of this for you nice and

**[9:42]** simple, of course, like usual, I have an

**[9:44]** Excalidraw diagram. So, we'll use this

**[9:46]** to talk about the business data and the

**[9:49]** context retriever right now, and then

**[9:51]** we'll get into the agent memory in a

**[9:52]** little bit. But, I want to show you

**[9:53]** everything that happens under the hood

**[9:55]** just to get that one response that we

**[9:57]** saw in our CLI. And so, again, the

**[10:00]** context retriever is for the business

**[10:02]** data, things like the customers or

**[10:04]** orders. And so, the way that it works,

**[10:06]** when we start with our Redis database,

**[10:08]** everything is unstructured. The agent

**[10:10]** doesn't have a way to really know, what

**[10:11]** is the information that I can even

**[10:13]** search through, much less how do I

**[10:15]** search through it efficiently. And so,

**[10:17]** context retriever is helping us do both

**[10:19]** of those things. And so, when we set up

**[10:21]** a retriever service, it is going to

**[10:23]** essentially help us document and

**[10:26]** establish the structure for our agent.

**[10:28]** And it even takes it as far as creating

**[10:31]** an MCP server. I'll show you this in the

**[10:33]** Redis dashboard in a little bit, but it

**[10:36]** auto generates the tools. So, it builds

**[10:38]** the intelligence of our data, and then

**[10:40]** formulates that into these are the tools

**[10:42]** to filter through things and to search

**[10:44]** by text, all the operations that our

**[10:46]** agent needs to search through our

**[10:48]** database at scale. It does not matter

**[10:50]** how many records we have in our Redis

**[10:52]** database, it's going to be able to sift

**[10:54]** through everything cuz the tools allow

**[10:55]** it to search by user, filter by the

**[10:59]** status of an order, whatever it might

**[11:00]** need to do. And so, now going into the

**[11:03]** Redis dashboard, we have the context

**[11:05]** retriever service. And so, setting up a

**[11:07]** brand new service is very, very

**[11:09]** straightforward. So, I already have mine

**[11:10]** built right here for North Peak Support.

**[11:13]** So, this is my context retriever

**[11:15]** service. And you can see that it exposes

**[11:18]** an MCP endpoint. More on that in a

**[11:20]** second. But, when you first set it up,

**[11:22]** you have to define your entities. And

**[11:25]** this is really cool because this is

**[11:26]** another tie-back to the Karpathy LLM

**[11:29]** wiki. We provide structure to the agent

**[11:32]** by telling it the different core

**[11:33]** entities that it's going to be operating

**[11:35]** on when it is sifting through our data.

**[11:38]** And this maps pretty much one-to-one to

**[11:40]** the different tables that we have in our

**[11:42]** underlying Redis database. And so, going

**[11:45]** back here to the retriever, we have the

**[11:47]** customer entity, we have the product

**[11:49]** entity, but you can see we're starting

**[11:51]** to specify a schema here. We're building

**[11:54]** the structure as the context layer on

**[11:56]** top of the database, like the different

**[11:58]** types that we have, how things are

**[12:00]** related, so it can go through that kind

**[12:01]** of like you would do in a knowledge

**[12:03]** graph in a personal agent. There are a

**[12:05]** lot of ties that we can make here.

**[12:08]** And so, now that we have the entities

**[12:09]** defined, this is the intelligence part

**[12:11]** that I was talking about. After you work

**[12:13]** through the setup process to create

**[12:16]** those entities, it is automatically

**[12:18]** going to generate all of the MCP tools

**[12:20]** based on the different ways you're going

**[12:22]** to have to access the data, like

**[12:24]** filtering a customer by city, filtering

**[12:26]** by email, basically just tool for each

**[12:28]** one of the attributes, and then for

**[12:30]** other types, like the text type, we also

**[12:32]** have a full search capability. So, being

**[12:34]** able to find keywords within the

**[12:36]** customer or the product description,

**[12:38]** that kind of thing. And this is my

**[12:40]** favorite part of the entire platform,

**[12:42]** just having these tools auto-generated.

**[12:44]** And I'll show you, if we go back into

**[12:45]** our CLI here, I will do {slash} tools,

**[12:48]** and we can see that these are all the

**[12:50]** tools that are automatically loaded into

**[12:51]** the MCP server attached to my Pydantic

**[12:54]** AI agent. And by the way, getting the

**[12:56]** MCP server attached very, very

**[12:58]** straightforward. It's just like any

**[12:59]** other MCP server. You can, of course, if

**[13:01]** you want to read the documentation right

**[13:04]** here. I'll have that linked in the

**[13:05]** description as well. I literally just

**[13:07]** gave the documentation to my Claude code

**[13:10]** and told it to connect and authenticate

**[13:12]** the context retriever MCP, and it just

**[13:14]** one-shot the whole thing. So, very easy

**[13:16]** to get this incorporated, giving it

**[13:18]** immediate intelligent access to all of

**[13:20]** the underlying data. And so, for

**[13:22]** example, going back to the CLI here, I

**[13:24]** can ask it, "Show me every delayed order

**[13:26]** with its product and total. So, more of

**[13:28]** a back-end analytics question. You

**[13:30]** wouldn't want every user to search over

**[13:32]** other users, but you can imagine this

**[13:34]** being an agent for people on your team

**[13:36]** for the e-commerce platform. And so,

**[13:37]** there we go. Here are the five delayed

**[13:39]** orders across the system, and the

**[13:41]** powerful thing here is instead of having

**[13:43]** to read an index document and then

**[13:44]** search through other markdown documents

**[13:46]** or figure out the schema of the database

**[13:48]** and then query that, it just had to make

**[13:50]** a single tool call, one MCP tool to

**[13:53]** filter the order by status, and that

**[13:55]** gave it all the information that it

**[13:56]** needed, and we got our final answer. And

**[13:58]** then, another example here, do we have

**[14:00]** any support tickets mentioning a refund?

**[14:02]** So, one where we're going to have to do

**[14:03]** a text search because we're going to

**[14:05]** have to see, does the ticket include the

**[14:06]** word refund? And there we go. Search

**[14:08]** ticket by text, a single MCP call again,

**[14:11]** query with refund. Here are the five

**[14:13]** support tickets mentioning a refund.

**[14:15]** Super fast, super efficient. And so, in

**[14:18]** the end, what it comes down to is no

**[14:19]** matter what your agent needs access to

**[14:21]** in the database, there's an MCP tool for

**[14:23]** that. And if you find that for some

**[14:25]** reason there isn't a tool available to

**[14:26]** the agent that you find it needing, then

**[14:28]** you just work with the entities and the

**[14:30]** types to make it so that tool is

**[14:31]** surfaced to the agent. And so, with

**[14:34]** that, that's really everything for the

**[14:35]** context retriever. That's the middleman

**[14:38]** to give the agent business data access.

**[14:40]** Now, let's talk about the agent memory,

**[14:42]** which again is both the short-term and

**[14:44]** long-term memory for all interactions

**[14:46]** with our agent. So, I'll show you in

**[14:48]** just a second what this looks like in

**[14:50]** the database, but my favorite part about

**[14:52]** this entire system is the fact that

**[14:54]** we're storing the short-term memory for

**[14:56]** every single conversation. But then,

**[14:58]** Redis Iris, with their agent memory,

**[15:01]** automatically is running a background

**[15:03]** process that is extracting the key

**[15:05]** information from the short-term memory

**[15:08]** to promote it to long-term memory. This

**[15:10]** is also a very common technique in

**[15:12]** personal agents and second brains.

**[15:14]** You're working with your second brain to

**[15:16]** do things over time like creating plans

**[15:18]** and doing research, and you're

**[15:19]** extracting key findings and things you

**[15:21]** tell it to remember into that promoted

**[15:23]** memory like that memory.md file that's

**[15:26]** always given to the agent. So, there's a

**[15:27]** very similar idea here where we're just

**[15:29]** trying to extract the golden nuggets out

**[15:31]** of conversations so that we can store it

**[15:33]** in Redis and then have the agent recall

**[15:35]** that later. And so, we are using vectors

**[15:38]** here. So, it's more traditional rag with

**[15:40]** semantic search. That way we're able to

**[15:42]** scale and each individual user can have

**[15:44]** millions of memories and we're still

**[15:46]** going to be able to pull out the most

**[15:48]** important ones for that next

**[15:49]** conversation they have. So, back in our

**[15:51]** dashboard, our agent memory works just

**[15:53]** like context retriever where we create a

**[15:55]** service. This time though, it's not an

**[15:57]** MCP server, it's just an API endpoint.

**[16:00]** So, we have the endpoint, we have the

**[16:01]** API key, and I just use Claude code to

**[16:03]** build the tools into my Pydantic AI

**[16:05]** agent to access and build up the

**[16:07]** memories here. And so, everything is

**[16:09]** managed in our database just like our

**[16:12]** business data. So, we have the memory

**[16:14]** folder here, all the key-value pairs for

**[16:16]** memory. So, we have the session memory,

**[16:17]** this is our short-term memory, and then

**[16:19]** the background process is automatically

**[16:21]** promoting the important things to write

**[16:23]** here. These are our long-term memory.

**[16:25]** So, we have the vector, this is what our

**[16:27]** agent uses to search. It's not supposed

**[16:29]** to be human readable for us, but then we

**[16:31]** also have the text. And so, look at

**[16:32]** this, "User prefers reshipments over

**[16:35]** refunds for delayed orders." This is the

**[16:38]** demo I showed you earlier where I had

**[16:40]** that conversation, I said that this is

**[16:41]** how I want you to handle any of the

**[16:43]** delayed orders and now it's going to

**[16:45]** remember that going forward. So, any

**[16:46]** conversation in the future where I say,

**[16:48]** "Help me handle my order like last time"

**[16:50]** or something like that, it's going to

**[16:52]** find this memory and use that so that

**[16:54]** the agent operates better on my behalf.

**[16:56]** And so, going back into the CLI, I'll

**[16:58]** just do a new session here. So, it's

**[16:59]** {slash} new session and then, "Hi, I'm

**[17:01]** Jordan and whenever an order of mine is

**[17:03]** delayed, always reship it expedited

**[17:05]** instead of refunding me." So, usually a

**[17:07]** user is not going to be this explicit in

**[17:09]** asking it to remember a fact, but this

**[17:11]** is just for the sake of demo. The agent

**[17:13]** Redis Iverson is still going to be able

**[17:14]** to extract key memories even if you're

**[17:16]** not being that explicit. And so, going

**[17:18]** into a brand new conversation here to

**[17:20]** prove that there's no short-term memory

**[17:22]** guiding this, we're going to ask it

**[17:23]** about our preferences, and it's going to

**[17:25]** quickly pull the memories and tell us

**[17:26]** everything we need to know. Like right

**[17:28]** here, summary of everything I know from

**[17:29]** our prior conversations. We have the

**[17:31]** identity, which of course could come

**[17:32]** from authentication as well, and it

**[17:33]** should in production. Past orders,

**[17:35]** support tickets, and preferences. You

**[17:37]** strongly prefer reshipments over

**[17:39]** refunds. That's the golden nugget right

**[17:42]** there. And the best part about all this

**[17:44]** with Redis Iris is if you don't use that

**[17:46]** as a platform, like of course the ideas

**[17:48]** still apply to whatever you might build

**[17:49]** in your own infrastructure, but you have

**[17:51]** to maintain the process that extract

**[17:53]** these memories. You have to build the

**[17:55]** tooling for the search. We can also

**[17:56]** delete memories here as well. The entire

**[17:59]** layer of memory management is just

**[18:00]** handled for you, but you have full

**[18:02]** control and visibility at the same time.

**[18:04]** Because everything is just in your Redis

**[18:06]** database. And so, there you go. That's

**[18:08]** everything you need to know on what it

**[18:10]** takes to build the architecture for

**[18:11]** production agents. And Redis Iris is a

**[18:14]** phenomenal platform. I'll link to them

**[18:15]** in the description. They just give the

**[18:17]** best idea of how you build that layer on

**[18:20]** top of your database to give your agent

**[18:23]** access and structure while still keeping

**[18:25]** your underlying data flexible.

**[18:27]** And remember, you don't need this for

**[18:28]** personal agents. LLM Wiki, if using

**[18:31]** Hermes or Claude code or whatever with

**[18:32]** Obsidian, like that's actually ideal to

**[18:34]** keep things simple and flexible. But as

**[18:37]** soon as you go into production, this is

**[18:39]** what you need. As soon as you have other

**[18:40]** people using your agent. And I'm going

**[18:42]** to keep making content on both of these

**[18:44]** lanes here. They're both super

**[18:46]** important. And so, if you appreciate

**[18:48]** this video and you're looking forward to

**[18:49]** more things on AI coding and building

**[18:51]** and shipping agents, I'd really

**[18:52]** appreciate a like and a subscribe. And

**[18:54]** with that, I will see you in the next

**[18:55]** video.
