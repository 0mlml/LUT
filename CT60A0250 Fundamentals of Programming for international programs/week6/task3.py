integers = list(map(int, input("Give integers separated by comma:\n").split(",")))
reversed_integers = [integers[i] for i in range(len(integers)-1, -1, -1)]
print(f"Reversed list: {reversed_integers}")