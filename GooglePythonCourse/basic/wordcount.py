#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import itertools
import sys
import re
# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.


def print_words(filename):
    fileRead = open(filename, 'r', encoding='utf-8')
    counter = {}
    for line in fileRead:
        # module re its for support regexp
        line = re.sub(r'[^a-z\s]', '', line.lower())
        # 1arg its the regular express
        # 2arg replacement of the matching items
        # 3arg the string that its gona be changed
        # sub is for substitution
        line = line.split()  # strip delete whitespaces at the beggining and the end
        # but its more eficcient using split, so the line of text is converted in alist
        for word in line:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    fileRead.close()  # not necesary but is a good practice
    sorted_counter = dict(sorted(counter.items()))
    for key, value in sorted_counter.items():
        print(key, value)


def print_top(filename):
    fileRead = open(filename, 'r', encoding='utf-8')
    counter = {}
    for line in fileRead:
        line = re.sub(r'[^a-z\s]', '', line.lower())
        line = line.split()  # if i knew about this method i could resolve this in a more easy way
        # WHY I KNOW THIS KNOW!!!
        for word in line:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    fileRead.close()  # not necesary but is a good practice
    sorted_counter = dict(
        sorted(counter.items(), key=lambda x: x[1], reverse=True))
    sorted_counter = dict(itertools.islice(
        sorted_counter.items(), 20))  # truncate the dict in 20
    # values
    for key, value in sorted_counter.items():
        print(key, value)


def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
