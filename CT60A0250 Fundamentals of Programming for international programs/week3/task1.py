y = int(input("Enter a year:\n"))

if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0:
            print(f"{y} is a leap year.")
        else:
            print(f"{y} is not a leap year.")
    else:
        print(f"{y} is a leap year.")