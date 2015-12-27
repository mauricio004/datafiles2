__author__ = 'MFlores1'


import feedparser
import re

# Returns title and dictionary of word counts for an RSS feed

def getwordcounts(url):
    # Parse the feed
    d = feedparser.parse(url)
    wc = {}

    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        # Extract list of words
        words = getWords(e.title+' '+summary)
        for word in words:
            wc.setdefault(word,0)
            wc[word] += 1
    return d.feed.title, wc


def getWords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


FILENAME = "C:/Users/mflores1/Dropbox/Mauricio/ci/chapter_3/feedlist.txt"
appcount = {}
wordcounts = {}
feedlist = [line for line in file(FILENAME)]
for feedurl in feedlist:
    try:
        title, wc = getwordcounts(feedurl)
        wordcounts[title] = wc
        for word, count in wc.items():
            appcount.setdefault(word, 0)
            if count > 1:
                appcount[word] += 1

    except:
        print 'Failed to parse feed %s' % feedurl

x = 8