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
        filename += '.md'
        if  not(os.path.exists(filename)):
            open(filename, 'w').close()
        
        file = open(filename, 'r')
        self.text = file.read()
        file.close()
        
    # Returns the text content of the page, optionally adding a page break.
    # @returns {string} The text content of the page, with an optional page break.
    # @method getText   
    def getText(self):
        if self.text.strip() != '':
            return self.text + (pagebreak if self.addPagebreak else '')
        else:
            return ''

# Represents an image with a filename.
# @constructor
class Image:
    def __init__(self, filename):
        self.filename = imageSource + filename

# Represents the source directories for text and images.
# The textSource is the base directory for all text files.
textSource = './source/text/'

# The textSource contains subdirectories for the preface, epilogue, and chapters.
# Each subdirectory contains markdown files for the respective sections of the book.
# The preface, epilogue, and chapters are subdirectories within the textSource.
preface = textSource + 'preface/'
epilogue = textSource + 'epilogue/'
chapter1 = textSource + 'chapter-1/'
chapter2 = textSource + 'chapter-2/'
chapter3 = textSource + 'chapter-3/'

# Represents the source directories for images.
imageSource = './source/images/'

# Represents the page break in the markdown file.
# This is used to separate pages in the final README.md file.
pagebreak = '\r\n\r\n<div style="page-break-after: always;"></div>\r\n\r\n'

# List of page files to be included in the README.
# Each Page object is initialized with the filename and whether to add a page break after the content
pageFiles =[
    # preface
    Page(preface + 'preface-1-1', True),
    Page(preface + 'preface-1-2', True),
    Page(preface + 'preface-1-3', True),
    Page(preface + 'preface-1-4', True),
    Page(preface + 'preface-1-5', True),
    Page(preface + 'preface-1-6', True),
    # chapter 1
    Page(chapter1 + 'chapter-1-preface-1', True),
    Page(chapter1 + 'chapter-1-preface-2', True),
    Page(chapter1 + 'chapter-1-preface-3', True),
    Page(chapter1 + 'chapter-1-preface-4', True),
    Page(chapter1 + 'chapter-1-preface-5', True),
    Page(chapter1 + 'chapter-1-preface-6', True),
    Page(chapter1 + 'chapter-1-1', True),
    Page(chapter1 + 'chapter-1-2', True),
    Page(chapter1 + 'chapter-1-3', True),
    Page(chapter1 + 'chapter-1-4', True),
    Page(chapter1 + 'chapter-1-5', True),
    Page(chapter1 + 'chapter-1-6', True),
    Page(chapter1 + 'chapter-1-7', True),
    Page(chapter1 + 'chapter-1-epilogue-1', True),
    # chapter 2
    Page(chapter2 + 'chapter-2-preface-1', True),
    Page(chapter2 + 'chapter-2-preface-2', True),
    Page(chapter2 + 'chapter-2-preface-3', True),
    Page(chapter2 + 'chapter-2-preface-4', True),
    Page(chapter2 + 'chapter-2-1', True),
    Page(chapter2 + 'chapter-2-2', True),
    Page(chapter2 + 'chapter-2-3', True),
    Page(chapter2 + 'chapter-2-4', True),
    Page(chapter2 + 'chapter-2-5', True),
    Page(chapter2 + 'chapter-2-6', True),
    Page(chapter2 + 'chapter-2-7', True),
    Page(chapter2 + 'chapter-2-8', True),
    Page(chapter2 + 'chapter-2-9', True),
    Page(chapter2 + 'chapter-2-10', True),
    Page(chapter2 + 'chapter-2-epilogue-1', True),
    # chapter 3
    Page(chapter3 + 'chapter-3-preface-1', True),
    Page(chapter3 + 'chapter-3-preface-2', True),
    Page(chapter3 + 'chapter-3-preface-3', True),
    Page(chapter3 + 'chapter-3-preface-4', True),
    Page(chapter3 + 'chapter-3-preface-5', True),
    Page(chapter3 + 'chapter-3-preface-6', True),
    Page(chapter3 + 'chapter-3-preface-7', True),
    Page(chapter3 + 'chapter-3-1', True),
    Page(chapter3 + 'chapter-3-2', True),
    Page(chapter3 + 'chapter-3-3', True),
    Page(chapter3 + 'chapter-3-4', True),
    Page(chapter3 + 'chapter-3-5', True),
    Page(chapter3 + 'chapter-3-6', True),
    Page(chapter3 + 'chapter-3-7', True),
    Page(chapter3 + 'chapter-3-epilogue-1', True),
    # epilogue
    Page(epilogue + 'epilogue-1-1', True),
    Page(epilogue + 'epilogue-1-2', True),
    Page(epilogue + 'epilogue-1-3', True),
    Page(epilogue + 'epilogue-1-4', True),
    Page(epilogue + 'epilogue-1-5', True),
]

# List of image files to be included in the README.
# Each Image object is initialized with the filename.   
imageFiles = [
    Image('staff-1.png'),
    Image('staff-2.png'),
    Image('staff-3.png'),
    Image('staff-4.png'),
    Image('staff-5.png'),
    Image('staff-6.png'),
    Image('staff-7.png'),
    Image('flute-1.png'),
    Image('flute-2.png'),
    Image('flute-3.png'),
    Image('flute-4.png'),
    Image('flute-5.png'),
    Image('flute-6.png'),
    Image('flute-7.png'),
    Image('staff-7-with-crown.png'),
    Image('staff-and-flute.png'),
    Image('staff-blossom-temple.png'),
    Image('staff-all.png'),
    Image('blossom-crown.png'),
]

# Initialize an empty list to hold the text content of all pages.
# This will be used to create the final README.md file.   
pages = []

# Iterate through each page file and append its text content to the pages list.
# If the page has an image, it will be added as well.
text = ''


for page in pageFiles:
    pageText = page.getText()
    text += pageText

file = open('./README.md', 'w')
file.write(text)
print(str(len(text)) + ' chars written to README.md')
file.close()

