# Transcript: jwtpMSRAPAQ

**URL:** https://www.youtube.com/watch?v=jwtpMSRAPAQ
**Segments:** 727

---

## Full Text

Let me tell you why I'm excited about this whole implementation challenge for agents. People think it's an agent story. It's actually the story of finance changing what it believes is the model of software in the future. And at the same time, the story of hyperscalers finding out what doesn't work. And at the same time, the story of companies figuring out where the disproportionate value in AI is. All of these forces are converging on this private equity-driven services deployment model that we're going to talk about today. It's so cool. So, private equity for a long time had this saying, it's a real saying, you can ask a financier that you know, that that SaaS companies all taste like chicken. In other words, all SaaS companies are the same from a balance sheet perspective. They all have the same growth characteristics, the same numbers, they're very easy to analyze, that makes them ideal as an investment vehicle until recently, when of course, SaaS company growth metrics and profitability all went to hell in a handbasket because they could not figure out how to make themselves relevant in a world where AI agents were taking over. This puts competitive pressure on the PE investment firms because I cannot tell you the number of PEs who have funds that are dated 26, 27, 28, who are wrestling with the with the challenge of trying to understand how they will sell these companies that when they bought them were good healthy SaaS companies and now are on the rocks or in danger. They don't have an answer. And so, that's why they are interested in pivoting into agentic workflows. Meanwhile, hyperscalers are realizing they cannot just sit in fancy brick-walled Silicon Valley conference rooms and talk cleverly about how AI is helpful and easy to implement and not be out in the trenches. They are realizing that Palantir is right. You have to have forward-deployed engineers who have to sit in the weeds with customers and figure out how this works. Open AI figured it out, Anthropic figured it out, and they realize they have a new business model for this. They're not equipped for this, and so they're starting to do joint ventures, and they're starting to look for capital to do that. Because, of course, what's the thing with hyperscalers? They are capital constrained. Anthropic is, OpenAI is. I do not care if they have raised more capital than just about any company in history. They are still capital constrained because of the tremendous costs of reaching AGI, of getting GPUs, of model training, etc., of serving models increasingly. So, they have to partner up. They have to find finance. Private equity is there with the finance. That's sort of how the incentives align for those two. And they're all aimed at the third player in this market, the company. The company is realizing, and I'm talking about the company as in Fortune 500 firms, SMB firms. I am talking about people who did not understand the difference between a chat and an agent just a few months ago. Something happened in December, and it's been accelerating since, and people who I have talked to, who have been in Copilot chat mode for years, are now understanding what agents can do because agents got that much more valuable. And they're desperate to put them to work in real use cases, and they know they don't have the expertise, they know they don't understand how agents work well, but they know they can get it done cuz they've seen enough examples in their own work. And I want to be very clear here. The value we're talking about is trillions of dollars. It It's because agents can do an entire workflow. And And there's disproportionate value in getting to 100% on that. And getting to 100% on an entire workflow is a new phenomenon. It is a 2026 spring phenomenon that you can do that reliably, clearly, at scale, and repeatably. That didn't used to be the case. It's brand new. It is super cool, and it means that these companies see enough of agents to know they can do this, know they have a lot of places to apply it, and know they they need help. And so, they are turning to these new companies saying, "OpenAI, Anthropic, somebody, please help us. Sit someone down, please. Consulting companies, help us. Maybe you sell snake oil, maybe you don't, I don't know. Please help us. And that is the dynamic that we're wrestling with when we talk about the implementation problem. Anthropic just announced a deployment company with Blackstone, Hellman & Friedman, and Goldman Sachs. It's reported to have 1 and 1/2 billion dollars in capital behind it. OpenAI is going after the same thing with a venture valued near 10 billion dollars. Now, I want you to look at that in the context of all of the AI products on the market because the AI products on the market right now are by and large not being taken as seriously as the OpenAI and Claude implementations that I just described as having billions of dollars of capital on the line. Those companies, OpenAI and Anthropic, are recognizing that they cannot just implement enterprise AI agent solutions without forward deployed engineers and very serious investment. And the labs aren't the only ones moving here. There are consultancies that have concluded that their best value is actually product. It's shipping agents into the same accounts that Anthropic and Google and OpenAI are all involved in. And what they're recognizing is that the value in the market right now is in the completed workflow. And that, by the way, if you're wondering where the dollars went, that is where the capital is coming from from these private equity firms for these OpenAI and Anthropic joint ventures. That these private equity firms are seeing trillions of dollars on the line in these workflows, and they are not going to miss their chance because they're already squeezed on their previous business model, which in many cases was SaaS predominated and SaaS is in danger. And so, I want to give you a strategic reframe for how you think about the battle to implement full delegated work agentic workflows. We're not talking about pricing here. We're talking about how you actually get these services up and running. Now, a lot of the conversation is about the idea that services are where we're going after software. I think that the larger conversation, beyond sort of whether services can be a replacement for SaaS, that's a finance conversation. I think the larger conversation is where the value of the model shows up in the workflow versus where the harness value shows up. Is the value in the data? Is it in the permissions? Is it in the evals? Is it in the audits? Is it in the ownership after the launch? This is the wrestling match that we're all having. The companies are having this with vendors, companies are having this with OpenAI and Anthropic around pricing. Private equity firms are trying to get their piece. And And for for years, we have been thinking that the moat is in the data. But that advice is not complete, and I want to differentiate data and model and workflow from the implementation layer, what you might call the harness around the model. And by the way, if you're wondering if I'm just making that up, the the labs are starting to talk this way, too. OpenAI's own Frontier Alliance's post argues that the bottleneck for enterprise AI is how agents are built and operated inside companies. When the company shipping the model tells you the bottleneck isn't their model, it's the whole implementation layer, we got to be taking notes. So, I'm going to dig into more of the lab strategy, and I'm going to dig in way, way deeper on the implementation side in the Substack post. But right now, I want to show you the squeeze that is making this whole shift unlock. There is a specific squeeze of pressure on generic AI for enterprise setups right now. And I'm going to name that squeeze across four different axes of pressure that are pressuring agentic workflows and how agentic workflows work and how companies selling agents work. Because if you are in the business of the AI economy, you are inevitably now in the business of agents, and these pressures affect you. And these pressures are exactly what this large hyperscaler forward implementation is about. It's what companies are wrestling with when they put agent workflows into place. It's what the private equity financiers want their piece of. How can they negotiate these pressures and get to value? So, first axis, frontier labs are moving down stack. This has been widely reported and observed. Anthropic and OpenAI used to ship the model and let everyone else build around that. But now they're standing up deployment companies. As I've said, they're hiring these engineers that are going to be inside embedded in companies. They're also going directly at product pieces, right? Like Claude releasing Claude design or Claude releasing finance agent templates. Uh or even going after traditional coding agent patterns, which of course we've kind of forgotten, but going after cursor, for example, with Codex with Claude code. That was the first example of this. You want to pay attention when they do that to where the labs are saying the value lives more than what they're claiming they own on the surface. I'll give you an example. I do not think, as amazing as Claude is at finance, that Claude is going to replace the Bloomberg terminal. It's not. I do not believe that these dedicated deeply embedded solutions are going to be easily displaced. I do think this is a signal very publicly of where AI labs are willing to allocate capital [snorts] to go after particular pieces of value in enterprise workflows that they have high confidence AI can solve, and that is a very, very valuable signal. So, I read their hiring lists, I read their launch notes as essentially a cheat sheet from the hyperscalers on where they think AI agents are good, which is really helpful for the rest of us. But it is also a source of pressure, right? It's a pressure on everyone around them when like Claude design releases, everyone begins to ask questions of Figma. Like and we should, right? And it becomes a source of pressure. So, second piece, second axis of pressure. Consultancies are moving up the stack. I'm talking big ones, McKinsey, BCG, Accenture, Capgemini, all are inside the Open AI Frontier Alliance program. PricewaterhouseCoopers is collaborating with Open AI on the office of the CFO. These firms are not just doing change management, they are now starting to build deliberate agentic practices. They're training delivery teams on production deployment patterns, and they're showing up with engineers who can wire AI into operating systems. They have decades of relationships, and they are coming for agentic workflows that they think are held by the decision-makers whom they have existing relationships with. This obviously puts them at a massive advantage versus the average startup, who may also be selling AI agents, because that's all anyone with AI is selling right now. Third axis of pressure, systems of record are exposing structured interfaces that make it easier and easier to stay with them. If you are trying to disrupt a system of record, it has gotten harder. Salesforce, ServiceNow, Workday, all have opened up APIs and agent frameworks for AI to act inside their systems. SAP announced an acquisition of Dreamio paired with Prior Labs specifically for a governed data play, right? These vendors don't need a startup sitting between their data and a customer's agent. They want the agent to call their platform directly with their permission and their auditor. I've talked about that. That is an axis of pressure on anyone trying to play the game for agent workflows today. Fourth axis of pressure, private equity has become a distribution channel. So, the Anthropic deployment company that I talked about, PE effectively owns and influences thousands of mid-market companies, especially SaaS companies around finance, ops, support, procurement, compliance, and they are desperate to get more efficiency out of those investments. As I discussed earlier in this video, a PE firm therefore can be an axis of deployment that gives someone who has a partnership with them an incredible advantage because they can introduce one deployment partner across the entire portfolio, compare results across companies, and standardize the playbooks where the same patterns repeat very quickly, and they are incentivized to do so. That is a very different distribution shape than vendor-by-vendor sales, which most startups go for, and you're just not going to win that battle. So, there are four pressures that are all aligning on a particular AI deployment pattern at the enterprise level, and we're going to get into that next. So, what does this mean for you if you're a builder? If you're shipping a generic AI for enterprise wrapper without owning a workflow, without owning an action layer or a governance structure, if you're just depending on the model and maybe saying we can access your data for the special sauce, you are going to get squeezed by the four pressures I just talked about. I'll go further and say those four pressures are also putting an enormous amount of strain on existing agentic procurement processes, and I talk about that in a separate video, but I want you to understand that if you're sitting there trying to figure out which agent to ladder across multiple workflows, you need to be thinking more about how your implementation layer shapes the value and less about whatever a particular vendor is claiming. All the vendors will tell you their data is key, accessing their data is key, that their agent is going to be the one that delivers for you. I get that. You need to decide in terms of the value that you are putting into place as a buyer now, are you getting value for money? Are you getting a agent that is extraordinarily capable within the implementation environment you actually have? Bring your developers to to table. And in keeping with the SaaS platforms, the data platforms you're actually integrating with. And that is where the pressures that we feel from uh everyone converging around this agentic workflow stack really start to bite. We're basically in a position where we're paralyzed for choice. And that choice paralysis is a function of the exact trillion-dollar market I talked about at the top of this video. The pot of gold here is so valuable that everyone is converging on it and it makes choosing and building on it difficult and it makes discerning value difficult. Look, plenty of wrapper companies are going to keep shipping in this market. The defensibility window may be closing, but most people who are building right now are still building and pricing in last year's market and they don't have good answers for someone who asks hard questions about the value of what they're selling versus the value of what you bring to bear as the installer of the system, as your devs implement and build the system. Now, if you want to dig in deeper on what specific moves you should take under this pressure, uh whether you are competing with a lab, whether you're a consultancy, whether you're a buyer, I have a much deeper dive on each of those personas on the Substack, but I want you to take away the idea that the squeeze matters regardless everyone is going to continue to apply pressure on agentic workflows until someone is able to clearly claim ownership in the space. And we are very much years away from having clarity there. It is not a foregone conclusion, for example, that Claude will own all those workflows. It's not a foregone conclusion OpenAI will own all those workflows. It's not a foregone conclusion that anyone will own them. That's why everyone's taking a claim and that's why you need real clarity on where value lies. Now, let's dig into this implementation layer just a little bit. Implementation layer is a phrase that gets thrown around and it's thrown around so often it can be difficult to define it. I'm going to be very specific here. There are specific implementation layer components that tie to the value I'm talking about. If you've built them, you understand. And if you haven't, I'll explain them so you get it. Workflow design comes first. You must decide which decisions the model gets to make, what steps stay human, where the handoffs are, and what counts as done. That's not a prompt. That is a defined process where every step has an owner, an input, an output. Most teams tend to skip this, and they will ship a model attached to a tool without a workflow definition behind it. Data access is another piece here. Which sources of truth does the agent read? Which permissions apply at the row and field level? Which records are authoritative and which are stale? The model can produce a very confident answer from a 6-month-old PDF or from a live record, but you probably care which, and the implementation layer decides which. Authority. What is the agent allowed to do? Against which systems? With what spending or commitment limits? Reading is one risk profile, writing is a whole separate risk profile, and spending is something you can't undo, typically. Evals are another one. How do you measure whether the agent's output is correct, complete, and safe before it goes anywhere? Evals are not a benchmark, right? Evals are actually the way you score the model's adherence to specific business rules. If you can't tell me what's in your eval, you're you're not going to be in position to tell me whether your agent works. Audit trails. What gets logged? What has to get logged? What can an auditor reconstruct after a failure? What about recovery and ongoing ownership? What happens when the agent does something wrong? How does an action get reversed? Who at the customer keeps the system tuned and up-to-date? These are all components that are not model work that are typically put on the enterprise to do, that have an extraordinary impact on the total package of value that the agent does. But, everyone's going to tell you, if they're a vendor, that they're selling you that value. And unless they're coming in to actually build that for you, they're not reasonably going to be selling you that value. The value lies with the builders. The value lies with people who can build an implementation layer that surrounds these agents and allows them to do work that is truly enterprise grade. Now, I have a deeper teardown of all of the components I just named over on the substack. And if you're building on any of those components, that is where you can get a full readout on regulated, unregulated workflows, how you think about them together. If we zoom out for a minute, and we ask why this is happening right now, I think we have to come back to that finance part of the story I called about earlier. Because the reason why PE is going after this space is twofold. One, they have a push pressure because PE has traditionally had a very clear value proposition in play around owning SaaS and growing it. I referenced that earlier. Two, there's a pull pressure. PE wants to pull in AI and use it across their portfolio companies. I talked about that as a distribution option earlier in this video, but you should also understand it as a financial incentive. PE firms are incentivized to put together AI stories for the companies they are selling. And they need to do that to turn their SaaS players into sellable companies. And that is part of why OpenAI and Anthropic can find the capital to do this right now. And so, the question you should ask if you are not at OpenAI or Anthropic is is your product something a PE firm could plausibly buy on behalf of 50 portfolio companies? Are you stuck in one-to-one enterprise sales? If you are getting sold a product, is it a product that has that kind of scale and track record to it where you can validate it? Or is it something that is one to one? You need to get into understanding how a particular move that the PE companies are making right now shapes your competitive set and build options. Because if you're not ready to explore PE as either a distribution channel or as a signal of real enterprise value, then you're probably not really talking about agentic workflows that scale. Because the ones that scale, PE is already going after them. And you should be seeing that when you have these conversations with people who are building them. Now, all of this can seem very difficult to follow, and I want to simplify it down for you. If I were building in the next 12 months, and I were thinking in terms of product strategy, the key thing I would think about, and this is true whether you are in the enterprise or whether you are building product for the enterprise or or even whether you're in PE, the key principle is to sit closer to the business object. Generic intelligence becomes valuable when it gets attached to the specific objects and actions that define real work. Not abstract reasoning, not better summarization, but the actual objects that drive business workflows. So, let's walk through what that might look like. Let's say you have a support product that has to understand cases and policies and customers and entitlements and escalation paths. You want a a implementation layer where the object model for customer support ties into a clear bundle the agent can act against to actually close on customer support tickets, etc. To actually deliver value for customers in a finished, fully formed way. Another example, let's say that you are working on sales. You are going outbound on sales, you're going inbound on sales, you're closing sales motions. You want a sales object-oriented model where you can actually have the model understand the different objects in the business workflows and work against them all the way across the entire sales funnel in a reliable consistent manner. And that requires thinking about your data layer and thinking about your implementation layer as one clearly integrated substrate that allows an agent to operate across the top. Now, specific agents are going to stand out in any conversation we have as buyers, as sellers, even in PE in the next 6 to 12 months. And the reason why they will stand out is because when you ask questions that dig for those specifics, vendors that haven't thought through or software builders that haven't thought through how their value proposition works at a discrete level, they're going to show their cards. They're not going to be what they say they are. They're going to be saying, "Oh, the model's great. We're betting on the model getting better and better. Uh we trust your data. Your data's going to help us." They're going to give these generic answers. Builders who do well, whether they sit in the enterprise or outside it, are builders who understand that the implementation layer is not something that is just up for grabs that Anthropic can take tomorrow with a product release. The implementation layer is the is the detail that allows you to actually get value out of your agents. Now, if you want the complete breakdown component by component on the implementation layer with specific guidance on what to keep inside the house versus what to bring to a partner with a buyer-side audit framework, I have all of that on the substack. Link is in the description. If if you're building with this, you do need to be clear on your implementation detail. I'm not just kidding around when I say you have to understand the detail here. You either need to understand the detail well enough to buy and not be caught when someone sells you something that isn't worth it, or you need to understand the detail well enough to build something and sell it so it is plausible. And I know that I have people who watch these videos who are in both of those camps. And if you're in PE, you have to understand enough of the detail of the people who are selling you software or offering you companies with software that you know that there's actual value there. And by the way, I do know for a fact there are PE firms out there who are currently testing SaaS company built by saying, "Can my crack team in-house build this in cloud code over the weekend?" The things I am talking about with the implementation layer are too complicated, too nuanced, and too far into the weeds on specific enterprises to be built in a weekend by cloud code. It just does not work that way. And that is part of the challenge is that the business models have to change. The business model of SaaS tastes like chicken was predicated on the idea that software could be generic and could be essentially the same format in every single place where it was put in every single company in the world. We don't live in that world anymore. The disproportionate value in agentic workflows is in customization. And so, the reason why I'm emphasizing that we are living through an implementation layer war is because people have figured out that there are trillions of dollars in getting this right. And people are trying to figure out where is the leverage point to get to that value? Is the leverage point in the data? Salesforce would probably argue that. There are others. SAP would argue that. Is the leverage point in the model? I'm sure Anthropic and OpenAI will tell you the leverage point is in the model. Maybe in the harness? Is the leverage point in the memory? We didn't even get a chance to talk about that, but there's a whole set of companies that will tell you the leverage point is in the memory. What I am here to tell you is that the actual leverage in this system is the way an implementation layer assembles a model, assembles a harness, assembles data into an actionable workflow. And that is going to be custom, and that is not going to be something anybody else can easily do. It is biased toward building internally. And you need to think about if you are bringing someone in whether they can build and bring in components that align to where your implementation detail lives. And that's sort of how you start to assess is you're going to have a custom agent implementation fabric inside your company. You have to ask yourself, does this vendor that comes in, does what they sell play nicely with my implementation fabric? Do they understand the data objects I work with? Do they understand my workflows at a very detailed level? If you want to keep learning and you want to keep digging into this, um hit subscribe. I've got more videos coming on this shortly. For a deeper read on this one, check out the Substack and happy building. The implementation layer is so encouraging to entrepreneurs. If you want to build in this space, it's wide open. If you want to build internally in this space as an intrapreneur, it's really wide open. And if you want to be part of figuring out how we unlock trillions of dollars of value, there's there's going to be so many roles around this space to go after. I'm so excited about this one. Have fun.

