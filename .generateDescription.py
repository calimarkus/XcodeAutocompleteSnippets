from xml.dom import minidom
import os
import glob

print ">> Updating README.md based on .codesnippet files"

file = open('README.md', 'w')
file.write('# CodeSnippets\n\n')
file.write('These are my Xcode CodeSnippets.  \n')
file.write('To use them, clone this repository into the following path:  \n')
file.write('(The folder must be empty, to clone the repository directly in it.)  \n\n')
file.write('    cd ~/Library/Developer/Xcode/UserData/CodeSnippets\n')
file.write('    git clone git@github.com:jaydee3/CodeSnippets.git .\n\n')
file.write('And you\'re ready to go.\n\n')
file.write('#### Installing the pre-commit hook  \n\n')
file.write('This README is generated automatically using `.generateDescription.py`.  \n')
file.write('To run this script automatically before each commit, install the pre-commit hook like this:\n\n')
file.write('    sh .install-precommit-hook.sh\n\n')
file.write('## Snippet Descriptions\n\n')

listing = os.listdir(".")
for fileName in listing:
    
    if not fileName.endswith(".codesnippet"):
    	continue

    xmldoc = minidom.parse(fileName)
    keyslist = xmldoc.getElementsByTagName('key')
    allChilds = xmldoc.getElementsByTagName('dict')[0].childNodes

    for x in allChilds:
    	if not x.firstChild:
    		allChilds.remove(x)

    title=""
    summary=""
    shortcut=""
    contents=""

    for key in keyslist:
    	value = key.firstChild.nodeValue
    	if (value == "IDECodeSnippetCompletionPrefix"):
    		shortcut = allChilds[allChilds.index(key)+1].firstChild.nodeValue
    	elif value == "IDECodeSnippetContents":
    		contents = allChilds[allChilds.index(key)+1].firstChild.nodeValue
    	elif value == "IDECodeSnippetSummary":
    		summary  = allChilds[allChilds.index(key)+1].firstChild.nodeValue
    	elif value == "IDECodeSnippetTitle":
    		title    = allChilds[allChilds.index(key)+1].firstChild.nodeValue

    file.write('**' + fileName + '**  (' + title + ')  \n')
    file.write('Shortcut: `' + shortcut + '`  \n')
    file.write(summary + '\n\n')
    file.write('    ' + contents.replace('\n', '\n    ') + '\n\n')

file.close()

