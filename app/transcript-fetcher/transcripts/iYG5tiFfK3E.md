# Transcript: This Claude Skill Watches Videos So You Don't Have To

**URL:** https://www.youtube.com/watch?v=iYG5tiFfK3E
**Segments:** 102
**Channel:** Taoufik
**Duration:** 3:56
**Uploaded:** 2026-06-12

---

## Full Text

While still completing on the first chapter, as you can see here, it gives me all the information that I need. So, I'll show you right now the Claude scale that I gave it to Claude, so it will be able to watch YouTube videos, Zoom calls, or Loom videos. Anything with a link, you give it to Claude and it will be able to watch it. So, I'm going to show you how it works, what it does, and how to install it in your own machine. Links in the description. Before I used to use transcript tools on YouTube videos when I wanted Claude code to analyze the transcript as well as the transcript for meetings and Zoom calls and so on. However, there was always a missing piece, which was the visual side of the video. Then I discovered this skill shared by a guy named Brad. Shout out to him. So, when I give it something like this, a 10-hour course from Netcode, it just couldn't keep up. It skipped what was on screen. So, I've spent some times and fixed it, and it can actually see what's happening, the motion graphics, the edits, the b-roll. So, here is how it works. A video is a two things, frames and transcripts. The transcript is the easy part. However, for the frames, were the problem. The old way grabbed 100 frames from the whole video. On 1-hour video, that's one frame every 36 seconds. On a 10-hour videos, one frame every 6 minutes. So, Claude was basically just reading the transcript with a few random screenshots. So, after a lot of trials and errors, I switched to FFmpeg scene detection. So, instead of grabbing frames on a timer, it grabs one frame every time the scene actually changes. For the audio, YouTube-DL pulls the caption straight off YouTube when the video has them, which is free. If it doesn't, like Loom or Zoom calls, in this case, it fall back to Whisper or Grok. And when Claude code done watching, it asks you one question, do you want to save this into your knowledge base? For this, I use Obsidian and as you can see right now, I have whenever I watch a new video or I want to analyze new video, as you can see, this got added to my second brain where lives everything all my context. So, everything got connected here and can leverage this on the future when I want. And let me show you right now how you can use this skill. So, it's pretty simple. You just go to my GitHub repository to use the cloud code version. Simply just take the link to my GitHub and it automatically clone it for you and you can start using it right away. For example, I will take a video from, let's say, Andrej Karpathy. I hope I pronounce his name correctly. So, I just go and paste the link here. First you do {slash} watch. You will have the skill and you paste the URL and while you are watching it, so for my case, just to analyze it and I can simply say analyze this video and tell me if there is some graphics or visuals that are mentioned on this video and what are the key concepts from this video. Your case it may as well first to download the YouTube DLP and the FFmpeg. So, you don't need to do anything right now. It will watch the video and it gives you all the analysis. So, here it's finished watching the video. So, it gives me all the information as you can see and I can go through this deeply and analyze it and as well it will ask me if I want to ingest this now. Does this mean that it can add it to my context? So, it will be related to the other pages that I have on my second brain. So, this is how you can watch YouTube video while you are doing the other work. And when it's finished, it will give you the full report. And in the next video I will show you how to set up this second brain. This took me a month in order to build it correctly. I will show you how you can do it as well. So, we it for this video, and I hope you find this useful.

---

## Timestamped Segments

**[0:00]** While still completing on the first

**[0:02]** chapter, as you can see here, it gives

**[0:04]** me all the information that I need. So,

**[0:06]** I'll show you right now the Claude scale

**[0:07]** that I gave it to Claude, so it will be

**[0:09]** able to watch YouTube videos, Zoom

**[0:12]** calls, or Loom videos. Anything with a

**[0:15]** link, you give it to Claude and it will

**[0:16]** be able to watch it. So, I'm going to

**[0:18]** show you how it works, what it does, and

**[0:21]** how to install it in your own machine.

**[0:23]** Links in the description.

**[0:25]** Before I used to use transcript tools on

**[0:27]** YouTube videos when I wanted Claude code

**[0:30]** to analyze the transcript as well as the

**[0:31]** transcript for meetings and Zoom calls

