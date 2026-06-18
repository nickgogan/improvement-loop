# Transcript: qMnClynCAmM

**URL:** https://www.youtube.com/watch?v=qMnClynCAmM
**Segments:** 907

---

## Full Text

Finally, after months and months of hard work behind the scenes, I am unveiling the new Archon, a massive overhaul of the AI command center that I was working on last year. It is now the first open-source harness builder for AI coding. So, similar vision, but a very different and powerful use case. Harnesses are the future. It's the layer on top of your coding agents that orchestrates the different sessions. It's what makes AI coding deterministic and repeatable. We'll talk about what that means. And now with Archon, you can build your own custom harnesses very easily. No matter how you work with AI coding agents right now, you can take that process and bundle it up into an Archon workflow that you can run across all your code bases, even handling different tasks in parallel. Archon handles all of the messy logic behind the scenes to make that possible. And so in this video, I want to talk about what makes Archon so powerful. I want to show you how to get started with it and even give you some inspiration for the kinds of things you can do with it. It's a very powerful tool. It's actually hard for me to explain everything in just one video, but a lot more content coming on Archon soon as well. So, the main idea with Archon is you can encode your development process as a workflow, no matter what it is. And so I will link to this repo in the description. I highly encourage you to try Archon today. It's very easy to get up and running. I'll show you that in a little bit. But I have an example here at the top of the readme for what an Archon workflow looks like. And so every single workflow is just a combination of nodes, where a node is either a prompt that we send into a coding agent session, or it is a deterministic command that we want to invoke. Because sometimes we want to enforce certain things to happen, like context creation or validation, that we don't want to leave up to the coding agent cuz it might forget to do so. So we want to plan, implement tasks in a loop, run the tests, have it do a review, even adding in a human approval gate so we can address our feedback. We can build ourselves into Archon workflows if we want as well, and then ending with a pull request. And Archon comes with a skill that I'll cover with you in a bit as well. So we just say like use Archon to build this feature, it knows automatically the workflow to use, it'll invoke it for us, and we have the logs so we can monitor the workflow along the way. Archon also comes with a ton of pre-packaged workflows that will immediately level up your agentic coding workflow. Fixing GitHub issues, creating pull requests from ideas. We have pull request validation and review commands, even one to help you create full PRDs with human in the loop. So, ton of things for you to use and very easy to create your own custom workflows as well. We're going to cover all of that in this video. I'm going to give you enough of a starting point for you to dive right into Archon. And then if you want a super deep dive, I'm also doing a live stream this Saturday, 9:00 a.m. Central Time. So come be a part of this as well cuz we're going to get really deep into building workflows and running them in parallel, doing a lot of fancy things. But for now, I want to give you a good overview of Archon, why it's important, where we're heading with agent harnesses, and then we'll get into the setup guide. So I want to start by talking about the evolution that we've seen that has brought us to harness engineering. So prompt engineering, that was all the rage back in 2022 through 2024. It was all about how can we prompt LLMs to get the single best output? And then that evolved into context engineering, which is all about how can we curate the perfect context for a single agent so it can handle a larger set of work. We give it all the context it needs and nothing more. And now that has evolved into harness engineering, where we're dealing with many different coding agent sessions, all tying that together through a harness. And so up until this point, everything we've done here is dealing with a single LLM or a single agent. Now we are stringing coding agent sessions together to handle much larger sets of work. And so maybe you've heard of the Ralph loop before, or Anthropic has built a couple open-source harnesses. There are a lot of harnesses out there, but the problem is that they're not custom to you. Maybe it's a good starting point or helpful to create a proof of concept, but what Archon unlocks for you is being able to create your own custom harness wrapping up your own software development life cycle. And harnesses are a big deal. It's the tooling, the prompting, chaining different coding agents together, everything to elevate the capabilities of a single large language model. And this is really important right now cuz Claude is about to release Mythos, but it's more enterprise use. Like us consumers, there's no way we're going to be able to afford using Mythos for everything. But what we can do is build a harness around Opus to make it more powerful than Mythos by itself. And this is proven. There have been studies that have been done that if we take a large language model and we just use it to create some code, the PR acceptance rate is only 6.7%. But if we create a harness, like the Ralph loop but probably more custom and better, we can get even as high as like almost 70% for a PR acceptance. And I don't want to get like super deep into the study here, but the point is we can elevate models a drastic amount by creating a harness where we build in validation, we build in a special kind of context curation. And that's exactly what Stripe did with Stripe Minion. So I covered this on my channel already actually, but Stripe, they ship 1,300 AI only generated pull requests every single week. And they did this by building their AI coding workflow, their context curation, their validation, enforcing that at different steps of the way in their workflow. So they actually built something kind of like Archon, but it's not open-source, right? You can't use it like you can use Archon. And with the Claude code source code leak, we found that even Anthropic is leaning a lot more into harnesses with agent teams and features they're building around sub-agents. 40% of their code base is just code for harnesses right now. And so that just is a signal for how much it's a big deal right now. And Archon, it wraps above Claude code and Codex. So the old Archon was more of a tool built into coding agents. That's kind of why it became irrelevant because these coding agents, they built all that themselves for rag and task management. You know what I'm talking about if you've used the old Archon. But now the new Archon, it sits above the coding agents and it orchestrates them. So the problem is before, you're dealing with AI shepherding. Like yes, you have your skills and commands and you're running workflows there, but you still have your entire process where you're running different skills and different commands, and you have to remember what comes next, and you have to kick off the code review after the implementation. But now your entire process, you can bundle as an Archon workflow. Define once, run forever, reusable across projects. You also get to pick where you're injecting context. Like maybe you have a skill that you only need during the validation step, or you have an MCP server that you only want during planning. We have that level of control per node with Archon. And kind of like the example I gave in the readme, here's an example of going from plan all the way to open a pull request. This is the kind of thing you can build with Archon. And I think you really see here how we're building in reliability through deterministic steps, enforcing validation at certain steps of the way, and human approvals. So we have our plan here. We can even like build this into a loop where we have the agent create the plan and then we give feedback, and we go in a loop until we go to the coding step. And we do that in a fresh context window. You always want to do your planning and implementation in different coding sessions to remove bias. And then after the coding, we go into the tests, and we run this every single time. Again, we don't want to rely on the coding agent to remember to do the tests all the time. And then we retry and have it fix issues if they come up. Otherwise, we go to the final human approval gate. When things look good, we then open the pull request. Just one example of how you can take I mean this is a more basic example of what your agentic coding workflow might look like, but there's going to be different things depending on if you're fixing bugs or refactoring or building a new feature. All of those things you can build into Archon. And the big secret here is the hybrid secret. This is what makes Stripe Minion so powerful. There are certain steps of the workflow that we don't want the coding agent to decide. Like sometimes we want to curate context in a specific way, or run our tests in a specific way. We have nodes for that that we can build into Archon workflows. But then of course, most of the workflow is still going to be driven by our commands and skills, just sending prompts into our coding agents. We have of course support for all of that so you can take your existing commands and skills, everything, and build it right into Archon. So I hope you can see why this is so powerful, building these kinds of harnesses for yourself. And so with that, I now want to get into the guide for you, how you can get Archon up and running using these workflows in less than 5 minutes. Now, installing Archon is actually incredibly easy because we can use our coding agent to guide us through the entire process. All you have to do is clone the repository, open up Claude, and then ask it to set up Archon. Because it will automatically load in a skill that we have in the code base here that guides you through the entire process. And I'll do this right now with you just to show how easy it is. We can do this in less than 5 minutes. So I'll take this first command here to clone the repository, and then obviously we want to open up our coding agent in this repo so we can load the skill. So we'll change our directory, and then we'll open up Claude. There we go. So now in Claude code, I just say set up Archon. That is all you have to do. And take a look at this. We'll see in just a second, it'll load the Archon skill, and then it'll kick off this process where it'll ask us all the questions we need in order to help us get our credentials set up and then validate that Archon is working on our machine. So first, Archon is going to check to make sure that we have the prerequisites in place, including Bun, and it'll install it if we don't have it already. Then it asks what repository we first want to use Archon with. So it's important that you add in your own project, not the Archon repo, because we want to use the Archon workflows on a target repository. And don't worry, it's super easy to add more projects into Archon after. And so, just for this demonstration here, I have a reg YouTube chat application that I'm going to be running some Archon workflows in. And so, I have the path to this repo cloned locally copied here. And so, I'll just go to option number two, specify a local path. And so, then it's going to ask me, you know, like what is the path? Please paste it. So, I'll paste it in here. And then, it'll register this as our first Archon registered project. And then, going forward, we can add any project into Archon by just running a workflow there for the first time or right within the web UI. I'll show you that in a little bit. Then, it asks what platforms do I want to set up. So, the CLI is included by default. You can run Archon through the CLI, ask your coding agent to do so. But, we can also run in GitHub. And then, we could run through Telegram, through Slack. I'm actually going to set up quite a few of these right now. There are a lot of different interfaces to interact with Archon. Then, I will submit my answer here. There we go. And now, it's going to walk us through setting up the credentials for each one of our platforms. Then, after Archon installs the global CLI, like it did right here, then it's going to walk us through a setup wizard to set our credentials for any other platforms we chose, like GitHub or Slack. We need to do this in a different window, because we don't want to send our API keys directly into Claude Code. So, it's going to spin up another terminal process for us to enter our keys, not going to a coding agent. And so, it should spin up the wizard automatically and bring up another terminal automatically. But, for certain operating systems, or if you're trying to run Archon in a VPS, you will probably have to open up a new session yourself. So, you just open up a new terminal, and you run the Archon setup command. So, Archon is now a globally recognized command, because we installed the CLI. So, this is going to work automatically. In my case, I'm just going to go back to the terminal that it popped up for me automatically. So, we can pick our database. SQLite by default, this is the easiest. Or, you can set up Postgres if you like. So, I'm going to do SQLite. And then, it asks which AI coding assistant you want to use. So, right now, we mostly support Claude. We're almost done with Codex support, and then we want to add in other coding assistants later, like the Pi Agent SDK and Open Code. And so, I'll go with Claude right here. So, I'll just do space to select, and then enter to confirm. And then, how do I want to authenticate with Claude? Well, I just want to use my Anthropic subscription. We are allowed to use our Anthropic subscription as long as it's an application running locally using the Claude Agent SDK. And that is the case for Archon. So, I'm going to use my global auth. Just going to hit enter here. What platforms do I want to connect? So, I'll just select GitHub, Telegram, and Slack. So, then it'll ask me for the credentials for those. And this is where it's going to guide you through getting the API keys for each of them. So, for each one of the platforms you select, there are instructions to walk you through getting your keys for each application. So, I'm just going to go through this quickly. You can take your time to get the keys yourself on your own. All right. Then, after you set all of your credentials, it's going to ask, do you want to install the Archon skill in your project? And I would highly recommend doing this, because then, if we open up Claude Code in our other code base, we can use the Archon CLI to kick off workflows automatically. Cuz then, if we have Claude open there, we can just say, "Use the Archon CLI to invoke whatever workflow to handle a pull request or an issue or something." And it'll know right away to load the skill, and it'll know exactly how to use the Archon CLI. Again, it's important for any CLI to have a skill paired with it, so that our coding agent knows how to use it. So, I will bring this over. It asks for the path. So, I'm just going to take the path that I copied earlier for the repo. Just paste it in right here, so it knows where to copy it. And then, it'll ask if you want a non-default docs directory. If you have other documentation you want to load into Archon, probably don't worry about that right now. That's something that we're working on currently. So, I'll do no there. And there we go. Our setup is complete. And so, what we do here is we actually go back to the first session where we first said, "Set up Archon." And it tells you this here. So, it says, you know, come back here, complete the configuration there, let me know when you are done. So, I'm I'll just say, "Done." And then, what it's going to do now, that I've set all my credentials, is verify that everything is working. So, it'll test the connections. It'll even test running a workflow through the Archon CLI. I'll come back once that is done. All right. So, it confirms that our credentials are good to go, without actually reading them, of course. Then, we list out all of the default Archon workflows to make sure they're available. Those are all the workflows that we have bundled ready for you to use immediately to fix GitHub issues, run a rough loop, create a PRD. There is a lot of value that we have built into this right away. And then, it of course runs a workflow as well. So, it runs our basic Archon assist one just to make sure that the Archon CLI is functioning, and we're ready to use it on any repository that we want. And then, it gives us a summary at the end. And look at how easy it is for us to just start using Archon right now. So, we just open up Claude Code in our target repository. You can really do this in any repo you want, because remember, when we run the Archon CLI in a repo for the first time, it automatically registers it with Archon. So, we just copy over the Archon skill into whatever repo, launch Claude there, and then we can just say, "Use Archon to, for example, fix this issue number." Or, "Help me create a PRD." Whatever workflow you want to use, and you can build your own, like I'll show you in a little bit. So, because I chose my reg YouTube chat application as my onboarding repo, I copied over the Archon skill. So, it knows how to use the Archon CLI when I ask it to. And so, I'm going to open up Claude Code right within this repository, and we are already ready to use a workflow. And so, I'm going to use Archon to help me fix a GitHub issue. And so, going into the issue list for my repo, you can see there is quite a few options that I have to work with here. Well, let's say I just want to deal with issue number one. And so, all I have to do is say, "Use Archon to fix issue number one in GitHub." That is it. I don't have to provide any more context, because it'll know to load the Archon skill, find the right workflow for the job, and then invoke it. And then, our Claude Code can just monitor it in the background. So, there we go. It used the GitHub CLI to view the issue to get context, loaded the Archon skill, and it decided, "Okay, I should use the Archon fix GitHub issue workflow." It's one of the defaults that we have bundled. It is a very powerful workflow, by the way, because it does full investigation, fixing, and validation before it creates the pull request. And that is the end result is we'll have a pull request that has the final implementation from the Archon workflow. So, we can see right here that in Claude Code, it is running as a background process. So, we can track the logs here. We can always ask Claude Code to give us an update for how the workflow is running, or we can view the workflow in the web UI as it is running. Okay. So, right here, we are focusing on using the CLI to run an Archon workflow. That is the most convenient way. But, we also have a web interface. If you want to more visualize what's happening with your workflows, we can also view the logs for the workflows more easily that we run through the CLI. So, I'm going to go back to the terminal where I had the Archon repository open with Claude Code. So, all I have to do, if I want to start the back end and front end of Archon, is I just have to ask my coding agent to do so. It is that easy. So, I can say, "Spin up the front end and back end of Archon." And it's going to, based on the review, understand the commands to run, and then get everything running for us as background processes. And so, take a look at this. If I go into the browser and go to port 5178, right? Cuz that's where it says it's running right now, I can see my conversations. I can see the workflows that are currently active. So, if I go into the dashboard here, I can see that it's using the Archon fix GitHub issue workflow. I can view the logs for it to see what is currently happening. So, this is the node that we just completed. Now, we're currently investigating the issue. So, we started with web research, then now we're investigating. We can see all the tool calls. So, all the logs from Claude Code, if you want to dig into all the individual actions that it's doing as it's going through this Archon workflow. And so, every single one of the nodes here is either a deterministic action, like a bash command, or it's a session with Claude Code. And again, in our Archon workflows, we can determine when we go from node to node, do we want to start a brand new session with Claude Code or continue the conversation? We have a lot of flexibility for token management, making sure we keep our context lean when we're dealing with our coding agents. One of the big things that Archon gives us that we were missing before. All right. And while we wait for this workflow to finish, it's going to create a pull request at the end, I want to show you what it actually looks like in the YAML. Cuz remember, all of the workflows in Archon are simply defined as YAML files. It is so easy to improve the existing ones that we have in Archon, and even create your own. That's one of the last things I'll show you in this video. And so, within the .archon folder in the Archon repository, we have all of the default workflows. These are also bundled into the CLI. So, when you run the CLI from any other repository, it'll automatically have access to these. So, take a look at this. We have all of these different workflows. The one that we're running right now is Archon fix GitHub issue. And [snorts] so, we have a description for the workflow. And this is important, because this is just like Claude Code's skills, where the description is what we first give to Claude Code. Like, "Hey, here's a workflow from Archon that you want to use when the user is specifically asking for you to fix a GitHub issue." Right? We don't want to load the entire workflow into context for the coding agent. That's way too much. It only needs this brief description up front. So, it uses this to determine if it should analyze and run this entire workflow. We can define the provider up front. Again, we're supporting more in the near future, the default model used for each of the nodes, and then we have the list of nodes. This is the step-by-step that we're going through. So, exactly what I have defined in the YAML document, we can see right here in the web UI. We see the full execution, all the different nodes that we have, the different branches and decisions that can be made. All of this is a direct visualization of what we have in the YAML right here. So, for this workflow specifically, we are going to first extract the issue number. So, based on the prompt that is fed into this workflow, it's kind of like running a sub agent in Claude Code, we're going to grab the issue number, and then we're going to classify the issue. Is this a bug that needs to be fixed or a feature that we need to build? Because that's going to determine what comes next, right? Do we have to investigate the issue or plan for a new feature? And we have the prompt here that we're sending into the model for this step specifically. And one of the most powerful things, I know that token consumption is a big deal right now, especially because of rate limits with Anthropic. One of the powerful things we can do with Archon is specify the model we want to use for the individual nodes. So, certain nodes, like classification, they don't need a lot of reasoning power. So, we can make it a lot more token efficient, a lot cheaper by just using Haiku for our model. And then we go into the research phase. In this one, we're just going to use the default model. So, we don't specify it here, it just means that it'll use the default model of Sonnet. And we don't have the prompt in line, we're actually using a command. And so, for every single workflow that's in this folder, and then the commands are sort of like the extensions that we run in certain nodes. So, for example, we have the Archon web research command right here. So, I'll just open this really quickly. It's just like commands or skills in Claude, where it's just a longer prompt that we're going to invoke for this node specifically. So, we do our web research, and then we investigate if it is a bug or we plan if it is a feature request. That's the the first decision that we can see right here. So, in the case of the workflow we just invoked, it went down the path of investigation because looking at our issue here, it's definitely a problem that we're addressing, not a new feature that we are adding. And so, not like I need to go like in super deep detail for every single node here, but I'm just trying to show you the idea of like how we can take a pretty comprehensive workflow and turn it into this single process that we run with Archon. It's more than just writing some code. It's doing classification, it's doing investigation or planning, it's implementing, validating, and then creating the pull request at the end as well, and even doing further review after that point. And so, we have a lot more faith by the time this workflow finishes that the pull request is really ready for us to review and merge. And yes, it takes a good number of tokens to go through this many steps, but that's why we lean on being able to specify the model at each step of the way. We're able to use Haiku for a lot of this here. So, we're just kind of giving more of a set of guidance around the coding agent. That's why we're calling it a harness, right? Like, this is sort of a harness wrapping many different Claude Code sessions to work together to fix a GitHub issue. And there are so many amazing workflows that we have available for you that you can use out of the box, and then anything that's not here, you can just create by yourself. So, we have the adversarial dev harness as an Archon workflow. I showed this in a live stream that I'll link to right here. We have a comprehensive PR review workflow. We have one to help you create issues. So, like investigating a problem creating a GitHub issue, idea to PR, this is a very comprehensive one. We have one with human in the loop. We actually have human in the loop with Archon. So, we can pause at any given node to ask for your input. So, we have this interactive PRD, where it'll have you sort of ideate with a coding agent to create that initial spec for a new application you want to create. We have the Ralph loop built as an Archon workflow. Uh man, there's just so many things that are here already. We even have an Archon workflow to help you build more workflows. We'll use this in just a second here. So, yeah, literally like no matter what you want to do with your AI coding assistants, it doesn't matter how many coding agent sessions you need, you can bundle it together into an Archon workflow, adding in reliability through deterministic nodes, like you always want to run validation at some point, or you always want to curate context in this way. The sky's the limit for what you can build with Archon. All right, so I'm just going to keep showing you some really cool ways to use Archon. I'm going to keep using the GitHub issue fix workflow because that is my most used, but there are so many amazing workflows you can use. And by the way, you can just ask it in the web UI here, what projects and workflows do you have? And so, the Archon agent in the UI is actually kind of special. It has all of the context around Archon, like our registered projects and workflows injected in at the start of the conversation. And by the way, in the web UI here, you can just click add project to give a GitHub URL or local path if you want to register more. So, right now, this is my only registered project, as you can see from the drop-down here. And then here are all of the available workflows, which this will also include any that you build on top yourself, but these are all of the default ones shipped with Archon. So, now, for example, I can say fix GitHub issue, and then if I go to the issue list here, we're currently handling this one and the other screen. So, we'll just do number three. So, I'll do number three for uh the rag YouTube chat project. So, we don't even have to call out the exact repo name, it can reason based on what we said and what context it has loaded to know which workflow to kick off. So, take a look at that. It invoked the Archon fix GitHub issue workflow specifically in our rag YouTube chat application. So, it does all of the routing for us from the web UI. And we can go into the logs, the beautiful screen. This is the exact same view we saw earlier, but this time we actually invoked it from the web UI. Very cool. And another really powerful thing I want to show you really quickly is that we can invoke a ton of workflows in parallel. And so, for example, I'm back here with Claude open in my rag YouTube chat application, and I can just say use Archon to fix GitHub issues 5 7 8 9 10 and 11. So, the last six in that list there that we haven't touched yet, I just want to rip through all of these at the exact same time. And so, we can invoke Archon directly from our project, or we can have Claude Code open within our Archon repository, and we can point it to any code base if we just give it the path. And remember, it will automatically register Archon at that point. So, now it used the Archon CLI. Boom, look at that. Six times in a row, all of them are running as background processes, so we can see that right here, and we can continue to have it monitor for us, or even just ask us along the way, like, you know, like give us a status update. So, we can view it in the user interface. Like, if I wanted to go back to the UI now, we can see that we have all of these workflows currently running, or we can just have Claude Code constantly check for us. We could, for example, use the slash loop command in Claude Code to say, you know, like every 10 minutes, check on the workflows and restart if there's a failure or something, which there usually isn't. But yeah, so all six workflows are running, progressing through the early DAG stages. So, yeah, most of them are on the classify step right now, figuring out is the issue a new feature or a problem that has to be addressed. Super cool. All right, so I'm back, and we have the pull requests for all of our Archon workflow runs. So, we can see them all complete in the web UI as well. We can click into the logs just see what happened every step of the way. And of course, we can go see our final result. Going to the repository for the first time here, I'll click on pull requests, and boom, there we go. We have eight new open pull requests handling each of the issues that we handled with an Archon workflow. All right, the last thing that I want to show you really quickly here, and I'm going to expand upon this a lot more in the Archon live stream, is how we can build our own custom Archon workflows. Because yes, there are a lot of very powerful workflows that we have as the defaults for you, like some of that I already showed you in this video, but there's always going to be an opportunity to build your own, something very custom to you, or if you want to take another framework like GSD or B-MAD and bring it into Archon, or take a strategy like beads for memory, like anything you want to do, you can build it as a custom workflow for yourself. And you can take advantage of this workflow builder workflow that we have. I know it's very meta, but all you have to do is open up Claude Code in the Archon repository and just say, use the workflow builder workflow to help me make an Archon workflow. If I had a dime for every time I said workflow in this video, I would be a rich man. But that is all you have to say, and it's going to automatically load the Archon skill, and then ask you questions. It'll give you a chance to obviously describe the workflow you want to build, and then it'll run this full builder afterwards to create the YAML structure, and then you will immediately be able to run the workflow on any code base. So, for example, something fun that I thought I would try right now for this video is creating an Archon workflow that essentially takes the idea from beads. So, beads, it's pretty cool. It's an open source repo that gives persistent structured memory for coding agents. And so, I want to essentially build the idea that we have here into an Archon workflow. So, I'm just going to copy this repo, paste it in here, go into my speech-to-text tool and say, I want to build an Archon workflow that incorporates beads. Basically, just taking all the ideas from beads in a simple sense. So, I want you to search through this repository, understand how it works, and then build this as an Archon workflow so that we can use beads to create any new feature on any code base. So, there we go. I'll send that off, and it's going to do some research and thinking for me, and then obviously invoke this workflow to create the final YAML. So, I'll show you that when it's done. And there we go. We have our full workflow created. It starts with exploration, then it decomposes the feature request into individual tasks. and We implement them in a loop with progress tracking, validating everything at the end as well. So, taking a lot of ideas from Beads and building a full Archon harness around it. So cool. We can also view the full workflow within the user interface. We're working on a workflow builder, so it's like N8N but for AI coding. Super cool. A ton of awesome things that we're actively working on right now with Archon. It's just in beta. Probably going to be some bugs that you'll find when you try it. A lot of new things that we're going to be adding over the next couple of months here. It is my biggest passion project. And so, please give it a shot. I think you'll really like it. And also, I would love to see you at the Archon livestream this Saturday at 9:00 a.m. Central Time. Going to be diving a lot deeper into building workflows and running them and showing you all these really cool features in Archon. So, I hope to see you there. Otherwise, if you appreciate this video and you're looking forward to more things on Archon and AI coding and agent harnesses, I would really appreciate a like and a subscribe. And with that, I will see you in the next video.

