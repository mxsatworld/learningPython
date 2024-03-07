# subprocess runs an external command and captures its output
# provides url fetching, making a url a file you can read from
from shutil import copyfileobj
from urllib.request import urlopen
import urllib.request
# urlparse can take apart and put together urls
import subprocess
import os
import sys
import shutil
fileNames = os.listdir('/')
print(fileNames)  # return a list with the filenames inside /
print(os.path.join('/', fileNames[0]))  # returns / + first filename
# given a path returns the absolute path /home/msxfm/Desktop/learningPython/GooglePythonCourse/test
print(os.path.abspath('test'))
print(os.path.dirname(
    '/home/msxfm/Desktop/learningPython/GooglePythonCourse/rawString.py'))  # returns the dirname
print(os.path.basename(
    '/home/msxfm/Desktop/learningPython/GooglePythonCourse/rawString.py'))  # returns the filename
print(os.path.exists('/'))  # True if exists, False if not
# os.mkdir('/home/msxfm/Desktop/Test')  # Make Test directory in Desktop
# Make TestTwo directory and Test2 in case of
# os.makedirs('/home/msxfm/Desktop/Test2/TestTwo')
# being necessary, with mkdir you cant make TestTwo if Test2 is not already existing
shutil.copy('/home/msxfm/Desktop/learningPython/GooglePythonCourse/rawString.py',
            '/home/msxfm/Desktop/')
# copys rawString.py to the Desktop


def listdir(dir):
    cmd = 'ls -l ' + dir
    print("Command to run:", cmd)
    (status, output) = subprocess.getstatusoutput(
        cmd)  # runs the command ls -l dir externally
    #
    # print(output)
    if status:
        # in sys.stderr its written the exceptions, in case of error
        sys.stderr.write(output)
        # sys.stderr.write its gonna print the error in console
        sys.exit(status)  # exits the sys functionality
    print(output)  # prints output


listdir('/home')

# this is similar to try catch in js
try:
    # this lines could throw an error
    f = open('Xd.py', 'r')
    data = f.read()
    f.close()
except IOError:
    sys.stderr.write('error reading: Xd.py')

# returns file like object for that url
ufile = urllib.request.urlopen('https://www.google.com')
text = ufile.read()  # prints all the html text
info = ufile.info()  # HTTPS metainfo (this usually goes in the header of the packet)
mimeType = info.get_content_type()  # type of content, text/html in this case
baseUrl = ufile.geturl()  # returns the url https://www.google.com

# THIS IS DEPRECATED FROM PYTHON2
# filename, headers =urllib.request.urlretrieve('https://www.google.com')  # downloads the url data
# to the given file path

# PYTHON3 VERSION
# this generates a file called my_filename and puts all the html code from www.google.com
with urlopen('https://www.google.com') as in_stream, open('my_filename', 'wb') as out_file:
    copyfileobj(in_stream, out_file)
print(baseUrl)

# join urls
urlJoin = urllib.parse.urljoin('https://www.infobae.com/', 'economia')
print(urlJoin)
