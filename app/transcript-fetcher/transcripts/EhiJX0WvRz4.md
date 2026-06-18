# Transcript: EhiJX0WvRz4

**URL:** https://www.youtube.com/watch?v=EhiJX0WvRz4
**Segments:** 241

---

## Full Text

Okay, so there's a brand new feature coming soon to cloud code known as ultra review. And whilst this feature will not be available to everyone right now, I did a bit of reverse engineering so I could get access to it early. Now, as the name would suggest, you would expect this to be a really good like review feature, much better than the default like /re built into cloud code. So bear in mind, we already have a /re to review a pull request. But now with this new feature enabled, if you do / ultra review, then you can see that it says roughly 10 to 20 minutes finds and verifies bugs in your branch for either like your local changes or a PR and it runs in cloud code on the cloud. So if I do / ultra review and then pass in a PR that I'm working on, which is a number 16, this has about 11,000 lines added to a codebase because it's like a pretty complicated voice calling feature. So running this command, this will then spin up a ultra reviewing session on the cloud code web version. So you can see it says that it's running on the cloud and it says this is free ultra review 2 out of free. So I'm on the $200 MO plan and it seems that we get a couple free ultra reviews right now. Anyways, going over to web session, this is what it looks like on the cloud code web. So it seems that we have a couple different stages running. We have the setup stage, the fine stage, the verify stage and the ddup stage. So essentially what's happening is that after running ultra review then it essentially spins out five independent sub aents on the cloud version of cloud code in the finding stage and you can see it found 47 candidates over here to find bugs throughout the entire codebase. So imagine what's happening is that each of them is starting in a different position on the codebase and then following a different path for any recent changes that have happened because the order in which things are loaded into context window can reveal a bug. But if that order is swapped then that bug can be like hidden to model or harder for the model to spot. And as I previously talked about in my cloud code masterass link down below if you're interested it's likely that these sub agents have personas. So one could be focused on billing, another could be focused on security. And the more sub agents as ultra reviews running behind the scenes, it's likely that even more personas are running. And the reason I know that five sub agents have been spun up is that when you look through the binary file of cloud code, then you essentially find that this feature is hidden under the word bug hunter and there is a default bug hunter fleet size of five with a maximum up to 20. NS20 may be for like enterprise organizations who are paying for like extra reviews or something like that. But as far as I know, this is not configurable right now. It's only on the Enthropic servers. So we can see that these sub agents have found 64 candidates for potential bugs. And these are all the bugs that are listed right over here and a brief description of each of the bugs and what potentially may be the problem. Now, this verifying stage is pretty interesting because essentially, you may have found with certain reviewing tools. They give you a bug and then you check and it's not actually a real bug. It just made something up instead. So, stage three is basically this independent verifier where we have another sub agent or a set of sub aents. It's not entirely clear to verify that these are actually bugs independently. So, right now we have one confirmed bug and one refuted. And it seems to be going in order one by one trying to verify each of these bugs. It's not exactly clear if this is happening each time in a brand new session or within the same like sub agent instead. And finally at the very end we will have a ddup stage whereby it may be the case that many of these sub aents that found these bugs actually found the same bug but like from two different angles or two different forms and the ddup stage basically combines it all into one unique finding instead. So as I mentioned over here, this may take between 10 to 20 minutes on the cloud version of cloud code. So I will come back to this later in the video once it is done so we can see the final stages. Now as a short aside, if you are interested in all things cloud code from a power user, then I do have a free newsletter all about this. There's a link down below and by signing up you get access to a bunch of free videos from my master class as well. So we can see that the verifying stage has refuted nine bugs so far. But essentially what I find interesting about this approach is that maybe with your traditional cloud code review so far, your current reviewing tool may just be flagging things and just leading to a lot of false positives instead or potentially doing the reverse and ignoring a bunch of issues. But what I find interesting about this ultra review approach that the Enthropic team created whereby it's verifying which bugs are actually bugs, it kind of prevents cloud code from making unnecessary changes for false positives. So I think that has been like the most unique part about this approach that I want to be integrating into my own workflows going forwards. And I think that really matters especially if you have a lot of different sub agents trying to find bugs from different angles because many of those issues may actually be non-issues or combined into an existing issue already. Now, whilst this feature is hidden behind a feature flag and you may not be able to reverse engineer it to get access to a feature, but the same pattern still applies whereby if you're making a multi- aent review, you want to have a verification synthesizing step whereby it's actually making sure that those things that were flagged are serious issues, especially for really big PRs kind of like this one which has 11,000 lines. So, you can still be applying this verification pattern to whichever review that you're doing. So, for example, I also use a built-in review, which reviews a pull request locally for the same pull request, which we'll be doing a comparison at the end to see which one is better. But essentially, the normal review built into cloud code, not the ultra review, does not have a verification step because it just spins up a bunch of sub aents to find bugs. Each of them being a sonnet sub aent instead, and then it just gives me the list from all the sub aents combined. So, so far the ultra review has been running for about 17 minutes and it's still underway, whereas the local review ran for about 3 to 4 minutes instead. And I think one of the reasons they added this brand new feature is because they may want to be testing this AB testing this going forwards with different sub agent configurations and different sub agent prompts that they have running in the cloud and potentially mixing different models including unreleased models as well. So I made a fleet review skill myself based on this idea whereby essentially what this fleet review skill is doing is that it spins up free claude code sub aents to try and find bugs and also free codec sub aents via the codeci headless mode to try and find those bugs as well. And then it passes it through a verify stage. So there will be a claude code verifier and then also a codeex verifier to make sure those bugs are actually real bugs. And this stage is pretty important because sometimes you will find that codeex says that a bug that cla code found isn't actually a real bug and the reverse also happens whereby codeex finds a bug and then claude says it's not a bug. So I think that by combining these two verification stages you may get a better output. So then I got chargex to compare the local review which is review one with the ultra review. So the way that I would kind of describe it is that SL review is kind of doing a quick audit of the entire codebase and everything that deviates from the mean slightly, it's just flagging as an issue. And the second review is kind of like an attacker instead. So it's trying to pick one path of this entire PR and breaking it anyway. So it kind of found some race conditions and life cycle bugs that the first review completely missed. Did a better job at holding like many different files in its mind together. So anyways, because it seems that we're only going to be getting free free ultra reviews, it may be the case that like this is just much more expensive for them to run like on their cloud or they may be using a different model in some way. Maybe they would be using some elements of the mystra review. So it seems that you would want to do a quick/ review for a PR or a new feature and then maybe use codeex as well to find any more bugs with another review. And if the feature is really important or really big, you may want to do a / ultra review as well once it is released. Anyways, if you do like this kind of stuff, then do subscribe to the channel because I do make the most in-depth videos on cloud code on YouTube. And if you're interested in learning more about cloud code, then I have a whole master class all about this linked down below.

