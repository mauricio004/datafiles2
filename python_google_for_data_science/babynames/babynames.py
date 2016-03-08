#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import glob

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
    names_lst = []

    # Open file
    f = open(filename, 'r')

    # Copy file content to text
    text = f.read()

    # Use re to extract data
    year_match = re.search(r'>Popularity in (\d\d\d\d)</h3>', text)
    names_match = re.findall(r'<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', text)

    # Copy to list
    if year_match:
        names_lst.append(year_match.group(1))

    # Create dictionary with names.  First name as key and rank as value. If name
    # already in dictionary skip it.
    names_rank_dict = {}
    for n in names_match:
        # Unpack tuples
        k, boy, girl = n
        if boy not in names_rank_dict:
            names_rank_dict[boy] = k
        if girl not in names_rank_dict:
            names_rank_dict[girl] = k

    # Sort dictionary by key (name)
    sorted_names = sorted(names_rank_dict.keys())

    # Append names to list
    for n_sorted in sorted_names:
        names_lst.append(n_sorted + ' ' + names_rank_dict[n_sorted])

    return names_lst

def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

    # For each filename, get the names, then either print the text output
    # or write it to a summary file

    for arg in args:
        for filename in glob.glob(arg):
            file_data = extract_names(filename)
            text = '\n'.join(file_data)

            if summary:
                f_out = open(filename + '.summary.txt', 'w')
                f_out.write(text)
                f_out.close()
            else:
                print(text)

if __name__ == '__main__':
    main()
