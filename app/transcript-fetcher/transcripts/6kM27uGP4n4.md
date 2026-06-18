# Transcript: 6kM27uGP4n4

**URL:** https://www.youtube.com/watch?v=6kM27uGP4n4
**Segments:** 620

---

## Full Text

Why cominator CEO Gary Tain's claw code toolkit GStack has many specialized workflows but the one most people are sleeping on is the planning workflow. It challenged my assumptions narrow down what really matters research the competitive landscape and have [clears throat] five different AI agent here reviewing my spec from CEO design engineering QA and devil advocate perspective all before writing a single line of code. So, in this video, I'm going to show you my entire planning pipeline on building a feature on a real SAS project with paying customers. So, with that being said, if that sounds interesting, let's get into this. Now, before we continue, I recently launched our school community where I help you to master AI agents, automations, and so much more. And that's all coming from someone who used to work as a senior AI software engineer at companies like Amazon and Microsoft. And in this community, you're going to get over 100 plus video materials like templates and workflows that I personally built and sold over 100 plus times. On top of that, you're also going to get access to our weekly live calls. And just to give you an idea, this week we're actually running a claw code master class where we're going to dive into how to improve Claw Co's accuracy when we're going to use it to building applications. Plus, you're also going to get full community support where you're going to get a chance to ask questions and get direct answers back. So, if you're ready to level up, make sure you jump right in and I'll see you in a community. All right. All right. So, to get started, first we're going to install this onto our local machine. So, to do so, right here, you can see this is the exact step we're going to follow to basically just copy this, open your code claw code, and just paste it and have it to install this completely onto our project. Or the other way you can do this is you're simply just going to copy that repository, paste it, and tell claw to follow the repository and try to install this and set this up. So, once you have this all set up, the next thing we're going to take a look at is how we can beble to use it into our existing project. So, right here, you can see this is my existing project called Book Zero. And right now if I were to log into the application, here is what it looks like. So I wanted to build a feature onto this existing brownfield projects. Basically by adding a AI chat agent here to query the expense based on the project data. For example, how much did I spend on gas in quarter 1 or show me the top five vendor this month or find all the receipts over $100. Right? So these are all some queries that we can be able to pass this chat agent here that can convert into a SQL query that can query the data in our database. Now obviously this feature is not really 100% defined. I think that the requirement here still needs to be refined a bit more with different personalities and that's where the Gstack comes in which can help us to refine govern this plan making sure that the plan here is fully ready before we pass it to execution. So in this case I'm just going to copy this link for Jira ticket and I already have my J MCP set up on my local machine. So in this case, I'm just going to head over to claw code really quick. And I basically mention that, hey, I already have this installed. And let's say if I want to bring this feature onto this project, what are some skills that I can use to build this project using GStack? And right here, you can see it uses GStack skill to give me a workflow on exactly how we're going to build this feature onto it. Now, obviously, we're not going to use it to build the building pipeline because it doesn't really have the test-driven elements like what Superpower does. So, I'm going to use it to do the PL pipeline because I think this is what GStack really shines. So in this case, I'm going to open a brand new terminal session and start a clock code. I'm just going to copy this diagram right here, pass it to a new clock session. And basically, this is what I'm going to say. I want you to follow this entire planning pipeline and try to do this for this entire ticket. Can you help me to do this, please? So, I'm going to paste this as my prompt and switch it over to planning mode. And right away, you can see that it starts to gather the context on exactly what this ticket is and how we can be able to build this. So first it's going to launch different sub aents here try to understand the AI chat codebase right also data models and services that we have then it's going to ask me some serious question to configure our GSTA stack framework like can we be able to copy other projects coding patterns or what is the goal right now is it a startup is it a hackathon projects or having fun and for this project right now is it in the ideation phase is it in the paying customer phase or doesn't have any paying customers right now right and then now once we have this all set so the changes everything you have real signal to work from since you already have the revenue. So the question that matters are about the wedge, the observation, the future fit and let me start. So the backlog spec describe three phases basic queries uh comparison trends and proactive insights. That's a lot of surface area. What is the smallest possible version of this AI chat that a paying customer will actually use this week? Not after you built all three phases. So for example, maybe the spending summaries or the receipt finder, the tax prep helper, right? Right? So all those kind of things. So in this case, this is what I'm going to say. So based on the research that we have done, the customers are looking to add the spending summaries in our AI chat a lot often, right? So they want to see the spending predictions, the patterns they see for the spendings. They want to learn from this using our AI chats. And most importantly, we want to have data visualizations to display charts, tables, or all kinds of data visualizations for the queries that they're querying for. And most importantly, they should be able to have the ability to save the conversation and also save the stats or the visualization and maybe add that into our data the dashboard and they can be able to review that in the later times. Most importantly, we need to have it to integrate it into our credit system so that they can be able to see the credit goes down when they have a conversation, right? So, how much we should charge per credit for per conversation or per chat? We need to define that as well. So there's a lot of things in place and I want you to package all together into this plan here. And basically you can see that's my prompt. Now this is there's a lot of things in the prompts. You can see it says I respect the ambition. I need to push back. You describe five features like spend analysis, chart visualizations, save queries, dashboard customizations, and credit based monetizations. This is not a wish. It's actually a platform. So we need to push back a bit more and we need to try to understand exactly what can users use right now this week after we have the MVP done. So here you can see pick one things that generate the word of mouth. Everything else can come in phase two. So how much did I spend on this category this quarter, right? What are my top expense for this month or show me the unusual spending this month or something like that, right? So you can see that it start to breaking this large prompts or large demand or large request into a step-by-step process that we can build the first MVP first. Then we're going to you know push back and adding those additional functionalities into phase 2 if we have time right so you can see these are the things that we have so in this case I'm just going to say hey uh all of them looks good right so show me the unusual spendings or um basically try to learn more about the spending that they made that's good and I think this is probably the feature we need to add right so all those queries should be in place yes we can you know forget about the charts but we definitely need to add the tables right be able to have user here to visualize things much more easier rather than just bunch of text. And furthermore, we also definitely need to support those queries to be able to fetch in our database and be able to have user here to understand their spending patterns. So that's basically my prompt and I'm just going to say yes and let's have it to basically plan this bit more and dive deep into how we're going to achieve this. Then it's asking me another PM kind of questions like have you sat down and watched how they use this platform without helping them? Did they struggle somewhere that you thought was obvious or did you ignore a feature you might you might thought uh was important. So this is kind of like a PM question and of course you cannot have this without like data or like user tracking all kind of things. So I actually made a video on the claw skills for marketings. In that video I demonstrate how you can be able to set up the entire tracking system like the usage you know have user fully on boarded like what have they done after they on boarded the entire user tracking here. I actually had made a video on this. So if you want to learn really more about how you can do this set of the tracking, make sure to check out that video right there. And I do have real usage for this specific surprise that I want to share. Yeah. So I want to say yes to this. And here you can see it says you have watched user that's good. Most founder at your stage here doesn't have that. So what surprise you and what the users do with book zero that didn't you expect. And this matters because AI chat features come from things user are already trying to do and just making it instant instead of the manual process. So one of the option that they give me is they export data to understand patterns and that is actually something that I found too not just from the AI but actually I found it as well that users actually turning to CSV here to analyze data rather than just doing it in our platform because in our dashboard there's only five charts and that's static for all users. Then we also have some other options like they ask question that I haven't anticipated or they struggle with the filter search from the UI. So all three options are pretty valid. So I'm just going to say based on these things that we have here first two is probably the most surprising that [clears throat] I want to resolve using this feature and that's basically what I wanted to add and I'm just going to say yes. So in this case I'm just going to enter this and let claw here to figure this out. Okay. So eventually here you can see this is what it responds. So this is a real signal user are exporting CSV to answer the questions that our platform should have this natively. So this is the what the future fit look like. So it actually look through the past this and look through the future here to see if it's actually meaningful in 3 years. So if AI gets cheaper, everyone has their own tools and the bookkeeping tools here in multiplies. Does this feature in our AI chat become more central or less? And honestly, I think this is kind of like a bonus feature from this framework to help you to look to the future to see if this feature is not replicatable or is unique compared to other competitors. So let's say every competitor now eventually add this feature like ask AI about your expense. What's your thesis about why your platform your your versions win? Right? Is it because of data that you have or is it because the domain knowledge or is it could be something else right like if you were to add this feature and other people are adding this feature you know what are some uniqueness what are some selling points what makes our platform our feature here from this platform different compared to others right so you can see it gives me some list of options here so in this case I'm going to take some time and try to answer this question and we're just going to proceed forward okay so after we have that answer submitted here you can see it basically is going to start to do some research and basically try to figure out what's the landscape for this feature that we're trying ad. Okay. So then it has done some research on the landscape for the AI conversational expense management and the conversational bookkeeping AI assistant for common mistakes in 2025 and 2026. So here is what it found. So layer one we have AI chatbot for small businesses are mainstream. Yes, that's good. And AI space is crowded with tools that try to do bookkeeping for like auto categorizations or auto reconciliations or auto filing but hallucination here and miscatategorization are the number one concerns across industry. So that's what it found for the concern and layer two here is that the shifting from child bots to agentic AI tools that take actions not just like answering questions is number one thing and the AI hallucination and bookkeeping is real. So hallucination here is a big problem and layer three here is about what's interesting our on our position here. So our AI here doesn't do bookkeeping. Our AI here only query data that are exist and most AI competitor here tries to generate accounting entries and that's where hallucination kills you. your AI answer questions about verified human review scripts or receives transaction data. So the accuracy here is higher because we're only querying structure data not generating any financial records which is what separates that apart. So you can see that that's the basically the difference right the clear difference here is that our AI doesn't hallucination your finance it reads what's actually there and that's it once we have our research done the next thing I'm going to do here is phase three for challenging our premise so here is the premise so here are the premise that I'm working from I need you to agree or disagree with the each so user want a natural language uh queries because they actually currently export CSV to answer the questions that the UI doesn't cover and the MVP here is spending analysis and unusual spending detections tables, no charts, no save queries or dashboard customizations and the credit based pricing promization is monetization model. AI query existing data only. This is the accuracy advantage plus the anomaly detection charts save queries proactive insights are in phase two and response time should be less than 5 seconds is the targets. So do we agree with all six? So you can see that it's actually able to break it and try to refine the plan here step by step on exactly what's the requirements which is a really structured way to do it. So here I'm just going to say yes I do agree with all six but one thing that I want to add here is or in this case confirm you mentioned about the credit based pricing per conversation is the monetization model. So I just want to confirm that we are going to add this in our monetization right in our current system for the credit. So can you also do a research to see how much should we price for the monetization and what's the model should we using uh underneath it is using you know AI here to generate a SQL query to run in our database. what are some of the tools that we're going to be calling right so that we can calculate the pricing for monetization. I'm not sure if we're going to do this later on in our steps here, but I just wanted to put it out there um before we're going to release this feature. So that's basically what I'm going to say. So the next section we're going to take a look at is phase 3.5 for the cross model second opinion. And this is basically going to have a second opinion from an individual or independent AI perspective. It will basically review the problem statements, the key answers, premise, landscape from this entire session without having seen this entire conversation, which will give us a second opinion on this for the future we're trying to build. So in this case, I'm going to say yes. Let's get a second opinion here to have a different sub agent here review this and try to see if there's anything that maybe we didn't think of. Right? So in this case, I'm going to say yes. Let's do that for the second opinion here. All right. So now you can see we have the second opinion from another sub agents and basically has review what the application does and also the answers we have here as well as everything that we have asked to review. So then after that it basically goes to the phase four for the alternative generation. So approach one is structure query mapper. So large language model here converts your natural language into a structure JSON intent maps to existing you know query that we have already built. So it doesn't generate a new query. It will basically use the existing query that we have and just map to that query. And here is the effort. So you can see it's going to be really low because we have the query defined. It's going to reuse the existing queries that we have. So that means that we have zero SQL injections for that which is really good. And that's basically the approach A which I really like. And the approach B here is direct SQL generation. So large language model here generates the parameterized SQL query against a read only uh SQL database view scope to the user's data. So basically we're going to have a different database and we're going to have large model here to generate whatever query that it that user asked for and it's going to basically run that for that only database right so it's only beble to create query that database based on the user's data and the risk here is being high because it handles like any query shape without a mapper for the updates and also the SQL injection could be part of it right needs a readonly database view and stuff like this so you know both approach you can see has some pros and con but there's also a hybrid one where yes we use the mapper but we can also to do a SQL fallback which will give us the best of both worlds which will have a safer mapper for common queries and SQL for edge cases. So you can see it gives you some approaches here that we can choose from. And the recommendation here is choosing option A here because it's the safest path to shipping reusing the entire existing infrastructure and cover 90% of the queries your users actually asking for and only the 10% of the queries that I can't handle are better to solve than by introducing the SQL generation risk. So you can see that's really good, right? is actually kind of like similar to the boil lake principle that the framework has actually introduced. So I actually really like this approach for generation the plan because this is probably the most safest way and also give us the fastest way to launch this MVP to the users. So in this case I'm going to choose an option one here and so far you can see we have consumed 130,000 for token assumptions for the conversation so far and currently we're at phase four. So approach A is chosen and currently it's going to proceed to next step. Okay. So after all those times we have been talking with the cloud here, the doc survived two rounds of the anniversary uh anniversar uh review 15 issue caught and fix and quality here is 8 out of 10. So it actually gives you a score out of this which is pretty cool and uh once we have this done so design doc for this ticket has been reviewed and refined. It covers problem statements, demand, evidence, approach and also 15 file for implementation plan, credit integrations, security model and success uh criteria. This is the output of step one in the planning pipeline. So the next steps are basically your spec team for detail spec then also the auto plan for CEO design engineer review and all those kind of roles right which is our different persona here to review the plan entirely. So in this case what would you like to do with the design doc? So I want to approve this but can I run this in a clear session due to I have consumed a lot of context here in this conversation already. If so uh what's the prompt that I can run in the nest clause session so that I can carry over for a fresh context window. So it says absolutely let me mark this as proved and save the handoff and here you can see it give you the exact command for the next session. So you can [clears throat] see I can still do that with a clear session especially for planning. Accuracy is so important. So I will highly recommend you know whenever you finish like one stage cuz currently I think we're at this stage right now for the office hour. We already complete this. So the next thing we're going to do is the spec team and the auto plan right so we want to ideally break it down right take this as like one claw session break it down save it in a handoff doc and then we're going to carry over in the next session for the next scale. Okay so you can see here it's going to write the plan here with the complete handoff for our net session. All right. So once we have the step one for the office hours done, next thing we're going to do is try to do the spec team and having AI agent here to basically create a spec for this feature that we're going to add. And notice here that the design doc here is actually saved in a root folder here for this MD file. And if you want to take a look at this, uh, basically this is what it looks like. So you can see we have our AI agent here for the expense query. So this is the ticket number and this is basically the product statement. So you can see we have the current design all in place here. So we can be able to take this MD file anywhere in a new claw session here and claw can do a still look at this as well. Right? So in this case I'm going to copy this prompt right here. Head over to a new claw code session here. You can see I'm going to trigger the spec team scale from the GStack and triggering the exact prompt. And you can see here that first it's going to trigger the spec team skill. Then it's going to start to look through the ticket and also looking through the state. So you can see that it's able to keep track of the current state as well for what current ticket is working on. And let's take a look at more here. So first question is asking is which area does do you want to discuss for the AI agents the design doc covers most decisions but these gray areas could use your input. So now this is going to be more kind of like once we have the directions down the next thing we're going to focus on is like okay how do we want to have the application to look like you know what kind of system what kind of infrastructure what kind of service we want right what kind of model we want this is going to be the place we're going to decide that so for example hey I want to you know make decision on the chat UI placement or maybe the large language model provider choice or the conversation context right and also the aggregation approach the design doc process the postgress RPC function function for the group by and sum. Alternatively, we can fetch rows and aggregate in JavaScript and the effects accuracy and also the scalability. So, I'm also going to choose that as well. And there's a couple more things like for example, what about the credits usage and what about the table view look like for the UI and is there any edge case that we need to consider. So, I also want to talk about that as well. So, that's basically my prompt. So, here I'm going to submit this and let's see what it does. Okay, cool. So, discussing all four areas plus your additional concerns. So where should the AI chat live in your dashboard? So definitely it's going to be in a dedicated page. So here we have our sidebar and there is a AI section or it could be a slide out panel. So user let's say currently on this page right now and there's going to be a side panel here where it's going to pop out and user can chat or it's going to be a floating widget here. Right? So, at the bottom here, oh, if you have questions, you can just display that. But I'm just going to choose the recommended approach for dedicated page because we're going to display uh more things on here like tables or visualizations. So, it will be nice to have it own dedicated page. So, I'm going to click on enter that for this. All right. So, the next part is the context. So, how much conversation context should the AM retain? And this will affect the prompt size, cost, and also the follow-up quality. So, here we have 5, 10, session only, and single query only. So in this case I'm going to choose five here because let's say user say hey I want to break that down by vendor then it knows exactly what it referenced to. So in this case I'm going to click on yes. Okay. So the next part we're going to take look at is aggregation. So how should we aggregate the data? Is it using the postgress RPC or it's going to be a JavaScript aggregation. Now both has different benefits. So RPC is going to live to query inside of our database. So when we query things it's just going to be calling that RPC function in our database to query data. And the other part we can do this is using the JavaScript aggregation. But I'm just going to say something on top of this. I'm going to say instead of using the JavaScript aggregation, I kind of want to use the subway OM, right? The object relation mapper here because let's say in the future we're going to switch to different database, right? So, you know, in this case, we can be able to have this function defined inside of our server actions or in our database in our backend logic and we can be able to trigger that function and let's say we're going to switch to different database, but the RM here, the OM logic here is still going to be the same. So, can this logic here be live in our back end here? so that we can be able to make it much more scalable and reusable in the future. Let's say we're going to switch to different database and this way it's also going to be less uh data migration because this is just only the functions for the queries that list inside of our back end. So that's basically what I want to achieve here and that's basically what I want to add onto this uh feature change and click on enter here. Okay. So once we have the aggregation logic in the backend service layer using subbase clients so the ORM style not the raw SQL RPCs portable if you want to switch database now let's cover your additional concerns so here you can see we have some additional questions for example the credits and also the table UI so how should the result table look in the chat and this affects both the AI response so if I were to zoom out a bit more so here you can see this is what the table look like so inline markdown for the table uh we have a style cascade for the table And also we have the card base. So um I would say is this so markdown is fine but we should definitely limit down how many records we should return right let's say you know user didn't specify or there should be a way that we can be able to hide or be able to expand or collapse right and be able to have the functionality here where user can be able to you know see it more clearly and also look through the chats right let's say user is going to refresh or come back to this chat um all the table here should be collapsed right or if there is a chat that's very long then we should definitely collapse this by default and and also reduce the load on how much data we're going to query right so let's say if user didn't specify that then we definitely want to uh mention that and then the other part is that we want to keep it minimal let's say user is going to uh fetch like a lot of records then we should definitely maybe send like some suggested uh some clarifications right before we're going to actually send something right so the chat here should also do some clarification here before it's going to um send out to the database here to fetch the right data and that's basically my answer. So I'm going to choose the inline for the markdown table and submit for the answer here. Okay. So finally you can see there's some additional questions like what are other dashboard page should be affected by the AI chat feature. So for example the sidebar right? So that's going to be adding the AI assistant here the dashboard home view. So try the AI assistant, the call to action card, and also for the receipts and transaction page, we're going to add like, hey, you can ask AI about this. But I'm just going to keep the scope here small. I'm not going to choose that for now. And the other part we're going to add here is our landing page. Making sure our landing page or blog page or any other parts. We're going to, you know, make sure that we add this. And the other part is the marketing. So we need to definitely add this feature as a shout out for the email list that we have inside of our system, right? making sure that we let user know that hey we have this feature in place doesn't matter they're paid or unpaid uh which tier they are in right so we need to let them know as well um they will get so we definitely need to use or trigger some marketing skills and try to see how we should be able to um email this instead of our email here and in terms of the edge case so for edge case here which scenario concerns you most for the spect address so empty data states so user with zero receives or transaction AI should guide them to import data first not return the empty results, right? That's the most important part. And the ambition query, so how much did I spend? So no time range, no categories. AI should ask for clarification. That's definitely true. And the other part is the cross currency. So uh for example, like maybe user has CD or USD receipts. Total spending needs to handle the mixed currency. Yes, we do have those currencies in place in our table. So it should be able to do that. And the rate limiting, so user spamming queries. So we should definitely have something like that as well. So in this case I'm just going to submit that as well and that's going to be our edge case here. So I'm going to submit this. And finally we have some additional question being asked. So cross currency uh queries. So CAD USD receives how should AI handle the mix uh currencies. So separate totals uh convert to the base currency. Yes, let's do the separate total is probably the best way to do it. All right. Perfect. So all areas are covered. ready to spin up different parallel research agent here to do the research. So launch the backend architect front designer and the QA strategist product manager here and the devil advocate agents in parallel here to do the research. So this is new this is really cool and I'm going to say yes let's start to do the research and I'm just going to let it do its thing at the background. So now you can see we have five different agents here has spun up and this is they're all doing research here with different angles backend front end QA product requirements and a devil advocates and here are their focus and right here you can see if you want to see this five agents we can click on this and these are currently the agents that are running right now. Okay. So, uh if you want to click on to view, click on enter here. If you don't want to view, uh you can just click on escape here to close. And I'm just going to wait for a bit until all the agents jobs are done. And we're just going to come back once everything's finished. Before we jump into the next part, I want to quickly show you something I've been using while building some of my projects. So, if you've ever used AI to generate code, you've probably noticed it works, but it also breaks in ways you don't always catch right away. That's basically where Test Sprite comes in. It's an AI testing agent that goes through your app, figures out what it's supposed to do, and then checks if everything actually works the way it should. Now, what's changed recently is how it fits into your workflow. So, I'm inside Cursor here, and through their MCP integration, it's not something I run separately. I can generate code, test it, fix things, and rerun everything right here in the IDE, which makes it feel way more natural when you're iterating. Where it gets really useful is when you start changing stuff. So, let's say I update part of the logic. instead of just running the same test again, it actually rechecks the flow and catches new issues that come from those changes. That's a big deal because most setups don't really handle that well once you start iterating. And if a test isn't quite right, you can actually edit it visually instead of digging through a bunch of test code. So, I can click into a step, adjust what it's checking, or regenerate part of the flow and keep everything else intact, which makes it a lot easier to control what's actually being tested. On top of that, they also added GitHub integration. So, whenever you push changes, it runs tests on your pull request and shows you exactly what passed or failed before you merge anything. It basically acts like a safety check so you don't accidentally ship something broken. Also, quick mention, they're running a hackathon right now with a $3,000 prize pool. So, if you're building anything or just experimenting with AI projects, it's actually a pretty fun way to try this out. I'll leave a link in the description if you want to check it out. Okay, now let's get back into the video. Okay, so it looks like everything's finished now and here you can see we have the entire spec are all covered and this is what the decisions been made and here is the complete spec. So once we have the spec, the next thing we're going to do is try to create using the auto plan here using different personality like CEO design review engineer review and the DX review here sequentially with the auto decisions using the auto plan feature to run a full review for the pipeline. So in this case, I'm going to use the auto plan scale here and basically point it out to the spec where the spec live inside of our backlog MD file and I'm just going to click on enter. All right. So finally you can see we have different sub agents here. For each sub aent that's going to be one persona. So we have the CEO persona here has run and here is their output. And we also have the the design sub agent here has run and review the spec. And here is his output. And then we also have the engineering design sub agent here to review. And here is its output as well. So eventually here you can see we have everything are all verified and once everything is all confirmed and modified our spec. So you can see total there are 41 findings 10 from CEO 15 from design and 16 from the engineering right to after has done the review for the spec and this is the three review phases that we have follow sequentially from CEO design engineering and each of them has its own sub agents and 22 decision has made and there's also some couple user decisions that we have flagged it along the way and I have already made the decision and you can see that this is the entire summary. Now the last part that I want to talk about is the token consumption. So these are the skills that we have went over for GStack. So for token consumption you can see here for the office hour we have consumed 170 for the spec team 200k and also the auto plan here also consume 200k,000 for tokens because we using different sub aents here. So in total here you can see we takes about 600k for token sumptions for the entire planning pipeline. That's how much it took for planning a feature on top a brownfield project. So at this point here, we can either use the build pipeline from GStack here to execute or the other way we can do here is basically try to use like GSD or super power here and try to execute this entire spec step by step. And of course, if you want to learn more about GSD and super powers, make sure to check out this video right here. I recently done a comparison between the two and in that video we give a brownfield project like this and basically adding a feature to add the end to end test coverage and have two framework here like super power and GSD here to both work on that same feature using git workshries and by the end of that video I went over the comparison between the two like which framework is better for executing the accuracy and the token assumption. So if you are learning more about like okay which framework for spectral element is the highest accuracy and has the low token lowest token consumption then make sure you check out that video. In that video we went over that. So pretty much that's it for this video. In this video we went over the office hours the spec team scale and also the auto plan from the GStack spectrum development framework. So pretty much that's what we covered in this video. So with that being said if you do thumb this video please make sure to like this video consider subscribe more content like this. But with that being said I'll see you in the next video. Why cominator CEO Gary Tain's claw code toolkit GStack has many specialized workflows but the one most people are sleeping on is the planning workflow. It challenged my assumptions narrow down what really matters research the competitive landscape and have [clears throat] five different AI agent here reviewing my spec from CEO design engineering QA and devil advocate perspective all before writing a single line of code. So, in this video, I'm going to show you my entire planning pipeline on building a feature on a real SAS project with paying customers. So, with that being said, if that sounds interesting, let's get into this. Now, before we continue, I recently launched our school community where I help you to master AI agents, automations, and so much more. And that's all coming from someone who used to work as a senior AI software engineer at companies like Amazon and Microsoft. And in this community, you're going to get over 100 plus video materials like templates and workflows that I personally built and sold over 100 plus times. On top of that, you're also going to get access to our weekly live calls. And just to give you an idea, this week we're actually running a claw code master class where we're going to dive into how to improve Claw Co's accuracy when we're going to use it to building applications. Plus, you're also going to get full community support where you're going to get a chance to ask questions and get direct answers back. So, if you're ready to level up, make sure you jump right in and I'll see you in a community. All right. All right. So, to get started, first we're going to install this onto our local machine. So, to do so, right here, you can see this is the exact step we're going to follow to basically just copy this, open your code claw code, and just paste it and have it to install this completely onto our project. Or the other way you can do this is you're simply just going to copy that repository, paste it, and tell claw to follow the repository and try to install this and set this up. So, once you have this all set up, the next thing we're going to take a look at is how we can beble to use it into our existing project. So, right here, you can see this is my existing project called Book Zero. And right now if I were to log into the application, here is what it looks like. So I wanted to build a feature onto this existing brownfield projects. Basically by adding a AI chat agent here to query the expense based on the project data. For example, how much did I spend on gas in quarter 1 or show me the top five vendor this month or find all the receipts over $100. Right? So these are all some queries that we can be able to pass this chat agent here that can convert into a SQL query that can query the data in our database. Now obviously this feature is not really 100% defined. I think that the requirement here still needs to be refined a bit more with different personalities and that's where the Gstack comes in which can help us to refine govern this plan making sure that the plan here is fully ready before we pass it to execution. So in this case I'm just going to copy this link for Jira ticket and I already have my J MCP set up on my local machine. So in this case, I'm just going to head over to claw code really quick. And I basically mention that, hey, I already have this installed. And let's say if I want to bring this feature onto this project, what are some skills that I can use to build this project using GStack? And right here, you can see it uses GStack skill to give me a workflow on exactly how we're going to build this feature onto it. Now, obviously, we're not going to use it to build the building pipeline because it doesn't really have the test-driven elements like what Superpower does. So, I'm going to use it to do the PL pipeline because I think this is what GStack really shines. So in this case, I'm going to open a brand new terminal session and start a clock code. I'm just going to copy this diagram right here, pass it to a new clock session. And basically, this is what I'm going to say. I want you to follow this entire planning pipeline and try to do this for this entire ticket. Can you help me to do this, please? So, I'm going to paste this as my prompt and switch it over to planning mode. And right away, you can see that it starts to gather the context on exactly what this ticket is and how we can be able to build this. So first it's going to launch different sub aents here try to understand the AI chat codebase right also data models and services that we have then it's going to ask me some serious question to configure our GSTA stack framework like can we be able to copy other projects coding patterns or what is the goal right now is it a startup is it a hackathon projects or having fun and for this project right now is it in the ideation phase is it in the paying customer phase or doesn't have any paying customers right now right and then now once we have this all set so the changes everything you have real signal to work from since you already have the revenue. So the question that matters are about the wedge, the observation, the future fit and let me start. So the backlog spec describe three phases basic queries uh comparison trends and proactive insights. That's a lot of surface area. What is the smallest possible version of this AI chat that a paying customer will actually use this week? Not after you built all three phases. So for example, maybe the spending summaries or the receipt finder, the tax prep helper, right? Right? So all those kind of things. So in this case, this is what I'm going to say. So based on the research that we have done, the customers are looking to add the spending summaries in our AI chat a lot often, right? So they want to see the spending predictions, the patterns they see for the spendings. They want to learn from this using our AI chats. And most importantly, we want to have data visualizations to display charts, tables, or all kinds of data visualizations for the queries that they're querying for. And most importantly, they should be able to have the ability to save the conversation and also save the stats or the visualization and maybe add that into our data the dashboard and they can be able to review that in the later times. Most importantly, we need to have it to integrate it into our credit system so that they can be able to see the credit goes down when they have a conversation, right? So, how much we should charge per credit for per conversation or per chat? We need to define that as well. So there's a lot of things in place and I want you to package all together into this plan here. And basically you can see that's my prompt. Now this is there's a lot of things in the prompts. You can see it says I respect the ambition. I need to push back. You describe five features like spend analysis, chart visualizations, save queries, dashboard customizations, and credit based monetizations. This is not a wish. It's actually a platform. So we need to push back a bit more and we need to try to understand exactly what can users use right now this week after we have the MVP done. So here you can see pick one things that generate the word of mouth. Everything else can come in phase two. So how much did I spend on this category this quarter, right? What are my top expense for this month or show me the unusual spending this month or something like that, right? So you can see that it start to breaking this large prompts or large demand or large request into a step-by-step process that we can build the first MVP first. Then we're going to you know push back and adding those additional functionalities into phase 2 if we have time right so you can see these are the things that we have so in this case I'm just going to say hey uh all of them looks good right so show me the unusual spendings or um basically try to learn more about the spending that they made that's good and I think this is probably the feature we need to add right so all those queries should be in place yes we can you know forget about the charts but we definitely need to add the tables right be able to have user here to visualize things much more easier rather than just bunch of text. And furthermore, we also definitely need to support those queries to be able to fetch in our database and be able to have user here to understand their spending patterns. So that's basically my prompt and I'm just going to say yes and let's have it to basically plan this bit more and dive deep into how we're going to achieve this. Then it's asking me another PM kind of questions like have you sat down and watched how they use this platform without helping them? Did they struggle somewhere that you thought was obvious or did you ignore a feature you might you might thought uh was important. So this is kind of like a PM question and of course you cannot have this without like data or like user tracking all kind of things. So I actually made a video on the claw skills for marketings. In that video I demonstrate how you can be able to set up the entire tracking system like the usage you know have user fully on boarded like what have they done after they on boarded the entire user tracking here. I actually had made a video on this. So if you want to learn really more about how you can do this set of the tracking, make sure to check out that video right there. And I do have real usage for this specific surprise that I want to share. Yeah. So I want to say yes to this. And here you can see it says you have watched user that's good. Most founder at your stage here doesn't have that. So what surprise you and what the users do with book zero that didn't you expect. And this matters because AI chat features come from things user are already trying to do and just making it instant instead of the manual process. So one of the option that they give me is they export data to understand patterns and that is actually something that I found too not just from the AI but actually I found it as well that users actually turning to CSV here to analyze data rather than just doing it in our platform because in our dashboard there's only five charts and that's static for all users. Then we also have some other options like they ask question that I haven't anticipated or they struggle with the filter search from the UI. So all three options are pretty valid. So I'm just going to say based on these things that we have here first two is probably the most surprising that [clears throat] I want to resolve using this feature and that's basically what I wanted to add and I'm just going to say yes. So in this case I'm just going to enter this and let claw here to figure this out. Okay. So eventually here you can see this is what it responds. So this is a real signal user are exporting CSV to answer the questions that our platform should have this natively. So this is the what the future fit look like. So it actually look through the past this and look through the future here to see if it's actually meaningful in 3 years. So if AI gets cheaper, everyone has their own tools and the bookkeeping tools here in multiplies. Does this feature in our AI chat become more central or less? And honestly, I think this is kind of like a bonus feature from this framework to help you to look to the future to see if this feature is not replicatable or is unique compared to other competitors. So let's say every competitor now eventually add this feature like ask AI about your expense. What's your thesis about why your platform your your versions win? Right? Is it because of data that you have or is it because the domain knowledge or is it could be something else right like if you were to add this feature and other people are adding this feature you know what are some uniqueness what are some selling points what makes our platform our feature here from this platform different compared to others right so you can see it gives me some list of options here so in this case I'm going to take some time and try to answer this question and we're just going to proceed forward okay so after we have that answer submitted here you can see it basically is going to start to do some research and basically try to figure out what's the landscape for this feature that we're trying ad. Okay. So then it has done some research on the landscape for the AI conversational expense management and the conversational bookkeeping AI assistant for common mistakes in 2025 and 2026. So here is what it found. So layer one we have AI chatbot for small businesses are mainstream. Yes, that's good. And AI space is crowded with tools that try to do bookkeeping for like auto categorizations or auto reconciliations or auto filing but hallucination here and miscatategorization are the number one concerns across industry. So that's what it found for the concern and layer two here is that the shifting from child bots to agentic AI tools that take actions not just like answering questions is number one thing and the AI hallucination and bookkeeping is real. So hallucination here is a big problem and layer three here is about what's interesting our on our position here. So our AI here doesn't do bookkeeping. Our AI here only query data that are exist and most AI competitor here tries to generate accounting entries and that's where hallucination kills you. your AI answer questions about verified human review scripts or receives transaction data. So the accuracy here is higher because we're only querying structure data not generating any financial records which is what separates that apart. So you can see that that's the basically the difference right the clear difference here is that our AI doesn't hallucination your finance it reads what's actually there and that's it once we have our research done the next thing I'm going to do here is phase three for challenging our premise so here is the premise so here are the premise that I'm working from I need you to agree or disagree with the each so user want a natural language uh queries because they actually currently export CSV to answer the questions that the UI doesn't cover and the MVP here is spending analysis and unusual spending detections tables, no charts, no save queries or dashboard customizations and the credit based pricing promization is monetization model. AI query existing data only. This is the accuracy advantage plus the anomaly detection charts save queries proactive insights are in phase two and response time should be less than 5 seconds is the targets. So do we agree with all six? So you can see that it's actually able to break it and try to refine the plan here step by step on exactly what's the requirements which is a really structured way to do it. So here I'm just going to say yes I do agree with all six but one thing that I want to add here is or in this case confirm you mentioned about the credit based pricing per conversation is the monetization model. So I just want to confirm that we are going to add this in our monetization right in our current system for the credit. So can you also do a research to see how much should we price for the monetization and what's the model should we using uh underneath it is using you know AI here to generate a SQL query to run in our database. what are some of the tools that we're going to be calling right so that we can calculate the pricing for monetization. I'm not sure if we're going to do this later on in our steps here, but I just wanted to put it out there um before we're going to release this feature. So that's basically what I'm going to say. So the next section we're going to take a look at is phase 3.5 for the cross model second opinion. And this is basically going to have a second opinion from an individual or independent AI perspective. It will basically review the problem statements, the key answers, premise, landscape from this entire session without having seen this entire conversation, which will give us a second opinion on this for the future we're trying to build. So in this case, I'm going to say yes. Let's get a second opinion here to have a different sub agent here review this and try to see if there's anything that maybe we didn't think of. Right? So in this case, I'm going to say yes. Let's do that for the second opinion here. All right. So now you can see we have the second opinion from another sub agents and basically has review what the application does and also the answers we have here as well as everything that we have asked to review. So then after that it basically goes to the phase four for the alternative generation. So approach one is structure query mapper. So large language model here converts your natural language into a structure JSON intent maps to existing you know query that we have already built. So it doesn't generate a new query. It will basically use the existing query that we have and just map to that query. And here is the effort. So you can see it's going to be really low because we have the query defined. It's going to reuse the existing queries that we have. So that means that we have zero SQL injections for that which is really good. And that's basically the approach A which I really like. And the approach B here is direct SQL generation. So large language model here generates the parameterized SQL query against a read only uh SQL database view scope to the user's data. So basically we're going to have a different database and we're going to have large model here to generate whatever query that it that user asked for and it's going to basically run that for that only database right so it's only beble to create query that database based on the user's data and the risk here is being high because it handles like any query shape without a mapper for the updates and also the SQL injection could be part of it right needs a readonly database view and stuff like this so you know both approach you can see has some pros and con but there's also a hybrid one where yes we use the mapper but we can also to do a SQL fallback which will give us the best of both worlds which will have a safer mapper for common queries and SQL for edge cases. So you can see it gives you some approaches here that we can choose from. And the recommendation here is choosing option A here because it's the safest path to shipping reusing the entire existing infrastructure and cover 90% of the queries your users actually asking for and only the 10% of the queries that I can't handle are better to solve than by introducing the SQL generation risk. So you can see that's really good, right? is actually kind of like similar to the boil lake principle that the framework has actually introduced. So I actually really like this approach for generation the plan because this is probably the most safest way and also give us the fastest way to launch this MVP to the users. So in this case I'm going to choose an option one here and so far you can see we have consumed 130,000 for token assumptions for the conversation so far and currently we're at phase four. So approach A is chosen and currently it's going to proceed to next step. Okay. So after all those times we have been talking with the cloud here, the doc survived two rounds of the anniversary uh anniversar uh review 15 issue caught and fix and quality here is 8 out of 10. So it actually gives you a score out of this which is pretty cool and uh once we have this done so design doc for this ticket has been reviewed and refined. It covers problem statements, demand, evidence, approach and also 15 file for implementation plan, credit integrations, security model and success uh criteria. This is the output of step one in the planning pipeline. So the next steps are basically your spec team for detail spec then also the auto plan for CEO design engineer review and all those kind of roles right which is our different persona here to review the plan entirely. So in this case what would you like to do with the design doc? So I want to approve this but can I run this in a clear session due to I have consumed a lot of context here in this conversation already. If so uh what's the prompt that I can run in the nest clause session so that I can carry over for a fresh context window. So it says absolutely let me mark this as proved and save the handoff and here you can see it give you the exact command for the next session. So you can [clears throat] see I can still do that with a clear session especially for planning. Accuracy is so important. So I will highly recommend you know whenever you finish like one stage cuz currently I think we're at this stage right now for the office hour. We already complete this. So the next thing we're going to do is the spec team and the auto plan right so we want to ideally break it down right take this as like one claw session break it down save it in a handoff doc and then we're going to carry over in the next session for the next scale. Okay so you can see here it's going to write the plan here with the complete handoff for our net session. All right. So once we have the step one for the office hours done, next thing we're going to do is try to do the spec team and having AI agent here to basically create a spec for this feature that we're going to add. And notice here that the design doc here is actually saved in a root folder here for this MD file. And if you want to take a look at this, uh, basically this is what it looks like. So you can see we have our AI agent here for the expense query. So this is the ticket number and this is basically the product statement. So you can see we have the current design all in place here. So we can be able to take this MD file anywhere in a new claw session here and claw can do a still look at this as well. Right? So in this case I'm going to copy this prompt right here. Head over to a new claw code session here. You can see I'm going to trigger the spec team scale from the GStack and triggering the exact prompt. And you can see here that first it's going to trigger the spec team skill. Then it's going to start to look through the ticket and also looking through the state. So you can see that it's able to keep track of the current state as well for what current ticket is working on. And let's take a look at more here. So first question is asking is which area does do you want to discuss for the AI agents the design doc covers most decisions but these gray areas could use your input. So now this is going to be more kind of like once we have the directions down the next thing we're going to focus on is like okay how do we want to have the application to look like you know what kind of system what kind of infrastructure what kind of service we want right what kind of model we want this is going to be the place we're going to decide that so for example hey I want to you know make decision on the chat UI placement or maybe the large language model provider choice or the conversation context right and also the aggregation approach the design doc process the postgress RPC function function for the group by and sum. Alternatively, we can fetch rows and aggregate in JavaScript and the effects accuracy and also the scalability. So, I'm also going to choose that as well. And there's a couple more things like for example, what about the credits usage and what about the table view look like for the UI and is there any edge case that we need to consider. So, I also want to talk about that as well. So, that's basically my prompt. So, here I'm going to submit this and let's see what it does. Okay, cool. So, discussing all four areas plus your additional concerns. So where should the AI chat live in your dashboard? So definitely it's going to be in a dedicated page. So here we have our sidebar and there is a AI section or it could be a slide out panel. So user let's say currently on this page right now and there's going to be a side panel here where it's going to pop out and user can chat or it's going to be a floating widget here. Right? So, at the bottom here, oh, if you have questions, you can just display that. But I'm just going to choose the recommended approach for dedicated page because we're going to display uh more things on here like tables or visualizations. So, it will be nice to have it own dedicated page. So, I'm going to click on enter that for this. All right. So, the next part is the context. So, how much conversation context should the AM retain? And this will affect the prompt size, cost, and also the follow-up quality. So, here we have 5, 10, session only, and single query only. So in this case I'm going to choose five here because let's say user say hey I want to break that down by vendor then it knows exactly what it referenced to. So in this case I'm going to click on yes. Okay. So the next part we're going to take look at is aggregation. So how should we aggregate the data? Is it using the postgress RPC or it's going to be a JavaScript aggregation. Now both has different benefits. So RPC is going to live to query inside of our database. So when we query things it's just going to be calling that RPC function in our database to query data. And the other part we can do this is using the JavaScript aggregation. But I'm just going to say something on top of this. I'm going to say instead of using the JavaScript aggregation, I kind of want to use the subway OM, right? The object relation mapper here because let's say in the future we're going to switch to different database, right? So, you know, in this case, we can be able to have this function defined inside of our server actions or in our database in our backend logic and we can be able to trigger that function and let's say we're going to switch to different database, but the RM here, the OM logic here is still going to be the same. So, can this logic here be live in our back end here? so that we can be able to make it much more scalable and reusable in the future. Let's say we're going to switch to different database and this way it's also going to be less uh data migration because this is just only the functions for the queries that list inside of our back end. So that's basically what I want to achieve here and that's basically what I want to add onto this uh feature change and click on enter here. Okay. So once we have the aggregation logic in the backend service layer using subbase clients so the ORM style not the raw SQL RPCs portable if you want to switch database now let's cover your additional concerns so here you can see we have some additional questions for example the credits and also the table UI so how should the result table look in the chat and this affects both the AI response so if I were to zoom out a bit more so here you can see this is what the table look like so inline markdown for the table uh we have a style cascade for the table And also we have the card base. So um I would say is this so markdown is fine but we should definitely limit down how many records we should return right let's say you know user didn't specify or there should be a way that we can be able to hide or be able to expand or collapse right and be able to have the functionality here where user can be able to you know see it more clearly and also look through the chats right let's say user is going to refresh or come back to this chat um all the table here should be collapsed right or if there is a chat that's very long then we should definitely collapse this by default and and also reduce the load on how much data we're going to query right so let's say if user didn't specify that then we definitely want to uh mention that and then the other part is that we want to keep it minimal let's say user is going to uh fetch like a lot of records then we should definitely maybe send like some suggested uh some clarifications right before we're going to actually send something right so the chat here should also do some clarification here before it's going to um send out to the database here to fetch the right data and that's basically my answer. So I'm going to choose the inline for the markdown table and submit for the answer here. Okay. So finally you can see there's some additional questions like what are other dashboard page should be affected by the AI chat feature. So for example the sidebar right? So that's going to be adding the AI assistant here the dashboard home view. So try the AI assistant, the call to action card, and also for the receipts and transaction page, we're going to add like, hey, you can ask AI about this. But I'm just going to keep the scope here small. I'm not going to choose that for now. And the other part we're going to add here is our landing page. Making sure our landing page or blog page or any other parts. We're going to, you know, make sure that we add this. And the other part is the marketing. So we need to definitely add this feature as a shout out for the email list that we have inside of our system, right? making sure that we let user know that hey we have this feature in place doesn't matter they're paid or unpaid uh which tier they are in right so we need to let them know as well um they will get so we definitely need to use or trigger some marketing skills and try to see how we should be able to um email this instead of our email here and in terms of the edge case so for edge case here which scenario concerns you most for the spect address so empty data states so user with zero receives or transaction AI should guide them to import data first not return the empty results, right? That's the most important part. And the ambition query, so how much did I spend? So no time range, no categories. AI should ask for clarification. That's definitely true. And the other part is the cross currency. So uh for example, like maybe user has CD or USD receipts. Total spending needs to handle the mixed currency. Yes, we do have those currencies in place in our table. So it should be able to do that. And the rate limiting, so user spamming queries. So we should definitely have something like that as well. So in this case I'm just going to submit that as well and that's going to be our edge case here. So I'm going to submit this. And finally we have some additional question being asked. So cross currency uh queries. So CAD USD receives how should AI handle the mix uh currencies. So separate totals uh convert to the base currency. Yes, let's do the separate total is probably the best way to do it. All right. Perfect. So all areas are covered. ready to spin up different parallel research agent here to do the research. So launch the backend architect front designer and the QA strategist product manager here and the devil advocate agents in parallel here to do the research. So this is new this is really cool and I'm going to say yes let's start to do the research and I'm just going to let it do its thing at the background. So now you can see we have five different agents here has spun up and this is they're all doing research here with different angles backend front end QA product requirements and a devil advocates and here are their focus and right here you can see if you want to see this five agents we can click on this and these are currently the agents that are running right now. Okay. So, uh if you want to click on to view, click on enter here. If you don't want to view, uh you can just click on escape here to close. And I'm just going to wait for a bit until all the agents jobs are done. And we're just going to come back once everything's finished. Before we jump into the next part, I want to quickly show you something I've been using while building some of my projects. So, if you've ever used AI to generate code, you've probably noticed it works, but it also breaks in ways you don't always catch right away. That's basically where Test Sprite comes in. It's an AI testing agent that goes through your app, figures out what it's supposed to do, and then checks if everything actually works the way it should. Now, what's changed recently is how it fits into your workflow. So, I'm inside Cursor here, and through their MCP integration, it's not something I run separately. I can generate code, test it, fix things, and rerun everything right here in the IDE, which makes it feel way more natural when you're iterating. Where it gets really useful is when you start changing stuff. So, let's say I update part of the logic. instead of just running the same test again, it actually rechecks the flow and catches new issues that come from those changes. That's a big deal because most setups don't really handle that well once you start iterating. And if a test isn't quite right, you can actually edit it visually instead of digging through a bunch of test code. So, I can click into a step, adjust what it's checking, or regenerate part of the flow and keep everything else intact, which makes it a lot easier to control what's actually being tested. On top of that, they also added GitHub integration. So, whenever you push changes, it runs tests on your pull request and shows you exactly what passed or failed before you merge anything. It basically acts like a safety check so you don't accidentally ship something broken. Also, quick mention, they're running a hackathon right now with a $3,000 prize pool. So, if you're building anything or just experimenting with AI projects, it's actually a pretty fun way to try this out. I'll leave a link in the description if you want to check it out. Okay, now let's get back into the video. Okay, so it looks like everything's finished now and here you can see we have the entire spec are all covered and this is what the decisions been made and here is the complete spec. So once we have the spec, the next thing we're going to do is try to create using the auto plan here using different personality like CEO design review engineer review and the DX review here sequentially with the auto decisions using the auto plan feature to run a full review for the pipeline. So in this case, I'm going to use the auto plan scale here and basically point it out to the spec where the spec live inside of our backlog MD file and I'm just going to click on enter. All right. So finally you can see we have different sub agents here. For each sub aent that's going to be one persona. So we have the CEO persona here has run and here is their output. And we also have the the design sub agent here has run and review the spec. And here is his output. And then we also have the engineering design sub agent here to review. And here is its output as well. So eventually here you can see we have everything are all verified and once everything is all confirmed and modified our spec. So you can see total there are 41 findings 10 from CEO 15 from design and 16 from the engineering right to after has done the review for the spec and this is the three review phases that we have follow sequentially from CEO design engineering and each of them has its own sub agents and 22 decision has made and there's also some couple user decisions that we have flagged it along the way and I have already made the decision and you can see that this is the entire summary. Now the last part that I want to talk about is the token consumption. So these are the skills that we have went over for GStack. So for token consumption you can see here for the office hour we have consumed 170 for the spec team 200k and also the auto plan here also consume 200k,000 for tokens because we using different sub aents here. So in total here you can see we takes about 600k for token sumptions for the entire planning pipeline. That's how much it took for planning a feature on top a brownfield project. So at this point here, we can either use the build pipeline from GStack here to execute or the other way we can do here is basically try to use like GSD or super power here and try to execute this entire spec step by step. And of course, if you want to learn more about GSD and super powers, make sure to check out this video right here. I recently done a comparison between the two and in that video we give a brownfield project like this and basically adding a feature to add the end to end test coverage and have two framework here like super power and GSD here to both work on that same feature using git workshries and by the end of that video I went over the comparison between the two like which framework is better for executing the accuracy and the token assumption. So if you are learning more about like okay which framework for spectral element is the highest accuracy and has the low token lowest token consumption then make sure you check out that video. In that video we went over that. So pretty much that's it for this video. In this video we went over the office hours the spec team scale and also the auto plan from the GStack spectrum development framework. So pretty much that's what we covered in this video. So with that being said if you do thumb this video please make sure to like this video consider subscribe more content like this. But with that being said I'll see you in the next video.

