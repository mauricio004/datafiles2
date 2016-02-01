__author__ = 'MFlores1'
import csv
import random

def matchRecord(filename_base, filename_new_data, dir_output):
    """
    Combines data from two files with a field in common.
    Performs task similar to an Excel vlookup.

    filename_base: .csv file with lease analysis results from Postgres sql (l1base with GC id)
    filename_new_data: .csv file with new data to add to filename_base
    dir_output: string with directory to write dictionary data
    returns a dictionary with fields from filename_base plus
    additional field from filename_new_data
    Also write to dir_output dictionary data.
    """
    # Copy all data from filename_base to dictionary.
    dict_base = {}
    try:
        with open(filename_base, 'rb') as f_base:
            reader = csv.reader(f_base, delimiter=',')
            # Skip header row
            reader.next()
            # Copy rows in dictionary with customer id as key (just email leads)
            for row in reader:
                if row[7] == 'Phone Call':
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

    # Create .csv file with some base data and new field
    try:
        with open(dir_output + 'output_s_ns.csv', 'wb') as f_output:
            writer = csv.writer(f_output, delimiter=',')
            for k_out, v_out in dict_base.iteritems():
                writer.writerow([k_out, v_out[1], v_out[3], v_out[4], v_out[6], v_out[9], v_out[10], v_out[11],
                                 v_out[34]])
    except Exception as err:
        print 'Error writing: ' + str(err)

    # returns dictionary
    return dict_base


def calculateConversion(dict_base, dir_output, run=100, sample_size=5000):
    """
    Reads a dictionary to calculate conversion rates for multiple samples.

    dict_base: dictionary with base data plus special/non-special flag (0 and 1)
    returns: a dictionary with run # as key and a tuple with conversion for 0(non_special) and 1(special).
    """

    # Create separate lists for 0's and 1's
    lst_0 = []
    lst_1 = []
    for k, v in dict_base.iteritems():
        if v[34] == 0:
            lst_0.append((k, v[10], v[11]))
        else:
            lst_1.append((k, v[10], v[11]))

    # Calculate conversion for samples of 0's and 1's.  Store results in dictionary.
    dict_results = {}
    # Run multiple comparisons (e.g. 50)
    for s in range(run):
        try:
            sample_lst_0 = random.sample(lst_0, sample_size)
            sample_lst_1 = random.sample(lst_1, sample_size)
        except Exception as err:
            print 'Error sampling: ' + str(err)
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
        if conv_0 >= conv_1:
            dict_results[s] = (conv_0, conv_1, 0)
        else:
            dict_results[s] = (conv_0, conv_1, 1)

    # Write output with all samples
    try:
        with open(dir_output + 'samples_s_ns.csv', 'wb') as f_output:
            writer = csv.writer(f_output, delimiter=',')
            for k_out, v_out in dict_results.iteritems():
                writer.writerow([k_out, v_out[0], v_out[1], v_out[2]])
    except Exception as err:
        print 'Error writing: ' + str(err)


def main():
    filename_base = "C:/Users/mflores1/dropbox/Mauricio/L1Base_June_to_August_with_GC.csv"
    filename_new_data = "C:/Users/mflores1/dropbox/Mauricio/s_ns.csv"
    dir_for_output = "C:/Users/mflores1/dropbox/Mauricio/"

    dict_base = matchRecord(filename_base, filename_new_data, dir_for_output)

    calculateConversion(dict_base, dir_for_output)

if __name__ == '__main__':
    main()
