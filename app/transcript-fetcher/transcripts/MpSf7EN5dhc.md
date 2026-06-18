# Transcript: MpSf7EN5dhc

**URL:** https://www.youtube.com/watch?v=MpSf7EN5dhc
**Segments:** 96

---

## Full Text

Okay, so we have a brand new tool inside of 
Claude Code called the monitor tool. And I'll   be going over exactly how this works and how 
you can be using it in your own workflows. Now,   essentially what the monitor tool allows for is 
a real-time event streaming in Claude Code from   background processes, whereby events that 
you care about are being delivered from a   background process to the main session of Claude 
Code, which means that tokens are only used when   events you care about actually happen, rather than 
continuously. So for example, you can be working   on a new feature and say to Claude Code, start the 
development server and watch for errors whilst I   work on the auth feature. It will then set up 
a monitor in the background and the dev server   will be running. And whenever an error happens, 
like you may have triggered an error by clicking   around on the local preview version, then that 
would go directly into Claude Code and then it   would like identify what that issue is. So if I 
gave that command to Claude Code right now and   pressed enter, then you can see that it's set up 
a monitor right over here. And the first monitor   event came through. So we have no errors right 
now. And if I then go down, click on this, I can   then see that we have the monitor running right 
over here. And these are the monitor details. And   this is what Claude Code is looking out for. So 
it's looking out for error, warn, failed, ready,   and a few other things. And then for the shell, 
this is the npm run dev that is happening. So   I just opened up the local server. And you can 
see that it gave us a warning which appeared in   the monitor right over here because it triggered 
warning and then went back into main session. Now,   for example, if I was on the website and then 
I triggered some kind of error or something,   then that would immediately go back to Claude 
Code into this Claude Code session as a brand   new monitor event. So I could then start working 
on a feature. And then when I test in the browser,   if an error does trigger behind the scenes, then 
Claude Code will be immediately notified with the   error. So I wouldn't have to tell it every single 
time, hey, there's an error that just happened.   Now let's do a quick comparison between the other 
ways of running these commands. So previously you   could have shell commands run in the foreground. 
So you could say run the tests and then it would   run the tests in the foreground. But that would 
mean that you couldn't enter in any more commands   and have them run immediately because they would 
be queued since you have something else running   in the foreground. If you had this running in 
the background instead, then that would run in   the background all like 47 tests. And only once 
a background command exited would it actually   notify the main session, like, hey, these are the 
tests that passed and failed. So in this case,   we would only get one notification at the end 
and not know about any failures until all 47   tests had finished. But in the case of a monitor, 
if I said run the tests and like use a monitor,   then it would start running the test-like 
command. And as tests are passing and failing,   that would be passed back into the main session. 
So I could specify like run the tests and monitor   only for failed tests. In which case only 
failed tests would pass back into main session.   And then Claude Code could start immediately 
diagnosing those issues with the failed test.   So if you had tests that were running for like 
10 minutes, then Claude Code would be diagnosing   them as each one fails instead of waiting until 
those 10 minutes had passed and then diagnosing   it. And that is essentially because anything 
that matches this filter that was defined   in the monitor is being passed back into the 
main session. Now the way that it works behind   the scenes is that we have 4 parameters for the 
monitor. We have the description of what it does,   the command itself, and each line that the monitor 
detects and filters for is considered one event.   And then the timeout and whether it is persistent. 
So essentially you would describe what you want to   watch. Claude Code would then write the command 
with the right filter for it. That command would   only print when something happens and that thing 
happening would be considered one event. And each   print of that would be considered notification 
that Claude Code can then react to. So you can   kind of consider this to be a security camera 
that only alerts on motion. And the reason why   this is more efficient is because previously you 
may have had the shell running in the background   and then Claude code would have to like poll 
every 30, 60 seconds to see if there are any   errors. And every single time it checks, is it 
ready? That would be consuming a little bit of   tokens that can add up a lot over the long term. 
Whereas with the monitor, only when things match   the event does it consume tokens. Okay, now you 
may be wondering like, how is this different from   /loop? Now /loop is time-driven, which means that 
it fires a prompt every N minutes. So like firing,   hey, check the development server every 2 minutes. 
And each iteration is a full API call. But this is   a much more token-efficient strategy whereby 
this is event-driven instead. So the script   that Claude Code writes for the monitor, it would 
only filter for those events that are relevant,   which means that there are basically zero costs 
when no event is being triggered. And when you do   have a monitor, then you may essentially have two 
different types of commands running. You may have   a stream filter or a poll & diff filter. So stream 
filter would be kind of like this one that I have   running over here with the npm run dev. That 
is essentially log tailing. Essentially here,   events are being triggered in real time. 
Whereas polling may be like you're checking   an API endpoint at a certain interval, and 
then that monitor would be only delivering   events into Claude Code once a certain threshold 
is met. So this can be more handy for situations   like remote APIs and stuff like that. So let's 
actually go through a couple examples. Firstly,   you may have a file drop watcher. So you may 
want to watch a shared folder for new files   and process them as soon as they arrive. So that 
monitor would be watching that. And as soon as   that event is triggered, because that file was 
added, then Claude Code would be woken up with   that event and then start acting on immediately. 
You could also do something like setting up a   monitor for an API endpoint. So for example, you 
may be pulling a price API for a stock price,   and then Claude Code would only be notified once 
that price drops below a certain point. And that   would go back into your Claude Code session, and 
then Claude Code can do any actions based on that.   And I know some people have been using Claude Code 
recently to like basically buy and sell stocks,   which does seem like a pretty fun thing to do, and 
I may have to try myself. And this monitor tool   can be pretty useful for that as well. And next 
up, you may have some kind of business workflow   yourself that the monitor can be notifying Claude 
Code of. So you may have launched a brand new sale   and you expect to get a lot of sales, over the 
next like hour, couple hours, you can basically   get a monitor to do a polling in the background. 
And then that poll would only drive events into   Claude Code whenever something unusual happened as 
defined in the code over here. So this can also be   handy for like launches for brand new products or 
like you just deployed a change to production and   you want to monitor it for the next like 2, 
3 hours or something like that, just to make   sure the error rates certainly don't spike. And as 
soon as they do, if you were away from your desk,   then Claude Code can quickly diagnose that issue 
because you said something like, hey, can you   monitor this for the next 3 hours, our logs, and 
then notify me when the error rates spike above   like 10 errors per second or something like that. 
So I would recommend trying this yourself. The   main things that I will personally be using it for 
is the Vercel deploy and also running test suites   as well. But sometimes I also deploy servers for 
clients. And I think in situations whereby we made   a pretty critical change and then something went 
to production, we may want to monitor it for the   next couple of hours. But essentially the main 
benefit here is that rather than wasting a lot of   tokens because Claude Code is polling, it becomes 
more event-driven where it only reacts to things   that happen that you care about. Now, if you do 
like this kind of stuff and you want to learn to   be a Claude Code power user like me, then you may 
find my Claude Code Masterclass to be helpful. It   is linked down below and I will soon be removing 
the lifetime access, so it will only be yearly. So   if you do want to get lifetime access, then there 
will be a small coupon code down below for you to   get lifetime access at a small discount before the 
lifetime access is completely removed. Now, some   people from some of the world's biggest companies 
have already taken this and have gone on to be   the best Claude code users at their companies. So 
you may also find it helpful for that reason too.

