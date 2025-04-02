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

- Why is AppearanceAssetElement empty in API?
  https://forums.autodesk.com/t5/revit-api-forum/why-is-appearanceassetelement-empty-in-api/m-p/13388041#M84456
  ask llm to summarise this post and q and a sokrates dialogue

- Revit API: Retrieving Room Data for Demolished Family Instances
  https://adndevblog.typepad.com/aec/2024/10/revit-api-retrieving-room-data-for-demolished-family-instances.html

- RST Results Package Create with Api
  https://forums.autodesk.com/t5/revit-api-forum/results-package-create-with-api/m-p/13093333
  Structural Analysis Toolkit, ResultsBuilder, Reviewing Stored Results in Revit
  https://forums.autodesk.com/t5/revit-api-forum/structural-analysis-toolkit-resultsbuilder-reviewing-stored/m-p/8778306

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

### New Release Webinar, Empty Assets and Demolished Rooms


<center>
<img src="img.png" alt="" title="" width="100"/>
</center>



####<a name="3"></a> Revit 2026 Webinar Announcement

Autodesk has announced Revit 2026, and you can register here for an webinar on April 10
on [What’s New in Revit 2026](https://www.autodesk.com/webinars/aec/autodesk-whats-new-in-revit-april10).


####<a name="4"></a> Empty Appearance Asset Element

Why is AppearanceAssetElement empty in API?
https://forums.autodesk.com/t5/revit-api-forum/why-is-appearanceassetelement-empty-in-api/m-p/13388041#M84456
ask llm to summarise this post and q and a sokrates dialogue

**Question:**

I was retrieving Appearance Assets from Elements in my project and came across this door (.rvt attached) which has a material (Door - Architrave) that, even though it has Appearance assets in the UI (see image "AppearanceAssets Revit UI"), Revit Lookup cannot seem to find them, as shown by AssetProperties.Size = 0 (see image "AppearanceAssets Revit Lookup"). This is the only material in my entire project with AssetProperties.Size = 0. Is this normal? How else can I get my Appearance assets if AssetProperties.Size = 0?

AppearanceAssets Revit UI.png

AppearanceAssets Revit Lookup.png

door.rvt

**Answer:**

how funny. We talked about that very thing right here just two weeks ago:

https://forums.autodesk.com/t5/revit-api-forum/iexportcontext-material-missing-appearance-asset-data...

**Response:**

I did indeed miss that thread. However, it does not solve my problem as that is already what I am doing, with the exception of using FindByName(propertyName). For reference, I'm trying to get specific appearance asset properties from various materials, including appearance description, category and main appearance image filepath.

I've tried using renderingAsset.FindByName("Description"), renderingAsset.FindByName("Category"), renderingAsset.FindByName("UnifiedBitmapSchema") and renderingAsset.FindByName("BaseSchema") but they all return null since renderingAssets is empty, i.e. AssetProperties.Size = 0.

For reference, here is my code:

<pre><code class="language-cs">private (string, string, string) GetMaterialAssets(Document doc, int materialId)
{
  string texturePath = "";
  string description = "";
  string category = "";

  // Get material element
  Material material = doc.GetElement(new ElementId(materialId)) as Material;
  if (material != null)
  {
    // Get appearance assets
    ElementId appearanceAssetId = material.AppearanceAssetId;
    AppearanceAssetElement appearanceAssetElem = doc.GetElement(appearanceAssetId) as AppearanceAssetElement;
    if (appearanceAssetElem == null) return (texturePath, description, category);

    // Get rendering asset
    Asset assetRend = appearanceAssetElem.GetRenderingAsset();

    if (assetRend != null)
    {
      if (assetRend.Size == 0)
      {
        AssetProperty baseSchema = assetRend.FindByName("BaseSchema");
        TaskDialog.Show("Base Schema", baseSchema?.ToString());
      }

      // Go through properties
      for (int assetIdx = 0; assetIdx < assetRend.Size; assetIdx++)
      {
        AssetProperty assetProperty = assetRend[assetIdx];
        Type type = assetProperty.GetType();

        if (assetProperty.Name.ToLower() == "description")
        {
          var prop = type.GetProperty("Value");
          if (prop != null && prop.GetIndexParameters().Length == 0)
          {
            description = prop.GetValue(assetProperty).ToString();
            continue;
          }
        }
        else if (assetProperty.Name.ToLower() == "category")
        {
          var prop = type.GetProperty("Value");
          if (prop != null && prop.GetIndexParameters().Length == 0)
          {
            category = prop.GetValue(assetProperty).ToString();
            continue;
          }
        }

        if (assetProperty.NumberOfConnectedProperties < 1)
          continue;

        Asset connectedAsset = assetProperty.GetConnectedProperty(0) as Asset;
        if (connectedAsset.Name == "UnifiedBitmapSchema")
        {
          if (assetProperty.Name.Contains("bump") || assetProperty.Name.Contains("pattern_map") ||
            assetProperty.Name.Contains("shader") || assetProperty.Name.Contains("opacity"))
            continue;

          // UnifiedBitmap contains file name and path
          AssetPropertyString path = connectedAsset.FindByName(UnifiedBitmap.UnifiedbitmapBitmap) as AssetPropertyString;
          if (path == null || string.IsNullOrEmpty(path.Value))
            continue;
          string pathString = path.Value;
          if (pathString.Contains("|"))
          {
            pathString = pathString.Split('|')[0];
          }
          // remove | this character
          if (Path.IsPathRooted(pathString))
          {
            texturePath = pathString;
            continue;
          }

          // return path using default texture
          string defaultTexturePath = @"C:\Program Files\Common Files\Autodesk Shared\Materials\Textures\";
          string defaultTexturePathx86 = @"C:\Program Files (x86)\Common Files\Autodesk Shared\Materials\Textures\";

          if (Directory.Exists(defaultTexturePath))
            texturePath = defaultTexturePath + pathString;
          else if (Directory.Exists(defaultTexturePathx86))
            texturePath = defaultTexturePathx86 + pathString;
        }
      }
    }
  }

  return (texturePath, description, category);
}</code></pre>


**Answer:**

I think it's because the AppearanceAsset doesn't really exist.
I had this when editing materials in a Rvt created by a Ifc convertion.

When opening the material in the material editor revit assigns the AppearanceAsset, But it's not saved to the material on closing the editor if no changes are made to the AppearanceAsset.
Change for instance the description field of the asset and save it. Now the AppearanceAsset will also be found by the API

In my case it always was a Generic class material (ifc convertion) and not a Wood Class, maybe that's why a AppearanceAsset is created by revit with wood "settings",  likely a copy of the first existing Wood Class Asset?? (or some default)

I solved it in my case by assigning my own AppearanceAsset (copy of a template AppearanceAsset with correct settings), editing some properties an assign it to the material.

**Response:**

It was indeed as you described. By changing a property of my Appearance asset and saving the material re-applies the appearance assets in the API.

No solution in my case, other then warning the user to this issue, since I can't programatically re-assign the properties without reading the assigned values first, which I can't since renderingAssets is empty. My materials do not come from IFC conversion.

But thanks for your input!!

**Answer:**

Could be the material original also was created/duplicated by API and no asset was attached, or from a material library.
Or even a (very) old Revit style material

**Response:**


I've been told that the family I'm using (attached in my original post above), that has the material with the empty Appearance Assets (Door - Architrave) is actually one of the default families that comes with Revit 2024 installation. So assuming this is a very old family, recycled between revit versions, it might be a very old material as well.


**Answer:**

I just checked the 2024 revit project template "Default-Multi-discipline". It seems to have 22 materials without a appearance asset.
Like "Analytical Spaces", "Metal - Stainless Steel" etc..(others do have a appearance asset.)

Duplicating such material (duplicate incl. asset, shared asset not tried) will result in a material with a appearance asset (size > 0)
The original wil still miss it as nothing changed to that one.

Duplicating such material in the API will result in a material with no appearance asset, because the UI version adds it internally.
So that's what then also should be done in the API in you're addin.
How revit's UI creates the asses....well that's another topic, I think it depends on the material class and what maybe already exists in the project/family and/or some internal default assets.

**Answer:**

I haven't tried this via the API yet but, after checking the Appearance Asset Element and finding it to have a size of 0, try duplicating it and see if Revit creates a properly defined version of it, if so then you could assign the newly created Appearance Asset to the material (along with searching for and redefining any other materials that might be using it as well).
I went in and tried my suggestion.
It does work. here's the code in VB (where RDB = Revit.DB and RDV =Revit.DB.Visual):

<pre><code class="language-vb">  'Forum Issue resolution
  Public Sub ReplaceEmptyAppearanceAssets(thisDoc As RDB.Document)
    Dim printStr As String = "Invalid Assets: " & vbCrLf

    'collect document materials
    Dim matCollector As RDB.FilteredElementCollector = New RDB.FilteredElementCollector(thisDoc)
    Dim allMats As IList(Of RDB.Material) = matCollector.OfClass(GetType(RDB.Material)).OfType(Of RDB.Material).ToList
    'collect document appearance Asset Elements
    Dim assetCollector As New RDB.FilteredElementCollector(thisDoc)
    Dim allAppearanceAssets As IList(Of RDB.AppearanceAssetElement) = assetCollector.OfClass(GetType(RDB.AppearanceAssetElement)) _
      .OfType(Of RDB.AppearanceAssetElement).ToList
    'create a list of asset names in use
    Dim currentNames As New List(Of String)
    For Each appAsset As RDB.AppearanceAssetElement In allAppearanceAssets
      If currentNames.Contains(appAsset.Name) = False Then
        currentNames.Add(appAsset.Name)
      End If
    Next

    'prep for creating Asset if required
    'this takes a while on first run to expand the default library,
    'could be moved to seperate function and called if neede
    Dim assetList As List(Of RDV.Asset) = thisDoc.Application.GetAssets(RDV.AssetType.Appearance)
    Dim genericAsset As RDV.Asset = Nothing

    'really shouldn't start a transaction unless modification is needed...
    Using thisTrans As New RDB.Transaction(thisDoc, "Create new material")
      thisTrans.Start()

      Dim nameStr As String = ""

      'parse materials looking for invalid Appearance Assets
      Dim thisAssetElem As RDB.AppearanceAssetElement
      For Each thisMat As RDB.Material In allMats
        If thisMat.AppearanceAssetId &lt;&gt; RDB.ElementId.InvalidElementId Then
          Dim renderAssetElem As RDB.AppearanceAssetElement = TryCast(thisDoc.GetElement(thisMat.AppearanceAssetId), RDB.AppearanceAssetElement)

          If renderAssetElem IsNot Nothing Then
            'Check to see if it's fully defined
            'from API help
            'AppearanceAssetElement.GetRenderingAsset
            'The retrieved Asset may be empty if it is loaded from material library without any modification.
            'In this case, you can use Application.GetAssets(AssetType.Appearance) to load all preset appearance assets,
            'and retrieve the asset by its name.

            Dim thisAsset As RDV.Asset = renderAssetElem.GetRenderingAsset()
            If thisAsset.Size = 0 Then
              printStr += "Invalid Asset Size in Material: " & thisMat.Name & " - Asset: " & renderAssetElem.Name & vbCrLf
              genericAsset = assetList.FirstOrDefault(Function(eachAsset) eachAsset.Name = thisAsset.Name)
              'We could read the default properties directly from this genericAsset or
              'create new as duplicate

              'the following would be a seperate function due to replication
              nameStr = renderAssetElem.Name

              Dim numb As Integer = 1
              Dim testStr As String = nameStr

              Do While currentNames.Contains(testStr) = True
                testStr = nameStr & "_" & numb.ToString()
                numb = numb + 1
              Loop
              nameStr = testStr

              If genericAsset IsNot Nothing Then
                printStr += "  : Duplicating Asset :" & nameStr & vbCrLf
                Dim newAssetElem As RDB.AppearanceAssetElement = RDB.AppearanceAssetElement.Create(thisDoc, nameStr, genericAsset)
                thisMat.AppearanceAssetId = newAssetElem.Id
                currentNames.Add(nameStr)
              Else
                printStr += "  !! Could not aquire Asset !!" & vbCrLf
              End If
            End If
          Else
            printStr += "Cannot aquire Asset from Material: " & thisMat.Name & vbCrLf
          End If
        Else
          'from API help
          'Material.AppearanceAssetId
          'The id of the AppearanceAssetElement, or InvalidElementId if the material does not have an associated appearance asset.
          'This is the id to the element that contains visual material information used for rendering.
          'In some cases where the material is created without setting up custom render appearance properties
          '(for example, when the material is created via an import, or when it is created by the API),
          'this property will be InvalidElementId. In that situation the standard material properties
          'such as Color and Transparency will dictate the appearance of the material during rendering.

          printStr += "Invalid Asset ID in Material: " & thisMat.Name & vbCrLf
          'create new from existing generic

          'the following would be a seperate function due to replication
          nameStr = thisMat.Name
          Dim numb As Integer = 1
          Dim testStr As String = nameStr

          Do While currentNames.Contains(testStr) = True
            testStr = nameStr & "_" & numb.ToString()
            numb = numb + 1
          Loop
          nameStr = testStr

          genericAsset = assetList.FirstOrDefault(Function(eachAsset) eachAsset.FindByName(RDV.Generic.GenericDiffuse) IsNot Nothing)
          If genericAsset IsNot Nothing Then
            printStr += "  : Creating Asset :" & nameStr & vbCrLf
            Dim newAssetElem As RDB.AppearanceAssetElement = RDB.AppearanceAssetElement.Create(thisDoc, nameStr, genericAsset)
            thisMat.AppearanceAssetId = newAssetElem.Id
            currentNames.Add(nameStr)
          Else
            printStr += "  !! Could not aquire Asset from App !!" & vbCrLf
          End If

        End If
      Next

      thisTrans.Commit()
    End Using

    RUI.TaskDialog.Show("Material Info", printStr)

  End Sub</code></pre>

You will also notice a couple of comments taken from the API help that directly answer your original question of "Why is... empty..." and further to those that do not have a valid AppearanceAssetId

Running this code on your posted file found many materials with no Appearance Asset Element as well as many Assets with size=0. It creates valid Assets in both cases.

This was a good exercise, thanks for the question and I hope this helps you in some way.

**Response:**
Thank you for your answer and sample code! I tried as you suggested and it does indeed work wonderfully!
Thanks everyone for the suggestions and input!

**Answer:**
I haven't tried this via the API yet but, after checking the Appearance Asset Element and finding it to have a size of 0, try duplicating it and see if Revit creates a properly defined version of it, if so then you could assign the newly created Appearance Asset to the material (along with searching for and redefining any other materials that might be using it as well).
It could have been better of course, and it really should have two other additions to it:

- When duplicating a 0 size asset, it should keep a record of which ones it creates a duplicate for and then check the remaining materials to see if they had that same original asset and simply assign the previously created duplicate asset to it as well.
- When creating an asset for a material whose asset ID is InvalidElementId it could read the color and transparency values from the material properties and modify the created asset to have those values (which, of course, would require adding an AppearanceAssetEditScope to make those edits).


####<a name="3"></a> Revit API: Retrieving Room Data for Demolished Family Instances

My colleague Naveen Kumar shared a solution
for [Retrieving Room Data for Demolished Family Instances](https://adndevblog.typepad.com/aec/2024/10/revit-api-retrieving-room-data-for-demolished-family-instances.html):

In Revit projects, it is important to track room data for family instances, especially when they are marked as 'Existing' and later demolished during the 'New Construction' phase.

**The Problem:** Missing Room Data for Demolished Family Instances

The issue comes from how the Revit API works. The `FamilyInstance.Room` property gives room data based on the final phase of the project. If a family instance has been demolished and no longer exists in the final phase, the API might return incorrect or null values This can be problematic when accurate room data is needed from earlier phases, before the family instance was demolished.

**The Solution:** Getting Room Data by Phase

To fix this, the Revit API provides a method called `FamilyInstance.get_Room(Phase)`. This allows you to retrieve room information for the specific phase you need, even if the family instance was demolished in a later phase. It ensures you’re getting the right data for each phase, just like in Revit schedules.

Another option is to use `Document.GetRoomAtPoint(XYZ, Phase)`, which retrieves the room based on the family instance’s exact location during a specific phase. This method is useful for more complex cases, ensuring that you get accurate room data regardless of what happens to the family instances in later phases.

<pre><code class="language-cs">// Get the active document and UIDocument from the commandData
Document doc = commandData.Application.ActiveUIDocument.Document;
UIDocument uidoc = commandData.Application.ActiveUIDocument;

// Retrieve all project phases (assuming 3 phases: "Existing", "New Construction", "Final Phase")
FilteredElementCollector phaseCollector = new FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_Phases)
.WhereElementIsNotElementType();

// Find the specific phases by name
Phase existingPhase=phaseCollector.FirstOrDefault(phase=>phase.Name=="Existing") as Phase;
Phase newConstructionPhase=phaseCollector.FirstOrDefault(phase=>phase.Name=="New Construction") as Phase;
Phase finalPhase=phaseCollector.FirstOrDefault(phase=>phase.Name=="Final Phase") as Phase;

// Let the user pick an element (family instance) from the Revit model
Autodesk.Revit.DB.Reference pickedReference = uidoc.Selection.PickObject(ObjectType.Element);
Element pickedElement = doc.GetElement(pickedReference);
FamilyInstance familyInstance = pickedElement as FamilyInstance;

if (familyInstance != null)
{
   // Room in which the family instance is located during the final phase of the project
    Room currentRoom = familyInstance.Room;

   // Access the room the family instance is located in, based on a specific phase
   // Modify this to set the desired phase: existingPhase, newConstructionPhase, or finalPhase
    Phase targetPhase = existingPhase;
    Room roomInSpecificPhase = familyInstance.get_Room(targetPhase);

   // Workaround: Get the family instance's location point
   //and find the corresponding room in the specified phase.
    LocationPoint familyLocation = familyInstance.Location as LocationPoint;
    if (familyLocation != null)
      {
        XYZ locationPoint = familyLocation.Point;
        Room roomAtPoint = doc.GetRoomAtPoint(locationPoint, targetPhase);
      }
}
Automating Phase-Based View Schedule Creation for Revit Projects

You can also use the Revit API to automate the creation of view schedules for different project phases. Instead of manually creating schedules for each phase, the API can automate this process, linking each schedule to the correct phase and organizing the data properly. This saves time and ensures accuracy across all phases of the project.

// Create a filtered collector to gather all Phase elements in the document
FilteredElementCollector collector = new FilteredElementCollector(doc)
.OfCategory(BuiltInCategory.OST_Phases)
.WhereElementIsNotElementType();
using (Transaction actrans = new Transaction(doc, "Create View Schedules"))
{
  actrans.Start();
  foreach (Element e in collector)
    {
      Phase phase = e as Phase;
      if (phase != null)
        {
          // Create a view schedule for the each phase
           CreateViewSchedule(doc ,phase);
        }
    }
  actrans.Commit();
}

private void CreateViewSchedule(Document doc , Phase phase)
{
  // Create a new view schedule in the document
  //with an InvalidElementId for a multi-category schedule
   ViewSchedule viewSchedule = ViewSchedule.CreateSchedule(doc, ElementId.InvalidElementId);

  // Set the name of the schedule
   viewSchedule.Name = "API-" + phase.Name;

  // Set the phase parameter of the view schedule to the required phase
   viewSchedule.get_Parameter(BuiltInParameter.VIEW_PHASE).Set(phase.Id);

   ScheduleDefinition definition = viewSchedule.Definition;

  // Loop through all schedulable fields and add them to the schedule definition
   foreach (SchedulableField sf in definition.GetSchedulableFields())
    {
      ScheduleField field = definition.AddField(sf);
    }
}</code></pre>

####<a name="4"></a> RST Results Package Create with Api

RST Results Package Create with Api
https://forums.autodesk.com/t5/revit-api-forum/results-package-create-with-api/m-p/13093333

Explorer akoukouselis
2024-10-18 05:26 AM
Not sure if you found it. I am struggling with a similar issue.
have a look here "C:\Program Files\Autodesk\Revit 2025\AddIns\ResultsManagerExplorer" and reference Autodesk.ResultsBuilder.DBApplication.dll
Also have a look here https://forums.autodesk.com/t5/revit-api-forum/structural-analysis-toolkit-resultsbuilder-reviewing-...
Still the examples are pretty old so the code needs some tweeks (eg for the ForgetypeID).

I hope someone from Autodesk creates some updated examples regarding this functionality. Especially if we take into consideration the major changes in the API.
In my case the example works (not perfectly) for linear results but for surface results nothing comes up.
Report
 akoukouselis
Explorer akoukouselis
2024-10-19 02:17 AM
I had a better look in the ResultsBuilder functionality and decided to summarize and share some information here that other users may find helpful.
Reference to the relevant Dll "Autodesk.ResultsBuilder.DBApplication.dll" may be found under the revit installation directory \addins\ResultsManagerExplorer e.g. C:\Program Files\Autodesk\Revit 2025\AddIns\ResultsManagerExplorer
 Examples of the SDK are a little old. Thus, code needs some changes as for example using ForgeTypeId. For example AddMeasurement(result.Item1, MeasurementResultType.Surface, UnitType.UT_Area, DisplayUnitType.DUT_SQUARE_METERS, MeasurementDependencyType.LoadCaseIndependent);  Should be changed to AddMeasurement(result.Item1, MeasurementResultType.Surface, SpecTypeId.Area, UnitTypeId.SquareMeters, MeasurementDependencyType.LoadCaseIndependent);
In a similar manner you have to take into account the changes in the Structures API and the newer structural analysis model.
E.g.

<pre><code class="language-cs">AnalyticalModel analyticalModel = (doc.GetElement(elementId) as AnalyticalModel);
IList&lt;Curve&gt; curves = analyticalModel.GetCurves(AnalyticalCurveType.RawCurves);</code></pre>

is now

<pre><code class="language-cs">AnalyticalPanel analyticalModel = (doc.GetElement(elementId) as AnalyticalPanel);
IList&lt;Curve&gt; curves = analyticalModel.GetOuterContour().ToList();</code></pre>

It is not always clear in the examples but the results are provided in Units and not relative to the length of the member. E.g. xCoordinateValues = new List<double>() { 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 }; means 0.1, 0.2 …. meters and not 10% of the length.
Care should be taken with units when introducing data. In contrast with the rest of the API that the internal units of Revit should be used when sending data, the results builder does not. Have not tested it with imperial units and I am not sure if it is related with the UnitsSystem declared in the CreateResultsPackage method, but in my case(and the example of the SDK) data (length area etc) are in metric system. So do not convert to  Internal. On the other hand you might need to convert from internal. The reason I did not get any results for the surface element was that the GetSurfaceContourPoints method returned the XYZ points in the Internal Units of Revit (Imperial) so I had to convert them to metric.
From my understanding, the ResultManager actually uses the AVF so it is up to you to decide whether it is more suited for your case to go for the ResultsBuilder and Manager or directly for the AVF. Here are some pros and cons.
Using the ResultsBuilder will get you where you want to be probably faster since you do not have to set up your own handling of results packages data.  Also no need to create your own user interface for handling result presentation. Last but not least you do not have to handle AVF, with clearing and creating spatialfieldmanagers schemas etc …
On the other hand you will “inherit” the limitations of the ResultsBuilder meaning you cannot intervene with how data are stored and sometimes presented. For example, when using AVF directly you can flag which data points are to be tagged with text for diagrams.  Also did not find a way to present results that are not based on an analytical member with ResultsBuilder. AVF supports the presentation of results with references that are not based on actually Revit elements.
Thus, I think that if you want just to show some results in Revit that are typical in the structural discipline go with ResultsBuilder. On the other hand if you want to present more complex data or need more control on the data you are better off with implementing your own datastructure and use AVF directly.

####<a name="4"></a> RST ResultsBuilder SDK Sample

Waldemar [@okapawal](https://forums.autodesk.com/t5/user/viewprofilepage/user-id/1218351) Okapa of the Revit Structural Sr Product Owner answered a question
on the [structural analysis toolkit `ResultsBuilder` and reviewing stored results in Revit](https://forums.autodesk.com/t5/revit-api-forum/structural-analysis-toolkit-resultsbuilder-reviewing-stored/m-p/8778306):


When calling the AddLinearResult function, the result package is set as type of  ResultsPackageTypes.All.


The ResultsPackageTypes.Static type package should be used here because the static analysis results are saved in this function
code1.png


Answering the second question:

Inside function AddArbitraryResults is calling the method with parameter which saying that  results are not dependent on load cases.

code2.png

In the case of saving the reinforcement results, it is preferable to create a new package that will contain results for reinforcement.

<pre><code class="language-cs">        /// &lt;summary&gt;
        /// Creates an empty results package to store reinforcement results
        /// &lt;/summary&gt;
        /// &lt;param name="doc"&gt;Revit document&lt;/param&gt;
        /// &lt;returns&gt;Reference to the newly created package&lt;/returns&gt;
        private ResultsPackageBuilder createReinforcementResultsPackageBuilder( Document doc)
      {
         ResultsAccess resultsAccess = ResultsAccess.CreateResultsAccess(doc);
         ResultsPackageBuilder resultsPackageBuilder = resultsAccess.CreateResultsPackage(reinfPackageGuid, "REINFORCEMENT_ResultsInRevit", UnitsSystem.Metric, ResultsPackageTypes.RequiredReinforcement);

         resultsPackageBuilder.SetAnalysisName("Reinforcement__ResultsInRevit_Analysis");
         resultsPackageBuilder.SetModelName("ResultsInRevit_Model");
         resultsPackageBuilder.SetDescription("Sample results");
         resultsPackageBuilder.SetVendorDescription("Autodesk");
         resultsPackageBuilder.SetVendorId("ADSK");

         return resultsPackageBuilder;
      }



        /// &lt;summary&gt;
        /// Adds reinforcement results to a linear element
        /// &lt;/summary&gt;
        /// &lt;param name="resultsPackageBuilder"&gt;Reference to the results package&lt;/param&gt;
        /// &lt;param name="elementId"&gt;Id of the linear element to which results are to be added&lt;/param&gt;
        private void AddReinforcementLinearResults(ResultsPackageBuilder resultsPackageBuilder, ElementId elementId)
        {
            // Create list of some results
            // Each list element contains result type and a list of result values
            List&lt;Tuple&lt;LinearResultType, List&lt;double&gt;&gt;&gt; valuesForRnf = new List&lt;Tuple&lt;LinearResultType, List&lt;double&gt;&gt;&gt;()
            {
              new Tuple&lt;LinearResultType,List&lt;double&gt;&gt; ( LinearResultType.AsBottom, new List&lt;double&gt;() {  45.00,  30.00,  15.00,  60.00,  0.00, 0.00, 10.00, 0.00, 0.00, 90.00 }),
              new Tuple&lt;LinearResultType,List&lt;double&gt;&gt; ( LinearResultType.AsTop,    new List&lt;double&gt;() {  45.00,  30.00,  15.00,  60.00,  0.00, 0.00, 10.00, 0.00, 0.00, 90.00 }),
              new Tuple&lt;LinearResultType,List&lt;double&gt;&gt; ( LinearResultType.AsLeft,   new List&lt;double&gt;() {  45.00,  30.00,  15.00,  60.00,  0.00, 0.00, 10.00, 0.00, 0.00, 90.00 }),
              new Tuple&lt;LinearResultType,List&lt;double&gt;&gt; ( LinearResultType.AsRight,  new List&lt;double&gt;() {  45.00,  30.00,  15.00,  60.00,  0.00, 0.00, 10.00, 0.00, 0.00, 90.00 }),
            };

            // Add result domain for load independent results
            List&lt;double&gt; xCoordinateValues = new List&lt;double&gt;() { 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 };
            resultsPackageBuilder.SetBarResult(elementId, null, DomainResultType.X, xCoordinateValues);
            // Add result values
            foreach (var valueForRnf in valuesForRnf)
            {
                resultsPackageBuilder.SetBarResult(elementId, null, valueForRnf.Item1, valueForRnf.Item2);
            }
        }

        /// &lt;summary&gt;
        /// Auxiliary method. Generates a list of sample reinforcement results for points on surface element contour
        /// &lt;/summary&gt;
        /// &lt;param name="points"&gt;List of points for which arbitrary results are to be generated&lt;/param&gt;
        /// &lt;returns&gt;A list containing a number of records with arbitrary surface result type and corresponding result values&lt;/returns&gt;
        private List&lt;Tuple&lt;SurfaceResultType, List&lt;double&gt;&gt;&gt; GenerateSampleReinforcementSurfaceResultsForContour(List&lt;XYZ&gt; points)
        {
            // Create an array of arbitrary result types.
            SurfaceResultType[] surfaceResultTypes = { SurfaceResultType.AxxBottom, SurfaceResultType.AyyBottom, SurfaceResultType.AxxTop, SurfaceResultType.AyyTop };

            // Create list
            var sampleResults = new List&lt;Tuple&lt;SurfaceResultType, List&lt;double&gt;&gt;&gt;();
            double coeff = 1.0e-4;
            // Iterate over types, create a value for each point and add a record to the list
            foreach (SurfaceResultType surfaceResultType in surfaceResultTypes)
            {
                coeff *= 1.5;
                List&lt;double&gt; results = points.Select(s =&gt; (s.X * coeff + s.Y * coeff + s.Z * coeff)).ToList();
                sampleResults.Add(new Tuple&lt;SurfaceResultType, List&lt;double&gt;&gt;(surfaceResultType, results));
            }
            return sampleResults;
        }</code></pre>




I am attaching  new source code, if you use it, you will see in Revit

ResBuilder.png





















####<a name="5"></a> IntersectionResult parameter getter throws an InvalidOperationException
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

