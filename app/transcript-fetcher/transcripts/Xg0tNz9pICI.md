# Transcript: Xg0tNz9pICI

**URL:** https://www.youtube.com/watch?v=Xg0tNz9pICI
**Segments:** 1364

---

## Full Text

dark factory today. And I know it sounds kind of spooky, but uh I'll start things off by explaining what that actually is. This is going to be a little bit more of a casual live stream. So, I did a live stream over the weekend where I dove really deep into Archon, the new open-source harness builder. And so, I'm going to actually be using this a lot today, but I want to just do more like a live building session. So, I'll still like be sure to explain everything that I'm doing and have a good time for Q&A and stuff, but it's going to be a little bit more like you guys just get to see the inside of a process that I'm starting here with a public experiment that I'm calling the dark factory. And so, I've got my left monitor open up here with all of your guys' comments in the chat. And then my right monitor where I have my recording software and then I've got my screen in the middle here. So, when you see me looking around, that's what I'm doing. But yeah, this is just going to be like a a good like two two and a half hours I'm thinking of streaming for where I'm going to be building the dark factory in public with you guys and even opening this up fully to the public in a couple weeks here. I'll talk about what that means as well, but I I need to explain first what the heck a dark factory actually is. So, I'll I'll cover the basics for you guys. I think you'll find it really really interesting because this is like the peak evolution of AI coding. Not that a dark factory is going to give you the most reliable results, but it is the way to give the most control possible to your AI coding assistants when they're working on a codebase. So, the idea of the dark factory, it uh originated actually in the late I think like 1980s, 1990s. There were some companies in China that were um running physical production lines with only robots. And so, the physical location only had robots in it. So they didn't even have to have the lights on, right? There's no need to pay for electricity when there's no humans operating in the facility. And so Dan Shapiro, I believe he's the first one that took [clears throat] this idea of the dark factory and applied it to code bases. So using generative AI to completely manage a codebase all the way from ideiation, implementation, code review, merging pull requests, handling releases, like actually shipping the code as well. That is what a dark factory is. And I think the best way to explain it is to go through his article here. So he put this out just at the end of January this year. And he talks about the five levels of AI coding. A lot of us are at level like three or four right now. So I think like seeing where you're at and then like how far we can take things with the dark factory with his analogy will like really help you understand like exactly what the heck a dark factory is. And so yeah, let me go and share my screen here with this blog article. I actually meant to be sharing my screen earlier, so that's my bad. But yeah, so let's take a look at this together here. So this is uh Dan Shapiro's post from uh the start of this year here. So the five levels from spicy autocomplete to the dark factory. And so level zero, this is how I started using AI to help me code. probably the same for a lot of you guys that came from an engineering background. You were writing code yourself before and then you slowly start leaning on AI more and more. So, I don't know why he calls it spicy autocomplete, but hey, I love it. So, I'm I'm for it. So, and in [snorts] this case, um the analogy that he uses throughout the different levels is um our control of a vehicle. So, at level zero, we're still driving. You can even think of it as like stick shift, right? Like supermanual. we are managing the vehicle and so the AI coding assistant or even just like the large language model serves as a reference tool or an enhanced search. So it's like a smarter Stack Overflow if you guys have used Stack Overflow in the past. And so here the developer manually writes all the code. We're just using AI as an adviser. So like help me with this code snippet or give me an idea for how I can implement this. But we still are the ones hands on the keyboard writing the actual code. So hopefully most of us aren't at this step anymore. Um I know some people still are because that's what they're comfortable with and that's totally okay. But then we go into level one. This is the coding intern. So you can think of it like cruise control. You still have your hands on the wheel but at least AI is managing something or like the car is managing keeping you at a certain speed like 65 miles hour. So here the AI writes the unimportant or boilerplate code. So you're still doing most of the work yourself, but for the things that you don't require much trust in the large language model, you're starting to hand it over. That's the coding intern. And um by the way, when we get to level five, I'll talk about how I'm actually building it myself. So we we'll get there, but I want to kind of give the basis for you here. So we then get to level two, the junior developer. This is the pair programmer. So we start to relax a little bit. We only have one hand on the wheel instead of two. So the developer and AI trade off control. So there are legitimately some more complex tasks that we are delegating to the coding agent, but not all the time. We still are the ones writing the code a lot. And then we get to level three. And so this is, you know, like the self-driving cars now, right? Like you got hands off the wheel, but you're still paying attention to the road. And so the AI is generating a majority of the code base, but you're still reviewing everything that the AI does. Like you're watching the road constantly, and you're going to be nitpicky. You're going to review plans. You're going to give feedback. You're going to review the code like the poll requests before you merge it. You're always the bottleneck for verification before progressing. That's level three. And honestly, that's where most of us are. And you know, like when I teach AI coding on my channel and in the Dynamis community, level three is actually what I generally recommend because this is the furthest you can push it right now and still get the most reliable results possible. So level four, um, this is where we get into the engineering team, when we get into harnesses for longer running tasks. And so this is where you actually get to fall asleep at the wheel. So you let the AI run unattended for long periods, handling very complex tasks. And so you think of harnesses like the Ralph loop or anthropics harness, giving your second brain the ability to handle issues and pull requests end to end. So here, you still are going to check the final results. like at some point you're gonna you're going to wake up and just like make sure the car is actually driving you to the right place and you know take your put your hands on the wheel if you need to, but for the most part you're trusting the coding agent to handle insanely long sets of work. So level four, I I wouldn't say this is like the most reliable at this point. If you want to ship the most reliable production code possible, you're still at level three because you're still going to monitor everything and be the bottleneck for verification, but you're starting to really take yourself out of the loop with level four. But there's still the steering wheel, right? Like there's still the opportunity for you to step in and fix things yourself or steer the agents in a different direction in the middle of some implementation. And then that brings us into level five. And I love the car analogy here cuz you like you look at level four and there's still the steering wheel like right there's still the opportunity for you to have control. But in level five, your vehicle looks like this, which someday we'll get there. That'll that'll be really cool. the day that I have a vehicle, it looks like this. But there's no there's no steering wheel in this vehicle. There's not even the option for us to take the reinss if we want. That's what a dark factory is. So the engineer manages the goal in the system, right? There's still some kind of console here to provide higher level direction. We're still going to write the PRDS. We might manage the some of the releases, but we're not managing the code. So we provide plain English descriptions but the agent defines implementation, writes code, tests, fixes, bugs and ships. That is a dark factory. And uh that my friend is what we are going to be building today. I have a good amount of the system already set up because I don't want to go through all the like really boring parts with you. But I I want to work on the workflows today. like actually build the workflows that are going to manage the entire dark factory because it's not enough to just point cloud code at a GitHub repo and say manage everything right we have to teach it like how do we want it to handle issues what kinds of features are we going to build into this application how do we want to evolve it what are the constraints that we have how are we going to review code right we have to create workflows to define exactly how we want to write so right so like the engineer manages the goal bonus system. I'm talking about building the system here for this vehicle. And so, um, what I'm going to be doing, and this is this is the most exciting part for me, is I'm going to be leveraging Archon workflows to manage every single part of the dark factory. So, Archon is my first ever or it is the first ever open- source harness for AI coding. First ever harness builder, sorry. So you think about like whatever your process is right now for software development, however you work with AI coding assistants, archon allows you to build workflows to package everything up so that you can build any on any codebase. You can invoke any workflow, [clears throat] excuse me, you can invoke any workflow in parallel and you get reliable results every single time because you're taking your process and you're packaging it up. That's what Archon gives us. And so if you're interested more how Archon works and you haven't seen my content on it recently. There's a lot that I put out on my channel recently. So there's a couple of live streams that I did. Actually one just two days ago. Um so I did it just on Saturday last week. And then I also have a YouTube video, my most recent YouTube video where I covered Archon. So I'm not going to get like super deep into an introduction to Archon today because I already have this content. But I'm going to be using it as a very critical part of the workflow of the whole system for the dark factory because it's going to drive everything. I'm going to build archon workflows to manage my issues, build archon workflows to write the code, review the code, manage the releases. I'll talk about what that looks like when I get into my plan here. So, I have this entire markdown document that outlines my entire plan for the dark factory and I took a lot of inspiration from um you know other examples of dark factories that are already out there on the internet. And so maybe you guys have heard of the strong DM use case. So strong DM is a company that they actually manage a production codebase with a dark factory. They are shipping pull requests all of the time that don't have any human review at all. And their dark factory is unfortunately not open source like mine is going to be for you guys to see and watch it evolve in real time. But they did share something like a PRD. So they have this open-source spec for building their dark factory. They call it the attractor. And so we don't have the codebase, but we do have the plan document that uh I guess theoretically you can use to have your coding agent build out exactly what they have for managing their code base with no humans involved. And so I I did actually take a lot of inspiration from the ideas here. If you guys are interested in any of this, I'm planning on putting out a YouTube video tomorrow where I'll have like a more concise overview of everything and I'll have links to this all. I can of course put links to this in the chat, too, if you guys are curious. So, um I will put a link to this blog post right here and then u I'll put a link to this resource covering the uh dark the strong DM dark factory if you guys want to read through it. Just want to make sure I give those to you guys because that's a lot of like my initial research for building a dark factory and I'm super fascinated by this. So, okay, let me be really clear here. I want to be clear on something and then I'll explain more the the architecture that I have for my archon dark factory. I know I already said this but it's worth repeating that you're not going to get the most reliable results with your coding agent when you give it this much autonomy. I highly recommend when you're doing things for real, you put yourself in the loop. At least reviewing plans and reviewing code. those two stages of the development cycle. I would at least have those. So, this is definitely a public experiment. I'm calling it an experiment because it might fall completely flat on its face. We'll see. I mean, I'm going to put a lot of work into trying to make it really reliable, but I have no idea how the codebase is going to end up evolving when I leave it to literally manage itself. And so, the input for the dark factory is going to be a GitHub issue. So I as a user and then I'm going to make this public so you guys can literally submit GitHub issues as well. It's going to be so fun when I get this really running. The input is a GitHub issue and so this is either a bug that we've noticed in the platform as we've tested it as a user or it's a new feature that we're requesting the dark factory to add into the codebase. So we create a set of GitHub issues like maybe there's you know 20 that are created in the last hour something like that and then on a schedule basis I'm going to run the first archon workflow and calling it the triage workflow because the responsibility of this archon workflow is to look at all of the GitHub issues and it's going to judge the issues against the core governance layer that I'm going to build into the the um dark factory repository. So, we're going to have our our mission for the repo and then the different rules. And these files are going to also include the scope that we're going to allow for the codebase evolution. Like here are features that we're definitely not going to allow. Here are types of features that we are going to allow. So, basically the triage workflow is going to evaluate all of the GitHub issues that were created in the last hour, you know, like everything that hasn't been triaged yet. And it's going to figure out like, you know, based on our mission and rules, what issues should we, you know, put in a comment and close and say like, hey, this doesn't apply for X, Y, or Z reason or here's an issue that we're going to go into the implement step. So, triage and then we're going to have a separate archon workflow that goes through the full implementation. So for every single issue that we decide we are going to address, we're going to invoke Archon workflows in parallel to do the full implementation. And so again leaning on the beauty of archon here, we can handle any number of issues in parallel because it each of the issues are going to be handled in a a work tree. So we have full isolation, full copy of the codebase for each one of the issues to be worked on independently without stepping on each other's toes. So we implement and then for every single one of the issues that we addressed either a bug that we fixed or a feature that we built we're going to have a separate archon validate workflow. So this is where we do the PR review before we do the merge into main. And one of the things that strong DM implemented in their dark factory that's very powerful is um what they call the hold out pattern. So the hold out pattern is the idea that we don't want the bias from the implementation to go into the testing. And this is such a prevalent problem with coding agents in general is they will uh if you ask it to check its own work, it's like asking a student to check their own homework. They might, you know, give a little bit of feedback just to seem like they're they are being critical of themselves, but in the end, their bias is going to win out and they're going to stuff the bigger problems under the rug. And so what we do is a handoff. After the implementation, we go through all of our testing scenarios, but we don't tell the validation agent what was just implemented. So we basically just do regression testing over the entire system. So that way there's no chance of bias because it doesn't even know like what the issue was meant to address. [clears throat] And that sounds kind of risky and like honestly myself I'm not fully convinced of this but that that is strong DM's hold out trick and we're going to try building that as well. That's why we have a separate workflow for validation and we don't just have it built into the implementation. Now in archon you can just like you know start fresh sessions between nodes. So I guess we could package this up as one workflow and still have the hold out pattern. Um, that's one of the things I'll just kind of have to explore as I'm building with you guys. Like I'm setting a lot of this up from scratch. Like this is a live coding session. Like I said, I'm not presenting something that I've already built like I did with Archon in the last live stream. So yeah, uh, that's pretty much the workflow here. So I mean really it just comes down to we have the governance layer. These are pieces of context we're always going to inject into every Archon workflow. And then we have Archon workflows to handle the full orchestration here. triage, implement, validate, and fix. And as far as the repository that this is going to operate on, it is going to be uh this one right here. So, obviously, I'm not going to use archon to work on archon here. I don't want to turn archon into a dark factory repository. It is too important that that this doesn't just become an experiment. So, there's a separate repo, a separate project that I'm going to build using the archon workflows in the dark factory. And uh it's actually a pretty cool um application like this is going to be a huge value ad for my YouTube channel because essentially it's going to be a chat platform and a gentic chat platform where you can ask it any kinds of questions around AI and then it's going to perform rag. It's going to search through my YouTube videos to give you an answer. So it's kind of like your own AI tutor based on my content. And then I was also thinking about doing something for the Dynamus community. If you are in the Dynamis community, you can connect your account into this platform. So then not only would it search over my YouTube content, but it would also search over my workshops and courses that I have in the community. So it become like the ultimate AI tutor. So it' be like available to everybody, but then it'd be even like a nice value ad to Dynamis as well. So I'm actually really excited to build this out. Um, and so if the dark factory experiment doesn't work for whatever reason, um, and like I have faith in it, but it is very risky. Like so if if if it doesn't really like build on anything that like works super super well then I'm just going to you know build it myself with my usual AI coding process because I want to have this by the end of the month for everyone. Uh but we'll see if a dark factory can manage everything because I'm going to work hard to build that initial AI layer. U let me actually refresh here because I I already created the mission factory rules in claw.md. So I'm going to work hard to build out the the [clears throat] governance layer, build out the archon workflows. I want to make this as reliable as possible. Now, the biggest risk that we have to this dark factory is that I can't actually use my anthropic subscription because I would hit my rate limits way too fast. And if I want to uh make this public so anybody can create GitHub issues for the dark factory, I believe that would be against the anthropic terms of service. if I let other people's GitHub issues get automatically consumed into the system because then it's essentially other people being able to use my anthropic subscription because I'm not the one starting the workflow. It's like technically another user I think. I just want to be careful there. And I'd hit my rate limits way too fast anyway. So I can't actually uh use my anthropic subscription for the dark factory. And so what that means is I have to pay for an API. I have to pay per token for everything I have built in this that I'm going to build in this dark factory. And u unfortunately opus would be way too expensive. So I have to resort to other means and actually what I came up with is I'm going to use Miniaax M2.7 as the large language model driving the entire dark factory. Now, um I've done a lot of research for different models. I considered um Quen 3.5 coder. I considered GLM 5.1. I thought about maybe using like Sonnet, but Sonnet would be too expensive. Um I was maybe going to use Sonnet through Open Router or just the Enthropic API directly. Haiku would definitely be not powerful enough. So, I I can't really use an anthropic model, right? Because like Opus and Sonnet are too expensive. Hi coup is like significantly worse than miniax m2.7 and they're actually a pretty similar cost I believe. Um yeah because like if I go to open router here and I search for claude haiku 3 or 4.5 it is um $1 for every 1 million input tokens. It's actually more expensive than um miniax m2.7 that this it's less than a dollar. Yeah, it's only 30 cents for every 1 million input tokens. So, it's a third the price of Haiku and way better. So, there's no reason if I'm not going to use my Anthropic subscription, there's no reason for me to actually use an anthropic model because Opus and Sonnet would be way too much. And so, yeah, I I did a lot of research and this is what I landed on. And I can always switch the entire system. But what I've done here, and this is part of the setup that I've already taken care of automat or behind the scenes, is I already have a VPS spun up where I have archon installed. I have the rag YouTube chat application cloned and and configured. And then I have my cloud code changed there to uh use Miniax M2.7 instead of enthropic. So if I ask like here uh give me the SSH command. I'll actually show you guys. I'll SSH into the machine live with you and show you what it looks like. So all right, I'll grab this command here. All right, cuz uh take a look at this. If I go into claude, I [snorts] open up Claude while SSH into this machine, you can see that it's using Miniax M2.7. And if I say, you know, like what model are you? Everything looks like I'm using Claude, but uh or that I'm using Claude code normally, but it is actually going and and using my miniax API key and running on M2.7. And by the way, if I wanted to use like GLM 5.1 instead, it would be super easy. Like I could swap over in like 30 seconds. Uh because all you have to do to swap the provider for cloud code is you just have to change a couple of environment variables under the hood like and and by the way this session that I have open with cloud code this is on my local computer where I'm doing some setup locally and uh what I had in this session I had it read my whole dark plan. So like everything you see right here it has loaded into the context currently. So I can just ask it here. Uh don't show any secrets but tell me exactly how I changed claude code to use miniax m2.7 instead of anthropic for the model. Um so I I might actually open source my entire dark factory plan cuz as I've been setting things up behind the scenes, I've just been like documenting everything in this like pretty massive file here, including all of the archon workflows that I'm going to build with you guys live right now. So, I have a a plan initially for every single one of these. So, we'll build them today and test them and maybe get to the point where we have the whole dark factory running. I'm not sure if we'll get that far because it's going to be quite a bit of setup. Um, but yeah, you can see that uh for switching the provider for cloud code, you just have to set these environment variables there. There's quite a bit here. So, I think it actually would be pretty useful to share this with you guys. uh because there were there was a it was a little bit trickier than I thought it would be to switch the provider. Uh because then you what the other thing you have to do for archon is you have to map the environment variables for the different model types because in archon you know for each of the workflows you can specify like for this node I want to use sonnet or this node I want to use haiku and so to make the archon workflows work out of the box without having to change these ids you just have to map it through environment variables. So like when I specify opus and claude code or in an archon workflow that maps to miniax m2.7 same thing with sonnet and then if I want to use haiku then it maps to miniax m2.7 high speed right so just a faster and cheaper version of m2.7 so I have the same effect in an archon workflow where I can make some things a lot faster and then other things I have the most power I possibly can um like if I typically would use opus or maybe sonnet So yeah, if you are interested in using claw code with a different provider, it's actually quite easy to set up. So you could have it use open router if you want to use the enthropic models there. Um GLM has an enthropic compatible endpoint. Um of course miniax does as well. I think Quen does. Does does Quen have a Claude code compatible endpoint? And if you want to run local models with [snorts] cloud code, you can use Olama as well. So Olama has a direct integration with cloud code. So it's kind of cool because we are planning on adding PI support this week for archon. So you can run all of your workflows through PI agents. But even right now, you are able to uh immediately switch cloud code to use any models so that you don't necessarily have to lean on another provider, but you're not stuck to using your anthropic subscription or the anthropic API key. Okay. Um let's see. Yeah, I don't think Quen has Okay. But like GLM and Miniax have the anthropic compatible endpoints. So yeah, just ask Claude to do some research for you to see like which ones are compatible with Claude code, but most models you're able to use directly like I set up with Miniax here. All right. See what it says here. Yep. So yeah, GLM has a first party anthropic compatible endpoint. So it's like literally their API endpoint and then you just add anthropic at the end. So that that's what you hit when you want to make it compatible with cloud code. So pretty cool. was pretty easy to set it up. All right, cool. So, uh, yeah, I want to get into building with you guys here. Let me check the context. Maybe I'll spend a little bit of time to answer you guys' questions. I know I haven't really looked at the chat yet. Definitely want to do that. So, I'll I'll spend a little bit of time doing that and then we can get right into building out our factory. So, going to the diagram here. I already have the governance layer built out and then as I'm creating the workflows I'll show you guys what that looks like. So right now I mostly just need to build out the archon workflows and it's important for all the archon workflows to like actually ingest these documents here. Like it needs to know like no matter what workflow I have running if I'm fixing something, validating something, whatever like it has to always know the mission and factory rules cuz that's going to be the primary guidance. And then I mean of course the global like the claw.md as well. So yes I am doing everything through cloud code but um I mean you could easily make this dark factory do like use codeex or open code or pi instead but yeah it's just what I'm using. I like using quad code as a harness even if I'm not using anthropic models. All right cool. So yeah, I'll leave this up and then I'll I'll go ahead and hit some questions from the chat here. And the future begins. That's right. That's what we're building. We're building the future here. I don't think that that uh the Dart factory is a pattern that's reliable enough right right now. But if we refine the workflows enough and if we have we'd probably need more powerful models as well, honestly, to like really make this production ready. But maybe Mythos is going to be the unlock. We'll see. All right. I'm level 11 or negative one. Not from a tech background at all. I mean, that's all good because uh with how powerful AI coding assistants are right now, you can get to level three very very quickly. And in fact, if you don't have a tech experience, you probably won't ever be level zero through level two because that requires you to write code yourself sometimes. And so these days when you learn how to leverage AI coding assistance and you're not coming from a technical background, you just jump right into level three. My big recommendation with that though is to ask your coding agent a lot of questions as it's creating code for you so that you can start to gain an understanding and like you know sort of become at least semi-technical yourself as you're using the tools. Um will this video be saved for later? Uh 100% Leonards. Yeah. So every single live stream on YouTube is automatically turned into a recording after. So I don't even have to like upload it myself. And so I think it takes a little bit of processing time, but like what we have right here, it says live right now. It'll be turned into another video just like my live stream this weekend. So you just have to go to the live tab. It's not in the main video tab for my long form content. You just go over here and then it'll be available for you. All right. I still feel like I need to test things myself. I don't yet trust AI to test and especially ship. I'm with you there. Yeah, like I said, level three is where it's at when you really care the most about reliability. Unless you've built some kind of level four harness that you really, really have faith in, I would generally recommend sticking to level three. And then level five is like no one really knows how much this is really going to work at this point. And that's what I want to find out with you guys. Like, yeah, we have examples like strong DM, but they haven't they they've not really shared that much, right? And like a lot of it could just be like marketing hype. So, that's what I want to figure out for you guys for real is like if we actually put a lot of effort into using Archon and uh building a lot of reliability through a government's layer. Like, how reliable can we really make it? And I'm excited to find out. We're going to do it together. um you don't trust that if it's secure more than everything is working. I mean okay so sorry this is the question to follow up from the other one but I mean I I would say personally that like security is a big concern for AI coding assistants. They do introduce more security issues than uh seasoned engineers. um they can valid they can fix them as well but like first pass they introduce more um and then yeah just like generally that everything is actually working cuz okay here's the other problem with AI coding assistance and then honestly probably the main reason that level five might fail it's not necessarily that the coding agent produces code that fails but it's more that it's just not aligned with what you want to create and that's part of why I'm going to be focusing so much upfront on building the government's layer because I need to be very clear on the guard rails and the guidelines for the coding agent so that when it picks up an issue and implements it uh first of all I want to make sure the issue is actually aligned with what I want for the codebase for the evolution of it and then also like when it does the implementation itself that it doesn't misunderstand what the issue is really getting at like if I open an issue because I want to improve the rag search I don't want it to like change the front end I want it to just like change the rag pipline line for example. All right. See what else we got here in the chat. Um I presume the dark factory can introduce bugs later down the line if proper unit testing linting and bug fression system is is set up correctly. Um, so yeah, that's going to be one of the risks of the dark factory as well as there might be little problems that creep in that our validation doesn't catch and they might blow up in our face later on. That's one of the reasons human in the loop is so important for reviewing things is to catch those little issues that become a bigger problem later. U so the dark factory could kind of be like boiling a frog in water, right? like the frog. If you put a frog in scalding hot water, it's going to immediately jump out of the pot. And so the analogy here is like if we have a massive issue in the codebase right after implementation, the validation is going to catch that and it's going to address it. But if it's something that slips under the crack cuz it's not super apparent right away, it's like the frog that you put in warm water and then you boil it over time and so it stays there until it's dead, [laughter] right? Like that could happen to a dark factory. you have the these little issues that creep in over time. It's not big enough for the validate agent to catch it, but then they combine together to produce bigger problems or it's just an issue that compounds on itself and you're not there in the loop to find those things and correct those things. So it's certainly possible and uh as much as we can that's why it's it's important for us to build a very comprehensive validation process not just with unit testing and linting but I'm going to be building in like full regression testing like every single time we handle an issue I want the validation to use a browser automation tool to go through the rag chat application like just like a user would and u like test this whole interface and have different conversations and click on the source ources at its sites and make sure that goes to the right part of a YouTube video. Like I it's got to be doing everything and constantly kind of like maintaining this list of features that it needs to test every time it's doing proper regression testing. So we'll get there. That's going to be probably one of the biggest challenges to build for this whole thing. All right. Um, also will be handy if you can suggest open source or free alternatives if available out there for the tools we're using. As a learner, those crazy bills make my heart sing. I'm with you. I understand the pain for sure. So, I guess I'm curious like what tools you're referring to exactly. If you're talking about AI coding assistance, unfortunately, there's not really a a free alternative to something like Claude Code that's just as good as Claude. Like I was talking about earlier, I'm using Miniax M2.7 instead of Opus because it's a lot cheaper. It's still not going to be as powerful. And if you really want like free AI coding, then my recommendation is to run a model in Cloud Code through Olama. Like you could run Gemma 4. Um Quen 3 has some smaller good models. You're not going to get nearly as good of results as Opus though. But like it is possible to do AI coding free. you just have the expectation that um you can't do the same things that you can do with Opus or some other more powerful model like GPT 5.4 for codeex in codeex for example. So all right let's see got only one year to experiment. Oh let's see the comment above. I'm thinking of creating some kind of architecture for local businesses here if I can and provide them. So got to be safe easy to set up and manage for them and myself and I don't get sued. Yeah, I'd be curious what kind of architecture you're talking about, like if it's an agentic system or if it's um like if it's an AI agent or like for AI coding. Sounds cool, though. All right. Gemini makes a good evaluator to run against Claude. Yeah, that is one of the things I want to be experimenting in with archon soon is building workflows that combine providers so that we can do like exactly what we were describing like claude for implementation and then Gemini a lot of people like using codeex for review as well just to to have a check on claude uh so yeah that's going to come soon for archon all right cool Um, was that excaladraw in Obsidian? Yes, my Excalad draw diagrams I always have in Obsidian. So, I'll show you that really quick. If I go to the settings and go to my community plugins here, I use I just use the Excal plugin by uh Z Sult. I don't know if I'm saying [laughter] that right, but yeah, I've used this for a long time now. Very, very good cuz I just want to have everything in my vault together. Diagrams, research, everything. So, I love using this plugin all the time. All right, cool. So, a little paywalled after all. Let's see. Right. For AI coding, if you want to get the best results, it is paywalled right now. Um, and I mean unfortunately it makes sense like these frontier models like Opus and GBT 5.4 Codeex, they are expensive, man. Like these companies are burning through billions of dollars of venture capital right now just to have these models running for the world and they're just starting to like make some profits from getting it like the higher levels of enterprise agreements. Um because trust me, they they don't make money off of your anthropic subscription if you are really maxing out your rate limits for claw code. Where they're really making the money is using you as the lever to get the enterprise agreements, the enterprise interest. So they're they're profitable, but it's it's very subsidized for our anthropic subscriptions. And that's part of why they're jacking down the rate limits right now. It's kind of unfortunate. It's uh I am not get I'm not able to get nearly as much out of claw code with my anthropic subscription compared to even like a couple weeks ago. Um the rate limits are are worse now unfortunately. And they took away my 1 million token claw code. That's another thing that I'm kind of frustrated by. Um, like if I if I do slashmodel, apparently some people still have this, so I don't know why it's just me, but I don't have the option to use a 1 million opus or or sonnet anymore. So, I'd be I'd be curious if anyone else has run into this as well, but I'm stuck to 200,000 tokens again as of like just three days ago. I don't know why. Or maybe it was like a week ago. But [sighs] yeah, anyway, so yeah, I'm gonna have more time to answer questions as we are waiting for the uh workflows to be built here. Uh, one thing I want to put in the chat quick is just a link to Archon. So, if you're interested in checking out Archon, like got some good content on my channel. Uh, I got the live stream from the weekend and then also I have the YouTube video that I put out just five days ago on Archon. So check that out if you're interested. Like I said, because I've already done so much content, I'm not going to be like hyperfocused on explaining Archon, I'm going to get quick, pretty quick here just into doing [snorts] a live coding session creating the Archon workflows with you guys. Um, and then also the repository that I'm using the dark factory to build this is private for now. Um, well, no, actually, I made it public, but I'm not going to make it so that you can give any issue to the dark factory yet. So, I'm going to start by having it only accept issues from me. And um, then I'll make it so it's available to everyone after I've like tested things for about a week is my plan. Something like that. In fact, I might actually want to make this repo private right now as I build this as a safety measure. We'll see. I I might have to switch it private and tell them I'm confident that it really is only handling my own issues. [laughter] So, we'll we'll have to do that in a little bit. But, let's start by building the Archon workflows here. Okay. So, in my chat, how much do I have? Okay, I have 40% of my context used. So, I should be good to continue here. So again, this conversation that I have, it already has my full dark factory plan loaded. And so I can literally just ask it like what should I build next? Because I've been keeping a log of everything that I've created as I built it. So like for example, one thing that I already did is I created the core government's uh doc governance documents. So I have like my mission.md factory rules. I can show that to you guys like a little bit of what went into that um as the workflow is building. I just want to be efficient with the time here. All right. So, so there's some things that I was doing during an event in the Dynamis community. And then uh here's the remaining punch list from section 14. I told you it's comprehensive. Section 14 of the plan. uh ordered by what makes sense to build now and save for live. Okay, so I guess there's a couple of things that it recommended that I do before the live stream here, but also these are going to be super quick to set up anyway. We need to create the GitHub labels, um the issue and PR template, orchestration shell script. Yeah, I'm going to Yeah, I'm going to have it rip through all these things in parallel. So, okay, the GitHub labels are actually kind of interesting because everything in the dark factory is going to be managed through labels. So, when the triage workflow runs, it's going to basically check on these labels as a status like this thing is currently being implemented, right? like don't don't send off another Archon workflow to work on this because it's already in progress or worst case scenario if it fails to implement a pull request two times in a row I'm going to have it label needs human so maybe I'm not making this like fully fully dark factory but I do want to at least have like a small escape if I really need to address something myself so I have a little bit of a system created for that and then uh yeah like if I reject an issue like this doesn't fit with our mission or if I approve it and we're not going into implementation yet, then I'll add that label. Um, and then factory rate limit. I'm going to have some protection to make sure I don't blow through like hundreds of dollars of miniax credits in a day. And so if we need to wait for the next day for the rate limits to subside that I'm going to build into the system, then we'll add this label as well. So yeah, it's hard even in a live stream to get like super deep into everything that I planned here. But I hope that you can see from the the label system that I have for these GitHub issues like there's a lot of thought that I put into this system even handling like rate limits and human escape if I really really need it. Um, so yeah, really like the important thing here is the GitHub issues are driving the entire dark factory because any kind of input into the system for a bug that needs to be fixed or a feature that needs to be created, the input comes in from an issue, whether that's me creating it or the dark factory itself creating the issue because we do also have a sort of feedback loop here where when the validation agent runs its regression testing, if it encounters any problems that are big enough to not just be fixed right then and there, then it'll create a GitHub issue and then go through that loop and then address that and so anything that it catches in regression can just be more issues for it to fix autonomously and uh so yeah I mean like hopefully doesn't mean that we'll hit infinite loops of creating issue and issue and issue after issue but might happen that's part of the experiment we don't we don't know what's going to happen or what could go wrong uh but that's why I have protections in place to make sure that it doesn't um just jack me up in credits so yeah like When I I have my balance here, I I only put like 25 bucks to start and then I've used like, you know, 87 cents in my testing so far. It's pretty efficient overall, but I'm going to make sure that I um yeah, never have like too much. like I'm I'm disabling auto billing so that if I run out of credits, I just have to manually u add credits and then I'll have the system that like detects when issues weren't handled because of rate limit and it'll pick it back up basically. Um, okay. So, I'm going to say, uh, so I'll go into my speech to text tool and I'll say, I want you to create the GitHub labels, issue and PR templates, and, uh, the orchestration, shell script, and cron entry on the VPS. So, handle all of these right now. I'm actually in the middle of the live stream now. And so, I will just explain the workflows briefly as you do these things. All right, there we go. It still thinks that I'm not in the live stream yet. So, I'll give it an update of of where I'm actually at. [laughter] Claude Code doesn't really have a sense of time. Okay. So, while that runs, who's paying for all this quota context? I'm paying for it. It's It's coming out of pocket, which is why I'm using something very cheap like Miniax M2.7. Yep. Okay. So, let's see. Okay, let's go back to the dark factory plan. I want to show you guys a little bit of what the archon workflows will probably look like. So, what I have here, these are very much rough drafts of the archon workflow. So, when I actually build them in a little bit in our stream here, they might end up looking quite different. But when I was doing my initial planning with claude code, creating this whole dark factory plan, I also had it load the primary archon skill. So it knows how to build workflows. It knows the different parameters, things like that, how to use the archon CLI. So it created the initial draft for them. And so there are four workflows that we need in total. We have the triage workflow. This figures out what GitHub issues we actually want to address and it handles the labeling and things like that. And then uh we have the implementation workflow. I have to gosh I have to scroll a while here. We have the uh implementation. Wait, I already scrolled past it. Where'd it go? Where's the header here? There might be some malfformmatting. Oh no, here it is. Um wait a second. Does this do the fix as well? Classify apply decisions. Oh, I think there might be a misordering here. So, okay. Anyway, we also have the validate PR workflow. So, this is what we're going to run that we're going to do the whole like hold out pattern for validation. We're going to run this on every pull request that's created from the workflow that does the issue fix. I thought that would be the second one. That's why I'm confused right now. Um, I'm not sure where that maybe that maybe it just misordered things. So, oh, oh, yeah, it did misorder things. Okay, that's kind of weird. But anyway, this this should be the second workflow. I don't know why Claude put it in the plan in this order, but our uh next workflow is the one to actually fix. Um, no, no, that's not it. This is this is a workflow to fix issues that happen during PR validation. So if there there are any problems that come up when creating the poll or when reviewing the pull request, then we run this to address things and then push a new change to update the poll request. Um and then we have the comprehensive test. So this is the regression testing workflow. And this one is going to take a lot of tokens. So, I'm planning on running this one only like once a day or once a week because it's going to look through every single possible user journey, every single way we can use the application, testing every single edge case, making sure that it works automatically. And then for any things that don't work, it's going to create a GitHub issue, right? So, every time we review a pull request, we are going to do a lot of regression testing, but it's going to be a more concise version of this workflow because this is going to be like pretty tokenheavy. And then yeah, I guess the one thing that it didn't do is it didn't create the workflow for actually fixing the issues. And um I I sorry, I remember now why that's the case. It's because there's a a default GitHub fix issue workflow in Archon that I'm just going to use or maybe make a little bit of an adaptation for, but then for all the other workflows, they have to be created from scratch. So I apologize. I Claude kind of confused me here or I forgot the planning that I did with it. But yeah, we'll get into creating the workflows in a second here. Okay, cool. So, all three tasks are done. We created the GitHub labels and the issue templates and then we created the orchestrator. So, we're we're basically going to create a cron job that runs on our VPS every so often. And whenever this job triggers, it's going to uh basically prompt Claude to use the Archon CLI to invoke the workflow. was like, "Okay, it's time to triage our issues or it's time to uh yeah, see this is the default one. It's time to fix the GitHub issue or it's time to validate the pull request. So, we can go to the GitHub repository here and actually check this out. So, if I refresh uh well, here I'll just go to an issue. And if I look at the labels for the issues, you can see that we have all these labels now. Factory accepted, approved, in progress, needs fixed, needs human. And if we look in the GitHub folder, we can see the pull request template. We want to make sure that as the dark factory is operating, it has a set standard for what goes into every single pull request description and every single issue description because being as consistent as possible is one of the best ways to actually make this reliable. So we have one template for when we're filing a bug, one for when we are uh you know requesting a feature. So, if I were to actually go and open an issue right now, uh it asks me is this a bug report, a feature request, or should I just create it from scratch? And we're only going to uh allow maintainers to to do this type. So, if I click on a bug report, then you can see that it automatically populates this form that's defined in the template that Claude Code just built for me. So, now we have some structure. we're enforcing certain things because we want to make sure like if I'm going to have this as a public experiment where anybody can open a GitHub issue, I I need some kind of expectation set for what information you're providing. So, we have these required fields. So, that way there is actually enough context for the dark factory to address the problem. And if a template's not used, then I'm just going to instruct the dark factory to automatically comment and close the issue. So, we're going to be pretty strict on that. All right, cool. So, uh, now we want to actually build our workflows here. The thing is I'm pretty low on context. So, I might start a new conversation to do this. So, I'm going to just say uh I'm going to build the archon workflows in a separate context window. So, just go ahead and update the plan with what we've just done here. And, uh, then I'll go into a new cloud code session to build the archon workflows. And while this runs, I can just open up a new Claude code and do that. So, let me close out of here. Open up a new Claude. And I'm going to copy the path to the full plan. I'll just put it at the start of the prompt here. And then the other thing is uh hold on, me close out of this. The other thing is I want it to load the archon skill because I want it to the archon skill that I have uh it gives a full reference to cloud code uh how to build archon workflows and best practices for doing so. And so I'm going to say uh read the entire dark factory plan that I gave you the path to. We are now going to work on building the archon workflows. And I want to start by building the triage, the dark factory triage workflow. So I also want you to load the archon skill. Um, so you understand all the best practices for building archon workflows. Then I want you to give me a summary of your plan for the triage workflow. all the nodes, what models we're going to use, what the prompts look like, and I want you to just like have a conversation here iterating on the ideas for the workflow before we actually build it. All right, so we're going to do a little bit of a piv loop. If you have uh gone through the agent coding course in Dynamus, you know what I'm talking about. We're going to do some exploration, some planning up front, and then we're going to create the workflow and test it. I don't even really know how we're going to test it exactly, but I'll I'll ask for its uh recommendations once we have it built because I might need to kind of like get the dark factory set up incrementally. Or maybe I need to like really run the triage workflow on the issues I already have in the repository here and just like see what kind of labels it adds and if everything's working. And then I'd probably have to ask it to also like undo all of its work so that we can still have like a blank slate of issues that aren't aren't muddled with yet. So, we'll see what we have to do once it once it builds it here. All right. Mini max is designed to mini max out those credits. I hope not. We'll see. I I'm down to switch something else like GLM if I need to. All right. Auto billing. It messed up last month. never doing it again. Okay, that's too bad. I will keep that in mind to probably not do that myself. Um, use the Miniax subscription gives good value for money. Okay, cool. Yeah, I don't know. I probably like if I really want to scale this experiment, I don't think I can use any kind of subscription because I'll hit rate limits, but that's good to know because I might. I use Miniax on Olama. Testing it now. Okay, that's very cool. Yeah, I mean I'm using a the biggest version of Miniax. I don't think that would really be realistically self-hosted. Like if I look up Miniax on Olama. Um yeah, they don't even offer you to install this yourself. It has to run through the cloud offering in Olama. But I I believe if you look up like um there are self-hosted options. You must be running something self-hosted, right? I just look up Miniax. Um, oh yeah. So, oh, maybe you are running the biggest thing cuz you I guess there's like local options. This has got to be huge though. Yeah, that's massive. 148 gigabytes for the main thing. And then if I if we were to look at a Q4 quantization Oh, wait. It's still 150 gigabytes. That doesn't seem right. But yeah, it's a 230 billion parameter model. I'm not running that on my computer. I'll tell you that. All right. Am I using local models for this? Nope. I'm using Miniax. Well, I mean, you can host Miniax yourself. So, it's an open source model, but I'm using it through the Miniax API. Uh, thank you very much for the donation, Jiren. Appreciate a lot. building a dark factory because even the machines refuse to work in light mode. Right. That's a good one. That's a very good and thank you for the donation. I appreciate it a lot. Uh when using Archon, is it needed to have bypass permissions for cloud code? Uh yeah, because you're running the Claude agent SDK under the hood. It's meant to be fire and forget, right? Like you're not supposed to babysit archon workflows. There's human in the loop built in, but that's a different thing. So I would use it like you can limit the permissions of claude when archon runs through hooks and if you really want to like create a settings.json JSON and manage permissions there. You can do that as well. But uh yeah, usually I just do like YOLO mode when I'm running Archon workflows and then I have like hooks that prevent reading from ENBs and removing directories and working outside of my uh designated codebase like the work tree that archon creates. All right. Uh we have eight H100s. Soon to get H200s. That is very, very cool. I'm jealous. [laughter] I do not have an H100. Uh, certainly not eight of them. That's awesome. Yeah, you're going to be able to run Miniax for sure. I think you could even run GLM. How big is GLM? I don't even know. Um, let's see. GLM is 744 billion parameters. If you have eight H100s though, I you would I think you'd be able to run. Can you run GLM 5.1 on eight H100s? I think you can. Like it should be decent. Yeah, because each one is 80 gigabytes of VRAM. You're sitting pretty pretty there. Um I mean you might still need to quantize it potentially. 12.4 4 tokens per second on HH 8 H100s. So it's not like super super fast, but uh that's still very cool. I mean that's that's impressive. All right. I have not even a 100th of an H100. Same. Yep. [laughter] Those are expensive. Yeah. So yeah, 640 gigabytes of VRAM. So yeah, you you I think you would definitely I mean you'd want to probably quantize to get good results, but still insane. All right, cool. So anyway, let's go back to our coding agent here because it came back with the summary. Okay, I've read the Dark Factory plan section 4.2 on triage specifically and the Archon workflow authoring guide. Here's my proposal designed for the dark factory triage before we build it. So our goal here, this is important for us to all understand, is to batch classify untriage GitHub issues against the mission and factory. So these core files that guide the scope of work and things we're going to actually care about and things we won't and then apply the labels and comments deterministically. So Claude makes the decision or I should say Miniax makes the decision, but then we're going to have a deterministic steps in the workflow to automatically label and comment just to make sure that everything works the same way every time we run the triage. So we're going to run the orchestrator or runs when the orchestrator detects open issues with no factory label. So the orchestrator is the cron job. It runs every so often and when it sees that we have things that don't have a factory label, that means it's a new issue that our triage workflow hasn't looked at yet. So, okay, we have five nodes. We're going to uh fetch the issues in parallel, fetch the rules. So, we're going to read in the mission and factory rules and then take a look at the pull request list because that'll also help us determine what is already in flight, which this doesn't really make sense because I think we should be able to rely on the GitHub issues alone to figure out what's already in flight. But maybe this is just like a bit of an extra safety check. So, I guess it doesn't really hurt to have it. But anyway, so layer one, we'll do our classification. So it says sonnet here but remember we have it configured to route to miniax when we specify opus sonnet or haiku in the archon workflows. So it's going to classify each one of the issues and then we're going to have a bash step. So a deterministic step that will take in the JSON array of decisions that we have from the structured output from cloud code and we're going to loop over the JSON and then use the GitHub CLI deterministically to apply the labels and then also the comments to the issues as well. Okay, so we we have uh bash steps. So we're not using AI for layer zero as well, right? Like we just run the GitHub CLI to search through all the issues. We fetch the rules, get the open pull requests. It says optional but useful. I mean, it's fine. I guess we can keep it. And then classify the plan explicitly calls out scope judgment against a written mission requires nuance. Haiku often fumbles or in our case the high-speed minia max would fumble. That makes sense. Cost is low since we run on less than 10 issues per batch in one call. Fair enough. Um okay. So you can see that one of the things we support in archon workflows is defining the exact output that we require from the model. So this is like structured output with more classic agents if you guys have dealt with that before. But the point of this here is that when our coding agent goes through the classification process, we need a standard. I'm going to keep saying this throughout our live stream here. Everything is all about standards for reliability. We need a standard for the coding agent. It needs to communicate in the same way every single time. Uh how we're going to label the issue. So it's going to output an issue number the verdict which is going to be either accept reject or needs human. It's right because need human that's our fail safe if it has failed to address the poll request multiple times. The priority and then the classification bug feature enhancement chore or docs that is good enough for me. And then we have the prompt skeleton as well. So just telling it like when it goes through the classification what it's actually doing. Um, and then what the script is, the bash script is going to look like to actually invoke the GitHub CLI to label and comment on things. And then it's got some open questions as well. Um, okay. So, let's go ahead and answer these questions. So, a batch size of 10 or five. Let's do a batch of 10. And then help me understand like if we have actually opened up like 30 issues since last time the orchestrator ran is it going to loop in archon or what does that look like? And then should triage ever label without closing on reject plan says close rejected issues without with explanation. Um yes we should definitely close issues when we reject them. Yep. Priority labels on need human currently I applied them. useful so you can see at a glance which human review issues are urgent. Yeah, I think that they are definitely worth applying priority. Also help me understand how is this triage workflow going to know that we need a human, right? Because like we talked about in the plan how once the workflow or the pull request has failed twice on an issue, then we would say need human. So like what does that look like exactly? Okay, man. These are some tough questions. Should I include a type star label or just lean on the existing GitHub issue labels? The plan doesn't mention type labels explicitly. I'd add them. Sheep signal for later filtering. Sure. Yeah, we can add them. And make sure you update the dark factory plan with that decision as well. Duplicate detection scope. Right now, the classifier sees open PRs and current uh issue batch. Should it also see recently closed issues to catch repeat reports? costs more context but catches more duplicates. Um, I would say we don't really need this because if we rejected an issue before, we'll probably just reject it again. So, we don't have to spend the context to look through recently closed issues. Um, do mission.md and factory rules.md exist in the target repo yet? The answer is yes, I did actually create them. They are on the main branch. Uh, target repo path. Which repo are we building this workflow into? The dark factory app repo, right? Not Dynamus engine. That is correct. And actually, I will give you the full path to the codebase here at the start of the prompt. Okay. All right. Woo. That's a mouthful. It asks a lot of questions, but okay. This is good. This is good because this is this is going to be a lot of work. have our work cut out for us when we're building the system up front because every single assumption the coding agent makes is potentially going to be drastic when we're at this level of leverage creating our workflows and governance documents up front. Like we have to be very very intricate here. So, I know that can it can seem like I'm spending a lot of time on this, but man, this is important because if it doesn't understand how to label things, right, or it's not using GitHub issues in the way that I want it to, the whole system is going to fall apart. So, I got to take time. I'm really glad that it's asking me a lot of clarifying questions here. All right, cool. I'm still playing with Gemma 4 on my AMD 395 for local. Pretty cool. Yeah, Gemma 4 is good. Like it is legitimately an impressive model. Uh it is Yeah, one of the most popular ones right now. An old llama. Um I actually haven't heard of this one. Neatron Cascade 2. That's cool. Man, there's so many models, local models I want to try out right now. Um, whoa, the benchmarks actually look pretty good. Live Codebench Pro, it beats, wow, it beats Quen 3.5, 397 billion, and it's almost as good as communicate 2.5, a one trillion parameter model. Seriously, that's kind of nuts. Interesting. kind of want to try this one with the the dark factory. Okay. Well, anyway, I'm getting a little distracted here. All right. Yeah, that's exactly right. Quality work up front makes for some stellar loops, and that is what I'm going for. All right, let's go back to Claude here. Okay, so let me address your two help me understand questions. No looping in the archon workflow itself. The triage workflow is not a loop node. It's a oneshot DAG that processes a single batch and exit. Here's the actual flow. Okay. So, if if we do have 30 issues opened in between orchestrator runs, orchestrator cycle one is going to fire triage workflows, process 10, then exit. Orchestrator cycle two sees work in the high priority lanes first. Only when those are empty does it fall through to the untriage issues exist and run triage again. Okay. U so, okay, this makes sense. So the 30 issue spike does drain across three orchestrator cycles. So we do have to be careful because theoretically if there's like more than 10 issues in like created every single hour then it is going to just kind of pile up and pile up. But I think this is actually okay because I don't that would be unfortunate if there's more than 10 created every single hour. That's going to be so much work for it. Um right. Okay, so that makes sense. We can always change a limit if we want. How does triage know it to needs mark or it needs to mark needs human? You conflated two distinct escalations in the plan. I want to make sure we're on the same page because they're unrelated. Flow A is triage time needs human when this workflow handles the issue itself is problematic at intake. The classifier marks needs human when the issue is in scope but ambiguous, architecturally risky. a product judgment call. Clearly the classifier's decision. Okay. I actually don't like that. I don't if I really want this to be a dark factory, I want it to either close issues or handle them. I don't want it to create this graveyard of issues that need my review when I'm not planning on actually reviewing them. So, okay, I want to be clear here. I don't want to review issues unless there have been multiple failed attempts to address them. And so for flow A, we should just close these issues with a comment. Like if it's ambiguous or architecturally risky or whatever, let's just make a comment explaining that and then close the issue. Um, and then I want you to check the codebase itself to see if it has archon. I believe it does. And then okay, one design requirement I want your okay on for the bash apply decisions node. I'm going to have to classify I'm going to have classify write its JSON output to the artifacts directory. Makes sense as a part of the prompt instructions. Then have apply decisions read the file with jq instead of relying on classify output substitution. The reason being the reason string will contain quotes, apostrophes, new lines and emojis and archons auto shell quoting um into a bash script is a footgun waiting to happen. I mean, I guess I don't Is that really not a problem? I'll have to look into that separately cuz that it might have just identified like a something we might want to fix in Archon. But anyway, writing to a file bypasses a whole quoting problem. It's one extra line in the prompt and a jQ recursive and bash. Sound good? Uh, sure. That sounds good for me. Okay, man. It's getting specific, but that's good. Like, I appreciate how in the weeds it is right now. That's that's what we need. All right, cool. So, I think this is the last thing I need and then I can actually build the workflow. Cool. All right. What else we got in the chat? Thanks, man, for your shared work. You're very welcome. It is my pleasure. I love doing this stuff live with you guys. It's so fun just sharing everything. And, you know, I I was a little bit um I'm going to be honest. I was a little bit hesitant to do this live stream because it it's a bit slower than how I usually roll in my videos and live streams because I'm I'm building something live and definitely at the stage where I'm taking something pretty slow. Like we're not we're not going to have, you know, massive payoffs constantly here. Um it's a slow and steady, right? It's a marathon, not a race. That's what it is when we're building a system like this up front. Okay. Um what now? This is a lot of uh information. Okay. Confirm the execution plan. Okay, makes sense. Scaffold archon. Write the workflow. Validate the workflow. Fix any validation errors and revalidate. This is great. Uh well, actually, yeah, I'll just say this is good. Go ahead. The other thing I was maybe going to ask it is like what's its plan to actually invoke the workflow because when it does the archon validate that's just making sure the syntax is good. So it's sort of like linting of the workflow. It's not going to run it yet and triage issues. But once it does the build then I'll just have a conversation with it and ask it what its plan is to test it end to end. All right cool. I don't think we are too low on context. Yeah. We should be good for it to rip through this whole thing. I wish I didn't only have 200,000 tokens, but oh well. All right. Cool. Can't wait till the Chinese firms use mytho mythos outputs to train their models so open source local can really go stratospheric. Yeah. I mean, I'd be down for that. So, yeah, if they would use Mythos for um synthetic data generation, like they used Opus, that that would be powerful. They're probably going to screw the lawsuits. They're probably just going to do it. [laughter] Yep. All right. Can I do a session on Hermise? I assume you mean Hermes as a new like kind of like open claw alternative. Um, I would consider it. However, I'm more of a proponent of building your own second brain versus using something like Hermes or Open Claw. And you know what? While we're waiting for it to build the workflow here, I think this is a good time to chat about this quick. Let me actually um, hold on. Let me open up a page in my browser quick. I think this is the right link. Yeah, here we go. So, one of the really, really exciting things that I did quite recently in the Dynamis community is I did a 4hour boot camp teaching you how to build your own AI second brain from scratch. And one of the things that I cover there is how you can take inspiration from tools like OpenClaw Hermes without having to build run it yourself. There are a lot of risks involved in running your own or in running a second brain that's not your own application. There's a lot of security problems with open client Hermes, not just in like vulnerabilities in the codebase itself, but even just running something that you don't understand with permissions for your agent that you don't also don't truly understand. So, I'm a big proponent of building your own second brain from the ground up. And that's exactly what I cover in this course. And then I also edit it down into a more polished threehour version that still has like a lot of the good like Q&A in it. So that's in the community as well as the third course for Dynamist. So if you're interested, like my second brain literally saves me 20 hours a week. Like no exaggeration. It's crazy. Like I been running my business for about a year and a half now. Like I know how long it takes for me to do a lot of these things that are like partially or fully automated for me now. And so that's what I want for you as well. That's what I cover in the course. So if that's if that sounds interesting, let me actually put a link to this in the chat for for YouTube quick. We've had a lot of people joining the community recently. It's very exciting for the second brain stuff and also because of archon. Uh a lot of people are going through the course and they're sharing their second brain like their own architecture and how they're molding it for their use cases because one of the things I cover in the course is like here's how you build the foundation of the second brain but then I also talk about how you can you know guide it to help you build your own integrations and skills and other use cases that you have for it even getting into it being like very proactive for you anticipating your needs. So yeah people are sharing their own use cases and things. really cool to see like I'm learning a lot from you guys even in the community itself. So outside of just how I'm evolving it on my own. So very very cool. So yeah, I wanted to call it out really quick. Uh let's see where we are at with Claude now. Okay. Everyone wants to sell a course. Well, I mean I provide a lot of value. I stand by what I what I provide there. So yeah, I don't I don't really appreciate that the the cursing in the message there. Um but yeah, I mean like I it's seriously there's a lot of value that I have and a lot of work I put into creating that boot camp. All right, cool. So anyway, here is what we've got for the workflow. It already built the whole thing. That's actually faster than I thought, honestly. But I guess we haven't really done any validation yet. Um let's see. So, we have our plan updated with the little bit of changes we made to the labeling system and the changes we made to our plan for the workflow. Um, and then okay, so we created the workflow itself. [sighs] A few implementation notes worth flagging. I don't want to spend like too much time reading through this right now. Okay, I think that's fine. What's not done yet? Orchestrator agent fix GitHub issue adaptation. Okay, so suggestion for next step before building the next workflow. Smoke test this one end to end. Create the labels in the repo. File one or two test issues. And um okay, that actually makes sense. But here here's the thing. Um, I would love to smoke test, but I already have some issues that I have in the repository. So, maybe what we could do is we could run the workflow to triage those issues, but then just delete the labels after, so we can bring us ourselves back to a blank slate. So, I want to do the full test, but I I want to like get it back to the original state before I did my testing, if that makes sense. Uh, but you can feel free to like iterate on the workflow and everything before you go back to the blank slate. Okay. So, yeah, I wanted to like actually run it but not like leave a mess of of triaging and stuff because this repo that I have right here, like I want to keep it pure, right, for like when I actually kick off the dark factory and like have all the workflows built. Okay. And then someone asked for me to share the link for what I had open up in Chrome. This is the link right here. Um, cool. All right. Thanks, Cole. This is awesome. I appreciate it a lot. Thank you very much. Thanks, Cole. will join Dynamus. Thank you. I appreciate a lot. Yeah, I'll be happy to have you in the community watching at 5:20 a.m. from New Zealand. Well, thank you for tuning in so early. I appreciate that a lot. Cool. All right, let's see. I I know it's a reference to shooting yourself in the foot, but I've never heard the term footgun. Am I alone? Actually, honestly, Chris, that's a good point. So that's in reference to what Claude mentioned earlier. Uh I guess I haven't heard foot gum either. I don't know. Yeah, I've heard I've heard shooting yourself in the foot a million times. I use that expression myself a lot. But yeah, I guess that's just a shorter way to put it. Cool. All right. I definitely want to join Dynamus, but just bought a house. Fair enough. Well, congratulations, Stuart, on your new home. Why I'm trying to get everything operating free and local for a first run. Then once I have output, I can pay for upgrades. Sounds good. Yeah, fair enough. Yeah, congrats on the house. That's exciting. You're joining as well. Very cool. I appreciate it. Welcome to the Dynamis community. Thanks, Cole. This is super cool. I appreciate it a lot. Yeah, I I appreciate you guys uh finding interest in something where it's like a little bit slower pace as I have to like really spend my time. ideating and and building the system up front. So, yeah, happy to to build this in in public, so to speak. All right, cool. So, let's see. The workflow is currently in progress. Looks good. Um, you know what I I kind of want to do because I'm running this workflow for the first time is I would love to uh view the logs in the Archon UI. So, let me actually ask it. I I don't have it started. I restarted my computer recently, so I don't have it up and running. Start the back end and front end of Archon. This is how easy it is, by the way. You know, you don't even have to run the commands in the terminal or run the containers or anything yourself. You just let it go. So, we'll take a look. Okay. I mean, bun rundev's not hard to remember, but I just like doing that. [laughter] All right. So, let's head on over to Archon. Go to the dashboard. Um, it looks like the backend is still starting. Can you monitor the back end and let me know if it's failing to start? Not sure. I might be on a wrong branch or something. Oh, no. Okay. I think Wait, hold on. Um, why is my workflow not showing? I have these these workflows from way back in the Saturday live stream that I forgot to continue are still running. That's funny. So, they're still paused, but it's not showing up. Where did it is it done running already? Oh, okay. It did actually finish. Huge win and a Windows bug. Let me break down what happened. All three parallel fetch nodes finished. classifier ran in 30 seconds. Decision.json was written successfully. The fetch open PR's node paid for itself immediately. Without the classifiers would have accepted seven issues that are already being worked. What broke is that jq uh failed on get bash for Windows. Oh, that makes sense. Yeah. Okay. So, let's see. Okay. So, it's figuring out a fix here. Caught another bug. Okay. Now, it's running the workflow again. It's cool that it's iterating like little little blips that it's finding, but like I mean, as long as it's able to iterate, I'm happy with it. U yeah. Okay, there we go. So, now we can see the workflow. It's not running, but the one that just failed, it uh shows up here. So, we can take a look at the logs of for the failure. So, yeah, everything is working as intended in the Archon web UI. We just need to fix the syntax for the the underlying workflow itself. Cool. So, all right. Oh, now it's running again. Okay. Very good. View the logs. Very cool. Looking good. All right. We'll see if it works this time. All right. Tail foot gun means that. Yep. Today I learned as well. Eric said the course in Dynamis are outstanding. I'm a career dev and seen a lot of courses. Dynamus courses are exceptional. Yeah, I appreciate it very much. I I appreciate you guys like sharing that especially after someone comes in and just like has to say something mean for no reason which I mean I got thick skin like it's fine. I I understand and and by the way like to to that person who who um was a little mean like I do get it like I understand that like everyone is just trying to sell a course. Uh and and I can see how it just feels like I'm just fitting in with that crowd. Like I I get it. It's okay. I'm not just like living in a bubble where I I think that you're saying it totally out of pocket. Like I understand, but like at the same time, like I really do believe that and I'm not saying I'm expecting you to do this, but like if you were to actually go through the second brain course, I I feel like you would take back what you said. Like honestly, I'm just going to say that. Um but yeah, not not like I'm thinking I'm going to change your mind or anything. Yeah. All right. Having never built anything before, but amazed how easy this is to learn if you think logically. That's right. Yeah. And even just like slowing down and using claude code to help you think logically like break it down for me step by step or like help me plan this and ask me questions like those kinds of things are are uh how you get the most out of claw code because it it can I mean like large language models make mistakes. They're never going to be perfect and that's why you need to align with them. But you can have them walk you through the alignment process because they do a really good job at that. Okay. Uh, cool. So, it looks like it ran end to end and it actually closed a lot of issues here. So, three were accepted and then seven were rejected. Okay. Interesting. Uh, well, I'm curious to dive into that now. It says that it's still waiting here. Cool. SmokeD Dev said as a part as part of as a student of the course I agree Dynamus absolute game changer for me lots of value I appreciate a lot thank you very much uh all right cool so uh looks like it is done cool and that was fast by the way it didn't take that long now we didn't run this workflow with Miniax let me be clear because we didn't run this on the VPS yet, but we will get there. We're just testing it right now locally. In fact, I should probably test my or check my enthropic rate limit. Uh oh, it's not even that bad. Okay, we're good here. I'll even share that on my screen here. Let me duplicate and bring it over. So, this is my limits right now. Uh, look at that. We've only we've literally only used 10% so far. So, not bad, especially with how bad the rate limits are. Um, wait. What is this? Daily included routine runs. This is new. Like as of just today. Included routine runs per rolling 24 hours. I actually This is weird. I've never seen this in the usage page before from the Cloud app. And yeah, my weekly limit I'm at already at 50% and it resets on Friday. And over the past couple days, I've been doing so much testing with Miniax that I haven't even been using my Enthropic that much. Like it's crazy. I got to like 40% over the weekend. Yeah. Okay. So, anyway, I was going to look at the classifications that it did here. Oh, it already undid everything. Shoot. So, I can't actually see because it deleted the comments. Okay. So, this is one of them that was accepted. So we can see that the labels are removed cuz I asked it to undo things after its testing. But we can see from the history here that like this one it added the factory accepted with a priority low. If we look at um I don't know one that it rejected here. Where is this one? This one it added factory rejected closes not planned. It had an issue comment here at one point but that's another thing that it cleaned up. So, I honestly kind of wish that it did the cleanup after I told it to, but that's my fault because I told it to do the cleanup immediately after. We can see here that um it has taken care of all the cleanup. All 11 issues are back open with zero labels. But anyway, the workflow actually worked extremely well. Um okay, what I did not touch. Yeah, that makes sense. Ready for the next step? The triage workflow is committable. Next logical builds per the plan. Uh GitHub label onetime setup for the real run already done implicitly dark factory validate PR. Well, shouldn't the next step be to create an adaptation of the archon GitHub issue fix workflow for the dark factory? Because I I think like I don't know why the plan wasn't really clear on like we got to actually build something for implementing the pull requests, not just validating and fixing the issues that come up. So I'm going to try to point it in the right direction here. Um because I I think that'd be the next workflow to work on. So we have the triage which is going to figure out what issues do we actually want to address and then in parallel we'll invoke the archon workflows to you know take it from issue to pull request. Okay you're right and I missed that. Of course Claude has to be sickopantic and tell me that I'm right. U but I am. The triage workflow produces labels, but those labels are inert until there's a working fix workflow. It knows how to validate. Uh the plan calls this out explicitly as a hard blocker. The moment a bug fix or feature lands, the default bun run validate will still blow up on Python syntax. Right? So this this is a little bit behind the scenes planning I was doing. Basically, the fix GitHub issue work get fix GitHub issue workflow built into Archon isn't quite specific enough for my codebase. So, I just need to take this as an example. This is one of the workflows that ships by default with archon. And I just need to tweak it to work a little bit better with my dark factory specifically. So, it's going to do some research for me. So, understand the structure of the repo. Um, understand the command or the workflow we're going to adapt and then see what we have for our global rules already. All right. Let's see. All right. Yeah, I appreciate it. Don't care for such comments. You're really delivering a lot of value for free as well. I think we all value that a lot. Yeah, I appreciate that. And um even when I do have the community as a, you know, paid thing, I I do try to give an insane amount for free like what I'm doing right now. So, I appreciate recognizing that. And that really is important to me. Like no matter what I always want to just be constantly giving. That's also why Archon is fully open source. This repository has nothing hidden. I mean the Dynamus community had early access to it and got to even help shape some of the direction for it. And that's one of the cool parts of having a community. Uh but it's it's for everyone. That's that's always been the goal. All right. Is there a link for the community? Uh yeah. Yeah. Sorry. I I'll send this again here in the chat. Um, so this this is a link to kind of like the page like showcasing the AI second brain, but you just scroll down and there's a lot of buttons here to join. So yeah, I appreciate that. All right, let's go. I'll watch the logs here. All right. See, a strong DM depends on a digital twin universe which creates behavioral clones of ex external services like oka, jira, slack to allow agents to run thousands of realistic tests. Yeah. Okay. If you really get into strong DM setup, it is quite impressive. So certainly won't be uh building everything strong has at least for now, but also my application is luckily a lot simpler. I won't necessarily need to to have the same level of depth, right? Like simpler application means I don't have to go as deep, but I still get like the same reliability like they've built. Uh but yeah, if you want to like really read into what Strongd DM has built, again, they haven't open sourced their Dark Factory, but they've, you know, open source the PRD like I showed at the start of the stream. And then I think they have like some blog posts as well where they break down a lot of what their architecture looks like. It's pretty cool. It's It's really inspirational. All right. Cool. Um, routine runs. Is that analogous to open claw crons? I mean, probably analogous to some kind of cron job. I don't know exactly. Like this. I've checked my anthropic usage every single day because I want to be on top of especially the 5 hour rate limit. This this I literally like wasn't this wasn't there this morning. Um so yeah, I don't I don't know what it is exactly. Maybe maybe they have something if I just like search cloud code routine runs. Okay. Um Oh yeah, there we go. 47 minutes ago. We have a post on the cloud code subreddit. New now in research preview. Routines and cloud. Configure a routine once, a prompt, a repo, your connectors, and it can run on a schedule. Schedule routines let you give Claude a cadence and walk away. Um, okay. I was just about to say they already have the slash schedule the CLI. If you've been using slash schedule in the CLI, those are routines now. There's nothing to migrate. Okay, that makes sense. So, they're they're taking something that was has already been there, but now they're just building it into other platforms. Like I I assume that like slash schedule used to be an only CLI thing and now it's like within claw desktop and co-work and the claw app. I guess that's what it is. I mean it's pretty cool. So yeah, literally it is cron jobs just being able to run something that runs every hour or day or whatever. That's pretty cool. All right, they are always shipping. It is crazy, but good for them. Okay, very cool. So now, uh, okay, how long have we been streaming for? Um, we've been streaming for a little over an hour and a half. Okay, so I am able to stream for Wait, I got to check my calendar. I'm able to stream for two and a half hours. And I'm I'm loving what we're building right now. So I'm think I'm going to go till Yeah, I'm planning on streaming till 1:30 Central time. So like another hour here. We'll see how far I get with all of our workflows. Okay. What are we doing here? Okay. Wow. There's so much output. I'm getting a little like uh burnt on all the like burnt out from all of Claude's output here. It's a lot to parse through because it's kind of it's fairly complex what we're working on right now, I will say. Okay. Rag YouTube chats validation story is prescribed but not wired. Okay. Uh, global rules prescribe the exact commands, but none of those dev steps are actually installed yet. No tests, no make file, no CI, right? Yeah, I haven't built that yet. The factory should add these when the first PR touches them. I don't actually agree with that. I want to build that ahead of time. [laughter] I love this. It's cute, but it creates a chicken and egg problem. Oh, that's funny. I Wow, Claude Claude has some personality now. I will say and yeah I agree with Claude here that that is a bad decision to put in the global rules. Um okay the bundled archon fix GitHub issue workflow is mostly language agnostic. That makes sense. So my surgical fix is just one file. My recommendation is option B custom command override. Um here's my Okay. All right. Yeah. Sure. full workflow fork. All right. You know, so it's saying I don't need to create a workflow from scratch and I can just use what I have as the bundled workflow. Um, yeah. Okay. Yes, you're right. We definitely want to bootstrap the development dependencies manually. And then I actually do want to create a custom workflow entirely. So yes, I know that there's not much we have to change from the GitHub issue fix workflow, but I want to be able to evolve it separately from the default Archon workflow anyway. So we can mostly copy it and then obviously just changing the validate command. But yeah, let's go ahead and do it that way. Um, yeah. And then sure, we can we can smoke test issue number 26 after. Okay, there we go. Um, oh crap, we have to run the compaction now. Oh, I forgot about that. I probably should have just worked on the workflow in a separate conversation. Uh, because now that it does a memory compaction, it has to reload its skills and stuff. So, all right. Now that you just did a memory compaction, I need you to uh read the dark factory plan again and then load the archon skill just to make sure you have full context before you go into building the second workflow and um doing the smoke test on issue number 26. Make sure you build this workflow from scratch. And then uh also I want to use the commands folder for all archon dark factory workflows. So make sure we don't have inline prompts for the other the triage workflow we just built as well. Um, so that's a little specific, but I just realized that um I wanted to organize my workflows a bit better than I did up front. If I go do the codebase now, we have the dark factory triage. Um, this prompt is in line and it's massive. So I would rather extract this to a command, right? We don't have any commands right now, but in Archon your workflows can reference a command, which is just like a separate markdown document just to have a better way to organize things. So we don't have these massive ugly prompts in line in the workflow itself. I might even want to do the same for this this uh apply decisions bash is like really long. Yeah. Uh there's there's a lot of optimizations that I can make just for the sake of the live stream. I am moving decently quickly. So certainly we'll be iterating on things off camera uh like before I make the YouTube video tomorrow. That kind of like, you know, sums everything up for the Dark Factory that I'm working on. All right, cool. I appreciate it. Haters going to hate Dynamus rocks and the value of your contributions, Cole, are frankly incalculable. I I appreciate it a lot. That means a lot. Price of Dynamus is a lot more reasonable than most of the courses community subscriptions being offered. A lot of them sound like snake oil. Get rich quick for thousands of dollars. Yeah, there there unfortunately is a lot of that out there. Uh there there's one sort of YouTuber in particular that I don't want to call out exactly uh or like namerop, but uh he he's a respectable guy. He does a lot around second brains specifically, like even before generative AI. A lot of you might know who I'm talking about. So, I'm not saying the course is going to be bad, but he like he's like running these cohorts for building your own second brain, and he's charging $2,000 for it. It's like crazy. Like, what? Like, $2,000 just to like learn how to build a second brain. Like, I taught that for in a 4-hour workshop and you can just join the community for it. Like, it's not $2,000. [laughter] Yeah. Anyway, there are some pretty expensive things out there for sure. All right. Um, will the Dark Factory repo be open source after the live? So, not fully, but uh it'll be within like the next couple of weeks I will open source it. So, I need some more time to validate and really polish things, but the the plan is to make it public by the end of the month, like everything public where you can even open an issue and have it work on it for you. So, Who could I be talking about? Yeah. Yeah. You guys, some of you guys know. Some of you guys know. And And again, I respect him. Well, I guess I would say I have more of a neutral opinion. I haven't gotten like too deep into his stuff. So, I'm not like trying to dunk on him or anything. I'm just saying that like to me, like $2,000 to join a cohort is a little ridiculous, but to each their own. I mean, some some people um definitely value having that kind of like cohort style. It's Yeah. Teach your own. All right. Okay. Let's see here. What else we got? The old You're absolutely correct. Yeah, that's right. All right. Um, a bit out of context, but uh, could we build a skill to make Claude code and and anti-gravity interoperable? Uh, you definitely could. Like if you wanted anti-gravity to invoke Claude like in headless mode, you could if you wanted to. Um I think I don't [snorts] know if anti-gravity has like a CLI, but Gemini has a CLI obviously. So you could have them invoke each other. So you could like have a workflow where it's like Claude implements the code and then it calls the Gemini CLI to do the validation. Like you could do that kind of thing 100%. Like that's something that I actually want to build like directly in the into Archon workflows like being able to have different providers at different nodes for planning and implementation and reviewing. All right. Uh okay. This is really interesting. Uh Miniax with open code performs much faster and better than in cloud code. Probably the context bloat of all the prompting that goes under the hood in cloud code. Um, so that okay, that's good to know because yeah, maybe I would want to change this harness to use like PI or open code instead. Uh, okay. I I will have to look into that. Like I said, there's so many ways that I can probably improve this harness with the prompting and how I organize the workflows and my mission document and my factory rules and even just the tool that I'm using under the hood. Like maybe I do want to use Pi or Open Code instead. All right, let's see. Uh, one way to find out if the course or subscription you paid for justify the cost is if you ship a product that others paid for to recoup that cost. I mean, yeah, exactly. Um, that right because then then it's like there's no argument there. Like if you made more money thanks to what you learned there and you built something from it, then yeah, it pays dividends. Exactly. Right. All right. Why does it feel like we've been here for one plus hours and not achieved much? I mean, that's something that I've been trying to be very transparent about here is that like we're spending a lot of time planning and defining the architecture and the system for the dark factory up front. And it it has to take time. It it it has to I can't rush it. And and to be honest, like I would probably be going even slower if I wasn't in a live stream here because in the end, like if I want this thing to rip through issues really quickly, if I want the Dark Factory to be self- sustaining and really efficient and reliable, I have to be slow up front. That's what I'm and that's kind of the the teaching lesson here, honestly, as well. So, yep, even miracles need time. That's a good way to put it. I wouldn't I feel like that'd be very egotistical to call this a miracle. It's certainly not. It's just an experiment that we'll see what happens. But uh yeah, it's a good way to put it. All right. That's very cool. John, I joined China two months ago today. Never wrote a single line of code. Have a functioning second brain. And yeah, that's that's awesome, John. I appreciate it. Once you get to that point where your second brain is up and running and saving you hours and hours every week, there is no better feeling. So good. All right. All right. One of the basic rules of marketing is people are willing to pay for high ticket. I mean that that's fair. Yeah. Like this uh individual that I mentioned. I mean maybe I could just say his name because I'm really not like hating on him or anything, but just for the sake of being careful. Um, I'm sure there are people that get a lot of value out of it and and yeah, he he like kind of is known as like the premium person. He's like he's been building second brains for a decade. I mean, I would like to think that like he's struggling to catch up with all the AI stuff because he he's more traditional his approach. He's probably doing fine. But anyway, like yeah, I'm sure there's when you when you have something high ticket, it signals value. And so you do attract that uh kind of person that is willing to shell out and they just want to make sure like I mean I don't always agree with this, but like sometimes people just think like, hey, most money means it's the best value, which definitely isn't always true, but uh it does kind of scream like this is going to be the safest bet if you have the money for it. I don't know. I don't know. I'm kind of rambling on that. Yeah. Uh, Dynamus is awesome. A part of the community since it came live. That's so cool. I appreciate you being a part of the community for so long. Uh, and by the way, the oneyear anniversary of Dynamus is uh this month, April 26th. So, there going to be some some exciting things that I've got going on for that. Some live streams I'll be doing on YouTube around the time. Um, and also some exciting events in Dynamis and some things that I am releasing as a part of the anniversary celebration. Also, just speaking of things that are going on around that time, uh, I want to call this out really quick as well. I'm doing a, this is kind of like unrelated, but around the same time, I'm doing an AI transformation workshop with a gentleman named Leor Weinstein on April 28th. So, that I believe that's a Tuesday at 9:00 am [snorts] Central time. So this is going to be really cool because uh Leor he's like an expert at coming into a company and helping it become AI native and so like designing like a AI native org chart and like how to enable each team and team member with AI technologies for coding and other things like even just like you know the sales and marketing and finance team and all of that. So he's going to like talk about that for an hour and then for an hour I'm going to talk about how to transform your organization with agentic coding and like how to transform developer teams. So we're like kind of tag teaming it together to give you like this full view of like how do you transform companies and even yourself as an individual. Uh so that's going to be really cool. So that's happening at the end of this month here. And yeah like you can see I'm on my you know scheduled live stream page on my channel. This is just going to be a free workshop just [clears throat] happening on live stream on my channel. All right, cool. Yeah, big shout out to Cole. Even the content you are delivering for free every week is insane. Thanks a lot. You're very welcome. Always my pleasure, man. Like I've been doing YouTube for uh it's almost two years now. I started like very beginning of July 2024 and it's just a blast. every single video. It's just so fun to make and uh keeps me ahead of the curve on everything, too. Just being a constantly in the trenches building and researching and doing what it takes to make the content for you guys. All right. What is going on now? [laughter] Uh sometimes it's stressful to come back and just see like it's in the middle of writing the package.json. You don't even know why. Oh, I guess it Oh, yeah. setting up the developer dependencies that we talked about. Okay, we're good. We're good. So, okay, what has it done now? I think it made the full workflow. Yeah. Okay. Dark Factory fix GitHub issue. Okay, good. So, we got our second workflow now. All right, dynamis. Uh, no, not that one. I need to go to the rag YouTube chat. I want to open up the second workflow. Okay, take this is good. So, now we have all of our different commands. So instead of the workflow just being like a bunch of massive inline prompts, we got it organized a lot better. Okay, so this is our fix GitHub issue. By the way, I'm thinking about renaming the whole uh rag YouTube chat repo to Dina Chat. That's why it references this name a couple times. Uh but anyway, so this workflow here, we're going to start by extracting the issue number. So this is very much based based on the default fix GitHub issue workflow archon. Then we classify the issue bug feature enhancement refactor chore or documentation just like we planned in the in the dark factory plan. Then we research the issue uh and then we either do a plan we create a plan if it is a feature to build or we investigate the problem if it is a bug to fix. Right? Because issues are going to be one of the two. Right? So like when we classify it's either going to be a bug and then I know we have all these different labels but basically all these are just feature additions right like if it's a chore or a refactor or an enhancement like all those are just like more specific versions of a feature. So may maybe the whole like issue labeling isn't optimized here but I think it's fine. It's actually pretty standard to have those kinds of labels. And then we go into implementation then validation create the poll request and we review. And so I am going to have a separate workflow to do complete pull request validation, but I still want to have the workflow it like when the PR is created at least have it do a little bit of review, right? So like initial round of review here and then I'll have a more comprehensive validate PR workflow that I'll create next. That's the plan just to give it a chance to do a little bit of self-fixing before we say like all right here's our poll request for for you uh you know next stage of Dark Factory to review. All right. So let's go back to our coding agent here. Where am I going? Okay. There we go. Okay. Status so far. So, we refactored, built the new workflow, seven new commands. Looking good. Got our dependencies set up. Uh, okay. Before I kick off the smoke test, two things to confirm. Dev dependencies are not installed locally. Um, okay, that's fine. Yes, I want you to install the dev dependencies. And actually, I would much prefer to use UV for the Python package management. So go ahead and change that in the repository. Get everything installed, test everything and um and then yes, go ahead and invoke after that invoke the archon workflow to run the dark factory fix GitHub issue on pull request or no on issue number 26. Okay. Yep, that's good. All right, cool. And then we're not going to have time for it in the live stream here, but um you know what? I I'm almost tempted to do another live stream tomorrow instead of a YouTube video. Maybe I probably should make a YouTube video because it it'll be a week. Uh but it'd be cool to like just keep building this live more. I know that it's a lot of time, but it it's it's fun to do this. And we're getting kind of close, right? Like we have a lot of it built. We just need to finish the last couple of workflows and then we need to bring everything onto the VPS so that we have the whole dark factory running autonomously and it's not relying on my computer being on. So, we're we're getting there. We're getting there. We we won't really be unfortunately be able to see everything running on our VPS today, but um it won't take long once we have the workflows built and validated to copy everything over because we already have the I think this is my directory dark factory. Yeah. Yeah. So, we already have the app here. So, we we already have everything like cloned and set up and verified. So, we just have to bring over the workflows and then set up the cron job that's going to run every hour to do the triaging and then the implementation and everything like it. It should work pretty quick once we have the workflows built. And that's why I wanted to use Archon for this because then I'm not even creating the harness myself from scratch. I'm just building Archon workflows. And that is the harness. It's a clear example of the value of Archon as a harness builder, which is part of the reason I wanted to do this dark factory, by the way. This is just such a cool use case to show the power of Archon. Like these workflows are defining processes that would actually take a good amount of time to architect from scratch if we wanted to. Like for example, even just having this process of triaging issues and then sending off miniacs to handle each one of these in parallel like that would take a lot of engineering if we didn't have archon as a starting point to bring in the context and handle work trees for isolation so we can build each one of them in parallel and then having the deterministic steps to uh you know label the issues and close issues like that. That's a lot of work. But now we're able to just rip through this like pretty quick. Like I know that that um the stream is like two hours now. But still like when you really think about how much we've already engineered here, like it's a lot that we've built already and we've taken our time with it. All right. Um, [laughter] can we use Archon and the Dark Factory as paperclip? So, yes, you could because each Archon workflow could be like the the, you know, individual AI employee kind of like how you manage that with um, paperclip. You could that'd be cool. It's kind of what I'm doing, I guess. Like each Archon workflow you could sort of think of as a different employee. I mean, we literally have the pattern here where we're doing the b the hold out where it's like this has to run completely separately from the implementation. So, it is sort of like two different AI employees that the the dark factory is delegating work to. Smooth as fast. Mistakes are 10x as expensive as planning time. That's right. Pays dividends. Take your time up front. All right, let's see. Learned a bunch about rag from you early on. Yeah, I still cover rag somewhat. Not as much anymore, but it is still important. A lot of that old content is still very relevant, too. But yeah, I used to I definitely used to be like the rag guy back in the day, especially when I first started my channel. Yeah, the appearance of value is very important. 100%. Yeah. I had a relative doing art and selling at craft shows. She switched to art shows and made a living off of it and has pieces in museums. That is so cool. Yeah. Right. So, it kind of goes back to our conversation earlier like when you have something priced at high ticket. Like if you have the good appearance of value, you can price it high like 100%. Yeah. All right. Providing unique individual value via video platforms, cohort platforms, etc. is the norm of the future, not the exception. Yeah, I mean, people crave individual uh attention, personalization more and more over time as AI takes it away in some parts of life. So, I can see what you're saying. Yep. Um, maybe Cole has an AI proof job. How many people would watch this stream if his second brain was doing it alone? [laughter] Oh, that'll be the day. I don't I don't know if I would ever want to have my second brain run a live stream. Also, I wouldn't it wouldn't look good right now. But, I mean, there are people that have AI avatars do videos, not necessarily live streams, but even that, like, it just looks bad. I I don't I don't think that it's really feasible. [snorts] Um unless like for some reason people are okay with it being an AI avatar because you're just like delivering the news or something. I know that's usually what most AI avatar channels they are just like AI news focused, right? All right. If you're paying 2K to learn how to use etal caston, then you may need more than a second brain. Uh, I mean that's funny. Yeah, I don't I don't know. Like you can get pretty deep with Zetocasten. I know myself personally I've only scratched the surface. I have actually taken inspiration from Zealcast in a little bit for how I've organized my Obsidian vault. But yeah, it's definitely something I personally like I agree. I feel like you can just figure it out on your own if you have a good hand on your shoulders. But again, to each their own. I'm I'm trying to like avoid getting like super opinionated on things that like I know like there is value. Um but yeah, it's just depends how much you want to just like get the best practices right away versus like figure out yourself over time, I guess, is what it comes down to. All right, what else we got here? Yeah. Okay, so this is exactly why I built my own GitHub issue fix workflow for just now. Uh the default archon commands are very no.js ccentric and that I think that is something we want to improve to make it a bit more language agnostic or a lot more language agnostic. I can see it arguing with itself to build my Golang app. Yeah. So I would recommend right now I mean just in general it's good to build your own harness, build your own workflows because then you can customize it more. I would recommend building your own and using the ones that we have as defaults as a starting point. So you can point your coding agent to the the default archon workflows and say look at these for best practices and even like leveraging the structure for fixing issues or creating PRDs or validating pull requests and like use that as a starting point to then make it specific to my validation flow or my tech stack or my architecture. Yeah. Cool. AI co-host. Okay, that could actually be interesting if I had my second brain not like run the stream, but just like be there as a peanut gallery or something more practical like kind of giving feedback in real time or even like answering some questions in the chat. I could Okay, that could actually be kind of cool. I should think about that. How I could have my second brain co-host a live stream with me. That would be cool. Okay, I'll think about that. I I'll definitely think about that. Okay. All right. Where are we at now? Um Oh, it's still going. Jeepers. All right. Well, I guess Oh, yeah, cuz we had the memory compaction, so that slowed things down a lot. Okay, [snorts] I just wanted to Okay, I'll let it keep running here. All right, then you don't need me anymore. No, no, no. I still I still want real people to help co-host live streams with me. So, Thomas, uh, he's the guy that I have the comment highlighted for. And then also Raasmus, they've done a lot of amazing work helping me on Archon. And I have said that like for some Archon live streams, I'd love to get them in to co-host. And I still stand by that. There's no way if I get my second brain to help co-host with me, it would be a different kind of thing and a different sort of of value proposition for the live stream uh compared to having a real person like you or Raasmus uh co-host with me. Like I would want to do both 100%. Yeah. [laughter] All right. All right. Let's see. Um, all right. We got some interesting feedback here. All right, let's take a look. Once you take this to production, it will just hallucinate success at every step. LM give the most plausible answer. They rationalize anything they can't reason. This whole video is from 2025. All right. Hot take. Hot take. But no, I appreciate the push back. um because what you're saying has some validity and that's why I'm calling it an experiment and that's also why I'm spending so much time up front planning the system and the architecture because yes, one of the biggest problems with large language models right now is that they are sickopantic. They always agree with everything that we say and they have an insane amount of bias towards their own opinions. They're going to rationalize everything and there is a risk if we don't build the system right that they're going to say that this thing is ready to merge and then it's going to merge it and then it's going to move on to the next issue and we go through this loop where every single time it's producing AI slop that is a risk but that's what I'm trying to engineer for here. I'm putting so much time up front because I'm doing things like defining the hold out pattern for validation so that I'm taking away for some of this I'm taking away from and preventing some of the psychicopantic behavior because when we go into our regression testing we don't even know what was just built and so it's just going to be a a neutral judge at least that's the goal what we're doing here there's still a risk to it 100%. And that's why I'm very clear at the start of the stream here that when we go to this level of autonomy for our coding agents, like going back to the five levels here, the dark factory here is not what I recommend. If you want the most reliable software possible, we might get there at some point and maybe this experiment is going to be a wild success and it's going to be like, whoa, dang. Actually, this can get us a really good, you know, MVP for any application. Maybe. But yeah, I'm I'm not I'm not like numbed to the fact that uh psychopantic or psychopanty is a big problem and we have to be really careful about that. So I I feel pretty confident in the approach that I have here. I think we are going to avoid a lot of that bias and a lot of shipping things that it says are good when they actually aren't. It's not going to be perfect, but that's also why I have other strategies. Like I have the like really deep regression testing that I'm going to run every day or every week and then create more issues to address that. I still am going to have some human in the loop for the very very end uh where I actually want to like push things to a platform that people are using. So I'll have a little bit like I've thought about a lot of it. So again, I appreciate the push back, but uh trust me, I'm I'm considering it all 100%. Okay, let's go back. Still working. Wow. Okay. All right. Anime girl co-host. Uh, you will never see me do that. [laughter] It's funny though. All right. Uh, you have to check the parameters to themselves. Introduce the specific parameters to check. You had extra math and type of engineering checks to achieve it. Little lost on what you're getting at there. Maybe you could elaborate. Uh, need to drop off. Good session, Cole. I appreciate it. All right. Cole the rag guy. Spicy mangoes. Yeah, spicy mangoes hasn't come up for a while, but I'll have to bring it into another video soon. Um, an LLM can't even join uh a chat room without everyone knowing instantly it's an AI. I mean, yes, that's true. Yep. That's that's why I wouldn't ever have this dream of having a second brain run anything anytime soon. Yep. All right. Let's see. Hard to explain. Yeah. All good. Yeah. Take your time. All right. Yeah. Okay. I agree with this 100%. If an LLM hosted a show, it would be boring and bland and obviously an LLM. I mean, yes, I agree. All right. Um, cool. So, okay. Anyway, our coding agent is done here. So, I want to come back and and give it some more attention. So, all right. We're done with all of our deb dependencies. The smoke test problem. Dark factory validate currently runs whole codebase checks. If I kick off the workflow on number 26, the agent will fix the one lines cores bug. Then validate will hit 130 pre-existing errors didn't create. Um, okay. So, wow. Okay. So, I guess what what happened here is we're creating the development environment for the first time. So there are a ton of issues that aren't actually related to the fix that we'd be running the workflow on. So I I need to actually address these things. Um yeah, let's do number one. Let's address all the problems and then run the workflow. Yeah, I just I mean this will take a while. Uh, but I I do just want to do that because because what I might be able to do is actually create the next workflow in another Cloud Code session here. I think that makes the most sense. Let's go ahead and do that. Okay. So, let me go back to my vault and copy the path again to our plan file. So I'll say uh read this plan file and uh also load the archon skills. You can help me build more archon workflows. I have just finished creating my dark factory adaptation of the fix GitHub issue workflow. Now I want to work on the validate PR workflow and it's very important that this follows the hold out pattern very closely. I just had someone in the live stream say that they don't believe in this approach. And I think the hold out pattern is one of the most important things to address their concern. So, let's uh let's focus on that. I'm being a little silly, but but yeah, I think it's it is very important that we make sure that we are taking lessons from the strong DM dark factory because it is it is very impressive. All right, let's see what else we got in the chat here. While I wait for this to run, we'll kind of monitor these two sessions in parallel here. Um, is there a way to use Quen 3.6 Plus with Archon, even if it's through Open Router? So, uh, one thing I learned the hard way recently with open router is you're not actually able to use claude code with open router for any models outside of the enthropic ones because it doesn't have an anthropic um, compatible endpoint like Miniax and GLM. So, if you wanted to use Quen 3.6 plus, I would wait until we have support for uh, Pi. PI is going to be the third provider that we add this week or next into Archon because then you'll be able to use other models really easily. You're not going to be like the obviously like right now we have Claude and CEOs and you're a little bit more vendor locked. You can do what I did in the VPS to point it to other providers but only if they are anthropic compatible like Miniax and GLM. So there might be a way but I actually tried first before I went to Miniax directly I tried going through open router and it didn't work. It only worked when I chose an anthropic model. Um, okay. It's confused here because it's trying to read my workflows in the remote machine, but I haven't actually pushed it to remote yet. I might need to Hold on. Oh, no. Hold on. It figured it out. We're good. We're good. All right. Need a new open source 120B. I mean, yeah, it's been a while since we've had one around that size, for sure. Yeah. All right. Um, since I love C, what do you think about Blitzies and their C compilers? Um I don't do I love C. I haven't programmed in C for a very long time. Actually it's been about five years since I programmed in C. Uh you mean like C the programming language? I assume because you're talking about C compiler. I I haven't used C in a long time. I also haven't heard about Blitzy. I'd be interested though. Um funny story or not funny but interesting fact for you guys. Uh when I was in college, I was a teacher's assistant for a C and machine learning course. So I I got to uh not sorry, not machine learning, goodness, a C and assembly course, machine architecture course. So I got to help students debug assembly code for hours and hours a day [laughter] at one point. That was fun. Yeah. All right. So all right, what did what do we got now? have enough context. Let me lay out what I'm building. So, hold out pattern design for the dark factory validate PR. This is the critical workflow for defending the AI rights code unsupervised concern. Here's how I'll enforce strict hold out across five layers. Okay, so this is the main concern that we're addressing here with AI sickle fancy in our dark factory. Not saying this is going to be perfect, but this is my first attempt for the public experiment to avoid the coding agent. just always saying it work is good and merging it. So we have a separate archon workflow, separate artifacts directory, separate work tree. There is no way that it can peer into the work of the other agent and potentially take its bias. So we exclude comments and review. No code, no code or chatter. Uh we have our our governance files. So we're going to read those as our rule book. Every AI node is going to start with fresh context. So every step of the way during the validation, we're not even going to build up bias in the validation itself through the different nodes. The behavior behavioral validation command leads with a hold out rules section enumerating what it must not consider. It can't find and search for implementation plans, commit messages, coder rationale, prior review comments. It answers exactly one question. Does the diff solve the issue body? Very good. And then even another hold out pattern I I was kind of referencing earlier is like when we do the full regression testing every day or every week, it also is going to have no knowledge of recent feature implementations or issues that we're in the middle of addressing, right? Like it just is going to answer the the straight question of like does this application work with all the user journeys we have laid out in the mission markdown. Good. All right. So now it's writing everything and we'll let it go. Both both of these are still running actually. So, I'm going to open up the repo again because I can I I just want to show off the uh mission and factory rules just like really quick. So, here's our mission document. So, it it's uh decently concise, not too long, but it covers um like the core of the application. What is Dino Chat? Um, who is it for? Uh, patent still pending by the way. I might not keep the name either. We'll see. We'll see. Uh, who is it for? The core capabilities of the applications. This is specifically calling out what is in scope. Like if I were to create an issue to add Google Oath to the platform. The triage is going to be like, oh yeah, good. Let's mark this as accepted because it's literally in the scope for the mission.md. And then we also cover what is out of scope. What must the factory never build? like we don't want it to add other YouTube channels. Like if someone created a GitHub issue, we'd want that to be rejected because at least for now, I mean, I could extend this application later, but at least for now, the scope of this app is for my YouTube content to be a resource for you guys. We don't want to, you know, allow someone to open an issue to swap the LLM. That would be bad for my credits. Uh we don't want to like add in payments or subscriptions like this is meant to stay free. We don't want to over complicate with a mobile app or a desktop desktop app like no like electronic app. Uh so yes like things that we don't want to build uh hard invariance like things that we have to we absolutely have to keep the same. So we can't allow for issues that would try to tweak the rate limiting or the authentication requirements things like that. Uh ways we're allowing it to evolve. And then quality standards right like that. That's our missions.mmd. And then I can evolve this over time. This is sort of like my console. So like going back to the analogy here of like you have a car that doesn't even have a steering wheel. Well, you're still going to have some kind of console to provide higher level directions. And so if I want to tweak the dark factory, I still have the levers to pull because I can still change the factory rules or the mission.md or I can update the archon workflows. If I really want to and there's like a drastic issue that I just really need to fix, I can make a commit myself just straight to the main branch. So I mean there's flexibility with this here. Um but yeah that's and then the factory rules. This file governs how the dark factory operates on this repo. So like here here's how we handle triaging right like this is more context that we it's quite important to feed into the triage workflow. Here's how we implement things. Here are our requirements for pull requests. For example, I don't want to allow more than 500 lines because I want every single issue to be a small focus scope of work. It's one of the most important things for getting reliability out of our coding agents here. Quality gates for automerge. Uh uh talking about the regression testing, I want to use the agent browser specifically. This is the Verscell agent browser CLI. It's an open source browser automation tool that I use a lot to test my frontends. Especially when I'm working on Archon itself, I'm using the agent browser skill. So, I want this to be built into my larger regression testing workflow that's going to really test everything every so often. Uh, protected files that it's not allowed to change, right? I don't want it to change its own governance documents because this is my console, my lever to pull, not its own. Um, how like rules around like when we should autoreject certain things, how we should escalate cost and throughput. I mean, I don't need to get like super deep into everything here, but uh yeah, you can see like the factory rules gets more specific. Like this is quite a few lines of code here. How many is it in total? Oh, sorry, not code lines of markdown. Even this isn't like super long, but it's 320 lines because there's quite a bit of specificity I want to supply there to really have my guardrails defined. All right. Have I you tried using prompts that presume failure and laziness? It can rationalize that too. Um I mean I've played around with that kind of thing in the past. Um it can rationalize that too. Are you saying that like that actually doesn't work or are you saying that uh that helps it rationalize or like helps it address problems? Let's see. You may want to leverage all your work with rag and build graph rag as the second brain. Obsidian as a second brain doesn't come close to graph rag, but obsidian is less setup. Yeah, I mean I found obsidian enough for me and like it's nice because it is less setup like you said, but I mean maybe at some point I will build a whole Greg graph rag system for my brain and share. It could be cool. uh still kind of wrestle with that might be overengineering depending on you know how much context you're storing in your brain but I have that in the back of my mind for sure. Oh, it does work. Okay, cool. Yeah. Yeah. I mean that's a good idea then. So like my validation process I could have a workflow in the dark factory that says like okay I need you to assume or like not even not even tell it to assume but just say like this agent was lazy. go and figure out why it's lazy, what could be better about the implementation, and then like open up another issue or resolve it directly. All right, that I like the idea of building that in for sure. All right. Could I use Carpathy's auto research to improve the dark factory in the future? Uh, until plot twist, it does not stop running, it starts replication, right? some yeah maybe it will who knows um so yeah I could use Karpathy's auto research basically if I were to apply Karpathy's auto research it would be a separate process that has control over actually editing these three files right because like the idea behind auto research is you have a a file that kind of dictates a larger system like a model or a repo and then that file you have a coding agent iterate on autonomously based on lessons that are learned from a feedback loop. So I could build Karpathy auto research to like evolve these over time. So like right now within the factory rules I have that that um hard rule where it's not allowed to um it's not allowed to change the governance the constitution. But this is only for the agents that are dealing with the issues in poll requests. So I could have a separate process that like its actual sole job is to evolve the governance over time. It's an interesting idea. I don't know if I want to take the autonomy that far right now because I really want this to be the lever that like only I am pulling on currently. But that could be a natural evolution at some point. It'd be interesting for sure. Cool. Yeah, I appreciate all the ideas you guys are sharing here. Seriously, like there there's so much to chew on. That's why I love this experiment because like the world becomes your oyster for the ways that you can evolve this and the things you can build with it as well. Like you could really apply this to any workflow. It's just cool being able to like use archon to guide the entire thing as well. Um like every single line of code that's written here is written from an archon workflow. So yeah. All right. Uh let's go back and see where we're at now. Um okay. So we built our third workflow here. And uh what's this one? This one is Okay. This one is in the middle of actually testing the uh the second workflow that we built. Cool. So, probably have to wait a while for that to happen. I think I'm going to go ahead and call the stream here though because we'll have to wait a while until we have like the next big thing happening. So, I'll keep working on this after the stream and then I'll be making a YouTube video on this as well for tomorrow, which I'm excited about. So, yeah. All right. Uh let's go back to full frame here. I appreciate all of you guys being here today. This is a very different live stream to to build and like actually take my time with something. I haven't really done that on a live stream before. So, yeah, I appreciate all you guys' ideas and and questions as well. And um yeah, for anyone who didn't get a chance to get their question answered, like always feel free to comment on a video. Join the Dynamis community as well because I'm active there every single day. Uh maybe I'll just show that uh one more time really quick here. I'll put a link once more in the chat here because yeah, if you want to build your own second brain, go through the agent coding course, just ask any question that uh you have like the Dynamus community is the place for it. So, I'd love to see you there. Otherwise, I'll go back to my full frame here. But yeah, more live streams coming as well. Uh because I I actually enjoy doing live streams more than making YouTube videos. I like both, of course. I love both, but I love doing live streaming. I love being live with you guys. So, yeah. All right. So, yeah, with that, appreciate all you guys being here. Uh, stay tuned for the YouTube video tomorrow on the Dark Factory with Archon and more live streams coming up soon. Hope that you guys have a great rest of your day and I'll see you all around. Have a good one, guys.

