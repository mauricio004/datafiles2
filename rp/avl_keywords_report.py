__author__ = 'MFlores1'

import csv
import numpy
from avl_word_count import read_keywords


def read_keywords_result(filename_base):
    dict_keywords_res = {}
    try:
        with open(filename_base, 'rb') as f_base:
            reader = csv.DictReader(f_base, delimiter=',')
            # Copy rows in dictionary with customer id as key
            for row in reader:
                dict_keywords_res[row['Customer_id']] = row
    except Exception as err:
        print 'There is an error with filename_base: ' + str(err)
    return dict_keywords_res


def calculate_visit_ratios(dict_keywords_result, dict_keywords, ils='Property Website'):
    # Update keyword dictionary
    for keyword_word, value in dict_keywords.iteritems():
        dict_keywords[keyword_word] = {'1': {'visits_set': 0, 'total_guest_cards': 0, 'visit_set_ratio': 0},
                                       '0': {'visits_set': 0, 'total_guest_cards': 0, 'visit_set_ratio': 0}}
    # Loop over results.
    for gc_id, dict_data_row in dict_keywords_result.iteritems():
        # Loop over keyword dictionary
        for word, value in dict_keywords.iteritems():
            # '1'
            if dict_data_row['ILS'] == ils and dict_data_row[word] == '1':
                dict_keywords[word]['1']['total_guest_cards'] += 1
            if dict_data_row['ILS'] == ils and dict_data_row[word] == '1' and dict_data_row['lead_status'] == \
                    'Visit Set':
                dict_keywords[word]['1']['visits_set'] += 1
            # '0'
            if dict_data_row['ILS'] == ils and dict_data_row[word] == '0':
                dict_keywords[word]['0']['total_guest_cards'] += 1
            if dict_data_row['ILS'] == ils and dict_data_row[word] == '0' and dict_data_row['lead_status'] == \
                    'Visit Set':
                dict_keywords[word]['0']['visits_set'] += 1

    # Find visit set ratios

    for w, v in dict_keywords.iteritems():
        # '1'
        dict_keywords[w]['1']['visit_set_ratio'] = (numpy.float64(dict_keywords[w]['1']['visits_set']) /
                                                    numpy.float64(dict_keywords[w]['1']['total_guest_cards']))
        # '0'
        dict_keywords[w]['0']['visit_set_ratio'] = (numpy.float64(dict_keywords[w]['0']['visits_set']) /
                                                    numpy.float64(dict_keywords[w]['0']['total_guest_cards']))
    return dict_keywords


def calculate_conversion(dict_keywords_result, dict_keywords, ils='Property Website'):
    # Update keyword dictionary
    for keyword_word, value in dict_keywords.iteritems():
        dict_keywords[keyword_word] = {'1': {'leases': 0, 'total_guest_cards': 0, 'conversion': 0},
                                       '0': {'leases': 0, 'total_guest_cards': 0, 'conversion': 0}}
    # Loop over results.
    for gc_id, dict_data_row in dict_keywords_result.iteritems():
        # Loop over keyword dictionary
        for word, value in dict_keywords.iteritems():
            # '1'
            if dict_data_row['ILS'] == ils and dict_data_row[word] == '1':
                dict_keywords[word]['1']['total_guest_cards'] += 1
            if dict_data_row['ILS'] == ils and dict_data_row[word] == '1':
                dict_keywords[word]['1']['leases'] += int(dict_data_row['leases'])
            # '0'
            if dict_data_row['ILS'] == ils and dict_data_row[word] == '0':
                dict_keywords[word]['0']['total_guest_cards'] += 1
            if dict_data_row['ILS'] == ils and dict_data_row[word] == '0':
                dict_keywords[word]['0']['leases'] += int(dict_data_row['leases'])

    # Find visit set ratios

    for w, v in dict_keywords.iteritems():
        # '1'
        dict_keywords[w]['1']['conversion'] = (numpy.float64(dict_keywords[w]['1']['leases']) /
                                                    numpy.float64(dict_keywords[w]['1']['total_guest_cards']))
        # '0'
        dict_keywords[w]['0']['conversion'] = (numpy.float64(dict_keywords[w]['0']['leases']) /
                                                    numpy.float64(dict_keywords[w]['0']['total_guest_cards']))
    return dict_keywords

filename_keywords_result = "C:/Users/mflores1/dropbox/Mauricio/avln/keywords_result_all_without_nulls.csv"
dict_key_res = read_keywords_result(filename_keywords_result)
filename_keywords = "C:/Users/mflores1/dropbox/Mauricio/avln/keywords.txt"
dict_keys = read_keywords(filename_keywords)
# Visits set ratio
results = calculate_visit_ratios(dict_key_res, dict_keys)
filename_keywords_visits_set = "C:/Users/mflores1/dropbox/Mauricio/avln/keywords_visits_set.csv"

with open(filename_keywords_visits_set, 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for k, v in results.iteritems():
        writer.writerow([k, v['1']['visits_set'], v['1']['total_guest_cards'], v['1']['visit_set_ratio'],
                         v['0']['visits_set'], v['0']['total_guest_cards'], v['0']['visit_set_ratio']])

# Conversion
results = calculate_conversion(dict_key_res, dict_keys)
filename_keywords_conversion = "C:/Users/mflores1/dropbox/Mauricio/avln/keywords_conversion.csv"

with open(filename_keywords_conversion, 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for k, v in results.iteritems():
        writer.writerow([k, v['1']['leases'], v['1']['total_guest_cards'], v['1']['conversion'],
                         v['0']['leases'], v['0']['total_guest_cards'], v['0']['conversion']])
