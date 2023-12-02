(lambda y: print(f"{y} is {'a leap' if not y & 3 and (y % 25 or not y & 15) else 'not a leap'} year."))(int(input("Enter a year:\n")))