---

## Timestamped Segments

**[0:00]** dark factory today. And I know it sounds kind of spooky, but uh I'll start things off by explaining what that actually is.

**[0:06]** This is going to be a little bit more of a casual live stream. So, I did a live stream over the weekend where I dove

**[0:13]** really deep into Archon, the new open-source harness builder. And so, I'm

**[0:19]** going to actually be using this a lot today, but I want to just do more like a live building session. So, I'll still

**[0:26]** like be sure to explain everything that I'm doing and have a good time for Q&A and stuff, but it's going to be a little

**[0:32]** bit more like you guys just get to see the inside of a process that I'm starting here with a public experiment

**[0:38]** that I'm calling the dark factory. And so, I've got my left monitor open up

**[0:44]** here with all of your guys' comments in the chat. And then my right monitor

**[0:49]** where I have my recording software and then I've got my screen in the middle here. So, when you see me looking around, that's what I'm doing. But yeah,

**[0:55]** this is just going to be like a a good like two two and a half hours I'm thinking of streaming for where I'm

**[1:01]** going to be building the dark factory in public with you guys and even opening this up fully to the public in a couple

**[1:07]** weeks here. I'll talk about what that means as well, but I I need to explain first what the heck a dark factory

**[1:13]** actually is. So, I'll I'll cover the basics for you guys. I think you'll find it really really interesting because

