# Transcript: The Official BMad-Method Masterclass (The Complete IDE Workflow)

**URL:** https://www.youtube.com/watch?v=LorEJPrALcg
**Segments:** 796
**Channel:** BMad Code
**Duration:** 1:14:51
**Uploaded:** 2025-08-02

---

## Full Text

Hey everybody, my name is Brian and I am the 
creator of the BMAD method. This is going to   be a long video, but I want to show everything 
involved with using Claude Code, all the agents,   all the options, all within the IDE. This is the 
first time I've done this, and I want to show you   so many details and just how cool some of these 
features are that I've never demonstrated before   in a video. And I've never seen anybody else 
show some of these techniques also. But there   are chapters here, so feel free to jump ahead 
to the chapter that you need. But honestly,   I really suggest watching this through from 
beginning to end. There's so much good information   that I'm going to be sharing with you today that 
this is this is just going to be so beneficial   for you. You might not be using Claude Code, but 
there's going to be a ton of information in here.   Trust me when I say if you can follow this, this 
applies to all of the other IDEs. So, install   it for whatever IDE you want. A lot of what I'm 
going to be showing applies to all of them. Also,   please give it a thumbs up. It helps the channel. 
Subscribe, tell your friends. Share this. Spread   the word about this. So many people are using 
this in their day-to-day lives. Um, people tell   me every day they're using this at work. They're 
using it for so many different things that I never   even imagined. Let's dive right in. You always 
want to come to the BMAD method and see what's   new. If you come to the BMAD method, this is also 
the easiest way to get started. And I really do   suggest that you start out here. you can come to 
the read me and you can see here's the link to   the YouTube where I'll have this video and other 
tutorial videos posted. Also, while you're here,   if you're a fan of the BMAD method or if you 
try it out and enjoy it, I will say come up   here to the top and then over to the right of 
the sponsorship button. There's a star over here.   Please click star. This helps other people also 
find out about this project on GitHub when they're   looking for agentic tools and helpers to help take 
their vibe coding to the next level. And this is   going to be showing you how to do a green field 
development of a very simple to-do application.   As always, I say take this method and make it your 
own. This is not meant to be the only way to do   it, but it is meant to give you a framework so 
you can mold it to your own way of working, your   own type of project. So, you'll want to subscribe 
to the channel, hit the notification bell so you   know exactly when that video comes out. But first, 
let's get to it, everybody. All right. So, aside   from uh these links here, if you scroll right down 
in the read me, you're going to see this workflow   user guide. This user guide is very simple to 
follow. You can read this, but if you scroll down,   look, there's two diagrams here, and they're very 
easy to follow. This shows you exactly how to use   the BMED method, whether you're doing it in the 
web or in the IDE of your choice. First of all,   you have a project idea in mind, right? You have 
two choices. You can use the analyst. The business   analyst is here to help you further refine your 
idea before you go to the PM and start making your   PRD. So, I'm going to show you how to install the 
VMAD method and actually get set up in cloud code   to start using the analyst. And I'm going to show 
you the optional brainstorming and then also how   we create a product brief which will then make 
the rest of the flow so much easier. And what's   so exciting is you can actually do everything 
with the BMAD method now all within cloud code,   all within the IDE. So if you so choose, you 
do not have to use the web and the full team   stack anymore if you do not want to. I actually 
enjoy and have had great success using the BMED   method fully in the IDE and I'm going to show 
you how to do that today. Really quick though,   we have the analyst, right? And then it's going 
to go to the product manager which we will then   go to the PO and then we will come down to the 
development phase. But take your time really   understanding this. It might look complicated but 
it's actually a very simple flowchart. This is if   you want to use the BMAD method for a brownfield 
or green field development to take it from   ideation all the way to actually developing it in 
the code. Right now you see the only thing I have   here is the BMAD method. Now, you do not have you 
do not have to install the full GitHub repo BMED   method locally. You will only clone that if you 
want to create your own expansion packs or maybe   make changes to the core system or contribute 
to the project, which I would love by the way,   but you don't need to do that. I'm going to show 
you how to use the BMAD method in cloud code   without even cloning the GitHub repo. So, first of 
all, let's um create a project. But what we can do   is from any directory. I suggest doing it from the 
dev directory. We are going to type npx and then   we're going to type bmad- method install. We are 
going to use the bad method 4.33.1. We will just   hit enter to accept that. Let's enter the full 
path of our directory. Since we're in the dev   folder, I'm just say dot meaning this folder. And 
then I'm going to say slash. And now I'm going to   put the name of the new directory that I want to 
create my project in. Since we're doing this from   scratch with no starter project, I'm just going to 
say simple to-do. That's the name of our project.   Just a very simple to-do application. And hit 
enter. It's fine if that directory doesn't already   exist. If you're doing this in a brownfield 
or if you already have started your project   maybe with a template, you'll just give it the 
directory to your project and it will add this   to an existing project. So then right here, this 
is a multi select, but we're just going to go with   the default and select the BMAD core. The BMAD 
core is the agile workflow AIdriven that we're   showing here. So just hit enter. And then we are 
going to shard the PRD, which means we're going   to generate a large document, but then we're going 
to split it up into smaller pieces. So just accept   the default here. And then the same thing with 
the architecture. The architecture file can be   very large depending on what type of project 
you're building. And so you'll want to shard   the architecture into smaller documents and this 
is all automated. I will show how this works. Um,   but that is really going to help you maximize the 
context in your agents so they only load what they   need instead of having to load and read through 
a whole massive file. They'll know which files   they need in the moment to load and it will help 
them with their context. So we'll say yes to that.   Now, here's a warning and this is just pointing 
out this is also a multis select. You can select   one or multiple IDEs that you want to install 
to. For example, let's say that you are a fan of   cursor and cloud code. Well, you can hit spacebar 
and cursor and spacebar and cla code. Today, I'm   just going to be doing this in vanilla VS code. 
So, I am only going to be using cloud code. So, I   have highlighted cloud code with the radio button. 
Make sure that you actually spacebar to hit the   radio button. And if you just highlight it like I 
have right here right now and hit enter, this will   actually not install it for any idees. Uh, one 
other quick tip is depending on the size of your   screen, you might not see all of these options 
here. So, just know that you can arrow up and down   and more options will appear and we're constantly 
adding more idees for support here. Hitting enter.   And now this is asking if we want to include the 
pre-built web bundles. The web bud the web bundles   are not needed for working in the IDE. This is 
kind of warning us in case we thought it existed   and we typed in the wrong directory. For example, 
you know, we could choose a different directory   location or we could cancel and start over. But in 
this case, we're going to say create the directory   and continue. Okay. So, if we scroll up here, we 
can see what did it do here. It installed some   commands for cloud code. So, these slash commands 
will be how we activate our different agents.   And then we've also installed some commands and 
these are great because sometimes we want to do   something without necessarily invoking an agent. 
We are now done. That is the install of the BMAD   method. I know it took a few minutes to explain it 
because I was going through the options, but let's   see how fast this literally is. I'm going to do 
it one more time. I'm going to do n px vad- method install. And I'm just going to give this a 
different folder this time. So I'm just going to   say uh let's say dash demo one, right? Just demo 
one. Enter. Enter. Enter. Enter. Select my IDE.   Enter. Enter. Enter. Boom. That's done. 5 seconds 
and you're ready to go with the BMED method. It's   really that simple. All right. And just to see 
that our two projects are there. If we do ls, we   can see that we do have the demo one, the one we 
just did, and also simple to-do. Simple to-do is   the project we're going to use. So, I'm just going 
to do rm-rf demo one. We do not need that anymore.   And now we can see that we have our simple 
to-do. So, I'm going to go into simple to-do and I am just going to open up uh VS Code. Now, 
right now we have no project here, right? All   we have is what we've installed for our agents 
under BMAD and our custom tasks or commands for   cloud code. And then we have the full BMAD core 
system here. Before we go on, I do want to say one   other thing though, and that is I want to thank 
everybody that has actually taken the time to   buy me a coffee. I've talked to a few of you and 
just know how much it really means for supporting   me and the BMED method and the community here. 
So, I want to thank everybody that's come and   supported the BMAD method. And if you would 
like to uh you can go to buy me a coffee,   look for BMAD code or the link in the description. 
Any amount helps and I truly thank all of you. I   like to use claude code in the terminal inside 
VS Code, but it doesn't matter if you use claude   code outside. You could use it inside the 
warp terminal or your own external terminal,   uh, you know, T-Max or anything, whatever you want 
to use, but I just find it convenient to kind of   keep it all in here. It's easy to, you know, just 
have the, uh, keyboard shortcut to show and hide   the terminal. Um, but we have no other project, 
right? So, as always, if you've used cloud code,   you should know how to do this. You just want to 
type claude. And we are going to launch Claude   Code. Of course, you will have to have installed 
Claude Code and set up your authentication,   but I'm assuming you've done that. If not, go to 
the Cloud Code website, see how to install it,   figure out whether you're going to do the $20 
plan on the 100 or the 200, and then you're   ready to go. Oh, by the way, I have been talking 
to a lot of people that have just been using the   $20 version of Claude Code. If you're fine not 
having the sonnet, excuse me, the opus model,   the $20 clog code will actually get you very 
far depending on how much you're doing. Uh,   so just say yes, we do trust this folder. This is 
the first time we've opened this in a project. You   could run the slashinit command, but I'm not going 
to do that yet cuz there's not really anything in   this project for it to know about. After we build 
a little bit of our project and get some stuff in   place, that's when I would do clait. Well, if 
we go back to the diagram, we can see that the   first person or the first agent that we want to 
talk to is the analyst because we're going to do   some brainstorming. And if you just hit slash, 
if you selected cloud code in the installation,   you're going to see all these all these options 
here. And if you don't want to arrow through this   list, what you can do is you can just start typing 
the part of the name of the agent that you want.   So, for example, analyst, you can just start 
typing it like that and it will highlight it.   Or if you know what it is, you can just type 
the whole thing or you can arrow up and down   to the one that you're looking for. So, here's the 
analyst. So, we're going to select it. This is how   simple it is to use clawed code with the BMED 
method. You saw it takes 5 seconds to install,   maybe 10 seconds if you want to read everything. 
So, this is Mary, our business analyst. I know   a lot of people think the power in the BMED 
method is in the development of actual code,   but I think Mary the business analyst is probably 
the most special agent in the whole BBA method.   If you are just trying to think of something to 
build or maybe you have a little bit of an idea,   I really strongly suggest that you try using this 
business analyst with the brainstorming method.   This goes beyond software development. You can use 
this for any type of brainstorming, whether it be   in your day job or, you know, life questions. 
I've tried many different brainstorming tools,   including professional brainstorming tools that 
have been developed by Google. For example, in the   Gemini gems, there is a default brainstorming gem 
that you can use. It's it's nothing like this. So,   you know, let's let's do that. So, we're talking 
to Mary right now. Mary is active. As always,   you can do star help. And so, now these are all 
of the different things that are available to   you. Now you can either select a number or you 
can type out the name of the command or you can   rely on the fuzzy matching and usually the LLM 
will get it right. So I'm just going to select   number five though which means brainstorm and I'm 
not going to give it a topic. I'm just going to   say number five. Even though Cloud Code supports 
a context window that seems to allow you to go   on and on and on without ever getting close to 
compaction, that doesn't mean you should. So,   when we're done with the analyst brainstorming, 
it will give us a brainstorming document. It will   save it to a folder called Docs, I will start a 
new chat. I like to start a new chat every time   I have an output document, then I'm ready to go. 
So, even if I'm going to talk to the same agent,   I will clear Claude or start a new Cloud session 
and then reload that agent and start going. So,   here we go though. We're going with uh Mary and 
first she's going to ask us four questions. So,   we are going to use our Super Whisper. What What 
is this brainstorming about? I would like to   create a simple to-do app to demonstrate the BMAD 
method. So, this should be a very simple NodeJS   background application. But what I really want 
to brainstorm about is some of the ideas we can   do to at least make it a little bit interesting. 
So let's play some of your brainstorming games   and see what we can come up with. So we'll let it 
spit all that out. So question two, are there any   constraints or parameters that I should know 
about? Well, I already mentioned that we're   using Node.js and I want this to be a very simple, 
straightforward small project just to demonstrate   the BMAD method with Node.js and TypeScript and 
then we will submit that. So this is how you work   with the agent. One of the magical things about 
the BBN method is it not it is not just like a   taskmaster or some of these other things where you 
just throw out your idea and then it does all the   thinking and working for you. As a matter of fact, 
what you're going to see with this brainstorming   is it is actually going to push on you to get your 
ideas out. It is going to be your coach. So that   is what is special about this. It is not checking 
your brain at the door and doing it all for you.   It is going to work with you and it's going 
to bring the best out of both of you. The   BMAD method, by the way, is all about elevating 
yourself, learning, and also elevating the LLM.   So, as a whole, you are both better collectively 
than each one on its own. That is the special   sauce of the BMED method. That's that's the secret 
everybody. Are we aiming for broad exploration of   possibilities or more focused ideiation? Let's go 
broad. Let's go crazy. I want to show just what   you are capable of as the amazing brainstorming 
agent that you are. Nothing wrong with flattering   your LLM every once in a while. They're sure going 
to do it to you. Yes, definitely. And that is also   the default. But when we're done here, this 
will take all of our brainstorming and give us   this amazing artifact. This is one of the coolest 
artifacts in one of the most recent additions to   the BMAD method. This was not even in the original 
release of V4. I thought this would be a V5 thing,   but I love the brainstorming document output, 
and I think you'll love it, too. We haven't   gotten to the brainstorming yet, but here 
we go. You have four options here again. So,   you can pick the techniques, and there's a whole 
list of 20 brainstorming techniques built into the   BMED method, or you can let the agent recommend 
it based on your project. Or you can do random   creative chaos. This one is fun. You never know 
what it's going to get, but sometimes it picks   some of the wackiest ones. or the progressive 
creative journey where we start super broad with   wild what if type scenarios and there's five of 
those and then gradually go down to focus. I just   want to show you all of the different options that 
we have here. So let's go to number one this time.   All right, so here we go. You can see that there's 
quite a few here and there's actually more coming   in the future. So we have what if scenarios, 
analogical thinking, reversal inversion,   first principles thinking, structured frameworks 
such as the scamper method, the six thinking hats,   mind mapping, collaborative techniques such as 
from the improv world, there's yesand, there's   brainwriting, roundroin, random stimulation. 
There's deep exploration with the five W's,   a classic brainstorming technique to really do 
a root cause analysis. There is morphological   analysis, advanced techniques such as forced 
relationships, assumption reversal, role-   playinging, timeshifting, resource constraints, 
metaphor mapping, questiontorming. But with the   power of the BMAD agent, Mary here, she's going to 
guide you through these and help you come up with   stuff that you never even probably imagined. 
You're going to see how with brainstorming,   we can even make a to-do list super interesting 
and exciting. If we would have selected one of   the other techniques up here, those also involve 
multiple selections from here and it will work   through each of them one at a time. Usually 10 
to 15 minutes is what it takes for each one.   So this can be a lengthy process, but look, 
if you're at the beginning of embarking on a   really large project or you have some ambitious 
ideas, it is worth doing this brainstorming to   really come up with, you know, super creative just 
interesting ideas. take the time here to build for   the future. Let's just pick a couple. Somebody 
in the community was suggesting that they would   love to see six thinking hats and also the five 
W's built into the BMAD method. And then they   realized that they were actually already in here. 
So just for them, I'm going to select number six,   the five W's. So we'll do 11. Uh let's do role 
playing. Role playing's always fun. So now the   agent will remember our choices and it's going 
to work with us one at a time. And remember here,   we are not asking Mary to brainstorm and come up 
with this for us. She's going to guide us through   this exercise. This is your own personal coach to 
brainstorm on complex, creative, or interesting   ideas. Folks, this is worth I don't even know 
what. You know, you can pay experts to teach you   how to brainstorm or be your brainstorming coach 
and it's going to cost you thousands of dollars   and you're getting this for free and we're doing 
all of this in claude code. So, this is amazing.   So, okay, what do we got here? Well, excellent 
choice. So, first we're going to start with the   first selection number six, which was the six 
thinking hats, five ways, and then roleplaying.   This is going to generate some seriously creative 
ideas. And again, this does not have to be about   apps. You can brainstorming about everything. 
Maybe you want to brainstorm ideas for a vacation   or brainstorm how you're going to retire in 10 
years or brainstorm, you know, what you should   do with your life or how you should unscrew 
up something in your life. I mean, this can   be used for anything. It is amazing. But, okay, 
so what are we going to do here? White hat. So,   the six hats, there's going to be six different 
colored hats. So, the first hat is the white hat.   What factual elements could make your to-do app 
interesting from a technical data perspective? So,   think about it. What kind of data could it track? 
What metrics, what information could it capture   that most to-do apps ignore? So, I would have 
never asked myself that question on my own. And   I'm already thinking now, wow, I was just thinking 
a simple to-do app from the white hat perspective.   It's now getting me to think about some really 
interesting aspects of a to-do app. So again,   there's no right or wrong answer and I don't 
even know if I'm going to come up with anything   interesting. This is not the actual product that 
we're going to create. We're just throwing ideas   out there. When we get the report at the end of 
all of this, it's going to help us distill down   what is interesting to then go to the next agent 
with. I think it could track how much time elapses   between when they enter a to-do and when they 
mark it done. Also, it would be interesting to   correlate the length or size of to-dos and the 
complexity of the to-dos and how that affects   how soon the to-dos get done. I love using Super 
Whisper, by the way, or Whisper Flow or one of the   other many voice to text ones. So, I'm just going 
to say yes. And one nice thing about working with   clawed code in the IDE is that as you work through 
each section of whatever whatever document you're   working on, it will start creating the document 
for you. So you don't have to worry about being   lost if you if you lose the chat, for example. 
I know sometimes there's anxiety when working   with the web agents that you might lose it and 
it's hard to get the full document out, but here   you're building up the document as you go. And we 
already have our brainstorming sessions here now.   Not too worried about what's in there yet. We're 
just going to keep going. So now we've gone to   the second hat. This is the yellow hat. Optimistic 
benefits. So look friends. Um this would take too   long to go through all of the brainstorming. So 
I'm going to go through all three brainstorming   techniques. All right. And look at this. We got 
our brainstorming session complete. We did all   three exercises. Let's now look at the document 
that it produced. So we will go to open preview.   This is actually going to give us the output 
and keep a record of the brainstorming that we   did. So first we did six thinking hats. critical 
concerns, creative alternatives, and we found some   fun ones in there. And then we went into process 
control. So, it really got me thinking about a lot   of different interesting things. This led to so 
many different things. Then we did the five W's.   The five W's was a lot of fun. The first why is 
why is complexity completion correlation valuable?   And then I gave it an answer. And the answer was 
because people consistently underestimate how long   complex tasks take. And the way the five W's works 
is then it's going to say okay well why does that   or why is that the case and then I gave an answer 
and then it's gonna say well why is that the case   why is that it's a way to really dig down in a 
somewhat annoying way but it's kind of fun doing   it with the AI so then we get into technique three 
which is role playing this is one of my favorite   because the AI will just invent some sort of role 
playing and you never know what it's going to give   you so here I came up with the overwhelmed 
freelancer the context is You're juggling 12   clients, 47 open tasks. You have a current to-do 
app, multiple of them, making matters worse. So,   how do we triage intelligence? Show me what 
actually needs to happen today versus what   I think needs to happen. Client workload balance, 
visual dashboard showing task distribution across   clients to prevent overcommitment. Imagine the 
project that you really want to launch in the   market and what this brainstorming agent can 
do for you. This is next effing level. Okay.   And then it gave us more because I wanted to 
do more brainstorming. So, we didn't just start   with the overland free overwhelmed freelancer. 
We talked about the perfectionist student and   what they would get out of a to-do app, the 
executive assistant, the ADHD creative. So,   I wouldn't have even necessarily thought of all 
those personas. uh the analyst Mary helped me come   up with these different role playinging scenarios 
and we talked back and forth and then it gives us   an executive summary because okay so it's great so 
we did all those things we're not going to use all   of that right it then we kind of talked about what 
was important to me and I kind of like gave it   some of the key insights and we came up with some 
of these key insights together transforming from   task management to behavioral intelligence your 
simple to-do app becomes a personal productivity   research lab that helps users understand their 
actual work patterns versus their assumptions   Tell me that is not powerful. And that is again 
just from like let's brainstorm about a to-do   app and this is what we came up with together. And 
now here's what's really cool is it breaks it down   into what can we do right now? What might we want 
to research and do in the future and then what are   like the moonshots or just the creative ambitious 
things we want to do later. And again this could   be like any aspect of your life. So use this 
use this in your personal life use it for work.   You can see now just how powerful the BMAD method 
is and you don't even need to be in the web. We're   doing this all with cloud code. And as a matter 
of fact, this is just on the cheapest model for   claude code. If I do slashmodel, you can see that 
I'm just using sonnet. I'm not using opus and I'm   not using the default. I'm just keeping it on 
set. You'll learn over time which model to use.   It's kind of an intuition that you'll develop. And 
trust me, even if you don't consider yourself a   strong developer or if you're new to this, you'll 
pick it up. You'll understand. It's it becomes   very intuitive to know which model to use. So, I 
would recommend though just so you can learn that.   Keep it on sonnet for most things. We are done 
with this. We've saved everything to a document.   This is the most important thing with the workflow 
in cloud code or really any agentic IDE that   you're using. we are going to start a new task 
with either the same agent or a new agent. So what   are we going to do? We're going to stop clear the 
context or if you don't want to clear the context   and keep that conversation history for later, 
we'll just kill the window, start a new one,   and restart Claude. Now, you might not know this 
if you haven't used Claude before. Let's say we   close this and then we realize, oh, we're not 
done with the conversation that we were just in.   If you hit slash and just hit the up arrow a few 
times or type slashres, you can now see the chat   that we were in here before. So if you've 
had multiple chats, you'll see a list here.   There's only one right now. If you highlight 
one in blue in this theme, if your theme,   it might be a different color. And now we're back 
in the chat that we were. So that is how you get   back to a previous chat. But we want to start a 
new chat. So again, I'm going to just close that.   I could have done slashcle, but I want to retain 
it. So, I'm just going to do cloud again. And now   we're going to start a new chat. Now, we're still 
going to talk to the analyst in this case. And now   I want to show you how to talk to the analyst to 
do basically the most important thing out of the   analyst that you really want is the project brief. 
Uh, by the way, the analyst is a totally optional   thing. You don't have to do brainstorming. You 
don't have to do a project brief. It is something   that you can do. Again, it really depends on 
the complexity of your project and how much you   already know. If you if if we were just doing the 
simplest to-do app, I would go right to the PM,   create a PRD for a simple to-do app. You can go 
right from PRD with its epics and stories directly   to development. I will show all of that in the 
A to B full walkth through, but right now I just   want to continue showing you this basic path of 
using cloud code. So, we're going to select number   two right now. And this is now going to help 
us create a project brief. And you'll see right   there it loaded elicitation methods. That is one 
of the other big awesome things that's built into   the BMED method. The BMAD method is built up of 
YAML templates which have two things. Basically,   the outline of the type of document, but more 
importantly, and this is what makes it, I think,   more powerful than any other method I've seen 
so far, but other people are starting to catch   on to these ideas. Embedded in the template 
is instructions for the LLM and how it should   work with you. Because as I said a little bit 
ago, the beauty of the BMAD method is not that   you ask it for something and it spits out a whole 
document, but that it really works back and forth   with you coming up with the best possible thing 
that you guys can come up with together. So,   first it's asking, do we already have any existing 
brainstorming results? Market research. Sometimes   it's best to look out in the marketplace, see 
what's out there, and build your own version of   it, maybe with your own twist. It's a big market 
out there. So don't feel like you always have to   be the first to market with anything. So maybe 
you want to do market research and see what is out   there or do a competitive analysis and see what 
your competitors are doing differently. But what   we're going to do is we're just going to take our 
brainstorming. We're going to drop it here and say   here's our brainstorming session results. We can 
use this to kickstart our work in interactive mode   in creating the project brief. You don't have to 
use these exact words by the way. So don't don't   you don't have to memorize the exact words. Talk 
to this as if you were talking to your business   analyst. Now this is going to kickstart it. So 
the nice thing here too is we started a new chat,   but you're seeing because we saved it to a 
document. I'm able to use a brand new context.   It's not getting polluted. It only has the output 
from the brainstorming session. And so it just   keeps it lean. And so now it's going to ask us 
some questions. It's going to pull things out   of our brainstorming and probably get us through 
the PRD a little bit quicker than normal because   you can see here, for example, it already knows 
what the executive summary is because we've told   it when we were doing the brief. I am only going 
to show this first section and then I'm going to   finish the document and then we'll move on to the 
PM. What you can see is after you complete the   executive summary, this is just one part of the 
overall brief by the way. It already figured some   stuff out from our previous brainstorming. we can 
correct it or we can tell it to change things. So,   you'll want to read this and obviously work with 
it. But at the end of each section, you're going   to have multiple options. These are called 
advanced elicitations. Whether you're working   with the PM or the architect or the business 
analyst right here, every section of a document,   most of them will ask you different advanced 
elicitations related to the document you're   working on. Now, unlike brainstorming where it's 
asking you, the user questions, this is where   another powerful aspect of the BMAD method kicks 
in, and I haven't talked a lot about this before,   so this is very important, but this is where 
you push on the LLM to do better. When you talk   to any LLM, whether you're just using the BMAD 
method or not, or you're just using Chat TBT,   if you picture a bell curve, you know, you're 
kind of getting the average slice of the entire,   you know, corpus of information in the LLM. It's 
giving you the average response. It's, you know,   not necessarily great. It's not necessarily 
weak. The advanced solicitation is your chance   to really stick the cattle prod to the agent 
and say, "Do better. Make sure that you have   put this through the fire and you're giving me 
the best possible result." Challenge the scope.   We can force it to brainstorm. So, just like 
it was having us brainstorm, we can now turn   the torture back around on the LLM and have it 
brainstorm different ideas. There's actually   many more advanced elicitations. Again, just so 
it doesn't overwhelm you, it's just giving some   of them. Please do number four and number five. 
And by the way, while we're waiting for that,   notice that it did already start our brief. This 
is our project brief. So again, the beauty of   doing this in the IDE with cloud code is that we 
are generating the documents as we go. But first,   it did critical assumption testing. So, it's 
basically, by the way, this is just another great   thing to do with any product idea that you have. 
And so, I love that the LLM thought about this.   Look at all of your ideas for your product and 
really stress test them and make sure that they   make sense, especially if you want to build an MVP 
first to just get something to market. And then we   also did explore alternative solution approaches. 
So at the very end of it, it kind of synthesizes   everything and it gives some recommendations based 
on what it was doing with itself right there.   Sure. This is just a demo. So we're just going to 
apply them all, update the section, and then we'll   move on to the next section of the product brief. 
Let me say please uh subscribe to the channel if   you're enjoying this. So much more content is 
coming out, my friends. You know, I know these   videos don't come out as often as I would like to 
because I'm also constantly working on actually   improving the BMED method. I'm not here to just 
hype up new things, new products, or, you know,   even tell you I'm using this, but I do want to be 
able to use this forum or this platform to share   the changes with you. But also, I spent a lot of 
time actually working on this. But subscribe to   the channel, hit that notification bell so you do 
know when the next one comes out because it is a   little sporadic sometimes. And join us in the 
Discord. I'm going to finish this up. We will   look at the whole product brief when it's done, 
and then we'll move on to the product manager.   All right. So, I'm going to pick up the pace here 
a little bit. We are done with the brief. We've   gone through the whole thing. The brief is now 
ready for the PM handoff. So before we do that,   I just want to show here's our product brief. 
Since we're in cloud code and not in the web, it   just keeps updating the document for us. We have 
the executive summary, the problem statement, pain   points, why we're doing this, what is the proposed 
solution, the target users. So this says like the   demographics, who do we expect to be using this? 
Why would they use it? How are they each going   to use it differently? And why is it valuable 
to them? This is so important. If you're just   wanting to put any kind of product in the market 
and you're just thinking you're just going to vibe   vibe code something, throw it out there and be 
an overnight millionaire. Maybe you will be, but   you have to consider all these things. You have to 
understand the target audience that you're looking   for. So that's the beauty of this product brief. 
It's going to really help you figure out a lot of   that and make sure you're building something that 
makes sense or might indicate that you want to   pivot on something because it's not actually going 
to achieve what you want to achieve. Why waste a   lot of money, effort, and time building something 
that's not going to go anywhere when instead   you can do this little bit of research up front, 
right? So, we're showing this this whole document.   The point of the product brief is to really work 
back and forth with it and produce this document   that helps you understand what it is you're going 
to build at a most fundamental level. As always,   what did I say? Even in cloud code, even though 
we could go on and on and probably talk to three   agents in a row without running out of context, 
we're still going to start a new one. So again,   we can just kill it and start a new cloud session. 
I'm going to show you a different way this time   and that is just slashcle and this is going to 
clear the conversation history and free up the   context is it's it's basically the same thing. 
You could also do compact. I do not recommend   it. And if you ever see your IDE is showing you 
the warning that you're almost ready to start   compaction. That means that means you've been 
in the chat for too long and you probably want   to wrap up what you're doing. There's different 
techniques for what you for that to get out of   there, but you generally do not want to rely on 
compaction. It's just randomly going to forget   things that might be important. So, there's other 
techniques, but basically, if you follow my method   and you just switch and do clear, but sometimes 
you'll forget and all of a sudden you'll see that   warning and then, you know, you have to adapt. But 
let's um let's talk to the next agent. So if you   don't know what agent to talk to, again, you can 
go back to the diagram. So we've done this, right?   So we we talked to the analyst. We've done our 
optional brainstorming. We didn't do the optional   market research or competitor analysis, but you 
can try those on your own. It depends on what   type of project, but we did create our project 
brief. So now we are going to talk to the product   manager. And if we have a product brief, we're 
going to give it to the product manager. it will   actually ask us. So, I mentioned you might have 
a similar pro or a simpler project. And if you do   or you already know what you want to do, maybe 
you even already have a product brief, you can   just talk to the PM and it will just ask you more 
questions if you don't provide the brief. But if   you provide the if you provide the brief, it kind 
of gives it a kickstart and it will get the PRD   done much quicker. But it just depends what you 
want to work. Again, if you're just doing a simple   app, you don't have to go through all of this. 
just go right to the PM, create the PRD, even   tell it you want it to be a technical PRD with 
architecture built into it. You'll be coding in   no time. So there's multiple flows and workflows 
and ways you can work this system. But again,   come back to this diagram if you're not sure. 
So let's go back to cloud code. So now again,   I hit slash here. We could just type PM. That'll 
take us right to it. If we're not sure, we can   also just kind of look through here and then arrow 
on it. The product manager is going to basically   create a PRD which is a product requirements doc. 
Building a PRD is important and also I'll say the   three most important things with this PRD is first 
of all it's going to give us all the functional   and non-functional requirements and the epic 
that is made up to meet all of those. So right   there we can see everything that is going to be 
encompassed by the build that we're planning here.   Secondly, it's going to help work with us to 
figure out what is in scope for the MVP and what   we can potentially pull out to have post MVP. 
Because if you can make your app the simplest   version of the app that you can make that will 
meet the initial goal, that's less risk, less   investment in a product. Maybe you want to get 
it out there with just a minimum set of features   to test it in the market. That's why you want 
to build an MVP or minimum viable product. what   is the basic thing of this core? But the PM here 
will also capture your other ideas and if they're   not part of the MVP, we'll still hold on to those 
and those will be post MVP epics that you might   do after the main build. So again, what is most 
important here? It helps us maintain MVP scope.   It gives us the functional and non-functional 
requirements with the epics. And then the the   third most important thing, but really kind of the 
key to the whole BMAD method is in those epics,   it is going to create the user stories, but more 
specifically, it knows that we are creating these   for very, very dumb developer agents. Now, as I've 
said all along with the BMED method, you cannot   just check your brain out and leave it at the door 
and rely on it 100%. Right? So, we will use the   advanced elicitation. We will read the information 
ourselves and logically think to yourselves,   does the story sequence make sense. If you don't 
see a story, for example, that says scaffold and   you know, set up your project or set up your 
accounts or whatever you need, you know there's   a problem and something's been missed, right? And 
usually that should be the first one like project   setup. You know, learn to kind of spot those 
things as you go. And there's also some advanced   elicitations that will help us discover that. So, 
let's move on here. So, we are just going to do   create PRD. And I want to show you before we've 
been doing the number, we can also just say star   and we can actually just give it the command name 
also or you could even speak it. Uh do notice that   there are two Yep. There's two different PRDs 
here. There's the regular PRD and then there's   the brownfield PRD. Brownfield is a term that you 
will hear and you'll also hear green field. And I   realize some people don't know what that means. 
So I want to explain it and it's very simple.   Green field means like you're looking out on 
a clean green pasture. It's all open. Pretty   much sky's is the limit. It's going to be easy to 
build your foundation. Nothing is there. Nothing   in is in the way. A brownfield is where all the 
[ __ ] has flowed. It's a cesspool. Maybe it's an   existing application that's existed for months or 
years or it was developed by other people. Maybe   you understand it. maybe it has a lot of issues in 
there. If you're going to work with something like   that, then you'll want to follow the path create 
brownfield and that will have a few more steps in   it to also provided the context of the existing 
application that you might be working on. Number   two, we're just going to do a regular PRD. Now, 
the PM is asking us, okay, do we have the product   brief to create the PRD? So, again, this will 
kickstart us to the PRD. If you were starting   here, you would say no and you would just start 
asking its question or you could go back and do   it. But we're just going to drag it in because 
we do have the brief. And we'll say here you go,   buddy. There is a lot of overlap between the 
product brief and some of the sections of the PRD,   but it's really going to translate that from the 
language of the product brief into functional and   non-functional requirements and a few of the 
other details that we need in there. Okay. So,   let's see what we got here. So, it gave us some 
goals. So, it understands what we're trying to   build, why we're building it. We got some detailed 
rationale here. Tradeoffs made, key assumptions,   and areas needing attention. We have options 
to do advanced solicitation. And by the way,   I love this. Just like before, as we produce our 
document, we are going to generate each section   of the document one at a time. So, it's always 
going to have access to everything it's done.   It's going to he keep kind of a cohesive vision 
of the document we're building and it's going to   build it up section by section. Beautiful. I love 
this. Now we are doing section two. We moved on to   the next section. So this is the requirements. 
So this is going to give us the functional and   non-functional requirements. Take your time and 
read through this. Again, getting this right is   important. And you really want to try to look, is 
there a functional requirement here that you do   need or don't need. I want to show you my absolute 
favorite advanced elicitation to use here. Let's   see if it suggests it. But I want to show you 
how you can actually find what other advanced   elicitations are available for the BMED method. 
But what you can do is you can go to data. We're   going to go to data and here are the elicitation 
methods. We can see them here. So there's explain   reasoning, critique and refine, analyze logical 
flow, assess alignment with overall goals,   identify potential risks, challenge from critical 
perspective, tree of thought, deep dives,   hindsight is 2020, the if only brainstorm, 
agile team perspective shift. This will take   your different agents and have them all look 
at it from a different perspective. It's a lot   of fun. Uh stakeholder roundt, metaprompting 
analysis. So some of these are very correct.   uh very creative. Um and then we get into some of 
the new advanced 2025 techniques that have been   added in recently. Self-ont self-consistency 
validations, the rewoo, which is reasoning   without observation. I love that. Rewoo, persona 
pattern hybrid, emerging collaborative discovery,   red team versus blue team, innovative tournament, 
escape room challenge, proceed and no further   action. I want to tell you, I've done a lot of 
research into how to really prompt engineer and   get the most out of LLMs, and these are some of 
the best techniques that I've found from Google   and Anthropic. But I've also studied multiple 
prompting competitions where expert prompters   just compete, and I see a lot of them using 
some of these very cool techniques, and some of   these are just crazy fun. So, let's let's pick a 
let's pick a wild one. I like the what if if only   hindsight is 2020. So what I'm going to do is I'm 
going to just select this here. This is another   thing you can do. Eventually these will all 
just be in the menu at one time. Close this now. This looks at all your functional and 
non-functional requirements and then it   imagines that we've built the application and 
that we're I don't know sometimes it does six   months out sometimes it does a couple years out 
and it's an analysis where the LLM does this   conversation with itself reflecting on a board 
meeting or something else where people are like if   only we would have done this something would have 
happened. So let's see what it did here. Imagine   it's 6 months from now the MVP is launched. You're 
looking back at these requirements. What if only   statement might you be making? If only we had. If 
only we had included basic team sharing features   from the start. Non-functional requirement one 
might be unrealistic for bootstrap budget and   single developer. What if we hadn't promised cross 
device sync and MVP? Functional requirement 7 adds   significant technical complexity. What if we 
started with single device and added sync in   phase 2? So what's going on here? This is actually 
helping you figure out how to cut scope out of   your MVP. Keep it a lean lean build so you can 
actually get something to market. Get it tested   and then layer those features in later. This is 
the real agile way of product development. Super   powerful. So I'm going to say apply changes and 
update sections. Revise the requirements based on   these insights. Uh before you do that, you can 
talk to it. You can question different things.   You can tell it what you want to keep and not 
keep, but I'm just going to do number one for   purposes of time. So, I'm going to finish this and 
I'm going to get this up to the epics and stories   and then we'll continue together. There's only one 
epic right now because I told it just CRUD. So,   foundation and core CRUD operation establish the 
project setup. As I said, always kind of look   out for that, right? Uh we are going to have local 
database. So, it'll do the database initialization   and then implement all basic to-do management 
commands. add, list, complete, delete, update,   basic crud. So, since there's only one epic, 
it's going to go right into the stories here. So,   epic foundation and core. You'd want to read this. 
And as always, read the stories and acceptance   criteria and think, does it make sense? Is there 
something being called out that actually relies   on something later? This is great. This is how 
agile actually works in story breakdown is each   piece of functionality can kind of be its own 
standalone story. Can we list and search for the   to-dos? Can we mark a to-do done, delete a to-do, 
update a to-do? You can also ask it questions if   you don't see the one you want here and you don't 
want to look. So, I'm going to tell a deep deep   think please that the order and granularity of the 
stories actually make sense. The sequencing must   be perfect with no story dependent on a later 
story. It's checking to make sure that they all   follow the correct progression. You're absolutely 
right. Let's deeply analyze the story sequencing   and granularity as there are significant 
dependency issues in the current approach. So,   do we accept it? We'll say yes. So, does this 
sequencing now make sense? So, let's say yes.   All right. So, looks like Claude now thinks we 
have seven stories in perfect sequential order.   Do we believe that? Well, don't check your brain 
at the door. Let's close that though because we're   done talking to the PM for now. But you do want 
to, you know, go through your doc. Imagine this   is a big ambitious project with multiple epics. 
Do you really just want to accept some slop and   move on and start developing? Maybe. But I would 
suggest take your time and really understand and   try to learn from this. Ask the LLM questions. The 
LLM is not going to always tell you to do this.   The reason we have agents and personas is because 
it's to help you also have a mental model. Not   not only does it help the agents perform better 
and keep focused on their domain expertise and   you know tailoring responses to that persona 
that they're interacting, but it's also for   you to understand that as they are serving this 
role, talk to them as if they were in that role.   So, you're talking to a product expert or 
an architect or a scrum master. Ask them   why they're choosing things. What do different 
things mean? The beauty of this too is you don't   have to be embarrassed about asking questions. 
You can ask this what people might think is the   dumbest question. Look, maybe you don't know, 
maybe you've heard the word database before,   but you don't even know what a database is. Okay, 
you can Google it. It'll give you a definition,   but you could also just ask why are you using a 
database for a to-do app. It mentioned a name of   a database. You could ask it why did you select 
this database? Why not something else? And it'll   give you an answer. So, you can learn a lot 
just by talking and at any time you can just   ask the agent questions about this document or 
any of the documents we're going to do. Now,   we can start a brand new chat with the architect. 
So, I'm going to open up Claude again. So,   we're in the brand new cleared context. Nothing 
here. And if you're not sure, you can always clear   it again just to make sure. Now, we're going to do 
slashchitects. Now, again, this is a very simple   project. I would probably try to just go from 
PRD to stories. There is a workflow that supports   that, but I want to show you basically how the 
architect works. So, same thing. It'll either show   you the commands. If it doesn't, type starhelp and 
you can see what's available here. Now, here we   have a couple different architectures. Don't be 
confused, but it's pretty simple. You're either   going to do a full stack architecture, which is 
front end and backend, maybe is a monor repo,   which means all the code is in one project such as 
Nex.js, or maybe it is two separate repos and two   separate projects, React for your front end, 
and maybe a cloud service for your back end,   and maybe in two different GitHub repos. Um, you 
also might be starting with a starter project such   as NECJ, Nex.js with Superbase and Shad Saiyan and 
Tailwind. If you're doing that, you would want to   generate your project, get your boiler plate and 
share that with the PM or the architect. So, as   they're doing the architecture, they already know 
what you have, what your technologies are, what is   in your requirements.txt if you're doing Python or 
your package.json JSON if you're doing TypeScript   or JavaScript, Node.js, excuse me. Create full 
stack architectures if you're doing front-end   back end. Create backend architectures if you're 
just building like maybe a service project or   utility or anything that does not involve a web 
front end or a guey front end. The one exception   is you might have a CLI. You will still want to 
select create backend architecture. And then there   is a create front-end architecture. If you're only 
working on a web front end, maybe you're working   on a website or maybe you already have a backend 
REST API and you just want to build the React app   to call that REST API. That's where you would say 
create front-end architecture. And then finally,   our friend the brownfield is back. So we can 
create a brownfield architecture. And again,   that's going to involve a lot of the research 
that the analyst and the PM did to understand your   current project. Feed that into the architecture 
along with some of the challenges of architecting   against an existing project. Creating our backend 
architecture because we are doing what a to-do app   only in the CLI. It's just running in the command 
line for demonstration purposes. So, we'll hit   number two. Now, let me give you a tip on working 
with the architecture. Regardless of what actual   IDE or system you're using, you want to use the 
best model you can. I'm showing you that this can   be done in the $20 version of Claude Code, but I 
would recommend, especially on a more challenging   architecture, use Opus or whatever powerful model 
you have because you will get potentially better   results. Or do this on the web with Web Gemini. 
save your credits and then just get into the IDE   after we have our architecture. But I actually 
enjoy doing the architecture here because as you   can see yet again we are producing our document 
in real time as we go section by section. It gave   us a sequence diagram. It gave us some highlevel 
architecture. You know what we're doing with the   database, how we're going to handle error handling 
and global installation and uninstallation   process. Do we want to focus on any of these? We 
can do alternative analysis, stakeholder input,   risk assessment, resource impact, user 
experience impact, technical feasibility,   market validation. You know, read what it gave you 
and think about if any of these make sense or if   you want to do any of these. And if not, just move 
on to the next section. Also, question in this   next section what technologies it comes up with. 
Make sure it knows what the latest versions are   or what the best version is. You can also tell it 
to use the web to make sure that it's considering   the latest technologies for everything that it 
picks is this is going to create a table of all   the specific versions and technologies we're 
using. If you don't have this and tell it what   specific technologies, what what testing framework 
you're using, for example, what'll happen is later   on your LLM will be developing. It might be using 
justest just because it sees that it's already   scaffolded and then it'll run into a problem and 
instead of trying to fix it, it might be sneaky   and just try to install a whole new test framework 
without you noticing. It'll tell it but maybe   you're not paying close enough attention or you 
walk away and you come back and all of a sudden   there's a new test framework or there's another 
new package. And that's because it's not forcing   it to stick to any list. When we create this table 
here and shard this out to a separate document,   the dev agent later on will always be aware of 
this technology stack and will not diverge from   it. It's a very powerful technique to make sure 
your agents are all using consistent libraries,   packages, and versions. So, I'm going to 
go through the rest of the architecture,   but just remember section by section you really 
want to use the advanced solicitation. So let me   show you right now just one quick example example 
and then like I said I'm just going to kind of run   through the rest and we'll pick up at the end. So 
let's say in here doing data models. So this is   great because if it makes data models that means 
later on the agents they'll always conform to the   same model. And much like our technology stack you 
don't want them producing different models on the   fly. But let's say for whatever reason I don't 
understand why we're creating these or I don't   like them. So I'm just going to ask a question. 
And this is one thing you can do. You don't need   the prompt here always to ask just ask a question. 
So say explain to me the interfaces you created   and I want an explanation of why each one of them 
exists and are we missing any? So the architect   is programmed to also be very explanatory and 
explain in a very clear way meeting you at your   level. I recommend talking to all these agents. 
Even if you're not in the middle of a project,   you can load up these agents and just talk 
to them. talk at them talk to them about your   ongoing project. What did he tell us? He told us a 
lot. So, let me explain each type script interface   I created and analyze if we're missing any. So, 
the to-do interface that's obviously important,   but why it exists? Type safety. So in other words, 
an interface allows us to define a object or a   par or basically this would be like the blueprint 
for an object that we will create later and every   object must have a task string completed completed 
at and an ID to make it unique. Um so why does   it exist? Type safety. We just talked about 
that database mapping. So that's interesting.   So what that's telling us is he's setting up an 
interface here that will later also map directly   to the SQL light. So we always make sure we 
have the same properties and fields in our local   database. And it's also going to help us define an 
API contract. The API contract when it returns a   to-do is going to be guaranteed with each to-do to 
return these properties. So if we wanted something   else in our to-dos, now would be a good time 
to add it, not later on when we're developing.   So that's again why you want to actually pay 
attention and try to understand what the architect   is telling you. And if you don't, just ask it. 
And if you read this and you still don't ask it,   play five W's with it and ask it why you did this, 
why you did that, well then why did you do that?   Well, why did you do that? And on and on and on. 
Again, you can learn so much just by engaging in   discussions with the architect to really start to 
learn how software is developed in reality. It's   very powerful stuff. All right. Right. And so the 
uh architecture looks like it is done. We finished   the last section. It gave us the final summary and 
the document is updated. Let's just make sure that   everything is in the document. It's pretty large 
document which is why we shard these documents,   but we have our success criteria. Before we 
shard our documents, just like with the PRD,   you really want to go through here and make 
sure that everything makes sense, such as   coding standards. As a matter of fact, coding 
standards is one of one of the most important ones   because this will be used by the developer agent. 
Directory structure. You want to make sure that   this makes sense. If you want to render sequence 
diagrams, you can just rightclick in VS Code and   you can say open preview and then you should be 
able to see some of these nice looking renders.   If you do not have that option in VS Code or in 
Cursor or Windsurf or whatever you're in, you'll   want to go to your extensions, which is this icon 
here. These are our installed extensions. And   you'll want to make sure that you have something 
similar to Markdown all-in-one. I like this one   along with Markdown preview mermaid. This will 
give us mermaid documents or mermaid rendering   from this one. And the markdown all-in-one will 
also let us auto format markdown to make sure that   it's valid markdown. Here's our sequence flow. 
Make sure that the flow makes sense. Here's our   database schema. Again, if you don't understand 
something here, ask it. Ask it why I did this,   but this makes sense to me. Here's the source 
tree that it's going to produce. This controls   where the LLM is going to look for files, where it 
should put them when it creates them. And again,   we'll just help it stay on the rail. Having 
a source tree is a very important document   to keeping the LLM on track. I'm going to open 
up this and I'm going to show you how you can   just talk to the agent. In the coding standards, I 
really want to make sure that the developer agent   will use Gab will use good Java do style comments 
or JS doc style comments on all public functions,   public interfaces, etc. So, please add that to 
the proper section in our architecture under the   coding standards. Okay, that was a little bit 
wordy, but that's why I like using just the uh   speech to text because I can kind of work it out 
in my mind as I'm saying it and usually the LLM   can get it right and understand what I'm talking 
about. But this should now add some documentation   standards so we will have good consistent 
documentation. Now, now I'm good with this. Now I   think the document is great and we are done here. 
So now I'm going to close cloud code. I'm going to   close all our documents and let's look back at 
our project. We now have an architecture and a   PRD. The two key documents that we need. We don't 
really need the LLM going forward anymore. Looking   at the brainstorming or the brief. Every file that 
you keep here is potential context that the LLM   might choose to load. You can add restrictions. 
you can tell it not to, but it's better sometimes   to add these to another folder. So, you could 
add these to a project references file, or you   could just take them out and store them, or maybe 
you store them online, depending on how you're   organizing your project artifacts. But whatever 
you do, you don't want them to get pulled in and   polluting your context overall. Okay. So, we'll 
come back to Claude use the shard command. So,   if we just type shard, we will see that there's 
a task shard doc. And do we want to use the MD   tree? Yes, we do want to do MD tree. So, okay. 
So, now it's saying great, the MD tree command   is available. If it was not available, 
it would suggest that you install it. So,   now I need to know which documents you'd like to 
shard. Please provide the path to the document you   want to shard. And I'll use the MD tree explode 
command to automatically split it into smaller   documents based on level two sections. So, first 
of all, we want to do our PRD. So, I'm just going   to drag it in there. That's it. And the default 
should be a folder called PRD, which it is. And   look at that. It's already done. That's how quick 
it is. We now have our epic list. And here is the   most important one. Epic 1, epic 2, epic 3 if 
there were multiple with all of the stories   because this is what the scrum master is going to 
use to build up our stuff for our developer. So,   that is great. So now we can say do the 
architecture and we're just going to drag it in. So as you can see using the BMAD method in cloud 
code is super easy. We don't have to jump back and   forth to the web. It's super powerful and it just 
does a great great job at following instructions   regardless of which model you use in cloud code. 
Here's our architecture again just in seconds. And   now this is the one that is really good to shard 
because look we have coding standards which has   our documentation and some of our other stuff 
in here that we wanted with examples source   tree. So this shows us exactly what our project 
structure is going to look like. Text deck those   three are critical and I want to show you why so 
you understand this regardless again of which tool   you're using. If you go into Claude, since we're 
using Claude, we'll look at the Claude version.   And let's look at what the developer agent has 
here. The developer agent has a command on here   that basically tells it, look at BMAD core, look 
for the core config. And this is what tells the   developer agent what files it will load every 
time. So the way the developer agent works,   I've explained this before but I'll say it again. 
The scrum master is going to take the highle epic   and story. It's going to read through various 
architecture documents. It's going to understand   one story at a time and it's going to create a 
very detailed story for the developer, a lower   level developer story. This is a self-contained 
file for the developer to have all of the context   it needs to build the application. We talked a few 
videos ago ago about context engineering. This is   the core of context engineering. Giving the agent 
exactly what it needs to build its little piece of   the kingdom, right? But additionally, not only 
is all of this information the scrum master is   going to put in there exactly what it needs from 
the architecture and other sources, the developer   is always going to load these files that you have 
listed under dev load always files. By the way,   I didn't have to make this myself. This file was 
created on the install. But if you ever wanted to   customize it, maybe there's another file that you 
always want the dev to load, you can add it here.   But again, here's our key documents that were 
sharded from the architecture, the coding   standards, the tech stack, and the source tree. 
Take your time and really go in there and make   updates to those if you need to and change them if 
any of these things change. All right, we've come   a long way. If you're still with me, thank you for 
sticking with me. If you made it this far, I would   love to know who's actually still watching. Um, 
because I bet this is a very long video. I hope   people are appreciating it, though. So, if you've 
made it this far, how about leaving a comment   down below and tell me what is the craziest thing 
that you want to brainstorm with the brainstorming   agent. Give me some of your wildest ideas. And if 
you actually use the brainstorming agent to do it,   come back and tell me one of the craziest things 
you came up with that you never thought you would   come up with before. I would love to hear it. 
Maybe also jump into the Discord and and talk   about your brainstorming adventures. So, as 
a matter of fact, some people in the Discord   actually talked about spending hours just doing 
brainstorming and coming up with some amazing   ideas. We sharted our documents. We have our 
architecture. We have our PRD. So, that is   great. Now, I'm going to do something here. I'm 
going to create a new folder that I'm just going   to call for now temporarily. And I'm going to say 
get init. put everything in there except for the   architecture in the PRD sharded documents. And now 
I'm going to add agit ignore. So I'm going to say   new file.getit ignore. I've added agit ignore 
file. Please populate it with the common things   that should be in a git ignore and also include 
the ignore folder in the git ignore and the.getit   get ignore those files should also generally be 
ignored by clouds so it won't clutter the context.   So there we go. So we just populated a get ignore 
with a lot of common properties. Now if you're   using a starter template or a starter project, 
it's probably going to set up your git ignore   for you. Or if you're using like Nex.js, it'll 
it'll set that up for you. In a complex project,   you would want to use the PO at this point. And 
the PO has a command called run checklist. And   it's going to run the PO checklist. What that does 
is it's going to look at all of your user stories   fresh and it's going to look at the architecture, 
make sure that they're aligned, make sure that   nothing came up in the architecture that needs to 
feed back into the stories because maybe something   changed or if there's any big gaps. It's a really 
good idea to do that. Sometimes it'll find things,   but this is such a simple app and like all of the 
BMED method, it's adaptable. We do not have to do   that step. So, we're going to skip that and we're 
going to jump right to the scrum master. Now,   if you've never used the scrum master, you 
might not know what it can do. So, as always,   I recommend doing /help if it doesn't give you 
the help commands automatically. Sometimes it   will. That's just the nature of LLM sometimes. 
Um, so we have a few things here. We can draft,   which means create the next story. We can 
do correct course. This is a feature that   a lot of people have asked for and don't know 
exists. Why does my chair keep sinking? Um,   correct course is something let's say you've 
developed, you know, halfway through some of   your epics. You're mid project in the middle of 
a story and you realize you forgot something or   you want to make a big change. Wrap up what you're 
doing and then talk to the scrum master or the PM.   You can choose either one and run this correct 
course command. It's going to ask you a bunch   of questions and it's going to analyze how far 
you've gone and whether it's better to, you know,   revert back to a certain earlier stage and produce 
new stories and epics or maybe generate new future   stories and epics from where you're at right now. 
Or your change might be so drastic that it just   recommends, although it generally shouldn't, that 
you start over. But not only is it going to give   you these suggestions, it is going to help you. 
It's going to figure out what epics and stories   need to be modified or changed or added or removed 
so you can do this pivot, account for it, and   still get to your end goal. Maybe it means making 
updates to the architecture or as I said the PRD   or maybe you found a new API or a new library 
that you want to do use, so it might put it in the   tech stack. All of that's a possibility with the 
correct course command. That could be a lifesaver   depending on the situation. Of course, it's 
best to avoid that which is why you go through   a lot of planning. What we're looking for here is 
number one, we want to draft the first story. Now,   if you know what story it's time to draft, 
just tell it. We know we want to do epic one,   story one. So, what we can do is we can just 
say we can say we can say star draft 1.1.   So, let's say we're halfway through and it's time 
to do story 2.3 because story 2.2 finished. You   can just tell it draft the next story and it will 
figure out what the next story is. Or you can tell   it which one to do. That'll just make it a little 
bit more streamlined. It'll go faster and it'll   start drafting drafting the story that it needs 
to. When it drafts a story, it's always going   to check if there was a previous story. if there 
was, it will also check if there's any notes in   that story that it needs to carry forward into 
the new one. A lot of times also these project   foundations will have steps in them. So, you 
really want to read these stories especially and   see if there's any human basically things that you 
need to do. Maybe you need to set up an account or   maybe you need to, you know, visit a website and 
provision some infrastructure that for whatever   reason cannot be done by the LLM through a command 
to the remote service. Maybe you have to get out a   credit card and pay for something. Okay, so it's 
done. Let's look at our story and let's see if   it followed the proper template. And it's always 
going to put it in draft mode. This is standard   agile story practice. So as a developer, I want to 
establish the basic noode.js JS TypeScript project   structure so that I have a solid foundation for 
CLI development. Acceptance criteria means what   does it actually take to say yes this story is 
done and complete. The tasks and the subtasks   are going to sound a little bit similar to this a 
lot of times and it should because these are the   actual steps that the developer agent is going 
to follow step by step to implement our story.   This is where the scrum master agent goes 
through all of the architecture documents,   finds information that is relevant to the 
story and gives it to it here. Since we're   doing project setup, the agent needs to know the 
structure of our project that the architect came   up with. So that's why it pasted it here. So the 
developer agent has this contextual information   and doesn't have to search for itself bloating 
its own context. So there are placeholders where   the dev agent can put notes and also where the Q 
agent QA agent can put their notes. Change this to   approved. We are done with the scrum master. 
We're just going to close our context and   we're going to start a new one because as always 
between every step even though we don't have to,   it's better practice and it minimizes the overall 
context. All right. And now we're here in the home   stretch. We got James, our full stack developer is 
locked and loaded. Let's do star help. Now you can   just tell James develop a story and it will find 
the highest numbered story that is set to approved   or already in progress that maybe wasn't finished 
by an instance of himself from before. Or you can   just tell him. So why don't we just tell him then 
he's not having to do the searching. It will just   be more uh more streamlined. So we'll say star 
develop story. We could have also just told it   develop story. We could also just say number five. 
Regardless, I'm just going to hit space. And then   I'm going to drag in the file. And now we should 
finally see our developer implementing story one.   I figure let's just do the first story and then 
we'll commit. But we're just going to say yes,   let it do whatever it wants to do. It's setting 
up our package.json. JSON. And one thing we can   do is as it adds the different packages that we 
need as it's going through the different subtasks.   We'll make sure that this is aligned. By the way, 
we could turn on the unsafe mode for cloud and it   would just churn through. But for right now, 
I just have it. I'm sitting here. We're doing   this together. I don't mind just telling it 
yes, continue. If you want to roll the dice,   you can turn off all the safety features 
and let Claude go wild. And look, we're   uh we're almost done. It it created a bunch of 
its own internal to-dos mapped to the actual   to-dos in the story. And then we should see that 
it will actually go through. Now it's starting to   check them off. We'll set the status to ready 
for review. So when it does that, you have two   options. I actually recommend doing both, but 
it depends on the story. If it's a simple story,   probably not necessary, but review it yourself. 
Maybe test out the functionality manually. Check   it out. I would start a new context yet again. 
So, we're just going to exit. We're going to say   Claude. And now we're going to use our QA agent, 
which is quality assurance. So, let's do star   help on Quinn. Quinn the QA agent. So, let's do 
number one. And let's pull in story number one. Now, again, this is a fresh, brand new context. 
So, it's going to be looking at the story and all   of the project source code and other updates 
that it made to really make sure that it did   a good job. So, this is going to this is 
going to do a pretty good deep examination.   This is another place where you might want 
to use Opus. Maybe even more importantly   than when we were doing the development because 
this is the critical kind of piece that makes   sure that the agent didn't go off the rails 
and stick files in a stupid place. Um, and it   looks like it's already uh finding some things. 
This was obviously a very small setup story. So   there's not a lot for the QA to do for the QA 
to do, but it did find a few things and it gave   us uh these compliance checks that it did here 
or improvements that it made. So this is great,   right? I just want to say thank you again. If 
you stuck all the way through this video and   made it through here, you're going to be so 
far ahead of the game. You're going to be a   power user using the BMED and understanding 
the BMAD method, especially in claude code.   I welcome you to come into the Discord forums 
and give me your shared experience of how it's   working for you. Share with the community or 
if you have questions still ask the community   and they'll be happy to help you. I'm sure also 
it's a great it's a great place. We'll see you   next time. My name is Brian. This has been a 
very long episode on the BMAD code, but I hope   it was helpful and also worth waiting for. So, 
thank you everybody and we'll see you next time.

