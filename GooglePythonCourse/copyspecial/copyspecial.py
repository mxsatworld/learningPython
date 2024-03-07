#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
# this was copied from https://developers.google.com/edu/python/exercises/copy-special
# because i didnt understand the task

# get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given
# directory xyz__hello__.txt and zz__something__.jpg

# copy_to(paths, dir) given a list of paths, copies those files into the given directory
# copy the xyz__hello__.txt and zz__something__.jpg to the specified dir

# zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile
#i cheated on this one because i have trouble understanding zip
#you need to run zip as an external command
def zip_to(paths, zippath):
    for path in paths:
        #zip -j zippath path The mistake was not running zip as an external command
        #i will solve it tomorrow because im tired
        #check that i have installed zip
        #zip -j /home/msxfm/Desktop/test.zip /home/msxfm/Desktop/learningPython/GooglePythonCourse/copyspecial/xyz__hello__.txt /home/msxfm/Desktop/learningPython/GooglePythonCourse/copyspecial/zz__something__.jpg
        #thats the external command that i have to run, zip is installed

def get_special_paths():
    #return [os.path.abspath("xyz__hello__.txt"), os.path.abspath("zz__something__.jpg")]
    #thinking about it better this maybe is a hardcoded answer


def copy_to(paths, dir):  # given a list of paths, copies those files into the given directory
    #print(paths)
    for path in paths:
        shutil.copy(path, dir)


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        # print(get_special_paths())
        print('usage: [--todir dir][--tozip zipfile] dir [dir ...]')
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        # print(args[1])
        todir = args[1]
        specialPaths = get_special_paths()
        copy_to(specialPaths, todir)
        # del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        specialPaths = get_special_paths()
        zip_to(specialPaths, tozip)
    #del args[0:2]

    # if not args:  # A zero length array evaluates to "False".
    # print('error: must specify one or more dirs')
    # sys.exit(1)

    # +++your code here+++
    # Call your functions


if __name__ == '__main__':
    main()
