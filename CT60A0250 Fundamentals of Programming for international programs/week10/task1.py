def input_integer():
    while True:
        try:
            return int(input("Enter an integer:\n"))
        except ValueError:
            print("Invalid input. Please enter an integer.")

print(f"The sum of the entered integers is: {sum(input_integer() for _ in range(input_integer()))}")