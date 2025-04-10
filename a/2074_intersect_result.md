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

- IntersectionResult parameter getter throws an InvalidOperationException
  https://forums.autodesk.com/t5/revit-api-forum/intersectionresult-parameter-getter-throws-an/m-p/13400449#M84547

- New training approach? *Iterated Distillation and Amplification (IDA)* - a scalable and efficient alignment strategy for general superintelligence using iterative self-improvement... to surpass the intelligence of whoever is training it, i.e., humans: [Cogito v1 Preview -- Introducing IDA as a path to general superintelligence](https://www.deepcogito.com/research/cogito-v1-preview).

- A scientific paper on [Artificial Intelligence for Software Architecture: Literature Review and the Road Ahead](https://arxiv.org/abs/2504.04334).

- Here is a nice [6-minute dystopian charade of vibe coding video](https://youtu.be/JeNS1ZNHQs8).

- The Slow Collapse of Critical Thinking in OSINT due to AI
  https://www.dutchosintguy.com/post/the-slow-collapse-of-critical-thinking-in-osint-due-to-ai
  Open-source intelligence
  https://en.wikipedia.org/wiki/Open-source_intelligence

- Dmytro Vakulenko
  https://dmytro-prototypes.net/
  Freelance Software Developer | Azure, .NET, Python, Typescript, AI | Transforming ideas into innovative and evolutionary solutions
  https://www.linkedin.com/in/ACoAAAirTFIB2JAw2fqoQYvyf0VqS_AaPvUHf3k
  I've been following your work for years and have noticed lately your interest in showcasing unique LLM integrations into CAD/BIM products.
  I wanted to share a couple of projects I’ve been developing, and I'm curious if they might resonate with you:
  1) Open-Source LLM Integration for AutoCAD:
  This project focuses on generating AutoCAD scripts through an iterative process that continues looping until the script is fully compilable/fixed.
  A standout feature is the use of reflection to provide additional insights about classes and methods—truly the “cherry on the top of the cake.”
  https://www.linkedin.com/posts/dmytro-vakulenko-software_scripture-demo-llm-based-autocad-automation-activity-7248239069292294144-pj2i
  2) LLM Querying (and Editing) Data in IFC Files:
  In this project, the chatbot not only retrieves information from IFC files but also generates and executes Python code to interact with them dynamically, tailoring responses in real time based on the data.
  https://www.linkedin.com/posts/dmytro-vakulenko-software_innovation-ifc-ai-agent-variables-activity-7285951367746080768-DIlr
  (and my other posts)
  I would be honored if you could take a look and share your thoughts.
  Your perspective would be invaluable, and I’m excited about the potential to contribute to the ongoing discussion surrounding LLM integrations in the CAD/CAE space.
  Thank you very much for your time and consideration.
  Best regards,
  Dmytro

Google announced the [A2A agent-to-agent protocol](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) including support for MCP.

developers.googleblog.comdevelopers.googleblog.com
Announcing the Agent2Agent Protocol (A2A)- Google Developers Blog
Explore A2A, Google's new open protocol empowering developers to build interoperable AI solutions. (364 kB)
https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/

[A2A is also included in Visual Studio](https://code.visualstudio.com/blogs/2025/04/07/agentMode.

Agent mode is great for scenarios where:

Your task involves multiple steps. The agent edits code, runs terminal commands, monitors for errors, and iterates to resolve any issues that arise.
You are unsure about the scope of the changes. The agent automatically determines the relevant files and context.
Your task requires interaction with external apps or data. The agent integrates with MCP servers and VS Code extensions.



twitter:

 @AutodeskAPS  @AutodeskRevit  #RevitAPI #BIM @DynamoBIM

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

### Intersection Result


####<a name="7"></a> IntersectionResult parameter getter throws an InvalidOperationException
https://forums.autodesk.com/t5/revit-api-forum/intersectionresult-parameter-getter-throws-an/m-p/13400449#M84547


 matyas.csanady3GW48
03-25-2025 02:20 AM
Hey everybody! As the title mentions I'm having some surprising difficulties with the IntersectionResult class. Long story short I check the intersection of 2 line elements (i know for a fact that these 2 lines intersect) with (link)
SetComparisonResult result = line1.Intersect(line2, out resultArray);
It's all nice and fine at this point since the result and resultArray are not null. I can get the IntersectionResult out of the IntersectionResultArray for example by:
IntersectionResult intResult = resultArray.get_Item(0);
But I'm intersected in IntersectionResult.Parameter property (link), and when i try to get the value of this parameter an InvalidOperationException is thrown. Checking the Parameter property documentation again it claims that it happens when it has not been set yet "Thrown in the getter when this property has not been set by the method providing the result. ".
Checking this Parameter property in debug reveals that it's not the only one failing. As you can see on the picture the "Distance", "EdgeObject", "EdgeParameter" and "Parameter" all fail with InvalidOperationException.
Kép.png
This issue occurred to me in a C# addin in all current version versions (22->25). For testing purposes I've created a python script that you can paste into RevitPytonShell and it results is the same error across all versions.

<pre><code class="language-py">results = clr.Reference[DB.IntersectionResultArray]()

t = DB.Transaction(doc, "Line Creation")
t.Start()

lineV = DB.Line.CreateBound(DB.XYZ(0,0,0), DB.XYZ(0,10,0))
lineH = DB.Line.CreateBound(DB.XYZ(-5,5,0), DB.XYZ(5,5,0))

doc.Create.NewDetailCurve(uidoc.ActiveView, lineV)
doc.Create.NewDetailCurve(uidoc.ActiveView, lineH)

result = lineV.Intersect(lineH, results)

intResult = results.get_Item(0)
# For example this works
print("XYZPoint: {}".format(intResult.XYZPoint))
# But the following all fail
print("Distance: {}".format(intResult.Distance))
print("EdgeObject: {}".format(intResult.EdgeObject))
print("EdgeParameter: {}".format(intResult.EdgeParameter))
print("Parameter: {}".format(intResult.Parameter))

t.Commit()

Even if it's outside of a Transaction (since Line creation and Line.Intersect does not require that), the results are the same.
results = clr.Reference[DB.IntersectionResultArray]()

lineV = DB.Line.CreateBound(DB.XYZ(0,0,0), DB.XYZ(0,10,0))
lineH = DB.Line.CreateBound(DB.XYZ(-5,5,0), DB.XYZ(5,5,0))
result = lineV.Intersect(lineH, results)

intResult = results.get_Item(0)
# For example this works
print("XYZPoint: {}".format(intResult.XYZPoint))
# But the following all fail
print("Distance: {}".format(intResult.Distance))
print("EdgeObject: {}".format(intResult.EdgeObject))
print("EdgeParameter: {}".format(intResult.EdgeParameter))
print("Parameter: {}".format(intResult.Parameter))</code></pre>

Would appreciate any help with this problem!


 jeremy_tammik
Autodesk jeremy_tammik
2025-03-25 08:03 AM
I would like to pass this on to the development team for analysis, including a complete minimal sample in order for them to be able to reproduce the issue with a single click, if possible. Could you create a simple RVT (that can be empty) including a C# macro to execute to reproduce the problem, please? Thank you!

https://thebuildingcoder.typepad.com/blog/about-the-author.html#1b

Jeremy Tammik  Developer Advocacy and Support + The Building Coder + Autodesk Developer Network + ADN Open
Report
 matyas.csanady3GW48
Explorer matyas.csanady3GW48
in reply to jeremy_tammik
2025-03-26 03:16 AM
Hi Jeremy!

Thank you for your quick reply and for the fact that you forward this issue to the DEV team. As you asked for I've created a macro that is able reproduce the same exception with a single click. I've attached an empty Revit project file that contains this macro, as expected running the macro throws the same exception.

IntersectionResult_InvalidOperationException_Macro_R22.rvt

Report
 jeremy_tammik
Autodesk jeremy_tammik
in reply to matyas.csanady3GW48
2025-03-26 04:09 AM
Thank you for creating the macro. I see that the RVT filename ends in R22. Does that stand for Revit 2022? Could you please try it out in a more recent version? I believe that the next major release is being expected soon, and the development team (and all of Autodesk) refuse to support more than three major versions back, so Revit 2022 is out of scope. Thank you!

Jeremy Tammik  Developer Advocacy and Support + The Building Coder + Autodesk Developer Network + ADN Open
Report
 matyas.csanady3GW48
Explorer matyas.csanady3GW48
2025-03-26 04:27 AM
I've updated it to Revit2025 and attached it.

IntersectionResult_InvalidOperationException_Macro_R25.rvt

Report
 mhannonQ65N2
Advocate mhannonQ65N2
2025-03-28 12:13 PM
The Curve.Intersect method does not set the IntersectionResult's Parameter property. Look at the documentation for Curve.Intersect to see which properties are set and what they mean.
Report
 tamas.deri
Advocate tamas.deri
2025-03-31 03:01 AM
Whoever designed this part of the API deserves a raise. /s
It seems that the Parameter and Distance properties of the IntersectResult object will never get set by any of the methods creating it. So what was the intent?
Report
 mhannonQ65N2
Advocate mhannonQ65N2
2025-03-31 01:07 PM
IntersectionResult's Parameter and Distance properties are both set by the Curve.Project method. The problem with IntersectionResult is that it is used to return results for several different geometric methods.




####<a name="2"></a>

<center>
<img src="img/.png" alt="" title="" width="100"/> <!--  -->
</center>


