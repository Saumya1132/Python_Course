# function takes list of string and return set of unique characters present in all strings

def find_unique_characters(strings):
    unique_chars = set()
    for string in strings:
        unique_chars.update(set(string))
    return unique_chars

strings = ["hello", "world", "python"]
unique_chars = find_unique_characters(strings)
print(unique_chars)
