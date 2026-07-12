# Transcript: Don't Use Karpathy's Second Brain (I BUILT SOMETHING BETTER)

**URL:** https://www.youtube.com/watch?v=z02Y-1OvWSM
**Segments:** 449
**Channel:** AI Impact
**Duration:** 12:43
**Uploaded:** 2026-05-01

---

## Full Text

So, there's a lot of people talking about knowledge graphs and how important they are for AI. So, one thing everybody is starting to discover is that what AIs need is your own knowledge graph. For an AI to understand you or your industry or anything else, AIs are extremely powerful, but without access to the proper knowledge, you just have mediocre AI. But, to get high-quality expert AI, you have to be able to give it the proper knowledge base. So, let's talk about how to set that up because most people are setting it up completely wrong. And we've seen it across Twitter, everybody is starting to talk about it. Even the founder of like auto research, Andre Karpathy, has even come out and said he's starting to build things with knowledge graphs, too. So, very, very cool stuff. And what I have here is a tool called Obsidian to visualize both knowledge graphs. And on the left side, you can see a building a second brain PARA base method. And on the right side, you can see the new method I'm using called infinite brain instead of second brain. I believe that everybody that's using AI should swap to the second method, and I've tested it and I can show you why it's so much better. So, let me quickly go into how these knowledge graphs work. It's very simple, actually. They're just a bunch of text files that all link together. But, what's cool is that you can scale up to hundreds or thousands or even millions of text files that all have different topics and that all tie back and forth to each other. So, I have an example here of what it could look like. And so, maybe you have one document that's like here here's our ICP, which is like our ideal customer profile. Uh and then it explains all these different details about it. But, then it links to these other documents. Like, what's our pricing philosophy? And then your pricing philosophy might tie to a decision where you said, "Hey, we've decided we're going to do no free tier." And then that decision may tie back to a source which was, "Hey, we were thinking before about doing round pricing." And then you can see all the details about that and basically have all of your knowledge uh linked together to where somebody could actually trace and see across all of your knowledge types, whether it's like a project or a decision or data or a strate- strategy idea, what whatever it is, you can be able to link it all together and then be able be able to have an your AI have high-quality knowledge about you, your industry, your world, and then it can advise you on top of that. Because what I think a lot of people have experienced is that when you just work with plain ChatGPT, it doesn't know your business, doesn't know the decisions you've made, it doesn't know all the different aspects of everything you've thought about, it's not going to be as good. Uh and so, this is the solution to solving that problem. You do have to build your own brain. And let me quickly just show you one example. And this is the old style. So, maybe what you would do is you'd have a folder that would be like your projects. And it would be like your quarter two launch push. And you would just have like some notes where it would be like, "Hey, this is like a note where on April 5th, I decided to kick this off. And then I 3 days later, I talked to my contractor." And maybe this is tagged like your notes, your log, your projects, and things like that. So, this is like a very basic structure, but it's basically just like a note-taker that links to other things. So, you can see here it even says like, "Hey, we clipped our we had Stripe pricing." And then you click to that and you're like, "Oh, well, here's some details about the Stripe pricing screenshots that we did analyze what Stripe would charge for pricing." And so, that way you can actually have really great documents that link back and forth to each other. That's what like a normal This used to be called like a PKM, a personal knowledge management system. And actually, my personal history with this is it went super viral back in like 2016 to 2020. People were building these. And I actually tried to build my own and I was very excited about it. I would drink a bunch of coffee on Saturday mornings and I would go through and take notes of all the books I read and try to organize it in a different way. And I really thought this was going to be really amazing for me. Um unfortunately, I just ran out of time. Like, I had full-time job, full-time consulting, had many other hobbies and projects. And so, I just wasn't able to actually put in enough effort to do the research and make it to where it it really was worth it to me. But, I loved the idea of having all of my knowledge and all of the things that I cared about in a structured knowledge graph for me, the human to access. But, what's cool is that AI has completely changed everything because before, it would have taken me so much time to both build it and also a lot of time to even use it properly, both of which I didn't have. However, now that AI exists, it can actually build these knowledge graphs for you super easily. It's very AI is great at making text. And AI is also great at reading text. And then also, there's all these capabilities that AI could do for you if only it understood your business. So, this really is what's holding people back from AI taking over more and more of the functions in your life and helping helping your business or helping you in different ways. And so, I think that knowledge graphs are now going to be the key thing that everybody's focused on. But, here's the problem. We built these PKM we built these like Obsidian libraries to basically be set up to where it's really easy for a human to look at and understand. And so, when you look over here, it's just grouped into four things: projects, areas, resources, and archives. And just to give you some context, like this is from a guy, his name's Tiago Forte. He does a lot of Twitter stuff. He created this course and this book called Building a Second Brain. I was all into it a few years ago. I really went really deep in it. And he had a lot of ideas with this like PARA method where you'd have different projects and you'd group things kind of operationally in the projects you're doing. You would just have areas for like deep research where you could build lots and lots of like just knowledge graphs and things like that. You had resources that maybe were things like SOPs or things like that that you could reference back and forth. And then you'd have archives where maybe there's like completed projects or ideas you're not as excited about or something you that basically just so that you still have everything you ever needed, but it's just in a different system. But, the thing is this is not perfect for AI. This is great for humans who need to have four folders. But, the truth is AI can analyze data so quickly and it can read so much um that we probably need to structure this a little bit better. So, I spent some time on this and I've actually built something that took it from the same question you could ask two knowledge graphs, one that was in the building a second brain type system and one that was in this new system I'm calling like the infinite brain system. And the tokens that were used, instead of it being 9,000 tokens, it was only 600. And that's because and it's literally it's the same data, but it was just structured slightly differently. So, let me show you what that looks like. Instead of using the projects, areas, resources, archives, which the problem with that is that then you have these giant massive notes. I'll show you one in a second. But, you also have like untyped links, the metadata isn't as structured as what I'm going to provide later. And then scope retrieval, what what I mean by this is that it's really hard for an AI to be like, "I want to know the pricing decision made on this certain day." and find it. It has to like look at like your pricing document and read the entire long document that would have been in this old system. And probably a lot of that's wasted tokens. Maybe even is going to confuse the AI with lots of different back-and-forth decisions or back-and-forth discussions. Instead of just like, "Hey hey, here's the perfect file for this exact thing, which is a decision." and read it there. So, what is the infinite brain different with? It basically has five pillars. We still have atomic notes. We want to keep those lines to 50 to 300 is kind of the max. Maybe there's a few times we could go above that, but at that point I'd rather break it into like part one, part two, part three, part four. The reason being is that this seems to be the perfect amount for an AI to just quickly ingest highly relevant information. And so, I'm trying to stick to that since I know the AI will be the primary reader for me. I also, instead of just using four nodes, which I think makes sense when you're trying to simplify for a human, but my assumption here is that it's not going to be me reading this. It's going to be an AI and I and the AI is fine with a little bit more complexity than a human. So, what I did is I actually took it into 16 different types. So, for this it would be like pillars, decisions, concepts, questions, playbooks, task, events, pattern, hypothesis, facts, source, bookmark, note, contact, reference, and custom. And the thing is that may sound overwhelming, but the truth is you don't have to understand any of it. Your AI can actually set this up for you, organize everything for you. And then when it's retrieving, it can retrieve stuff for you. So, this really is more for the AI to understand things. And this is the proper grouping, I believe, for the AI to best understand what's going on. And so, this way you can chat with an AI, you can give it data, you can give it knowledge, you can give it books you've read, and different things like that. And then maybe discuss with it different things you think about it. And then it can take all that data and then structure it into something like this for for you. Now, this is where I got a lot more advanced than what I feel the typical Obsidian basic setups are. Instead of just linking things together, I actually made more complex edge types. An edge basically means like connecting from one to the other. Like, what is the connection? Instead of just saying, "Hey, they link." it's like, "What is the nature of that link?" So, I have supports, basically like this argument supports another argument. Or contradicts. You know, that those are two very different ways you want to link something. I think those are very relevant to link them differently. But, this basically says, "Hey, this disagrees with this other idea." Um depends on. So, for this to be true, this other thing must be true. Um derived from. Uh basically, it was like this was created based on this other idea. Related to. This is more just like a little bit if it's unclear what it's related with with any others, you can do that. Um part of. So, maybe if you were saying like, "Hey, like I have my infinite brain system, right? I have this certain way it works. And then I may have like these tactics inside it that I'd want to use. Those are all part of my infinite brain strategy." Um preceded by. So, that would be like just something that happens beforehand. Maybe if you're doing like SOP stuff, it's like, "Hey, this is preceded by step step three is preceded by step two." Followed by kind of the opposite. Authored. Who made Who made this? Was this Claude who made it? Was it a human? Was it a human plus Claude? Was it ChatGPT? Um really good to know that. And then also just tagging. So, that just makes it where it's really easy for you to tag other things in the system if it doesn't fit into one of those options. Um so, why I love this is that otherwise, AI would just see, "Hey, this is linked together." and that's the common thing. But, it would have to then read everything about it to then know, "Oh, this actually The reason it's linked is because it contradicts or because it depends on it. Or hey, this is just preceded by it. It doesn't even matter. It doesn't even It's not even relevant for what we're talking about. It's just It's only relevant if you're looking at the operations side, not relevant if you're thinking conceptually. So, I think that these 10 edge types in the gives the AI the ability when it's looking at one node, it can then decide where else it wants to go. And then that also shows this. Like, what I was showing before with this knowledge graph, you can then tell the AI a question and maybe it realizes like, "Hey, this deals with pricing, right?" And so, it would start with um decision no free tier. It would see that. And then it would be like, "Oh, well, now I see pricing philosophy." And what is it that made up this pricing philosophy? And you can see like, "Oh, well, they looked at this source. They looked at this decision. They looked at this um team tier was like a question they had, should there be a team tier or not?" And so, then it has all this amazing understanding of of this unique complex question or all the ideas of pricing. And then let's say you have a new team member that maybe doesn't have all this institutional knowledge. They weren't on these calls talking about it. This is documented and it can outlive the team that you have today and provide make it to where the AI can help you have this rich knowledge for future use. So, just to show you what this would look like quantitatively, because token costs are starting to adjust. I think that your people a lot of the free tiers and really great deals in AI are starting to disappear a little bit like Claude Max. And so, it's getting to be a world where tokens matter more. So, let me now show you on the infinite brain side of things. Instead of having all this in like these giant long documents that then link to you different different other long documents, instead you have like these tiny little nodes that it's like, "Hey, here's a decision point." And then with that you could actually see what are the things that are the edges for it. And you can see pricing philosophy. You can see here's the other related pieces. So, it's very easy to quickly the AI can get a quick overview that's very simplified. And then when it wants to have more data, it can look at these other options here and go deeper into it. It can look at the What was our monthly recurring revenue for April? That would probably be really relevant to knowing what the pricing should be. What's Stripe fees? What's Stripe international fees for international clients? Our hypothesis is that creators will pay and that positioning against incumbents will not replace them. So, I mean, basically you then can go through and the AI can actually analyze this and know and before it even reads it and uses the tokens on it, it can then read this quick little summary which is like, "Hey, this is the idea in one sentence." Do you want to And then the AI can basically decide, "Okay, do I want to I spent 50 tokens reading this sentence. Do I now want to go down and read more in depth on the whole topic?" And so, I really like this system. It's working way better for me. It's way working way better for my clients. I'm using this for data. I'm using this for design. I'm using this for for analysis. I'm using this for building knowledge libraries or SOP libraries. I think that this is the system that AI needs and I believe it's one that is really going to make this whole second brain personal knowledge management. I I think all the people like me that were super into this in 2018, 2019, but then really weren't able to make it work, I think now it's going to be possible to make it work. And I think also this is the key that unlocks AI that understands you and that is also able to help you push your life and business forward with the proper knowledge and context it needs. By the way, something we have in our school community, if you're interested, we have three prompts to basically build your own vault or if you have a a PARA style building a second brain system, we actually have a prompt that can help you convert that to an infinite brain and then also giving you some prompts to help you query this type of brain that can make it very efficient. So, if you're interested, feel free to join the school community where we can give that to you and we'll have more topics about building your own infinite brain. And then also or if you want to just DM me on LinkedIn or Twitter and I'm happy to send it to you as well. All right. So, that's our topic on knowledge graphs. If you enjoyed it, subscribe to the channel. We always go into the in-depth news that you need to know as an AI power user. And then I also share things where me as an AI architect working with my clients and what we're setting up and how you can then use that same architecture to help you perform better with AI. So, if you like this content, subscribe to the channel, hit the bell, like the video, and we'll see you next time. >> [music]

