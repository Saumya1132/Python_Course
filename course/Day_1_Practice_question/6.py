# Compound interest

def calculate_compound_interest(principal, rate, time, n=1):

    amount = principal * (1 + rate / n) ** (n * time)
    compound_interest = amount - principal
    return compound_interest, amount

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): ")) / 100
time = float(input("Enter the time period in years: "))
n = int(input("Enter the number of times interest is compounded per year (default is 1): ") or 1)

compound_interest, amount = calculate_compound_interest(principal, rate, time, n)

print(f"The compound interest is: {compound_interest:.2f}")
print(f"The total amount after {time} years is: {amount:.2f}")
