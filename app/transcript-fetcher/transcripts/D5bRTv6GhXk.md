# Transcript: D5bRTv6GhXk

**URL:** https://www.youtube.com/watch?v=D5bRTv6GhXk
**Segments:** 521

---

## Full Text

In this video, I'm going to show you seven tips on how to improve Claude code's accuracy when you're using it to building products. And the reason why you should listen to me is because I've been using Claude code for more than a year since it released. And prior to this, I was a senior AI software engineer working at companies like Amazon and Microsoft. And right now, I've been using Claude code here to building my startup called bookzero.ai, where the software is using AI here to help businesses to automate bookkeepings. And I was able to do this completely using the power of Claude code. So, that's why in this video, I'm going to show you seven tips on how to improve Claude code's accuracy in this video. So, with that being said, if you're interested, let's get into this. Now, before we continue, I recently launched our school community where I help you to master AI agents, automations, and so much more. And that's all coming from someone who used to work as a senior AI software engineer at companies like Amazon and Microsoft. And in this community, you're going to get over 100 plus video materials like templates and workflows that I personally built and sold over 100 plus times. On top of that, you're also going to get access to our weekly live calls. And just give you an idea, this week we're actually running a Claude code masterclass where we're going to dive into how to improve Claude code's accuracy when we're going to use it to building applications. Plus, you're also going to get full community supports where you're going to get chance to ask questions and get direct answers back. So, if you're ready to level up, make sure you drop right in and I'll see you in a community. So now, to in order to improve Claude code's accuracy, the first thing we're going to take a look at is how we can be able to improve the Claude code's context. And right here you can see, this is how it works. We have user here interacting with Claude code. And the first 20% when we're interacting with Claude code for the conversation, it's going to go great. The accuracy here is really good, great results. But when we get to the 40% for the conversation progress, and then the accuracy here started to drop significantly. And when it gets to 60%, 80%, you can see now accuracy for Claude code is going to get very, very low. And the impact here you can see is going to cause software bugs and AI hallucinations. And by the time when we get to 80% for the context window, maybe that's going to be a huge time wasted because you have to step in and revert the changes that Claude code has done. Now, to solve this, we have to keep track of our context. And to do so, here you can see I have a progress bar at the bottom when I start a Claude code session. It shows exactly where we are, how much context we have consumed so far. So, right here you can see it says 0% because I have no conversation at all in this conversation sessions. And if I were to have some conversation with Claude code, for example, like tell me what this project is about, you can see that it has consumed 3% of the overall conversation context window. So, what we can do here is that if we reach to, for example, like 50% for the progress bar, then it's maybe the best time to start to restart the context window. For example, I'm simply just going to type in {slash} clear. It's going to clear the entire conversation, free up the context here, it's going to down to 0%. And in order to set up the status line right here, you can simply check out this video right here on how you can be able to set this up on your local machine. And simply, you can just going to simply download this MD file right here for the status line setup from our school community and just paste it right here inside your terminal for your Claude code session. And just say, "Please help me to set this up on my Claude code." And what's going to happen here is going to read through the MD file and try to use the status line here to set up the agents. And now you can see we have this changed to just model and also the progress bar as well as how much context we have consumed. Now, of course, we can also be able to further customize this and you can see here that I can also be able to ask, "Hey, I don't want to show this kind of progress bar. What are some other options that we have?" So, you can see it gives me some couple options. I can be able to have emoji met meter here. So, when it reach to like 50% and above, it can be able to show a different emoji, right? Or it can also be like something like a fraction or also a hash bar like this. So, I like the option E here, which gives me a visual on where we are. So, I'm just going to choose option E right here. So, you're going to have a much more customized status bar right off the bat. So, for example, here you can see we're at 4% right here. And this is the current progress bar. So, as we start to progress, it's going to show the hash here to show exactly where we are. And this is also happened universally. So, you can see here if I were to open this in VS Code, start a Claude code session in terminal, right here you can see this is the model, this is the progress bar, context we have consumed, and also the branch that we're in. If currently it's in a different work tree, it's also going to show that right here in the status line. So, as you can see here, that's exactly how we can be able to improve our context by simply keeping track of our context using our status line here to prevent AI here from its hallucination. But the problem here is that after we reach to a certain percentage, for example, over 50%, we're going to restart our context. The problem here is that it's not going to be very productive. And that's where the sub agents here is going to solve this problem. Where we have orchestrator here that's going to orchestrate the task to different sub agents. And each sub agent here is going to have its own fresh context window. And for example, let's say we're working on the back end, we can be able to delegate the task for the API task to a sub agent. Another task here for testing to another sub agent. And another agent here is going to focus on a review. And you can see here that we're going to break those contexts into different sub agents. And the benefits of using sub agents here you can see is that each sub agent is going to have its own fresh context. And they can also be able to work in parallel as well as they're going to produce fewer bugs and less hallucination on the AI because now we're going to delegate the task different sub agents rather than just singly rely on one single agent. And of course, if you're looking to learn more about sub agents, I have a playlist on my YouTube channel on how you can get started with sub agents as well as 10 curated AI sub agents that I personally use to use Claude code here to build features much more faster and much more accurate. So, make sure you check it out. But obviously, having to plan which sub agent to use is always going to be very difficult. And that's why there's a plugin called Superpowers, which will give Claude code here the superpowers here to manage different sub agents and also be able to follow the spectrum of developments here, which will basically help us to clarify what we're trying to build, generate a spec on exactly the execution plan. Then it's going to generate a to-do list on exactly what each sub agent here is going to do. For example, here you can see I have Superpowers installed onto a project. And currently, it's running different sub agents here for different task. And I was able to do this by using the ability here to brainstorm the entire spec and generating different phases here for the implementation plan. And you can see that for implementation plan here, we also have a list of task. And for each task, it's going to have its own sub task here to perform. And not only that, they also follows the test-driven developments, which will basically focusing on writing the plan first and setting the expectation on how the application should perform. And then it's going to write the app logic and then it's going to do the refactoring. Then it's going to cycle through until there's no more to refactor. So, clearly you can see that Superpowers here is going to help you to do all this by improving the accuracy for Claude code. Like I said, be able to manage different sub agents here, be able to create a plan here before we're going to do the execution, and also be able to follow the test-driven developments here to be able to set the expectation on exactly how the application should be able to behave. And then it's going to focus on the app logic until the testing are passed. And you can see that with this agentic framework that Superpowers come with, it's going to help your Claude code here to be much more accurate when you're going to build applications. And of course, if you're looking to go a deep dive on how to set it up, how you can be able to use Superpowers, make sure you check out this video right here that I made on this channel on how you can be able to use Superpowers here to improve Claude code's performance. Now, if you want to take your sub agents here even further, there's also a feature called agent teams that Claude released. And simply, what it does here is that it's going to have a shared communication channel between all the sub agents we have. Because before when we're using sub agents here, we have orchestrator, we dispatch the task to different sub agents. And each sub agent here is basically working on its own task and there's no communication between each workers. And that's where the concept of agent teams that set up the cross-communication environment between all the agents that we have. For example, we can have agent here working on the front end, communicate to agent working on the back end, and also another agent here who working on database communicating with other agents that we have here. And of course, if you want to learn more about agent teams, make sure you check out this video right here when we went on a deep dive on how to use agent teams here inside of Claude code. And just to recap really quickly on what we talked about so far in this video, we went over how to protect our context in Claude code to ensure accuracy, also how we can be able to delegate different contexts to different sub agents, and also how we can be able to make this easier by using a framework called Superpowers, which is agentic skill framework that help Claude code here to build applications much more accurate and much more faster. And furthermore, we also went over how we can be able to take our sub agents here one step further by using a feature called agent teams. And now, what I want to show you here is I want to show you three more tools that can help Claude code here to improve the accuracy even further. So, in that case, the first tool we're going to take a look at is Context Seven, which can help our large language model here providing up-to-date docs to help large language model here to make the right decision. And for example, here you can see there's a clear difference. Before with our Context Seven, large language model here rely on outdated, generic information about libraries that we're going to use. And what you get here is you get code examples outdated based on the year old training data, hallucinate APIs that don't even exist, or even generic answers. But with Context Seven, you can see we're able to pull up-to-date, version-specific documentation, code examples straight from the source. For example, if you're creating NestJS middleware or configure Cloudflare workers, you're able to do this using Context Seven. And simply to do so, all we have to do here just click on the contextseven.com/dashboard. And what's going to happen here is that if you sign up with Context Seven, it will give you API key that you can simply use and connect it with your large language model. So, I'm just going to connect it with Context Seven right here with the account. So now, once we have the key, all we have to do here just copy this command right here to set up the Context Seven for our coding agents. So simply, if I were to open a new terminal session, I'm just going to paste that command right here and it's going to help me to set up Context Seven. So, I'm going to say, "Yes, let's proceed." And it's going to install this onto my local machine. So, right here you can see it's asking agent here to access Context Seven through the MCP server or the CLI skill. And for our case here, I'm going to select CLI plus skills. So now, once I have myself authorized, now it's time for us to set up the coding agents. So, for our case here, I'm going to select Claude code and click on space, click on enter. It's going to set up Claude code with that particular skill on how to use Context Seven. Now, back to the Superpowers project that I mentioned earlier, let's say if I have all the implementation here has completed, now it's moving on to the final review. And what I want to do here is I also want to add a section saying that, "Please use the Context Seven here to fetch the related, up-to-date version of the documentations, using the right documentation here to fact-check everything that we have coded to see everything makes sense." And that's basically my prompt. And what I'm going to do here is I'm just going to copy this prompt right here. Simply, the goal here is try to review the spec on exactly what the expectation is, and also try to look through all the things that we have developed, as well as using Context Seven here to fact-check everything based on the documentation that we have. And that's exactly how we can be able to fact check, making sure that large language model here is using the most up-to-date documentations before it's going to do coding work. And the next I'm going to take a look at is how we can be able to build our knowledge base. Because usually what happens here is that you might be having a lot of web sources with a lot of documentations laying around in your code base. And let's say you're going to start a brand new Claude code session, it's going to take all the documentations that you have locally in your repositories, put it inside of our context. And that will get us back to the step one, which we really have to protect our context window. So, to do so, what we can do here is that we can be able to update, let's say if you have done some lot research, you wrote those documentations in your repositories, maybe from a YouTube video, from Google Drive files, from PRD files, or any other web sources, we can be able to stuff them in into NotebookLM and treat that as a knowledge base with a grounded sources, so that every time when Claude code have any questions, we can be able to have Claude code here to query this information to a third-party knowledge base using NotebookLM here, which is completely free. And this way we no longer have to stuff those documentations into the initial context window when Claude code starts. It's going to fetch those information from NotebookLM here to fetch the right information in the knowledge base. And the benefits of using this here, you can see it's going to help us to think better, right? It's going to give us better instructions and build better. Because like I said, right before we have bunch of documentation or maybe research that we have done, and if you were to keep it in just NotebookLM and having Claude code here to only fetch those information when it needs to, it's going to have a clear instruction because when Claude needs it, it's going to fetch that information from NotebookLM without putting everything into the initial context when we start Claude code here just during the execution. And just to put a perspective on how the workflow is going to work, before you're going to start coding, maybe you have done some bunch of research, like YouTube videos, Google Drive files, or any browser searches, you can be able to put those sources into NotebookLM or any mockups or coding best practice, and then we can save this into our system prompt for Claude the MD file, so that we tell exactly to query NotebookLM here for the grounded answer. And then during the time when Claude code here start coding, it's going to fetch the information from NotebookLM here only for the grounded sources. This way we're going to ensure that Claude code here is going to get the accurate answer because the sources that we have in NotebookLM here is grounded because it only uses sources that we provided. And the context window here is going to be a lot less compared to before because now we're only putting information that we need into the context. If the information that we don't need, they're going to stay in the NotebookLM. And you can also be able to use that across different sessions, like let's say you have different sub agents, they can be able to query this using the NotebookLM here as well, so that we have a persistent knowledge across different sessions. And you can see here with this approach, this is going to be very powerful. So, if you're interested to see how we can be able to combine the power of NotebookLM here with Claude code, then be sure to check out this video right here that I made on this channel on how we can be able to turn Claude code here just become executor and NotebookLM here is going to be the brain. And lastly, what I want to talk about is basically a trend going on recently of using CLI over MCP. And you can see from this Google trend right here that CLI seems to be over dominating for the trends over MCP. And the reason here is also very simple, it's token efficiency. Because whenever it loads up the context when we start Claude code, it's going to feed in all the data schema into the context window. And like I mentioned before, it's going to go back to square one, that we are going to have AI here start hallucinating if the context window start getting too big. And you can see here by having a CLI plus skills, it's going to teach Claude code how to use the CLI, and we only load information where we need to to the context window on how to use it because Claude code is using CLI, and a lot of those information on how to use CLI and can be converted into skills, and we all know that skills here we only load informations when the work that Claude here is doing is relevant, right? So, we don't load all the skills, we only load the skills when Claude here is doing work that's related to that skill. And that's the benefits of using CLI here over MCP to avoid the context rod. And you can clearly see that this also dramatically reduce the cost. On the right here, you can see this is from the skill kits, where it's saying that CLI here cost less compared to the MCP. And just to prove to you that on this video on this channel, I actually did a Playwright CLI and also MCP video. And latest video that I made on Playwright CLI, I actually test this with MCP version and CLI version for Playwrights, and I find that token consumption here Playwright seems to be a lot less, and the result here is more accurate compared to MCP. So, if you're interested to see the results, make sure to check out this playlist right here to see the entire comparison. So now, there you have it, guys. Here are the seven tips on how to improve Claude code's accuracy in this video that we went over. And if you do find value in this video, please make sure to like this video. And of course, if you're looking to level up your Claude code, make sure to check out our school community to get all the video materials plus live calls and also our community supports. So, with that being said, I'll see you in the next one.

