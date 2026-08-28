
def matrix_scalar_multiply(matrix, scalar):
    return [[element * scalar for element in row] for row in matrix]


def main():
    print(matrix_scalar_multiply([[1, 2], [3, 4]], 3))

if __name__ == "__main__":
    main()
