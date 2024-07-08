# Convert the day of the week and year

def convert_days(days):
    days_in_year = 365
    days_in_week = 7

    years = days // days_in_year
    remaining_days = days % days_in_year

    weeks = remaining_days // days_in_week

    days = remaining_days % days_in_week

    return years, weeks, days

days = 800
years, weeks, days = convert_days(days)
print(f"{days} days is equivalent to {years} years, {weeks} weeks, and {days} days.")
