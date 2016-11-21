#!/usr/bin/python3
# environment checks

import sys
import urllib.request
import datetime

def main():
    time = datetime.datetime.now()
    print(time)
    print('System environment: ', sys.platform)
    print('Python version {}.{}.{}'.format(*sys.version_info))
    page = urllib.request.urlopen('http://python.org/')
    print(page)
#    for line in page:
#        print(str(line, encoding='utf_8'), end = '')



if __name__ == "__main__": main()
