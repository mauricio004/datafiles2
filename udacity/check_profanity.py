__author__ = 'MFlores1'

import urllib

def read_text():
    quotes = open('C:/Users/mflores1/Dropbox/Mauricio/udacity/movie_quotes.txt')
    contents_of_file = quotes.read()
    print contents_of_file
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen('http://www.wdyl.com/profanity?q='+text_to_check)
    output = connection.read()
    print output
    connection.close()


def read_text_2():
    words = {}

    for line in open('C:/Users/mflores1/Dropbox/Mauricio/udacity/movie_quotes.txt'):
        for word in line.split(' '):
            words.setdefault(word, 1)
            words[word] += 1


# read_text()
check_profanity('shot')