---

## Timestamped Segments

**[0:00]** Why cominator CEO Gary Tain's claw code toolkit GStack has many specialized workflows but the one most people are

**[0:06]** sleeping on is the planning workflow. It challenged my assumptions narrow down what really matters research the

**[0:11]** competitive landscape and have [clears throat] five different AI agent here reviewing my spec from CEO design

**[0:17]** engineering QA and devil advocate perspective all before writing a single

**[0:22]** line of code. So, in this video, I'm going to show you my entire planning pipeline on building a feature on a real

**[0:28]** SAS project with paying customers. So, with that being said, if that sounds interesting, let's get into this. Now,

**[0:33]** before we continue, I recently launched our school community where I help you to master AI agents, automations, and so

**[0:39]** much more. And that's all coming from someone who used to work as a senior AI software engineer at companies like

**[0:44]** Amazon and Microsoft. And in this community, you're going to get over 100 plus video materials like templates and

**[0:50]** workflows that I personally built and sold over 100 plus times. On top of that, you're also going to get access to

**[0:56]** our weekly live calls. And just to give you an idea, this week we're actually running a claw code master class where

**[1:01]** we're going to dive into how to improve Claw Co's accuracy when we're going to use it to building applications. Plus,

**[1:06]** you're also going to get full community support where you're going to get a chance to ask questions and get direct answers back. So, if you're ready to

