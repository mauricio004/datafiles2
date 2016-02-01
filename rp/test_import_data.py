__author__ = 'MFlores1'

import csv

filename = "C:/Users/mflores1/dropbox/Mauricio/avln/keywords_result_all_without_nulls.csv"
try:
    with open(filename, 'rb') as f:
        reader = csv.DictReader(f, delimiter=',')
        # Skip header row
        # reader.next()
        # Copy rows in dictionary with customer id as key
        for row in reader:
            ils = row['ILS']
            customer_id = row['Customer_id']
except Exception as err:
    print 'There is an error with filename: ' + str(err)



