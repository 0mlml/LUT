from datetime import datetime

(lambda o: print(f"Month: {o.strftime('%B')}\nWeekday: {o.strftime('%A')}\nWeek nr: {o.strftime('%U')}\nDay nr: {o.strftime('%j')}"))(datetime.strptime(input("Give a datetime string in format \"%Y/%m/%d %H:%M:%S\":\n"), "%Y/%m/%d %H:%M:%S"))
