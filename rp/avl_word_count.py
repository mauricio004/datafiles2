# -*- coding: utf-8 -*-
import re
import os
import csv
import unicodedata

from bs4 import BeautifulSoup, NavigableString, Tag


def readDataFromFile(filename):
    """
    xxx
    """
    customer_id_dict = {}
    try:
        with open(filename, "r") as f:
            # Separate data by customer id.  Store in tuples -> (CustomerID, ils id, ils, plaintext/html text)
            tuples = re.findall(r'CustomerID:(\d+),(\d+),(.*?),(.*?)(?=CustomerID:)', f.read(), re.DOTALL)
            # Copy to a dictionary with Customer id as key
            for text_tuple in tuples:
                (customer_id, ils_id, ils, text) = text_tuple
                if customer_id not in customer_id_dict:
                    customer_id_tuple = (ils, text)
                    customer_id_dict[customer_id] = customer_id_tuple
    except Exception as err:
        print 'Error reading file ' + str(err)
    return customer_id_dict


def readText(customer_id_dict):
    """
    """
    customer_id_results_dict = {}

    for k, v in customer_id_dict.iteritems():
        if v[0] == 'ForRent.com':
            if k not in customer_id_results_dict:
                # Search for comments text
                comments_match = re.search(r'Comments:(.*?)ForRent.com', v[1], re.DOTALL)
                # If find match, add key and text to dictionary
                if comments_match:
                    customer_id_results_dict[k] = comments_match.group(1).strip()
                # If not match, add key and 'CannotGetData'
                else:
                    customer_id_results_dict[k] = 'CannotGetData'
        elif v[0] == 'Hotpads / Zillow':
            soup = BeautifulSoup(v[1], 'html5lib')
            for br in soup.findAll('br'):
                next = br.nextSibling
                if not (next and isinstance(next, NavigableString)):
                    continue
                next2 = next.nextSibling
                if next2 and isinstance(next2, Tag) and next2.name == 'br':
                    next = next.encode('ascii', 'ignore')
                    text = str(next).strip()
                    if text:
                        print "Found:" + k, next
        elif v[0] == 'ApartmentGuide.com':
            if k not in customer_id_results_dict:
                # Search for comments text
                comments_match = re.search(r'Comments:(.*?)-----', v[1], re.DOTALL)
                # If find match, add key and text to dictionary
                if comments_match:
                    customer_id_results_dict[k] = comments_match.group(1).strip()
                # If not match, add key and 'CannotGetData'
                else:
                    customer_id_results_dict[k] = 'CannotGetData'
        elif v[0] == 'New Property Website':
            soup = BeautifulSoup(v[1], 'html5lib')
            # Convert Unicode string to a a string
            email_text = unicodedata.normalize('NFKD', soup.get_text()).encode('ascii', 'ignore')
            comments_match = re.search(r'Comments:(.*)', email_text, re.DOTALL)
            if k not in customer_id_results_dict:
                # Search for comments text
                comments_match = re.search(r'Comments:(.*) ', email_text, re.DOTALL)
                # If find match, add key and text to dictionary
                if comments_match:
                    customer_id_results_dict[k] = comments_match.group(1).strip()
                # If not match, add key and 'CannotGetData'
                else:
                    customer_id_results_dict[k] = 'CannotGetData'
        else:
            print 'unknown ils'
    return customer_id_results_dict

def convertToText(filename):
    """Returns an string

    filename: Delimited file with text and html.  Convert html to readable format.  Convert unicode to string
    """
    with open(filename, "r") as f:
        #raw = BeautifulSoup(f).get_text()
        soup = BeautifulSoup(f)
        # raw_text = unicodedata.normalize('NFKD', raw).encode('ascii', 'ignore')
    return soup


def readData(rawtxt):
        """Returns a dictionary

        rawtxt: Includes Customer id's and email text.  Separate text by customer id.  Store data in dictionary.  Use
        customer id as key and comments text as value.  Split comments text by words
        ---Works for ForRent.com---
        """
        customer_id_dict = {}
        # Separate data by customer id.  Store in tuples
        tuples = re.findall(r'CustomerID:(\d+),(\d+),(.*?(Comments:.*?)(?=CustomerID:)', rawtxt, re.DOTALL)
        # Read data just in comments fields.  Split comments text into words.  Copy to a dictionary with
        # Customer id as key and split comments text as value
        for text_tuple in tuples:
            (customer_id, text) = text_tuple
            if customer_id not in customer_id_dict:
                print 's'
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
    filename = "C:/Users/mflores1/dropbox/Mauricio/property_website_sample.txt"
    cust_id_dict = readDataFromFile(filename)
    results_dict = readText(cust_id_dict)

    # Write to file
    os.chdir('C:/Users/mflores1/dropbox/Mauricio/')

    with open('email_results.csv', 'w') as to_write:
        writer = csv.writer(to_write, delimiter=',')
        for a in results_dict.keys():
            writer.writerow([a, results_dict[a]])

    # for k, v in cust_id_dict.iteritems():
    #     print k, ', ', v[0]

    # try:
    #     t = convertToText(filename)
    # except IOError:
    #     print 'Cannot open file'
    #
    # word_dictionary = countWords(readData(t))
    # for k in sorted(word_dictionary.keys()):
    #     print k, '%', word_dictionary[k]



