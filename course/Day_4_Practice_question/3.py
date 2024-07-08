# reverse the string

def rev():
    user = input("Enter a string: ")
    reversed_string = user[::-1]
    return reversed_string

print(rev())