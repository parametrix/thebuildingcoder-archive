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

- [OpenAI o3 and o4-mini](https://youtu.be/sq8GBPUb3rk) impress coders and scientists.
  Open AI Codex coding agent runs locally: [tweet](https://x.com/sama/status/1912558495997784441).
  Here's the quick low-down of 03 and 04mini by Dan Shipper:
  - It's agentic. Someone at OpenAI referred to o3 as deep research-lite to me, and that's exactly what it is. Set it to do a task, and come back in 30 seconds or three minutes and get a thorough answer. It can use tools like web search, code interpreter, reminders, and memory in a loop so you can have it code complex features, answer tricky research queries over long documents, or even build you a course that it reminds you to take every day.
  - It's fast. Speed is a dimension of intelligence. Maybe your model can unify physics, but if it doesn't happen in this lifetime I don't care. In my testing, o3 was consistently faster than Anthropic's and Google's frontline reasoning models (3.7
  Sonnet and Gemini 2.5 Pro, respectively) on this dimension. It feels smooth.
  - It's very smart. I don't have access to benchmarks as of this writing, but I fed it expert-level Sudoku problems and it solved them on the first try. Gemini 2.5 Pro and 3.7 Sonnet both failed.
  - It busts some old Chat GPT limitations. Because it's agentic, the old rules don't apply. You don't have to be as wary of web search because it doesn't summarize the first spam blog post it finds in a Google search. You can give it many files and expect coherent, complete answers —I had it read an entire book and outline it, for example. When you use it for coding it will automatically do multiple searches through the web to find up-to-date documentation, which cuts down errors a lot.
  Basically, it makes ChatGPT way more useful.
  - It's not as socially awkward as 01, and it's not a try-hard like 3.7 Sonnet. I found myself coding with it a lot this weekend, and I really liked it. It understands what you mean and does what it's told to at high quality. It doesn't plow ahead and try to build the Taj Mahal when you tell it to fix a bug, like Sonnet does. It also seems a little more vibe-y than other o-series models. It's more fun to talk to; not as good a writer as GPT 4.5 (RIP) or Sonnet 3.5, but still good.

- Super interesting statistical news on global AI development: [AI Index 2025: State of AI in 10 Charts](https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts)

- An interesting short article explaining how to handle challenges using AI for complex app coding: [Vibe coding considered harmful, Lego code instead](https://sundaylettersfromsam.substack.com/p/vibe-coding-considered-harmful-lego).

- A [prompting guide for GPT-4.1 models](https://platform.openai.com/docs/guides/text?api-mode=responses#prompting-gpt-4-1-models).
  While the cookbook has the best and most comprehensive guidance for prompting this model, here are a few best practices to keep in mind.
  - Building agentic workflows
  - Using long context
  - Prompting for chain of thought
  - Instruction following

- Demystifying the #! (shebang): Kernel Adventures
  https://crocidb.com/post/kernel-adventures/demystifying-the-shebang/

- Wall: attach top/base, no API?
  https://forums.autodesk.com/t5/revit-api-forum/wall-attach-top-base-no-api/m-p/13427160#M84749
  Wall.AddAttachment Method
  https://revapidocs.com/2026.htm?id=bef619ea-dede-2795-d767-04a464a997f0.htm
  https://www.revitapidocs.com/2026/bef619ea-dede-2795-d767-04a464a997f0.htm


twitter:

@AutodeskRevit #RevitAPI @AutodeskAPS #BIM @DynamoBIM

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

### Revit API with Copilot and Codex

I have used GitHub Copilot in VS Code for Revit API add-in coding for a few days, and installed OpenAI Codex this morning.

Exciting times, moving fast:

- [OpenAI o3 and o4-mini](https://youtu.be/sq8GBPUb3rk) impress coders and scientists.
  Open AI Codex coding agent runs locally: [tweet](https://x.com/sama/status/1912558495997784441).
  Here's the quick low-down of 03 and 04mini by Dan Shipper:
  - It's agentic. Someone at OpenAI referred to o3 as deep research-lite to me, and that's exactly what it is. Set it to do a task, and come back in 30 seconds or three minutes and get a thorough answer. It can use tools like web search, code interpreter, reminders, and memory in a loop so you can have it code complex features, answer tricky research queries over long documents, or even build you a course that it reminds you to take every day.
  - It's fast. Speed is a dimension of intelligence. Maybe your model can unify physics, but if it doesn't happen in this lifetime I don't care. In my testing, o3 was consistently faster than Anthropic's and Google's frontline reasoning models (3.7
  Sonnet and Gemini 2.5 Pro, respectively) on this dimension. It feels smooth.
  - It's very smart. I don't have access to benchmarks as of this writing, but I fed it expert-level Sudoku problems and it solved them on the first try. Gemini 2.5 Pro and 3.7 Sonnet both failed.
  - It busts some old Chat GPT limitations. Because it's agentic, the old rules don't apply. You don't have to be as wary of web search because it doesn't summarize the first spam blog post it finds in a Google search. You can give it many files and expect coherent, complete answers —I had it read an entire book and outline it, for example. When you use it for coding it will automatically do multiple searches through the web to find up-to-date documentation, which cuts down errors a lot.
  Basically, it makes ChatGPT way more useful.
  - It's not as socially awkward as 01, and it's not a try-hard like 3.7 Sonnet. I found myself coding with it a lot this weekend, and I really liked it. It understands what you mean and does what it's told to at high quality. It doesn't plow ahead and try to build the Taj Mahal when you tell it to fix a bug, like Sonnet does. It also seems a little more vibe-y than other o-series models. It's more fun to talk to; not as good a writer as GPT 4.5 (RIP) or Sonnet 3.5, but still good.

- Super interesting statistical news on global AI development: [AI Index 2025: State of AI in 10 Charts](https://hai.stanford.edu/news/ai-index-2025-state-of-ai-in-10-charts)

- An interesting short article explaining how to handle challenges using AI for complex app coding: [Vibe coding considered harmful, Lego code instead](https://sundaylettersfromsam.substack.com/p/vibe-coding-considered-harmful-lego).

- A [prompting guide for GPT-4.1 models](https://platform.openai.com/docs/guides/text?api-mode=responses#prompting-gpt-4-1-models).
  While the cookbook has the best and most comprehensive guidance for prompting this model, here are a few best practices to keep in mind.
  - Building agentic workflows
  - Using long context
  - Prompting for chain of thought
  - Instruction following

- Demystifying the #! (shebang): Kernel Adventures
  https://crocidb.com/post/kernel-adventures/demystifying-the-shebang/

- Wall: attach top/base, no API?
  https://forums.autodesk.com/t5/revit-api-forum/wall-attach-top-base-no-api/m-p/13427160#M84749
  Wall.AddAttachment Method
  https://revapidocs.com/2026.htm?id=bef619ea-dede-2795-d767-04a464a997f0.htm
  https://www.revitapidocs.com/2026/bef619ea-dede-2795-d767-04a464a997f0.htm



####<a name="2"></a>

<pre><code class="language-cs">
</code></pre>



<center>
<img src="img/.png" alt="" title="" width="800"/> <!-- 1200 -->
</center>


- OpenAI o3 and o4-mini -- https://youtu.be/sq8GBPUb3rk
- Open AI Codex coding agent runs locally -- https://youtu.be/FUq9qRwrDrI




https://www.linkedin.com/feed/update/urn:li:activity:7318574255611236353?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7318574255611236353%2C7318581431536959489%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287318581431536959489%2Curn%3Ali%3Aactivity%3A7318574255611236353%29

https://www.linkedin.com/feed/update/urn:li:activity:7318574255611236353


https://www.linkedin.com/feed/update/urn:li:activity:7318574255611236353?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7318574255611236353%2C7318581431536959489%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287318581431536959489%2Curn%3Ali%3Aactivity%3A7318574255611236353%29


Roman [@Nice3point](https://t.me/nice3point) Karpovich ([LinkedIn](https://www.linkedin.com/in/nice3point/)), aka Роман Карпович,
principal contributor and maintainer of RevitLookup,
[commented on the last post](https://www.linkedin.com/feed/update/urn:li:activity:7318574255611236353?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7318574255611236353%2C7318581431536959489%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287318581431536959489%2Curn%3Ali%3Aactivity%3A7318574255611236353%29)
discussing [intersection result, LLM for IFC and more AI](https://thebuildingcoder.typepad.com/blog/2025/04/intersection-result-llm-for-ifc-and-more-ai.html),
saying:

Microsoft has already prepared great packages for AI, and they can already be used in C#, with just a couple of lines of code:

- [Artificial intelligence in .NET](https://learn.microsoft.com/en-us/dotnet/core/extensions/artificial-intelligence?tabs=dotnet-cli)
- [Build a Model Context Protocol (MCP) server in C#](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)

I tested some other approaches myself.

In the past week, I installed Visual Studio Code on MacOS, with GitHub Copilot integrated, and used that for some Revit API work with impressive results.

This morning, I installed OpenAI Codex and asked it to explain the purpose of my current Revit API code WIP.
I provided one single prompt, six words:

- "please explain what this application does"

Here is the answer it provided right out of the box:

This is a small C# /.NET add‑in for Autodesk Revit (a “Revit plug‑in”) whose goal is to let you take an existing plumbing (or HVAC) distribution network in your model—pipes, fittings (elbows, tees, reducers, etc.) and even ducts—and make a full copy of it, displaced to one side. Under the hood it does four main things:

- Ribbon integration
  &ndash; On startup, it adds an “HVAC System Tools” tab with buttons for
    - “Find Root Node” (identify the “start” of any piping system)
    - “Duplicate Pipe System”
    - “Duplicate Duct System”
    - (There is also a “Rolling Offset” command for auto‑calculating and inserting a two‑pipe offset with 45° bends.)

- Graph‑based network traversal
  &ndash; Before duplicating, it walks your existing system and builds a little graph of “nodes” (every pipe segment or fitting) and their “connectors” (endpoints), capturing for each:
    - Its element id and type (pipe vs. fitting vs. duct)
    - Its geometric transform (location, orientation, rotation)
    - All the connector points (and which other element they’re linked to)
    - Any important parameters (diameter, width/height, family parameters on reducers, etc.)

- Duplication at offset
  &ndash; In a single TransactionGroup it:
    - Starts a transaction and creates a copy of every pipe/duct segment at a fixed offset (e.g. +30 ft in X) using the same system type, level, curve endpoints and size parameters.
    - Places new family instances for each fitting at the corresponding translated origin, applies the same symbol, size parameters and re‑rotates them so their connector axes line up.
    - Commits that transaction.

- Re‑connecting the network
  &ndash; In a second transaction it revisits every new node, finds on each its closest connector on a neighboring new element (using a tiny distance‑threshold test) and calls the Revit API “ConnectTo” to wire them back up in exactly the same topology as the original.

Beyond pure duplication, there are also commands to:

- Find and report the “root” element of any PipingSystem (CmdRootFinder + PipeSystemRootFinder).
- Analyze/traverse a piping system and export its graph to disk (PipingSystemAnalyzer → text file).
- Re‑create a piping system from that file (PipeSystemRecreator).
- Compute and insert a two‑pipe rolling offset (CmdRollingOffset), optionally with real fittings or just a model line.

All of this is built on small data classes &ndash; NodeData, ConnectorData, ParamData &ndash; to snapshot each element’s geometry, connectivity and parameters, plus a few utility routines (in Util.cs) to find connectors, compare points, and manage the various Revit API quirks.

