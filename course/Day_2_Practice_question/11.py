# hours and minutes

def convert_minutes(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return hours, remaining_minutes

def main():
    total_minutes = int(input("Enter the number of minutes: "))
    hours, minutes = convert_minutes(total_minutes)
    print(f"{total_minutes} minutes is equal to {hours} hours and {minutes} minutes.")

main()
