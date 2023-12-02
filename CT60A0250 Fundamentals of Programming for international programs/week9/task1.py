def add_employee(dict_list):
    dict_list.append([
        input("Enter worker's name:\n"), 
        input("Enter worker's workplace:\n"),
        input("Enter worker's age:\n"),
    ])

def print_employees(dict_list):
    print("List of Employees:")
    for worker in dict_list:
        print(f"Name: {worker[0]}, Workplace: {worker[1]}, Age: {worker[2]}")

employees = []

employees_count = int(input("How many employees do you want to add?:\n"))

for _ in range(employees_count):
    add_employee(employees)

print_employees(employees)