---

## Timestamped Segments

**[0:00]** Hey everybody, my name is Brian and I am the 
creator of the BMAD method. This is going to  

**[0:05]** be a long video, but I want to show everything 
involved with using Claude Code, all the agents,  

**[0:10]** all the options, all within the IDE. This is the 
first time I've done this, and I want to show you  

**[0:15]** so many details and just how cool some of these 
features are that I've never demonstrated before  

**[0:20]** in a video. And I've never seen anybody else 
show some of these techniques also. But there  

**[0:24]** are chapters here, so feel free to jump ahead 
to the chapter that you need. But honestly,  

**[0:29]** I really suggest watching this through from 
beginning to end. There's so much good information  

**[0:33]** that I'm going to be sharing with you today that 
this is this is just going to be so beneficial  

**[0:39]** for you. You might not be using Claude Code, but 
there's going to be a ton of information in here.  

**[0:44]** Trust me when I say if you can follow this, this 
applies to all of the other IDEs. So, install  

**[0:50]** it for whatever IDE you want. A lot of what I'm 
going to be showing applies to all of them. Also,  

**[0:56]** please give it a thumbs up. It helps the channel. 
Subscribe, tell your friends. Share this. Spread  

**[1:03]** the word about this. So many people are using 
this in their day-to-day lives. Um, people tell  

