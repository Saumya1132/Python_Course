# Palindrome

def checkPalindrome(original):
    reverseNum = 0
    tempOriginal = original

    while tempOriginal > 0:
        lastDigit = tempOriginal % 10
        reverseNum = reverseNum * 10 + lastDigit
        tempOriginal = tempOriginal // 10  

    if original == reverseNum:
        return True
    else:
        return False
    
original = int(input("Enter the number to check for palindrome: "))

if checkPalindrome(original):
    print(f"{original} is a palindrome.")
else:
    print(f"{original} is not a palindrome.")
