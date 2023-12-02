n = int(input("Enter a non-negative integer:\n"))

if n < 0:
    print("Error: Factorial is not defined for negative numbers")
    exit(0)

f = 1
for i in range(1, n + 1):
    f *= i 

print(f"Factorial of {n} is {f}")