**[1:12]** level up, make sure you jump right in and I'll see you in a community. All right. All right. So, to get started, first we're going to install this onto

**[1:17]** our local machine. So, to do so, right here, you can see this is the exact step we're going to follow to basically just copy this, open your code claw code, and

**[1:23]** just paste it and have it to install this completely onto our project. Or the other way you can do this is you're simply just going to copy that

**[1:29]** repository, paste it, and tell claw to follow the repository and try to install this and set this up. So, once you have

**[1:35]** this all set up, the next thing we're going to take a look at is how we can beble to use it into our existing project. So, right here, you can see

**[1:41]** this is my existing project called Book Zero. And right now if I were to log into the application, here is what it

**[1:46]** looks like. So I wanted to build a feature onto this existing brownfield projects. Basically by adding a AI chat

**[1:52]** agent here to query the expense based on the project data. For example, how much did I spend on gas in quarter 1 or show

**[1:59]** me the top five vendor this month or find all the receipts over $100. Right? So these are all some queries that we

**[2:06]** can be able to pass this chat agent here that can convert into a SQL query that can query the data in our database. Now

**[2:12]** obviously this feature is not really 100% defined. I think that the requirement here still needs to be refined a bit more with different

**[2:18]** personalities and that's where the Gstack comes in which can help us to refine govern this plan making sure that

