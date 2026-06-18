# Transcript: ASAaKhK1B5w

**URL:** https://www.youtube.com/watch?v=ASAaKhK1B5w
**Segments:** 304

---

## Full Text

Okay, so I've been doing a lot of Claude 
Code consulting lately to help companies and people improve their workflows. And one 
of the most powerful ideas that people have found handy is that of interactive artifacts. 
So I'll be going through all 3 layers of that. And hopefully by the end of the video, you will 
be one step closer to being a power user. Okay, so layer 1, we have static artifacts. And you may 
already be doing something like this, but just in case you aren't, I'll quickly go through what this 
is. And that is generating a single HTML file with Claude Code to basically do some brainstorming 
or exploration with. So for example, one of my most common use cases is doing design variations. 
So this is one of my upcoming projects and I have this page of application and it looks fine, but 
I feel like it could look better, but I don't exactly know what better looks like. So usually 
in these situations, what I do is say to Claude, hey, so for the Retrieval Settings card, can 
you gimme like 10 variations on an HTML file, one after another, each one should be fairly 
distinct and follow the same light theme. So giving a prompt kind of like this, Claude Code 
would then extract this card out onto a separate page. Give me a couple of variations. I look 
for it. I know it when I see it, like, hey, this is the one that I was after. And then I just 
tell it to put that back into main application. So whilst we're waiting, here is an example that I 
made before, which is essentially different design variations for the HyperWhisper iOS settings. 
So I'm making the iOS application for my voice-to-text application. And I was like, I don't 
really know what the settings should look like. So then Claude Code made me a nice HTML file with 
10 different variations over here. And I can kind of look through this and be like, okay, this looks 
kind of bad. This looks a bit nicer, but a bit too long. And then this kind of looks like the best 
one over here, but some things need changing. And this is especially helpful for design because I 
don't know how to describe what I want, but I will know it when I see it. And you don't necessarily 
have to do this for design variations. So another use case that I like is if you have a LinkedIn 
skill to basically help you write LinkedIn posts, then you can have it generate you a final HTML 
artifact to show you what the post will look like on LinkedIn. So this is the artifact that's 
included in the skill. And this is a much nicer way to view the output compared to the Claude UI. 
So I could just read through the one that I like, copy it over, change a few things around to make 
it like more natural, but it's already kind of in my writing style and then paste it onto LinkedIn. 
Now I would personally recommend having a HTML artifact as an output for any of the skills that 
you have, especially when you're making decisions between many different variations. And when it 
comes to design-related work, I do this so often that I turn this into a design-variations 
skill. So if I do /design-variations, I can reference any component on my website and then 
it will make variations of that. So for example, for my Claude Code Masterclass, which by the way, 
there is a sale going on right now. So there is a lifetime plan, which I will be removing on April 
23rd. So if you want to buy the lifetime plan at a discount for the most comprehensive Claude Code 
class that is updated almost every single day, then there will be a link down below for this. 
And you may be wondering, why would I buy lifetime access when I don't know if Claude Code is 
still going to be relevant a year from now? And chances are a year from now, there will 
be another more powerful tool, which I will then be making classes on. So by buying lifetime 
access now, you get access to all future agentic coding related classes that I make. Anyways, I 
made a new component right over here and I don't really like the design. So I can get Claude Code 
to make some variations here for this. With the design-variations skill. So I just reference this 
and say the bottom right card that shows how many people have enrolled in the class on the landing 
page. And then I type in the number of variations that I want. So I'll say 20 variations, press 
enter, and it will make them for me isolated. And these are the variations that it made. And I think 
the one that I like the most is probably 2 and maybe 17. Okay, now we can take this further onto 
layer 2 and make this an interactive artifact. So for example, here, it'd be really nice if I 
could just like leave a comment with like a bubble here and then somehow send that feedback back to 
Claude Code and it makes us some modifications. And one of the really good ways of doing this 
is to have Bun, which you may have installed on your computer, make a mini server. So this 
is like a really lightweight server where Bun can basically hot reload the HTML artifact. Make 
this interactive by adding the ability for me to click somewhere and leave a comment and then add 
an export to JSON button in the top right where any feedback will be exported to my clipboard 
and I can copy and paste back to you. And then also make it a Bun interactive HTML artifact 
that is running on a local server instead. Now, whilst we're waiting for this to complete, I also 
really like using this to help me make interactive artifacts to understand an idea better. So for 
example, let's say Claude Code decided to add row-level security to my codebase and I'm like, 
hey, what on earth is this? I want to understand this idea better. I can just say to Claude Code, 
Hey, can you make me an interactive HTML artifact explaining what row-level security is? Add 
buttons, help me click around. I basically want to understand this concept better at like 3 
different levels. And it seems that our previous artifact was made interactive with Bun hot reload 
on this endpoint. So this is what it looks like. I can click somewhere. So for example, if I 
clicked over here, I could say, this looks okay, can you make it like 10 avatar profiles instead? 
And let's say for this one, I can click on this, say, can you add country flags here instead? That 
seems more interesting. And then press save here. And now I can press export to JSON. This will copy 
the comments over to my clipboard. Then we can paste that into Claude and those comments will go 
back. And then Claude Code can do a quick update of that artifact to implement those changes that 
I just mentioned. And then it will automatically reload without me having to refresh a page. So 
it hot reloaded over here. And now in a second, I think it should also make the change over here. 
And then hot reload. So you can see it has flags instead. And yeah, I could add something like this 
to my LinkedIn post variations one. So I could just have this being editable for me and then I 
can copy over and it will highlight the changes back to Claude Code so I can update my skill to 
like better adapt to my style. Now we have our row-level security explainer ready as well. So 
you can see it gave me a nice explainer here. I can then click through the different levels and 
the different ideas. And then I understand it better. Now, of course, you can use this for more 
complicated ideas. I said in this case, can you make me one to show me how PG Bouncer works, add 
diagrams, animations, and stuff. And then this is what it came up with. So this looks pretty handy. 
And then looking through this animation, I'm like, okay, this makes way more sense about what is 
exactly happening behind the scenes. Now, moving on to layer 3, this is like even more complicated, 
but can be even more powerful. And that is by connecting your HTML artifact with Claude Code 
channels to explore data more visually. So this uses the built-in Claude Code channels feature, 
and you may already be aware of this because we use it for Telegram, Discord, iMessage, so you 
can message with Claude Code, but you can also build your own channel as well. So we're going to 
quickly build a channel between our interactive artifact and Claude Code so we can have things 
pass back and forth more easily. So let me use an example of my Claude Code Masterclass. Now let's 
make an HTML artifact for this, whereby I map the customer journey with the help of any events that 
were captured in my analytics tool. Also using any Stripe data and stuff so I can explore the data 
in a much richer way using the channels feature that we have. So firstly, I want to make sure that 
I have my MCP servers connected. So I have PostHog over here and then Stripe. So these are the two 
main data sources that I'm using. So first of all, I will tag the @claude-code-guide agent here. And 
then say, using my data from Stripe and PostHog, the MCP service, can you make an interactive 
HTML artifact with the help of Claude Code channels and make it such that I can leave 
a comment, like pinned comment, for any of the data that's being visualized for the customer 
journey? And then that will go directly back into you for the channel with that question. And then 
the artifact will be automatically updated after you fetch that relevant data. Use the codebase 
to help you map the customer journeys with the events that are being triggered and then give me 
like actual numbers. So in this case, I'm blurring out the revenue data, but you will get the bigger 
picture idea. So essentially what is happening here is that like with our previous example where 
we had to press export to JSON and then paste it back into Claude Code, the whole idea here is that 
what if I just clicked here, left a comment, and then that comment would automatically go back into 
Claude Code and it would make those adjustments. Now, in many cases that can be a bit overkill, 
like in this example, but if you're doing like deep data analysis and work for something in your 
business with the help of MCP servers and stuff, this can be more powerful. So you can see over 
here, this is how it would do the Claude Code channels extension. And it would make us a custom 
channel plugin so that when I leave a comment, that information will automatically go back into 
Claude Code whereby it will query PostHog and Stripe for us and then update the artifact for 
us. So I will say, go ahead and do this whole implementation here. And it gave me a new command 
to run Claude Code with. So I can copy this over, go to a new tab, and it's essentially claude 
--dangerously-load-development-channels server:customer-journey, press enter. This is 
a local development one. So I can press enter here and then it will load that in. And it tells 
me the server will be running on this port over here. So clicking on that, I can open it up. Now 
this is what the interactive artifact looks like. Now this is a bunch of fake data, but you kind of 
get the point. So we can use a pin mode to send a message back into the Claude Code client. So I can 
click on this section over here, leave a comment and say, can you expand on this? Essentially, 
looking at PostHog, make another Sankey diagram to show like how far people scroll down the page 
or something like that. Pressing pin comment here, that should then go back to Claude Code. So you 
can see right over here, customer-journey sent a message. Can you expand on this? So the comment 
that we left. And now Claude Code is going to run its bash commands, MCP servers and stuff like 
that to expand on the data and then update that artifact dynamically. So essentially what we've 
done here is that we've made our own mini app custom frontend with Claude Code as the backend. 
And I can click around and actually change the UI itself. So click over here and say, can you 
remove the revenue card? And then that will also go back to Claude as a brand new message of: can 
you remove the revenue card. And then going back, I can see this pinned comment removed the revenue 
thing I mentioned earlier. And now this pinned comment leads to another thing where I can see 
how many people have viewed each section of the landing page. Okay, now to summarize at layer 3 
with our channel, what we're doing is that we have our artifact communicating with Claude Code via 
the channel. Claude Code has the relevant skills, MCP servers, context about our codebase and stuff 
like that. And then it dynamically updates the artifact again. And it's communicating via the 
Claude Code channels feature, which is exactly the same way that Claude Code can communicate 
with Telegram. And essentially each artifact of ours is doing two things at the same time. 
The first of which is our UI is capturing any decisions that we made. So for example, I could 
be like, okay, well not enough people are viewing the pricing section over here. Maybe this needs to 
be moved up. And then I can tell like Claude Code, Hey, can you move up the pricing section in the 
projects because it seems not as many people are viewing it? That will then go back to the channel. 
And then it's also serving as a conversational surface to edit the tool itself. So of course this 
is like a really basic version of a tool. We can make this better over time and very hyper-specific 
to our use case by doing something like clicking over here and saying, okay, can you add tabs? So 
instead of having one long page, I just have tabs to flick through between. And then pressing pin, 
waiting a while, Claude will then automatically update the UI. So essentially it becomes much 
easier to switch between actually using the tool, the artifact, and building the artifact. And 
if you get a form factor that you really like, then you could turn this into a product or like 
an internal dashboard or something like that. This can be a really good starting point, especially 
to get the feel for the product. Anyways, to make layer 3 a little bit easier for you, I have 
a free video in my Claude Code Masterclass. So you can literally just go here and if you 
don't want to purchase it, then you can sign up, make yourself an account, and then clicking on 
the class for my daily workflows, you will see that there will be a video about this particular 
thing and showing you how to set it up alongside a skill that you can download. And of course, if 
you do want to take advantage of the sale on the lifetime plan before it is gone and get access 
to all future Agentic Coding classes that I make, then there will be a link down below for that. And 
if you are a business owner or a business manager, and you want to get some Claude Code 
coaching for yourself or your team, then there will be a link 
down below for that as well. Okay, so I've been doing a lot of Claude 
Code consulting lately to help companies and people improve their workflows. And one 
of the most powerful ideas that people have found handy is that of interactive artifacts. 
So I'll be going through all 3 layers of that. And hopefully by the end of the video, you will 
be one step closer to being a power user. Okay, so layer 1, we have static artifacts. And you may 
already be doing something like this, but just in case you aren't, I'll quickly go through what this 
is. And that is generating a single HTML file with Claude Code to basically do some brainstorming 
or exploration with. So for example, one of my most common use cases is doing design variations. 
So this is one of my upcoming projects and I have this page of application and it looks fine, but 
I feel like it could look better, but I don't exactly know what better looks like. So usually 
in these situations, what I do is say to Claude, hey, so for the Retrieval Settings card, can 
you gimme like 10 variations on an HTML file, one after another, each one should be fairly 
distinct and follow the same light theme. So giving a prompt kind of like this, Claude Code 
would then extract this card out onto a separate page. Give me a couple of variations. I look 
for it. I know it when I see it, like, hey, this is the one that I was after. And then I just 
tell it to put that back into main application. So whilst we're waiting, here is an example that I 
made before, which is essentially different design variations for the HyperWhisper iOS settings. 
So I'm making the iOS application for my voice-to-text application. And I was like, I don't 
really know what the settings should look like. So then Claude Code made me a nice HTML file with 
10 different variations over here. And I can kind of look through this and be like, okay, this looks 
kind of bad. This looks a bit nicer, but a bit too long. And then this kind of looks like the best 
one over here, but some things need changing. And this is especially helpful for design because I 
don't know how to describe what I want, but I will know it when I see it. And you don't necessarily 
have to do this for design variations. So another use case that I like is if you have a LinkedIn 
skill to basically help you write LinkedIn posts, then you can have it generate you a final HTML 
artifact to show you what the post will look like on LinkedIn. So this is the artifact that's 
included in the skill. And this is a much nicer way to view the output compared to the Claude UI. 
So I could just read through the one that I like, copy it over, change a few things around to make 
it like more natural, but it's already kind of in my writing style and then paste it onto LinkedIn. 
Now I would personally recommend having a HTML artifact as an output for any of the skills that 
you have, especially when you're making decisions between many different variations. And when it 
comes to design-related work, I do this so often that I turn this into a design-variations 
skill. So if I do /design-variations, I can reference any component on my website and then 
it will make variations of that. So for example, for my Claude Code Masterclass, which by the way, 
there is a sale going on right now. So there is a lifetime plan, which I will be removing on April 
23rd. So if you want to buy the lifetime plan at a discount for the most comprehensive Claude Code 
class that is updated almost every single day, then there will be a link down below for this. 
And you may be wondering, why would I buy lifetime access when I don't know if Claude Code is 
still going to be relevant a year from now? And chances are a year from now, there will 
be another more powerful tool, which I will then be making classes on. So by buying lifetime 
access now, you get access to all future agentic coding related classes that I make. Anyways, I 
made a new component right over here and I don't really like the design. So I can get Claude Code 
to make some variations here for this. With the design-variations skill. So I just reference this 
and say the bottom right card that shows how many people have enrolled in the class on the landing 
page. And then I type in the number of variations that I want. So I'll say 20 variations, press 
enter, and it will make them for me isolated. And these are the variations that it made. And I think 
the one that I like the most is probably 2 and maybe 17. Okay, now we can take this further onto 
layer 2 and make this an interactive artifact. So for example, here, it'd be really nice if I 
could just like leave a comment with like a bubble here and then somehow send that feedback back to 
Claude Code and it makes us some modifications. And one of the really good ways of doing this 
is to have Bun, which you may have installed on your computer, make a mini server. So this 
is like a really lightweight server where Bun can basically hot reload the HTML artifact. Make 
this interactive by adding the ability for me to click somewhere and leave a comment and then add 
an export to JSON button in the top right where any feedback will be exported to my clipboard 
and I can copy and paste back to you. And then also make it a Bun interactive HTML artifact 
that is running on a local server instead. Now, whilst we're waiting for this to complete, I also 
really like using this to help me make interactive artifacts to understand an idea better. So for 
example, let's say Claude Code decided to add row-level security to my codebase and I'm like, 
hey, what on earth is this? I want to understand this idea better. I can just say to Claude Code, 
Hey, can you make me an interactive HTML artifact explaining what row-level security is? Add 
buttons, help me click around. I basically want to understand this concept better at like 3 
different levels. And it seems that our previous artifact was made interactive with Bun hot reload 
on this endpoint. So this is what it looks like. I can click somewhere. So for example, if I 
clicked over here, I could say, this looks okay, can you make it like 10 avatar profiles instead? 
And let's say for this one, I can click on this, say, can you add country flags here instead? That 
seems more interesting. And then press save here. And now I can press export to JSON. This will copy 
the comments over to my clipboard. Then we can paste that into Claude and those comments will go 
back. And then Claude Code can do a quick update of that artifact to implement those changes that 
I just mentioned. And then it will automatically reload without me having to refresh a page. So 
it hot reloaded over here. And now in a second, I think it should also make the change over here. 
And then hot reload. So you can see it has flags instead. And yeah, I could add something like this 
to my LinkedIn post variations one. So I could just have this being editable for me and then I 
can copy over and it will highlight the changes back to Claude Code so I can update my skill to 
like better adapt to my style. Now we have our row-level security explainer ready as well. So 
you can see it gave me a nice explainer here. I can then click through the different levels and 
the different ideas. And then I understand it better. Now, of course, you can use this for more 
complicated ideas. I said in this case, can you make me one to show me how PG Bouncer works, add 
diagrams, animations, and stuff. And then this is what it came up with. So this looks pretty handy. 
And then looking through this animation, I'm like, okay, this makes way more sense about what is 
exactly happening behind the scenes. Now, moving on to layer 3, this is like even more complicated, 
but can be even more powerful. And that is by connecting your HTML artifact with Claude Code 
channels to explore data more visually. So this uses the built-in Claude Code channels feature, 
and you may already be aware of this because we use it for Telegram, Discord, iMessage, so you 
can message with Claude Code, but you can also build your own channel as well. So we're going to 
quickly build a channel between our interactive artifact and Claude Code so we can have things 
pass back and forth more easily. So let me use an example of my Claude Code Masterclass. Now let's 
make an HTML artifact for this, whereby I map the customer journey with the help of any events that 
were captured in my analytics tool. Also using any Stripe data and stuff so I can explore the data 
in a much richer way using the channels feature that we have. So firstly, I want to make sure that 
I have my MCP servers connected. So I have PostHog over here and then Stripe. So these are the two 
main data sources that I'm using. So first of all, I will tag the @claude-code-guide agent here. And 
then say, using my data from Stripe and PostHog, the MCP service, can you make an interactive 
HTML artifact with the help of Claude Code channels and make it such that I can leave 
a comment, like pinned comment, for any of the data that's being visualized for the customer 
journey? And then that will go directly back into you for the channel with that question. And then 
the artifact will be automatically updated after you fetch that relevant data. Use the codebase 
to help you map the customer journeys with the events that are being triggered and then give me 
like actual numbers. So in this case, I'm blurring out the revenue data, but you will get the bigger 
picture idea. So essentially what is happening here is that like with our previous example where 
we had to press export to JSON and then paste it back into Claude Code, the whole idea here is that 
what if I just clicked here, left a comment, and then that comment would automatically go back into 
Claude Code and it would make those adjustments. Now, in many cases that can be a bit overkill, 
like in this example, but if you're doing like deep data analysis and work for something in your 
business with the help of MCP servers and stuff, this can be more powerful. So you can see over 
here, this is how it would do the Claude Code channels extension. And it would make us a custom 
channel plugin so that when I leave a comment, that information will automatically go back into 
Claude Code whereby it will query PostHog and Stripe for us and then update the artifact for 
us. So I will say, go ahead and do this whole implementation here. And it gave me a new command 
to run Claude Code with. So I can copy this over, go to a new tab, and it's essentially claude 
--dangerously-load-development-channels server:customer-journey, press enter. This is 
a local development one. So I can press enter here and then it will load that in. And it tells 
me the server will be running on this port over here. So clicking on that, I can open it up. Now 
this is what the interactive artifact looks like. Now this is a bunch of fake data, but you kind of 
get the point. So we can use a pin mode to send a message back into the Claude Code client. So I can 
click on this section over here, leave a comment and say, can you expand on this? Essentially, 
looking at PostHog, make another Sankey diagram to show like how far people scroll down the page 
or something like that. Pressing pin comment here, that should then go back to Claude Code. So you 
can see right over here, customer-journey sent a message. Can you expand on this? So the comment 
that we left. And now Claude Code is going to run its bash commands, MCP servers and stuff like 
that to expand on the data and then update that artifact dynamically. So essentially what we've 
done here is that we've made our own mini app custom frontend with Claude Code as the backend. 
And I can click around and actually change the UI itself. So click over here and say, can you 
remove the revenue card? And then that will also go back to Claude as a brand new message of: can 
you remove the revenue card. And then going back, I can see this pinned comment removed the revenue 
thing I mentioned earlier. And now this pinned comment leads to another thing where I can see 
how many people have viewed each section of the landing page. Okay, now to summarize at layer 3 
with our channel, what we're doing is that we have our artifact communicating with Claude Code via 
the channel. Claude Code has the relevant skills, MCP servers, context about our codebase and stuff 
like that. And then it dynamically updates the artifact again. And it's communicating via the 
Claude Code channels feature, which is exactly the same way that Claude Code can communicate 
with Telegram. And essentially each artifact of ours is doing two things at the same time. 
The first of which is our UI is capturing any decisions that we made. So for example, I could 
be like, okay, well not enough people are viewing the pricing section over here. Maybe this needs to 
be moved up. And then I can tell like Claude Code, Hey, can you move up the pricing section in the 
projects because it seems not as many people are viewing it? That will then go back to the channel. 
And then it's also serving as a conversational surface to edit the tool itself. So of course this 
is like a really basic version of a tool. We can make this better over time and very hyper-specific 
to our use case by doing something like clicking over here and saying, okay, can you add tabs? So 
instead of having one long page, I just have tabs to flick through between. And then pressing pin, 
waiting a while, Claude will then automatically update the UI. So essentially it becomes much 
easier to switch between actually using the tool, the artifact, and building the artifact. And 
if you get a form factor that you really like, then you could turn this into a product or like 
an internal dashboard or something like that. This can be a really good starting point, especially 
to get the feel for the product. Anyways, to make layer 3 a little bit easier for you, I have 
a free video in my Claude Code Masterclass. So you can literally just go here and if you 
don't want to purchase it, then you can sign up, make yourself an account, and then clicking on 
the class for my daily workflows, you will see that there will be a video about this particular 
thing and showing you how to set it up alongside a skill that you can download. And of course, if 
you do want to take advantage of the sale on the lifetime plan before it is gone and get access 
to all future Agentic Coding classes that I make, then there will be a link down below for that. And 
if you are a business owner or a business manager, and you want to get some Claude Code 
coaching for yourself or your team, then there will be a link 
down below for that as well.