---

## Timestamped Segments

**[0:00]** Finally, after months and months of hard

**[0:02]** work behind the scenes, I am unveiling

**[0:04]** the new Archon, a massive overhaul of

**[0:08]** the AI command center that I was working

**[0:10]** on last year. It is now the first

**[0:12]** open-source harness builder for AI

**[0:14]** coding. So, similar vision, but a very

**[0:17]** different and powerful use case.

**[0:20]** Harnesses are the future. It's the layer

**[0:22]** on top of your coding agents that

**[0:25]** orchestrates the different sessions.

**[0:26]** It's what makes AI coding deterministic

**[0:29]** and repeatable. We'll talk about what

**[0:30]** that means. And now with Archon, you can

**[0:33]** build your own custom harnesses very

**[0:36]** easily. No matter how you work with AI

**[0:38]** coding agents right now, you can take

**[0:41]** that process and bundle it up into an

**[0:43]** Archon workflow that you can run across

**[0:45]** all your code bases, even handling

**[0:48]** different tasks in parallel. Archon

**[0:50]** handles all of the messy logic behind

**[0:52]** the scenes to make that possible. And so

**[0:55]** in this video, I want to talk about what

**[0:57]** makes Archon so powerful. I want to show

**[0:59]** you how to get started with it and even

**[1:01]** give you some inspiration for the kinds