**[1:19]** this is like the peak evolution of AI coding. Not that a dark factory is going

**[1:25]** to give you the most reliable results, but it is the way to give the most control possible to your AI coding

**[1:31]** assistants when they're working on a codebase. So, the idea of the dark factory, it uh originated actually in

**[1:38]** the late I think like 1980s, 1990s. There were some companies in China that

**[1:44]** were um running physical production lines with only robots. And so, the physical location only had robots in it.

**[1:52]** So they didn't even have to have the lights on, right? There's no need to pay for electricity when there's no humans

**[1:57]** operating in the facility. And so Dan Shapiro, I believe he's the first one

**[2:02]** that took [clears throat] this idea of the dark factory and applied it to code bases. So using generative AI to

**[2:10]** completely manage a codebase all the way from ideiation, implementation, code review, merging pull requests, handling

**[2:17]** releases, like actually shipping the code as well. That is what a dark factory is. And I think the best way to

**[2:23]** explain it is to go through his article here. So he put this out just at the end of January this year. And he talks about

**[2:30]** the five levels of AI coding. A lot of us are at level like three or four right

**[2:35]** now. So I think like seeing where you're at and then like how far we can take things with the dark factory with his analogy will like really help you

**[2:42]** understand like exactly what the heck a dark factory is. And so yeah, let me go and share my screen here with this blog

