# Transcript: DeepMind’s New AI: A Gift To Humanity

**URL:** https://www.youtube.com/watch?v=Sk9tvyRSCgY
**Segments:** 102
**Channel:** Two Minute Papers
**Duration:** 11:55
**Uploaded:** 2026-04-16

---

## Full Text

Google DeepMind gave an amazing gift to humanity. 
And it is full of surprises. Here’s why. Today, we are living in the age of AI where these 
smart assistants and agents can do things we could only dream of 10 years ago. But. 
Many of these solutions are proprietary, require a subscription, and run in the cloud.
And then this happens. Yup, some OpenClaw users reported losing access to their Claude 
AI subscription citing “heavy workloads”. Now, maybe they did something unsavory, I don’t 
know. I also understand you pay a fixed rate, you can’t eat all you want. 
I respect that. However, this is the point. We have to rely on the 
goodwill of these companies for our workflows. So this is why I keep saying over and over that we should always look for options where you 
we own these AIs and run them on our own systems for free, forever.
No one can take them away. NVIDIA came out with their Nemotron 3 Super, which has super capabilities…but its 
hardware requirements are also super. Not so much with Google DeepMind’s new AI, Gemma 
4. This is a free and open family of models, and yes, finally, the smallest ones 
require only a few gigabytes of memory. No need for an expensive GPU. So much so that 
I wanted to wait a bit before publishing this video to see how you Fellow Scholars use 
it in practice. And…look at that! It runs on your phone without an internet connection. 
And folks are already using it in practice to create offline translation and summarization 
apps. Also, real time image classification running in your browser while talking like a 
bard? No problem. You can already fine tune it with Matt’s work. It is so good, it has a little 
ecosystem around it already in just a few days. Because of the brilliance of 
you Fellow Scholars. Nice work. But it gets better. You see, the smallest Gemma is 
so small, it runs on…oh my. Look…I love that. It runs even on an old beat up nintendo switch, 
first generation. Not exactly something with a lot of memory or processing power. Still 
runs the 2 billion parameter Gemma 4 model. Now that is a gift to humanity. But 
it gets really strange from here on out. Here are 4 things that I found 
really surprising. Dear Fellow Scholars, this is Two Minute Papers 
with Dr. Károly Zsolnai-Fehér. One, they also have a bigger, 31B 
model which was the #3 best open model, and now hold on to your papers Fellow 
Scholars, because it beat some models that are 10 times larger. And still 
competitive with some that are 20 times larger. On some measurements. And it is a 
dense model. What? What is going on here? You see, many of the modern AI systems 
you encounter are what they call mixture of experts models. MoE. These are 
huge AI models with many parameters, and to make sure we don’t burn down all of our 
hardware using them, it splits up this big brain into many small ones. If you have a biology 
question, it chops it up into small parts, and routes them to the parts of the brain that 
it thinks are the best experts at processing it. Typically, to the top 2 to 8 experts. Only 
ask them. Yes, with that, we only activate one small part of a brain at a time. It makes 
sense, right? It’s not a simple process, but it is possible. This enables us to create 
huge intelligent models that are still efficient. Dense models, however, just light up every 
parameter of the system. These are not new, and in some ways, these are very 
inefficient. You light up all the 31 billion parameters in the brain all 
the time, no matter how simple or complex the question is. But this one…this 
one is somehow magically good. How? They did four amazing things: one, Google 
didn’t just dump half the internet into it to learn about us. They apply super strict 
filters to give it only highly curated training data. That is actually good advice 
for our thinking too. Don’t let everything in, curate your information diet. There is lots of 
noise out there - ignore it. That is excellent. Two, they use an interesting attention 
mechanism that has a sliding window and also global attention at the same time. What 
does that mean? Well, when you read a book, you read it line by line to finish a page. That is 
a local sliding window. With that, you get all the details. But sometimes you want to zoom out and 
ask, okay, what book are we reading? Which chapter is this? That is global attention. Here, they use 
both, and call the mechanism hybrid attention. Three, it is better at understanding images. 
You know, Gemma 3 had weird glasses on, and its image understanding was kind of 
a lie. If you gave it a landscape image, it squished it back to a square image before 
processing it, losing some information. It squishes everything into its own preconceived box. 
Not good. Gemma 4 understands the image as-is, and the difference really shows on any 
benchmark that has to do with images. Four, it has a shared KV-cache. 
KV-cache is short term memory for what you are currently talking with it, 
documents, questions. Now the layers of this neural network like to recompute their 
fresh memory from scratch. This one doesn’t, it essentially borrows the memory already computed 
by earlier layers. Less work, nearly the same result. This is one of those ideas where we are 
wondering why we didn’t always do it like this. Okay, and all this was just part of my first 
surprise. Second surprise. It is fantastic at agentic workflows. This is where we don’t just 
have an AI assistant that spits out a bunch of text, this is when we give it arms and legs and 
ask it to do stuff. Tool use, local coding, and a ton more. Plug it into OpenClaw and it can book 
a plane ticket. Look for news and summarize it in a more unbiased way. Or write silly emails to 
Károly from Two Minute Papers. That sort of thing. It is really good at that. So when any company 
decides that you can’t use their system anymore, that’s alright. Just plug in Gemma 4, and you 
are good to go. For free. People find that if you give it custom instructions, sometimes you 
don’t even notice the difference. That is huge. Surprise number three, the context window was 
improved to 256k, twice as big as Gemma 3 had. This is pretty expensive to compute, so don’t 
take it for granted. Here, you are not going to chuck gigabytes of movies into it, but for 
a few long documents, it is perfectly fine. Four, the license. Oh my, the license. This 
one gets overlooked so much. Gemma 3 came with a Gemma license. In other words, it comes with 
strings attached. The model comes with handcuffs, if you will. If you use it to create training data 
for a derivative model. Yup, that one inherits the handcuffs too. But, with Gemma 4, not anymore. 
Look, Apache 2.0 license. Now we’re talking, yes! This license is true to the open 
source spirit. You can modify it, sell it, deploy it commercially with 
almost zero friction. Make derivative models, do a ton of stuff with far fewer 
restrictions. This is huge. Thank you so much! Now, not even this technique is perfect. 
For instance, the model does not have a live database. Without an agent harness, it 
cannot browse or look up stuff. Meaning? Well, meaning that it can be confidently incorrect. 
The internet special. Also for highly complex, open-ended tasks - it’s not great at that. Or, when you have images with lots of high-frequency 
visual details, thin structures, blades of grass, or a fence from far away. Not great at that, 
it’s going to need even better glasses. But, adding this all up, this is an amazing 
gift to humanity, one that cannot be taken from us. This is not for Mr moneybags, this 
is for the little man, and it is free, for all of us, forever. Hugely appreciated. 
Absolutely loving it. What a time to be alive! Also, I waited with this video because I did 
not just want to take the marketing messaging and copy-paste it to you. I wanted to see how 
you Fellow Scholars are actually using it in practice. Read through your experiences 
with it. Does it really work in practice? Super important. That’s what we are here 
for, not the copy-pasted media headlines. That needs time. Trying to explain all this in 
simple words also takes time. I don’t have a team here, I do everything from the writing to 
recording, video editing. I am trying my best here. But it gives you more accurate information, 
and that is the most important for me. So, now, after 10 million downloads in the 
first week and more thorough testing. My opinion is that yes, this thing rocks. I would 
like to send a big thank you to every single scientist who worked on this! And hold on to 
this one for dear life because a frontier model just got locked down for a few select clients. 
You know, it’s a big club. And we ain’t in it. If you enjoyed this, consider 
subscribing and hitting that bell.

