# Transcript: L8 Principal's Agentic Engineering Workflow

**URL:** https://www.youtube.com/watch?v=iQyg-KypKAA
**Segments:** 1608
**Channel:** Kun Chen
**Duration:** 45:46
**Uploaded:** 2026-06-20

---

## Full Text

Hi everyone. Welcome to this video and this will be a full walkthrough of my agent engineering workflow. My name is Kun. I was previously an late principal engineer, worked at meta, Microsoft, and assassin on many large scale systems like the Bing search engine, windows, and Facebook games. In the recent couple of years, I have been building frontier coding agents at Atlassian and helped many engineering teams figure out how to use them effectively. and I have been building heavily with agents myself and shipping 40 to 50 almost every day, sometimes more. And these are all well tested and shipped production. not those Minecraft demos. You see people wipe code on social media. I have shaped my workflow to be both highly productive and enjoyable. Many people recently asked me what it looks like, be honest, I did debate a lot with myself whether I should make this video a paid course because it does have that level of value, but ultimately I decided to just share it here with everyone because I want to stay focused on building products as my main business. you can see this is a bit of a long video, because I'm going to walk through many fundamental concepts of agent engineering that's not only show you how I do it, but also the why and how things really work under the hood. These are not gimmicks that look cool but can't actually be used for real work. These are all real workflows that professionals like myself use to get real work done. By the end of this video, I want you to feel like a captain that can sail a large ship with a crew of agents working for you, and do so in a stress free and satisfying way. Largely speaking, we will be walking through these chapters. We'll start with assembling our ship, where I will introduce the core setup. We will then talk through how we recruit and ramp up our crewmates with the right usage of memory and skills. I will then demonstrate how we work with a single crewmate effectively. Then we'll upgrade to working with multiple crewmates all at the same time. And lastly, we will recruit a first mate that manages a lot of the overhead for us so we can stay focused on the big picture. As a captain, the very first level is to gather our gears and build our ship. Now, as we get into my workflow, something that's going to be really hard to miss is that I do almost everything in my terminal. I know there are a lot of people who will tell you that the graphical user interface is better. It allows richer interactions and better visuals, but I think by the end of this video, I might just be able to convince you that terminal is not quite that yet. I use the terminal mostly for two very real reasons. One is to allow my hands to almost never have to leave the keyboard. This is actually a much bigger deal than most people think, because when your hands stay on the keyboard, you stay in the flow. But if you have to move your hand to the mouse every couple of seconds, it breaks the flow and forces your brain to contact switch. I know there are some guy apps that also have great key points that allow you to do most things with the keyboard as well, but that's just not the primary interaction paradigm for guy apps, And it's hard to build the discipline of hands on keyboard when every once in a while you still have to use the mouse terminal apps. On the other hand, are all designed for the keyboard, so there is no reason for your hands to move anywhere else. The other very important factor that drives me to use the terminal is that I can keep the exact same workflow everywhere, even on my phone. but if you really don't like the terminal, that's okay too. I designed this video to be more about the fundamental concepts behind agent engineering rather than the mechanics. So most of the things that I talk about should be applicable to GUI based workflows as well. Now. Since we are looking at a terminal here, let me share what it is I'm using this beautiful, clean and elegant terminal emulator you are looking at here is called Western. Western is a highly performance terminal emulator built by a guy named West. It's got 26 k GitHub stars and has existed for many years. I like it mostly for two reasons. One is that it's truly cross-platform. It's pretty much the only terminal emulator I can find that can work on windows exactly the same way it works on Mac and Linux. Right now I mostly only work on Mac, but it was a big lifesaver when I was working for Microsoft and was forced to use windows for work. The other reason is that it's highly customizable. You can write Lua scripts to configure pretty much everything. Here. Let me show you my config in my dot files. It's all in this file called Western dot lua. It's a lower script. So it's not just static values. You can actually set conditions and write various kind of logic to make your config very dynamic and flexible. If I change some settings here, let's say I change the color scheme to chalk. You will see that it does a hot reload instantly, which is super handy. But I still like my rose pine moon, so let's come back to it. I can't use anything else. Inside of West term, I run something called tmux. It's short for terminal multiplexer. If you haven't come across this yet, it's probably easiest to just show you what this does. so I'm typing this command here to start a session. Now I'm inside of t max. You can see not much is different except for that. There is a bar at the top showing some information, and I still get a shell where I can type commands, But now I can split my terminal into multiple panes, as many of them as I like. This is super useful because I can spin up an agent in one pain and spin up an editor in another, and still have a pain to myself so I can just run commands. I can also spin up multiple tabs and they are also called windows in. This is very useful for running multiple agent sessions in parallel. The other cool thing is that tmux sessions are persistent in the server. So if I use a keyboard shortcut here to detach from tmux, you can see I'm back in the normal shell without the status bar at the top. But if I type the same command to launch tmux again, I get back to the exact same state I was in So I can continue my work here. What's even more useful is that I can connect to this same session from another device, like my laptop or my phone. that's a real game changer. That's very hard to replicate without this terminal centric workflow. If you just install tmux by default, it doesn't have the same experience while showing here, like the tab bar and the metadata. You will probably need to do a bit of configuration and customize it. Let me show you my team config. Here it is. Most of these settings are key points that I have been using for many years, and built into my muscle memory. Some of these are for styling and various kind of behaviors. There are many YouTube videos that go into more details about tmux configuration. So I'm not going to go down the rabbit hole here. For now. You just need to know that you are likely want to spend some time configuring your t mux for it. Look good and work well for This text editor here is Nuvem. It's basically the modern version of vim. It's my favorite text editor. If you are not familiar with vim yet, it's an editor whose main purpose is to keep your hands on the keyboard. So if you watch my keystrokes here, I can move the cursor up and down, left and right with keys. I can also scroll up or scroll down. If I have to make edits, I can go into insert mode and start to type anything I like. There are a ton of keyboard shortcuts for doing everything you need. For example, let's say I want to delete the current line. I can just type dd and it's gone. I can undo it by typing you. And if you look at the left hand side I have relative line numbers. This line number 238 is the current line number. And the line above shows one, which means it's one line above the current line and the lines below as well. So let's say I want to jump to the line that says set environment. That's 11 lines above the current line. So I can just type 11 k. And I'm here. So once you have enough muscle memory, you can just navigate around much more quickly than using a mouse. I also have a bunch of plugins that help me get around in as well. And I have key points for all of them. Like space S allows me to search or grep for the code base, so I can just type rows and it will find all the occurrences of rows in the current code base. I can type space F to find files by their names, like if I type flake I'll get to the flake file immediately. Working with them has a learning curve for sure. But once you get used to it, it just feels really, really good. Whenever I'm in, I'm just flying like a bird and it's awesome okay? I have to stop here before this turns into a vim tutorial. You can find a lot of great YouTube videos that will help you get started on them and become a master. Maybe one last tip for me is just how to exit. Here you go. All right. Our ship is ready to sail, but we have no crewmates yet. Where? The captain. We can't do everything by ourselves. We need to bring in agents as our crewmates. I use four different agent harnesses regularly. There is cloud, which is cloud code, which is basically the only practical choice if you are using the subscription from anthropic. Generally speaking, though, it's a pretty good harness. I think it has the most sensible default experience out of the box. It's also got a pretty rich feature set. The downside is that sometimes it's a little bit buggy, and it's not as customizable as some of the other options. The next one I use a lot is Codex COI. It's written in rust, and you can feel it's a little bit smoother than cloud code when you use it. It's also open source, so if you run into some problems, You can often just have Codex inspect its own source code and figure out a workaround by itself. It's a bit lacking in terms of bells and whistles, and it's also not very customizable. And then there is the Pi coding agent. And this whole philosophy is to be minimal and highly extensible. It's great if you don't want any bloat and you'd like to tinker around and kind of make it your own. and lastly, there is open code. I like it a lot. It's got a battery smooth t UI, And it's got good integration with pretty much every model you can find. It's also got a more complete out of the box feature set than Pi. So if you want to use an agent harness that is model agnostic and one that you can just grab from the shelf and just go. Open code is a pretty good choice. For the rest of this video though. I'm going to use cloud code because I know many people are already familiar with it, but I have been very strict about making my workflow agent agnostic because the landscape is changing very, very fast. who knows which model or agents will be the best performing one next month? Right. So everything I show here in the video is agent agnostic and should be applicable regardless of which model or harness you use. The problem with this crewmates is that they are fresh recruits, and they have no idea how we run our ship or how we like to work. We need a proper onboarding process to ramp them up. We will do this mostly through two ways memory files and skills. There are few types of memory files, global memory files, and project level memory files. The global memory file for cloud code is at this location, and every other agent uses the other standard location here. So what I do is that I use this command Which made MD a symbolic link to MD. So they both exist, but under the hood they point to the same file. Here's the content of my actual global memory file. You can see it's pretty minimal. There is only 27 lines. Because everything in this file gets loaded into the system prompt of every single agent session across all our projects. If we have too much content in this file, it will silently use a lot of our tokens. I mostly write down my personal preferences here, like never use em. Somehow AI models are trained to use em by default instead of a plain dash. So now whenever I see em, I just feel like it's robotic. And I don't like that when I need the agent to write something for me. Like PR descriptions. Oh, and this is a good one. When making technical decisions, don't give too much weight to development cost. Here is something interesting that you may not know. Let me show you. If we ask a frontier model to estimate the development cost of a project, let's say I want to build a 3D first person shooting game that I can play locally with AI enemies. How long do you think that will take? Let's see what cloud will say. Okay, here it is. See, the estimate is in days and weeks and months. But if we ask the agents to actually build it now, I can guarantee it will come back with a playable version in just a few minutes. Because I have done this so many times. This mismatch is happening because the models were trained from human data, and that is what a typical human developer would give as the estimate. AI doesn't seem to know it can code much faster than humans yet. When AI is making technical decisions, it's implicitly assuming the development cost for some of the options are much higher than they actually are. This biases the model to choose cheap solutions that are often low quality, not scalable, or hard to maintain. So I have this rule here to correct that bias. I also said when doing bug fixes always starts with reproducing the bug in an end to end setting as closely aligned with how an end user would experience it as possible. AI models today by default like to write unit tests, which are often not sufficient and not really covering the product behaviors we want to guard. I found that leaning into end to end testing is a lot more reliable. Besides these preferences, I also have some interesting stuff opinions, which is super useful. That's a slightly different topic though, so I won't go into too much detail here, but I do have a blog post explaining how that works, which I'll link here in case you're interested. Besides the global memory file, each project can also have a project level memory file. Let me show you one example here by going into this project called High Bit. This is an AI Twitter app I have been working on. The project level memory file is typically stored as cloud or agents, depending on which agent you use. I do the same thing here with a symbolic link. So the same file is shared for both cloud and other agents. This one we are looking at here is a little bit verbose. I would say I will probably clean this up after this, but let me show you on a high level what I put into this file. It has some context on what this project is, how the repo is laid out, some terminology, how some of the most important components work, and how to do end to end testing, and some conventions at the bottom. This file is a lot more verbose than the global memory file, because this is basically the collective learning of all the agent sessions in this project. The way I built this file is not by writing everything by hand, but rather that every time I saw the agent doing something wrong, I would correct it and ask it to remember to not make the same mistake again by storing the learning into this memory file. So over time, our crewmates working on this project get smarter and more experienced. You don't need any fancy memory system to do that. This markdown file is all it takes over time. It does tend to get more and more bloated though. One way I reduce the size of this file is by moving some conditional information that is not always needed into a skill. For example, the end to end testing instruction here is only needed if the agent is making changes, right? So if I just ask the agent a question, this whole section is totally useless and would be wasting tokens. The way to improve efficiency here is by converting this kind of conditionally useful information from the memory file into skills. I typically just ask the agent to do this. Here, let me do it alive. I will say let's extract the end to end testing instructions junctions in our agents and file into a project level skill. Cloud already knew how to do this, what skills mean and how to create them, but other agent harnesses may not understand how to do that out of the box. To teach your agent how to create skills, you can install a skill called Skill Creator which which was written by anthropic. You can do that by running this command. This NPC's skills thing is a call from Vercel that is very handy. It's basically my main tool for installing and managing skills. It supports pretty much any agent. Once this skill is installed, your agent will be able to follow the rules and create new skills for you moving forward. cloud has done its work. Let's look at what cloud created for us. It basically removed a large chunk of the content from our agents MD file and move that into this this skill file. This is a good thing about skills is that it's designed for progressive disclosure, which means when your agent starts, it only loads this tiny description field from your skills into the system prompt to know what these skills do, and only when it actually decides that it needs to use a certain skill. It will then reads the rest of this file. This allows you to store a lot of the knowledge about how to do various kinds of things without blowing up your system. Prompt and memory file with a ton of contents that uses your tokens for every single request, whether the request actually needs those skills or not. One thing I do want you to know about skills is that you should generally avoid installing random skills from the internet. Even the ones that have a lot of GitHub stars. First of all, these skills can instruct your agents to run pretty much anything on your machine. This is a very risky thing to do, because the agent can lick your API keys or even credentials to your bank account to untrusted third parties without you knowing. even if we put aside the security problem, some of the skills actually degrade your agents performance. Look at this repo here called Android Skills, which has 177,000 GitHub stars. That's like massive. So it must be really good, right? I actually evaluated a skill in this repo with Program Bench, which tests the agent's ability to build programs end to end. And the result shows that by using this skill, the agent will use 5% more tokens while making the results worse. And if you look closely, this skill is not even written by André Karpathy himself. I'm not here to criticize the author of this repo, though. I'm mainly saying that being popular is not the same as actually being good. A lot of the skills being widely shared today have not been rigorously evaluated, and are typically just some random guy who found something that worked for themselves and and somehow got it to go viral. Their GitHub stars only tell you how popular they are and not whether they are actually helpful. So as a general rule of thumb, I recommend that you do not install any skill from the internet that claims to magically make your agent perform better, but hasn't published anything rigorous that proves its claim. All right. Now that we have memory files and skills to help ramp up crewmates, it's finally time to actually start working with the crewmates and set sail. The first thing about working with the crewmate is how you talk to them. I have pretty much completely moved to voice input now, So. Instead of typing, I will just say, explain this repo in a concise way and give me a recap of what the recent press have been working on. This is just so easy. There is an actual paper from Stanford that seriously compared the efficiency. And basically talking is three times faster than typing. So this is a very big boost in productivity. I also want to show you something interesting here. If we go to the references of this paper look who's here. It's our guy Dario. What is the CEO of anthropic doing here? Apparently if we follow this link Dario was doing some speech recognition stuff back in 2016. Now we're using speech recognition technology to talk to cloud which is also created by Dario. What a small world. The voice input. We just did was actually transcribed locally using this app called Open Super Whisper. It's completely free and open source, which is what I think this type of software should be. It runs the whisper model locally on your machine and do the transcription. And the quality is like really, really good. So this is how I do most of my prompts. Now, the only case where I fall back to typing is when I need to give the agent a URL or a file path, or something like that. Trust me, you don't want to speak a URL out loud, whether it's by yourself or with other humans around. If we come back to this prompt and let the agent run, you will see that because we asked the agent to look at recent polls, it will need to call GitHub to fetch the data. This is an important thing to pay attention to, because agents rely on external tools like GitHub to do its tasks. The design of these external tools can greatly affect your agents performance. Take GitHub as an example. Many people use the GitHub MCP server for accessing GitHub. However, I ran this benchmark here that measured various kinds of ways to access GitHub For the exact same tasks using GitHub, MCP server will cost you to spend three times more on token cost, and more than double the latency compared to using the CLI. If you are using the GitHub MCP, you are pretty much wasting both time and money for no clear benefits. Now you can see there's this thing called axi, which has the lowest cost but highest success rate. So what is it? Let me show you. Axi is a set of design standards I authored after discovering the huge upside we can have by designing our tools to treat agents as a first class citizen and optimize for agent ergonomics. I created ten principles for how to make a tool highly efficient for agents. For example, using token efficient output format can save about 40% tokens compared to using JSON. And then I built a few axes with Besides the GitHub axis I showed earlier, I also built Chrome dev tools actually, and benchmarked it against other various browser tools. And Here you can see the agents taking less turns and using less tokens to get the same tasks done with the ax. The main point here is when you give tools to your agents, do some research on their efficiency because they can greatly affect how much mileage you get out of your agents. If you want to use the axes I mentioned earlier, you can just go to this site called axis and find them in this catalog. You can just go to the repo and find instructions for how to start using them. Speaking of this catalog, there is something called lavish axi here. This is a very important tool in my setup. I pretty much rely on this tool for planning any kind of complex work. Let's do a real feature live and I'll show you how it works. Let me first launch high bit to show you what I'm trying to work on here. Hybrid is an AI Twitter I'm building for kids. I'll just create a test profile here. You can see here at the top I have these two buttons, what I can do and my progress. They are showing very similar content right now which is a problem. So and also the UI is not very exciting or fun. So let me go back and talk to cloud. I'll still use voice input here. I'll just say I'd like to consolidate the what I can do and my progress buttons, because their functionality is very similar and I'd like to revamp the experience there to be something more fun and exciting, like in an achievement system. Come up with some options and let's discuss. Don't use lavish. Okay, the reason I said don't use lavish is that I wanted to show you what's the default workflow today. Looks like for many people. And then I'm going to show you the difference lavish makes. Because I already have leverage skills installed. My cloud will automatically use lavish for this type of question, which is why I had to tell it not to do that right now. Okay, cloud is doing this work. Now. Cloud has come back with a response. Sometimes it will use its plan mode, or sometimes I will ask you to write down the plan in the markdown file, but it's more or less the same. It's a wall of text I now have to read through. It's not very easy to understand what what each option is actually going to look like, and if I'm not happy with some parts of it, I can't very easily tell cloud which parts I'm talking about. I can select a piece of text in the plan and say, this is wrong. Now let's try the exact same prompt with lavish. Here it goes again. I actually don't have to say use lavish because the agent already has the lavish skill that tells the agent for this type of planning it should establish, for demo purpose, I just wanted to be explicit. Cloud would roughly do the same things to figure out the options, except at the end it would not print out that wall of text. Again, it will launch the browser and show me this page. Now look at this. This is the lavish editor. The reason I named it lavish is that it's richer than a rich editor. I almost named it filthy rich editor, but that's just not the best sounding name. Lavish editor basically instructed the agent to create an HTML artifact to visualize what we need to discuss. It always uses the same design system as the current project being worked on, so this is consistent with how the app actually looks. This makes it very easy to reveal concepts and prototypes. See the option is laid out here. This is so much easier to understand than the huge wall of text we were looking at in the terminal, right? I can also annotate and make comments on specific parts of the artifacts to give feedback to the agent. This is something that's really hard to do with the wall of text, or a markdown file And at the bottom, there are things for me to decide on, and I can just click on these options to make the decisions. I just sent this feedback back to the agents inside of lavish without even having to go back to the terminal. Honestly, I can never go back to reading text in the terminal anymore. This is just way too much more efficient. Now the agent has made updates to the and I feel happy about this, so I'll just tell the agent to start building. Start building and we'll end the session. We can then go back to the terminal now and see. The agent will start to work on the implementation, because we already clarified all the requirements in the planning phase. I typically don't need to interfere at all during this implementation phase. I only come back to this when the agent has done. And when the agent says it's done, that's actually when things get really tricky. This is where a lot of people will spin up their editor and start reviewing the diff. The problem is, AI writes code so fast, and if every piece of code requires your review, then you are creating a big bottleneck on yourself because you can only review so many every day. Your velocity will be hard capped by it. And even more importantly, reviewing diff is just not fun. No one says I became an engineer because I love reviewing diffs all day. My advice here is that in order to really scale ourselves with AI, we have to think of ourselves more as an engineering manager or engineering director. Your directors most likely don't review any place yet. They can influence the quality of their team's software by creating good culture and processes, and rely on the team to carry them out. That's what we should do with AI. What I do here, when the agent says the work is done, is not to start reviewing the dips or start manually testing the changes. That's too much overhead. On myself, I sense the change into a pipeline I built called No Mistakes. No mistakes is also free and open source. It orchestrates your agent to execute a series of steps that takes this first pass code all the way through to a clean PR. It would first create a branch if one doesn't exist yet, and then create a commit and then take it through a pipeline in an isolated work tree, so nothing during the validation would affect your current repo. It would first understand your real intent behind the change by analyzing your agent session, then rebase the change on top of the latest main branch on remote origin and resolve merge conflicts up front, then starts an adversarial review in its own fresh context window. This is where most problems get caught, and obvious problems will get self corrected, but ambiguous ones that have product implications will be escalated to us humans for a decision after review. It also tries to test the change end to end against the original intent, and this step will actually record evidence that proves the change is working that we can. Then later on look at to gain more confidence. It will then do a documentation pass of updating all relevant documentation to reflect the latest change. And also finally, make sure there is no linting problems before pushing the branch to remote and raise a PR. The no mistakes pipeline will also keep babysitting the PR until it's merged, because during the PR phase, we can still have merge conflicts that come in, or CI pipeline failures that are very annoying as well, with no mistakes doing the babysitting. We don't have to waste our own time at all. Another way to trigger no mistakes is as a skill. I can just type no mistakes in the agent and it will do the same pipeline as This may seem very slow, but in practice I never stare at this screen. I would go spin up other tasks. I come back only when no mistake says all checks passed that's when I go to the PR and apply my judgment. Here's the PR from the change we just did. We can see here it summarized the original intent. What's changed, how it's tested, and what happened during the normal stakes pipeline. We can click to see the evidence from its testing to know whether it's really done what we asked for, depending on what the change is, the evidence could be a screenshot like this a video demo, a log file, or something else. It's designed to give you the most direct way to see the change working as you intended. We can also see that the pipeline discovers some problems and fix them before raising the PR. This is a good time to audit whether these changes are actually what we need. If anything doesn't look right, we can go back to the agent and ask for more changes before merging this PR. This risk assessment here is also very useful. I basically look at this to decide how much time I should spend on reviewing this change in more detail. For low risk changes, I don't really look at the diff at all Because I have validated time and time again for low risk changes. Any problem I could catch is very likely already caught by the pipeline only more risky changes are worth my This is how I scale up the volume of code changes I do every day through a large crew of agents, without losing control on quality. One thing we are starting to see now is that the place where I spend time is towards the beginning and the end of the task. At the beginning I would spend time in lavish to plan the requirements more clearly. At the end I would come in and hold a bar on quality. All these parts in the middle is done by AI, which frees me up to spin up other tasks. This is a core aspect of how I work, and you can see the more time I can free up in the middle, the more work I can go do in parallel. So an interesting question now is how do we get the agents to work for longer and longer in the middle? That depends on us giving them more and more complex tasks that take longer to complete. But more complex tasks are often not as easy for our agents to complete autonomously. An extreme version of this is when I go to bed, I sleep for 7 to 8 hours every night. How do I keep the agents busy for eight hours? This is where I say good night. Have fun. It's another free and open source tool I built specifically for long running tasks. It's becoming quite popular. It's that simple to use. Just give it an objective and it will keep going until it meets some stop condition you defined. Let me show you a real example that I often do. This is again in the hybrid repo I will run. Good night. Have fun and give a prompt. Pretend you are a seven year old kid and use the high bit app end to end. Don't mind the profile creation step which is designed for parents in the rest of the app. Try to do different things and find the first usability problem that will confuse you as a kid, or stop you from knowing how to proceed. If you find a problem, stop and fix it, then rinse and repeat. Here he goes. Good night. Have fun. Is now running in the loop. To execute on what I just asked for. I can monitor token usage here or how many iterations have been done. The iterations will be showing up as the moons in this row, and I can see how many commits have been made as well. Or I can just go to bed knowing the agents won't stop until there is no more problem to be found. When I wake up, I can reveal a list of commits made on this new branch and decide which ones I want. I typically use goodnight. Have fun for improving on some verifiable objectives or objectives, where I trust the agent to have the reasonable judgment over, like the one we just did. Verifiable objectives are more like reducing page load time, improving end to end test coverage or like Android hypothesis auto research. Keep experimenting different hypotheses to improve on the metric. These are all well suited for a long running loop. To tackle the recently introduced slash goal command in Codex and Cloud code can also do something similar, good night. Have fun still gives me a better experience. Because I can set a token cap or iteration cap or stop condition more precisely, whereas in Cloud Code and Codex, if I set a goal before I go to bed, I might wake up realizing my weekly quota is all Good night. Have fun. Solved a very important problem, which is to keep the agents running for a long time. So when the agents are running, I'm freed up to do more things. This is when we level up and start working with multiple crewmates in parallel. So let's spin up another tab in teams and get more work started. Now here's the problem. In this directory I already have. Good night. Have fun running. So if I spin up another agent working in the same directory, they will step on each other's toes and cause conflicts. The default solution here is git work tree. For those of you who aren't familiar with it, a guitar work tree is basically creating a clone of your report directory. I can create one by typing git work tree add and give a path here. Now we have to think about a name. This is when you waste five minutes and eventually give up and just say hi. Bit two. Now we have a work tree and we can navigate to it. So let's go find it. It's in high bit two. This is a separate directory on the file system. So we can have an agent doing anything here. And it won't conflict with good night to have fun, which is running in the original report directory. The problem with work trees is that we now have something to maintain in our head. I need to remember. Oh, I have hybrid two here. Next time I come into this hybrid two directory I would wonder what was I doing in this work tree last time? Is there still an agent running or is it All of that has to exist in my head, and there is no way I'm going to remember all that. So this work tree basically becomes a debt. To get rid of it. I need to run this remove command. Remove. This is just a lot of overhead. My solution to that is another tool I built called Treehouse. It's very simple. I just come into this repo and I run Treehouse. It would drop me into a fresh work tree where I can start doing whatever I want. I can keep spinning up more and more of this work trees by running Treehouse again. And if I want, I can see a list of all the work trees by typing Treehouse status. So I can see which ones are being used versus not. When I'm done, I can just close this tab and Treehouse knows that I'm done, so it will free up that work tree for future use. Next time I ask for work tree, it will try to reuse one of the idol work trees instead of creating a brand new So let's start some real work. I have a bunch of user feedback from my son's last round of playtesting, so let me use this first worksheet we created and launch cloud, and I will say, I remember it's hard for the kid to realize they can press and hold the voice input button to talk. By default they just click it and then they will see a popover. Maybe in the popover, we add a label that tells them they can also press and hold and I'll enter. Then I'll spin up a new tab Treehouse Cloud, and this time I will say the Image attachment dropdown menu should have an action that takes a screenshot of the current app and use that as the attachment. All right, one more tab. Treehouse cloud. Our agent status bar right above the chat input is not always showing bot activity. Look into what happened there and make sure when any bots are in progress, it always displays something that reflects the latest activity. Boom! We now have three sessions running in parallel. Now I can keep going because none of these sessions will need my attention anytime soon, especially if I tell them to run. No mistakes after implementation. I know whether they need me by looking at the top status bar, and I can switch between the tabs using keyboard shortcuts like this. That's very important for managing a lot of parallel sessions efficiently. That said, after doing this for a while, you will discover that juggling between all these sessions, it's quite exhausting. The constant context switch and having to remind yourself what each session was even doing just doesn't feel like an ideal end game experience. So I kept pushing the boundary on this and I discovered that I needed a first mate, someone I can talk to as a captain that will carry out all my directions and manage all the crewmates for me so I can focus on the big picture like where should we go next? not playing whack a mole with this increasingly high number of crewmates, this is how I level up and truly become a captain. My First mate is another free and open source project and it's very new. The way to use it is by just cloning it. And then I can run an agent in this repository. Now I just talk to it and ask it to work on any projects I like. Let's say I'd like to work on lavish access, GitHub, Axi and Chrome dev tools. Actually They are all GitHub projects I own. first mate is starting up and the first time we run it it will do some setup and ask for some preferences, but it's also just talking to it, which is pretty easy. you might wonder why is the transcription so good? Because it's recognizing this project names. Let me show you. Open Silver Whisper actually supports this customization through a system prompt. So what we can do here is in this model menu in the transcription menu there is an initial prompt. And we can put in some common vocabulary that we use into this system prompt. this prompt is what makes the transcription really good. First mate here is asking how strict I want to be with the code changes in this repos, and I want to select full gates to PR. This is basically going to be using no mistakes as the pipeline to validate its change and first task. Yeah, I'll describe it. Right now. A real thing I want to do is for all three projects, I'd like to add an update command on the CLI that will update their version to the latest on npm. And let's see what First Mate does. It realizes that this is not one task, but three parallel tasks, and it's now spinning up these tabs in timox, just like we be the scenes. It would also call tree House to create work trees, and then run an agent in that work tree to get the work done, and then it will run. No mistakes to validate the change and get the PR ready for us to review. Now you can see it's first made that it's doing the juggling. I don't need to worry about any of this now. I can just keep giving it more work. Hey first mate, let's also look at the most recent three open issues in lavish axillary and let's discuss which ones are actionable. Boom! First mate now is pulling the open issues from the repo while waiting for the three background agents working in parallel. All right, first mate said number 87 is cleanest. It's very actionable. And let me just see. What is this? Don't toggle in annotation mode. Okay. That's the clear bug. All right, first mate, let's address number 87. Look, now first mate is struggling a lot of tasks for me that I otherwise would have to manage by myself. Watching it context switch is actually an oddly satisfying experience, because I know that's what I would have to do otherwise. First mate is basically all my tools coming together as one cohesive workflow, and I have been really happy with it. It's been a pretty significant improvement to my overall experience working with agents. I highly recommend trying it out if you are still directly talking to every single agent session one by one, it will be a pretty massive upgrade. Something you start to notice after having a first mate. Is that because first mate took care of so many things for you, you start to run out of ideas for what to ask you to do. This is a good thing because it indicates the bottleneck is shifting, but it also means you, as the captain, needs to keep up. This requires a mindset shift of focusing more of your energy on understanding what matters by talking to your users, understanding the competitive landscape, and crafting a good treasure map that can lead your crew to a good direction. Once you started doing that, congratulations! You have successfully transitioned from a sailor into a great captain. All right. We have gone from not having a ship to being a captain that has a first mate and a big crew that sailed together. This is a pretty good time to wrap up this video. All my tools can be found on my GitHub and will be linked in the description below. They are all free and open source. I built them because I just want to see more people learning how to do a genetic engineering effectively and doing it in an enjoyable way, and that's what I hope you can get out of this video. I will continue to share more of my workflow and things I find useful on my channel, so don't forget to subscribe if you don't want to miss anything. Thank you for watching and see you next time!

