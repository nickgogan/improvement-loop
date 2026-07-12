# Transcript: Why AI is like a (Clever Hans) Horse - Computerphile

**URL:** https://www.youtube.com/watch?v=0GQ2RP-25gM
**Segments:** 573
**Channel:** Computerphile
**Duration:** 18:42
**Uploaded:** 2026-06-25

---

## Full Text

Uh, well, today we're going to be talking about um the Clever Hans effect. >> Okay, who's this Hans character then? >> I don't know if you can use who for an animal. So, Clever Hans was a horse born in the late 1890s in Germany. This is our Clever Hans for today. He was an extraordinary horse. He could do mathematics and answer other types of questions. So, he would be put on display in public and somebody would ask him, "What's What's 3 + 3, Hans?" And they'd start counting up cuz obviously horses can't speak. Go 1 2 3 4 5 and the horse would neigh, stomp its feet, >> Yeah. >> and it'd be six. Amazing. And he could do other types of problems as well, not just mathematics. So, the Clever Hans effect um is something we find in AI in particular. Was Hans doing mathematics? >> Questionable. >> Well, actually, that's still disputed. >> Okay. >> Uh, and we'll never know because Hans died in the First World War and was probably eaten. So, poor Hans. Um but one particular German psychologist um thought that Hans wasn't doing mathematics. >> All right. >> He was observing body language. So, Hans was clever, but he wasn't counting. >> Okay. >> So, the questioner, this is our questioner, would ask, "What's 3 + 3?" And when the correct answer approached, there'd be an involuntary signal that Hans had learned. >> Right. >> So, uh Hans would go ooh, almost I suppose like a Pavlovian response, but a bit more sophisticated because there were more types of trigger. Uh, and a model, an AI model, might do exactly the same thing. So, let's talk about uh the Clever Hans effect in music. So, about I think 12 years ago, there was a paper by a guy called Bob Sturm, and he said that actually music classifier models are all horses, they're just Clever Hans. And I can show that this is the case because what he did is he took some classifiers, he took some music, and he just applied equalization filters, delays, and it changed the classification. So, you had rock music, you add some delay to it, and suddenly the model says it's reggae. But he doesn't know why this happened. So, we today are going to look at why this is happening. Now, if you want want to ask a question a why question in uh computer science or just in general, you probably need causality. So, what in the music caused the model to say this is rock or caused it to say this is reggae. I hope this is reasonable that most people know that audio can be represented as a wave. That might look I don't know, something like this. Okay, so we've got our signal, and this is time along this axis, and this is amplitude, which we can say is volume. I'm not going to be that fussy about it. Now, here's the here's the big leap. So, there's something called a Fourier transform. There's probably been a number file video on it. Maybe. Or computer file. There should be. I'm not going to go into it today cuz it's mathematically quite complicated, but the upshot is that this signal can be decomposed into a load of different sinusoidal signals, each at a different frequency. So, it might look like this. You've got one like this, and you can have one like this, and then you might have one like this. And when you add them all together, you get that. We want to test the hypothesis that our model is not using musical information, but is doing something else, some sort of shortcut learning. So, one way you could do it, it's not the only way, the way I have done it, is to say, "Well, let's decompose this signal into all of its different frequency components." And what you get is something usually called the FFT, which is the fast Fourier transform. And it might look like this. So, on the x-axis, we have the frequencies. And here we have amplitude. And you'll have something that looks >> It's like a histogram of it. >> Yeah, exactly. Histogram of the um It's not quite a histogram, but close enough. Uh of the frequencies that are present in the signal. And then we can ask the question, what frequencies are needed? What is the minimum information I can pass to the model to Let's say this was classified as the blues. >> Mhm. >> Do I need all of this information for it to be the blues? I mean, maybe I do, but we don't know. So, how are we going to find out? I could test every single combination of frequencies. That's mad. In a 30-second piece of audio, which is what our classifiers take, these frequency bins, they're called, there's going to be something like 240,000 of them. So, I can't do that in my head. Uh it's a big number if we look at all possible combinations. So, we're not going to do that. We are going to um sort of do a divide and conquer algorithm, which actually you've got a previous video on. Uh Hannah Chocoler talked about I think it was called Deep Cover at the time. It's now called Rex. Look it up. Uh so, we're going to use a similar technique. And what we're going to do is we're going to divide this up randomly into chunks. And [snorts] so, now we've got 0 1 2 and 3. And we can look at the combinations of these pretty easily. So, we look at the combinations and let's say what was needed 0 and 2 were all that were needed for the blues. Okay, fine. Then we can do the same thing again. So, now we get rid of this. Goodbye. Goodbye. Uh and we can subdivide these and keep searching, keep searching, keep searching. So, that's now 0 1 2 3 until eventually it turns out maybe we just needed this and this for the classifier. To be happy that that's the blues. So that is sufficient. To get the classification blues. So we're going to call that sufficient signal. And I'll play you some later so you can see if you think they're sufficient or not. So that's a sufficient signal. It's enough to get back the blues. Um but it's not necessary. So what do I mean by that? It means that if I remove these frequencies, let me see if I can redraw this approximately the same. So that's the blues and we agree. I hope. That this and this. Are sufficient for the blues. But what if I just removed these and left everything else the same? That might still be the blues. There can be more than one reason. Why the model thinks it's the blues. And I think that's perfectly reasonable. So we can compute also what we call a complete explanation. So a complete. Means that it's sufficient. So by itself it's the blues. And if I remove it. By just setting these frequency values to zero. It's no longer the blues. So we can literally extract the blues from the audio. >> But I mean presumably to our human ears it kind of still sounds like the blues, right? >> Well that's. Um. >> Cuz we did a video a few years ago about image classifier fires and adding a bit of noise and making I don't know a stapler turn into a laptop. >> So short answer to your question. Excellent question. Is yes. Uh really what it does is highlight these models are not. They are horses. This is a clever Hans. Um they're not doing what we would expect. So if I to ask you. Um. I'll crack open my guitar. So if I were to ask you. What the blues is. I mean so I'm going to play like a 12 bar blues. Very simple 12 bar blues. How do you know that's the blues? What would you say? >> Yeah. I I think it's a pattern that I've heard before. That's how I would say. >> Well that's what a model is doing as well. >> Yeah. But I'm envisaging somebody sat on the stoop in front of a, you know, it it it conjures things. >> Okay, so you're saying that there's almost like an emotional >> somebody whose life has left them and then their dog has died and all this sort of stuff. >> Well, lots of blues is also pretty lascivious. It could be I'm your backdoor man and I'm going to come in and have an affair with your wife. >> Oh, yes. >> I'm not. I don't know where she lives. >> [laughter] >> Probably more fits about that actually, isn't it? >> Yeah, probably. So, it's a tricky question, isn't it? There is actually no really simple answer to why that's the blues. We talk about the rhythm. We talk about the instrumentation. We could talk about the harmonic progression, the exact phrasing. Are models doing this? Ideally, yes. >> But probably not. >> But probably not. And I'll I'll as a spoiler, I'll tell you that the fact that we can do this says that they're not. Because it wouldn't be possible, I think, to subtract some frequencies from that and convince you that I was playing Bach. >> Okay, yeah. >> Maybe I could, but but I probably couldn't. So, we've got the sufficient for the blues. We've got the complete >> Just a slight side track then, all right? If you played that on a marimba, would people still think it was the blues? >> Possibly not, because again, timbre is really important in this sort of thing. So, if I would play that on a saxophone or marimba is an interesting choice. >> I just went for something like completely >> completely different, yeah. Do you [music] know what? That'd be a great experiment. >> [music] >> I don't do many user studies. I don't know how to set them up, but I think that's a user study experiment. So, we've got a complete, which means that it's sufficient and necessary. So, if I take it away, we get a new classification. So, the question is then, what is that new classification? So, we call that one the inverse, which is not a very exciting name. And this may or may not exist. So, again, if the models were really doing what we wanted, the complete signal sufficient and necessary should be everything. There should be no inverse. It shouldn't be possible to change the classification by just subtracting a couple of frequencies. Um now, I've got an example we can listen to. Full disclosure, I chose an extreme example >> [laughter] >> so that you can really hear the difference. Um So, let's have a listen. Okay, so what we have here is uh an example that I pre-recorded. I was going to do it live, but you know, nerves got the better of me. So, uh it's my 11-year-old son on drums. Hi, William. Um so, it's it's a basic blues. I think we'll agree that it's the blues. I apologize for the rubbish guitar solo over the top. I'm not a blues player. >> It sounds bluesy to me. It's decent. >> You get the idea. So, that's the original audio. So, remember that we talked about sufficient signals. What is the minimal number of frequencies I can pass in to a classifier? I'm not going to tell you which classifier. It's publicly available, but I don't want to embarrass them cuz it's not a particularly good classifier. What is the minimal number of frequencies I can pass in to get back the classification blues? And the beautiful thing is we can listen to it. So, it's here. This is it. Let's compare it to the original. I broadly speaking, you can see it's got louder bits in the same sort of place. It follows vaguely the same sort of contour, but you can see it's not the same. Do you want to hear it? >> Let's have a listen. >> [music] >> The blues. >> Well, you've made it blue on the screen. I mean, that's the only blue thing about it. >> I wish that were deliberate. That was random. So, that's >> like some kind of I know what it sounds like, the noise some of these electric cars make when they're going slowly. >> [laughter] >> Yeah, I suppose so. Yeah. So, are you telling me that they're they're playing the blues as they as they sort of drive along? Um So, that against all reasonable definitions is the blues for this particular model. So, I also talked about um sufficient and necessary. So, we would hope this is slightly better. So, sufficient can be really really really small. Remember that the model >> So, it would still classify that as the blues even if it was just that sound we just heard. That's >> That is the blues. That's That's the absolute minimum. >> Minimum, yeah. >> Okay, so we've now we're going to ask ourselves a question, what is sufficient and necessary? I suppose ideally we would hope that this sounds better, this sounds more like the blues. If we look at the actual signal, it's quite intriguing. So, remember that we're removing frequencies from all sorts of different parts of the frequency range. And for this simple experiment, I just set them to zero. You don't have to set them to zero, really. You can do anything you want, but zero seems reasonable. It's basically turning off that frequency. So, if we look at it, it actually kind of looks a bit like it's been brick walled. So, I don't know if you know this this term. So, in the early 2000s, maybe even earlier, there was a period in music that I called the the sound wars or the volume wars. And everybody just had to be louder and louder and louder. So, the way you do that is you make the really loud parts quieter, and then then you can make the quieter parts louder. Um and you end up with looks something that looks like this, everything equally loud. So, we can listen to this. So, remember this is the blues by itself is the blues. And if I remove this from this, it's no longer the blues. What I have left over is not the blues. So, let's listen to this. And let's see what you think. >> [music] >> That's reasonable, isn't it? >> Interesting that the bass is gone. >> Yeah. And a lot of the drums is gone. In fact, what it's really holding on to is is my amazing guitar playing. >> [laughter] >> So, so clearly my my guitar playing is the blues, which is not a compliment because the model also thinks that this is the blues. So, hmm, not sure about that. Okay, so the last question we can ask is if we do subtract this from this, do we have enough signal left over to send to the classifier? In this case, we do. We don't always. This case, we do. And we can ask what what is it? So, let's just solo that. >> [music] >> Where's that bass? >> There's the bass. So, [music] and the guitar is a lot less prominent, and the drums are much more prominent. So, this is not the blues. What it What is it? >> Okay, the Well, what would it classify it as? >> Yeah. You've got 10 options. I can't remember all 10, but I'll give you hip hop, rock, heavy metal, reggae, pop. They're five choices for you. It's one of those. >> My uh my clever hands is going to say rock. >> Your clever hands is going to be shot and and turned into glue, I'm afraid. Uh that's classified as hip hop. >> Okay. >> Um and I don't know enough about hip hop actually to say if that's reasonable. I suppose you could say that as a sample, it could be used in a hip hop context, but I think most people would agree that that by itself is not hip hop. But the model says it is. So, what does it all mean? It means your model, this model at least, is a clever hands. And unfortunately, it's not even that clever because actually it's really easy to fool. Uh we've seen a sufficient signal, which doesn't sound anything like the blues. I think even if you were deaf, you would say that's not the blues. Um but the model says it is. And then worse, we can extract the blues from the audio and have something left over that to my ear at least is still kind of the blues. It's borderline. Um but the model says it's now hip hop. It doesn't just say it's hip hop, it says it's quite confident that it's hip hop. So, every model will also, in addition to the classification, gives you something that we we usually refer to as the confidence. Now, whether it really is a confidence score or not is debatable. Um but this has a score that's quite high, this particular audio. So, that had 83% confidence that that was hip hop. And at least in this room, we don't we don't agree. Um and you can do this with pretty much any model. I've chosen one here because it's quite a an extreme example where I think that the sufficient at least is not really open for debate. Um but I've tried this on many, many models and it always works. So, they are not uh listening to the music in any way that a human would understand. They are just doing frequency analysis. And sometimes they're learning the wrong thing. They're doing shortcut learning. So, they listen to this and they say, "Okay, that that's the blues. We're done." And I'll play you one more thing, which I think you might find intriguing. What if I took loads of sufficient signals, hundred of them, all for the blues and added them together and asked the question, "Is that the blues?" Well, I've done it. And it is the blues. And I'll play it for you now. So, remember this is 100 sufficient signals blended together. >> [music] >> And that is classified as the blues. >> Sounds like [music] the sort of thing you might hear in the womb or >> Yeah. It's It's a Yeah. I I played that to somebody else and they said it sounded like you were outside a tent at a festival. Uh and you know, presumably on drugs. I'm not really sure. But, um as not not any festival I've been to. But, I I suppose the point is that the these models they they do work. I mean, the accuracy of this model is very good. But, it's not working the way a human wants it to work. Or certainly not working in a way that a human understands. I think that's a reasonable assertion. And so, Stern's paper when he first looked at this in music is 14 years old and he said, "Look, these models I'm testing. These are horses. These are not understanding music." It's now 14 years later and we haven't got any better. If anything, it's probably worse. >> you were dealing with financial data or weather data or something like that. The minute-by-minute or hour-by-hour fluctuations might not be important. Actually, what you want is a smoother curve. Okay? Well, how would you do that? Have a guess how you do that. >> It's averaging, isn't it? >> Just averaging.

