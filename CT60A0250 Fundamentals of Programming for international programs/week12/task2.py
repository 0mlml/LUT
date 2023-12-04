power = lambda x, n: x*power(x, n-1) if n >= 0 else 1

print((lambda x, n: f"{x} power to {n} is {power(x, n-1)}")(float(input("Give a float x:\n")), int(input("Give a non-negative integer n:\n"))))