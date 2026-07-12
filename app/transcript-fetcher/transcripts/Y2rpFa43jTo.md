# Transcript: Obsidian + Claude Code: The Second Brain Setup That Actually Works

**URL:** https://www.youtube.com/watch?v=Y2rpFa43jTo
**Segments:** 609
**Channel:** Eric Tech
**Duration:** 17:09
**Uploaded:** 2026-04-06

---

## Full Text

In this video, I'm going to show exactly how to build your second brain using Claude Code and the power of Obsidian. And specifically for my use case, I use Obsidian here to manage different projects. And furthermore, I was able to use Claude Code here as like a AI assistant here to manage my notes. Right here, you can see I have a bunch of Obsidian CLI skills, which will basically help us to create better Obsidian notes. And right here, you can see one of the skills that I created called the onboarding projects, which can help me to take any data source that I have like Gmails and local files, have Claude Code here to organize, summarize those informations, and store that inside of my Obsidians using the Obsidian skills. I'm going to show you in later on this video. And pretty much, you can see that we can use Claude Code here with the power of Obsidian to basically help us to answer any questions, perform any actions on our notes. So, with that being said, that's what we're going to cover in this video. If you're interested, let's get into this. Now, before we continue, I recently launched our school community where I help you to master AI agents, automations, and so much more. And that's all coming from someone who used to work as a senior AI software engineer at companies like Amazon and Microsoft. And in this community, you're going to get over 100 plus video materials like templates and workflows that I personally built and sold over 100 plus times. On top of that, you're also going to get access to our weekly live calls. And just give you an idea, this week we're actually running a Claude Code masterclass where we're going to dive into how to improve Claude Code's accuracy. We're going to use it to building applications. Plus, you're also going to get full community supports where you're going to get a chance to ask questions and get direct answers back. So, if you're ready to level up, make sure to jump right in, and I'll see you in the community. Now, because Obsidian here is not free, the free version here doesn't allow you to sync notes or do the version control. And that's why the first step we're going to do here is basically have Obsidian here to connect it with our GitHub by first creating a repository. And any changes that we're making in our Obsidian notes, we're going to push that onto our GitHub repository. This way, we're going to have a version control and also completely free for cloud storage. So, in this case, let's take a look at how we can do this first. All right, so to get started, first thing first, we're going to do here is make sure to create our GitHub accounts. And simply, all we have to do here is just click on new right here to create a new repository. And this will basically going to be a folder we're going to dump all the data here inside of our repository in GitHub so that we have the right version control, and we can also be able to change the visibility. So, here I'm going to change that to be private because I don't want anyone else here to see the brain because you only want to use this for your cloud storage and version control. So, in this case, I'm going to give it a name for the repository, and I'm just going to call it the Eric Tech Brain. And simply, once that's done, I will just click on create new repository. And now, you can see we have a repository created inside of our GitHub. So, once we have a repository now, what we have to do here is we want to make sure to clone this inside of our local machine so we can move to add any local files here onto our GitHub for cloud storage and version control. And to do so, if you're really new to terminal and you're not really a developer, I highly recommend you just to install GitHub Desktop where you can be able to manage the entire version control and the cloud storage in a desktop graphical user interface rather than just using the terminal. So, for demonstration, I'm just going to download this onto my local machine. Now, once you have your GitHub Desktop app downloaded on your local machine, this is what it looks like. So, all we have to do here is just make sure to select the repository that I just created. For example, mine is called the Eric Tech Brain. So, there's one called Eric Tech Brain, and we can see that currently it is private. So, I'm just going to choose that and be able to clone this onto our local machine. So, I'm just going to click on clone, and it's telling you exactly where you can clone this. So, you can see that the local file path here is actually inside of documents. But if I want to change that, for example, I want to change that to be in my desktop, I can be able to change that and click on select. And then here, all I have to do here is just click on clone, and it's going to clone the repository here on our desktop folder in our local machine. So, now you can see we have the repository cloned inside of our desktop folder. The next thing we're going to do here is make sure to have Obsidian installed on our local machine as well. So, now if I were to head over to the Obsidian download page, simply all I have to do here is click on download, and it's going to download this app on our local machine. So, I'm going to download this for my Mac version. All right, so now once I have downloaded this on my Mac OS, the next thing we're going to do here is make sure to open folder as vault. So, I'm going to click on open. And then here, I'm going to click on desktop. Then we're going to click on the repository that we just cloned and click on open. And then here, you can see this is the notebook that we have for our Eric Tech Brain. So, now once we have this open, here you can see on the right, this is the entire Eric Tech folders. that we write on the Obsidian is going to be reflected inside of this folder. So, for example, if I were to create a new note, for example, here you can see this is the note. And right here on the right, you can see we have untitled.md file. So, now if I were to type in, for example, Eric Tech, and that's going to be the file name, you can see that has changed reflected right away. And if I were to create a folder in Obsidian, it's going to do the same thing here as well. So, next we're going to show you here is basically commit the changes onto our GitHub so that we have a cloud backup. So, right here, you can see if I were to open the GitHub Desktop app, currently on the left, you can see we have six changes on the files. And simply, I'm just going to give the message summary on exactly what are the changes that we have just made. I'm just going to say this is the initial summary. You can see this is the initial commit. And commit this, then click on push here to basically push that changes onto the remote, which is our GitHub repository. So, now if I were to click on the history here, you can see this is the commit that we just committed, and now has that change. So, if I want to revert it back, you can do so. So, now if I were to head over to the GitHub repository browser, here you can see this is the Eric Tech Brain. And right here, you can see this is my first initial commit, which basically means that we have successfully saved the changes onto our GitHub repository here. Now, obviously, making changes and manually have to commit this is going to be really painful. And you might be asking, "Well, is there any ways that we can be able to automatically commit this onto our GitHub repository?" And the answer here is yes. So, now if I were to head over to the Obsidian here, all we have to do here is just click on the gear icon. And basically, if I were to click on the community plugins and click on the turn on community plugins right here, now we can be able to browse a community plugins. And there's actually a plugin here that can actually help us to automatically commit these changes that we have onto our GitHub repository. So, simply all I have to do here is just click on browse. And then the plugin here is called Git. So, right here, you can see this is the plugin which integrates the Git version here with automatically backup and other advanced features. So, if I were to click on this, right here, you can see you can be able to learn more about this from this open source repository. But simply, if you want to install this, all you have to do is just click on install right here. So, right here, you can see the repository here is fully installed. And then simply, click on enable. Then we're going to click on options. And right here, you can see there's a feature called auto commit and sync after stopping file edits, which basically means that after we stop editing the files in the Obsidian, it will basically start to commit the changes that we have onto GitHub. So, simply if we were to enable this feature, and all we have to do here is set an interval on how often should it be able to sync the changes, right? It could be like every minute, right? After we stop changing or after we stop editing the files in Obsidian, it's going to automatically do that with a set interval. So, for example, it could be like 1 minute. So, that's what I'm going to set right here. And then furthermore, if you scroll down, there's also a feature called pull on startup, which basically automatically pull the latest changes from Obsidian when it starts. So, in this case, I'm just going to enable this. So, for example, maybe you're making changes from device one, and then you want to open your device two here to basically sync the changes. This will basically allow you to have that option. So, make sure to pull on startup. Okay, so now if I were to test the changes here, if I were to close this, and let's say if I were to make some changes, for example, right? So, in this case, I'm going to say example, right? And then be able to give some like words here. And then you can see here that after 1 minute, it has committed six files here automatically onto our GitHub page. So, now if I were to head over to the version control, you can see that we have all backups as well as committed automatically through the Obsidian. And if I were to head over to the repository and just refresh now, you can see we have the example.md file that we just created. And right here, you can see this is the change that we have. So, now let's say if I were to edit something, for example, say hello, and click on commit, and click on uh changes, right? So, now you can see we have some additional changes added onto this MD file. So, now you can see if I were to restart the Obsidian, it has automatically pulled the changes. Now, you can see that we have hello here inside of our notebook. So, now once we have our Obsidian notebook set up, the next thing we're going to take a look at is how we can be able to connect it with our large language model like Claude Code. And to make this process easier, we're going to use the Obsidian skill, which basically teach our AI agent here to use all the capabilities that Obsidian has like the markdown, base, JSON, canvas, all through the Obsidian CLI. And of course, if you want to have your CLI for Obsidian set up, make sure to head over to your settings for the Obsidian, and just click on the general. And then here, inside of general, there's the advanced, and we have the command line interface. So, make sure to toggle this on. It will basically allow you to interact Obsidian with CLI. Now, once we have the CLI enabled, the next thing we're going to take a look at is how we can be able to set up the Obsidian skills. So, right here, you can see simply if we want to install this, we're just going to copy the commands right here to install this either through the marketplace or the MPX skills. So, now once you have this installed, the next thing we're going to take a look at is how we can be able to use that for a practical use case. So, what I can do here is I can be able to onboard those data onto Claude Code, and Claude Code here is going to trigger the Obsidian skills that we just installed, and it's going to help us to organize and summarize everything into one single location. So, in this case, let me show you exactly how I would do that. All right, so to do so here, you can see I basically created a skill called onboard projects. And essentially, what it does here is that it will collect data from my external Gmail, right? Like basically my all my emails from a particular projects. And also for the internal files, right? Let's say if I have bunch of project contexts on my local drive, I can also be able to upload that here for this particular skill or any text that I want to paste. It will basically use the existing Obsidian skills, right? Like the markdown, the base, the CLI here to create everything, okay? And this is the entire skill structures. It will basically uses some of the scripts that I created here to like, for example, getting a email label, right? Getting the messages, getting the threads from Gmail, and then be able to fetch those things and download the attachments using this part of the skills here. And it will basically try to output it as the vault here. So, you can see it's going to output as a project folder. And then here, inside of this projects folder here, we have a projects.base, which is basically a table where we keep track of all the projects that we have. And then we also have the project name. So, that's basically whatever project like we have like ABC projects. We're going to have the overview, exactly okay, what is this project about? And then we also have the conversation log like, okay, what is the conversation summary in a chronological order for all the conversation that we have going on with this project, right? So, that we know exactly what's happening. And we also have the links on exactly okay, what are some external links. And then we also, most importantly, we have the documentations. So, there's some documents that could be like static file like NDA or agreements or contracts that we need to cap inside of the agreements that cannot be summarized, right? So, some files here shouldn't be summarized. Some of information here should be summarized and condensed it down into the conversation log. So, that this way it's much more easier for me to juggle multiple projects at the same time. So, you can see here that this is the entire five that workflow on exactly how the skill does. Right here you can see we first try to create a project. So, if the project exists already, we might just want to update or import more data on this project and that's it. If it's a new project, we're just going to create a new project here and then we also have collecting sources here. So, let's say we're going to collect like Gmail, internal, and also the paste text or screenshots. We're also going to collect that as well. And it's going to process and see if there if it's existing projects, we're going to see if there's any duplicates. And also if it's going to be new projects, we're going to filter out if it's like static file, conversations, references, key details, we're going to put them into the right place. Then furthermore, it's going to auto extract the profile. So, extract like the wiki links, the industry, and be able to update the overview.md file. And by the end of it, it's also going to generate summary on exactly what are the key events for this project, what is the timeline, and also what is the import stats. So, then you can see I basically instructed to create that skill and now we can be able to use it to onboard projects much more faster onto Obsidian. So, now if I were to restart my Clockwise session, I should now be able to use this skill called onboard projects. And now if I were to simply trigger this, it should prompt me exactly what should we call this project. So, right here you can see it's going to check the current state of the current project folder. And then there's no project exists, what's the name of the project you would like to set up. So, for example, I'm just going to call like map B, right? For example, like it doesn't matter which name you're you're using. You can see it's going to just create the project structures called map B. And here you can see it's going to create the project dashboard, creating the conversation log, and then it also has create the project base, which is how we're going to create the project status for all the projects that we have, right? So far you can see we have set up the these things, right? The overview, the conversation log, links, documents, and also the projects.base, which is the dashboard. And now what we need to do here is we need to be able to input the data source, right? Maybe you have like external like Gmail label where this label here contains bunch of emails that you have with this projects. Or and also if you have like internal files, right? Like PDF, docs, contracts from your local drive, you can be able to upload here. And also if there's any text you want to paste, any screenshots that the AI here can be able to extract from, we can also be able to paste it here into this particular skill. And it's going to help us to analyze everything and aggregate everything into this project folder structure that we have here. So, in this case, I'm first going to upload the internal local file path that I have as well as the entire Gmail label link on exactly where it contains all the data source. So, in this case, I'm just going to enter this and it's going to fetch that automatically for us. Okay, so now you can see all the local files here has been processed and now for Gmail here, the scripts are not configured because for Gmail label here, we need the uh credentials. So, right here you can see it tells you exactly how you can get the credentials like Google Cloud Console, enable Gmail API, and also create the OAuth credentials right there. So, basically you guys are going to download the JSON once after you create the OAuth two credentials. So, if I were to open this, here you can see there's the folder called dot Gmail credentials. You're just going to save your credentials here right here, right? That's it. And what essentially here you can see it from the dot env file, it actually referenced this particular folder for the credentials and tokens here to be able to fetch those emails here using those scripts. Okay, so that's exactly how it works. So, now you can see everything is all done and here is what's imported. So, we have five files here are imported to this particular projects for the documents like the service agreements, the proposal, like the project plans, uh freelancer brief, all those kind of things, right? And then we also have the Gmail, which is all the emails that we have fetched from the entire thread conversation from December all the way to April, which is in chronological order. And also here you can see this is the entire key takeaways for this entire projects. So, as you can see at the end of it, this is what the project has created. So, this is the map B. Obviously, I don't want to show you the project from the client, but here you can see this is the demo project, which I actually create a clone version of this, but have Clockwise here to basically create kind of like the anonymous version of this projects. But you can see that this is the entire overview, right? You can see it has the properties, the overview. And then here you can see we also have the info card on exactly what's the project profile and also the scope. So, phase one, phase two, phase three, and then the tech stack. And we also have the conversation log. This is going to be the conversation tracking, which tracks the conversation from the initial like discovery call all the way to contract sign, weeks one to week three, and then the live demo, system goes live, uh scope of expansion, and also the phase one handoff is being summarized and condensed inside of the conversation log, which you can see here. So, you can see that's really powerful. And then if we were to scroll all the way down, there's also some action item. So, respond to clients and deliver phase two and phase three, which we can see here. Okay, so that's exactly how that works. Now, furthermore, we also have the projects.base file, which keeps track of all the status for all the projects that we have. We can also be able to use Clockwise here combining with the contacts that we have in our notebook and be able to craft anything, right? For example, be able to craft a response based on the projects that we have. For example, this demo project, uh can you be able to help me to tell me what's the current status of this project is? And can you tell me exactly how I should be able to craft a response or what are some action item that I need to do? And I can use that as like my brain or second brain here and using Clockwise here as my assistant, so that now I give Clockwise here the power or the knowledge of what's currently going on with my projects and have Clockwise here to decide exactly what I need to do. And you can see here that Clockwise here gives me the response. So, this is the current status of the demo projects. Phase one here is all completed and the final payment is already received. The phase two here is authorized. So, here is the key contacts and then here are some action items. And here you can see craft your response to the clients. So, here are found some things that we have. So, here you can see it says, "Do you want to craft a actual email response?" And honestly, what we can do here is that we can even use the power of Google Workspace CLI. So, connect that with Clockwise, so that we can have Clockwise here to interact with Google Workspace through the CLI without having me to open the Gmail app here to paste the email that I have to respond. And I think this is a great use case. Obviously, this is my use case. Your case could be like studying, researching, right? You can be able to combine it with the power of Notebook LM here inside of Clockwise, so make sure to check out this video right here how you can be able to combine the power of Notebook LM here within Clockwise, so that you can be able to automate the process for doing research and be able to organize all your knowledge base into one single place. All right, so pretty much that's it for this video. In this video, we went over how we can be able to combine the power of Clockwise and Obsidian here to be your second brain, where Clockwise here is going to basically help you to manage your memories, your notes, and also answer any questions, be able to save it inside of your GitHub here for version control. And also furthermore, you can also be able to use that to ingest any data and be able to query any questions that you have. And a lot of those things are all through the Obsidian skills with the power of Clockwise and Obsidian. So, I'll make sure to put every resource that we have mentioned in this video in our school community, so you can check it out in our link in the description. And with that being said, if you do find value in this video, please make sure to like this video. Consider to subscribe for more content like this. With that being said, I'll see you in the next video.

