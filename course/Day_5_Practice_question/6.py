# check pangram 

import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    letters_in_string = set(s.lower())
    return alphabet <= letters_in_string

test_string = input("Enter string: ")
if is_pangram(test_string):
    print(f'"{test_string}" is a pangram.')
else:
    print(f'"{test_string}" is not a pangram.')