---

## Timestamped Segments

**[0:00]** Hi everyone.

**[0:01]** Welcome to this video

**[0:02]** and this will be a full

**[0:03]** walkthrough of my agent

**[0:05]** engineering workflow.

**[0:06]** My name is Kun.

**[0:07]** I was previously an late

**[0:09]** principal engineer,

**[0:10]** worked at meta, Microsoft, and assassin

**[0:13]** on many large scale systems

**[0:14]** like the Bing search engine,

**[0:16]** windows, and Facebook games.

**[0:18]** In the recent couple of years,

**[0:19]** I have been building frontier

**[0:21]** coding agents at Atlassian

**[0:22]** and helped many engineering teams

**[0:24]** figure out how to use them effectively.

**[0:27]** and I have been building heavily

**[0:28]** with agents myself

**[0:29]** and shipping 40 to 50

**[0:32]** almost every day, sometimes more.

**[0:34]** And these are all well tested

**[0:36]** and shipped production.

**[0:37]** not those Minecraft demos.

**[0:38]** You see people wipe code on social media.

**[0:40]** I have shaped my workflow

**[0:42]** to be both highly

**[0:43]** productive and enjoyable.

**[0:45]** Many people recently asked me

**[0:47]** what it looks like,

**[0:48]** be honest,