---

## Timestamped Segments

**[0:00]** In this video, I'm going to show you

**[0:01]** seven tips on how to improve Claude

**[0:03]** code's accuracy when you're using it to

**[0:05]** building products. And the reason why

**[0:06]** you should listen to me is because I've

**[0:08]** been using Claude code for more than a

**[0:09]** year since it released. And prior to

**[0:11]** this, I was a senior AI software

**[0:13]** engineer working at companies like

**[0:15]** Amazon and Microsoft. And right now,

**[0:17]** I've been using Claude code here to

**[0:18]** building my startup called bookzero.ai,

**[0:20]** where the software is using AI here to

**[0:22]** help businesses to automate

**[0:23]** bookkeepings. And I was able to do this

**[0:25]** completely using the power of Claude

**[0:27]** code. So, that's why in this video, I'm

**[0:28]** going to show you seven tips on how to

**[0:30]** improve Claude code's accuracy in this

**[0:32]** video. So, with that being said, if

**[0:33]** you're interested, let's get into this.

**[0:35]** Now, before we continue, I recently

**[0:37]** launched our school community where I

**[0:38]** help you to master AI agents,

**[0:40]** automations, and so much more. And

**[0:42]** that's all coming from someone who used

**[0:43]** to work as a senior AI software engineer