**[2:50]** article. I actually meant to be sharing my screen earlier, so that's my bad. But yeah, so let's take a look at this

**[2:57]** together here. So this is uh Dan Shapiro's post from uh the start of this year here. So the five levels from spicy

**[3:05]** autocomplete to the dark factory. And so level zero, this is how I started using

**[3:13]** AI to help me code. probably the same for a lot of you guys that came from an engineering background. You were writing

**[3:18]** code yourself before and then you slowly start leaning on AI more and more. So, I

**[3:25]** don't know why he calls it spicy autocomplete, but hey, I love it. So, I'm I'm for it. So, and in [snorts] this

**[3:31]** case, um the analogy that he uses throughout the different levels is um our control of a vehicle. So, at level

**[3:38]** zero, we're still driving. You can even think of it as like stick shift, right? Like supermanual. we are managing the

**[3:45]** vehicle and so the AI coding assistant or even just like the large language

**[3:50]** model serves as a reference tool or an enhanced search. So it's like a smarter Stack Overflow if you guys have used

**[3:56]** Stack Overflow in the past. And so here the developer manually writes all the code. We're just using AI as an adviser.

**[4:04]** So like help me with this code snippet or give me an idea for how I can implement this. But we still are the

**[4:09]** ones hands on the keyboard writing the actual code. So hopefully most of us

**[4:14]** aren't at this step anymore. Um I know some people still are because that's what they're comfortable with and that's

**[4:19]** totally okay. But then we go into level one. This is the coding intern. So you

**[4:25]** can think of it like cruise control. You still have your hands on the wheel but at least AI is managing something or

**[4:30]** like the car is managing keeping you at a certain speed like 65 miles hour. So

**[4:36]** here the AI writes the unimportant or boilerplate code. So you're still doing most of the work yourself, but for the

**[4:42]** things that you don't require much trust in the large language model, you're starting to hand it over. That's the

**[4:48]** coding intern. And um by the way, when we get to level five, I'll talk about how I'm actually building it myself. So

**[4:54]** we we'll get there, but I want to kind of give the basis for you here. So we then get to level two, the junior

**[4:59]** developer. This is the pair programmer. So we start to relax a little bit. We only have one hand on the wheel instead

**[5:05]** of two. So the developer and AI trade off control. So there are legitimately some more complex tasks that we are

**[5:11]** delegating to the coding agent, but not all the time. We still are the ones writing the code a lot. And then we get

**[5:18]** to level three. And so this is, you know, like the self-driving cars now, right? Like you got hands off the wheel,

**[5:24]** but you're still paying attention to the road. And so the AI is generating a majority of the code base, but you're

**[5:31]** still reviewing everything that the AI does. Like you're watching the road constantly, and you're going to be

**[5:37]** nitpicky. You're going to review plans. You're going to give feedback. You're going to review the code like the poll requests before you merge it. You're

**[5:43]** always the bottleneck for verification before progressing. That's level three. And honestly, that's where most of us

**[5:50]** are. And you know, like when I teach AI coding on my channel and in the Dynamis

**[5:55]** community, level three is actually what I generally recommend because this is the furthest you can push it right now

**[6:02]** and still get the most reliable results possible. So level four, um, this is

**[6:08]** where we get into the engineering team, when we get into harnesses for longer running tasks. And so this is where you

**[6:14]** actually get to fall asleep at the wheel. So you let the AI run unattended for long periods, handling very complex

**[6:21]** tasks. And so you think of harnesses like the Ralph loop or anthropics harness, giving your second brain the

**[6:26]** ability to handle issues and pull requests end to end. So here, you still

**[6:31]** are going to check the final results. like at some point you're gonna you're going to wake up and just like make sure the car is actually driving you to the

**[6:37]** right place and you know take your put your hands on the wheel if you need to, but for the most part you're trusting

**[6:42]** the coding agent to handle insanely long sets of work. So level four, I I

**[6:48]** wouldn't say this is like the most reliable at this point. If you want to ship the most reliable production code possible, you're still at level three

**[6:55]** because you're still going to monitor everything and be the bottleneck for verification, but you're starting to really take yourself out of the loop

**[7:01]** with level four. But there's still the steering wheel, right? Like there's still the opportunity for you to step in

**[7:07]** and fix things yourself or steer the agents in a different direction in the middle of some implementation.

**[7:14]** And then that brings us into level five. And I love the car analogy here cuz you

**[7:19]** like you look at level four and there's still the steering wheel like right there's still the opportunity for you to have control. But in level five, your

**[7:26]** vehicle looks like this, which someday we'll get there. That'll that'll be really cool. the day that I have a

**[7:31]** vehicle, it looks like this. But there's no there's no steering wheel in this vehicle. There's not even the option for

**[7:37]** us to take the reinss if we want. That's what a dark factory is. So the engineer

**[7:43]** manages the goal in the system, right? There's still some kind of console here to provide higher level direction. We're

**[7:49]** still going to write the PRDS. We might manage the some of the releases, but

**[7:54]** we're not managing the code. So we provide plain English descriptions but the agent defines implementation, writes

**[8:00]** code, tests, fixes, bugs and ships. That is a dark factory. And uh that my friend

**[8:07]** is what we are going to be building today. I have a good amount of the system already set up because I don't

**[8:13]** want to go through all the like really boring parts with you. But I I want to work on the workflows today. like

**[8:20]** actually build the workflows that are going to manage the entire dark factory because it's not enough to just point

**[8:26]** cloud code at a GitHub repo and say manage everything right we have to teach

**[8:31]** it like how do we want it to handle issues what kinds of features are we going to build into this application how

**[8:37]** do we want to evolve it what are the constraints that we have how are we going to review code right we have to

**[8:44]** create workflows to define exactly how we want to write so right so like the engineer manages the goal bonus system.

**[8:50]** I'm talking about building the system here for this vehicle. And so, um, what

**[8:56]** I'm going to be doing, and this is this is the most exciting part for me, is I'm going to be leveraging Archon workflows

**[9:03]** to manage every single part of the dark factory. So, Archon is my first ever or

**[9:09]** it is the first ever open- source harness for AI coding. First ever harness builder, sorry. So you think

**[9:16]** about like whatever your process is right now for software development, however you work with AI coding

**[9:21]** assistants, archon allows you to build workflows to package everything up so that you can build any on any codebase.

**[9:28]** You can invoke any workflow, [clears throat] excuse me, you can invoke any workflow in parallel and you

**[9:34]** get reliable results every single time because you're taking your process and you're packaging it up. That's what Archon gives us. And so if you're

**[9:41]** interested more how Archon works and you haven't seen my content on it recently. There's a lot that I put out on my

**[9:47]** channel recently. So there's a couple of live streams that I did. Actually one just two days ago. Um so I did it just

**[9:52]** on Saturday last week. And then I also have a YouTube video, my most recent

**[9:58]** YouTube video where I covered Archon. So I'm not going to get like super deep into an introduction to Archon today

**[10:03]** because I already have this content. But I'm going to be using it as a very critical part of the workflow of the

**[10:10]** whole system for the dark factory because it's going to drive everything. I'm going to build archon workflows to

**[10:16]** manage my issues, build archon workflows to write the code, review the code,

**[10:22]** manage the releases. I'll talk about what that looks like when I get into my plan here. So, I have this entire

**[10:29]** markdown document that outlines my entire plan for the dark factory and I

**[10:36]** took a lot of inspiration from um you know other examples of dark factories that are already out there on the

**[10:42]** internet. And so maybe you guys have heard of the strong DM use case. So

**[10:48]** strong DM is a company that they actually manage a production codebase

**[10:53]** with a dark factory. They are shipping pull requests all of the time that don't have any human review at all. And their

**[11:02]** dark factory is unfortunately not open source like mine is going to be for you guys to see and watch it evolve in real

**[11:08]** time. But they did share something like a PRD. So they have this open-source

**[11:15]** spec for building their dark factory. They call it the attractor. And so we

**[11:20]** don't have the codebase, but we do have the plan document that uh I guess theoretically you can use to have your

**[11:27]** coding agent build out exactly what they have for managing their code base with no humans involved. And so I I did

**[11:34]** actually take a lot of inspiration from the ideas here. If you guys are interested in any of this, I'm planning

**[11:39]** on putting out a YouTube video tomorrow where I'll have like a more concise overview of everything and I'll have links to this all. I can of course put

**[11:46]** links to this in the chat, too, if you guys are curious. So, um I will put a

**[11:53]** link to this blog post right here and then u I'll put a link to this resource

**[12:01]** covering the uh dark the strong DM dark factory if you guys want to read through it.

**[12:07]** Just want to make sure I give those to you guys because that's a lot of like my initial research for building a dark

**[12:12]** factory and I'm super fascinated by this. So, okay, let me be really clear

**[12:18]** here. I want to be clear on something and then I'll explain more the the architecture that I have for my archon

**[12:24]** dark factory. I know I already said this but it's worth repeating that you're not going to

**[12:30]** get the most reliable results with your coding agent when you give it this much autonomy. I highly recommend when you're

**[12:37]** doing things for real, you put yourself in the loop. At least reviewing plans and reviewing code. those two stages of

**[12:45]** the development cycle. I would at least have those. So, this is definitely a public experiment. I'm calling it an

**[12:52]** experiment because it might fall completely flat on its face. We'll see. I mean, I'm going to put a lot of work

**[12:58]** into trying to make it really reliable, but I have no idea how the codebase is going to end up evolving when I leave it

**[13:05]** to literally manage itself. And so, the input for the dark factory is going to

**[13:11]** be a GitHub issue. So I as a user and then I'm going to make this public so

**[13:16]** you guys can literally submit GitHub issues as well. It's going to be so fun when I get this really running. The

**[13:21]** input is a GitHub issue and so this is either a bug that we've noticed in the platform as we've tested it as a user or

**[13:28]** it's a new feature that we're requesting the dark factory to add into the codebase. So we create a set of GitHub issues like

**[13:36]** maybe there's you know 20 that are created in the last hour something like that and then on a schedule basis I'm

**[13:41]** going to run the first archon workflow and calling it the triage workflow because the responsibility of this

**[13:47]** archon workflow is to look at all of the GitHub issues and it's going to judge

**[13:53]** the issues against the core governance layer that I'm going to build into the

**[13:58]** the um dark factory repository. So, we're going to have our our mission for the repo and then the different rules.

**[14:06]** And these files are going to also include the scope that we're going to allow for the codebase evolution. Like

**[14:12]** here are features that we're definitely not going to allow. Here are types of features that we are going to allow. So,

**[14:18]** basically the triage workflow is going to evaluate all of the GitHub issues

**[14:24]** that were created in the last hour, you know, like everything that hasn't been triaged yet. And it's going to figure

**[14:30]** out like, you know, based on our mission and rules, what issues should we, you know, put in a comment and close and say

**[14:36]** like, hey, this doesn't apply for X, Y, or Z reason or here's an issue that we're going to go into the implement

**[14:42]** step. So, triage and then we're going to have a separate archon workflow that goes through the full implementation. So

**[14:49]** for every single issue that we decide we are going to address, we're going to invoke Archon workflows in parallel to

**[14:56]** do the full implementation. And so again leaning on the beauty of archon here, we can handle any number of

**[15:03]** issues in parallel because it each of the issues are going to be handled in a a work tree. So we have full isolation,

**[15:10]** full copy of the codebase for each one of the issues to be worked on independently without stepping on each

**[15:17]** other's toes. So we implement and then for every single one of the issues that

**[15:22]** we addressed either a bug that we fixed or a feature that we built we're going to have a separate archon validate

**[15:28]** workflow. So this is where we do the PR review before we do the merge into main.

**[15:34]** And one of the things that strong DM implemented in their dark factory that's very powerful is um what they call the

**[15:41]** hold out pattern. So the hold out pattern is the idea that we don't want

**[15:47]** the bias from the implementation to go into the testing. And this is such a

**[15:53]** prevalent problem with coding agents in general is they will uh if you ask it to

**[15:59]** check its own work, it's like asking a student to check their own homework.

**[16:04]** They might, you know, give a little bit of feedback just to seem like they're they are being critical of themselves,

**[16:10]** but in the end, their bias is going to win out and they're going to stuff the bigger problems under the rug. And so

**[16:15]** what we do is a handoff. After the implementation, we go through all of our testing scenarios, but we don't tell the

**[16:23]** validation agent what was just implemented. So we basically just do regression testing over the entire system. So that way there's no chance of

**[16:30]** bias because it doesn't even know like what the issue was meant to address. [clears throat] And that sounds kind of

**[16:36]** risky and like honestly myself I'm not fully convinced of this but that that is strong DM's hold out trick and we're

