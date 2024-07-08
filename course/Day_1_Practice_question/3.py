# Even odd numbers

def even_odd(number):
    if number % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
    
number = int(input("Enter number to check even or odd number :"))
even_odd(number)    
