# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "c:/users/mflores1/datafiles/python_mit_2/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList


def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    #>>> isWord(wordList, 'bat') returns
    True
    #>>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList


def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)


def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])


def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scramble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i - 1] == ' ']
    return applyShift(s, shifts)[:-1]


def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    # Create dictionary & add lower case letters
    alpha_lc = string.ascii_lowercase
    alpha_dict = {}
    for lc in alpha_lc:
        index_key = alpha_lc.index(lc)
        index_value = index_key + shift
        if index_value < 26:
            alpha_dict[lc] = alpha_lc[index_value]
        elif 26 <= index_value <= 50:
            index_value -= 26
            alpha_dict[lc] = alpha_lc[index_value]

    # add upper case letters
    alpha_uc = string.ascii_uppercase
    for uc in alpha_uc:
        index_key = alpha_uc.index(uc)
        index_value = index_key + shift
        if index_value < 26:
            alpha_dict[uc] = alpha_uc[index_value]
        elif 26 <= index_value <= 50:
            index_value -= 26
            alpha_dict[uc] = alpha_uc[index_value]

    return alpha_dict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    encodedtext = ""
    for c in text:
        encodedtext += coder.get(c, c)
    return encodedtext

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))
#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    #Create a dictionary to store the shift and number of valid words.
    shift_dict = {}
    #For all possible shifts (0 to 25).
    for i in range(25):
        # Use applyshift method to decrypte the text.
        decrypted_text = applyShift(text, i)
	    # Store decrypted text in a list (consider using string.split function)
        decrypted_text_list = decrypted_text.split(' ')
	    # For all possible words in the list, check to see if word is valid (use isWord function).
        count = 0
        for w in decrypted_text_list:
        # Count the number of valid words and store it in dictionary
            if isWord(wordList, w):
                count += 1
        shift_dict[i] = count

    # Use the dictionary, return the shift with the highest number of valid words.
    max = 0
    for k in shift_dict:
        if shift_dict[k] > max:
            max = k
    return max

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList = loadWords()
    bestshift = findBestShift(wordList, getStoryString())
    return applyShift(getStoryString(), bestshift)

#
# Build data structures used for entire session and run encryption
#

def main():
    # To test findBestShift:
    # wordList = loadWords()
    # s = applyShift('Hello, world!', 8)
    # bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    decryptStory()


if __name__ == '__main__':
    main()
