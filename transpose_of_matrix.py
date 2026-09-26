
def transpose_of_matrix(matrix):
    if not matrix:
        return []
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def main():
    matrices = [
        [[1, 2, 3], [4, 5, 6]],
        [[1, 2], [3, 4], [5, 6]],
        [[1]]
    ]
    for matrix in matrices:
        print(f"Original: {matrix}")
        print(f"Transpose: {transpose_of_matrix(matrix)}")


if __name__ == "__main__":
    main()
