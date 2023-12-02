a = int(input("Enter a:\n"))
b = int(input("Enter b:\n"))

while a < 1000 and b < 1000:
    print(f"a: {a} b: {b}")
    a *= 2
    b += 100

if a > 1000:
    print(f"a exceeded 1000")

if b > 1000:
    print(f"b exceeded 1000")
