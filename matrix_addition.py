
def matrix_addition(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def main():
    print(matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]]))

if __name__ == "__main__":
    main()
