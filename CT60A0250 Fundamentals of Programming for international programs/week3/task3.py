left = int(input("Enter the first number:\n"))
right = int(input("Enter the second number:\n"))

print(
    "The calculator can perform the following operations:",
    "1) Add",
    "2) Subtract",
    "3) Multiply ",
    "4) Divide",
    sep="\n"
)

opn = input(f"The numbers you entered are {left} and {right}\nSelect the operation (1-4):\n")

match opn:
    case "1":
        print(f"Selection 1: {left} + {right} = {left + right}")
    case "2":
        print(f"Selection 2: {left} - {right} = {left - right}")
    case "3":
        print(f"Selection 3: {left} * {right} = {left * right}")
    case "4":
        if right == 0:
            print("Error: Zero cannot be used as a divisor.")
        else:
            print(f"Selection 4: {left} / {right} = {(left / right):.2f}")
    case _:
        print("The operation was not recognized.")