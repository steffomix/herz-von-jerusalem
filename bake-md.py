import os

class Page:
    def __init__(self, filename, addPagebreak):
        self.addPagebreak = addPagebreak
        filename += '.md'
        if  not(os.path.exists(filename)):
            open(filename, 'w').close()
        
        file = open(filename, 'r')
        self.text = file.read()
        file.close()
        
    def getText(self):
        if self.text != '':
            return self.text + (pagebreak if self.addPagebreak else '')
        else:
            return ''


class Image:
    def __init__(self, filename):
        self.filename = imageSource + filename


textSource = './source/text/'
preface = textSource + 'preface/'
epilogue = textSource + 'epilogue/'
chapter1 = textSource + 'chapter-1/'
chapter2 = textSource + 'chapter-2/'
chapter3 = textSource + 'chapter-3/'


imageSource = './source/images/'
pagebreak = '<div style="page-break-after: always;"></div>'

pageFiles =[
    # preface
    Page(preface + 'preface-1.1', True),
    Page(preface + 'preface-1.2', True),
    Page(preface + 'preface-1.3', True),
    Page(preface + 'preface-1.4', True),
    Page(preface + 'preface-1.5', True),
    # chapter 1
    Page(chapter1 + 'chapter-1-preface-1', True),
    Page(chapter1 + 'chapter-1.1', True),
    Page(chapter1 + 'chapter-1-2', True),
    Page(chapter1 + 'chapter-1-3', True),
    Page(chapter1 + 'chapter-1-4', True),
    Page(chapter1 + 'chapter-1-5', True),
    Page(chapter1 + 'chapter-1-6', True),
    Page(chapter1 + 'chapter-1-7', True),
    Page(chapter1 + 'chapter-1-epilogue-1', True),
    # chapter 2
    Page(chapter2 + 'chapter-2-preface-1', True),
    Page(chapter2 + 'chapter-2.1', True),
    Page(chapter2 + 'chapter-2-2', True),
    Page(chapter2 + 'chapter-2-3', True),
    Page(chapter2 + 'chapter-2-4', True),
    Page(chapter2 + 'chapter-2-5', True),
    Page(chapter2 + 'chapter-2-6', True),
    Page(chapter2 + 'chapter-2-7', True),
    Page(chapter2 + 'chapter-2-epilogue-1', True),
    # chapter 3
    Page(chapter3 + 'chapter-3-preface-1', True),
    Page(chapter3 + 'chapter-3.1', True),
    Page(chapter3 + 'chapter-3-2', True),
    Page(chapter3 + 'chapter-3-3', True),
    Page(chapter3 + 'chapter-3-4', True),
    Page(chapter3 + 'chapter-3-5', True),
    Page(chapter3 + 'chapter-3-6', True),
    Page(chapter3 + 'chapter-3-7', True),
    Page(chapter3 + 'chapter-3-epilogue-1', True),
    # epilogue
    Page(epilogue + 'epilogue-1.1', True),
    Page(epilogue + 'epilogue-1.2', True),
    Page(epilogue + 'epilogue-1.3', True),
    Page(epilogue + 'epilogue-1.4', True),
    Page(epilogue + 'epilogue-1.5', True),
]

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

pages = []

text = ''

for page in pageFiles:
    text += page.getText()

file = open('./README.md', 'w')
file.write(text)
file.close()