---

## Timestamped Segments

**[0:00]** Let me tell you why I'm excited about

**[0:01]** this whole implementation challenge for

**[0:03]** agents. People think it's an agent

**[0:05]** story. It's actually the story of

**[0:08]** finance changing what it believes is the

**[0:10]** model of software in the future. And at

**[0:12]** the same time, the story of hyperscalers

**[0:14]** finding out what doesn't work. And at

**[0:16]** the same time, the story of companies

**[0:19]** figuring out where the disproportionate

**[0:21]** value in AI is. All of these forces are

**[0:24]** converging on this private equity-driven

**[0:26]** services deployment model that we're

**[0:27]** going to talk about today. It's so cool.

**[0:29]** So, private equity for a long time had

**[0:32]** this saying, it's a real saying, you can

**[0:33]** ask a financier that you know, that that

**[0:36]** SaaS companies all taste like chicken.

**[0:39]** In other words, all SaaS companies are

**[0:41]** the same from a balance sheet

**[0:43]** perspective. They all have the same

**[0:44]** growth characteristics, the same

**[0:46]** numbers, they're very easy to analyze,

**[0:48]** that makes them ideal as an investment

**[0:49]** vehicle until recently, when of course,

**[0:52]** SaaS company growth metrics and

**[0:54]** profitability all went to hell in a

