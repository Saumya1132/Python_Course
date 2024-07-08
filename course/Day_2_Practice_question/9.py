# check pangram 

import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    letters_in_string = set(s.lower())
    return alphabet <= letters_in_string

# Test the function
test_string = "The quick brown fox jumps over the lazy dog"
if is_pangram(test_string):
    print(f'"{test_string}" is a pangram.')
else:
    print(f'"{test_string}" is not a pangram.')