---

## Timestamped Segments

**[0:00]** In this video, I'm going to show exactly

**[0:01]** how to build your second brain using

**[0:03]** Claude Code and the power of Obsidian.

**[0:05]** And specifically for my use case, I use

**[0:07]** Obsidian here to manage different

**[0:08]** projects. And furthermore, I was able to

**[0:10]** use Claude Code here as like a AI

**[0:12]** assistant here to manage my notes. Right

**[0:14]** here, you can see I have a bunch of

**[0:15]** Obsidian CLI skills, which will

**[0:16]** basically help us to create better

**[0:18]** Obsidian notes. And right here, you can

**[0:19]** see one of the skills that I created

**[0:21]** called the onboarding projects, which

**[0:23]** can help me to take any data source that

**[0:24]** I have like Gmails and local files, have

**[0:26]** Claude Code here to organize, summarize

**[0:28]** those informations, and store that

**[0:30]** inside of my Obsidians using the

**[0:32]** Obsidian skills. I'm going to show you

**[0:33]** in later on this video. And pretty much,

**[0:35]** you can see that we can use Claude Code

**[0:36]** here with the power of Obsidian to

**[0:38]** basically help us to answer any

**[0:39]** questions, perform any actions on our

**[0:41]** notes. So, with that being said, that's

