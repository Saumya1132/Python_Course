def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year , "Leap year")
    else:
        print(year , "Leap not a year")

year = int(input("Enter year: "))
is_leap_year(year)