import math

while True:
    choice = input("Trigonometric Calculations:\n1. Sine Calculation\n2. Cosine Calculation\n3. Inverse Sine Calculation\n4. Inverse Cosine Calculation\n5. Exit\nEnter your choice (1/2/3/4/5):\n")

    if choice == '5':
        print("Bye!")
        exit(0)
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please select a valid option.\n")
        continue

    if choice in ['1', '2']:
        angle = float(input("Enter an angle in degrees: "))
        result = math.sin(math.radians(angle)) if choice == '1' else math.cos(math.radians(angle))
        print(f"The {'sine' if choice == '1' else 'cosine'} of {angle} degrees is {result:.3f}\n")

    if choice in ['3', '4']:
        value = float(input("Enter the value: "))
        result = math.degrees(math.asin(value)) if choice == '3' else math.degrees(math.acos(value))
        print(f"The inverse {'sine' if choice == '3' else 'cosine'} (in degrees) of {value} is {result:.3f}\n")