---

## Timestamped Segments

**[0:00]** Okay, so I've been doing a lot of Claude 
Code consulting lately to help companies

**[0:03]** and people improve their workflows. And one 
of the most powerful ideas that people have

**[0:07]** found handy is that of interactive artifacts. 
So I'll be going through all 3 layers of that.

**[0:12]** And hopefully by the end of the video, you will 
be one step closer to being a power user. Okay,

**[0:17]** so layer 1, we have static artifacts. And you may 
already be doing something like this, but just in

**[0:22]** case you aren't, I'll quickly go through what this 
is. And that is generating a single HTML file with

**[0:27]** Claude Code to basically do some brainstorming 
or exploration with. So for example, one of my

**[0:33]** most common use cases is doing design variations. 
So this is one of my upcoming projects and I have

**[0:38]** this page of application and it looks fine, but 
I feel like it could look better, but I don't

**[0:44]** exactly know what better looks like. So usually 
in these situations, what I do is say to Claude,

**[0:49]** hey, so for the Retrieval Settings card, can 
you gimme like 10 variations on an HTML file,

**[0:55]** one after another, each one should be fairly 
distinct and follow the same light theme. So

**[1:00]** giving a prompt kind of like this, Claude Code 
would then extract this card out onto a separate

**[1:04]** page. Give me a couple of variations. I look 
for it. I know it when I see it, like, hey,

