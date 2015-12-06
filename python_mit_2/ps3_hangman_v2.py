# 6.00 Problem Set 3
#
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "c:/Users/mflores1/pycharmprojects/practicepython/python_mit/words_ps3.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print("Loading word list from file...")
    # inFile: file
    # inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    # line = inFile.readline()
    # wordlist: list of strings
    # wordlist = string.split(line)
    # print("  ", len(wordlist), "words loaded.")
    # return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    count = 0
    for c in secretWord:
        if c in lettersGuessed:
            count += 1
    if count == len(secretWord):
        return True
    return False


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    temp_guess = secretWord
    for c in secretWord:
        if c not in lettersGuessed:
            temp_guess = temp_guess.replace(c, "_ ")
    return temp_guess


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    temp_alpha = string.ascii_lowercase
    for c in lettersGuessed:
        if c in temp_alpha:
            temp_alpha = temp_alpha.replace(c, '')
    return temp_alpha


def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    """
    letters_guessed = []
    max_guesses = 8
    guesses_left = max_guesses
    mistakes_made = 0
    available_letters = getAvailableLetters(letters_guessed)
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")
    while not isWordGuessed(secretWord, letters_guessed) and guesses_left > 0:
        print("You have " + str(guesses_left) + " guesses left")
        print("Available letters: " + available_letters)
        # Need to update raw input
        guess_letter = input("Please guess a letter: ")
        guess_letter_lower = guess_letter.lower()
        if guess_letter_lower in letters_guessed:
            print("Oops! You've already guessed that letter:" + getGuessedWord(secretWord, letters_guessed))
            print("-----------")
        else:
            letters_guessed.append(guess_letter_lower)
            available_letters = getAvailableLetters(letters_guessed)
            if guess_letter_lower in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, letters_guessed))
                print("-----------")
                if isWordGuessed(secretWord, letters_guessed):
                    print("Congratulations, you won!")
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, letters_guessed))
                print("-----------")
                mistakes_made += 1
                guesses_left = max_guesses - mistakes_made
                if guesses_left == 0:
                    print("Sorry, you ran out of guesses. The word was " + secretWord)


def main():
    secretWord = 'y'
    hangman(secretWord)
    #print(getGuessedWord(secretWord, ['r', 'c', 'l', 'a', 'q', 'w', 'k', 'i', 'g', 'j']))

if __name__ == '__main__':
    main()



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)