**[0:43]** what we're going to cover in this video.

**[0:44]** If you're interested, let's get into

**[0:45]** this. Now, before we continue, I

**[0:47]** recently launched our school community

**[0:48]** where I help you to master AI agents,

**[0:50]** automations, and so much more. And

**[0:52]** that's all coming from someone who used

**[0:54]** to work as a senior AI software engineer

**[0:56]** at companies like Amazon and Microsoft.

**[0:59]** And in this community, you're going to

**[1:00]** get over 100 plus video materials like

**[1:02]** templates and workflows that I

**[1:04]** personally built and sold over 100 plus

**[1:06]** times. On top of that, you're also going

**[1:07]** to get access to our weekly live calls.

**[1:10]** And just give you an idea, this week

**[1:11]** we're actually running a Claude Code

**[1:12]** masterclass where we're going to dive

**[1:14]** into how to improve Claude Code's

**[1:16]** accuracy. We're going to use it to

**[1:17]** building applications. Plus, you're also

**[1:19]** going to get full community supports

**[1:20]** where you're going to get a chance to

**[1:21]** ask questions and get direct answers

**[1:23]** back. So, if you're ready to level up,

**[1:25]** make sure to jump right in, and I'll see

**[1:26]** you in the community. Now, because

**[1:28]** Obsidian here is not free, the free