**[0:48]** I did debate a lot with myself

**[0:51]** whether I should make this video

**[0:52]** a paid course

**[0:53]** because it does

**[0:54]** have that level of value,

**[0:56]** but ultimately

**[0:57]** I decided to just share it here

**[0:58]** with everyone

**[0:59]** because I want to stay focused

**[1:00]** on building products as my main business.

**[1:03]** you can see

**[1:03]** this is a bit of a long video,

**[1:05]** because I'm going to walk through

**[1:06]** many fundamental

**[1:07]** concepts of agent engineering

**[1:09]** that's not only show you how I do it,

**[1:11]** but also the why

**[1:13]** and how things really work

**[1:14]** under the hood.

**[1:15]** These are not gimmicks that look cool

**[1:17]** but can't actually be used for real work.

**[1:19]** These are all real workflows

**[1:21]** that professionals like myself

**[1:23]** use to get real work done.

**[1:25]** By the end of this video,

**[1:26]** I want you to feel like

**[1:27]** a captain

**[1:28]** that can sail a large ship

**[1:30]** with a crew of agents

**[1:31]** working for you,

**[1:32]** and do so

**[1:33]** in a stress free and satisfying way.

**[1:36]** Largely speaking,

**[1:37]** we will be walking

**[1:37]** through these chapters.

**[1:39]** We'll start with assembling our ship,

**[1:42]** where I will introduce the core setup.

**[1:45]** We will then talk through

**[1:46]** how we recruit and ramp up

**[1:48]** our crewmates

**[1:49]** with the right usage of memory

**[1:51]** and skills.

**[1:52]** I will then demonstrate

**[1:54]** how we work

**[1:54]** with a single crewmate effectively.

**[1:57]** Then we'll upgrade

**[1:58]** to working with multiple crewmates

**[2:00]** all at the same time.

**[2:01]** And lastly, we will recruit a first mate

**[2:04]** that manages

**[2:05]** a lot of the overhead for us

**[2:07]** so we can stay focused

**[2:08]** on the big picture.

**[2:09]** As a captain,

**[2:10]** the very first level

**[2:12]** is to gather our gears

**[2:13]** and build our ship.

**[2:14]** Now, as we get into my workflow,

**[2:17]** something that's going to be really hard

**[2:19]** to miss

**[2:19]** is that I do

**[2:20]** almost everything in my terminal.

**[2:22]** I know there are a lot of people

**[2:24]** who will tell you

**[2:25]** that the graphical user interface

**[2:26]** is better.

**[2:27]** It allows richer

**[2:28]** interactions and better visuals,

**[2:30]** but I think by the end of this video,

**[2:32]** I might just be able to convince you

**[2:34]** that terminal is not quite that yet.

**[2:37]** I use the terminal mostly

**[2:39]** for two very real reasons.

**[2:41]** One is to allow my hands to almost