---

## Timestamped Segments

**[0:00]** So, there's a lot of people talking

**[0:01]** about knowledge graphs and how important

**[0:02]** they are for AI. So, one thing everybody

**[0:04]** is starting to discover is that what AIs

**[0:06]** need is your own knowledge graph. For an

**[0:08]** AI to understand you or your industry or

**[0:10]** anything else, AIs are extremely

**[0:11]** powerful, but without access to the

**[0:13]** proper knowledge, you just have mediocre

**[0:15]** AI. But, to get high-quality expert AI,

**[0:17]** you have to be able to give it the

**[0:18]** proper knowledge base. So, let's talk

**[0:20]** about how to set that up because most

**[0:22]** people are setting it up completely

**[0:23]** wrong. And we've seen it across Twitter,

**[0:24]** everybody is starting to talk about it.

**[0:26]** Even the founder of like auto research,

**[0:27]** Andre Karpathy, has even come out and

**[0:29]** said he's starting to build things with

**[0:30]** knowledge graphs, too. So, very, very

**[0:32]** cool stuff. And what I have here is a

**[0:34]** tool called Obsidian to visualize both

**[0:35]** knowledge graphs. And on the left side,

**[0:37]** you can see a building a second brain

**[0:39]** PARA base method. And on the right side,

**[0:41]** you can see the new method I'm using