**[1:30]** version here doesn't allow you to sync

**[1:31]** notes or do the version control. And

**[1:33]** that's why the first step we're going to

**[1:34]** do here is basically have Obsidian here

**[1:36]** to connect it with our GitHub by first

**[1:37]** creating a repository. And any changes

**[1:39]** that we're making in our Obsidian notes,

**[1:41]** we're going to push that onto our GitHub

**[1:42]** repository. This way, we're going to

**[1:43]** have a version control and also

**[1:45]** completely free for cloud storage. So,

**[1:47]** in this case, let's take a look at how

**[1:48]** we can do this first. All right, so to

**[1:49]** get started, first thing first, we're

**[1:50]** going to do here is make sure to create

**[1:51]** our GitHub accounts. And simply, all we

**[1:53]** have to do here is just click on new

**[1:55]** right here to create a new repository.

**[1:57]** And this will basically going to be a

**[1:58]** folder we're going to dump all the data

**[1:59]** here inside of our repository in GitHub

**[2:02]** so that we have the right version

**[2:03]** control, and we can also be able to

**[2:04]** change the visibility. So, here I'm

**[2:06]** going to change that to be private

**[2:08]** because I don't want anyone else here to

**[2:09]** see the brain because you only want to

**[2:11]** use this for your cloud storage and

**[2:12]** version control. So, in this case, I'm

**[2:14]** going to give it a name for the

**[2:15]** repository, and I'm just going to call

**[2:16]** it the Eric Tech Brain. And simply, once

**[2:18]** that's done, I will just click on create

**[2:20]** new repository. And now, you can see we

**[2:21]** have a repository created inside of our

**[2:23]** GitHub. So, once we have a repository

**[2:25]** now, what we have to do here is we want

**[2:27]** to make sure to clone this inside of our

**[2:28]** local machine so we can move to add any

**[2:30]** local files here onto our GitHub for

**[2:32]** cloud storage and version control. And

**[2:34]** to do so, if you're really new to

**[2:35]** terminal and you're not really a

**[2:36]** developer, I highly recommend you just

**[2:38]** to install GitHub Desktop where you can

**[2:40]** be able to manage the entire version

**[2:41]** control and the cloud storage in a

**[2:43]** desktop graphical user interface rather

**[2:45]** than just using the terminal. So, for

**[2:46]** demonstration, I'm just going to

**[2:47]** download this onto my local machine.

**[2:49]** Now, once you have your GitHub Desktop

**[2:50]** app downloaded on your local machine,

**[2:52]** this is what it looks like. So, all we

**[2:54]** have to do here is just make sure to

**[2:55]** select the repository that I just

**[2:56]** created. For example, mine is called the

**[2:58]** Eric Tech Brain. So, there's one called

**[3:00]** Eric Tech Brain, and we can see that

**[3:02]** currently it is private. So, I'm just

**[3:03]** going to choose that and be able to

**[3:04]** clone this onto our local machine. So,

**[3:06]** I'm just going to click on clone, and

**[3:08]** it's telling you exactly where you can

**[3:09]** clone this. So, you can see that the

**[3:10]** local file path here is actually inside

**[3:12]** of documents. But if I want to change

**[3:14]** that, for example, I want to change that

**[3:15]** to be in my desktop, I can be able to

**[3:17]** change that and click on select. And

