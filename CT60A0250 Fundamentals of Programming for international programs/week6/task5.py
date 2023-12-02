def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            row = input(f"Give row {i + 1}:\n").split()
            if len(row) == cols:
                break
            print("Error: Invalid number of elements in the row. Please try again.")
        matrix.append([int(elem) for elem in row])
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("|", end="")
        print("\t".join(map(str, row)), end="")
        print("|")

rows = int(input("Enter the number of rows:\n"))
cols = int(input("Enter the number of columns:\n"))

matrix = create_matrix(rows, cols)
print("The original matrix:")
print_matrix(matrix)
print("Its transpose:")
print_matrix(transpose(matrix))
