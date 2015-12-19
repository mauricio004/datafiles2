# -*- coding: utf-8 -*-
import re
import os
import csv
import time
from bs4 import BeautifulSoup, NavigableString, Tag


def readDataFromFile(filename):
    """
    xxx
    """
    try:
        with open(filename, "r") as f:
            # Separate data by customer id.  Store in tuples -> (CustomerID, ils id, ils, plaintext/html text)
            tuples = re.findall(r'CustomerID:(\d+),(\d+),(.*?),(.*?)(?=CustomerID:)', f.read(), re.DOTALL)
    except Exception as err:
        print 'Error reading file ' + str(err)
    return tuples


def readText(tuples):
    customer_id_dict = {}

    for text_tuple in tuples:
        (customer_id, ils_id, ils, text) = text_tuple
        if ils == 'ForRent.com':
            # Search for comments' text
            comments_match = re.search(r'Comments:(.*?)ForRent.com', text, re.DOTALL)
            date_match = re.search(r'Date/Time:(.*?)To:', text, re.DOTALL)
            if date_match:
                customer_id_date_str = date_match.group(1).strip()
                try:
                    customer_id_date = time.strptime(customer_id_date_str, '%m/%d/%Y %I:%M:%S %p')
                except ValueError:
                    customer_id_date = time.strptime('01/01/2100', '%m/%d/%Y')
            else:
                customer_id_date = customer_id_date = time.strptime('01/01/2100', '%m/%d/%Y')

            if comments_match:
                customer_id_comments = comments_match.group(1).strip()
            else:
                customer_id_comments = 'cannotFindCommentsText'

            if customer_id not in customer_id_dict:
                customer_id_dict[customer_id] = (customer_id_date, customer_id_comments)
            else:
                date_in_dict = customer_id_dict[customer_id][0]
                if not comments_match:
                    continue
                elif customer_id_date < date_in_dict:
                        customer_id_dict.pop(customer_id, None)
                        customer_id_dict[customer_id] = (customer_id_date, customer_id_comments)
    return customer_id_dict




if __name__ == '__main__':
    filename = "C:/Users/mflores1/dropbox/Mauricio/for_rent_4_month.csv"
    customer_id_dict = readText(readDataFromFile(filename))

    # Write to file
    os.chdir('C:/Users/mflores1/dropbox/Mauricio/')

    try:
        with open('email_results.csv', 'w') as to_write:
            writer = csv.writer(to_write, delimiter=',')
            for a in customer_id_dict.keys():
                data_str = time.strftime('%m/%d/%Y %I:%M:%S %p', customer_id_dict[a][0])
                writer.writerow([a, data_str, customer_id_dict[a][1]])
    except Exception as err:
        print 'Error writing file ' + str(err)