---

## Timestamped Segments

**[0:00]** Okay, so we have a brand new tool inside of 
Claude Code called the monitor tool. And I'll  

**[0:05]** be going over exactly how this works and how 
you can be using it in your own workflows. Now,  

**[0:10]** essentially what the monitor tool allows for is 
a real-time event streaming in Claude Code from  

**[0:16]** background processes, whereby events that 
you care about are being delivered from a  

**[0:20]** background process to the main session of Claude 
Code, which means that tokens are only used when  

**[0:26]** events you care about actually happen, rather than 
continuously. So for example, you can be working  

**[0:32]** on a new feature and say to Claude Code, start the 
development server and watch for errors whilst I  

**[0:37]** work on the auth feature. It will then set up 
a monitor in the background and the dev server  

**[0:41]** will be running. And whenever an error happens, 
like you may have triggered an error by clicking  

**[0:46]** around on the local preview version, then that 
would go directly into Claude Code and then it  

**[0:51]** would like identify what that issue is. So if I 
gave that command to Claude Code right now and  

**[0:56]** pressed enter, then you can see that it's set up 
a monitor right over here. And the first monitor  

**[1:01]** event came through. So we have no errors right 
now. And if I then go down, click on this, I can  

**[1:06]** then see that we have the monitor running right 
over here. And these are the monitor details. And  

