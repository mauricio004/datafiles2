__author__ = 'MFlores1'

import re
import copy
from avl_word_extract_2 import read_data_from_file
from avl_word_extract_2 import read_text_for_rent


def split_text_in_words(customer_dict, key_dict):
    customer_wc_dict = {}
    # Loop over all customer ids
    for (key, value) in customer_dict.items():
        wc = {}
        # Create a deep copy of keyword_dict
        keyword_dict = copy.deepcopy(key_dict)
        # Select date and text for each customer id
        (date, text) = value
        # Extract a list of words
        words = get_words(text)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1
        # Compare word count with keywords
        match = False
        for k, v in keyword_dict.items():
            if k in wc:
                keyword_dict[k] += 1
                match = True
        customer_wc_dict[key] = (date, match, wc, keyword_dict)



def get_words(txt):
    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


def read_keywords(filename):
    keywords_dict = {}
    try:
        with open(filename, 'r') as f:
            for k in f:
                keywords_dict.setdefault(k.strip(), 0)
    except Exception as err:
        print 'Error reading file ' + str(err)
    return keywords_dict

filename_txt = "C:/Users/mflores1/dropbox/Mauricio/avln/for_rent_4_month.csv"
customer_dict = read_text_for_rent(read_data_from_file(filename_txt))
filename_keywords = "C:/Users/mflores1/dropbox/Mauricio/avln/keywords.txt"
keyword_dict = read_keywords(filename_keywords)
split_text_in_words(customer_dict, keyword_dict)
