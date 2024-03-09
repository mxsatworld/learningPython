#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def url_sort_key(url):
    # print(url)
    match = re.search(r'-(\w+)-(\w+)\.\w+', url)
    # print(match)
    # \w a to Z 0 to 9 and unserscore match
    if match:
        # print("bumbum")
        return match.group(2)
    else:
        # print("bambam")
        return url


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    # filePath = os.path.abspath(filename)
    # with open(filePath, 'rt', encoding='utf-8') as f:
    # text = f.read()
    # all images formats
    # images = re.findall(r'(.+?)images(.+?)', text)
    # images = re.findall(r'^.*substring.*$', text)
    # images = images.group(1)
    # i couldnt solve this so i will copy the solution and use this in the future as a guide
    # for solving other problems
    # matching = [s for s in text if "images" in s]
    # print(matching)
    # in the title animal_code.google.com _ is in the 6 position
    underbar = filename.index('_')
    # NEW THING LEARNED: the index method in a string can return you the index of a searched substring
    # extract all after the underbar so you can get the host
    host = filename[underbar + 1:]
    # code.google.com
    url_dict = {}
    with open(filename) as f:
        # this is a good technique, put a for inside the open filename to analyze it line by line
        for line in f:
            match = re.search(r'"GET (\S+)', line)
            # match a line starting with "GET followed by \S+
            # \S = any non space character
            # + One or more ocurrences
            # match all GET request with his paths
            if match:
                path = match.group(1)  # with this
                # .group you indicate tha you want to capture the group 1 \S+
                # the group 0 would be "GET
                # print(match)
                # with this you only match the path
                if 'puzzle' in path:
                    url_dict['http://' + host + path] = 1
        print(url_dict)
        return sorted(url_dict.keys(), key=url_sort_key)
    # sorts keys using the url_sort_key function


def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    # print(img_urls, dest_dir)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    index = open(os.path.join(dest_dir, 'index.html'), 'w')
    index.write('<html><body>\n')

    i = 0
    for img_url in img_urls:
        local_name = 'img%d' % i
        print('Retrieving...', img_url)
        urllib.request.urlretrieve(img_url, os.path.join(dest_dir, local_name))
        index.write('<img src="%s">' % (local_name,))
        i += 1
    index.write('\n</body></html>\n')
    index.close()


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile ')
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:1]
    # print(args)
    # print(todir)
    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))


if __name__ == '__main__':
    main()
