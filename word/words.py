# scrabble prelim exercise

import scrabble
import string

# print all words containing uu

# for word in scrabble.wordlist:
#    if "uu" in word:
#        print(word)


# print all letters that never appear doubled.  Should reveal Q and X

for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            print(word)
            exists = True
        if not exists:
            print('There are no English words with double' + letter)

# print words that have all vowels

vowels = "aeiou"


def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
        return True


for word in scrabble.wordlist:
    currentword = word()
    if has_all_vowels(word):
        print(word)
    print('Last word was: ', currentword)


# Just remember the new way to print a value in Python3