**[0:56]** handbasket because they could not figure

**[1:00]** out how to make themselves relevant in a

**[1:04]** world where AI agents were taking over.

**[1:06]** This puts competitive pressure on the PE

**[1:08]** investment firms because I cannot tell

**[1:10]** you the number of PEs who have funds

**[1:12]** that are dated 26, 27, 28, who are

**[1:15]** wrestling with the with the challenge of

**[1:18]** trying to understand how they will sell

**[1:21]** these companies that when they bought

**[1:22]** them were good healthy SaaS companies

**[1:24]** and now are on the rocks or in danger.

**[1:26]** They don't have an answer. And so,

**[1:28]** that's why they are interested in

**[1:29]** pivoting into agentic workflows.

**[1:31]** Meanwhile, hyperscalers are realizing

**[1:34]** they cannot just sit in fancy

**[1:36]** brick-walled Silicon Valley conference

**[1:38]** rooms and talk cleverly about how AI is

**[1:41]** helpful and easy to implement and not be

**[1:43]** out in the trenches. They are realizing

**[1:44]** that Palantir is right. You have to have

**[1:46]** forward-deployed engineers who have to

**[1:48]** sit in the weeds with customers and

**[1:50]** figure out how this works. Open AI

**[1:52]** figured it out, Anthropic figured it