**[1:03]** of things you can do with it. It's a

**[1:04]** very powerful tool. It's actually hard

**[1:06]** for me to explain everything in just one

**[1:08]** video, but a lot more content coming on

**[1:10]** Archon soon as well.

**[1:13]** So, the main idea with Archon is you can

**[1:15]** encode your development process as a

**[1:17]** workflow, no matter what it is. And so I

**[1:20]** will link to this repo in the

**[1:21]** description. I highly encourage you to

**[1:23]** try Archon today. It's very easy to get

**[1:25]** up and running. I'll show you that in a

**[1:27]** little bit. But I have an example here

**[1:29]** at the top of the readme for what an

**[1:31]** Archon workflow looks like. And so every

**[1:34]** single workflow is just a combination of

**[1:36]** nodes, where a node is either a prompt

**[1:38]** that we send into a coding agent

**[1:39]** session, or it is a deterministic

**[1:42]** command that we want to invoke. Because

**[1:44]** sometimes we want to enforce certain

**[1:45]** things to happen, like context creation

**[1:48]** or validation, that we don't want to

**[1:49]** leave up to the coding agent cuz it

**[1:51]** might forget to do so. So we want to

**[1:52]** plan, implement tasks in a loop, run the

**[1:55]** tests, have it do a review, even adding

