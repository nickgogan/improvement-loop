# Transcript: Block Laid Off Half Its Company for AI. AI Can't Do the Job.

**URL:** https://www.youtube.com/watch?v=fm6mYqFAM5c
**Segments:** 163
**Channel:** AI News & Strategy Daily | Nate B Jones
**Duration:** 20:21
**Uploaded:** 2026-04-19

---

## Full Text

Here's the idea that just broke the internet. What if instead of managers spending half their time synthesizing status, relaying priorities, and making sure three teams have the same picture of reality, what if software just maintained that picture? What if software maintained a living, always updated model of everything happening across the company? What's being built, what's blocked, where the resources are, where the customers are struggling, you get the idea. Everyone queries it directly and you get real results in real time. It's called a world model and it means that nobody waits for the Monday meeting. Nobody needs a middle manager to carry context between the people doing the work and the people deciding what work to do. And this is the dream. This is what people are building toward. Jack Dorsey published a blueprint for this last week. It got 5 million views in two days. Agency founders are jumping in to post their own implementations. Enterprise vendors are immediately rebranding their products around the concept. And I get it right. The idea is sound as far as it goes. A huge share of what fills manager calendars like status syncs and alignment meetings and information shuttling is all work that software can do faster and cheaper today. The companies that automate it will be faster than the ones that don't. But but but world model is one phrase covering three completely different architectures that fail in different ways. And all three share a similar blind spot. The line between information flow, which the system handles well, and judgment, which it does not handle at all, that's not really defined. That's something that we have to explore. And so, we need to start to think about what it means to understand the actual quality of our decisions in a world where software is automating big parts of our internal knowledge systems. So, this video gives you the full picture. It dives into how world models actually work. not the pitch, but the actual architecture. It dives into the approaches companies are taking now, what each one is good at, and the specific way each one breaks. We're going to cover three of them. And it dives into the principles that determine whether a world model compounds into real advantage or stagnates into an expensive knowledge base. And if you're stuck, I built a plugin to help you assess your readiness, right? Where your signal actually lives, whether you have a boundary layer that prevents bad judgment failures, what to build first. Basically, a get started on a world model kit. And by the way, the reason it's important to assess your readiness is because failure tends to be invisible with world models. When you talk about some of the experiments in management of the 2010s, you get loud failures. Zapos infamously adopted holocrisy and satisfaction scores absolutely collapsed and they fell off the fortune list. Valve has a hidden power structure that has become a wellocumented case study. Medium's head of operations wrote publicly that the system was getting in the way of the work. When you have management systems that are unconventional and don't work, everyone can see the damage. The world model failure is different because it's going to be quiet. It's going to look like a system flagging a revenue dip is significant when in fact it was seasonal and it drove a prioritization change it shouldn't have. And the person who said, "Ignore that. It happens every year." Maybe they were removed in the last reorg and now nobody catches it because the system presented the finding with a kind of calm structured confidence it uses to talk to senior leaders. That's dangerous. Or take another example. Let's say the system surfaces a correlation between a feature launch and a spike in churn. So the product team kills the feature, but the actual cause was different. It was a billing change that shipped the same week. And the system couldn't tell the difference between correlation and causation. It's not built to do that. and nothing in the interface signaled that distinction and the team treated the output the way they treat a director's analysis. Or most insidiously, let's say the system stops sending information to certain people because it has drift. Nobody notices. The absence of information is kind of invisible in the noise of the company. Decisions start getting made on incomplete pictures and the quality of those decisions degrades so gradually that it reads as the market shifted or execution was off rather than the system was quietly filtering out the signal we needed. There's a common mechanism behind all three of those examples. When a company removes a management layer and replaces it with nothing, the absence is obvious. Nobody is synthesizing status. Nobody is interpreting strategy. Nobody is catching drift. And people tend to feel that gap right away. The chaos is visible, diagnosible, fixable. It's the Zappos example. But when a company removes a management layer and replaces it with the world model, the information does keep flowing. Status gets synthesized. Dependencies get flagged, reports get generated. So far so good, right? From the outside, from a dashboard, from an executive review, it looks like that routing function has been successfully automated. And for the pure information logistics piece of things, that's true. The problem is that managers don't just route information. They edit it. They decide what matters. And when you're talking about building world models, you have to start to think about that piece, right? I've talked about the idea that our management models need to adjust and be unbundled. Well, part of the unbundling effect is understanding how new models of management affect the way we think about world models. We need to think about what applying judgment to information means. If we are going to have a world model that encodes so much information in our businesses, if a system prioritizes, if it highlights, if it suppresses, if it escalates, it is making judgments. The system is deciding which anomalies to surface. The system is deciding which information reaches which teams. The system is deciding through a relevance model what counts as important. Every one of those decisions used to be made by a human who could factor in things the system can't. Like organizational politics, the CEO's real priorities versus stated ones, the difference between a structural problem and a seasonal blip, the context that turns noise into signal. And the output can look similar on the surface, but the quality of those decisions embedded in that output is really fundamentally different. And the organization won't feel that difference right away. It'll just feel this sort of slow degradation of decision quality that it might attribute to bad luck. But it's really a system that's making thousands of small editorial choices it was never equipped to make because no one understood that when you build a world model, you have to think about when you have good judgment versus when you have information. When is this information the system can surface and when is this requires human interpretation before action. Those are really distinct things. And so if we step back, the phrase world model currently refers to at least three fundamentally different architectures. Each one gets that boundary I'm describing wrong in a different way. The vector database approach fails by never drawing the line. If you wire up your data sources, if you embed everything, and you let agents retrieve by semantic similarity, it's a super popular approach because it's super fast to deploy and it's adequate for pure information logistics, for status synthesis, for dependency detection, for report generation. It works, but the boundary failure is pretty simple. Semantic retrieval has no structural mechanism to distinguish surfacing from interpreting. When the system returns results ranked by relevance, that ranking is an interpretation. It's a claim about what matters, but nothing in the architecture says it actually knows what matters. The output arrives with the same confidence regardless, and the user has no way to tell which is which. At a small scale, this is probably manageable. The senior people who consume the output have enough context to apply their own judgment and override bad rankings. But at a big scale, hundreds or thousands of people consuming system output as the primary info source, the ranking becomes a reality no one intended. And what the system surfaces, people just automatically act on. And what it doesn't surface, people never see. The editorial function has been automated by default without anyone deciding to automate it. Approach number two is the structured ontology approach. And that approach fails by drawing the line too conservatively. We can look at the palanteer model for that. You define the objects. You define the relationships and you define the actions of your business really explicitly. The AI reasons within that bounded structure. A customer is an entity with specific properties. A work order has defined connections. The system cannot hallucinate relationships that don't exist in the schema. And so the boundary is really clear by construction. The system handles structured queries within the ontology and humans handle everything else. Interpretation stays with the human. There is no simulated judgment and that makes sense as far as it goes. But the boundary failure is this. The ontology can only represent what you have already categorized. It handles known relationships really precisely is blind to emergent relationships. The unnamed pattern that once someone sees it reframes how you understand the business. So by drawing the line more conservatively from an information perspective, the system is unable to surface an unexpected signal that human judgment needs in order to do its job. You can get precision that way, but you cost yourself something on the discovery front. And so that world model is accurate about what it knows. It's silent about what it doesn't know. And the things it doesn't know might be the things that matter the most. Another approach, the third approach is the signal fidelity approach. That approach fails by assuming the signal interprets itself. And that's effectively Jack Dorsey's bet. If you build the world model around the highest fidelity data exhaust your business generates, like transactions in Block's case, you're going to get good results. Dorsy thinks, right? Money is honest is his thesis. Every purchase is a fact. The model will improve as a byproduct of doing business. The boundary is partially solved by the nature of the signal. Right? A transaction is a fact and facts require less interpretation than sentiment or conversation. But but but the connections between facts like why a merchant's cash flow is tightening that still requires judgment. And so the boundary failure here is pretty simple. Because the underlying signal is clean, the systems interpretive moves probably look more trustworthy than they should be. A correlation in transaction data feels much more authoritative than a correlation in Slack messages, even when the causal reasoning behind both is equally thin. High signal fidelity at the input layer creates an illusion of high judgment quality at the output layer and the illusion is harder to see precisely because the inputs are really really good. So how do you want to approach this if you are trying to actually make progress so we can't just throw up our hands? We have to be among those who act. And so if you are trying to figure out how to build a world model and you've been one of those that saw Jack Dorsey's post, I would say the first thing you need to do is you need to think about your data structure and your classification system. You need to think about what would you categorize as act on this versus interpret this first. Act on this feels like an output that is factual, that's verified, that's low risk. It's something that is very clearly a status rollup, a dependency flag, a metric that crossed a threshold with clear historical precedent for what the threshold means. It's something that the world model is good at because the information is obvious and has a clear output. Then you need to find the pieces of information that are interpretive. Interpret this first means the output involves a judgment call that the system isn't equipped to make reliably like a trend that might be significant or maybe it's just noise or a correlation that might be causal or maybe it's just coincidental or a prioritization that might reflect the actual strategic landscape or maybe just the biases in the model. Regardless, it's information that needs a human to look at the data and make a call. That boundary is never going to be perfect, but you must try to draw it. you are not excused from trying to draw it. The difference between a world model that helps your org and the one that slowly degrades it is whether the system communicates uncertainty and demands interpretation correctly. And right now almost every implementation I'm seeing discussed actively hides that because the output looks so clean and the dashboards look so authoritative and nothing in the interface says this is a place where the system's making a judgment call. It might be getting wrong. That is an architectural failure. That's not a database choice failure. It's not an embedding model failure. It's not an ingestion frequency failure. It's a fundamental failure in the way the system presents everything, facts, interpretations, routine and novel information. It presents high confidence and low confidence and is presenting them all at the same level at the same salience in the same way without giving you the ability to see the difference. And the organization may not realize that and may treat it all with the same level of trust. You even if it's imperfect have to label your outputs. You have to make what I call the interpretive boundary visible. You need to give those who are responsible for interpreting these world models a clear signal about where the system is operating within its competence and where it's operating with inference. So if we step back and we want to be constructive, we want to listen to this idea of this boundary. What are some principles we can use to build a world model system that actually works well? Number one, your signal fidelity determines the ceiling of your world model. Your world model can only be as good as the ground truth feeding it. Transactions can be high fidelity operational telemetry from real systems that can be a highfidelity signal. Slack messages and Google docs tend to be fairly low fidelity signals. The question is really how high quality is your context graph? Because context is really slippery right now and you have to ask yourself does the reality you're feeding the model give a really clear fingerprint of your business that is really really easy for a model to interpret. If the answer is, well, it's not so clear, you need to think about how to clarify the inputs to the model first. Number two, structure needs to be earned, not imposed. And I've said in other context that you need to do this. In this particular situation, think about where you need to impose a schema upfront versus where you need the model to take the first pass and be exploratory and catch things you wouldn't catch otherwise. This is the palanter example, right? You sometimes want the model to be free to discover something it wouldn't have seen otherwise. And so this is where you have to balance an entity graph that you say this is my schema. This is what I know versus exploratory behavior by the model to discover connections and to discover objects in your business graph that you might not have realized were significant. You are not excused from thinking about that relationship relative to your business risk, your business landscape, and your business opportunity set. You have to figure out how to draw the line between how to give the model an expected version of the world that you think is predictable and where to give the model room to explore. Three, the model compounds only when it encodes outcomes. So a knowledge base might record what happened. A world model is supposed to record what happened, what was done about it, and what happened next, what resulted. That third element, outcomes, creates a feedback loop that makes the system smarter over time. Without it, month six looks a lot like month one. But outcomes don't encode themselves. Someone has to close the loop between action and results. And that is an organizational change that none of us are talking about enough because it requires the habit of saying I did this and this is what happened and honestly this is the result even if it's a failure and most of our teams aren't ready for that. Is your team ready to be honest with the model? That brings us to number four. Design for resistance. The world model only works if the team as a whole is feeding it. And people may resist feeding a system that threatens their information advantages. They may route around it with back channel conversations. They may keep critical context in their heads. This may be malicious, but it also may be forgetfulness. The system has to capture signal as a byproduct of work, not as a separate act of documentation or it probably won't work well. If feeding the model requires lots of extra effort, most people won't do it. And the people with the most valuable context will be the most strategic about withholding it. You need to be honest about the idea that the team needs to be incentivized genuinely to work with the model as a partner and needs to realize that there is an advantage to doing so for them or this will not work. And number five, start now because the mode is time. It's not a special architecture. Right? If you can start to get good continuous data sooner, you're going to create a foundation that's more difficult to replicate. If we learned anything from the Claude code leak, it's that it's easy to copy architecture. But it's harder to copy a good world model because you get months and months and months of business reality flowing through that model and the outcome loops that accumulated along the way. And so companies that started sooner effectively have a time advantage that's hard to replicate. So what does this look like in practice? Let's say you have a 100 people or less and you have a very strong senior team. You might go with a vector database approach for information flow because your senior people are effectively the ones who have judgment and it's going to work until you outgrow their bandwidth and you can choose to go that way. Now, if you are an enterprise, if you have very complicated regulations, if you're regulated, you probably have to go with a structured anttology a little bit like Palanteer where you have high upfront cost and you have to think a lot about that boundary to make sure that you catch surprises and you're not overfitting to the data. Now, if you're a platform business and you sit on Signal like Block does, you are going to have to think about how you avoid false confidence that you get when you have really clean, fancy inputs like all of Block's transactions and it looks like a perfectly authoritative conclusion and it's actually only correlation, not causation. But let's say you're none of those things. Let's say you're a knowledge work company and you're running on conversations and documents and that is actually very very common and it's something that people are really wrestling with. I would say start with a vector database approach if you're small, but you're going to have to be very intentional about building an interpretive layer over the top or you're going to be in trouble. I would also call out that you will scale out of that inevitably and you should start thinking now about a more structured data approach because if you don't, you are going to be in trouble. Vector databases approach do break down when they get to a certain scale, maybe 10,000 documents or so, you're going to start to get into trouble. And in that situation, you need to be in a place where you can actually say this is what we want. This is the part of our data that is factual that we want to encode, that we want the world model to be aware of, and this is the part that's interpretive that we want our humans to pay attention to. If you can't start to think about that, whether you're at a knowledge world company or whether you're at any of the other company types I talked about, you're going to be in trouble. So, if you want to get started, I built a world model readiness plugin that runs you through the framework in this piece and gives you a really concrete assessment. It asks about your company's data sources, your current information flow, how decisions get made, and where your highest fidelity signal lives. And then it maps you into a paradigm, right? It identifies whether you have an interpretive boundary layer. It flags where you're most exposed, and it gives you a prioritized starting sequence. It's going to work in any LLM, right? Claude, Chad, CPT, Gemini. That's not the point, right? Increasingly, it's about your ability to think well. And that's the focus that we have here because we want you to think through the consequences of building a world model before you read a post and say, "Oh my gosh," and paste it into chat GPT and just get started. Because it's so tempting to build something that will look like intelligence, it's actually hard to build something that will act as intelligence. And the most dangerous version of a world model is the one that works well enough that nobody questions it until the decision quality degrades and someone finally asks what happened and what changed. You don't want to be in that position. You want to think through where the world model is going to actually give you information that's helpful to automate all of the complexity of your systems versus where the world model is going to be overconfident and try and do interpretation that a human needs to do. Take the time, think that through. You can use the plugin if it's helpful and don't get swept up the next time someone writes a post that gets 5 million views in 48 hours. There's going to be a lot of hype in the age of AI. It's worth taking it apart and understanding what's going on under the surface. And I think World Model offers a great paradigm for us to take apart those concepts and actually get it something buildable. Best of luck. And yes, we can build world models. We just have to be thoughtful about it. Cheers.