**[0:46]** at companies like Amazon and Microsoft.

**[0:48]** And in this community, you're going to

**[0:50]** get over 100 plus video materials like

**[0:51]** templates and workflows that I

**[0:53]** personally built and sold over 100 plus

**[0:55]** times. On top of that, you're also going

**[0:57]** to get access to our weekly live calls.

**[0:59]** And just give you an idea, this week

**[1:01]** we're actually running a Claude code

**[1:02]** masterclass where we're going to dive

**[1:03]** into how to improve Claude code's

**[1:05]** accuracy when we're going to use it to

**[1:07]** building applications. Plus, you're also

**[1:08]** going to get full community supports

**[1:10]** where you're going to get chance to ask

**[1:11]** questions and get direct answers back.

**[1:13]** So, if you're ready to level up, make

**[1:15]** sure you drop right in and I'll see you

**[1:16]** in a community. So now, to in order to

**[1:18]** improve Claude code's accuracy, the

**[1:19]** first thing we're going to take a look

**[1:20]** at is how we can be able to improve the

**[1:22]** Claude code's context. And right here

**[1:24]** you can see, this is how it works. We

**[1:25]** have user here interacting with Claude

**[1:27]** code. And the first 20% when we're

**[1:29]** interacting with Claude code for the

**[1:31]** conversation, it's going to go great.

