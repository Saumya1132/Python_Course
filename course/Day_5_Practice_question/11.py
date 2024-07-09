# Remove duplicates characters from the string

def remove_duplicates(input_string):
    unique_chars = []
    seen = set()
    for char in input_string:
        if char not in seen:
            seen.add(char)
            unique_chars.append(char)
    unique_string = ''.join(unique_chars)
    
    print("Unique characters:", ' '.join(unique_chars))
    
    return unique_string

input_string = input("Enter a string: ")
print("String with duplicates removed:", remove_duplicates(input_string))