---

## Timestamped Segments

**[0:00]** Here's the idea that just broke the internet. What if instead of managers spending half their time synthesizing status, relaying priorities, and making

**[0:07]** sure three teams have the same picture of reality, what if software just maintained that picture? What if software maintained a living, always updated model of everything happening across the company? What's being built,

**[0:18]** what's blocked, where the resources are,

**[0:21]** where the customers are struggling, you get the idea. Everyone queries it directly and you get real results in

**[0:28]** real time. It's called a world model and it means that nobody waits for the Monday meeting. Nobody needs a middle manager to carry context between the

**[0:36]** people doing the work and the people deciding what work to do. And this is the dream. This is what people are building toward. Jack Dorsey published a

**[0:43]** blueprint for this last week. It got 5 million views in two days. Agency founders are jumping in to post their own implementations. Enterprise vendors

**[0:51]** are immediately rebranding their products around the concept. And I get it right. The idea is sound as far as it goes. A huge share of what fills manager

**[1:00]** calendars like status syncs and alignment meetings and information shuttling is all work that software can do faster and cheaper today. The companies that automate it will be

**[1:08]** faster than the ones that don't. But but but world model is one phrase covering three completely different architectures

**[1:16]** that fail in different ways. And all three share a similar blind spot. The line between information flow, which the