**[1:32]** The accuracy here is really good, great

**[1:34]** results. But when we get to the 40% for

**[1:38]** the conversation progress, and then the

**[1:39]** accuracy here started to drop

**[1:41]** significantly. And when it gets to 60%,

**[1:43]** 80%, you can see now accuracy for Claude

**[1:46]** code is going to get very, very low. And

**[1:48]** the impact here you can see is going to

**[1:49]** cause software bugs and AI

**[1:51]** hallucinations. And by the time when we

**[1:53]** get to 80% for the context window, maybe

**[1:55]** that's going to be a huge time wasted

**[1:57]** because you have to step in and revert

**[1:58]** the changes that Claude code has done.

**[2:00]** Now, to solve this, we have to keep

**[2:01]** track of our context. And to do so, here

**[2:03]** you can see I have a progress bar at the

**[2:05]** bottom when I start a Claude code

**[2:06]** session. It shows exactly where we are,

**[2:09]** how much context we have consumed so

**[2:10]** far. So, right here you can see it says

**[2:12]** 0% because I have no conversation at all

**[2:15]** in this conversation sessions. And if I

**[2:16]** were to have some conversation with

**[2:18]** Claude code, for example, like tell me

**[2:19]** what this project is about, you can see

**[2:21]** that it has consumed 3% of the overall

**[2:24]** conversation context window. So, what we

**[2:26]** can do here is that if we reach to, for

**[2:28]** example, like 50% for the progress bar,

**[2:30]** then it's maybe the best time to start

**[2:32]** to restart the context window. For

**[2:34]** example, I'm simply just going to type

**[2:35]** in {slash} clear. It's going to clear

**[2:37]** the entire conversation, free up the

**[2:39]** context here, it's going to down to 0%.

**[2:41]** And in order to set up the status line

**[2:42]** right here, you can simply check out

**[2:43]** this video right here on how you can be

**[2:45]** able to set this up on your local

**[2:46]** machine. And simply, you can just going

**[2:48]** to simply download this MD file right

**[2:49]** here for the status line setup from our

**[2:51]** school community and just paste it right

**[2:53]** here inside your terminal for your

**[2:54]** Claude code session. And just say,

**[2:56]** "Please help me to set this up on my

**[2:57]** Claude code." And what's going to happen

**[2:59]** here is going to read through the MD

**[3:00]** file and try to use the status line here

**[3:02]** to set up the agents. And now you can

**[3:03]** see we have this changed to just model

**[3:05]** and also the progress bar as well as how