**[3:19]** then here, all I have to do here is just

**[3:20]** click on clone, and it's going to clone

**[3:21]** the repository here on our desktop

**[3:23]** folder in our local machine. So, now you

**[3:25]** can see we have the repository cloned

**[3:27]** inside of our desktop folder. The next

**[3:29]** thing we're going to do here is make

**[3:30]** sure to have Obsidian installed on our

**[3:32]** local machine as well. So, now if I were

**[3:33]** to head over to the Obsidian download

**[3:35]** page, simply all I have to do here is

**[3:36]** click on download, and it's going to

**[3:37]** download this app on our local machine.

**[3:39]** So, I'm going to download this for my

**[3:40]** Mac version. All right, so now once I

**[3:42]** have downloaded this on my Mac OS, the

**[3:43]** next thing we're going to do here is

**[3:44]** make sure to open folder as vault. So,

**[3:47]** I'm going to click on open. And then

**[3:48]** here, I'm going to click on desktop.

**[3:49]** Then we're going to click on the

**[3:50]** repository that we just cloned and click

**[3:52]** on open. And then here, you can see this

**[3:53]** is the notebook that we have for our

**[3:55]** Eric Tech Brain. So, now once we have

**[3:56]** this open, here you can see on the

**[3:58]** right, this is the entire Eric Tech

**[3:59]** folders. that we write on the Obsidian

**[4:01]** is going to be reflected inside of this

**[4:04]** folder. So, for example, if I were to

**[4:05]** create a new note, for example, here you

**[4:07]** can see this is the note. And right here

**[4:08]** on the right, you can see we have

**[4:09]** untitled.md file. So, now if I were to

**[4:12]** type in, for example, Eric Tech, and

**[4:14]** that's going to be the file name, you

**[4:15]** can see that has changed reflected right

**[4:17]** away. And if I were to create a folder

**[4:18]** in Obsidian, it's going to do the same

**[4:20]** thing here as well. So, next we're going

**[4:21]** to show you here is basically commit the

**[4:22]** changes onto our GitHub so that we have

**[4:24]** a cloud backup. So, right here, you can

**[4:26]** see if I were to open the GitHub Desktop

**[4:28]** app, currently on the left, you can see

**[4:29]** we have six changes on the files. And

**[4:32]** simply, I'm just going to give the

**[4:33]** message summary on exactly what are the

**[4:35]** changes that we have just made. I'm just

**[4:36]** going to say this is the initial

**[4:37]** summary. You can see this is the initial

**[4:39]** commit. And commit this, then click on

**[4:41]** push here to basically push that changes

**[4:43]** onto the remote, which is our GitHub

**[4:45]** repository. So, now if I were to click

**[4:46]** on the history here, you can see this is

**[4:48]** the commit that we just committed, and

**[4:50]** now has that change. So, if I want to

**[4:51]** revert it back, you can do so. So, now

**[4:53]** if I were to head over to the GitHub

**[4:54]** repository browser, here you can see

**[4:55]** this is the Eric Tech Brain. And right

**[4:57]** here, you can see this is my first

**[4:58]** initial commit, which basically means

**[5:00]** that we have successfully saved the

**[5:01]** changes onto our GitHub repository here.

**[5:04]** Now, obviously, making changes and

**[5:05]** manually have to commit this is going to

**[5:07]** be really painful. And you might be

**[5:08]** asking, "Well, is there any ways that we

**[5:09]** can be able to automatically commit this

**[5:11]** onto our GitHub repository?" And the

**[5:13]** answer here is yes. So, now if I were to

**[5:14]** head over to the Obsidian here, all we

**[5:16]** have to do here is just click on the

**[5:17]** gear icon. And basically, if I were to

**[5:19]** click on the community plugins and click

**[5:21]** on the turn on community plugins right

**[5:23]** here, now we can be able to browse a

**[5:25]** community plugins. And there's actually

**[5:26]** a plugin here that can actually help us

**[5:28]** to automatically commit these changes

**[5:29]** that we have onto our GitHub repository.

**[5:32]** So, simply all I have to do here is just

**[5:33]** click on browse. And then the plugin

**[5:34]** here is called Git. So, right here, you

**[5:36]** can see this is the plugin which

**[5:37]** integrates the Git version here with

**[5:38]** automatically backup and other advanced

**[5:40]** features. So, if I were to click on

**[5:42]** this, right here, you can see you can be

**[5:43]** able to learn more about this from this

**[5:44]** open source repository. But simply, if

**[5:46]** you want to install this, all you have

**[5:47]** to do is just click on install right

**[5:49]** here. So, right here, you can see the

**[5:50]** repository here is fully installed. And

**[5:52]** then simply, click on enable. Then we're

**[5:53]** going to click on options. And right

**[5:55]** here, you can see there's a feature

**[5:56]** called auto commit and sync after

**[5:58]** stopping file edits, which basically

**[6:00]** means that after we stop editing the

**[6:01]** files in the Obsidian, it will basically

**[6:04]** start to commit the changes that we have

**[6:06]** onto GitHub. So, simply if we were to

**[6:08]** enable this feature, and all we have to

**[6:09]** do here is set an interval on how often

**[6:12]** should it be able to sync the changes,

**[6:13]** right? It could be like every minute,

**[6:15]** right? After we stop changing or after

**[6:17]** we stop editing the files in Obsidian,

**[6:19]** it's going to automatically do that with

**[6:21]** a set interval. So, for example, it

**[6:22]** could be like 1 minute. So, that's what

**[6:24]** I'm going to set right here. And then

**[6:25]** furthermore, if you scroll down, there's

**[6:26]** also a feature called pull on startup,

**[6:28]** which basically automatically pull the

**[6:30]** latest changes from Obsidian when it

