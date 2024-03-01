#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

# imports system module
import sys

# Define a main() function that prints a little greeting.


def main():
    # Get the name from the command line, using 'World' as a fallback.
    if len(sys.argv) >= 2:  # len returns the length of a list, sys.argv always would have
      # sys.argv[0] because sys.argv[0] has the name of the script, so the length always would be
        # 1 or more
        # if the length is 2 or more it means that an argument was passed in the terminal
        # command line arguments are in sys.argv[1] sys.argv[2] and so on
        name = sys.argv[1]
        # sys.argv[0] has the name of the script and can be ignored
    else:
        name = 'World'
    print('Hello', name)


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