**[16:42]** going to try building that as well. That's why we have a separate workflow for validation and we don't just have it built into the implementation.

**[16:49]** Now in archon you can just like you know start fresh sessions between nodes. So I guess we could package this up as one

**[16:55]** workflow and still have the hold out pattern. Um, that's one of the things I'll just kind of have to explore as I'm building with you guys. Like I'm setting

**[17:01]** a lot of this up from scratch. Like this is a live coding session. Like I said, I'm not presenting something that I've

**[17:07]** already built like I did with Archon in the last live stream. So yeah, uh, that's pretty much the

**[17:15]** workflow here. So I mean really it just comes down to we have the governance layer. These are pieces of context we're

**[17:20]** always going to inject into every Archon workflow. And then we have Archon workflows to handle the full orchestration here. triage, implement,

**[17:27]** validate, and fix. And as far as the repository that this

**[17:32]** is going to operate on, it is going to be uh this one right here. So,

**[17:37]** obviously, I'm not going to use archon to work on archon here. I don't want to turn archon into a dark factory

**[17:44]** repository. It is too important that that this doesn't just become an experiment. So, there's a separate repo,

**[17:50]** a separate project that I'm going to build using the archon workflows in the dark factory. And uh it's actually a

**[17:56]** pretty cool um application like this is going to be a huge value ad for my

**[18:01]** YouTube channel because essentially it's going to be a chat platform and a gentic chat platform where you can ask it any

**[18:08]** kinds of questions around AI and then it's going to perform rag. It's going to search through my YouTube videos to give

**[18:15]** you an answer. So it's kind of like your own AI tutor based on my content. And then I was also thinking about doing

**[18:21]** something for the Dynamus community. If you are in the Dynamis community, you can connect your account into this

**[18:27]** platform. So then not only would it search over my YouTube content, but it would also search over my workshops and

**[18:33]** courses that I have in the community. So it become like the ultimate AI tutor. So it' be like available to everybody, but

**[18:39]** then it'd be even like a nice value ad to Dynamis as well. So I'm actually really excited to build this out. Um,

**[18:44]** and so if the dark factory experiment doesn't work for whatever reason, um, and like I have faith in it, but it is

**[18:51]** very risky. Like so if if if it doesn't really like build on anything that like works super super well then I'm just

**[18:56]** going to you know build it myself with my usual AI coding process because I want to have this by the end of the month for everyone. Uh but we'll see if

**[19:03]** a dark factory can manage everything because I'm going to work hard to build that initial AI layer. U let me actually

**[19:10]** refresh here because I I already created the mission factory rules in claw.md. So I'm going to work hard to build out

**[19:17]** the the [clears throat] governance layer, build out the archon workflows. I want to make this as reliable as

**[19:22]** possible. Now, the biggest risk that we have to this dark factory

**[19:30]** is that I can't actually use my anthropic subscription

**[19:36]** because I would hit my rate limits way too fast. And if I want to uh make this

**[19:42]** public so anybody can create GitHub issues for the dark factory, I believe

**[19:47]** that would be against the anthropic terms of service. if I let other people's GitHub issues

**[19:53]** get automatically consumed into the system because then it's essentially other people being able to use my

**[19:58]** anthropic subscription because I'm not the one starting the workflow. It's like technically another user I think. I just

**[20:06]** want to be careful there. And I'd hit my rate limits way too fast anyway. So I can't actually uh use my anthropic

**[20:12]** subscription for the dark factory. And so what that means is I have to pay for an API. I have to pay per token for

**[20:20]** everything I have built in this that I'm going to build in this dark factory. And

**[20:26]** u unfortunately opus would be way too expensive. So I have to resort to other means and

**[20:34]** actually what I came up with is I'm going to use Miniaax M2.7

**[20:40]** as the large language model driving the entire dark factory.

**[20:46]** Now, um I've done a lot of research for different models. I considered um Quen

**[20:51]** 3.5 coder. I considered GLM 5.1. I thought about maybe using like Sonnet,

**[20:58]** but Sonnet would be too expensive. Um I was maybe going to use Sonnet through Open Router or just the Enthropic API

**[21:05]** directly. Haiku would definitely be not powerful enough. So, I I can't really use an anthropic model, right? Because

**[21:10]** like Opus and Sonnet are too expensive. Hi coup is like significantly worse than miniax m2.7 and they're actually a

**[21:17]** pretty similar cost I believe. Um yeah because like if I go to open router here

**[21:24]** and I search for claude haiku 3 or 4.5

**[21:29]** it is um $1 for every 1 million input tokens. It's actually more expensive

**[21:35]** than um miniax m2.7 that this it's less

**[21:41]** than a dollar. Yeah, it's only 30 cents for every 1 million input tokens. So, it's a third the price of Haiku and way

**[21:47]** better. So, there's no reason if I'm not going to use my Anthropic subscription, there's no reason for me to actually use

**[21:52]** an anthropic model because Opus and Sonnet would be way too much. And so,

**[21:57]** yeah, I I did a lot of research and this is what I landed on. And I can always switch the entire system. But what I've

**[22:04]** done here, and this is part of the setup that I've already taken care of automat or behind the scenes, is I already have

**[22:11]** a VPS spun up where I have archon installed. I have the rag YouTube chat

**[22:18]** application cloned and and configured. And then I have my cloud code changed

**[22:25]** there to uh use Miniax M2.7 instead of

**[22:30]** enthropic. So if I ask like here uh give me the SSH command. I'll actually show

**[22:35]** you guys. I'll SSH into the machine live with you and show you what it looks like. So all right, I'll grab this

**[22:43]** command here. All right,

**[22:48]** cuz uh take a look at this. If I go into claude, I [snorts] open up Claude while

**[22:54]** SSH into this machine, you can see that it's using Miniax M2.7. And if I say,

**[23:00]** you know, like what model are you? Everything looks like I'm using Claude, but uh or that I'm using Claude code

**[23:07]** normally, but it is actually going and and using my miniax API key and running

**[23:12]** on M2.7. And by the way, if I wanted to use like GLM 5.1 instead, it would be super easy.

**[23:19]** Like I could swap over in like 30 seconds. Uh because all you have to do to swap the provider for cloud code is

**[23:27]** you just have to change a couple of environment variables under the hood like and and by the way this session that I have open with cloud code this is

**[23:33]** on my local computer where I'm doing some setup locally and uh what I had in

**[23:39]** this session I had it read my whole dark plan. So like everything you see right here it has loaded into the context

**[23:45]** currently. So I can just ask it here. Uh don't show any secrets but tell me exactly how I changed claude code to use

**[23:52]** miniax m2.7 instead of anthropic for the model. Um so I I might actually open source my

**[24:00]** entire dark factory plan cuz as I've been setting things up behind the scenes, I've just been like documenting everything in this like pretty massive

**[24:07]** file here, including all of the archon workflows that I'm going to build with you guys live right now. So, I have a a

**[24:13]** plan initially for every single one of these. So, we'll build them today and test them and maybe get to the point

**[24:18]** where we have the whole dark factory running. I'm not sure if we'll get that far because it's going to be quite a bit of setup. Um, but yeah, you can see that

**[24:26]** uh for switching the provider for cloud code, you just have to set these

**[24:32]** environment variables there. There's quite a bit here. So, I think it actually would be pretty useful to share

**[24:37]** this with you guys. uh because there were there was a it was a little bit trickier than I thought it would be to

**[24:43]** switch the provider. Uh because then you what the other thing you have to do for archon is you have to map the

**[24:50]** environment variables for the different model types because in archon you know for each of the workflows you can

**[24:55]** specify like for this node I want to use sonnet or this node I want to use haiku

**[25:00]** and so to make the archon workflows work out of the box without having to change these ids you just have to map it

**[25:07]** through environment variables. So like when I specify opus and claude code or in an archon workflow that maps to

**[25:14]** miniax m2.7 same thing with sonnet and then if I want to use haiku then it maps

**[25:19]** to miniax m2.7 high speed right so just a faster and cheaper version of m2.7 so

**[25:26]** I have the same effect in an archon workflow where I can make some things a lot faster and then other things I have

**[25:32]** the most power I possibly can um like if I typically would use opus or maybe sonnet

**[25:39]** So yeah, if you are interested in using claw code with a different provider, it's actually quite easy to set up. So

**[25:47]** you could have it use open router if you want to use the enthropic models there. Um GLM has an enthropic compatible

**[25:53]** endpoint. Um of course miniax does as well. I think Quen does. Does does Quen

**[26:00]** have a Claude code compatible endpoint? And if you want to run local models with

**[26:07]** [snorts] cloud code, you can use Olama as well. So Olama has a direct

**[26:12]** integration with cloud code. So it's kind of cool because we are planning on adding PI support this week for archon.

**[26:19]** So you can run all of your workflows through PI agents. But even right now, you are able to uh

**[26:25]** immediately switch cloud code to use any models so that you don't necessarily have to lean on another provider, but

**[26:30]** you're not stuck to using your anthropic subscription or the anthropic API key.

**[26:38]** Okay. Um let's see. Yeah, I don't think Quen has

**[26:45]** Okay. But like GLM and Miniax have the anthropic compatible endpoints.

**[26:52]** So yeah, just ask Claude to do some research for you to see like which ones are compatible with Claude code, but most models you're able to use directly

**[27:00]** like I set up with Miniax here. All right.

**[27:07]** See what it says here. Yep. So yeah, GLM has a first party anthropic compatible endpoint. So it's like literally their

**[27:12]** API endpoint and then you just add anthropic at the end. So that that's what you hit when you want to make it compatible with cloud code. So pretty

**[27:20]** cool. was pretty easy to set it up. All right, cool. So, uh, yeah, I want to

**[27:26]** get into building with you guys here. Let me check the context. Maybe I'll spend a little bit of time to answer you

**[27:32]** guys' questions. I know I haven't really looked at the chat yet. Definitely want to do that. So, I'll I'll spend a little bit of time doing that and then we can

**[27:39]** get right into building out our factory. So, going to the diagram here. I already have the governance layer built out and

**[27:46]** then as I'm creating the workflows I'll show you guys what that looks like. So right now I mostly just need to build

**[27:51]** out the archon workflows and it's important for all the archon workflows to like actually ingest these

**[27:59]** documents here. Like it needs to know like no matter what workflow I have running if I'm fixing something,

**[28:04]** validating something, whatever like it has to always know the mission and factory rules cuz that's going to be the primary guidance. And then I mean of

**[28:11]** course the global like the claw.md as well. So yes I am doing everything through

**[28:16]** cloud code but um I mean you could easily make this dark factory do like use codeex or open code or pi instead

**[28:23]** but yeah it's just what I'm using. I like using quad code as a harness even if I'm not using anthropic models.

**[28:31]** All right cool. So yeah, I'll leave this up and then I'll I'll go ahead and hit some questions from the chat here.

**[28:38]** And the future begins. That's right. That's what we're building. We're building the future here. I don't think that that uh the Dart factory is a

**[28:45]** pattern that's reliable enough right right now. But if we refine the workflows enough and if we have we'd

**[28:51]** probably need more powerful models as well, honestly, to like really make this production ready. But maybe Mythos is

**[28:56]** going to be the unlock. We'll see. All right.

**[29:03]** I'm level 11 or negative one. Not from a tech background at all. I mean, that's

**[29:08]** all good because uh with how powerful AI coding assistants are right now, you can

**[29:13]** get to level three very very quickly. And in fact, if you don't have a tech

**[29:20]** experience, you probably won't ever be level zero through level two because that requires you to write code yourself

**[29:26]** sometimes. And so these days when you learn how to leverage AI coding assistance and you're not coming from a

**[29:32]** technical background, you just jump right into level three. My big recommendation with that though is to

**[29:37]** ask your coding agent a lot of questions as it's creating code for you so that you can start to gain an understanding

**[29:42]** and like you know sort of become at least semi-technical yourself as you're using the tools.

**[29:50]** Um will this video be saved for later? Uh 100% Leonards. Yeah. So every single

**[29:55]** live stream on YouTube is automatically turned into a recording after. So I don't even have to like upload it myself. And so I think it takes a little

**[30:02]** bit of processing time, but like what we have right here, it says live right now. It'll be turned into another video just

**[30:08]** like my live stream this weekend. So you just have to go to the live tab. It's not in the main video tab for my long

**[30:13]** form content. You just go over here and then it'll be available for you.

**[30:19]** All right.

**[30:26]** I still feel like I need to test things myself. I don't yet trust AI to test and especially ship. I'm with you there.

**[30:34]** Yeah, like I said, level three is where it's at when you really care the most about reliability. Unless you've built

**[30:40]** some kind of level four harness that you really, really have faith in, I would generally recommend sticking to level

**[30:46]** three. And then level five is like no one really knows how much this is really

**[30:52]** going to work at this point. And that's what I want to find out with you guys. Like, yeah, we have examples like strong DM, but they haven't they they've not

**[30:59]** really shared that much, right? And like a lot of it could just be like marketing hype. So, that's what I want to figure out for you guys for real is like if we

**[31:06]** actually put a lot of effort into using Archon and uh building a lot of reliability through a government's

**[31:11]** layer. Like, how reliable can we really make it? And I'm excited to find out. We're going to do it together.

**[31:20]** um you don't trust that if it's secure more than everything is working. I mean okay so sorry this is the question to

**[31:26]** follow up from the other one but I mean I I would say personally that like security is a big concern for AI coding

**[31:32]** assistants. They do introduce more security issues than uh seasoned engineers. um they can valid they can

**[31:40]** fix them as well but like first pass they introduce more um and then yeah just like generally that everything is

**[31:45]** actually working cuz okay here's the other problem with AI coding assistance and then honestly probably the main

**[31:51]** reason that level five might fail it's not necessarily that the coding agent produces code that fails but it's more

**[31:59]** that it's just not aligned with what you want to create and that's part of why I'm going to be focusing so much upfront

**[32:05]** on building the government's layer because I need to be very clear on the guard rails and the guidelines for the

**[32:12]** coding agent so that when it picks up an issue and implements it uh first of all

**[32:18]** I want to make sure the issue is actually aligned with what I want for the codebase for the evolution of it and

**[32:24]** then also like when it does the implementation itself that it doesn't misunderstand what the issue is really getting at like if I open an issue

**[32:30]** because I want to improve the rag search I don't want it to like change the front

**[32:35]** end I want it to just like change the rag pipline line for example.

**[32:41]** All right. See what else we got here in the chat.

**[32:47]** Um I presume the dark factory can introduce bugs later down the line if proper unit testing linting and bug

**[32:53]** fression system is is set up correctly. Um, so yeah, that's going to be one of

**[32:59]** the risks of the dark factory as well as there might be little problems that creep in that our validation doesn't

**[33:05]** catch and they might blow up in our face later on. That's one of the reasons human in the loop is so important for

**[33:11]** reviewing things is to catch those little issues that become a bigger problem later. U so the dark factory

**[33:19]** could kind of be like boiling a frog in water, right? like the frog. If you put a frog in scalding hot water, it's going

**[33:26]** to immediately jump out of the pot. And so the analogy here is like if we have a

**[33:31]** massive issue in the codebase right after implementation, the validation is going to catch that

**[33:37]** and it's going to address it. But if it's something that slips under the crack cuz it's not super apparent right away, it's like the frog that you put in

**[33:44]** warm water and then you boil it over time and so it stays there until it's dead, [laughter] right? Like that could

**[33:49]** happen to a dark factory. you have the these little issues that creep in over time. It's not big enough for the validate agent to catch it, but then

**[33:57]** they combine together to produce bigger problems or it's just an issue that compounds on itself and you're not there

**[34:03]** in the loop to find those things and correct those things. So it's certainly possible and uh as much as we can that's

**[34:10]** why it's it's important for us to build a very comprehensive validation process not just with unit testing and linting

**[34:17]** but I'm going to be building in like full regression testing like every single time we handle an issue I want

**[34:22]** the validation to use a browser automation tool to go through the rag

**[34:27]** chat application like just like a user would and u like test this whole interface and have different

**[34:33]** conversations and click on the source ources at its sites and make sure that goes to the right part of a YouTube video. Like I it's got to be doing

**[34:40]** everything and constantly kind of like maintaining this list of features that it needs to test every time it's doing

**[34:46]** proper regression testing. So we'll get there. That's going to be probably one of the biggest challenges to build for

**[34:51]** this whole thing.

**[34:57]** All right. Um, also will be handy if you can suggest open source or free alternatives

**[35:03]** if available out there for the tools we're using. As a learner, those crazy bills make my heart sing. I'm with you.

**[35:09]** I understand the pain for sure. So, I guess I'm curious like what tools you're referring to exactly. If you're talking

**[35:15]** about AI coding assistance, unfortunately, there's not really a a free alternative to something like

**[35:22]** Claude Code that's just as good as Claude. Like I was talking about earlier, I'm using Miniax M2.7 instead

**[35:28]** of Opus because it's a lot cheaper. It's still not going to be as powerful. And if you really want like free AI coding,

**[35:35]** then my recommendation is to run a model in Cloud Code through Olama. Like you

**[35:41]** could run Gemma 4. Um Quen 3 has some smaller good models. You're not going to get nearly as good of results as Opus

**[35:48]** though. But like it is possible to do AI coding free. you just have the expectation that um you can't do the

**[35:55]** same things that you can do with Opus or some other more powerful model like GPT

**[36:00]** 5.4 for codeex in codeex for example. So all right

**[36:12]** let's see got only one year to experiment.

**[36:17]** Oh let's see the comment above. I'm thinking of creating some kind of architecture for local businesses here

**[36:22]** if I can and provide them. So got to be safe easy to set up and manage for them and myself and I don't get sued.

**[36:28]** Yeah, I'd be curious what kind of architecture you're talking about, like if it's an agentic system or if it's um

**[36:34]** like if it's an AI agent or like for AI coding. Sounds cool, though.

**[36:42]** All right. Gemini makes a good evaluator to run

**[36:48]** against Claude. Yeah, that is one of the things I want to be experimenting in with archon soon is building workflows

**[36:54]** that combine providers so that we can do like exactly what we were describing like claude for implementation and then

**[37:01]** Gemini a lot of people like using codeex for review as well just to to have a check on claude uh so yeah that's going

**[37:08]** to come soon for archon all right

**[37:15]** cool Um,

**[37:22]** was that excaladraw in Obsidian? Yes, my Excalad draw diagrams I always

**[37:28]** have in Obsidian. So, I'll show you that really quick. If I go to the settings and go to my community plugins here, I

**[37:37]** use I just use the Excal plugin by uh Z Sult. I don't know if I'm saying

**[37:43]** [laughter] that right, but yeah, I've used this for a long time now. Very, very good cuz I just want to have

**[37:49]** everything in my vault together. Diagrams, research, everything. So, I love using this plugin all the time.

**[37:58]** All right, cool. So, a little paywalled after all. Let's

**[38:05]** see. Right. For AI coding, if you want to get the best results, it is paywalled

**[38:10]** right now. Um, and I mean unfortunately it makes sense like these frontier models like

**[38:16]** Opus and GBT 5.4 Codeex, they are expensive, man. Like these companies are

**[38:22]** burning through billions of dollars of venture capital right now just to have these models running for the world and

**[38:28]** they're just starting to like make some profits from getting it like the higher levels of enterprise agreements. Um

**[38:34]** because trust me, they they don't make money off of your anthropic subscription if you are really maxing out your rate

**[38:42]** limits for claw code. Where they're really making the money is using you as the lever to get the enterprise

**[38:48]** agreements, the enterprise interest. So they're they're profitable, but it's

**[38:54]** it's very subsidized for our anthropic subscriptions. And that's part of why they're jacking down the rate limits

**[39:01]** right now. It's kind of unfortunate. It's uh I am not get I'm not able to get nearly as much out of claw code with my

**[39:08]** anthropic subscription compared to even like a couple weeks ago. Um the rate limits are are worse now unfortunately.

**[39:16]** And they took away my 1 million token claw code. That's another thing that I'm kind of frustrated by. Um, like if I if

**[39:23]** I do slashmodel, apparently some people still have this, so I don't know why it's just me, but I don't have the

**[39:30]** option to use a 1 million opus or or sonnet anymore.

**[39:35]** So, I'd be I'd be curious if anyone else has run into this as well,

**[39:40]** but I'm stuck to 200,000 tokens again as of like just three days ago. I don't

**[39:46]** know why. Or maybe it was like a week ago. But [sighs] yeah, anyway,

**[39:52]** so yeah, I'm gonna have more time to answer questions as we are waiting for the uh workflows to be built here. Uh,

**[40:00]** one thing I want to put in the chat quick is just a link to Archon. So, if

**[40:06]** you're interested in checking out Archon, like got some good content on my channel. Uh, I got the live stream from

**[40:13]** the weekend and then also I have the YouTube video that I put out just five days ago on Archon. So check that out if

**[40:19]** you're interested. Like I said, because I've already done so much content, I'm not going to be like hyperfocused on explaining Archon, I'm going to get

**[40:25]** quick, pretty quick here just into doing [snorts] a live coding session creating the Archon workflows with you guys. Um,

**[40:34]** and then also the repository that I'm using the dark factory to build this is

**[40:40]** private for now. Um, well, no, actually, I made it public, but I'm not going to

**[40:45]** make it so that you can give any issue to the dark factory yet. So, I'm going

**[40:50]** to start by having it only accept issues from me. And um, then I'll make it so

**[40:56]** it's available to everyone after I've like tested things for about a week is my plan. Something like that. In fact, I

**[41:03]** might actually want to make this repo private right now as I build this as a safety measure. We'll see. I I might

**[41:09]** have to switch it private and tell them I'm confident that it really is only handling my own issues. [laughter]

**[41:15]** So, we'll we'll have to do that in a little bit. But, let's start by building the Archon workflows here.

**[41:23]** Okay. So, in my chat, how much do I have? Okay, I have 40% of my context

**[41:28]** used. So, I should be good to continue here. So again, this conversation that I have,

**[41:35]** it already has my full dark factory plan loaded. And so I can literally just ask it like

**[41:41]** what should I build next? Because I've been keeping a log of everything that I've created as I built it. So like for

**[41:49]** example, one thing that I already did is I created the core government's uh doc

**[41:54]** governance documents. So I have like my mission.md factory rules. I can show that to you guys like a little bit of

**[42:00]** what went into that um as the workflow is building. I just want to be efficient with the time here.

**[42:07]** All right. So,

**[42:13]** so there's some things that I was doing during an event in the Dynamis community. And then uh here's the remaining punch

**[42:20]** list from section 14. I told you it's comprehensive. Section 14 of the plan.

**[42:25]** uh ordered by what makes sense to build now and save for live.

**[42:30]** Okay, so I guess there's a couple of things that it recommended that I do before the live stream here, but also

**[42:35]** these are going to be super quick to set up anyway. We need to create the GitHub labels, um the issue and PR template,

**[42:44]** orchestration shell script. Yeah, I'm going to

**[42:49]** Yeah, I'm going to have it rip through all these things in parallel. So, okay, the GitHub labels are actually kind of interesting because everything in the

**[42:56]** dark factory is going to be managed through labels. So, when the triage workflow runs, it's going to basically

**[43:02]** check on these labels as a status like this thing is currently being implemented, right? like don't don't

**[43:08]** send off another Archon workflow to work on this because it's already in progress

**[43:14]** or worst case scenario if it fails to implement a pull request two times in a row I'm going to have it label needs

**[43:21]** human so maybe I'm not making this like fully fully dark factory but I do want

**[43:26]** to at least have like a small escape if I really need to address something myself so I have a little bit of a

**[43:32]** system created for that and then uh yeah like if I reject an issue like this doesn't fit with our mission or if I

**[43:38]** approve it and we're not going into implementation yet, then I'll add that label. Um, and then factory rate limit.

**[43:44]** I'm going to have some protection to make sure I don't blow through like hundreds of dollars of miniax credits in a day. And so if we need to wait for the

**[43:52]** next day for the rate limits to subside that I'm going to build into the system, then we'll add this label as well. So

**[43:57]** yeah, it's hard even in a live stream to get like super deep into everything that I planned here. But I hope that you can

**[44:03]** see from the the label system that I have for these GitHub issues like there's a lot of thought that I put into

**[44:09]** this system even handling like rate limits and human escape if I really

**[44:14]** really need it. Um, so yeah, really like the important thing here is the GitHub

**[44:19]** issues are driving the entire dark factory because any kind of input into

**[44:25]** the system for a bug that needs to be fixed or a feature that needs to be created, the input comes in from an

**[44:30]** issue, whether that's me creating it or the dark factory itself creating the

**[44:35]** issue because we do also have a sort of feedback loop here where when the validation agent runs its regression

**[44:41]** testing, if it encounters any problems that are big enough to not just be fixed right then and there, then it'll create

**[44:46]** a GitHub issue and then go through that loop and then address that and so anything that it catches in regression

**[44:51]** can just be more issues for it to fix autonomously and uh so yeah I mean like

**[44:57]** hopefully doesn't mean that we'll hit infinite loops of creating issue and issue and issue after issue but might

**[45:02]** happen that's part of the experiment we don't we don't know what's going to happen or what could go wrong uh but that's why I have protections in place

**[45:08]** to make sure that it doesn't um just jack me up in credits

**[45:14]** so yeah like When I I have my balance here, I I only put like 25 bucks to

**[45:20]** start and then I've used like, you know, 87 cents in my testing so far. It's

**[45:25]** pretty efficient overall, but I'm going to make sure that I um

**[45:30]** yeah, never have like too much. like I'm I'm disabling auto billing so that if I

**[45:36]** run out of credits, I just have to manually u add credits and then I'll have the

**[45:41]** system that like detects when issues weren't handled because of rate limit and it'll pick it back up basically.

**[45:47]** Um, okay. So, I'm going to say, uh, so I'll go into my speech to text

**[45:53]** tool and I'll say, I want you to create the GitHub labels, issue and PR templates, and, uh, the orchestration,

**[46:00]** shell script, and cron entry on the VPS. So, handle all of these right now.

**[46:05]** I'm actually in the middle of the live stream now. And so, I will just explain the workflows briefly as you do these

**[46:12]** things. All right, there we go. It still thinks that I'm not in the live stream yet. So, I'll give it an update

**[46:18]** of of where I'm actually at. [laughter] Claude Code doesn't really have a sense of time.

**[46:26]** Okay. So, while that runs, who's paying for all this quota context?

**[46:33]** I'm paying for it. It's It's coming out of pocket, which is why I'm using something very cheap like Miniax M2.7.

**[46:40]** Yep. Okay. So, let's see. Okay, let's go back

**[46:45]** to the dark factory plan. I want to show you guys a little bit of what the archon

**[46:50]** workflows will probably look like. So, what I have here, these are very much

**[46:57]** rough drafts of the archon workflow. So, when I actually build them in a little bit in our stream here, they might end

**[47:03]** up looking quite different. But when I was doing my initial planning with claude code, creating this whole

**[47:10]** dark factory plan, I also had it load the primary archon skill. So it knows

**[47:15]** how to build workflows. It knows the different parameters, things like that, how to use the archon CLI. So it created

**[47:21]** the initial draft for them. And so there are four workflows that we need in

**[47:26]** total. We have the triage workflow. This figures out what GitHub issues we

**[47:32]** actually want to address and it handles the labeling and things like that.

**[47:37]** And then uh we have the implementation workflow. I have to gosh I have to scroll a while here. We have the uh

**[47:44]** implementation. Wait, I already scrolled past it. Where'd it go? Where's the header here?

**[47:51]** There might be some malfformmatting. Oh no, here it is. Um wait a second.

**[48:00]** Does this do the fix as well? Classify apply decisions.

**[48:07]** Oh, I think there might be a misordering here. So, okay. Anyway, we also have the validate PR workflow. So, this is what

**[48:13]** we're going to run that we're going to do the whole like hold out pattern for validation. We're going to run this on

**[48:18]** every pull request that's created from the workflow that does the issue fix.

**[48:24]** I thought that would be the second one. That's why I'm confused right now. Um, I'm not sure where that maybe that maybe

**[48:29]** it just misordered things. So, oh, oh, yeah, it did misorder things. Okay, that's kind of weird. But anyway, this this should be the second workflow. I

**[48:35]** don't know why Claude put it in the plan in this order, but our uh next workflow is the one to actually fix. Um, no, no,

**[48:42]** that's not it. This is this is a workflow to fix issues that happen during PR validation. So if there there

**[48:49]** are any problems that come up when creating the poll or when reviewing the pull request, then we run this to

**[48:54]** address things and then push a new change to update the poll request.

**[48:59]** Um and then we have the comprehensive test. So this is the

