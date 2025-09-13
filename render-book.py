import os
import shutil
import subprocess

# bake-md.py
# This script reads markdown files from specified directories and combines them into a single README.md file.


# Represents a page in the book.
# Each page is initialized with a filename and an option to add a page break after the content.
# @constructor
class Page:

    pagebreak = '\r\n\r\n'

    # Initializes a new Page instance.
    # @param {string} filename - The name of the file to read.
    # @param {boolean} addPagebreak - Whether to add a page break after the content.
    # @constructor 
    def __init__(self, filename, addPagebreak):
        self.addPagebreak = addPagebreak
        
        if  not(os.path.exists(filename)):
            open(filename, 'w').close()
        
        file = open(filename, 'r')
        self.text = file.read().strip()
        file.close()

        # Adjust image paths for German version
        self.text = self.text.replace('![images/', '![de/images/')
        self.text = self.text.replace('](images/', '](de/images/')

        
    # Returns the text content of the page, optionally adding a page break.
    # @returns {string} The text content of the page, with an optional page break.
    # @method getText   
    def getText(self):
        if(self.text == ''):
            return ''
        
        # search for title: to make it a top-level header
        lines = self.text.split('\n')
        title = ""
        for i in range(len(lines)):
            line = lines[i].strip()
            if(line.startswith('title:')):
                title = line.split('title:')[1].strip().strip('"').strip("'")
                break
        
        # remove qmd metadata
        if(self.text.startswith('---')):
            parts = self.text.split('---')
            if(len(parts) > 2):
                self.text = '---'.join(parts[2:]).strip()
            else:
                self.text = parts[1].strip()

        if(title != ''):
            self.text = '# ' + title + '\n\n' + self.text

        self.text += (Page.pagebreak if self.addPagebreak else '')

        return self.text
        

# extract pages from _quarto.yml

dir = 'de/'
file = open('_quarto.yml', 'r')
lines = file.readlines()
file.close()
fileLines = [line.strip() for line in lines if line.strip() != '']

pages = [Page('index.qmd', True)]
for line in fileLines:
    if(line.startswith('- ' + dir)):
        f = line.split(dir)[1].strip()
        pages.append(Page(dir + f, True))

# Iterate through each page file and append its text content to the pages list.
text = ''
for page in pages:
    text += page.getText()

def writeFile(path, content):
    file = open(path, 'w')
    file.write(content)
    file.close()
    print(str(len(content)) + ' chars written to ' + path)

writeFile('./README.md', text)

subprocess.run(['quarto', 'render'])

writeFile('./Das-Herz-von-Jerusalem/Das-Herz-von-Jerusalem.md', text)