**[1:58]** in a human approval gate so we can

**[1:59]** address our feedback. We can build

**[2:01]** ourselves into Archon workflows if we

**[2:03]** want as well, and then ending with a

**[2:04]** pull request. And Archon comes with a

**[2:06]** skill that I'll cover with you in a bit

**[2:08]** as well. So we just say like use Archon

**[2:10]** to build this feature, it knows

**[2:12]** automatically the workflow to use, it'll

**[2:14]** invoke it for us, and we have the logs

**[2:16]** so we can monitor the workflow along the

**[2:18]** way.

**[2:19]** Archon also comes with a ton of

**[2:21]** pre-packaged workflows that will

**[2:23]** immediately level up your agentic coding

**[2:25]** workflow. Fixing GitHub issues, creating

**[2:27]** pull requests from ideas. We have pull

**[2:30]** request validation and review commands,

**[2:32]** even one to help you create full PRDs

**[2:34]** with human in the loop. So, ton of

**[2:36]** things for you to use and very easy to

**[2:38]** create your own custom workflows as

**[2:40]** well. We're going to cover all of that

**[2:42]** in this video. I'm going to give you

**[2:43]** enough of a starting point for you to

**[2:45]** dive right into Archon. And then if you

**[2:47]** want a super deep dive, I'm also doing a

**[2:49]** live stream this Saturday, 9:00 a.m.

**[2:51]** Central Time. So come be a part of this

**[2:53]** as well cuz we're going to get really

**[2:54]** deep into building workflows and running

**[2:56]** them in parallel, doing a lot of fancy

**[2:58]** things. But for now, I want to give you

**[3:00]** a good overview of Archon, why it's

**[3:02]** important, where we're heading with

**[3:04]** agent harnesses, and then we'll get into

**[3:06]** the setup guide. So I want to start by

**[3:08]** talking about the evolution that we've

**[3:10]** seen that has brought us to harness

**[3:12]** engineering. So prompt engineering, that

**[3:14]** was all the rage back in 2022 through

**[3:17]** 2024. It was all about how can we prompt

**[3:19]** LLMs to get the single best output? And

**[3:23]** then that evolved into context

**[3:24]** engineering, which is all about how can

**[3:26]** we curate the perfect context for a

**[3:28]** single agent so it can handle a larger

**[3:31]** set of work. We give it all the context

**[3:33]** it needs and nothing more.

**[3:35]** And now that has evolved into harness

**[3:37]** engineering, where we're dealing with

**[3:38]** many different coding agent sessions,

**[3:41]** all tying that together through a

**[3:43]** harness. And so up until this point,

**[3:45]** everything we've done here is dealing

**[3:46]** with a single LLM or a single agent. Now

**[3:49]** we are stringing coding agent sessions

**[3:51]** together to handle much larger sets of

**[3:54]** work. And so maybe you've heard of the

**[3:56]** Ralph loop before, or Anthropic has

**[3:59]** built a couple open-source harnesses.

**[4:00]** There are a lot of harnesses out there,

**[4:02]** but the problem is that they're not

**[4:03]** custom to you. Maybe it's a good

**[4:06]** starting point or helpful to create a

**[4:07]** proof of concept, but what Archon

**[4:09]** unlocks for you is being able to create

**[4:11]** your own custom harness wrapping up your

**[4:14]** own software development life cycle. And

**[4:16]** harnesses are a big deal. It's the

**[4:18]** tooling, the prompting, chaining

**[4:20]** different coding agents together,

**[4:22]** everything to elevate the capabilities

**[4:23]** of a single large language model. And

**[4:25]** this is really important right now cuz

**[4:27]** Claude is about to release Mythos, but

**[4:29]** it's more enterprise use. Like us

**[4:31]** consumers, there's no way we're going to

**[4:32]** be able to afford using Mythos for

**[4:34]** everything. But what we can do is build

**[4:36]** a harness around Opus to make it more

**[4:38]** powerful than Mythos by itself. And this

**[4:41]** is proven. There have been studies that

**[4:42]** have been done that if we take a large

**[4:44]** language model and we just use it to

**[4:46]** create some code, the PR acceptance rate

**[4:48]** is only 6.7%. But if we create a

**[4:51]** harness, like the Ralph loop but

**[4:53]** probably more custom and better, we can

**[4:55]** get even as high as like almost 70% for

**[4:57]** a PR acceptance. And I don't want to get

**[4:59]** like super deep into the study here, but

**[5:01]** the point is we can elevate models a

**[5:03]** drastic amount by creating a harness

**[5:06]** where we build in validation, we build

**[5:08]** in a special kind of context curation.

**[5:11]** And that's exactly what Stripe did with

**[5:12]** Stripe Minion. So I covered this on my

**[5:14]** channel already actually, but Stripe,

**[5:16]** they ship 1,300 AI only generated pull

**[5:20]** requests every single week. And they did

**[5:23]** this by building their AI coding

**[5:26]** workflow, their context curation, their

**[5:28]** validation, enforcing that at different

**[5:30]** steps of the way in their workflow. So

**[5:32]** they actually built something kind of

**[5:33]** like Archon, but it's not open-source,

**[5:35]** right? You can't use it like you can use

**[5:37]** Archon. And with the Claude code source

**[5:40]** code leak, we found that even Anthropic

**[5:42]** is leaning a lot more into harnesses

**[5:44]** with agent teams and features they're

**[5:45]** building around sub-agents. 40% of their

**[5:47]** code base is just code for harnesses

**[5:50]** right now. And so that just is a signal

**[5:52]** for how much it's a big deal right now.

**[5:54]** And Archon, it wraps above Claude code

**[5:57]** and Codex. So the old Archon was more of

**[6:00]** a tool built into coding agents. That's

**[6:02]** kind of why it became irrelevant because

**[6:04]** these coding agents, they built all that

**[6:05]** themselves for rag and task management.

**[6:07]** You know what I'm talking about if

**[6:08]** you've used the old Archon. But now the

**[6:10]** new Archon, it sits above the coding

**[6:12]** agents and it orchestrates them.

**[6:15]** So the problem is before, you're dealing

**[6:17]** with AI shepherding. Like yes, you have

**[6:19]** your skills and commands and you're

**[6:21]** running workflows there, but you still

**[6:23]** have your entire process where you're

**[6:25]** running different skills and different

**[6:26]** commands, and you have to remember what