**[1:09]** this is the one that I was after. And then I just 
tell it to put that back into main application.

**[1:14]** So whilst we're waiting, here is an example that I 
made before, which is essentially different design

**[1:18]** variations for the HyperWhisper iOS settings. 
So I'm making the iOS application for my

**[1:23]** voice-to-text application. And I was like, I don't 
really know what the settings should look like.

**[1:27]** So then Claude Code made me a nice HTML file with 
10 different variations over here. And I can kind

**[1:32]** of look through this and be like, okay, this looks 
kind of bad. This looks a bit nicer, but a bit too

**[1:36]** long. And then this kind of looks like the best 
one over here, but some things need changing. And

**[1:41]** this is especially helpful for design because I 
don't know how to describe what I want, but I will

**[1:46]** know it when I see it. And you don't necessarily 
have to do this for design variations. So another

**[1:50]** use case that I like is if you have a LinkedIn 
skill to basically help you write LinkedIn posts,

**[1:55]** then you can have it generate you a final HTML 
artifact to show you what the post will look

**[2:00]** like on LinkedIn. So this is the artifact that's 
included in the skill. And this is a much nicer

**[2:04]** way to view the output compared to the Claude UI. 
So I could just read through the one that I like,

**[2:09]** copy it over, change a few things around to make 
it like more natural, but it's already kind of in