**[2:43]** never have to leave the keyboard.

**[2:45]** This is actually a much bigger deal

**[2:47]** than most people think,

**[2:48]** because when your hands

**[2:50]** stay on the keyboard,

**[2:51]** you stay in the flow.

**[2:52]** But if you have to move your hand

**[2:55]** to the mouse every couple of seconds,

**[2:57]** it breaks the flow and forces

**[2:58]** your brain to contact switch.

**[3:01]** I know there are some guy apps

**[3:02]** that also have great key points

**[3:04]** that allow you to do most things

**[3:05]** with the keyboard as well,

**[3:07]** but that's just not

**[3:08]** the primary interaction

**[3:09]** paradigm for guy apps,

**[3:11]** And it's hard to build the discipline

**[3:13]** of hands on keyboard

**[3:15]** when every once in a while

**[3:16]** you still have to use the mouse

**[3:18]** terminal apps.

**[3:19]** On the other hand,

**[3:20]** are all designed for the keyboard,

**[3:22]** so there is no reason for your hands

**[3:24]** to move anywhere else.

**[3:25]** The other

**[3:26]** very important factor

**[3:27]** that drives me to use

**[3:28]** the terminal is that

**[3:29]** I can keep the exact same workflow

**[3:32]** everywhere, even on my phone.

**[3:33]** but if you really don't

**[3:35]** like the terminal, that's okay too.

**[3:37]** I designed this video to be more

**[3:38]** about the fundamental

**[3:40]** concepts behind

**[3:41]** agent engineering

**[3:42]** rather than the mechanics.

**[3:43]** So most of the things that I talk about

**[3:46]** should be applicable

**[3:47]** to GUI based workflows as well. Now.

**[3:50]** Since we are looking at a terminal here,

**[3:52]** let me share what it is

**[3:53]** I'm using this

**[3:55]** beautiful, clean and elegant

**[3:56]** terminal emulator

**[3:57]** you are looking at

**[3:58]** here is called Western.

**[4:01]** Western is a highly performance

**[4:03]** terminal emulator built by a guy

**[4:05]** named West.

**[4:06]** It's got 26

**[4:07]** k GitHub stars and has existed

**[4:09]** for many years.

**[4:10]** I like it mostly for two reasons.

**[4:13]** One is that it's truly cross-platform.

**[4:15]** It's pretty much

**[4:16]** the only terminal emulator I can find

**[4:18]** that can work on windows

**[4:20]** exactly the same way

**[4:21]** it works on Mac and Linux.

**[4:23]** Right now

**[4:23]** I mostly only work on Mac,

**[4:25]** but it was a big lifesaver

**[4:27]** when I was working for Microsoft

**[4:28]** and was forced to use windows for work.

**[4:32]** The other reason is that it's

**[4:33]** highly customizable.

**[4:34]** You can write Lua scripts to configure

**[4:36]** pretty much everything. Here.

**[4:38]** Let me show you my config in my dot

**[4:40]** files.

**[4:41]** It's all in this file

**[4:42]** called Western dot lua.

**[4:44]** It's a lower script.

**[4:45]** So it's not just static values.

**[4:47]** You can actually set conditions

**[4:48]** and write various

**[4:49]** kind of

**[4:50]** logic to make your config

**[4:51]** very dynamic and flexible.

**[4:54]** If I change some settings

**[4:55]** here, let's say

**[4:56]** I change the color scheme to chalk.

**[5:00]** You will see that

**[5:00]** it does a hot reload instantly,

**[5:02]** which is super handy.

**[5:04]** But I still like my rose pine moon,

**[5:06]** so let's come back to it.

**[5:07]** I can't use anything else.

**[5:09]** Inside of West

**[5:10]** term, I run something called tmux.

**[5:13]** It's short for terminal multiplexer.

**[5:16]** If you haven't come across this yet,

**[5:17]** it's probably easiest

**[5:18]** to just show you what this does.

**[5:20]** so I'm

**[5:20]** typing this command here

**[5:21]** to start a session.

**[5:24]** Now I'm inside of t max.

**[5:26]** You can see

**[5:26]** not much is different except for that.

**[5:29]** There is a bar at the top

**[5:30]** showing some information,

**[5:32]** and I still get a shell

**[5:34]** where I can type commands,

**[5:35]** But now I can split my terminal

**[5:37]** into multiple panes,

**[5:39]** as many of them as I like.

**[5:41]** This is super useful

**[5:42]** because I can spin up an agent

**[5:44]** in one pain and spin up

**[5:46]** an editor in another,

**[5:47]** and still have a pain to myself

**[5:50]** so I can just run commands.

**[5:52]** I can also spin up

**[5:53]** multiple tabs

**[5:54]** and they are also called windows in.

**[5:57]** This is very useful

**[5:58]** for running multiple

**[5:59]** agent sessions in parallel.

**[6:01]** The other cool thing is

**[6:02]** that tmux

**[6:03]** sessions are persistent in the server.

**[6:06]** So if I use a keyboard shortcut here

**[6:08]** to detach from tmux, you can see

**[6:11]** I'm back in the normal shell

**[6:12]** without the status bar at the top.

**[6:14]** But if I type the same command to launch

**[6:17]** tmux again,

**[6:19]** I get back to the exact same state

**[6:21]** I was in So I can continue my work here.

**[6:24]** What's even more useful

**[6:25]** is that I can connect

**[6:26]** to this same session

**[6:27]** from another device,

**[6:28]** like my laptop or my phone.

**[6:30]** that's a real game changer.

**[6:32]** That's very hard to replicate

**[6:34]** without this terminal centric workflow.

**[6:36]** If you just install tmux by default,

**[6:39]** it doesn't have the same experience

**[6:40]** while showing here,

**[6:42]** like the tab bar and the metadata.

**[6:44]** You will probably need to

**[6:45]** do a bit of configuration

**[6:46]** and customize it.

**[6:48]** Let me show you my team config.

**[6:52]** Here it is.

**[6:53]** Most of these settings are key points

**[6:55]** that I have been using

**[6:56]** for many years,

**[6:57]** and built into my muscle memory.

**[7:00]** Some of these are for styling and various

**[7:02]** kind of behaviors.

**[7:03]** There are many

**[7:04]** YouTube videos

**[7:05]** that go into more details

**[7:06]** about tmux configuration.

**[7:08]** So I'm not going to go down the rabbit

**[7:09]** hole here. For now.

**[7:11]** You just need to know

**[7:12]** that you are likely

**[7:13]** want to spend some time

**[7:15]** configuring your t mux for it.

**[7:17]** Look good and work

**[7:18]** well for This text editor here is Nuvem.

**[7:21]** It's basically the modern version of vim.

**[7:23]** It's my favorite text editor.

**[7:25]** If you are not familiar with vim yet,

**[7:27]** it's an editor

**[7:28]** whose main purpose

**[7:29]** is to keep your hands on the keyboard.

**[7:31]** So if you watch my keystrokes here,

**[7:34]** I can move the cursor

**[7:35]** up and down, left and right with keys.

**[7:38]** I can also scroll up or scroll down.

**[7:42]** If I have to make edits,

**[7:43]** I can go into insert

**[7:44]** mode and start to type anything I like.

**[7:48]** There are a ton of keyboard shortcuts

**[7:50]** for doing everything you need.

**[7:51]** For example,

**[7:52]** let's say

**[7:52]** I want to delete the current line.

**[7:54]** I can just type dd and it's gone.

**[7:56]** I can undo it by typing you.

**[7:59]** And if you look at the left hand side

**[8:01]** I have relative line numbers.

**[8:03]** This line number 238

**[8:06]** is the current line number.

**[8:07]** And the line above

**[8:09]** shows one,

**[8:09]** which means it's one line

**[8:11]** above the current line

**[8:12]** and the lines below as well.

**[8:14]** So let's say

**[8:15]** I want to jump to the line

**[8:16]** that says set environment.

**[8:19]** That's 11 lines above the current line.

**[8:21]** So I can just type 11 k.

**[8:23]** And I'm here.

**[8:24]** So once you have enough muscle memory,

**[8:27]** you can just navigate around

**[8:28]** much more quickly than using a mouse.

**[8:31]** I also have a bunch of plugins

**[8:32]** that help me get around in as well.

**[8:35]** And I have key points for all of them.

**[8:38]** Like space S

**[8:39]** allows me to search

**[8:40]** or grep for the code base,

**[8:41]** so I can just type rows

**[8:43]** and it will find all the occurrences

**[8:45]** of rows in the current code base.

**[8:48]** I can type space F

**[8:50]** to find files by their names,

**[8:51]** like if I type flake

**[8:53]** I'll get to the flake file immediately.

**[8:56]** Working with them

**[8:57]** has a learning curve for sure.

**[8:59]** But once you get used to it,

**[9:00]** it just feels really, really good.

**[9:03]** Whenever I'm

**[9:03]** in, I'm just flying like a bird

**[9:06]** and it's awesome okay?

**[9:07]** I have to stop here before

**[9:08]** this turns into a vim tutorial.

**[9:10]** You can find a lot of great

**[9:12]** YouTube videos

**[9:12]** that will help

**[9:13]** you get started on them

**[9:14]** and become a master.

**[9:16]** Maybe one last tip for me

**[9:18]** is just how to exit.

**[9:20]** Here you go.

**[9:21]** All right.

**[9:22]** Our ship is ready to sail,

**[9:23]** but we have no crewmates yet.

**[9:25]** Where? The captain.

**[9:27]** We can't do everything by ourselves.

**[9:28]** We need to bring in agents

**[9:30]** as our crewmates.

**[9:31]** I use four different

**[9:32]** agent harnesses regularly.

**[9:34]** There is cloud,

**[9:35]** which is cloud code,

**[9:37]** which is basically

**[9:37]** the only practical choice

**[9:39]** if you are using the subscription

**[9:40]** from anthropic.

**[9:42]** Generally speaking, though,

**[9:43]** it's a pretty good harness.

**[9:45]** I think

**[9:45]** it has the most sensible

**[9:47]** default experience out of the box.

**[9:49]** It's also got a pretty rich feature set.

**[9:51]** The downside

**[9:52]** is that sometimes it's a little

**[9:54]** bit buggy,

**[9:54]** and it's not as customizable

**[9:57]** as some of the other options.

**[9:58]** The next one I use a lot is Codex COI.

**[10:02]** It's written in rust,

**[10:03]** and you can feel

**[10:04]** it's a little bit smoother

**[10:05]** than cloud code when you use it.

**[10:07]** It's also open source,

**[10:09]** so if you run into some problems,

**[10:10]** You can often

**[10:11]** just have Codex

**[10:12]** inspect its own source code

**[10:14]** and figure out a workaround by itself.

**[10:17]** It's a bit

**[10:17]** lacking in terms of bells and whistles,

**[10:19]** and it's also not very customizable.

**[10:22]** And then there is the Pi coding agent.

**[10:25]** And this whole philosophy

**[10:27]** is to be minimal and highly extensible.

**[10:29]** It's great

**[10:30]** if you don't want any bloat

**[10:31]** and you'd like to tinker around

**[10:33]** and kind of make it your own.

**[10:35]** and lastly, there is open code.

**[10:38]** I like it a lot.

**[10:40]** It's got a battery smooth t UI,

**[10:42]** And it's got

**[10:43]** good integration

**[10:44]** with pretty much

**[10:45]** every model you can find.

**[10:46]** It's also got a more complete

**[10:48]** out of the box feature set than Pi.

**[10:50]** So if you want to use an agent harness

**[10:52]** that is model agnostic

**[10:54]** and one that you can just grab

**[10:56]** from the shelf and just go.

**[10:57]** Open code is a pretty good choice.

