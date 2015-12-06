#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib.request


"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # Find server name
    match_server_name = re.search(r'_(\S+)', filename)
    server_name = match_server_name.group(1)
    # Open and read data from file
    f = open(filename, 'rU')
    # Copy data into a string
    text = f.read()
    # Create a list of urls.  Use findall.
    urls = re.findall(r'GET\s\S+\sHTTP', text)
    # Find image urls with puzzle pattern
    image_urls = []
    # Need to add try/except code
    for url in urls:
        # Search for puzzle pattern in url
        match_url = re.search(r'\S+/puzzle/\S+', url)
        if match_url:
            image_url = match_url.group(0)
            # Add complete path
            complete_path = 'http://' + server_name + image_url
            # Add image urls with puzzle pattern to list
            if complete_path not in image_urls:
                image_urls.append(complete_path)
    # Creates a temp dictionary for sorting
    sort_image_dict = {}
    for img_url in image_urls:
        match_img_url = re.search(r'-\w+-(\w+)\.jpg', img_url)
        if match_img_url:
            sort_image_dict[img_url] = match_img_url.group(1)
        else:
            sort_image_dict[img_url] = img_url
    # Copy sorted urls back to list
    del image_urls[:]
    for v in sorted(sort_image_dict.values()):
        image_urls.append(v)
    print(image_urls)


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # Creates directory if it does not exit
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    # Copy special files into PC directory
    img_count = 0
    img_path_dict = {}
    # Need to add try/except
    for img_url in img_urls:
        img_name = 'img' + str(img_count)
        full_path = dest_dir + '/' + img_name
        urllib.request.urlretrieve(img_url, full_path)
        # Store full path in a dictionary to keep order.  Need for creating image tag
        img_path_dict[img_count] = full_path
        img_count += 1
    # Create an html file with image tag.
    # Create image tag
    img_tag = ''
    for key in sorted(img_path_dict.keys()):
        img_tag = img_tag + '<img src=\"' + img_path_dict[key] + '\">'
    text = '<verbatim>\n' + '<html>\n' + '<body>\n' + img_tag + '\n' \
           + '</body>\n' + '</html>'
    # Create html file
    html_file = dest_dir + '/' + 'index.html'
    outf = open(html_file, 'w')
    outf.write(text)
    outf.close()


def main():
    image_urls = read_urls('c:/users/mflores1/pycharmprojects/practicepython/python_google/animal_code.google.com')
    # download_images(image_urls, 'c:/users/mflores1/pycharmprojects/practicepython/python_google/images')
    # args = sys.argv[1:]
    #
    # if not args:
    #     print('usage: [--todir dir] logfile ')
    #     sys.exit(1)
    #
    # todir = ''
    # if args[0] == '--todir':
    #     todir = args[1]
    #     del args[0:2]
    #
    # img_urls = read_urls(args[0])
    #
    # if todir:
    #     download_images(img_urls, todir)
    # else:
    #     print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