---

## Timestamped Segments

**[0:00]** Uh, well, today we're going to be

**[0:01]** talking about um

**[0:03]** the Clever Hans effect.

**[0:05]** >> Okay, who's this Hans character then?

**[0:08]** >> I don't know if you can use who for an

**[0:09]** animal. So, Clever Hans was a horse born

**[0:11]** in the late 1890s in Germany.

**[0:14]** This is our Clever Hans for today. He

**[0:16]** was an extraordinary horse. He could do

**[0:18]** mathematics and answer other types of

**[0:20]** questions. So, he would be put on

**[0:22]** display in public and somebody would ask

**[0:24]** him, "What's What's 3 + 3, Hans?" And

**[0:27]** they'd start counting up cuz obviously

**[0:28]** horses can't speak. Go 1 2 3 4 5

**[0:35]** and the horse would neigh,

**[0:36]** stomp its feet,

**[0:37]** >> Yeah.

**[0:38]** >> and it'd be six. Amazing. And he could

**[0:40]** do other types of problems as well, not

**[0:42]** just mathematics. So, the Clever Hans

**[0:44]** effect

**[0:46]** um

**[0:46]** is something we find in AI in

**[0:49]** particular.

**[0:53]** Was Hans doing mathematics?

**[0:54]** >> Questionable.