**[1:53]** out, and they realize they have a new

**[1:54]** business model for this. They're not

**[1:56]** equipped for this, and so they're

**[1:57]** starting to do joint ventures, and

**[1:59]** they're starting to look for capital to

**[2:00]** do that. Because, of course, what's the

**[2:01]** thing with hyperscalers? They are

**[2:03]** capital constrained. Anthropic is,

**[2:05]** OpenAI is. I do not care if they have

**[2:07]** raised more capital than just about any

**[2:09]** company in history. They are still

**[2:10]** capital constrained because of the

**[2:11]** tremendous costs of reaching AGI, of

**[2:14]** getting GPUs, of model training, etc.,

**[2:17]** of serving models increasingly.

**[2:19]** So,

**[2:20]** they have to partner up. They have to

**[2:22]** find finance. Private equity is there

**[2:23]** with the finance. That's sort of how the

**[2:25]** incentives align for those two. And

**[2:27]** they're all aimed at the third player in

**[2:30]** this market, the company. The company is

**[2:32]** realizing, and I'm talking about the

**[2:34]** company as in Fortune 500 firms, SMB

**[2:36]** firms. I am talking about people who did

**[2:38]** not understand the difference between a

**[2:41]** chat and an agent just a few months ago.

**[2:45]** Something happened in December, and it's

**[2:47]** been accelerating since, and people who

**[2:49]** I have talked to, who have been in

**[2:51]** Copilot chat mode for years, are now

**[2:54]** understanding what agents can do because

**[2:56]** agents got that much more valuable. And

**[2:58]** they're desperate to put them to work in

**[3:00]** real use cases, and they know they don't

**[3:01]** have the expertise, they know they don't

**[3:03]** understand how agents work well, but

**[3:06]** they know they can get it done cuz

**[3:07]** they've seen enough examples in their

**[3:09]** own work. And I want to be very clear

**[3:11]** here. The value we're talking about is

**[3:13]** trillions of dollars. It It's because

**[3:16]** agents can do an entire workflow. And

**[3:20]** And there's disproportionate value in

**[3:22]** getting to 100% on that. And getting to

**[3:24]** 100% on an entire workflow is a new

**[3:26]** phenomenon. It is a 2026 spring

**[3:28]** phenomenon that you can do that

**[3:29]** reliably, clearly, at scale, and

**[3:31]** repeatably. That didn't used to be the

**[3:32]** case. It's brand new. It is super cool,

**[3:35]** and it means that these companies see

**[3:38]** enough of agents to know they can do

**[3:39]** this, know they have a lot of places to

**[3:41]** apply it, and know they they need help.

**[3:43]** And so, they are turning to these new

**[3:45]** companies saying, "OpenAI, Anthropic,

**[3:46]** somebody, please help us. Sit someone

**[3:48]** down, please. Consulting companies, help

**[3:50]** us. Maybe you sell snake oil, maybe you

**[3:51]** don't, I don't know. Please help us. And

**[3:54]** that is the dynamic that we're wrestling

**[3:56]** with when we talk about the

**[3:57]** implementation problem.

**[3:59]** Anthropic just announced a deployment

**[4:01]** company with Blackstone, Hellman &

**[4:02]** Friedman, and Goldman Sachs. It's

**[4:04]** reported to have 1 and 1/2 billion

**[4:06]** dollars in capital behind it. OpenAI is

**[4:07]** going after the same thing with a

**[4:09]** venture valued near 10 billion dollars.

**[4:11]** Now, I want you to look at that in the

**[4:13]** context of all of the AI products on the

**[4:16]** market because the AI products on the

**[4:17]** market right now are by and large not

**[4:20]** being taken as seriously as the OpenAI

**[4:23]** and Claude implementations that I just

**[4:25]** described as having billions of dollars

**[4:27]** of capital on the line. Those companies,

**[4:29]** OpenAI and Anthropic, are recognizing

**[4:32]** that they cannot just implement

**[4:34]** enterprise AI agent solutions without

**[4:37]** forward deployed engineers and very

**[4:39]** serious investment. And the labs aren't

**[4:41]** the only ones moving here. There are

**[4:42]** consultancies that have concluded that

**[4:44]** their best value is actually product.

**[4:47]** It's shipping agents into the same

**[4:49]** accounts that Anthropic and Google and

**[4:53]** OpenAI are all involved in. And what

**[4:55]** they're recognizing is that the value in

**[4:59]** the market right now is in the completed

**[5:01]** workflow. And that, by the way, if

**[5:03]** you're wondering where the dollars went,

**[5:05]** that is where the capital is coming from

**[5:07]** from these private equity firms for

