from datetime import datetime

(lambda a, b: print(f"The number of days between {a.strftime('%d.%m.%Y')} and {b.strftime('%d.%m.%Y')} is {abs((b - a).days)} days."))(datetime.strptime(input("Enter the first date (DD.MM.YYYY):\n"), "%d.%m.%Y"), datetime.strptime(input("Enter the second date (DD.MM.YYYY):\n"), "%d.%m.%Y"))