**[0:56]** >> Well, actually, that's still disputed.

**[0:58]** >> Okay.

**[0:58]** >> Uh, and we'll never know because Hans

**[1:00]** died in the First World War and was

**[1:02]** probably eaten.

**[1:03]** So, poor Hans.

**[1:04]** Um

**[1:05]** but one particular German psychologist

**[1:09]** um

**[1:10]** thought that Hans wasn't doing

**[1:11]** mathematics.

**[1:12]** >> All right.

**[1:12]** >> He was observing

**[1:14]** body language. So, Hans was clever,

**[1:16]** but he wasn't counting.

**[1:17]** >> Okay.

**[1:18]** >> So, the questioner, this is our

**[1:20]** questioner, would ask, "What's 3 + 3?"

**[1:22]** And when the correct answer approached,

**[1:25]** there'd be an involuntary signal that

**[1:27]** Hans had learned.

**[1:28]** >> Right.

**[1:29]** >> So, uh Hans would go ooh, almost I

**[1:30]** suppose like a Pavlovian response, but a

**[1:33]** bit more sophisticated because there

**[1:34]** were more types of trigger.

**[1:36]** Uh, and a model, an AI model, might do

**[1:39]** exactly the same thing. So,

**[1:42]** let's talk about uh the Clever Hans