**[1:23]** system handles well, and judgment, which it does not handle at all, that's not really defined. That's something that we

**[1:30]** have to explore. And so, we need to start to think about what it means to understand the actual quality of our

**[1:39]** decisions in a world where software is automating big parts of our internal knowledge systems. So, this video gives

**[1:46]** you the full picture. It dives into how world models actually work. not the pitch, but the actual architecture. It dives into the approaches companies are taking now, what each one is good at,

**[1:56]** and the specific way each one breaks.

**[1:57]** We're going to cover three of them. And it dives into the principles that determine whether a world model compounds into real advantage or stagnates into an expensive knowledge

**[2:05]** base. And if you're stuck, I built a plugin to help you assess your readiness, right? Where your signal actually lives, whether you have a boundary layer that prevents bad judgment failures, what to build first.

**[2:15]** Basically, a get started on a world model kit. And by the way, the reason it's important to assess your readiness is because failure tends to be invisible

**[2:24]** with world models. When you talk about some of the experiments in management of the 2010s, you get loud failures. Zapos

**[2:31]** infamously adopted holocrisy and satisfaction scores absolutely collapsed and they fell off the fortune list.

**[2:38]** Valve has a hidden power structure that has become a wellocumented case study.

**[2:43]** Medium's head of operations wrote publicly that the system was getting in the way of the work. When you have management systems that are unconventional and don't work, everyone

