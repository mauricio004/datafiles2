__author__ = 'MFlores1'

import re
import copy
import csv
import operator
from avl_keywords_extract import read_data_from_file
from avl_keywords_extract import read_text_for_rent
from avl_keywords_extract import read_text_hot_pads
from avl_keywords_extract import read_text_apartment_guide
from avl_keywords_extract import read_text_apartment_list
from avl_keywords_extract import read_text_new_property_website


def split_text_in_words(customer_dict, key_dict):
    """
    This function clean, split and count the words in email's leads comments.  It also compares the words in the
    email with the keywords. This functions use the helper function 'get words' to split the words.
    :param customer_dict: a dictionary with customer id as key and a tuple as value.  Tuple includes date
    (if no date available use '01/01/2100' as default) and text in comment.
    :param key_dict: a dictionary with 'keyword' as key and zero as value
    :return: a dictionary with customer id as key and a tuple as value.  Tuple includes date, a boolean (True if any of
    the keywords has match, False otherwise), a dictionary (with each word in comment as key and the number of
    instances of this word as value) and another dictionary (key_dict above with keyword as key and 1 if keyword in
    email lead)
    """

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
    return customer_wc_dict


def get_words(txt):
    """
    This function split text into single words. It also converts all
    words to lower case.
    :param txt: a string with the email lead's comment text
    :return: a list with all the words in the comment text
    """

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']


def read_keywords(filename):
    """
    This function reads the list of keywords from disk.
    :param filename: the location of a .csv file in disk with a list of keywords.
    :return: a dictionary with 'keyword' as key and zero as value.
    """

    # Read keywords from list in disk
    keywords_dict = {}
    try:
        with open(filename, 'r') as f:
            for k in f:
                keywords_dict.setdefault(k.strip(), 0)
    except Exception as err:
        print 'Error reading file ' + str(err)
    return keywords_dict


def write_results_to_file(customer_dict, filename_results):
    """
    This function writes the results to disk.
    :param customer_dict: a dictionary with customer id as key and a tuple as value.  Tuple includes date, a boolean
    (True if any of the keywords has match, False otherwise), a dictionary (with each word in comment as key and the
    number of instances of this word as value) and another dictionary (with keyword as key and '1' if keyword in
    email lead)
    :param filename_results: the location of a .csv file in disk to write results
    """

    # Write .csv file to disk
    try:
        with open(filename_results, 'wb') as f_output:
            writer = csv.writer(f_output, delimiter=',')
            for k, v in customer_dict.iteritems():
                date, match_boolean, comments_count, keywords_count = v
                # sort keywords by name (key in dictionary)
                sorted_x = sorted(keywords_count.items(), key=operator.itemgetter(0))
                writer.writerow(['ForRent.com', k, sorted_x[0][1], sorted_x[1][1], sorted_x[2][1], sorted_x[3][1],
                                sorted_x[4][1],
                                sorted_x[5][1], sorted_x[6][1], sorted_x[7][1], sorted_x[8][1], sorted_x[9][1],
                                sorted_x[10][1], sorted_x[11][1], sorted_x[12][1], sorted_x[13][1], sorted_x[14][1],
                                sorted_x[15][1], sorted_x[16][1], sorted_x[17][1], sorted_x[18][1], sorted_x[19][1],
                                sorted_x[20][1], sorted_x[21][1], sorted_x[22][1], sorted_x[23][1], sorted_x[24][1],
                                sorted_x[25][1], sorted_x[26][1], sorted_x[27][1], sorted_x[28][1], sorted_x[29][1],
                                sorted_x[30][1], sorted_x[31][1]])
    except Exception as err:
        print 'Error writing: ' + str(err)

# Need to change both lines to select ILS
filename_txt = "C:/Users/mflores1/dropbox/Mauricio/avln/for_rent_4_month.csv"
customer_dict = read_text_for_rent(read_data_from_file(filename_txt))

filename_keywords = "C:/Users/mflores1/dropbox/Mauricio/avln/keywords.txt"
keyword_dict = read_keywords(filename_keywords)
# split_text_in_words(customer_dict, keyword_dict)
filename_result = "C:/Users/mflores1/dropbox/Mauricio/avln/keywords_result.csv"
write_results_to_file(split_text_in_words(customer_dict, keyword_dict), filename_result)