---

## Timestamped Segments

**[0:00]** Google DeepMind gave an amazing gift to humanity. 
And it is full of surprises. Here’s why. Today,

**[0:08]** we are living in the age of AI where these 
smart assistants and agents can do things

**[0:13]** we could only dream of 10 years ago. But. 
Many of these solutions are proprietary,

**[0:20]** require a subscription, and run in the cloud.
And then this happens. Yup, some OpenClaw users

**[0:28]** reported losing access to their Claude 
AI subscription citing “heavy workloads”.

**[0:33]** Now, maybe they did something unsavory, I don’t 
know. I also understand you pay a fixed rate,

**[0:40]** you can’t eat all you want. 
I respect that. However,

**[0:44]** this is the point. We have to rely on the 
goodwill of these companies for our workflows.

**[0:49]** So this is why I keep saying over and over that we

**[0:53]** should always look for options where you 
we own these AIs and run them on our own

**[0:58]** systems for free, forever.
No one can take them away.

**[1:02]** NVIDIA came out with their Nemotron 3 Super,

**[1:06]** which has super capabilities…but its 
hardware requirements are also super.

**[1:13]** Not so much with Google DeepMind’s new AI, Gemma 
4. This is a free and open family of models,

**[1:20]** and yes, finally, the smallest ones 
require only a few gigabytes of memory.