**[2:51]** can see the damage. The world model failure is different because it's going to be quiet. It's going to look like a system flagging a revenue dip is

**[2:59]** significant when in fact it was seasonal and it drove a prioritization change it shouldn't have. And the person who said,

**[3:06]** "Ignore that. It happens every year."

**[3:08]** Maybe they were removed in the last reorg and now nobody catches it because the system presented the finding with a kind of calm structured confidence it

**[3:17]** uses to talk to senior leaders. That's dangerous. Or take another example.

**[3:21]** Let's say the system surfaces a correlation between a feature launch and a spike in churn. So the product team kills the feature, but the actual cause

**[3:29]** was different. It was a billing change that shipped the same week. And the system couldn't tell the difference between correlation and causation. It's not built to do that. and nothing in the

**[3:38]** interface signaled that distinction and the team treated the output the way they treat a director's analysis. Or most insidiously, let's say the system stops

**[3:45]** sending information to certain people because it has drift. Nobody notices.

**[3:50]** The absence of information is kind of invisible in the noise of the company.

**[3:54]** Decisions start getting made on incomplete pictures and the quality of those decisions degrades so gradually that it reads as the market shifted or

**[4:01]** execution was off rather than the system was quietly filtering out the signal we needed. There's a common mechanism behind all three of those examples. When