**[0:43]** called infinite brain instead of second

**[0:45]** brain. I believe that everybody that's

**[0:46]** using AI should swap to the second

**[0:48]** method, and I've tested it and I can

**[0:50]** show you why it's so much better. So,

**[0:51]** let me quickly go into how these

**[0:52]** knowledge graphs work. It's very simple,

**[0:54]** actually. They're just a bunch of text

**[0:56]** files that all link together. But,

**[0:58]** what's cool is that you can scale up to

**[0:59]** hundreds or thousands or even millions

**[1:01]** of text files that all have different

**[1:02]** topics and that all tie back and forth

**[1:04]** to each other. So, I have an example

**[1:06]** here of what it could look like. And so,

**[1:07]** maybe you have one document that's like

**[1:09]** here here's our ICP, which is like our

**[1:12]** ideal customer profile. Uh and then it

**[1:14]** explains all these different details

**[1:15]** about it. But, then it links to these

**[1:18]** other documents. Like, what's our

**[1:19]** pricing philosophy? And then your

**[1:21]** pricing philosophy might tie to a

**[1:23]** decision where you said, "Hey, we've

**[1:24]** decided we're going to do no free tier."

**[1:26]** And then that decision may tie back to a

**[1:28]** source which was, "Hey, we were thinking

**[1:29]** before about doing round pricing." And

