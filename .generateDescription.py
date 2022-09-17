from xml.dom import minidom
import os
import glob

print (">> Updating README.md based on .codesnippet files")

file = open('README.md', 'w')
file.write('# CodeSnippets\n\n')
file.write('These are my Xcode CodeSnippets.  \n')
file.write('To use them, clone this repository into the following path:  \n')
file.write('(The folder must be empty, to clone the repository directly in it.)  \n\n')
file.write('```sh\n')
file.write('cd ~/Library/Developer/Xcode/UserData/CodeSnippets\n')
file.write('git clone git@github.com:jaydee3/CodeSnippets.git .\n\n')
file.write('```\n')
file.write('And you\'re ready to go.\n\n')
file.write('#### Installing the pre-commit hook  \n\n')
file.write('This README is generated automatically using `.generateDescription.py`.  \n')
file.write('To run this script automatically before each commit, install the pre-commit hook like this:\n\n')
file.write('```sh\n')
file.write('sh .install-precommit-hook.sh\n\n')
file.write('```\n')
file.write('## Snippet Descriptions\n\n')

# get all filenames and sort by name
listing = os.listdir(".")
listing.sort()

for fileName in listing:
    
    # ignore other files than snippets & ignore focus ones
    if fileName.startswith("focus_") or not fileName.endswith(".codesnippet"):
        continue

    # parse snippet file
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
    lang=""

    # parse relevant fields
    for key in keyslist:
        value = key.firstChild.nodeValue
        if (value == "IDECodeSnippetCompletionPrefix"):
            shortcut = allChilds[allChilds.index(key)+1].firstChild.nodeValue
        elif value == "IDECodeSnippetContents":
            contents = allChilds[allChilds.index(key)+1].firstChild.nodeValue
        elif value == "IDECodeSnippetSummary":
            summary = allChilds[allChilds.index(key)+1].firstChild.nodeValue
        elif value == "IDECodeSnippetTitle":
            title = allChilds[allChilds.index(key)+1].firstChild.nodeValue
        elif value == "IDECodeSnippetLanguage":
            langstr = allChilds[allChilds.index(key)+1].firstChild.nodeValue
            if langstr.endswith("Swift"):
                lang = "Swift"
            else:
                lang = "Obj-C"

    # write snippet description to README.md
    file.write('**' + title + '**  \n')
    file.write(summary + '\n\n')
    file.write('Shortcut: `' + shortcut + '`  \n')
    file.write('File: `' + fileName + '`  \n\n')
    file.write('```' + lang + '\n' + contents + '\n```\n\n')

file.close()

