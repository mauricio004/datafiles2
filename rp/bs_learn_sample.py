__author__ = 'mflores1'


from bs4 import BeautifulSoup, NavigableString, Tag
FILENAME = "C:/Users/mflores1/dropbox/Mauricio/hot_pad_sample_only_1.txt"

exampleFile = open(FILENAME)
soup = BeautifulSoup(exampleFile, 'html5lib')
for br in soup.findAll('br'):
    next = br.nextSibling
    if not (next and isinstance(next, NavigableString)):
        continue
    next2 = next.nextSibling
    if next2 and isinstance(next2, Tag) and next2.name == 'br':
        text = str(next).strip()
        if text:
            print "Found:", next