**[1:32]** then you can see all the details about

**[1:34]** that and basically have all of your

**[1:36]** knowledge uh linked together to where

**[1:38]** somebody could actually trace and see

**[1:39]** across all of your knowledge types,

**[1:41]** whether it's like a project or a

**[1:43]** decision or data or a strate- strategy

**[1:47]** idea, what whatever it is, you can be

**[1:48]** able to link it all together and then be

**[1:49]** able be able to have an your AI have

**[1:51]** high-quality knowledge about you, your

**[1:53]** industry, your world, and then it can

**[1:55]** advise you on top of that. Because what

**[1:57]** I think a lot of people have experienced

**[1:58]** is that when you just work with plain

**[1:59]** ChatGPT, it doesn't know your business,

**[2:01]** doesn't know the decisions you've made,

**[2:02]** it doesn't know all the different

**[2:04]** aspects of everything you've thought

**[2:05]** about, it's not going to be as good. Uh

**[2:07]** and so, this is the solution to solving

**[2:08]** that problem. You do have to build your

**[2:10]** own brain. And let me quickly just show

**[2:11]** you one example. And this is the old

**[2:13]** style. So, maybe what you would do is

**[2:14]** you'd have a folder that would be like

**[2:16]** your projects. And it would be like your

**[2:17]** quarter two launch push. And you would

**[2:19]** just have like some notes where it would

**[2:21]** be like, "Hey, this is like a note where

**[2:23]** on April 5th, I decided to kick this

**[2:25]** off. And then I 3 days later, I talked

**[2:27]** to my contractor." And maybe this is

**[2:29]** tagged like your notes, your log, your

**[2:30]** projects, and things like that. So, this