**[6:32]** starts. So, in this case, I'm just going

**[6:33]** to enable this. So, for example, maybe

**[6:35]** you're making changes from device one,

**[6:37]** and then you want to open your device

**[6:38]** two here to basically sync the changes.

**[6:40]** This will basically allow you to have

**[6:42]** that option. So, make sure to pull on

**[6:43]** startup. Okay, so now if I were to test

**[6:45]** the changes here, if I were to close

**[6:46]** this, and let's say if I were to make

**[6:48]** some changes, for example, right? So, in

**[6:49]** this case, I'm going to say example,

**[6:51]** right? And then be able to give some

**[6:53]** like words here. And then you can see

**[6:54]** here that after 1 minute, it has

**[6:56]** committed six files here automatically

**[6:58]** onto our GitHub page. So, now if I were

**[7:00]** to head over to the version control, you

**[7:01]** can see that we have all backups as well

**[7:03]** as committed automatically through the

**[7:06]** Obsidian. And if I were to head over to

**[7:08]** the repository and just refresh now, you

**[7:10]** can see we have the example.md file that

**[7:11]** we just created. And right here, you can

**[7:13]** see this is the change that we have. So,

**[7:14]** now let's say if I were to edit

**[7:16]** something, for example, say hello, and

**[7:18]** click on commit, and click on

**[7:21]** uh changes, right? So, now you can see

**[7:22]** we have some additional changes added

**[7:23]** onto this MD file. So, now you can see

**[7:25]** if I were to restart the Obsidian, it

**[7:27]** has automatically pulled the changes.

**[7:29]** Now, you can see that we have hello here

**[7:30]** inside of our notebook. So, now once we

**[7:32]** have our Obsidian notebook set up, the

**[7:34]** next thing we're going to take a look at

**[7:34]** is how we can be able to connect it with

**[7:36]** our large language model like Claude

**[7:37]** Code. And to make this process easier,

**[7:39]** we're going to use the Obsidian skill,

**[7:41]** which basically teach our AI agent here

**[7:42]** to use all the capabilities that

**[7:44]** Obsidian has like the markdown, base,

**[7:46]** JSON, canvas, all through the Obsidian

**[7:49]** CLI. And of course, if you want to have

**[7:50]** your CLI for Obsidian set up, make sure

**[7:52]** to head over to your settings for the

**[7:54]** Obsidian, and just click on the general.

**[7:56]** And then here, inside of general,

**[7:57]** there's the advanced, and we have the

**[7:59]** command line interface. So, make sure to

**[8:00]** toggle this on. It will basically allow

**[8:02]** you to interact Obsidian with CLI. Now,

**[8:04]** once we have the CLI enabled, the next

**[8:06]** thing we're going to take a look at is

**[8:07]** how we can be able to set up the

**[8:08]** Obsidian skills. So, right here, you can

**[8:09]** see simply if we want to install this,

**[8:11]** we're just going to copy the commands

**[8:12]** right here to install this either

**[8:14]** through the marketplace or the MPX

**[8:16]** skills. So, now once you have this

**[8:17]** installed, the next thing we're going to

**[8:18]** take a look at is how we can be able to

**[8:19]** use that for a practical use case. So,

**[8:22]** what I can do here is I can be able to

**[8:23]** onboard those data onto Claude Code, and

**[8:25]** Claude Code here is going to trigger the

**[8:26]** Obsidian skills that we just installed,

**[8:28]** and it's going to help us to organize

**[8:29]** and summarize everything into one single

**[8:32]** location. So, in this case, let me show

**[8:33]** you exactly how I would do that. All

**[8:35]** right, so to do so here, you can see I

**[8:36]** basically created a skill called onboard

**[8:38]** projects. And essentially, what it does

**[8:39]** here is that it will collect data from

**[8:41]** my external Gmail, right? Like basically

**[8:43]** my all my emails from a particular

**[8:45]** projects. And also for the internal

**[8:47]** files, right? Let's say if I have bunch

**[8:49]** of project contexts on my local drive, I

**[8:51]** can also be able to upload that here for

**[8:53]** this particular skill or any text that I

**[8:55]** want to paste. It will basically use the

**[8:56]** existing Obsidian skills, right? Like

**[8:58]** the markdown, the base, the CLI here to

**[9:01]** create everything, okay?

**[9:02]** And this is the entire skill structures.

**[9:04]** It will basically uses some of the

**[9:05]** scripts that I created here to like, for

**[9:07]** example, getting a email label, right?

**[9:09]** Getting the messages, getting the

**[9:11]** threads from Gmail, and then be able to

**[9:13]** fetch those things and download the

**[9:14]** attachments using this part of the

**[9:16]** skills here. And it will basically try

**[9:18]** to output it as the vault here. So, you

**[9:20]** can see it's going to output as a

**[9:21]** project folder. And then here, inside of

**[9:23]** this projects folder here, we have a

**[9:25]** projects.base, which is basically a

**[9:28]** table where we keep track of all the

**[9:29]** projects that we have. And then we also

**[9:31]** have the project name. So, that's

**[9:33]** basically whatever project like we have

**[9:35]** like ABC projects. We're going to have

**[9:37]** the overview, exactly okay, what is this

**[9:39]** project about? And then we also have the

**[9:41]** conversation log like, okay, what is the

**[9:43]** conversation summary in a chronological

**[9:45]** order for all the conversation that we

**[9:46]** have going on with this project, right?

**[9:48]** So, that we know exactly what's

**[9:50]** happening. And we also have the links on

**[9:52]** exactly okay, what are some external

**[9:53]** links. And then we also, most

**[9:54]** importantly, we have the documentations.

**[9:56]** So, there's some documents that could be

