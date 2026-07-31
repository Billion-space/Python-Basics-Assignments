def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = input(f"Enter row {i + 1}: ").split()
        row = [float(x) for x in row]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    widths = [max(len(f"{row[j]:g}") for row in matrix) for j in range(len(matrix[0]))]
    for row in matrix:
        print("  ".join(f"{val:g}".rjust(widths[j]) for j, val in enumerate(row)))
    print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def add_matrices(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(a[i][j] + b[i][j])
        result.append(new_row)
    return result


def multiply_matrices(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += a[i][k] * b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


if __name__ == "__main__":
    # PART A — Transpose
    print("PART A — Transpose a Matrix")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    print("Transposed Matrix:")
    print_matrix(transpose_matrix(matrix))

    # PART B — Add two matrices
    print("PART B — Add Two Matrices")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print("Matrix A:")
    matrix_a = read_matrix(rows, cols)
    print("Matrix B:")
    matrix_b = read_matrix(rows, cols)
    print("\nSum:")
    print_matrix(add_matrices(matrix_a, matrix_b))

    # PART C — Multiply two matrices
    print("PART C — Multiply Two Matrices")
    rows_a = int(input("Enter rows for Matrix A: "))
    cols_a = int(input("Enter columns for Matrix A: "))
    print("Matrix A:")
    matrix_a = read_matrix(rows_a, cols_a)

    rows_b = cols_a
    cols_b = int(input("Enter columns for Matrix B: "))
    print(f"Matrix B ({rows_b} rows required):")
    matrix_b = read_matrix(rows_b, cols_b)

    print("\nProduct:")
    print_matrix(multiply_matrices(matrix_a, matrix_b))