**[4:10]** a company removes a management layer and replaces it with nothing, the absence is obvious. Nobody is synthesizing status.

**[4:16]** Nobody is interpreting strategy. Nobody is catching drift. And people tend to feel that gap right away. The chaos is visible, diagnosible, fixable. It's the

**[4:25]** Zappos example. But when a company removes a management layer and replaces it with the world model, the information does keep flowing. Status gets synthesized. Dependencies get flagged,

**[4:36]** reports get generated. So far so good,

**[4:39]** right? From the outside, from a dashboard, from an executive review, it looks like that routing function has been successfully automated. And for the

**[4:47]** pure information logistics piece of things, that's true. The problem is that managers don't just route information.

**[4:55]** They edit it. They decide what matters.

**[4:58]** And when you're talking about building world models, you have to start to think about that piece, right? I've talked about the idea that our management models need to adjust and be unbundled.

**[5:08]** Well, part of the unbundling effect is understanding how new models of management affect the way we think about world models. We need to think about

**[5:16]** what applying judgment to information means. If we are going to have a world model that encodes so much information in our businesses, if a system

**[5:25]** prioritizes, if it highlights, if it suppresses, if it escalates, it is making judgments. The system is deciding which anomalies to surface. The system

**[5:34]** is deciding which information reaches which teams. The system is deciding through a relevance model what counts as important. Every one of those decisions

**[5:42]** used to be made by a human who could factor in things the system can't. Like organizational politics, the CEO's real priorities versus stated ones, the

**[5:50]** difference between a structural problem and a seasonal blip, the context that turns noise into signal. And the output can look similar on the surface, but the

**[5:58]** quality of those decisions embedded in that output is really fundamentally different. And the organization won't feel that difference right away. It'll

**[6:06]** just feel this sort of slow degradation of decision quality that it might attribute to bad luck. But it's really a system that's making thousands of small

