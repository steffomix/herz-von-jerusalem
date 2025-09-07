import os

# bake-md.py
# This script reads markdown files from specified directories and combines them into a single README.md file.


# Represents a page in the book.
# Each page is initialized with a filename and an option to add a page break after the content.
# @constructor
class Page:


    # Initializes a new Page instance.
    # @param {string} filename - The name of the file to read.
    # @param {boolean} addPagebreak - Whether to add a page break after the content.
    # @constructor 
    def __init__(self, filename, addPagebreak):
        self.addPagebreak = addPagebreak
        
        if  not(os.path.exists(filename)):
            open(filename, 'w').close()
        
        file = open(filename, 'r')
        self.text = file.read()
        file.close()

        # Adjust image paths for German version
        self.text = self.text.replace('![images/', '![de/images/')
        self.text = self.text.replace('](images/', '](de/images/')

        
    # Returns the text content of the page, optionally adding a page break.
    # @returns {string} The text content of the page, with an optional page break.
    # @method getText   
    def getText(self):
        if self.text.strip() != '':
            return self.text + (pagebreak if self.addPagebreak else '')
        else:
            return ''


# Represents the page break in the markdown file.
# This is used to separate pages in the final README.md file.
pagebreak = '\r\n\r\n<div style="page-break-after: always;"></div>\r\n\r\n'

# List of page files to be included in the README.
# Each Page object is initialized with the filename and whether to add a page break after the content
pageFiles =[
    # preface
    Page('de/index.qmd', True),
    Page('de/book-preface-index.qmd', True),
    Page('de/book-preface-1.qmd', True),
    Page('de/book-preface-2.qmd', True),
    Page('de/book-preface-3.qmd', True),
    Page('de/book-preface-4.qmd', True),
    Page('de/book-preface-5.qmd', True),
    Page('de/chapter-1-index.qmd', True),
    Page('de/chapter-1-preface-1.qmd', True),
    Page('de/chapter-1-preface-2.qmd', True),
    Page('de/chapter-1-preface-3.qmd', True),
    Page('de/chapter-1-preface-4.qmd', True),
    Page('de/chapter-1-preface-5.qmd', True),
    Page('de/chapter-1-preface-6.qmd', True),
    Page('de/chapter-1-1.qmd', True),
    Page('de/chapter-1-2.qmd', True),
    Page('de/chapter-1-3.qmd', True),
    Page('de/chapter-1-4.qmd', True),
    Page('de/chapter-1-5.qmd', True),
    Page('de/chapter-1-6.qmd', True),
    Page('de/chapter-1-7.qmd', True),
    Page('de/chapter-1-epilogue-1.qmd', True),
    Page('de/chapter-2-index.qmd', True),
    Page('de/chapter-2-preface-1.qmd', True),
    Page('de/chapter-2-preface-2.qmd', True),
    Page('de/chapter-2-preface-3.qmd', True),
    Page('de/chapter-2-preface-4.qmd', True),
    Page('de/chapter-2-1.qmd', True),
    Page('de/chapter-2-2.qmd', True),
    Page('de/chapter-2-3.qmd', True),
    Page('de/chapter-2-4.qmd', True),
    Page('de/chapter-2-5.qmd', True),
    Page('de/chapter-2-6.qmd', True),
    Page('de/chapter-2-7.qmd', True),
    Page('de/chapter-2-epilogue-1.qmd', True),
    Page('de/chapter-3-index.qmd', True),
    Page('de/chapter-3-preface-1.qmd', True),
    Page('de/chapter-3-preface-2.qmd', True),
    Page('de/chapter-3-preface-3.qmd', True),
    Page('de/chapter-3-preface-4.qmd', True),
    Page('de/chapter-3-preface-5.qmd', True),
    Page('de/chapter-3-preface-6.qmd', True),
    Page('de/chapter-3-preface-7.qmd', True),
    Page('de/chapter-3-1.qmd', True),
    Page('de/chapter-3-2.qmd', True),
    Page('de/chapter-3-3.qmd', True),
    Page('de/chapter-3-4.qmd', True),
    Page('de/chapter-3-5.qmd', True),
    Page('de/chapter-3-6.qmd', True),
    Page('de/chapter-3-7.qmd', True),
    Page('de/chapter-3-epilogue-1.qmd', True),
    Page('de/book-epilogue-index.qmd', True),
    Page('de/book-epilogue-1.qmd', True),
    Page('de/book-epilogue-2.qmd', True),
    Page('de/book-epilogue-3.qmd', True),
    Page('de/book-epilogue-4.qmd', True),
    Page('de/book-epilogue-5.qmd', True)
]


# Initialize an empty list to hold the text content of all pages.
# This will be used to create the final README.md file.   
pages = []

# Iterate through each page file and append its text content to the pages list.
text = ''


for page in pageFiles:
    pageText = page.getText()
    text += pageText

def writeFile(path, content):
    file = open(path, 'w')
    file.write(content)
    file.close()
    print(str(len(content)) + ' chars written to ' + path)

writeFile('./README.md', text)


