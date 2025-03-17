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

###

####<a name="2"></a> RvtDocs Revit API Documentation

Competition is heating up.

Erik Frits of [LearnRevitAPI](https://learnrevitapi.com/) launched yet another Revit API Documentation website:

<center>
  <a href="https://rvtdocs.com/">RvtDocs</a>
</center>

Welcome to the pack!

RevitApiDocs
CivApiDocs 2069#3

2069_fab_part_service.md:[Apidocs](https://apidocs.co) also includes API documentation for Grasshopper, Navisworks, Rhino and previous Revit releases all the way back to Revit 2015.

<!-- grep -i apidoc 2*d -->



####<a name="2"></a> Revit Parallel Task Orchestration on the Server

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

####<a name="3"></a> Local Ollama LLM APS Metadata Querying

Chuong Ho
Ollma3 LLM Agent APS WSL System (Autodesk Platform Services)
https://youtu.be/-Nr-_ZgK8qI
Exploring Open Source & Local LLM Ollama for Design Metadata Querying in Autodesk Platform Services! 🤖
I'm excited to share my recent experiment with an open-source project that brings Local LLM AI and Autodesk Platform Services (APS) together! You can choose any model from your localhost with free AI open source model, and use this chatbot for a wide range of purposes!
This is just the first version of my hackathon project, and I’m excited about how it turned out. A huge thanks to Petr Broz for the repository and inspiration!
Check out the video below to see the real-time speed response using LLM on a local machine with WSL. It’s fascinating how fast and efficient the response time is!
Make a comment if you want me to make a tutorials 🤖
Open Source : https://lnkd.in/gkBw5ggV
hashtag#OpenSource hashtag#LLM hashtag#Autodesk hashtag#BIM hashtag#Hackathon hashtag#AI hashtag#Chatbot hashtag#APIS hashtag#Technology hashtag#Innovation

Many thanks to Chuong Ho for implementing and sharing this exciting innovative project.

####<a name="4"></a> Conversational Voice Generation

conversational voice generation and simulation demo
https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice#demo
Sesame &ndash; Crossing the uncanny valley of conversational voice
At Sesame, our goal is to achieve “voice presence”—the magical quality that makes spoken interactions feel real, understood, and valued.

<center>
<img src="img/" alt="" title="" width="100"/> <!-- Pixel Width: 800 -->
</center>

<pre><code class="language-cs"></code></pre>


