
def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]


def main():
    print(transpose_matrix([[1, 2], [3, 4]]))

if __name__ == "__main__":
    main()