**[6:14]** editorial choices it was never equipped to make because no one understood that when you build a world model, you have

**[6:21]** to think about when you have good judgment versus when you have information. When is this information the system can surface and when is this

**[6:30]** requires human interpretation before action. Those are really distinct things. And so if we step back, the phrase world model currently refers to

**[6:38]** at least three fundamentally different architectures. Each one gets that boundary I'm describing wrong in a different way. The vector database approach fails by never drawing the line. If you wire up your data sources,

**[6:48]** if you embed everything, and you let agents retrieve by semantic similarity,

**[6:52]** it's a super popular approach because it's super fast to deploy and it's adequate for pure information logistics,

**[6:58]** for status synthesis, for dependency detection, for report generation. It works, but the boundary failure is pretty simple. Semantic retrieval has no

**[7:07]** structural mechanism to distinguish surfacing from interpreting. When the system returns results ranked by relevance, that ranking is an

**[7:14]** interpretation. It's a claim about what matters, but nothing in the architecture says it actually knows what matters. The output arrives with the same confidence

**[7:21]** regardless, and the user has no way to tell which is which. At a small scale,

**[7:25]** this is probably manageable. The senior people who consume the output have enough context to apply their own judgment and override bad rankings. But

**[7:32]** at a big scale, hundreds or thousands of people consuming system output as the primary info source, the ranking becomes a reality no one intended. And what the

**[7:41]** system surfaces, people just automatically act on. And what it doesn't surface, people never see. The editorial function has been automated by default without anyone deciding to

**[7:50]** automate it. Approach number two is the structured ontology approach. And that approach fails by drawing the line too conservatively. We can look at the

**[7:58]** palanteer model for that. You define the objects. You define the relationships and you define the actions of your business really explicitly. The AI

**[8:06]** reasons within that bounded structure. A customer is an entity with specific properties. A work order has defined connections. The system cannot

**[8:14]** hallucinate relationships that don't exist in the schema. And so the boundary is really clear by construction. The system handles structured queries within

**[8:23]** the ontology and humans handle everything else. Interpretation stays with the human. There is no simulated judgment and that makes sense as far as

**[8:31]** it goes. But the boundary failure is this. The ontology can only represent what you have already categorized. It

**[8:40]** handles known relationships really precisely is blind to emergent relationships. The unnamed pattern that once someone sees it reframes how you

**[8:49]** understand the business. So by drawing the line more conservatively from an information perspective, the system is unable to surface an unexpected signal

**[8:57]** that human judgment needs in order to do its job. You can get precision that way,

**[9:02]** but you cost yourself something on the discovery front. And so that world model is accurate about what it knows. It's silent about what it doesn't know. And

**[9:09]** the things it doesn't know might be the things that matter the most. Another approach, the third approach is the signal fidelity approach. That approach

**[9:17]** fails by assuming the signal interprets itself. And that's effectively Jack Dorsey's bet. If you build the world

**[9:24]** model around the highest fidelity data exhaust your business generates, like transactions in Block's case, you're going to get good results. Dorsy thinks,

**[9:32]** right? Money is honest is his thesis.

**[9:33]** Every purchase is a fact. The model will improve as a byproduct of doing business. The boundary is partially solved by the nature of the signal.

**[9:42]** Right? A transaction is a fact and facts require less interpretation than sentiment or conversation. But but but the connections between facts like why a

**[9:51]** merchant's cash flow is tightening that still requires judgment. And so the boundary failure here is pretty simple. Because the underlying signal is clean,

**[9:59]** the systems interpretive moves probably look more trustworthy than they should be. A correlation in transaction data feels much more authoritative than a

**[10:07]** correlation in Slack messages, even when the causal reasoning behind both is equally thin. High signal fidelity at the input layer creates an illusion of

**[10:14]** high judgment quality at the output layer and the illusion is harder to see precisely because the inputs are really really good. So how do you want to

**[10:22]** approach this if you are trying to actually make progress so we can't just throw up our hands? We have to be among those who act. And so if you are trying

**[10:29]** to figure out how to build a world model and you've been one of those that saw Jack Dorsey's post, I would say the first thing you need to do is you need

**[10:37]** to think about your data structure and your classification system. You need to think about what would you categorize as act on this versus interpret this first.

**[10:47]** Act on this feels like an output that is factual, that's verified, that's low risk. It's something that is very clearly a status rollup, a dependency