**[2:24]** the plan here is fully ready before we pass it to execution. So in this case I'm just going to copy this link for

**[2:29]** Jira ticket and I already have my J MCP set up on my local machine. So in this case, I'm just going to head over to claw code really quick. And I basically

**[2:36]** mention that, hey, I already have this installed. And let's say if I want to bring this feature onto this project, what are some skills that I can use to

**[2:43]** build this project using GStack? And right here, you can see it uses GStack skill to give me a workflow on exactly

**[2:48]** how we're going to build this feature onto it. Now, obviously, we're not going to use it to build the building pipeline

**[2:53]** because it doesn't really have the test-driven elements like what Superpower does. So, I'm going to use it to do the PL pipeline because I think

**[3:00]** this is what GStack really shines. So in this case, I'm going to open a brand new terminal session and start a clock code.

**[3:06]** I'm just going to copy this diagram right here, pass it to a new clock session. And basically, this is what I'm going to say. I want you to follow this

**[3:12]** entire planning pipeline and try to do this for this entire ticket. Can you help me to do this, please? So, I'm

**[3:19]** going to paste this as my prompt and switch it over to planning mode. And right away, you can see that it starts to gather the context on exactly what

**[3:25]** this ticket is and how we can be able to build this. So first it's going to launch different sub aents here try to

**[3:30]** understand the AI chat codebase right also data models and services that we have then it's going to ask me some serious question to configure our GSTA

**[3:37]** stack framework like can we be able to copy other projects coding patterns or what is the goal right now is it a

**[3:42]** startup is it a hackathon projects or having fun and for this project right now is it in the ideation phase is it in

**[3:49]** the paying customer phase or doesn't have any paying customers right now right and then now once we have this all

**[3:54]** set so the changes everything you have real signal to work from since you already have the revenue. So the

**[4:01]** question that matters are about the wedge, the observation, the future fit and let me start. So the backlog spec

**[4:07]** describe three phases basic queries uh comparison trends and proactive insights. That's a lot of surface area.

**[4:14]** What is the smallest possible version of this AI chat that a paying customer will actually use this week? Not after you

**[4:20]** built all three phases. So for example, maybe the spending summaries or the receipt finder, the tax prep helper,

**[4:27]** right? Right? So all those kind of things. So in this case, this is what I'm going to say. So based on the research that we have done, the customers are looking to add the

**[4:33]** spending summaries in our AI chat a lot often, right? So they want to see the spending predictions, the patterns they

**[4:41]** see for the spendings. They want to learn from this using our AI chats. And most importantly, we want to have data

**[4:47]** visualizations to display charts, tables, or all kinds of data visualizations for the queries that

**[4:52]** they're querying for. And most importantly, they should be able to have the ability to save the conversation and also save the stats or the visualization

**[5:00]** and maybe add that into our data the dashboard and they can be able to review that in the later times. Most

**[5:06]** importantly, we need to have it to integrate it into our credit system so that they can be able to see the credit

**[5:12]** goes down when they have a conversation, right? So, how much we should charge per credit for per conversation or per chat?

**[5:17]** We need to define that as well. So there's a lot of things in place and I want you to package all together into this plan here. And basically you can

**[5:24]** see that's my prompt. Now this is there's a lot of things in the prompts. You can see it says I respect the ambition. I need to push back. You

**[5:30]** describe five features like spend analysis, chart visualizations, save queries, dashboard customizations, and