**[1:08]** me every day they're using this at work. They're 
using it for so many different things that I never  

**[1:13]** even imagined. Let's dive right in. You always 
want to come to the BMAD method and see what's  

**[1:18]** new. If you come to the BMAD method, this is also 
the easiest way to get started. And I really do  

**[1:23]** suggest that you start out here. you can come to 
the read me and you can see here's the link to  

**[1:28]** the YouTube where I'll have this video and other 
tutorial videos posted. Also, while you're here,  

**[1:33]** if you're a fan of the BMAD method or if you 
try it out and enjoy it, I will say come up  

**[1:37]** here to the top and then over to the right of 
the sponsorship button. There's a star over here.  

**[1:41]** Please click star. This helps other people also 
find out about this project on GitHub when they're  

**[1:46]** looking for agentic tools and helpers to help take 
their vibe coding to the next level. And this is  

**[1:52]** going to be showing you how to do a green field 
development of a very simple to-do application.  

**[1:57]** As always, I say take this method and make it your 
own. This is not meant to be the only way to do  

**[2:02]** it, but it is meant to give you a framework so 
you can mold it to your own way of working, your  

**[2:07]** own type of project. So, you'll want to subscribe 
to the channel, hit the notification bell so you  

**[2:12]** know exactly when that video comes out. But first, 
let's get to it, everybody. All right. So, aside  

