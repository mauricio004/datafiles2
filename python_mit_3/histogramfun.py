import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    word_fraction_lst = []
    for w in wordList:
        vowel_count = 0
        for v in w:
            if v in 'aeiou':
                vowel_count += 1
        word_fraction = 0.0
        try:
            word_fraction_lst.append(float(vowel_count)/len(w))
        except ZeroDivisionError:
            word_fraction_lst.append(float(0))

    pylab.hist(word_fraction_lst, numBins)
    pylab.title('Proportion of vowels in words')
    pylab.xlabel('Fraction of vowels')
    pylab.ylabel('Number of words')
    pylab.show()
if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