**[2:14]** my writing style and then paste it onto LinkedIn. 
Now I would personally recommend having a HTML

**[2:20]** artifact as an output for any of the skills that 
you have, especially when you're making decisions

**[2:24]** between many different variations. And when it 
comes to design-related work, I do this so often

**[2:29]** that I turn this into a design-variations 
skill. So if I do /design-variations, I can

**[2:34]** reference any component on my website and then 
it will make variations of that. So for example,

**[2:38]** for my Claude Code Masterclass, which by the way, 
there is a sale going on right now. So there is a

**[2:43]** lifetime plan, which I will be removing on April 
23rd. So if you want to buy the lifetime plan at

**[2:49]** a discount for the most comprehensive Claude Code 
class that is updated almost every single day,

**[2:54]** then there will be a link down below for this. 
And you may be wondering, why would I buy lifetime

**[2:58]** access when I don't know if Claude Code is 
still going to be relevant a year from now?

**[3:01]** And chances are a year from now, there will 
be another more powerful tool, which I will

**[3:06]** then be making classes on. So by buying lifetime 
access now, you get access to all future agentic

**[3:11]** coding related classes that I make. Anyways, I 
made a new component right over here and I don't

**[3:16]** really like the design. So I can get Claude Code 
to make some variations here for this. With the

