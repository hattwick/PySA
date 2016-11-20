# Python3 module for buffered read
# Based on exercise files from Python3 Essential Training
# Goal is to evolve this to a reusable module

def main():
    buffersize = 50000
    file_in = open('file.txt', 'r')
    file_out = open('newfile.txt', 'w')
    buffer = file_in.read(buffersize)
    while len(buffer):
        file_out.write(buffer)
        print('.', end = '')
        buffer = file_in.read(buffersize)