**[2:32]** is like a very basic structure, but it's

**[2:34]** basically just like a note-taker that

**[2:35]** links to other things. So, you can see

**[2:36]** here it even says like, "Hey, we clipped

**[2:38]** our we had Stripe pricing." And then you

**[2:40]** click to that and you're like, "Oh,

**[2:41]** well, here's some details about the

**[2:42]** Stripe pricing screenshots that we did

**[2:44]** analyze what Stripe would charge for

**[2:46]** pricing." And so, that way you can

**[2:47]** actually have really great documents

**[2:49]** that link back and forth to each other.

**[2:51]** That's what like a normal This used to

**[2:52]** be called like a PKM, a personal

**[2:54]** knowledge management system. And

**[2:55]** actually, my personal history with this

**[2:57]** is it went super viral back in like 2016

**[3:00]** to 2020. People were building these. And

**[3:02]** I actually tried to build my own and I

**[3:03]** was very excited about it. I would drink

**[3:05]** a bunch of coffee on Saturday mornings

**[3:07]** and I would go through and take notes of

**[3:08]** all the books I read and try to organize

**[3:10]** it in a different way. And I really

**[3:11]** thought this was going to be really

**[3:11]** amazing for me. Um unfortunately, I just

**[3:13]** ran out of time. Like, I had full-time

**[3:15]** job, full-time consulting, had many

**[3:17]** other hobbies and projects. And so, I

**[3:18]** just wasn't able to actually put in

**[3:20]** enough effort to do the research and

**[3:22]** make it to where it it really was worth

**[3:23]** it to me. But, I loved the idea of

**[3:24]** having all of my knowledge and all of

**[3:26]** the things that I cared about in a

**[3:28]** structured knowledge graph for me, the

**[3:30]** human to access. But, what's cool is

**[3:31]** that AI has completely changed

**[3:33]** everything because before, it would have

**[3:34]** taken me so much time to both build it

**[3:37]** and also a lot of time to even use it

**[3:38]** properly, both of which I didn't have.

**[3:40]** However, now that AI exists, it can

**[3:42]** actually build these knowledge graphs

**[3:44]** for you super easily. It's very AI is

**[3:46]** great at making text. And AI is also

**[3:48]** great at reading text. And then also,

**[3:50]** there's all these capabilities that AI

**[3:51]** could do for you if only it understood

**[3:53]** your business. So, this really is what's

**[3:55]** holding people back from AI taking over

**[3:58]** more and more of the functions in your

**[3:59]** life and helping helping your business

**[4:01]** or helping you in different ways. And

**[4:02]** so, I think that knowledge graphs are

**[4:04]** now going to be the key thing that

**[4:06]** everybody's focused on. But, here's the

**[4:07]** problem. We built these PKM we built

**[4:10]** these like Obsidian libraries to

**[4:12]** basically be set up to where it's really

**[4:14]** easy for a human to look at and

**[4:16]** understand. And so, when you look over

**[4:17]** here, it's just grouped into four

**[4:19]** things: projects, areas, resources, and

**[4:22]** archives. And just to give you some

**[4:24]** context, like this is from a guy, his

**[4:26]** name's Tiago Forte. He does a lot of

**[4:28]** Twitter stuff. He created this course

**[4:30]** and this book called Building a Second

**[4:31]** Brain. I was all into it a few years

**[4:33]** ago. I really went really deep in it.

**[4:35]** And he had a lot of ideas with this like

**[4:36]** PARA method where you'd have different

**[4:37]** projects and you'd group things kind of

**[4:39]** operationally in the projects you're

**[4:41]** doing. You would just have areas for

**[4:42]** like deep research where you could build

**[4:44]** lots and lots of like just knowledge

**[4:46]** graphs and things like that. You had

**[4:47]** resources that maybe were things like

**[4:49]** SOPs or things like that that you could

**[4:51]** reference back and forth. And then you'd

**[4:52]** have archives where maybe there's like

**[4:54]** completed projects or ideas you're not

**[4:55]** as excited about or something you that

**[4:57]** basically just so that you still have

**[4:58]** everything you ever needed, but it's

**[4:59]** just in a different system. But, the

**[5:01]** thing is this is not perfect for AI.

**[5:02]** This is great for humans who need to

**[5:04]** have four folders. But, the truth is AI

**[5:06]** can analyze data so quickly and it can