**[3:20]** design-variations skill. So I just reference this 
and say the bottom right card that shows how many

**[3:25]** people have enrolled in the class on the landing 
page. And then I type in the number of variations

**[3:29]** that I want. So I'll say 20 variations, press 
enter, and it will make them for me isolated. And

**[3:35]** these are the variations that it made. And I think 
the one that I like the most is probably 2 and

**[3:39]** maybe 17. Okay, now we can take this further onto 
layer 2 and make this an interactive artifact.

**[3:46]** So for example, here, it'd be really nice if I 
could just like leave a comment with like a bubble

**[3:50]** here and then somehow send that feedback back to 
Claude Code and it makes us some modifications.

**[3:55]** And one of the really good ways of doing this 
is to have Bun, which you may have installed

**[4:00]** on your computer, make a mini server. So this 
is like a really lightweight server where Bun

**[4:05]** can basically hot reload the HTML artifact. Make 
this interactive by adding the ability for me to

**[4:10]** click somewhere and leave a comment and then add 
an export to JSON button in the top right where

**[4:15]** any feedback will be exported to my clipboard 
and I can copy and paste back to you. And then

**[4:21]** also make it a Bun interactive HTML artifact 
that is running on a local server instead. Now,

**[4:26]** whilst we're waiting for this to complete, I also 
really like using this to help me make interactive

**[4:31]** artifacts to understand an idea better. So for 
example, let's say Claude Code decided to add

**[4:37]** row-level security to my codebase and I'm like, 
hey, what on earth is this? I want to understand

**[4:42]** this idea better. I can just say to Claude Code, 
Hey, can you make me an interactive HTML artifact

**[4:48]** explaining what row-level security is? Add 
buttons, help me click around. I basically

**[4:51]** want to understand this concept better at like 3 
different levels. And it seems that our previous

**[4:56]** artifact was made interactive with Bun hot reload 
on this endpoint. So this is what it looks like.

**[5:02]** I can click somewhere. So for example, if I 
clicked over here, I could say, this looks okay,

**[5:08]** can you make it like 10 avatar profiles instead? 
And let's say for this one, I can click on this,

**[5:14]** say, can you add country flags here instead? That 
seems more interesting. And then press save here.

**[5:19]** And now I can press export to JSON. This will copy 
the comments over to my clipboard. Then we can

**[5:23]** paste that into Claude and those comments will go 
back. And then Claude Code can do a quick update

**[5:28]** of that artifact to implement those changes that 
I just mentioned. And then it will automatically

**[5:32]** reload without me having to refresh a page. So 
it hot reloaded over here. And now in a second,

**[5:38]** I think it should also make the change over here. 
And then hot reload. So you can see it has flags

**[5:43]** instead. And yeah, I could add something like this 
to my LinkedIn post variations one. So I could

**[5:48]** just have this being editable for me and then I 
can copy over and it will highlight the changes

**[5:53]** back to Claude Code so I can update my skill to 
like better adapt to my style. Now we have our

**[5:58]** row-level security explainer ready as well. So 
you can see it gave me a nice explainer here. I

**[6:04]** can then click through the different levels and 
the different ideas. And then I understand it

**[6:08]** better. Now, of course, you can use this for more 
complicated ideas. I said in this case, can you

**[6:12]** make me one to show me how PG Bouncer works, add 
diagrams, animations, and stuff. And then this is

**[6:17]** what it came up with. So this looks pretty handy. 
And then looking through this animation, I'm like,

**[6:21]** okay, this makes way more sense about what is 
exactly happening behind the scenes. Now, moving

**[6:25]** on to layer 3, this is like even more complicated, 
but can be even more powerful. And that is by

**[6:31]** connecting your HTML artifact with Claude Code 
channels to explore data more visually. So this

**[6:37]** uses the built-in Claude Code channels feature, 
and you may already be aware of this because we

**[6:41]** use it for Telegram, Discord, iMessage, so you 
can message with Claude Code, but you can also

**[6:46]** build your own channel as well. So we're going to 
quickly build a channel between our interactive

**[6:52]** artifact and Claude Code so we can have things 
pass back and forth more easily. So let me use an

**[6:57]** example of my Claude Code Masterclass. Now let's 
make an HTML artifact for this, whereby I map the

**[7:03]** customer journey with the help of any events that 
were captured in my analytics tool. Also using any

**[7:08]** Stripe data and stuff so I can explore the data 
in a much richer way using the channels feature

**[7:13]** that we have. So firstly, I want to make sure that 
I have my MCP servers connected. So I have PostHog

**[7:18]** over here and then Stripe. So these are the two 
main data sources that I'm using. So first of all,

**[7:23]** I will tag the @claude-code-guide agent here. And 
then say, using my data from Stripe and PostHog,

**[7:30]** the MCP service, can you make an interactive 
HTML artifact with the help of Claude Code

**[7:36]** channels and make it such that I can leave 
a comment, like pinned comment, for any of

**[7:41]** the data that's being visualized for the customer 
journey? And then that will go directly back into

**[7:45]** you for the channel with that question. And then 
the artifact will be automatically updated after

**[7:51]** you fetch that relevant data. Use the codebase 
to help you map the customer journeys with the

**[7:56]** events that are being triggered and then give me 
like actual numbers. So in this case, I'm blurring

**[8:00]** out the revenue data, but you will get the bigger 
picture idea. So essentially what is happening

**[8:04]** here is that like with our previous example where 
we had to press export to JSON and then paste it

