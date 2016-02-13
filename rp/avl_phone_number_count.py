__author__ = 'MFlores1'

import re
import csv
from avl_keywords_extract import read_data_from_file
from avl_keywords_extract import read_text_for_rent
from avl_keywords_extract import read_text_hot_pads
from avl_keywords_extract import read_text_apartment_guide
from avl_keywords_extract import read_text_apartment_list
from avl_keywords_extract import read_text_new_property_website


def find_phone_in_comment(customer_dict):
    """
    This function finds phone numbers in email's lead comments.
    :param customer_dict: a dictionary with customer id as key and a tuple as value.  Tuple includes date
    (if no date available use '01/01/2100' as default) and text in comment.
    :return: a dictionary with customer id as key and a tuple as value.  Tuple includes date, a boolean (True if
    any phone in comments, False otherwise) and the phone number if found (otherwise use 'doesNotFindAPhoneNumber'
    as default text
    """

    customer_phone_dict = {}
    # Loop over all customer ids
    for (key, value) in customer_dict.items():
        # Select date and text for each customer id
        (date, text) = value
        # Search for phone in text
        phone_match = re.search(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d'
                                r'{4})', text, re.DOTALL)
        match = False
        if phone_match:
            customer_id_phone = phone_match.group(1).strip()
            match = True
        else:
            customer_id_phone = 'doesNotFindAPhoneNumber'

        customer_phone_dict[key] = (date, match, customer_id_phone)
    return customer_phone_dict


def write_phone_results_to_file(customer_phone_dict, filename_results):
    """
    :param customer_phone_dict:
    :param filename_results:
    :return:
    """
    # Write .csv file to disk
    try:
        with open(filename_results, 'wb') as f_output:
            writer = csv.writer(f_output, delimiter=',')
            for k, v in customer_phone_dict.iteritems():
                date, match_phone, phone_number = v
                writer.writerow(['ApartmentGuide.com', k, match_phone, phone_number])
    except Exception as err:
        print 'Error writing: ' + str(err)


if __name__ == '__main__':
    # Need to change both lines to specify ILS
    filename_txt = "C:/Users/mflores1/dropbox/Mauricio/avln/apt_list_4_month.csv"
    customer_dict = read_text_apartment_list(read_data_from_file(filename_txt))
    # Writes data to disk
    filename_phone_results = "C:/Users/mflores1/dropbox/Mauricio/avln/phone_results_apt_list.csv"
    write_phone_results_to_file(find_phone_in_comment(customer_dict), filename_phone_results)