**[3:07]** much context we have consumed. Now, of

**[3:09]** course, we can also be able to further

**[3:10]** customize this and you can see here that

**[3:12]** I can also be able to ask, "Hey, I don't

**[3:14]** want to show this kind of progress bar.

**[3:16]** What are some other options that we

**[3:17]** have?" So, you can see it gives me some

**[3:18]** couple options. I can be able to have

**[3:20]** emoji met meter here. So, when it reach

**[3:22]** to like 50% and above, it can be able to

**[3:24]** show a different emoji, right? Or it can

**[3:26]** also be like something like a fraction

**[3:27]** or also a hash bar like this. So, I like

**[3:30]** the option E here, which gives me a

**[3:32]** visual on where we are. So, I'm just

**[3:33]** going to choose option E right here. So,

**[3:35]** you're going to have a much more

**[3:36]** customized status bar right off the bat.

**[3:39]** So, for example, here you can see we're

**[3:40]** at 4% right here. And this is the

**[3:42]** current progress bar. So, as we start to

**[3:44]** progress, it's going to show the hash

**[3:46]** here to show exactly where we are. And

**[3:47]** this is also happened universally. So,

**[3:49]** you can see here if I were to open this

**[3:51]** in VS Code, start a Claude code session

**[3:53]** in terminal, right here you can see this

**[3:54]** is the model, this is the progress bar,

**[3:56]** context we have consumed, and also the

**[3:58]** branch that we're in. If currently it's

**[4:00]** in a different work tree, it's also

**[4:01]** going to show that right here in the

**[4:02]** status line. So, as you can see here,

**[4:04]** that's exactly how we can be able to

**[4:05]** improve our context by simply keeping

**[4:07]** track of our context using our status

**[4:09]** line here to prevent AI here from its

**[4:10]** hallucination. But the problem here is

**[4:12]** that after we reach to a certain

**[4:13]** percentage, for example, over 50%, we're

**[4:15]** going to restart our context. The

**[4:17]** problem here is that it's not going to

**[4:18]** be very productive. And that's where the

**[4:20]** sub agents here is going to solve this

**[4:21]** problem. Where we have orchestrator here

**[4:22]** that's going to orchestrate the task to

**[4:24]** different sub agents. And each sub agent

**[4:26]** here is going to have its own fresh

**[4:27]** context window. And for example, let's

**[4:29]** say we're working on the back end, we

**[4:30]** can be able to delegate the task for the

**[4:32]** API task to a sub agent. Another task

**[4:34]** here for testing to another sub agent.

**[4:37]** And another agent here is going to focus

**[4:38]** on a review. And you can see here that

**[4:40]** we're going to break those contexts into

**[4:41]** different sub agents. And the benefits

**[4:43]** of using sub agents here you can see is

**[4:44]** that each sub agent is going to have its

**[4:46]** own fresh context. And they can also be

**[4:48]** able to work in parallel as well as

**[4:49]** they're going to produce fewer bugs and

**[4:51]** less hallucination on the AI because now

**[4:53]** we're going to delegate the task

**[4:54]** different sub agents rather than just

**[4:56]** singly rely on one single agent. And of

**[4:58]** course, if you're looking to learn more

**[4:59]** about sub agents, I have a playlist on

**[5:01]** my YouTube channel on how you can get

**[5:02]** started with sub agents as well as 10

**[5:04]** curated AI sub agents that I personally

**[5:06]** use to use Claude code here to build

**[5:07]** features much more faster and much more

**[5:09]** accurate. So, make sure you check it

**[5:11]** out. But obviously, having to plan which

**[5:12]** sub agent to use is always going to be

**[5:14]** very difficult. And that's why there's a

**[5:15]** plugin called Superpowers, which will

**[5:17]** give Claude code here the superpowers

**[5:18]** here to manage different sub agents and

**[5:20]** also be able to follow the spectrum of

**[5:22]** developments here, which will basically

**[5:23]** help us to clarify what we're trying to

**[5:24]** build, generate a spec on exactly the

**[5:26]** execution plan. Then it's going to

**[5:28]** generate a to-do list on exactly what

**[5:30]** each sub agent here is going to do. For

**[5:31]** example, here you can see I have

**[5:33]** Superpowers installed onto a project.

**[5:35]** And currently, it's running different

**[5:36]** sub agents here for different task. And

**[5:38]** I was able to do this by using the

**[5:39]** ability here to brainstorm the entire

**[5:41]** spec and generating different phases

**[5:43]** here for the implementation plan. And

**[5:45]** you can see that for implementation plan

**[5:46]** here, we also have a list of task. And

**[5:49]** for each task, it's going to have its

**[5:50]** own sub task here to perform. And not

**[5:52]** only that, they also follows the

**[5:53]** test-driven developments, which will

**[5:54]** basically focusing on writing the plan

**[5:56]** first and setting the expectation on how

