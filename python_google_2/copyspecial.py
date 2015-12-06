#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
# import commands

"""Copy Special exercise
"""


def find_special_files(dir):
    # Store special files in a list
    special_files = []
    # Creates a list of files in directory
    filenames = os.listdir(dir)
    for filename in filenames:
        # Find special files in directory
        match_file = re.search(r'\w+__\w+__\.\w+', filename)
        if match_file:
            # Find path for each special file
            path = os.path.join(dir, filename)
            # Find absolute path for each special file
            abs_path = os.path.abspath(path)
            # Add absolute path to list
            special_files.append(abs_path)
    return special_files


def copy_special_files(files, todir):
    # Check directory has special files to copy
    if len(files) != 0:
        # Creates directory if it does not exit
        if not os.path.exists(todir):
            os.mkdir(todir)
        # Copy special files into directory
        for file in files:
            shutil.copy(file, todir)
    else:
        print('no special files to copy')


def main():
    # list = find_special_files('c:/users/mflores1/pycharmprojects/practicepython')
    # copy_special_files(list, 'c:/users/mflores1/pycharmprojects/practicepython/test')

    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)

    # +++your code here+++
    dir = args[0]
    if todir:
        # Need to enter complete path for new directory
        files = find_special_files(dir)
        copy_special_files(files, todir)
    elif tozip:
        print('tozip')
    else:
        files = find_special_files(dir)
        text = '\n'.join(files)
        print(text)


if __name__ == "__main__":
    main()
