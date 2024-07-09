import calendar

def print_calendar(year, month):
    print(f'calendar for {calendar.month_name[month]} year {year}:')
    print(calendar.month(year, month))

if __name__ == "__main__":
    year = int(input("year: "))
    month = int(input("month: "))
    print_calendar(year, month)