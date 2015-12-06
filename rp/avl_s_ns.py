__author__ = 'MFlores1'
import csv
import random


def matchRecord(filename_base, filename_new_data):
    """
    Combines data from two files with a field in common.
    Performs task similar to a Vlookup in Excel.

    filename_base: .csv file includes leases analysis results from Postgres sql (l1base with GC id)
    filename_new_data: .csv file includes GC data with
    Creates a .csv file with all filename_base fields plus additional field from filename_new_data
    """
    # Copy all data from filename_base to dictionary.
    dict_base = {}
    try:
        with open(filename_base, 'rb') as f_base:
            reader = csv.reader(f_base, delimiter=',')
            # Skip header row
            reader.next()
            # Copy rows in dictionary with customer id as key
            for row in reader:
                # Fill match_count with 0 if empty
                if row[12] == '':
                    match_count = 0
                else:
                    match_count = int(row[12])

                # Fill channel_disagree with 0 if empty
                if row[13] == '':
                    channel_disagree = 0
                else:
                    channel_disagree = int(row[13])

                # Fill channel_disagree with 0 if empty
                if row[14] == '':
                    channel_agree = 0
                else:
                    channel_agree = int(row[14])

                lst = [row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], int(row[11]),
                       match_count, channel_disagree, channel_agree, row[15], row[16], row[17], row[18], row[19],
                       row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29],
                       row[30], row[31], row[32], row[33], row[34]]
                dict_base[row[0]] = lst
    except Exception as err:
        print 'There is an error with filename_base: ' + str(err)

    # Copy customer id and new field to dictionary.
    dict_new = {}
    try:
        with open(filename_new_data, 'rb') as f_new:
            reader_new = csv.reader(f_new, delimiter=',')
            # Skip header row
            reader_new.next()
            # Copy only new data to dictionary.  Use customer id as key
            for row in reader_new:
                # Fill channel_disagree with 0 if empty
                if row[26] not in ('0', '1'):
                    s_ns = 0
                else:
                    s_ns = int(row[26])
                dict_new[row[2]] = s_ns
    except Exception as err:
        print 'There is an error with filename_new_data: ' + str(err)

    # Match records
    for k_match, v_match in dict_base.iteritems():
        if k_match in dict_new:
            dict_base[k_match].append(dict_new[k_match])
        else:
            dict_base[k_match].append(0)

    # Create .csv file with base data and new field
    try:
        with open('s_ns_output.csv', 'wb') as f_output:
            writer = csv.writer(f_output, delimiter=',')
            for k_out, v_out in dict_base.iteritems():
                writer.writerow([k_out, v_out[34]])
    except Exception as err:
        print 'Error writing: ' + str(err)

def readDataFromFile(filename):
    """
    Reads a .csv file with customer id data

    filename: .csv file with guest card data
    returns: dictionary with customer id as key and a list of values
    """
    # Copy data from filename_base to dictionary.
    dict_customer_id = {}
    with open(filename, 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        # Skip header row
        reader.next()
        # Copy rows in a dictionary with customer id as key
        for row in reader:
            # Fill match_count with 0 if empty
            if row[14] == '':
                match_count = 0
            else:
                match_count = int(row[14])
            lst = [int(row[1]), row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                   row[12], int(row[13]), match_count, row[15], row[16]]
            dict_customer_id[row[0]] = lst
    return dict_customer_id


def calculateConversion(dict_cust_id):
    """
    xxxxxxxxxx
    dict_cust_id: dictionary with customer id as key and a list of values
    returns: a dictionary
    """
    # Create separate lists for 0's and 1's
    lst_0 = []
    lst_1 = []
    for k, v in dict_cust_id.iteritems():
        if v[0] == 0:
            lst_0.append((k, v[12], v[13]))
        else:
            lst_1.append((k, v[12], v[13]))

    # Calculate conversion for samples of 0's and 1's.  Store results in dictionary.
    dict_results = {}
    # Run multiple comparision (e.g. 50)
    for s in range(50):
        sample_lst_0 = random.sample(lst_0, 5000)
        sample_lst_1 = random.sample(lst_1, 5000)
        # Calculate conversion for both groups
        # Group 0
        sum_gcs = 0
        sum_matches = 0
        for s_0 in sample_lst_0:
            sum_gcs += s_0[1]
            sum_matches += s_0[2]
        conv_0 = float(sum_matches) / float(sum_gcs)
        # Group 1
        sum_gcs = 0
        sum_matches = 0
        for s_1 in sample_lst_1:
            sum_gcs += s_1[1]
            sum_matches += s_1[2]
        conv_1 = float(sum_matches) / float(sum_gcs)
        dict_results[s] = (conv_0, conv_1)
    return dict_results


def main():
    filename_base = "C:/Users/mflores1/dataforpython/L1Base_April_to_August_with_GC.csv"
    filename_new_data = "C:/Users/mflores1/dataforpython/s_ns.csv"
    test = matchRecord(filename_base, filename_new_data)

    # dict_output = readDataFromFile(filename)
    # results = calculateConversion(dict_output)
    # for k, v in results.iteritems():
    #    print v[0], ',', v[1]


if __name__ == '__main__':
    main()
