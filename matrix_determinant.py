
def matrix_determinant(matrix):
    n = len(matrix)
    
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for col in range(n):
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * matrix_determinant(minor)
    
    return det


def main():
    matrices = [
        [[5]],
        [[1, 2], [3, 4]],
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    ]
    for matrix in matrices:
        print(f"Matrix: {matrix}")
        print(f"Determinant: {matrix_determinant(matrix)}")


if __name__ == "__main__":
    main()
