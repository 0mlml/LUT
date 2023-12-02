numbers = []
while True:
    user_input = input("Enter an integer (or 'done' to finish): ")
    if user_input == 'done':
        break
    try:
        numbers.append(int(user_input))
    except ValueError:
        print("Invalid input.")

target_sum = int(input("Enter the target sum: "))
pairs = [(numbers[i], numbers[j]) for i in range(len(numbers)) for j in range(i, len(numbers)) if numbers[i] + numbers[j] == target_sum]

print(f"Pairs with a sum of {target_sum}:")
for pair in pairs:
    print(pair, tuple(reversed(pair)), sep="\n")