**[1:44]** effect in music. So, about I think 12

**[1:48]** years ago, there was a paper

**[1:50]** by a guy called Bob Sturm, and he said

**[1:52]** that actually music classifier models

**[1:54]** are all horses, they're just Clever

**[1:56]** Hans. And I can show that this is the

**[1:58]** case because what he did is he took some

**[2:00]** classifiers, he took some music, and he

**[2:03]** just applied equalization filters,

**[2:05]** delays,

**[2:07]** and it changed the classification. So,

**[2:08]** you had rock music, you add some delay

**[2:11]** to it,

**[2:12]** and suddenly the model says it's reggae.

**[2:16]** But he doesn't know why

**[2:17]** this happened.

**[2:19]** So, we today are going to look at

**[2:22]** why this is happening. Now, if you want

**[2:24]** want to ask a question a why question in

**[2:28]** uh computer science or just in general,

**[2:30]** you probably need causality. So, what in

**[2:34]** the music caused the model to say this

**[2:37]** is rock or caused it to say this is

**[2:39]** reggae. I hope this is reasonable that

**[2:42]** most people know that audio can be

**[2:45]** represented as a wave. That might look I

**[2:47]** don't know, something like this.

**[2:49]** Okay, so we've got our signal, and this

**[2:51]** is time along this axis, and this is

**[2:53]** amplitude, which we can say is volume.

**[2:56]** I'm not going to be that fussy about it.

**[2:58]** Now,

**[2:59]** here's the here's the big leap. So,

**[3:01]** there's something called a Fourier

**[3:02]** transform. There's probably been a

**[3:04]** number file video on it. Maybe. Or

**[3:07]** computer file. There should be. I'm not

**[3:08]** going to go into it today cuz it's

**[3:10]** mathematically quite complicated, but

**[3:12]** the upshot is that this signal can be

**[3:14]** decomposed

**[3:16]** into a load of different sinusoidal

**[3:17]** signals, each at a different frequency.

**[3:20]** So, it might look like this. You've got

**[3:22]** one like this,

**[3:24]** and you can have one like this, and then

**[3:27]** you might have one like this. And when

**[3:28]** you add them all together, you get that.

**[3:31]** We want to test the hypothesis that our

**[3:32]** model is not using musical information,

**[3:36]** but is doing something else, some sort

**[3:38]** of shortcut learning.

**[3:39]** So, one way you could do it, it's not

**[3:41]** the only way, the way I have done it, is

**[3:43]** to say, "Well, let's decompose this

**[3:45]** signal

**[3:46]** into all of its different frequency

**[3:47]** components." And what you get is

**[3:49]** something usually called the FFT, which

**[3:52]** is the fast Fourier transform. And it

**[3:53]** might look like this.

**[3:54]** So, on the x-axis, we have the

**[3:56]** frequencies.

**[3:58]** And here we have amplitude.

**[4:00]** And you'll have

**[4:02]** something that looks

**[4:04]** >> It's like a histogram of it.

**[4:05]** >> Yeah, exactly. Histogram