**[1:12]** this is what Claude Code is looking out for. So 
it's looking out for error, warn, failed, ready,  

**[1:17]** and a few other things. And then for the shell, 
this is the npm run dev that is happening. So  

**[1:21]** I just opened up the local server. And you can 
see that it gave us a warning which appeared in  

**[1:26]** the monitor right over here because it triggered 
warning and then went back into main session. Now,  

**[1:31]** for example, if I was on the website and then 
I triggered some kind of error or something,  

**[1:35]** then that would immediately go back to Claude 
Code into this Claude Code session as a brand  

**[1:39]** new monitor event. So I could then start working 
on a feature. And then when I test in the browser,  

**[1:43]** if an error does trigger behind the scenes, then 
Claude Code will be immediately notified with the  

**[1:48]** error. So I wouldn't have to tell it every single 
time, hey, there's an error that just happened.  

**[1:52]** Now let's do a quick comparison between the other 
ways of running these commands. So previously you  

**[1:57]** could have shell commands run in the foreground. 
So you could say run the tests and then it would  

**[2:01]** run the tests in the foreground. But that would 
mean that you couldn't enter in any more commands  

**[2:06]** and have them run immediately because they would 
be queued since you have something else running  

**[2:10]** in the foreground. If you had this running in 
the background instead, then that would run in  

**[2:14]** the background all like 47 tests. And only once 
a background command exited would it actually  

**[2:19]** notify the main session, like, hey, these are the 
tests that passed and failed. So in this case,  

**[2:24]** we would only get one notification at the end 
and not know about any failures until all 47  

**[2:29]** tests had finished. But in the case of a monitor, 
if I said run the tests and like use a monitor,  

**[2:35]** then it would start running the test-like 
command. And as tests are passing and failing,  

**[2:39]** that would be passed back into the main session. 
So I could specify like run the tests and monitor  

**[2:44]** only for failed tests. In which case only 
failed tests would pass back into main session.  

**[2:50]** And then Claude Code could start immediately 
diagnosing those issues with the failed test.  

**[2:54]** So if you had tests that were running for like 
10 minutes, then Claude Code would be diagnosing  

**[2:59]** them as each one fails instead of waiting until 
those 10 minutes had passed and then diagnosing  

**[3:04]** it. And that is essentially because anything 
that matches this filter that was defined  

**[3:08]** in the monitor is being passed back into the 
main session. Now the way that it works behind  

**[3:13]** the scenes is that we have 4 parameters for the 
monitor. We have the description of what it does,  

**[3:18]** the command itself, and each line that the monitor 
detects and filters for is considered one event.  

**[3:23]** And then the timeout and whether it is persistent. 
So essentially you would describe what you want to  

**[3:28]** watch. Claude Code would then write the command 
with the right filter for it. That command would  

**[3:32]** only print when something happens and that thing 
happening would be considered one event. And each  

**[3:38]** print of that would be considered notification 
that Claude Code can then react to. So you can  

**[3:42]** kind of consider this to be a security camera 
that only alerts on motion. And the reason why  

**[3:46]** this is more efficient is because previously you 
may have had the shell running in the background  

**[3:52]** and then Claude code would have to like poll 
every 30, 60 seconds to see if there are any  

**[3:56]** errors. And every single time it checks, is it 
ready? That would be consuming a little bit of  

**[4:01]** tokens that can add up a lot over the long term. 
Whereas with the monitor, only when things match  

**[4:06]** the event does it consume tokens. Okay, now you 
may be wondering like, how is this different from  

**[4:10]** /loop? Now /loop is time-driven, which means that 
it fires a prompt every N minutes. So like firing,  

