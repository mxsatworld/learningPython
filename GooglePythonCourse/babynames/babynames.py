#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

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
    # +++your code here+++
    # the first mistake i made is analyze the file line by linea instead of analyze
    # the whole file like the solution recommends, USING THE read() method
    # with open(filename, 'rt', encoding='utf-8') as f:
    # text = f.read()
    # the following in solutions its kinda the same that i did so i only have to remark
    # the read method
    fileRead = open(filename, 'r', encoding='utf-8')
    returnList = []
    for line in fileRead:
        year = re.findall("Popularity in \d{4}", line)
        td = re.findall("<td.*?>(.+?)</td>", line)
        # . = any character except new line \n
        # * = zero or more ocurrences
        # ? = zero or one ocurrences
        # () = capture and group
        # + = one or more ocurrences
        # .*? = any character with zero, one or more ocurrences
        # (.+?) = group with any character with zero, one or more ocurrences
        if len(td) == 3:
            nameAndYearMale = td[1] + " " + td[0]
            nameAndYearFemale = td[2] + " " + td[0]
            returnList.append(nameAndYearMale)
            returnList.append(nameAndYearFemale)
        if len(year) != 0:
            # print(year[0])
            year = re.sub(r'[^\d]', '', year[0])
            returnList.append(year)
    returnList = sorted(returnList)
    fileRead.close()
    return returnList


def main():
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
        list = extract_names(args[0])

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    # print(args)
    fileWrite = open('summary.txt', 'w', encoding='utf-8')
    for element in list:
        fileWrite.write(element + "\n")
    fileWrite.close()


if __name__ == '__main__':
    main()