**[6:28]** comes next, and you have to kick off the

**[6:30]** code review after the implementation.

**[6:32]** But now your entire process, you can

**[6:34]** bundle as an Archon workflow. Define

**[6:36]** once, run forever, reusable across

**[6:38]** projects. You also get to pick where

**[6:41]** you're injecting context. Like maybe you

**[6:43]** have a skill that you only need during

**[6:45]** the validation step, or you have an MCP

**[6:47]** server that you only want during

**[6:48]** planning. We have that level of control

**[6:50]** per node with Archon. And kind of like

**[6:54]** the example I gave in the readme, here's

**[6:56]** an example of going from plan all the

**[6:58]** way to open a pull request. This is the

**[7:00]** kind of thing you can build with Archon.

**[7:02]** And I think you really see here how

**[7:03]** we're building in reliability through

**[7:05]** deterministic steps, enforcing

**[7:08]** validation at certain steps of the way,

**[7:10]** and human approvals.

**[7:12]** So we have our plan here. We can even

**[7:14]** like build this into a loop where we

**[7:16]** have the agent create the plan and then

**[7:17]** we give feedback, and we go in a loop

**[7:19]** until we go to the coding step. And we

**[7:21]** do that in a fresh context window. You

**[7:23]** always want to do your planning and

**[7:25]** implementation in different coding

**[7:27]** sessions to remove bias. And then after

**[7:29]** the coding, we go into the tests, and we

**[7:32]** run this every single time. Again, we

**[7:33]** don't want to rely on the coding agent

**[7:35]** to remember to do the tests all the

**[7:37]** time. And then we retry and have it fix

**[7:39]** issues if they come up. Otherwise, we go

**[7:41]** to the final human approval gate. When

**[7:43]** things look good, we then open the pull

**[7:46]** request. Just one example of how you can

**[7:48]** take I mean this is a more basic example

**[7:50]** of what your agentic coding workflow

**[7:52]** might look like, but there's going to be

**[7:54]** different things depending on if you're

**[7:55]** fixing bugs or refactoring or building a

**[7:57]** new feature. All of those things you can

**[7:58]** build into Archon. And the big secret

**[8:01]** here is the hybrid secret. This is what

**[8:03]** makes Stripe Minion so powerful. There

**[8:06]** are certain steps of the workflow that

**[8:07]** we don't want the coding agent to

**[8:09]** decide. Like sometimes we want to curate

**[8:11]** context in a specific way, or run our

**[8:14]** tests in a specific way. We have nodes

**[8:16]** for that that we can build into Archon

**[8:18]** workflows. But then of course, most of

**[8:20]** the workflow is still going to be driven

**[8:22]** by our commands and skills, just sending

**[8:25]** prompts into our coding agents. We have

**[8:28]** of course support for all of that so you

**[8:29]** can take your existing commands and

**[8:31]** skills, everything, and build it right

**[8:33]** into Archon. So I hope you can see why

**[8:36]** this is so powerful, building these

**[8:38]** kinds of harnesses for yourself. And so

**[8:40]** with that, I now want to get into the

**[8:42]** guide for you, how you can get Archon up

**[8:44]** and running using these workflows in

**[8:46]** less than 5 minutes. Now, installing

**[8:48]** Archon is actually incredibly easy

**[8:51]** because we can use our coding agent to

**[8:53]** guide us through the entire process. All

**[8:56]** you have to do is clone the repository,

**[8:59]** open up Claude, and then ask it to set

**[9:01]** up Archon. Because it will automatically

**[9:03]** load in a skill that we have in the code

**[9:05]** base here that guides you through the

**[9:07]** entire process. And I'll do this right

**[9:08]** now with you just to show how easy it

**[9:10]** is. We can do this in less than 5

**[9:12]** minutes. So I'll take this first command

**[9:13]** here to clone the repository, and then

**[9:16]** obviously we want to open up our coding

**[9:17]** agent in this repo so we can load the

**[9:19]** skill. So we'll change our directory,

**[9:21]** and then we'll open up Claude. There we

**[9:23]** go. So now in Claude code, I just say

**[9:25]** set up Archon. That is all you have to

**[9:27]** do. And take a look at this. We'll see

**[9:28]** in just a second, it'll load the Archon

**[9:30]** skill, and then it'll kick off this

**[9:32]** process where it'll ask us all the

**[9:34]** questions we need in order to help us

**[9:35]** get our credentials set up and then

**[9:37]** validate that Archon is working on our

**[9:39]** machine. So first, Archon is going to

**[9:41]** check to make sure that we have the

**[9:43]** prerequisites in place, including Bun,

**[9:45]** and it'll install it if we don't have it

**[9:47]** already. Then it asks what repository we

**[9:50]** first want to use Archon with. So it's

**[9:52]** important that you add in your own

**[9:54]** project, not the Archon repo, because we

**[9:56]** want to use the Archon workflows on a

**[9:59]** target repository. And don't worry, it's

**[10:01]** super easy to add more projects into

**[10:03]** Archon after. And so, just for this

**[10:06]** demonstration here, I have a reg YouTube

**[10:08]** chat application that I'm going to be

**[10:10]** running some Archon workflows in. And

**[10:12]** so, I have the path to this repo cloned

**[10:14]** locally copied here. And so, I'll just

**[10:16]** go to option number two, specify a local

**[10:18]** path. And so, then it's going to ask me,

**[10:20]** you know, like what is the path? Please

**[10:21]** paste it. So, I'll paste it in here. And

**[10:23]** then, it'll register this as our first

**[10:26]** Archon registered project. And then,

**[10:28]** going forward, we can add any project

**[10:30]** into Archon by just running a workflow

**[10:32]** there for the first time or right within

**[10:34]** the web UI. I'll show you that in a

**[10:35]** little bit. Then, it asks what platforms

**[10:37]** do I want to set up. So, the CLI is

**[10:40]** included by default. You can run Archon

**[10:42]** through the CLI, ask your coding agent

**[10:44]** to do so. But, we can also run in

**[10:47]** GitHub. And then, we could run through

**[10:48]** Telegram, through Slack. I'm actually

**[10:50]** going to set up quite a few of these

**[10:51]** right now. There are a lot of different

**[10:53]** interfaces to interact with Archon.

**[10:55]** Then, I will submit my answer here.

**[10:57]** There we go. And now, it's going to walk

**[10:59]** us through setting up the credentials

**[11:01]** for each one of our platforms. Then,

**[11:03]** after Archon installs the global CLI,

**[11:06]** like it did right here, then it's going

**[11:08]** to walk us through a setup wizard to set

**[11:10]** our credentials for any other platforms

**[11:12]** we chose, like GitHub or Slack. We need

**[11:14]** to do this in a different window,

**[11:15]** because we don't want to send our API

**[11:17]** keys directly into Claude Code. So, it's

**[11:19]** going to spin up another terminal

**[11:20]** process for us to enter our keys, not

**[11:23]** going to a coding agent. And so, it

**[11:26]** should spin up the wizard automatically

**[11:27]** and bring up another terminal

**[11:29]** automatically. But, for certain

**[11:31]** operating systems, or if you're trying

**[11:32]** to run Archon in a VPS, you will

**[11:35]** probably have to open up a new session

**[11:36]** yourself. So, you just open up a new

**[11:38]** terminal, and you run the Archon setup

**[11:41]** command. So, Archon is now a globally

**[11:43]** recognized command, because we installed

**[11:45]** the CLI. So, this is going to work

**[11:46]** automatically. In my case, I'm just

**[11:48]** going to go back to the terminal that it

**[11:50]** popped up for me automatically. So, we

**[11:52]** can pick our database. SQLite by

**[11:54]** default, this is the easiest. Or, you

**[11:56]** can set up Postgres if you like. So, I'm

**[11:58]** going to do SQLite. And then, it asks

**[12:00]** which AI coding assistant you want to

**[12:02]** use. So, right now, we mostly support

**[12:04]** Claude. We're almost done with Codex

**[12:06]** support, and then we want to add in

**[12:07]** other coding assistants later, like the

**[12:10]** Pi Agent SDK and Open Code. And so, I'll

**[12:13]** go with Claude right here. So, I'll just

**[12:15]** do space to select, and then enter to

**[12:17]** confirm. And then, how do I want to

**[12:19]** authenticate with Claude? Well, I just

**[12:20]** want to use my Anthropic subscription.

**[12:22]** We are allowed to use our Anthropic

**[12:24]** subscription as long as it's an

**[12:26]** application running locally using the

**[12:27]** Claude Agent SDK. And that is the case

**[12:30]** for Archon. So, I'm going to use my