**[5:09]** these OpenAI and Anthropic joint

**[5:11]** ventures. That these private equity

**[5:13]** firms are seeing trillions of dollars on

**[5:16]** the line in these workflows, and they

**[5:19]** are not going to miss their chance

**[5:20]** because they're already squeezed on

**[5:21]** their previous business model, which in

**[5:23]** many cases was SaaS predominated and

**[5:25]** SaaS is in danger. And so, I want to

**[5:28]** give you a strategic reframe for how you

**[5:31]** think about the battle to implement full

**[5:35]** delegated work agentic workflows. We're

**[5:37]** not talking about pricing here. We're

**[5:40]** talking about how you actually get these

**[5:43]** services up and running. Now, a lot of

**[5:46]** the conversation is about the idea that

**[5:49]** services are where we're going after

**[5:52]** software.

**[5:53]** I think that the larger conversation,

**[5:55]** beyond sort of whether services can be a

**[5:57]** replacement for SaaS, that's a finance

**[5:59]** conversation. I think the larger

**[6:01]** conversation is where the value of the

**[6:05]** model shows up in the workflow versus

**[6:08]** where the harness value shows up. Is the

**[6:11]** value in the data? Is it in the

**[6:12]** permissions? Is it in the evals? Is it

**[6:14]** in the audits? Is it in the ownership

**[6:18]** after the launch? This is the wrestling

**[6:21]** match that we're all having. The

**[6:22]** companies are having this with vendors,

**[6:24]** companies are having this with OpenAI

**[6:26]** and Anthropic around pricing. Private

**[6:28]** equity firms are trying to get their

**[6:29]** piece. And And for for years,

**[6:32]** we have been thinking that the moat is

**[6:36]** in the data.

**[6:39]** But that advice is not complete, and I

**[6:42]** want to differentiate data and model and

**[6:45]** workflow from the implementation layer,

**[6:46]** what you might call the harness around

**[6:48]** the model. And by the way, if you're

**[6:49]** wondering if I'm just making that up,

**[6:51]** the the labs are starting to talk this

**[6:53]** way, too. OpenAI's own Frontier

**[6:55]** Alliance's post argues that the

**[6:57]** bottleneck for enterprise AI is how

**[6:59]** agents are built and operated inside

**[7:01]** companies. When the company shipping the

**[7:02]** model tells you the bottleneck isn't

**[7:05]** their model, it's the whole

**[7:06]** implementation layer, we got to be

**[7:08]** taking notes. So, I'm going to dig into

**[7:10]** more of the lab strategy, and I'm going

**[7:11]** to dig in way, way deeper on the

**[7:13]** implementation side in the Substack

**[7:15]** post. But right now, I want to show you

**[7:18]** the squeeze

**[7:19]** that is making this whole shift unlock.

**[7:22]** There is a specific squeeze of pressure

**[7:25]** on generic AI for enterprise setups

**[7:28]** right now. And I'm going to name that

**[7:30]** squeeze across four different axes of

**[7:32]** pressure that are pressuring agentic

**[7:35]** workflows and how agentic workflows work

**[7:36]** and how companies selling agents work.

**[7:38]** Because if you are in the business of

**[7:40]** the AI economy, you are inevitably now

**[7:42]** in the business of agents, and these

**[7:43]** pressures affect you. And these

**[7:45]** pressures are exactly what this large

**[7:48]** hyperscaler forward implementation is

**[7:50]** about. It's what companies are wrestling

**[7:52]** with when they put agent workflows into

**[7:53]** place. It's what the private equity

**[7:56]** financiers want their piece of. How can

**[7:58]** they negotiate these pressures and get

**[8:01]** to value? So, first axis, frontier labs

**[8:04]** are moving down stack. This has been

**[8:06]** widely reported and observed. Anthropic

**[8:08]** and OpenAI used to ship the model and

**[8:10]** let everyone else build around that. But

**[8:13]** now they're standing up deployment

**[8:14]** companies. As I've said, they're hiring

**[8:15]** these engineers that are going to be

**[8:16]** inside embedded in companies. They're

**[8:18]** also going directly at product pieces,

**[8:21]** right? Like Claude releasing Claude

**[8:23]** design or Claude releasing finance agent

**[8:25]** templates. Uh or even going after

**[8:28]** traditional coding agent patterns, which

**[8:30]** of course we've kind of forgotten, but

**[8:32]** going after cursor, for example, with

**[8:33]** Codex with Claude code. That was the

**[8:35]** first example of this. You want to pay

**[8:37]** attention when they do that to

**[8:41]** where the labs are saying the value

**[8:44]** lives more than what they're claiming

**[8:46]** they own on the surface. I'll give you

**[8:48]** an example. I do not think, as amazing

**[8:51]** as Claude is at finance, that Claude is

**[8:53]** going to replace the Bloomberg terminal.

**[8:55]** It's not.

**[8:56]** I do not believe that these dedicated

**[8:59]** deeply embedded solutions are going to

**[9:01]** be easily displaced. I do think this is

**[9:04]** a signal very publicly of where AI labs

**[9:08]** are willing to allocate capital [snorts]

**[9:10]** to go after particular pieces of value

**[9:12]** in enterprise workflows that they have

**[9:14]** high confidence AI can solve, and that

**[9:16]** is a very, very valuable signal. So, I

**[9:18]** read their hiring lists, I read their

**[9:21]** launch notes as essentially a cheat

**[9:23]** sheet from the hyperscalers on where

**[9:24]** they think AI agents are good, which is

**[9:26]** really helpful for the rest of us. But

**[9:28]** it is also a source of pressure, right?

**[9:30]** It's a pressure on everyone around them

**[9:31]** when like Claude design releases,

**[9:33]** everyone begins to ask questions of

**[9:35]** Figma. Like and we should, right? And it

**[9:36]** becomes a source of pressure. So, second

**[9:38]** piece, second axis of pressure.

**[9:40]** Consultancies are moving up the stack.

**[9:42]** I'm talking big ones, McKinsey, BCG,

**[9:44]** Accenture, Capgemini, all are inside the

**[9:47]** Open AI Frontier Alliance program.

**[9:49]** PricewaterhouseCoopers is collaborating

**[9:51]** with Open AI on the office of the CFO.

**[9:53]** These firms are not just doing change

**[9:55]** management, they are now starting to

**[9:56]** build deliberate agentic practices.

**[9:59]** They're training delivery teams on

**[10:00]** production deployment patterns, and

**[10:02]** they're showing up with engineers who

**[10:04]** can wire AI into operating systems. They

**[10:06]** have decades of relationships,

**[10:09]** and they are coming for agentic

**[10:11]** workflows that they think are held by

**[10:14]** the decision-makers whom they have

**[10:16]** existing relationships with. This