**[1:27]** No need for an expensive GPU. So much so that 
I wanted to wait a bit before publishing this

**[1:33]** video to see how you Fellow Scholars use 
it in practice. And…look at that! It runs

**[1:41]** on your phone without an internet connection. 
And folks are already using it in practice to

**[1:47]** create offline translation and summarization 
apps. Also, real time image classification

**[1:54]** running in your browser while talking like a 
bard? No problem. You can already fine tune it

**[2:01]** with Matt’s work. It is so good, it has a little 
ecosystem around it already in just a few days.

**[2:11]** Because of the brilliance of 
you Fellow Scholars. Nice work.

**[2:16]** But it gets better. You see, the smallest Gemma is 
so small, it runs on…oh my. Look…I love that. It

**[2:27]** runs even on an old beat up nintendo switch, 
first generation. Not exactly something with

**[2:34]** a lot of memory or processing power. Still 
runs the 2 billion parameter Gemma 4 model.

**[2:39]** Now that is a gift to humanity. But 
it gets really strange from here

**[2:45]** on out. Here are 4 things that I found 
really surprising. Dear Fellow Scholars,

**[2:50]** this is Two Minute Papers 
with Dr. Károly Zsolnai-Fehér.

**[2:53]** One, they also have a bigger, 31B 
model which was the #3 best open model,

**[3:00]** and now hold on to your papers Fellow 
Scholars, because it beat some models

**[3:07]** that are 10 times larger. And still 
competitive with some that are 20 times

**[3:13]** larger. On some measurements. And it is a 
dense model. What? What is going on here?

**[3:24]** You see, many of the modern AI systems 
you encounter are what they call mixture

**[3:29]** of experts models. MoE. These are 
huge AI models with many parameters,

**[3:36]** and to make sure we don’t burn down all of our 
hardware using them, it splits up this big brain

**[3:41]** into many small ones. If you have a biology 
question, it chops it up into small parts,

**[3:47]** and routes them to the parts of the brain that 
it thinks are the best experts at processing it.

**[3:53]** Typically, to the top 2 to 8 experts. Only 
ask them. Yes, with that, we only activate one

**[4:02]** small part of a brain at a time. It makes 
sense, right? It’s not a simple process,

**[4:08]** but it is possible. This enables us to create 
huge intelligent models that are still efficient.

**[4:15]** Dense models, however, just light up every 
parameter of the system. These are not new,

**[4:23]** and in some ways, these are very 
inefficient. You light up all the

**[4:28]** 31 billion parameters in the brain all 
the time, no matter how simple or complex

**[4:34]** the question is. But this one…this 
one is somehow magically good. How?

**[4:41]** They did four amazing things: one, Google 
didn’t just dump half the internet into it

**[4:47]** to learn about us. They apply super strict 
filters to give it only highly curated

**[4:53]** training data. That is actually good advice 
for our thinking too. Don’t let everything in,

**[5:01]** curate your information diet. There is lots of 
noise out there - ignore it. That is excellent.

**[5:09]** Two, they use an interesting attention 
mechanism that has a sliding window and

**[5:15]** also global attention at the same time. What 
does that mean? Well, when you read a book,

**[5:23]** you read it line by line to finish a page. That is 
a local sliding window. With that, you get all the

**[5:31]** details. But sometimes you want to zoom out and 
ask, okay, what book are we reading? Which chapter

**[5:39]** is this? That is global attention. Here, they use 
both, and call the mechanism hybrid attention.

**[5:47]** Three, it is better at understanding images. 
You know, Gemma 3 had weird glasses on,

**[5:54]** and its image understanding was kind of 
a lie. If you gave it a landscape image,

**[6:00]** it squished it back to a square image before 
processing it, losing some information. It

**[6:06]** squishes everything into its own preconceived box. 
Not good. Gemma 4 understands the image as-is,