**[5:36]** credit based monetizations. This is not a wish. It's actually a platform. So we need to push back a bit more and we need

**[5:41]** to try to understand exactly what can users use right now this week after we have the MVP done. So here you can see

**[5:47]** pick one things that generate the word of mouth. Everything else can come in phase two. So how much did I spend on

**[5:53]** this category this quarter, right? What are my top expense for this month or

**[5:59]** show me the unusual spending this month or something like that, right? So you can see that it start to breaking this

**[6:04]** large prompts or large demand or large request into a step-by-step process that

**[6:09]** we can build the first MVP first. Then we're going to you know push back and adding those additional functionalities

**[6:15]** into phase 2 if we have time right so you can see these are the things that we have so in this case I'm just going to

**[6:20]** say hey uh all of them looks good right so show me the unusual spendings or um

**[6:26]** basically try to learn more about the spending that they made that's good and I think this is probably the feature we

**[6:31]** need to add right so all those queries should be in place yes we can you know forget about the charts but we

**[6:37]** definitely need to add the tables right be able to have user here to visualize things much more easier rather than just

**[6:43]** bunch of text. And furthermore, we also definitely need to support those queries to be able to fetch in our database and

**[6:48]** be able to have user here to understand their spending patterns. So that's basically my prompt and I'm just going

**[6:54]** to say yes and let's have it to basically plan this bit more and dive deep into how we're going to achieve

**[6:59]** this. Then it's asking me another PM kind of questions like have you sat down and watched how they use this platform

**[7:05]** without helping them? Did they struggle somewhere that you thought was obvious or did you ignore a feature you might

**[7:11]** you might thought uh was important. So this is kind of like a PM question and of course you cannot have this without

**[7:17]** like data or like user tracking all kind of things. So I actually made a video on the claw skills for marketings. In that

**[7:23]** video I demonstrate how you can be able to set up the entire tracking system like the usage you know have user fully

**[7:28]** on boarded like what have they done after they on boarded the entire user tracking here. I actually had made a video on this. So if you want to learn

**[7:35]** really more about how you can do this set of the tracking, make sure to check out that video right there. And I do have real usage for this specific

**[7:41]** surprise that I want to share. Yeah. So I want to say yes to this. And here you can see it says you have watched user that's good. Most founder at your stage

**[7:47]** here doesn't have that. So what surprise you and what the users do with book zero that didn't you expect. And this matters

**[7:54]** because AI chat features come from things user are already trying to do and just making it instant instead of the

**[8:00]** manual process. So one of the option that they give me is they export data to understand patterns and that is actually

**[8:05]** something that I found too not just from the AI but actually I found it as well that users actually turning to CSV here

**[8:11]** to analyze data rather than just doing it in our platform because in our dashboard there's only five charts and that's static for all users. Then we

**[8:17]** also have some other options like they ask question that I haven't anticipated or they struggle with the filter search

**[8:23]** from the UI. So all three options are pretty valid. So I'm just going to say based on these things that we have here first two is probably the most

**[8:29]** surprising that [clears throat] I want to resolve using this feature and that's basically what I wanted to add and I'm

**[8:35]** just going to say yes. So in this case I'm just going to enter this and let claw here to figure this out. Okay. So eventually here you can see this is what

**[8:40]** it responds. So this is a real signal user are exporting CSV to answer the questions that our platform should have

**[8:46]** this natively. So this is the what the future fit look like. So it actually look through the past this and look

**[8:51]** through the future here to see if it's actually meaningful in 3 years. So if AI gets cheaper, everyone has their own

**[8:57]** tools and the bookkeeping tools here in multiplies. Does this feature in our AI chat become more central or less? And

**[9:04]** honestly, I think this is kind of like a bonus feature from this framework to help you to look to the future to see if this feature is not replicatable or is

**[9:11]** unique compared to other competitors. So let's say every competitor now eventually add this feature like ask AI

**[9:16]** about your expense. What's your thesis about why your platform your your versions win? Right? Is it because of

**[9:23]** data that you have or is it because the domain knowledge or is it could be something else right like if you were to

**[9:28]** add this feature and other people are adding this feature you know what are some uniqueness what are some selling points what makes our platform our

**[9:35]** feature here from this platform different compared to others right so you can see it gives me some list of options here so in this case I'm going

**[9:41]** to take some time and try to answer this question and we're just going to proceed forward okay so after we have that answer submitted here you can see it

**[9:47]** basically is going to start to do some research and basically try to figure out what's the landscape for this feature that we're trying ad. Okay. So then it

**[9:54]** has done some research on the landscape for the AI conversational expense management and the conversational bookkeeping AI assistant for common

**[10:00]** mistakes in 2025 and 2026. So here is what it found. So layer one we have AI

**[10:05]** chatbot for small businesses are mainstream. Yes, that's good. And AI space is crowded with tools that try to

**[10:11]** do bookkeeping for like auto categorizations or auto reconciliations or auto filing but hallucination here

**[10:17]** and miscatategorization are the number one concerns across industry. So that's what it found for the concern and layer

**[10:22]** two here is that the shifting from child bots to agentic AI tools that take actions not just like answering

**[10:28]** questions is number one thing and the AI hallucination and bookkeeping is real. So hallucination here is a big problem

**[10:34]** and layer three here is about what's interesting our on our position here. So our AI here doesn't do bookkeeping. Our

**[10:39]** AI here only query data that are exist and most AI competitor here tries to generate accounting entries and that's

**[10:45]** where hallucination kills you. your AI answer questions about verified human review scripts or receives transaction

**[10:51]** data. So the accuracy here is higher because we're only querying structure data not generating any financial

**[10:56]** records which is what separates that apart. So you can see that that's the basically the difference right the clear

**[11:02]** difference here is that our AI doesn't hallucination your finance it reads what's actually there and that's it once

**[11:07]** we have our research done the next thing I'm going to do here is phase three for challenging our premise so here is the

**[11:12]** premise so here are the premise that I'm working from I need you to agree or disagree with the each so user want a

**[11:19]** natural language uh queries because they actually currently export CSV to answer the questions that the UI doesn't cover

**[11:25]** and the MVP here is spending analysis and unusual spending detections tables, no charts, no save queries or

**[11:32]** dashboard customizations and the credit based pricing promization is monetization model. AI query existing

**[11:38]** data only. This is the accuracy advantage plus the anomaly detection charts save queries proactive insights

**[11:43]** are in phase two and response time should be less than 5 seconds is the targets. So do we agree with all six? So

**[11:49]** you can see that it's actually able to break it and try to refine the plan here step by step on exactly what's the

**[11:55]** requirements which is a really structured way to do it. So here I'm just going to say yes I do agree with all six but one thing that I want to add

**[12:01]** here is or in this case confirm you mentioned about the credit based pricing per conversation is the monetization

**[12:07]** model. So I just want to confirm that we are going to add this in our monetization right in our current system

**[12:12]** for the credit. So can you also do a research to see how much should we price for the monetization and what's the

**[12:18]** model should we using uh underneath it is using you know AI here to generate a SQL query to run in our database. what

**[12:24]** are some of the tools that we're going to be calling right so that we can calculate the pricing for monetization. I'm not sure if we're going to do this

**[12:29]** later on in our steps here, but I just wanted to put it out there um before we're going to release this feature. So

**[12:35]** that's basically what I'm going to say. So the next section we're going to take a look at is phase 3.5 for the cross

**[12:40]** model second opinion. And this is basically going to have a second opinion from an individual or independent AI

**[12:46]** perspective. It will basically review the problem statements, the key answers, premise, landscape from this entire

**[12:52]** session without having seen this entire conversation, which will give us a second opinion on this for the future

**[12:57]** we're trying to build. So in this case, I'm going to say yes. Let's get a second opinion here to have a different sub agent here review this and try to see if

**[13:03]** there's anything that maybe we didn't think of. Right? So in this case, I'm going to say yes. Let's do that for the second opinion here. All right. So now

**[13:10]** you can see we have the second opinion from another sub agents and basically has review what the application does and

**[13:16]** also the answers we have here as well as everything that we have asked to review. So then after that it basically goes to

**[13:22]** the phase four for the alternative generation. So approach one is structure query mapper. So large language model

**[13:28]** here converts your natural language into a structure JSON intent maps to existing you know query that we have already

**[13:34]** built. So it doesn't generate a new query. It will basically use the existing query that we have and just map to that query. And here is the effort.

**[13:40]** So you can see it's going to be really low because we have the query defined. It's going to reuse the existing queries that we have. So that means that we have

**[13:47]** zero SQL injections for that which is really good. And that's basically the approach A which I really like. And the

**[13:53]** approach B here is direct SQL generation. So large language model here generates the parameterized SQL query

**[13:58]** against a read only uh SQL database view scope to the user's data. So basically

**[14:03]** we're going to have a different database and we're going to have large model here to generate whatever query that it that user asked for and it's going to

**[14:10]** basically run that for that only database right so it's only beble to create query that database based on the user's data and the risk here is being

**[14:16]** high because it handles like any query shape without a mapper for the updates and also the SQL injection could be part

**[14:22]** of it right needs a readonly database view and stuff like this so you know both approach you can see has some pros

**[14:29]** and con but there's also a hybrid one where yes we use the mapper but we can also to do a SQL fallback which will

**[14:34]** give us the best of both worlds which will have a safer mapper for common queries and SQL for edge cases. So you

**[14:41]** can see it gives you some approaches here that we can choose from. And the recommendation here is choosing option A here because it's the safest path to

**[14:48]** shipping reusing the entire existing infrastructure and cover 90% of the queries your users actually asking for

**[14:54]** and only the 10% of the queries that I can't handle are better to solve than by introducing the SQL generation risk. So

**[15:00]** you can see that's really good, right? is actually kind of like similar to the boil lake principle that the framework has actually introduced. So I actually

**[15:06]** really like this approach for generation the plan because this is probably the most safest way and also give us the fastest way to launch this MVP to the

**[15:14]** users. So in this case I'm going to choose an option one here and so far you can see we have consumed 130,000 for

**[15:20]** token assumptions for the conversation so far and currently we're at phase four. So approach A is chosen and

**[15:26]** currently it's going to proceed to next step. Okay. So after all those times we have been talking with the cloud here,

**[15:33]** the doc survived two rounds of the anniversary uh anniversar uh review 15

**[15:39]** issue caught and fix and quality here is 8 out of 10. So it actually gives you a score out of this which is pretty cool

**[15:45]** and uh once we have this done so design doc for this ticket has been reviewed and refined. It covers problem

**[15:51]** statements, demand, evidence, approach and also 15 file for implementation plan, credit integrations, security

**[15:58]** model and success uh criteria. This is the output of step one in the planning pipeline. So the next steps are

**[16:05]** basically your spec team for detail spec then also the auto plan for CEO design engineer review and all those kind of

**[16:11]** roles right which is our different persona here to review the plan entirely. So in this case what would you like to do with the design doc? So I

**[16:18]** want to approve this but can I run this in a clear session due to I have consumed a lot of context here in this

**[16:24]** conversation already. If so uh what's the prompt that I can run in the nest clause session so that I can carry over

**[16:30]** for a fresh context window. So it says absolutely let me mark this as proved and save the handoff and here you can

**[16:36]** see it give you the exact command for the next session. So you can [clears throat] see I can still do that with a clear session especially for

**[16:41]** planning. Accuracy is so important. So I will highly recommend you know whenever you finish like one stage cuz currently

**[16:47]** I think we're at this stage right now for the office hour. We already complete this. So the next thing we're going to

**[16:52]** do is the spec team and the auto plan right so we want to ideally break it down right take this as like one claw

**[16:58]** session break it down save it in a handoff doc and then we're going to carry over in the next session for the next scale. Okay so you can see here

**[17:05]** it's going to write the plan here with the complete handoff for our net session. All right. So once we have the step one for the office hours done, next

**[17:11]** thing we're going to do is try to do the spec team and having AI agent here to basically create a spec for this feature

**[17:17]** that we're going to add. And notice here that the design doc here is actually saved in a root folder here for this MD

**[17:22]** file. And if you want to take a look at this, uh, basically this is what it looks like. So you can see we have our AI agent here for the expense query. So

**[17:29]** this is the ticket number and this is basically the product statement. So you can see we have the current design all

**[17:35]** in place here. So we can be able to take this MD file anywhere in a new claw session here and claw can do a still

**[17:41]** look at this as well. Right? So in this case I'm going to copy this prompt right here. Head over to a new claw code session here. You can see I'm going to

**[17:47]** trigger the spec team scale from the GStack and triggering the exact prompt.

**[17:52]** And you can see here that first it's going to trigger the spec team skill. Then it's going to start to look through the ticket and also looking through the

**[17:59]** state. So you can see that it's able to keep track of the current state as well for what current ticket is working on. And let's take a look at more here. So

**[18:06]** first question is asking is which area does do you want to discuss for the AI agents the design doc covers most

**[18:12]** decisions but these gray areas could use your input. So now this is going to be more kind of like once we have the

**[18:19]** directions down the next thing we're going to focus on is like okay how do we want to have the application to look like you know what kind of system what

**[18:25]** kind of infrastructure what kind of service we want right what kind of model we want this is going to be the place we're going to decide that so for

**[18:31]** example hey I want to you know make decision on the chat UI placement or maybe the large language model provider

**[18:38]** choice or the conversation context right and also the aggregation approach the

**[18:43]** design doc process the postgress RPC function function for the group by and sum. Alternatively, we can fetch rows

**[18:49]** and aggregate in JavaScript and the effects accuracy and also the scalability. So, I'm also going to

**[18:55]** choose that as well. And there's a couple more things like for example, what about the credits usage and what

**[19:00]** about the table view look like for the UI and is there any edge case that we need to consider. So, I also want to

**[19:05]** talk about that as well. So, that's basically my prompt. So, here I'm going to submit this and let's see what it does. Okay, cool. So, discussing all

**[19:12]** four areas plus your additional concerns. So where should the AI chat live in your dashboard? So definitely

**[19:17]** it's going to be in a dedicated page. So here we have our sidebar and there is a AI section or it could be a slide out

**[19:24]** panel. So user let's say currently on this page right now and there's going to be a side panel here where it's going to