**[49:05]** regression testing workflow. And this one is going to take a lot of tokens. So, I'm planning on running this

**[49:12]** one only like once a day or once a week because it's going to look through every

**[49:17]** single possible user journey, every single way we can use the application, testing every single edge case, making

**[49:22]** sure that it works automatically. And then for any things that don't work, it's going to create a GitHub issue,

**[49:28]** right? So, every time we review a pull request, we are going to do a lot of regression testing, but it's going to be

**[49:33]** a more concise version of this workflow because this is going to be like pretty tokenheavy. And then yeah, I guess the one thing

**[49:39]** that it didn't do is it didn't create the workflow for actually fixing the issues. And um I I sorry, I remember now

**[49:46]** why that's the case. It's because there's a a default GitHub fix issue workflow in Archon that I'm just going

**[49:53]** to use or maybe make a little bit of an adaptation for, but then for all the other workflows, they have to be created

**[49:58]** from scratch. So I apologize. I Claude kind of confused me here or I forgot the planning that I did with it. But yeah,

**[50:05]** we'll get into creating the workflows in a second here. Okay,

**[50:11]** cool. So, all three tasks are done. We created the GitHub labels and the issue

**[50:16]** templates and then we created the orchestrator. So, we're we're basically going to create a cron job that runs on

**[50:22]** our VPS every so often. And whenever this job triggers, it's going to uh

**[50:28]** basically prompt Claude to use the Archon CLI to invoke the workflow. was

**[50:33]** like, "Okay, it's time to triage our issues or it's time to uh yeah, see this is the default one. It's time to fix the

**[50:39]** GitHub issue or it's time to validate the pull request.

**[50:45]** So, we can go to the GitHub repository here and actually check this out. So, if

**[50:50]** I refresh uh well, here I'll just go to an issue. And if I look at the labels for the issues, you can see that we have

**[50:57]** all these labels now. Factory accepted, approved, in progress, needs fixed, needs human. And if we look in the

**[51:03]** GitHub folder, we can see the pull request template. We want to make sure that as the dark factory is operating,

**[51:09]** it has a set standard for what goes into every single pull request description and every single issue description

**[51:16]** because being as consistent as possible is one of the best ways to actually make this reliable. So we have one template

**[51:22]** for when we're filing a bug, one for when we are uh you know requesting a feature. So, if I were to

**[51:28]** actually go and open an issue right now, uh it asks me is this a bug report, a feature request, or should I just create

**[51:36]** it from scratch? And we're only going to uh allow maintainers to to do this type. So, if I click on a bug report, then you

**[51:44]** can see that it automatically populates this form that's defined in the template

**[51:49]** that Claude Code just built for me. So, now we have some structure. we're enforcing certain things because we want

**[51:55]** to make sure like if I'm going to have this as a public experiment where anybody can open a GitHub issue, I I

**[52:01]** need some kind of expectation set for what information you're providing. So, we have these required fields. So, that

**[52:06]** way there is actually enough context for the dark factory to address the problem. And if a template's not used, then I'm

**[52:13]** just going to instruct the dark factory to automatically comment and close the issue. So, we're going to be pretty

**[52:18]** strict on that. All right,

**[52:24]** cool. So, uh, now we want to actually build our workflows here.

**[52:30]** The thing is I'm pretty low on context. So, I might start a new conversation to do this. So, I'm going to just say uh

**[52:36]** I'm going to build the archon workflows in a separate context window. So, just go ahead and update the plan with what we've just done here. And, uh, then I'll

**[52:44]** go into a new cloud code session to build the archon workflows. And while this runs, I can just open up

**[52:51]** a new Claude code and do that. So, let me close out of here. Open up a new Claude. And I'm going to copy the path

**[52:59]** to the full plan. I'll just put it at the start of the prompt here.

**[53:06]** And then the other thing is uh hold on, me close out of this. The other thing is

**[53:11]** I want it to load the archon skill because I want it to the archon skill

**[53:18]** that I have uh it gives a full reference to cloud code uh how to build archon

**[53:24]** workflows and best practices for doing so. And so I'm going to say uh read the

**[53:30]** entire dark factory plan that I gave you the path to. We are now going to work on

**[53:36]** building the archon workflows. And I want to start by building the triage, the dark factory triage workflow. So I

**[53:44]** also want you to load the archon skill. Um, so you understand all the best

**[53:50]** practices for building archon workflows. Then I want you to give me a summary of your plan for the triage workflow. all

**[53:57]** the nodes, what models we're going to use, what the prompts look like, and I want you to just like have a

**[54:03]** conversation here iterating on the ideas for the workflow before we actually build it.

**[54:08]** All right, so we're going to do a little bit of a piv loop. If you have uh gone through

**[54:15]** the agent coding course in Dynamus, you know what I'm talking about. We're going to do some exploration, some planning up front, and then we're going to create

**[54:22]** the workflow and test it. I don't even really know how we're going to test it exactly, but I'll I'll ask

**[54:28]** for its uh recommendations once we have it built because I might need to kind of like

**[54:34]** get the dark factory set up incrementally. Or maybe I need to like really run the

**[54:40]** triage workflow on the issues I already have in the repository here and just

**[54:45]** like see what kind of labels it adds and if everything's working. And then I'd probably have to ask it to also like

**[54:51]** undo all of its work so that we can still have like a blank slate of issues that aren't aren't muddled with yet. So,

**[54:57]** we'll see what we have to do once it once it builds it here. All right.

**[55:04]** Mini max is designed to mini max out those credits. I hope not. We'll see. I

**[55:10]** I'm down to switch something else like GLM if I need to. All right.

**[55:15]** Auto billing. It messed up last month. never doing it again. Okay, that's too bad. I will keep that in mind to

**[55:21]** probably not do that myself. Um, use the Miniax subscription gives

**[55:27]** good value for money. Okay, cool. Yeah, I don't know. I probably like if I really want to scale this experiment, I

**[55:33]** don't think I can use any kind of subscription because I'll hit rate limits, but that's good to know because I might.

**[55:41]** I use Miniax on Olama. Testing it now. Okay, that's very cool. Yeah, I mean I'm

**[55:46]** using a the biggest version of Miniax. I don't think that would really be realistically self-hosted. Like if I

**[55:53]** look up Miniax on Olama. Um yeah, they don't even offer you to

**[55:59]** install this yourself. It has to run through the cloud offering in Olama. But I I believe if you look up like um

**[56:07]** there are self-hosted options. You must be running something self-hosted, right?

**[56:13]** I just look up Miniax. Um,

**[56:19]** oh yeah. So, oh, maybe you are running the biggest thing cuz you I guess there's like local

**[56:25]** options. This has got to be huge though.

**[56:32]** Yeah, that's massive. 148 gigabytes for the main thing. And then if I if we were to look at a

**[56:39]** Q4 quantization Oh, wait. It's still 150 gigabytes. That doesn't seem right. But

**[56:44]** yeah, it's a 230 billion parameter model. I'm not running that on my computer. I'll tell you that.

**[56:51]** All right. Am I using local models for this? Nope. I'm using Miniax. Well, I mean, you can

**[56:57]** host Miniax yourself. So, it's an open source model, but I'm using it through the Miniax API.

**[57:04]** Uh, thank you very much for the donation, Jiren. Appreciate a lot. building a dark factory because even the

**[57:10]** machines refuse to work in light mode. Right. That's a good one. That's a very good and thank you for the donation. I

**[57:16]** appreciate it a lot. Uh when using Archon, is it needed to have bypass permissions for cloud code?

**[57:23]** Uh yeah, because you're running the Claude agent SDK under the hood. It's meant to be fire and forget, right? Like

**[57:30]** you're not supposed to babysit archon workflows. There's human in the loop built in, but that's a different thing.

**[57:36]** So I would use it like you can limit the permissions of claude when archon runs

**[57:42]** through hooks and if you really want to like create a settings.json JSON and manage permissions there. You can do

**[57:48]** that as well. But uh yeah, usually I just do like YOLO mode when I'm running Archon workflows

**[57:54]** and then I have like hooks that prevent reading from ENBs and removing directories and working outside of my uh

**[58:01]** designated codebase like the work tree that archon creates.

**[58:07]** All right. Uh we have eight H100s. Soon to get

**[58:13]** H200s. That is very, very cool. I'm jealous. [laughter] I do not have an H100. Uh, certainly not

**[58:19]** eight of them. That's awesome. Yeah, you're going to be able to run Miniax for sure. I think you could even run

**[58:24]** GLM. How big is GLM? I don't even know.

**[58:31]** Um, let's see. GLM is 744

**[58:40]** billion parameters. If you have eight H100s though, I you would I think you'd

**[58:45]** be able to run. Can you run GLM 5.1 on eight H100s? I

**[58:52]** think you can. Like it should be decent. Yeah, because each one is 80 gigabytes of VRAM. You're sitting pretty pretty

**[58:59]** there. Um I mean you might still need to quantize it potentially.

**[59:08]** 12.4 4 tokens per second on HH 8 H100s.

**[59:13]** So it's not like super super fast, but uh that's still very cool. I mean

**[59:19]** that's that's impressive. All right. I have not even a 100th of an H100.

**[59:26]** Same. Yep. [laughter] Those are expensive. Yeah. So yeah, 640

**[59:32]** gigabytes of VRAM. So yeah, you you I think you would definitely

**[59:38]** I mean you'd want to probably quantize to get good results, but still insane.

**[59:44]** All right, cool. So anyway, let's go back to our coding agent here because it came back

**[59:51]** with the summary. Okay, I've read the Dark Factory plan section 4.2 on triage

**[59:57]** specifically and the Archon workflow authoring guide. Here's my proposal designed for the dark factory triage

**[1:00:03]** before we build it. So our goal here, this is important for us to all understand, is to batch classify

**[1:00:11]** untriage GitHub issues against the mission and factory. So these core files that guide the scope of work and things

**[1:00:17]** we're going to actually care about and things we won't and then apply the labels and comments deterministically.

**[1:00:23]** So Claude makes the decision or I should say Miniax makes the decision, but then

**[1:00:28]** we're going to have a deterministic steps in the workflow to automatically label and comment just to make sure that everything works the same way every time

**[1:00:35]** we run the triage. So we're going to run the orchestrator or runs when the orchestrator detects

**[1:00:42]** open issues with no factory label. So the orchestrator is the cron job. It

**[1:00:47]** runs every so often and when it sees that we have things that don't have a factory label, that means it's a new

**[1:00:53]** issue that our triage workflow hasn't looked at yet. So, okay, we have five

**[1:00:59]** nodes. We're going to uh fetch the issues in parallel, fetch the rules. So,

**[1:01:05]** we're going to read in the mission and factory rules and then take a look at the pull request list because that'll

**[1:01:10]** also help us determine what is already in flight, which this doesn't really make sense

**[1:01:17]** because I think we should be able to rely on the GitHub issues alone to figure out what's already in flight. But

**[1:01:23]** maybe this is just like a bit of an extra safety check. So, I guess it doesn't really hurt to have it. But anyway, so layer one, we'll do our

**[1:01:31]** classification. So it says sonnet here but remember we have it configured to route to miniax when we specify opus

**[1:01:37]** sonnet or haiku in the archon workflows. So it's going to classify each one of the issues and then we're going to have

**[1:01:44]** a bash step. So a deterministic step that will take in the JSON array of

**[1:01:49]** decisions that we have from the structured output from cloud code and we're going to loop over the JSON and

**[1:01:55]** then use the GitHub CLI deterministically to apply the labels and then also the comments to the issues

**[1:02:00]** as well. Okay, so we we have uh bash steps. So

**[1:02:06]** we're not using AI for layer zero as well, right? Like we just run the GitHub CLI to search through all the issues. We

**[1:02:14]** fetch the rules, get the open pull requests. It says optional but useful.

**[1:02:23]** I mean, it's fine. I guess we can keep it. And then classify the plan explicitly

**[1:02:29]** calls out scope judgment against a written mission requires nuance. Haiku often fumbles or in our case the

**[1:02:35]** high-speed minia max would fumble. That makes sense. Cost is low since we run on less than 10 issues per batch in one

**[1:02:41]** call. Fair enough. Um okay. So

**[1:02:48]** you can see that one of the things we support in archon workflows is defining the exact output that we require from

**[1:02:55]** the model. So this is like structured output with more classic agents if you guys have dealt with that before. But

**[1:03:01]** the point of this here is that when our coding agent goes through the classification process, we need a

**[1:03:08]** standard. I'm going to keep saying this throughout our live stream here. Everything is all about standards for reliability. We need a standard for the

**[1:03:14]** coding agent. It needs to communicate in the same way every single time. Uh how

**[1:03:20]** we're going to label the issue. So it's going to output an issue number the verdict which is going to be either

**[1:03:26]** accept reject or needs human. It's right because need human that's our fail safe if it has failed to address the poll

**[1:03:33]** request multiple times. The priority and then the classification bug feature

**[1:03:38]** enhancement chore or docs that is good enough for me.

**[1:03:44]** And then we have the prompt skeleton as well. So just telling it like when it goes through the classification what

**[1:03:49]** it's actually doing. Um, and then what the script is, the bash script is going to look like to

**[1:03:55]** actually invoke the GitHub CLI to label and comment on things. And then it's got some open questions as well.

**[1:04:05]** Um, okay. So, let's go ahead and answer these questions. So, a batch size of 10

**[1:04:10]** or five. Let's do a batch of 10. And then help me understand like if we have actually opened up like 30 issues since

**[1:04:16]** last time the orchestrator ran is it going to loop in archon or what does that look like? And then should triage

**[1:04:24]** ever label without closing on reject plan says close rejected issues without

**[1:04:30]** with explanation. Um yes we should definitely close issues when we reject them. Yep. Priority

**[1:04:37]** labels on need human currently I applied them. useful so you can see at a glance which human review issues are urgent.

**[1:04:45]** Yeah, I think that they are definitely worth applying priority. Also help me

**[1:04:51]** understand how is this triage workflow going to know that we need a human,

**[1:04:58]** right? Because like we talked about in the plan how once the workflow or the pull request has failed twice on an

**[1:05:04]** issue, then we would say need human. So like what does that look like exactly?

**[1:05:09]** Okay, man. These are some tough questions. Should I include a type star label or just lean on the existing

**[1:05:15]** GitHub issue labels? The plan doesn't mention type labels explicitly. I'd add them. Sheep signal for later

**[1:05:21]** filtering. Sure. Yeah, we can add them. And make sure you update the dark factory plan with that decision as well.

**[1:05:27]** Duplicate detection scope. Right now, the classifier sees open PRs and current uh issue batch. Should it also see

**[1:05:33]** recently closed issues to catch repeat reports? costs more context but catches more duplicates.

**[1:05:41]** Um, I would say we don't really need this because if we rejected an issue before, we'll probably just reject it again. So, we don't have to spend the

**[1:05:47]** context to look through recently closed issues. Um, do mission.md and factory rules.md

**[1:05:53]** exist in the target repo yet? The answer is yes, I did actually create them. They are on the main branch. Uh, target repo

**[1:05:59]** path. Which repo are we building this workflow into? The dark factory app repo, right? Not Dynamus engine. That is

**[1:06:05]** correct. And actually, I will give you the full path to the codebase here at the start of the prompt.

**[1:06:13]** Okay. All right. Woo. That's a mouthful. It asks a lot of questions, but okay.

**[1:06:18]** This is good. This is good because this is this is going to be a lot of work. have our work cut out for us when we're

**[1:06:26]** building the system up front because every single assumption the coding agent makes is potentially going to be drastic

**[1:06:33]** when we're at this level of leverage creating our workflows and governance

**[1:06:38]** documents up front. Like we have to be very very intricate here. So, I know that can it can seem like I'm spending a

**[1:06:45]** lot of time on this, but man, this is important because if it doesn't understand how to label things, right,

**[1:06:51]** or it's not using GitHub issues in the way that I want it to, the whole system is going to fall apart. So, I got to

**[1:06:57]** take time. I'm really glad that it's asking me a lot of clarifying questions here.

**[1:07:04]** All right, cool. I'm still playing with Gemma 4 on my AMD

**[1:07:10]** 395 for local. Pretty cool. Yeah, Gemma 4 is good. Like it is legitimately an

**[1:07:16]** impressive model. Uh it is Yeah, one of the most popular ones right now. An old

**[1:07:21]** llama. Um I actually haven't heard of this one.

**[1:07:26]** Neatron Cascade 2. That's cool. Man, there's so many

**[1:07:32]** models, local models I want to try out right now. Um, whoa, the benchmarks actually look

**[1:07:39]** pretty good. Live Codebench Pro, it beats,

**[1:07:45]** wow, it beats Quen 3.5, 397 billion, and it's almost as good as communicate 2.5,

**[1:07:52]** a one trillion parameter model. Seriously, that's kind of nuts.

**[1:08:02]** Interesting. kind of want to try this one with the

**[1:08:07]** the dark factory. Okay. Well, anyway, I'm getting a little distracted here.

**[1:08:13]** All right. Yeah, that's exactly right. Quality work up front makes for some stellar loops, and that is what I'm

**[1:08:19]** going for. All right, let's go back to Claude here.

**[1:08:26]** Okay, so let me address your two help me understand questions. No looping in the archon workflow itself. The triage

**[1:08:32]** workflow is not a loop node. It's a oneshot DAG that processes a single batch and exit. Here's the actual flow.

**[1:08:38]** Okay. So, if if we do have 30 issues opened in between orchestrator runs,

**[1:08:43]** orchestrator cycle one is going to fire triage workflows, process 10, then exit. Orchestrator cycle two sees work in the

**[1:08:49]** high priority lanes first. Only when those are empty does it fall through to the untriage issues exist and run triage

**[1:08:55]** again. Okay. U so, okay, this makes sense. So the 30 issue spike does drain

**[1:09:01]** across three orchestrator cycles. So we do have to be careful

**[1:09:07]** because theoretically if there's like more than 10 issues in like created every single hour then it is going to

**[1:09:15]** just kind of pile up and pile up. But I think this is actually okay because I don't that would be unfortunate if

**[1:09:21]** there's more than 10 created every single hour. That's going to be so much work for it. Um right.

**[1:09:28]** Okay, so that makes sense. We can always change a limit if we want. How does

**[1:09:35]** triage know it to needs mark or it needs to mark needs human? You conflated two distinct escalations

**[1:09:42]** in the plan. I want to make sure we're on the same page because they're unrelated. Flow A is triage time needs

**[1:09:47]** human when this workflow handles the issue itself is problematic at intake. The classifier marks needs human when

**[1:09:53]** the issue is in scope but ambiguous, architecturally risky. a product

**[1:09:58]** judgment call. Clearly the classifier's decision.

**[1:10:04]** Okay. I actually don't like that.

**[1:10:10]** I don't if I really want this to be a dark factory, I want it to either close issues or handle them. I don't want it

**[1:10:18]** to create this graveyard of issues that need my review when I'm not planning on actually reviewing them. So, okay, I

**[1:10:25]** want to be clear here. I don't want to review issues unless there have been multiple failed attempts to address

**[1:10:31]** them. And so for flow A, we should just close these issues with a comment. Like

**[1:10:37]** if it's ambiguous or architecturally risky or whatever, let's just make a comment explaining that and then close

**[1:10:42]** the issue. Um, and then I want you to check the codebase itself to see if it has archon.

**[1:10:49]** I believe it does. And then okay, one design requirement I want your okay on for the bash apply

**[1:10:55]** decisions node. I'm going to have to classify I'm going to have classify write its JSON output to the artifacts

**[1:11:02]** directory. Makes sense as a part of the prompt instructions. Then have apply decisions read the file with jq instead

**[1:11:07]** of relying on classify output substitution. The reason being the reason string will contain quotes,

**[1:11:12]** apostrophes, new lines and emojis and archons auto shell quoting um into a bash script is a footgun waiting to

**[1:11:18]** happen. I mean, I guess I don't Is that really not a problem? I'll have to look into that separately cuz that it might

**[1:11:25]** have just identified like a something we might want to fix in Archon. But anyway, writing to a file bypasses a whole

**[1:11:30]** quoting problem. It's one extra line in the prompt and a jQ recursive and bash. Sound good? Uh, sure. That sounds good

**[1:11:37]** for me. Okay, man. It's getting specific, but that's good. Like, I appreciate how in the weeds it is right

**[1:11:43]** now. That's that's what we need. All right, cool. So, I think this is the

**[1:11:49]** last thing I need and then I can actually build the workflow. Cool.

**[1:11:58]** All right. What else we got in the chat?

**[1:12:04]** Thanks, man, for your shared work. You're very welcome. It is my pleasure. I love doing this stuff live with you

**[1:12:10]** guys. It's so fun just sharing everything. And, you know, I I was a little bit um I'm going to be honest. I

**[1:12:16]** was a little bit hesitant to do this live stream because it it's a bit slower than how I usually roll in my videos and

**[1:12:23]** live streams because I'm I'm building something live and definitely at the stage where I'm taking something pretty

**[1:12:29]** slow. Like we're not we're not going to have, you know, massive payoffs constantly here. Um it's a slow and

**[1:12:36]** steady, right? It's a marathon, not a race. That's what it is when we're building a system like this up front.

**[1:12:43]** Okay. Um what now?

**[1:12:50]** This is a lot of uh information. Okay. Confirm the execution plan.

**[1:12:58]** Okay, makes sense. Scaffold archon. Write the workflow. Validate the

**[1:13:03]** workflow. Fix any validation errors and revalidate. This is great. Uh well, actually, yeah,

**[1:13:11]** I'll just say this is good. Go ahead. The other thing I was maybe going to ask it is like what's its plan

**[1:13:17]** to actually invoke the workflow because when it does the archon validate that's just making sure the syntax is good. So

**[1:13:23]** it's sort of like linting of the workflow. It's not going to run it yet and triage issues. But once it does the

**[1:13:29]** build then I'll just have a conversation with it and ask it what its plan is to test it end to end.

**[1:13:37]** All right cool. I don't think we are too low on context.

**[1:13:42]** Yeah. We should be good for it to rip through this whole thing. I wish I didn't only have 200,000 tokens, but oh

**[1:13:48]** well. All right.

**[1:13:58]** Cool.

**[1:14:03]** Can't wait till the Chinese firms use mytho mythos outputs to train their models so open source local can really

**[1:14:09]** go stratospheric. Yeah. I mean, I'd be down for that. So,

**[1:14:15]** yeah, if they would use Mythos for um synthetic data generation, like they used Opus, that that would be powerful.

**[1:14:22]** They're probably going to screw the lawsuits. They're probably just going to do it. [laughter]

**[1:14:28]** Yep. All right. Can I do a session on Hermise? I assume

**[1:14:35]** you mean Hermes as a new like kind of like open claw alternative. Um, I would consider it. However, I'm

**[1:14:43]** more of a proponent of building your own second brain versus using something like Hermes or Open Claw.

**[1:14:50]** And you know what? While we're waiting for it to build the workflow here, I think this is a good time to chat about this quick. Let me actually um, hold on.

**[1:14:58]** Let me open up a page in my browser quick.

**[1:15:04]** I think this is the right link. Yeah, here we go. So, one of the really, really exciting

**[1:15:09]** things that I did quite recently in the Dynamis community is I did a 4hour boot

**[1:15:17]** camp teaching you how to build your own AI second brain from scratch. And one of

**[1:15:24]** the things that I cover there is how you can take inspiration from tools like OpenClaw Hermes without having to build

**[1:15:30]** run it yourself. There are a lot of risks involved in running your own or in

**[1:15:37]** running a second brain that's not your own application. There's a lot of security problems with open client

**[1:15:43]** Hermes, not just in like vulnerabilities in the codebase itself, but even just running something that you don't understand with permissions for your

**[1:15:49]** agent that you don't also don't truly understand. So, I'm a big proponent of

**[1:15:55]** building your own second brain from the ground up. And that's exactly what I cover in this course. And then I also

**[1:16:00]** edit it down into a more polished threehour version that still has like a lot of the good like Q&A in it. So

**[1:16:06]** that's in the community as well as the third course for Dynamist. So if you're

**[1:16:11]** interested, like my second brain literally saves me 20 hours a week. Like no exaggeration. It's crazy. Like I been

**[1:16:18]** running my business for about a year and a half now. Like I know how long it takes for me to do a lot of these things that are like partially or fully

**[1:16:25]** automated for me now. And so that's what I want for you as well. That's what I cover in the course. So if that's if that sounds interesting, let me actually

**[1:16:31]** put a link to this in the chat for for YouTube quick. We've had a lot of people

**[1:16:39]** joining the community recently. It's very exciting for the second brain stuff and also because of archon. Uh a lot of

**[1:16:45]** people are going through the course and they're sharing their second brain like their own architecture and how they're molding it for their use cases because

**[1:16:51]** one of the things I cover in the course is like here's how you build the foundation of the second brain but then I also talk about how you can you know

**[1:16:58]** guide it to help you build your own integrations and skills and other use cases that you have for it even getting

**[1:17:03]** into it being like very proactive for you anticipating your needs. So yeah people are sharing their own use cases

**[1:17:09]** and things. really cool to see like I'm learning a lot from you guys even in the community itself. So outside of just how

**[1:17:15]** I'm evolving it on my own. So very very cool. So yeah, I wanted to call it out really quick. Uh let's see where we are

**[1:17:22]** at with Claude now. Okay.

**[1:17:28]** Everyone wants to sell a course. Well, I mean I provide a lot of value. I stand

**[1:17:34]** by what I what I provide there. So yeah, I don't I don't really appreciate that

**[1:17:40]** the the cursing in the message there. Um but yeah, I mean like I it's seriously

**[1:17:46]** there's a lot of value that I have and a lot of work I put into creating that boot camp.

**[1:17:52]** All right, cool. So anyway, here is what we've got for the workflow. It already built the whole thing. That's actually

**[1:17:58]** faster than I thought, honestly. But I guess we haven't really done any validation yet. Um let's see. So, we

**[1:18:04]** have our plan updated with the little bit of changes we made to the labeling system and the changes we made to our

**[1:18:11]** plan for the workflow. Um, and then

**[1:18:17]** okay, so we created the workflow itself. [sighs] A few implementation notes worth flagging. I don't want to spend like too

**[1:18:24]** much time reading through this right now.

**[1:18:31]** Okay, I think that's fine. What's not done yet? Orchestrator agent fix GitHub

**[1:18:37]** issue adaptation. Okay, so suggestion

**[1:18:42]** for next step before building the next workflow. Smoke test this one end to end. Create the labels in the repo. File

**[1:18:49]** one or two test issues. And um okay,

**[1:18:55]** that actually makes sense. But here here's the thing. Um, I would love to smoke test, but I

**[1:19:01]** already have some issues that I have in the repository. So, maybe what we could do is we could run the workflow to

**[1:19:08]** triage those issues, but then just delete the labels after, so we can bring us ourselves back to a blank slate. So,

**[1:19:14]** I want to do the full test, but I I want to like get it back to the original state before I did my testing, if that

**[1:19:21]** makes sense. Uh, but you can feel free to like iterate on the workflow and everything before you go back to the blank slate.

**[1:19:28]** Okay. So, yeah, I wanted to like actually run it but not like leave a mess of of

**[1:19:34]** triaging and stuff because this repo that I have right here, like I want to keep it pure, right, for like when I

**[1:19:40]** actually kick off the dark factory and like have all the workflows built.

**[1:19:45]** Okay. And then someone asked for me to share the link for what I had open up in Chrome. This is the link right here.

**[1:19:51]** Um, cool. All right. Thanks, Cole. This is awesome. I appreciate it a lot. Thank you very much. Thanks, Cole. will join

**[1:19:58]** Dynamus. Thank you. I appreciate a lot. Yeah, I'll be happy to have you in the community watching at 5:20 a.m. from New

**[1:20:05]** Zealand. Well, thank you for tuning in so early. I appreciate that a lot. Cool.

**[1:20:12]** All right, let's see.

**[1:20:19]** I I know it's a reference to shooting yourself in the foot, but I've never heard the term footgun. Am I alone?

**[1:20:25]** Actually, honestly, Chris, that's a good point. So that's in reference to what Claude mentioned earlier. Uh I guess I

**[1:20:32]** haven't heard foot gum either. I don't know. Yeah, I've heard I've heard shooting yourself in the foot a million

**[1:20:37]** times. I use that expression myself a lot. But yeah, I guess that's just a shorter way to put it.

**[1:20:45]** Cool. All right.

**[1:20:51]** I definitely want to join Dynamus, but just bought a house. Fair enough. Well, congratulations, Stuart, on your new

**[1:20:57]** home. Why I'm trying to get everything operating free and local for a first run. Then once I have output, I can pay

