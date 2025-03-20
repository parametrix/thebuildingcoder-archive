<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<link rel="stylesheet" type="text/css" href="bc.css">

<!--
https://prismjs.com
<pre><code class="language-cs">
-->
<link href="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/themes/prism.min.css" rel="stylesheet" />
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-core.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
<style> code[class*=language-], pre[class*=language-] { font-size : 90%; } </style>

</head>

<!--


- feedspot
  From: Anuj Agarwal <dev@f1.feedspot.com>
  Date: Thursday, 20 March 2025 at 09:44
  To: Jeremy Tammik <jeremy.tammik@autodesk.com>
  Subject: The Building Coder featured in FeedSpot Top 25 Revit Blogs
  Hi Jeremy,
  My name is Anuj Agarwal, I'm the Founder of FeedSpot.
  I would like to personally congratulate you as your blog The Building Coder has been selected by our panelist as one of the Top 25 Revit Blogs on the web.
  https://bloggers.feedspot.com/revit_blogs/
  This is the most comprehensive list of Top 25 Revit Blogs on the internet and I'm honored to have you as part of this!
  You can also add your website link and other social media handles to get more visibility in our list and get discovered by brands for collaboration.
  We've created a badge for you to share with your audience. You can display it on your website or post it on social media to showcase this amazing milestone.
  We'd be grateful if you can help us spread the word by briefly mentioning about the Top 25 Revit Blogs list in any of your upcoming post.
  Please feel free to reach out with any questions.
  Best,
  Anuj