**[4:18]** hey, check the development server every 2 minutes. 
And each iteration is a full API call. But this is  

**[4:24]** a much more token-efficient strategy whereby 
this is event-driven instead. So the script  

**[4:29]** that Claude Code writes for the monitor, it would 
only filter for those events that are relevant,  

**[4:33]** which means that there are basically zero costs 
when no event is being triggered. And when you do  

**[4:38]** have a monitor, then you may essentially have two 
different types of commands running. You may have  

**[4:43]** a stream filter or a poll & diff filter. So stream 
filter would be kind of like this one that I have  

**[4:49]** running over here with the npm run dev. That 
is essentially log tailing. Essentially here,  

**[4:54]** events are being triggered in real time. 
Whereas polling may be like you're checking  

**[4:58]** an API endpoint at a certain interval, and 
then that monitor would be only delivering  

**[5:03]** events into Claude Code once a certain threshold 
is met. So this can be more handy for situations  

**[5:09]** like remote APIs and stuff like that. So let's 
actually go through a couple examples. Firstly,  

**[5:13]** you may have a file drop watcher. So you may 
want to watch a shared folder for new files  

**[5:19]** and process them as soon as they arrive. So that 
monitor would be watching that. And as soon as  

**[5:23]** that event is triggered, because that file was 
added, then Claude Code would be woken up with  

**[5:28]** that event and then start acting on immediately. 
You could also do something like setting up a  

**[5:32]** monitor for an API endpoint. So for example, you 
may be pulling a price API for a stock price,  

**[5:38]** and then Claude Code would only be notified once 
that price drops below a certain point. And that  

**[5:43]** would go back into your Claude Code session, and 
then Claude Code can do any actions based on that.  

**[5:48]** And I know some people have been using Claude Code 
recently to like basically buy and sell stocks,  

**[5:53]** which does seem like a pretty fun thing to do, and 
I may have to try myself. And this monitor tool  

**[5:58]** can be pretty useful for that as well. And next 
up, you may have some kind of business workflow  

**[6:02]** yourself that the monitor can be notifying Claude 
Code of. So you may have launched a brand new sale  

**[6:08]** and you expect to get a lot of sales, over the 
next like hour, couple hours, you can basically  

**[6:13]** get a monitor to do a polling in the background. 
And then that poll would only drive events into  

**[6:18]** Claude Code whenever something unusual happened as 
defined in the code over here. So this can also be  

**[6:25]** handy for like launches for brand new products or 
like you just deployed a change to production and  

**[6:30]** you want to monitor it for the next like 2, 
3 hours or something like that, just to make  

**[6:34]** sure the error rates certainly don't spike. And as 
soon as they do, if you were away from your desk,  

**[6:39]** then Claude Code can quickly diagnose that issue 
because you said something like, hey, can you  

**[6:43]** monitor this for the next 3 hours, our logs, and 
then notify me when the error rates spike above  

**[6:49]** like 10 errors per second or something like that. 
So I would recommend trying this yourself. The  

**[6:53]** main things that I will personally be using it for 
is the Vercel deploy and also running test suites  

**[6:58]** as well. But sometimes I also deploy servers for 
clients. And I think in situations whereby we made  

**[7:04]** a pretty critical change and then something went 
to production, we may want to monitor it for the  

**[7:09]** next couple of hours. But essentially the main 
benefit here is that rather than wasting a lot of  

**[7:13]** tokens because Claude Code is polling, it becomes 
more event-driven where it only reacts to things  

**[7:18]** that happen that you care about. Now, if you do 
like this kind of stuff and you want to learn to  

**[7:22]** be a Claude Code power user like me, then you may 
find my Claude Code Masterclass to be helpful. It  

**[7:28]** is linked down below and I will soon be removing 
the lifetime access, so it will only be yearly. So  

**[7:34]** if you do want to get lifetime access, then there 
will be a small coupon code down below for you to  

**[7:38]** get lifetime access at a small discount before the 
lifetime access is completely removed. Now, some  

**[7:44]** people from some of the world's biggest companies 
have already taken this and have gone on to be  

**[7:48]** the best Claude code users at their companies. So 
you may also find it helpful for that reason too.