**[8:09]** back into Claude Code, the whole idea here is that 
what if I just clicked here, left a comment, and

**[8:15]** then that comment would automatically go back into 
Claude Code and it would make those adjustments.

**[8:19]** Now, in many cases that can be a bit overkill, 
like in this example, but if you're doing like

**[8:23]** deep data analysis and work for something in your 
business with the help of MCP servers and stuff,

**[8:28]** this can be more powerful. So you can see over 
here, this is how it would do the Claude Code

**[8:32]** channels extension. And it would make us a custom 
channel plugin so that when I leave a comment,

**[8:38]** that information will automatically go back into 
Claude Code whereby it will query PostHog and

**[8:43]** Stripe for us and then update the artifact for 
us. So I will say, go ahead and do this whole

**[8:48]** implementation here. And it gave me a new command 
to run Claude Code with. So I can copy this over,

**[8:53]** go to a new tab, and it's essentially claude 
--dangerously-load-development-channels

**[8:58]** server:customer-journey, press enter. This is 
a local development one. So I can press enter

**[9:02]** here and then it will load that in. And it tells 
me the server will be running on this port over

**[9:07]** here. So clicking on that, I can open it up. Now 
this is what the interactive artifact looks like.

**[9:13]** Now this is a bunch of fake data, but you kind of 
get the point. So we can use a pin mode to send a

**[9:19]** message back into the Claude Code client. So I can 
click on this section over here, leave a comment

**[9:25]** and say, can you expand on this? Essentially, 
looking at PostHog, make another Sankey diagram

**[9:32]** to show like how far people scroll down the page 
or something like that. Pressing pin comment here,

**[9:37]** that should then go back to Claude Code. So you 
can see right over here, customer-journey sent

**[9:42]** a message. Can you expand on this? So the comment 
that we left. And now Claude Code is going to run

**[9:47]** its bash commands, MCP servers and stuff like 
that to expand on the data and then update that

**[9:52]** artifact dynamically. So essentially what we've 
done here is that we've made our own mini app

**[9:57]** custom frontend with Claude Code as the backend. 
And I can click around and actually change the

**[10:02]** UI itself. So click over here and say, can you 
remove the revenue card? And then that will also

**[10:07]** go back to Claude as a brand new message of: can 
you remove the revenue card. And then going back,

**[10:12]** I can see this pinned comment removed the revenue 
thing I mentioned earlier. And now this pinned

**[10:16]** comment leads to another thing where I can see 
how many people have viewed each section of the

**[10:21]** landing page. Okay, now to summarize at layer 3 
with our channel, what we're doing is that we have

**[10:26]** our artifact communicating with Claude Code via 
the channel. Claude Code has the relevant skills,

**[10:32]** MCP servers, context about our codebase and stuff 
like that. And then it dynamically updates the

**[10:39]** artifact again. And it's communicating via the 
Claude Code channels feature, which is exactly

**[10:43]** the same way that Claude Code can communicate 
with Telegram. And essentially each artifact

**[10:48]** of ours is doing two things at the same time. 
The first of which is our UI is capturing any

**[10:53]** decisions that we made. So for example, I could 
be like, okay, well not enough people are viewing

**[10:57]** the pricing section over here. Maybe this needs to 
be moved up. And then I can tell like Claude Code,

**[11:03]** Hey, can you move up the pricing section in the 
projects because it seems not as many people are

**[11:07]** viewing it? That will then go back to the channel. 
And then it's also serving as a conversational

**[11:13]** surface to edit the tool itself. So of course this 
is like a really basic version of a tool. We can

**[11:19]** make this better over time and very hyper-specific 
to our use case by doing something like clicking

**[11:24]** over here and saying, okay, can you add tabs? So 
instead of having one long page, I just have tabs

**[11:29]** to flick through between. And then pressing pin, 
waiting a while, Claude will then automatically

**[11:33]** update the UI. So essentially it becomes much 
easier to switch between actually using the tool,

**[11:38]** the artifact, and building the artifact. And 
if you get a form factor that you really like,

**[11:43]** then you could turn this into a product or like 
an internal dashboard or something like that. This

**[11:48]** can be a really good starting point, especially 
to get the feel for the product. Anyways, to make

**[11:52]** layer 3 a little bit easier for you, I have 
a free video in my Claude Code Masterclass.

**[11:57]** So you can literally just go here and if you 
don't want to purchase it, then you can sign up,

**[12:01]** make yourself an account, and then clicking on 
the class for my daily workflows, you will see

**[12:06]** that there will be a video about this particular 
thing and showing you how to set it up alongside

**[12:11]** a skill that you can download. And of course, if 
you do want to take advantage of the sale on the

**[12:15]** lifetime plan before it is gone and get access 
to all future Agentic Coding classes that I make,

**[12:20]** then there will be a link down below for that. And 
if you are a business owner or a business manager,

**[12:25]** and you want to get some Claude Code 
coaching for yourself or your team,

**[12:28]** then there will be a link 
down below for that as well.

**[0:00]** Okay, so I've been doing a lot of Claude 
Code consulting lately to help companies

**[0:03]** and people improve their workflows. And one 
of the most powerful ideas that people have

**[0:07]** found handy is that of interactive artifacts. 
So I'll be going through all 3 layers of that.

**[0:12]** And hopefully by the end of the video, you will 
be one step closer to being a power user. Okay,

**[0:17]** so layer 1, we have static artifacts. And you may 
already be doing something like this, but just in

**[0:22]** case you aren't, I'll quickly go through what this 
is. And that is generating a single HTML file with

**[0:27]** Claude Code to basically do some brainstorming 
or exploration with. So for example, one of my

**[0:33]** most common use cases is doing design variations. 
So this is one of my upcoming projects and I have

**[0:38]** this page of application and it looks fine, but 
I feel like it could look better, but I don't

**[0:44]** exactly know what better looks like. So usually 
in these situations, what I do is say to Claude,

**[0:49]** hey, so for the Retrieval Settings card, can 
you gimme like 10 variations on an HTML file,

**[0:55]** one after another, each one should be fairly 
distinct and follow the same light theme. So

**[1:00]** giving a prompt kind of like this, Claude Code 
would then extract this card out onto a separate

**[1:04]** page. Give me a couple of variations. I look 
for it. I know it when I see it, like, hey,

**[1:09]** this is the one that I was after. And then I just 
tell it to put that back into main application.

**[1:14]** So whilst we're waiting, here is an example that I 
made before, which is essentially different design