**[10:59]** For the rest of this video though.

**[11:01]** I'm going to use cloud code

**[11:02]** because I know

**[11:03]** many people are already familiar with it,

**[11:05]** but I have been very strict

**[11:07]** about making my workflow

**[11:08]** agent agnostic

**[11:09]** because the landscape is changing very,

**[11:11]** very fast.

**[11:12]** who knows which model or agents

**[11:14]** will be the best

**[11:15]** performing one next month?

**[11:16]** Right.

**[11:16]** So everything I show here in

**[11:18]** the video is agent agnostic

**[11:20]** and should be applicable

**[11:21]** regardless of which model or harness

**[11:23]** you use.

**[11:25]** The problem with this crewmates

**[11:27]** is that they are fresh recruits,

**[11:28]** and they have no idea how we run our ship

**[11:30]** or how we like to work.

**[11:32]** We need a proper onboarding process

**[11:34]** to ramp them up.

**[11:35]** We will do this mostly through

**[11:37]** two ways memory files and skills.

**[11:40]** There are few types of memory

**[11:41]** files, global memory

**[11:43]** files, and project level memory files.

**[11:45]** The global memory

**[11:46]** file for cloud code is at this location,

**[11:51]** and every other

**[11:52]** agent

**[11:53]** uses the other standard location here.

**[11:56]** So what I do is that I use this command

**[11:59]** Which made MD a symbolic link to MD.

**[12:04]** So they both exist,

**[12:05]** but under the hood

**[12:06]** they point to the same file.

**[12:08]** Here's

**[12:08]** the content of my actual global memory

**[12:11]** file. You can see it's pretty minimal.

**[12:14]** There is only 27 lines.

**[12:16]** Because everything in this file

**[12:17]** gets loaded into the system

**[12:19]** prompt of every single agent session

**[12:21]** across all our projects.

**[12:23]** If we have too much content in this file,

**[12:26]** it will silently use a lot of our tokens.

**[12:29]** I mostly write down

**[12:30]** my personal preferences here,

**[12:31]** like never use em.

**[12:34]** Somehow AI models are trained

**[12:36]** to use

**[12:36]** em by default instead of a plain dash.

**[12:39]** So now whenever I see em,

**[12:41]** I just feel like it's robotic.

**[12:43]** And I don't like that

**[12:44]** when I need the agent

**[12:45]** to write something for me.

**[12:46]** Like PR descriptions.

**[12:48]** Oh, and this is a good one.

**[12:49]** When making technical decisions,

**[12:51]** don't give too much weight

**[12:52]** to development cost.

**[12:54]** Here is something interesting

**[12:55]** that you may not know. Let me show you.

**[12:58]** If we ask a frontier model

**[13:00]** to estimate the development

**[13:01]** cost of a project,

**[13:03]** let's say

**[13:04]** I want to build a 3D

**[13:06]** first person shooting game

**[13:08]** that I can play locally with AI enemies.

**[13:12]** How long do you think that will take?

**[13:16]** Let's see what cloud will say.

**[13:18]** Okay, here it is.

**[13:19]** See, the estimate is in days

**[13:21]** and weeks and months.

**[13:23]** But if we ask the agents to

**[13:25]** actually build it now,

**[13:26]** I can guarantee

**[13:27]** it will come back with a playable version

**[13:29]** in just a few minutes.

**[13:31]** Because I have done this so many times.

**[13:33]** This mismatch is happening

**[13:35]** because the models

**[13:36]** were trained from human data,

**[13:38]** and that is what

**[13:39]** a typical human developer

**[13:40]** would give as the estimate.

**[13:43]** AI doesn't seem to know it

**[13:44]** can code much faster than humans yet.

**[13:47]** When AI is making technical decisions,

**[13:50]** it's implicitly

**[13:51]** assuming the development cost

**[13:52]** for some of the options are much higher

**[13:55]** than they actually are.

**[13:56]** This biases the model to choose

**[13:59]** cheap solutions

**[14:00]** that are often low quality,

**[14:02]** not scalable, or hard to maintain.

**[14:04]** So I have this rule here to

**[14:06]** correct that bias.

**[14:09]** I also said when

**[14:10]** doing bug fixes

**[14:12]** always starts

**[14:13]** with reproducing the bug

**[14:14]** in an end to end setting

**[14:16]** as closely aligned

**[14:17]** with how an end user

**[14:19]** would experience it as possible.

**[14:21]** AI models today by default

**[14:23]** like to write unit tests,

**[14:25]** which are often not sufficient

**[14:26]** and not really covering

**[14:28]** the product behaviors we want to guard.

**[14:30]** I found that leaning into end to end

**[14:32]** testing is a lot more reliable.

**[14:34]** Besides these preferences,

**[14:35]** I also have

**[14:36]** some interesting stuff opinions,

**[14:39]** which is super useful.

**[14:41]** That's a slightly different

**[14:42]** topic though,

**[14:42]** so I won't go into too much detail here,

**[14:44]** but I do have a blog post

**[14:46]** explaining how that works,

**[14:47]** which I'll link here

**[14:48]** in case you're interested.

**[14:49]** Besides the global memory

**[14:51]** file, each project

**[14:52]** can also have a project level memory

**[14:54]** file.

**[14:54]** Let me show you

**[14:55]** one example here by going into

**[14:57]** this project called High Bit.

**[14:59]** This is an AI Twitter app

**[15:00]** I have been working on.

**[15:01]** The project level memory file

**[15:03]** is typically stored as cloud or agents,

**[15:07]** depending on which agent you use.

**[15:09]** I do the same thing here

**[15:10]** with a symbolic link.

**[15:11]** So the same file is shared

**[15:13]** for both cloud and other agents.

**[15:15]** This one we are looking at

**[15:16]** here is a little bit verbose.

**[15:18]** I would say

**[15:19]** I will probably clean this up after this,

**[15:21]** but let me show you on a high level

**[15:23]** what I put into this file.

**[15:24]** It has some context on what

**[15:26]** this project is,

**[15:27]** how the repo is laid out,

**[15:30]** some terminology,

**[15:32]** how some of the most important

**[15:34]** components work,

**[15:35]** and how to do end to end testing,

**[15:37]** and some conventions at the bottom.

**[15:40]** This file is a lot more verbose

**[15:42]** than the global memory file,

**[15:44]** because this is basically the collective

**[15:46]** learning of all the agent sessions

**[15:48]** in this project.

**[15:49]** The way I built

**[15:49]** this file is not by writing

**[15:51]** everything by hand,

**[15:52]** but rather that every time

**[15:54]** I saw the agent doing something wrong,

**[15:56]** I would correct it

**[15:57]** and ask it to remember

**[15:58]** to not make the same mistake again

**[16:00]** by storing the learning

**[16:01]** into this memory file.

**[16:03]** So over time,

**[16:04]** our crewmates working on this project

**[16:06]** get smarter and more experienced.

**[16:08]** You don't need any fancy memory system

**[16:10]** to do that.

**[16:10]** This markdown file is all

**[16:12]** it takes over time.

**[16:13]** It does tend to get more

**[16:15]** and more bloated though.

**[16:16]** One way

**[16:17]** I reduce the size of this file

**[16:19]** is by moving

**[16:20]** some conditional information

**[16:21]** that is not always needed into a skill.

**[16:24]** For example,

**[16:25]** the end to end

**[16:26]** testing instruction here is only needed

**[16:29]** if the agent is making changes, right?

**[16:31]** So if I just ask the agent a question,

**[16:34]** this whole section is totally useless

**[16:36]** and would be wasting tokens.

**[16:38]** The way to improve efficiency

**[16:40]** here is by converting

**[16:42]** this kind of

**[16:43]** conditionally useful information

**[16:44]** from the memory file into skills.

**[16:47]** I typically just

**[16:48]** ask the agent to do this.

**[16:49]** Here, let me do it alive.

**[16:52]** I will say let's extract the end to end

**[16:56]** testing instructions

**[16:58]** junctions in our agents

**[17:01]** and file into a project level skill.

**[17:07]** Cloud already knew how

**[17:09]** to do this,

**[17:10]** what skills mean and how to create them,

**[17:12]** but other agent

**[17:13]** harnesses may not understand

**[17:15]** how to do that out of the box.

**[17:17]** To teach your agent how to create skills,

**[17:20]** you can install a skill called

**[17:22]** Skill Creator which

**[17:24]** which was written by anthropic.

**[17:26]** You can do that by running this command.

**[17:28]** This NPC's skills thing

**[17:31]** is a call from Vercel that is very handy.

**[17:34]** It's basically my main tool

**[17:36]** for installing and managing skills.

**[17:38]** It supports pretty much any agent.

**[17:41]** Once this skill is installed,

**[17:42]** your agent will be able

**[17:43]** to follow the rules and create

**[17:45]** new skills for you moving forward.

**[17:48]** cloud has done its work.

**[17:49]** Let's look at what cloud created for us.

**[17:53]** It basically removed

**[17:56]** a large chunk of the content

**[17:58]** from our agents MD file and move

**[18:02]** that into this this skill file.

**[18:05]** This is a good thing about skills

**[18:07]** is that it's designed

**[18:08]** for progressive disclosure,

**[18:10]** which means when your agent starts,

**[18:12]** it only loads this tiny description

**[18:14]** field from your skills into the system

**[18:16]** prompt to know what these skills do,

**[18:18]** and only when it actually decides

**[18:21]** that it needs to use a certain skill.

**[18:23]** It will then reads the rest of this file.

**[18:25]** This allows you to store

**[18:27]** a lot of the knowledge

**[18:28]** about how to do various

**[18:29]** kinds of things

**[18:30]** without blowing up your system.

**[18:32]** Prompt and memory file

**[18:33]** with a ton of contents

**[18:34]** that uses your tokens

**[18:35]** for every single request,

**[18:37]** whether the request actually

**[18:38]** needs those skills or not.

**[18:40]** One thing

**[18:40]** I do want you to know about skills

**[18:42]** is that you should generally avoid

**[18:45]** installing random skills

**[18:46]** from the internet.

**[18:47]** Even the ones that have a lot of

**[18:49]** GitHub stars.

**[18:50]** First of all,

**[18:51]** these skills

**[18:52]** can instruct your agents to run

**[18:53]** pretty much anything on your machine.

**[18:56]** This is a very risky thing to do,

**[18:57]** because the agent can lick your API keys

**[19:00]** or even credentials to your bank

**[19:02]** account to untrusted

**[19:03]** third parties without you knowing.

**[19:06]** even if we put aside

**[19:07]** the security problem,

**[19:08]** some of the skills

**[19:09]** actually degrade your agents performance.

**[19:12]** Look at this repo

**[19:13]** here called Android Skills, which has

**[19:16]** 177,000 GitHub stars.

**[19:20]** That's like massive.

**[19:21]** So it must be really good, right?

**[19:23]** I actually evaluated a skill in this repo

**[19:26]** with Program Bench,

**[19:28]** which tests

**[19:29]** the agent's ability to build

**[19:30]** programs end to end.

**[19:32]** And the result shows

**[19:34]** that by using this skill,

**[19:36]** the agent will use

**[19:37]** 5% more tokens

**[19:38]** while making the results worse.

**[19:40]** And if you look closely, this skill is

**[19:44]** not even written by André

**[19:45]** Karpathy himself.

**[19:47]** I'm not here to criticize

**[19:48]** the author of this repo, though.

**[19:50]** I'm mainly saying

**[19:51]** that being popular

**[19:52]** is not the same as actually being good.

**[19:55]** A lot of the skills

**[19:56]** being widely shared today

**[19:58]** have not been rigorously evaluated,

**[20:00]** and are typically just some random guy

**[20:03]** who found something