**[2:17]** from uh these links here, if you scroll right down 
in the read me, you're going to see this workflow  

**[2:23]** user guide. This user guide is very simple to 
follow. You can read this, but if you scroll down,  

**[2:29]** look, there's two diagrams here, and they're very 
easy to follow. This shows you exactly how to use  

**[2:33]** the BMED method, whether you're doing it in the 
web or in the IDE of your choice. First of all,  

**[2:40]** you have a project idea in mind, right? You have 
two choices. You can use the analyst. The business  

**[2:45]** analyst is here to help you further refine your 
idea before you go to the PM and start making your  

**[2:52]** PRD. So, I'm going to show you how to install the 
VMAD method and actually get set up in cloud code  

**[2:57]** to start using the analyst. And I'm going to show 
you the optional brainstorming and then also how  

**[3:02]** we create a product brief which will then make 
the rest of the flow so much easier. And what's  

**[3:07]** so exciting is you can actually do everything 
with the BMAD method now all within cloud code,  

**[3:14]** all within the IDE. So if you so choose, you 
do not have to use the web and the full team  

**[3:20]** stack anymore if you do not want to. I actually 
enjoy and have had great success using the BMED  

**[3:26]** method fully in the IDE and I'm going to show 
you how to do that today. Really quick though,  

**[3:31]** we have the analyst, right? And then it's going 
to go to the product manager which we will then  

**[3:37]** go to the PO and then we will come down to the 
development phase. But take your time really  

**[3:44]** understanding this. It might look complicated but 
it's actually a very simple flowchart. This is if  

**[3:50]** you want to use the BMAD method for a brownfield 
or green field development to take it from  

**[3:54]** ideation all the way to actually developing it in 
the code. Right now you see the only thing I have  

**[4:00]** here is the BMAD method. Now, you do not have you 
do not have to install the full GitHub repo BMED  

**[4:06]** method locally. You will only clone that if you 
want to create your own expansion packs or maybe  

**[4:14]** make changes to the core system or contribute 
to the project, which I would love by the way,  

**[4:18]** but you don't need to do that. I'm going to show 
you how to use the BMAD method in cloud code  

**[4:23]** without even cloning the GitHub repo. So, first of 
all, let's um create a project. But what we can do  

**[4:31]** is from any directory. I suggest doing it from the 
dev directory. We are going to type npx and then  

**[4:37]** we're going to type bmad- method install. We are 
going to use the bad method 4.33.1. We will just  

**[4:44]** hit enter to accept that. Let's enter the full 
path of our directory. Since we're in the dev  

**[4:49]** folder, I'm just say dot meaning this folder. And 
then I'm going to say slash. And now I'm going to  

**[4:54]** put the name of the new directory that I want to 
create my project in. Since we're doing this from  

**[4:59]** scratch with no starter project, I'm just going to 
say simple to-do. That's the name of our project.  

**[5:06]** Just a very simple to-do application. And hit 
enter. It's fine if that directory doesn't already  

**[5:11]** exist. If you're doing this in a brownfield 
or if you already have started your project  

**[5:15]** maybe with a template, you'll just give it the 
directory to your project and it will add this  

**[5:21]** to an existing project. So then right here, this 
is a multi select, but we're just going to go with  

**[5:26]** the default and select the BMAD core. The BMAD 
core is the agile workflow AIdriven that we're  

**[5:34]** showing here. So just hit enter. And then we are 
going to shard the PRD, which means we're going  

**[5:40]** to generate a large document, but then we're going 
to split it up into smaller pieces. So just accept  

**[5:45]** the default here. And then the same thing with 
the architecture. The architecture file can be  

**[5:50]** very large depending on what type of project 
you're building. And so you'll want to shard  

**[5:55]** the architecture into smaller documents and this 
is all automated. I will show how this works. Um,  

**[6:00]** but that is really going to help you maximize the 
context in your agents so they only load what they  

**[6:07]** need instead of having to load and read through 
a whole massive file. They'll know which files  

**[6:11]** they need in the moment to load and it will help 
them with their context. So we'll say yes to that.  

**[6:17]** Now, here's a warning and this is just pointing 
out this is also a multis select. You can select  

**[6:22]** one or multiple IDEs that you want to install 
to. For example, let's say that you are a fan of  

**[6:28]** cursor and cloud code. Well, you can hit spacebar 
and cursor and spacebar and cla code. Today, I'm  

**[6:35]** just going to be doing this in vanilla VS code. 
So, I am only going to be using cloud code. So, I  

**[6:40]** have highlighted cloud code with the radio button. 
Make sure that you actually spacebar to hit the  

**[6:45]** radio button. And if you just highlight it like I 
have right here right now and hit enter, this will  

**[6:50]** actually not install it for any idees. Uh, one 
other quick tip is depending on the size of your  

**[6:55]** screen, you might not see all of these options 
here. So, just know that you can arrow up and down  

**[7:00]** and more options will appear and we're constantly 
adding more idees for support here. Hitting enter.  

**[7:06]** And now this is asking if we want to include the 
pre-built web bundles. The web bud the web bundles  

**[7:12]** are not needed for working in the IDE. This is 
kind of warning us in case we thought it existed  

**[7:18]** and we typed in the wrong directory. For example, 
you know, we could choose a different directory  

**[7:22]** location or we could cancel and start over. But in 
this case, we're going to say create the directory  

**[7:27]** and continue. Okay. So, if we scroll up here, we 
can see what did it do here. It installed some  

**[7:34]** commands for cloud code. So, these slash commands 
will be how we activate our different agents.  