**[5:08]** read so much um that we probably need to

**[5:11]** structure this a little bit better. So,

**[5:12]** I spent some time on this and I've

**[5:14]** actually built something that took it

**[5:16]** from the same question you could ask two

**[5:18]** knowledge graphs, one that was in the

**[5:20]** building a second brain type system and

**[5:21]** one that was in this new system I'm

**[5:23]** calling like the infinite brain system.

**[5:24]** And the tokens that were used, instead

**[5:26]** of it being 9,000 tokens, it was only

**[5:29]** 600. And that's because and it's

**[5:31]** literally it's the same data, but it was

**[5:33]** just structured slightly differently.

**[5:34]** So, let me show you what that looks

**[5:36]** like. Instead of using the projects,

**[5:38]** areas, resources, archives, which the

**[5:40]** problem with that is that then you have

**[5:41]** these giant massive notes. I'll show you

**[5:43]** one in a second. But, you also have like

**[5:45]** untyped links, the metadata isn't as

**[5:46]** structured as what I'm going to provide

**[5:47]** later. And then scope retrieval, what

**[5:49]** what I mean by this is that it's really

**[5:50]** hard for an AI to be like, "I want to

**[5:52]** know the pricing decision made on this

**[5:53]** certain day." and find it. It has to

**[5:55]** like look at like your pricing document

**[5:57]** and read the entire long document that

**[5:59]** would have been in this old system. And

**[6:00]** probably a lot of that's wasted tokens.

**[6:02]** Maybe even is going to confuse the AI

**[6:03]** with lots of different back-and-forth

**[6:05]** decisions or back-and-forth discussions.

**[6:07]** Instead of just like, "Hey hey, here's

**[6:09]** the perfect file for this exact thing,

**[6:10]** which is a decision." and read it there.

**[6:12]** So, what is the infinite brain different

**[6:14]** with? It basically has five pillars. We

**[6:16]** still have atomic notes. We want to keep

**[6:18]** those lines to 50 to 300 is kind of the

**[6:20]** max. Maybe there's a few times we could

**[6:22]** go above that, but at that point I'd

**[6:23]** rather break it into like part one, part

**[6:25]** two, part three, part four. The reason

**[6:27]** being is that this seems to be the

**[6:28]** perfect amount for an AI to just quickly

**[6:29]** ingest highly relevant information. And

**[6:32]** so, I'm trying to stick to that since I

**[6:33]** know the AI will be the primary reader

**[6:35]** for me. I also, instead of just using

**[6:36]** four nodes, which I think makes sense

**[6:38]** when you're trying to simplify for a

**[6:39]** human, but my assumption here is that

**[6:40]** it's not going to be me reading this.

**[6:41]** It's going to be an AI and I and the AI

**[6:43]** is fine with a little bit more

**[6:44]** complexity than a human. So, what I did

**[6:46]** is I actually took it into 16 different

**[6:47]** types. So, for this it would be like

**[6:49]** pillars, decisions, concepts, questions,

**[6:51]** playbooks, task, events, pattern,

**[6:53]** hypothesis, facts, source, bookmark,

**[6:55]** note, contact, reference, and custom.

**[6:57]** And the thing is that may sound

**[6:59]** overwhelming, but the truth is you don't

**[7:00]** have to understand any of it. Your AI

**[7:01]** can actually set this up for you,

**[7:03]** organize everything for you. And then

**[7:05]** when it's retrieving, it can retrieve

**[7:06]** stuff for you. So, this really is more

**[7:08]** for the AI to understand things. And

**[7:09]** this is the proper grouping, I believe,

**[7:11]** for the AI to best understand what's

**[7:13]** going on. And so, this way you can chat

**[7:14]** with an AI, you can give it data, you

**[7:16]** can give it knowledge, you can give it

**[7:17]** books you've read, and different things

**[7:18]** like that. And then maybe discuss with

**[7:21]** it different things you think about it.

**[7:22]** And then it can take all that data and

**[7:23]** then structure it into something like

**[7:24]** this for for you. Now, this is where I

**[7:26]** got a lot more advanced than what I feel

**[7:28]** the typical Obsidian basic setups are.

**[7:31]** Instead of just linking things together,

**[7:33]** I actually made more complex edge types.

**[7:35]** An edge basically means like connecting

**[7:37]** from one to the other. Like, what is the

