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


twitter:

Vibe programming, generative AI, and MCP connector and RAG docs for @AutodeskRevit #RevitAPI @AutodeskAPS #BIM @DynamoBIM https://thebuildingcoder.typepad.com/blog/2025/03/revit-gen-ai-mcp-rag-and-vibe.html

AI-related news keeps piling in fast
&ndash; Revit Vibe: generative AI in the BIM
&ndash; Revit MCP connector
&ndash; Convert Revit API help file to RAG for LLM
&ndash; AI effect on programming jobs
&ndash; Nice Jupyter interactive graph
&ndash; Art is theft...

linkedin:

Vibe programming, generative AI, and MCP connector and RAG docs for #RevitAPI

https://thebuildingcoder.typepad.com/blog/2025/03/revit-gen-ai-mcp-rag-and-vibe.html

- Revit Vibe: generative AI in the BIM
- Revit MCP connector
- Convert Revit API help file to RAG for LLM
- AI effect on programming jobs
- Nice Jupyter interactive graph
- Art is theft...

#BIM #DynamoBIM #AutodeskAPS #Revit #API #IFC #SDK #Autodesk #AEC #adsk

the [Revit API discussion forum](http://forums.autodesk.com/t5/revit-api-forum/bd-p/160) thread

<center>
<img src="img/" alt="" title="" width="600"/>
<p style="font-size: 80%; font-style:italic"></p>
<a href="img/.gif"><p style="font-size: 80%; font-style:italic">Click for animation</p></a>
</center>

-->

### Lookup Foundation, Empty Asset, Demoished Room

####<a name="2"></a> RevitLookup and the Lookup Foundation

Roman [@Nice3point](https://t.me/nice3point) Karpovich, aka Роман Карпович,
has been heroically maintaining and enhancing RevitLookup for several years now.

He would like to expand and generalise it to implement a whole suite of tools for exploring the .NET objects.

For that purpose, we transferred ownership of the RevitLookup repository to
the new [Lookup Foundation](https://github.com/lookup-foundation):

<center>
<img src="img/lookup_foundation.png" alt="Lookup Foundation" title="Lookup Foundation" width="800"/> <!-- width="1824" -->
</center>

GitHub redirects from the old URL to the new one, so existing links on the web will continue working:

> All links to the previous repository location are automatically redirected to the new location. When you use git clone, git fetch, or git push on a transferred repository, these commands will redirect to the new repository location or URL. However, to avoid confusion, we strongly recommend updating any existing local clones to point to the new repository URL

RevitLookup has been actively developed for many years, shaped by the contributions of a dedicated open-source community. Today, we mark an important milestone: the project transitions from its original home under Jeremy Tammik’s leadership to a new organization — the Lookup Foundation — where its development will be guided by the community that relies on it.

The repository has moved to its new address:

🔗 https://github.com/lookup-foundation/RevitLookup

This transition ensures RevitLookup's continued growth as a community-driven project . RevitLookup is no longer just one person’s project; it belongs to the community that builds, tests, and improves it every day.

The Lookup Foundation will ensure the project remains open, sustainable, and driven by its users. Whether you're a developer, a Revit expert, or simply someone who benefits from the tool, you have a role to play in its evolution.





####<a name="4"></a> Direwolf Fast Revit Data Extraction

[Direwolf](https://github.com/Framebuffers/Direwolf) implements a data analysis framework for Autodesk Revit.
It extracts, serialises, and stores parameters from BIM models in fractions of a second.

####<a name="4"></a> Memory Stick versus Floppies

I bought a 1 TB memory stick, and it got me thinking.
In the beginning of my programming career, we used [floppy disks](https://en.wikipedia.org/wiki/Floppy_disk).
They originally held 360 KB.

<pre><code class="language-py">kb = 1024 byte
floppy = 360 * kb = 368640 byte
mb = 1024 * kb = 1048576 byte
tb = 1024 * mb = 1073741824 byte
tb / floppy = 2912.711111</code></pre>

Assuming a floppy is 3 millimetres thick, this would be a stack about 2900 &middot; 0.003 = 8.7 metres high.