- [Erik Gette](https://github.com/erikgett) of [ГК Страна Девелопмент](https://strana.com)
How to Debug Revit Plugins: Speeding Up Development
https://www.linkedin.com/pulse/how-debug-revit-plugins-speeding-up-development-gette-erik-8usef/
January 29, 2025
> The Runner.txt file is a VBA script (Revit journal) that allows executing specific commands in Revit upon startup. Essentially, it can be used to trigger any sequence of actions automatically.
In the context of my article, this file is used to launch Revit without any third-party plugins, ensuring a clean environment for testing and debugging.
Interestingly, Revit generates similar log files for each session. These files can be read and analyzed, which opens up a range of automation possibilities. For example, in our workflow, we use these logs to orchestrate 10 running instances of Revit to export over 5,000 files into NWC format efficiently.
The use cases for this approach are vast, and I plan to explore them in more detail in future articles. Stay tuned! 😊
Navisworks orchestration on the server: how to execute typical tasks in parallel within the Navisworks environment
https://www.linkedin.com/pulse/navisworks-orchestration-server-how-execute-typical-tasks-erik-gette-pmjjf/
March 5, 2025
Revit Orchestration on the Server: How to Execute Typical Tasks in Parallel in the Revit Context
https://www.linkedin.com/pulse/revit-orchestration-server-how-execute-typical-tasks-parallel-gette-ct1wc/
February 20, 2025

- Chuong HoChuong Ho
  Ollma3 LLM Agent APS WSL System (Autodesk Platform Services)
  https://youtu.be/-Nr-_ZgK8qI
  Exploring Open Source & Local LLM Ollama for Design Metadata Querying in Autodesk Platform Services! 🤖
  I'm excited to share my recent experiment with an open-source project that brings Local LLM AI and Autodesk Platform Services (APS) together! You can choose any model from your localhost with free AI open source model, and use this chatbot for a wide range of purposes!
  This is just the first version of my hackathon project, and I’m excited about how it turned out. A huge thanks to Petr Broz for the repository and inspiration!
  Check out the video below to see the real-time speed response using LLM on a local machine with WSL. It’s fascinating how fast and efficient the response time is!
  Make a comment if you want me to make a tutorials 🤖
  Open Source : https://lnkd.in/gkBw5ggV
  hashtag#OpenSource hashtag#LLM hashtag#Autodesk hashtag#BIM hashtag#Hackathon hashtag#AI hashtag#Chatbot hashtag#APIS hashtag#Technology hashtag#Innovation

- conversational voice generation and simulation demo
  https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice#demo
  Sesame &ndash; Crossing the uncanny valley of conversational voice
  At Sesame, our goal is to achieve “voice presence”—the magical quality that makes spoken interactions feel real, understood, and valued.

twitter:

 @AutodeskAPS
 @AutodeskRevit #RevitAPI
 #BIM @DynamoBIM


&ndash; ...

linkedin:

#BIM #DynamoBIM #AutodeskAPS #Revit #API #IFC #SDK #Autodesk #AEC #adsk

the [Revit API discussion forum](http://forums.autodesk.com/t5/revit-api-forum/bd-p/160) thread

<center>
<img src="img/" alt="" title="" width="600"/>
<p style="font-size: 80%; font-style:italic"></p>
<a href="img/.gif"><p style="font-size: 80%; font-style:italic">Click for animation</p></a>
</center>

-->

### Docs, Local APS LLM and Parallel Task Orchestration


By the way, The Building Coder was selected by feedspot as one of
the [Top 25 Revit Blogs](https://bloggers.feedspot.com/revit_blogs/).
Thank you for the recognition, even if the list does look rather arbitrary to me...

####<a name="2"></a> RvtDocs Revit API Documentation

After a long lack of online API documentatiojn for Revit 2025, we suddenly have a whole collection of choices, and competition is increasing.

The newest candidate is from Erik Frits of [LearnRevitAPI](https://learnrevitapi.com/), who launched yet another Revit API documentation website:

<center>
  <a href="https://rvtdocs.com/">RvtDocs</a>
</center>

Welcome to the pack!

Here is an overview of the choices to date that I am aware of:

- [apidocs.co](https://apidocs.co) &ndash; Revit API documentation for 2015, 2016, 2017, 2017.1, 2018, 2018.1, 2018.2, 2019, 2019.1, 2019.2, 2020, 2020.1, 2021, 2021.1, 2022, 2022.1, 2023, 2024, 2025 and 2025.3, plus API documentation for Grasshopper, Navisworks and Rhino
- [Rev API Docs](https://revapidocs.com/) &ndash; Revit API documentation for 2020, 2021, 2022, 2023, 2024 and 2025, sister website of [Civ API Docs](https://civapidocs.com/), Civil 3D API documentation for 2022, 2023, 2024 and 2025
- [Revit API Docs](https://www.revitapidocs.com/) &ndash; Revit API documentation for 2021.1, 2022, 2023, 2024, 2025 and 2025.3
- [RVTDocs](https://rvtdocs.com/) &ndash; Revit API documentation for 2021, 2022, 2023, 2024 and 2025

####<a name="3"></a> Revit Parallel Task Orchestration on the Server

[Erik Gette](https://github.com/erikgett) of [ГК Страна Девелопмент](https://strana.com)
How to Debug Revit Plugins: Speeding Up Development
https://www.linkedin.com/pulse/how-debug-revit-plugins-speeding-up-development-gette-erik-8usef/
January 29, 2025
> The Runner.txt file is a VBA script (Revit journal) that allows executing specific commands in Revit upon startup. Essentially, it can be used to trigger any sequence of actions automatically.
In the context of my article, this file is used to launch Revit without any third-party plugins, ensuring a clean environment for testing and debugging.
Interestingly, Revit generates similar log files for each session. These files can be read and analyzed, which opens up a range of automation possibilities. For example, in our workflow, we use these logs to orchestrate 10 running instances of Revit to export over 5,000 files into NWC format efficiently.
The use cases for this approach are vast, and I plan to explore them in more detail in future articles. Stay tuned! 😊
Navisworks orchestration on the server: how to execute typical tasks in parallel within the Navisworks environment
https://www.linkedin.com/pulse/navisworks-orchestration-server-how-execute-typical-tasks-erik-gette-pmjjf/
March 5, 2025
Revit Orchestration on the Server: How to Execute Typical Tasks in Parallel in the Revit Context
https://www.linkedin.com/pulse/revit-orchestration-server-how-execute-typical-tasks-parallel-gette-ct1wc/
February 20, 2025

Thank you, Erik, for your valuable research and documentation.

####<a name="4"></a> Local Ollama LLM APS Metadata Querying

[Chuong Ho](https://chuongmep.com/) published a one-minute video
on [Ollma3 LLM Agent APS WSL System (Autodesk Platform Services)](https://youtu.be/-Nr-_ZgK8qI):

> Exploring Open Source & Local LLM Ollama for Design Metadata Querying in Autodesk Platform Services!

> I'm excited to share my recent experiment with an open-source project that brings Local LLM AI and Autodesk Platform Services (APS) together!
You can choose any model from your localhost with free AI open source model, and use this chatbot for a wide range of purposes!
This is just the first version of my hackathon project, and I’m excited about how it turned out.
A huge thanks to Petr Broz for the repository and inspiration!

> Check out the video below to see the real-time speed response using LLM on a local machine with WSL.
Its fascinating how fast and efficient the response time is!

> [aps-local-chatbot GitHub repository](https://github.com/chuongmep/aps-ollma-chatbot)

> Simple chatbot for querying metadata of designs in Autodesk Platform Services using Ollama for chat completion.
This projects connects a powerful local LLM with zero cost into Autodesk Platform Services.

Many thanks to Chuong Ho for implementing and sharing this exciting innovative project.

<center>
<img src="img/ch_acc_ollama.png" alt="Ollama LLM with APS and ACC" title="Ollama LLM with APS and ACC" width="600"/> <!-- Pixel Width: 900 -->
</center>

####<a name="5"></a> Moore's Law for Agent Autonomy: 7 Months

[Moore's law for agents: autonomy doubles every 7 months](https://buttondown.com/ainews/archive/ainews-every-7-months-the-moores-law-for-agent/), cf. the paper on [Measuring AI Ability to Complete Long Tasks](https://arxiv.org/pdf/2503.14499).

<center>
<img src="img/moores_law_agent.png" alt="Moore's law for agents: autonomy doubles every 7 months" title="Moore's law for agents: autonomy doubles every 7 months" width="600"/> <!-- Pixel Width: 1200 -->
</center>

> Figure 1: The length of tasks (measured by how long they take human professionals) that generalist autonomous frontier model agents can complete with 50% reliability has been doubling approximately every 7 months for the last 6 years. The shaded region represents 95% CI calculated by hierarchical bootstrap over task families, tasks, and task attempts. Even if the absolute measurements are off by a factor of 10, the trend predicts that in under a decade we will see AI agents that can independently complete a large fraction of software tasks that currently take humans days or weeks.

####<a name="6"></a> Conversational Voice Generation

Non-Revit-related, this conversational voice generation and simulation demo highlights
[Sesame &ndash; Crossing the uncanny valley of conversational voice](https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice#demo):

> At Sesame, our goal is to achieve “voice presence”—the magical quality that makes spoken interactions feel real, understood, and valued.


<pre><code class="language-cs"></code></pre>