**[7:38]** connection? Instead of just saying,

**[7:39]** "Hey, they link." it's like, "What is

**[7:41]** the nature of that link?" So, I have

**[7:43]** supports, basically like this argument

**[7:45]** supports another argument. Or

**[7:47]** contradicts. You know, that those are

**[7:49]** two very different ways you want to link

**[7:50]** something. I think those are very

**[7:51]** relevant to link them differently. But,

**[7:52]** this basically says, "Hey, this

**[7:53]** disagrees with this other idea." Um

**[7:55]** depends on. So, for this to be true,

**[7:58]** this other thing must be true. Um

**[7:59]** derived from. Uh basically, it was like

**[8:02]** this was created based on this other

**[8:03]** idea. Related to. This is more just like

**[8:06]** a little bit if it's unclear what it's

**[8:07]** related with with any others, you can do

**[8:09]** that. Um part of. So, maybe if you were

**[8:11]** saying like, "Hey, like I have my

**[8:12]** infinite brain system, right? I have

**[8:14]** this certain way it works. And then I

**[8:15]** may have like these tactics inside it

**[8:17]** that I'd want to use. Those are all part

**[8:18]** of my infinite brain strategy." Um

**[8:20]** preceded by. So, that would be like just

**[8:22]** something that happens beforehand. Maybe

**[8:24]** if you're doing like SOP stuff, it's

**[8:26]** like, "Hey, this is preceded by step

**[8:27]** step three is preceded by step two."

**[8:29]** Followed by kind of the opposite.

**[8:31]** Authored. Who made Who made this? Was

**[8:33]** this Claude who made it? Was it a human?

**[8:34]** Was it a human plus Claude? Was it

**[8:35]** ChatGPT? Um really good to know that.

**[8:37]** And then also just tagging. So, that

**[8:39]** just makes it where it's really easy for

**[8:40]** you to tag other things in the system if

**[8:42]** it doesn't fit into one of those

**[8:43]** options. Um so, why I love this is that

**[8:46]** otherwise, AI would just see, "Hey, this

**[8:48]** is linked together." and that's the

**[8:50]** common thing. But, it would have to then

**[8:51]** read everything about it to then know,

**[8:53]** "Oh, this actually The reason it's

**[8:54]** linked is because it contradicts or

**[8:55]** because it depends on it. Or hey, this

**[8:57]** is just preceded by it. It doesn't even

**[8:59]** matter. It doesn't even It's not even

**[9:00]** relevant for what we're talking about.

**[9:01]** It's just It's only relevant if you're

**[9:03]** looking at the operations side, not

**[9:04]** relevant if you're thinking

**[9:05]** conceptually. So, I think that these 10

**[9:07]** edge types in the gives the AI the

**[9:09]** ability when it's looking at one node,

**[9:11]** it can then decide where else it wants

**[9:12]** to go. And then that also shows this.

**[9:14]** Like, what I was showing before with

**[9:15]** this knowledge graph, you can then tell

**[9:17]** the AI a question and maybe it realizes

**[9:18]** like, "Hey, this deals with pricing,

**[9:20]** right?" And so, it would start with um

**[9:22]** decision no free tier. It would see

**[9:24]** that. And then it would be like, "Oh,

**[9:25]** well, now I see pricing philosophy." And

**[9:27]** what is it that made up this pricing

**[9:29]** philosophy? And you can see like, "Oh,

**[9:30]** well, they looked at this source. They

**[9:31]** looked at this decision. They looked at

**[9:33]** this um team tier was like a question

**[9:36]** they had, should there be a team tier or

**[9:37]** not?" And so, then it has all this

**[9:38]** amazing understanding of of this unique

**[9:41]** complex question or all the ideas of

**[9:43]** pricing. And then let's say you have a

**[9:45]** new team member that maybe doesn't have

**[9:46]** all this institutional knowledge. They

**[9:48]** weren't on these calls talking about it.

**[9:50]** This is documented and it can outlive

**[9:51]** the team that you have today and provide

**[9:54]** make it to where the AI can help you

**[9:56]** have this rich knowledge for future use.

**[9:59]** So, just to show you what this would

**[10:00]** look like quantitatively, because token

**[10:02]** costs are starting to adjust. I think

**[10:04]** that your people a lot of the free tiers

**[10:07]** and really great deals in AI are