---

## Timestamped Segments

**[0:00]** Okay, so there's a brand new feature

**[0:01]** coming soon to cloud code known as ultra

**[0:04]** review. And whilst this feature will not

**[0:06]** be available to everyone right now, I

**[0:08]** did a bit of reverse engineering so I

**[0:10]** could get access to it early. Now, as

**[0:12]** the name would suggest, you would expect

**[0:13]** this to be a really good like review

**[0:15]** feature, much better than the default

**[0:17]** like /re built into cloud code. So bear

**[0:21]** in mind, we already have a /re to review

**[0:23]** a pull request. But now with this new

**[0:26]** feature enabled, if you do / ultra

**[0:28]** review, then you can see that it says

**[0:30]** roughly 10 to 20 minutes finds and

**[0:32]** verifies bugs in your branch for either

**[0:34]** like your local changes or a PR and it

**[0:37]** runs in cloud code on the cloud. So if I

**[0:40]** do / ultra review and then pass in a PR

**[0:43]** that I'm working on, which is a number

**[0:45]** 16, this has about 11,000 lines added to

**[0:48]** a codebase because it's like a pretty

**[0:50]** complicated voice calling feature. So

**[0:52]** running this command, this will then

**[0:54]** spin up a ultra reviewing session on the

**[0:57]** cloud code web version. So you can see

**[0:59]** it says that it's running on the cloud

**[1:01]** and it says this is free ultra review 2

**[1:04]** out of free. So I'm on the $200 MO plan

**[1:07]** and it seems that we get a couple free

**[1:09]** ultra reviews right now. Anyways, going

**[1:11]** over to web session, this is what it

**[1:13]** looks like on the cloud code web. So it

**[1:15]** seems that we have a couple different

**[1:17]** stages running. We have the setup stage,

**[1:19]** the fine stage, the verify stage and the

**[1:21]** ddup stage. So essentially what's

**[1:23]** happening is that after running ultra

**[1:25]** review then it essentially spins out

**[1:28]** five independent sub aents on the cloud

**[1:30]** version of cloud code in the finding

**[1:32]** stage and you can see it found 47

**[1:34]** candidates over here to find bugs

**[1:37]** throughout the entire codebase. So

**[1:38]** imagine what's happening is that each of

**[1:40]** them is starting in a different position