**[10:18]** obviously puts them at a massive

**[10:20]** advantage versus the average startup,

**[10:21]** who may also be selling AI agents,

**[10:23]** because that's all anyone with AI is

**[10:24]** selling right now. Third axis of

**[10:26]** pressure, systems of record are exposing

**[10:30]** structured interfaces that make it

**[10:33]** easier and easier to stay with them. If

**[10:35]** you are trying to disrupt a system of

**[10:37]** record, it has gotten harder.

**[10:39]** Salesforce, ServiceNow, Workday, all

**[10:41]** have opened up APIs and agent frameworks

**[10:43]** for AI to act inside their systems. SAP

**[10:46]** announced an acquisition of Dreamio

**[10:47]** paired with Prior Labs specifically for

**[10:49]** a governed data play, right? These

**[10:51]** vendors don't need a startup sitting

**[10:54]** between their data and a customer's

**[10:55]** agent. They want the agent to call their

**[10:58]** platform directly with their permission

**[11:00]** and their auditor. I've talked about

**[11:01]** that. That is an axis of pressure on

**[11:04]** anyone trying to play the game for agent

**[11:06]** workflows today.

**[11:08]** Fourth axis of pressure, private equity

**[11:11]** has become a distribution channel.

**[11:14]** So, the Anthropic deployment company

**[11:15]** that I talked about,

**[11:17]** PE effectively owns and influences

**[11:21]** thousands of mid-market companies,

**[11:23]** especially SaaS companies around

**[11:24]** finance, ops, support, procurement,

**[11:27]** compliance, and they are desperate to

**[11:29]** get more efficiency out of those

**[11:31]** investments. As I discussed earlier in

**[11:32]** this video, a PE firm therefore can be

**[11:35]** an axis of deployment that gives someone

**[11:37]** who has a partnership with them an

**[11:39]** incredible advantage because they can

**[11:41]** introduce one deployment partner across

**[11:43]** the entire portfolio, compare results

**[11:45]** across companies, and standardize the

**[11:47]** playbooks where the same patterns repeat

**[11:48]** very quickly, and they are incentivized

**[11:50]** to do so. That is a very different

**[11:51]** distribution shape than vendor-by-vendor

**[11:53]** sales, which most startups go for, and

**[11:56]** you're just not going to win that

**[11:56]** battle. So, there are four pressures

**[11:59]** that are all aligning on a particular AI

**[12:02]** deployment pattern at the enterprise

**[12:04]** level, and we're going to get into that

**[12:06]** next. So, what does this mean for you if

**[12:08]** you're a builder? If you're shipping a

**[12:10]** generic AI for enterprise wrapper

**[12:12]** without owning a workflow, without

**[12:14]** owning an action layer or a governance

**[12:16]** structure, if you're just depending on

**[12:18]** the model and maybe saying we can access

**[12:20]** your data for the special sauce, you are

**[12:23]** going to get squeezed by the four

**[12:24]** pressures I just talked about. I'll go

**[12:27]** further and say those four pressures are

**[12:29]** also putting an enormous amount of

**[12:31]** strain on existing agentic procurement

**[12:36]** processes, and I talk about that in a

**[12:38]** separate video, but I want you to

**[12:40]** understand that if you're sitting there

**[12:41]** trying to figure out which agent to

**[12:43]** ladder across multiple workflows, you

**[12:47]** need to be thinking more about how your

**[12:50]** implementation layer shapes the value

**[12:53]** and less about whatever a particular

**[12:55]** vendor is claiming. All the vendors will

**[12:57]** tell you their data is key, accessing

**[12:59]** their data is key, that their agent is

**[13:02]** going to be the one that delivers for

**[13:03]** you. I get that. You need to decide in

**[13:07]** terms of the value that you are putting

**[13:09]** into place as a buyer now,

**[13:12]** are you getting value for money? Are you

**[13:15]** getting a agent that is extraordinarily

**[13:19]** capable within the implementation

**[13:21]** environment you actually have? Bring

**[13:24]** your developers to to table.

**[13:26]** And in keeping with the SaaS platforms,

**[13:29]** the data platforms you're actually

**[13:30]** integrating with. And that is where the

**[13:31]** pressures that we feel from uh everyone

**[13:34]** converging around this agentic workflow

**[13:36]** stack really start to bite. We're

**[13:37]** basically in a position where we're

**[13:39]** paralyzed for choice. And that choice

**[13:41]** paralysis is a function of the exact

**[13:44]** trillion-dollar market I talked about at

**[13:46]** the top of this video. The pot of gold

**[13:48]** here is so valuable that everyone is

**[13:51]** converging on it and it makes choosing

**[13:53]** and building on it difficult and it

**[13:55]** makes discerning value difficult. Look,

**[13:58]** plenty of wrapper companies are going to

**[14:00]** keep shipping in this market. The

**[14:03]** defensibility window may be closing, but

**[14:05]** most people who are building right now

**[14:07]** are still building and pricing in last

**[14:10]** year's market and they don't have good

**[14:12]** answers for someone who asks hard

**[14:14]** questions about the value of what

**[14:15]** they're selling versus the value of what

**[14:17]** you bring to bear as the installer of

**[14:20]** the system, as your devs implement and

**[14:22]** build the system.

**[14:23]** Now, if you want to dig in deeper on

**[14:25]** what specific moves you should take

**[14:27]** under this pressure, uh whether you are

**[14:29]** competing with a lab, whether you're a

**[14:31]** consultancy, whether you're a buyer, I

**[14:33]** have a much deeper dive on each of those

**[14:36]** personas on the Substack, but I want you

**[14:38]** to take away the idea that the squeeze

**[14:40]** matters regardless

**[14:43]** everyone is going to continue to apply

**[14:46]** pressure on agentic workflows until

**[14:49]** someone is able to clearly claim

**[14:52]** ownership in the space. And we are very

**[14:55]** much years away from having clarity

**[14:57]** there. It is not a foregone conclusion,

**[15:00]** for example, that Claude will own all

**[15:01]** those workflows. It's not a foregone

**[15:03]** conclusion OpenAI will own all those

**[15:05]** workflows. It's not a foregone

**[15:07]** conclusion that anyone will own them.

**[15:09]** That's why everyone's taking a claim and

**[15:11]** that's why you need real clarity on

**[15:13]** where value lies. Now, let's dig into

**[15:15]** this implementation layer just a little

**[15:17]** bit. Implementation layer is a phrase

**[15:19]** that gets thrown around and it's thrown

**[15:21]** around so often it can be difficult to

**[15:23]** define it. I'm going to be very specific

**[15:25]** here. There are specific implementation

**[15:27]** layer components that tie to the value

**[15:29]** I'm talking about. If you've built them,

