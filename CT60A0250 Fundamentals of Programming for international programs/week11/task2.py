def powers(x):
    (lambda x: print(f"Powers of {x}:\n"+"\n".join(f"x^{i}: {round(x**i, 4)}" for i in range(2, 6))))(float(x))

powers(input("Enter a number:\n"))