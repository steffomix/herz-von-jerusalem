import os
import shutil
import subprocess



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
        self.filename = filename
        self.text = ''
        
        if  os.path.exists(filename):
            file = open(filename, 'r')
            self.text = file.read().strip()

            # Adjust image paths for German version
            self.text = self.text.replace('![images/', '![de/images/')
            self.text = self.text.replace('](images/', '](de/images/')
            return

        if(self.text == ''):
            self.text = '\r\n\r\n' + '# ' + filename.strip().strip('"') + '\r\n'

        
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
part = '- part: '
file = open('_quarto.yml', 'r')
lines = file.readlines()
file.close()
fileLines = [line.strip() for line in lines if line.strip() != '']

pages = [Page('index.qmd', True)]
for line in fileLines:
    if(line.startswith(part)):
        header = line.split(part)[1].strip()
        pages.append(Page(header, True))
        continue
    
    if(line.startswith('- ' + dir)):
        f = line.split(dir)[1].strip()
        pages.append(Page(dir + f, True))

# Join pages to final book text in markdown format
text = ''
for page in pages:
    print(page.filename)
    text += page.getText()

readmeFile = './README.md'

file = open(readmeFile, 'w')
file.write(text)
file.close()
print(str(len(text)) + ' chars written to ' + readmeFile)

subprocess.run(['quarto', 'render'])

dest = '/Das-Herz-von-Jerusalem'
shutil.copy(readmeFile, '.' + dest + dest + '.md')
shutil.copy('.' + dest+ '/index.html', '.' + dest + dest + '.html')



