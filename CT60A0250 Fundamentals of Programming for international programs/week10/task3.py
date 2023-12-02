def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("You must enter valid numbers")
            break
        except ZeroDivisionError:
            print("You cannot divide by zero")
            break


num1 = get_float("Enter the first number:\n")
num2 = get_float("Enter the second number:\n")

if num1 is not None and num2 is not None:
    try:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result:.8f}")
    except ZeroDivisionError:
        print("You cannot divide by zero")