**[1:41]** on the codebase and then following a

**[1:43]** different path for any recent changes

**[1:45]** that have happened because the order in

**[1:47]** which things are loaded into context

**[1:48]** window can reveal a bug. But if that

**[1:51]** order is swapped then that bug can be

**[1:53]** like hidden to model or harder for the

**[1:54]** model to spot. And as I previously

**[1:56]** talked about in my cloud code masterass

**[1:58]** link down below if you're interested

**[2:00]** it's likely that these sub agents have

**[2:02]** personas. So one could be focused on

**[2:04]** billing, another could be focused on

**[2:05]** security. And the more sub agents as

**[2:07]** ultra reviews running behind the scenes,

**[2:09]** it's likely that even more personas are

**[2:11]** running. And the reason I know that five

**[2:12]** sub agents have been spun up is that

**[2:14]** when you look through the binary file of

**[2:16]** cloud code, then you essentially find

**[2:18]** that this feature is hidden under the

**[2:20]** word bug hunter and there is a default

**[2:22]** bug hunter fleet size of five with a

**[2:26]** maximum up to 20. NS20 may be for like

**[2:29]** enterprise organizations who are paying

**[2:30]** for like extra reviews or something like

**[2:32]** that. But as far as I know, this is not

**[2:35]** configurable right now. It's only on the

**[2:37]** Enthropic servers. So we can see that

**[2:39]** these sub agents have found 64

**[2:41]** candidates for potential bugs. And these

**[2:43]** are all the bugs that are listed right

**[2:44]** over here and a brief description of

**[2:47]** each of the bugs and what potentially

**[2:49]** may be the problem. Now, this verifying

**[2:52]** stage is pretty interesting because

**[2:54]** essentially, you may have found with

**[2:56]** certain reviewing tools. They give you a

**[2:58]** bug and then you check and it's not

**[3:00]** actually a real bug. It just made

**[3:02]** something up instead. So, stage three is

**[3:04]** basically this independent verifier

**[3:06]** where we have another sub agent or a set

**[3:08]** of sub aents. It's not entirely clear to

**[3:11]** verify that these are actually bugs

**[3:13]** independently. So, right now we have one

**[3:15]** confirmed bug and one refuted. And it

**[3:17]** seems to be going in order one by one

**[3:19]** trying to verify each of these bugs.

**[3:21]** It's not exactly clear if this is

**[3:23]** happening each time in a brand new

**[3:25]** session or within the same like sub

**[3:27]** agent instead. And finally at the very

**[3:29]** end we will have a ddup stage whereby it

**[3:32]** may be the case that many of these sub

**[3:34]** aents that found these bugs actually

**[3:36]** found the same bug but like from two

**[3:38]** different angles or two different forms

**[3:40]** and the ddup stage basically combines it

**[3:42]** all into one unique finding instead. So

**[3:45]** as I mentioned over here, this may take

**[3:46]** between 10 to 20 minutes on the cloud

**[3:48]** version of cloud code. So I will come

**[3:50]** back to this later in the video once it

**[3:52]** is done so we can see the final stages.

**[3:54]** Now as a short aside, if you are

**[3:55]** interested in all things cloud code from

**[3:57]** a power user, then I do have a free

**[3:59]** newsletter all about this. There's a

**[4:01]** link down below and by signing up you

**[4:03]** get access to a bunch of free videos

**[4:04]** from my master class as well. So we can

**[4:06]** see that the verifying stage has refuted

**[4:08]** nine bugs so far. But essentially what I

**[4:11]** find interesting about this approach is

**[4:13]** that maybe with your traditional cloud

**[4:15]** code review so far, your current

**[4:16]** reviewing tool may just be flagging

**[4:18]** things and just leading to a lot of

**[4:20]** false positives instead or potentially

**[4:21]** doing the reverse and ignoring a bunch

**[4:23]** of issues. But what I find interesting

**[4:25]** about this ultra review approach that

**[4:26]** the Enthropic team created whereby it's

**[4:28]** verifying which bugs are actually bugs,

**[4:30]** it kind of prevents cloud code from

**[4:32]** making unnecessary changes for false

**[4:34]** positives. So I think that has been like

**[4:36]** the most unique part about this approach

**[4:38]** that I want to be integrating into my

**[4:39]** own workflows going forwards. And I

**[4:41]** think that really matters especially if

**[4:43]** you have a lot of different sub agents

**[4:45]** trying to find bugs from different

**[4:46]** angles because many of those issues may

**[4:48]** actually be non-issues or combined into

**[4:51]** an existing issue already. Now, whilst

**[4:52]** this feature is hidden behind a feature