**[10:54]** flag, a metric that crossed a threshold with clear historical precedent for what the threshold means. It's something that the world model is good at because the

**[11:03]** information is obvious and has a clear output. Then you need to find the pieces of information that are interpretive.

**[11:09]** Interpret this first means the output involves a judgment call that the system isn't equipped to make reliably like a

**[11:16]** trend that might be significant or maybe it's just noise or a correlation that might be causal or maybe it's just coincidental or a prioritization that

**[11:24]** might reflect the actual strategic landscape or maybe just the biases in the model. Regardless, it's information that needs a human to look at the data

**[11:32]** and make a call. That boundary is never going to be perfect, but you must try to draw it. you are not excused from trying to draw it. The difference between a

**[11:40]** world model that helps your org and the one that slowly degrades it is whether the system communicates uncertainty and

**[11:47]** demands interpretation correctly. And right now almost every implementation I'm seeing discussed actively hides that because the output looks so clean and

**[11:55]** the dashboards look so authoritative and nothing in the interface says this is a place where the system's making a judgment call. It might be getting wrong. That is an architectural failure.

**[12:05]** That's not a database choice failure. It's not an embedding model failure. It's not an ingestion frequency failure.

**[12:10]** It's a fundamental failure in the way the system presents everything, facts,

**[12:14]** interpretations, routine and novel information. It presents high confidence and low confidence and is presenting them all at the same level at the same

**[12:21]** salience in the same way without giving you the ability to see the difference.

**[12:25]** And the organization may not realize that and may treat it all with the same level of trust. You even if it's imperfect have to label your outputs.

**[12:34]** You have to make what I call the interpretive boundary visible. You need to give those who are responsible for interpreting these world models a clear

**[12:43]** signal about where the system is operating within its competence and where it's operating with inference. So if we step back and we want to be

**[12:51]** constructive, we want to listen to this idea of this boundary. What are some principles we can use to build a world model system that actually works well?

**[12:59]** Number one, your signal fidelity determines the ceiling of your world model. Your world model can only be as good as the ground truth feeding it.

**[13:07]** Transactions can be high fidelity operational telemetry from real systems that can be a highfidelity signal. Slack messages and Google docs tend to be

**[13:14]** fairly low fidelity signals. The question is really how high quality is your context graph? Because context is

**[13:22]** really slippery right now and you have to ask yourself does the reality you're feeding the model give a really clear fingerprint of your business that is

**[13:30]** really really easy for a model to interpret. If the answer is, well, it's not so clear, you need to think about how to clarify the inputs to the model

**[13:39]** first. Number two, structure needs to be earned, not imposed. And I've said in other context that you need to do this.

**[13:46]** In this particular situation, think about where you need to impose a schema upfront versus where you need the model

**[13:54]** to take the first pass and be exploratory and catch things you wouldn't catch otherwise. This is the palanter example, right? You sometimes

**[14:02]** want the model to be free to discover something it wouldn't have seen otherwise. And so this is where you have to balance an entity graph that you say

**[14:11]** this is my schema. This is what I know versus exploratory behavior by the model to discover connections and to discover

**[14:19]** objects in your business graph that you might not have realized were significant. You are not excused from thinking about that relationship

**[14:26]** relative to your business risk, your business landscape, and your business opportunity set. You have to figure out how to draw the line between how to give the model an expected version of the

**[14:35]** world that you think is predictable and where to give the model room to explore.

**[14:38]** Three, the model compounds only when it encodes outcomes. So a knowledge base might record what happened. A world model is supposed to record what

**[14:47]** happened, what was done about it, and what happened next, what resulted. That third element, outcomes, creates a feedback loop that makes the system

**[14:55]** smarter over time. Without it, month six looks a lot like month one. But outcomes don't encode themselves. Someone has to close the loop between action and

**[15:04]** results. And that is an organizational change that none of us are talking about enough because it requires the habit of saying I did this and this is what

**[15:12]** happened and honestly this is the result even if it's a failure and most of our teams aren't ready for that. Is your team ready to be honest with the model?

**[15:19]** That brings us to number four. Design for resistance. The world model only works if the team as a whole is feeding it. And people may resist feeding a

**[15:27]** system that threatens their information advantages. They may route around it with back channel conversations. They may keep critical context in their

**[15:35]** heads. This may be malicious, but it also may be forgetfulness. The system has to capture signal as a byproduct of work, not as a separate act of

