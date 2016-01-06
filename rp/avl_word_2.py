# -*- coding: utf-8 -*-
import re
import os
import csv
import time
from bs4 import BeautifulSoup, NavigableString, Tag


def read_data_from_file(filename):
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


# ------------------------ ForRent.com ---------------------------------------------------------------
def read_text_for_rent(tuples):

    customer_id_dict = {}
    for text_tuple in tuples:
        (customer_id, ils_id, ils, text) = text_tuple
        if ils == 'ForRent.com':
            # Search for comments' text
            comments_match = re.search(r'Comments:(.*?)ForRent.com', text, re.DOTALL)
            # Search for date
            date_match = re.search(r'Date/Time:(.*?)To:', text, re.DOTALL)
            # Add date
            if date_match:
                # Read data for date text
                customer_id_date_str = date_match.group(1).strip()
                try:
                    customer_id_date = time.strptime(customer_id_date_str, '%m/%d/%Y %I:%M:%S %p')
                # Add default date '01/01/2100'
                except ValueError:
                    customer_id_date = time.strptime('01/01/2100', '%m/%d/%Y')
            # Add default date '01/01/2100'
            else:
                customer_id_date = time.strptime('01/01/2100', '%m/%d/%Y')
            # Add comment's text
            if comments_match:
                customer_id_comments = comments_match.group(1).strip()
            # Add 'cannotFindCommentsText'
            else:
                customer_id_comments = 'cannotFindCommentsText'
            # Add customer id
            if customer_id not in customer_id_dict:
                customer_id_dict[customer_id] = (customer_id_date, customer_id_comments)
            # Customer id already in dictionary
            else:
                # Find customer id's date
                date_in_dict = customer_id_dict[customer_id][0]
                # Move to next customer id
                if not comments_match:
                    continue
                # Replace customer id
                elif customer_id_date < date_in_dict:
                        customer_id_dict.pop(customer_id, None)
                        customer_id_dict[customer_id] = (customer_id_date, customer_id_comments)
        else:
            print 'Not a ForRent.com email'
            continue
    return customer_id_dict


# ------------------------ HotPads.com ---------------------------------------------------------------
def read_text_hot_pads(tuples):

    customer_id_dict = {}
    for text_tuple in tuples:
        (customer_id, ils_id, ils, text) = text_tuple
        if ils == 'Hotpads / Zillow':
            soup = BeautifulSoup(text, 'html5lib')
            for br in soup.findAll('br'):
                next = br.nextSibling
                if not (next and isinstance(next, NavigableString)):
                    continue
                next2 = next.nextSibling
                if next2 and isinstance(next2, Tag) and next2.name == 'br':
                    next = next.encode('ascii', 'ignore')
                    comments_text = str(next).strip()
                    # Add customer id
                    if customer_id not in customer_id_dict:
                        customer_id_date = time.strptime('01/01/2100', '%m/%d/%Y')
                        customer_id_dict[customer_id] = (customer_id_date, comments_text)
                    # Customer id already in dictionary
                    else:
                        # Move to next customer id
                        if not comments_text:
                            continue
                        # Replace customer id
                        else:
                            customer_id_date = time.strptime('01/01/2100', '%m/%d/%Y')
                            customer_id_dict.pop(customer_id, None)
                            customer_id_dict[customer_id] = (customer_id_date, comments_text)
        else:
            print 'Not a HotPads.com email'
            continue
    return customer_id_dict


# ------------------------ ApartmentGuide.com ---------------------------------------------------------------
def read_text_apartment_guide(tuples):

    customer_id_dict = {}
    for text_tuple in tuples:
        (customer_id, ils_id, ils, text) = text_tuple
        if ils == 'ApartmentGuide.com':
            # Search for comments' text
            comments_match = re.search(r'Comments:(.*?)-----', text, re.DOTALL)
            # Search for date
            date_match = re.search(r'Lead Date:(.*?)Property Name:', text, re.DOTALL)
            # Add date
            if date_match:
                # Read data for date text
                customer_id_date_str = date_match.group(1).strip()
                try:
                    customer_id_date = time.strptime(customer_id_date_str, '%m-%d-%Y')
                # Add default date '01/01/2100'
                except ValueError:
                    customer_id_date = time.strptime('01/01/2100', '%m/%d/%Y')
            # Add default date '01/01/2100'
            else:
                customer_id_date = time.strptime('01/01/2100', '%m/%d/%Y')
            # Add comment's text
            if comments_match:
                customer_id_comments = comments_match.group(1).strip()
            # Add 'cannotFindCommentsText'
            else:
                customer_id_comments = 'cannotFindCommentsText'
            # Add customer id
            if customer_id not in customer_id_dict:
                customer_id_dict[customer_id] = (customer_id_date, customer_id_comments)
            # Customer id already in dictionary
            else:
                # Find customer id's date
                date_in_dict = customer_id_dict[customer_id][0]
                # Move to next customer id
                if not comments_match:
                    continue
                # Replace customer id
                elif customer_id_date < date_in_dict:
                        customer_id_dict.pop(customer_id, None)
                        customer_id_dict[customer_id] = (customer_id_date, customer_id_comments)
        else:
            print 'Not an ApartmentGuide.com email'
            continue
    return customer_id_dict