**[19:30]** pop out and user can chat or it's going to be a floating widget here. Right? So, at the bottom here, oh, if you have

**[19:36]** questions, you can just display that. But I'm just going to choose the recommended approach for dedicated page because we're going to display uh more

**[19:43]** things on here like tables or visualizations. So, it will be nice to have it own dedicated page. So, I'm

**[19:49]** going to click on enter that for this. All right. So, the next part is the context. So, how much conversation

**[19:54]** context should the AM retain? And this will affect the prompt size, cost, and also the follow-up quality. So, here we

**[20:00]** have 5, 10, session only, and single query only. So in this case I'm going to choose five here because let's say user

**[20:06]** say hey I want to break that down by vendor then it knows exactly what it referenced to. So in this case I'm going to click on yes. Okay. So the next part

**[20:12]** we're going to take look at is aggregation. So how should we aggregate the data? Is it using the postgress RPC or it's going to be a JavaScript

**[20:18]** aggregation. Now both has different benefits. So RPC is going to live to query inside of our database. So when we

**[20:24]** query things it's just going to be calling that RPC function in our database to query data. And the other

**[20:29]** part we can do this is using the JavaScript aggregation. But I'm just going to say something on top of this. I'm going to say instead of using the

**[20:35]** JavaScript aggregation, I kind of want to use the subway OM, right? The object relation mapper here because let's say

**[20:42]** in the future we're going to switch to different database, right? So, you know, in this case, we can be able to have this function defined inside of our

**[20:48]** server actions or in our database in our backend logic and we can be able to trigger that function and let's say

**[20:54]** we're going to switch to different database, but the RM here, the OM logic here is still going to be the same. So,

**[20:59]** can this logic here be live in our back end here? so that we can be able to make it much more scalable and reusable in

**[21:04]** the future. Let's say we're going to switch to different database and this way it's also going to be less uh data

**[21:10]** migration because this is just only the functions for the queries that list inside of our back end. So that's

**[21:15]** basically what I want to achieve here and that's basically what I want to add

**[21:20]** onto this uh feature change and click on enter here. Okay. So once we have the aggregation logic in the backend service

**[21:27]** layer using subbase clients so the ORM style not the raw SQL RPCs portable if

**[21:33]** you want to switch database now let's cover your additional concerns so here you can see we have some additional

**[21:38]** questions for example the credits and also the table UI so how should the result table look in the chat and this

**[21:44]** affects both the AI response so if I were to zoom out a bit more so here you can see this is what the table look like

**[21:49]** so inline markdown for the table uh we have a style cascade for the table And

**[21:54]** also we have the card base. So um I would say is this so markdown is fine

**[22:00]** but we should definitely limit down how many records we should return right let's say you know user didn't specify

**[22:07]** or there should be a way that we can be able to hide or be able to expand or collapse right and be able to have the

**[22:13]** functionality here where user can be able to you know see it more clearly and also look through the chats right let's

**[22:19]** say user is going to refresh or come back to this chat um all the table here should be collapsed right or if there is

**[22:25]** a chat that's very long then we should definitely collapse this by default and and also reduce the load on how much

**[22:32]** data we're going to query right so let's say if user didn't specify that then we definitely want to uh mention that and

**[22:38]** then the other part is that we want to keep it minimal let's say user is going to uh fetch like a lot of records then

**[22:44]** we should definitely maybe send like some suggested uh some clarifications right before we're going to actually

**[22:50]** send something right so the chat here should also do some clarification here before it's going to um send out to the

**[22:56]** database here to fetch the right data and that's basically my answer. So I'm going to choose the inline for the

**[23:02]** markdown table and submit for the answer here. Okay. So finally you can see there's some additional questions like

**[23:08]** what are other dashboard page should be affected by the AI chat feature. So for example the sidebar right? So that's

**[23:14]** going to be adding the AI assistant here the dashboard home view. So try the AI assistant, the call to action card, and

**[23:21]** also for the receipts and transaction page, we're going to add like, hey, you can ask AI about this. But I'm just

**[23:26]** going to keep the scope here small. I'm not going to choose that for now. And the other part we're going to add here is our landing page. Making sure our

**[23:31]** landing page or blog page or any other parts. We're going to, you know, make sure that we add this. And the other

**[23:37]** part is the marketing. So we need to definitely add this feature as a shout out for the email list that we have

**[23:44]** inside of our system, right? making sure that we let user know that hey we have this feature in place doesn't matter

**[23:49]** they're paid or unpaid uh which tier they are in right so we need to let them know as well um they will get so we

**[23:55]** definitely need to use or trigger some marketing skills and try to see how we should be able to um email this instead

**[24:01]** of our email here and in terms of the edge case so for edge case here which scenario concerns you most for the spect

**[24:07]** address so empty data states so user with zero receives or transaction AI

**[24:13]** should guide them to import data first not return the empty results, right? That's the most important part. And the ambition query, so how much did I spend?

**[24:20]** So no time range, no categories. AI should ask for clarification. That's definitely true. And the other part is

**[24:27]** the cross currency. So uh for example, like maybe user has CD or USD receipts.

**[24:33]** Total spending needs to handle the mixed currency. Yes, we do have those currencies in place in our table. So it

**[24:38]** should be able to do that. And the rate limiting, so user spamming queries. So we should definitely have something like

**[24:44]** that as well. So in this case I'm just going to submit that as well and that's going to be our edge case here. So I'm

**[24:49]** going to submit this. And finally we have some additional question being asked. So cross currency uh queries. So

**[24:55]** CAD USD receives how should AI handle the mix uh currencies. So separate

**[25:01]** totals uh convert to the base currency. Yes, let's do the separate total is

**[25:06]** probably the best way to do it. All right. Perfect. So all areas are covered. ready to spin up different parallel research agent here to do the

**[25:13]** research. So launch the backend architect front designer and the QA strategist product manager here and the

**[25:19]** devil advocate agents in parallel here to do the research. So this is new this is really cool and I'm going to say yes

**[25:26]** let's start to do the research and I'm just going to let it do its thing at the background. So now you can see we have

**[25:32]** five different agents here has spun up and this is they're all doing research here with different angles backend front

**[25:37]** end QA product requirements and a devil advocates and here are their focus and right here you can see if you want to

**[25:43]** see this five agents we can click on this and these are currently the agents that are running right now. Okay. So, uh

**[25:49]** if you want to click on to view, click on enter here. If you don't want to view, uh you can just click on escape here to close. And I'm just going to

**[25:56]** wait for a bit until all the agents jobs are done. And we're just going to come back once everything's finished. Before

**[26:01]** we jump into the next part, I want to quickly show you something I've been using while building some of my projects. So, if you've ever used AI to

**[26:08]** generate code, you've probably noticed it works, but it also breaks in ways you don't always catch right away. That's

**[26:15]** basically where Test Sprite comes in. It's an AI testing agent that goes through your app, figures out what it's

**[26:20]** supposed to do, and then checks if everything actually works the way it should. Now, what's changed recently is

**[26:26]** how it fits into your workflow. So, I'm inside Cursor here, and through their MCP integration, it's not something I

**[26:32]** run separately. I can generate code, test it, fix things, and rerun everything right here in the IDE, which

**[26:38]** makes it feel way more natural when you're iterating. Where it gets really useful is when you start changing stuff.

**[26:44]** So, let's say I update part of the logic. instead of just running the same test again, it actually rechecks the

**[26:49]** flow and catches new issues that come from those changes. That's a big deal because most setups don't really handle

**[26:55]** that well once you start iterating. And if a test isn't quite right, you can actually edit it visually instead of

**[27:01]** digging through a bunch of test code. So, I can click into a step, adjust what it's checking, or regenerate part of the

**[27:07]** flow and keep everything else intact, which makes it a lot easier to control what's actually being tested. On top of

**[27:12]** that, they also added GitHub integration. So, whenever you push changes, it runs tests on your pull

**[27:18]** request and shows you exactly what passed or failed before you merge anything. It basically acts like a

**[27:23]** safety check so you don't accidentally ship something broken. Also, quick mention, they're running a hackathon right now with a $3,000 prize pool. So,

**[27:30]** if you're building anything or just experimenting with AI projects, it's actually a pretty fun way to try this

**[27:35]** out. I'll leave a link in the description if you want to check it out. Okay, now let's get back into the video.

**[27:40]** Okay, so it looks like everything's finished now and here you can see we have the entire spec are all covered and

**[27:46]** this is what the decisions been made and here is the complete spec. So once we have the spec, the next thing we're

**[27:52]** going to do is try to create using the auto plan here using different personality like CEO design review

**[27:59]** engineer review and the DX review here sequentially with the auto decisions using the auto plan feature to run a

**[28:06]** full review for the pipeline. So in this case, I'm going to use the auto plan scale here and basically point it out to the spec where the spec live inside of

**[28:13]** our backlog MD file and I'm just going to click on enter. All right. So finally you can see we have different sub agents

**[28:19]** here. For each sub aent that's going to be one persona. So we have the CEO persona here has run and here is their

**[28:24]** output. And we also have the the design sub agent here has run and review the spec. And here is his output. And then

**[28:31]** we also have the engineering design sub agent here to review. And here is its output as well. So eventually here you

**[28:37]** can see we have everything are all verified and once everything is all confirmed and modified our spec. So you

**[28:43]** can see total there are 41 findings 10 from CEO 15 from design and 16 from the

**[28:49]** engineering right to after has done the review for the spec and this is the three review phases that we have follow

**[28:55]** sequentially from CEO design engineering and each of them has its own sub agents and 22 decision has made and there's

**[29:02]** also some couple user decisions that we have flagged it along the way and I have already made the decision and you can

**[29:07]** see that this is the entire summary. Now the last part that I want to talk about is the token consumption. So these are

**[29:12]** the skills that we have went over for GStack. So for token consumption you can see here for the office hour we have

**[29:18]** consumed 170 for the spec team 200k and also the auto plan here also consume

**[29:24]** 200k,000 for tokens because we using different sub aents here. So in total here you can see we takes about 600k for

**[29:32]** token sumptions for the entire planning pipeline. That's how much it took for planning a feature on top a brownfield

**[29:38]** project. So at this point here, we can either use the build pipeline from GStack here to execute or the other way

**[29:44]** we can do here is basically try to use like GSD or super power here and try to execute this entire spec step by step.

**[29:50]** And of course, if you want to learn more about GSD and super powers, make sure to check out this video right here. I recently done a comparison between the

**[29:56]** two and in that video we give a brownfield project like this and basically adding a feature to add the

**[30:02]** end to end test coverage and have two framework here like super power and GSD here to both work on that same feature

**[30:08]** using git workshries and by the end of that video I went over the comparison between the two like which framework is

**[30:14]** better for executing the accuracy and the token assumption. So if you are learning more about like okay which

**[30:20]** framework for spectral element is the highest accuracy and has the low token lowest token consumption then make sure

**[30:26]** you check out that video. In that video we went over that. So pretty much that's it for this video. In this video we went over the office hours the spec team

**[30:32]** scale and also the auto plan from the GStack spectrum development framework. So pretty much that's what we covered in this video. So with that being said if

**[30:38]** you do thumb this video please make sure to like this video consider subscribe more content like this. But with that being said I'll see you in the next

**[30:45]** video.

**[0:00]** Why cominator CEO Gary Tain's claw code toolkit GStack has many specialized workflows but the one most people are

**[0:06]** sleeping on is the planning workflow. It challenged my assumptions narrow down what really matters research the

**[0:11]** competitive landscape and have [clears throat] five different AI agent here reviewing my spec from CEO design

**[0:17]** engineering QA and devil advocate perspective all before writing a single

**[0:22]** line of code. So, in this video, I'm going to show you my entire planning pipeline on building a feature on a real

**[0:28]** SAS project with paying customers. So, with that being said, if that sounds interesting, let's get into this. Now,

**[0:33]** before we continue, I recently launched our school community where I help you to master AI agents, automations, and so

**[0:39]** much more. And that's all coming from someone who used to work as a senior AI software engineer at companies like

**[0:44]** Amazon and Microsoft. And in this community, you're going to get over 100 plus video materials like templates and

**[0:50]** workflows that I personally built and sold over 100 plus times. On top of that, you're also going to get access to

**[0:56]** our weekly live calls. And just to give you an idea, this week we're actually running a claw code master class where

**[1:01]** we're going to dive into how to improve Claw Co's accuracy when we're going to use it to building applications. Plus,

**[1:06]** you're also going to get full community support where you're going to get a chance to ask questions and get direct answers back. So, if you're ready to

**[1:12]** level up, make sure you jump right in and I'll see you in a community. All right. All right. So, to get started, first we're going to install this onto

**[1:17]** our local machine. So, to do so, right here, you can see this is the exact step we're going to follow to basically just copy this, open your code claw code, and

**[1:23]** just paste it and have it to install this completely onto our project. Or the other way you can do this is you're simply just going to copy that

**[1:29]** repository, paste it, and tell claw to follow the repository and try to install this and set this up. So, once you have

**[1:35]** this all set up, the next thing we're going to take a look at is how we can beble to use it into our existing project. So, right here, you can see

**[1:41]** this is my existing project called Book Zero. And right now if I were to log into the application, here is what it

**[1:46]** looks like. So I wanted to build a feature onto this existing brownfield projects. Basically by adding a AI chat

**[1:52]** agent here to query the expense based on the project data. For example, how much did I spend on gas in quarter 1 or show

**[1:59]** me the top five vendor this month or find all the receipts over $100. Right? So these are all some queries that we

**[2:06]** can be able to pass this chat agent here that can convert into a SQL query that can query the data in our database. Now

**[2:12]** obviously this feature is not really 100% defined. I think that the requirement here still needs to be refined a bit more with different

**[2:18]** personalities and that's where the Gstack comes in which can help us to refine govern this plan making sure that

**[2:24]** the plan here is fully ready before we pass it to execution. So in this case I'm just going to copy this link for

**[2:29]** Jira ticket and I already have my J MCP set up on my local machine. So in this case, I'm just going to head over to claw code really quick. And I basically

**[2:36]** mention that, hey, I already have this installed. And let's say if I want to bring this feature onto this project, what are some skills that I can use to

