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

- still feeling with nick:
  Reading the news today, I explored further an item on Chinese calligraphy and stumbled over a poem from the year (ca.) 350 AD, the [Lantingji Xu, Preface to the Poems Collected from the Orchid Pavilion](https://en.wikipedia.org/wiki/Lantingji_Xu). I found it touching and fitting to be shared here, and maybe you will enjoy it too:
  In the ninth year of Yonghe, at the onset of late spring,
  we have gathered at the Orchid Pavilion in the North of Kuaiji Mountain for the purification ritual.
  All the literati, the young and the aged, have congregated.
  This location has high mountains and steep hills, dense woods, and tall bamboo,
  as well as a clear, limpid stream reflecting the surroundings.
  We sit by a redirected stream, allowing the wine goblets to float beside us on its winding course.
  Although without the accompaniment of music,
  the wine and poem reciting are sufficient for us to exchange our feelings.
  On this day, the sky is clear, the air is fresh, and a gentle breeze is blowing.
  Looking up, we admire the vastness of the universe;
  looking down, we see the myriad works of poetry.
  Letting the gaze wander and the mind roam, one can fully enjoy the pleasures of sight and sound, truly a delight.
  People's interactions with each other quickly pass through a lifetime.
  Some would share their ambitions in a chamber;
  others may freely indulge in diverse interests and pursuits.
  The choices are plenty and our temperaments vary.
  We enjoy the momentary satisfaction of pleasures that regale us,
  yet we hardly realize how swiftly we age.
  As desires fade and circumstances change, grief arises.
  What previously gratified us will soon be a relic,
  we cannot help but mourn.
  Whether life is long or short, there is always an end.
  As the ancients said,
  "Death and birth are momentous."
  How agonizing!
  Reading the past compositions reveals a consistent melancholy from the ancients.
  One may find themselves lamenting in response to their words, unable to articulate their feelings.
  It is absurd to equate life with death,
  and it is equally foolish to think that longevity is the same as the short-lived.
  The future generations will look upon us,
  just like we look upon our past.
  How sad!
  Hence, we record the people presented here today and their works;
  Even though time and circumstances will be different,
  the feelings expressed will remain unchanged.
  Future readers shall find the same empathy through this collection of poems.

- get bounding box of element on sheet
  Chuong Ho shared a more reliable method GetBboxElementOnSheet
  Getting element coordiantes on sheet
  https://forums.autodesk.com/t5/revit-api-forum/getting-element-coordiantes-on-sheet/td-p/9785396

- a nice little essay on the topic of using AI for speedy coding and/or in-depth learning: [New Junior Developers Can’t Actually Code](https://nmn.gl/blog/ai-and-learning).

- XOR
  https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/xor/
  Simon Tatham made a good stab at summarising everything one might possibly want to know about XOR.

- three horizons
  https://www.h3uni.org/tutorial/three-horizons/

twitter:

 #RevitAPI @AutodeskAPS @AutodeskRevit #BIM @DynamoBIM


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

### UIApplication and Bounding Box on Sheet

####<a name="2"></a> Feeling with Nick

My daughter's baby was born, and my brother is still alive, though extremely weak.

Reading the news today, I explored further an item on Chinese calligraphy and stumbled over a poem from the year 353 AD,
the [Lantingji Xu, Preface to the Poems Collected from the Orchid Pavilion](https://en.wikipedia.org/wiki/Lantingji_Xu).
I found it touching and fitting to be shared here, and maybe you will enjoy it too:

> In the ninth year of Yonghe, at the onset of late spring,
<br/>we have gathered at the Orchid Pavilion in the North of Kuaiji Mountain for the purification ritual.
<br/>All the literati, the young and the aged, have congregated.
<br/>This location has high mountains and steep hills, dense woods, and tall bamboo,
<br/>as well as a clear, limpid stream reflecting the surroundings.
<br/>We sit by a redirected stream, allowing the wine goblets to float beside us on its winding course.
<br/>Although without the accompaniment of music,
<br/>the wine and poem reciting are sufficient for us to exchange our feelings.
<br/>On this day, the sky is clear, the air is fresh, and a gentle breeze is blowing.
<br/>Looking up, we admire the vastness of the universe;
<br/>looking down, we see the myriad works of poetry.
<br/>Letting the gaze wander and the mind roam, one can fully enjoy the pleasures of sight and sound, truly a delight.
<br/>People's interactions with each other quickly pass through a lifetime.
<br/>Some would share their ambitions in a chamber;
<br/>others may freely indulge in diverse interests and pursuits.
<br/>The choices are plenty and our temperaments vary.
<br/>We enjoy the momentary satisfaction of pleasures that regale us,
<br/>yet we hardly realize how swiftly we age.
<br/>As desires fade and circumstances change, grief arises.
<br/>What previously gratified us will soon be a relic,
<br/>we cannot help but mourn.
<br/>Whether life is long or short, there is always an end.
<br/>As the ancients said,
<br/>"Death and birth are momentous."
<br/>How agonizing!
<br/>Reading the past compositions reveals a consistent melancholy from the ancients.
<br/>One may find themselves lamenting in response to their words, unable to articulate their feelings.
<br/>It is absurd to equate life with death,
<br/>and it is equally foolish to think that longevity is the same as the short-lived.
<br/>The future generations will look upon us,
<br/>just like we look upon our past.
<br/>How sad!
<br/>Hence, we record the people presented here today and their works;
<br/>Even though time and circumstances will be different,
<br/>the feelings expressed will remain unchanged.
<br/>Future readers shall find the same empathy through this collection of poems.

####<a name="3"></a> Access UIApplication Anywhere

Continuing with Revit API re4lated topics,
Luiz Henrique [@ricaun](https://ricaun.com/) Cassettari shares yet another new discovery,
how to [get `UIApplication` anywhere](https://forums.autodesk.com/t5/revit-api-forum/get-uiapplication-anywhere/td-p/13341551):

`UIApplication` is the most useful class inside Revit API, providing access to all events, documents and to know whether your code is in the AddInContext (Revit API Context).

It would be really handy is there was way to have access to `UIApplication` any time you need.

There is a way, a native way in the RevitAPIUI.dll, to retrieve the `UIApplication` without any reflection or internal code.
I figured that out that a long time ago (~3 years) when I was messing with events.

The class `RibbonItemEventArgs` provides a direct reference for a new `UIApplication` class:

<pre><code class="language-cs">UIApplication uiapp = new Autodesk.Revit.UI.Events.RibbonItemEventArgs().Application;</code></pre>

I created a class `RevitApplication` in
my [ricaun.Revit.UI](https://github.com/ricaun-io/ricaun.Revit.UI) library
just to have a base standard:

- [RevitApplication.cs](https://github.com/ricaun-io/ricaun.Revit.UI/blob/master/ricaun.Revit.UI/RevitApplication.cs)

<pre><code class="language-cs">UIApplication uiapp = RevitApplication.UIApplication;
UIControlledApplication application = RevitApplication.UIControlledApplication;
bool inAddInContext = RevitApplication.IsInAddInContext;</code></pre>

It would be better still if Autodesk would create a static class like RevitApplication in RevitAPIUI.dll.

That concludes my post, I hope you like it.

See yaa!

####<a name="4"></a> Determine Element Bounding Box on Sheet

Also Revit API related,
[Chuong Ho](https://chuongmep.com/) shares
another important solution providing a more reliable method `GetBboxElementOnSheet`
for [getting element coordiantes on sheet](https://forums.autodesk.com/t5/revit-api-forum/getting-element-coordiantes-on-sheet/td-p/9785396):

> I just want to share a cleaner solution for anyone who wants to understand or make use of it:

<pre><code class="language-cs">public BoundingBoxXYZ? GetBboxElementOnSheet(
  Autodesk.Revit.DB.Document doc,
  Autodesk.Revit.DB.Element element,
  Autodesk.Revit.DB.Viewport viewport)
{
  View? v = (View)doc.GetElement(viewport.ViewId);
  if (v == null) return null;
  Outline vpoln = viewport.GetBoxOutline(); // Viewport outline in Sheet coords.
  BoundingBoxUV voln = v.Outline; // View outline.
  if(vpoln == null || voln == null) return null;
  int scale = v.Scale;

  /*Transform for view coords (very important for rotated view plans set to true north etc.)
  completely not important when view plan is not rotated*/
  Transform t = Transform.Identity;
  t.BasisX = v.RightDirection;
  t.BasisY = v.UpDirection;
  t.BasisZ = v.ViewDirection;
  t.Origin = v.Origin;
  // You can probably get this transform above from elsewhere such as cropbox.

  var volnCen = (voln.Min + voln.Max) / 2; // View outline centre
  XYZ vpcen = (vpoln.MaximumPoint + vpoln.MinimumPoint) / 2; // Viewport centre
  vpcen = new XYZ(vpcen.X, vpcen.Y, 0); // Zero z

  // Correction offset from VCen to centre of Viewport in sheet coords
  XYZ offset = vpcen - new XYZ(volnCen.U, volnCen.V, 0);
  BoundingBoxXYZ bb = element.get_BoundingBox(v);
  if (bb == null) return null;
  // Location of door bounding box in sheet coords
  XYZ j1 = t.Inverse.OfPoint(bb.Min).Multiply((Double)1 / scale) + offset;
  XYZ j2 = t.Inverse.OfPoint(bb.Max).Multiply(1 / scale) + offset;

  // return bb of element in sheet coords
  BoundingBoxXYZ boxXyz = new BoundingBoxXYZ();
  boxXyz.Min = new XYZ(j1.X, j1.Y, 0);
  boxXyz.Max = new XYZ(j2.X, j2.Y, 0);
  return boxXyz;
}</code></pre>

<center>
<img src="img/element_coordinates_on_sheet.png" alt="GetBboxElementOnSheet" title="GetBboxElementOnSheet" width="600"/> <!-- Pixel Height: 624 Pixel Width: 1013 -->
</center>

####<a name="5"></a> AI and Human Coding

A nice little essay on the topic of using AI for speedy coding versus in-depth learning comes to the conclusion
that [new junior developers can’t actually code](https://nmn.gl/blog/ai-and-learning)

####<a name="6"></a> XOR

For a purely technical in-depth analysis of a topic that turn out to have a surprisingly large scope, check out Simon Tatham's thoughts
on [XOR](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/xor/).
He made a good stab at summarising everything one might possibly want to know about XOR.

####<a name="7"></a> Three Horizons

Pondering all the personal and global turmoil of our times, I chanced upon another point of view on some aspects,
the [Three Horizons](https://www.h3uni.org/tutorial/three-horizons/):

> We stand for a vision of a different kind of relationship between humans, life and the planet that we explore in the creative space of the future that we call the third horizon.