**[20:04]** that worked for themselves and

**[20:06]** and somehow got it to go viral.

**[20:08]** Their GitHub stars

**[20:10]** only tell you how popular they are

**[20:11]** and not

**[20:12]** whether they are actually helpful.

**[20:14]** So as a general rule of thumb,

**[20:16]** I recommend that you do not install

**[20:18]** any skill

**[20:19]** from the internet

**[20:20]** that claims to magically

**[20:22]** make your agent perform better,

**[20:23]** but hasn't published anything

**[20:25]** rigorous that proves its claim.

**[20:27]** All right.

**[20:28]** Now that we have memory files

**[20:30]** and skills to help ramp up

**[20:31]** crewmates, it's

**[20:32]** finally time

**[20:33]** to actually start working

**[20:34]** with the crewmates and set sail.

**[20:36]** The first thing about working with

**[20:38]** the crewmate is how you talk to them.

**[20:40]** I have pretty much completely moved

**[20:42]** to voice input now, So.

**[20:44]** Instead of typing,

**[20:45]** I will just say, explain this

**[20:47]** repo in a concise way

**[20:48]** and give me a recap of what

**[20:50]** the recent press have been working on.

**[20:53]** This is just so easy.

**[20:54]** There is an actual paper from Stanford

**[20:57]** that seriously compared the efficiency.

**[20:59]** And basically

**[21:01]** talking is three times

**[21:02]** faster than typing.

**[21:04]** So this is a very big boost

**[21:05]** in productivity.

**[21:07]** I also want to show you something

**[21:08]** interesting here.

**[21:09]** If we go to the references of this paper

**[21:13]** look who's here.

**[21:15]** It's our guy Dario.

**[21:17]** What is the CEO of anthropic doing here?

**[21:20]** Apparently if we follow this link

**[21:23]** Dario was doing some speech recognition

**[21:26]** stuff back in 2016.

**[21:28]** Now we're using speech recognition

**[21:29]** technology to talk to cloud

**[21:31]** which is also created by Dario.

**[21:33]** What a small world.

**[21:35]** The voice input.

**[21:36]** We just did

**[21:37]** was actually transcribed

**[21:38]** locally using this app called Open

**[21:41]** Super Whisper.

**[21:43]** It's completely free and open source,

**[21:45]** which is what I think

**[21:46]** this type of software should be.

**[21:47]** It runs the whisper model

**[21:49]** locally on your machine

**[21:50]** and do the transcription.

**[21:51]** And the quality is like

**[21:53]** really, really good.

**[21:54]** So this is how I do most of my prompts.

**[21:56]** Now, the only case

**[21:58]** where I fall back to typing

**[22:00]** is when I need to give the agent a URL

**[22:03]** or a file path, or something like that.

**[22:05]** Trust me,

**[22:06]** you don't want to speak a URL out loud,

**[22:09]** whether it's by yourself or

**[22:10]** with other humans around.

**[22:13]** If we

**[22:13]** come back to this prompt

**[22:15]** and let the agent run,

**[22:16]** you will see that

**[22:17]** because we asked the agent

**[22:19]** to look at recent polls,

**[22:20]** it will need to call GitHub

**[22:22]** to fetch the data.

**[22:24]** This is an important thing

**[22:25]** to pay attention to,

**[22:26]** because agents

**[22:27]** rely on external tools

**[22:29]** like GitHub to do its tasks.

**[22:31]** The design of these external tools

**[22:33]** can greatly affect

**[22:34]** your agents performance.

**[22:35]** Take GitHub as an example.

**[22:37]** Many people use the GitHub MCP

**[22:39]** server for accessing GitHub.

**[22:41]** However, I ran this benchmark here

**[22:44]** that measured various

**[22:45]** kinds of ways

**[22:46]** to access GitHub For the exact same tasks

**[22:50]** using GitHub, MCP

**[22:51]** server will cost you to spend three times

**[22:54]** more on token cost,

**[22:56]** and more than double

**[22:57]** the latency compared to using the CLI.

**[23:00]** If you are using the GitHub MCP,

**[23:01]** you are pretty much wasting

**[23:03]** both time and money

**[23:04]** for no clear benefits.

**[23:06]** Now you can see there's

**[23:07]** this thing called axi,

**[23:09]** which has the lowest cost

**[23:10]** but highest success rate.

**[23:12]** So what is it? Let me show you.

**[23:16]** Axi is a set of

**[23:18]** design standards

**[23:19]** I authored

**[23:19]** after discovering the huge upside

**[23:21]** we can have by designing our tools

**[23:24]** to treat agents as a first class citizen

**[23:27]** and optimize for agent ergonomics.

**[23:30]** I created ten principles

**[23:32]** for how to make a tool

**[23:33]** highly efficient for agents.

**[23:35]** For example,

**[23:37]** using token efficient output

**[23:38]** format can save about 40%

**[23:40]** tokens compared to using JSON.

**[23:42]** And then I built a few axes with

**[23:45]** Besides the GitHub axis I showed earlier,

**[23:47]** I also built Chrome dev tools actually,

**[23:49]** and benchmarked

**[23:51]** it against other various browser tools.

**[23:54]** And Here you can see

**[23:56]** the agents taking less turns

**[23:58]** and using less tokens

**[23:59]** to get the same tasks done with the ax.

**[24:02]** The main point here

**[24:03]** is when you give tools to your agents,

**[24:05]** do some research on their efficiency

**[24:07]** because they can greatly affect

**[24:09]** how much mileage

**[24:10]** you get out of your agents.

**[24:12]** If you want to use the axes

**[24:14]** I mentioned earlier,

**[24:15]** you can just go to this site called axis

**[24:18]** and find them in this catalog.

**[24:20]** You can just go to the repo

**[24:22]** and find instructions

**[24:23]** for how to start using them.

**[24:25]** Speaking of this catalog,

**[24:27]** there is something called

**[24:28]** lavish axi here.

**[24:30]** This is a very important tool

**[24:32]** in my setup.

**[24:33]** I pretty much rely on this tool

**[24:35]** for planning any kind of complex work.

**[24:37]** Let's do a real feature live

**[24:39]** and I'll show you how it works.

**[24:40]** Let me first launch high bit

**[24:42]** to show you

**[24:43]** what I'm trying to work on here.

**[24:45]** Hybrid is an AI Twitter

**[24:46]** I'm building for kids.

**[24:48]** I'll just create a test profile here.

**[24:53]** You can see here

**[24:54]** at the top I

**[24:55]** have these two buttons,

**[24:56]** what I can do and my progress.

**[24:59]** They are showing very similar content

**[25:01]** right now which is a problem.

**[25:03]** So and also the UI is not very exciting

**[25:07]** or fun.

**[25:08]** So let me go back and talk to cloud.

**[25:14]** I'll still use voice input here.

**[25:16]** I'll just say

**[25:18]** I'd like to consolidate

**[25:19]** the what I can do

**[25:21]** and my progress buttons,

**[25:23]** because their functionality

**[25:25]** is very similar

**[25:25]** and I'd like to revamp the experience

**[25:28]** there to be something

**[25:29]** more fun

**[25:30]** and exciting,

**[25:31]** like in an achievement system.

**[25:33]** Come up with some options

**[25:35]** and let's discuss.

**[25:36]** Don't use lavish.

**[25:39]** Okay, the reason I said don't use

**[25:41]** lavish is that I wanted to show you

**[25:44]** what's the default workflow today.

**[25:45]** Looks like for many people.

**[25:47]** And then I'm going to show you

**[25:48]** the difference lavish makes.

**[25:50]** Because I already have leverage

**[25:52]** skills installed.

**[25:53]** My cloud will automatically use lavish

**[25:55]** for this type of question,

**[25:56]** which is why I had to tell

**[25:58]** it not to do that right now.

**[26:00]** Okay, cloud is doing this work.

**[26:02]** Now. Cloud has come back with a response.

**[26:05]** Sometimes it will use its plan mode,

**[26:07]** or sometimes I will ask you

**[26:09]** to write down the plan

**[26:09]** in the markdown file,

**[26:10]** but it's more or less the same.

**[26:13]** It's a wall of text

**[26:14]** I now have to read through.

**[26:15]** It's not very easy to understand

**[26:17]** what what

**[26:18]** each option

**[26:20]** is actually going to look like,

**[26:22]** and if I'm not happy

**[26:23]** with some parts of it,

**[26:24]** I can't very easily tell cloud

**[26:27]** which parts I'm talking about.

**[26:28]** I can select a piece of text

**[26:30]** in the plan and say, this is wrong.

**[26:32]** Now let's try

**[26:33]** the exact same prompt with lavish.

**[26:35]** Here it goes again.

**[26:36]** I actually don't have to say

**[26:37]** use lavish

**[26:38]** because the agent already

**[26:40]** has the lavish skill

**[26:41]** that tells the agent

**[26:42]** for this type of planning

**[26:44]** it should establish, for demo purpose,

**[26:46]** I just wanted to be explicit.

**[26:48]** Cloud would roughly do the same things

**[26:50]** to figure out the options,

**[26:52]** except at the end

**[26:53]** it would not print out that wall of text.

**[26:56]** Again,

**[26:56]** it will launch the browser

**[26:58]** and show me this page. Now look at this.

**[27:01]** This is the lavish editor.

**[27:03]** The reason I named it lavish

**[27:04]** is that it's richer than a rich editor.

**[27:07]** I almost named it filthy

**[27:09]** rich editor,

**[27:09]** but that's just not the best

**[27:11]** sounding name.

**[27:12]** Lavish editor basically

**[27:14]** instructed the agent

**[27:15]** to create an HTML artifact

**[27:17]** to visualize what we need to discuss.

**[27:19]** It always uses the same design system

**[27:22]** as the current project being worked on,

**[27:24]** so this is consistent

**[27:25]** with how the app actually looks.

**[27:28]** This makes it very easy

**[27:29]** to reveal concepts and prototypes.

**[27:32]** See the option is laid out here.

**[27:33]** This is so much easier to understand

**[27:36]** than the huge wall of text

**[27:37]** we were looking at

**[27:38]** in the terminal, right?

**[27:40]** I can also annotate

**[27:41]** and make comments

**[27:43]** on specific parts of the artifacts

**[27:45]** to give feedback to the agent.

**[27:47]** This is something

**[27:47]** that's really hard

**[27:48]** to do with the wall of

**[27:49]** text, or a markdown file

**[27:52]** And at the bottom, there

**[27:54]** are things for me to decide on,

**[27:56]** and I can just click on these options

**[27:59]** to make the decisions.

**[28:00]** I just sent this feedback back

**[28:02]** to the agents inside of lavish

**[28:04]** without even having to go back

**[28:05]** to the terminal.

**[28:06]** Honestly, I can never go back

**[28:08]** to reading text in the terminal anymore.

**[28:10]** This is just way too much more efficient.

**[28:12]** Now the agent has made updates to the and

**[28:15]** I feel happy about this,

**[28:16]** so I'll just tell the agent

**[28:18]** to start building.

**[28:19]** Start building and we'll end

**[28:22]** the session.

**[28:23]** We can

**[28:24]** then go back to the terminal now and see.

**[28:27]** The agent will start to work

**[28:28]** on the implementation,

**[28:30]** because we already clarified

**[28:31]** all the requirements

**[28:32]** in the planning phase.

**[28:33]** I typically don't

**[28:34]** need to interfere at all

**[28:35]** during this implementation phase.

**[28:37]** I only come back to this

**[28:38]** when the agent has done.

**[28:39]** And when the agent says it's done,

**[28:42]** that's actually

**[28:42]** when things get really tricky.

**[28:45]** This is where a lot of people

**[28:46]** will spin up

