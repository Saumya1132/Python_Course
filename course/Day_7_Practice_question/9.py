# count the number of occurrences of each character in the string using the dictionary


def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

my_string = "Hello, World!"
char_counts = count_characters(my_string)
print(char_counts)