**[7:41]** And then we've also installed some commands and 
these are great because sometimes we want to do  

**[7:46]** something without necessarily invoking an agent. 
We are now done. That is the install of the BMAD  

**[7:52]** method. I know it took a few minutes to explain it 
because I was going through the options, but let's  

**[7:57]** see how fast this literally is. I'm going to do 
it one more time. I'm going to do n px vad- method

**[8:07]** install. And I'm just going to give this a 
different folder this time. So I'm just going to  

**[8:12]** say uh let's say dash demo one, right? Just demo 
one. Enter. Enter. Enter. Enter. Select my IDE.  

**[8:22]** Enter. Enter. Enter. Boom. That's done. 5 seconds 
and you're ready to go with the BMED method. It's  

**[8:29]** really that simple. All right. And just to see 
that our two projects are there. If we do ls, we  

**[8:35]** can see that we do have the demo one, the one we 
just did, and also simple to-do. Simple to-do is  

**[8:39]** the project we're going to use. So, I'm just going 
to do rm-rf demo one. We do not need that anymore.  

**[8:46]** And now we can see that we have our simple 
to-do. So, I'm going to go into simple to-do

**[8:55]** and I am just going to open up uh VS Code. Now, 
right now we have no project here, right? All  

**[9:01]** we have is what we've installed for our agents 
under BMAD and our custom tasks or commands for  

**[9:10]** cloud code. And then we have the full BMAD core 
system here. Before we go on, I do want to say one  

**[9:16]** other thing though, and that is I want to thank 
everybody that has actually taken the time to  

**[9:21]** buy me a coffee. I've talked to a few of you and 
just know how much it really means for supporting  

**[9:28]** me and the BMED method and the community here. 
So, I want to thank everybody that's come and  

**[9:34]** supported the BMAD method. And if you would 
like to uh you can go to buy me a coffee,  

**[9:39]** look for BMAD code or the link in the description. 
Any amount helps and I truly thank all of you. I  

**[9:45]** like to use claude code in the terminal inside 
VS Code, but it doesn't matter if you use claude  

**[9:51]** code outside. You could use it inside the 
warp terminal or your own external terminal,  

**[9:57]** uh, you know, T-Max or anything, whatever you want 
to use, but I just find it convenient to kind of  

**[10:02]** keep it all in here. It's easy to, you know, just 
have the, uh, keyboard shortcut to show and hide  

**[10:07]** the terminal. Um, but we have no other project, 
right? So, as always, if you've used cloud code,  

**[10:13]** you should know how to do this. You just want to 
type claude. And we are going to launch Claude  

**[10:18]** Code. Of course, you will have to have installed 
Claude Code and set up your authentication,  

**[10:23]** but I'm assuming you've done that. If not, go to 
the Cloud Code website, see how to install it,  

**[10:29]** figure out whether you're going to do the $20 
plan on the 100 or the 200, and then you're  

**[10:33]** ready to go. Oh, by the way, I have been talking 
to a lot of people that have just been using the  

**[10:38]** $20 version of Claude Code. If you're fine not 
having the sonnet, excuse me, the opus model,  

**[10:45]** the $20 clog code will actually get you very 
far depending on how much you're doing. Uh,  

**[10:50]** so just say yes, we do trust this folder. This is 
the first time we've opened this in a project. You  

**[10:56]** could run the slashinit command, but I'm not going 
to do that yet cuz there's not really anything in  

**[11:00]** this project for it to know about. After we build 
a little bit of our project and get some stuff in  

**[11:06]** place, that's when I would do clait. Well, if 
we go back to the diagram, we can see that the  

**[11:14]** first person or the first agent that we want to 
talk to is the analyst because we're going to do  

**[11:19]** some brainstorming. And if you just hit slash, 
if you selected cloud code in the installation,  

**[11:25]** you're going to see all these all these options 
here. And if you don't want to arrow through this  

**[11:29]** list, what you can do is you can just start typing 
the part of the name of the agent that you want.  

**[11:36]** So, for example, analyst, you can just start 
typing it like that and it will highlight it.  

**[11:43]** Or if you know what it is, you can just type 
the whole thing or you can arrow up and down  

**[11:48]** to the one that you're looking for. So, here's the 
analyst. So, we're going to select it. This is how  

**[11:52]** simple it is to use clawed code with the BMED 
method. You saw it takes 5 seconds to install,  

**[11:58]** maybe 10 seconds if you want to read everything. 
So, this is Mary, our business analyst. I know  

**[12:03]** a lot of people think the power in the BMED 
method is in the development of actual code,  

**[12:12]** but I think Mary the business analyst is probably 
the most special agent in the whole BBA method.  

**[12:20]** If you are just trying to think of something to 
build or maybe you have a little bit of an idea,  

**[12:26]** I really strongly suggest that you try using this 
business analyst with the brainstorming method.  

**[12:33]** This goes beyond software development. You can use 
this for any type of brainstorming, whether it be  

**[12:39]** in your day job or, you know, life questions. 
I've tried many different brainstorming tools,  

**[12:46]** including professional brainstorming tools that 
have been developed by Google. For example, in the  

**[12:51]** Gemini gems, there is a default brainstorming gem 
that you can use. It's it's nothing like this. So,  

**[12:58]** you know, let's let's do that. So, we're talking 
to Mary right now. Mary is active. As always,  

**[13:03]** you can do star help. And so, now these are all 
of the different things that are available to  

**[13:07]** you. Now you can either select a number or you 
can type out the name of the command or you can  

**[13:16]** rely on the fuzzy matching and usually the LLM 
will get it right. So I'm just going to select  

**[13:22]** number five though which means brainstorm and I'm 
not going to give it a topic. I'm just going to  

**[13:27]** say number five. Even though Cloud Code supports 
a context window that seems to allow you to go  

**[13:33]** on and on and on without ever getting close to 
compaction, that doesn't mean you should. So,  

**[13:40]** when we're done with the analyst brainstorming, 
it will give us a brainstorming document. It will  

**[13:45]** save it to a folder called Docs, I will start a 
new chat. I like to start a new chat every time  

**[13:53]** I have an output document, then I'm ready to go. 
So, even if I'm going to talk to the same agent,  

**[13:58]** I will clear Claude or start a new Cloud session 
and then reload that agent and start going. So,  

**[14:04]** here we go though. We're going with uh Mary and 
first she's going to ask us four questions. So,  

**[14:09]** we are going to use our Super Whisper. What What 
is this brainstorming about? I would like to  

**[14:14]** create a simple to-do app to demonstrate the BMAD 
method. So, this should be a very simple NodeJS  

**[14:22]** background application. But what I really want 
to brainstorm about is some of the ideas we can  

**[14:27]** do to at least make it a little bit interesting. 
So let's play some of your brainstorming games  

**[14:32]** and see what we can come up with. So we'll let it 
spit all that out. So question two, are there any  

**[14:36]** constraints or parameters that I should know 
about? Well, I already mentioned that we're  

**[14:40]** using Node.js and I want this to be a very simple, 
straightforward small project just to demonstrate  

**[14:45]** the BMAD method with Node.js and TypeScript and 
then we will submit that. So this is how you work  

**[14:50]** with the agent. One of the magical things about 
the BBN method is it not it is not just like a  

**[14:55]** taskmaster or some of these other things where you 
just throw out your idea and then it does all the  

**[15:00]** thinking and working for you. As a matter of fact, 
what you're going to see with this brainstorming  

**[15:04]** is it is actually going to push on you to get your 
ideas out. It is going to be your coach. So that  

**[15:11]** is what is special about this. It is not checking 
your brain at the door and doing it all for you.  

**[15:17]** It is going to work with you and it's going 
to bring the best out of both of you. The  

**[15:22]** BMAD method, by the way, is all about elevating 
yourself, learning, and also elevating the LLM.  

**[15:29]** So, as a whole, you are both better collectively 
than each one on its own. That is the special  

**[15:35]** sauce of the BMED method. That's that's the secret 
everybody. Are we aiming for broad exploration of  

**[15:41]** possibilities or more focused ideiation? Let's go 
broad. Let's go crazy. I want to show just what  

**[15:46]** you are capable of as the amazing brainstorming 
agent that you are. Nothing wrong with flattering  

**[15:52]** your LLM every once in a while. They're sure going 
to do it to you. Yes, definitely. And that is also  

**[15:59]** the default. But when we're done here, this 
will take all of our brainstorming and give us  

**[16:03]** this amazing artifact. This is one of the coolest 
artifacts in one of the most recent additions to  

**[16:08]** the BMAD method. This was not even in the original 
release of V4. I thought this would be a V5 thing,  

**[16:15]** but I love the brainstorming document output, 
and I think you'll love it, too. We haven't  

**[16:20]** gotten to the brainstorming yet, but here 
we go. You have four options here again. So,  

**[16:24]** you can pick the techniques, and there's a whole 
list of 20 brainstorming techniques built into the  

**[16:28]** BMED method, or you can let the agent recommend 
it based on your project. Or you can do random  

**[16:34]** creative chaos. This one is fun. You never know 
what it's going to get, but sometimes it picks  

**[16:39]** some of the wackiest ones. or the progressive 
creative journey where we start super broad with  

**[16:44]** wild what if type scenarios and there's five of 
those and then gradually go down to focus. I just  

**[16:52]** want to show you all of the different options that 
we have here. So let's go to number one this time.  

**[16:56]** All right, so here we go. You can see that there's 
quite a few here and there's actually more coming  

**[17:01]** in the future. So we have what if scenarios, 
analogical thinking, reversal inversion,  

**[17:06]** first principles thinking, structured frameworks 
such as the scamper method, the six thinking hats,  

**[17:13]** mind mapping, collaborative techniques such as 
from the improv world, there's yesand, there's  

**[17:18]** brainwriting, roundroin, random stimulation. 
There's deep exploration with the five W's,  

**[17:24]** a classic brainstorming technique to really do 
a root cause analysis. There is morphological  

**[17:30]** analysis, advanced techniques such as forced 
relationships, assumption reversal, role-  

**[17:36]** playinging, timeshifting, resource constraints, 
metaphor mapping, questiontorming. But with the  

**[17:41]** power of the BMAD agent, Mary here, she's going to 
guide you through these and help you come up with  

**[17:46]** stuff that you never even probably imagined. 
You're going to see how with brainstorming,  

**[17:51]** we can even make a to-do list super interesting 
and exciting. If we would have selected one of  

**[17:56]** the other techniques up here, those also involve 
multiple selections from here and it will work  

**[18:03]** through each of them one at a time. Usually 10 
to 15 minutes is what it takes for each one.  

**[18:09]** So this can be a lengthy process, but look, 
if you're at the beginning of embarking on a  

**[18:14]** really large project or you have some ambitious 
ideas, it is worth doing this brainstorming to  

**[18:19]** really come up with, you know, super creative just 
interesting ideas. take the time here to build for  

**[18:26]** the future. Let's just pick a couple. Somebody 
in the community was suggesting that they would  

**[18:31]** love to see six thinking hats and also the five 
W's built into the BMAD method. And then they  

**[18:38]** realized that they were actually already in here. 
So just for them, I'm going to select number six,  

**[18:45]** the five W's. So we'll do 11. Uh let's do role 
playing. Role playing's always fun. So now the  

**[18:51]** agent will remember our choices and it's going 
to work with us one at a time. And remember here,  

**[18:56]** we are not asking Mary to brainstorm and come up 
with this for us. She's going to guide us through  

**[19:02]** this exercise. This is your own personal coach to 
brainstorm on complex, creative, or interesting  

**[19:09]** ideas. Folks, this is worth I don't even know 
what. You know, you can pay experts to teach you  

**[19:16]** how to brainstorm or be your brainstorming coach 
and it's going to cost you thousands of dollars  

**[19:20]** and you're getting this for free and we're doing 
all of this in claude code. So, this is amazing.  

**[19:25]** So, okay, what do we got here? Well, excellent 
choice. So, first we're going to start with the  

**[19:29]** first selection number six, which was the six 
thinking hats, five ways, and then roleplaying.  

**[19:35]** This is going to generate some seriously creative 
ideas. And again, this does not have to be about  

**[19:40]** apps. You can brainstorming about everything. 
Maybe you want to brainstorm ideas for a vacation  

**[19:45]** or brainstorm how you're going to retire in 10 
years or brainstorm, you know, what you should  

**[19:51]** do with your life or how you should unscrew 
up something in your life. I mean, this can  

**[19:56]** be used for anything. It is amazing. But, okay, 
so what are we going to do here? White hat. So,  

**[20:02]** the six hats, there's going to be six different 
colored hats. So, the first hat is the white hat.  

**[20:07]** What factual elements could make your to-do app 
interesting from a technical data perspective? So,  

**[20:14]** think about it. What kind of data could it track? 
What metrics, what information could it capture  

**[20:20]** that most to-do apps ignore? So, I would have 
never asked myself that question on my own. And  

**[20:26]** I'm already thinking now, wow, I was just thinking 
a simple to-do app from the white hat perspective.  

**[20:30]** It's now getting me to think about some really 
interesting aspects of a to-do app. So again,  

**[20:36]** there's no right or wrong answer and I don't 
even know if I'm going to come up with anything  

**[20:40]** interesting. This is not the actual product that 
we're going to create. We're just throwing ideas  

**[20:44]** out there. When we get the report at the end of 
all of this, it's going to help us distill down  

**[20:49]** what is interesting to then go to the next agent 
with. I think it could track how much time elapses  

**[20:56]** between when they enter a to-do and when they 
mark it done. Also, it would be interesting to  

**[21:02]** correlate the length or size of to-dos and the 
complexity of the to-dos and how that affects  

**[21:09]** how soon the to-dos get done. I love using Super 
Whisper, by the way, or Whisper Flow or one of the  

**[21:15]** other many voice to text ones. So, I'm just going 
to say yes. And one nice thing about working with  

**[21:20]** clawed code in the IDE is that as you work through 
each section of whatever whatever document you're  

**[21:27]** working on, it will start creating the document 
for you. So you don't have to worry about being  

**[21:33]** lost if you if you lose the chat, for example. 
I know sometimes there's anxiety when working  

**[21:37]** with the web agents that you might lose it and 
it's hard to get the full document out, but here  

**[21:42]** you're building up the document as you go. And we 
already have our brainstorming sessions here now.  

**[21:47]** Not too worried about what's in there yet. We're 
just going to keep going. So now we've gone to  

**[21:50]** the second hat. This is the yellow hat. Optimistic 
benefits. So look friends. Um this would take too  

**[21:55]** long to go through all of the brainstorming. So 
I'm going to go through all three brainstorming  

**[21:59]** techniques. All right. And look at this. We got 
our brainstorming session complete. We did all  

**[22:03]** three exercises. Let's now look at the document 
that it produced. So we will go to open preview.  

**[22:08]** This is actually going to give us the output 
and keep a record of the brainstorming that we  

**[22:11]** did. So first we did six thinking hats. critical 
concerns, creative alternatives, and we found some  

**[22:17]** fun ones in there. And then we went into process 
control. So, it really got me thinking about a lot  

**[22:22]** of different interesting things. This led to so 
many different things. Then we did the five W's.  

**[22:26]** The five W's was a lot of fun. The first why is 
why is complexity completion correlation valuable?  

**[22:32]** And then I gave it an answer. And the answer was 
because people consistently underestimate how long  

**[22:38]** complex tasks take. And the way the five W's works 
is then it's going to say okay well why does that  

**[22:45]** or why is that the case and then I gave an answer 
and then it's gonna say well why is that the case  

**[22:50]** why is that it's a way to really dig down in a 
somewhat annoying way but it's kind of fun doing  

**[22:54]** it with the AI so then we get into technique three 
which is role playing this is one of my favorite  

**[23:00]** because the AI will just invent some sort of role 
playing and you never know what it's going to give  

**[23:06]** you so here I came up with the overwhelmed 
freelancer the context is You're juggling 12  

**[23:11]** clients, 47 open tasks. You have a current to-do 
app, multiple of them, making matters worse. So,  

**[23:19]** how do we triage intelligence? Show me what 
actually needs to happen today versus what  

**[23:23]** I think needs to happen. Client workload balance, 
visual dashboard showing task distribution across  

**[23:29]** clients to prevent overcommitment. Imagine the 
project that you really want to launch in the  

**[23:34]** market and what this brainstorming agent can 
do for you. This is next effing level. Okay.  

**[23:41]** And then it gave us more because I wanted to 
do more brainstorming. So, we didn't just start  

**[23:45]** with the overland free overwhelmed freelancer. 
We talked about the perfectionist student and  

**[23:51]** what they would get out of a to-do app, the 
executive assistant, the ADHD creative. So,  

**[23:57]** I wouldn't have even necessarily thought of all 
those personas. uh the analyst Mary helped me come  

**[24:02]** up with these different role playinging scenarios 
and we talked back and forth and then it gives us  

**[24:06]** an executive summary because okay so it's great so 
we did all those things we're not going to use all  

**[24:10]** of that right it then we kind of talked about what 
was important to me and I kind of like gave it  

