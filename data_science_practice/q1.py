__author__ = 'MFlores1'

import re
def read_text(filename):
    txt_dict = {}
    lines_lst = []

    # Open file and read text
    try:
        with open(filename, 'r') as f:
            text = f.read()
    except Exception as err:
        print 'Error reading file ' + str(err)

    # Count all lines in text
    lines_lst_all = text.splitlines()

    # Remove empty lines
    for l in lines_lst_all:
        if l != "":
            lines_lst.append(l)

    # Extract list of words
    words = get_words(text)

    # Create dictionary of words
    for word in words:
        txt_dict.setdefault(word, 0)
        txt_dict[word] += 1

    total_word_count = sum(txt_dict.values())
    unique_words = len(txt_dict.keys())
    number_of_sentences = len(lines_lst)

    return total_word_count, unique_words, number_of_sentences, txt_dict


def get_words(txt):
    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


def print_top(txt_dict, top=20):
    txt_list_tuples = sorted(txt_dict.items(), key=last_element, reverse=True)

    for t in txt_list_tuples[:top]:
        print t[0], ' ', t[1]


def last_element(last):
    return last[-1]

def main():
    # Change filename below to select your document
    # e.g. filename = 'C:\users\mflores1\mydocument.txt
    filename = 'C:\Users\mflores1\datafiles2\data_science_practice\\mydocument.txt'
    total_words, unique_words, sentences, txt_dict = read_text(filename)
    print 'Total word count: ', total_words
    print 'Unique words: ', unique_words
    print 'Sentences: ', sentences
    print '******************************************************'
    print 'A list of words used, in order of descending frequency'
    print_top(txt_dict)

if __name__ == '__main__':
    main()