# ------------------------ ApartmentList.com ---------------------------------------------------------------
def read_text_apartment_list(tuples):

    customer_id_dict = {}
    for text_tuple in tuples:
        (customer_id, ils_id, ils, text) = text_tuple
        if ils == 'ApartmentList.com':
            # Search for comments' text
            comments_match = re.search(r'Notes:(.*?)=====', text, re.DOTALL)
            # Create a default date
            customer_id_date = time.strptime('01/01/2100', '%m/%d/%Y')
            # Add comment's text
            if comments_match:
                customer_id_comments = comments_match.group(1).strip()
            # Add 'cannotFindCommentsText'
            else:
                customer_id_comments = 'cannotFindCommentsText'
            # Add customer id
            if customer_id not in customer_id_dict:
                customer_id_dict[customer_id] = (customer_id_date, customer_id_comments)
            # Customer id already in dictionary
            else:
                # Move to next customer id if not comment's match
                if not comments_match:
                    continue
                # Replace customer id
                else:
                    customer_id_dict.pop(customer_id, None)
                    customer_id_dict[customer_id] = (customer_id_date, customer_id_comments)
        else:
            print 'Not an ApartmentList.com email'
            continue
    return customer_id_dict


# ------------------------ New Property Website ---------------------------------------------------------------
def read_text_new_property_website(tuples):

    customer_id_dict = {}
    for text_tuple in tuples:
        (customer_id, ils_id, ils, text) = text_tuple
        if ils == 'New Property Website':
            soup = BeautifulSoup(text, 'html5lib')
            text_u = soup.get_text()
            text = text_u.encode('ascii', 'ignore')
            # Search for comments' text
            comments_match = re.search(r'Comments:(.*)', text, re.DOTALL)
            # Search for date
            date_match = re.search(r'Date Submitted:(.*?)Prospect Name:', text, re.DOTALL)
            # Add date
            if date_match:
                # Read data from date text e.g. Date Submitted: 11/23/2015
                customer_id_date_str = date_match.group(1).strip()
                try:
                    customer_id_date = time.strptime(customer_id_date_str, '%m/%d/%Y')
                # Add default date '01/01/2100'
                except ValueError:
                    customer_id_date = time.strptime('01/01/2100', '%m/%d/%Y')
            # Add default date '01/01/2100'
            else:
                customer_id_date = time.strptime('01/01/2100', '%m/%d/%Y')
            # Add comment's text
            if comments_match:
                customer_id_comments = comments_match.group(1).strip()
            # Add 'cannotFindCommentsText'
            else:
                customer_id_comments = 'cannotFindCommentsText'
            # Add customer id
            if customer_id not in customer_id_dict:
                customer_id_dict[customer_id] = (customer_id_date, customer_id_comments)
            # Customer id already in dictionary
            else:
                # Find customer id's date
                date_in_dict = customer_id_dict[customer_id][0]
                # Move to next customer id
                if not comments_match:
                    continue
                # Replace customer id
                elif customer_id_date < date_in_dict:
                        customer_id_dict.pop(customer_id, None)
                        customer_id_dict[customer_id] = (customer_id_date, customer_id_comments)
        else:
            print 'Not a New Property Website email'
            continue
    return customer_id_dict


if __name__ == '__main__':
    # Change filename to read ILS data
    # ForRent.com
    # filename = "C:/Users/mflores1/dropbox/Mauricio/avln/for_rent_4_month.csv"
    # customer_id_dict_result = read_text_for_rent(read_data_from_file(filename))
    # HotPads
    # filename = "C:/Users/mflores1/dropbox/Mauricio/avln/hot_pads_4_month.csv"
    # customer_id_dict_result = read_text_hot_pads(read_data_from_file(filename))
    # ApartmentGuide.com
    # filename = "C:/Users/mflores1/dropbox/Mauricio/avln/apt_guide_4_month.csv"
    # customer_id_dict_result = read_text_apartment_guide(read_data_from_file(filename))
    # ApartmentList.com
    # filename = "C:/Users/mflores1/dropbox/Mauricio/avln/apt_list_4_month.csv"
    # customer_id_dict_result = read_text_apartment_list(read_data_from_file(filename))
    # Property Website
    filename = "C:/Users/mflores1/dropbox/Mauricio/avln/property_website_4_month.csv"
    customer_id_dict_result = read_text_new_property_website(read_data_from_file(filename))

    # Write to file
    os.chdir('C:/Users/mflores1/dropbox/Mauricio/avln')
    try:
        with open('email_results.csv', 'w') as to_write:
            writer = csv.writer(to_write, delimiter=',')
            for a in customer_id_dict_result.keys():
                data_str = time.strftime('%m/%d/%Y %I:%M:%S %p', customer_id_dict_result[a][0])
                writer.writerow([a, data_str, customer_id_dict_result[a][1]])
    except Exception as err:
        print 'Error writing file ' + str(err)