**[9:57]** like static file like NDA or agreements

**[10:00]** or contracts that we need to cap inside

**[10:02]** of the agreements that cannot be

**[10:03]** summarized, right? So, some files here

**[10:05]** shouldn't be summarized. Some of

**[10:06]** information here should be summarized

**[10:08]** and condensed it down into the

**[10:09]** conversation log. So, that this way it's

**[10:11]** much more easier for me to juggle

**[10:12]** multiple projects at the same time. So,

**[10:14]** you can see here that this is the entire

**[10:16]** five that workflow on exactly how the

**[10:18]** skill does. Right here you can see we

**[10:19]** first try to create a project. So, if

**[10:21]** the project exists already, we might

**[10:23]** just want to update or import more data

**[10:25]** on this project and that's it. If it's a

**[10:27]** new project, we're just going to create

**[10:28]** a new project here and then we also have

**[10:30]** collecting sources here. So, let's say

**[10:32]** we're going to collect like Gmail,

**[10:33]** internal, and also the paste text or

**[10:36]** screenshots. We're also going to collect

**[10:37]** that as well. And it's going to process

**[10:39]** and see if there if it's existing

**[10:40]** projects, we're going to see if there's

**[10:41]** any duplicates. And also if it's going

**[10:43]** to be new projects, we're going to

**[10:45]** filter out if it's like static file,

**[10:47]** conversations, references, key details,

**[10:49]** we're going to put them into the right

**[10:51]** place. Then furthermore, it's going to

**[10:52]** auto extract the profile. So, extract

**[10:54]** like the wiki links, the industry, and

**[10:56]** be able to update the overview.md file.

**[10:58]** And by the end of it, it's also going to

**[11:00]** generate summary on exactly what are the

**[11:01]** key events for this project, what is the

**[11:03]** timeline, and also what is the import

**[11:05]** stats. So, then you can see I basically

**[11:06]** instructed to create that skill and now

**[11:08]** we can be able to use it to onboard

**[11:09]** projects much more faster onto Obsidian.

**[11:12]** So, now if I were to restart my

**[11:13]** Clockwise session, I should now be able

**[11:15]** to use this skill called onboard

**[11:16]** projects. And now if I were to simply

**[11:18]** trigger this, it should prompt me

**[11:20]** exactly what should we call this

**[11:21]** project. So, right here you can see it's

**[11:22]** going to check the current state of the

**[11:24]** current project folder. And then there's

**[11:26]** no project exists, what's the name of

**[11:28]** the project you would like to set up.

**[11:29]** So, for example, I'm just going to call

**[11:30]** like map B, right? For example, like it

**[11:32]** doesn't matter which name you're you're

**[11:34]** using. You can see it's going to just

**[11:35]** create the project structures called map

**[11:37]** B. And here you can see it's going to

**[11:39]** create the project dashboard, creating

**[11:41]** the conversation log, and then it also

**[11:43]** has create the project base, which is

**[11:45]** how we're going to create the project

**[11:47]** status for all the projects that we

**[11:48]** have, right? So far you can see we have

**[11:50]** set up the these things, right? The

**[11:52]** overview, the conversation log, links,

**[11:53]** documents, and also the projects.base,

**[11:56]** which is the dashboard. And now what we

**[11:57]** need to do here is we need to be able to

**[11:59]** input the data source, right? Maybe you

**[12:01]** have like external like Gmail label

**[12:04]** where this label here contains bunch of

**[12:05]** emails that you have with this projects.

**[12:08]** Or and also if you have like internal

**[12:10]** files, right? Like PDF, docs, contracts

**[12:12]** from your local drive, you can be able

**[12:13]** to upload here. And also if there's any

**[12:15]** text you want to paste, any screenshots

**[12:17]** that the AI here can be able to extract

**[12:18]** from, we can also be able to paste it

**[12:20]** here into this particular skill. And

**[12:22]** it's going to help us to analyze

**[12:23]** everything and aggregate everything into

**[12:25]** this project folder structure that we

**[12:26]** have here. So, in this case, I'm first

**[12:28]** going to upload the internal local file

**[12:30]** path that I have as well as the entire

**[12:31]** Gmail label link on exactly where it

**[12:33]** contains all the data source. So, in

**[12:35]** this case, I'm just going to enter this

**[12:36]** and it's going to fetch that

**[12:38]** automatically for us. Okay, so now you

**[12:39]** can see all the local files here has

**[12:41]** been processed and now for Gmail here,

**[12:43]** the scripts are not configured because

**[12:45]** for Gmail label here, we need the uh

**[12:47]** credentials. So, right here you can see

**[12:49]** it tells you exactly how you can get the

**[12:50]** credentials like Google Cloud Console,

**[12:52]** enable Gmail API, and also create the

**[12:54]** OAuth credentials right there. So,

**[12:56]** basically you guys are going to download

**[12:57]** the JSON once after you create the OAuth

**[13:00]** two credentials. So, if I were to open

**[13:01]** this, here you can see there's the

**[13:03]** folder called dot Gmail credentials.

**[13:05]** You're just going to save your

**[13:06]** credentials here right here, right?

**[13:07]** That's it. And what essentially here you

**[13:09]** can see it from the dot env file, it

**[13:11]** actually referenced this particular

**[13:13]** folder for the credentials and tokens

**[13:14]** here to be able to fetch those emails

**[13:16]** here using those scripts. Okay, so

**[13:17]** that's exactly how it works. So, now you

**[13:19]** can see everything is all done and here

**[13:21]** is what's imported. So, we have five

**[13:22]** files here are imported to this

**[13:24]** particular projects for the documents

**[13:26]** like the service agreements, the

**[13:27]** proposal, like the project plans, uh