**[0:34]** and so on. However, there was always a

**[0:36]** missing piece, which was the visual side

**[0:38]** of the video. Then I discovered this

**[0:40]** skill shared by a guy named Brad. Shout

**[0:43]** out to him.

**[0:45]** So, when I give it something like this,

**[0:47]** a 10-hour course from Netcode,

**[0:49]** it just couldn't keep up. It skipped

**[0:51]** what was on screen. So, I've spent some

**[0:53]** times and fixed it, and it can actually

**[0:56]** see what's happening, the motion

**[0:58]** graphics, the edits, the b-roll.

**[1:01]** So, here is how it works. A video is a

**[1:03]** two things, frames and transcripts. The

**[1:05]** transcript is the easy part. However,

**[1:08]** for the frames, were the problem. The

**[1:10]** old way grabbed 100 frames from the

**[1:12]** whole video. On 1-hour video, that's one

**[1:15]** frame every 36 seconds. On a 10-hour

**[1:18]** videos, one frame every 6 minutes. So,

**[1:22]** Claude was basically just reading the

**[1:23]** transcript with a few random

**[1:25]** screenshots. So, after a lot of trials

**[1:27]** and errors, I switched to FFmpeg scene

**[1:30]** detection. So, instead of grabbing

**[1:32]** frames on a timer, it grabs one frame

**[1:35]** every time the scene actually changes.

**[1:38]** For the audio, YouTube-DL pulls the

**[1:40]** caption straight off YouTube when the

**[1:42]** video has them, which is free. If it

**[1:44]** doesn't, like Loom or Zoom calls, in

**[1:47]** this case, it fall back to Whisper or

**[1:49]** Grok.

**[1:50]** And when Claude code done watching, it

**[1:52]** asks you one question, do you want to

**[1:54]** save this into your knowledge base? For

**[1:57]** this, I use Obsidian and as you can see

**[1:59]** right now, I have whenever I watch a new

**[2:01]** video or I want to analyze new video, as

**[2:04]** you can see, this got added to my second

**[2:06]** brain where lives everything all my

**[2:09]** context. So, everything got connected

**[2:11]** here and can leverage this on the future

**[2:13]** when I want. And let me show you right

**[2:15]** now how you can use this skill. So, it's

**[2:17]** pretty simple. You just go to my GitHub

**[2:20]** repository to use the cloud code

**[2:22]** version. Simply just take the link to my

**[2:25]** GitHub and it automatically clone it for

**[2:27]** you and you can start using it right

**[2:29]** away. For example, I will take a video

**[2:32]** from, let's say, Andrej Karpathy. I hope

**[2:35]** I pronounce his name correctly. So, I

**[2:37]** just go and paste the link here. First

**[2:40]** you do {slash} watch. You will have the

**[2:43]** skill and you paste the URL and while

**[2:47]** you are watching it, so for my case,

**[2:49]** just to analyze it and I can simply say

**[2:52]** analyze this video and tell me if there

**[2:54]** is some graphics or visuals that are

**[2:56]** mentioned on this video and what are the

**[2:58]** key concepts from this video. Your case

**[3:00]** it may as well first to download the

**[3:03]** YouTube DLP and the FFmpeg. So, you

**[3:06]** don't need to do anything right now. It

**[3:08]** will watch the video and it gives you

**[3:09]** all the analysis.

**[3:16]** So, here it's finished watching the

**[3:18]** video. So, it gives me all the

**[3:19]** information as you can see and I can go

**[3:21]** through this deeply and analyze it and

**[3:24]** as well it will ask me if I want to

**[3:26]** ingest this now. Does this mean that it

**[3:29]** can add it to my context? So, it will be

**[3:31]** related to the other pages that I have

**[3:33]** on my second brain. So, this is how you

**[3:35]** can watch YouTube video while you are

**[3:37]** doing the other work. And when it's

**[3:39]** finished, it will give you the full

**[3:41]** report. And in the next video I will

**[3:43]** show you how to set up this second

**[3:45]** brain. This took me a month in order to

**[3:47]** build it correctly. I will show you how

**[3:49]** you can do it as well. So, we it for

**[3:50]** this video, and I hope you find this

**[3:53]** useful.