**[15:43]** documentation or it probably won't work well. If feeding the model requires lots of extra effort, most people won't do it. And the people with the most

**[15:51]** valuable context will be the most strategic about withholding it. You need to be honest about the idea that the

**[15:57]** team needs to be incentivized genuinely to work with the model as a partner and needs to realize that there is an

**[16:05]** advantage to doing so for them or this will not work. And number five, start now because the mode is time. It's not a

**[16:12]** special architecture. Right? If you can start to get good continuous data sooner, you're going to create a foundation that's more difficult to

**[16:20]** replicate. If we learned anything from the Claude code leak, it's that it's easy to copy architecture. But it's harder to copy a good world model

**[16:27]** because you get months and months and months of business reality flowing through that model and the outcome loops that accumulated along the way. And so

**[16:34]** companies that started sooner effectively have a time advantage that's hard to replicate. So what does this look like in practice? Let's say you

**[16:42]** have a 100 people or less and you have a very strong senior team. You might go with a vector database approach for information flow because your senior

**[16:50]** people are effectively the ones who have judgment and it's going to work until you outgrow their bandwidth and you can choose to go that way. Now, if you are an enterprise, if you have very

**[16:58]** complicated regulations, if you're regulated, you probably have to go with a structured anttology a little bit like Palanteer where you have high upfront

**[17:06]** cost and you have to think a lot about that boundary to make sure that you catch surprises and you're not overfitting to the data. Now, if you're a platform business and you sit on

**[17:14]** Signal like Block does, you are going to have to think about how you avoid false confidence that you get when you have

**[17:23]** really clean, fancy inputs like all of Block's transactions and it looks like a perfectly authoritative conclusion and it's actually only correlation, not

**[17:31]** causation. But let's say you're none of those things. Let's say you're a knowledge work company and you're running on conversations and documents and that is actually very very common

**[17:39]** and it's something that people are really wrestling with. I would say start with a vector database approach if you're small, but you're going to have

**[17:46]** to be very intentional about building an interpretive layer over the top or you're going to be in trouble. I would also call out that you will scale out of

**[17:54]** that inevitably and you should start thinking now about a more structured data approach because if you don't, you

**[18:01]** are going to be in trouble. Vector databases approach do break down when they get to a certain scale, maybe 10,000 documents or so, you're going to

**[18:10]** start to get into trouble. And in that situation, you need to be in a place where you can actually say this is what

**[18:18]** we want. This is the part of our data that is factual that we want to encode,

**[18:23]** that we want the world model to be aware of, and this is the part that's interpretive that we want our humans to pay attention to. If you can't start to think about that, whether you're at a

**[18:31]** knowledge world company or whether you're at any of the other company types I talked about, you're going to be in trouble. So, if you want to get started,

**[18:37]** I built a world model readiness plugin that runs you through the framework in this piece and gives you a really concrete assessment. It asks about your company's data sources, your current

**[18:45]** information flow, how decisions get made, and where your highest fidelity signal lives. And then it maps you into a paradigm, right? It identifies whether you have an interpretive boundary layer.

**[18:55]** It flags where you're most exposed, and it gives you a prioritized starting sequence. It's going to work in any LLM,

**[19:01]** right? Claude, Chad, CPT, Gemini. That's not the point, right? Increasingly, it's about your ability to think well. And that's the focus that we have here

**[19:09]** because we want you to think through the consequences of building a world model before you read a post and say, "Oh my

**[19:16]** gosh," and paste it into chat GPT and just get started. Because it's so tempting to build something that will look like intelligence, it's actually

**[19:24]** hard to build something that will act as intelligence. And the most dangerous version of a world model is the one that works well enough that nobody questions

**[19:32]** it until the decision quality degrades and someone finally asks what happened and what changed. You don't want to be in that position. You want to think

**[19:39]** through where the world model is going to actually give you information that's helpful to automate all of the complexity of your systems versus where

**[19:48]** the world model is going to be overconfident and try and do interpretation that a human needs to do.

**[19:53]** Take the time, think that through. You can use the plugin if it's helpful and don't get swept up the next time someone writes a post that gets 5 million views

**[20:02]** in 48 hours. There's going to be a lot of hype in the age of AI. It's worth taking it apart and understanding what's going on under the surface. And I think

**[20:09]** World Model offers a great paradigm for us to take apart those concepts and actually get it something buildable.

**[20:15]** Best of luck. And yes, we can build world models. We just have to be thoughtful about it. Cheers.