**[24:15]** some of the key insights and we came up with some 
of these key insights together transforming from  

**[24:19]** task management to behavioral intelligence your 
simple to-do app becomes a personal productivity  

**[24:24]** research lab that helps users understand their 
actual work patterns versus their assumptions  

**[24:30]** Tell me that is not powerful. And that is again 
just from like let's brainstorm about a to-do  

**[24:35]** app and this is what we came up with together. And 
now here's what's really cool is it breaks it down  

**[24:40]** into what can we do right now? What might we want 
to research and do in the future and then what are  

**[24:46]** like the moonshots or just the creative ambitious 
things we want to do later. And again this could  

**[24:51]** be like any aspect of your life. So use this 
use this in your personal life use it for work.  

**[24:58]** You can see now just how powerful the BMAD method 
is and you don't even need to be in the web. We're  

**[25:03]** doing this all with cloud code. And as a matter 
of fact, this is just on the cheapest model for  

**[25:07]** claude code. If I do slashmodel, you can see that 
I'm just using sonnet. I'm not using opus and I'm  

**[25:14]** not using the default. I'm just keeping it on 
set. You'll learn over time which model to use.  

**[25:19]** It's kind of an intuition that you'll develop. And 
trust me, even if you don't consider yourself a  

**[25:24]** strong developer or if you're new to this, you'll 
pick it up. You'll understand. It's it becomes  

**[25:30]** very intuitive to know which model to use. So, I 
would recommend though just so you can learn that.  

**[25:35]** Keep it on sonnet for most things. We are done 
with this. We've saved everything to a document.  

**[25:42]** This is the most important thing with the workflow 
in cloud code or really any agentic IDE that  

**[25:47]** you're using. we are going to start a new task 
with either the same agent or a new agent. So what  

**[25:53]** are we going to do? We're going to stop clear the 
context or if you don't want to clear the context  

**[25:58]** and keep that conversation history for later, 
we'll just kill the window, start a new one,  

**[26:04]** and restart Claude. Now, you might not know this 
if you haven't used Claude before. Let's say we  

**[26:09]** close this and then we realize, oh, we're not 
done with the conversation that we were just in.  

**[26:14]** If you hit slash and just hit the up arrow a few 
times or type slashres, you can now see the chat  

**[26:21]** that we were in here before. So if you've 
had multiple chats, you'll see a list here.  

**[26:25]** There's only one right now. If you highlight 
one in blue in this theme, if your theme,  

**[26:30]** it might be a different color. And now we're back 
in the chat that we were. So that is how you get  

**[26:35]** back to a previous chat. But we want to start a 
new chat. So again, I'm going to just close that.  

**[26:40]** I could have done slashcle, but I want to retain 
it. So, I'm just going to do cloud again. And now  

**[26:45]** we're going to start a new chat. Now, we're still 
going to talk to the analyst in this case. And now  

**[26:49]** I want to show you how to talk to the analyst to 
do basically the most important thing out of the  

**[26:55]** analyst that you really want is the project brief. 
Uh, by the way, the analyst is a totally optional  

**[27:01]** thing. You don't have to do brainstorming. You 
don't have to do a project brief. It is something  

**[27:05]** that you can do. Again, it really depends on 
the complexity of your project and how much you  

**[27:09]** already know. If you if if we were just doing the 
simplest to-do app, I would go right to the PM,  

**[27:15]** create a PRD for a simple to-do app. You can go 
right from PRD with its epics and stories directly  

**[27:21]** to development. I will show all of that in the 
A to B full walkth through, but right now I just  

**[27:27]** want to continue showing you this basic path of 
using cloud code. So, we're going to select number  

**[27:31]** two right now. And this is now going to help 
us create a project brief. And you'll see right  

**[27:35]** there it loaded elicitation methods. That is one 
of the other big awesome things that's built into  

**[27:41]** the BMED method. The BMAD method is built up of 
YAML templates which have two things. Basically,  

**[27:47]** the outline of the type of document, but more 
importantly, and this is what makes it, I think,  

**[27:52]** more powerful than any other method I've seen 
so far, but other people are starting to catch  

**[27:57]** on to these ideas. Embedded in the template 
is instructions for the LLM and how it should  

**[28:03]** work with you. Because as I said a little bit 
ago, the beauty of the BMAD method is not that  

**[28:09]** you ask it for something and it spits out a whole 
document, but that it really works back and forth  

**[28:14]** with you coming up with the best possible thing 
that you guys can come up with together. So,  

**[28:19]** first it's asking, do we already have any existing 
brainstorming results? Market research. Sometimes  

**[28:25]** it's best to look out in the marketplace, see 
what's out there, and build your own version of  

**[28:29]** it, maybe with your own twist. It's a big market 
out there. So don't feel like you always have to  

**[28:34]** be the first to market with anything. So maybe 
you want to do market research and see what is out  

**[28:39]** there or do a competitive analysis and see what 
your competitors are doing differently. But what  

**[28:44]** we're going to do is we're just going to take our 
brainstorming. We're going to drop it here and say  

**[28:48]** here's our brainstorming session results. We can 
use this to kickstart our work in interactive mode  

**[28:55]** in creating the project brief. You don't have to 
use these exact words by the way. So don't don't  

**[29:00]** you don't have to memorize the exact words. Talk 
to this as if you were talking to your business  

**[29:04]** analyst. Now this is going to kickstart it. So 
the nice thing here too is we started a new chat,  

**[29:08]** but you're seeing because we saved it to a 
document. I'm able to use a brand new context.  

**[29:13]** It's not getting polluted. It only has the output 
from the brainstorming session. And so it just  

**[29:18]** keeps it lean. And so now it's going to ask us 
some questions. It's going to pull things out  

**[29:22]** of our brainstorming and probably get us through 
the PRD a little bit quicker than normal because  

**[29:29]** you can see here, for example, it already knows 
what the executive summary is because we've told  

**[29:33]** it when we were doing the brief. I am only going 
to show this first section and then I'm going to  

**[29:38]** finish the document and then we'll move on to the 
PM. What you can see is after you complete the  

**[29:44]** executive summary, this is just one part of the 
overall brief by the way. It already figured some  

**[29:48]** stuff out from our previous brainstorming. we can 
correct it or we can tell it to change things. So,  

**[29:51]** you'll want to read this and obviously work with 
it. But at the end of each section, you're going  

**[29:56]** to have multiple options. These are called 
advanced elicitations. Whether you're working  

**[30:02]** with the PM or the architect or the business 
analyst right here, every section of a document,  

**[30:08]** most of them will ask you different advanced 
elicitations related to the document you're  

**[30:12]** working on. Now, unlike brainstorming where it's 
asking you, the user questions, this is where  

**[30:19]** another powerful aspect of the BMAD method kicks 
in, and I haven't talked a lot about this before,  

**[30:23]** so this is very important, but this is where 
you push on the LLM to do better. When you talk  

**[30:28]** to any LLM, whether you're just using the BMAD 
method or not, or you're just using Chat TBT,  

**[30:33]** if you picture a bell curve, you know, you're 
kind of getting the average slice of the entire,  

**[30:39]** you know, corpus of information in the LLM. It's 
giving you the average response. It's, you know,  

**[30:44]** not necessarily great. It's not necessarily 
weak. The advanced solicitation is your chance  

**[30:50]** to really stick the cattle prod to the agent 
and say, "Do better. Make sure that you have  

**[30:55]** put this through the fire and you're giving me 
the best possible result." Challenge the scope.  

**[30:59]** We can force it to brainstorm. So, just like 
it was having us brainstorm, we can now turn  

**[31:03]** the torture back around on the LLM and have it 
brainstorm different ideas. There's actually  

**[31:08]** many more advanced elicitations. Again, just so 
it doesn't overwhelm you, it's just giving some  

**[31:13]** of them. Please do number four and number five. 
And by the way, while we're waiting for that,  

**[31:18]** notice that it did already start our brief. This 
is our project brief. So again, the beauty of  

**[31:23]** doing this in the IDE with cloud code is that we 
are generating the documents as we go. But first,  

**[31:30]** it did critical assumption testing. So, it's 
basically, by the way, this is just another great  

**[31:38]** thing to do with any product idea that you have. 
And so, I love that the LLM thought about this.  

**[31:43]** Look at all of your ideas for your product and 
really stress test them and make sure that they  

**[31:49]** make sense, especially if you want to build an MVP 
first to just get something to market. And then we  

**[31:55]** also did explore alternative solution approaches. 
So at the very end of it, it kind of synthesizes  

**[32:00]** everything and it gives some recommendations based 
on what it was doing with itself right there.  

**[32:05]** Sure. This is just a demo. So we're just going to 
apply them all, update the section, and then we'll  

**[32:10]** move on to the next section of the product brief. 
Let me say please uh subscribe to the channel if  

**[32:15]** you're enjoying this. So much more content is 
coming out, my friends. You know, I know these  

**[32:19]** videos don't come out as often as I would like to 
because I'm also constantly working on actually  

**[32:23]** improving the BMED method. I'm not here to just 
hype up new things, new products, or, you know,  

**[32:29]** even tell you I'm using this, but I do want to be 
able to use this forum or this platform to share  

**[32:34]** the changes with you. But also, I spent a lot of 
time actually working on this. But subscribe to  

**[32:39]** the channel, hit that notification bell so you do 
know when the next one comes out because it is a  

**[32:43]** little sporadic sometimes. And join us in the 
Discord. I'm going to finish this up. We will  

**[32:48]** look at the whole product brief when it's done, 
and then we'll move on to the product manager.  

**[32:52]** All right. So, I'm going to pick up the pace here 
a little bit. We are done with the brief. We've  

**[32:57]** gone through the whole thing. The brief is now 
ready for the PM handoff. So before we do that,  

**[33:02]** I just want to show here's our product brief. 
Since we're in cloud code and not in the web, it  

**[33:07]** just keeps updating the document for us. We have 
the executive summary, the problem statement, pain  

**[33:13]** points, why we're doing this, what is the proposed 
solution, the target users. So this says like the  

**[33:19]** demographics, who do we expect to be using this? 
Why would they use it? How are they each going  

**[33:24]** to use it differently? And why is it valuable 
to them? This is so important. If you're just  

**[33:29]** wanting to put any kind of product in the market 
and you're just thinking you're just going to vibe  

**[33:35]** vibe code something, throw it out there and be 
an overnight millionaire. Maybe you will be, but  

**[33:40]** you have to consider all these things. You have to 
understand the target audience that you're looking  

**[33:45]** for. So that's the beauty of this product brief. 
It's going to really help you figure out a lot of  

**[33:49]** that and make sure you're building something that 
makes sense or might indicate that you want to  

**[33:54]** pivot on something because it's not actually going 
to achieve what you want to achieve. Why waste a  

**[33:59]** lot of money, effort, and time building something 
that's not going to go anywhere when instead  

**[34:04]** you can do this little bit of research up front, 
right? So, we're showing this this whole document.  

**[34:08]** The point of the product brief is to really work 
back and forth with it and produce this document  

**[34:14]** that helps you understand what it is you're going 
to build at a most fundamental level. As always,  

**[34:20]** what did I say? Even in cloud code, even though 
we could go on and on and probably talk to three  

**[34:24]** agents in a row without running out of context, 
we're still going to start a new one. So again,  

**[34:30]** we can just kill it and start a new cloud session. 
I'm going to show you a different way this time  

**[34:34]** and that is just slashcle and this is going to 
clear the conversation history and free up the  

**[34:41]** context is it's it's basically the same thing. 
You could also do compact. I do not recommend  

**[34:46]** it. And if you ever see your IDE is showing you 
the warning that you're almost ready to start  

**[34:51]** compaction. That means that means you've been 
in the chat for too long and you probably want  

**[34:56]** to wrap up what you're doing. There's different 
techniques for what you for that to get out of  

**[35:01]** there, but you generally do not want to rely on 
compaction. It's just randomly going to forget  

**[35:08]** things that might be important. So, there's other 
techniques, but basically, if you follow my method  

**[35:13]** and you just switch and do clear, but sometimes 
you'll forget and all of a sudden you'll see that  

**[35:18]** warning and then, you know, you have to adapt. But 
let's um let's talk to the next agent. So if you  

**[35:24]** don't know what agent to talk to, again, you can 
go back to the diagram. So we've done this, right?  

**[35:30]** So we we talked to the analyst. We've done our 
optional brainstorming. We didn't do the optional  

**[35:35]** market research or competitor analysis, but you 
can try those on your own. It depends on what  

**[35:38]** type of project, but we did create our project 
brief. So now we are going to talk to the product  

**[35:46]** manager. And if we have a product brief, we're 
going to give it to the product manager. it will  

**[35:51]** actually ask us. So, I mentioned you might have 
a similar pro or a simpler project. And if you do  

**[35:57]** or you already know what you want to do, maybe 
you even already have a product brief, you can  

**[36:02]** just talk to the PM and it will just ask you more 
questions if you don't provide the brief. But if  

**[36:07]** you provide the if you provide the brief, it kind 
of gives it a kickstart and it will get the PRD  

**[36:13]** done much quicker. But it just depends what you 
want to work. Again, if you're just doing a simple  

**[36:17]** app, you don't have to go through all of this. 
just go right to the PM, create the PRD, even  

**[36:22]** tell it you want it to be a technical PRD with 
architecture built into it. You'll be coding in  

**[36:28]** no time. So there's multiple flows and workflows 
and ways you can work this system. But again,  

**[36:33]** come back to this diagram if you're not sure. 
So let's go back to cloud code. So now again,  

**[36:38]** I hit slash here. We could just type PM. That'll 
take us right to it. If we're not sure, we can  

**[36:43]** also just kind of look through here and then arrow 
on it. The product manager is going to basically  

**[36:49]** create a PRD which is a product requirements doc. 
Building a PRD is important and also I'll say the  

**[36:54]** three most important things with this PRD is first 
of all it's going to give us all the functional  

**[36:59]** and non-functional requirements and the epic 
that is made up to meet all of those. So right  

**[37:06]** there we can see everything that is going to be 
encompassed by the build that we're planning here.  

**[37:13]** Secondly, it's going to help work with us to 
figure out what is in scope for the MVP and what  

**[37:18]** we can potentially pull out to have post MVP. 
Because if you can make your app the simplest  

**[37:24]** version of the app that you can make that will 
meet the initial goal, that's less risk, less  

**[37:31]** investment in a product. Maybe you want to get 
it out there with just a minimum set of features  

**[37:35]** to test it in the market. That's why you want 
to build an MVP or minimum viable product. what  

**[37:41]** is the basic thing of this core? But the PM here 
will also capture your other ideas and if they're  

**[37:48]** not part of the MVP, we'll still hold on to those 
and those will be post MVP epics that you might  

**[37:54]** do after the main build. So again, what is most 
important here? It helps us maintain MVP scope.  

**[37:59]** It gives us the functional and non-functional 
requirements with the epics. And then the the  

**[38:04]** third most important thing, but really kind of the 
key to the whole BMAD method is in those epics,  

**[38:09]** it is going to create the user stories, but more 
specifically, it knows that we are creating these  

**[38:15]** for very, very dumb developer agents. Now, as I've 
said all along with the BMED method, you cannot  

**[38:22]** just check your brain out and leave it at the door 
and rely on it 100%. Right? So, we will use the  

**[38:27]** advanced elicitation. We will read the information 
ourselves and logically think to yourselves,  

**[38:33]** does the story sequence make sense. If you don't 
see a story, for example, that says scaffold and  

**[38:41]** you know, set up your project or set up your 
accounts or whatever you need, you know there's  

**[38:45]** a problem and something's been missed, right? And 
usually that should be the first one like project  

**[38:48]** setup. You know, learn to kind of spot those 
things as you go. And there's also some advanced  

**[38:52]** elicitations that will help us discover that. So, 
let's move on here. So, we are just going to do  

**[38:56]** create PRD. And I want to show you before we've 
been doing the number, we can also just say star  

**[39:03]** and we can actually just give it the command name 
also or you could even speak it. Uh do notice that  

**[39:07]** there are two Yep. There's two different PRDs 
here. There's the regular PRD and then there's  

**[39:14]** the brownfield PRD. Brownfield is a term that you 
will hear and you'll also hear green field. And I  

**[39:21]** realize some people don't know what that means. 
So I want to explain it and it's very simple.  

**[39:25]** Green field means like you're looking out on 
a clean green pasture. It's all open. Pretty  

**[39:32]** much sky's is the limit. It's going to be easy to 
build your foundation. Nothing is there. Nothing  

**[39:37]** in is in the way. A brownfield is where all the 
[ __ ] has flowed. It's a cesspool. Maybe it's an  

**[39:45]** existing application that's existed for months or 
years or it was developed by other people. Maybe  

**[39:52]** you understand it. maybe it has a lot of issues in 
there. If you're going to work with something like  

**[39:57]** that, then you'll want to follow the path create 
brownfield and that will have a few more steps in  

**[40:02]** it to also provided the context of the existing 
application that you might be working on. Number  

**[40:08]** two, we're just going to do a regular PRD. Now, 
the PM is asking us, okay, do we have the product  

