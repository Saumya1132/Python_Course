# remove vowels from string

def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    return ''.join([char for char in input_string if char not in vowels])

input_string = input("Enter string: ")
print(remove_vowels(input_string))  