**[15:33]** you understand. And if you haven't, I'll

**[15:34]** explain them so you get it. Workflow

**[15:36]** design comes first. You must decide

**[15:39]** which decisions the model gets to make,

**[15:41]** what steps stay human, where the

**[15:43]** handoffs are, and what counts as done.

**[15:46]** That's not a prompt. That is a defined

**[15:48]** process where every step has an owner,

**[15:50]** an input, an output. Most teams tend to

**[15:53]** skip this, and they will ship a model

**[15:55]** attached to a tool without a workflow

**[15:57]** definition behind it. Data access is

**[16:00]** another piece here. Which sources of

**[16:02]** truth does the agent read? Which

**[16:04]** permissions apply at the row and field

**[16:06]** level? Which records are authoritative

**[16:07]** and which are stale? The model can

**[16:09]** produce a very confident answer from a

**[16:11]** 6-month-old PDF or from a live record,

**[16:14]** but you probably care which, and the

**[16:15]** implementation layer decides which.

**[16:17]** Authority. What is the agent allowed to

**[16:19]** do? Against which systems? With what

**[16:21]** spending or commitment limits?

**[16:24]** Reading is one risk profile, writing is

**[16:27]** a whole separate risk profile, and

**[16:28]** spending is something you can't undo,

**[16:31]** typically. Evals are another one. How do

**[16:33]** you measure whether the agent's output

**[16:35]** is correct, complete, and safe before it

**[16:38]** goes anywhere? Evals are not a

**[16:39]** benchmark, right? Evals are actually the

**[16:42]** way you score the model's adherence to

**[16:45]** specific business rules. If you can't

**[16:47]** tell me what's in your eval, you're

**[16:49]** you're not going to be in position to

**[16:51]** tell me whether your agent works. Audit

**[16:52]** trails. What gets logged? What has to

**[16:55]** get logged? What can an auditor

**[16:56]** reconstruct after a failure? What about

**[16:58]** recovery and ongoing ownership? What

**[17:00]** happens when the agent does something

**[17:02]** wrong? How does an action get reversed?

**[17:04]** Who at the customer keeps the system

**[17:05]** tuned and up-to-date? These are all

**[17:08]** components that are not model work that

**[17:10]** are typically put on the enterprise to

**[17:12]** do, that have an extraordinary impact on

**[17:15]** the total package of value that the

**[17:17]** agent does. But, everyone's going to

**[17:20]** tell you, if they're a vendor, that

**[17:22]** they're selling you that value. And

**[17:23]** unless they're coming in to actually

**[17:25]** build that for you,

**[17:26]** they're not reasonably going to be

**[17:28]** selling you that value. The value lies

**[17:30]** with the builders. The value lies with

**[17:32]** people who can build an implementation

**[17:35]** layer that surrounds these agents and

**[17:37]** allows them to do work that is truly

**[17:40]** enterprise grade. Now, I have a deeper

**[17:42]** teardown of all of the components I just

**[17:45]** named over on the substack. And if

**[17:46]** you're building on any of those

**[17:47]** components, that is where you can get a

**[17:50]** full readout on regulated, unregulated

**[17:53]** workflows, how you think about them

**[17:54]** together.

**[17:55]** If we zoom out for a minute, and we ask

**[17:57]** why this is happening right now, I think

**[18:00]** we have to come back to that finance

**[18:02]** part of the story I called about

**[18:03]** earlier.

**[18:04]** Because the reason why PE is going after

**[18:08]** this space is twofold. One, they have a

**[18:12]** push pressure because PE has

**[18:16]** traditionally had a very clear value

**[18:18]** proposition in play around owning SaaS

**[18:20]** and growing it. I referenced that

**[18:22]** earlier. Two, there's a pull pressure.

**[18:24]** PE wants to pull in AI and use it across

**[18:27]** their portfolio companies. I talked

**[18:29]** about that as a distribution option

**[18:31]** earlier in this video, but you should

**[18:32]** also understand it as a financial

**[18:33]** incentive. PE firms are incentivized to

**[18:36]** put together AI stories for the

**[18:38]** companies they are selling. And they

**[18:40]** need to do that to turn their SaaS

**[18:42]** players into sellable companies. And

**[18:44]** that is part of why OpenAI and Anthropic

**[18:47]** can find the capital to do this right

**[18:49]** now. And so, the question you should ask

**[18:51]** if you are not at OpenAI or Anthropic is

**[18:54]** is your product something a PE firm

**[18:56]** could plausibly buy on behalf of 50

**[18:59]** portfolio companies? Are you stuck in

**[19:01]** one-to-one enterprise sales? If you are

**[19:04]** getting sold a product, is it a product

**[19:06]** that has that kind of scale and track

**[19:08]** record to it where you can validate it?

**[19:10]** Or is it something that is one to one?

**[19:12]** You need to get into understanding

**[19:15]** how

**[19:16]** a particular

**[19:19]** move that the PE companies are making

**[19:21]** right now

**[19:22]** shapes your competitive set and build

**[19:24]** options. Because if you're not ready to

**[19:26]** explore PE as either a distribution

**[19:28]** channel or as a signal of real

**[19:31]** enterprise value, then you're probably

**[19:34]** not really talking about agentic

**[19:36]** workflows that scale. Because the ones

**[19:39]** that scale, PE is already going after

**[19:41]** them.

**[19:42]** And you should be seeing that when you

**[19:44]** have these conversations with people who

**[19:45]** are building them. Now, all of this can

**[19:47]** seem very difficult to follow, and I

**[19:50]** want to simplify it down for you. If I

**[19:53]** were building in the next 12 months, and

**[19:55]** I were thinking in terms of product

**[19:56]** strategy, the key thing I would think

**[19:59]** about, and this is true whether you are

**[20:01]** in the enterprise or whether you are

**[20:02]** building product for the enterprise or

**[20:04]** or even whether you're in PE, the key

**[20:06]** principle is to sit closer to the

**[20:08]** business object. Generic intelligence

**[20:10]** becomes valuable when it gets attached

**[20:12]** to the specific objects and actions that

**[20:14]** define real work. Not abstract

**[20:16]** reasoning, not better summarization, but

**[20:18]** the actual objects that drive business

**[20:21]** workflows. So, let's walk through what

**[20:23]** that might look like. Let's say you have

**[20:24]** a support product that has to understand

**[20:26]** cases and policies and customers and

**[20:28]** entitlements and escalation paths.

**[20:31]** You want a a implementation layer where

**[20:34]** the object model for customer support

**[20:36]** ties into a clear bundle the agent can

**[20:39]** act against to actually close on

**[20:43]** customer support tickets, etc.

**[20:45]** To actually deliver value for customers

**[20:48]** in a finished, fully formed way. Another