**[4:54]** flag and you may not be able to reverse

**[4:56]** engineer it to get access to a feature,

**[4:58]** but the same pattern still applies

**[5:00]** whereby if you're making a multi- aent

**[5:02]** review, you want to have a verification

**[5:06]** synthesizing step whereby it's actually

**[5:08]** making sure that those things that were

**[5:09]** flagged are serious issues, especially

**[5:12]** for really big PRs kind of like this one

**[5:14]** which has 11,000 lines. So, you can

**[5:16]** still be applying this verification

**[5:18]** pattern to whichever review that you're

**[5:20]** doing. So, for example, I also use a

**[5:22]** built-in review, which reviews a pull

**[5:24]** request locally for the same pull

**[5:26]** request, which we'll be doing a

**[5:28]** comparison at the end to see which one

**[5:29]** is better. But essentially, the normal

**[5:31]** review built into cloud code, not the

**[5:33]** ultra review, does not have a

**[5:35]** verification step because it just spins

**[5:38]** up a bunch of sub aents to find bugs.

**[5:40]** Each of them being a sonnet sub aent

**[5:42]** instead, and then it just gives me the

**[5:43]** list from all the sub aents combined.

**[5:45]** So, so far the ultra review has been

**[5:47]** running for about 17 minutes and it's

**[5:49]** still underway, whereas the local review

**[5:51]** ran for about 3 to 4 minutes instead.

**[5:53]** And I think one of the reasons they

**[5:55]** added this brand new feature is because

**[5:56]** they may want to be testing this AB

**[5:58]** testing this going forwards with

**[6:00]** different sub agent configurations and

**[6:02]** different sub agent prompts that they

**[6:03]** have running in the cloud and

**[6:05]** potentially mixing different models

**[6:07]** including unreleased models as well. So

**[6:09]** I made a fleet review skill myself based

**[6:12]** on this idea whereby essentially what

**[6:14]** this fleet review skill is doing is that

**[6:17]** it spins up free claude code sub aents

**[6:20]** to try and find bugs and also free codec

**[6:22]** sub aents via the codeci headless mode

**[6:25]** to try and find those bugs as well. And

**[6:27]** then it passes it through a verify

**[6:29]** stage. So there will be a claude code

**[6:32]** verifier and then also a codeex verifier

**[6:35]** to make sure those bugs are actually

**[6:36]** real bugs. And this stage is pretty

**[6:38]** important because sometimes you will

**[6:39]** find that codeex says that a bug that

**[6:42]** cla code found isn't actually a real bug

**[6:44]** and the reverse also happens whereby

**[6:45]** codeex finds a bug and then claude says

**[6:48]** it's not a bug. So I think that by

**[6:49]** combining these two verification stages

**[6:52]** you may get a better output. So then I

**[6:53]** got chargex to compare the local review

**[6:57]** which is review one with the ultra

**[6:59]** review. So the way that I would kind of

**[7:01]** describe it is that SL review is kind of

**[7:03]** doing a quick audit of the entire

**[7:04]** codebase and everything that deviates

**[7:06]** from the mean slightly, it's just

**[7:08]** flagging as an issue. And the second

**[7:10]** review is kind of like an attacker

**[7:11]** instead. So it's trying to pick one path

**[7:14]** of this entire PR and breaking it

**[7:16]** anyway. So it kind of found some race

**[7:18]** conditions and life cycle bugs that the

**[7:20]** first review completely missed. Did a

**[7:22]** better job at holding like many

**[7:24]** different files in its mind together. So

**[7:26]** anyways, because it seems that we're

**[7:28]** only going to be getting free free ultra

**[7:30]** reviews, it may be the case that like

**[7:32]** this is just much more expensive for

**[7:33]** them to run like on their cloud or they

**[7:36]** may be using a different model in some

**[7:38]** way. Maybe they would be using some

**[7:40]** elements of the mystra

**[7:43]** review. So it seems that you would want

**[7:44]** to do a quick/ review for a PR or a new

**[7:47]** feature and then maybe use codeex as

**[7:49]** well to find any more bugs with another

**[7:52]** review. And if the feature is really

**[7:54]** important or really big, you may want to

**[7:55]** do a / ultra review as well once it is

**[7:58]** released. Anyways, if you do like this

**[8:00]** kind of stuff, then do subscribe to the

**[8:01]** channel because I do make the most

**[8:02]** in-depth videos on cloud code on

**[8:04]** YouTube. And if you're interested in

**[8:05]** learning more about cloud code, then I

**[8:07]** have a whole master class all about this

**[8:09]** linked down below.