**[6:15]** and the difference really shows on any 
benchmark that has to do with images.

**[6:20]** Four, it has a shared KV-cache. 
KV-cache is short term memory for

**[6:26]** what you are currently talking with it, 
documents, questions. Now the layers of

**[6:31]** this neural network like to recompute their 
fresh memory from scratch. This one doesn’t,

**[6:37]** it essentially borrows the memory already computed 
by earlier layers. Less work, nearly the same

**[6:45]** result. This is one of those ideas where we are 
wondering why we didn’t always do it like this.

**[6:52]** Okay, and all this was just part of my first 
surprise. Second surprise. It is fantastic at

**[7:00]** agentic workflows. This is where we don’t just 
have an AI assistant that spits out a bunch of

**[7:06]** text, this is when we give it arms and legs and 
ask it to do stuff. Tool use, local coding, and

**[7:14]** a ton more. Plug it into OpenClaw and it can book 
a plane ticket. Look for news and summarize it

**[7:21]** in a more unbiased way. Or write silly emails to 
Károly from Two Minute Papers. That sort of thing.

**[7:30]** It is really good at that. So when any company 
decides that you can’t use their system anymore,

**[7:38]** that’s alright. Just plug in Gemma 4, and you 
are good to go. For free. People find that if

**[7:44]** you give it custom instructions, sometimes you 
don’t even notice the difference. That is huge.

**[7:51]** Surprise number three, the context window was 
improved to 256k, twice as big as Gemma 3 had.

**[7:59]** This is pretty expensive to compute, so don’t 
take it for granted. Here, you are not going

**[8:05]** to chuck gigabytes of movies into it, but for 
a few long documents, it is perfectly fine.

**[8:11]** Four, the license. Oh my, the license. This 
one gets overlooked so much. Gemma 3 came with

**[8:20]** a Gemma license. In other words, it comes with 
strings attached. The model comes with handcuffs,

**[8:28]** if you will. If you use it to create training data 
for a derivative model. Yup, that one inherits the

**[8:36]** handcuffs too. But, with Gemma 4, not anymore. 
Look, Apache 2.0 license. Now we’re talking,

**[8:48]** yes! This license is true to the open 
source spirit. You can modify it,

**[8:52]** sell it, deploy it commercially with 
almost zero friction. Make derivative

**[8:57]** models, do a ton of stuff with far fewer 
restrictions. This is huge. Thank you so much!

**[9:07]** Now, not even this technique is perfect. 
For instance, the model does not have a

**[9:12]** live database. Without an agent harness, it 
cannot browse or look up stuff. Meaning? Well,

**[9:20]** meaning that it can be confidently incorrect. 
The internet special. Also for highly complex,

**[9:29]** open-ended tasks - it’s not great at that. Or,

**[9:33]** when you have images with lots of high-frequency 
visual details, thin structures, blades of grass,

**[9:40]** or a fence from far away. Not great at that, 
it’s going to need even better glasses.

**[9:47]** But, adding this all up, this is an amazing 
gift to humanity, one that cannot be taken from

**[9:54]** us. This is not for Mr moneybags, this 
is for the little man, and it is free,

**[9:59]** for all of us, forever. Hugely appreciated. 
Absolutely loving it. What a time to be alive!

**[10:09]** Also, I waited with this video because I did 
not just want to take the marketing messaging

**[10:14]** and copy-paste it to you. I wanted to see how 
you Fellow Scholars are actually using it in

**[10:20]** practice. Read through your experiences 
with it. Does it really work in practice?

**[10:25]** Super important. That’s what we are here 
for, not the copy-pasted media headlines.

**[10:32]** That needs time. Trying to explain all this in 
simple words also takes time. I don’t have a

**[10:39]** team here, I do everything from the writing to 
recording, video editing. I am trying my best

**[10:47]** here. But it gives you more accurate information, 
and that is the most important for me.

**[10:54]** So, now, after 10 million downloads in the 
first week and more thorough testing. My

**[11:00]** opinion is that yes, this thing rocks. I would 
like to send a big thank you to every single

**[11:07]** scientist who worked on this! And hold on to 
this one for dear life because a frontier model

**[11:14]** just got locked down for a few select clients. 
You know, it’s a big club. And we ain’t in it.

**[11:21]** If you enjoyed this, consider 
subscribing and hitting that bell.