**[1:21:03]** for upgrades. Sounds good. Yeah, fair enough. Yeah, congrats on the house. That's exciting. You're joining as well.

**[1:21:10]** Very cool. I appreciate it. Welcome to the Dynamis community. Thanks, Cole. This is super cool. I

**[1:21:16]** appreciate it a lot. Yeah, I I appreciate you guys uh finding interest in something where it's like a little

**[1:21:21]** bit slower pace as I have to like really spend my time. ideating and and building the system up front. So, yeah, happy to

**[1:21:28]** to build this in in public, so to speak. All right, cool. So,

**[1:21:35]** let's see. The workflow is currently in progress.

**[1:21:41]** Looks good. Um, you know what I I kind of want to do because I'm running this workflow for the first time is I would

**[1:21:47]** love to uh view the logs in the Archon UI.

**[1:21:53]** So, let me actually ask it. I I don't have it started. I restarted my computer recently, so I don't have it up and running. Start the back end and front

**[1:21:59]** end of Archon. This is how easy it is, by the way. You know, you don't even have to run the commands in the terminal

**[1:22:04]** or run the containers or anything yourself. You just let it go. So, we'll take a look.

**[1:22:13]** Okay. I mean, bun rundev's not hard to remember, but I just like doing that.

**[1:22:18]** [laughter] All right. So, let's head on over to Archon.

**[1:22:25]** Go to the dashboard. Um, it looks like the backend is still

**[1:22:32]** starting. Can you monitor the back end and let me know if it's failing to start? Not sure.

**[1:22:39]** I might be on a wrong branch or something. Oh, no. Okay. I think Wait, hold on.

**[1:22:48]** Um, why is my workflow not showing? I have these these workflows from way back in

**[1:22:54]** the Saturday live stream that I forgot to continue are still running. That's funny. So, they're still paused, but it's not showing up. Where did it is it

**[1:23:03]** done running already? Oh, okay. It did actually finish.

**[1:23:10]** Huge win and a Windows bug. Let me break down what happened. All three parallel fetch nodes finished. classifier ran in

**[1:23:16]** 30 seconds. Decision.json was written successfully. The fetch open PR's node paid for itself

**[1:23:22]** immediately. Without the classifiers would have accepted seven issues that are already being worked. What broke is

**[1:23:27]** that jq uh failed on get bash for Windows. Oh, that makes sense. Yeah.

**[1:23:33]** Okay. So, let's see. Okay. So, it's figuring out a fix here. Caught another bug.

**[1:23:39]** Okay. Now, it's running the workflow again. It's cool that it's iterating like

**[1:23:46]** little little blips that it's finding, but like I mean, as long as it's able to iterate, I'm happy with it. U yeah.

**[1:23:51]** Okay, there we go. So, now we can see the workflow. It's not running, but the one that just failed, it uh shows up

**[1:23:57]** here. So, we can take a look at the logs of for the failure.

**[1:24:02]** So, yeah, everything is working as intended in the Archon web UI. We just need to fix the syntax for the the

**[1:24:09]** underlying workflow itself. Cool. So, all right. Oh, now it's

**[1:24:14]** running again. Okay. Very good. View the logs. Very cool. Looking good. All right. We'll see if it works this time.

**[1:24:26]** All right. Tail foot gun means that. Yep. Today I

**[1:24:31]** learned as well. Eric said the course in Dynamis are

**[1:24:36]** outstanding. I'm a career dev and seen a lot of courses. Dynamus courses are exceptional. Yeah, I appreciate it very

**[1:24:41]** much. I I appreciate you guys like sharing that especially after someone comes in and just like has to say

**[1:24:47]** something mean for no reason which I mean I got thick skin like it's fine. I I understand and and by the way like to

**[1:24:53]** to that person who who um was a little mean like I do get it like I understand

**[1:24:59]** that like everyone is just trying to sell a course. Uh and and I can see how it just feels like I'm just fitting in

**[1:25:05]** with that crowd. Like I I get it. It's okay. I'm not just like living in a bubble where I I think that you're saying it totally out of pocket. Like I

**[1:25:11]** understand, but like at the same time, like I really do believe that and I'm not saying I'm expecting you to do this,

**[1:25:17]** but like if you were to actually go through the second brain course, I I feel like you would take back what you said. Like honestly, I'm just going to

**[1:25:23]** say that. Um but yeah, not not like I'm thinking I'm going to change your mind or anything.

**[1:25:29]** Yeah. All right. Having never built anything

**[1:25:35]** before, but amazed how easy this is to learn if you think logically. That's right. Yeah. And even just like

**[1:25:41]** slowing down and using claude code to help you think logically like break it

**[1:25:46]** down for me step by step or like help me plan this and ask me questions like

**[1:25:51]** those kinds of things are are uh how you get the most out of claw code because it

**[1:25:57]** it can I mean like large language models make mistakes. They're never going to be perfect and that's why you need to align

**[1:26:03]** with them. But you can have them walk you through the alignment process because they do a really good job at

**[1:26:09]** that. Okay. Uh, cool. So, it looks like it ran

**[1:26:15]** end to end and it actually closed a lot of issues here. So, three were accepted and then seven were rejected. Okay.

**[1:26:21]** Interesting. Uh, well, I'm curious to dive into that now. It says that it's still waiting here.

**[1:26:30]** Cool. SmokeD Dev said as a part as part of as a student of the course I agree Dynamus absolute game changer for me

**[1:26:37]** lots of value I appreciate a lot thank you very much uh all right cool so uh looks like it is

**[1:26:47]** done cool and that was fast by the way it

**[1:26:53]** didn't take that long now we didn't run this workflow with Miniax let me be clear because we didn't run this on the

**[1:26:59]** VPS yet, but we will get there. We're just testing it right now locally. In fact, I should probably test my or check

**[1:27:05]** my enthropic rate limit. Uh oh, it's not even that bad. Okay, we're good here.

**[1:27:12]** I'll even share that on my screen here. Let me duplicate

**[1:27:18]** and bring it over. So, this is my limits right now. Uh, look at that. We've only

**[1:27:24]** we've literally only used 10% so far. So, not bad, especially with how bad the rate limits are. Um,

**[1:27:31]** wait. What is this? Daily included routine runs. This is new. Like as of

**[1:27:37]** just today. Included routine runs per rolling 24 hours. I actually This is

**[1:27:43]** weird. I've never seen this in the usage page before from the Cloud app. And

**[1:27:48]** yeah, my weekly limit I'm at already at 50% and it resets on Friday. And over

**[1:27:53]** the past couple days, I've been doing so much testing with Miniax that I haven't even been using my Enthropic that much. Like it's crazy. I got to like 40% over

**[1:28:00]** the weekend. Yeah. Okay. So, anyway, I was going to look at

**[1:28:06]** the classifications that it did here. Oh, it already undid everything. Shoot.

**[1:28:13]** So, I can't actually see because it deleted the comments.

**[1:28:21]** Okay. So, this is one of them that was accepted. So we can see that the labels are removed cuz I asked it to undo

**[1:28:27]** things after its testing. But we can see from the history here that like this one it added the factory accepted with a

**[1:28:34]** priority low. If we look at um I don't know one that it rejected here.

**[1:28:41]** Where is this one? This one it added factory rejected closes not planned. It

**[1:28:47]** had an issue comment here at one point but that's another thing that it cleaned up. So, I honestly kind of wish that it

**[1:28:52]** did the cleanup after I told it to, but that's my fault because I told it to do the cleanup immediately after.

**[1:28:59]** We can see here that um it has taken care of all the cleanup. All 11 issues

**[1:29:04]** are back open with zero labels. But anyway, the workflow actually worked extremely well.

**[1:29:10]** Um okay, what I did not touch. Yeah, that makes sense. Ready for the next

**[1:29:16]** step? The triage workflow is committable. Next logical builds per the plan. Uh GitHub label onetime setup for

**[1:29:22]** the real run already done implicitly dark factory validate PR.

**[1:29:29]** Well, shouldn't the next step be to create an adaptation of the archon GitHub issue fix workflow for the dark

**[1:29:35]** factory? Because I I think like I don't know why the plan wasn't really clear on

**[1:29:41]** like we got to actually build something for implementing the pull requests, not just validating and fixing the issues that come up. So I'm going to try to

**[1:29:47]** point it in the right direction here. Um because I I think that'd be the next workflow to work on. So we have the

**[1:29:53]** triage which is going to figure out what issues do we actually want to address and then in parallel we'll invoke the archon workflows to you know take it

**[1:30:01]** from issue to pull request. Okay you're right and I missed that. Of

**[1:30:08]** course Claude has to be sickopantic and tell me that I'm right. U but I am. The

**[1:30:14]** triage workflow produces labels, but those labels are inert until there's a working fix workflow. It knows how to

**[1:30:20]** validate. Uh the plan calls this out explicitly as a hard blocker. The moment a bug fix or feature lands, the default

**[1:30:26]** bun run validate will still blow up on Python syntax. Right? So this this is a little bit behind the scenes planning I

**[1:30:33]** was doing. Basically, the fix GitHub issue work get fix GitHub issue workflow

**[1:30:38]** built into Archon isn't quite specific enough for my codebase. So, I just need to take this as an example. This is one

**[1:30:45]** of the workflows that ships by default with archon. And I just need to tweak it to work a little bit better with my dark

**[1:30:51]** factory specifically. So, it's going to do some research for me. So, understand the structure of the

**[1:30:57]** repo. Um, understand the command or the workflow we're going to adapt and then see what we have for our global rules

**[1:31:04]** already. All right.

**[1:31:10]** Let's see. All right. Yeah, I appreciate it. Don't

**[1:31:17]** care for such comments. You're really delivering a lot of value for free as well. I think we all value that a lot.

**[1:31:22]** Yeah, I appreciate that. And um even when I do have the community as a, you know, paid thing, I I do try to give an

**[1:31:28]** insane amount for free like what I'm doing right now. So, I appreciate recognizing that. And that really is

**[1:31:34]** important to me. Like no matter what I always want to just be constantly giving. That's also why Archon is fully

**[1:31:40]** open source. This repository has nothing hidden. I mean the Dynamus community had

**[1:31:45]** early access to it and got to even help shape some of the direction for it. And that's one of the cool parts of having a

**[1:31:51]** community. Uh but it's it's for everyone. That's that's always been the goal.

**[1:31:58]** All right. Is there a link for the community? Uh yeah. Yeah. Sorry. I I'll send this

**[1:32:03]** again here in the chat. Um, so this this is a link to kind of like the page like

**[1:32:10]** showcasing the AI second brain, but you just scroll down and there's a lot of buttons here to join. So yeah, I

**[1:32:16]** appreciate that. All right, let's go. I'll watch the logs here. All

**[1:32:22]** right. See, a strong DM depends on a digital

**[1:32:28]** twin universe which creates behavioral clones of ex external services like oka,

**[1:32:34]** jira, slack to allow agents to run thousands of realistic tests. Yeah. Okay. If you really get into strong DM

**[1:32:41]** setup, it is quite impressive. So certainly won't be uh building everything strong has at least for now,

**[1:32:49]** but also my application is luckily a lot simpler. I won't necessarily need to to

**[1:32:54]** have the same level of depth, right? Like simpler application means I don't have to go as deep, but I still get like

**[1:33:00]** the same reliability like they've built. Uh but yeah, if you want to like really read into what Strongd DM has built,

**[1:33:05]** again, they haven't open sourced their Dark Factory, but they've, you know, open source the PRD like I showed at the

**[1:33:12]** start of the stream. And then I think they have like some blog posts as well where they break down a lot of what

**[1:33:17]** their architecture looks like. It's pretty cool. It's It's really inspirational.

**[1:33:25]** All right. Cool.

**[1:33:30]** Um, routine runs. Is that analogous to open claw crons? I mean, probably

**[1:33:36]** analogous to some kind of cron job. I don't know exactly. Like this. I've

**[1:33:41]** checked my anthropic usage every single day because I want to be on top of especially the 5 hour rate limit. This

**[1:33:47]** this I literally like wasn't this wasn't there this morning. Um so yeah, I don't

**[1:33:52]** I don't know what it is exactly. Maybe maybe they have something if I just like search cloud code routine runs.

**[1:34:00]** Okay. Um Oh yeah, there we go. 47 minutes ago. We have a post on the cloud code

**[1:34:07]** subreddit. New now in research preview. Routines and cloud. Configure a routine

**[1:34:13]** once, a prompt, a repo, your connectors, and it can run on a schedule. Schedule routines let you give Claude a

**[1:34:19]** cadence and walk away. Um, okay. I was just about to say they

**[1:34:25]** already have the slash schedule the CLI. If you've been using slash schedule in the CLI, those are routines now. There's

**[1:34:30]** nothing to migrate. Okay, that makes sense. So, they're they're taking something that was has already been there, but now they're just building it

**[1:34:37]** into other platforms. Like I I assume that like slash schedule used to be an only CLI thing and now it's like within

**[1:34:43]** claw desktop and co-work and the claw app. I guess that's what it is. I mean it's pretty cool. So yeah, literally it

**[1:34:49]** is cron jobs just being able to run something that runs every hour or day or whatever.

**[1:34:55]** That's pretty cool. All right, they are always shipping. It

**[1:35:01]** is crazy, but good for them. Okay, very cool. So now, uh, okay, how

**[1:35:09]** long have we been streaming for? Um, we've been streaming for a little over an hour and a half. Okay, so I am able

**[1:35:15]** to stream for Wait, I got to check my calendar. I'm able to stream for two and a half hours. And I'm I'm loving what

**[1:35:22]** we're building right now. So I'm think I'm going to go till Yeah, I'm planning on streaming till 1:30 Central time. So

**[1:35:29]** like another hour here. We'll see how far I get with all of our workflows.

**[1:35:35]** Okay. What are we doing here? Okay. Wow.

**[1:35:41]** There's so much output. I'm getting a little like uh burnt on all the like

**[1:35:46]** burnt out from all of Claude's output here. It's a lot to parse through because it's kind of it's fairly complex

**[1:35:52]** what we're working on right now, I will say. Okay. Rag YouTube chats validation story

**[1:35:59]** is prescribed but not wired. Okay. Uh, global rules prescribe the exact

**[1:36:05]** commands, but none of those dev steps are actually installed yet. No tests, no make file, no CI, right? Yeah, I haven't

**[1:36:12]** built that yet. The factory should add these when the first PR touches them. I don't actually

**[1:36:18]** agree with that. I want to build that ahead of time. [laughter] I love this. It's cute, but

**[1:36:23]** it creates a chicken and egg problem. Oh, that's funny. I Wow, Claude Claude has some personality now. I will say

**[1:36:32]** and yeah I agree with Claude here that that is a bad decision to put in the global rules. Um okay

**[1:36:39]** the bundled archon fix GitHub issue workflow is mostly language agnostic. That makes sense. So my surgical fix is

**[1:36:45]** just one file. My recommendation is option B custom command override.

**[1:36:53]** Um here's my Okay. All right. Yeah. Sure. full workflow fork.

**[1:37:02]** All right.

**[1:37:07]** You know, so it's saying I don't need to create a workflow from scratch and I can just use what I have as the bundled

**[1:37:14]** workflow. Um, yeah. Okay. Yes, you're right. We

**[1:37:20]** definitely want to bootstrap the development dependencies manually. And then I actually do want to create a

**[1:37:27]** custom workflow entirely. So yes, I know that there's not much we have to change from the GitHub issue fix workflow, but

**[1:37:34]** I want to be able to evolve it separately from the default Archon workflow anyway. So we can mostly copy it and then obviously just changing the

**[1:37:40]** validate command. But yeah, let's go ahead and do it that way. Um,

**[1:37:47]** yeah. And then sure, we can we can smoke test

**[1:37:53]** issue number 26 after. Okay, there we go. Um, oh crap, we have to run the

**[1:37:59]** compaction now. Oh, I forgot about that. I probably should have just worked on the workflow in a separate conversation.

**[1:38:05]** Uh, because now that it does a memory compaction, it has to reload its skills and stuff. So, all right. Now that you

**[1:38:11]** just did a memory compaction, I need you to uh read the dark factory plan again and then load the archon skill just to

**[1:38:18]** make sure you have full context before you go into building the second workflow and um doing the smoke test on issue

**[1:38:24]** number 26. Make sure you build this workflow from scratch. And then uh also I want to use

**[1:38:31]** the commands folder for all archon dark factory workflows. So make sure we don't have inline prompts for the other the

**[1:38:38]** triage workflow we just built as well. Um, so that's a little specific, but I just realized that um I wanted to

**[1:38:45]** organize my workflows a bit better than I did up front. If I go do the codebase now, we have the dark factory triage.

**[1:38:52]** Um, this prompt is in line and it's massive. So I would rather extract this to a

**[1:38:59]** command, right? We don't have any commands right now, but in Archon your workflows can reference a command, which

**[1:39:06]** is just like a separate markdown document just to have a better way to organize things. So we don't have these massive ugly prompts in line in the

**[1:39:12]** workflow itself. I might even want to do the same for this this uh apply decisions bash is

**[1:39:19]** like really long. Yeah. Uh there's there's a lot of

**[1:39:24]** optimizations that I can make just for the sake of the live stream. I am moving decently quickly. So certainly we'll be

**[1:39:32]** iterating on things off camera uh like before I make the YouTube video tomorrow. That kind of like, you know,

**[1:39:37]** sums everything up for the Dark Factory that I'm working on.

**[1:39:44]** All right, cool.

**[1:39:51]** I appreciate it. Haters going to hate Dynamus rocks and the value of your contributions, Cole, are frankly incalculable. I I appreciate it a lot.

**[1:39:58]** That means a lot. Price of Dynamus is a lot more reasonable than most of the courses community subscriptions being

**[1:40:04]** offered. A lot of them sound like snake oil. Get rich quick for thousands of dollars. Yeah, there there unfortunately

**[1:40:10]** is a lot of that out there. Uh there there's one sort of YouTuber in

**[1:40:16]** particular that I don't want to call out exactly uh or like namerop, but uh he he's a

**[1:40:23]** respectable guy. He does a lot around second brains specifically, like even before generative AI. A lot of you might

**[1:40:30]** know who I'm talking about. So, I'm not saying the course is going to be bad, but he like he's like running these

**[1:40:36]** cohorts for building your own second brain, and he's charging $2,000 for it.

**[1:40:42]** It's like crazy. Like, what? Like, $2,000 just to like learn how to build a second brain. Like, I taught that for in

**[1:40:49]** a 4-hour workshop and you can just join the community for it. Like, it's not

**[1:40:54]** $2,000. [laughter] Yeah. Anyway, there are some pretty

**[1:41:00]** expensive things out there for sure. All right. Um, will the Dark Factory

**[1:41:06]** repo be open source after the live? So, not fully, but uh it'll be within like

**[1:41:12]** the next couple of weeks I will open source it. So, I need some more time to validate and really polish things, but

**[1:41:17]** the the plan is to make it public by the end of the month, like everything public where you can even open an issue and have it work on it for you. So,

**[1:41:27]** Who could I be talking about? Yeah. Yeah. You guys, some of you guys know. Some of you guys know. And And

**[1:41:33]** again, I respect him. Well, I guess I would say I have more of a neutral opinion. I haven't gotten like too deep into his stuff. So, I'm not like trying

**[1:41:39]** to dunk on him or anything. I'm just saying that like to me, like $2,000 to join a cohort is a little ridiculous,

**[1:41:44]** but to each their own. I mean, some some people um definitely

**[1:41:50]** value having that kind of like cohort style. It's Yeah. Teach your own.

**[1:41:57]** All right. Okay. Let's see here. What else we got?

**[1:42:04]** The old You're absolutely correct. Yeah, that's right. All right. Um, a bit out of context, but

**[1:42:13]** uh, could we build a skill to make Claude code and and anti-gravity interoperable?

**[1:42:20]** Uh, you definitely could. Like if you wanted anti-gravity to invoke Claude like in headless mode, you could if you

**[1:42:26]** wanted to. Um I think I don't [snorts] know if anti-gravity has like a CLI, but

**[1:42:31]** Gemini has a CLI obviously. So you could have them invoke each other.

**[1:42:38]** So you could like have a workflow where it's like Claude implements the code and then it calls the Gemini CLI to do the

**[1:42:45]** validation. Like you could do that kind of thing 100%. Like that's something that I actually want to build like directly in the into Archon workflows

**[1:42:51]** like being able to have different providers at different nodes for planning and implementation and reviewing.

**[1:42:59]** All right. Uh okay. This is really interesting. Uh Miniax with open code performs much

**[1:43:06]** faster and better than in cloud code. Probably the context bloat of all the prompting that goes under the hood in

**[1:43:11]** cloud code. Um, so that okay, that's good to know because yeah, maybe I would want to change this harness to use like

**[1:43:18]** PI or open code instead. Uh, okay. I I will have to look into

**[1:43:23]** that. Like I said, there's so many ways that I can probably improve this harness with the prompting and how I organize

**[1:43:29]** the workflows and my mission document and my factory rules and even just the

**[1:43:34]** tool that I'm using under the hood. Like maybe I do want to use Pi or Open Code instead.

**[1:43:41]** All right, let's see. Uh, one way to find out if

**[1:43:48]** the course or subscription you paid for justify the cost is if you ship a product that others paid for to recoup

**[1:43:54]** that cost. I mean, yeah, exactly. Um, that right because then then it's like

**[1:44:00]** there's no argument there. Like if you made more money thanks to what you learned there and you built something from it, then yeah, it pays dividends.

**[1:44:07]** Exactly. Right.

**[1:44:12]** All right.

**[1:44:18]** Why does it feel like we've been here for one plus hours and not achieved much? I mean, that's something that I've

**[1:44:23]** been trying to be very transparent about here is that like we're spending a lot of time planning and defining the

**[1:44:28]** architecture and the system for the dark factory up front. And it it has to take time. It it it has to I can't rush it.

**[1:44:36]** And and to be honest, like I would probably be going even slower if I wasn't in a live stream here because in

**[1:44:42]** the end, like if I want this thing to rip through issues really quickly, if I want the Dark Factory to be self- sustaining and really efficient and

**[1:44:50]** reliable, I have to be slow up front. That's what I'm and that's kind of the the teaching lesson here, honestly, as

**[1:44:55]** well. So, yep,

**[1:45:01]** even miracles need time. That's a good way to put it. I wouldn't I feel like that'd be very egotistical to call this

**[1:45:08]** a miracle. It's certainly not. It's just an experiment that we'll see what happens. But uh yeah, it's a good way to

**[1:45:13]** put it. All right.

**[1:45:20]** That's very cool. John, I joined China two months ago today. Never wrote a single line of code. Have a functioning

**[1:45:25]** second brain. And yeah, that's that's awesome, John. I appreciate it. Once you get to that point where your second

**[1:45:30]** brain is up and running and saving you hours and hours every week, there is no better feeling. So good.

**[1:45:37]** All right. All right.

**[1:45:43]** One of the basic rules of marketing is people are willing to pay for high ticket. I mean that that's fair. Yeah.

**[1:45:48]** Like this uh individual that I mentioned. I mean maybe I could just say his name because I'm really not like

**[1:45:53]** hating on him or anything, but just for the sake of being careful. Um, I'm sure there are people that get a

**[1:45:59]** lot of value out of it and and yeah, he he like kind of is known as like the premium person. He's like he's been

**[1:46:06]** building second brains for a decade. I mean, I would like to think that like he's struggling to catch up with all the

**[1:46:12]** AI stuff because he he's more traditional his approach. He's probably doing fine. But anyway, like yeah, I'm sure there's when you when you have

**[1:46:18]** something high ticket, it signals value. And so you do attract that uh kind of person that is willing to shell out and

**[1:46:26]** they just want to make sure like I mean I don't always agree with this, but like sometimes people just think like, hey,

**[1:46:32]** most money means it's the best value, which definitely isn't always true, but uh it does kind of scream like this is

**[1:46:38]** going to be the safest bet if you have the money for it. I don't know. I don't know. I'm kind of rambling on that.

**[1:46:43]** Yeah. Uh, Dynamus is awesome. A part of the

**[1:46:48]** community since it came live. That's so cool. I appreciate you being a part of the community for so long. Uh, and by

**[1:46:54]** the way, the oneyear anniversary of Dynamus is uh this month, April 26th.

**[1:47:01]** So, there going to be some some exciting things that I've got going on for that. Some live streams I'll be doing on YouTube around the time. Um, and also

**[1:47:08]** some exciting events in Dynamis and some things that I am releasing as a part of the anniversary celebration. Also, just

**[1:47:15]** speaking of things that are going on around that time, uh, I want to call this out really quick as well. I'm doing a, this is kind of like unrelated, but

**[1:47:22]** around the same time, I'm doing an AI transformation workshop with a gentleman

**[1:47:28]** named Leor Weinstein on April 28th. So, that I believe that's a Tuesday at 9:00

**[1:47:34]** am [snorts] Central time. So this is going to be really cool because uh Leor he's like an expert at coming into a

**[1:47:41]** company and helping it become AI native and so like designing like a AI native

**[1:47:47]** org chart and like how to enable each team and team member with AI technologies for coding and other things

**[1:47:54]** like even just like you know the sales and marketing and finance team and all of that. So he's going to like talk

**[1:47:59]** about that for an hour and then for an hour I'm going to talk about how to transform your organization with agentic

**[1:48:06]** coding and like how to transform developer teams. So we're like kind of tag teaming it together to give you like this full view of like how do you

**[1:48:13]** transform companies and even yourself as an individual. Uh so that's going to be really cool. So that's happening at the end of this month here.

**[1:48:20]** And yeah like you can see I'm on my you know scheduled live stream page on my channel. This is just going to be a free

**[1:48:26]** workshop just [clears throat] happening on live stream on my channel.

**[1:48:32]** All right, cool. Yeah, big shout out to Cole. Even the content you are delivering for free

**[1:48:38]** every week is insane. Thanks a lot. You're very welcome. Always my pleasure, man. Like I've been doing YouTube for uh

**[1:48:45]** it's almost two years now. I started like very beginning of July 2024

**[1:48:51]** and it's just a blast. every single video. It's just so fun to make and uh keeps me ahead of the curve on

**[1:48:57]** everything, too. Just being a constantly in the trenches building and researching and doing what it takes to make the

**[1:49:02]** content for you guys. All right.

**[1:49:09]** What is going on now? [laughter] Uh sometimes it's stressful to come back

**[1:49:14]** and just see like it's in the middle of writing the package.json. You don't even know why. Oh, I guess it Oh, yeah.

**[1:49:20]** setting up the developer dependencies that we talked about. Okay, we're good. We're good. So, okay, what has it done

**[1:49:26]** now? I think it made the full workflow. Yeah. Okay. Dark Factory fix GitHub

**[1:49:32]** issue. Okay, good. So, we got our second workflow now. All right,

**[1:49:38]** dynamis. Uh, no, not that one. I need to go to the rag YouTube chat. I want to open up the second workflow. Okay, take

**[1:49:46]** this is good. So, now we have all of our different commands. So instead of the workflow just being like

**[1:49:52]** a bunch of massive inline prompts, we got it organized a lot better.

**[1:49:57]** Okay, so this is our fix GitHub issue. By the way, I'm thinking about renaming the whole uh rag YouTube chat repo to

**[1:50:04]** Dina Chat. That's why it references this name a couple times. Uh but anyway, so this workflow here,

**[1:50:12]** we're going to start by extracting the issue number. So this is very much based based on the default fix GitHub issue

**[1:50:18]** workflow archon. Then we classify the issue bug feature enhancement refactor

**[1:50:23]** chore or documentation just like we planned in the in the dark factory plan. Then we research the issue uh and then

**[1:50:31]** we either do a plan we create a plan if it is a feature to build or we

**[1:50:36]** investigate the problem if it is a bug to fix. Right? Because issues are going to be one of the two. Right? So like

**[1:50:43]** when we classify it's either going to be a bug and then I know we have all these different labels but basically all these are just feature additions right like if

**[1:50:50]** it's a chore or a refactor or an enhancement like all those are just like more specific versions of a feature. So

**[1:50:56]** may maybe the whole like issue labeling isn't optimized here but I think it's fine. It's actually pretty standard to

**[1:51:03]** have those kinds of labels. And then we go into implementation then

**[1:51:08]** validation create the poll request and we review. And so I am going to have a

**[1:51:13]** separate workflow to do complete pull request validation, but I still want to have the workflow it like when the PR is

**[1:51:20]** created at least have it do a little bit of review, right? So like initial round of review here and then I'll have a more

**[1:51:26]** comprehensive validate PR workflow that I'll create next. That's the plan just