**[12:31]** global auth.

**[12:33]** Just going to hit enter here. What

**[12:35]** platforms do I want to connect? So, I'll

**[12:36]** just select GitHub, Telegram, and Slack.

**[12:38]** So, then it'll ask me for the

**[12:39]** credentials for those. And this is where

**[12:42]** it's going to guide you through getting

**[12:44]** the API keys for each of them. So, for

**[12:46]** each one of the platforms you select,

**[12:48]** there are instructions to walk you

**[12:50]** through getting your keys for each

**[12:52]** application. So, I'm just going to go

**[12:54]** through this quickly. You can take your

**[12:55]** time to get the keys yourself on your

**[12:58]** own.

**[13:08]** All right. Then, after you set all of

**[13:09]** your credentials, it's going to ask, do

**[13:10]** you want to install the Archon skill in

**[13:12]** your project? And I would highly

**[13:14]** recommend doing this, because then, if

**[13:17]** we open up Claude Code in our other code

**[13:19]** base, we can use the Archon CLI to kick

**[13:22]** off workflows automatically. Cuz then,

**[13:23]** if we have Claude open there, we can

**[13:24]** just say, "Use the Archon CLI to invoke

**[13:27]** whatever workflow to handle a pull

**[13:28]** request or an issue or something." And

**[13:30]** it'll know right away to load the skill,

**[13:32]** and it'll know exactly how to use the

**[13:34]** Archon CLI. Again, it's important for

**[13:36]** any CLI to have a skill paired with it,

**[13:38]** so that our coding agent knows how to

**[13:40]** use it. So, I will bring this over. It

**[13:42]** asks for the path. So, I'm just going to

**[13:44]** take the path that I copied earlier for

**[13:46]** the repo. Just paste it in right here,

**[13:48]** so it knows where to copy it. And then,

**[13:50]** it'll ask if you want a non-default docs

**[13:52]** directory. If you have other

**[13:53]** documentation you want to load into

**[13:54]** Archon, probably don't worry about that

**[13:56]** right now. That's something that we're

**[13:57]** working on currently. So, I'll do no

**[13:58]** there. And there we go. Our setup is

**[14:01]** complete. And so, what we do here is we

**[14:03]** actually go back to the first session

**[14:05]** where we first said, "Set up Archon."

**[14:08]** And it tells you this here. So, it says,

**[14:10]** you know, come back here, complete the

**[14:11]** configuration there, let me know when

**[14:12]** you are done. So, I'm I'll just say,

**[14:14]** "Done." And then, what it's going to do

**[14:16]** now, that I've set all my credentials,

**[14:18]** is verify that everything is working.

**[14:20]** So, it'll test the connections. It'll

**[14:22]** even test running a workflow through the

**[14:24]** Archon CLI. I'll come back once that is

**[14:26]** done. All right. So, it confirms that

**[14:28]** our credentials are good to go, without

**[14:30]** actually reading them, of course. Then,

**[14:32]** we list out all of the default Archon

**[14:34]** workflows to make sure they're

**[14:35]** available. Those are all the workflows

**[14:36]** that we have bundled ready for you to

**[14:38]** use immediately to fix GitHub issues,

**[14:40]** run a rough loop, create a PRD. There is

**[14:42]** a lot of value that we have built into

**[14:44]** this right away. And then, it of course

**[14:47]** runs a workflow as well. So, it runs our

**[14:49]** basic Archon assist one just to make

**[14:51]** sure that the Archon CLI is functioning,

**[14:53]** and we're ready to use it on any

**[14:55]** repository that we want.

**[14:57]** And then, it gives us a summary at the

**[14:59]** end. And look at how easy it is for us

**[15:01]** to just start using Archon right now.

**[15:03]** So, we just open up Claude Code in our

**[15:06]** target repository. You can really do

**[15:08]** this in any repo you want, because

**[15:10]** remember, when we run the Archon CLI in

**[15:12]** a repo for the first time, it

**[15:13]** automatically registers it with Archon.

**[15:15]** So, we just copy over the Archon skill

**[15:17]** into whatever repo, launch Claude there,

**[15:20]** and then we can just say, "Use Archon

**[15:21]** to, for example, fix this issue number."

**[15:24]** Or, "Help me create a PRD." Whatever

**[15:25]** workflow you want to use, and you can

**[15:27]** build your own, like I'll show you in a

**[15:29]** little bit. So, because I chose my reg

**[15:31]** YouTube chat application as my

**[15:33]** onboarding repo, I copied over the

**[15:36]** Archon skill. So, it knows how to use

**[15:38]** the Archon CLI when I ask it to. And so,

**[15:41]** I'm going to open up Claude Code right

**[15:43]** within this repository, and we are

**[15:45]** already ready to use a workflow. And so,

**[15:48]** I'm going to use Archon to help me fix a

**[15:50]** GitHub issue. And so, going into the

**[15:52]** issue list for my repo, you can see

**[15:54]** there is quite a few options that I have

**[15:56]** to work with here. Well, let's say I

**[15:57]** just want to deal with issue number one.

**[15:59]** And so, all I have to do is say, "Use

**[16:02]** Archon to fix issue number one in

**[16:05]** GitHub." That is it. I don't have to

**[16:07]** provide any more context, because it'll

**[16:08]** know to load the Archon skill,

**[16:11]** find the right workflow for the job, and

**[16:14]** then invoke it. And then, our Claude

**[16:16]** Code can just monitor it in the

**[16:18]** background. So, there we go. It used the

**[16:20]** GitHub CLI to view the issue to get

**[16:22]** context, loaded the Archon skill, and it

**[16:24]** decided, "Okay, I should use the Archon

**[16:26]** fix GitHub issue workflow." It's one of

**[16:28]** the defaults that we have bundled. It is

**[16:30]** a very powerful workflow, by the way,

**[16:32]** because it does full investigation,

**[16:34]** fixing, and validation before it creates

**[16:36]** the pull request. And that is the end

**[16:37]** result is we'll have a pull request that

**[16:39]** has the final implementation from the

**[16:42]** Archon workflow. So, we can see right

**[16:44]** here that in Claude Code, it is running

**[16:46]** as a background process. So, we can

**[16:48]** track the logs here. We can always ask

**[16:50]** Claude Code to give us an update for how

**[16:52]** the workflow is running, or we can view

**[16:54]** the workflow in the web UI as it is

**[16:57]** running. Okay. So, right here, we are

**[16:59]** focusing on using the CLI to run an

**[17:02]** Archon workflow. That is the most

**[17:03]** convenient way. But, we also have a web

**[17:06]** interface. If you want to more visualize

**[17:08]** what's happening with your workflows, we

**[17:09]** can also view the logs for the workflows

**[17:11]** more easily that we run through the CLI.

**[17:14]** So, I'm going to go back to the terminal

**[17:16]** where I had the Archon repository open

**[17:19]** with Claude Code. So, all I have to do,

**[17:21]** if I want to start the back end and

**[17:23]** front end of Archon, is I just have to

**[17:25]** ask my coding agent to do so. It is that

**[17:27]** easy. So, I can say, "Spin up the front

**[17:29]** end and back end of Archon." And it's

**[17:31]** going to, based on the review,

**[17:32]** understand the commands to run, and then

**[17:34]** get everything running for us as

**[17:35]** background processes. And so, take a

**[17:37]** look at this. If I go into the browser

**[17:40]** and go to port 5178, right? Cuz that's

**[17:42]** where it says it's running right now, I

**[17:44]** can see my conversations. I can see the

**[17:46]** workflows that are currently active. So,

**[17:48]** if I go into the dashboard here, I can

**[17:49]** see that it's using the Archon fix

**[17:51]** GitHub issue workflow. I can view the

**[17:53]** logs for it to see what is currently

**[17:56]** happening. So, this is the node that we

**[17:58]** just completed. Now, we're currently

**[18:00]** investigating the issue. So, we started

**[18:02]** with web research, then now we're

**[18:04]** investigating. We can see all the tool

**[18:06]** calls. So, all the logs from Claude

**[18:07]** Code, if you want to dig into all the

**[18:09]** individual actions that it's doing as

**[18:11]** it's going through this Archon workflow.

**[18:13]** And so, every single one of the nodes

**[18:15]** here is either a deterministic action,

**[18:17]** like a bash command, or it's a session

**[18:20]** with Claude Code. And again, in our

**[18:22]** Archon workflows, we can determine when

**[18:24]** we go from node to node, do we want to

**[18:25]** start a brand new session with Claude

**[18:27]** Code or continue the conversation? We

**[18:29]** have a lot of flexibility for token

**[18:31]** management, making sure we keep our