**[2:43]** build this project using GStack? And right here, you can see it uses GStack skill to give me a workflow on exactly

**[2:48]** how we're going to build this feature onto it. Now, obviously, we're not going to use it to build the building pipeline

**[2:53]** because it doesn't really have the test-driven elements like what Superpower does. So, I'm going to use it to do the PL pipeline because I think

**[3:00]** this is what GStack really shines. So in this case, I'm going to open a brand new terminal session and start a clock code.

**[3:06]** I'm just going to copy this diagram right here, pass it to a new clock session. And basically, this is what I'm going to say. I want you to follow this

**[3:12]** entire planning pipeline and try to do this for this entire ticket. Can you help me to do this, please? So, I'm

**[3:19]** going to paste this as my prompt and switch it over to planning mode. And right away, you can see that it starts to gather the context on exactly what

**[3:25]** this ticket is and how we can be able to build this. So first it's going to launch different sub aents here try to

**[3:30]** understand the AI chat codebase right also data models and services that we have then it's going to ask me some serious question to configure our GSTA

**[3:37]** stack framework like can we be able to copy other projects coding patterns or what is the goal right now is it a

**[3:42]** startup is it a hackathon projects or having fun and for this project right now is it in the ideation phase is it in

**[3:49]** the paying customer phase or doesn't have any paying customers right now right and then now once we have this all

**[3:54]** set so the changes everything you have real signal to work from since you already have the revenue. So the

**[4:01]** question that matters are about the wedge, the observation, the future fit and let me start. So the backlog spec

**[4:07]** describe three phases basic queries uh comparison trends and proactive insights. That's a lot of surface area.

**[4:14]** What is the smallest possible version of this AI chat that a paying customer will actually use this week? Not after you

**[4:20]** built all three phases. So for example, maybe the spending summaries or the receipt finder, the tax prep helper,

**[4:27]** right? Right? So all those kind of things. So in this case, this is what I'm going to say. So based on the research that we have done, the customers are looking to add the

**[4:33]** spending summaries in our AI chat a lot often, right? So they want to see the spending predictions, the patterns they

**[4:41]** see for the spendings. They want to learn from this using our AI chats. And most importantly, we want to have data

**[4:47]** visualizations to display charts, tables, or all kinds of data visualizations for the queries that

**[4:52]** they're querying for. And most importantly, they should be able to have the ability to save the conversation and also save the stats or the visualization

**[5:00]** and maybe add that into our data the dashboard and they can be able to review that in the later times. Most

**[5:06]** importantly, we need to have it to integrate it into our credit system so that they can be able to see the credit

**[5:12]** goes down when they have a conversation, right? So, how much we should charge per credit for per conversation or per chat?

**[5:17]** We need to define that as well. So there's a lot of things in place and I want you to package all together into this plan here. And basically you can

**[5:24]** see that's my prompt. Now this is there's a lot of things in the prompts. You can see it says I respect the ambition. I need to push back. You

**[5:30]** describe five features like spend analysis, chart visualizations, save queries, dashboard customizations, and

**[5:36]** credit based monetizations. This is not a wish. It's actually a platform. So we need to push back a bit more and we need

**[5:41]** to try to understand exactly what can users use right now this week after we have the MVP done. So here you can see

**[5:47]** pick one things that generate the word of mouth. Everything else can come in phase two. So how much did I spend on

**[5:53]** this category this quarter, right? What are my top expense for this month or

**[5:59]** show me the unusual spending this month or something like that, right? So you can see that it start to breaking this

**[6:04]** large prompts or large demand or large request into a step-by-step process that

**[6:09]** we can build the first MVP first. Then we're going to you know push back and adding those additional functionalities

**[6:15]** into phase 2 if we have time right so you can see these are the things that we have so in this case I'm just going to

**[6:20]** say hey uh all of them looks good right so show me the unusual spendings or um

**[6:26]** basically try to learn more about the spending that they made that's good and I think this is probably the feature we

**[6:31]** need to add right so all those queries should be in place yes we can you know forget about the charts but we

**[6:37]** definitely need to add the tables right be able to have user here to visualize things much more easier rather than just

**[6:43]** bunch of text. And furthermore, we also definitely need to support those queries to be able to fetch in our database and

**[6:48]** be able to have user here to understand their spending patterns. So that's basically my prompt and I'm just going

**[6:54]** to say yes and let's have it to basically plan this bit more and dive deep into how we're going to achieve

**[6:59]** this. Then it's asking me another PM kind of questions like have you sat down and watched how they use this platform

**[7:05]** without helping them? Did they struggle somewhere that you thought was obvious or did you ignore a feature you might

**[7:11]** you might thought uh was important. So this is kind of like a PM question and of course you cannot have this without

**[7:17]** like data or like user tracking all kind of things. So I actually made a video on the claw skills for marketings. In that

**[7:23]** video I demonstrate how you can be able to set up the entire tracking system like the usage you know have user fully

**[7:28]** on boarded like what have they done after they on boarded the entire user tracking here. I actually had made a video on this. So if you want to learn

**[7:35]** really more about how you can do this set of the tracking, make sure to check out that video right there. And I do have real usage for this specific

**[7:41]** surprise that I want to share. Yeah. So I want to say yes to this. And here you can see it says you have watched user that's good. Most founder at your stage

**[7:47]** here doesn't have that. So what surprise you and what the users do with book zero that didn't you expect. And this matters

**[7:54]** because AI chat features come from things user are already trying to do and just making it instant instead of the

**[8:00]** manual process. So one of the option that they give me is they export data to understand patterns and that is actually

**[8:05]** something that I found too not just from the AI but actually I found it as well that users actually turning to CSV here

**[8:11]** to analyze data rather than just doing it in our platform because in our dashboard there's only five charts and that's static for all users. Then we

**[8:17]** also have some other options like they ask question that I haven't anticipated or they struggle with the filter search

**[8:23]** from the UI. So all three options are pretty valid. So I'm just going to say based on these things that we have here first two is probably the most

**[8:29]** surprising that [clears throat] I want to resolve using this feature and that's basically what I wanted to add and I'm

**[8:35]** just going to say yes. So in this case I'm just going to enter this and let claw here to figure this out. Okay. So eventually here you can see this is what

**[8:40]** it responds. So this is a real signal user are exporting CSV to answer the questions that our platform should have

**[8:46]** this natively. So this is the what the future fit look like. So it actually look through the past this and look

**[8:51]** through the future here to see if it's actually meaningful in 3 years. So if AI gets cheaper, everyone has their own

**[8:57]** tools and the bookkeeping tools here in multiplies. Does this feature in our AI chat become more central or less? And

**[9:04]** honestly, I think this is kind of like a bonus feature from this framework to help you to look to the future to see if this feature is not replicatable or is

**[9:11]** unique compared to other competitors. So let's say every competitor now eventually add this feature like ask AI

**[9:16]** about your expense. What's your thesis about why your platform your your versions win? Right? Is it because of

**[9:23]** data that you have or is it because the domain knowledge or is it could be something else right like if you were to

**[9:28]** add this feature and other people are adding this feature you know what are some uniqueness what are some selling points what makes our platform our

**[9:35]** feature here from this platform different compared to others right so you can see it gives me some list of options here so in this case I'm going

**[9:41]** to take some time and try to answer this question and we're just going to proceed forward okay so after we have that answer submitted here you can see it

**[9:47]** basically is going to start to do some research and basically try to figure out what's the landscape for this feature that we're trying ad. Okay. So then it

**[9:54]** has done some research on the landscape for the AI conversational expense management and the conversational bookkeeping AI assistant for common

**[10:00]** mistakes in 2025 and 2026. So here is what it found. So layer one we have AI

**[10:05]** chatbot for small businesses are mainstream. Yes, that's good. And AI space is crowded with tools that try to

**[10:11]** do bookkeeping for like auto categorizations or auto reconciliations or auto filing but hallucination here

**[10:17]** and miscatategorization are the number one concerns across industry. So that's what it found for the concern and layer

**[10:22]** two here is that the shifting from child bots to agentic AI tools that take actions not just like answering

**[10:28]** questions is number one thing and the AI hallucination and bookkeeping is real. So hallucination here is a big problem

**[10:34]** and layer three here is about what's interesting our on our position here. So our AI here doesn't do bookkeeping. Our

**[10:39]** AI here only query data that are exist and most AI competitor here tries to generate accounting entries and that's

**[10:45]** where hallucination kills you. your AI answer questions about verified human review scripts or receives transaction

**[10:51]** data. So the accuracy here is higher because we're only querying structure data not generating any financial

**[10:56]** records which is what separates that apart. So you can see that that's the basically the difference right the clear

**[11:02]** difference here is that our AI doesn't hallucination your finance it reads what's actually there and that's it once

**[11:07]** we have our research done the next thing I'm going to do here is phase three for challenging our premise so here is the

**[11:12]** premise so here are the premise that I'm working from I need you to agree or disagree with the each so user want a

**[11:19]** natural language uh queries because they actually currently export CSV to answer the questions that the UI doesn't cover

**[11:25]** and the MVP here is spending analysis and unusual spending detections tables, no charts, no save queries or

**[11:32]** dashboard customizations and the credit based pricing promization is monetization model. AI query existing

**[11:38]** data only. This is the accuracy advantage plus the anomaly detection charts save queries proactive insights

**[11:43]** are in phase two and response time should be less than 5 seconds is the targets. So do we agree with all six? So

**[11:49]** you can see that it's actually able to break it and try to refine the plan here step by step on exactly what's the

**[11:55]** requirements which is a really structured way to do it. So here I'm just going to say yes I do agree with all six but one thing that I want to add

**[12:01]** here is or in this case confirm you mentioned about the credit based pricing per conversation is the monetization

**[12:07]** model. So I just want to confirm that we are going to add this in our monetization right in our current system

**[12:12]** for the credit. So can you also do a research to see how much should we price for the monetization and what's the

**[12:18]** model should we using uh underneath it is using you know AI here to generate a SQL query to run in our database. what

**[12:24]** are some of the tools that we're going to be calling right so that we can calculate the pricing for monetization. I'm not sure if we're going to do this

**[12:29]** later on in our steps here, but I just wanted to put it out there um before we're going to release this feature. So

**[12:35]** that's basically what I'm going to say. So the next section we're going to take a look at is phase 3.5 for the cross

**[12:40]** model second opinion. And this is basically going to have a second opinion from an individual or independent AI

**[12:46]** perspective. It will basically review the problem statements, the key answers, premise, landscape from this entire

**[12:52]** session without having seen this entire conversation, which will give us a second opinion on this for the future

**[12:57]** we're trying to build. So in this case, I'm going to say yes. Let's get a second opinion here to have a different sub agent here review this and try to see if

**[13:03]** there's anything that maybe we didn't think of. Right? So in this case, I'm going to say yes. Let's do that for the second opinion here. All right. So now

**[13:10]** you can see we have the second opinion from another sub agents and basically has review what the application does and

**[13:16]** also the answers we have here as well as everything that we have asked to review. So then after that it basically goes to

**[13:22]** the phase four for the alternative generation. So approach one is structure query mapper. So large language model

**[13:28]** here converts your natural language into a structure JSON intent maps to existing you know query that we have already

**[13:34]** built. So it doesn't generate a new query. It will basically use the existing query that we have and just map to that query. And here is the effort.

**[13:40]** So you can see it's going to be really low because we have the query defined. It's going to reuse the existing queries that we have. So that means that we have

**[13:47]** zero SQL injections for that which is really good. And that's basically the approach A which I really like. And the

**[13:53]** approach B here is direct SQL generation. So large language model here generates the parameterized SQL query

**[13:58]** against a read only uh SQL database view scope to the user's data. So basically

**[14:03]** we're going to have a different database and we're going to have large model here to generate whatever query that it that user asked for and it's going to

**[14:10]** basically run that for that only database right so it's only beble to create query that database based on the user's data and the risk here is being

**[14:16]** high because it handles like any query shape without a mapper for the updates and also the SQL injection could be part

**[14:22]** of it right needs a readonly database view and stuff like this so you know both approach you can see has some pros

**[14:29]** and con but there's also a hybrid one where yes we use the mapper but we can also to do a SQL fallback which will

**[14:34]** give us the best of both worlds which will have a safer mapper for common queries and SQL for edge cases. So you

**[14:41]** can see it gives you some approaches here that we can choose from. And the recommendation here is choosing option A here because it's the safest path to

**[14:48]** shipping reusing the entire existing infrastructure and cover 90% of the queries your users actually asking for

**[14:54]** and only the 10% of the queries that I can't handle are better to solve than by introducing the SQL generation risk. So

**[15:00]** you can see that's really good, right? is actually kind of like similar to the boil lake principle that the framework has actually introduced. So I actually

**[15:06]** really like this approach for generation the plan because this is probably the most safest way and also give us the fastest way to launch this MVP to the

**[15:14]** users. So in this case I'm going to choose an option one here and so far you can see we have consumed 130,000 for

**[15:20]** token assumptions for the conversation so far and currently we're at phase four. So approach A is chosen and

**[15:26]** currently it's going to proceed to next step. Okay. So after all those times we have been talking with the cloud here,

**[15:33]** the doc survived two rounds of the anniversary uh anniversar uh review 15

**[15:39]** issue caught and fix and quality here is 8 out of 10. So it actually gives you a score out of this which is pretty cool

**[15:45]** and uh once we have this done so design doc for this ticket has been reviewed and refined. It covers problem

**[15:51]** statements, demand, evidence, approach and also 15 file for implementation plan, credit integrations, security

**[15:58]** model and success uh criteria. This is the output of step one in the planning pipeline. So the next steps are

**[16:05]** basically your spec team for detail spec then also the auto plan for CEO design engineer review and all those kind of

**[16:11]** roles right which is our different persona here to review the plan entirely. So in this case what would you like to do with the design doc? So I

**[16:18]** want to approve this but can I run this in a clear session due to I have consumed a lot of context here in this

**[16:24]** conversation already. If so uh what's the prompt that I can run in the nest clause session so that I can carry over

**[16:30]** for a fresh context window. So it says absolutely let me mark this as proved and save the handoff and here you can

**[16:36]** see it give you the exact command for the next session. So you can [clears throat] see I can still do that with a clear session especially for

