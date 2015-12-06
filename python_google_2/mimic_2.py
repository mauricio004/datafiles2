#!/usr/bin/python -tt

"""Mimic exercise"""

import sys
import random


def read_file(filename):
    """Returns a dictionary of words with all subsequent words in a list."""
    mimic_dict = {}
    f = open(filename, 'r')
    text = f.read()
    f.close()
    words_list = text.split()
    prev = ''

    for word in words_list:
        if prev not in mimic_dict:
            mimic_dict[prev] = [word]
        else:
            mimic_dict[prev].append(word)
        prev = word
    return mimic_dict


def print_words(mimic_dict, word):
    """Prints a word and a randomly subsequent word """
    for unused_i in range(200):
        print(word, end=' ')
        if unused_i % 15 == 0:
            print()
        next = mimic_dict.get(word)          # Returns None if not found
        if not next:
            next = mimic_dict['']  # Fallback to '' if not found
        word = random.choice(next)


def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    #dict = read_file('c:/users/mflores1/pycharmprojects/practicepython/alice.txt')
    dict = read_file(sys.argv[1])
    print_words(dict, '')


if __name__ == '__main__':
    main()
