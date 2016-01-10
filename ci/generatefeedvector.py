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


FILENAME = "C:/Users/mflores1/Dropbox/Mauricio/ci/chapter_3/feedlist_sample.txt"
apcount = {}
wordcounts = {}
feedlist = [line for line in file(FILENAME)]
for feedurl in feedlist:
    try:
        title, wc = getwordcounts(feedurl)
        wordcounts[title] = wc
        for word, count in wc.items():
            apcount.setdefault(word, 1)
            if count > 1:
                apcount[word] += 1

    except:
        print 'Failed to parse feed %s' % feedurl

wordlist = []
for (w, bc) in apcount.items():
    frac = float(bc) / len(feedlist)
    # if 0.1 < frac < 0.5:
    wordlist.append(w)

FILENAME_MATRIX = "C:/Users/mflores1/Dropbox/Mauricio/ci/chapter_3/blogdata.txt"
out = file(FILENAME_MATRIX, 'w')
out.write('Blog')
for word in wordlist:
    out.write('\t%s' % word)
out.write('\n')
for (blog, wc) in wordcounts.items():
    blog = blog.encode('ascii', 'ignore')
    out.write(blog)
    for word in wordlist:
        if word in wc:
            out.write('\t%d' % wc[word])
        else:
            out.write('\t0')
    out.write('\n')