**[1:18]** variations for the HyperWhisper iOS settings. 
So I'm making the iOS application for my

**[1:23]** voice-to-text application. And I was like, I don't 
really know what the settings should look like.

**[1:27]** So then Claude Code made me a nice HTML file with 
10 different variations over here. And I can kind

**[1:32]** of look through this and be like, okay, this looks 
kind of bad. This looks a bit nicer, but a bit too

**[1:36]** long. And then this kind of looks like the best 
one over here, but some things need changing. And

**[1:41]** this is especially helpful for design because I 
don't know how to describe what I want, but I will

**[1:46]** know it when I see it. And you don't necessarily 
have to do this for design variations. So another

**[1:50]** use case that I like is if you have a LinkedIn 
skill to basically help you write LinkedIn posts,

**[1:55]** then you can have it generate you a final HTML 
artifact to show you what the post will look

**[2:00]** like on LinkedIn. So this is the artifact that's 
included in the skill. And this is a much nicer

**[2:04]** way to view the output compared to the Claude UI. 
So I could just read through the one that I like,

**[2:09]** copy it over, change a few things around to make 
it like more natural, but it's already kind of in

**[2:14]** my writing style and then paste it onto LinkedIn. 
Now I would personally recommend having a HTML

**[2:20]** artifact as an output for any of the skills that 
you have, especially when you're making decisions

**[2:24]** between many different variations. And when it 
comes to design-related work, I do this so often

**[2:29]** that I turn this into a design-variations 
skill. So if I do /design-variations, I can

**[2:34]** reference any component on my website and then 
it will make variations of that. So for example,

**[2:38]** for my Claude Code Masterclass, which by the way, 
there is a sale going on right now. So there is a

**[2:43]** lifetime plan, which I will be removing on April 
23rd. So if you want to buy the lifetime plan at

**[2:49]** a discount for the most comprehensive Claude Code 
class that is updated almost every single day,

**[2:54]** then there will be a link down below for this. 
And you may be wondering, why would I buy lifetime

**[2:58]** access when I don't know if Claude Code is 
still going to be relevant a year from now?

**[3:01]** And chances are a year from now, there will 
be another more powerful tool, which I will

**[3:06]** then be making classes on. So by buying lifetime 
access now, you get access to all future agentic

**[3:11]** coding related classes that I make. Anyways, I 
made a new component right over here and I don't

**[3:16]** really like the design. So I can get Claude Code 
to make some variations here for this. With the

**[3:20]** design-variations skill. So I just reference this 
and say the bottom right card that shows how many

**[3:25]** people have enrolled in the class on the landing 
page. And then I type in the number of variations

**[3:29]** that I want. So I'll say 20 variations, press 
enter, and it will make them for me isolated. And

**[3:35]** these are the variations that it made. And I think 
the one that I like the most is probably 2 and

**[3:39]** maybe 17. Okay, now we can take this further onto 
layer 2 and make this an interactive artifact.

**[3:46]** So for example, here, it'd be really nice if I 
could just like leave a comment with like a bubble

**[3:50]** here and then somehow send that feedback back to 
Claude Code and it makes us some modifications.

**[3:55]** And one of the really good ways of doing this 
is to have Bun, which you may have installed

**[4:00]** on your computer, make a mini server. So this 
is like a really lightweight server where Bun

**[4:05]** can basically hot reload the HTML artifact. Make 
this interactive by adding the ability for me to

**[4:10]** click somewhere and leave a comment and then add 
an export to JSON button in the top right where

**[4:15]** any feedback will be exported to my clipboard 
and I can copy and paste back to you. And then

**[4:21]** also make it a Bun interactive HTML artifact 
that is running on a local server instead. Now,

**[4:26]** whilst we're waiting for this to complete, I also 
really like using this to help me make interactive

**[4:31]** artifacts to understand an idea better. So for 
example, let's say Claude Code decided to add

**[4:37]** row-level security to my codebase and I'm like, 
hey, what on earth is this? I want to understand

**[4:42]** this idea better. I can just say to Claude Code, 
Hey, can you make me an interactive HTML artifact

**[4:48]** explaining what row-level security is? Add 
buttons, help me click around. I basically

**[4:51]** want to understand this concept better at like 3 
different levels. And it seems that our previous

**[4:56]** artifact was made interactive with Bun hot reload 
on this endpoint. So this is what it looks like.

**[5:02]** I can click somewhere. So for example, if I 
clicked over here, I could say, this looks okay,

**[5:08]** can you make it like 10 avatar profiles instead? 
And let's say for this one, I can click on this,

**[5:14]** say, can you add country flags here instead? That 
seems more interesting. And then press save here.

**[5:19]** And now I can press export to JSON. This will copy 
the comments over to my clipboard. Then we can

**[5:23]** paste that into Claude and those comments will go 
back. And then Claude Code can do a quick update

**[5:28]** of that artifact to implement those changes that 
I just mentioned. And then it will automatically

**[5:32]** reload without me having to refresh a page. So 
it hot reloaded over here. And now in a second,

**[5:38]** I think it should also make the change over here. 
And then hot reload. So you can see it has flags

**[5:43]** instead. And yeah, I could add something like this 
to my LinkedIn post variations one. So I could

**[5:48]** just have this being editable for me and then I 
can copy over and it will highlight the changes

**[5:53]** back to Claude Code so I can update my skill to 
like better adapt to my style. Now we have our

**[5:58]** row-level security explainer ready as well. So 
you can see it gave me a nice explainer here. I

**[6:04]** can then click through the different levels and 
the different ideas. And then I understand it

**[6:08]** better. Now, of course, you can use this for more 
complicated ideas. I said in this case, can you

**[6:12]** make me one to show me how PG Bouncer works, add 
diagrams, animations, and stuff. And then this is

**[6:17]** what it came up with. So this looks pretty handy. 
And then looking through this animation, I'm like,

**[6:21]** okay, this makes way more sense about what is 
exactly happening behind the scenes. Now, moving

**[6:25]** on to layer 3, this is like even more complicated, 
but can be even more powerful. And that is by

**[6:31]** connecting your HTML artifact with Claude Code 
channels to explore data more visually. So this

**[6:37]** uses the built-in Claude Code channels feature, 
and you may already be aware of this because we

**[6:41]** use it for Telegram, Discord, iMessage, so you 
can message with Claude Code, but you can also

**[6:46]** build your own channel as well. So we're going to 
quickly build a channel between our interactive

