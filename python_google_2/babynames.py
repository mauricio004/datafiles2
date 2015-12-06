#!/usr/bin/python


import sys
import re
import glob
import os

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # This list returns the final list of names with ranks.
    names = []
    # Open and read file
    f = open(filename, 'rU')
    text = f.read()

    # Get the year
    match_year = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
    if not match_year:
        sys.stderr.write('Could not find year')
        sys.exit(1)
    year = match_year.group(1)
    names.append(year)

    # Extract all the data tuples with a findall()
    #  each tuple is: (rank, boy-name, girl-name)
    tuples = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

    # Store data in a dictionary.  Use name as a key.
    names_dict = {}
    for rank, boyname, girlname in tuples:
        if boyname not in names_dict:
            names_dict[boyname] = rank
        if girlname not in names_dict:
            names_dict[girlname] = rank

    for k in sorted(names_dict.keys()):
        names.append(k + ' ' + names_dict[k])
    return names


def print_list(summary_list):
    print('\n'.join(summary_list))


def write_summaries():
    os.chdir('c:/users/mflores1/pycharmprojects/practicepython/')
    html_list = glob.glob('./*.html')
    for file in html_list:
        filename = str(file) + '.summary'
        f = open(filename, 'w')
        f.write('\n'.join(extract_names(file)))


def main():
    # sum_list = extract_names('c:/users/mflores1/pycharmprojects/practicepython/baby2006.html')
    # print_list(sum_list)
    # write_summaries()

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
            filedata = extract_names(filename)
            text = '\n'.join(filedata) + '\n'

        if summary:
            outf = open(filename + '.summary', 'w')
            outf.write(text + '\n')
            outf.close()
        else:
            print(text)


if __name__ == '__main__':
    main()
