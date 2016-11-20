#!/usr/bin/python3
# test exercise file from Python 3 Essential Training on lynda.com
# modifications during exercise to operate on a character data (bytes)
# parse string with unprintable characters and append characters as xml unicode entitie for proper formatting
# goal is to evolve this to a reusable module

def main():
    print('This is the containers.py file.\n')
    file_in = open('utf8.txt', 'r', encoding= 'utf_8')
    file_out = open('utf8.html', 'w')
    outbytes = bytearray()
    print(file_in)
    for line in file_in:
        for c in line:
            if ord(c) > 127:
                outbytes += bytes('&#{:04d};'.format(ord(c)), encoding='utf_8')
            else: outbytes.append(ord(c))
    outstr = str(outbytes, encoding= 'utf_8')

    print(outstr, file = file_out)
    print(outstr)
    print('conversion complete')



if __name__ == "__main__": main()