**[1:51:31]** to give it a chance to do a little bit of self-fixing before we say like all right here's our poll request for for

**[1:51:36]** you uh you know next stage of Dark Factory to review.

**[1:51:45]** All right. So let's go back to our coding agent

**[1:51:51]** here. Where am I going? Okay. There we go.

**[1:51:57]** Okay. Status so far. So, we refactored, built the new workflow, seven new

**[1:52:02]** commands. Looking good. Got our dependencies set up. Uh, okay. Before I

**[1:52:08]** kick off the smoke test, two things to confirm. Dev dependencies are not installed locally.

**[1:52:15]** Um, okay, that's fine. Yes, I want you to install the dev

**[1:52:21]** dependencies. And actually, I would much prefer to use UV for the Python package management. So go ahead and change that

**[1:52:27]** in the repository. Get everything installed, test everything and um and then yes, go ahead and invoke

**[1:52:35]** after that invoke the archon workflow to run the dark factory fix GitHub issue on

**[1:52:40]** pull request or no on issue number 26.

**[1:52:47]** Okay. Yep, that's good. All right, cool. And then we're not going to have time

**[1:52:53]** for it in the live stream here, but um you know what? I I'm almost tempted to

**[1:52:58]** do another live stream tomorrow instead of a YouTube video. Maybe I probably should make a YouTube video because it

**[1:53:04]** it'll be a week. Uh but it'd be cool to like just keep building this live more. I know that it's a lot of time, but it

**[1:53:10]** it's it's fun to do this. And we're getting kind of close, right? Like we have a lot of it built. We just need to

**[1:53:16]** finish the last couple of workflows and then we need to bring everything onto the VPS so that we have the whole dark

**[1:53:22]** factory running autonomously and it's not relying on my computer being on. So, we're we're getting there. We're getting

**[1:53:29]** there. We we won't really be unfortunately be able to see everything running on our VPS today, but um

**[1:53:38]** it won't take long once we have the workflows built and validated to copy everything over because we already have

**[1:53:45]** the I think this is my directory dark factory. Yeah. Yeah. So, we already have

**[1:53:51]** the app here. So, we we already have everything like cloned and set up and verified. So, we just have to bring over

**[1:53:57]** the workflows and then set up the cron job that's going to run every hour to do the triaging and then the implementation

**[1:54:02]** and everything like it. It should work pretty quick once we have the workflows built. And that's why I wanted to use

**[1:54:08]** Archon for this because then I'm not even creating the harness myself from scratch. I'm just building Archon

**[1:54:14]** workflows. And that is the harness. It's a clear example of the value of Archon as a harness builder, which is part of

**[1:54:20]** the reason I wanted to do this dark factory, by the way. This is just such a cool use case to show the power of

**[1:54:26]** Archon. Like these workflows are defining processes that would actually take a good amount of time to architect

**[1:54:33]** from scratch if we wanted to. Like for example, even just having this process of triaging issues and then sending off

**[1:54:42]** miniacs to handle each one of these in parallel like that would take a lot of engineering if we didn't have archon as

**[1:54:47]** a starting point to bring in the context and handle work trees for isolation so we can build each one of them in

**[1:54:53]** parallel and then having the deterministic steps to uh you know label the issues and close issues like that.

**[1:55:01]** That's a lot of work. But now we're able to just rip through this like pretty quick. Like I know that that um the

**[1:55:07]** stream is like two hours now. But still like when you really think about how much we've already engineered here, like

**[1:55:13]** it's a lot that we've built already and we've taken our time with it.

**[1:55:19]** All right.

**[1:55:26]** Um, [laughter] can we use Archon and the Dark Factory as paperclip?

**[1:55:33]** So, yes, you could because each Archon workflow could be like the the, you

**[1:55:40]** know, individual AI employee kind of like how you manage that with um, paperclip. You could that'd be cool.

**[1:55:48]** It's kind of what I'm doing, I guess. Like each Archon workflow you could sort of think of as a different employee. I mean, we literally have the pattern here

**[1:55:54]** where we're doing the b the hold out where it's like this has to run completely separately from the implementation. So, it is sort of like

**[1:56:00]** two different AI employees that the the dark factory is delegating work to.

**[1:56:10]** Smooth as fast. Mistakes are 10x as expensive as planning time. That's right. Pays dividends. Take your time up

**[1:56:16]** front.

**[1:56:24]** All right,

**[1:56:30]** let's see. Learned a bunch about rag from you early on. Yeah, I still cover rag somewhat. Not as much anymore, but

**[1:56:36]** it is still important. A lot of that old content is still very relevant, too. But

**[1:56:42]** yeah, I used to I definitely used to be like the rag guy back in the day, especially when I first started my

**[1:56:47]** channel. Yeah, the appearance of value is very

**[1:56:52]** important. 100%. Yeah. I had a relative doing art and selling at craft shows. She switched to art shows and made a

**[1:56:58]** living off of it and has pieces in museums. That is so cool. Yeah. Right. So, it kind of goes back to our

**[1:57:03]** conversation earlier like when you have something priced at high ticket. Like if you have the good appearance of value, you can price it high like 100%. Yeah.

**[1:57:14]** All right.

**[1:57:23]** Providing unique individual value via video platforms, cohort platforms, etc. is the norm of the future, not the

**[1:57:30]** exception. Yeah, I mean, people crave individual uh

**[1:57:35]** attention, personalization more and more over time as AI takes it away in some parts of life. So, I can see what you're

**[1:57:43]** saying. Yep. Um,

**[1:57:49]** maybe Cole has an AI proof job. How many people would watch this stream if his second brain was doing it alone?

**[1:57:56]** [laughter] Oh, that'll be the day. I don't I don't know if I would ever want to have my second brain run a live stream. Also, I

**[1:58:02]** wouldn't it wouldn't look good right now. But, I mean, there are people that have AI avatars do videos, not

**[1:58:09]** necessarily live streams, but even that, like, it just looks bad. I I don't I don't think that it's really feasible.

**[1:58:16]** [snorts] Um unless like for some reason people are okay with it being an AI avatar because you're just like

**[1:58:22]** delivering the news or something. I know that's usually what most AI avatar channels they are just like AI news

**[1:58:28]** focused, right?

**[1:58:35]** All right. If you're paying 2K to learn how to use etal caston, then you may need more than a second brain.

**[1:58:42]** Uh, I mean that's funny. Yeah, I don't I don't know. Like you can get pretty deep with

**[1:58:49]** Zetocasten. I know myself personally I've only scratched the surface. I have actually taken inspiration from Zealcast

**[1:58:55]** in a little bit for how I've organized my Obsidian vault. But yeah, it's definitely something I personally like I

**[1:59:01]** agree. I feel like you can just figure it out on your own if you have a good hand on your shoulders. But again, to

**[1:59:08]** each their own. I'm I'm trying to like avoid getting like super opinionated on things that like I know like there is

**[1:59:14]** value. Um but yeah, it's just depends how much you want to just like get the

**[1:59:19]** best practices right away versus like figure out yourself over time, I guess, is what it comes down to.

**[1:59:27]** All right, what else we got here?

**[1:59:36]** Yeah. Okay, so this is exactly why I built my own GitHub issue fix workflow for just now. Uh the default archon

**[1:59:43]** commands are very no.js ccentric and that I think that is something we want to improve to make it a bit more language agnostic or a lot more language

**[1:59:50]** agnostic. I can see it arguing with itself to build my Golang app. Yeah. So

**[1:59:56]** I would recommend right now I mean just in general it's good to build your own harness, build your own workflows

**[2:00:01]** because then you can customize it more. I would recommend building your own and using the ones that we have as defaults

**[2:00:07]** as a starting point. So you can point your coding agent to the the default archon workflows and say look at these

**[2:00:14]** for best practices and even like leveraging the structure for fixing issues or creating PRDs or validating

**[2:00:20]** pull requests and like use that as a starting point to then make it specific to my validation flow or my tech stack

**[2:00:27]** or my architecture. Yeah. Cool.

**[2:00:34]** AI co-host. Okay, that could actually be interesting if I had my second brain not like run

**[2:00:40]** the stream, but just like be there as a peanut gallery or something more

**[2:00:46]** practical like kind of giving feedback in real time or even like answering some questions in the chat.

**[2:00:52]** I could Okay, that could actually be kind of cool. I should think about that. How I could have my second brain co-host

**[2:00:58]** a live stream with me. That would be cool.

**[2:01:03]** Okay, I'll think about that. I I'll definitely think about that. Okay. All right. Where are we at now?

**[2:01:11]** Um Oh, it's still going. Jeepers. All right. Well, I guess Oh, yeah, cuz we

**[2:01:17]** had the memory compaction, so that slowed things down a lot. Okay, [snorts]

**[2:01:25]** I just wanted to Okay, I'll let it keep running here.

**[2:01:30]** All right, then you don't need me anymore. No, no, no. I still I still want real people to

**[2:01:36]** help co-host live streams with me. So, Thomas, uh, he's the guy that I have the

**[2:01:42]** comment highlighted for. And then also Raasmus, they've done a lot of amazing work helping me on Archon. And I have

**[2:01:48]** said that like for some Archon live streams, I'd love to get them in to co-host. And I still stand by that. There's no

**[2:01:54]** way if I get my second brain to help co-host with me, it would be a different kind of thing and a different sort of of

**[2:02:01]** value proposition for the live stream uh compared to having a real person like

**[2:02:06]** you or Raasmus uh co-host with me. Like I would want to do both 100%.

**[2:02:12]** Yeah. [laughter] All right.

**[2:02:19]** All right.

**[2:02:24]** Let's see. Um, all right. We got some interesting feedback here.

**[2:02:30]** All right, let's take a look. Once you take this to production, it will just hallucinate success at every step. LM

**[2:02:35]** give the most plausible answer. They rationalize anything they can't reason. This whole video is from 2025.

**[2:02:42]** All right. Hot take. Hot take. But no, I appreciate the push back. um because

**[2:02:47]** what you're saying has some validity and that's why I'm calling it an experiment and that's also why I'm spending so much

**[2:02:54]** time up front planning the system and the architecture because yes, one of the biggest problems with large language

**[2:03:00]** models right now is that they are sickopantic. They always agree with everything that we say and they have an

**[2:03:07]** insane amount of bias towards their own opinions. They're going to rationalize everything and there is a risk if we

**[2:03:14]** don't build the system right that they're going to say that this thing is ready to merge and then it's going to merge it and then it's going to move on to the next issue and we go through this

**[2:03:20]** loop where every single time it's producing AI slop that is a risk but

**[2:03:26]** that's what I'm trying to engineer for here. I'm putting so much time up front because I'm doing things like defining

**[2:03:31]** the hold out pattern for validation so that I'm taking away for some of this I'm taking away from and preventing some

**[2:03:38]** of the psychicopantic behavior because when we go into our regression testing we don't even know what was just built

**[2:03:44]** and so it's just going to be a a neutral judge at least that's the goal what we're doing here there's still a risk to

**[2:03:51]** it 100%. And that's why I'm very clear at the start of the stream here that when we go to this level of autonomy for

**[2:03:59]** our coding agents, like going back to the five levels here, the dark factory here is not what I recommend. If you

**[2:04:05]** want the most reliable software possible, we might get there at some point and maybe this experiment is going

**[2:04:12]** to be a wild success and it's going to be like, whoa, dang. Actually, this can get us a really good, you know, MVP for

**[2:04:17]** any application. Maybe. But yeah, I'm I'm not I'm not like numbed to the fact

**[2:04:23]** that uh psychopantic or psychopanty is a big problem and we have to be really

**[2:04:29]** careful about that. So I I feel pretty confident in the approach that I have here. I think we are going to avoid a

**[2:04:36]** lot of that bias and a lot of shipping things that it says are good when they actually aren't. It's not going to be perfect, but that's also why I have

**[2:04:43]** other strategies. Like I have the like really deep regression testing that I'm going to run every day or every week and

**[2:04:48]** then create more issues to address that. I still am going to have some human in the loop for the very very end uh where

**[2:04:55]** I actually want to like push things to a platform that people are using. So I'll have a little bit like I've thought

**[2:05:01]** about a lot of it. So again, I appreciate the push back, but uh trust me, I'm I'm considering it all 100%.

**[2:05:09]** Okay, let's go back. Still working. Wow. Okay.

**[2:05:18]** All right. Anime girl co-host. Uh, you will never see me do that. [laughter]

**[2:05:25]** It's funny though. All right. Uh, you have to check the parameters to

**[2:05:32]** themselves. Introduce the specific parameters to check. You had extra math and type of engineering checks to

**[2:05:38]** achieve it. Little lost on what you're getting at there. Maybe you could elaborate.

**[2:05:45]** Uh, need to drop off. Good session, Cole. I appreciate it.

**[2:05:51]** All right. Cole the rag guy. Spicy mangoes. Yeah,

**[2:05:56]** spicy mangoes hasn't come up for a while, but I'll have to bring it into another video soon.

**[2:06:03]** Um, an LLM can't even join uh a chat room without everyone knowing

**[2:06:11]** instantly it's an AI. I mean, yes, that's true. Yep. That's that's why I

**[2:06:16]** wouldn't ever have this dream of having a second brain run anything anytime soon. Yep.

**[2:06:23]** All right.

**[2:06:28]** Let's see.

**[2:06:33]** Hard to explain. Yeah. All good. Yeah. Take your time. All right.

**[2:06:41]** Yeah. Okay. I agree with this 100%. If an LLM hosted a show, it would be boring and bland and obviously an LLM. I mean,

**[2:06:47]** yes, I agree. All right.

**[2:06:52]** Um, cool. So, okay. Anyway, our coding agent is done here. So, I want to come back and and give it some more

**[2:06:57]** attention. So, all right. We're done with all of our deb dependencies. The smoke test problem. Dark factory

**[2:07:04]** validate currently runs whole codebase checks. If I kick off the workflow on number 26, the agent will fix the one

**[2:07:10]** lines cores bug. Then validate will hit 130 pre-existing errors didn't create. Um, okay.

**[2:07:17]** So, wow. Okay. So, I guess what what happened here is we're creating the development environment for the first

**[2:07:22]** time. So there are a ton of issues that aren't actually related to the fix that

**[2:07:28]** we'd be running the workflow on. So I I need to actually address these things.

**[2:07:35]** Um yeah, let's do number one. Let's address

**[2:07:41]** all the problems and then run the workflow. Yeah, I just I mean this will take a

**[2:07:48]** while. Uh, but I I do just want to do that because because what I might be able to do is actually create the next workflow

**[2:07:55]** in another Cloud Code session here. I think that makes the most sense.

**[2:08:02]** Let's go ahead and do that.

**[2:08:08]** Okay. So, let me go back to my vault and copy the path again to our plan file.

**[2:08:21]** So I'll say uh read this plan file and uh also load the archon skills. You

**[2:08:27]** can help me build more archon workflows. I have just finished creating my dark

**[2:08:32]** factory adaptation of the fix GitHub issue workflow. Now I want to work on the validate PR workflow and it's very

**[2:08:39]** important that this follows the hold out pattern very closely. I just had someone in the live stream say that they don't

**[2:08:45]** believe in this approach. And I think the hold out pattern is one of the most important things to address their concern. So, let's uh let's focus on

**[2:08:51]** that. I'm being a little silly, but but yeah, I think it's it is very important that we make sure that we are taking

**[2:08:58]** lessons from the strong DM dark factory because it is it is very impressive.

**[2:09:07]** All right, let's see what else we got in the chat

**[2:09:12]** here. While I wait for this to run, we'll kind of monitor these two sessions in parallel here.

**[2:09:19]** Um, is there a way to use Quen 3.6 Plus with Archon, even if it's through Open

**[2:09:24]** Router? So, uh, one thing I learned the hard way recently with open router is you're not

**[2:09:30]** actually able to use claude code with open router for any models outside of the enthropic ones because it doesn't

**[2:09:36]** have an anthropic um, compatible endpoint like Miniax and GLM. So, if you

**[2:09:42]** wanted to use Quen 3.6 plus, I would wait until we have support for uh, Pi.

**[2:09:49]** PI is going to be the third provider that we add this week or next into Archon because then you'll be able to

**[2:09:55]** use other models really easily. You're not going to be like the obviously like right now we have Claude and CEOs and you're a little bit more vendor locked.

**[2:10:02]** You can do what I did in the VPS to point it to other providers but only if they are anthropic compatible like

**[2:10:08]** Miniax and GLM. So there might be a way but I actually tried first before I went

**[2:10:14]** to Miniax directly I tried going through open router and it didn't work. It only worked when I chose an anthropic model.

**[2:10:27]** Um, okay. It's confused here because it's trying to read my workflows in the remote

**[2:10:34]** machine, but I haven't actually pushed it to remote yet.

**[2:10:43]** I might need to Hold on. Oh, no. Hold on. It figured it out. We're good. We're good. All right.

**[2:10:58]** Need a new open source 120B. I mean, yeah, it's been a while since we've had one around that size, for sure. Yeah.

**[2:11:07]** All right. Um, since I love C, what do you think about Blitzies and their C

**[2:11:13]** compilers? Um I don't do I love C. I haven't

**[2:11:18]** programmed in C for a very long time. Actually it's been about five years since I programmed in C. Uh you mean

**[2:11:25]** like C the programming language? I assume because you're talking about C compiler. I I haven't used C in a long

**[2:11:31]** time. I also haven't heard about Blitzy. I'd be interested though. Um funny story

**[2:11:37]** or not funny but interesting fact for you guys. Uh when I was in college, I was a teacher's assistant for a C and

**[2:11:45]** machine learning course. So I I got to uh not sorry, not machine learning,

**[2:11:50]** goodness, a C and assembly course, machine architecture course. So I got to help students debug assembly code for

**[2:11:57]** hours and hours a day [laughter] at one point. That was fun. Yeah.

**[2:12:05]** All right. So all right, what did what do we got now? have enough context. Let me lay out what I'm building. So, hold

**[2:12:11]** out pattern design for the dark factory validate PR. This is the critical workflow for defending the AI rights

**[2:12:18]** code unsupervised concern. Here's how I'll enforce strict hold out across five layers. Okay, so this is the main

**[2:12:23]** concern that we're addressing here with AI sickle fancy in our dark factory. Not

**[2:12:29]** saying this is going to be perfect, but this is my first attempt for the public experiment to avoid the coding agent.

**[2:12:35]** just always saying it work is good and merging it. So we have a separate archon workflow, separate artifacts directory,

**[2:12:42]** separate work tree. There is no way that it can peer into the work of the other agent and potentially take its bias.

**[2:12:50]** So we exclude comments and review. No code, no code or chatter.

**[2:12:56]** Uh we have our our governance files. So we're going to read those as our rule

**[2:13:01]** book. Every AI node is going to start with fresh context. So every step of the way during the validation, we're not

**[2:13:07]** even going to build up bias in the validation itself through the different nodes. The behavior behavioral validation

**[2:13:14]** command leads with a hold out rules section enumerating what it must not consider. It can't find and search for

**[2:13:21]** implementation plans, commit messages, coder rationale, prior review comments. It answers exactly one question. Does

**[2:13:27]** the diff solve the issue body? Very good. And then even another hold

**[2:13:34]** out pattern I I was kind of referencing earlier is like when we do the full regression testing every day or every

**[2:13:40]** week, it also is going to have no knowledge of recent feature implementations or issues that we're in

**[2:13:45]** the middle of addressing, right? Like it just is going to answer the the straight question of like does this application work with all the user journeys we have

**[2:13:52]** laid out in the mission markdown. Good. All right. So now it's writing

**[2:13:59]** everything and we'll let it go. Both both of these are still running actually.

**[2:14:04]** So, I'm going to open up the repo again

**[2:14:11]** because I can I I just want to show off the uh mission and factory rules just like really quick.

**[2:14:18]** So, here's our mission document. So, it it's uh decently concise, not too long,

**[2:14:23]** but it covers um like the core of the application. What is Dino Chat?

**[2:14:30]** Um, who is it for? Uh, patent still pending by the way. I might not keep the

**[2:14:35]** name either. We'll see. We'll see. Uh, who is it for? The core capabilities of the applications. This is specifically

**[2:14:41]** calling out what is in scope. Like if I were to create an issue to add Google Oath to the platform. The triage is

**[2:14:48]** going to be like, oh yeah, good. Let's mark this as accepted because it's literally in the scope for the mission.md.

**[2:14:55]** And then we also cover what is out of scope. What must the factory never build? like we don't want it to add

**[2:15:00]** other YouTube channels. Like if someone created a GitHub issue, we'd want that to be rejected because at least for now,

**[2:15:06]** I mean, I could extend this application later, but at least for now, the scope of this app is for my YouTube content to

**[2:15:12]** be a resource for you guys. We don't want to, you know, allow someone to open an issue to swap the LLM. That would be

**[2:15:20]** bad for my credits. Uh we don't want to like add in payments or subscriptions

**[2:15:25]** like this is meant to stay free. We don't want to over complicate with a mobile app or a desktop desktop app like

**[2:15:30]** no like electronic app. Uh so yes like things that we don't want to build uh

**[2:15:35]** hard invariance like things that we have to we absolutely have to keep the same. So we can't allow for issues that would

**[2:15:41]** try to tweak the rate limiting or the authentication requirements things like that. Uh ways we're allowing it to

**[2:15:49]** evolve. And then quality standards right like that. That's our missions.mmd. And then I can evolve this

**[2:15:55]** over time. This is sort of like my console. So like going back to the analogy here of like you have a car that

**[2:16:00]** doesn't even have a steering wheel. Well, you're still going to have some kind of console to provide higher level directions. And so if I want to tweak

**[2:16:07]** the dark factory, I still have the levers to pull because I can still change the factory rules or the

**[2:16:14]** mission.md or I can update the archon workflows. If I really want to and there's like a drastic issue that I just

**[2:16:20]** really need to fix, I can make a commit myself just straight to the main branch. So I mean there's flexibility with this

**[2:16:26]** here. Um but yeah that's and then the factory rules. This file governs how the

**[2:16:31]** dark factory operates on this repo. So like here here's how we handle triaging

**[2:16:36]** right like this is more context that we it's quite important to feed into the triage workflow. Here's how we implement

**[2:16:43]** things. Here are our requirements for pull requests. For example, I don't want to allow more than 500 lines because I

**[2:16:48]** want every single issue to be a small focus scope of work. It's one of the most important things for getting

**[2:16:54]** reliability out of our coding agents here. Quality gates for automerge. Uh uh

**[2:17:00]** talking about the regression testing, I want to use the agent browser specifically. This is the Verscell agent

**[2:17:05]** browser CLI. It's an open source browser automation tool that I use a lot to test my frontends. Especially when I'm

**[2:17:12]** working on Archon itself, I'm using the agent browser skill. So, I want this to be built into my larger regression

**[2:17:17]** testing workflow that's going to really test everything every so often. Uh,

**[2:17:22]** protected files that it's not allowed to change, right? I don't want it to change its own governance documents because this is my console, my lever to pull,

**[2:17:30]** not its own. Um, how like rules around like when we should autoreject certain

**[2:17:36]** things, how we should escalate cost and throughput. I mean, I don't need to get like super deep into everything here,

**[2:17:42]** but uh yeah, you can see like the factory rules gets more specific. Like this is quite a few lines of code here.

**[2:17:49]** How many is it in total? Oh, sorry, not code lines of markdown. Even this isn't

**[2:17:54]** like super long, but it's 320 lines because there's quite a bit of specificity I want to supply there to

**[2:18:00]** really have my guardrails defined. All right.

**[2:18:10]** Have I you tried using prompts that presume failure and laziness? It can rationalize that too. Um I mean I've

**[2:18:18]** played around with that kind of thing in the past. Um it can rationalize that too. Are you

**[2:18:23]** saying that like that actually doesn't work or are you saying that uh that helps it rationalize or like helps it

**[2:18:29]** address problems?

**[2:18:36]** Let's see. You may want to leverage all your work with rag and build graph rag as the second brain. Obsidian as a

**[2:18:42]** second brain doesn't come close to graph rag, but obsidian is less setup. Yeah, I mean I found obsidian enough for me and

**[2:18:49]** like it's nice because it is less setup like you said, but I mean maybe at some point I will build a whole Greg graph

**[2:18:55]** rag system for my brain and share. It could be cool. uh

**[2:19:01]** still kind of wrestle with that might be overengineering depending on you know how much context you're storing in your brain but I have

**[2:19:08]** that in the back of my mind for sure. Oh, it does work. Okay, cool. Yeah.

**[2:19:15]** Yeah. I mean that's a good idea then. So like my validation process I could have a workflow in the dark factory that says

**[2:19:21]** like okay I need you to assume or like not even not even tell it to assume but just say like this agent was lazy. go

**[2:19:28]** and figure out why it's lazy, what could be better about the implementation, and then like open up another issue or

**[2:19:33]** resolve it directly. All right, that I like the idea of building that in for sure.

**[2:19:42]** All right. Could I use Carpathy's auto research to

**[2:19:48]** improve the dark factory in the future? Uh, until plot twist, it does not stop

**[2:19:54]** running, it starts replication, right? some yeah maybe it will who knows um so

**[2:19:59]** yeah I could use Karpathy's auto research basically if I were to apply Karpathy's auto research it would be a

**[2:20:06]** separate process that has control over actually editing these three files right because like the idea behind auto

**[2:20:13]** research is you have a a file that kind of dictates a larger system like a model

**[2:20:18]** or a repo and then that file you have a coding agent iterate on autonomously based on lessons that are learned from a

**[2:20:25]** feedback loop. So I could build Karpathy auto research to like evolve these over

**[2:20:30]** time. So like right now within the factory rules I have that that um hard rule where it's not allowed to um it's

**[2:20:38]** not allowed to change the governance the constitution. But this is only for the

**[2:20:44]** agents that are dealing with the issues in poll requests. So I could have a separate process that like its actual

**[2:20:49]** sole job is to evolve the governance over time. It's an interesting idea. I don't know if I want to take the

**[2:20:55]** autonomy that far right now because I really want this to be the lever that like only I am pulling on currently. But

**[2:21:00]** that could be a natural evolution at some point. It'd be interesting for sure.

**[2:21:06]** Cool. Yeah, I appreciate all the ideas you guys are sharing here. Seriously, like there there's so much to chew on.

**[2:21:11]** That's why I love this experiment because like the world becomes your oyster for the ways that you can evolve

**[2:21:17]** this and the things you can build with it as well. Like you could really apply this to any workflow. It's just cool being able to like use archon to guide

**[2:21:24]** the entire thing as well. Um like every single line of code that's written here is written from an archon workflow.

**[2:21:32]** So yeah. All right. Uh let's go back and see where we're at now.

**[2:21:37]** Um okay. So we built our third workflow here.

**[2:21:43]** And uh what's this one? This one is Okay. This one is in the middle of actually testing the uh the second

**[2:21:51]** workflow that we built. Cool. So, probably have to wait a while for that to happen. I think I'm going to go

**[2:21:57]** ahead and call the stream here though because we'll have to wait a while until we have like the next big thing

**[2:22:02]** happening. So, I'll keep working on this after the stream and then I'll be making a YouTube video on this as well for

**[2:22:08]** tomorrow, which I'm excited about. So, yeah. All right. Uh let's go back to

**[2:22:14]** full frame here. I appreciate all of you guys being here today. This is a very different live stream to to build and

**[2:22:21]** like actually take my time with something. I haven't really done that on a live stream before. So, yeah, I appreciate all you guys' ideas and and

**[2:22:27]** questions as well. And um yeah, for anyone who didn't get a chance to get their question answered, like always

**[2:22:33]** feel free to comment on a video. Join the Dynamis community as well because I'm active there every single day. Uh

**[2:22:39]** maybe I'll just show that uh one more time really quick here. I'll put a link

**[2:22:44]** once more in the chat here because yeah, if you want to build your own second brain, go through the agent coding

**[2:22:50]** course, just ask any question that uh you have like the Dynamus community is the place for it. So, I'd love to see

**[2:22:56]** you there. Otherwise, I'll go back to my full frame here. But yeah, more live streams coming as

**[2:23:02]** well. Uh because I I actually enjoy doing live streams more than making

**[2:23:07]** YouTube videos. I like both, of course. I love both, but I love doing live streaming. I love being live with you

**[2:23:13]** guys. So, yeah. All right. So, yeah, with that, appreciate all you guys being

**[2:23:19]** here. Uh, stay tuned for the YouTube video tomorrow on the Dark Factory with Archon and more live streams coming up

**[2:23:26]** soon. Hope that you guys have a great rest of your day and I'll see you all

**[2:23:31]** around. Have a good one, guys.
