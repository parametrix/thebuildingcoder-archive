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

- Chuong Ho new Revit Vibe Revit Gen AI

- Cesare Caoduro
  [@CaoduroC](https://forums.autodesk.com/t5/user/viewprofilepage/user-id/6036188)
  Convert Revit SDK documentation for local RAG (aka use it with a LLM)
  https://forums.autodesk.com/t5/revit-api-forum/convert-revit-sdk-documentation-for-local-rag-aka-use-it-with-a/td-p/13384246
  email Re: Agentic RAG tool
  Caoduro, Cesare <cesare.caoduro@aecom.com>

twitter:

 #RevitAPI
  @AutodeskRevit
   @AutodeskAPS #BIM
    @DynamoBIM

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

### Demolished Room, Empty Asset, RST Result, Gen AI and RAG



####<a name="2"></a> Empty Appearance Asset Element

Why is AppearanceAssetElement empty in API?
https://forums.autodesk.com/t5/revit-api-forum/why-is-appearanceassetelement-empty-in-api/m-p/13388041#M84456
ask llm to summarise this post and q and a sokrates dialogue

####<a name="3"></a> Revit API: Retrieving Room Data for Demolished Family Instances

Revit API: Retrieving Room Data for Demolished Family Instances
https://adndevblog.typepad.com/aec/2024/10/revit-api-retrieving-room-data-for-demolished-family-instances.html

####<a name="4"></a> RST Results Package Create with Api

RST Results Package Create with Api
https://forums.autodesk.com/t5/revit-api-forum/results-package-create-with-api/m-p/13093333
Structural Analysis Toolkit, ResultsBuilder, Reviewing Stored Results in Revit
https://forums.autodesk.com/t5/revit-api-forum/structural-analysis-toolkit-resultsbuilder-reviewing-stored/m-p/8778306

####<a name="5"></a> Revit Vibe: Generative AI in the BIM

Chuong Ho new Revit Vibe Revit Gen AI

####<a name="6"></a> Convert Revit API Help File to RAG for LLM

Cesare Caoduro
[@CaoduroC](https://forums.autodesk.com/t5/user/viewprofilepage/user-id/6036188)
Convert Revit SDK documentation for local RAG (aka use it with a LLM)
https://forums.autodesk.com/t5/revit-api-forum/convert-revit-sdk-documentation-for-local-rag-aka-use-it-with-a/td-p/13384246

email Re: Agentic RAG tool
  Caoduro, Cesare <cesare.caoduro@aecom.com>
  Hi Jeremy hope to find you well.
  I am reaching out as I am thinking to create a tutorial on how to create an agentic RAG that is an expert in Revit APIs. As one of the sources for that RAG, I was hoping I could use your blog as a source.
  Before I go and do that, I wanted to. let you know and get your permission. If that’s ok, I will publish the entire process and cite you of course.
  After that the idea is to add more knowledge using the SDK documentation, and finally build a Revit addin that consumes that local model. Everything will be leveraging opensource or free for commercial use tools.
  What do you think? There is sooo much knowledge embedded in your work, that would just be nice to be able to access it at your fingertips 😊
  Cheers,
  Cesare Caoduro
  Development & Integration Director, Enterprise Capabilities
  M +61 483 191 342
  cesare.caoduro@aecom.com
  Click here to connect with me on LinkedIn
  AECOM
  L21 420, George Street
  Address Line 2
  Sydney, 2000, Australia
  T +61 02 893 40000
Dear Cesare,
  I think that is a splendid idea that I wholeheartedly support. You certainly have my permission.
  In fact, I looked at similar ideas myself already; here are some notes that might come in handy for you:
  APS Accelerator and Q4R4 Chunking with Claude
  LLM Prompting, RAG Ingestion and New Projects
  Docling Markdown Generator
  Please let me know if I can help you in any way. Looking forward to hearing how it goes.
  Thank you and good luck!
  Cheers
  jeremy

with all this hypes around LLMs, MCPs, RAG, and everything else you read in your LinkedIn feed, I also wanted to give my 2 cents.
I was looking at an automated way to pull the SDK documentation into a vector database, in a way that was useful. As you know the documentation comes as a chm file which is basically a zip file with a lot of HTML in it.
Unfortunately, HTML files are very verbose and full of unwanted tags. Markdown (md) files, on the other hand, are just text files with some unique syntax to apply styles. and they turn to be very good for embeddings.
So, I started to use out of the box libraries in python to convert html to markdown, but the problem is that the results were absolutely rubbish. One major issue (specifically with the Revit SDK documentation) is that there are JavaScript that will be executed when you click on certain things in the page. An example with the Revit documentation is the availability of multiple examples depending on the programming language of your choice (C#, VB, F#, etc.).
It took me a bit of sweeting and a good amount of Cursor (if you don't know what it is,
check out [Cursor &ndash; The AI Code Editor](https://www.cursor.com/)),
to come up with an approach to properly parse the html into md, and maintain a decent format.
Without further ado, here the code. Test it and let me know!
If you like it, I can also publish a quick tutorial on how to get this to work with a LLMs locally.

<pre><code class="language-py">import os
import re
import shutil
import asyncio
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
import html2text
import aiofiles

# Lists to customize removals.
tags_to_remove = [
  "iframe",
  "object",
  "script",
  "br",
  "img"
]

classes_to_remove = [
  "collapsibleAreaRegion",
  "collapsibleRegionTitle",
  "collapseToggle",
  "codeSnippetContainerTab",
  "codeSnippetToolBar",
  "codeSnippetContainerTabs",
]

ids_to_remove = [
  "PageFooter",
]

def update_links(soup):
  for a in soup.find_all('a', href=True):
    if a['href'] == "#PageHeader":
      a.decompose()
    elif a['href'].lower().endswith(('.htm', '.html')):
      base, _ = os.path.splitext(a['href'])
      a['href'] = base + ".md"
  return soup

def remove_unwanted_elements(soup):
  for script in soup.find_all("script"):
    script.decompose()
  for tag in tags_to_remove:
    for element in soup.find_all(tag):
      element.decompose()
  for tag in soup.find_all(lambda tag: tag.has_attr("class") and any(cls in tag.get("class") for cls in classes_to_remove)):
    tag.decompose()
  for element_id in ids_to_remove:
    for tag in soup.find_all(id=element_id):
      tag.decompose()
  return soup

def replace_code_snippets(soup):
  id_to_lang = {
    "IDAB_code_Div1": "csharp",
    "IDAB_code_Div2": "vb",
    "IDAB_code_Div3": "cpp",
    "IDAB_code_Div4": "fsharp"
  }
  code_blocks = {}
  counter = 0
  for div_id, lang in id_to_lang.items():
    for code_div in soup.find_all("div", id=div_id):
      counter += 1
      pre_tag = code_div.find("pre")
      if pre_tag:
        code_text = pre_tag.get_text()
      else:
        code_text = code_div.get_text()
      placeholder = f"&lt;&lt;CODE_BLOCK_{counter}&gt;&gt;"
      code_block_markdown = f"```{lang}\n{code_text}\n```\n"
      code_blocks[placeholder] = code_block_markdown
      new_node = soup.new_string(placeholder)
      code_div.replace_with(new_node)
  return soup, code_blocks

def convert_html_to_markdown(html_content):
  soup = BeautifulSoup(html_content, "html.parser")
  soup = remove_unwanted_elements(soup)
  soup = update_links(soup)
  soup, code_blocks = replace_code_snippets(soup)
  modified_html = str(soup)
  h = html2text.HTML2Text()
  h.body_width = 0
  markdown_text = h.handle(modified_html)
  for placeholder, code_block in code_blocks.items():
    markdown_text = markdown_text.replace(placeholder, code_block)
  markdown_text = fix_tables(markdown_text)
  return markdown_text

def fix_tables(markdown_text):
  lines = markdown_text.splitlines()
  fixed_lines = []
  i = 0
  while i &lt; len(lines):
    if '|' in lines[i] and i+1 &lt; len(lines) and re.match(r'^[\s\-\|:]+$', lines[i+1]):
      table_lines = []
      while i &lt; len(lines) and '|' in lines[i]:
        table_lines.append(lines[i])
        i += 1
      table_lines = fix_table_block(table_lines)
      fixed_lines.extend(table_lines)
    else:
      fixed_lines.append(lines[i])
      i += 1
  return "\n".join(fixed_lines)

def fix_table_block(table_lines):
  split_lines = [[cell.strip() for cell in line.split("|")] for line in table_lines]
  header = split_lines[0]
  if header and header[0] == "":
    header = header[1:]
  remove_first = header and (header[0] == "-" or header[0] == "")
  if remove_first:
    new_split_lines = []
    for row in split_lines:
      if row and row[0] == "":
        row = row[1:]
      new_split_lines.append(row[1:])
  else:
    new_split_lines = split_lines
  new_lines = []
  for row in new_split_lines:
    new_line = "| " + " | ".join(row) + " |"
    new_lines.append(new_line)
  return new_lines

def clear_folder(folder_path):
  """Delete all files and folders within the specified folder."""
  if os.path.exists(folder_path):
    for filename in os.listdir(folder_path):
      file_path = os.path.join(folder_path, filename)
      try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
          os.unlink(file_path)
        elif os.path.isdir(file_path):
          shutil.rmtree(file_path)
      except Exception as e:
        print(f'Failed to delete {file_path}. Reason: {e}')
  else:
    os.makedirs(folder_path)

async def export_chm_to_htm(chm_path, export_folder):
  """
  Export HTML files from a CHM file using 7-Zip asynchronously.
  """
  if not os.path.exists(export_folder):
    os.makedirs(export_folder)
  clear_folder(export_folder)

  seven_zip = r"C:\Program Files\7-Zip\7z.exe"
  if not os.path.exists(seven_zip):
    print("7z.exe not found. Please install 7-Zip and update the seven_zip path accordingly.")
    return

  try:
    process = await asyncio.create_subprocess_exec(
      seven_zip, "x", chm_path, f"-o{export_folder}",
      stdout=asyncio.subprocess.PIPE,
      stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    print(stdout.decode())
    if stderr:
      print(stderr.decode())
  except Exception as e:
    print(f"Error extracting CHM file using 7z.exe: {e}")

async def process_file(executor, input_path, output_path, semaphore):
  """Process a single HTML file asynchronously using a semaphore to limit concurrent file I/O."""
  loop = asyncio.get_running_loop()
  try:
    async with semaphore:
      async with aiofiles.open(input_path, "r", encoding="utf-8") as f:
        html_content = await f.read()
    markdown_content = await loop.run_in_executor(executor, convert_html_to_markdown, html_content)
    async with semaphore:
      async with aiofiles.open(output_path, "w", encoding="utf-8") as f:
        await f.write(markdown_content)
  except Exception as e:
    print(f"Error processing {input_path}: {e}")

async def process_folder_async(input_folder, output_folder, max_workers=4, semaphore_limit=20, batch_size=10):
  """
  Asynchronously process HTML files in batches.

  For each batch, processes 'batch_size' files concurrently, waits for them to finish,
  then prints a summary showing the batch number, how many files were processed,
  and how many remain.
  """
  html_folder = os.path.join(input_folder, "html")
  if not os.path.exists(html_folder):
    print(f"HTML folder does not exist: {html_folder}")
    return

  if not os.path.exists(output_folder):
    os.makedirs(output_folder)

  file_list = [f for f in os.listdir(html_folder) if f.lower().endswith((".htm", ".html"))]
  total_files = len(file_list)
  print(f"Found {total_files} HTML files to process in {html_folder}")

  semaphore = asyncio.Semaphore(semaphore_limit)
  with ThreadPoolExecutor(max_workers=max_workers) as executor:
    for i in range(0, total_files, batch_size):
      batch_files = file_list[i:i + batch_size]
      batch_tasks = []
      for filename in batch_files:
        input_path = os.path.join(html_folder, filename)
        base, _ = os.path.splitext(filename)
        output_filename = base + ".md"
        output_path = os.path.join(output_folder, output_filename)
        batch_tasks.append(process_file(executor, input_path, output_path, semaphore))
      await asyncio.gather(*batch_tasks)
      batch_number = (i // batch_size) + 1
      processed_in_batch = len(batch_files)
      remaining = total_files - (i + processed_in_batch)
      print(f"Batch {batch_number}: Processed {processed_in_batch} files. {remaining} files remaining.")

async def main():
  # --- Configuration ---
  input_folder = r"C:\Revit 2025.3 SDK\extracted"
  output_folder = r"C:\Revit 2025.3 SDK\extracted\output"
  chm_file_path = r"C:\Revit 2025.3 SDK\RevitAPI.chm"  # Set your CHM file path here

  print("Clearing existing folders...")
  clear_folder(input_folder)
  clear_folder(output_folder)


  if chm_file_path and os.path.exists(chm_file_path) and chm_file_path.lower().endswith(".chm"):
    print(f"Exporting CHM file {chm_file_path} to HTML...")
    await export_chm_to_htm(chm_file_path, input_folder)
  elif chm_file_path:
    print("Provided CHM file does not exist or is not a CHM file.")

  print("Converting HTML files to Markdown asynchronously in batches...")
  await process_folder_async(input_folder, output_folder, max_workers=8, semaphore_limit=20, batch_size=50)

if __name__ == "__main__":
  asyncio.run(main())</code></pre>

p.s.: I have also a version of the script that works in C# is someone is interested.

p.p.s: I have also a script to pulls the entire "The Building Coder" blog into RAG.
I did ask permission from @jeremytammik for this 🙂

Congratulations to cesare on this nice project, and many thanks for sharing it.

Some thoughts and questions that come to mind:

- Have you tried using the Docling Markdown Generator? Does it handle CHM?
- https://thebuildingcoder.typepad.com/blog/2025/02/tools-for-extensible-storage-and-oauth-auth0.html#5
- What is you use case for the RAG? How do you feed this in to your processing system? What system are you using it for?
- LangChain provides several integrated CHM reader libraries, I believe, and can also generate a vector databaase right out of the box, afaik. How does this compare to your approach?



<center>
<img src="img/.png" alt="" title="" width="100"/>
</center>


<pre><code class="language-cs"></code></pre>

