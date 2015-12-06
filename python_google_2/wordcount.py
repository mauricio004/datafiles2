#!/usr/bin/python -tt

"""Wordcount exercise"""

import sys


def read_file(filename):
    """Returns a word/count dict for this filename."""
    words_dict = {}
    f = open(filename, 'r')

    for line in f:
        for word in line.split():
            word = word.lower()
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    f.close()
    return words_dict


def print_words(filename):
    """Prints one per line '<word> <count>' sorted by word for the given file."""
    words_dict = read_file(filename)

    for w in sorted(words_dict.keys()):
        print(w, '  ', words_dict[w])


def get_count(words_tuple):
    """Returns the count from a dict word/count tuple  -- used for custom sort."""
    return words_tuple[1]


def print_top(filename):
    """Prints the top count listing for the given file."""
    words_dict = read_file(filename)
    items = sorted(words_dict.items(), key=get_count, reverse=True)

    for item in items[:20]:
        print(item[0], item[1])


def main():
    print_words('c:/users/mflores1/pycharmprojects/practicepython/python_google/small.txt')
    # print('-' * 60)
    # print_top('c:/users/mflores1/pycharmprojects/practicepython/small.txt')

    #if len(sys.argv) != 3:
    #    print('usage: ./wordcount.py {--count | --topcount} file')
    #    sys.exit(0)

    #option = sys.argv[1]
    #filename = sys.argv[2]
    #if option == '--count':
    #    print_words(filename)
    #elif option == '--topcount':
    #    print_top(filename)
    #else:
    #    print('unknown option: ' + option)
    #    sys.exit(1)

if __name__ == '__main__':
    main()
