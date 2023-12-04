integer_sum = lambda n: 0 if n < 1 else n + integer_sum(n-2)

print("n + (n-2) + (n-4) + ... = " + str(integer_sum(int(input("Give a non-negative integer n:\n")))))