**[13:30]** freelancer brief, all those kind of

**[13:31]** things, right? And then we also have the

**[13:33]** Gmail, which is all the emails that we

**[13:34]** have fetched from the entire thread

**[13:36]** conversation from December all the way

**[13:38]** to April, which is in chronological

**[13:40]** order. And also here you can see this is

**[13:42]** the entire key takeaways for this entire

**[13:44]** projects. So, as you can see at the end

**[13:46]** of it, this is what the project has

**[13:47]** created. So, this is the map B.

**[13:49]** Obviously, I don't want to show you the

**[13:50]** project from the client, but here you

**[13:52]** can see this is the demo project, which

**[13:54]** I actually create a clone version of

**[13:56]** this, but have Clockwise here to

**[13:58]** basically create kind of like the

**[13:59]** anonymous version of this projects. But

**[14:01]** you can see that this is the entire

**[14:02]** overview, right? You can see it has the

**[14:04]** properties, the overview. And then here

**[14:06]** you can see we also have the info card

**[14:08]** on exactly what's the project profile

**[14:10]** and also the scope. So, phase one, phase

**[14:12]** two, phase three, and then the tech

**[14:14]** stack. And we also have the conversation

**[14:16]** log. This is going to be the

**[14:17]** conversation tracking, which tracks the

**[14:20]** conversation from the initial like

**[14:21]** discovery call all the way to contract

**[14:23]** sign, weeks one to week three, and then

**[14:25]** the live demo, system goes live, uh

**[14:28]** scope of expansion, and also the phase

**[14:30]** one handoff is being summarized and

**[14:32]** condensed inside of the conversation

**[14:34]** log, which you can see here. So, you can

**[14:35]** see that's really powerful. And then if

**[14:37]** we were to scroll all the way down,

**[14:38]** there's also some action item. So,

**[14:39]** respond to clients and deliver phase two

**[14:41]** and phase three, which we can see here.

**[14:44]** Okay, so that's exactly how that works.

**[14:46]** Now, furthermore, we also have the

**[14:47]** projects.base file, which keeps track of

**[14:49]** all the status for all the projects that

**[14:50]** we have. We can also be able to use

**[14:52]** Clockwise here combining with the

**[14:53]** contacts that we have in our notebook

**[14:55]** and be able to craft anything, right?

**[14:57]** For example, be able to craft a response

**[14:58]** based on the projects that we have. For

**[15:00]** example, this demo project, uh can you

**[15:02]** be able to help me to tell me what's the

**[15:03]** current status of this project is? And

**[15:06]** can you tell me exactly how I should be

**[15:08]** able to craft a response or what are

**[15:09]** some action item that I need to do? And

**[15:11]** I can use that as like my brain or

**[15:12]** second brain here and using Clockwise

**[15:14]** here as my assistant, so that now I give

**[15:16]** Clockwise here the power or the

**[15:18]** knowledge of what's currently going on

**[15:19]** with my projects and have Clockwise here

**[15:21]** to decide exactly what I need to do. And

**[15:23]** you can see here that Clockwise here

**[15:25]** gives me the response. So, this is the

**[15:26]** current status of the demo projects.

**[15:28]** Phase one here is all completed and the

**[15:30]** final payment is already received. The

**[15:32]** phase two here is authorized. So, here

**[15:34]** is the key contacts and then here are

**[15:36]** some action items. And here you can see

**[15:38]** craft your response to the clients. So,

**[15:40]** here are found some things that we have.

**[15:41]** So, here you can see it says, "Do you

**[15:43]** want to craft a actual email response?"

**[15:45]** And honestly, what we can do here is

**[15:46]** that we can even use the power of Google

**[15:48]** Workspace CLI. So, connect that with

**[15:50]** Clockwise, so that we can have Clockwise

**[15:52]** here to interact with Google Workspace

**[15:54]** through the CLI without having me to

**[15:56]** open the Gmail app here to paste the

**[15:57]** email that I have to respond. And I

**[15:59]** think this is a great use case.

**[16:00]** Obviously, this is my use case. Your

**[16:02]** case could be like studying,

**[16:03]** researching, right? You can be able to

**[16:05]** combine it with the power of Notebook LM

**[16:06]** here inside of Clockwise, so make sure

**[16:09]** to check out this video right here how

**[16:10]** you can be able to combine the power of

**[16:11]** Notebook LM here within Clockwise, so

**[16:13]** that you can be able to automate the

**[16:14]** process for doing research and be able

**[16:16]** to organize all your knowledge base into

**[16:18]** one single place. All right, so pretty

**[16:19]** much that's it for this video. In this

**[16:21]** video, we went over how we can be able

**[16:22]** to combine the power of Clockwise and

**[16:23]** Obsidian here to be your second brain,

**[16:26]** where Clockwise here is going to

**[16:27]** basically help you to manage your

**[16:28]** memories, your notes, and also answer

**[16:30]** any questions, be able to save it inside

**[16:32]** of your GitHub here for version control.

**[16:34]** And also furthermore, you can also be

**[16:35]** able to use that to ingest any data and

**[16:38]** be able to query any questions that you

**[16:39]** have. And a lot of those things are all

**[16:41]** through the Obsidian skills with the

**[16:43]** power of Clockwise and Obsidian. So,

**[16:45]** I'll make sure to put every resource

**[16:47]** that we have mentioned in this video in

**[16:49]** our school community, so you can check

**[16:50]** it out in our link in the description.

**[16:51]** And with that being said, if you do find

**[16:52]** value in this video, please make sure to

**[16:53]** like this video. Consider to subscribe

**[16:55]** for more content like this. With that

**[16:56]** being said, I'll see you in the next

**[16:58]** video.