**[18:33]** context lean when we're dealing with our

**[18:36]** coding agents. One of the big things

**[18:37]** that Archon gives us that we were

**[18:38]** missing before. All right. And while we

**[18:40]** wait for this workflow to finish, it's

**[18:42]** going to create a pull request at the

**[18:45]** end, I want to show you what it actually

**[18:46]** looks like in the YAML. Cuz remember,

**[18:48]** all of the workflows in Archon are

**[18:51]** simply defined as YAML files. It is so

**[18:53]** easy to improve the existing ones that

**[18:55]** we have in Archon, and even create your

**[18:58]** own. That's one of the last things I'll

**[18:59]** show you in this video. And so, within

**[19:01]** the .archon folder in the Archon

**[19:03]** repository, we have all of the default

**[19:06]** workflows. These are also bundled into

**[19:08]** the CLI. So, when you run the CLI from

**[19:10]** any other repository, it'll

**[19:12]** automatically have access to these. So,

**[19:14]** take a look at this. We have all of

**[19:16]** these different workflows. The one that

**[19:18]** we're running right now is Archon fix

**[19:20]** GitHub issue. And [snorts] so, we have a

**[19:22]** description for the workflow. And this

**[19:24]** is important, because this is just like

**[19:26]** Claude Code's skills, where the

**[19:28]** description is what we first give to

**[19:30]** Claude Code. Like, "Hey, here's a

**[19:32]** workflow from Archon that you want to

**[19:34]** use when the user is specifically asking

**[19:36]** for you to fix a GitHub issue." Right?

**[19:39]** We don't want to load the entire

**[19:41]** workflow into context for the coding

**[19:43]** agent. That's way too much. It only

**[19:45]** needs this brief description up front.

**[19:46]** So, it uses this to determine if it

**[19:49]** should analyze and run this entire

**[19:51]** workflow. We can define the provider up

**[19:54]** front. Again, we're supporting more in

**[19:55]** the near future, the default model used

**[19:58]** for each of the nodes, and then we have

**[20:00]** the list of nodes. This is the

**[20:01]** step-by-step that we're going through.

**[20:03]** So, exactly what I have defined in the

**[20:05]** YAML document, we can see right here in

**[20:07]** the web UI. We see the full execution,

**[20:09]** all the different nodes that we have,

**[20:10]** the different branches and decisions

**[20:12]** that can be made. All of this is a

**[20:14]** direct visualization of what we have in

**[20:16]** the YAML right here.

**[20:18]** So, for this workflow specifically, we

**[20:20]** are going to first extract the issue

**[20:22]** number. So, based on the prompt that is

**[20:24]** fed into this workflow, it's kind of

**[20:26]** like running a sub agent in Claude Code,

**[20:28]** we're going to grab the issue number,

**[20:31]** and then we're going to classify the

**[20:33]** issue. Is this a bug that needs to be

**[20:34]** fixed or a feature that we need to

**[20:36]** build? Because that's going to determine

**[20:38]** what comes next, right? Do we have to

**[20:39]** investigate the issue or plan for a new

**[20:42]** feature? And we have the prompt here

**[20:44]** that we're sending into the model for

**[20:46]** this step specifically. And one of the

**[20:49]** most powerful things, I know that token

**[20:51]** consumption is a big deal right now,

**[20:52]** especially because of rate limits with

**[20:54]** Anthropic. One of the powerful things we

**[20:55]** can do with Archon is specify the model

**[20:58]** we want to use for the individual nodes.

**[21:01]** So, certain nodes, like classification,

**[21:03]** they don't need a lot of reasoning

**[21:05]** power. So, we can make it a lot more

**[21:07]** token efficient, a lot cheaper by just

**[21:09]** using Haiku for our model.

**[21:11]** And then we go into the research phase.

**[21:13]** In this one, we're just going to use the

**[21:14]** default model. So, we don't specify it

**[21:16]** here, it just means that it'll use the

**[21:17]** default model of Sonnet. And we don't

**[21:20]** have the prompt in line, we're actually

**[21:21]** using a command. And so, for every

**[21:23]** single workflow that's in this folder,

**[21:25]** and then the commands are sort of like

**[21:27]** the extensions that we run in certain

**[21:29]** nodes. So, for example, we have the

**[21:32]** Archon web research command right here.

**[21:34]** So, I'll just open this really quickly.

**[21:36]** It's just like commands or skills in

**[21:38]** Claude, where it's just a longer prompt

**[21:40]** that we're going to invoke for this node

**[21:43]** specifically. So, we do our web

**[21:44]** research, and then we investigate if it

**[21:46]** is a bug or we plan if it is a feature

**[21:49]** request. That's the the first decision

**[21:51]** that we can see right here. So, in the

**[21:53]** case of the workflow we just invoked, it

**[21:55]** went down the path of investigation

**[21:57]** because looking at our issue here, it's

**[22:00]** definitely a problem that we're

**[22:01]** addressing, not a new feature that we

**[22:04]** are adding.

**[22:05]** And so, not like I need to go like in

**[22:07]** super deep detail for every single node

**[22:10]** here, but I'm just trying to show you

**[22:11]** the idea of like how we can take a

**[22:13]** pretty comprehensive workflow and turn

**[22:15]** it into this single process that we run

**[22:18]** with Archon. It's more than just writing

**[22:20]** some code. It's doing classification,

**[22:21]** it's doing investigation or planning,

**[22:23]** it's implementing, validating, and then

**[22:25]** creating the pull request at the end as

**[22:28]** well, and even doing further review

**[22:29]** after that point. And so, we have a lot

**[22:32]** more faith by the time this workflow

**[22:34]** finishes that the pull request is really

**[22:36]** ready for us to review and merge. And

**[22:39]** yes, it takes a good number of tokens to

**[22:41]** go through this many steps, but that's

**[22:43]** why we lean on being able to specify the

**[22:46]** model at each step of the way. We're

**[22:48]** able to use Haiku for a lot of this

**[22:50]** here. So, we're just kind of giving more

**[22:52]** of a set of guidance around the coding

**[22:54]** agent. That's why we're calling it a

**[22:56]** harness, right? Like, this is sort of a

**[22:58]** harness wrapping many different Claude

**[23:00]** Code sessions to work together to fix a

**[23:02]** GitHub issue. And there are so many

**[23:04]** amazing workflows that we have available

**[23:06]** for you that you can use out of the box,

**[23:08]** and then anything that's not here, you

**[23:10]** can just create by yourself. So, we have

**[23:13]** the adversarial dev harness as an Archon

**[23:15]** workflow. I showed this in a live stream

**[23:17]** that I'll link to right here. We have a

**[23:20]** comprehensive PR review workflow.

**[23:23]** We have one to help you create issues.

**[23:25]** So, like investigating a problem

**[23:26]** creating a GitHub issue, idea to PR,

**[23:29]** this is a very comprehensive one. We

**[23:31]** have one with human in the loop. We

**[23:32]** actually have human in the loop with

**[23:34]** Archon. So, we can pause at any given

**[23:36]** node to ask for your input. So, we have

**[23:38]** this interactive PRD, where it'll have

**[23:41]** you sort of ideate with a coding agent

**[23:42]** to create that initial spec for a new

**[23:45]** application you want to create. We have

**[23:47]** the Ralph loop built as an Archon

**[23:50]** workflow.

**[23:51]** Uh man, there's just so many things that

**[23:52]** are here already. We even have an Archon

**[23:55]** workflow to help you build more

**[23:57]** workflows. We'll use this in just a

**[23:59]** second here. So, yeah, literally like no

**[24:01]** matter what you want to do with your AI

**[24:03]** coding assistants, it doesn't matter how

**[24:05]** many coding agent sessions you need, you

**[24:08]** can bundle it together into an Archon

**[24:10]** workflow, adding in reliability through

**[24:12]** deterministic nodes, like you always

**[24:14]** want to run validation at some point, or

**[24:16]** you always want to curate context in

**[24:17]** this way. The sky's the limit for what

**[24:20]** you can build with Archon. All right, so

**[24:22]** I'm just going to keep showing you some

**[24:23]** really cool ways to use Archon. I'm

**[24:25]** going to keep using the GitHub issue fix

**[24:27]** workflow because that is my most used,

**[24:29]** but there are so many amazing workflows

**[24:30]** you can use. And by the way, you can

**[24:32]** just ask it in the web UI here, what

**[24:34]** projects and workflows do you have? And

**[24:38]** so, the Archon agent in the UI is

**[24:41]** actually kind of special. It has all of

**[24:43]** the context around Archon, like our

**[24:45]** registered projects and workflows

**[24:47]** injected in at the start of the