**[10:08]** starting to disappear a little bit like

**[10:10]** Claude Max. And so, it's getting to be a

**[10:12]** world where tokens matter more. So, let

**[10:14]** me now show you on the infinite brain

**[10:15]** side of things. Instead of having all

**[10:17]** this in like these giant long documents

**[10:20]** that then link to you different

**[10:21]** different other long documents, instead

**[10:23]** you have like these tiny little nodes

**[10:25]** that it's like, "Hey, here's a decision

**[10:26]** point."

**[10:27]** And then with that you could actually

**[10:28]** see what are the things that are the

**[10:29]** edges for it. And you can see pricing

**[10:31]** philosophy. You can see here's the other

**[10:33]** related pieces. So, it's very easy to

**[10:35]** quickly the AI can get a quick overview

**[10:37]** that's very simplified. And then when it

**[10:39]** wants to have more data, it can look at

**[10:41]** these other options here and go deeper

**[10:43]** into it. It can look at the What was our

**[10:45]** monthly recurring revenue for April?

**[10:46]** That would probably be really relevant

**[10:47]** to knowing what the pricing should be.

**[10:50]** What's Stripe fees? What's Stripe

**[10:52]** international fees for international

**[10:53]** clients? Our hypothesis is that creators

**[10:55]** will pay and that positioning against

**[10:56]** incumbents will not replace them. So, I

**[10:58]** mean, basically you then can go through

**[11:00]** and the AI can actually analyze this and

**[11:01]** know and before it even reads it and

**[11:03]** uses the tokens on it, it can then read

**[11:05]** this quick little summary which is like,

**[11:06]** "Hey, this is the idea in one sentence."

**[11:08]** Do you want to And then the AI can

**[11:09]** basically decide, "Okay, do I want to I

**[11:11]** spent 50 tokens reading this sentence.

**[11:13]** Do I now want to go down and read more

**[11:15]** in depth on the whole topic?" And so, I

**[11:16]** really like this system. It's working

**[11:18]** way better for me. It's way working way

**[11:19]** better for my clients. I'm using this

**[11:21]** for data. I'm using this for design. I'm

**[11:23]** using this for for analysis. I'm using

**[11:25]** this for building knowledge libraries or

**[11:27]** SOP libraries. I think that this is the

**[11:29]** system that AI needs and I believe it's

**[11:32]** one that is really going to make this

**[11:33]** whole second brain personal knowledge

**[11:35]** management. I I think all the people

**[11:37]** like me that were super into this in

**[11:38]** 2018, 2019, but then really weren't able

**[11:41]** to make it work, I think now it's going

**[11:42]** to be possible to make it work. And I

**[11:43]** think also this is the key that unlocks

**[11:45]** AI that understands you and that is also

**[11:48]** able to help you push your life and

**[11:50]** business forward with the proper

**[11:51]** knowledge and context it needs. By the

**[11:53]** way, something we have in our school

**[11:54]** community, if you're interested, we have

**[11:56]** three prompts to basically build your

**[11:58]** own vault or if you have a a PARA style

**[12:01]** building a second brain system, we

**[12:03]** actually have a prompt that can help you

**[12:04]** convert that to an infinite brain and

**[12:06]** then also giving you some prompts to

**[12:08]** help you query this type of brain that

**[12:09]** can make it very efficient. So, if

**[12:11]** you're interested, feel free to join the

**[12:12]** school community where we can give that

**[12:13]** to you and we'll have more topics about

**[12:15]** building your own infinite brain. And

**[12:17]** then also or if you want to just DM me

**[12:19]** on LinkedIn or Twitter and I'm happy to

**[12:20]** send it to you as well. All right. So,

**[12:22]** that's our topic on knowledge graphs. If

**[12:24]** you enjoyed it, subscribe to the

**[12:25]** channel. We always go into the in-depth

**[12:27]** news that you need to know as an AI

**[12:29]** power user. And then I also share things

**[12:30]** where me as an AI architect working with

**[12:32]** my clients and what we're setting up and

**[12:34]** how you can then use that same

**[12:35]** architecture to help you perform better

**[12:37]** with AI. So, if you like this content,

**[12:38]** subscribe to the channel, hit the bell,

**[12:40]** like the video, and we'll see you next

**[12:41]** time.

**[12:42]** >> [music]