**[4:07]** of the um

**[4:09]** It's not quite a histogram, but close

**[4:10]** enough. Uh of the frequencies that are

**[4:12]** present in the signal. And then we can

**[4:13]** ask the question, what frequencies are

**[4:15]** needed?

**[4:16]** What is the minimum information I can

**[4:19]** pass to the model

**[4:20]** to Let's say this was classified as

**[4:23]** the blues.

**[4:25]** >> Mhm.

**[4:27]** >> Do I need all of this information for it

**[4:29]** to be the blues? I mean, maybe I do, but

**[4:31]** we don't know. So, how are we going to

**[4:33]** find out? I could test every single

**[4:34]** combination

**[4:36]** of frequencies.

**[4:38]** That's mad. In a 30-second piece of

**[4:40]** audio, which is what our classifiers

**[4:42]** take, these frequency bins, they're

**[4:44]** called, there's going to be something

**[4:45]** like 240,000 of them.

**[4:48]** So, I can't do that in my head. Uh it's

**[4:50]** a big number if we look at all possible

**[4:52]** combinations. So, we're not going to do

**[4:54]** that. We are going to um

**[4:57]** sort of do a divide and conquer

**[4:58]** algorithm, which actually you've got a

**[5:00]** previous video on. Uh Hannah Chocoler

**[5:02]** talked about I think it was called Deep

**[5:03]** Cover at the time. It's now called Rex.

**[5:05]** Look it up. Uh so, we're going to use a

**[5:06]** similar technique. And what we're going

**[5:07]** to do is we're going to divide this up

**[5:11]** randomly

**[5:12]** into chunks.

**[5:14]** And [snorts] so, now we've got 0 1 2 and

**[5:16]** 3. And we can look at the combinations

**[5:18]** of these pretty easily.

**[5:21]** So, we look at the combinations and

**[5:22]** let's say what was needed 0 and 2 were

**[5:26]** all that were needed for the blues.

**[5:27]** Okay, fine. Then we can do the same

**[5:30]** thing again. So, now we get rid of this.

**[5:31]** Goodbye.

**[5:32]** Goodbye.

**[5:34]** Uh and we can subdivide these

**[5:37]** and keep searching, keep searching, keep

**[5:38]** searching. So, that's now 0 1

**[5:40]** 2 3

**[5:42]** until eventually it turns out maybe we

**[5:44]** just needed this

**[5:46]** and this

**[5:48]** for the classifier.

**[5:50]** To be happy that that's the blues.

**[5:52]** So that is sufficient.

**[5:55]** To get the classification blues. So

**[5:56]** we're going to call that sufficient

**[5:57]** signal.

**[5:59]** And I'll play you some later so you can

**[6:00]** see if you think they're sufficient or

**[6:01]** not. So that's a sufficient signal. It's

**[6:03]** enough to get back the blues. Um but

**[6:06]** it's not necessary. So what do I mean by

**[6:09]** that?

**[6:10]** It means that if I remove these

**[6:12]** frequencies, let me see if I can redraw

**[6:13]** this approximately the same. So that's

**[6:15]** the blues and we agree. I hope.

**[6:19]** That this and this.

**[6:22]** Are sufficient for the blues. But what

**[6:24]** if I just removed these and left

**[6:25]** everything else the same? That might

**[6:27]** still be the blues. There can be more

**[6:29]** than one reason.

**[6:30]** Why the model thinks it's the blues. And

**[6:32]** I think that's perfectly reasonable. So

**[6:33]** we can compute also what we call a

**[6:35]** complete explanation. So a complete.

**[6:39]** Means that it's sufficient.

**[6:41]** So by itself it's the blues. And if I

**[6:43]** remove it. By just setting these

**[6:45]** frequency values to zero. It's no longer

**[6:47]** the blues.

**[6:48]** So we can literally extract the blues

**[6:51]** from the audio.

**[6:52]** >> But I mean presumably to our human ears

**[6:54]** it kind of still sounds like the blues,

**[6:55]** right?

**[6:56]** >> Well that's. Um.

**[6:57]** >> Cuz we did a video a few years ago about

**[6:59]** image classifier fires and adding a bit

**[7:01]** of noise and making I don't know a

**[7:03]** stapler turn into a laptop.

**[7:04]** >> So short answer to your question.

**[7:06]** Excellent question. Is yes.

**[7:08]** Uh really what it does is highlight

**[7:10]** these models are not.

**[7:12]** They are horses. This is a clever Hans.

**[7:15]** Um they're not doing what we would

**[7:17]** expect. So if I to ask you. Um.

**[7:21]** I'll crack open my guitar. So if I were

**[7:23]** to ask you.

**[7:26]** What the blues is. I mean so I'm going

**[7:28]** to play like a 12 bar blues.

**[7:33]** Very simple 12 bar blues.

**[7:35]** How do you know that's the blues? What

**[7:36]** would you say?

**[7:37]** >> Yeah. I I think it's a pattern that I've

**[7:39]** heard before. That's how I would say.

**[7:42]** >> Well that's what a model is doing as