**[16:41]** planning. Accuracy is so important. So I will highly recommend you know whenever you finish like one stage cuz currently

**[16:47]** I think we're at this stage right now for the office hour. We already complete this. So the next thing we're going to

**[16:52]** do is the spec team and the auto plan right so we want to ideally break it down right take this as like one claw

**[16:58]** session break it down save it in a handoff doc and then we're going to carry over in the next session for the next scale. Okay so you can see here

**[17:05]** it's going to write the plan here with the complete handoff for our net session. All right. So once we have the step one for the office hours done, next

**[17:11]** thing we're going to do is try to do the spec team and having AI agent here to basically create a spec for this feature

**[17:17]** that we're going to add. And notice here that the design doc here is actually saved in a root folder here for this MD

**[17:22]** file. And if you want to take a look at this, uh, basically this is what it looks like. So you can see we have our AI agent here for the expense query. So

**[17:29]** this is the ticket number and this is basically the product statement. So you can see we have the current design all

**[17:35]** in place here. So we can be able to take this MD file anywhere in a new claw session here and claw can do a still

**[17:41]** look at this as well. Right? So in this case I'm going to copy this prompt right here. Head over to a new claw code session here. You can see I'm going to

**[17:47]** trigger the spec team scale from the GStack and triggering the exact prompt.

**[17:52]** And you can see here that first it's going to trigger the spec team skill. Then it's going to start to look through the ticket and also looking through the

**[17:59]** state. So you can see that it's able to keep track of the current state as well for what current ticket is working on. And let's take a look at more here. So

**[18:06]** first question is asking is which area does do you want to discuss for the AI agents the design doc covers most

**[18:12]** decisions but these gray areas could use your input. So now this is going to be more kind of like once we have the

**[18:19]** directions down the next thing we're going to focus on is like okay how do we want to have the application to look like you know what kind of system what

**[18:25]** kind of infrastructure what kind of service we want right what kind of model we want this is going to be the place we're going to decide that so for

**[18:31]** example hey I want to you know make decision on the chat UI placement or maybe the large language model provider

**[18:38]** choice or the conversation context right and also the aggregation approach the

**[18:43]** design doc process the postgress RPC function function for the group by and sum. Alternatively, we can fetch rows

**[18:49]** and aggregate in JavaScript and the effects accuracy and also the scalability. So, I'm also going to

**[18:55]** choose that as well. And there's a couple more things like for example, what about the credits usage and what

**[19:00]** about the table view look like for the UI and is there any edge case that we need to consider. So, I also want to

**[19:05]** talk about that as well. So, that's basically my prompt. So, here I'm going to submit this and let's see what it does. Okay, cool. So, discussing all

**[19:12]** four areas plus your additional concerns. So where should the AI chat live in your dashboard? So definitely

**[19:17]** it's going to be in a dedicated page. So here we have our sidebar and there is a AI section or it could be a slide out

**[19:24]** panel. So user let's say currently on this page right now and there's going to be a side panel here where it's going to

**[19:30]** pop out and user can chat or it's going to be a floating widget here. Right? So, at the bottom here, oh, if you have

**[19:36]** questions, you can just display that. But I'm just going to choose the recommended approach for dedicated page because we're going to display uh more

**[19:43]** things on here like tables or visualizations. So, it will be nice to have it own dedicated page. So, I'm

**[19:49]** going to click on enter that for this. All right. So, the next part is the context. So, how much conversation

**[19:54]** context should the AM retain? And this will affect the prompt size, cost, and also the follow-up quality. So, here we

**[20:00]** have 5, 10, session only, and single query only. So in this case I'm going to choose five here because let's say user

**[20:06]** say hey I want to break that down by vendor then it knows exactly what it referenced to. So in this case I'm going to click on yes. Okay. So the next part

**[20:12]** we're going to take look at is aggregation. So how should we aggregate the data? Is it using the postgress RPC or it's going to be a JavaScript

**[20:18]** aggregation. Now both has different benefits. So RPC is going to live to query inside of our database. So when we

**[20:24]** query things it's just going to be calling that RPC function in our database to query data. And the other

**[20:29]** part we can do this is using the JavaScript aggregation. But I'm just going to say something on top of this. I'm going to say instead of using the

**[20:35]** JavaScript aggregation, I kind of want to use the subway OM, right? The object relation mapper here because let's say

**[20:42]** in the future we're going to switch to different database, right? So, you know, in this case, we can be able to have this function defined inside of our

**[20:48]** server actions or in our database in our backend logic and we can be able to trigger that function and let's say

**[20:54]** we're going to switch to different database, but the RM here, the OM logic here is still going to be the same. So,

**[20:59]** can this logic here be live in our back end here? so that we can be able to make it much more scalable and reusable in

**[21:04]** the future. Let's say we're going to switch to different database and this way it's also going to be less uh data

**[21:10]** migration because this is just only the functions for the queries that list inside of our back end. So that's

**[21:15]** basically what I want to achieve here and that's basically what I want to add

**[21:20]** onto this uh feature change and click on enter here. Okay. So once we have the aggregation logic in the backend service

**[21:27]** layer using subbase clients so the ORM style not the raw SQL RPCs portable if

**[21:33]** you want to switch database now let's cover your additional concerns so here you can see we have some additional

**[21:38]** questions for example the credits and also the table UI so how should the result table look in the chat and this

**[21:44]** affects both the AI response so if I were to zoom out a bit more so here you can see this is what the table look like

**[21:49]** so inline markdown for the table uh we have a style cascade for the table And

**[21:54]** also we have the card base. So um I would say is this so markdown is fine

**[22:00]** but we should definitely limit down how many records we should return right let's say you know user didn't specify

**[22:07]** or there should be a way that we can be able to hide or be able to expand or collapse right and be able to have the

**[22:13]** functionality here where user can be able to you know see it more clearly and also look through the chats right let's

**[22:19]** say user is going to refresh or come back to this chat um all the table here should be collapsed right or if there is

**[22:25]** a chat that's very long then we should definitely collapse this by default and and also reduce the load on how much

**[22:32]** data we're going to query right so let's say if user didn't specify that then we definitely want to uh mention that and

**[22:38]** then the other part is that we want to keep it minimal let's say user is going to uh fetch like a lot of records then

**[22:44]** we should definitely maybe send like some suggested uh some clarifications right before we're going to actually

**[22:50]** send something right so the chat here should also do some clarification here before it's going to um send out to the

**[22:56]** database here to fetch the right data and that's basically my answer. So I'm going to choose the inline for the

**[23:02]** markdown table and submit for the answer here. Okay. So finally you can see there's some additional questions like

**[23:08]** what are other dashboard page should be affected by the AI chat feature. So for example the sidebar right? So that's

**[23:14]** going to be adding the AI assistant here the dashboard home view. So try the AI assistant, the call to action card, and

**[23:21]** also for the receipts and transaction page, we're going to add like, hey, you can ask AI about this. But I'm just

**[23:26]** going to keep the scope here small. I'm not going to choose that for now. And the other part we're going to add here is our landing page. Making sure our

**[23:31]** landing page or blog page or any other parts. We're going to, you know, make sure that we add this. And the other

**[23:37]** part is the marketing. So we need to definitely add this feature as a shout out for the email list that we have

**[23:44]** inside of our system, right? making sure that we let user know that hey we have this feature in place doesn't matter

**[23:49]** they're paid or unpaid uh which tier they are in right so we need to let them know as well um they will get so we

**[23:55]** definitely need to use or trigger some marketing skills and try to see how we should be able to um email this instead

**[24:01]** of our email here and in terms of the edge case so for edge case here which scenario concerns you most for the spect

**[24:07]** address so empty data states so user with zero receives or transaction AI

**[24:13]** should guide them to import data first not return the empty results, right? That's the most important part. And the ambition query, so how much did I spend?

**[24:20]** So no time range, no categories. AI should ask for clarification. That's definitely true. And the other part is

**[24:27]** the cross currency. So uh for example, like maybe user has CD or USD receipts.

**[24:33]** Total spending needs to handle the mixed currency. Yes, we do have those currencies in place in our table. So it

**[24:38]** should be able to do that. And the rate limiting, so user spamming queries. So we should definitely have something like

**[24:44]** that as well. So in this case I'm just going to submit that as well and that's going to be our edge case here. So I'm

**[24:49]** going to submit this. And finally we have some additional question being asked. So cross currency uh queries. So

**[24:55]** CAD USD receives how should AI handle the mix uh currencies. So separate

**[25:01]** totals uh convert to the base currency. Yes, let's do the separate total is

**[25:06]** probably the best way to do it. All right. Perfect. So all areas are covered. ready to spin up different parallel research agent here to do the

**[25:13]** research. So launch the backend architect front designer and the QA strategist product manager here and the

**[25:19]** devil advocate agents in parallel here to do the research. So this is new this is really cool and I'm going to say yes

**[25:26]** let's start to do the research and I'm just going to let it do its thing at the background. So now you can see we have

**[25:32]** five different agents here has spun up and this is they're all doing research here with different angles backend front

**[25:37]** end QA product requirements and a devil advocates and here are their focus and right here you can see if you want to

**[25:43]** see this five agents we can click on this and these are currently the agents that are running right now. Okay. So, uh

**[25:49]** if you want to click on to view, click on enter here. If you don't want to view, uh you can just click on escape here to close. And I'm just going to

**[25:56]** wait for a bit until all the agents jobs are done. And we're just going to come back once everything's finished. Before

**[26:01]** we jump into the next part, I want to quickly show you something I've been using while building some of my projects. So, if you've ever used AI to

**[26:08]** generate code, you've probably noticed it works, but it also breaks in ways you don't always catch right away. That's

**[26:15]** basically where Test Sprite comes in. It's an AI testing agent that goes through your app, figures out what it's

**[26:20]** supposed to do, and then checks if everything actually works the way it should. Now, what's changed recently is

**[26:26]** how it fits into your workflow. So, I'm inside Cursor here, and through their MCP integration, it's not something I

**[26:32]** run separately. I can generate code, test it, fix things, and rerun everything right here in the IDE, which

**[26:38]** makes it feel way more natural when you're iterating. Where it gets really useful is when you start changing stuff.

**[26:44]** So, let's say I update part of the logic. instead of just running the same test again, it actually rechecks the

**[26:49]** flow and catches new issues that come from those changes. That's a big deal because most setups don't really handle

**[26:55]** that well once you start iterating. And if a test isn't quite right, you can actually edit it visually instead of

**[27:01]** digging through a bunch of test code. So, I can click into a step, adjust what it's checking, or regenerate part of the

**[27:07]** flow and keep everything else intact, which makes it a lot easier to control what's actually being tested. On top of

**[27:12]** that, they also added GitHub integration. So, whenever you push changes, it runs tests on your pull

**[27:18]** request and shows you exactly what passed or failed before you merge anything. It basically acts like a

**[27:23]** safety check so you don't accidentally ship something broken. Also, quick mention, they're running a hackathon right now with a $3,000 prize pool. So,

**[27:30]** if you're building anything or just experimenting with AI projects, it's actually a pretty fun way to try this

**[27:35]** out. I'll leave a link in the description if you want to check it out. Okay, now let's get back into the video.

**[27:40]** Okay, so it looks like everything's finished now and here you can see we have the entire spec are all covered and

**[27:46]** this is what the decisions been made and here is the complete spec. So once we have the spec, the next thing we're

**[27:52]** going to do is try to create using the auto plan here using different personality like CEO design review

**[27:59]** engineer review and the DX review here sequentially with the auto decisions using the auto plan feature to run a

**[28:06]** full review for the pipeline. So in this case, I'm going to use the auto plan scale here and basically point it out to the spec where the spec live inside of

**[28:13]** our backlog MD file and I'm just going to click on enter. All right. So finally you can see we have different sub agents

**[28:19]** here. For each sub aent that's going to be one persona. So we have the CEO persona here has run and here is their

**[28:24]** output. And we also have the the design sub agent here has run and review the spec. And here is his output. And then

**[28:31]** we also have the engineering design sub agent here to review. And here is its output as well. So eventually here you

**[28:37]** can see we have everything are all verified and once everything is all confirmed and modified our spec. So you

**[28:43]** can see total there are 41 findings 10 from CEO 15 from design and 16 from the

**[28:49]** engineering right to after has done the review for the spec and this is the three review phases that we have follow

**[28:55]** sequentially from CEO design engineering and each of them has its own sub agents and 22 decision has made and there's

**[29:02]** also some couple user decisions that we have flagged it along the way and I have already made the decision and you can

**[29:07]** see that this is the entire summary. Now the last part that I want to talk about is the token consumption. So these are

**[29:12]** the skills that we have went over for GStack. So for token consumption you can see here for the office hour we have

**[29:18]** consumed 170 for the spec team 200k and also the auto plan here also consume

**[29:24]** 200k,000 for tokens because we using different sub aents here. So in total here you can see we takes about 600k for

**[29:32]** token sumptions for the entire planning pipeline. That's how much it took for planning a feature on top a brownfield

**[29:38]** project. So at this point here, we can either use the build pipeline from GStack here to execute or the other way

**[29:44]** we can do here is basically try to use like GSD or super power here and try to execute this entire spec step by step.

**[29:50]** And of course, if you want to learn more about GSD and super powers, make sure to check out this video right here. I recently done a comparison between the

**[29:56]** two and in that video we give a brownfield project like this and basically adding a feature to add the

**[30:02]** end to end test coverage and have two framework here like super power and GSD here to both work on that same feature

**[30:08]** using git workshries and by the end of that video I went over the comparison between the two like which framework is

**[30:14]** better for executing the accuracy and the token assumption. So if you are learning more about like okay which

**[30:20]** framework for spectral element is the highest accuracy and has the low token lowest token consumption then make sure

**[30:26]** you check out that video. In that video we went over that. So pretty much that's it for this video. In this video we went over the office hours the spec team

**[30:32]** scale and also the auto plan from the GStack spectrum development framework. So pretty much that's what we covered in this video. So with that being said if

**[30:38]** you do thumb this video please make sure to like this video consider subscribe more content like this. But with that being said I'll see you in the next

**[30:45]** video.