**[5:58]** the application should perform. And then

**[6:00]** it's going to write the app logic and

**[6:01]** then it's going to do the refactoring.

**[6:03]** Then it's going to cycle through until

**[6:04]** there's no more to refactor. So, clearly

**[6:06]** you can see that Superpowers here is

**[6:07]** going to help you to do all this by

**[6:08]** improving the accuracy for Claude code.

**[6:10]** Like I said, be able to manage different

**[6:12]** sub agents here, be able to create a

**[6:13]** plan here before we're going to do the

**[6:14]** execution, and also be able to follow

**[6:16]** the test-driven developments here to be

**[6:17]** able to set the expectation on exactly

**[6:19]** how the application should be able to

**[6:21]** behave. And then it's going to focus on

**[6:22]** the app logic until the testing are

**[6:23]** passed. And you can see that with this

**[6:25]** agentic framework that Superpowers come

**[6:26]** with, it's going to help your Claude

**[6:28]** code here to be much more accurate when

**[6:29]** you're going to build applications. And

**[6:31]** of course, if you're looking to go a

**[6:32]** deep dive on how to set it up, how you

**[6:34]** can be able to use Superpowers, make

**[6:35]** sure you check out this video right here

**[6:36]** that I made on this channel on how you

**[6:38]** can be able to use Superpowers here to

**[6:39]** improve Claude code's performance. Now,

**[6:41]** if you want to take your sub agents here

**[6:42]** even further, there's also a feature

**[6:44]** called agent teams that Claude released.

**[6:46]** And simply, what it does here is that

**[6:47]** it's going to have a shared

**[6:48]** communication channel between all the

**[6:50]** sub agents we have. Because before when

**[6:52]** we're using sub agents here, we have

**[6:53]** orchestrator, we dispatch the task to

**[6:55]** different sub agents. And each sub agent

**[6:56]** here is basically working on its own

**[6:58]** task and there's no communication

**[6:59]** between each workers. And that's where

**[7:01]** the concept of agent teams that set up

**[7:03]** the cross-communication environment

**[7:04]** between all the agents that we have. For

**[7:06]** example, we can have agent here working

**[7:07]** on the front end, communicate to agent

**[7:09]** working on the back end, and also

**[7:10]** another agent here who working on

**[7:12]** database communicating with other agents

**[7:14]** that we have here. And of course, if you

**[7:15]** want to learn more about agent teams,

**[7:16]** make sure you check out this video right

**[7:17]** here when we went on a deep dive on how

**[7:19]** to use agent teams here inside of Claude

**[7:21]** code. And just to recap really quickly

**[7:23]** on what we talked about so far in this

**[7:24]** video, we went over how to protect our

**[7:26]** context in Claude code to ensure

**[7:27]** accuracy, also how we can be able to

**[7:29]** delegate different contexts to different

**[7:30]** sub agents, and also how we can be able

**[7:32]** to make this easier by using a framework

**[7:34]** called Superpowers, which is agentic

**[7:36]** skill framework that help Claude code

**[7:37]** here to build applications much more

**[7:39]** accurate and much more faster. And

**[7:41]** furthermore, we also went over how we

**[7:42]** can be able to take our sub agents here

**[7:44]** one step further by using a feature

**[7:45]** called agent teams. And now, what I want

**[7:47]** to show you here is I want to show you

**[7:48]** three more tools that can help Claude

**[7:50]** code here to improve the accuracy even

**[7:52]** further. So, in that case, the first

**[7:53]** tool we're going to take a look at is

**[7:54]** Context Seven, which can help our large

**[7:56]** language model here providing up-to-date

**[7:58]** docs to help large language model here

**[7:59]** to make the right decision. And for

**[8:01]** example, here you can see there's a

**[8:02]** clear difference. Before with our

**[8:03]** Context Seven, large language model here

**[8:05]** rely on outdated, generic information

**[8:07]** about libraries that we're going to use.

**[8:09]** And what you get here is you get code

**[8:10]** examples outdated based on the year old

**[8:12]** training data, hallucinate APIs that

**[8:14]** don't even exist, or even generic

**[8:16]** answers. But with Context Seven, you can

**[8:17]** see we're able to pull up-to-date,

**[8:19]** version-specific documentation, code

**[8:21]** examples straight from the source. For

**[8:23]** example, if you're creating NestJS

**[8:24]** middleware or configure Cloudflare

**[8:26]** workers, you're able to do this using

**[8:28]** Context Seven. And simply to do so, all

**[8:30]** we have to do here just click on the

**[8:32]** contextseven.com/dashboard.

**[8:34]** And what's going to happen here is that

**[8:35]** if you sign up with Context Seven, it

**[8:37]** will give you API key that you can

**[8:38]** simply use and connect it with your

**[8:40]** large language model. So, I'm just going