**[7:43]** well.

**[7:44]** >> Yeah.

**[7:45]** But I'm envisaging

**[7:47]** somebody sat on the stoop in front of a,

**[7:49]** you know, it it it conjures things.

**[7:53]** >> Okay, so you're saying that there's

**[7:55]** almost like an emotional

**[7:56]** >> somebody whose life has left them and

**[7:58]** then their dog has died and all this

**[7:59]** sort of stuff.

**[8:00]** >> Well, lots of blues is also pretty

**[8:01]** lascivious. It could be I'm your

**[8:03]** backdoor man and I'm going to come in

**[8:04]** and have an affair with your wife.

**[8:06]** >> Oh, yes.

**[8:06]** >> I'm not. I don't know where she lives.

**[8:08]** >> [laughter]

**[8:09]** >> Probably more fits about that actually,

**[8:10]** isn't it?

**[8:11]** >> Yeah, probably. So, it's a tricky

**[8:13]** question, isn't it? There is actually no

**[8:15]** really simple answer to why that's the

**[8:17]** blues.

**[8:18]** We talk about the rhythm.

**[8:20]** We talk about the instrumentation. We

**[8:21]** could talk about the harmonic

**[8:23]** progression, the exact phrasing.

**[8:26]** Are models doing this? Ideally, yes.

**[8:30]** >> But probably not.

**[8:31]** >> But probably not. And

**[8:34]** I'll I'll as a spoiler, I'll tell you

**[8:36]** that the fact that we can do this says

**[8:38]** that they're not.

**[8:39]** Because it wouldn't be possible, I

**[8:41]** think, to subtract some frequencies from

**[8:44]** that and convince you that I was playing

**[8:47]** Bach.

**[8:48]** >> Okay, yeah.

**[8:49]** >> Maybe I could, but but I probably

**[8:51]** couldn't. So, we've got the sufficient

**[8:53]** for the blues. We've got the complete

**[8:54]** >> Just a slight side track then, all

**[8:55]** right? If you played that on a marimba,

**[8:57]** would people still think it was the

**[8:58]** blues?

**[8:59]** >> Possibly not, because again, timbre is

**[9:01]** really important in this sort of thing.

**[9:03]** So, if I would play that on a saxophone

**[9:05]** or marimba is an interesting choice.

**[9:07]** >> I just went for something like

**[9:08]** completely

**[9:09]** >> completely different, yeah. Do you

**[9:10]** [music] know what? That'd be a great

**[9:12]** experiment.

**[9:16]** >> [music]

**[9:18]** >> I don't do many user studies. I don't

**[9:20]** know how to set them up, but I think

**[9:21]** that's a user study experiment. So,

**[9:22]** we've got a complete, which means that

**[9:24]** it's sufficient and necessary. So, if I

**[9:26]** take it away, we get a new

**[9:27]** classification. So, the question is

**[9:29]** then, what is that new classification?

**[9:31]** So, we call that one the inverse, which

**[9:34]** is not a very exciting name. And this

**[9:35]** may or may not exist. So, again, if the

**[9:39]** models were really doing what we wanted,

**[9:42]** the complete signal

**[9:43]** sufficient and necessary should be

**[9:45]** everything.

**[9:46]** There should be no inverse. It shouldn't

**[9:48]** be possible to change the classification

**[9:50]** by just subtracting

**[9:52]** a couple of frequencies.

**[9:54]** Um now, I've got an example we can

**[9:56]** listen to. Full disclosure,

**[9:59]** I chose an extreme example

**[10:00]** >> [laughter]

**[10:00]** >> so that you can really hear the

**[10:02]** difference.

**[10:03]** Um

**[10:05]** So, let's have a listen. Okay, so what

**[10:07]** we have here is uh an example that I

**[10:11]** pre-recorded. I was going to do it live,

**[10:13]** but you know, nerves got the better of

**[10:15]** me. So, uh it's my 11-year-old son on

**[10:18]** drums. Hi, William. Um so, it's it's a

**[10:22]** basic blues. I think we'll agree that

**[10:23]** it's the blues.

**[10:28]** I apologize for the rubbish guitar solo

**[10:29]** over the top. I'm not a blues player.

**[10:33]** >> It sounds bluesy to me. It's decent.

**[10:38]** >> You get the idea. So, that's the

**[10:40]** original audio.

**[10:41]** So, remember that we talked about

**[10:43]** sufficient signals. What is the minimal

**[10:47]** number of frequencies I can pass in to a

**[10:49]** classifier? I'm not going to tell you

**[10:50]** which classifier. It's publicly

**[10:52]** available, but I don't want to embarrass

**[10:53]** them cuz it's not a particularly good

**[10:55]** classifier. What is the minimal number

**[10:57]** of frequencies I can pass in

**[11:00]** to get back the classification blues?

**[11:02]** And the beautiful thing is we can listen

**[11:04]** to it. So, it's here. This is it.

**[11:08]** Let's compare it to the original.

**[11:11]** I broadly speaking, you can see it's got

**[11:14]** louder bits in the same sort of place.

