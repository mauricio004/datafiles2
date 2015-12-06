#!/usr/bin/python -tt

"""Mimic exercise"""

import sys
import random


def read_file(filename):
    """Returns a dictionary of words with all subsequent words in a list."""
    words_dict = {}
    index = 0  # Start with second word
    f = open(filename, 'r')
    text_list = f.read().replace('/n', '').split()

    for word in text_list:
        index += 1
        sub_index = index + 1
        if sub_index < len(text_list):
            if word in words_dict:
                if text_list[sub_index] not in words_dict[word]:
                    words_dict[word].append(text_list[sub_index])
            else:
                list_subs_words = [text_list[sub_index]]
                words_dict[word] = list_subs_words
    f.close()
    return words_dict


def print_words(filename):
    """Prints a word and a randomly subsequent word """
    word_dict = read_file(filename)
    word_list_output = []
    first_word = "Alice's"
    word_list_output.append(first_word)

    for i in range(0, 100):
        next_word = random.choice(word_dict[word_list_output[i]])
        word_list_output.append(next_word)

    for word in word_list_output:
        print(word, end=" ")


def main():
    #print_text('c:/users/mflores1/pycharmprojects/practicepython/alice.txt')

    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(0)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--mimic':
        print_words(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
