# scrabble prelim exercise

import scrabble
import string

#print all words containing uu

for word in scrabble.wordlist:
    if "uu" in word:
        print(word)


#print all letters that never appear doubled.  Should reveal Q and X

for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            print(word)
            exists = True
        if not exists:
            print('There are no English words with double' + letter)
