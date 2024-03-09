# I did not understand the copyspecial exercise so i did my own implementation (and this google
# course is in python v2 and im currently using v3 so that might be the problem in the first place)


# INPUT: ./copyspecial2.py xyz__hello__.txt zz__something__.jpg
# OUTPUT: /Users/nparlante/pycourse/day2/xyz__hello__.txt
# /Users/nparlante/pycourse/day2/zz__something__.jpg

# INPUT: ./copyspecial2.py --todir /home/msxfm/Desktop xyz__hello__.txt zz__something__.jpg
# ls /home/msxfm/Desktop
# OUTPUT: xyz__hello__.txt zz__something__.jpg

# INPUT: ./copyspecial2.py --tozip tmp.zip xyz__hello__.txt zz__something__.jpg
# zip -j tmp.zip /Users/nparlante/pycourse/day2/xyz__hello__.txt
# /Users/nparlante/pycourse/day2/zz__something__.jpg

import os
import shutil
import sys


def main():
    # print(os.listdir())  # ls equivalent in python
    # returns the absolute path of the jpg file
    # args = sys.argv
    # check if is a valid path
    if sys.argv[1] == "--todir":
        # print(sys.argv[2])
        if len(sys.argv) >= 4:
            path = os.path.abspath(sys.argv[2])
            filenames = sys.argv[3:]
            for filename in filenames:
                shutil.copy(os.path.abspath(filename), path)
        else:
            print("Error: path or file not specified")
    elif sys.argv[1] == "--tozip":
        if len(sys.argv) >= 4:
            zipName = os.path.abspath(sys.argv[2])
            zipString = "zip -j " + zipName + " "
            files = sys.argv[3:]

            # zip -j tmp.zip
            # /Users/nparlante/pycourse/day2/xyz__hello__.txt /Users/nparlante/pycourse/day2/zz__something__.jpg

            filenames = sys.argv[3:]
            for filename in filenames:
                shutil.copy(filename, path)
        else:
            print("Error: name or file not specified")
    else:
        for path in sys.argv[1:]:
            if os.path.exists(path):
                print(os.path.abspath(path))
            else:
                print("File not found")
    # print(os.path.abspath('xyz__hello__.txt'))


if __name__ == "__main__":
    main()