**[8:42]** to connect it with Context Seven right

**[8:43]** here with the account. So now, once we

**[8:44]** have the key, all we have to do here

**[8:46]** just copy this command right here to set

**[8:47]** up the Context Seven for our coding

**[8:49]** agents. So simply, if I were to open a

**[8:51]** new terminal session, I'm just going to

**[8:53]** paste that command right here and it's

**[8:54]** going to help me to set up Context

**[8:56]** Seven. So, I'm going to say, "Yes, let's

**[8:58]** proceed." And it's going to install this

**[9:00]** onto my local machine. So, right here

**[9:01]** you can see it's asking agent here to

**[9:03]** access Context Seven through the MCP

**[9:05]** server or the CLI skill. And for our

**[9:07]** case here, I'm going to select CLI plus

**[9:08]** skills. So now, once I have myself

**[9:10]** authorized, now it's time for us to set

**[9:12]** up the coding agents. So, for our case

**[9:14]** here, I'm going to select Claude code

**[9:16]** and click on space, click on enter. It's

**[9:18]** going to set up Claude code with that

**[9:19]** particular skill on how to use Context

**[9:21]** Seven. Now, back to the Superpowers

**[9:23]** project that I mentioned earlier, let's

**[9:24]** say if I have all the implementation

**[9:26]** here has completed, now it's moving on

**[9:28]** to the final review. And what I want to

**[9:29]** do here is I also want to add a section

**[9:31]** saying that, "Please use the Context

**[9:33]** Seven here to fetch the related,

**[9:34]** up-to-date version of the

**[9:35]** documentations, using the right

**[9:37]** documentation here to fact-check

**[9:39]** everything that we have coded to see

**[9:40]** everything makes sense."

**[9:42]** And that's basically my prompt. And what

**[9:44]** I'm going to do here is I'm just going

**[9:45]** to copy this prompt right here. Simply,

**[9:47]** the goal here is try to review the spec

**[9:48]** on exactly what the expectation is, and

**[9:50]** also try to look through all the things

**[9:52]** that we have developed, as well as using

**[9:53]** Context Seven here to fact-check

**[9:55]** everything based on the documentation

**[9:56]** that we have. And that's exactly how we

**[9:58]** can be able to fact check, making sure

**[9:59]** that large language model here is using

**[10:01]** the most up-to-date documentations

**[10:03]** before it's going to do coding work. And

**[10:05]** the next I'm going to take a look at is

**[10:06]** how we can be able to build our

**[10:08]** knowledge base. Because usually what

**[10:09]** happens here is that you might be having

**[10:11]** a lot of web sources with a lot of

**[10:12]** documentations laying around in your

**[10:14]** code base. And let's say you're going to

**[10:15]** start a brand new Claude code session,

**[10:17]** it's going to take all the

**[10:18]** documentations that you have locally in

**[10:20]** your repositories, put it inside of our

**[10:22]** context. And that will get us back to

**[10:25]** the step one, which we really have to

**[10:26]** protect our context window. So, to do

**[10:29]** so, what we can do here is that we can

**[10:30]** be able to update, let's say if you have

**[10:31]** done some lot research, you wrote those

**[10:33]** documentations in your repositories,

**[10:35]** maybe from a YouTube video, from Google

**[10:37]** Drive files, from PRD files, or any

**[10:40]** other web sources, we can be able to

**[10:41]** stuff them in into NotebookLM and treat

**[10:44]** that as a knowledge base with a grounded

**[10:46]** sources, so that every time when Claude

**[10:47]** code have any questions, we can be able

**[10:49]** to have Claude code here to query this

**[10:51]** information to a third-party knowledge

**[10:53]** base using NotebookLM here, which is

**[10:55]** completely free. And this way we no

**[10:57]** longer have to stuff those

**[10:58]** documentations into the initial context

**[11:01]** window when Claude code starts. It's

**[11:02]** going to fetch those information from

**[11:04]** NotebookLM here to fetch the right

**[11:05]** information in the knowledge base. And

**[11:07]** the benefits of using this here, you can

**[11:09]** see it's going to help us to think

**[11:10]** better, right? It's going to give us

**[11:12]** better instructions and build better.

**[11:14]** Because like I said, right before we

**[11:15]** have bunch of documentation or maybe

**[11:17]** research that we have done, and if you

**[11:18]** were to keep it in just NotebookLM and

**[11:21]** having Claude code here to only fetch

**[11:22]** those information when it needs to, it's

**[11:24]** going to have a clear instruction

**[11:25]** because when Claude needs it, it's going

**[11:27]** to fetch that information from

**[11:29]** NotebookLM without putting everything

**[11:30]** into the initial context when we start

**[11:32]** Claude code here just during the

**[11:33]** execution. And just to put a perspective

**[11:35]** on how the workflow is going to work,

**[11:37]** before you're going to start coding,