**[6:52]** artifact and Claude Code so we can have things 
pass back and forth more easily. So let me use an

**[6:57]** example of my Claude Code Masterclass. Now let's 
make an HTML artifact for this, whereby I map the

**[7:03]** customer journey with the help of any events that 
were captured in my analytics tool. Also using any

**[7:08]** Stripe data and stuff so I can explore the data 
in a much richer way using the channels feature

**[7:13]** that we have. So firstly, I want to make sure that 
I have my MCP servers connected. So I have PostHog

**[7:18]** over here and then Stripe. So these are the two 
main data sources that I'm using. So first of all,

**[7:23]** I will tag the @claude-code-guide agent here. And 
then say, using my data from Stripe and PostHog,

**[7:30]** the MCP service, can you make an interactive 
HTML artifact with the help of Claude Code

**[7:36]** channels and make it such that I can leave 
a comment, like pinned comment, for any of

**[7:41]** the data that's being visualized for the customer 
journey? And then that will go directly back into

**[7:45]** you for the channel with that question. And then 
the artifact will be automatically updated after

**[7:51]** you fetch that relevant data. Use the codebase 
to help you map the customer journeys with the

**[7:56]** events that are being triggered and then give me 
like actual numbers. So in this case, I'm blurring

**[8:00]** out the revenue data, but you will get the bigger 
picture idea. So essentially what is happening

**[8:04]** here is that like with our previous example where 
we had to press export to JSON and then paste it

**[8:09]** back into Claude Code, the whole idea here is that 
what if I just clicked here, left a comment, and

**[8:15]** then that comment would automatically go back into 
Claude Code and it would make those adjustments.

**[8:19]** Now, in many cases that can be a bit overkill, 
like in this example, but if you're doing like

**[8:23]** deep data analysis and work for something in your 
business with the help of MCP servers and stuff,

**[8:28]** this can be more powerful. So you can see over 
here, this is how it would do the Claude Code

**[8:32]** channels extension. And it would make us a custom 
channel plugin so that when I leave a comment,

**[8:38]** that information will automatically go back into 
Claude Code whereby it will query PostHog and

**[8:43]** Stripe for us and then update the artifact for 
us. So I will say, go ahead and do this whole

**[8:48]** implementation here. And it gave me a new command 
to run Claude Code with. So I can copy this over,

**[8:53]** go to a new tab, and it's essentially claude 
--dangerously-load-development-channels

**[8:58]** server:customer-journey, press enter. This is 
a local development one. So I can press enter

**[9:02]** here and then it will load that in. And it tells 
me the server will be running on this port over

**[9:07]** here. So clicking on that, I can open it up. Now 
this is what the interactive artifact looks like.

**[9:13]** Now this is a bunch of fake data, but you kind of 
get the point. So we can use a pin mode to send a

**[9:19]** message back into the Claude Code client. So I can 
click on this section over here, leave a comment

**[9:25]** and say, can you expand on this? Essentially, 
looking at PostHog, make another Sankey diagram

**[9:32]** to show like how far people scroll down the page 
or something like that. Pressing pin comment here,

**[9:37]** that should then go back to Claude Code. So you 
can see right over here, customer-journey sent

**[9:42]** a message. Can you expand on this? So the comment 
that we left. And now Claude Code is going to run

**[9:47]** its bash commands, MCP servers and stuff like 
that to expand on the data and then update that

**[9:52]** artifact dynamically. So essentially what we've 
done here is that we've made our own mini app

**[9:57]** custom frontend with Claude Code as the backend. 
And I can click around and actually change the

**[10:02]** UI itself. So click over here and say, can you 
remove the revenue card? And then that will also

**[10:07]** go back to Claude as a brand new message of: can 
you remove the revenue card. And then going back,

**[10:12]** I can see this pinned comment removed the revenue 
thing I mentioned earlier. And now this pinned

**[10:16]** comment leads to another thing where I can see 
how many people have viewed each section of the

**[10:21]** landing page. Okay, now to summarize at layer 3 
with our channel, what we're doing is that we have

**[10:26]** our artifact communicating with Claude Code via 
the channel. Claude Code has the relevant skills,

**[10:32]** MCP servers, context about our codebase and stuff 
like that. And then it dynamically updates the

**[10:39]** artifact again. And it's communicating via the 
Claude Code channels feature, which is exactly

**[10:43]** the same way that Claude Code can communicate 
with Telegram. And essentially each artifact

**[10:48]** of ours is doing two things at the same time. 
The first of which is our UI is capturing any

**[10:53]** decisions that we made. So for example, I could 
be like, okay, well not enough people are viewing

**[10:57]** the pricing section over here. Maybe this needs to 
be moved up. And then I can tell like Claude Code,

**[11:03]** Hey, can you move up the pricing section in the 
projects because it seems not as many people are

**[11:07]** viewing it? That will then go back to the channel. 
And then it's also serving as a conversational

**[11:13]** surface to edit the tool itself. So of course this 
is like a really basic version of a tool. We can

**[11:19]** make this better over time and very hyper-specific 
to our use case by doing something like clicking

**[11:24]** over here and saying, okay, can you add tabs? So 
instead of having one long page, I just have tabs

**[11:29]** to flick through between. And then pressing pin, 
waiting a while, Claude will then automatically

**[11:33]** update the UI. So essentially it becomes much 
easier to switch between actually using the tool,

**[11:38]** the artifact, and building the artifact. And 
if you get a form factor that you really like,

**[11:43]** then you could turn this into a product or like 
an internal dashboard or something like that. This

**[11:48]** can be a really good starting point, especially 
to get the feel for the product. Anyways, to make

**[11:52]** layer 3 a little bit easier for you, I have 
a free video in my Claude Code Masterclass.

**[11:57]** So you can literally just go here and if you 
don't want to purchase it, then you can sign up,

**[12:01]** make yourself an account, and then clicking on 
the class for my daily workflows, you will see

**[12:06]** that there will be a video about this particular 
thing and showing you how to set it up alongside

**[12:11]** a skill that you can download. And of course, if 
you do want to take advantage of the sale on the

**[12:15]** lifetime plan before it is gone and get access 
to all future Agentic Coding classes that I make,

**[12:20]** then there will be a link down below for that. And 
if you are a business owner or a business manager,

**[12:25]** and you want to get some Claude Code 
coaching for yourself or your team,

**[12:28]** then there will be a link 
down below for that as well.