**[28:47]** their editor

**[28:48]** and start reviewing the diff.

**[28:51]** The problem is, AI writes code so fast,

**[28:54]** and if every piece of code requires

**[28:57]** your review,

**[28:57]** then you are creating a big

**[28:59]** bottleneck on yourself

**[29:00]** because you can only review so many

**[29:02]** every day.

**[29:03]** Your velocity will be hard capped by it.

**[29:06]** And even more importantly, reviewing diff

**[29:09]** is just not fun.

**[29:11]** No one says I became an engineer

**[29:13]** because I love reviewing diffs all day.

**[29:15]** My advice

**[29:16]** here is that

**[29:18]** in order to

**[29:18]** really scale ourselves with AI,

**[29:21]** we have to think of ourselves

**[29:22]** more as an engineering manager

**[29:24]** or engineering director.

**[29:26]** Your directors

**[29:27]** most likely don't review any place yet.

**[29:30]** They can influence the quality

**[29:31]** of their team's software

**[29:32]** by creating good culture

**[29:34]** and processes, and rely on the team

**[29:37]** to carry them out.

**[29:38]** That's what we should do with AI.

**[29:40]** What I do here,

**[29:41]** when the agent says the work is

**[29:43]** done, is not to start

**[29:44]** reviewing the dips or start

**[29:46]** manually testing the changes.

**[29:48]** That's too much overhead.

**[29:49]** On myself,

**[29:50]** I sense the change into a pipeline

**[29:52]** I built called No Mistakes.

**[29:57]** No mistakes is also free and open source.

**[30:00]** It orchestrates your agent

**[30:01]** to execute a series of steps

**[30:03]** that takes this first pass code

**[30:05]** all the way through to a clean PR.

**[30:07]** It would first create a branch

**[30:09]** if one doesn't exist yet,

**[30:10]** and then create a commit

**[30:12]** and then take it through a pipeline

**[30:14]** in an isolated work tree,

**[30:16]** so nothing during the validation

**[30:18]** would affect your current repo.

**[30:19]** It would first understand

**[30:20]** your real intent behind the change

**[30:22]** by analyzing

**[30:23]** your agent session,

**[30:24]** then rebase the change

**[30:26]** on top of the latest main branch

**[30:28]** on remote

**[30:28]** origin and resolve merge

**[30:30]** conflicts up front,

**[30:31]** then starts

**[30:32]** an adversarial review

**[30:34]** in its own fresh context window.

**[30:36]** This is where most problems get caught,

**[30:38]** and obvious problems

**[30:40]** will get self corrected,

**[30:41]** but ambiguous ones

**[30:43]** that have product

**[30:44]** implications will be escalated

**[30:46]** to us humans for a decision after review.

**[30:49]** It also tries to test

**[30:51]** the change end to end

**[30:52]** against the original intent,

**[30:53]** and this step will

**[30:55]** actually record evidence that proves

**[30:57]** the change is working that we can.

**[30:58]** Then later on

**[30:59]** look at to gain more confidence.

**[31:02]** It will then do a documentation pass

**[31:04]** of updating all relevant documentation

**[31:06]** to reflect the latest change.

**[31:08]** And also finally,

**[31:09]** make sure there is no linting problems

**[31:11]** before pushing the branch

**[31:13]** to remote and raise a PR.

**[31:15]** The no mistakes

**[31:16]** pipeline will also keep babysitting

**[31:18]** the PR

**[31:19]** until it's merged,

**[31:20]** because during the PR phase,

**[31:22]** we can still have merge conflicts

**[31:23]** that come in, or CI pipeline failures

**[31:26]** that are very annoying as well,

**[31:28]** with no mistakes doing the babysitting.

**[31:30]** We don't have to waste our own time

**[31:31]** at all.

**[31:32]** Another way to trigger

**[31:33]** no mistakes is as a skill.

**[31:36]** I can just type no mistakes in the agent

**[31:39]** and it will do the same pipeline

**[31:41]** as This may seem very slow,

**[31:43]** but in practice

**[31:44]** I never stare at this screen.

**[31:46]** I would go spin up other tasks.

**[31:47]** I come back only when no mistake says

**[31:50]** all checks passed

**[31:51]** that's when I go to the PR

**[31:53]** and apply my judgment.

**[31:54]** Here's the PR

**[31:55]** from the change we just did.

**[31:57]** We can see here

**[31:58]** it summarized the original intent.

**[32:00]** What's changed,

**[32:02]** how it's tested,

**[32:03]** and what happened

**[32:04]** during the normal stakes pipeline.

**[32:06]** We can click to see the evidence

**[32:09]** from its testing

**[32:10]** to know

**[32:11]** whether it's really done

**[32:12]** what we asked for,

**[32:14]** depending on what the change is,

**[32:16]** the evidence

**[32:17]** could be a screenshot like this

**[32:19]** a video demo,

**[32:20]** a log file, or something else.

**[32:22]** It's designed

**[32:22]** to give you the most direct way

**[32:24]** to see the change

**[32:25]** working as you intended.

**[32:26]** We can also see that

**[32:27]** the pipeline discovers

**[32:29]** some problems

**[32:29]** and fix them before raising the PR.

**[32:32]** This is a good time to audit

**[32:34]** whether these changes

**[32:35]** are actually what we need.

**[32:36]** If anything doesn't look right,

**[32:38]** we can go back to the agent

**[32:39]** and ask for more changes

**[32:40]** before merging this PR.

**[32:42]** This risk assessment

**[32:43]** here is also very useful.

**[32:45]** I basically look at this to decide

**[32:47]** how much time

**[32:47]** I should spend on reviewing

**[32:49]** this change in more detail.

**[32:51]** For low risk changes,

**[32:52]** I don't really look at the diff at all

**[32:54]** Because I have validated

**[32:56]** time and time again for low risk changes.

**[32:58]** Any problem I could catch

**[33:00]** is very likely

**[33:01]** already caught by the pipeline

**[33:03]** only more

**[33:03]** risky changes are worth my

**[33:05]** This is how I scale up

**[33:06]** the volume of code changes

**[33:07]** I do every day through

**[33:09]** a large crew of agents,

**[33:10]** without losing control on quality.

**[33:12]** One thing we are starting to see

**[33:14]** now is that the place where I spend

**[33:16]** time is towards the beginning

**[33:18]** and the end of the task.

**[33:20]** At the beginning

**[33:21]** I would spend time in lavish to plan

**[33:23]** the requirements more clearly.

**[33:25]** At the end

**[33:26]** I would come in and hold

**[33:27]** a bar on quality.

**[33:29]** All these parts in the middle

**[33:31]** is done by AI,

**[33:32]** which frees me up to spin up other tasks.

**[33:35]** This is a core aspect of how I work,

**[33:37]** and you can see the more time

**[33:39]** I can free up in the middle,

**[33:41]** the more work I can go do in parallel.

**[33:43]** So an interesting question

**[33:45]** now is

**[33:46]** how do we get the agents

**[33:47]** to work for longer

**[33:48]** and longer in the middle?

**[33:50]** That depends on us

**[33:51]** giving them more and more complex tasks

**[33:53]** that take longer to complete.

**[33:55]** But more complex tasks are often

**[33:58]** not as easy for our agents

**[33:59]** to complete autonomously.

**[34:02]** An extreme version of this is

**[34:03]** when I go to bed,

**[34:04]** I sleep for 7 to 8 hours every night.

**[34:07]** How do I keep the agents busy

**[34:09]** for eight hours?

**[34:10]** This is where I say good night.

**[34:13]** Have fun.

**[34:13]** It's another free and open source tool

**[34:15]** I built specifically

**[34:17]** for long running tasks.

**[34:18]** It's becoming quite popular.

**[34:20]** It's that simple to use.

**[34:22]** Just give it an objective

**[34:23]** and it will keep going

**[34:24]** until it meets some stop condition

**[34:26]** you defined.

**[34:27]** Let me show you a real example

**[34:29]** that I often do.

**[34:30]** This is again in the hybrid repo

**[34:32]** I will run.

**[34:33]** Good night.

**[34:33]** Have fun and give a prompt.

**[34:36]** Pretend you are a seven year

**[34:38]** old kid and use the high bit

**[34:40]** app end to end.

**[34:41]** Don't mind

**[34:42]** the profile

**[34:42]** creation step

**[34:43]** which is designed for parents

**[34:45]** in the rest of the app.

**[34:46]** Try to do different things

**[34:47]** and find the first usability problem

**[34:50]** that will confuse you as a kid,

**[34:52]** or stop you from knowing how to proceed.

**[34:54]** If you find a problem, stop and fix it,

**[34:57]** then rinse and repeat.

**[35:00]** Here he goes.

**[35:01]** Good night. Have fun.

**[35:02]** Is now running in the loop.

**[35:03]** To execute on what I just asked for.

**[35:06]** I can monitor token usage here

**[35:08]** or how many iterations have been done.

**[35:10]** The iterations will be showing up

**[35:12]** as the moons in this row,

**[35:13]** and I can see how many commits

**[35:15]** have been made as well.

**[35:16]** Or I can just go to bed

**[35:17]** knowing the agents won't stop

**[35:19]** until there is no more problem

**[35:20]** to be found.

**[35:21]** When I wake up,

**[35:22]** I can reveal a list of commits

**[35:24]** made on this new branch and decide

**[35:26]** which ones I want.

**[35:28]** I typically use goodnight.

**[35:29]** Have fun for improving

**[35:31]** on some verifiable objectives

**[35:33]** or objectives,

**[35:34]** where I trust the agent

**[35:36]** to have the reasonable judgment over,

**[35:38]** like the one we just did.

**[35:39]** Verifiable objectives

**[35:41]** are more like reducing page load

**[35:43]** time, improving

**[35:44]** end to end test coverage

**[35:45]** or like Android hypothesis auto research.

**[35:48]** Keep experimenting different hypotheses

**[35:51]** to improve on the metric.

**[35:52]** These are all

**[35:53]** well suited for a long running loop.

**[35:55]** To tackle

**[35:56]** the recently introduced

**[35:57]** slash goal

**[35:58]** command in Codex and Cloud

**[36:00]** code can also do something similar,

**[36:02]** good night.

**[36:03]** Have fun

**[36:03]** still gives me a better experience.

**[36:05]** Because I can set a token cap or

**[36:08]** iteration cap or stop condition

**[36:10]** more precisely,

**[36:12]** whereas in Cloud Code and Codex,

**[36:14]** if I set a goal before I go to bed,

**[36:16]** I might wake up realizing my weekly

**[36:19]** quota is all Good night.

**[36:20]** Have fun.

**[36:21]** Solved a very important problem,

**[36:23]** which is to keep the agents

**[36:24]** running for a long time.

**[36:26]** So when the agents are running,

**[36:28]** I'm freed up to do more things.

**[36:30]** This is when we level up

**[36:32]** and start working with multiple crewmates

**[36:34]** in parallel.

**[36:34]** So let's spin up another tab in teams

**[36:37]** and get more work started.

**[36:39]** Now here's the problem.

**[36:40]** In this directory I already have.

**[36:42]** Good night.

**[36:43]** Have fun running.

**[36:44]** So if I spin up another agent

**[36:46]** working in the same directory,

**[36:47]** they will step on each other's

**[36:49]** toes and cause conflicts.

**[36:51]** The default solution

**[36:52]** here is git work tree.

**[36:54]** For those of you

**[36:54]** who aren't familiar with it,

**[36:56]** a guitar work

**[36:57]** tree is basically creating

**[36:58]** a clone of your report directory.

**[37:00]** I can create one by typing git work tree

**[37:03]** add and give a path here.

**[37:07]** Now we have to think about a name.