**[11:16]** It follows vaguely the same sort of

**[11:18]** contour, but you can see it's not the

**[11:19]** same.

**[11:20]** Do you want to hear it?

**[11:21]** >> Let's have a listen.

**[11:23]** >> [music]

**[11:25]** >> The blues.

**[11:28]** >> Well, you've made it blue on the screen.

**[11:29]** I mean, that's the only blue thing about

**[11:31]** it.

**[11:31]** >> I wish that were deliberate. That was

**[11:33]** random.

**[11:34]** So, that's

**[11:36]** >> like some kind of I know what it sounds

**[11:38]** like, the noise some of these electric

**[11:40]** cars make when they're going slowly.

**[11:42]** >> [laughter]

**[11:43]** >> Yeah, I suppose so. Yeah. So, are you

**[11:45]** telling me that they're they're playing

**[11:46]** the blues as they as they sort of drive

**[11:48]** along?

**[11:49]** Um

**[11:50]** So,

**[11:51]** that

**[11:52]** against all reasonable definitions is

**[11:56]** the blues

**[11:57]** for this particular model.

**[11:59]** So, I also talked about um

**[12:01]** sufficient and necessary. So, we would

**[12:03]** hope this is slightly better. So,

**[12:05]** sufficient can be really really really

**[12:07]** small. Remember that the model

**[12:09]** >> So, it would still classify that as the

**[12:11]** blues even if it was just that sound we

**[12:13]** just heard. That's

**[12:14]** >> That is the blues. That's That's the

**[12:15]** absolute minimum.

**[12:16]** >> Minimum, yeah.

**[12:17]** >> Okay, so we've now we're going to ask

**[12:19]** ourselves a question, what is sufficient

**[12:20]** and necessary?

**[12:22]** I suppose ideally we would hope that

**[12:25]** this sounds better, this sounds more

**[12:26]** like the blues. If we look at the actual

**[12:28]** signal,

**[12:30]** it's quite intriguing. So, remember that

**[12:32]** we're removing frequencies from all

**[12:35]** sorts of different parts of the

**[12:36]** frequency range. And for this simple

**[12:38]** experiment, I just set them to zero. You

**[12:40]** don't have to set them to zero, really.

**[12:41]** You can do anything you want, but zero

**[12:43]** seems reasonable. It's basically turning

**[12:45]** off that frequency. So, if we look at

**[12:46]** it,

**[12:47]** it actually kind of looks a bit like

**[12:49]** it's been brick walled. So, I don't know

**[12:50]** if you know this this term. So, in the

**[12:52]** early 2000s, maybe even earlier, there

**[12:55]** was a period in music that I called the

**[12:56]** the sound wars or the volume wars.

**[12:59]** And everybody just had to be louder and

**[13:00]** louder and louder. So, the way you do

**[13:02]** that is you make the really loud parts

**[13:04]** quieter,

**[13:05]** and then then you can make the quieter

**[13:07]** parts louder.

**[13:09]** Um and you end up with looks something

**[13:10]** that looks like this, everything equally

**[13:12]** loud.

**[13:13]** So, we can listen to this. So, remember

**[13:15]** this is the blues

**[13:17]** by itself is the blues.

**[13:21]** And if I remove this from this,

**[13:26]** it's no longer the blues. What I have

**[13:27]** left over is not the blues. So, let's

**[13:29]** listen to this.

**[13:31]** And let's see what you think.

**[13:38]** >> [music]

**[13:39]** >> That's reasonable, isn't it?

**[13:45]** >> Interesting that the bass is gone.

**[13:47]** >> Yeah.

**[13:49]** And a lot of the drums is gone. In fact,

**[13:50]** what it's really holding on to is is my

**[13:52]** amazing guitar playing.

**[13:54]** >> [laughter]

**[13:56]** >> So, so clearly my my guitar playing

**[13:59]** is the blues, which is not a compliment

**[14:01]** because the model also thinks that this

**[14:04]** is the blues. So, hmm, not sure about

**[14:07]** that. Okay, so the last question we can

**[14:09]** ask is

**[14:11]** if we do subtract this

**[14:13]** from this,

**[14:17]** do we have enough signal left over

**[14:19]** to

**[14:20]** send to the classifier? In this case, we

**[14:21]** do. We don't always. This case, we do.

**[14:24]** And we can ask what what is it?

**[14:27]** So, let's just solo that.

**[14:30]** >> [music]

**[14:33]** >> Where's that bass?

**[14:35]** >> There's the bass.

**[14:37]** So, [music]

**[14:38]** and the guitar is a lot less prominent,

**[14:39]** and the drums are much more prominent.

**[14:41]** So, this is not the blues. What it What

**[14:44]** is it?

**[14:45]** >> Okay, the Well, what would it classify

**[14:48]** it as?

**[14:48]** >> Yeah. You've got 10 options. I can't

**[14:50]** remember all 10, but I'll give you hip

**[14:52]** hop, rock, heavy metal, reggae, pop.

**[14:58]** They're five choices for you. It's one

**[14:59]** of those.