**[11:38]** maybe you have done some bunch of

**[11:39]** research, like YouTube videos, Google

**[11:41]** Drive files, or any browser searches,

**[11:44]** you can be able to put those sources

**[11:45]** into NotebookLM or any mockups or coding

**[11:48]** best practice, and then we can save this

**[11:50]** into our system prompt for Claude the MD

**[11:52]** file, so that we tell exactly to query

**[11:54]** NotebookLM here for the grounded answer.

**[11:56]** And then during the time when Claude

**[11:57]** code here start coding, it's going to

**[11:59]** fetch the information from NotebookLM

**[12:01]** here only for the grounded sources. This

**[12:03]** way we're going to ensure that Claude

**[12:04]** code here is going to get the accurate

**[12:06]** answer because the sources that we have

**[12:08]** in NotebookLM here is grounded because

**[12:10]** it only uses sources that we provided.

**[12:12]** And the context window here is going to

**[12:13]** be a lot less compared to before because

**[12:14]** now we're only putting information that

**[12:16]** we need into the context. If the

**[12:18]** information that we don't need, they're

**[12:20]** going to stay in the NotebookLM.

**[12:22]** And you can also be able to use that

**[12:23]** across different sessions, like let's

**[12:24]** say you have different sub agents, they

**[12:26]** can be able to query this using the

**[12:27]** NotebookLM here as well, so that we have

**[12:30]** a persistent knowledge across different

**[12:31]** sessions. And you can see here with this

**[12:33]** approach, this is going to be very

**[12:34]** powerful. So, if you're interested to

**[12:36]** see how we can be able to combine the

**[12:37]** power of NotebookLM here with Claude

**[12:39]** code, then be sure to check out this

**[12:41]** video right here that I made on this

**[12:42]** channel on how we can be able to turn

**[12:43]** Claude code here just become executor

**[12:46]** and NotebookLM here is going to be the

**[12:47]** brain. And lastly, what I want to talk

**[12:49]** about is basically a trend going on

**[12:50]** recently of using CLI over MCP. And you

**[12:53]** can see from this Google trend right

**[12:55]** here that CLI seems to be over

**[12:57]** dominating for the trends over MCP. And

**[13:00]** the reason here is also very simple,

**[13:01]** it's token efficiency. Because whenever

**[13:03]** it loads up the context when we start

**[13:05]** Claude code, it's going to feed in all

**[13:07]** the data schema into the context window.

**[13:09]** And like I mentioned before, it's going

**[13:11]** to go back to square one, that we are

**[13:13]** going to have AI here start

**[13:14]** hallucinating if the context window

**[13:16]** start getting too big. And you can see

**[13:18]** here by having a CLI plus skills, it's

**[13:21]** going to teach Claude code how to use

**[13:23]** the CLI, and we only load information

**[13:25]** where we need to to the context window

**[13:28]** on how to use it because Claude code is

**[13:29]** using CLI, and a lot of those

**[13:31]** information on how to use CLI and can be

**[13:33]** converted into skills, and we all know

**[13:35]** that skills here we only load

**[13:37]** informations when the work that Claude

**[13:39]** here is doing is relevant, right? So, we

**[13:41]** don't load all the skills, we only load

**[13:42]** the skills when Claude here is doing

**[13:44]** work that's related to that skill. And

**[13:46]** that's the benefits of using CLI here

**[13:48]** over MCP to avoid the context rod. And

**[13:51]** you can clearly see that this also

**[13:53]** dramatically reduce the cost. On the

**[13:55]** right here, you can see this is from the

**[13:57]** skill kits, where it's saying that CLI

**[13:59]** here cost less compared to the MCP. And

**[14:02]** just to prove to you that on this video

**[14:04]** on this channel, I actually did a

**[14:05]** Playwright CLI and also MCP video. And

**[14:08]** latest video that I made on Playwright

**[14:10]** CLI, I actually test this with MCP

**[14:12]** version and CLI version for Playwrights,

**[14:15]** and I find that token consumption here

**[14:16]** Playwright seems to be a lot less, and

**[14:18]** the result here is more accurate

**[14:20]** compared to MCP. So, if you're

**[14:21]** interested to see the results, make sure

**[14:23]** to check out this playlist right here to

**[14:24]** see the entire comparison. So now, there

**[14:26]** you have it, guys. Here are the seven

**[14:27]** tips on how to improve Claude code's

**[14:29]** accuracy in this video that we went

**[14:31]** over. And if you do find value in this

**[14:32]** video, please make sure to like this

**[14:33]** video. And of course, if you're looking

**[14:35]** to level up your Claude code, make sure

**[14:36]** to check out our school community to get

**[14:38]** all the video materials plus live calls

**[14:40]** and also our community supports. So,

**[14:42]** with that being said, I'll see you in

**[14:43]** the next one.
