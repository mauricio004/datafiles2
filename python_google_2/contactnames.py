#!/usr/bin/python
import sys
import re

def extract_contacts(filename):
    """
    Extracts contact data, lease begin date, lease end date, and move in date.
    """
    # This list returns the final data
    names = []

    # open file
    f = open(filename, 'rU')
    text = f.read()

    # extract site name
    match_site = re.search(r'Property:\s*(\w+)', text)
    if not match_site:
        sys.stderr.write('No site match')
        sys.exit(1)
    site = match_site.group(1)
    names.append(site)

    # extract names
    # name_match = re.findall(r'p\w+,,"(\w+,\s\w+)"[\.\w*\s*,()-]+(\d+/\d+/\d+)[,]+(\d+/\d+/\d+)[,]+(\d+/\d+/\d+)', text)
    tuples = re.findall(r't\d+[,]+([*]*\w+\s*\w+)[\.\w*\s*",()-]+(\d+/\d+/\d+)[,]+(\d+/\d+/\d+)[,]+(\d+/\d+/\d+)', text)
    if not tuples:
        sys.stderr.write("No names matches")
        sys.exit(1)
    # store data in a dictionary of names
    names_dict = {}
    for name, lease_begin, lease_end, move_in in tuples:
        if name not in names_dict:
            names_dict[name] = [lease_begin, lease_end, move_in]
    for k in sorted(names_dict.keys()):
        names.append(k + ',' + names_dict[k][0] + ',' + names_dict[k][1] + ',' + names_dict[k][2])
    return names


def main():
    # extract_contacts('c:/users/mflores1/pycharmprojects/practicepython/ApexMoveInReport.csv')

    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    import glob
    for arg in args:
        for filename in glob.glob(arg):
            filedata = extract_contacts(filename)
            text = '\n'.join(filedata) + '\n'

        if summary:
            outf = open(filename + '.summary', 'w')
            outf.write(text + '\n')
            outf.close()
        else:
            print(text)



if __name__ == '__main__':
    main()

