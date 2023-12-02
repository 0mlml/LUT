integers = list(map(int, input("Give integers separated by comma:\n").split(",")))
resultant = list(dict.fromkeys(integers))
print(f"Original List: {integers}\nList with duplicates removed: {resultant}")