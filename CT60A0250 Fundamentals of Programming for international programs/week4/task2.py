n = int(input("Enter a positive integer:\n"))

if n <= 0:
    print(f"{n} is not positive")

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end="...")