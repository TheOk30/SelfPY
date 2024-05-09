import calendar

def main():
    date = input("Enter a date (dd/mm/yyyy): ") # 01/01/2000

    # Split date string into day, month, and year
    day, month, year = map(int, date.split('/'))

    # Get the day of the week using the weekday() method
    week_day = calendar.weekday(year, month, day)

    print(calendar.day_name[week_day])
    #Saturday
if __name__ == "__main__":
    main()