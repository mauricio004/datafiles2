__author__ = 'MFlores1'
import re
import os
import csv


def read_data_from_file(filename):
    """
    This function separates data from IT in individual email leads.  It helps to count the total
    customer id's in IT data.
    :param filename: a .csv file with all email leads
    :return: a list with customer id's
    """
    customer_id_lst = []
    try:
        with open(filename, "r") as f:
            # Separate data by customer id.  Store in tuples -> (CustomerID, ils id, ils, plaintext/html text)
            tuples = re.findall(r'CustomerID:(\d+),(\d+),(.*?),(.*?)(?=CustomerID:)', f.read(), re.DOTALL)
            # Copy to a dictionary with Customer id as key
            for text_tuple in tuples:
                (customer_id, ils_id, ils, text) = text_tuple
                customer_id_lst.append(customer_id)
    except Exception as error:
        print 'Error reading file ' + str(error)
    return customer_id_lst


if __name__ == '__main__':
    filename = "C:/Users/mflores1/dropbox/Mauricio/avln/property_website_1_month.csv"
    cust_id_lst = read_data_from_file(filename)

    # Write to this directory
    os.chdir('C:/Users/mflores1/dropbox/Mauricio/avln')

    # Creates a .csv file and write to directory --- just id's
    try:
        with open('email_results_just_ids.csv', 'w') as to_write:
            writer = csv.writer(to_write, delimiter=',')
            for a in cust_id_lst:
                writer.writerow([a])
    except Exception as err:
        print 'Error writing file ' + str(err)