**[40:15]** brief to create the PRD? So, again, this will 
kickstart us to the PRD. If you were starting  

**[40:20]** here, you would say no and you would just start 
asking its question or you could go back and do  

**[40:25]** it. But we're just going to drag it in because 
we do have the brief. And we'll say here you go,  

**[40:31]** buddy. There is a lot of overlap between the 
product brief and some of the sections of the PRD,  

**[40:39]** but it's really going to translate that from the 
language of the product brief into functional and  

**[40:44]** non-functional requirements and a few of the 
other details that we need in there. Okay. So,  

**[40:49]** let's see what we got here. So, it gave us some 
goals. So, it understands what we're trying to  

**[40:53]** build, why we're building it. We got some detailed 
rationale here. Tradeoffs made, key assumptions,  

**[40:59]** and areas needing attention. We have options 
to do advanced solicitation. And by the way,  

**[41:05]** I love this. Just like before, as we produce our 
document, we are going to generate each section  

**[41:11]** of the document one at a time. So, it's always 
going to have access to everything it's done.  

**[41:16]** It's going to he keep kind of a cohesive vision 
of the document we're building and it's going to  

**[41:21]** build it up section by section. Beautiful. I love 
this. Now we are doing section two. We moved on to  

**[41:27]** the next section. So this is the requirements. 
So this is going to give us the functional and  

**[41:30]** non-functional requirements. Take your time and 
read through this. Again, getting this right is  

**[41:35]** important. And you really want to try to look, is 
there a functional requirement here that you do  

**[41:40]** need or don't need. I want to show you my absolute 
favorite advanced elicitation to use here. Let's  

**[41:46]** see if it suggests it. But I want to show you 
how you can actually find what other advanced  

**[41:52]** elicitations are available for the BMED method. 
But what you can do is you can go to data. We're  

**[41:58]** going to go to data and here are the elicitation 
methods. We can see them here. So there's explain  

**[42:04]** reasoning, critique and refine, analyze logical 
flow, assess alignment with overall goals,  

**[42:10]** identify potential risks, challenge from critical 
perspective, tree of thought, deep dives,  

**[42:16]** hindsight is 2020, the if only brainstorm, 
agile team perspective shift. This will take  

**[42:22]** your different agents and have them all look 
at it from a different perspective. It's a lot  

**[42:26]** of fun. Uh stakeholder roundt, metaprompting 
analysis. So some of these are very correct.  

**[42:32]** uh very creative. Um and then we get into some of 
the new advanced 2025 techniques that have been  

**[42:38]** added in recently. Self-ont self-consistency 
validations, the rewoo, which is reasoning  

**[42:45]** without observation. I love that. Rewoo, persona 
pattern hybrid, emerging collaborative discovery,  

**[42:51]** red team versus blue team, innovative tournament, 
escape room challenge, proceed and no further  

**[42:57]** action. I want to tell you, I've done a lot of 
research into how to really prompt engineer and  

**[43:04]** get the most out of LLMs, and these are some of 
the best techniques that I've found from Google  

**[43:10]** and Anthropic. But I've also studied multiple 
prompting competitions where expert prompters  

**[43:15]** just compete, and I see a lot of them using 
some of these very cool techniques, and some of  

**[43:21]** these are just crazy fun. So, let's let's pick a 
let's pick a wild one. I like the what if if only  

**[43:28]** hindsight is 2020. So what I'm going to do is I'm 
going to just select this here. This is another  

**[43:33]** thing you can do. Eventually these will all 
just be in the menu at one time. Close this now.

**[43:42]** This looks at all your functional and 
non-functional requirements and then it  

**[43:46]** imagines that we've built the application and 
that we're I don't know sometimes it does six  

**[43:50]** months out sometimes it does a couple years out 
and it's an analysis where the LLM does this  

**[43:56]** conversation with itself reflecting on a board 
meeting or something else where people are like if  

**[44:02]** only we would have done this something would have 
happened. So let's see what it did here. Imagine  

**[44:08]** it's 6 months from now the MVP is launched. You're 
looking back at these requirements. What if only  

**[44:14]** statement might you be making? If only we had. If 
only we had included basic team sharing features  

**[44:21]** from the start. Non-functional requirement one 
might be unrealistic for bootstrap budget and  

**[44:26]** single developer. What if we hadn't promised cross 
device sync and MVP? Functional requirement 7 adds  

**[44:34]** significant technical complexity. What if we 
started with single device and added sync in  

**[44:39]** phase 2? So what's going on here? This is actually 
helping you figure out how to cut scope out of  

**[44:44]** your MVP. Keep it a lean lean build so you can 
actually get something to market. Get it tested  

**[44:51]** and then layer those features in later. This is 
the real agile way of product development. Super  

**[44:58]** powerful. So I'm going to say apply changes and 
update sections. Revise the requirements based on  

**[45:03]** these insights. Uh before you do that, you can 
talk to it. You can question different things.  

**[45:08]** You can tell it what you want to keep and not 
keep, but I'm just going to do number one for  

**[45:12]** purposes of time. So, I'm going to finish this and 
I'm going to get this up to the epics and stories  

**[45:17]** and then we'll continue together. There's only one 
epic right now because I told it just CRUD. So,  

**[45:22]** foundation and core CRUD operation establish the 
project setup. As I said, always kind of look  

**[45:27]** out for that, right? Uh we are going to have local 
database. So, it'll do the database initialization  

**[45:32]** and then implement all basic to-do management 
commands. add, list, complete, delete, update,  

**[45:38]** basic crud. So, since there's only one epic, 
it's going to go right into the stories here. So,  

**[45:44]** epic foundation and core. You'd want to read this. 
And as always, read the stories and acceptance  

**[45:49]** criteria and think, does it make sense? Is there 
something being called out that actually relies  

**[45:56]** on something later? This is great. This is how 
agile actually works in story breakdown is each  

**[46:01]** piece of functionality can kind of be its own 
standalone story. Can we list and search for the  

**[46:06]** to-dos? Can we mark a to-do done, delete a to-do, 
update a to-do? You can also ask it questions if  

**[46:14]** you don't see the one you want here and you don't 
want to look. So, I'm going to tell a deep deep  

**[46:17]** think please that the order and granularity of the 
stories actually make sense. The sequencing must  

**[46:24]** be perfect with no story dependent on a later 
story. It's checking to make sure that they all  

**[46:29]** follow the correct progression. You're absolutely 
right. Let's deeply analyze the story sequencing  

**[46:34]** and granularity as there are significant 
dependency issues in the current approach. So,  

**[46:40]** do we accept it? We'll say yes. So, does this 
sequencing now make sense? So, let's say yes.  

**[46:46]** All right. So, looks like Claude now thinks we 
have seven stories in perfect sequential order.  

**[46:52]** Do we believe that? Well, don't check your brain 
at the door. Let's close that though because we're  

**[46:56]** done talking to the PM for now. But you do want 
to, you know, go through your doc. Imagine this  

**[47:01]** is a big ambitious project with multiple epics. 
Do you really just want to accept some slop and  

**[47:08]** move on and start developing? Maybe. But I would 
suggest take your time and really understand and  

**[47:14]** try to learn from this. Ask the LLM questions. The 
LLM is not going to always tell you to do this.  

**[47:20]** The reason we have agents and personas is because 
it's to help you also have a mental model. Not  

**[47:26]** not only does it help the agents perform better 
and keep focused on their domain expertise and  

**[47:33]** you know tailoring responses to that persona 
that they're interacting, but it's also for  

**[47:38]** you to understand that as they are serving this 
role, talk to them as if they were in that role.  

**[47:46]** So, you're talking to a product expert or 
an architect or a scrum master. Ask them  

**[47:52]** why they're choosing things. What do different 
things mean? The beauty of this too is you don't  

**[47:58]** have to be embarrassed about asking questions. 
You can ask this what people might think is the  

**[48:03]** dumbest question. Look, maybe you don't know, 
maybe you've heard the word database before,  

**[48:09]** but you don't even know what a database is. Okay, 
you can Google it. It'll give you a definition,  

**[48:15]** but you could also just ask why are you using a 
database for a to-do app. It mentioned a name of  

**[48:21]** a database. You could ask it why did you select 
this database? Why not something else? And it'll  

**[48:26]** give you an answer. So, you can learn a lot 
just by talking and at any time you can just  

**[48:31]** ask the agent questions about this document or 
any of the documents we're going to do. Now,  

**[48:37]** we can start a brand new chat with the architect. 
So, I'm going to open up Claude again. So,  

**[48:43]** we're in the brand new cleared context. Nothing 
here. And if you're not sure, you can always clear  

**[48:48]** it again just to make sure. Now, we're going to do 
slashchitects. Now, again, this is a very simple  

**[48:56]** project. I would probably try to just go from 
PRD to stories. There is a workflow that supports  

**[49:01]** that, but I want to show you basically how the 
architect works. So, same thing. It'll either show  

**[49:07]** you the commands. If it doesn't, type starhelp and 
you can see what's available here. Now, here we  

**[49:12]** have a couple different architectures. Don't be 
confused, but it's pretty simple. You're either  

**[49:16]** going to do a full stack architecture, which is 
front end and backend, maybe is a monor repo,  

**[49:24]** which means all the code is in one project such as 
Nex.js, or maybe it is two separate repos and two  

**[49:30]** separate projects, React for your front end, 
and maybe a cloud service for your back end,  

**[49:34]** and maybe in two different GitHub repos. Um, you 
also might be starting with a starter project such  

**[49:41]** as NECJ, Nex.js with Superbase and Shad Saiyan and 
Tailwind. If you're doing that, you would want to  

**[49:49]** generate your project, get your boiler plate and 
share that with the PM or the architect. So, as  

**[49:56]** they're doing the architecture, they already know 
what you have, what your technologies are, what is  

**[50:02]** in your requirements.txt if you're doing Python or 
your package.json JSON if you're doing TypeScript  

**[50:08]** or JavaScript, Node.js, excuse me. Create full 
stack architectures if you're doing front-end  

**[50:14]** back end. Create backend architectures if you're 
just building like maybe a service project or  

**[50:19]** utility or anything that does not involve a web 
front end or a guey front end. The one exception  

**[50:26]** is you might have a CLI. You will still want to 
select create backend architecture. And then there  

**[50:33]** is a create front-end architecture. If you're only 
working on a web front end, maybe you're working  

**[50:38]** on a website or maybe you already have a backend 
REST API and you just want to build the React app  

**[50:43]** to call that REST API. That's where you would say 
create front-end architecture. And then finally,  

**[50:49]** our friend the brownfield is back. So we can 
create a brownfield architecture. And again,  

**[50:52]** that's going to involve a lot of the research 
that the analyst and the PM did to understand your  

**[50:58]** current project. Feed that into the architecture 
along with some of the challenges of architecting  

**[51:03]** against an existing project. Creating our backend 
architecture because we are doing what a to-do app  

**[51:09]** only in the CLI. It's just running in the command 
line for demonstration purposes. So, we'll hit  

**[51:14]** number two. Now, let me give you a tip on working 
with the architecture. Regardless of what actual  

**[51:22]** IDE or system you're using, you want to use the 
best model you can. I'm showing you that this can  

**[51:28]** be done in the $20 version of Claude Code, but I 
would recommend, especially on a more challenging  

**[51:34]** architecture, use Opus or whatever powerful model 
you have because you will get potentially better  

**[51:42]** results. Or do this on the web with Web Gemini. 
save your credits and then just get into the IDE  

**[51:48]** after we have our architecture. But I actually 
enjoy doing the architecture here because as you  

**[51:52]** can see yet again we are producing our document 
in real time as we go section by section. It gave  

**[52:03]** us a sequence diagram. It gave us some highlevel 
architecture. You know what we're doing with the  

**[52:07]** database, how we're going to handle error handling 
and global installation and uninstallation  

**[52:12]** process. Do we want to focus on any of these? We 
can do alternative analysis, stakeholder input,  

**[52:18]** risk assessment, resource impact, user 
experience impact, technical feasibility,  

**[52:24]** market validation. You know, read what it gave you 
and think about if any of these make sense or if  

**[52:29]** you want to do any of these. And if not, just move 
on to the next section. Also, question in this  

**[52:34]** next section what technologies it comes up with. 
Make sure it knows what the latest versions are  

**[52:40]** or what the best version is. You can also tell it 
to use the web to make sure that it's considering  

**[52:46]** the latest technologies for everything that it 
picks is this is going to create a table of all  

**[52:50]** the specific versions and technologies we're 
using. If you don't have this and tell it what  

**[52:55]** specific technologies, what what testing framework 
you're using, for example, what'll happen is later  

**[53:00]** on your LLM will be developing. It might be using 
justest just because it sees that it's already  

**[53:05]** scaffolded and then it'll run into a problem and 
instead of trying to fix it, it might be sneaky  

**[53:12]** and just try to install a whole new test framework 
without you noticing. It'll tell it but maybe  

**[53:17]** you're not paying close enough attention or you 
walk away and you come back and all of a sudden  

**[53:22]** there's a new test framework or there's another 
new package. And that's because it's not forcing  

**[53:27]** it to stick to any list. When we create this table 
here and shard this out to a separate document,  

**[53:32]** the dev agent later on will always be aware of 
this technology stack and will not diverge from  

**[53:38]** it. It's a very powerful technique to make sure 
your agents are all using consistent libraries,  

**[53:44]** packages, and versions. So, I'm going to 
go through the rest of the architecture,  

**[53:47]** but just remember section by section you really 
want to use the advanced solicitation. So let me  

**[53:52]** show you right now just one quick example example 
and then like I said I'm just going to kind of run  

**[53:57]** through the rest and we'll pick up at the end. So 
let's say in here doing data models. So this is  

**[54:01]** great because if it makes data models that means 
later on the agents they'll always conform to the  

**[54:06]** same model. And much like our technology stack you 
don't want them producing different models on the  

**[54:11]** fly. But let's say for whatever reason I don't 
understand why we're creating these or I don't  

**[54:20]** like them. So I'm just going to ask a question. 
And this is one thing you can do. You don't need  

**[54:24]** the prompt here always to ask just ask a question. 
So say explain to me the interfaces you created  

**[54:30]** and I want an explanation of why each one of them 
exists and are we missing any? So the architect  

**[54:36]** is programmed to also be very explanatory and 
explain in a very clear way meeting you at your  

**[54:42]** level. I recommend talking to all these agents. 
Even if you're not in the middle of a project,  

**[54:47]** you can load up these agents and just talk 
to them. talk at them talk to them about your  

**[54:51]** ongoing project. What did he tell us? He told us a 
lot. So, let me explain each type script interface  

**[54:57]** I created and analyze if we're missing any. So, 
the to-do interface that's obviously important,  

**[55:02]** but why it exists? Type safety. So in other words, 
an interface allows us to define a object or a  

**[55:09]** par or basically this would be like the blueprint 
for an object that we will create later and every  

**[55:15]** object must have a task string completed completed 
at and an ID to make it unique. Um so why does  

**[55:24]** it exist? Type safety. We just talked about 
that database mapping. So that's interesting.  

**[55:29]** So what that's telling us is he's setting up an 
interface here that will later also map directly  

**[55:34]** to the SQL light. So we always make sure we 
have the same properties and fields in our local  

**[55:38]** database. And it's also going to help us define an 
API contract. The API contract when it returns a  

**[55:44]** to-do is going to be guaranteed with each to-do to 
return these properties. So if we wanted something  

**[55:51]** else in our to-dos, now would be a good time 
to add it, not later on when we're developing.  

**[55:56]** So that's again why you want to actually pay 
attention and try to understand what the architect  

**[56:00]** is telling you. And if you don't, just ask it. 
And if you read this and you still don't ask it,  

**[56:06]** play five W's with it and ask it why you did this, 
why you did that, well then why did you do that?  

**[56:11]** Well, why did you do that? And on and on and on. 
Again, you can learn so much just by engaging in  

**[56:17]** discussions with the architect to really start to 
learn how software is developed in reality. It's  

**[56:24]** very powerful stuff. All right. Right. And so the 
uh architecture looks like it is done. We finished  

**[56:29]** the last section. It gave us the final summary and 
the document is updated. Let's just make sure that  

**[56:36]** everything is in the document. It's pretty large 
document which is why we shard these documents,  

**[56:40]** but we have our success criteria. Before we 
shard our documents, just like with the PRD,  

**[56:46]** you really want to go through here and make 
sure that everything makes sense, such as  

**[56:51]** coding standards. As a matter of fact, coding 
standards is one of one of the most important ones  

**[56:56]** because this will be used by the developer agent. 
Directory structure. You want to make sure that  

**[57:01]** this makes sense. If you want to render sequence 
diagrams, you can just rightclick in VS Code and  

**[57:07]** you can say open preview and then you should be 
able to see some of these nice looking renders.  

**[57:13]** If you do not have that option in VS Code or in 
Cursor or Windsurf or whatever you're in, you'll  

**[57:20]** want to go to your extensions, which is this icon 
here. These are our installed extensions. And  

**[57:26]** you'll want to make sure that you have something 
similar to Markdown all-in-one. I like this one  