**[24:48]** conversation. And by the way, in the web

**[24:51]** UI here, you can just click add project

**[24:52]** to give a GitHub URL or local path if

**[24:55]** you want to register more. So, right

**[24:56]** now, this is my only registered project,

**[24:58]** as you can see from the drop-down here.

**[25:00]** And then here are all of the available

**[25:01]** workflows, which this will also include

**[25:03]** any that you build on top yourself, but

**[25:05]** these are all of the default ones

**[25:07]** shipped with Archon. So, now, for

**[25:08]** example, I can say fix GitHub issue, and

**[25:12]** then if I go to the issue list here,

**[25:14]** we're currently handling this one and

**[25:15]** the other screen. So, we'll just do

**[25:17]** number three. So, I'll do number three

**[25:19]** for uh the rag YouTube chat project. So,

**[25:23]** we don't even have to call out the exact

**[25:25]** repo name, it can reason based on what

**[25:27]** we said and what context it has loaded

**[25:30]** to know which workflow to kick off. So,

**[25:32]** take a look at that. It invoked the

**[25:33]** Archon fix GitHub issue workflow

**[25:36]** specifically in our rag YouTube chat

**[25:38]** application. So, it does all of the

**[25:40]** routing for us from the web UI. And we

**[25:43]** can go into the logs, the beautiful

**[25:44]** screen. This is the exact same view we

**[25:47]** saw earlier, but this time we actually

**[25:49]** invoked it from the web UI. Very cool.

**[25:52]** And another really powerful thing I want

**[25:53]** to show you really quickly is that we

**[25:55]** can invoke a ton of workflows in

**[25:57]** parallel. And so, for example, I'm back

**[26:00]** here with Claude open in my rag YouTube

**[26:02]** chat application, and I can just say use

**[26:05]** Archon to fix GitHub issues 5 7 8 9 10

**[26:08]** and 11. So, the last six in that list

**[26:10]** there that we haven't touched yet, I

**[26:12]** just want to rip through all of these at

**[26:13]** the exact same time. And so, we can

**[26:17]** invoke Archon directly from our project,

**[26:19]** or we can have Claude Code open within

**[26:22]** our Archon repository, and we can point

**[26:24]** it to any code base if we just give it

**[26:26]** the path. And remember, it will

**[26:27]** automatically register Archon at that

**[26:29]** point. So, now it used the Archon CLI.

**[26:31]** Boom, look at that. Six times in a row,

**[26:33]** all of them are running as background

**[26:35]** processes, so we can see that right

**[26:37]** here, and we can continue to have it

**[26:39]** monitor for us, or even just ask us

**[26:41]** along the way, like, you know, like give

**[26:43]** us a status update. So, we can view it

**[26:45]** in the user interface. Like, if I wanted

**[26:47]** to go back to the UI now, we can see

**[26:49]** that we have all of these workflows

**[26:51]** currently running, or we can just have

**[26:52]** Claude Code constantly check for us. We

**[26:54]** could, for example, use the slash loop

**[26:56]** command in Claude Code to say, you know,

**[26:57]** like every 10 minutes, check on the

**[26:59]** workflows and restart if there's a

**[27:01]** failure or something, which there

**[27:02]** usually isn't. But yeah, so all six

**[27:04]** workflows are running, progressing

**[27:06]** through the early DAG stages. So, yeah,

**[27:08]** most of them are on the classify step

**[27:09]** right now, figuring out is the issue a

**[27:11]** new feature or a problem that has to be

**[27:13]** addressed. Super cool. All right, so I'm

**[27:16]** back, and we have the pull requests for

**[27:18]** all of our Archon workflow runs. So, we

**[27:21]** can see them all complete in the web UI

**[27:23]** as well. We can click into the logs just

**[27:24]** see what happened every step of the way.

**[27:26]** And of course, we can go see our final

**[27:28]** result. Going to the repository for the

**[27:30]** first time here, I'll click on pull

**[27:31]** requests, and boom, there we go. We have

**[27:33]** eight new open pull requests handling

**[27:36]** each of the issues that we handled with

**[27:38]** an Archon workflow. All right, the last

**[27:40]** thing that I want to show you really

**[27:42]** quickly here, and I'm going to expand

**[27:43]** upon this a lot more in the Archon live

**[27:45]** stream, is how we can build our own

**[27:47]** custom Archon workflows. Because yes,

**[27:50]** there are a lot of very powerful

**[27:51]** workflows that we have as the defaults

**[27:53]** for you, like some of that I already

**[27:55]** showed you in this video, but there's

**[27:57]** always going to be an opportunity to

**[27:58]** build your own, something very custom to

**[28:00]** you, or if you want to take another

**[28:01]** framework like GSD or B-MAD and bring it

**[28:04]** into Archon, or take a strategy like

**[28:07]** beads for memory, like anything you want

**[28:09]** to do, you can build it as a custom

**[28:10]** workflow for yourself. And you can take

**[28:13]** advantage of this workflow builder

**[28:15]** workflow that we have. I know it's very

**[28:16]** meta, but all you have to do is open up

**[28:18]** Claude Code in the Archon repository and

**[28:21]** just say, use the workflow builder

**[28:23]** workflow

**[28:25]** to help me make an Archon workflow. If I

**[28:28]** had a dime for every time I said

**[28:29]** workflow in this video, I would be a

**[28:31]** rich man. But that is all you have to

**[28:32]** say, and it's going to automatically

**[28:35]** load the Archon skill, and then ask you

**[28:37]** questions. It'll give you a chance to

**[28:39]** obviously describe the workflow you want

**[28:41]** to build, and then it'll run this full

**[28:43]** builder afterwards to create the YAML

**[28:46]** structure, and then you will immediately

**[28:48]** be able to run the workflow on any code

**[28:50]** base. So, for example, something fun

**[28:52]** that I thought I would try right now for

**[28:53]** this video is creating an Archon

**[28:55]** workflow that essentially takes the idea

**[28:57]** from beads. So, beads, it's pretty cool.

**[28:59]** It's an open source repo that gives

**[29:01]** persistent structured memory for coding

**[29:03]** agents. And so, I want to essentially

**[29:05]** build the idea that we have here into an

**[29:08]** Archon workflow. So, I'm just going to

**[29:10]** copy this repo, paste it in here, go

**[29:13]** into my speech-to-text tool and say,

**[29:15]** I want to build an Archon workflow that

**[29:18]** incorporates beads. Basically, just

**[29:20]** taking all the ideas from beads in a

**[29:21]** simple sense. So, I want you to search

**[29:23]** through this repository, understand how

**[29:25]** it works, and then build this as an

**[29:27]** Archon workflow so that we can use beads

**[29:30]** to create any new feature on any code

**[29:32]** base. So, there we go. I'll send that

**[29:34]** off, and it's going to do some research

**[29:36]** and thinking for me, and then obviously

**[29:38]** invoke this workflow to create the final

**[29:40]** YAML. So, I'll show you that when it's

**[29:42]** done. And there we go. We have our full

**[29:44]** workflow created. It starts with

**[29:45]** exploration, then it decomposes the

**[29:47]** feature request into individual tasks.

**[29:49]** and We implement them in a loop with

**[29:51]** progress tracking, validating everything

**[29:54]** at the end as well. So, taking a lot of

**[29:56]** ideas from Beads and building a full

**[29:58]** Archon harness around it. So cool. We

**[30:00]** can also view the full workflow within

**[30:03]** the user interface. We're working on a

**[30:04]** workflow builder, so it's like N8N but

**[30:07]** for AI coding. Super cool. A ton of

**[30:09]** awesome things that we're actively

**[30:10]** working on right now with Archon. It's

**[30:12]** just in beta. Probably going to be some

**[30:14]** bugs that you'll find when you try it. A

**[30:15]** lot of new things that we're going to be

**[30:17]** adding over the next couple of months

**[30:18]** here. It is my biggest passion project.

**[30:21]** And so, please give it a shot. I think

**[30:23]** you'll really like it. And also, I would

**[30:24]** love to see you at the Archon livestream

**[30:27]** this Saturday at 9:00 a.m. Central Time.

**[30:29]** Going to be diving a lot deeper into

**[30:30]** building workflows and running them and

**[30:32]** showing you all these really cool

**[30:33]** features in Archon. So, I hope to see

**[30:35]** you there. Otherwise, if you appreciate

**[30:37]** this video and you're looking forward to

**[30:39]** more things on Archon and AI coding and

**[30:41]** agent harnesses, I would really

**[30:42]** appreciate a like and a subscribe. And

**[30:44]** with that, I will see you in the next

**[30:46]** video.
