# Python3 module for buffered read
# Based on exercise files from Python3 Essential Training
# Goal is to evolve this to a reusable module

def unbuffered():
    file_in = open('file.txt', 'r')
    file_out = open('newfile.txt', 'w')
    for line in file_in:
        print(line, file = file_out, end ='')
    print('Unbuffered read has been save in newfile.txt.')

def buffered():
    buffersize = 50000
    file_in = open('file.txt', 'r')
    file_out = open('newfile.txt', 'w')
    buffer = file_in.read(buffersize)
    while len(buffer):
        file_out.write(buffer)
        print('.', end = '')
        buffer = file_in.read(buffersize)

if __name__ == "__main__":  buffered()