**[57:32]** along with Markdown preview mermaid. This will 
give us mermaid documents or mermaid rendering  

**[57:39]** from this one. And the markdown all-in-one will 
also let us auto format markdown to make sure that  

**[57:44]** it's valid markdown. Here's our sequence flow. 
Make sure that the flow makes sense. Here's our  

**[57:52]** database schema. Again, if you don't understand 
something here, ask it. Ask it why I did this,  

**[57:57]** but this makes sense to me. Here's the source 
tree that it's going to produce. This controls  

**[58:03]** where the LLM is going to look for files, where it 
should put them when it creates them. And again,  

**[58:08]** we'll just help it stay on the rail. Having 
a source tree is a very important document  

**[58:13]** to keeping the LLM on track. I'm going to open 
up this and I'm going to show you how you can  

**[58:18]** just talk to the agent. In the coding standards, I 
really want to make sure that the developer agent  

**[58:23]** will use Gab will use good Java do style comments 
or JS doc style comments on all public functions,  

**[58:32]** public interfaces, etc. So, please add that to 
the proper section in our architecture under the  

**[58:40]** coding standards. Okay, that was a little bit 
wordy, but that's why I like using just the uh  

**[58:48]** speech to text because I can kind of work it out 
in my mind as I'm saying it and usually the LLM  

**[58:54]** can get it right and understand what I'm talking 
about. But this should now add some documentation  

**[58:58]** standards so we will have good consistent 
documentation. Now, now I'm good with this. Now I  

**[59:03]** think the document is great and we are done here. 
So now I'm going to close cloud code. I'm going to  

**[59:09]** close all our documents and let's look back at 
our project. We now have an architecture and a  

**[59:14]** PRD. The two key documents that we need. We don't 
really need the LLM going forward anymore. Looking  

**[59:20]** at the brainstorming or the brief. Every file that 
you keep here is potential context that the LLM  

**[59:26]** might choose to load. You can add restrictions. 
you can tell it not to, but it's better sometimes  

**[59:31]** to add these to another folder. So, you could 
add these to a project references file, or you  

**[59:36]** could just take them out and store them, or maybe 
you store them online, depending on how you're  

**[59:41]** organizing your project artifacts. But whatever 
you do, you don't want them to get pulled in and  

**[59:47]** polluting your context overall. Okay. So, we'll 
come back to Claude use the shard command. So,  

**[59:54]** if we just type shard, we will see that there's 
a task shard doc. And do we want to use the MD  

**[59:59]** tree? Yes, we do want to do MD tree. So, okay. 
So, now it's saying great, the MD tree command  

**[1:00:03]** is available. If it was not available, 
it would suggest that you install it. So,  

**[1:00:08]** now I need to know which documents you'd like to 
shard. Please provide the path to the document you  

**[1:00:13]** want to shard. And I'll use the MD tree explode 
command to automatically split it into smaller  

**[1:00:19]** documents based on level two sections. So, first 
of all, we want to do our PRD. So, I'm just going  

**[1:00:26]** to drag it in there. That's it. And the default 
should be a folder called PRD, which it is. And  

**[1:00:36]** look at that. It's already done. That's how quick 
it is. We now have our epic list. And here is the  

**[1:00:42]** most important one. Epic 1, epic 2, epic 3 if 
there were multiple with all of the stories  

**[1:00:47]** because this is what the scrum master is going to 
use to build up our stuff for our developer. So,  

**[1:00:52]** that is great. So now we can say do the 
architecture and we're just going to drag it in.

**[1:01:03]** So as you can see using the BMAD method in cloud 
code is super easy. We don't have to jump back and  

**[1:01:09]** forth to the web. It's super powerful and it just 
does a great great job at following instructions  

**[1:01:15]** regardless of which model you use in cloud code. 
Here's our architecture again just in seconds. And  

**[1:01:21]** now this is the one that is really good to shard 
because look we have coding standards which has  

**[1:01:27]** our documentation and some of our other stuff 
in here that we wanted with examples source  

**[1:01:32]** tree. So this shows us exactly what our project 
structure is going to look like. Text deck those  

**[1:01:37]** three are critical and I want to show you why so 
you understand this regardless again of which tool  

**[1:01:42]** you're using. If you go into Claude, since we're 
using Claude, we'll look at the Claude version.  

**[1:01:48]** And let's look at what the developer agent has 
here. The developer agent has a command on here  

**[1:01:54]** that basically tells it, look at BMAD core, look 
for the core config. And this is what tells the  

**[1:02:04]** developer agent what files it will load every 
time. So the way the developer agent works,  

**[1:02:08]** I've explained this before but I'll say it again. 
The scrum master is going to take the highle epic  

**[1:02:14]** and story. It's going to read through various 
architecture documents. It's going to understand  

**[1:02:19]** one story at a time and it's going to create a 
very detailed story for the developer, a lower  

**[1:02:25]** level developer story. This is a self-contained 
file for the developer to have all of the context  

**[1:02:34]** it needs to build the application. We talked a few 
videos ago ago about context engineering. This is  

**[1:02:42]** the core of context engineering. Giving the agent 
exactly what it needs to build its little piece of  

**[1:02:49]** the kingdom, right? But additionally, not only 
is all of this information the scrum master is  

**[1:02:55]** going to put in there exactly what it needs from 
the architecture and other sources, the developer  

**[1:03:01]** is always going to load these files that you have 
listed under dev load always files. By the way,  

**[1:03:07]** I didn't have to make this myself. This file was 
created on the install. But if you ever wanted to  

**[1:03:12]** customize it, maybe there's another file that you 
always want the dev to load, you can add it here.  

**[1:03:18]** But again, here's our key documents that were 
sharded from the architecture, the coding  

**[1:03:23]** standards, the tech stack, and the source tree. 
Take your time and really go in there and make  

**[1:03:28]** updates to those if you need to and change them if 
any of these things change. All right, we've come  

**[1:03:34]** a long way. If you're still with me, thank you for 
sticking with me. If you made it this far, I would  

**[1:03:39]** love to know who's actually still watching. Um, 
because I bet this is a very long video. I hope  

**[1:03:44]** people are appreciating it, though. So, if you've 
made it this far, how about leaving a comment  

**[1:03:49]** down below and tell me what is the craziest thing 
that you want to brainstorm with the brainstorming  

**[1:03:56]** agent. Give me some of your wildest ideas. And if 
you actually use the brainstorming agent to do it,  

**[1:04:03]** come back and tell me one of the craziest things 
you came up with that you never thought you would  

**[1:04:07]** come up with before. I would love to hear it. 
Maybe also jump into the Discord and and talk  

**[1:04:11]** about your brainstorming adventures. So, as 
a matter of fact, some people in the Discord  

**[1:04:15]** actually talked about spending hours just doing 
brainstorming and coming up with some amazing  

**[1:04:19]** ideas. We sharted our documents. We have our 
architecture. We have our PRD. So, that is  

**[1:04:26]** great. Now, I'm going to do something here. I'm 
going to create a new folder that I'm just going  

**[1:04:32]** to call for now temporarily. And I'm going to say 
get init. put everything in there except for the  

**[1:04:39]** architecture in the PRD sharded documents. And now 
I'm going to add agit ignore. So I'm going to say  

**[1:04:46]** new file.getit ignore. I've added agit ignore 
file. Please populate it with the common things  

**[1:04:54]** that should be in a git ignore and also include 
the ignore folder in the git ignore and the.getit  

**[1:05:01]** get ignore those files should also generally be 
ignored by clouds so it won't clutter the context.  

**[1:05:08]** So there we go. So we just populated a get ignore 
with a lot of common properties. Now if you're  

**[1:05:17]** using a starter template or a starter project, 
it's probably going to set up your git ignore  

**[1:05:21]** for you. Or if you're using like Nex.js, it'll 
it'll set that up for you. In a complex project,  

**[1:05:26]** you would want to use the PO at this point. And 
the PO has a command called run checklist. And  

**[1:05:33]** it's going to run the PO checklist. What that does 
is it's going to look at all of your user stories  

**[1:05:39]** fresh and it's going to look at the architecture, 
make sure that they're aligned, make sure that  

**[1:05:46]** nothing came up in the architecture that needs to 
feed back into the stories because maybe something  

**[1:05:51]** changed or if there's any big gaps. It's a really 
good idea to do that. Sometimes it'll find things,  

**[1:05:57]** but this is such a simple app and like all of the 
BMED method, it's adaptable. We do not have to do  

**[1:06:03]** that step. So, we're going to skip that and we're 
going to jump right to the scrum master. Now,  

**[1:06:10]** if you've never used the scrum master, you 
might not know what it can do. So, as always,  

**[1:06:13]** I recommend doing /help if it doesn't give you 
the help commands automatically. Sometimes it  

**[1:06:19]** will. That's just the nature of LLM sometimes. 
Um, so we have a few things here. We can draft,  

**[1:06:26]** which means create the next story. We can 
do correct course. This is a feature that  

**[1:06:31]** a lot of people have asked for and don't know 
exists. Why does my chair keep sinking? Um,  

**[1:06:36]** correct course is something let's say you've 
developed, you know, halfway through some of  

**[1:06:40]** your epics. You're mid project in the middle of 
a story and you realize you forgot something or  

**[1:06:46]** you want to make a big change. Wrap up what you're 
doing and then talk to the scrum master or the PM.  

**[1:06:52]** You can choose either one and run this correct 
course command. It's going to ask you a bunch  

**[1:06:57]** of questions and it's going to analyze how far 
you've gone and whether it's better to, you know,  

**[1:07:04]** revert back to a certain earlier stage and produce 
new stories and epics or maybe generate new future  

**[1:07:11]** stories and epics from where you're at right now. 
Or your change might be so drastic that it just  

**[1:07:16]** recommends, although it generally shouldn't, that 
you start over. But not only is it going to give  

**[1:07:22]** you these suggestions, it is going to help you. 
It's going to figure out what epics and stories  

**[1:07:27]** need to be modified or changed or added or removed 
so you can do this pivot, account for it, and  

**[1:07:33]** still get to your end goal. Maybe it means making 
updates to the architecture or as I said the PRD  

**[1:07:40]** or maybe you found a new API or a new library 
that you want to do use, so it might put it in the  

**[1:07:45]** tech stack. All of that's a possibility with the 
correct course command. That could be a lifesaver  

**[1:07:50]** depending on the situation. Of course, it's 
best to avoid that which is why you go through  

**[1:07:54]** a lot of planning. What we're looking for here is 
number one, we want to draft the first story. Now,  

**[1:08:01]** if you know what story it's time to draft, 
just tell it. We know we want to do epic one,  

**[1:08:08]** story one. So, what we can do is we can just 
say we can say we can say star draft 1.1.  

**[1:08:16]** So, let's say we're halfway through and it's time 
to do story 2.3 because story 2.2 finished. You  

**[1:08:23]** can just tell it draft the next story and it will 
figure out what the next story is. Or you can tell  

**[1:08:28]** it which one to do. That'll just make it a little 
bit more streamlined. It'll go faster and it'll  

**[1:08:34]** start drafting drafting the story that it needs 
to. When it drafts a story, it's always going  

**[1:08:39]** to check if there was a previous story. if there 
was, it will also check if there's any notes in  

**[1:08:45]** that story that it needs to carry forward into 
the new one. A lot of times also these project  

**[1:08:50]** foundations will have steps in them. So, you 
really want to read these stories especially and  

**[1:08:54]** see if there's any human basically things that you 
need to do. Maybe you need to set up an account or  

**[1:09:01]** maybe you need to, you know, visit a website and 
provision some infrastructure that for whatever  

**[1:09:07]** reason cannot be done by the LLM through a command 
to the remote service. Maybe you have to get out a  

**[1:09:14]** credit card and pay for something. Okay, so it's 
done. Let's look at our story and let's see if  

**[1:09:18]** it followed the proper template. And it's always 
going to put it in draft mode. This is standard  

**[1:09:23]** agile story practice. So as a developer, I want to 
establish the basic noode.js JS TypeScript project  

**[1:09:29]** structure so that I have a solid foundation for 
CLI development. Acceptance criteria means what  

**[1:09:35]** does it actually take to say yes this story is 
done and complete. The tasks and the subtasks  

**[1:09:42]** are going to sound a little bit similar to this a 
lot of times and it should because these are the  

**[1:09:48]** actual steps that the developer agent is going 
to follow step by step to implement our story.  

**[1:09:55]** This is where the scrum master agent goes 
through all of the architecture documents,  

**[1:10:01]** finds information that is relevant to the 
story and gives it to it here. Since we're  

**[1:10:06]** doing project setup, the agent needs to know the 
structure of our project that the architect came  

**[1:10:11]** up with. So that's why it pasted it here. So the 
developer agent has this contextual information  

**[1:10:16]** and doesn't have to search for itself bloating 
its own context. So there are placeholders where  

**[1:10:22]** the dev agent can put notes and also where the Q 
agent QA agent can put their notes. Change this to  

**[1:10:30]** approved. We are done with the scrum master. 
We're just going to close our context and  

**[1:10:35]** we're going to start a new one because as always 
between every step even though we don't have to,  

**[1:10:41]** it's better practice and it minimizes the overall 
context. All right. And now we're here in the home  

**[1:10:46]** stretch. We got James, our full stack developer is 
locked and loaded. Let's do star help. Now you can  

**[1:10:56]** just tell James develop a story and it will find 
the highest numbered story that is set to approved  

**[1:11:02]** or already in progress that maybe wasn't finished 
by an instance of himself from before. Or you can  

**[1:11:08]** just tell him. So why don't we just tell him then 
he's not having to do the searching. It will just  

**[1:11:12]** be more uh more streamlined. So we'll say star 
develop story. We could have also just told it  

**[1:11:23]** develop story. We could also just say number five. 
Regardless, I'm just going to hit space. And then  

**[1:11:29]** I'm going to drag in the file. And now we should 
finally see our developer implementing story one.  

**[1:11:36]** I figure let's just do the first story and then 
we'll commit. But we're just going to say yes,  

**[1:11:41]** let it do whatever it wants to do. It's setting 
up our package.json. JSON. And one thing we can  

**[1:11:46]** do is as it adds the different packages that we 
need as it's going through the different subtasks.  

**[1:11:51]** We'll make sure that this is aligned. By the way, 
we could turn on the unsafe mode for cloud and it  

**[1:11:57]** would just churn through. But for right now, 
I just have it. I'm sitting here. We're doing  

**[1:12:02]** this together. I don't mind just telling it 
yes, continue. If you want to roll the dice,  

**[1:12:06]** you can turn off all the safety features 
and let Claude go wild. And look, we're  

**[1:12:11]** uh we're almost done. It it created a bunch of 
its own internal to-dos mapped to the actual  

**[1:12:17]** to-dos in the story. And then we should see that 
it will actually go through. Now it's starting to  

**[1:12:23]** check them off. We'll set the status to ready 
for review. So when it does that, you have two  

**[1:12:28]** options. I actually recommend doing both, but 
it depends on the story. If it's a simple story,  

**[1:12:32]** probably not necessary, but review it yourself. 
Maybe test out the functionality manually. Check  

**[1:12:38]** it out. I would start a new context yet again. 
So, we're just going to exit. We're going to say  

**[1:12:42]** Claude. And now we're going to use our QA agent, 
which is quality assurance. So, let's do star  

**[1:12:49]** help on Quinn. Quinn the QA agent. So, let's do 
number one. And let's pull in story number one.

**[1:13:00]** Now, again, this is a fresh, brand new context. 
So, it's going to be looking at the story and all  

**[1:13:05]** of the project source code and other updates 
that it made to really make sure that it did  

**[1:13:12]** a good job. So, this is going to this is 
going to do a pretty good deep examination.  

**[1:13:16]** This is another place where you might want 
to use Opus. Maybe even more importantly  

**[1:13:23]** than when we were doing the development because 
this is the critical kind of piece that makes  

**[1:13:28]** sure that the agent didn't go off the rails 
and stick files in a stupid place. Um, and it  

**[1:13:34]** looks like it's already uh finding some things. 
This was obviously a very small setup story. So  

**[1:13:39]** there's not a lot for the QA to do for the QA 
to do, but it did find a few things and it gave  

**[1:13:45]** us uh these compliance checks that it did here 
or improvements that it made. So this is great,  

**[1:13:49]** right? I just want to say thank you again. If 
you stuck all the way through this video and  

**[1:13:53]** made it through here, you're going to be so 
far ahead of the game. You're going to be a  

**[1:13:58]** power user using the BMED and understanding 
the BMAD method, especially in claude code.  

**[1:14:03]** I welcome you to come into the Discord forums 
and give me your shared experience of how it's  

**[1:14:10]** working for you. Share with the community or 
if you have questions still ask the community  

**[1:14:15]** and they'll be happy to help you. I'm sure also 
it's a great it's a great place. We'll see you  

**[1:14:19]** next time. My name is Brian. This has been a 
very long episode on the BMAD code, but I hope  

**[1:14:25]** it was helpful and also worth waiting for. So, 
thank you everybody and we'll see you next time.
