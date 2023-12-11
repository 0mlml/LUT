import datetime

print("This program prints the calendar of a desired month.")

dc, sp = (lambda y, m: tuple([(datetime.date(y + m // 12, m % 12 + 1, 1) - datetime.date(y, m, 1)).days, datetime.date(y, m, 1).weekday()]))(int(input("Give me the year:\n")), int(input("Give the month:\n")))

print("_____________________\n Mo Tu We Th Fr Sa Su")

print("   " * sp, end="")
for day in range(1, dc + 1):
    print(f"{day:3}", end="")
    sp = (sp + 1) % 7
    if sp == 0:
        print()
print()