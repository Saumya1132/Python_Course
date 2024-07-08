# Cleck palindrome

def check_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
word = input("Enter word :")
if check_palindrome(word):
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")