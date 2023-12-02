from datetime import datetime

date = input("Enter a date in YYYY-MM-DD format:\n")
try:
    datetime.strptime(date, "%Y-%m-%d")
    print(f"{date} is a valid date.")
except ValueError:
    print(f"{date} is not a valid date.")
