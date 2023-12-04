gcd = lambda a, b: a if b == 0 else gcd(b, a % b)

print((lambda a, b: f"gcd({a},{b}) = {gcd(int(a), int(b))}")(*input("Give two positive integers separated by comma:\n").split(", ")))