**[37:09]** This is when you waste five minutes

**[37:11]** and eventually give up and just say hi.

**[37:13]** Bit two.

**[37:15]** Now we have a work tree

**[37:16]** and we can navigate to it.

**[37:18]** So let's go find it.

**[37:20]** It's in high bit two.

**[37:21]** This is a separate directory

**[37:23]** on the file system.

**[37:24]** So we can have an agent

**[37:25]** doing anything here.

**[37:26]** And it won't conflict

**[37:27]** with good night to have fun,

**[37:29]** which is running in the original report

**[37:31]** directory.

**[37:31]** The problem with work trees

**[37:33]** is that we now have something

**[37:35]** to maintain in our head.

**[37:36]** I need to remember.

**[37:38]** Oh, I have hybrid two here.

**[37:40]** Next time I come into this hybrid

**[37:42]** two directory

**[37:43]** I would wonder

**[37:44]** what was I doing in this work

**[37:45]** tree last time?

**[37:47]** Is there still an agent running or is it

**[37:49]** All of

**[37:50]** that has to

**[37:50]** exist in my head,

**[37:52]** and there is no way I'm

**[37:53]** going to remember all that.

**[37:54]** So this work tree

**[37:56]** basically becomes a debt.

**[37:57]** To get rid of it.

**[37:58]** I need to run this remove command.

**[38:02]** Remove.

**[38:05]** This is just a lot of overhead.

**[38:07]** My solution to

**[38:08]** that is another tool

**[38:09]** I built called Treehouse.

**[38:11]** It's very simple.

**[38:12]** I just come into this

**[38:13]** repo and I run Treehouse.

**[38:16]** It would drop me into a fresh work tree

**[38:18]** where I can start doing whatever I want.

**[38:21]** I can keep spinning up

**[38:22]** more and more of this work trees

**[38:24]** by running Treehouse again.

**[38:27]** And if I want, I can see a list

**[38:30]** of all the work trees

**[38:32]** by typing Treehouse status.

**[38:34]** So I can see

**[38:35]** which ones are being used versus not.

**[38:37]** When I'm done,

**[38:38]** I can just close this tab

**[38:39]** and Treehouse knows that I'm done,

**[38:42]** so it will free up

**[38:43]** that work tree for future use.

**[38:45]** Next time I ask for work tree,

**[38:47]** it will try to reuse one of the idol

**[38:50]** work trees

**[38:50]** instead of creating a brand new

**[38:52]** So let's start some real work.

**[38:54]** I have a bunch of user feedback

**[38:56]** from my son's last round of playtesting,

**[38:58]** so let me use this

**[38:59]** first worksheet

**[39:00]** we created and launch

**[39:01]** cloud, and I will say,

**[39:04]** I remember it's hard for the kid

**[39:06]** to realize

**[39:06]** they can press and hold

**[39:08]** the voice input button to talk.

**[39:10]** By default

**[39:10]** they just click it

**[39:11]** and then they will see a popover.

**[39:13]** Maybe in the popover,

**[39:14]** we add a label that tells them

**[39:16]** they can also press and hold

**[39:19]** and I'll enter.

**[39:21]** Then I'll spin up a new tab

**[39:23]** Treehouse Cloud, and this time I will say

**[39:28]** the Image attachment dropdown

**[39:29]** menu should have an action

**[39:31]** that takes a screenshot

**[39:32]** of the current app

**[39:33]** and use that as the attachment.

**[39:37]** All right, one more tab.

**[39:39]** Treehouse cloud.

**[39:44]** Our agent status bar right above the chat

**[39:46]** input is not always showing bot activity.

**[39:49]** Look into

**[39:50]** what happened

**[39:51]** there and make sure

**[39:52]** when any bots are in progress,

**[39:54]** it always displays

**[39:55]** something that reflects

**[39:56]** the latest activity.

**[39:59]** Boom!

**[40:00]** We now have three

**[40:00]** sessions running in parallel.

**[40:02]** Now I can keep going

**[40:03]** because none of these sessions

**[40:05]** will need my attention anytime soon,

**[40:07]** especially if I tell them to run.

**[40:09]** No mistakes after implementation.

**[40:11]** I know

**[40:11]** whether they need me

**[40:13]** by looking at the top status bar,

**[40:15]** and I can switch

**[40:16]** between the tabs using keyboard

**[40:17]** shortcuts like this.

**[40:19]** That's very important

**[40:20]** for managing a lot of parallel

**[40:21]** sessions efficiently.

**[40:23]** That said,

**[40:24]** after doing this for a while,

**[40:26]** you will discover that

**[40:27]** juggling between all these sessions,

**[40:29]** it's quite exhausting.

**[40:31]** The constant context switch

**[40:32]** and having to remind yourself

**[40:34]** what each session was even doing

**[40:36]** just doesn't feel like an ideal end

**[40:38]** game experience.

**[40:39]** So I kept pushing the boundary on this

**[40:42]** and I discovered that

**[40:44]** I needed a first mate,

**[40:46]** someone I can talk to as a captain

**[40:48]** that will carry out

**[40:49]** all my directions and manage

**[40:51]** all the crewmates for me

**[40:53]** so I can focus on the big picture

**[40:55]** like where should we go next?

**[40:56]** not playing whack

**[40:57]** a mole

**[40:58]** with this

**[40:58]** increasingly high number of crewmates,

**[41:00]** this is how I level up

**[41:02]** and truly become a captain.

**[41:04]** My First mate is another free

**[41:06]** and open source project

**[41:07]** and it's very new.

**[41:08]** The way to use it is by just cloning it.

**[41:14]** And then I can run

**[41:17]** an agent in this repository.

**[41:19]** Now I just talk to it

**[41:21]** and ask it to work on any projects

**[41:23]** I like.

**[41:24]** Let's say

**[41:25]** I'd like to work on lavish

**[41:27]** access, GitHub, Axi and Chrome dev tools.

**[41:29]** Actually They are all GitHub projects

**[41:31]** I own.

**[41:32]** first mate is starting up

**[41:33]** and the first time we run it

**[41:35]** it will do some setup

**[41:36]** and ask for some preferences,

**[41:38]** but it's also just talking to it,

**[41:39]** which is pretty easy.

**[41:41]** you might wonder

**[41:42]** why is the transcription so good?

**[41:44]** Because it's

**[41:45]** recognizing this project names.

**[41:47]** Let me show you.

**[41:49]** Open Silver Whisper actually supports

**[41:52]** this customization

**[41:54]** through a system prompt.

**[41:56]** So what we can do

**[41:57]** here is in this model menu

**[42:00]** in the transcription menu

**[42:01]** there is an initial prompt.

**[42:03]** And we can put in some common vocabulary

**[42:05]** that we use into this system prompt.

**[42:08]** this prompt is

**[42:09]** what makes the transcription really good.

**[42:10]** First mate here is asking how strict

**[42:13]** I want to be

**[42:13]** with the code changes in this repos,

**[42:15]** and I want to select full gates to PR.

**[42:19]** This is basically going

**[42:20]** to be using no mistakes

**[42:21]** as the pipeline to validate its change

**[42:25]** and first task.

**[42:26]** Yeah, I'll describe it. Right now.

**[42:29]** A real thing I want to do

**[42:30]** is for all three

**[42:32]** projects, I'd like to add an update

**[42:34]** command on the CLI

**[42:36]** that will update their

**[42:37]** version to the latest on npm.

**[42:41]** And let's see what First Mate does.

**[42:43]** It realizes that this is not one task,

**[42:46]** but three parallel tasks,

**[42:47]** and it's now spinning up

**[42:49]** these tabs in timox,

**[42:51]** just like we be the scenes.

**[42:53]** It would also call tree House

**[42:54]** to create work trees,

**[42:56]** and then run an agent in that work

**[42:58]** tree to get the work done,

**[42:59]** and then it will run.

**[43:00]** No mistakes to validate the change

**[43:02]** and get the PR ready for us to review.

**[43:04]** Now you can see

**[43:05]** it's first made that

**[43:07]** it's doing the juggling.

**[43:08]** I don't need to worry

**[43:09]** about any of this now.

**[43:10]** I can just keep giving it more work.

**[43:13]** Hey first mate,

**[43:14]** let's also look at the most recent

**[43:16]** three open issues in lavish axillary

**[43:19]** and let's discuss which

**[43:20]** ones are actionable.

**[43:23]** Boom!

**[43:24]** First mate

**[43:25]** now is pulling the open

**[43:26]** issues from the repo

**[43:27]** while waiting for the three background

**[43:29]** agents working in parallel.

**[43:31]** All right,

**[43:31]** first mate said number 87 is cleanest.

**[43:35]** It's very actionable.

**[43:36]** And let me just see.

**[43:38]** What is this?

**[43:39]** Don't toggle in annotation mode.

**[43:42]** Okay.

**[43:44]** That's the clear bug.

**[43:46]** All right, first mate, let's address

**[43:49]** number 87.

**[43:52]** Look, now first mate is struggling

**[43:54]** a lot of tasks for me

**[43:56]** that I otherwise

**[43:57]** would have to manage by myself.

**[43:59]** Watching it

**[43:59]** context switch is actually

**[44:01]** an oddly satisfying experience,

**[44:03]** because I know that's what

**[44:04]** I would have to do otherwise.

**[44:06]** First mate is basically all my tools

**[44:08]** coming together

**[44:09]** as one cohesive workflow,

**[44:11]** and I have been really happy with it.

**[44:13]** It's been a pretty

**[44:14]** significant improvement

**[44:15]** to my overall experience

**[44:17]** working with agents.

**[44:18]** I highly recommend trying it out

**[44:19]** if you are still directly talking

**[44:21]** to every single agent session one by one,

**[44:23]** it will be a pretty massive upgrade.

**[44:26]** Something you start to notice

**[44:27]** after having a first mate.

**[44:28]** Is that because first mate took care

**[44:31]** of so many things for you,

**[44:32]** you start to run out of ideas

**[44:34]** for what to ask you to do.

**[44:36]** This is a good thing because it indicates

**[44:38]** the bottleneck is shifting,

**[44:40]** but it also means you,

**[44:41]** as the captain, needs to keep up.

**[44:44]** This requires a mindset shift

**[44:46]** of focusing more of your energy

**[44:48]** on understanding what matters

**[44:50]** by talking to your users,

**[44:52]** understanding the competitive landscape,

**[44:54]** and crafting a good treasure

**[44:56]** map that can lead your crew

**[44:58]** to a good direction.

**[45:00]** Once you started doing

**[45:01]** that, congratulations!

**[45:03]** You have successfully transitioned

**[45:04]** from a sailor into a great captain.

**[45:07]** All right.

**[45:08]** We have gone from not having a ship

**[45:10]** to being a captain

**[45:11]** that has a first mate and a big crew

**[45:14]** that sailed together.

**[45:15]** This is a pretty good time

**[45:17]** to wrap up this video.

**[45:18]** All my tools can be found on my GitHub

**[45:20]** and will be linked

**[45:21]** in the description below.

**[45:23]** They are all free and open source.

**[45:25]** I built them

**[45:26]** because I just want

**[45:26]** to see more people learning

**[45:28]** how to do

**[45:28]** a genetic engineering

**[45:29]** effectively and doing it

**[45:31]** in an enjoyable way,

**[45:32]** and that's what I hope

**[45:34]** you can get out of this video.

**[45:36]** I will continue to share

**[45:37]** more of my workflow

**[45:38]** and things

**[45:38]** I find useful

**[45:39]** on my channel,

**[45:40]** so don't forget to subscribe

**[45:41]** if you don't want to miss anything.

**[45:43]** Thank you for watching

**[45:44]** and see you next time!
