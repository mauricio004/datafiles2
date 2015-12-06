# -*- coding: utf-8 -*-
import csv
import re
import unicodedata
from bs4 import BeautifulSoup


def convertToText(filename):
    """Returns an string

    filename: Delimited file with text and html.  Convert html to readable format.  Convert unicode to string
    """
    with open(filename, "r") as f:
        raw = BeautifulSoup(f).get_text()
    # raw_text = unicodedata.normalize('NFKD', raw).encode('ascii', 'ignore')
    return raw


def readData(rawtxt):
        """Returns a dictionary

        rawtxt: Includes Customer id's and email text.  Separate text by customer id.  Store data in dictionary.  Use
        customer id as key and comments text as value.  Split comments text by words
        ---Works for ForRent.com---
        """
        customer_id_dict = {}
        # Separate data by customer id.  Store in tuples
        tuples = re.findall(r'CustomerID:(\d+).*?(Comments:.*?)(?=CustomerID:)', rawtxt, re.DOTALL)
        # Read data just in comments fields.  Split comments text into words.  Copy to a dictionary with
        # Customer id as key and split comments text as value
        for text_tuple in tuples:
            (customer_id, text) = text_tuple
            if customer_id not in customer_id_dict:
                text_match = re.findall(r'Comments:(.*?)ForRent.com', text, re.DOTALL)
                if len(text_match) >= 1:
                    text_match_list = text_match[0].split()
                else:
                    text_match_list = []
                customer_id_dict[customer_id] = text_match_list
        return customer_id_dict


def countWords(customer_dict):
    word_dict = {}
    for k_dict, v_dict in customer_dict.iteritems():
        for v in v_dict:
            v = v.lower()
            v = v.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
            if v not in word_dict:
                word_dict[v] = 1
            else:
                word_dict[v] += 1
    return word_dict


if __name__ == '__main__':
    filename = "C:/Users/mflores1/dataforpython/for_rent_all.csv"
    try:
        t = convertToText(filename)
    except IOError:
        print 'Cannot open file'

    word_dictionary = countWords(readData(t))
    for k in sorted(word_dictionary.keys()):
        print k, '%', word_dictionary[k]



