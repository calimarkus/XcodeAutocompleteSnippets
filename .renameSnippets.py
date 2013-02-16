from xml.dom import minidom
import os
import glob
import re

# define first character lowercase function
first_lower = lambda s: s[:1].lower() + s[1:] if s else ''

print "Updating codesnippet filenames with their actual titles"

count = 0
listing = os.listdir(".")
for fileName in listing:
    
    # ignore other files than snippets
    if not fileName.endswith(".codesnippet"):
    	continue

    # parse snippet file
    xmldoc = minidom.parse(fileName)
    keyslist = xmldoc.getElementsByTagName('key')
    allChilds = xmldoc.getElementsByTagName('dict')[0].childNodes

    for x in allChilds:
    	if not x.firstChild:
    		allChilds.remove(x)

    snippetTitle = None

    # find title
    for key in keyslist:
    	value = key.firstChild.nodeValue
    	if value == "IDECodeSnippetTitle":
    		snippetTitle = allChilds[allChilds.index(key)+1].firstChild.nodeValue

    # if snippet has a title
    if not snippetTitle == None:

      # build filename (only a-zA-Z)
      snippetTitle = snippetTitle.replace("&","and")
      allWords = re.findall("[a-zA-Z]+", snippetTitle)
      uppercaseWords = map(lambda x: x.title(), allWords)
      newName = "".join(uppercaseWords) + ".codesnippet"
      newName = first_lower(newName)

      # if name changed, rename file
      if not newName == fileName:
        os.rename(fileName, newName)
        count = count + 1

        # log renamed files
        print " renamed: " + fileName + " -> "
        print "          " + newName

# show total count
print str(count) + " snippets renamed."



