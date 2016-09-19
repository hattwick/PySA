# Short palindrome finder

import string
import scrabble

print(string.ascii_lowercase)

# test long palindrome
word = "rotavator"
print('\nIs rotavator a palindrom?\n')
print(word == word[::-1])

# Now the full check

longest = ""

for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest):
        longest = word
print('After checking the scrabble file, the longest word is', longest)