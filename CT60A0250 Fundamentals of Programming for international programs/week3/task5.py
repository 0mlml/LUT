g = float(input("Enter your number of points:\n"))

print(f"Your grade is:", (g - 50) // 10 + 1 if g >= 50 else 0)