**[20:51]** example, let's say that you are working

**[20:53]** on sales. You are going outbound on

**[20:55]** sales, you're going inbound on sales,

**[20:56]** you're closing sales motions.

**[20:59]** You want a sales object-oriented model

**[21:01]** where you can actually have the model

**[21:03]** understand the different objects in the

**[21:05]** business workflows and work against them

**[21:09]** all the way across the entire sales

**[21:12]** funnel in a reliable consistent manner.

**[21:15]** And that requires thinking about your

**[21:17]** data layer and thinking about your

**[21:19]** implementation layer as one clearly

**[21:22]** integrated substrate that allows an

**[21:24]** agent to operate across the top. Now,

**[21:26]** specific agents are going to stand out

**[21:28]** in any conversation we have as buyers,

**[21:32]** as sellers, even in PE in the next 6 to

**[21:35]** 12 months. And the reason why they will

**[21:36]** stand out is because when you ask

**[21:39]** questions that dig for those specifics,

**[21:42]** vendors that haven't thought through or

**[21:44]** software builders that haven't thought

**[21:46]** through how their value proposition

**[21:48]** works at a discrete level, they're going

**[21:49]** to show their cards. They're not going

**[21:51]** to be what they say they are. They're

**[21:52]** going to be saying, "Oh, the model's

**[21:54]** great. We're betting on the model

**[21:55]** getting better and better. Uh we trust

**[21:57]** your data. Your data's going to help

**[21:58]** us." They're going to give these generic

**[21:59]** answers. Builders who do well, whether

**[22:02]** they sit in the enterprise or outside

**[22:03]** it, are builders who understand that the

**[22:06]** implementation layer is not something

**[22:08]** that is just up for grabs that Anthropic

**[22:10]** can take tomorrow with a product

**[22:11]** release. The implementation layer is the

**[22:14]** is the detail that allows you to

**[22:17]** actually get value out of your agents.

**[22:20]** Now, if you want the complete breakdown

**[22:22]** component by component on the

**[22:24]** implementation layer with specific

**[22:26]** guidance on what to keep inside the

**[22:27]** house versus what to bring to a partner

**[22:30]** with a buyer-side audit framework, I

**[22:31]** have all of that on the substack. Link

**[22:33]** is in the description. If if you're

**[22:35]** building with this, you do need to be

**[22:38]** clear on your implementation detail. I'm

**[22:40]** not just kidding around when I say you

**[22:41]** have to understand the detail here. You

**[22:43]** either need to understand the detail

**[22:45]** well enough to buy and not be caught

**[22:47]** when someone sells you something that

**[22:49]** isn't worth it, or you need to

**[22:50]** understand the detail well enough to

**[22:51]** build something and sell it so it is

**[22:54]** plausible. And I know that I have people

**[22:56]** who watch these videos who are in both

**[22:57]** of those camps. And if you're in PE, you

**[23:00]** have to understand enough of the detail

**[23:02]** of the people who are selling you

**[23:03]** software or offering you companies with

**[23:05]** software that you know that there's

**[23:07]** actual value there. And by the way, I do

**[23:10]** know for a fact there are PE firms out

**[23:12]** there who are currently testing SaaS

**[23:15]** company built by saying, "Can my crack

**[23:17]** team in-house build this in cloud code

**[23:19]** over the weekend?" The things I am

**[23:21]** talking about with the implementation

**[23:23]** layer are too complicated, too nuanced,

**[23:25]** and too far into the weeds on specific

**[23:27]** enterprises to be built in a weekend by

**[23:30]** cloud code. It just does not work that

**[23:31]** way. And that is part of the challenge

**[23:33]** is that the business models have to

**[23:35]** change. The business model of SaaS

**[23:36]** tastes like chicken was predicated on

**[23:39]** the idea that software could be generic

**[23:41]** and could be essentially the same format

**[23:44]** in every single place where it was put

**[23:46]** in every single company in the world. We

**[23:48]** don't live in that world anymore. The

**[23:49]** disproportionate value in agentic

**[23:51]** workflows is in customization. And so,

**[23:53]** the reason why I'm emphasizing that we

**[23:55]** are living through an implementation

**[23:57]** layer war is because people have figured

**[24:00]** out that there are trillions of dollars

**[24:01]** in getting this right. And people are

**[24:03]** trying to figure out where is the

**[24:05]** leverage point to get to that value? Is

**[24:08]** the leverage point in the data?

**[24:10]** Salesforce would probably argue that.

**[24:12]** There are others. SAP would argue that.

**[24:14]** Is the leverage point in the model? I'm

**[24:16]** sure Anthropic and OpenAI will tell you

**[24:17]** the leverage point is in the model.

**[24:19]** Maybe in the harness? Is the leverage

**[24:21]** point in the memory? We didn't even get

**[24:23]** a chance to talk about that, but there's

**[24:24]** a whole set of companies that will tell

**[24:26]** you the leverage point is in the memory.

**[24:27]** What I am here to tell you

**[24:29]** is that the actual leverage in this

**[24:31]** system is the way an implementation

**[24:35]** layer assembles a model, assembles a

**[24:38]** harness, assembles data into an

**[24:41]** actionable workflow. And that is going

**[24:44]** to be custom, and that is not going to

**[24:46]** be something anybody else can easily do.

**[24:49]** It is biased toward building internally.

**[24:52]** And you need to think about if you are

**[24:55]** bringing someone in whether they can

**[24:57]** build and bring in components that align

**[25:02]** to where your implementation detail

**[25:04]** lives. And that's sort of how you start

**[25:06]** to assess is you're going to have a

**[25:07]** custom agent implementation fabric

**[25:09]** inside your company. You have to ask

**[25:11]** yourself, does this vendor that comes

**[25:14]** in, does what they sell play nicely with

**[25:17]** my implementation fabric? Do they

**[25:18]** understand the data objects I work with?

**[25:20]** Do they understand my workflows at a

**[25:21]** very detailed level? If you want to keep

**[25:23]** learning and you want to keep digging

**[25:25]** into this, um hit subscribe. I've got

**[25:27]** more videos coming on this shortly. For

**[25:29]** a deeper read on this one, check out the

**[25:30]** Substack and happy building. The

**[25:33]** implementation layer is so encouraging

**[25:35]** to entrepreneurs. If you want to build

**[25:37]** in this space, it's wide open. If you

**[25:39]** want to build internally in this space

**[25:40]** as an intrapreneur, it's really wide

**[25:42]** open.

**[25:43]** And if you want to be part of figuring

**[25:45]** out how we unlock trillions of dollars

**[25:47]** of value, there's there's going to be so

**[25:48]** many roles around this space to go

**[25:49]** after. I'm so excited about this one.

**[25:51]** Have fun.
