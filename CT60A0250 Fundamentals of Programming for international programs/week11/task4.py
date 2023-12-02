import numpy


def create_matrix(prompt):
    rows, cols = map(int, [input(f"Enter the number of rows for the {prompt.split('|')[0]} matrix:\n"),
                           input(f"Enter the number of columns for the {prompt.split('|')[0]} matrix:\n")])
    matrix = numpy.zeros((rows, cols))
    print(f"Enter values for a {rows}x{cols} matrix:")
    for i in range(rows):
        matrix[i] = list(map(float, input(f"Enter {cols} values for row {i + 1} (separated by space):\n").split()))
    print(f"This is matrix {prompt.split('|')[1]}:\n" + str(matrix))
    return matrix


matrix1 = create_matrix("first|1")
matrix2 = create_matrix("second|2")

if matrix1.shape == matrix2.shape:
    print("Matrix sum:\n" + str(matrix1 + matrix2))
else:
    print("Error: sum not possible")

if matrix1.shape[1] == matrix2.shape[0]:
    try:
        print("Matrix multiplication:\n" + str(numpy.matmul(matrix1, matrix2)))
    except ValueError:
        print("Error: multiplication not possible")
else:
    print("Error: multiplication not possible")
