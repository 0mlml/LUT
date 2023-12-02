matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

try:
    row_index = int(input("Enter the row index:\n"))
    col_index = int(input("Enter the column index:\n"))

    value = matrix[row_index][col_index]
    print(f"Value at position ({row_index}, {col_index}): {value}")
except IndexError:
    print("Error: Index out of bounds. Please enter valid row and column indices.")
except ValueError:
    print("Error: Please enter valid integers for row and column indices.")