**[14:59]** >> My uh my clever hands is going to say

**[15:01]** rock.

**[15:03]** >> Your clever hands is going to be shot

**[15:04]** and and turned into glue, I'm afraid. Uh

**[15:06]** that's classified as hip hop.

**[15:08]** >> Okay.

**[15:08]** >> Um

**[15:09]** and I don't know enough about hip hop

**[15:12]** actually to say if that's reasonable.

**[15:14]** I suppose you could say that as a

**[15:15]** sample, it could be used in a hip hop

**[15:17]** context, but I think most people would

**[15:20]** agree that that by itself is not hip

**[15:21]** hop. But the model says it is.

**[15:25]** So,

**[15:26]** what does it all mean? It means your

**[15:28]** model, this model at least, is a clever

**[15:29]** hands. And unfortunately, it's not even

**[15:31]** that clever because actually it's really

**[15:33]** easy to fool.

**[15:34]** Uh we've seen a sufficient signal,

**[15:37]** which doesn't sound anything like the

**[15:38]** blues. I think even if you were deaf,

**[15:40]** you would say that's not the blues. Um

**[15:42]** but the model says it is.

**[15:44]** And then worse,

**[15:46]** we can extract the blues from the audio

**[15:51]** and have something left over that to my

**[15:52]** ear at least

**[15:54]** is still kind of the blues. It's

**[15:55]** borderline.

**[15:57]** Um but the model says it's now hip hop.

**[15:59]** It doesn't just say it's hip hop, it

**[16:00]** says it's quite confident that it's hip

**[16:02]** hop. So, every model will also, in

**[16:04]** addition to the classification, gives

**[16:06]** you something that we

**[16:07]** we usually refer to as the confidence.

**[16:09]** Now, whether it really is a confidence

**[16:11]** score or not is debatable.

**[16:14]** Um but this has a score that's quite

**[16:16]** high, this particular audio. So, that

**[16:18]** had 83%

**[16:20]** confidence that that was hip hop.

**[16:22]** And at least in this room, we don't we

**[16:24]** don't agree.

**[16:26]** Um and you can do this with pretty much

**[16:27]** any model.

**[16:29]** I've chosen one here because it's quite

**[16:30]** a an extreme example where I think that

**[16:33]** the sufficient at least is not really

**[16:35]** open for debate.

**[16:36]** Um but I've tried this on many, many

**[16:38]** models

**[16:39]** and it always works. So,

**[16:43]** they are not

**[16:45]** uh listening to the music in any way

**[16:47]** that a human

**[16:49]** would understand. They are just doing

**[16:51]** frequency analysis.

**[16:53]** And sometimes they're learning the wrong

**[16:55]** thing. They're doing shortcut learning.

**[16:57]** So, they listen to this and they say,

**[16:58]** "Okay, that that's the blues. We're

**[17:01]** done." And I'll play you one more thing,

**[17:03]** which I think you might find intriguing.

**[17:04]** What if I took loads of sufficient

**[17:06]** signals, hundred of them,

**[17:08]** all for the blues and added them

**[17:09]** together and asked the question, "Is

**[17:10]** that the blues?"

**[17:12]** Well, I've done it.

**[17:13]** And it is the blues.

**[17:16]** And I'll play it for you now. So,

**[17:17]** remember this is 100 sufficient signals

**[17:20]** blended together.

**[17:22]** >> [music]

**[17:26]** >> And that is classified as the blues.

**[17:28]** >> Sounds like [music] the sort of thing

**[17:29]** you might hear in the womb or

**[17:31]** >> Yeah. It's It's a Yeah.

**[17:34]** I I played that to somebody else and

**[17:35]** they said it sounded like you were

**[17:36]** outside a tent at a festival.

**[17:38]** Uh and you know, presumably on drugs.

**[17:40]** I'm not really sure. But, um as not not

**[17:43]** any festival I've been to.

**[17:45]** But,

**[17:46]** I I suppose the point is that the these

**[17:48]** models they they do work.

**[17:51]** I mean, the accuracy of this model is

**[17:53]** very good.

**[17:54]** But, it's not working the way a human

**[17:57]** wants it to work. Or certainly not

**[17:59]** working in a way that a human

**[18:00]** understands. I think that's a reasonable

**[18:02]** assertion. And so, Stern's paper when he

**[18:04]** first looked at this in music is 14

**[18:06]** years old and he said, "Look, these

**[18:08]** models I'm testing. These are horses.

**[18:10]** These are not understanding music." It's

**[18:12]** now 14 years later

**[18:14]** and we haven't got any better.

**[18:16]** If anything, it's probably worse.

**[18:26]** >> you were dealing with financial data or

**[18:27]** weather data or something like that. The

**[18:30]** minute-by-minute or hour-by-hour

**[18:32]** fluctuations might not be important.

**[18:34]** Actually, what you want is a smoother

**[18:36]** curve. Okay?

**[18:38]** Well, how would you do that? Have a

**[18:39]** guess how you do that.

**[18:40]** >> It's averaging, isn't it?

**[18:41]** >> Just averaging.
